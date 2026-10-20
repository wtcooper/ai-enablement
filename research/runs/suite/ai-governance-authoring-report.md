# Authoring report: ai-governance skill

Date: 2026-10-20 · Brief: `research/runs/suite/briefs/author-ai-governance.md` · Validator: 0 errors and 0 warnings in
`skills/ai-governance/` (the remaining errors in the run belong to sibling skills that link to `../ai-enablement/SKILL.md`,
which had not been written yet when the validator ran).

## Files written (plugins/ai-transformation/skills/ai-governance/)

| File | Lines | Fed by |
|---|---|---|
| `SKILL.md` | 216 | Spec §2-§4; advisor `SKILL.md` (structure, voice); core-rules block copied verbatim; all step files |
| `references/baseline.md` (step 1) | 172 | topic-governance §3 moves 1-3, 19, 24, 26; §4 Onboard/Diagnose questions; §8 Onboard; §7 Example C; topic-partners (JOTWELL-EMPSON-2013) |
| `references/policy-and-data.md` (step 2) | 165 | topic-governance §2 concepts 1, 2, 6; moves 4-6, 23; §5 traps; §8 Frame |
| `references/risk-tiers.md` (step 3) | 181 | topic-governance §2 concepts 3, 5; moves 15, 16, 25, 29; §8 Reimagine and runtime-class notes; §7 Example B; library index §1, §3 (pattern checkpoints); plan-and-control §3.4; onboarding §5 gates |
| `references/records.md` (step 4) | 158 | topic-governance concept 4; moves 7, 17-19; §8 Map; assurance guardrails §5 (FRC-AIAUDIT-2025); tax guardrails §3; professional-services guardrails §1, §4 |
| `references/professional-duties.md` (step 5) | 178 | topic-governance concept 8; moves 8-14; §7 Example A; tax, assurance, professional-services and security guardrails |
| `references/vendor-evaluation.md` (step 6) | 163 | topic-governance concept 9; moves 5-8, 20-22; §4 vendor questions; §7 Example D; professional-services guardrails §8 |
| `references/secure-enablement.md` (step 7) | 181 | topic-governance concept 10; moves 23, 27, 28; §8 Plan and Roll-up; §7 Example C; topic-partners (POLSINELLI-2026, LAWNEXT-2024, VINCI-2026, CIPD-2026, IAB-KPMG-2025) |
| `references/briefs/evaluate-tool.md` | 59 | Vendor-evaluation scorecard; advisor brief format |
| `references/templates/policy.md` | 148 | topic-governance §8 Frame policy skeleton and Diagnose gap register |
| `references/templates/guardrails.md` | 27 | Workspace `overlay-example/guardrails.md` shape (kept compatible) |
| `references/templates/tool-catalog.yaml` | 35 | Workspace `overlay-example/tool-catalog.yaml` shape plus §8 Map inventory and Plan approval-record fields |
| `references/templates/vendor.md` | 71 | Scorecard; §8 Plan approval record |
| `references/schemas/policy.md` (`policy/v1`) | 136 | State fields; defines the governance controlled values |
| `references/schemas/tool-catalog.md` (`tool-catalog/v1`) | 122 | Backward-compatible extension of the starter catalog |
| `references/schemas/vendor.md` (`vendor/v1`) | 86 | Scorecard frontmatter |
| `references/library/index.md` | 6 | Pointer stub (see conflicts) |
| `references/method/people-and-change.md` | 6 | Pointer stub (see conflicts) |

All three schema examples and both templates with YAML parse with `yaml.safe_load`.

## Conflicts resolved

1. **The core-rules block in this skill points to `references/library/index.md` and
   `references/method/people-and-change.md`.** Those paths resolve from the advisor, not from a sibling. I added
   two short pointer files at those paths that redirect to the shared files (the ai-portfolio and
   ai-solution-delivery authors did the same). Owner may prefer to change the validator or the rules' wording.
2. **IRS guidance on AI.** The governance research found "no AI-specific IRS guidance"; the tax archetype records
   OPR Alert 2026-19 (24 June 2026). I used the archetype: the alert exists, is introductory, and does not mention
   consent, so there is still no IRS guidance on AI and section 7216 consent.
3. **ABA Opinion 512.** The research read it through a secondary summary (ABA-512-2024); the professional-services
   archetype read a copy of the opinion (ABA-OP512-2024). I cite ABA-OP512-2024 for points the archetype records
   (consent before self-learning tools, boilerplate not enough, bill time actually spent) and keep ABA-512-2024,
   marked "as summarised", for the two points found only in the summary (consent not needed when no client
   information is input; full responsibility whatever the review level).
4. **Same article, two keys.** The research's JOFA-2026 and the archetype's JOFA-ETHAI-2026 are the same Journal of
   Accountancy article (different URLs). I used JOFA-2026.
5. **"Synthesis" items.** The research's synthesis heuristics (tier thresholds, ladder rule, re-approval triggers,
   lanes, measures, matrix) appear as "advisor default", never as sourced requirements; SKILL.md rule 14 requires
   the assistant to label them.
6. **Review cadence vs. no calendar deadlines.** I kept MSFT-RAI-2022's "at least annually, on new uses, before a
   release stage" as a sourced cadence template and put dates in YAML only as records (`updated`, `last_reviewed`),
   never as deadlines. Research example C's "quarterly" sampling was dropped.

## Gaps

- No firm's actual AI acceptable-use policy text was found; worked examples are illustrative composites.
- Vendor contract-term prevalence (notice periods, indemnities, exit) is unknown; scorecard "meets" criteria are an
  advisor default.
- ISO/IEC 42001 text not read; no Annex A count is stated.
- FRC guidance PDF and thematic review were not read by the governance research; documentation detail comes from the
  assurance archetype's FRC-AIAUDIT-2025 entry.
- State bar variation, GDPR Article 28 and DPIA detail, US state AI laws, SEC and FINRA, HIPAA and cyber-insurance
  requirements are not covered.
- No independent measure of review effectiveness (override or error rates) exists in the inputs.
- No evidence grades are cited: this skill cites no archetype use cases (it governs them rather than proposing them).

## New controlled values proposed (defined in `references/schemas/policy.md` §3)

None of these exist in `vocabulary.yaml`; I propose adding them as new keys:

- `regimes`: tax-7216, attest-independence, legal-practice, client-terms, eu-deployer, privacy-law
- `data_classes`: public, firm-internal, client-confidential, regulated
- `tool_tiers`: consumer, commercial, firm-controlled
- `risk_tiers`: tier-1, tier-2, tier-3, tier-4
- `catalog_status`: approved, approved-with-conditions, pilot, under-review, not-approved, retired
- `scorecard_ratings`: meets, partial, gap, unknown; scorecard dimensions: security_privacy, retention_training,
  certifications, contract_terms, change_control, exit
- `screen_results`: clear, needs-review, not-applicable, unknown; `own_sample_test`: not-run, passed, failed,
  not-applicable
- `reapproval_triggers`: model-change, sub-processor-change, terms-change, new-data-class, new-use, incident
- `backbone`: nist-ai-rmf, iso-42001, internal

Reused from the shared vocabulary: `runtime_classes`, `patterns`, `ladder`, `journey_stages` (by reference), and the
opportunities schema's `label: draft-to-validate`.

## Open questions for the owner

1. Should the governance ids above move into `vocabulary.yaml` (and the validator check `tool-catalog.yaml` against
   them), or stay local to this skill?
2. Should the workspace starter (`templates/workspace/overlay-example/`) ship the new `tool-catalog/v1` fields, a
   `policy.md` and a `vendors/` folder? I did not change it (outside my folder); the current example stays valid.
3. The advisor's rule 6 says "recommend tools from it". The new `status` field means readers should recommend only
   approved entries; should the advisor's library §4 or core rule 6 say so, or is the note in
   `schemas/tool-catalog.md` §3 enough?
4. Pointer stubs vs. a validator change for the core-rules paths (conflict 1).
5. Is a separate AI inventory file (beyond the catalog) wanted in the workspace layout? The skill currently keeps the
   inventory design in `policy.md` section 5 and tools found in use in section 1.
