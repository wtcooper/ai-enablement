# Synthesis report: advisory / transactions

Run date 2026-10-20 (wave 5). Outputs:
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/transactions.md` (252 lines, table of contents, 10 sections)
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/transactions.yaml` (16 entries, valid YAML)

`scripts/validate.py` reports 0 errors. It warns that the file is below the 50% A/B target (31%).

## Counts in and out

| Input | Candidates | Kept as entries |
|---|---|---|
| adv-transactions-combined.md (deep dive) | 16 use cases | 16, ids kept as -01 to -16 |
| adv-x-independence-pricing.md | 1 (its "advisory-transactions-01": outcome-linked and success-fee pricing) | 0. Pricing the firm's own work belongs to professional-services. Cross-referenced to professional-services-scoping-pricing-19 and -17, and used as a guardrail on contingent fees |
| adv-x-state-of-ai-disruption.md | 0 transactions use cases (it offers a talent warning and a tracker narrative) | Used in roles, objections and frontier |
| landscape-advisory.md | 1 lead (QOE-VENDORS-2026, search-only) plus FORVIS-QOE-2026 and ACG-DEALMAX-2026 | Lead merged into -05 as a search-only source |
| Other adv-*.md "Routed to other modules" sections | 0 items routed to transactions (also searched for transaction-advisory, consulting-fpa and risk-advisory) | none |

Total in: 18 candidates or leads. Total out: 16 entries.

## Duplicates merged

- QOE-VENDORS-2026 (landscape lead: Finsider, QoEAgent and Shepi claims such as 60-80% faster diligence) merged into -05. It also overlaps -03 and -04. It is search-only and is not used as an outcome.
- The disruption file's Forvis Mazars talent warning is the same document as FORVIS-QOE-2026. It is already in -01, -10 and -12, so no new entry was made.
- The independence-pricing candidate (outcome-linked fees) was routed, not merged, as noted above.
- No two deep-dive entries describe the same change to the work. Close pairs were kept apart and cross-referenced: -01 and -03 (FDD workbench vs proof of cash), -02 and -04 (meeting prep vs adjustment sign-off), and -05 and -06 (direct-to-buyer vs sub-contracted capacity).

## Normalization changes

- -03 moved from augment to **automate**. Matching runs with no person on the normal path, and flagged items go to CPAs, as in the vocabulary's matching example. The reason is recorded in the notes.
- -09 gained PwC UK's 2,500-practitioner platform count (ICAEW-BIGSIX-2024) and a client-consent guardrail (JOFA-ETHICSAI-2026). -11 gained SEC-RULE2-01-2026 ((c)(4)(viii) investment banking; (c)(5) contingent fees). Both points come from the inputs.
- Renamed CITYAM-DELOITTEAU-2025 to **CITYAM-DELOITTE-2025**, the ref the forensic, risk-controls and fpa-performance inputs use for the same URL.
- Removed one unsourced connective phrase from -06 ("without adding headcount"). -07's problem statement is now attributed to QoEAgent's reading of the SOP, because the SBA clause text was not read.
- Added plain-language definitions (proof of cash, flux analysis, data room, TSA, agentic harness, databook).

## Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | -15 | | | 1 |
| augment | -01, -02, -04, -08, -09, -12, -14 | -07, -10, -11 | -05, -06, -13 | 13 |
| automate | | -03 | | 1 |
| delegate | | -16 (idea, D) | | 1 |

Gaps: delegate has only an idea; no named agent owns a diligence outcome, and Deloitte's agent harness is described as "human-led". Automate has a single vendor-run entry. Assist rests on one academic abstract. There is no automate-at-step entry and no delegate-at-model entry. None was invented.

## Grade mix

A 0, B 5 (-01, -02, -03, -09, -11), C 10, D 1 (-16). That is 31% A/B.
- None qualifies for A under the 2026-10-17 rule. The nearest measured figure, 74-95% contract-review accuracy, comes from legal due diligence, which is an adjacent process.
- The B grades rest on named deployments with usage counts, a customer recollection (Miller Cooper) or one vendor-published engagement.

## Gaps

- **Quality evidence.** There is no error rate, override rate, parallel run, inspection finding or independent test for AI-assisted QoE or FDD. All speed figures (27%, 80%, 24 hours, 21-30%) are vendor or self-reported.
- **Mid-market firms are nearly invisible.** Only Miller Cooper and Pease Bell appear, with nothing from RSM, Baker Tilly, CohnReznick, Citrin, CBIZ or Crowe TAS. Big Four evidence is at announcement level.
- **Independence.** It was not verified which diligence services are restricted for the firm's own audit clients. The module points to assurance-acceptance-independence-15.
- **Lenders and insurers.** The SBA clause was read only through vendor pages. No source covers how R&W underwriters treat AI-assisted QoE.
- **Missing sources and topics.** There are no podcasts or session-level conference sources, and no standard-setter statement on AI in TAS. SPA and completion-accounts work has only a 2024 spoken view.

## Routed items (for other modules' synthesis)

From adv-transactions-combined.md section 4:
- **valuation:** SBA valuation independence clause (QOEAGENT-WHO-2026).
- **risk-controls:**
  - AI governance diligence on targets (FORVIS-AIBUYSIDE-2024, FASKEN-RWI-2026).
  - GT-PEAI-2026: 9% very confident of passing an AI governance audit in 90 days; date not found.
  - The Deloitte Australia refund (CITYAM-DELOITTE-2025).
- **fpa-performance:** portfolio-company operational AI (SPGLOBAL-PE-2026: 72% of GPs rank operational improvements top; GT-PEAI-2026).
- **forensic-disputes:** fraud found in diligence; forged or deepfaked data-room documents. Not researched.
- **professional-services:**
  - Junior-pipeline depletion and the effect of cheap QoE products on pricing (FORVIS-QOE-2026).
  - Fee ranges on a broker page (CTACQ-QOE-2026).
  - Outcome-linked advisory fees (BBTAX-SH-2026, from the independence-pricing file).
- **tax:** transaction tax diligence and structuring. Not researched.
- **Outside the archetype:**
  - Legal contract-review accuracy (ARTLAW-AG-2024, used here only as an adjacent measure).
  - Expert-call synthesis (THIRDBRIDGE-PEDD-2026).
  - R&W policy mechanics.
  - The withdrawn arXiv paper (ARXIV-KIM-2024), cited only as "do not cite".

## Ref aliases to reconcile

- The independence-pricing input uses SEC-RULE2-01-2026 and JOFA-ETHICSAI-2026. The published assurance files use SEC-REGSX-2-01 and JOFA-ETHAI-2026 for the same documents, and the CAS and risk-controls inputs use JOFA-ETHICS-2026.
- This file keeps the advisory inputs' refs. A repo-wide alias pass is needed.

## Suggested improvements to the briefs

1. Ask deep dives to classify ladder against the vocabulary's worked examples. Matching with exceptions reviewed is automate, and the analyst had marked it augment.
2. Give one canonical ref per document across waves, through a shared ref registry, so syntheses do not have to rename refs.
3. For low-evidence modules, lower the 15-entry and 50% A/B validator targets, or let a module declare "thin evidence". This avoids pressure to pad or to over-grade.
4. Ask module researchers to confirm independence restrictions against primary rule text for their module's specific services, not only the general SEC list.
5. Ask for at least one attempt at practitioner primary sources (firm TAS leaders' talks, podcasts, ACG chapter sessions) before falling back to vendor pages.
