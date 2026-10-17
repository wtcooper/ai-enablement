# Completion and reporting (assurance)

Verified against sources 2026-10-17. Use cases live in `../use-cases/completion-reporting.yaml` (18
entries). Ids are shortened here: `#06` means `assurance-completion-reporting-06`; `ST-13` means
`assurance-substantive-testing-13`. Source keys in brackets are in the YAML or in §12. Public evidence sits almost
entirely in two steps, the disclosure checklist and the mechanical review of draft statements. Nearly every figure is
vendor-published, and no accuracy or miss rate exists for any completion tool in live use. Say so when you quote one.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Open questions: steps with no public AI evidence](#4-open-questions-steps-with-no-public-ai-evidence)
5. [Interview probes](#5-interview-probes)
6. [Metrics and benchmarks](#6-metrics-and-benchmarks)
7. [Guardrails](#7-guardrails)
8. [Accountability and the audit committee](#8-accountability-and-the-audit-committee)
9. [Roles and how they evolve](#9-roles-and-how-they-evolve)
10. [Frontier](#10-frontier)
11. [Common objections](#11-common-objections)
12. [Sources](#12-sources)

## 1. What this module covers

The end of a financial-statement audit, from the point the statements are drafted to the signed opinion. Disclosure
checklists (a list of every disclosure the framework requires, ticked against the draft) and the read and tie-out
of the statements (casting: checking the arithmetic; tie-out: agreeing figures to the trial balance and audited
amounts), the read of other information, subsequent events, going concern, written representations, the summary of
misstatements, engagement quality review (EQR: an independent partner's review before release), key or critical
audit matters (KAMs under ISA 701, CAMs under PCAOB AS 3101: the hardest judgment areas, disclosed in the report),
audit committee communications, and drafting the opinion.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain | AI evidence |
|---|---|---|---|---|
| Disclosure checklist | Answer each requirement against the draft; decide "not applicable" and "if material" calls | review-assurance, expert-judgment | 1,200-1,500 requirements in one product's checklist; fatigue; last year's checklist rolled forward [TR-DISCLOSURE-2026] | Vendor products, beta figures (`#01`-`#04`) |
| Casting, cross-referencing, tie-out | Foot, cross-check and agree figures; repeat on every draft | review-assurance, data-reporting | 4-5 drafts per engagement; ~1,200 h a year on first drafts at one firm [CASEWARE-HLB-2025] | Two named firms, measured (`#06`); ST-13 |
| Other information, management report | Read front-half text for consistency and statutory content | review-assurance | Manual and checklist-based; late edits break cross-references [HAMBURG-FABIAN-2026; FIELDGUIDE-DISC-2026] | One peer-reviewed study (`#05`) |
| Subsequent events | Events after the balance-sheet date, adjusting or not [PCAOB-AS2801] | expert-judgment, research-synthesis | Reading minutes, legal letters, interim figures | None (§4) |
| Going concern | Evaluate substantial doubt / management's assessment [PCAOB-AS2415; IAASB-ISA570-2025] | expert-judgment | Significant judgment; regulators ask for more scepticism | Experiments only (`#10`, `#11`) |
| Written representations | Obtain management's letter | document-production, client-interaction | Letters left in an inbox, not on file [ICAEW-REPLETTER-2026] | None (§4) |
| Summary of misstatements | Accumulate and evaluate uncorrected misstatements | data-reporting, expert-judgment | Not described in the inputs | None (§4) |
| Manager and partner file review | Clear notes, check completeness, sign-off readiness | review-assurance, coordination-scheduling | Review re-performs the work; gaps found late [FIELDGUIDE-QR-2026] | Demos, announcements (`#08`) |
| Engagement quality review | Objective evaluation of significant judgments; concurring approval [PCAOB-AS1220; IAASB-ISQM2-2020] | review-assurance, expert-judgment | 42% of inspected firms had an EQR deficiency comment (2022) [PCAOB-EQR-2023] | None for the reviewer (§4) |
| KAMs / CAMs | Select from matters communicated to the committee; draft the wording | expert-judgment, document-production | Usefulness contested [PCAOB-AGENDA-2026]; CAM count per report declining [PCAOB-PIRCAM-2022] | Research on identification only (`#12`) |
| Audit committee communications | Required communications (AS 1301, ISA 260) | client-interaction, document-production | Findings in 11% of listed audits where inspected in 2025, 4% in 2024 [IFIAR-SURVEY-2026] | One firm statement (`#09`) |
| Opinion and report drafting | Draft and issue the auditor's report | document-production | PwC: report "still looks the same" [CFODIVE-PWC-2026] | None in external audit; internal audit (`#14`) |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`, or a process that stops existing).
**Coverage:** assist 6, augment 9, automate 1, delegate 2 (both ideas). Step 15, process 3, model 0. No evidence was
found for reinvent; nobody sells completion as an agent-delivered service, and no step has stopped existing.

**Disclosure checklist**
- Improve: `#01` AI first pass with cited answers (Caseware, Thomson Reuters, Ideagen, DataSnipper): 2.7 h saved per
  run in beta; ~30% of eligible TR customers. `#02` Big Four platform engines (KPMG Financial Report Analyzer,
  Deloitte Omnia), announced. `#03` AI second look at a completed checklist, flagging divergence.
- Frontier: `#04` AI proposing "No" and "Not applicable" calls (TR roadmap). This is where judgment lives.

**Statements: casting, tie-out, drafting**
- Automate: `#06` Caseware Validate at HLB Mann Judd Perth (~600 h a year) and MHA (casting 25 to 12 min, zero
  false positives in a head-to-head trial); Suralink tie-out. PwC's fund-audit tie-out tool is ST-13.
- Improve, process scope: `#07` Fieldguide Field Financials drafts from prior year and live trial balance with
  continuous tie-out (announced; raises a non-attest question if the auditor drafts).
- Ideas: `#15` LLM finds statement errors and the standard breached; `#16` XBRL consistency. Both benchmarks show gaps.

**Other information**
- Improve: `#05` an unnamed German Big 4 firm links management-report passages to statutory requirements; auditors perceive
  gains on standardised tasks, limits on nuance and discretion.

**Review, sign-off and documentation**
- Improve: `#08` file-review assistant (Caseware Verity, Fieldguide Field Reviewer), announced. `#13` GenAI drafts
  of memos and preliminary conclusions, with source checks; `#14` Uniper internal audit uses ChatGPT for reporting
  (50-80% efficiency estimate, several processes).
- Delegate (ideas): `#17` a reviewing agent checks the preparing agent; `#18` agent completes and reviews
  workpapers (FinancialAuditBench: much done well, some incorrect documentation).

**Going concern, KAMs, audit committee**
- Improve: `#10` model or LLM going-concern signal (BDO Netherlands experiment: no accuracy or speed gain); `#11`
  idea: ISA 570 tools for sensitivity analysis; `#12` idea: LLM proposes KAM/CAM candidates (~37% overlap in one
  study); `#09` PwC tool analyses audit committee communications (announced, function unclear).

## 4. Open questions: steps with no public AI evidence

Each step below was searched for and returned only standards, exam material or unrelated
items. Absence of public evidence is not proof no firm does it. Do not offer invented use cases; ask.

| Step | What the research found | Probe |
|---|---|---|
| Subsequent events | Nothing on AI reading post-year-end minutes, legal letters or interim figures. Closest analogue: FRC worked example summarising board minutes, a planning use [FRC-GENAI-2026] | "How do you scan for events after year end today, and would a tool that reads minutes and new filings help, or is the risk in what management doesn't write down?" |
| Written representations | Nothing on AI-drafted letters. The AICPA aid says that where a service auditor's report is not enough, auditors may obtain AI-related representations from management, such as which AI the entity uses [AT-AICPAPA-2026]; that is about client AI | "Who tailors the representation letter, and have you added anything about the client's own AI use?" |
| Summary of misstatements | Nothing. Adjacent: `#07` flags stale overrides when trial-balance adjustments change | "Where is the summary built, and how often do late adjustments make it stale?" |
| Engagement quality review | Nothing on AI used by the reviewer; firms say supervisors review AI work as before [PCAOB-GENAI-2024] | "Does your EQ reviewer use any AI, and how is that documented, given how often EQR documentation is cited?" |
| KAM / CAM wording | Identification studied (`#12`); drafting not | "Who drafts KAM wording, and would you let a tool propose first drafts from last year's report and the committee papers?" |
| Opinion and report | Nothing; PwC says the report is unchanged [CFODIVE-PWC-2026] | "Is any part of report drafting templated or automated now? Where would you never let AI in?" |
| Going concern, live audits | No 2025-26 firm deployment; only experiments (`#10`). ISA 570 names tools as examples (`#11`) | "Under revised ISA 570, do you use any model to challenge management's forecast, and what goes in the file?" |
| Audit committee communications drafting | Only PwC's analysis tool (`#09`) | "Do you draft committee communications with any AI support, and what do you tell the committee about it?" |
| Final analytics, completion memo | Nothing specific | "What does your completion memo pull together, and how long does it take?" |

## 5. Interview probes

1. **"When the checklist tool marks a requirement identified or not found, who confirms it? Have you re-performed a
   sample to see how often it is wrong in either direction?"** Reveals whether any quality evidence exists; none is
   public, so the firm's own parallel run is the only benchmark (`#01`, `#03`).
2. **"Who owns 'not applicable' and 'if material' calls today, and what would have to be true before a tool proposes
   them?"** Reveals readiness for `#04` and where seniors' time goes.
3. **"What evidence of AI-assisted review stays in the file after lock?"** Reveals documentation risk; Caseware's
   agent does not keep its reasoning and citations after lock [CASEWARE-DCA-DOCS-2026].
4. **"How many drafts of the statements do you review per engagement, and how long does each first pass take?"**
   Reveals the baseline against HLB (3-4 h per full-year set, 4-5 drafts) and whether `#06` pays back.
5. **"Do your tools draft or roll forward the client's statements or footnotes? Who owns them, and how does that sit
   with independence?"** Reveals non-attest and management-responsibility exposure (`#07`; [CCAB-AI-2026]).
6. **"What do your audit committee chairs ask about your AI use, what do you tell them, and has it come up in fee
   talks?"** Reveals transparency practice (§8) and fee pressure.
7. **"Which completion steps is AI explicitly allowed or barred from, and why in each case?"** Reveals policy, and
   whether the gaps in §4 are choice or neglect.
8. **"If one agent prepares and another checks, what does the human reviewer, and the EQ reviewer, attest to? Where
   is that written?"** Reveals readiness for `#17`, and the AICPA point that a second tool does not reduce review duties.
9. **"Has anyone measured review time since tools arrived? Has review gone up while preparation went down?"** Reveals
   whether savings are real; PwC calls them "not that drastic yet" [CFODIVE-PWC-2026].
10. **"How do you train juniors to judge a disclosure when the tool gives them the answer and rationale?"** Reveals
    skill-loss risk [HAMBURG-FABIAN-2026] and whether rationale is used for learning [TR-DISCLOSURE-2026].
11. **"Is going concern changing for you under revised ISA 570 from December 2026?"** Reveals appetite for `#10`-`#11`.

## 6. Metrics and benchmarks

**Named or vendor outcomes (all vendor-published or self-reported)**
- Disclosure checklist: 2.7 h saved per run, average of unnamed beta firms; unit is "per workflow" in another
  Caseware document [CASEWARE-CWX-2026]. TR: ~30% of eligible customers, close to 300 analyses a month [TR-DISCLOSURE-2026].
- Statement review: HLB ~600 h a year, 40-50% on later drafts [CASEWARE-HLB-2025]. MHA: casting 25 to 12 min,
  first pass 58 to 42 min, zero false positives in a two-tool trial (baseline may be the other tool) [CASEWARE-MHA-2025].
- Internal audit (Uniper): 50-80% estimated efficiency across several processes [EULERICH-2025].
- Going concern (BDO NL thesis, 20 cases): model 85%, accountants 77%, LLM-assisted 78%; same speed [LEIDEN-GC-2025].
- CAMs: AI predicted ~37% of auditor-reported CAMs (seminar abstract) [GUO-CAM-2024].

**Baselines (independent)**
- Automated foot and proofing at 39% of 54 US firms; automated report production 17%; not limited to AI [CPACOM-ATR-2025].
- IFIAR 2025, listed public-interest audits with at least one finding, where the theme was inspected: audit
  committee communications 79 of 725 (11%; 24 of 593, 4%, in 2024); presentation and disclosure 41 of 445 (9%);
  going concern 11 of 232 (5%); review and supervision 23 of 420 (5%); audit report 24 of 758 (3%); EQ control
  review 10 of 341 (3%). No finding is linked to AI [IFIAR-SURVEY-2026].
- PCAOB: firms with an EQR-deficiency comment form 37% (2020) to 42% (2022) [PCAOB-EQR-2023]; EQ reviewer hours
  about 1% (large firms) and 3% (small) of audit hours, per the 2018 post-implementation review [PCAOB-PIR1220-2018].
- Audit committee chairs (250+): 90% say the auditor discussed CAMs [PCAOB-ACCHAIRS-2026].
- GPPC networks report ~30% year-on-year growth in AI-enabled tools for 2025 [IFIAR-TTF-2026].

**Sentiment and readiness (surveys)**
- DataSnipper (vendor, 200+): 73% call AI essential, 13% have it in real workflows; 80% comfortable with AI
  extracting data, 38% with AI signing off [DATASNIPPER-AIREPORT-2026].
- Deloitte/CAQ (248 committee members): AI governance top-three for 75% (35% a year earlier); 56% confident they
  can oversee it [DELOITTE-ACPR-2026; AT-ACPR-2026]. CAQ partner pulse: AI governance the top committee challenge at
  57% [BOARDMEMBER-CAQ-2026].
- Secondary academic findings (Fedyk et al. 2022, via the Japan FSA paper; original not read): one standard deviation more AI
  investment, 5.0% lower likelihood of report reissuance and 0.9% lower fees [FSA-DP-2025].

**What to measure:** reviewer override rate on checklist answers; misses found in a parallel manual run; review hours
per draft; review notes and rework; time from draft to sign-off; inspection and internal review findings on
disclosures and committee communications. Hours saved alone says nothing about quality.

## 7. Guardrails

**No regulator bars AI in completion and none has a completion-specific rule.** Keyword checks of AS 2415, AS 2801,
AS 1301, AS 3101 and AS 1220 found no mention of technology (a keyword check, not a legal reading).
- **FRC (UK, 30 Mar 2026):** first regulator guidance on generative and agentic AI. Risks: deficient output
  (omission, hallucination, distortion), misuse of output, non-compliant methodology. Mitigations: design,
  certification and recertification, training, human review at control points. Its worked examples are not
  completion steps [FRC-GENAI-2026; FRC-NEWS-2026].
- **AICPA practice aid (13 Oct 2026):** the auditor remains responsible for the audit and opinion;
  one AI tool may help evaluate another without reducing supervision and review; AU-C 210 does not require naming
  AI tools in the engagement letter [AICPA-PA-2026; AT-AICPAPA-2026].
- **ISA 220 (Revised):** overreliance on automated tools and automation bias impede scepticism [IAASB-ISA220-2020].
- **ISA 570 (Revised 2024), effective for periods from 15 Dec 2026:** names automated tools as examples, not
  requirements (`#11`) [IAASB-ISA570-2025].
- **PCAOB:** going concern on the standard-setting agenda; research on audit committee communications; a further
  CAM review planned; no AI proposal [PCAOB-AGENDA-2026; TR-PCAOBAGENDA-2026]. 2024 staff outreach (not Board
  policy): some firms barred GenAI from audit procedures; some had not changed supervision policies [PCAOB-GENAI-2024].
- **IFIAR (Apr 2026):** firms say audits will stay "human-led"; IFIAR asks them to show it, e.g. named people for
  decision checkpoints and review of autonomous decisions [IFIAR-TTF-2026].
- **IAASB documentation material (2020)** on automated tools under ISA 230 [IAASB-NAM-2020].

**Design guardrails seen in tools:** cited evidence per answer; flag-not-answer when unsure; nothing written to the
file without acceptance; indeterminate flags; deterministic rules for tie-out; marked-up audit trail (`#01`, `#06`).

**Steps that stay with a person:** applicability and materiality calls; the going-concern conclusion; KAM/CAM
selection; evaluating uncorrected misstatements; EQ concurring approval; the opinion and signature.

## 8. Accountability and the audit committee

The loudest completion discourse is not about AI doing the work but about who answers for it.
- **Accountability does not move.** The FRC says firms and responsible individuals stay accountable
  [BOARDAGENDA-FRC-2026]. A law firm says an erroneous AI output is unlikely to excuse an auditor in negligence;
  documentation of judgement will be critical [DACB-2026]. The PCAOB chair said AI can do "the science, the
  transaction part"; the "art" needs people [ATODAY-LOGOTHETIS-2026].
- **Committees ask first.** Two-thirds of audit partners say committees proactively raised the company's use of AI [BOARDMEMBER-CAQ-2026]. Chairs
  want insight on AI in financial reporting, and several asked about fees [PCAOB-ACCHAIRS-2026]. CPAB's forums:
  transparency, scepticism, fees, talent, and an expectation-gap risk if AI-enabled audits are seen as doing more
  than auditors are responsible for [CPAB-AC-2026].
- **Guidance tells committees what to ask:** how the auditor uses GenAI and agents and assures quality
  [KPMG-ACAGENDA-2025]; how the company's AI affects estimates and disclosures [CAQ-ACI-2026-03]; how AI-assisted judgments are
  documented [TCC-PCAOBQ-2026]. IFIAR encourages auditors to explain how technology affects decisions [IFIAR-TTF-2026].
- **Regulators ask auditors too:** the SEC chief accountant asks how AI improves engagement quality and wants
  independence rules to stay fit for purpose [KPMG-HOHL-2026].
- **Implication:** a firm using `#01`-`#08` should be ready to explain to the committee which tools ran, what they
  decided and who checked; `#09` is the only tool aimed at the communication itself.

## 9. Roles and how they evolve

- **Preparers become reviewers.** Vendors pitch a move from searching to reviewing [CASEWARE-CWX-2026]; Fieldguide
  argues review hours rise at first (vendor view, not measured) [FIELDGUIDE-REVIEW-2026].
- **Seniors move to judgment.** HLB: any team member runs the first pass, seniors focus on disclosures [CASEWARE-HLB-2025].
- **Juniors learn from rationale, or lose skills.** TR and Caseware's Withum beta partner present rationale as
  teaching [TR-DISCLOSURE-2026; CASEWARE-CWX-2026]; auditors at the German Big 4 firm worry about over-reliance and
  skill loss [HAMBURG-FABIAN-2026]; a registered-report proposal predicts lower motivation and judgment quality when
  auditors shift from preparing to reviewing, with no results yet [HOLMSTROM-PETERS-2024]. The acting PCAOB chair
  said juniors may need new paths to build scepticism [AT-PCAOBPE-2025].
- **New skills and roles:** MHA's Technical Director for Audit Data Analytics chose its tool [CASEWARE-MHA-2025];
  PwC hires engineers and dual-track CPA/data-science candidates [PWC-AT-2025]; a Deloitte audit manager posting asks
  for validating AI outputs before they enter workpapers [DELOITTE-JOBCAIRO-2026].
- **Talent supply:** a TR executive says 75% of audit partners are due to retire within ten years (vendor claim)
  [TR-STATE-2026].

## 10. Frontier

- **2025-04-22** KPMG: Financial Report Analyzer; more agents within 12 months, incl. FS analysis (no follow-up) [KPMG-CLARA-2025].
- **2025-10-28** PwC hopes for a tool for every step in 2026, incl. FS review and tie-out [PWC-AT-2025].
- **2026-03-30** FRC generative and agentic AI guidance [FRC-GENAI-2026].
- **2026-04-07** EY: agents in all audit phases; end-to-end support expected by 2028 [EY-CANVAS-2026].
- **2026-04-20** IFIAR: agentic AI "may evolve" toward orchestrating audit activities [IFIAR-TTF-2026].
- **2026-04-30** PCAOB Investor Advisory Group asks for the most decision-useful 2025 CAMs/KAMs [PCAOB-IAG-2026].
- **2026-05-20 / 06-17** Caseware launches Verity; CwX goal of automating up to 50% of the engagement workflow
  [CASEWARE-LAUNCH-2026; CASEWARE-CWX-2026].
- **2026-06-24** Deloitte unifies Omnia agents, incl. disclosure evaluation [DELOITTE-OMNIA-2026].
- **2026-08-12** Fieldguide Field Financials; tie-out and disclosure agents due "in the fall" [FIELDGUIDE-FINANCIALS-2026].
- **2026-09-23** TR Disclosure Review launches; "No" and "Not applicable" calls next [TR-DISCLOSURE-2026].
- **2026-09-30** PCAOB agendas: going concern, audit committee communications research [TR-PCAOBAGENDA-2026].
- **2026-10-07** PwC: savings modest; committee-communications tool for 2026 year-ends [CFODIVE-PWC-2026].
- **2026-10-13** AICPA practice aid; sections on risk and evidence to follow [JOFA-AIPA-2026].
- **2026-12-15** Amended AS 1220 takes effect; ISA 570 (Revised 2024) applies to periods beginning on or after this date [IAASB-ISA570PAGE-2025; PCAOB-AS1220].

## 11. Common objections

- **"The figures are vendor marketing."** Mostly true: the only named, measured results (HLB, MHA) are
  vendor-written case studies. Ask for a parallel run on the firm's own files; a TR executive says firms must build
  their own testing muscle, not rely on demos [TR-STATE-2026].
- **"A checklist isn't judgment."** Correct: a checklist proves coverage, not adequacy [FIELDGUIDE-DISC-2026]. Use AI
  for matching and tie-out, and spend freed senior time on the conditional calls (`#04` stays with people).
- **"It will miss a disclosure and we'll get an inspection finding."** No miss rate is published. Use flag-not-answer
  tools and a divergence check (`#03`); keep the reviewer's evidence trail after lock.
- **"Savings aren't real."** PwC calls its savings so far "not that drastic yet" [CFODIVE-PWC-2026]; HLB reports ~600 h
  on a narrow, repetitive step. Start where drafts repeat.
- **"Juniors won't learn."** A real concern [HAMBURG-FABIAN-2026]; vendors argue rationale teaches [TR-DISCLOSURE-2026].
  Design review so juniors explain the answer, not accept it.
- **"The committee will think AI makes the audit more than it is."** CPAB flags that expectation gap [CPAB-AC-2026].
  Explain tools, limits and human checkpoints up front (§8).
- **"Regulators will penalise AI use."** None prohibits it; all keep accountability with the auditor [FRC-NEWS-2026;
  AICPA-PA-2026]. Documentation is the exposure.
- **"Drafting the client's statements is not our job."** Right to ask: `#07` raises management-responsibility and
  independence questions the vendor does not address [CCAB-AI-2026].

## 12. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML (all opened and checked):
- AICPA-PA-2026: AICPA & CIMA, AICPA releases guidance on AI in financial reporting and auditing, 2026-10-13, https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing
- AT-ACPR-2026: Accounting Today, Audit committees focusing on emerging risks like AI, 2026-09-22, https://www.accountingtoday.com/news/audit-committees-focusing-on-emerging-risks-like-ai
- AT-PCAOBPE-2025: Accounting Today, PCAOB warns auditors about AI and PE, 2025-12-09, https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe
- ATODAY-LOGOTHETIS-2026: Accounting Today, PCAOB's Logothetis: AI can only do part of an auditor's job, 2026-09-22, https://www.accountingtoday.com/news/pcaobs-logothetis-ai-can-only-do-part-of-an-auditors-job
- BOARDMEMBER-CAQ-2026: Corporate Board Member, What audit partners are seeing on AI, 2026-07-15, https://boardmember.com/?p=50023
- CAQ-ACI-2026-03: CAQ, Audit Committee Insights March 2026, 2026-03-17, https://www.thecaq.org/audit-committee-insights-march-2026
- DACB-2026: DAC Beachcroft, AI: the future of audit, 2026-07-13, https://www.dacbeachcroft.com/en/what-we-think/ai-the-future-of-audit
- DELOITTE-JOBCAIRO-2026: Deloitte Middle East, Manager, Audit (Cairo, FSI) job posting, 2026-05-17, https://middleeastjobs.deloitte.com/careersME/PipelineDetail/Cairo-Egypt-Manager-Audit-Audit-Assurance-Cairo-FSI/254184
- EY-CANVAS-2026: CPA Practice Advisor, EY rolls out agentic AI in assurance, 2026-04-07, https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/
- FRC-NEWS-2026: FRC, Innovative new guidance supports audit firm adoption of emerging AI technologies, 2026-03-30, https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/
- FSA-DP-2025: Japan FSA Financial Research Center, DP2025-3 on generative AI in audit, 2025-07, https://www.fsa.go.jp/frtc/english/seika/discussion/2025/DP2025-3_Eng.pdf
- HOLMSTROM-PETERS-2024: PCAOB conference registered-report proposal, 2024-06, https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf
- ICAEW-REPLETTER-2026: ICAEW, Letters of representation: a key protection for auditors, 2026-05-14, https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/letters-of-representation-a-key-protection-for-auditors
- JOFA-AIPA-2026: Journal of Accountancy, AICPA publishes practice aid, 2026-10-13, https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/
- KPMG-HOHL-2026: KPMG Board Leadership Center, Q&A with Kurt Hohl, 2026-05-26, https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html
- PCAOB-AS2415: PCAOB, AS 2415 Going Concern (current text, read via a text mirror), 2026, https://pcaobus.org/oversight/standards/auditing-standards/details/AS2415
- PCAOB-AS2801: PCAOB, AS 2801 Subsequent Events (current text, read via a text mirror), 2026, https://pcaobus.org/oversight/standards/auditing-standards/details/AS2801
- PCAOB-IAG-2026: PCAOB investor advisory on CAM/KAM examples, 2026-04-30, https://pcaobus.org/resources/information-for-investors/investor-advisories/investor-advisory--pcaob-investor-advisory-group-requests-public-submit-examples-of-critical-or-key-audit-matters-5-2026
- PCAOB-PIR1220-2018: PCAOB, Post-implementation review of AS 1220, 2018-12-19, https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/pir/documents/pir-as1220-board-report.pdf
- TCC-PCAOBQ-2026: TheCorporateCounsel.net, PCAOB-related questions to ask your auditor, 2026-07-09, https://www.thecorporatecounsel.net/blog/2026/07/audit-committees-pcaob-related-questions-to-ask-your-auditor.html
- TR-PCAOBAGENDA-2026: Thomson Reuters, PCAOB unveils first agendas under Logothetis, 2026-10-01, https://tax.thomsonreuters.com/news/pcaob-unveils-first-standard-setting-rulemaking-agendas-under-chairman-logothetis/
- TR-STATE-2026: Thomson Reuters, The state of AI in audit 2026, 2026-03-30, https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/
