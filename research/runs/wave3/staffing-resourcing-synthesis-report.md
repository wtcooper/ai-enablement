# Synthesis report: professional-services / staffing-resourcing

Prepared 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/staffing-resourcing.md` (285 lines, contents table)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/staffing-resourcing.yaml` (21 entries; `scripts/validate.py` passes with the expected A/B-share warning)

## Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| ps-staffing-resourcing-practice.md | 17 | B 3, C 13, D 1 |
| ps-staffing-resourcing-discourse.md | 15 | B 3, C 11, D 1 |
| ps-staffing-resourcing-governance.md | 13 | B 4, C 4, D 5 |
| Routed in from other ps-*.md files | 3 named deployments added to existing entries (Nextview, Diabsolut, zeb) | n/a |
| **Total in** | **45** | B 10, C 28, D 7 |
| **Out** | **21** | A 0, B 6, C 12, D 3 |

## Duplicates merged (P = practice, Dc = discourse, G = governance)

| Out | Merged from | Note |
|---|---|---|
| 01 shortlists in PSA/workflow tool | P01, P02, Dc01, Dc11, G01 + routed Nextview, Diabsolut, zeb | WK CCH Axcess (accounting) and BigHand preview (law) folded in as product examples |
| 02 McKinsey | P04, Dc02 | Kept apart from 01: firm-built, central staffing team, announced only |
| 03 demand documents to roles | P09, Dc04 | Email/portal intake and SOW-to-assignment are one change |
| 04 rolling forecast | P07, Dc05, Dc13, G02 | Accounting busy-season forecasting folded in |
| 05 staffing scenarios with margin | P08 | |
| 06 reallocation of work in flight | P05, Dc03, G06 | |
| 07 bench detection | P06, Dc07 | |
| 08 utilisation monitoring | P13, G09 | G graded it D (idea); product descriptions exist, so C |
| 09 conversational assistant | P11 | |
| 10 skills inventory | P14, Dc06, G03 | G graded D; product descriptions exist, so C |
| 11 matching across externals | P15 | |
| 12 central resourcing, opportunity boards | P03, P16, Dc10, Dc12 | Deutsche Telekom pool, project marketplace, law-firm platform, Reed Smith |
| 13 automated assignment (Peru) | P17, G04 | |
| 14 suggested completion dates (Peru) | G05 (figure also inside P17) | Distinct change: nudge with manager kept |
| 15 one professional with AI vs pair | G12 | |
| 16 agents as capacity | P10, Dc08, G07 | |
| 17 flexible talent | Dc14 | |
| 18 in-house insourcing | G13 | change_scope set to model (sourcing) |
| 19 outcome-aware staffing (idea) | P12, Dc09, G08 | Dc graded C; no deployment, so D |
| 20 freed-capacity check (idea) | Dc15, G11 | |
| 21 allocation controls (idea) | G10 | |

24 duplicate candidates removed by merging (45 in, 21 out).

## Coverage

- **Ladder:** assist 7, augment 13, automate 1, delegate 0. **Delegate: no evidence.** Every agent read proposes or
  recommends; zeb's agent pre-books, but no source describes an agent owning a staffing outcome. **Automate** has one
  entry, an optimisation algorithm in a Peruvian public agency (adjacent, not AI in the generative sense), which did
  worse than managers.
- **Change scope:** step 10, process 8, model 3. Model entries (16, 17, 18) rest on announcements, a podcast and an
  expectations survey.
- **Firm kinds:** consulting and implementation (01, 02, 03, 04, 05-09, 11), law (01 preview, 12, 17, 20), accounting
  (01 CCH, 04, 17), in-house legal (18, 20), telecom group with consulting arms (12), adjacent non-firm evidence (13,
  14 public agency; 15 consumer goods).

## Grade mix and grading decisions

A 0, B 6 (29%), C 12, D 3. Below the 50% A/B target; not inflated. No grade A: no named organisation reports a measured
AI staffing result. Four of the six B entries are capped: 12 (law-firm platform not described as AI; Reed Smith AI use
is a 2023 announcement), 13 and 14 (independent RCT, adjacent public-sector process), 15 (independent RCT, consumer
goods). 01 and 04 are B on named deployments with vendor-published figures only.

## Source-key normalisation

Same document, same key, aligned with finished modules: KANTATA-STATE-2026 / CPAPA-KANTATASOPS-2026 facts cited as
KANTATA-SOPSI-2026; DELTEK-SPIBENCH-2026 (two different documents across dives) split into DELTEK-SPI-2026 (benchmark
article) and DELTEK-SPIKPI-2026 (5 KPIs article); IPA-PERU-2026 = FERREIRA-PERU-2026; BLOOMBERGLAW-MCK-2026 =
BLOOMBERGLAW-MCKINSEY-2026; BLOOMBERGLAW-BILLABLE-2026 = BLOOMBERG-AICOST-2026; CERTINIA-PROVING-2026 =
CERTINIA-CUSTOMERS-2026; AIACT-ANNEX3-2024 = EU-AIACT-ANNEX3-2024; TRI-TEAMS-2025 = TRI-HUMANAGENT-2025;
ICO-AIRECRUIT-2024 = ICO-RECRUIT-2024; ILGA-HB3773-2024 = ILLINOIS-HB3773-2024; NYC-LL144-2023 = NYC-AEDT-2023.
The two Rocketlane URLs (blog. and bare domain) were unified. The McKinsey article is recorded as `full` with a
paywall locator; the discourse dive had recorded it as search-only (grade C either way).

## Gaps

- No grade A; no override, acceptance, error or parallel-run figure for any AI staffing tool.
- No law-firm AI staffing deployment beyond Reed Smith (2023) and a BigHand preview; no Big Four, Accenture, BCG or Bain
  primary material; McKinsey rests on a paywalled opening.
- Non-legal in-house shared services, and A&E staffing beyond Deltek's survey, not covered.
- Full texts not read: SPI 2026 reports, Kantata State of the Industry report, Dayshape report (Onrec summary only),
  ISQM 1 (search-only).
- Scope of NYC LL144, Illinois HB 3773, Colorado SB26-189 and EU Annex III 4(b) over work assignment unresolved.
- Bias in law-firm work allocation (ABA, MCCA studies) seen in search but not opened.

## Routed to other modules (from the three staffing inputs)

- **talent-learning:** Aderant talent evaluation agent (LEGALIT-ADERANT-2026); manager skills for hybrid teams
  (KANTATA-RMI-2026); stretch assignments for juniors (PROJECTWORKS-2026); associate hiring and pyramid (BLOOMBERGLAW-BAKER-2026;
  TRI-LAWYERDEV-2026); associates choosing billable work over AI-training credit (GEEK-LATITUDE-2026); Canaries
  employment trend and junior bifurcation (STANFORD-CANARIES-2026; NBER-AUTOR-2026).
- **delivery-management:** project health monitoring, PMO, project-manager and handoff agents, role briefs for new
  joiners (CERTINIA-VEDA-2026; KANTATA-AGENT-2026; SDTIMES-PLANVIEW-2026; KANTATA-SUPERAGENT-2026); Rocketlane
  Timesheet Policy Agent (ROCKETLANE-2026).
- **billing-collections:** automated and calendar-based time capture feeding utilisation actuals (CERTINIA-VEDA-2026;
  KANTATA-SUPERAGENT-2026; DELTEK-DELA-2026).
- **scoping-pricing:** estimate and SOW agents (CERTINIA-VEDA-2026); outcome-based pricing effects (KANTATA-RMI-2026;
  UNITEAI-KANTATA-2026; TRI-FOP-2025; TR-FOPLAW-2026); Australian requirement that suppliers declare planned AI use in
  quotes (CANBERRATIMES-APSAI-2025); hourly-fee rule (ABA-OP512-2024).
- **pursuit-proposals:** Kantata Sales Accelerator (KANTATA-ENGINE-2025); CV and proposal generation (CINODE-2026);
  capacity-aware bid/no-bid (DAYSHAPE-ONREC-2026).
- **client-development:** RFP buyers asking how firms use AI to reduce cost (UNITEAI-KANTATA-2026).
- **knowledge-management:** expert judgment and "expertise compounding" (KANTATA-SUPERAGENT-2026; KANTATA-ENGINE-2025;
  UNITEAI-KANTATA-2026; KANTATA-BASWARE-2026).
- **firm-finance:** Certinia's 1% utilisation to 1.5% EBITDA claim (CPAPA-CERTINIA-2026); costing agents
  (SDTIMES-PLANVIEW-2026); COO roundtable measurement gap (WESTERNALLIANCE-COO-2026); leverage and rates
  (TRI-LFFI-Q2-2026; BLOOMBERG-AICOST-2026).
- **acceptance-risk:** in-house intake triage (DOCUSIGN-LEGALOPS-2026); client AI bans (TRI-LEGALWEEK-2026).
- **quality-review:** SRA warning notice, 42 reports (LAWSOCIE-SRAWARN-2026); supervision text (CALBAR-GENAI-2026).
- **assurance archetype:** ISQM 1 resource requirements (IAASB-ISQM1-2020, search-only).

**Inbound items routed to staffing-resourcing:** picked up Nextview, Diabsolut and zeb staffing agents
(CERTINIA-CUSTOMERS-2026; NTTDATA-ZEB-2026) into 01; Kantata/RMI, Certinia agents, Deltek and EU AI Act items were
already covered. Not used: Laurel-Dayshape time-to-utilisation link (LAUREL-DAYSHAPE-2026), Laurel Signal staffing
forecasts (LAUREL-SIGNAL-2026), blended-workforce commentary (CONSULTANCYUK-BONE-2026), Stinson and Projectworks bid-team
matching (STINSON-LAW360-2026; PROJECTWORKS-BD-2026), and Arup/Neudesic expert finders (IKAUN-ARUP-2026,
IKAUN-NEUDESIC-2026): each arrived as a one-line routing note without enough detail or an AI claim to stand as an entry.
A future pass could open them.

## Cross-references used instead of duplicating

professional-services-delivery-management-01, -04, -05, -07, -14, -16; professional-services-talent-learning-04, -11,
-12, -19, -20; assurance-planning-risk-assessment-22 and assurance-quality-management-11 (RSM Luca Resourcing);
assurance-soc-attestation-01 (scheduling concurrent audits; not cited in the module). No tax or security entry overlaps.

## Suggested improvements to the briefs

1. Ask deep-dive agents to reuse source keys from finished modules (give them a key index); about a dozen keys needed
   renaming here, and DELTEK-SPIBENCH-2026 named two different documents.
2. Require routed items to carry a source row (title, URL, date, locator), not just a key, so the target synthesis can
   use them without reopening the other dive.
3. State the grade cap for adjacent evidence (non-firm or non-AI) in the vocabulary, not only in notes; three dives
   applied it independently.
4. Ask the governance angle to propose fewer D "idea" entries that restate a regulation; fold control sets into one
   entry per module.
5. Add a check that `access: full` is not used for paywalled pages read only in part, or define a `partial` value.
6. Note in the vocabulary that interview-probe questions are not quotations (the quote-length check flags them).

Other module issue seen, not touched: `modules/client-development.md` is 303 lines and fails the validator.
