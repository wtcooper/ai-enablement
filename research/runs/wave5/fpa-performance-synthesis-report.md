# Synthesis report: advisory / fpa-performance

Run 2026-10-21 (sources checked 2026-10-20, the research run date; `last_reviewed` is set to that date to match the
sibling advisory modules). Outputs:

- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/fpa-performance.md` (about 285 lines, TOC at top)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/fpa-performance.yaml` (14 entries; loads with `yaml.safe_load`; `scripts/validate.py` reports 0 errors and one warning for this file, see Gaps)

## Counts in and out

- In: 16 candidate entries from `adv-fpa-performance-combined.md` (0 A, 2 B, 13 C, 1 D). The landscape and the two
  cross-cutting files added no new fpa-performance entries; the independence file proposed one fractional-CFO
  candidate, which belongs in client-accounting-services (see Routing).
- Routed in from other wave 5 files and absorbed into existing entries (no new entries): Citrin Cooperman / Rosetree
  (into `-09`), Rillet partnership postings (into `-12`), Aprio FP&A posting (into `-03` and module §7), S&P Global GP
  survey and Grant Thornton PE AI survey (into `-08` notes and module §5), the "clients self-prepare with AI" view
  (module §9). The CAS discourse and risk-controls discourse routes are already covered by `-02`, `-10` and `-02` (KPMG
  forecast-accuracy figures).
- Out: 14 entries (0 A, 2 B, 11 C, 1 D).

| New id | From candidate | Grade |
|---|---|---|
| -01 | 01 + 11 (merged) | C |
| -02 | 02 + 16 (merged) | B |
| -03 | 08 | C |
| -04 | 15 | C |
| -05 | 03 | B |
| -06 | 14 | C |
| -07 | 09 | C |
| -08 | 12 | C |
| -09 | 05 (+ Rosetree) | C |
| -10 | 04 | C |
| -11 | 06 | C |
| -12 | 07 (+ Rillet postings) | C |
| -13 | 10 | C |
| -14 | 13 (idea) | D |

## Duplicates merged

1. **01 + 11.** Both describe AI drafting reporting narrative and KPI views for a reviewer. Merged; all sources kept.
   The bookkeeping-based package and ledger dashboard part already lives in advisory-client-accounting-services-06,
   so `-01` cross-references it and keeps only the planning-model and board-reporting layer.
2. **02 + 16.** Both describe a machine baseline forecast that a person adjusts (Jirav in firms; ML forecasting in
   planning platforms). Merged; grade B kept from the Jirav named deployment. Candidate 02 was tagged `process`;
   the merged entry is `step` because only the baseline-building step changes (Jirav says driver-based models remain
   for some clients). The CAS 13-week forecast stays in advisory-client-accounting-services-07.
3. Considered and kept separate: 03 (agents inside the planning platform) and 14 (governed data pushed to general
   assistants through MCP) differ in who uses them and the runtime; 13 (forecast validation idea) is cross-referenced
   to advisory-risk-controls-21 and advisory-client-accounting-services-21 rather than merged, because it covers
   forecast back-testing, not controls before agents go live.

## Corrections made while editing

- `-01`: candidate 11 said Bourke stated AI "can quickly find a variance and suggest an explanation". The article
  says "Think how quickly Claude or ChatGPT could find a variance ... and probably come up with an explanation". The
  modal verbs are restored (checked against ACCTODAY-CASKEYS-2026).
- `-11`: the CPA Practice Advisor statement that AICPA had not published SOC guidance on AI is marked as apparently
  superseded, per JOFA-PRACTICEAID-2026 (conflict logged in the independence file).
- Role-evolution sentences without a source were rewritten or sourced: `-05` (ONESTREAM-FPAWEBINAR-2026), `-07`
  (unsourced claim about consultant roles replaced by RSM's stated pitch), `-10` (Abacum's "practitioners in the loop"
  line traced to ABACUM-CFGI-2026), `-11` and `-12`.
- `-13`: added the contingent-fee rule (SEC 2-01(c)(5); NYSSCPA description of the AICPA Code) from the independence
  file, since the entry is priced on outcomes.
- Ref normalised: `SEC-REGSX-2026` renamed to `SEC-RULE2-01-2026`, the key the other advisory modules use for the same
  regulation.

## Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | -06, -09, -11, -14 | | |
| augment | -01, -02, -05, -07, -08 | -03, -10 | -12 |
| automate | | -04 | |
| delegate | | | -13 |

- Every ladder level and every change scope has at least one entry, but the top of the ladder is thin: automate and
  delegate have one entry each, both C and `announced`.
- No evidence for: automate at step scope; delegate at step or process scope (no firm runs an agent that owns a
  forecast or close-to-board-pack outcome); assist at process or model scope. None was invented.

## Grade mix

- A 0, B 2 (`-02` Jirav named firms, vendor release, 2024; `-05` Cox Enterprises in-house, vendor-presented
  figures), C 11, D 1 (labelled idea).
- 14% A/B, below the validator's 50% target. This is honest: no advisory firm published a measured outcome, the only
  named-firm figures are a 2024 vendor release, and the Cox figures are in-house and vendor-presented. Vendor
  benchmarks were not graded A; webcasts and event pages already held were not used to support A or B.

## Gaps

- No measured outcome (error, edit or override rate, parallel run, forecast accuracy, cycle time) from any
  accounting or advisory firm for AI-assisted FP&A, budgeting or performance work.
- Independent FP&A-specific evidence is one Gartner ranking with no percentages; academic evidence is adjacent
  (SME bookkeeping, LBO modelling).
- AICPA Code text for private-company attest clients not read; whether specific FP&A, CPM or managed scopes count as
  financial information systems design or management functions not analysed.
- No community, practitioner-forum or conference-session content specific to FP&A (ENGAGE titles only).
- Performance-improvement work has one C entry; no mid-market firm describes an AI-assisted engagement.
- The validator target of 15-25 entries is missed (14). The brief asked for 12-20; going to 15 would have meant
  splitting a merged duplicate or inventing an entry.

## Routed to other modules (from this module's inputs)

- **client-accounting-services:** fractional and interim CFO demand (interim CFO demand up 14% per Business Talent
  Group, CFODIVE-FRACTIONAL-2026); the independence file's proposed "fractional CFO with AI-built dashboards, hourly
  billing" candidate (CFODIVE-FRACTIONAL-2026; SEC-RULE2-01-2026 (c)(4)(vi)), which fits advisory-client-accounting-services-08;
  client-run close and reconciliation agents (BlackLine Verity Prepare GA July 2026, FloQast, Microsoft reconciliation
  agent in preview, Workday close agent announced; CPAPA-AGENTSCLOSE-2026); SME bookkeeping field evidence
  (STANFORD-JAR-2026); bookkeeping-based reporting packages (JOFA-CASAI-2026).
- **risk-controls:** the five-controls checklist for client AI agents and COSO's generative AI guidance as an advisory
  service (CPAPA-AGENTSCLOSE-2026; COSO-GENAI-2026); `-14` stays here only as an idea.
- **assurance archetype (and risk-controls):** AICPA and AIUC joint SOC 2 plus AIUC-1 engagement, 2026-10-19
  (JOFA-AIUC-2026); Grant Thornton Enterprise Assurance Services (GT-EAS-2026).
- **transactions:** frontier LLM accuracy on LBO modelling (SSRN-VIDAL-2026, cited here only as quality evidence in
  `-07`); Forvis Mazars quality-of-earnings article (FORVIS-QOE-2026).
- **valuation:** Kim, Muhn and Nikolaev on LLM earnings prediction (SSRN-KMN-2024, search-only; note the transactions
  module flags the arXiv version as withdrawn).
- **professional-services:** firm quality control for AI-assisted deliverables (CITYAM-DELOITTE-2025); PE and APS
  context for CFGI (Carlyle and CVC) and the independence split (ABACUM-CFGI-2026); outcome-based commercial
  structures (ISG-FAOFPA-2026); junior-talent pipeline data (INTUIT-ACCTTECH-2026; KARBON-AISTATE-2026).
- **tax:** Withum's expectation of complete automation of the tax process, as a competitive signal
  (ACCTODAY-CASKEYS-2026).

## Ref inconsistencies across wave 5 files (for the ref registry)

- SEC Rule 2-01: `SEC-REGSX-2026` (fpa research) vs `SEC-RULE2-01-2026` (elsewhere). Normalised to the latter here.
- AICPA ethics article of 2026-08-05: `JOFA-ETHICSAI-2026`, `JOFA-ETHAI-2026` and `JOFA-ETHICS-2026` all appear in
  finished advisory files. This module uses `JOFA-ETHICSAI-2026`.
- `RSM-MMAI-2026` points to two documents: the newsroom release (2026-07-21, used here) and the survey introduction
  page (used in transactions). They should get separate refs.
- PEEC APS article: `JOFA-PEEC-APS2-2026` vs `JOFA-PEEC2-2026`; Bloomberg pricing article: `BBLAW-PRICING-2026` vs
  `BLOOMBERG-PRICING-2026`; Deloitte Australia refund: `CITYAM-DELOITTE-2025` vs `CITYAM-DELOITTEAU-2025`.
- `COSO-GENAI-2026`: this file uses the COSO page (2026-02-23); the CAS YAML uses a hosted PDF (2026-02).
- Thomson Reuters Future of Professionals figures differ between the cross-cutting files (77/5/31 vs 78/6/32); not used
  here.

## Suggested improvements to the briefs

1. Give module researchers a shared ref registry (or a check script) so the same document gets one key; seven
   collisions or splits turned up in this module alone.
2. Ask researchers to quote the modal verb of any forward-looking or hedged statement in `measures` or the solution;
   the one drift found here was a "could ... probably" turned into "can".
3. Require a source ref in every `role_evolution` sentence at research time; five entries needed repair.
4. For thin modules, set the validator expectation to the brief's target (12-20) and allow a lower A/B share with a
   stated reason, so the warning does not push editors to split or pad.
5. Ask for a "who measured it" column for every survey figure, and the subgroup for subgroup figures (the RSM 53% and
   47% are for organisations with moderate or limited pilot success, not all respondents).
6. Name the overlapping finished entries in the brief (here CAS-06, -07, -08, -20, -21) so researchers do not
   reproduce them.
