# Trim report: ai-governance

Brief: `research/runs/trim/brief.md` (moderate trim). Edits are only in
`plugins/ai-transformation/skills/ai-governance/`. I made no commits. Other sessions' checkpoint commits (`c5bf438`,
`949b30d`, `09d2b45`) swept most of these edits into history while I worked, so `git diff` shows only the last few.

## Checks

- `python3 scripts/validate.py`: 0 errors (the same 31 archetype warnings).
- `claude plugin validate --strict plugins/ai-transformation`: passed.
- The three schema examples, the policy and vendor template frontmatter, and `templates/tool-catalog.yaml` all parse
  with a YAML loader that rejects duplicate keys.
- In every method file, each cited source key has an entry in that file's Sources list, and no entry is left uncited.
- The core-rules block is byte for byte unchanged; the validator confirms it.

## Line counts

| File | Before | After | Change |
|---|---|---|---|
| `SKILL.md` | 241 | 140 | -42% |
| `references/baseline.md` | 173 | 99 | -43% |
| `references/policy-and-data.md` | 168 | 99 | -41% |
| `references/risk-tiers.md` | 183 | 100 | -45% |
| `references/records.md` | 161 | 100 | -38% |
| `references/professional-duties.md` | 182 | 100 | -45% |
| `references/vendor-evaluation.md` | 173 | 100 | -42% |
| `references/secure-enablement.md` | 185 | 100 | -46% |
| **Method files, total** | **1225** | **698** | **-43%** |
| `references/schemas/policy.md` | 140 | 131 | -6% |
| `references/schemas/tool-catalog.md` | 122 | 118 | -3% |
| `references/schemas/vendor.md` | 91 | 86 | -5% |
| `references/templates/policy.md` | 148 | 147 | -1% |
| `references/templates/vendor.md` | 73 | 71 | -3% |
| `references/templates/tool-catalog.yaml` | 35 | 35 | 0 |
| `references/templates/guardrails.md` | 27 | 27 | 0 |
| `references/briefs/evaluate-tool.md` | 59 | 56 | -5% |
| **All reference files** | **1920** | **1369** | **-29%** |

The method files are 43% shorter. All reference files together are 29% shorter, which misses the brief's target of
about 40%. The gap comes from the schemas and templates, which I barely changed: the brief freezes the tool-catalog
fields, and the templates set the shape of the files users receive (see "Kept" below). Every method file is now at most
100 lines, so none needs a contents list. The policy and tool-catalog schemas are over 100 lines and keep theirs.

## What I cut or merged, and why

**SKILL.md**
- The seven step sections, each with a goal, four questions, exit criteria and output, are now one table: step, goal,
  file to read, anchor question ids, output. The questions and exit criteria live in each step file's §3 and §1, and
  the skill reads that file when it enters the step.
- The step 6 handback to ai-solution-delivery ("whatever the decision"), and step 7's advice on which files to share,
  sit under the table.
- "How to talk", "Start or resume" and "Delegation" are shorter. I dropped advice the core rules already give and kept
  the skill's own routes: "one answer only", "a later step drafted now" (N9) and the resume logic.
- The save rule is now one paragraph. It keeps every fixed behaviour: no advance while exit criteria are open, write
  only the sections the templates define and refresh status notes (D8), quoted free text, the YAML parse check and the
  duplicate-key check (N6).
- I kept rules 10 to 15. Rule 14 now says that defaults can be changed and should be stated once. None of these rules
  overlap enough to merge.

**Method files (all seven)**
- Each file keeps the same structure: 1 Goal and exit, 2 How to run, 3 Question bank, 4 Expert moves, 5 Defaults and
  decision rules, 6 Worked example, 7 Output, 8 Sources.
- The "Common traps" tables are gone. A trap that carried a rule now sits in §5. Traps that only repeated a move were
  dropped.
- I dropped the "More, as needed" question lists.
- Each worked example is now two to four lines.
- Each claim is stated once and other files point to it. Examples: the ban-first finding (baseline move 2), the
  urgent-deployment bypass (policy-and-data move 3), embedded AI in the inventory (baseline move 5), agent controls
  (risk-tiers move 4) and own-sample testing (risk-tiers move 3).
- `risk-tiers.md`: the 11-row pattern table is now a rule with three minimum-tier bands. The skill reads the per-pattern
  checkpoints from the shared library §3. The five runtime-class notes are folded into move 4 and one decision rule.
- `professional-duties.md`: regime detail that the archetype `guardrails.md` files already hold, with their sources,
  is now a pointer table. This covers UK PCRT, Australia's TPB, CalBar, NYC Bar, the Law Society, ICMCI, IFIAR and the
  JofA SOC article. The 7216 triage, the consent elements, the independence screen and the processing-location rules
  stay in full in §4. Other skills link to that section.
- `vendor-evaluation.md`: NIST's contract checklist is folded into the scorecard's evidence column. The
  certification-scope and liability traps are now one decision rule.
- `records.md`: the inventory field list is shorter (NIST fields kept). The PCAOB "document source data" move is cut.
- `policy-and-data.md`: the policy skeleton is cut, because the template already sets it. So is the CSA AI Controls
  Matrix detail.

**Sources I removed, along with the claims they backed:** CSA-AICM-2025, MSFT-WTI-2024, JOTWELL-EMPSON-2013, RAJI-2020,
KN-2025, OPENLAYER-2026, INSINSIDER-LAWYERS-2026, LAWSOC-GENAI-2026, GEND-2026, AMPCUS-2026, CIPD-2026,
POLSINELLI-2026, VINCI-2026, SDNY-AVIANCA-2023 and GUARDIAN-DELOITTE-2025 (both cut from secure-enablement only; still
cited in risk-tiers), CALBAR-GENAI-2026, NYCBAR-OP2024-5-2024, ICMCI-AICODE-2026, IFIAR-TTF-2026, JOFA-SOCETH-2026,
PCRT-AI-2026, TPB-GS55-2026, FRB-SR117-2011 (from vendor-evaluation only), EU-OMNIBUS-2026 (from professional-duties
only), and a few per-file duplicates. All the archetype ones are still cited in the archetype `guardrails.md` files.

**Schemas, templates, brief**
- The controlled-value tables in the policy schema (§3.1 to §3.4) are now lists, with the same ids and the same
  section numbers.
- The field-rule prose in all three schemas is merged.
- I shortened the template header comments and merged the brief's ten-item "Find" list into five items.

## Deferred features

Each line says what the cut material would add back and when that would be worth it.

- **Per-pattern risk table** (11 patterns: rung, minimum tier, what the reviewer owns, failure mode): worth it once a
  firm runs three or more agentic patterns, or once users ask "which tier is pattern X?".
- **Per-runtime-class control notes** (personal assistant, team skills, workflow automation, background agent,
  managed runtime): worth it when a firm puts its first background agent or managed runtime into the catalog.
- **Internal-audit frame for tier-4 uses** (scope, map, collect, test, reflect; RAJI-2020): worth it when a firm takes a
  tier-4 use toward production.
- **Mapping to framework controls** (CSA AI Controls Matrix, ISO/IEC 42001 clauses): worth it when a firm seeks ISO/IEC
  42001 certification or its board asks for a control mapping.
- **Non-US regimes held in this file** (UK PCRT, Australia's TPB, UK Law Society, SRA supervision, state bars, ICMCI
  code): worth it when users regularly work outside the US. For now the archetype files cover them.
- **Contract and liability depth** (who carries liability with legal AI vendors, certification versus EU AI Act
  conformity): worth it when firms negotiate enterprise AI contracts through this skill, or prepare for EU high-risk
  obligations (from December 2027).
- **Survey context for a business case** (bring-your-own-AI rates, who owns AI governance, rates of reliance without
  review): worth it if users ask the skill to argue for a governance budget.
- **Partnership leadership evidence** (Empson's "leadership constellation", a law-firm chair's interview, training
  before access in a CIPD case study): worth it if users often stall on partner buy-in. ai-enablement may be the better
  home.
- **Extra questions and "common traps" tables per step:** worth adding back trap by trap, when end-to-end runs show the
  same mistake twice.
- **Longer worked examples:** worth it if test users misread a step's output format.

## Kept, though a reader might expect it cut

- **The whole 7216 triage and the consent elements** (`professional-duties.md` §4). `ai-portfolio/.../acquired-firms.md`
  and `transformation-advisor/.../acquisitions.md` link to this section by number.
- **The tool-catalog schema format and template, unchanged.** The brief freezes catalog fields for the coming
  `use_for` work, and every sibling skill reads the catalog.
- **The policy template, almost unchanged.** It defines the sections the skill writes, and D8's "write only template
  sections" rule depends on them. The policy document is the deliverable.
- **The policy schema's `parent` field and the one "across units" line.** They make rule 13 (stricter, never looser)
  work for unit policies, and they cost two lines.
- **The default tables** (data matrix, four risk tiers, record by tier, request-path lanes, re-approval triggers).
  Each is stated once and labelled as a default the user can change (rule 14). The skill never asks the user to
  configure them up front.
- **The EU AI Act Annex III rule and the December 2027 date, with "re-verify".** It sets a tier and shows the user a
  regulatory date.
- **The vendor `evaluation` null/desk/full rule, the "Evaluated by" draft labels and the handback to delivery whatever
  the decision** (D5, D7, D8). It now appears in the vendor-evaluation Output section, the vendor schema and the
  template comment, each in shorter form, because each of those files can be read on its own.

## Shared files that need a change

- **None are required.** The only links into this skill from other skills point to `professional-duties.md` §4, which
  still holds the triage and the independence screen. The sibling SKILL.md files link only to `../ai-governance/SKILL.md`.
- **Optional, `spec/2026-10-20-skill-suite.md` §5:** it sets a SKILL.md target of 150-250 lines. After this trim the
  governance SKILL.md is 140, and the brief's new ceiling is 160. The spec could state the new target.
- **Optional, `evals/e2e/2026-10-21-suite-handoff/FIXES.md`, "Declined or left open":** it still says the ai-governance
  YAML check was not added. Round 2 (N6) added it, and the trimmed save rule keeps it. That line is out of date.
