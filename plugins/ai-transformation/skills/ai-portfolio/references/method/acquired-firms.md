# Rolling capabilities into acquired firms

Read this when the firm has acquired, or is about to acquire, another firm and wants to move its proven AI
capabilities there: approved tools, workflows from the enablement library, the governance overlay and data
foundations. It is the detail behind `stage-gates.md` §9. Assessing the acquired firm first is the
transformation-advisor's acquisition path (`../../../transformation-advisor/references/method/acquisitions.md`).
Rules 1, 2, 5 and 9 in `SKILL.md` apply throughout. Keys in brackets are listed in §13; most acquisition figures are
vendor-published or self-reported, and no independent measurement of AI value at a roll-up platform was found.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [What moves first: order by dependency](#3-what-moves-first-order-by-dependency)
4. [Readiness checks before each layer](#4-readiness-checks-before-each-layer)
5. [Client-data separation and consent](#5-client-data-separation-and-consent)
6. [Independence checks](#6-independence-checks)
7. [Change management for incoming partners and staff](#7-change-management-for-incoming-partners-and-staff)
8. [Tracking adoption and value in benefits.yaml](#8-tracking-adoption-and-value-in-benefitsyaml)
9. [Describing the platform's AI without overstating it](#9-describing-the-platforms-ai-without-overstating-it)
10. [Question bank and common traps](#10-question-bank-and-common-traps)
11. [Worked example](#11-worked-example)
12. [Output](#12-output)
13. [Sources](#13-sources)

## 1. Goal and exit criteria

**Goal.** Each capability reaches the acquired firm only after what it depends on is in place there, enters the
portfolio at the stage its evidence in that firm supports, and is tracked against the acquired firm's own baseline.

**Exit criteria** for a firm's rollout plan:
- The acquired firm has an assessment (the advisor's unit `units/<target-id>/`), validated or labelled draft.
- Each capability to move is a portfolio item with `unit` set to the acquired firm, its layer (§3), its
  `depends_on`, and an entry stage justified by evidence in that firm.
- Consent, client-data and independence clearances are recorded before any item that moves data or tools (§5, §6).
- Each item past `g3` has adoption and value rows in `benefits.yaml` on the acquired firm's baseline (§8).
- Incoming partners have a written description of the platform's AI with each capability's evidence status (§9).

## 2. How to run it

1. **Read the assessment** of the acquired firm: journey stage per dimension, red flags, foundation items. If none
   exists, hand off to transformation-advisor (acquisition path) first.
2. **Settle the model.** A platform can fully merge firms or sit above firms that keep their own brand and leadership
   and take shared services [NJCPA-PE-2026]. Merged: one stack and one workflow set, sequenced. Umbrella: offer the
   capabilities with evidence and let each firm adopt (advisor synthesis from NJCPA-PE-2026 and GT-AIIMPACT-2026).
3. **Write the integration thesis's short list.** Bain advises focusing integration on a short list of value drivers
   and an order of operations: where to stabilize and integrate, where and when to transform [BAIN-OUTLOOK-2026].
   Hold AI capabilities to the transform list.
4. **Log each capability per firm** through intake (`intake.md`): one item per capability per acquired firm, because
   each firm moves through the gates at its own pace. Id pattern `<capability>-<firm>`; `source` back-links to the
   home item or the advisor's unit `opportunities.yaml`.
5. **Set the entry stage from the acquired firm's evidence,** not the stage reached at home. A capability in
   production at home usually enters at `pilot`: feasibility is shown, adoption and value in this firm are not
   (proposed default). Use the light path where the risk tier allows it (`stage-gates.md` §3.2).
6. **Sequence by layer and dependency** (§3), check readiness before each layer (§4), and hold gates as usual.
7. **Add the firm to the AI inventory** from day one: what runs, who owns it, what stage, what governance
   [GT-AIIMPACT-2026]. In the portfolio, that is the items filtered by `unit`.

## 3. What moves first: order by dependency

RSM puts policy, data centralization and training ahead of use cases after close [RSM-AIDD-2025]. Bain warns that
winners do not get caught up resolving internal complexity in the first wave [BAIN-OUTLOOK-2026]. The layers below
are this skill's ordering (advisor synthesis); each layer depends on the ones above it, and a firm can move through
them as fast as its checks pass.

| Layer | Capabilities | Depends on | Why this order |
|---|---|---|---|
| **0 Clearances** | Client notice and file-transfer consent; tax-return consent for affiliate or central processing; independence screen and monitoring; data-separation rules | Deal structure | Nothing that moves client data or tools is safe without them (§5, §6) |
| **1 Governance overlay** | The platform's `overlay/policy.md` risk tiers and data rules, `overlay/guardrails.md` human-review rules, records of AI use, extended to the firm | Layer 0 | Tools and workflows are approved against the policy; RSM's first wave includes policy [RSM-AIDD-2025] |
| **2 Approved tools and training** | `overlay/tool-catalog.yaml` entries for the firm (personal-assistant tier first); training; an approved alternative for each unsanctioned tool found | Layers 0–1 | Training is in RSM's first wave [RSM-AIDD-2025]; personal productivity alone is "table stakes" [CFOBREW-BAKERTILLY-2026] |
| **3 Data foundations** | Common systems of record, data centralized and governed, connections the workflows need | Layers 0–1 | Siloed data costs time and money before benefits show [RSM-AIDD-2025]; work moves between offices only on common tools and workflows [WK-PE-2025] (vendor view) |
| **4 Library workflows** | Entries from `enablement/workflows/` (shared team skills), then workflow automation on one or two high-volume flows with a baseline and a case count | Layers 2–3 | Current's reported tax pilot gave a figure over a stated count of returns, a design worth copying even though the figure is self-reported [CPAPA-CURRENT-2026] |
| **5 Rebuilt workflows and agents** | Workflow-native redesigns; delegated agents behind the five onboarding gates; new advisory offers | Layer 4 in production in this firm | Baker Tilly's CEO expects the P&L change from rebuilt workflows [CFOBREW-BAKERTILLY-2026] |

## 4. Readiness checks before each layer

Proposed defaults; no source gives thresholds. Record each check as met, not met or not presented in the item's gate.

| Before | Check | Who confirms |
|---|---|---|
| Layer 1 | Clearances recorded for every service line the overlay will cover; regimes flagged (`tax-7216`, `attest-independence`) | Counsel, independence function |
| Layer 2 | Policy adopted in the firm; each tool's data rule covers the firm's client terms; the firm's unsanctioned tools listed | ai-governance owner |
| Layer 3 | Data owners named in the firm; a migration plan with training time and cost (one practitioner estimates up to USD 10,000 per FTE to move a firm onto a new IT platform, an estimate) [JOFA-CULTURE-2018] | Firm leader, IT |
| Layer 4 | Baseline from the firm's own records; named reviewers with time for review; the workflow entry tested on the firm's real cases | Benefit owner, practice lead |
| Layer 5 | The five delegation gates (`../../../transformation-advisor/references/method/onboarding.md` §5) hold in this firm | Gatekeepers at `g2` and `g3` |

**Move a capability from one firm to wider rollout** only when its baseline and method are documented, consent and
independence checks are complete, named reviewers exist, and one firm other than the pilot firm has run it. **Pause**
when reviewer workload or client complaints rise (proposed defaults). Review burden is real: 40% of 1,150 workers
surveyed say they take on extra work from low-quality AI output (cross-industry, relayed by trade press)
[TECHCRUNCH-AIROLLUP-2025].

## 5. Client-data separation and consent

- **Keep the acquired firm's client data in its own space** until consent and access rules for it are recorded
  (proposed default). Record on each item which consents it relies on.
- **File transfer.** Professional-liability guidance sets written-consent steps for transferring client files, with
  a 90-day negative-consent option; whether selling partners become equity or non-equity partners changes the
  client-notice duty [CAMICO-MERGE-2022].
- **Tax-return information.** Sec. 7216 consent can be needed for disclosures to affiliates and for uses beyond
  preparation [TAXADVISER-7216-2024]. No authoritative reading of AI tools under 7216 was found: take counsel's view.
  Use the triage in `../../../ai-governance/references/professional-duties.md` §4.
- **Attest versus non-attest.** Only licensed firms provide attest services; Aprio describes investors owning a
  separate non-attest entity while the attest firm stays independent [CPAPA-APRIO-PE-2024]. Data, tools and people shared across that line need an
  independence assessment (§6).
- Route every open question to **ai-governance**; the answer comes back through `overlay/`.

## 6. Independence checks

- **Screen before signing, monitor after.** Proposed AICPA rules (exposure draft released 2025-12-29) would restrict
  attest services to a sponsor's portfolio companies and tighten who counts as a covered member [WINSTON-APS-2026];
  if approved, they take effect one year after adoption [NYSSCPA-APS-2025]. Confirm the current status. Portfolios
  change often, so conflicts are hard to track without monitoring [ACCOUNTANCYEUROPE-TPO-2025].
- **No shared AI tool or data flow into an attest entity without an independence assessment** (advisor rule; no
  source was found on shared AI services across the attest line). The governance file's screen applies to every AI
  service to, and vendor tie with, an attest client (`professional-duties.md` §4).
- **Expect scrutiny.** The PCAOB says its inspections will look at firms that have taken private equity and at AI use
  [ATODAY-PCAOB-2025]; the FRC and ICAEW urge early engagement [BLOOMBERGTAX-FRC-2025; ICAEW-PE-2025].

## 7. Change management for incoming partners and staff

- **Partners who keep their clients and brand need evidence, not mandates.** An operating partner in Grant Thornton's
  survey says you cannot mandate a deployment; evidence from a similar business, on a timeline that works for them,
  moves management teams [GT-AIIMPACT-2026]. Use the stakeholder map and partner briefing in
  `../../../transformation-advisor/references/method/leading-partners.md`.
- **Put what stays local in writing.** Current says its partner firms keep leadership, brand and culture
  [CPAPA-CURRENT-2026]; Reuters reported that local owners keep a minority stake [REUTERS-CRETE-2025].
- **Take culture seriously.** 80% of independent UK firms cited cultural and ethical alignment as a
  reason not to pursue private equity (ICAEW finding as cited by Accountancy Europe) [ACCOUNTANCYEUROPE-TPO-2025].
- **Ask staff what worries them** and how leadership has explained AI's purpose [RSM-AIDD-2025].
- **Lead with the talent argument, not cost.** More than one-quarter of tax and audit professionals say they would not accept
  a job at a firm lacking professional-grade AI, and almost one in three would consider leaving if AI expectations are
  not met within two years (vendor survey) [TR-FOP-2026].
- **Leave time to absorb change.** Bain says people still need time to process change even with good information
  [BAIN-CAPABILITY-2026]. Budget learning time explicitly.
- **Never use tool-usage counts to judge people.** Baker Tilly's CEO called usage measurement in reviews a "red
  herring" [CFOBREW-BAKERTILLY-2026]. Adoption is measured per item (§8), never per person (rule 1).
- **Protect the junior pipeline.** The PCAOB's acting chair said new paths for junior auditors will be needed
  [ATODAY-PCAOB-2025]. Each item's role evolution says how juniors still learn (rule 2).
- Hand training, champions and skeptics to **ai-enablement**.

## 8. Tracking adoption and value in benefits.yaml

Follow `value-tracking.md` and `../schemas/benefits.md`; these rules add to them for acquired firms.

- **Adoption is a leading indicator, not value** (rule 13). Record it as a row with `type: interim`,
  `financial: false`, `level: use-case`, and a metric on the work, such as "share of the firm's returns prepared
  through the workflow", not seats or logins.
- **Value rows use the acquired firm's own baseline** (`basis: from-record` from its records), never the home
  firm's. A home result is evidence for the forecast range, not the baseline.
- **Use the staggered rollout as the counterfactual.** Firms that receive the capability later can serve as the
  comparison (`counterfactual: staggered-start`); name in `attribution` every integration change that ships at the
  same time, such as a system migration or a new review checklist (proposed default).
- **Track the deal's AI business case.** Record the AI lines written at underwriting as `level: enterprise` rows tied
  to the value creation plan line (`value-tracking.md` §3.5), and report exceeded, met or missed through `status`. In
  FTI's survey, high performers were more likely to report exceeding their AI business case (19% against 5%;
  vendor-published) [FTI-VCI-2026]. Never sum use-case rows into an enterprise figure.
- **Record losses too.** Client moves or departures linked to integration go in `disbenefit` rows as counts by role
  or client group, never named people. No source reports partner attrition or client retention after acquisitions
  of accounting firms [UVA-FAR-2026], so the firm's own counts are the only evidence.
- **Capacity per firm.** Each firm's freed capacity gets its own redeploy-or-reduce decision (rule 2).

## 9. Describing the platform's AI without overstating it

Platforms pitch AI to targets alongside local control, capital, shared technology and upskilling
[CPAPA-CURRENT-2026]. Keep the pitch apart from the evidence (advisor move). Describe each capability with:

- **Its evidence status**, using the shared `maturity` terms: announced, piloting, in production, and whether its
  value is measured, in how many firms, against what baseline. A press release is not adoption.
- **Figures as ranges, with who measured them.** Public platform claims are self-reported: Current reported 31%
  average savings in tax preparation time and up to 98% accuracy across 7,000 returns, with no baseline or accuracy
  measure published [CPAPA-CURRENT-2026]. Treat your own platform's numbers the same way.
- **What will change in their work, and what is asked of them:** consent updates, review duties, training time.
- **What will not change**, only if it is in writing (§7).
- **No promises on roles.** Say what the capacity choice is and who makes it (rule 2; `people-and-change.md`).
- **The category is young.** It is too early to assess roll-up performance as a category [NEWCOMER-ROLLUP-2025].

Sample wording (illustrative): "Return preparation with document extraction is in production in our home offices;
it saved 0.4 to 0.6 preparer hours per return against two comparison offices last season, measured from time
records. It has not yet run in a firm your size. We propose a pilot on your returns, with your own baseline, before
deciding anything further."

## 10. Question bank and common traps

**Questions**
- Is this firm merged or under the umbrella, and who decides whether it takes shared tools?
- Which clearances (consent, file transfer, independence) does each capability need, and are they recorded?
- What is this firm's baseline for the workflow, from its own records?
- Who will review AI output here, and do they have the time?
- What do incoming partners get in writing about brand, leadership and client relationships?
- Which firm will serve as the comparison for this rollout?

| Trap | How to avoid it |
|---|---|
| Starting with use cases before policy, data and training | Layers 0–3 first [RSM-AIDD-2025] |
| Carrying the home stage into the acquired firm | Entry stage from the firm's own evidence (§2 step 5) |
| Mandating tools in a partner-led firm | Evidence from a comparable firm and a sequence that suits them [GT-AIIMPACT-2026] |
| Seats and logins reported as adoption | Interim rows on work volume; value rows on the firm's baseline (§8) |
| Over-integrating early | Stabilize first; transform only where the thesis needs it [BAIN-OUTLOOK-2026] |
| Pitching home results as guaranteed | Evidence status and provenance on every claim (§9) |
| Reviewer time left out of the margin case | Size reviewer capacity; pause on rising review load (§4) |

## 11. Worked example

*Illustrative*, continuing the firm in `stage-gates.md` §8. The firm acquires a 70-person tax and bookkeeping firm
(advisor unit `units/target-cedar/`, assessed at Experimenting; merged model). K-1 extraction is in production at home.

- **Layer 0.** Counsel updates tax engagement letters for affiliate processing; the independence function clears
  two attest relationships. Recorded as clearances on the items.
- **Layers 1–2.** The overlay is extended; the approved assistant replaces two personal tools found in the
  assessment; training is scheduled with protected time.
- **Layer 3.** Cedar's two tax systems move to one. Item `tax-k1-extraction-cedar` is logged with `depends_on` the
  migration and enters at `pilot`.
- **Pilot.** Baseline from Cedar's last-season time records; the comparison is a second acquired firm that starts a
  season later. Benefit rows: an interim row (share of K-1-heavy returns through the workflow) and a direct row
  (preparer hours per return), with the migration named in `attribution`.
- **Partners.** Cedar's partners receive the §9 description, including that the home figure is not their forecast.

## 12. Output

Per capability per firm: an item in `portfolio.yaml` (`unit`, `depends_on`, entry stage, clearances in the gate
record); intake record; gate decisions. In `benefits.yaml`: interim, direct, enterprise and disbenefit rows as in §8.
The firm's AI inventory is the set of items with its `unit`.

## 13. Sources

- **ACCOUNTANCYEUROPE-TPO-2025**: Accountancy Europe, *Beyond Private Equity: Third-party ownership in the accountancy and audit sector* (professional body information paper, 2025-11). https://accountancyeurope.eu/wp-content/uploads/2025/11/251127-Third-party-ownership-in-accountancy-and-audit-sector.pdf
- **ATODAY-PCAOB-2025**: Accounting Today, *PCAOB warns auditors about AI and PE* (trade press on regulator speeches, 2025-12-09). https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe
- **BAIN-CAPABILITY-2026**: Bain & Company, *M&A Capability for a New Era* (consultancy, 2026-01-27). https://www.bain.com/insights/capability-for-a-new-era-m-and-a-report-2026/
- **BAIN-OUTLOOK-2026**: Bain & Company, *Looking Ahead (Global M&A Report 2026)* (consultancy, 2026-01-27). https://www.bain.com/insights/looking-ahead-m-and-a-report-2026/
- **BLOOMBERGTAX-FRC-2025**: Bloomberg Tax, *UK Watchdog Says Private Equity Poised to Help Audit Quality* (trade press on regulator statement, 2025-02-13). https://news.bloombergtax.com/financial-accounting/uk-watchdog-says-private-equity-poised-to-help-audit-quality
- **CAMICO-MERGE-2022**: CAMICO, *Responsibilities to Clients When a CPA Firm Is Merging or Acquired* (professional-liability insurer guidance, 2022-05-17). https://camico.com/?p=9057
- **CFOBREW-BAKERTILLY-2026**: CFO Brew, *AI is a key ingredient in Baker Tilly's transformation recipe* (trade press interview, 2026-08-25). https://www.cfobrew.com/stories/ai-is-a-key-ingredient-in-baker-tillys-transformation-recipe
- **CPAPA-APRIO-PE-2024**: CPA Practice Advisor, *Aprio Gets Private Equity Infusion* (trade press, 2024-07-11). https://www.cpapracticeadvisor.com/2024/07/11/aprio-gets-private-equity-infusion/107851/
- **CPAPA-CURRENT-2026**: CPA Practice Advisor, *Crete Professionals Alliance Rebrands as Current* (trade press, 2026-06-03). https://www.cpapracticeadvisor.com/?p=184461
- **FTI-VCI-2026**: FTI Consulting, *AI Speeds Up Returns in Private Equity as M&A Becomes Top Value Generator* (press release, survey of 555, 2026-06-04). https://www.fticonsulting.com/about/newsroom/press-releases/ai-speeds-up-returns-in-private-equity-as-ma-becomes-top-value-generator-for-firms
- **GT-AIIMPACT-2026**: Grant Thornton, *Private Equity insights: 2026 AI Impact Survey Report* (consultancy survey, fielded 2026-02/03). https://www.grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey-report
- **ICAEW-PE-2025**: ICAEW, *What private equity might mean for a firm's audit status* (professional body, 2025-02-13). https://www.icaew.com/insights/viewpoints-on-the-news/2025/feb-2025/what-private-equity-might-mean-for-a-firms-audit-status
- **JOFA-CULTURE-2018**: Journal of Accountancy, *After the merger: Creating a culture of success* (practitioner guide, 2018-12-01). https://www.journalofaccountancy.com/issues/2018/dec/after-merger-culture-of-success/
- **NEWCOMER-ROLLUP-2025**: Newcomer, *Inside the VC Roll-up Craze That Has Taken Silicon Valley by Storm* (newsletter, 2025-12-18). https://www.newcomer.co/p/inside-the-vc-roll-up-craze-that
- **NJCPA-PE-2026**: NJCPA, *The Rapid Growth of Private Equity Investment in Public Accounting* (professional-society article, 2026-07-17). https://www.njcpa.org/development/dom-test/2026/07/17/the-rapid-growth-of-private-equity-investment-in-public-accounting
- **NYSSCPA-APS-2025**: NYSSCPA, *AICPA Calls for Comments on Ethics Rules Update for Alternative Practice Structures in Private Equity* (professional body news, 2025-12-22). https://nysscpa.org/news/1045198-aicpa-calls-for-comments-on-ethics-rules-update-for-alternative-practice-structures-in-private-equity-2025-12-22
- **REUTERS-CRETE-2025**: Reuters (via AOL), *Thrive-backed accounting firm Crete to spend $500 million in AI roll-up* (news, 2025-06-04). https://www.aol.com/news/thrive-backed-accounting-firm-crete-130200514.html
- **RSM-AIDD-2025**: RSM US, *Artificial intelligence: ready or not?* (consultancy guidance, 2025). https://rsmus.com/insights/industries/private-equity/ai-due-diligence-assessment-private-equity.html
- **TAXADVISER-7216-2024**: The Tax Adviser (AICPA), *The many implications of Sec. 7216* (professional body, 2024-01). https://www.thetaxadviser.com/issues/2024/jan/the-many-implications-of-sec-7216.html
- **TECHCRUNCH-AIROLLUP-2025**: TechCrunch, *The AI services transformation may be harder than VCs think* (trade press, 2025-09-29). https://techcrunch.com/2025/09/28/the-ai-services-transformation-may-be-harder-than-vcs-think/
- **TR-FOP-2026**: Thomson Reuters Institute, *What the "2026 Future of Professionals Report" says tax & audit firm leaders should be prioritizing now* (vendor research summary, 2026-07-21). https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
- **UVA-FAR-2026**: University of Amsterdam, *ABS researcher receives grant for auditing research* (academic project announcement, 2026-05-12). https://www.uva.nl/en/shared-content/faculteiten/en/faculteit-economie-en-bedrijfskunde/news/2026/05/abs-researcher-receives-grant-for-auditing-research.html
- **WINSTON-APS-2026**: Winston & Strawn, *AICPA proposes significant changes to ethics rules governing private equity investments in accounting firms* (law-firm summary, page undated, 2026). https://www.winston.com/en/insights-news/aicpa-proposes-significant-changes-to-ethics-rules-governing-private-equity-investments-in-accounting-firms
- **WK-PE-2025**: Wolters Kluwer, *Private equity is reshaping the tax and accounting industry* (vendor article, 2025-09-02). https://www.wolterskluwer.com/en/expert-insights/private-equity-is-reshaping-the-tax-and-accounting-industry
