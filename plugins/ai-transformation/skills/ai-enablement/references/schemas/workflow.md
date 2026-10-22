# Schema: enablement/workflows/<id>.md (workflow/v1)

One markdown file per reusable workflow in the library: YAML frontmatter for the fields below, then a body in the
shape of `../templates/workflow.md`. Step 5 writes and curates these files; ai-solution-delivery may add one when a
launched solution changes how a role works. Shared ids (`work_types`, `patterns`, `ladder`, `runtime_classes`) come
from `../../../transformation-advisor/references/schemas/vocabulary.yaml`; the other enums are local.

## 1. Frontmatter

```yaml
schema: workflow/v1
id: string                         # the file name without .md, e.g. notice-response-draft
title: string
roles: [ string ]                  # role groups that use it
practice: string
task: string                       # the task in the role's own words
kind: prompt | skill | procedure   # a pattern a person adapts | packaged, used the same way across a team | written steps mixing AI and manual work
work_types: [ id ]
pattern: id                        # often draft-review-loop, research-brief, grounded-knowledge-assistant or other
ladder: assist | augment           # automate or delegate belongs in ai-solution-delivery
runtime_class: id                  # usually personal-assistant or shared-team-skills
tool: string | null                # only a product listed in overlay/tool-catalog.yaml
status: candidate | testing | approved | needs-retest | retired   # lifecycle in ../workflow-library.md §4
origin: crowd | champion | central | solution   # any user, a champion, the central team, or a launched solution
owner: role                        # keeps the entry current
reviewer: role                     # approves it for the library
human_checkpoint: string           # who checks what before the output is used or leaves the team
data_rules: string                 # from overlay/policy.md or the tool catalog; "unknown" blocks approval
risk_tier: string | null           # the tier name from overlay/policy.md, if one exists
tested: { as_of: YYYY-MM-DD, cases: integer, passed: integer, by: role, notes: string } | null
reuse: { as_of: YYYY-MM-DD, groups_using: [ string ], evidence: string } | null
review_when: [ string ]            # conditions that send the entry back to testing
retired_because: string | null
links: { opportunity: id | null, solution: path | null, measures: [ id ] }
updated: YYYY-MM-DD
```

## 2. Field rules

- **Required for every status:** `schema`, `id`, `title`, `roles`, `task`, `kind`, `status`, `origin`, `owner`,
  `human_checkpoint`, `data_rules`, `updated`.
- **Required before `approved`:** `reviewer`, `tested` (with `passed` and `cases` from real, sanitized examples run by
  someone other than the author), `data_rules` not "unknown", and `risk_tier` when the overlay defines tiers.
- **Human checkpoint is never empty.** Name the role, the check and the moment ("Reviewer checks every cited
  authority against the source before the letter is sent"). "Review as needed" is not a checkpoint.
- **Roles, not people.** `owner` and `reviewer` are roles. The body may credit a contributor by name only if the user
  offers it; never rate anyone.
- **Tools.** `tool` names a product only if `overlay/tool-catalog.yaml` lists it; otherwise `null`, and rely on
  `runtime_class`.
- **Ladder.** `assist` or `augment` only. A workflow with no person on the normal path is a solution: route it to
  ai-solution-delivery.
- **Retirement.** Set `status: retired` and `retired_because`; keep the file so links do not break.
- **Quote free text** in double quotes. Dates record events; they are never deadlines.

## 3. Example

```yaml
schema: workflow/v1
id: notice-response-draft
title: "First draft of a reply to a routine tax authority notice"
roles: ["Tax senior", "Tax manager"]
practice: "Business tax compliance"
task: "Draft the reply letter to a routine notice from the notice, the return and the client file"
kind: procedure
work_types: [document-production, research-synthesis]
pattern: draft-review-loop
ladder: augment
runtime_class: shared-team-skills
tool: null
status: approved
origin: champion
owner: "Business tax champion"
reviewer: "Tax technology manager"
human_checkpoint: "The manager checks every figure and cited rule against the return and the source before signing"
data_rules: "Approved tool only; client name and identifiers removed from prompts unless the tool is approved for client data"
risk_tier: null
tested: { as_of: 2026-10-14, cases: 12, passed: 10, by: "Tax manager (not the author)", notes: "Two drafts cited the wrong period; checkpoint caught both" }
reuse: { as_of: 2026-10-20, groups_using: ["Business tax, Leeds", "Business tax, York"], evidence: "Champion clinic notes" }
review_when: ["Tool or model changes", "Notice format changes", "Governance changes the data rule"]
retired_because: null
links: { opportunity: null, solution: null, measures: ["embedded-workflows"] }
updated: 2026-10-20
```

The example is illustrative, not evidence.
