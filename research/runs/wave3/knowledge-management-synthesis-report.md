# Synthesis report: professional-services / knowledge-management

Prepared 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/knowledge-management.md` (287 lines, table of contents)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/knowledge-management.yaml` (23 entries)

`scripts/validate.py`: 0 errors; the knowledge-management YAML reports 23 use cases, 14 graded A/B (61%). Every
source key cited in the module is in the YAML or the module's §10 (checked by script); every key named inside a YAML
entry is in that entry's sources. No downloads were needed; all inputs were local.

## 1. Counts in and out

| Input | Candidates |
|---|---|
| ps-knowledge-management-practice.md (P) | 16 (A 0, B 11, C 4, D 1) |
| ps-knowledge-management-discourse.md (D) | 17 (A 0, B 2, C 12, D 3) |
| ps-knowledge-management-governance.md (G) | 15 (A 0, B 4, C 11, D 0) |
| Routed in from other deep dives | 13 items (see §6) |
| **Total in** | **48 candidates + 13 routed items** |
| **Out** | **23 use cases** (A 0, B 14, C 8, D 1) |

No candidate was dropped. Six were folded into an output entry for their knowledge-management part, with the rest
cross-referenced to a finished work-production entry (see §2).

## 2. Duplicates merged

| Out | Title (short) | Merged from |
|---|---|---|
| 01 | AI search over a curated precedent library | P01, D01, G01 (search part) |
| 02 | Ask questions of the firm's documents; clause finding in DMS or Word | P02, D02 |
| 03 | Consulting firm-wide assistant (Lilli, PairD, Infosys) | P03, D12, G11 |
| 04 | Expertise and experience location | P04, D07, G07, P15 (experience-record part); Intapp Celeste and ikaun Arup routed in |
| 05 | Bulk reclassification into a knowledge bank (Clifford Chance) | P05 |
| 06 | Classification and extraction at filing | D04 |
| 07 | Repository clean-up with human confirmation | P14 |
| 08 | Context graph | P12, D05 |
| 09 | Governed connections (MCP), agentic search, logged write-back | P06, D06, G01 (MCP part), G12 |
| 10 | Agents file work and update metadata (delegate) | G13 |
| 11 | Precedent database from deal history (Ropes & Gray) | P07 |
| 12 | Curated, owned collections as grounding set | D03, G03; KM-validation part of G04; reuse and sanitisation part of G02 |
| 13 | In-house knowledge base and legal operations | P08, G15; BLOOMBERGLAW-GCXAI-2026 routed in |
| 14 | In-house decisions as approved positions (Coheso) | D09 |
| 15 | Close-out capture and retrospectives | P09, D10, G08; delivery-management routing |
| 16 | Call and meeting transcripts as capture | G09 |
| 17 | Briefs for joiners and before client calls | P10, P11, D13; ERPTODAY-KANTATA-2026 routed in |
| 18 | KM teams curate AI know-how; gated rollout | P13, G06 (KM part), D11 (template-author role); LATHAM-INNOVATIONATTY-2026 routed in |
| 19 | Senior judgment and reviewer corrections for juniors | P16, G10, D14; JOFA-LEARN-2026 routed in |
| 20 | AI twins of individuals | D08 |
| 21 | Idea: tacit-knowledge elicitation and retirement capture | D16, D17 |
| 22 | Client-facing knowledge portal (Debevoise) | D15; BLOOMBERGLAW-DEBEVOISE-2026 routed in |
| 23 | Measuring the knowledge layer | G14, G05 (KM part) |

Cross-referenced instead of duplicated: G02 drafting from precedent (professional-services-work-production-05, -15);
G04 source-checking (work-production-01, -11); G05 firm test sets (work-production-23); G06 gated rollout
(work-production-22); D11 process templates (work-production-15); P15 proposal assembly (pursuit-proposals);
the NBER trial in 19 (work-production-06); Debevoise's priced offer in 22 (scoping-pricing-23).

**Source-key harmonisation.** JUDICIARY-AYINDE-2025 became EWHC-AYINDE-2025 (work-production key); ACCTODAY-AINATIVE-2026
became AT-AINATIVE-2026 (landscape and work-production key; date set to 2026); KANTATA-EXPERTISE-AGENT-2026 became
KANTATA-AGENT-2026 (same URL); LAWPUNX-2025 (client-development) became AL-LAWPUNX-2025; LAWSITES-LEGORAIM-2026 (LawSites
reprint) dropped in favour of LEGORA-IMANAGE-2026 (the original release). VALS-VLAIR-2025, CALBAR-GENAI-2026,
ILTA-TECHSURVEY-2026 and TR-FOP-2026 carry work-production's field values. **Key collision:** work-production uses
LAWSOC-AGENTIC-2026 for the Law Society explainer "What is agentic AI" (2026-10-19); the governance dive used the same
key for a different document, the report summary "The future of agentic AI in legal practice" (2026-04-14). This file
uses LAWSOC-AGENTICFUTURE-2026 for the report.

## 3. Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | 2 (01, 04) | 4 (12, 18, 21, 23) | 0 | 6 |
| augment | 8 (02, 03, 07, 09, 11, 13, 16, 17) | 6 (05, 08, 14, 15, 19, 20) | 0 | 14 |
| automate | 1 (06) | 0 | 1 (22) | 2 |
| delegate | 0 | 1 (10) | 0 | 1 |
| total | 11 | 11 | 1 | 23 |

- **Automate** rests on a NetDocuments private preview (06, grade C) and Debevoise's beta portal (22, grade B). No
  evidence for automate at process scope.
- **Delegate** has one entry (10), built on iManage and Harvey product announcements (grade C). The Law Society's
  guidance page reports its April 2026 report found no evidence of agentic AI currently used in legal practice.
- **Model** has one entry (22), a beta with about 10 clients and no reported result. No entry was invented to fill a cell.

## 4. Grade mix and grading decisions

Final: A 0, B 14 (01, 02, 03, 04, 05, 07, 11, 12, 13, 15, 17, 18, 19, 22), C 8 (06, 08, 09, 10, 14, 16, 20, 23),
D 1 (21, labelled "Idea"). A/B share 61%.

- **No A.** No named organisation reports a measured outcome for its own knowledge work. McKinsey's usage and "30% time
  saved" are self-reported, relayed second hand, with no method (B under the 2026-10-17 rule).
- **Raised by merging:** 12 rose from C (D03, G03) to B because Womble Bond Dickinson and McKinsey describe curation as
  their own practice; 22 rose from D (D15) to B on Debevoise's named beta; 15 is B on named firms' KMWorld Europe
  abstracts (D10), with Certinia agents (C) inside it.
- **Judgment calls to flag for the verifier:** 05 keeps maturity "announced" with grade B (Clifford Chance says 400,000+
  documents are already in the platform; use is not shown). 19 is B on Ascend's own description of a piloted feature
  plus adjacent measured trials (NBER 35720, NBER 31161); the discourse dive graded the Ascend part C because the speaker
  is the platform's CEO. NBER-AUTOR-2026 provenance is set to vendor-published to match work-production-06 (Google built
  the assistant); the governance dive had "independent".
- **Kept at C despite named firms:** 23 (Vals consortium firms are named, but that evidence is work-production-23's;
  no firm publishes knowledge-layer measures).

## 5. Gaps

- **No deployer quality data.** No error, override, search-success, parallel-run or permission-leakage result for any
  firm's knowledge base, search or expert finder. Measured figures are adjacent (Vals document Q&A, Stanford research
  tools, NBER trials) or vendor-run (Harvey Graph, NetDocuments benchmark).
- **No public test of ethical-wall inheritance.** Every vendor claims it; nobody publishes a test.
- **Consulting and accounting thin.** Consulting rests on McKinsey (primary pages blocked) plus KMWorld Europe
  abstracts (A&M, Simon-Kucher); accounting on one podcast (Ascend). BCG, Bain, Deloitte, EY, KPMG and PwC knowledge
  platforms were not reached. Engineering: Arup (via a vendor), AECOM and Buro Happold abstracts.
- **Vendor-hosted evidence.** Seven named-firm examples are iManage customer stories, undated; Harvey and Legora pages
  supply most of the rest.
- **In-house beyond legal.** Only Basware's services team and Digital Commerce Bank's legal and technology team.
- **No job postings for KM roles** other than Latham's innovation attorney posting (routed); APQC and iManage full
  reports gated.

## 6. Routed items picked up from other modules

| From | Item | Used in |
|---|---|---|
| ps-acceptance-risk-combined | Intapp Celeste surfaces matters, partner experience and pitch materials (INTAPP-CELESTEGA-2026) | 04 |
| ps-client-development-discourse | Firms sharing knowledge with clients via AI (LAWPUNX-2025, harmonised to AL-LAWPUNX-2025); "legal memory" ownership (BLOOMBERGLAW-GCXAI-2026) | 22, 13 |
| ps-client-development-practice | Latham capability catalogue (LATHAM-INNOVATIONATTY-2026) | 18 |
| ps-delivery-management-discourse and -governance | Certinia Retrospective Drafter and Knowledge Base agents; Kantata knowledge in handoffs (ERPTODAY-KANTATA-2026) | 15, 17 |
| ps-firm-finance-discourse | Partner-as-gatekeeper burden of a client-facing portal (BLOOMBERGLAW-DEBEVOISE-2026) | 22 |
| ps-firm-finance-practice | Kirkland's platform and Clifford Chance mention (BLOOMBERGLAW-KIRKLAND-2026) | Not used: work-production-21 holds Kirkland; Clifford Chance is 05 from primary press |
| ps-pursuit-proposals-practice and -discourse | Experience and CV databases (IKAUN-ARUP-2026; Gowling, GRSM) | 04 (Arup); bid-time figures left with pursuit-proposals |
| ps-quality-review-discourse | Citator and corpus quality (LAWSITES-FILEVINE-2026) | Not used: detail is citator verification, covered by work-production-11 |
| ps-staffing-resourcing-discourse and -practice | Kantata expertise compounding (UNITEAI-KANTATA-2026); Basware best-people idea; superagent and engine | 19 (Basware), 15 (engine), 9 objections (superagent); UNITEAI not used (vendor interview not read) |
| ps-talent-learning-discourse and -governance | Accounting training assistant (JOFA-LEARN-2026); curator rotations (TRI-AILAWPROF-JUNIOR-2026); knowledge extraction (VAULT-PYRAMID-2026) | 19; module §7 |
| ps-talent-learning-practice | Hogan Lovells Cadwalader pilot (LEGORA-HLC-2026); Ascend closed loop | 19 (Ascend); HLC left to work-production |
| ps-work-production-discourse and -practice | HLC knowledge-management agents (HARVEY-HLC-2026); Blank Rome brief bank; Horizon Scanning | Module §7 (HLC); brief bank and horizon scanning stay in work-production-17 and -04 |
| ps-delivery-management-discourse | Firm-level AI programme management, "no clear module" (TRI-PMO-ILTACON-2025) | Not used; nearest fit is 18, but the source is about PMO practice, not knowledge |

## 7. Routed to other modules (from the three knowledge-management inputs)

- **work-production:** precedent-grounded first drafts (LAWSITES-MSFT-2026; LEGORA-BMW-2026); Harvey review tables (HARVEY-INDEMNITY-2026); Vals benchmarks (VALS-VLAIR-2025). Already picked up as work-production-03 and -05.
- **pursuit-proposals:** proposal assembly from past engagements (Kantata Sales Accelerator, KANTATA-ENGINE-2025/-2026; Intapp experience-based pitch generation, INTAPP-EXPERIENCE-2026; Certinia RFP Responder, CERTINIA-VEDA-2026).
- **staffing-resourcing:** Kantata Expertise Agent ranked staffing recommendations; its 40% resource-planning accuracy claim is an unmeasured vendor figure (KANTATA-AGENT-2026); Certinia Resourcing agents; outcome data and hybrid teams (KANTATA-RMI-2026); EU AI Act treatment of AI for worker management (EC-AIACT-2026).
- **delivery-management:** Kantata portfolio-health monitoring; Certinia project assistant and PMO agents (KANTATA-AGENT-2026; CERTINIA-VEDA-2026).
- **talent-learning:** McKinsey on junior tasks (THEOUTPOST-LILLI-2025); NBER-AUTOR-2026; TR-FOP-2026 finding 07; Ascend interns (AT-AINATIVE-2026); Gilchrist Connell combined AI and knowledge officer (LAWYERSWEEKLY-GILCHRIST-2026); MCA training concern (MCA-SURVEY-2026); ILTA headcount intent (ILTA-TECHSURVEY-2026).
- **quality-review:** Vals benchmark design (VALS-VLAIR-2025); hallucination and verification evidence (STANFORD-MAGESH-2024; EWHC-AYINDE-2025; CTV-DELOITTE-2025); BCG experiment (BOERSEN-LILLI-2024); reviewer overload (AL-DIDOMENICO-2026); playbook review against institutional positions (LAWSITES-IMANAGE-2026; LAWSITES-SIMPLEDOCS-2026); sampling-based oversight (LAWSOC-AGENTICFUTURE-2026).
- **acceptance-risk:** ethical-wall management and conflicts (over 35% of Chaffetz Lindsey matters screened, IMANAGE-CHAFFETZ-2026; NYCBAR-OP2024-5-2024 pp. 3-4); Coheso and Legora intake (AL-COHESO-2026); client AI instructions at intake.
- **client-development:** Litera business-development intelligence from firm data (LAWSITES-ILTACON4-2026).
- **firm-finance:** KM and technology spend (TRI-SOTLM-2026); Harvey Command Center analytics (LAWSITES-HARVEYDJ-2026); Legalweek ROI sessions (EDRM-LEGALWEEK-2026); consumption pricing (EDISCOVERYTODAY-ILTACON-2026); AI ROI (DELTEK-CLARITY-2026; SPI-AI-2026).
- **scoping-pricing and billing-collections:** client AI line items and "we get nothing" view (TRI-LEGALWEEK-2026; AL-CLIENT-2026); California fee rules (CALBAR-GENAI-2026 p. 8); consulting pricing and internal AI (STANFORD-DEL-2026).
- **assurance archetype:** PwC ChatNational research assistant for US assurance staff, announced 2024-08-01 (ACCTODAY-CHATNATIONAL-2024); compare assurance-quality-management-12. Accounting-body AI guidance on methodology libraries was not reached.
- **customer service (out of archetype):** Basware's support-ticket agent (KANTATA-BASWARE-2026).

## 8. Suggested improvements to the briefs

1. **Register keys per document, not per dive.** The LAWSOC-AGENTIC-2026 collision (two Law Society documents, one key)
   and four renamed keys in this module show the need for a shared registry checked before synthesis.
2. **Say how to grade a merged entry whose named example is weaker than its adjacent measured evidence** (entry 19:
   a named firm's unmeasured pilot plus measured trials elsewhere). A one-line rule would stop B/C disagreements.
3. **Ask deep dives to flag cross-module overlaps by finished id.** Six candidates here were already covered by
   work-production entries; checking the finished module first would have saved the dives effort.
4. **Give the knowledge-management brief a consulting and accounting search budget,** and ask for one attempt at named
   KM job postings; all three dives ran out of search budget and ended legal-heavy.
5. **Ask vendor-page readers to record the page's own date or "undated".** Seven iManage stories carry only a read date.
6. **Name "permission-leakage test" as a target evidence type** in the governance brief; it is the module's biggest
   open question and no dive searched for it directly.
