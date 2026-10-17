# Synthesis report: assurance / assurance-over-ai

Wave 1 · 2026-10-16 · Brief: `research/briefs/templates/synthesis.md`

**Outputs**
- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/assurance-over-ai.md` (291 lines, table of contents)
- Use cases: `.../assurance/use-cases/assurance-over-ai.yaml` (24 entries)
- `python3 scripts/validate.py`: no errors in these files. One warning: 24 use cases, 8 graded A/B (33%), below the 50% target (explained in §4). At the time of the run the validator also showed an ERROR in `modules/soc-attestation.md` (308 lines), a file from another synthesis that this run did not touch.

## 1. Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| `landscape-assurance.md` | 0 (context and leads only) | n/a |
| `assurance-assurance-over-ai-practice.md` | 19 | A 1, B 4, C 13, D 1 |
| `assurance-assurance-over-ai-discourse.md` | 20 | B 6, C 10, D 4 |
| `assurance-assurance-over-ai-governance.md` | 21 | B 2, C 5, D 14 |
| **Total in** | **60** | A 1, B 12, C 28, D 19 |
| **Out** | **24** | A 0, B 8, C 10, D 6 |

59 candidates were merged or kept; 1 was dropped (governance-12, Raji et al. 2020 internal algorithmic audit framework: academic only, pre-GenAI, and no practitioner or regulator in the inputs discusses it).

## 2. Duplicates merged

P = practice, D = discourse, G = governance (input entry numbers).

| Out | Title (short) | Merged from |
|---|---|---|
| 01 | Inventory and scope entity AI (idea) | P14, D01, G01 |
| 02 | Classify AI controls by reliance and AI role | G02, D02 |
| 03 | Extend ITGCs to AI components; choose evidence mix (extends CT#15) | P15, P16, D03, D06, G03, G04 |
| 04 | Evidence trail; auditable agent records | D05, G10 |
| 05 | Monitoring metrics, tolerances, remediation logs (idea) | D04, G05, G06 |
| 06 | Challenger models and test populations (idea) | G09 |
| 07 | SOC reports and AI representations for vendor AI (idea) | P17, G07 |
| 08 | AI-enabled fraud risk (idea) | G08 |
| 09 | Audit committee dialogue and AI disclosure controls | D07, D08 |
| 10 | Internal audit assurance over AI governance | D09, G13, P18 |
| 11 | Continuous, AI-assisted assurance over AI (idea) | D15, D20 |
| 12 | Governance / conformity / performance scoping | G18, P08 (taxonomy part) |
| 13 | Readiness and gap assessment | P06 (+ KPMG NL readiness scans from G17) |
| 14 | ISAE (UK) 3000 "SOC 2+" opinion over AI governance | P01, D12, G16 |
| 15 | ISO/IEC 42001 certification | P02, D10, G14, P11 |
| 16 | Accrediting certifiers against ISO/IEC 42006 | G15 (+ 42006 detail from P02, P19) |
| 17 | Firms self-certify their AI management systems | P03 |
| 18 | Firms build AI assurance service lines | D18, P04, P05, P08 (suite part) |
| 19 | AIUC-1 agent certification with insurance | P09, D14, G19, D17 |
| 20 | System-level technical AI assurance | P07, D13, G17, G11 |
| 21 | NYC Local Law 144 bias audits | P13 |
| 22 | EU AI Act conformity assessment | P12, D19, G20 |
| 23 | Buyer-side verification; STAR for AI registry | D11, P10 |
| 24 | Professionalising AI assurers | D16, P19, G21 |

**Overlap with controls-testing.** `assurance-controls-testing-15` (testing AI-performed controls) covers the same test object from the SOX-programme side. Entries 02, 03 and 07 reference it by id and hold only what it lacks: COSO's reliance evidence standard, BDO's component and agent-type ITGC scoping, the AICPA evidence-mix guidance, and the user-auditor view of service-organisation AI. ITGC extension and evidence strategy were merged into one entry (03) rather than two to avoid duplicating CT#15.

**Grade and field changes made in synthesis (editorial judgement, noted in each entry):**
- P02 graded A in input → entry 15 graded B. Schellman's "26 signed contracts" (Oct 2024) counts demand at one certifier, not an outcome of certification.
- D18 graded B → entry 18 graded C. The evidence is offers, positioning and one press quote, with no named client engagement.
- D14 ladder `automate` → entry 19 `augment` (auditor oversight stays on the normal path).
- D09 maturity `in-production` → entry 10 `emerging` (no named internal audit function).
- P14 (C) and P17 (C) folded into entries graded D because the merged evidence is non-authoritative guidance with no engagement.

**Source keys normalised.**
- Inside this module: DART-COSOHU-2026 / DART-COSO-2026 → DART-COSO-2026; DSIT-ROADMAP-2025 / DSIT-ASSURANCE-2025 (same 2025 roadmap) → DSIT-ROADMAP-2025, kept separate from DSIT-ASSURANCE-2024 (the Nov 2024 market report); TECHUK-ASSURANCE-2026 → TECHUK-ROADMAP-2026; IIA-AIFW-2024 → IIA-AIFRAMEWORK-2024; SCHELLMAN-AIUC-2026 → SCHELLMAN-AIUC1-2026; CALCPA-AI-2026 / CALCPA-AIREG-2026 → CALCPA; OJEWALE-2025 → OJEWALE-2024; AIACT-ART43-2024 → EU-AIACT-ART43-2024.
- Aligned with controls-testing.yaml (same URL, same key in every file): COSO-GENAI, AICPA-PA, BDO-ITGC, EY-SOC, K-SOX30, K-404A, K-UKCA, OPTRO-SURVEY, CALCPA, CSA-SOC2, JOFA-EVAL, JOFA-FAST, UNIQUS. Acceptance-independence.yaml also uses AICPA-PA, AT-AICPAPA-2026 and EY-CANVAS-2026, so those match too.
- COSO URL: the coso.org PDF (governance) is used instead of a copy hosted by a Spanish internal-audit body (practice).

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 01, 02, 07, 08, 09, 10, 12 | 03, 04, 23 | 13, 14, 15, 16, 17, 18, 20, 21, 22, 24 | 20 |
| augment | 06 | 05, 11 | 19 | 4 |
| automate | none | none | none | 0 |
| delegate | none | none | none | 0 |

- **No evidence for automate or delegate.** In this module the AI is mostly the object of assurance, so `ladder` describes the assurance team's own tooling and stays at `assist`. The four `augment` entries are three ideas (05, 06, 11) and AIUC-1's automated adversarial testing under auditor oversight (19). No source describes an agent auditing an AI system end to end, or AI on the normal path with no person.
- Every change scope has evidence. Model scope dominates (11), because Area 2 is new services, credentials and accreditation.
- Maturity: in-production 8 · announced 3 · piloting 1 · emerging 12.

## 4. Grade mix

A 0 · B 8 (09, 15, 16, 17, 19, 20, 21, 24) · C 10 · D 6 (01, 05, 06, 07, 08, 11, each titled and noted "idea").

**Why A/B is 33%, below the 50% target.** The evidence really is thin, and the target cannot be met without inflating grades.
- Area 1 (auditing entity AI) rests on guidance: COSO, the AICPA practice aid read only through press, BDO, and Deloitte DART. No named audit engagement, inspection finding or disclosed AI-related material weakness was found in three independent searches, including EDGAR full-text queries in the discourse run.
- Area 2's B grades rest on named certifications (BSI clients, Big Four self-certificates, AIUC-1 certified agents) and survey or market measures. None measures assurance quality.
- D entries were kept only where COSO, the AICPA, Deloitte or EY conference speakers discuss them.

## 5. Gaps

- **No quality evidence at all**: no error, override or drift rates, no parallel runs, no inspection findings, no measured effect of an AI assurance engagement. The only independent evidence is academic (Groves, Birhane, Ojewale, Nian) plus UK government market sizing.
- **Commercial facts missing**: no fees, margins, certificate counts, issued ISAE 3000 / SOC 2+ opinions or named Big Four clients. The only fee data (six to twelve months; tens of thousands of dollars) comes via a CSA note citing an unopened consultancy blog.
- **Primary texts not read**: AICPA practice aid (login), TQA 9561 (login), ISO/IEC 42001 and 42006 (403), ACCA/EY paper (DNS failure), IIA framework English text (member-only), EU AI Omnibus Official Journal text, PCAOB pages (403).
- **Practice voices**: no practitioner survey of how external auditors scope or test entity AI; little from mid-tier and small practices (Baker Tilly, Cherry Bekaert, Uniqus, Schellman only); no community sources (Reddit blocked; LinkedIn not used).
- **Unresolved conflicts** (recorded in entry notes): COSO's eighth capability name; ISO/IEC 42006 date (7 Jul, 21 Jul or 5 Aug 2025); UK 2035 market potential (GBP 6.53bn vs 18.8bn); Omnibus adoption dates; AIUC funding ($40M vs $55M) and consortium size; "authorized" vs "accredited" AIUC-1 auditor; BDO's paraphrase of COSO's reliance definition; whether the CSA note discloses AI-assisted drafting (the landscape says yes; the deep dives did not find it).

## 6. Routed to other modules (collected from the inputs)

| Target module | Item | Source key(s) |
|---|---|---|
| controls-testing | KPMG UK ~18% testing-time reduction from AI in controls assurance; one team ~15% with DataSnipper | K-UKCA (PDF pp. 2, 6) |
| controls-testing | KPMG on synthetic data, agents stress-testing controls, 100% coverage | K-SOX30 (p. 11) |
| controls-testing | Optro/Midship SOX test from ~16 h to under 15 min, up to 85% of controls (vendor claim); PayPal "swarm auditing" | SRA-POD-2026 |
| controls-testing; business-model lens | SEC filer-status proposal (about half of attested issuers out of 404(b), if adopted) | UNIQUS |
| controls-testing; substantive-testing | PCAOB technology-assisted-analysis amendments (AS 1105, AS 2301) | CALCPA |
| substantive-testing | IAASB Technology Catalog matters 6(a)-(h) on tools, explainability, outliers, documentation | IAASB-CATALOG-2026 (p. 3) |
| quality-management | FRC generative and agentic AI guidance (risk categories, certification, control points, worked examples) | FRC-GENAI-2026, FRC-GENAINEWS-2026 |
| quality-management | AICPA practice aid Part 2 (firm's own AI use, supervision, one tool checking another) | AICPA-PA, AT-AICPAPA-2026, JOFA-AIPA-2026 |
| quality-management | Board Agenda: none of six firms monitored tool impact on quality (conflicts with the landscape's "building ways to monitor") | BOARDAGENDA-FRC-2026 |
| quality-management | ICAEW view on FRC guidance; ICAEW podcast with FRC, GT, Deloitte | ICAEW-FRCVIEW-2026, ICAEW-POD-2025 |
| quality-management; substantive-testing | CalCPA's unattributed claim of PCAOB deficiencies in AI-assisted journal-entry testing (unverified) | CALCPA |
| quality-management | IAASB Technology Quality Management initiative | IAASB-TECH-2026 |
| quality-management; acceptance-independence | PCAOB Acting Chair Botic (9 Dec 2025): AI and skepticism; private equity | KSLAW-BOTIC-2025 |
| acceptance-independence | AI as an acceptance factor (heavy reliance resembles complex valuation models; untraceable agent workflows); engagement-letter disclosure and state law | AT-AICPAPA-2026 |
| acceptance-independence | Independence of AI assurance or readiness sold to audit clients; certifier impartiality; Big Four tool partnerships; PE-backed firms | KPMGUS-ISO-2025, BSI-ANAB-2026, EY-CANVAS-2026, CONSULTANCY-BIG4-2025 |
| acceptance-independence | SEC staff: consultations involve AI in accounting tools and business relationships, PE, partner rotation | JDSUPRA-ALI-2026 |
| planning-risk-assessment | AI-enabled fraud risk in planning; understanding the entity's IT and AI | AT-AICPAPA-2026, COSO-GENAI (p. 11) |
| specialists | ISACA AAIA; AICPA "specialist support"; AI-component ITGC specialists; "two-in-the-box" model | ISACA-AAIA-2026, ISACA-5Q-2026, AICPA-PA, JOFA-EVAL |
| specialists | IAASB matters 7(b)-(c): management's expert; experts presumed human | IAASB-CATALOG-2026 (p. 3) |
| other-assurance (SOC) | TQA 9561 (AI in SOC 1 / SOC 2); no AI-specific Trust Services Criteria; "fast and easy" warning; Peer Review Board action (14 May 2026) | CSA-SOC2, JOFA-FAST, JOFA-PEER-2026 |
| other-assurance (SOC) | EY SOC conference poll: AI used for evidence collection 63%, Section 3 45%, deviation responses 41% | EY-SOC |
| other-assurance (sustainability) | IAASB catalog matter 10(a); ISSA 5000 | IAASB-CATALOG-2026 (p. 14) |

## 7. Suggested improvements to the briefs

1. **Add a field or pattern for "AI as the object".** `ladder`, `pattern` and `runtime_class` assume the AI does the work. All three angles had to fill them with placeholders. Suggest a field `ai_role: tool | object`, or a new pattern `assure-ai-system`, so modules like this and CT#15 are not counted as "assist" coverage.
2. **Say what to put in `provenance` when nothing is published.** Every input wrote `provenance: n/a`, which fails the enum. The vocabulary should say to omit `provenance` for "none published" outcomes.
3. **Keep a shared source-key registry before synthesis.** Wave 1 inputs use `PUBLISHER-SHORT-YYYY`, while the pilot module uses short keys (K-SOX30, COSO-GENAI). Parallel syntheses will diverge unless a registry (URL → key) exists. This run aligned 13 keys by hand.
4. **Write a grading rule for guidance-only entries.** The angles graded the same AICPA and COSO guidance as C (practice) and D (governance). Suggested rule: standard-setter or regulator guidance with no deployment → D, labelled idea; a firm's or vendor's service offer with no named client → C; a named engagement or certificate → B.
5. **Clarify that grade A needs an outcome of the change.** A count of contracts or of survey respondents is not enough.
6. **Ask angle researchers to read overlapping verified modules first**, here CT#15, and mark candidates that duplicate them. About a fifth of the Area 1 candidates restated CT#15.
7. **Fix a convention for undated pages.** Inputs used the retrieval date as the publication date. Suggest the year only, with "page undated, retrieved YYYY-MM-DD" in the locator. This run did that for five pages.
8. **Ask the discourse angle to flag AI-generated aggregator pages** (such as the welcome.ai Genpact summary) as low authority by default. This run kept one only as a D-grade signal.
