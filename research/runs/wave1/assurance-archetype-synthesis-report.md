# Archetype synthesis report: assurance

- **Archetype:** assurance (extends professional-services, not yet written).
- **Written:** 2026-10-17. **Output:** 11 archetype-level files in
  `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/` (1,823 lines in
  total). Module files and use-case YAML were read and linked, not edited.
- **Inputs read:** `landscape-assurance.md`; the five cross-cutting files (economics-business-model, workforce-talent,
  guardrails-regulation, state-of-ai-disruption, data-evidence-acquisition); the nine wave 1 module synthesis reports
  and the pilot controls-testing synthesis report (gaps and routed sections); all ten module files (header, scope and
  process sections in full, other sections skimmed); `method/onboarding.md` (stage names, gates, delegation decision)
  and the headings and question banks of the other method files.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. Its 8 warnings are pre-existing: SKILL.md is missing,
  and seven module YAMLs fall below the 50% A/B target.
- **Source keys:** 159 distinct keys are cited. 126 that are used in two or more files (or in ARCHETYPE.md) are listed in
  `sources.md` Part B; the other 33 sit in the Sources list at the end of the one file that cites them. A script
  checked that every bracketed key resolves and that every relative link and in-file anchor works.

## 1. What each file draws on

| File | Lines | Main inputs | Notes |
|---|---|---|---|
| `ARCHETYPE.md` | 99 | Landscape §1, §10, §11; onboarding §4-§5; module headers; validator A/B counts | Module table gains an evidence column (strong ≥50% A/B; moderate 30-49%; thin <30%, adjusted for named practice) plus a note to use thin modules for risk awareness and probes. Stage markers are rewritten from landscape §11 to match the onboarding stage names and gates. The delegation reference case is controls-testing `#05`, worded to match what that entry actually shows |
| `interview-guide.md` | 194 | Onboarding §3 and §5; the probes in the cross-cutting files' §3.2; module scope sections; landscape vocabulary | Adds a role table, assurance wording for the profile questions, a module-detection table, ten boundary probes, questions for each phase, internal audit variants, sensitive topics, and vocabulary (21 terms) with words to avoid |
| `value-chain.md` | 207 | Module §2 tables (summarised to process level); data-evidence-acquisition file; landscape module check | Stages 0 and 7 are marked as inherited from professional-services. §4 is the archetype home of the data and evidence acquisition layer, which has no module. §6 maps the internal audit chain; §7 shows where work types cluster, for Diagnose |
| `economics.md` | 200 | Economics file (nearly all); workforce file (leverage, partner pay); state-of-ai file (pricing); data file (SOX hours) | Firm revenue table, FERF and FRC fee benchmarks, CPA.com metric shares, leverage, technology commitments, private equity, AI pricing pressure, internal audit budgets, metric table |
| `state-of-ai.md` | 153 | State-of-ai file; landscape §6-§9; guardrails file (CPAB finding, IFIAR 2026) | Dated 2026-10-17. Keeps measured, announced and forecast apart. Covers the IFIAR 2023-2024 table, the CPA.com benchmark, internal audit surveys, the firm platform table, maturity tiers and client-side maturity |
| `frontier.md` | 106 | Frontier tables in the landscape and in all five cross-cutting files | 29 dated, sourced signals in four themed tables, each with what it means for a leader. Adds a calendar of scheduled dates and a labelled list of forecasts |
| `guardrails.md` | 191 | Guardrails file (most); data file (AS 2310, AS 1105.10A, ED-500); landscape R-rows | Bodies table, standards with dates, inspection focus, documentation, confidentiality, EU AI Act, independence, liability, a human-judgment table and pre-plan checks. Tool governance detail is left to the quality-management module |
| `workforce.md` | 180 | Workforce file (most); economics file | Roles table, pyramid and leverage, pipeline and licensure, intake, firm forecasts, skills, the apprenticeship question with design options, attrition table, internal audit |
| `disruption.md` | 173 | State-of-ai file §2.4-§2.8; economics file; guardrails file §2.9 | Seven scenarios, each with evidence, forecasts (with who made them), signals and a question. Ends with a service-line exposure table tied to Frame question F15 |
| `objections.md` | 89 | Objection tables in the five cross-cutting files | 28 cross-cutting objections in six groups. Step-specific objections are left in the modules |
| `sources.md` | 240 | Landscape §2-§9 and §15; source tables in the cross-cutting files | Part A covers the landscape by type plus where evidence is thin. Part B holds the shared keys. Carries `last_researched: 2026-10-17` |

## 2. Gaps

**Evidence gaps that run across the archetype (carried from the inputs):**
- No independent accuracy, error, override or parallel-run result exists for any audit AI tool in live use. No measured
  change in hours, fees, staffing mix or margin caused by AI exists at any firm.
- Pricing evidence is thin. The only audit-fee case is the KPMG and Grant Thornton UK episode, known only through trade
  retellings (the FT original is paywalled). No firm leader has said publicly how audit pricing will change, and no
  network publishes margin, realization or leverage.
- Smaller firms: the only data is one 54-firm US benchmark, which its authors call unrepresentative. No non-US
  equivalent was found.
- Workforce: no audit-specific measure of skill formation under AI; offshore headcount only for KPMG UK (relayed); no
  Big Four posting for new AI roles found.
- Guardrails: no audit regulator text applies GDPR to audit AI tools; no official view on whether audit tools are
  high-risk under the EU AI Act; PCAOB primary pages and the AICPA practice aid text were not read in the inputs.

**Gaps in the files written:**
- Some landscape conference entries in `sources.md` point to organiser or press-release pages, not session lists (IIA
  International, World Congress, DCPA). The journal list was not re-verified.
- `frontier.md` signals are dated, but most forward-looking items are firm or vendor forecasts. They are labelled as such.
- Interview-guide phase questions are advisor-designed from the inputs' probes; they have not been tested with users.
- The professional-services base archetype does not exist yet. ARCHETYPE.md and value-chain.md name it without a link;
  stages 0 and 7 assume its content.
- `archetypes/index.md`, which onboarding §4 points to, does not exist yet. It was out of scope for this brief.

**Data conflicts and how they were handled:**
- The A/B share for acceptance-independence: the caller gave 14%, but the validator counts 4 of 21 (19%). Both are thin,
  so the label is unaffected, and ARCHETYPE.md prints no percentages.
- `NYSSCPA-BOTIC-2025` has two URLs across the inputs. The key is used for the Botic remarks article (1051584, juniors
  and scepticism). PCAOB private-equity remarks are cited to `CAALLEY-PCAOBPE-2025`, because the economics file's
  `AT-PCAOBAI-2025` has no URL.
- Modus (7 or 8 Apr 2026), Repodo and Fieldguide each had two URLs. The opened, full-access copy was used (Accounting
  Today, Crowdfund Insider, SiliconANGLE).
- EY assurance growth: 3.0% in local currency (EY release) is used, not 5.8% in US dollars.
- The CPA.com figure for firms using no AI is given as "a quarter to a third", because the report states both.

## 3. Routed items placed at archetype level

| Routed item (from) | Placed in |
|---|---|
| PE investment, fee pressure, AI-native entrants, junior skill erosion, graduate intake (acceptance-independence; substantive-testing; quality-management; planning cross-cutting rows) | economics §5-§7; disruption §2, §4; workforce §4, §5, §7 |
| Big Four AI hiring and "lifting the pyramid"; TRI 81% regular AI use; Gartner internal audit survey (substantive-testing) | workforce §2, §4, §6; state-of-ai §2 |
| Fee debate, including KPMG's AI fee argument (planning; quality-management; substantive-testing) | economics §7; disruption §4; objections §3 |
| Client AI-governance maturity (CAQ 6% advanced), which acceptance-independence did not use (acceptance-independence; completion-reporting) | state-of-ai §5; frontier §5; disruption §7 |
| EY Canvas scale figures (completion-reporting; sustainability-assurance cross-cutting context) | state-of-ai §3; frontier §3 |
| Modus staff co-authoring FinancialAuditBench (substantive-testing) | state-of-ai §6; frontier §3 (flagged as unconfirmed) |
| SEC filer-status proposal and 404(b) (assurance-over-ai, as business-model lens) | disruption §6; frontier §5; interview-guide Frame |
| Landscape module-check recommendation 4: a cross-cutting data and evidence acquisition theme | value-chain §4 |
| Landscape module-check recommendation 8: business model and workforce as a lens, not a module | economics; workforce; disruption |

**Not placed:**
- PwC Australia AI-native audit trial. It is already in planning-risk-assessment via controls-testing CT-17, and the
  cross-cutting inputs gave no URL.
- FEDYK-2022 (abstract only).
- GARTNER-AUG-2026 (snippet).
- The KPMG-Anthropic alliance (search-only; advisory, not audit).
- Items the module reports send outside the archetype: preparer-side sustainability tools, and SOC report use by
  vendor-risk teams.

## 4. Suggested module changes

Items routed between modules that the target module still lacks. Each was checked by searching the module text.

1. **substantive-testing:** add the CPAB December 2025 inspection finding (a tool used as primary evidence, limited input
   validation, low-risk items untested) [CPAB-EVOLVING-2025], routed from quality-management. Also point to
   `value-chain.md` §4 for data acquisition, since no module owns it.
2. **sustainability-assurance:** add the AICPA ASB attestation exposure draft (new AT-C 325 and 330, proposed effective
   for engagements beginning on or after 15 Jun 2029) [CPAPA-ASB-2026], routed from soc-attestation.
3. **acceptance-independence:** add the IESSA lines on reporting software and management responsibility (5606.4 A3,
   R5606.6, 5400.20 A3), routed from sustainability-assurance. They apply to firms selling AI reporting tools.
4. **specialists:** add Deloitte UK's automated impairment modelling, which found calculation inaccuracies across ten
   consumer entities (DELOITTE-UKTR-2025), routed from quality-management.
5. **controls-testing:** add the CAQ material on "invisible AI" and "shadow AI" in ICFR and its six audit committee
   questions (CAQ-ACI-2026-08, CAQ-ACI-2026-03), routed from completion-reporting.
6. **quality-management:** record the conflict between Board Agenda ("none of six firms monitored tool impact") and the
   module's "0 of 6 quantified quality impact". Line 274 also mentions "the synthesis report" and "the pilot's keys",
   which should not ship.
7. **All modules:** use the archetype's canonical keys (IFIAR-TTF-2026 rather than IFIAR-TTF26, CPACOM-ATR-2025 rather
   than CPACOM-ATR, AICPA-PA-2026 rather than AICPA-PA, FRC-GENAI-2026 rather than FRC-GENAI), so one key resolves
   across files.
8. **Thin modules** (acceptance-independence, specialists, completion-reporting, sustainability-assurance): consider a
   short "how to use this module" line that matches the ARCHETYPE.md note (risk awareness and probes, not proof points).
   Several already say something close.
