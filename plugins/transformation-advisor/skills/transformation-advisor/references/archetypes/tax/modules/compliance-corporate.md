# Corporate direct-tax compliance (tax)

Last reviewed 2026-10-17. Use cases live in `../use-cases/compliance-corporate.yaml` (24 entries). Ids are shortened
here: `#05` means `tax-compliance-corporate-05`. Source keys in brackets, such as [PWC-MEGNA-2025], are given in full
in the YAML or in §10. **Evidence is thin.** No entry has a measured outcome from a named organisation (no grade A);
3 of 24 entries are grade B (a named deployment without published numbers). Sources re-verified 2026-10-17.
Nearly every figure here is vendor-published or self-reported. Say so when you quote one.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Corporate income tax compliance done in house by corporate tax departments and by large firms for corporate
clients: the federal return (Form 1120), international information returns (Forms 5471 and 8858, on foreign
subsidiaries and branches), state apportionment (splitting income among states) and state income tax returns,
return workpapers and review, credits and incentives (above all the R&D credit and Form 6765 Section G), and
estimated payments and the tax calendar. Individual and small-business returns, ASC 740 provision, notices and
stand-alone tax research sit in other tax modules (compliance individual-business, provision, controversy,
research-advisory). A Thomson Reuters Institute recap of the April 2026 TEI seminar says "Does this work?" is
effectively settled and the harder problems are silent failures, ownership, training and token costs [TEI-TAXTECH-2026].

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Data collection and tax-sensitising | Extract trial balances and ledgers from many entities; map accounts to the tax chart of accounts | data-reporting, transaction-processing | Weeks of manual mapping at multinationals [EY-COMPL-2024]; Baker Tilly states 63% of departments still gather ERP/GL data manually and 76% rely heavily on Excel (survey unnamed) [BAKERTILLY-2026] |
| Source-document intake | Read K-1s (partnership income statements), foreign financials, third-party data | transaction-processing | Many formats; footnotes need interpretation; extraction errors flow silently into the return [TAXADVISER-WERFEL-2026] |
| Book-to-tax adjustments | M-1/M-3 schedules (reconciling book income to taxable income), depreciation, E&P | transaction-processing | Rules-heavy; mostly rules-based automation today (Baxter's Corptax bots) [CSC-BAXTER-2026] |
| Federal return and workpapers | Roll forward prior-year workpapers; prepare the 1120 in the compliance engine (ONESOURCE, Corptax) | document-production | Staff-level preparation followed by layers of review [EY-COMPL-2024] |
| International forms | 5471, 8858, foreign tax credit forms | transaction-processing, data-reporting | Volume; no AI-specific case found, only rules-based bots (200+ reports in 2 hours, vendor-published) [CSC-BAXTER-2026] |
| State apportionment and returns | Apportion income, file state returns | transaction-processing | Only one source describes AI here (Byron) [BYRON-2026] |
| Credits and incentives | R&D credit studies; Form 6765 Section G business-component detail | data-reporting, expert-judgment | Interview-based studies take 200+ hours a year (vendor) [TR-NEOTAX-2025]; new Section G detail [IRS-F6765-INSTR-2025] |
| Review and sign-off | Preparer and reviewer checks, analytics, sign-off | review-assurance | Growing volume; quiet, polite AI errors [TEI-TAXTECH-2026] |
| Calendar, extensions, estimated payments | Track due dates and rule changes across entities | coordination-scheduling | Spreadsheet trackers [OPENAI-USTAXOPSJOB-2026]; penalties more common in reactive departments [TR-CORPTAX-2025] |
| Return-to-provision true-up | Reconcile the filed return with the provision | data-reporting | Mainly the provision module |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment one step), automate (no person on the normal
path), delegate (an agent owns a multi-step outcome), reinvent (the process or the service model changes).
Coverage: assist 5, augment 12, automate 3 (one grade B, two ideas), delegate 4. Scope: step 12, process 8,
model 4. Automate has almost no deployed evidence.

**Data intake and mapping**
- Improve: `#01` AI maps ledger accounts to tax accounts; EY says weeks become two days with review (illustration).
  `#02` PwC agents interpret K-1 footnotes, state a confidence level and log override reasons (grade B; adjacent
  asset-management setting). `#17` analysts build their own pipelines with AI coding tools (about 15 minutes against
  about two months in the IT queue, as attendees described it).
- Automate: `#10` Oxford Industries' tax team deploys Savant's governed automation platform (grade B; a pre-event
  vendor release names the team but not its workflows; Savant's demos covered reconciliation, extraction and lineage,
  and also indirect tax).
- Ideas: `#23` a gate that checks inputs for contradictions before any calculation; `#22` a deterministic engine
  computes while a model translates rules into tested logic.

**Return preparation and workpapers**
- Improve: `#11` cited research inside ONESOURCE and Bloomberg Tax workpapers; `#18` PwC's model explains inputs,
  outputs and assumptions so the reasoning chain replaces the memo, and approved logic is locked (grade C: the named
  deployment is an effective-tax-rate model, a provision process); `#19` a record of AI use and verification with each AI-assisted item.
- Delegate: `#06` agents roll forward workpapers and prepare review-ready 1120, 1120-S and 1065 returns, including
  book-to-tax and state apportionment (Byron; >97% extraction accuracy is the company's claim).
- Reinvent: `#05` AI prepares, staff review, and fewer review layers may be needed (EY's stated direction; PwC keeps
  multi-eye review for complex outputs). `#07` OpenAI's tax team sets out to move from outsourced preparation to
  agent-driven computation of 1120, 1065, 5471 and state returns (grade B; job listings and a live demonstration of
  automation pipelines).

**Credits and incentives**
- Reinvent the process: `#09` Neo.Tax in ONESOURCE builds contemporaneous R&D evidence from project, payroll and
  ledger data and populates Form 6765 with Section G [TR-CORPAI-2026]. Vendor figures: weeks to days; 50-75% lower
  fees and 20-30% lower FIN 48 reserves, "companies report", no sample [TR-NEOTAX-2025].

**Review, risk and sign-off**
- Improve: `#03` year-on-year anomaly flags on returns, source data and reconciliations; `#04` validation agents
  critique other agents' output; `#13` pre-filing audit-risk prediction (a Corptax roadmap item).
- Reinvent the process: `#21` gated rollout with full logging, override-rate and error thresholds and unaided
  competence checks (a worked example by former IRS Commissioner Werfel, not a standard).
- Idea: `#24` continuous, always-on monitoring in place of batch preparation (EY, Deloitte).

**Calendar, estimated payments and modelling**
- Improve: `#12` agents track rule and form changes and the filing calendar (Bloomberg Compliance Tracker, Orbitax
  Tax Flows). `#14` continuously updated effective-rate and cash-tax models (Baker Tilly; provision-heavy).
- No source describes AI calculating or scheduling corporate estimated payments or extensions.

**Operating and service model**
- Delegate/reinvent: `#08` firm agent platforms (EY Tax Agent Factory, PwC Agent OS, KPMG Digital Gateway with
  Claude). `#15` compliance bought as an AI-enabled managed service, with in-house teams asking providers to
  disclose AI use. `#16` idea: value-based pricing in place of hours. `#20` approved enterprise tools with vendor
  terms that bar training on company data and require notice of model changes.

## 4. Interview probes

1. **Walk me through how ledger data reaches your return software. Which steps are rules, which are a person,
   which are AI?** Reveals whether the bottleneck is data (a vendor, Kognitos, argues data is now the binding
   constraint [KOGNITOS-2026]) and where `#01`, `#10` or `#17` fit.
2. **Which inputs still arrive as K-1s, foreign financials or spreadsheets you do not control, and who keys them?**
   Shows the document-intake load for `#02` and where extraction errors could enter silently.
3. **Who owns AI in tax: tax, finance or IT?** At TEI, 2 of more than 50 attendees said tax does
   [TEI-TAXTECH-2026]. No owner usually means no logs, no metrics and stalled pilots.
4. **What can a reviewer see on an AI-assisted workpaper: prompt, output, sources, what was checked?** Tests
   readiness for an examiner or auditor (`#19`) and for OPR's documentation expectation [IRS-OPR-2026].
5. **What review layers apply to AI-prepared work, and do you record overrides? Do you know the rate?** In a
   worked example, an override rate below 5% signals rubber-stamping [AICPA-WERFEL-2026]; no rate means no quality evidence (`#21`).
6. **For R&D credits: where does project and time data live today, and can you report by business component for
   Section G? Who signs off the four-part test?** Separates `#09` readiness from a data-capture project.
7. **Where has a tool failed quietly in the last year, and what did you change?** Surfaces silent-failure
   experience and whether validation (`#04`, `#23`) exists.
8. **Do your outside compliance providers use AI, and has it changed fees or what you receive?** 77% of business
   tax departments want providers to use GenAI, and 59% "aren't sure" about GenAI use (the source's wording is
   ambiguous about whose use) [TR-TENSIONS-2025] (`#15`, `#16`).
9. **Which AI tools may staff use with return data, and how would you know about use outside that list?**
   Reveals shadow-AI exposure under IRC 7216 and 6713 (`#20`).
10. **Have you measured anything before and after: cycle time, review rework, notices, penalties?** Only 20% of
    professional-services organisations measured GenAI ROI in 2025 [TR-TENSIONS-2025], though two-thirds of tax
    departments say they track time savings [TR-TAXTALENT-2026]; it decides whether a business case can be shown.
11. **How do you expect tax authorities' AI to change audit timing and data requests?** Gauges `#13` and `#24`
    interest; the IRS already scores some 1120 lines with machine learning [TIGTA-2025].

## 5. Metrics and benchmarks

What to measure: cycle time per return or entity; hours on data collection and mapping; review rework and
override rates; errors found in review and after filing; notices and penalties; R&D credit study hours and
examination adjustments; share of AI-assisted items with a verification record. None of these has a published
AI benchmark for corporate returns.

| Figure | What it counts | Source and caveat |
|---|---|---|
| 67% | Corporate tax departments not using GenAI (288 surveyed) | [TR-CORPTAX-2025], vendor survey, 2025 |
| 58% (51% a year earlier) | Departments saying they are under-resourced | [TR-CORPTAX-2025] |
| 56% vs 31% | Reactive vs mainly proactive respondents whose departments incurred penalties | [TR-CORPTAX-2025]; an association, not a tool effect |
| 17% / 21% / 45% | Specific AI and data policy / covered by general policy / no relevant policy | [TR-TENSIONS-2025]; sample not stated |
| 20% | Organisations measuring GenAI ROI (professional services broadly) | [TR-TENSIONS-2025] |
| 34% (from 56%) | Satisfaction with tax technology | [TR-TAXTALENT-2026], with TEI |
| Two-thirds; 55% | Departments measuring time savings and efficiency gains; tracking accuracy improvements | [TR-TAXTALENT-2026] |
| 50% (from 59%) | Departments providing technology training in 2025 | [TR-TAXTALENT-2026] |
| 67% | Respondents saying technology investment enabled more proactive work (170 tax leaders) | [TR-CORPTECH-2026] |
| 71%; 66% | German tax departments using AI tools; AI users reporting noticeable time savings | [KPMG-DE-2026]; sample not stated |
| 77% | Tax leaders requiring 90%+ accuracy before trusting AI with tax processes | [DELOITTE-LU-2025]; sample not stated |
| 48%; 36% | Apply governance controls before production; track model documentation and lineage | [RSM-AISURVEY-2026]; mid-market, sample not stated |
| 2 of 50+ | Hands raised: tax owns AI implementation | [TEI-TAXTECH-2026]; one seminar |
| Weeks to days; 50-75%; 20-30% | Neo.Tax filing time; fees vs accounting firms; FIN 48 reserves | [TR-NEOTAX-2025]; vendor, "companies report" |
| >97% | Byron extraction accuracy (not return correctness) | [BYRON-2026]; company claim |
| 32.35% | Best model's fully correct simplified 1040s (51 cases) | [COLUMN-TAXCALCBENCH-2025]; individual returns, vendor authors |
| 63-76% | Strong models answering through contradictory inputs with no warning | [SADOWSKI-VERIFY-2026]; benchmark cases |
| 200+ reports, 2 h vs 80 h | Baxter international reports with rules-based Corptax bots | [CSC-BAXTER-2026]; not AI, vendor case |

Not found anywhere: error rates, override rates, parallel-run results or inspection findings for AI on corporate
returns, Forms 5471/8858, state returns or Section G.

## 6. Guardrails

- **Existing duties apply; no AI-specific rule for corporate returns.** IRS OPR Alert 2026-19 (24 Jun 2026) maps
  Circular 230 onto AI: review all AI output before it reaches a client or the IRS (10.22 due diligence); fees
  must not bill time not spent (10.27); understand the tool (10.35); firm procedures and documentation (10.36);
  no reliance on AI authorities without verification (10.37); IRC 6713 and 7216 on disclosure of return
  information [IRS-OPR-2026]. It addresses practitioners, not in-house teams directly.
- **Preparer reliance.** Treas. Reg. 1.6694-1(e) allows good-faith reliance on taxpayer-furnished information but
  not ignoring apparent errors; the sources do not say how it applies to AI output [ECFR-1694-1].
- **Section G.** Required for tax years beginning after 2025, with exceptions for qualified small businesses and
  small filers; report at least 80% of QREs by business component, but no more than 50 components
  [IRS-F6765-INSTR-2025]. Records must
  be in "sufficiently usable form and detail" [ECFR-141-4]. Sources disagree on timeline wording; use the IRS
  instructions for the filing year.
- **Risk framework.** Werfel's framework, with a 20-risk register for tax authorities and a 15-risk register for
  preparers [TAXADVISER-WERFEL-2026], and the AICPA's Council on AI Risk in Tax (CART, 23 Sep 2026) [AICPA-CART-2026];
  the article states it is the author's view, not AICPA policy.
- **UK and software.** PCRT guidance: members remain responsible for AI-assisted work and must apply professional
  judgement; entering client data into a public AI model without consent is likely a breach of confidentiality
  [ICAEW-PCRT-2026]. HMRC expects AI tax software to keep monitoring and version control
  [HMRC-GENAI-2026].
- **Courts.** *Clinco* (T.C. Memo. 2026-16): three of four cited cases likely fabricated; no formal sanction
  [TAXCT-CLINCO-2026].
- **Audit trail.** Deloitte says agentic corrections to source data must be written back to the system of record
  [DELOITTE-TTT-2026].

Steps that need human judgment: sign-off of every return; whether an R&D business component qualifies and the
four-part test; positions and disclosures; resolving flagged anomalies and abstentions; approving mapping rules
and locked logic; deciding remediation on any alert; fee basis and provider terms.

## 7. Roles and how they evolve

- **Preparer to reviewer.** EY says staff will monitor AI and review initial outputs [EY-COMPL-2024]; PwC says one
  reviewer replaces a group huddle on novel items, with logged overrides [PWC-MEGNA-2025]; OpenAI's 2026 listing
  focuses the manager on "review, validation, and improvement of tax outputs" [OPENAI-USTAXOPSJOB-2026].
- **Tax people as builders.** OpenAI frames a role as "from compliance executor to process architect"
  [OPENAI-TAXCOMPLIANCEJOB-2025]; analysts build pipelines themselves [TRINST-TEIAUDITOR-2026]. Risk: workflows
  nobody can explain after the builder leaves [TEI-TAXTECH-2026].
- **Hiring.** 62% of 2025 new hires emphasised tax expertise over technology, after a 2024 tilt to tech hires;
  hybrid roles are rising [TR-TAXTALENT-2026]. Corporate departments often rely on dual tax and technology roles
  [TR-DUALROLES-2025].
- **Headcount.** Sala argues teams will not shrink much because AI cannot carry culpability and tax practice is
  more than preparation [SALA-TAXNOTES-2026]. KPMG Germany: 58% expect stable domestic headcount, 72% abroad
  [KPMG-DE-2026]. Bloomberg Tax noted firm platforms could dampen future staff needs [BTAX-BIG4-2025].
- **Skills.** EY sees a divide between experienced staff who spot AI problems and newer staff who over-rely
  [BTAX-EYGRIP-2025]; Werfel lists skill erosion as a workforce risk [TAXADVISER-WERFEL-2026].
- **New owners.** A named AI governance owner, a tax technology owner of tools and measurement (`#20`, `#21`), and
  tax directors as informed buyers of AI-enabled services (`#15`).

## 8. Frontier

- **2025-03-24:** EY reported planning up to 150 agents for 80,000 tax professionals [BTAX-BIG4-2025].
- **2025-06-05:** OpenAI lists a role to build "the world's first fully autonomous corporate tax reporting system"
  [OPENAI-TAXCOMPLIANCEJOB-2025].
- **2025-11-05:** Thomson Reuters launches ONESOURCE+, an AI compliance network [TR-ONESOURCEPLUS-2025].
- **2025-11-25:** EY announces Tax Labs and the Tax Agent Factory [EY-TAXLABS-2025].
- **2026-03:** TEI Midyear's preliminary programme schedules hands-on Tax Labs on research credit automation,
  notices and Excel analysis [TEI-MIDYEAR-2026].
- **2026-05-04:** TEI Tax Tech recap: silent failures, no owner, failed training, rising token costs [TEI-TAXTECH-2026].
- **2026-05-20:** KPMG and Anthropic announce Digital Gateway with Claude, tax clients first [KPMG-ANTHROPIC-2026].
- **2026-05-27:** Byron launches agents for 1120, 1120-S and 1065 preparation [BYRON-2026].
- **2026-06-24:** IRS OPR issues Alert 2026-19, introductory guidelines on AI use in tax practice [IRS-OPR-2026].
- **2026-06-30:** First GloBE Information Returns due, compressing the direct-tax calendar [TR-CORPAI-2026].
- **2026-09-08:** The AICPA seeks IRS clarity on OPR's fee language [AICPA-FEES-2026].
- **2026-09-23:** AICPA and Werfel launch CART [AICPA-CART-2026].
- **2026-10-02:** Neuro-symbolic research matches all 51 held-out TaxCalcBench returns [HAN-LAWORDER-2026]; the
  same day the IRS CEO's "AI-first IRS" is reported [IRS-AIFIRST-2026].
- **Tax years beginning after 2025:** Section G becomes required [IRS-F6765-INSTR-2025].

Direction: data pipelines and governance before agents; deterministic engines with model layers rather than
model-only calculation; firms selling agent platforms; authorities that see more data sooner.

## 9. Common objections

- **"It fails quietly."** True: an agent told an attendee it could not open a file and had been telling them what
  they wanted to hear [TEI-TAXTECH-2026]; the strongest models answered through injected contradictions in 63-76%
  of benchmark cases [SADOWSKI-VERIFY-2026]. Response: validation agents (`#04`), input gates (`#23`), logged overrides (`#02`) and
  tie-out sampling (`#01`).
- **"AI cannot be accountable."** Agreed by the rules: the signer stays responsible [IRS-OPR-2026] and AI cannot
  carry culpability [SALA-TAXNOTES-2026]. Response: design AI as preparation and evidence; keep sign-off human.
- **"The models get returns wrong."** On simplified 1040s the best model was fully right in about a third of
  cases [COLUMN-TAXCALCBENCH-2025]. Response: compute in the deterministic engine you already run; use AI for
  data, mapping and documentation (`#22`).
- **"AI-only R&D tools won't survive Section G."** A competing human-led adviser argues this, and notes vendor
  liability is typically capped at fees [STRIKETAX-2026]. Response: treat AI as evidence capture; keep the
  qualification judgment with the R&D tax lead (`#09`).
- **"We need 90%+ accuracy first."** 77% of leaders say so [DELOITTE-LU-2025]. Response: measure it; gated rollout
  with thresholds (`#21`) turns the demand into a test.
- **"Token costs will kill the business case."** Raised at TEI [TEI-TAXTECH-2026]. Response: only 20% measure ROI
  [TR-TENSIONS-2025]; set baselines first.
- **"Nobody owns it."** 2 of 50+ say tax owns AI [TEI-TAXTECH-2026]. Response: name an owner before scaling (`#21`).
- **"The fee rule stops value pricing."** Contested: OPR warns against billing time not spent [IRS-OPR-2026]; the
  AICPA says the language is not authoritative and seeks clarity [AICPA-FEES-2026] (`#16`).
- **"Training rollouts fail."** One tool meant to save two hours consumed a day because users were not consulted
  [TEI-TAXTECH-2026]; panellists describe transformation fatigue [TR-TRANSFATIGUE-2025]. Response: involve users;
  start with one step.

## 10. Sources

Full details for every key used in the use cases are in the YAML. Keys cited here that are not in the YAML:

- [TR-CORPTECH-2026] Thomson Reuters Institute, Corporate tax teams eager for AI, but frustrated by pace of change, new report shows (on the 2026 Corporate Tax Department Technology Report, with TEI), 2026-03-16, https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026
- [TR-DUALROLES-2025] Thomson Reuters Institute, Corporate tax departments are hiring dual tax/technology roles, 2025-02-26, https://www.thomsonreuters.com/en/institute/articles/corporate-tax-dual-technology-roles
- [TR-TRANSFATIGUE-2025] Thomson Reuters Institute, The human in the loop: tackling transformation fatigue, 2025-06-03, https://www.thomsonreuters.com/en/institute/articles/transformation-fatigue-tax-tech
- [TR-ONESOURCEPLUS-2025] Thomson Reuters, launch of ONESOURCE+, 2025-11-05, https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-onesource-plus-the-ai-powered-intelligent-compliance-network
- [CSC-BAXTER-2026] CSC Corptax, Baxter International case study (rules-based Corptax bots, not AI; page undated and its copyright year is script-filled, so 2026 is the retrieval year; the text refers to Transition Tax work, so the case is likely several years older), 2026, https://cscglobal.com/service/corptax/case-studies/baxter/
- [IRS-AIFIRST-2026] Nextgov/FCW, Tax chief pushes "AI-first IRS", 2026-10-02, https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/

Most-used keys in this file: PWC-MEGNA-2025 (PwC interview), TEI-TAXTECH-2026 and TRINST-TEIAUDITOR-2026 (TEI
seminar recaps), TR-CORPAI-2026 and TR-NEOTAX-2025 (Thomson Reuters), IRS-OPR-2026 (OPR Alert 2026-19),
IRS-F6765-INSTR-2025 (Form 6765 instructions), AICPA-WERFEL-2026 and TAXADVISER-WERFEL-2026 (Werfel framework),
OPENAI-* (OpenAI job listings), TR-CORPTAX-2025 and TR-TENSIONS-2025 (Thomson Reuters surveys), KPMG-DE-2026.
