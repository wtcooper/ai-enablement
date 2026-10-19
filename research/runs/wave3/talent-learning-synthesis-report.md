# Synthesis report: professional-services / talent-learning

Prepared 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/talent-learning.md` (about 270 lines)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/talent-learning.yaml` (25 entries; `scripts/validate.py` reports 0 errors, 60% A/B)

## 1. Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| ps-talent-learning-practice.md | 25 | A 2, B 13, C 8, D 2 |
| ps-talent-learning-discourse.md | 20 | A 1, B 6, C 9, D 4 |
| ps-talent-learning-governance.md | 19 | A 1, B 6, C 10, D 2 |
| Routed from other ps-* files (used) | 3 items folded in | Blank Rome (quality-review, work-production), MinterEllison (work-production), Forrester pyramid view (firm-finance governance) |
| **Total in** | **64 candidates** | A 4, B 25, C 27, D 8 (the same NBER trial is the A in all three) |
| **Out** | **25 use cases** | **A 2, B 13, C 7, D 3** |

Out-of-scope candidates were not dropped. Each one was merged into a surviving entry, with every source kept.

## 2. Duplicates merged (output id <- inputs)

| Out | Title (short) | Merged from (P = practice, D = discourse, G = governance) |
|---|---|---|
| 01 | Firmwide training, access gated | P18, D18, G01; Blank Rome 95% in-house (routed) |
| 02 | Duane Morris onboarding | P04, D03, G02 (also routed from quality-review and work-production) |
| 03 | Billable-credit time and competitions | P01, D04; Blank Rome hackathon (routed) |
| 04 | Seats and secondments into AI teams | P02, D09, G05; MinterEllison (routed) |
| 05 | Training moved upstream | P03, P23 |
| 06 | Simulations, personas, pre-review feedback | P05, P21, D01, D02, D08, G04 |
| 07 | Reviewer-first entry roles | P06, D06, G11 |
| 08 | Graduate programmes and human skills | P07, P14 |
| 09 | Teach and check verification | D05, D19, P24, G03 |
| 10 | Disclosure and second-level review | G13 |
| 11 | NBER patent trial | P22, D14, G06 |
| 12 | Skill-aware task allocation | G07 |
| 13 | Recruit for judgment and AI working | P12, P13, D11, G12 |
| 14 | AI screening interviews under rules | P11, G18 |
| 15 | AI adoption in objectives and promotion | P15, D13, G16 |
| 16 | Shoosmiths prompt-linked bonus | P16 |
| 17 | AI in performance evaluation | P17, G19 |
| 18 | Professional-grade AI as retention lever | D12, G15 |
| 19 | Resize and reshape intake | P08, P09, D15, D16, D17, G08, G09, G10 |
| 20 | Hybrid human-agent workforce model | P10, G17; Forrester (routed) |
| 21 | Accenture upskill-or-exit | P19 |
| 22 | Support-function roles re-scoped | P20 |
| 23 | Idea: junior operational roles | D10 |
| 24 | Idea: milestones and measures beyond hours | P25, D07, G14 |
| 25 | Idea: residency-style formation | D20 |

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model | Total |
|---|---|---|---|---|
| assist | 01, 05, 09, 10, 13, 16, 18 | 02, 03, 04, 08, 15 | 21, 23, 24, 25 | 16 |
| augment | 06, 11, 12, 17 | 07, 14 | - | 6 |
| automate | - | 22 | 19 | 2 |
| delegate | - | - | 20 | 1 |
| Total | 11 | 8 | 6 | 25 |

- **Delegate:** one entry (#20, grade C, emerging). Its evidence is firms' expectations (14% of law firms in one survey expect agents to do most work) and a McKinsey CEO statement. No source describes an agent owning a talent or learning process. No delegate entry was invented.
- **Automate:** two entries. #22 (support roles) is the only automate/process entry. #19 is set to automate because its premise is AI taking entry-level tasks; no AI makes the intake decision.
- **Augment/model:** no evidence.
- **Why assist dominates:** in this module AI mostly changes the work that people learn from. The talent processes themselves (training, reviews, hiring decisions) stay human-run. That is a feature of the evidence, not a gap in the search.

## 4. Grade mix and grading decisions

- **A (2):** #11, the NBER 35720 trial. Provenance is set to `vendor-published` because the discourse angle read the disclosures: Google conducted the trial and funded its direct costs, and five of seven authors have Google ties. The practice, governance, quality-review and work-production files mark it `independent`, so the two labels conflict across modules. #16, Shoosmiths' tracked prompt count, meets the A rule as a tracked metric, but it measures activity, not a talent outcome.
- **Regraded down:** G07 (skill-aware task routing) went from B to C, because the experiments measure task performance and no firm is named routing tasks this way. G04 (Three Crowns simulator, weak B) became part of #06 at C: the source is a vendor-authored panel recap and shows no use at scale. P13 (Fredrikson, B) absorbed McKinsey's reported AI interview (C), and the merged entry stays B on Fredrikson.
- **Provenance changes:** TR-FOP-2026 figures are labelled vendor-published throughout; quality-review practice had labelled them independent. BCG's 43% figure is labelled self-reported, because BCG took part in the experiment.
- **No firm-measured talent outcome exists anywhere.** Every B is a named deployment without published measurements.

## 5. Gaps

- **No outcome data for any junior programme:** no error-catch, override, retention or time-to-competence figures. This covers Ropes & Gray, Sidley, Duane Morris, PwC, KPMG, Mishcon, A&O Shearman, MinterEllison and Blank Rome.
- **NBER 35720 abstract only:** the full paper was blocked in all three runs. Effect heterogeneity and task design are unread, and p-values were garbled in two mirrors, so they are omitted.
- **Coverage skew:** law and large accounting firms dominate. Consulting rests on McKinsey (reported), Accenture and BCG (a 2023 experiment). Architecture and engineering have only Deltek's talent-strain figures. No mid-tier consultancy evidence was found.
- **In-house:** no named in-house talent or learning programme was found. In-house voices appear only in TR-FOP-2026, the LexisNexis survey quotes and Harvey Academy's audience.
- **Employment-AI in practice:** apart from Mishcon's trial, no professional-services firm describes AI screening, AI-scored evaluation or AI-informed promotion.
- **Primary texts not reached:** ABA Opinion 512, the SRA warning notice, NALP, Citi, SurePoint, BCG Attorney Search, The Telegraph and FT originals, and the Reuters piece on Ropes & Gray.
- **Possible mirror artefacts:** Bloomberg Law firm names 'Winston Taylor' and 'Sheppard LLP' (#08). Check them before naming.
- **Conference content:** only previews and recaps were read (Legalweek, ENGAGE, CMBDO). No session transcript on talent was read.
- **Job postings:** no usable named-firm posting for AI training roles. The Experis posting was search-only and has expired.

## 6. Source-key normalisation

The same document carried different keys across the angle files. The YAML uses the first key in each row below; aliases should be mapped to it.

| Canonical | Aliases seen |
|---|---|
| TRI-ONBOARDING-2026 | TRI-ONBOARD-2026 |
| JOA-TRAINING-2026 | JOFA-LEARN-2026, JOA-LEARN-2026 (quality-review discourse) |
| TRI-LDEV-2026 | TRI-LAWYERDEV-2026 |
| TRI-DESIGNL-2026 | TRI-SEYFARTH-2026 |
| TRI-TAAP2030-2026 | TRI-TAX2030-2026 |
| ICAEW-WORRY-2026 | ICAEW-WORRIED-2026 |
| SFN-BIG4-2025 | SFN-BIGFOUR-2025 |
| ICO-RECRUIT-2024 | ICO-AIRECRUIT-2024 |
| NYC-AEDT-2023 | NYC-LL144-2023 |
| TRI-FOPTALENT-2025 | TRI-TALENT-AI-2025 |
| TRI-GENAITALENT-2024 | TRI-GENAI-TALENT-2024 |
| BLOOMBERGLAW-HIRING-2026 (landscape key) | BLAW-FIRSTYEAR-2026, BLOOMBERG-FIRSTYEAR-2026 |
| TRI-LEGALWEEK-ASSOC-2026 | TRI-LEGALWEEK-CRISIS-2026 (firm-finance discourse) |
| LEXIS-MENTORSHIP-2026 (report page) | Governance used the same key for the press release; the press release is now LEXIS-MENTORPR-2026 |

Other conflicts:
- TR-FOP-2026 is dated `2026` here; quality-review practice uses `2026-06-22`.
- NBER-AUTOR-2026 uses the nber.org URL here; some files use EconPapers.
- ILTA-TECHSURVEY-2026 and KANTATA-RMI-2026 are typed `survey` here; some angle files typed them `professional-body` or `vendor`.

## 7. Routed to other modules (collected from the three talent-learning inputs)

- **staffing-resourcing:** KANTATA-RMI-2026 (52.7% not equipped for hybrid teams; 7.3% use outcome data; sample of 44 organisations); DELTEK-CLARITY-2026 (staff growth 1.2%, turnover above 13%); EU AI Act treatment of AI used to allocate work (EC-AIACT-2026); TRI-HUMANAGENT-2025 (64% of IT leaders expect HR and IT to merge). #20 keeps only the workforce-design angle.
- **firm-finance:** KPMG measuring the value of its AI investment through usage tracking (BLOOMBERG-KPMG-2025); PwC's USD 3bn network investment (ATODAY-PWC-2026); Accenture's charges and savings (FORTUNE-ACCENTURE-2025); Fredrikson's three business-model scenarios (TRI-LDEV-2026); Citi's expectation of AI-driven consolidation (LAW360-CITI-2025); leverage and equity-partner counts (VAULT-PYRAMID-2026); LFFI Q2 leverage economics (TRI-LFFI-Q2-2026); 67% AI wage premium (PWC-AIJB-PS-2026); 4.2% demand growth (BLOOMBERG-AICOST-2026); frozen consulting starting salaries (SLASHDOT-CONSULTING-2025, secondary).
- **scoping-pricing / billing-collections:** clients asking for AI line items and refusing to pay for AI-done work (TRI-LEGALWEEK-2026); PwC subscription services (CPAPA-PWC-2026); 75% of law firms rethinking pricing communication and 41% reporting more client scrutiny (LAW360-GA-2026); client says junior hours too high (ICAEW-EXPECT-2026); Citi's three-fourths expecting the billable hour to be affected by 2028 (BLOOMBERG-AICOST-2026); STANFORD-DEL-2026; Cal Bar rules on charging for AI (CALBAR-GENAI-2026, p.8).
- **client-development:** partners not discussing AI with clients (TRI-STANDOUT-2026); TRI-AIFORUM-2026 (in-house: judgment, transparency and speed separate firms); clients reconsidering firms over AI capability (TR-FOP-2026).
- **quality-review / acceptance-risk:** California supervision duties (CALBAR-GENAI-2026); 85% of law firms using manual checks to enforce AI policy (LAW360-GA-2026); SRA warning notice, Cork & Anor v Smith and the 67 UK hallucination cases (DWF-SRA-2026); hallucinated-citation incidents (LEGALCHEEK-REDDIT-2026); judgment-validation and override-tracking standards (TRI-STANDARDS-2026); California agentic confidentiality rules (pp.5-6).
- **knowledge-management / work-production:** Hogan Lovells Cadwalader's pilot of more than 1,300 lawyers (LEGORA-HLC-2026); Ascend's closed-loop data capture (ATODAY-ASCEND-2026); High Rock's assistant grounded in firm reconciliations (JOA-TRAINING-2026); knowledge-curator roles (TRI-AILAWPROF-JUNIOR-2026); firms extracting lawyers' knowledge into AI workflows (VAULT-PYRAMID-2026).
- **delivery-management / sourcing:** offshoring to India, Malaysia and the Philippines alongside intake cuts (CITYAM-BIG4-2025).

## 8. Items routed to talent-learning from other ps-* files

| From | Item | Handling |
|---|---|---|
| quality-review practice; work-production practice | Blank Rome apprenticeship, 95% in-house training, Trial Academy, 300-associate hackathon (HARVEY-BLANKROME-2026) | Used in #01 and #03 (vendor story, so no grade lift) |
| work-production practice | MinterEllison accelerator and legal-engineer cohort (LEGORA-MINTERELLISON-2026) | Used in #04 |
| firm-finance governance | Forrester pyramid view (FORRESTER-BLOG-2025) | Used in #20 |
| knowledge-management discourse | Gilchrist Connell chief AI and knowledge officer (LAWYERSWEEKLY-GILCHRIST-2026) | Module §7 |
| firm-finance discourse | Legal engineer path (BLOOMBERGLAW-GCXAI-2026); Legalweek junior crisis (TRI-LEGALWEEK-CRISIS-2026 = TRI-LEGALWEEK-ASSOC-2026) | Module §7; #06 |
| NBER, TR-FOP, MCA, ILTA headcount (many files) | Same sources as the angle files | Already covered |
| firm-finance practice | PwC headcount down 5,600 and UK graduate cuts (RESULTSENSE-2026, secondary) | Not used: secondary, with no talent detail beyond #19 |
| knowledge-management practice | McKinsey's tech leader on Lilli doing analysts' slide work without fewer analysts (THEOUTPOST-LILLI-2025) | Not used: aggregator summary of an interview; candidate for #07 or #19 once the original is read |
| pursuit-proposals practice | Robins & Morton onboarding with AI search (KANTIV-ROBINS-2026); Loopio's 15% using AI for onboarding (LOOPIO-TRENDS-2026, p.57) | Not used: the inputs hold no onboarding detail beyond the routing line |
| quality-review discourse | ABA podcast 'Developing Lawyers in the Age of AI' (13 Oct 2026) | Not used: not opened by any run; a lead |
| work-production discourse | Allens supervision practice (ALLENS-XEXAM-2026); legal writing pedagogy (TRI-CLARITYWRITE-2026); junior consultant learning (STRATEGYCASE-JUNIOR-2026) | Not used: no detail in my inputs; leads for a refresh (consulting evidence is thin) |
| work-production governance | Choi, Monahan and Schwarcz recommendation to limit first-year law students' AI use (LEGALFUTURES-CHOI-2023); ICMCI code assessment-integrity sections (ICMCI-AICODE-2026) | Not used: only the routing line was available. UMN-CHOI-2024 is in #12 |
| scoping-pricing discourse and governance | Junior training under AFAs (ILTA-PULSE-2025); Wipfli on decade-old metrics (BLOOMBERGTAX-PRICING-2026) | Not used as entries; both support #24 on a refresh |

## 9. Suggested improvements to the briefs

1. **Fix one key per document before the deep dives start.** Fourteen documents carried two or three keys across the angle files. Give each angle a seed key list from the landscape, and require that list to be checked before minting a new key.
2. **Require a funding and disclosure check for academic studies.** Only one of three angles read the NBER disclosures, and that one changed the provenance. Add a rule: for any academic or study-based A, read and record the funding and conflict disclosures.
3. **Say how to set the ladder for workforce-planning use cases.** Intake resizing was set to automate, assist and automate/model by different angles. Add a worked example, such as 'a firm cuts intake because AI does junior tasks', to the vocabulary.
4. **Ask angles to give routed items one line of substance.** Several items routed to this module (ABA podcast, Allens, ICMCI code, Robins & Morton) arrived as a key only and could not be used. Ask for the claim, figure or locator with each routed item.
5. **Name in-house targets for the people modules.** All three angles found no in-house talent programme. Point the brief at CLOC talent sessions, ACC surveys or GBS (global business services) learning teams, rather than general searches.
6. **Budget searches per angle.** All three angles ran out of the shared search budget before targeted firm-career and job-posting searches. A per-angle reserve of three or four searches for job postings would fill the job-posting source type.
