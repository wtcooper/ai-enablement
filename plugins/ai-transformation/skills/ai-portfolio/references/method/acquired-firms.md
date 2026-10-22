# Rolling capabilities into acquired firms

Read this to move proven AI capabilities (approved tools, library workflows, the governance overlay, data
foundations) into an acquired firm; it is the detail behind `stage-gates.md` §9. Assessing the firm first is the
advisor's acquisition path (`../../../transformation-advisor/references/method/acquisitions.md`). Rules 1, 2, 5
and 9 apply throughout. Keys in brackets are listed in §10.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [What moves first: layers and readiness checks](#3-what-moves-first-layers-and-readiness-checks)
4. [Clearances: client data, consent and independence](#4-clearances-client-data-consent-and-independence)
5. [Incoming partners and staff](#5-incoming-partners-and-staff)
6. [Tracking adoption and value](#6-tracking-adoption-and-value)
7. [Questions](#7-questions)
8. [Worked example](#8-worked-example)
9. [Output](#9-output)
10. [Sources](#10-sources)

## 1. Goal and exit criteria

**Goal.** Each capability reaches the acquired firm only after what it depends on is in place there, enters the
portfolio at the stage its evidence in that firm supports, and is tracked against that firm's own baseline.

**Exit criteria** for a firm's rollout plan:

- An assessment of the acquired firm (the advisor's unit `units/<target-id>/`), validated or labelled draft.
- Each capability to move is an item with `unit` set to the firm, its layer (§3), `depends_on`, and an entry
  stage justified by evidence in that firm; clearances recorded before anything moves data or tools (§4).
- Items past `g3` have adoption and value rows on the firm's own baseline (§6); incoming partners have a written
  description of the platform's AI with each capability's evidence status (§5).

## 2. How to run it

1. **Read the assessment** (stage per dimension, red flags, foundation items), or hand off to
   transformation-advisor's acquisition path first.
2. **Settle the model.** A platform can buy smaller firms into one larger organization, or sit above firms that
   keep their own brand and leadership and take shared services [NJCPA-PE-2026]. Merged: one stack and one
   workflow set, sequenced. Umbrella: offer the capabilities with evidence and let each firm adopt.
3. **Stabilize before transforming.** Writing about large deals, Bain says winners focus integration on a short
   list of value drivers and set an order of operations: where to stabilize and integrate, where and when to
   transform [BAIN-OUTLOOK-2026]. Hold AI capabilities to the transform list.
4. **Log each capability per firm** through intake (`intake.md`): one item per capability per acquired firm,
   because each firm moves through the gates at its own pace. Id pattern `<capability>-<firm>`; `source`
   back-links to the home item or the advisor's unit `opportunities.yaml`.
5. **Set the entry stage from the acquired firm's evidence,** not the stage reached at home. A capability in
   production at home usually enters at `pilot`: feasibility is shown, adoption and value in this firm are not
   (this skill's default). Use the light path where the risk tier allows it (`stage-gates.md` §3.2).
6. **Sequence by layer** (§3), check readiness before each layer, and hold gates as usual.
7. **Add the firm to the AI inventory** from day one (what runs, who owns it, what stage, what governance)
   [GT-AIIMPACT-2026]: the items filtered by `unit`.

## 3. What moves first: layers and readiness checks

RSM treats a weak AI policy and guardrails as a first-wave priority after close, and says siloed data must be
centralized and governed before AI delivers meaningful results [RSM-AIDD-2025]. The layers are this skill's
ordering; each depends on the ones above it, and a firm moves through them as fast as its checks pass. The checks
are defaults (no source gives thresholds); record each as met, not met or not presented in the item's gate.

| Layer | What moves | Check before it moves | Who confirms |
|---|---|---|---|
| **0 Clearances** | Client notice and file-transfer consent; tax-return consent; independence screen and monitoring; data-separation rules (§4) | Deal structure known | Counsel, independence function |
| **1 Governance overlay** | `overlay/policy.md` risk tiers and data rules, `overlay/guardrails.md`, records of AI use, extended to the firm | Clearances recorded for every service line covered; regimes flagged (`tax-7216`, `attest-independence`) | Counsel, independence function |
| **2 Approved tools and training** | `overlay/tool-catalog.yaml` entries for the firm; training; an approved alternative for each unsanctioned tool | Policy adopted in the firm; each tool's data rule covers the firm's client terms | ai-governance owner |
| **3 Data foundations** | Common systems of record; data centralized and governed | Data owners named; a migration plan with training time and cost | Firm leader, IT |
| **4 Library workflows** | Entries from `enablement/workflows/`, then automation of one or two high-volume flows | The firm's own baseline; named reviewers with time; the workflow tested on the firm's real cases | Benefit owner, practice lead |
| **5 Rebuilt workflows and agents** | Workflow-native redesigns; delegated agents | Layer 4 in production in this firm; the five delegation gates (`../../../transformation-advisor/references/method/onboarding.md` §5) hold | Gatekeepers at `g2` and `g3` |

**Move a capability to wider rollout** only when its baseline and method are documented, consent and independence
checks are complete, named reviewers exist, and one firm other than the pilot firm has run it. **Pause** when
reviewer workload or client complaints rise (defaults).

## 4. Clearances: client data, consent and independence

- **Keep the acquired firm's client data in its own space** until consent and access rules for it are recorded
  (default). Record on each item which consents it relies on.
- **File transfer.** The AICPA Code (ET 1.400.205, as summarized by a professional-liability insurer) requires a
  written request for consent to transfer client files when the seller keeps no ownership in the successor, with
  a 90-day negative-consent option; if the target's owners become equity partners the notice does not apply, if
  non-equity partners it does [CAMICO-MERGE-2022].
- **Tax-return information.** Sec. 7216 consent can be needed for disclosures to affiliates and for uses beyond
  preparation; a third-party provider that only helps prepare or process the return needs none unless it makes
  substantive decisions [TAXADVISER-7216-2024]. 7216 consent has no negative-consent option, so where the target's
  owners keep no equity, the cautious course is affirmative written consent [CAMICO-MERGE-2022]. No authoritative
  reading of AI tools under 7216 was found: take counsel's view, using the triage in
  `../../../ai-governance/references/professional-duties.md` §4.
- **Independence.** No shared AI tool or data flow into an attest entity without an independence assessment
  (advisor rule; the screen in `professional-duties.md` §4 applies to every AI service to, and vendor tie with, an
  attest client). Screen before signing and monitor after. Proposed AICPA rules (exposure draft of 2025-12-29)
  would restrict attest services to a sponsor's portfolio companies and tighten who counts as a covered member
  [WINSTON-APS-2026]; in August 2026 the ethics committee was still discussing changes [JOFA-PEEC-2026], so confirm
  the current status. PCAOB officials said inspections will focus on firms that have taken private equity, and on
  AI use [ATODAY-PCAOB-2025].
- Route every open question to **ai-governance**; the answer comes back through `overlay/`.

## 5. Incoming partners and staff

- **Evidence, not mandates.** A Grant Thornton transaction advisory partner says you cannot mandate an AI
  deployment in a portfolio company; evidence from a similar business, on a timeline that works for them, moves
  management teams [GT-AIIMPACT-2026]. Use the stakeholder map and partner briefing in
  `../../../transformation-advisor/references/method/leading-partners.md`.
- **Put what stays local in writing,** and ask staff what worries them and how leadership has explained AI's
  purpose [RSM-AIDD-2025]. Budget learning time explicitly.
- **Measure adoption per item, never per person** (rule 1), and say in each item's role evolution how juniors
  still learn (rule 2).
- **Describe the platform's AI without overstating it.** Keep the pitch apart from the evidence. For each
  capability give its evidence status (announced, piloting, in production; whether value is measured, in how many
  firms, against what baseline), figures as ranges with who measured them, what will change in their work and what
  is asked of them, and no promises on roles. Public platform claims are self-reported: Current reported 31%
  average savings in tax preparation time and up to 98% accuracy across 7,000 returns, with no baseline or accuracy
  measure published [CPAPA-CURRENT-2026]. Treat your own platform's numbers the same way.
- Hand training, champions and skeptics to **ai-enablement**.

## 6. Tracking adoption and value

Follow `value-tracking.md` and `../schemas/benefits.md`; these rules add to them.

- **Adoption is a leading indicator, not value** (rule 13): a row with `type: interim`, `financial: false`,
  `level: use-case`, and a metric on the work, such as "share of the firm's returns prepared through the
  workflow", not seats or logins.
- **Value rows use the acquired firm's own baseline** (`basis: from-record`), never the home firm's. A home result
  is evidence for the forecast range, not the baseline.
- **Use the staggered rollout as the counterfactual** (`counterfactual: staggered-start`); name in `attribution`
  every integration change that ships at the same time, such as a system migration.
- **Track the deal's AI business case** as `level: enterprise` rows tied to the value creation plan line
  (`value-tracking.md` §3.4). Never sum use-case rows into an enterprise figure.
- **Record losses too.** Client moves or departures linked to integration go in `disbenefit` rows as counts by role
  or client group, never named people.
- **Capacity per firm.** Each firm's freed capacity gets its own redeploy-or-reduce decision (rule 2).

## 7. Questions

Ask who decides whether the firm takes shared tools, which clearances each capability needs, what the firm's own
baseline is and which firm will serve as the comparison, and who will review AI output there, with what time.

## 8. Worked example

*Illustrative.* The firm acquires a 70-person tax firm (unit `units/target-cedar/`; merged model). After
clearances, overlay and tools (layers 0–2) and a move to one tax system, `tax-k1-extraction-cedar` enters at
`pilot` with `depends_on` the migration, on Cedar's own baseline, compared with a firm that starts a season later.
Rows: interim (share of K-1-heavy returns through the workflow) and direct (preparer hours per return), with the
migration named in `attribution`.

## 9. Output

Per capability per firm: an item in `portfolio.yaml` (`unit`, `depends_on`, entry stage, clearances in the gate
record), an intake record and gate decisions. In `benefits.yaml`: interim, direct, enterprise and disbenefit rows
as in §6. The firm's AI inventory is the set of items with its `unit`.

## 10. Sources

- **ATODAY-PCAOB-2025**: Accounting Today, *PCAOB warns auditors about AI and PE* (trade press on regulator speeches, 2025-12-09). https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe
- **BAIN-OUTLOOK-2026**: Bain & Company, *Looking Ahead (Global M&A Report 2026)* (consultancy, 2026-01-27). https://www.bain.com/insights/looking-ahead-m-and-a-report-2026/
- **CAMICO-MERGE-2022**: CAMICO, *Responsibilities to Clients When a CPA Firm Is Merging or Acquired* (professional-liability insurer guidance, 2022-05-17). https://camico.com/?p=9057
- **CPAPA-CURRENT-2026**: CPA Practice Advisor, *Crete Professionals Alliance Rebrands as Current* (trade press, 2026-06-03). https://www.cpapracticeadvisor.com/?p=184461
- **GT-AIIMPACT-2026**: Grant Thornton, *Private Equity insights: 2026 AI Impact Survey Report* (consultancy survey, fielded 2026-02/03). https://www.grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey-report
- **JOFA-PEEC-2026**: Journal of Accountancy, *PEEC to continue discussions on alternative practice structures* (professional body news, 2026-08-10). https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures.html
- **NJCPA-PE-2026**: NJCPA, *The Rapid Growth of Private Equity Investment in Public Accounting* (professional-society article, 2026-07-17). https://www.njcpa.org/development/dom-test/2026/07/17/the-rapid-growth-of-private-equity-investment-in-public-accounting
- **RSM-AIDD-2025**: RSM US, *Artificial intelligence: ready or not?* (consultancy guidance, 2025). https://rsmus.com/insights/industries/private-equity/ai-due-diligence-assessment-private-equity.html
- **TAXADVISER-7216-2024**: The Tax Adviser (AICPA), *The many implications of Sec. 7216* (professional body, 2024-01). https://www.thetaxadviser.com/issues/2024/jan/the-many-implications-of-sec-7216.html
- **WINSTON-APS-2026**: Winston Taylor (published as Winston & Strawn before the firm's 2026-06-01 combination), *AICPA proposes significant changes to ethics rules governing private equity investments in accounting firms* (law-firm summary, page undated, between 2025-12-29 and 2026-06-01). https://www.winston.com/en/insights-news/aicpa-proposes-significant-changes-to-ethics-rules-governing-private-equity-investments-in-accounting-firms
