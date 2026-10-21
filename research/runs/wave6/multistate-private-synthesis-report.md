# Synthesis report: tax / multistate-private (wave 6, mid-market extension)

Synthesised 2026-10-21. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/modules/multistate-private.md` (258 lines)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/use-cases/multistate-private.yaml` (14 entries; `scripts/validate.py` reports 0 errors, and the only warning for this file is the expected below-target A/B share)

## Counts in and out

| | Entries | A | B | C | D |
|---|---|---|---|---|---|
| In: combined deep dive (`mm-multistate-private-combined.md`) | 13 | 0 | 1 | 8 | 4 |
| In: routed from `mm-widen-tax.md` (state PTET modelling) | 1 | 0 | 0 | 1 | 0 |
| In: landscape scan, new candidates | 0 | | | | |
| **Out** | **14** | **0** | **1** | **9** | **4** |

The landscape's multistate items (South Carolina DOR, the Tax Notes 49-agency survey, the SEATA recap and the MTC panel) were
already in the deep dive. Its SALT-VENDORS-2026 row is search-only and is routed to indirect-tax. The other `mm-*.md` files
checked were nonprofit-government, private-company-practice and widen-tax. Only widen-tax routes an item here.

No entries were dropped. All 13 dive entries describe different changes to the work, and the C and D entries each add
something the B entry lacks (the firm side, payroll nexus, apportionment, ideas for the taxpayer's defence).

## Duplicates merged

- **Within the inputs:** none. The deep dive was a single combined pass and arrived de-duplicated.
- **Same document, different refs:** the landscape's POSTCOURIER-SCDOR-2026 and TAXNOTES-STATES-2026 are the archetype's
  SCPOST-AUDIT-2026 and TAXNOTES-UNWATCHED-2026. The archetype refs are kept.
- **Overlaps with other modules, kept as cross-references rather than merged** (the archetype's modules are not edited):
  `#01` with `tax-controversy-15`; `#12` with `tax-controversy-14`; `#04` and `#05` with `tax-indirect-tax-13`; `#06` with
  `tax-compliance-corporate-06`; `#07` with `tax-research-advisory-01` to `-08` and `-04`; `#08` with `tax-compliance-corporate-12`
  and `tax-research-advisory-23`; `#09` with `tax-compliance-corporate-13`; `#14` with the widen pass's research-advisory
  entry (provisional id `tax-research-advisory-new-01`).

**Edits to the dive's entries.**
- Example-type and cross-reference sentences were added to every entry's `notes`.
- `pattern: other` is now described in the notes of `#11`, `#12` and `#13`.
- The unsourced prerequisite in `#11` is now marked "inferred".
- "See section 4" pointers were replaced with module ids.

No grade, outcome or source was changed.

## Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | 07, 08 (D), 10 (D) | 12 (D) | 11, 13 |
| augment | 04, 06, 14 | 01 (B), 02, 03, 09 (D) | none |
| automate | none | 05 | none |
| delegate | none | none | none |

- **Delegate: no evidence in this module.** The nearest entries are `tax-indirect-tax-13` (sales tax registration agents) and
  `tax-compliance-corporate-06` (agent-prepared returns with state apportionment). No entry was invented to fill the gap.
- **Automate: one vendor claim** (`#05`, payroll registration: Gusto/Mosey, Warp, Skyvern).
- **Model scope: two entries.** Both are demand created by AI (remediation marketing, AI companies as a client segment),
  not AI used in the work.
- **Counterparty versus firm side:** 01, 02, 03 and 12 are agency-side. The rest are firm or in-house side, and all of those
  are C or D.

## Grade mix

- **0 A, 1 B, 9 C, 4 D.** That is 7% graded A or B, which makes the module thin.
- **The one B** (`#01`) rests on press and podcast accounts of named state deployments. No agency published a measured
  outcome.
- **Independent figures exist but grade nothing above C for the firm side.** These are the Tax Notes survey, the MTC
  programme data and the Vals benchmark. They measure agency adoption, disclosure demand or model answers, not the outcome
  of a use case.
- **Ideas:** the four D entries are titled "Idea:". `#10` rests on a conference talk announcement (talk content not seen),
  so it is held at D.
- **Considered and not changed:** `#13` could be read as B (a named firm's real offering). It stays C because the pages are
  marketing and show no engagement.

## Gaps

- **No firm-side deployment.** No top-100, regional or local firm, PE-backed platform or in-house team was found describing
  AI in multistate income, franchise or payroll work. No error, override, parallel-run or time-saving figure exists.
- **No state guidance.** No state board of accountancy or revenue department guidance on AI-assisted state tax work was
  found. OPR Alert 2026-19 is federal.
- **No published agency results.** No state has published audit-yield, no-change or false-positive figures for its selection
  models. Primary contracts (South Carolina FAST, New York CISS) were not available.
- **Only adjacent quality evidence.** There is no SALT-only benchmark, and the Vals P-004 question is a single item.
  **Discrepancy to verify:** `#07` reports the 2026-10-20 read (leader 91%, three models at 76.5%, one passing all checks).
  `tax-research-advisory-04` reports the 2026-10-16 read as "twelve of eighteen models scored 0". VALS-TAXAGENT-2026 is also
  dated 2026-10-20 here and 2026-10-16 in the archetype's sources.md.
- **Thin areas:** payroll nexus (vendor-only), PTET (an AI-native firm and a vendor), and state conformity and credits
  (nothing found).
- **Sources not reached:** practitioner communities (r/taxpros blocked) and paywalled Bloomberg Tax and Law360.

## Routed to other modules (from the inputs, for those modules' synthesis)

- **indirect-tax:**
  - Sales and use tax nexus monitoring and registration agents (`tax-indirect-tax-13`).
  - Avalara Aviator agent hub (product page, Sep 2026) [AVALARA-AVIATOR-2026], plus the Kintsugi, Vertex and Sovos claims
    [SALT-VENDORS-2026, search-only].
  - Taxation of AI products and automated services (Maryland, Texas, Washington, Indiana, Illinois) [TRFORD-SALT-2026].
  - Streamlined Sales Tax multistate voluntary disclosure proposal (MTC Nexus Committee agenda, 27 Jul 2026) [MTC-ANNUAL-2026].
- **controversy:**
  - State agency generative AI in call centres (CDTFA with SymSoft; Missouri's chatbot) [CDTFA-PR-2025; CDTFA-2025], already
    `tax-controversy-20`.
  - General state risk targeting (`tax-controversy-15`).
  - State notice triage (`tax-controversy-01`).
- **compliance-corporate:**
  - Agent-prepared business returns with state apportionment [BYRON-2026] (`tax-compliance-corporate-06`).
  - Law-change and calendar tracking (`tax-compliance-corporate-12`).
- **compliance-individual-business:** Basis and commentary on agent-prepared partnership returns [OLIVER-1065-2026];
  composite and PTET return preparation for owners.
- **research-advisory:** general AI tax research tools and benchmarks [VALS-TAXAGENT-2026]; Blue J; the Vals P-004
  discrepancy above.
- **transfer-pricing:** states devoting more resources to related-party transactions, royalties and management fees
  [WITHUM-SEATA-2026].
- **provision-pillar-two:** state tax disclosure under the new income tax rate reconciliation (the MTC seminar covered ITEP
  analysis) [MTC-ANNUAL-2026].
- **Archetype guardrails:** OPR Alert 2026-19 [KTS-OPR-2026; IRS-OPR-2026].
- **Coordinator:** a suggested index row for ARCHETYPE.md is "multistate-private | state income, franchise and payroll nexus,
  apportionment, voluntary disclosure, PTET, and state agencies' AI; almost all named evidence is agency-side | thin
  (1 of 14 A/B)".

## Suggested improvements to the briefs

1. **Fix source keys at the landscape stage.** Ask landscape authors to check the archetype's sources.md before minting a
   key. Here, two keys were minted for documents the archetype already cites.
2. **Ask for an "example type" field in deep-dive notes.** Use a fixed list (top-100, regional or local firm, PE-backed
   platform, Big Four, AI-native firm, law firm, vendor, regulator, counterparty). Synthesis then would not have to infer
   types from prose.
3. **Have routed items name a final or provisional target id**, and say whether the receiving module should hold a full
   entry or a cross-reference. The PTET item could sit in either place.
4. **Ask deep dives to record the version date of any leaderboard read** and to compare it with figures the archetype
   already holds. Vals P-004 differs between reads four days apart.
5. **Add a counterparty note to the vocabulary.** Agency-side use cases have no natural `function` value (the dive used
   `risk-compliance-legal`); a convention would keep modules consistent.
