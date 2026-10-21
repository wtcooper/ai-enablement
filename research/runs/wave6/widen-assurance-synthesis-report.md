# Synthesis report: widen assurance for mid-market firms (quality-management, soc-attestation, assurance-over-ai)

Done 2026-10-21. Inputs: `mm-widen-assurance.md`, `landscape-mid-market.md`, and the "Routed to other modules"
sections of `mm-nonprofit-government-combined.md`, `mm-private-company-governance.md` and
`mm-private-company-practice.md` (the tax and multistate files route nothing to these modules). Only the three modules
and their YAML files were edited. `python3 scripts/validate.py`: 0 errors. The warnings for these files are
target warnings only (see Gaps).

## 1. Entries added and merged

### quality-management (25 -> 28 entries)

| Research item | Action | Result |
|---|---|---|
| new-01 SQMS 1 risk assessment and first annual evaluation (idea, D) | Added; Yellow Book clock (GAO-YBFAQ-2025) and GAQC watch item (GAQC-DEV-2026) from the nonprofit routing folded in | `-26` (D, idea) |
| new-02 AuditFile QualityLink (C) | Merged into `-14` (AI in the firm's own quality monitoring): same change; contrast with CPA.com QMCore (no AI on page) added | `-14`, grade **D -> C**, maturity emerging -> announced, title rewritten |
| new-03 Citrin Cooperman and PKF O'Connor Davies on Caseware DAS (C) | Merged into `-16` (firm-wide programmes on an AI-enabled platform): same change at mid-size firms with several engagement types | `-16`, grade B unchanged (rests on Sanville) |
| new-04 PKF builds its own agents in Caseware's governed platform (C) + new-08 staff-built automations checklist (D) + routed CASEWARE-PIONEER-2026 | Combined into one new entry: both make the same change (firm-built agents enter the QM system under review and change control) | `-27` (C, announced) |
| new-05 peer-review-ready AI governance file (idea, D) | Merged into `-13` (inspection-ready file per tool) as its AICPA peer-review version, labelled an idea | `-13`, grade C unchanged |
| new-06 Crowe and Eide Bailly PE/APS funding AI (C) + new-07 Oath AI-native firm in an APS (C) | Combined into one new entry (outside capital plus APS funding AI; same guardrails: PCAOB focus, PEEC drafts) | `-28` (C, announced) |
| Routed: Plante Moran CoCounsel pilot survey (nonprofit file) | Merged into `-12` (firm-approved guidance assistant) as a mid-market example with its vendor-published survey figures; RSM's middle-market positioning (private-company-practice file) added to notes | `-12`, grade B unchanged |
| Routed: engagement-letter disclosure, state laws (CFODIVE-AICPAPA-2026) | Added as a risk line to `-24` | `-24`, grade B unchanged |
| Routed: second AI tool checking the first; practice aid part 2 to `-17`, `-21`, `-23`; firm-level certification (FRC) | Already covered; no change | none |

### soc-attestation (16 -> 18 entries)

| Research item | Action | Result |
|---|---|---|
| soc new-01 AICPA and AIUC joint SOC 2 plus AIUC-1 offering (B) | Added; the existing AIUC-1 entry (`assurance-over-ai-19`) and platform-bundled SOC entries (`-13` to `-15`) are a different change | `-17` (B, piloting) |
| soc new-02 Kaufman Rossin pairs AI governance advisory with its SOC practice (B) | Added; overlaps `assurance-over-ai-13` and `-18` but the new element is the SOC pairing and the independence boundary | `-18` (B, in-production) |
| Routed: Baker Tilly expanded Fieldguide use (search-only) | Module text only, labelled search-only | none |
| Routed: SOC 2 platform reliance, ethics with tool providers (private-company-governance) | Already covered (`-12`, `-13`, `-14`, §6) | none |

### assurance-over-ai (24 -> 27 entries)

| Research item | Action | Result |
|---|---|---|
| aoai new-01 MSCI agent-evaluation attestation handed to SOX auditors (B) | Added (larger public-company example; notes say why it is kept) | `-25` (B) |
| aoai new-02 AIUC developer-versus-deployer matrix (C) | Added; scoping by responsibility split is not in `-12` | `-26` (C) |
| aoai new-03 CPA audit package for AI-generated analysis (idea, D) | Added; assurance over AI output is not covered by `-01` to `-24` | `-27` (D, idea) |
| Routed: Prager Metis argument (ATODAY-DAVIS-2026) | Module §9 objection only (not in YAML) | none |
| Routed: practice aid part 1 (entity's AI use, acceptance, service-organisation evidence) | Already in `-01`, `-03`, `-07`; module §6 and new §10 extended | none |

## 2. Sections added or extended

Each module now has a **§10 Mid-market firms** section (Sources moved to §11; contents list and §-references updated):
- quality-management: peer review as the inspector on the 2026 clock (SQMS 1, Yellow Book); no public AI
  peer-review finding (Tennessee 2025 data, Reviewer Alert titles, Peer Review Conference listing); readiness
  (CPA.com 54-firm survey, UK mid-tier study); tools arriving with methodology; ownership (PE, APS, PCAOB focus,
  PEEC timeline); four probes. Also extended §1, §3, §5 (pointer), §7, §8 (AuditFile, Pioneer Program, PE deals,
  PEEC draft, 15 Dec 2026 evaluations), §9 ("PE gives us money for AI") and §11.
- soc-attestation: small-firm quality pressure (platform referral networks, peer review, Tennessee SOC data); AI
  assurance through SOC practices (Schellman; Sensiba and Baker Tilly as search-only leads); advisory and attest;
  three probes. Also extended §3 (`#17`, `#18`, coverage counts), §5 (40,000+ organisations, first AIUC-1 audit,
  Schellman survey), §6 (advisory independence; "certification" wording), §7 (first audit-firm SOC job posting found;
  the old "no audit-firm posting" sentence is replaced), §8, §9, §11.
- assurance-over-ai: Area 1 as the near-term work for private-company auditors (practice aid part 1; ASB and peer
  review); outside evidence (`#25`, `#26`); Area 2 at regional firms; two probes. Also extended §3 (`#25`-`#27`,
  coverage counts), §5 (AIUC control split, MSCI tests), §6 (51 pages; tests of controls alone), §7, §8, §9
  (Prager Metis, AI-risk-is-old-risk, MSCI CISO), §11.

Line counts: quality-management 291, soc-attestation 299, assurance-over-ai 285. To stay at or under 300 lines
without dropping facts, the list items in §4, §8 and §9 of each module are now one line per item instead of
hard-wrapped, and the new §10 is written the same way; no wording was removed except the sentences the new evidence
replaced.

## 3. Grade changes

- `assurance-quality-management-14`: **D -> C** (maturity emerging -> announced). The new evidence (AuditFile
  QualityLink, vendor-announced, vendor claims only) is about the same change; firm use and AI root-cause analysis
  remain ideas and the notes say so.
- No other existing grade changed. No entry is grade A: no figure is reported as measured by the named
  organisation (the Plante Moran and MSCI figures are vendor-published).

## 4. Source keys

Archetype keys were used where the research used a different key for the same document:
AICPA-AIPA-2026 -> AICPA-PA-2026 (QM) / AICPA-PA (assurance-over-ai, as that file already uses);
AICPA-AIPARES-2026 -> AICPA-AIPAID-2026; CFODIVE-AIPA-2026 -> CFODIVE-AICPAPA-2026; JOFA-PEER-2026 -> JOFA-PRB;
JOFA-FAST-2026 -> JOFA-FAST; PEEC-APS-2026 -> JOFA-PEEC-2026; PEEC-APS-2025 -> JOFA-PEED-2025; AT-PEIND-2026 ->
AT-PEEC-2026; JOFA-ETHICSAI-2026 -> JOFA-ETHAI-2026; JOFA-CYBERCHK-2026 -> JOFA-CHECKLIST-2026; OATH-SITE-2026 ->
OATH-2026; AICPA-AIUC-2026 (JofA article) -> JOFA-AIUC-2026; AIUC-SITE-2026 -> AIUC1-SITE-2026.
New key: AIUC-SCHELLMAN-2026 for the AIUC-hosted copy of the Schellman release with the 2 Apr 2026 update (the
research called it SCHELLMAN-AIUC1-2026, which the archetype already uses for the Schellman-hosted page).
AICPA-REVALERT-2026 is reused for the Reviewer Alert series; the QM entry points to the September 2026 edition
download, the soc-attestation entry to the landing page. Every bracketed key in the three modules resolves to the
module's YAML or to its "Not in the YAML" list (with URL).

## 5. Gaps

- **Count targets.** quality-management (28) and assurance-over-ai (27) now exceed the 25-entry target, and both stay
  below 50% A/B (36% and 26%); validate.py reports these as warnings. The new mid-market evidence is mostly ideas,
  vendor announcements and one job posting, so it cannot raise the A/B share. A later pass could fold `-27`
  (assurance-over-ai, an idea from mathematics) into the module text if the cap matters.
- **ARCHETYPE.md** module table counts (and any `sources.md` additions for the new keys) were not updated; those files
  were outside this brief.
- **Not used:** STATE-PR-2025 (search-only peer review figures; the research said not to use them as proof points);
  AT-ACCAETH-2026 (global ACCA survey, not mid-market); JOFA-AIPA-2026 and CPAPA-AIPA-2026 (duplicate coverage of
  the practice aid); routed items for acceptance-independence, planning-risk-assessment, substantive-testing,
  benefit-plan-audits, nonprofit-government and private-company-assurance (other modules).
- **Evidence gaps carried from the research:** practice aid text is member-only; no AI-related peer-review finding
  is public, and Reviewer Alert article text was not read; no mid-market CPA firm is named delivering the joint SOC 2
  plus AIUC-1 offering; Sensiba's AIUC-1 accreditation and Baker Tilly's Fieldguide expansion are search-only; PCAOB
  statements come through Accounting Today; whether the Crowe and Eide Bailly deals closed was not checked; the
  outcome of PEEC's October 2026 meeting was not found; no error rate, override rate or parallel-run result for AI at
  any mid-market firm exists.
