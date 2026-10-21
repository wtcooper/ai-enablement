# Synthesis report: advisory / risk-controls

Run date 2026-10-20. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/risk-controls.md` (299 lines, table of contents at top)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/risk-controls.yaml` (24 entries; `scripts/validate.py` reports no errors for this file)

## 1. Counts in and out

| Input | Candidates |
|---|---|
| adv-risk-controls-practice.md | 19 YAML entries |
| adv-risk-controls-discourse.md | 18 YAML entries |
| adv-risk-controls-governance.md | 20 YAML entries |
| adv-x-independence-pricing.md | 2 candidate rows (close-agent controls; CPA-led AI assurance) |
| adv-x-state-of-ai-disruption.md | 0 entries (module notes only: GT governance demand, KPMG readiness) |
| landscape-advisory.md | 0 entries (leads only) |
| Routed in from other wave-5 modules | 4 item groups (forensic-disputes, client-accounting-services x2, transactions) |
| **Total in** | **59 candidates** |
| **Out** | **24 use cases** |

## 2. Duplicates merged (final id <- inputs; P = practice, D = discourse, G = governance, IP = independence-pricing)

| Final | Merged from |
|---|---|
| 01 Assistive planning and fieldwork | P09, D07, D15, G07 |
| 02 Board-material and risk signals to audit actions | P15, D17 |
| 03 RCM, narratives, test procedures, request lists | P10, D01, D02 |
| 04 Evidence requests and completeness checks | P08, D04 |
| 05 In-house agentic SOX testing (Reddit, Klaviyo) | P01, G04 |
| 06 Firms run agentic testing in co-sourced and outsourced IA | P03, D03 |
| 07 Full-population testing (Armanino) | P04, plus full-population points of D08 and G04 |
| 08 Year-round testing (Klaviyo) | P05, G09 |
| 09 First-line continuous monitoring, auto-clear rules, self-healing controls | D08, P18 |
| 10 Pre-review and challenge of workpapers and findings | P07, G08, D05 |
| 11 Observation drafting | D06 |
| 12 Vendor SOC reports and vendor AI risk | P11, D12, G11 |
| 13 One agentic platform (Aprio, Cherry Bekaert, Baker Tilly) | P16, D18, G05 |
| 14 Havertys in-sourcing | P06 |
| 15 AI-native SOX testing vendors | P17 |
| 16 Controls-adviser repositioning | D09 |
| 17 AI governance, control design and certification-readiness advisory | P13, D10, G01, G10, IP-02 (readiness side), transactions routed items |
| 18 AI inventory, shadow AI, user-built automations | P14, G12, G13 |
| 19 Audit of client AI governance (GT bank) | P12, D11, G03 |
| 20 SOX scoping of AI inside business controls | D14 |
| 21 Idea: controls before finance agents go live | P19, D13, G02, IP-01, CAS routed item |
| 22 Confidence-threshold routing | G18 |
| 23 Idea: AI-enabled fraud readiness | D16, forensic and CAS routed items |
| 24 Idea: certify and parallel-run AI testing tools | G06 (plus the CPAPA-5Q-2026 parallel-run point from practice) |

**Not kept as entries; cross-referenced by id instead (overlap with other archetypes):**
- P02 Microsoft ITGC change-management agent -> `assurance-controls-testing-06` (same deployment); figure kept in the module's metrics.
- G17 citation-verification gate (Deloitte Australia) -> `professional-services-quality-review-04` (and -02).
- G16 AI-use record on the file -> `professional-services-quality-review-03`.
- G15 AI clauses in engagement letters -> `professional-services-scoping-pricing-07`, `professional-services-acceptance-risk-11`, `assurance-acceptance-independence-11`.
- G19 synthetic-data stress tests -> `assurance-controls-testing-25` (same KPMG idea).
- G20 disclosure review of client AI claims -> `assurance-assurance-over-ai-09`; AI-washing investigations to forensic-disputes.
- G14 AI incident playbooks -> partly `security-governance-risk-18`; no advisory evidence beyond an ISACA gap survey.
- IP-02 CPA-led SOC 2 plus AIUC-1 assurance -> `assurance-assurance-over-ai-19`.

**Source refs normalised (same document, one ref):** OPTRO-CRX-2026 -> OPTRO-AGENTS-2026; RSM-BEACON-2026 ->
ACCTODAY-RSMBEACON-2026; DELOITTE-COSO-2026 -> DART-COSO-2026; JOFA-ETHICSAI-2026 -> JOFA-ETHICS-2026; AICPA-AIUC-2026 ->
JOFA-AIUC-2026; JOFA-CHECKLIST-2026 -> JOFA-CYBERCHECK-2026; JOFA-PRACTICEAID-2026 -> AICPA-AUDITAID-2026;
SEC-REGSX2-01-2026 -> SEC-RULE2-01-2026 (eCFR URL); KPMG-ICFR-WEBCAST-2026 -> KPMG-FUTURESOX-2026; RSM-MMAI-2026 as cited
with the CPA Practice Advisor URL -> CPAPA-RSMMM-2026; COSO-GENAI-2026 (three URLs) -> the coso.org PDF.
KPMG-REVCONTROLS-2026 (the "-new" PDF of the same webcast summary) is kept as a separate ref because its pagination and
date differ; a later pass should confirm whether the two files are one document.

**Classification changes from the research files:** P03/D03 (#06) and G04 (#05) set to delegate/process, following the
vocabulary's worked example "agent tests key controls end to end and drafts the workpaper"; D18 (#13) delegate -> augment
(every source stresses oversight at each stage); G18 (#22) augment -> automate (only low-confidence items go to people);
D13 (#21) C -> D (no deployment found; labelled idea).

## 3. Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 01, 20, 21 (D), 23 (D), 24 (D) | none | 17, 19 |
| augment | 03, 04, 10, 11, 12, 18 | 02, 07, 08, 13 | 14, 16 |
| automate | 22 | 09 | none |
| delegate | not applicable | 05, 06 | 15 |

No evidence for automate at model level or assist at process level. Automate rests on one firm description (#09, C, partly
idea) and one adjacent academic case (#22, bookkeeping data). No source describes a control-testing design without a
human reviewer.

## 4. Grade mix

A = 0, B = 13 (54%), C = 8, D = 3 (all labelled idea). No entry reaches A under the 2026-10-17 rule: every figure is
vendor-published (Reddit, Petual, PwC, Diligent, Armanino via DataSnipper) or self-reported without method (Microsoft,
RSM, Grant Thornton). #22 is B because its independent measurement is from adjacent bookkeeping work. No conference
session is used as A or B evidence; scheduled sessions appear only as frontier signals.

## 5. Routed to other modules (collected from the inputs for their syntheses)

- **assurance:** Grant Thornton Enterprise Assurance Services with provisional AIUC-1 accreditation (GT-EAS-2026); AICPA
  and AIUC joint SOC 2 plus AIUC-1 offering (JOFA-AIUC-2026); Aprio's ANAB accreditation to certify against ISO/IEC 42001
  (APRIO-ISO42001-2026); the SOC and financial-audit portions of Cherry Bekaert's and Aprio's Fieldguide deployments; BDO
  Risk Assessment Coach and Chat BDO (BDO-AI-2025); AICPA practice aid (AICPA-AUDITAID-2026); AICPA TQA 9561
  (DART-TQA9561-2026); FRC guidance and PCAOB spotlight as audit methodology; KPMG UK SOC/ISAE assurance with about 18% less
  testing time (KPMG-UKCONTROLS-2026); full-population testing at an employee-benefit-plan audit firm (CPAPA-FULLPOP-2026);
  KPMG's "AI as the subject of the audit" where the work is an attest opinion.
- **professional-services:** Aprio's $300M five-year AI investment (APRIO-FIELDGUIDE-2026); realization claims on engagement
  platforms (Fieldguide; undated case studies, not used); PE ownership (Riveron/Kohlberg; APS split; GT-CBIZ-2026);
  pricing of outsourced testing as spend moves to advisory (Havertys); fee reasonableness when AI shortens work
  (ABA-FO512-2024, II.F); AI audit mentor agent for onboarding (IIA-PODCAST-2026); junior pipeline and talent
  (CPAPA-TECHLAB-2026); AI in firm quality control and peer review (CSA-SOC2AI-2026 note); Deloitte Australia refund as a
  deliverable-quality case (CITYAM-DELOITTE-2025).
- **client-accounting-services:** governance of agentic close tools delivered as CAS (CPAPA-AGENTSCLOSE-2026); bookkeeping
  field evidence (STANFORD-JAR-2026). #21 and #22 keep only the control design.
- **forensic-disputes:** fraud-indicator flagging in board materials (DILIGENT-AUDITAI-2026); AI-enabled fraud
  investigation and deepfake evidence (IAF-AIFRAUD-2026; ACFE items); AI-washing investigations (SEC-AIWASH-2024).
- **tax:** IRS OPR and UK PCRT AI guidance (ACCA-ENGLETTERS-2026).
- **valuation:** IVSC AI disclosure (IVSC-IVSED-2026).
- **fpa-performance:** finance-function AI results such as forecast accuracy (KPMG-AIFINANCE-2026).

Items routed **to** risk-controls and picked up: DOJ-ECCP-2024, FINCEN-DEEPFAKE-2024, ACFE-TECHBENCH-2026,
ACFE-CANADA-2026 (forensic-disputes) -> #23 and frontier; CPAPA-AGENTSCLOSE-2026, COSO-GENAI-2026, JOFA-AIUC-2026 and
AFP-PAYFRAUD-2026 (client-accounting-services) -> #17, #21, #23; FORVIS-AIBUYSIDE-2024 and GT-PEAI-2026 (transactions)
-> #17. Not used: FASKEN-RWI-2026 (insurer view of target AI risk; mentioned in #17 notes only) and the Deloitte
Australia refund (cross-referenced to professional-services).

## 6. Gaps

- **No quality evidence**: no error, override, false-exception, parallel-run, rework or inspection result for AI in
  internal audit, SOX or risk advisory. All three angles report this.
- **No outsourced-provider outcome**: every figure is from an in-house team or a vendor; RSM, Riveron, Baker Tilly,
  Aprio and Cherry Bekaert publish no measures.
- **ERM and cyber/IT risk advisory**: no named AI deployment; #02 is the only ERM-adjacent entry.
- **Mid-market breadth**: no Crowe, Forvis Mazars, CohnReznick, Moss Adams, CBIZ or Weaver internal-audit AI deployment
  found in 2026 sources.
- **Independence for non-SEC clients**: AICPA nonattest rules (ET 1.295) were not read in primary text; whether AIUC-1
  readiness advice conflicts with a later examination by the same firm is unresolved.
- **Unresolved items**: whether KPMG-REVCONTROLS-2026 and KPMG-FUTURESOX-2026 are one document; IIA framework date
  (2024-09-13 versus 2023); Gartner strategy-figure base (743 versus 161); IIA Pulse and Internal Audit Foundation
  figures cited second-hand in places.

## 7. Suggested improvements to the briefs

1. Give researchers a canonical ref table for documents that recur across angles (Optro release, RSM Beacon, COSO, KPMG
   webcast, SEC Rule 2-01, JofA articles); 11 aliases had to be normalised here.
2. Tell researchers to apply the vocabulary's worked examples when setting the ladder; two angles graded the same
   agent-testing case augment, which the worked example calls delegate.
3. Ask each angle to state, per entry, the overlapping id in assurance or professional-services when one exists;
   controls-testing in assurance already holds the Reddit, Microsoft, Havertys and firm-delivered cases.
4. Ask the governance angle to keep firm-operations controls (engagement letters, file documentation, citation checks)
   out of the module candidate list and route them directly; four of its 20 candidates were firm operations.
5. Ask for one targeted search for parallel-run or override data per module; all angles report it missing, and the
   discourse angle never ran its quality-evidence query because the search budget ran out.
6. For independence, give researchers the primary AICPA Code sections to check, since the code site was login-gated in
   every run.
