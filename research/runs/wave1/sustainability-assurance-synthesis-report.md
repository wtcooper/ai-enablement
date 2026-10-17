# Synthesis report: assurance / sustainability-assurance

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-assurance.md` (context only; sections 3, 4, 7, 9, 13 mention sustainability) and
  `assurance-sustainability-assurance-combined.md` (one combined practice + discourse + governance pass, 15 candidates)
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/sustainability-assurance.md` (298 lines)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/sustainability-assurance.yaml` (13 entries)
- **Validator:** `INFO .../sustainability-assurance.yaml: 13 use cases, 0 graded A/B (0%)` plus the matching
  below-target WARN. No ERROR lines (0 errors overall). The module first came out at 310 lines and was trimmed to 298.
- **Why the target warning stands:** the caller set aside the 15–25 and 50% A/B targets for this module because the
  evidence does not exist. The deep dive found no grade A or B candidate, and none could be created without
  inventing facts. Padding to 15 would have meant keeping candidate 14 (which its own author called weak) and splitting
  the merged 08 back apart.
- **Not yet verified.** This output needs the verification pass against the sources.

## 1. Counts in and out

| | Combined deep dive | Landscape |
|---|---|---|
| Candidates in | 15 | 0 (no YAML entries; used for context) |
| Kept as their own entry (same id) | 12 (01–07, 09–13) | |
| Merged into another entry | 1 (15 into 08) | |
| Moved out of the YAML to module context | 1 (14) | |
| Out | **13** | |

- **Ids kept stable.** Output ids 01–13 equal the deep-dive ids 01–13, so verifiers can trace each entry directly.
- **Candidate 14 (AI-assisted digital tagging, D)** was dropped from the YAML. Its notes said nothing links AI tagging
  to assurance work, and the only AI sentence (ESMA) is about AI in ESEF generally. Its useful facts now sit in the
  module: the limited-assurance opinion covers mark-up compliance (§2) and ESMA's Q1 2027 tagging consultation and AI
  monitoring (§9). ESMA-AWP-2027 is listed in the module's Sources section because it no longer appears in the YAML.
- **Edits to kept entries:**
  - Ref `IAASB-TECHCAT-2026` renamed `IAASB-CATALOG-2026` (entry 13) to match the key for the same PDF in
    `assurance-over-ai.yaml`. Date kept as `2026-07` from the input (assurance-over-ai has `2026-07-09`).
  - Entry 02 `role_evolution` replaced. The input's line ("reviewers spend less time reading for tone...; no source
    measures this shift") was an unsourced editorial expectation. It now cites MDPI-SUSAI-2026 s. 7.2 on skills.
  - Entry 09 gained DECHERT-SEC-2026 as a source, because its notes already relied on that note's footnote 5.
  - `last_reviewed` set to 2026-10-17 on all entries.

## 2. Duplicates merged

| Output | Merged from | Choices made |
|---|---|---|
| 08 Preparer-side gap check and narrative drafting | 08 (Workiva Sustainability Disclosure Agent) + 15 (LLM drafting of ESRS/ISSB narrative) | Both describe preparers drafting disclosure text with AI before assurance sees it. Runtime class workflow-automation (08) over personal-assistant (15). Both outcomes, all six sources and both sets of checkpoints kept. Grade C and maturity announced in both. |

Considered and not merged: 03 (anomaly analytics during evidence work) and 06 (risk signals for planning). They share a
source and some flag types but change different steps and sit on different ladder rungs (augment vs assist).

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 06, 13 | | | 2 |
| augment | 01, 02, 03, 04, 05, 08, 10, 12 | | | 8 |
| automate | 11 | 07, 09 | | 3 |
| delegate | | | | 0 |
| **Total** | 11 | 2 | 0 | 13 |

- **No delegate entry and no model-scope entry.** No source shows an agent owning a multi-step sustainability
  assurance outcome, or a changed service or pricing model. EY's April 2026 agentic release covers audit engagements
  only (EY-MENAPR-2026). PwC Germany's CSRD.AI Manager (11) could become a model-level question (firms selling AI
  reporting tools to clients they might assure), but no source frames it that way, so it stays at step.
- **Automate/process:** 07 is an idea that rests on an ISSA 5000 example (A249). 09 is preparer-side, with vendor
  figures only.
- **By side:** assurance provider 8 (01–07, 13; function service-delivery); preparer 5 (08–12; function
  finance-accounting). Only 01 and 02 on the provider side are above D, and both rest on one 2024 analyst sentence.
- **Maturity:** in-production 1 (09), announced 5 (01, 02, 08, 10, 11), emerging 7 (03, 04, 05, 06, 07, 12, 13),
  piloting 0.

## 4. Grade mix

| Grade | In (15) | Out (13) |
|---|---|---|
| A | 0 | 0 |
| B | 0 | 0 |
| C | 8 (01, 02, 08, 09, 10, 11, 12, 15) | 7 (01, 02, 08, 09, 10, 11, 12) |
| D (idea) | 7 (03, 04, 05, 06, 07, 13, 14) | 6 (03, 04, 05, 06, 07, 13) |

- **D entries kept** because the provider side has nothing else. Each shows a different step (planning, analytics,
  external data, documentation, continuous evaluation, testing a client's AI) and carries standards-based guardrails
  (ISSA 5000 A91, A96–A98, A249, A262; IESSA R5320.11).
- **Grade-B candidates considered:** 09 (Watershed names Smiths Group and Harris Farm Markets) and 11 (PwC Germany).
  Both stay at C as the deep dive graded them. All 09 figures are vendor-published, and 11 names no client.

## 5. Gaps

- **No provider-side evidence.** No firm primary source names AI in sustainability assurance. Deloitte Omnia ESG and
  KPMG's greenwashing analytics appear only in one Verdantix press-release sentence from 2024. Searches for DNV, Bureau
  Veritas, ERM CVS and SGS found no AI content.
- **No quality evidence.** No error, override, parallel-run, inspection or enforcement figure for AI in this module. No
  regulator inspection findings for sustainability assurance at all.
- **Standards silent on AI by name.** Usable text is limited to "automated tools" paragraphs (ISSA 5000 A91, A96–A98,
  A231, A249, A262) and IESSA technology provisions. The IAASB rates the topic "Low" priority, "continue monitoring".
- **Weak practitioner discourse.** The only practitioner survey (ASE-CIKE-2025, n = 77, Moldova) reports its figures
  for financial audit. No podcasts found. One low-authority community site (ESGsource).
- **Blocked or unread:** PwC sustainability reporting survey (403); the Gu, Dai and Vasarhelyi satellite-GHG study
  (captcha); the published MDPI version of MDPI-SUSAI-2026 (the landscape's "graded reliance ceilings" description is
  not in the preprint read); the Verdantix full report (paywall); the full Hogan Lovells OAL article.
- **Ladder and scope:** delegate and model are empty (see §3).
- **Workforce:** no source measures team size, staffing pyramid or fees.

## 6. Routed to other modules (from the deep dive's §4)

- **planning-risk-assessment / substantive-testing / quality-management:** EY agentic AI release, 130,000 assurance
  professionals, 160,000 audit engagements, end-to-end support expected by 2028; audit-only text (EY-MENAPR-2026).
- **quality-management:** IFIAR 2026 technology report (about 30% growth in AI-enabled tools at the six largest
  networks in 2025; ISQM 1 monitoring; auditors in control) (IFIAR-TTF-2026). IAASB technology quality-management
  roundtables (243 participants) and planned guide series (IAASB-TQM-2026; IAASB-ENEWS-2026).
- **substantive-testing:** IAASB ISA 330/500/520 exposure drafts, comments due 15 Dec 2026 (IAASB-ENEWS-2026).
- **assurance-over-ai:** IAASB Technology Catalog 10(b), firms starting to offer AI assurance (IAASB-CATALOG-2026);
  FT summary that the Big Four are developing AI-verification services building on ESG assurance experience
  (FT-AIASSURE-2025, 2025-06-03, summary only).
- **acceptance-independence:** IESSA 5606.4 A3, R5606.6 and 5400.20 A3 on reporting software and management
  responsibility (IESBA-IESSA-2025). The AICPA SOC tool-provider ethics article may carry the same reasoning.
- **controls-testing / specialists:** assurance over a client's AI-operated controls (landscape R20, R24).
- **Outside the assurance archetype (preparer-side sustainability reporting):** Workiva, Watershed, IRIS Carbon,
  Briink and PwC Germany tool claims (entries 08, 09, 11, and former 15) belong in a corporate-reporting or
  sustainability-function archetype if one is researched. They are kept here only for their effect on assurance.

## 7. Suggested improvements to the briefs

1. **Add a low-evidence variant of the synthesis template.** The current template assumes three angle deep dives and
   15–25 entries. For combined single-pass modules, set the target as "every defensible candidate, no padding", and ask
   for a context section (dates, scope, data) and an open-questions section. Both were needed here and are not in the
   template's section list.
2. **Let the validator take a per-module target override** (for example a `targets: low-evidence` line in the YAML
   header). Otherwise this module will warn forever, and real regressions elsewhere get lost in the noise.
3. **Keep a canonical ref registry across modules.** The same IAASB Technology Catalog PDF had two keys
   (IAASB-TECHCAT-2026 and IAASB-CATALOG-2026) with two dates. Deep-dive briefs should check existing YAML keys before
   minting new ones.
4. **Add an optional `side` field (provider, preparer, user)** or a convention for it. This module and soc-attestation
   both lean on `function` as a stand-in for "whose AI is this", which is lossy.
5. **Tell deep-dive authors not to fill `role_evolution` with editorial expectations.** "Not described in the
   sources" is the right default. The one unsourced line in this input had to be replaced.
6. **Ask landscape scans to mark snippet-based descriptions of papers as provisional.** The landscape's description of
   MDPI-SUSAI-2026 did not match the preprint that was actually read.
