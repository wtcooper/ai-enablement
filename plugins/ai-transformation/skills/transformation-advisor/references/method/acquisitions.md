# Acquisitions: assessing a target or acquired firm

Read this when the user is weighing a firm to acquire, or has just acquired one, and needs to know how ready its AI
and data really are. It covers when to take this path, what to ask and count, red flags, the value-creation questions
for the deal thesis, and how to record the result as a unit of the plan. Rolling the platform's capabilities into the
firm after close belongs to the ai-portfolio skill (`../../../ai-portfolio/references/method/acquired-firms.md`).
Source keys in brackets are listed in §10. Most published acquisition figures are vendor-published or self-reported.

## Contents

1. [When to use it](#1-when-to-use-it)
2. [Intake](#2-intake)
3. [What to ask and what to count](#3-what-to-ask-and-what-to-count)
4. [Red flags](#4-red-flags)
5. [Value-creation questions for the thesis](#5-value-creation-questions-for-the-thesis)
6. [Recording the assessment as a unit](#6-recording-the-assessment-as-a-unit)
7. [Common traps](#7-common-traps)
8. [Worked example](#8-worked-example)
9. [Output](#9-output)
10. [Sources](#10-sources)

## 1. When to use it

| Situation | Who usually asks | What the assessment is for |
|---|---|---|
| **Diligence** (before signing) | The acquirer's head of AI, an operating partner, or a platform's integration lead | What must be fixed before AI can deliver, what it costs, and which AI claims in the thesis are real |
| **Sign to close** | The same, plus the integration team | Consent, independence and data-access steps that must be in place before files or tools move |
| **First period after close** | The acquired firm's leader or the platform's head of AI | A baseline for the firm: its journey stage, binding constraints and first foundation items |
| **Target side** | A partner at a firm being courted | Separating a platform's AI pitch from the evidence behind it (§5, last block) |

- **The point is a priced list of fixes, not a score.** Consultancy diligence frameworks link maturity findings to
  EBITDA, price and the post-close plan [KPMG-AIDD-2025; RSM-AIDD-2025]. Some frame that plan as the first 100
  days; this skill sequences by dependency instead (rule 9 in `SKILL.md`).
- **Frameworks converge but none is validated.** RSM, KPMG, PwC and Baker Tilly assess versions of strategy, data,
  technology, talent, governance and adoption [RSM-AIDD-2025; KPMG-AIDD-2025; PWC-AIDD-ND; BAKERTILLY-AIDD-2024];
  no independent validation of any of them was found.
- **Exit criteria.** Each of the ten dimensions in §3 has a rating with its evidence type; the journey stage is placed
  by what was seen or counted; red flags are listed with an owner; each AI claim in the thesis is marked base case or
  upside; the assessment is saved as a unit (§6), labelled "draft to validate" until people at the firm confirm it.

## 2. Intake

Ask one at a time; skip what is known.

- Who is asking: the acquirer, the target, or an operating partner? At what deal stage?
- What is the structure: a platform that buys smaller firms into one larger organization, an umbrella of firms that
  keep their own brand and leadership and take shared services [NJCPA-PE-2026], or a capability buy? Is there an
  attest firm? Aprio and Baker Tilly describe an alternative practice structure: a licensed CPA firm provides attest
  services and a separate entity that is not a licensed CPA firm provides tax and advisory services
  [CPAPA-APRIO-PE-2024; BAKERTILLY-AIDD-2024].
- What is the thesis: capacity, margin, growth, or acquiring a capability? Which AI claims are in the base case?
- What can the user share? Public information and the firm's own documents (policies, tool lists, usage reports,
  org charts), never client names or client files (rule 5). Data-room material stays under the deal's confidentiality
  terms; for tax clients, guidance calls for a written agreement limiting use of return information to the purchase
  [JOFA-MA-2017; CPAI-SUCCESSION-ND].

## 3. What to ask and what to count

Use RSM's six prerequisites (data, infrastructure, skilled talent, governance and security guardrails, cultural
openness, aligned use cases) as the spine [RSM-AIDD-2025], plus four dimensions other sources add. Rate each red, amber
or green, and record the evidence type: **document**, **interview**, **public**, or **inferred**.

| # | Dimension | Ask | Count or see |
|---|---|---|---|
| 1 | Data | How often do you meet missing or wrong data? Can you combine data across departments? [RSM-AIDD-2025] | Where client data lives; systems a central team would need to reach |
| 2 | Infrastructure and tool stack | Legacy on-premise systems, manual pipelines, ad hoc integrations? [RSM-AIDD-2025] Same stack in every office? [WK-PE-2025] | Offices on a common stack; systems of record per service line |
| 3 | Talent and training | Who owns AI or analytics? How much depends on outside parties? Who is trained, how often? [RSM-AIDD-2025] | Roles, outside dependencies, staff trained in the last year |
| 4 | Governance and security | Written AI policy? Human-review rule for high-stakes outputs? Data-privacy practice? [RSM-AIDD-2025] Who approves new tools? (advisor addition) | Approved-tool list; tools staff use outside it |
| 5 | Culture | What have staff raised (job security, accuracy)? How has leadership explained AI's purpose? Ask staff, not only leaders [RSM-AIDD-2025] | Concerns by theme, from staff conversations |
| 6 | Use cases | Which are tied to measurable goals, and which exist for AI's sake? [RSM-AIDD-2025] | Workflows in normal use with an owner and a baseline |
| 7 | Client data and consent | Do engagement letters allow processing by a third party, an affiliate or a central team? [TAXADVISER-7216-2024] | Share of letters with that permission, by service line |
| 8 | Independence and structure | Which attest clients are portfolio companies or related parties of the sponsor? [WINSTON-APS-2026] | Result of the firm's independence screen (counts, not names) |
| 9 | Vendors and licences | Licensing terms, data ownership, portability, lock-in? [KPMG-AIDD-2025] | AI and data contracts; which can move to the new owner |
| 10 | Measured results | How were claimed savings measured, over what baseline, and has anyone outside the team checked? [KPMG-AIDD-2025] Do roadmaps match delivery pace? [PWC-AIDD-ND] | Claims with a method and data behind them |

**Count active use, not licences.** Ask for a usage report by named tool for the last full month. In a vendor's
survey, over 40% of firms were not fully using their current technology investments [WK-PE-2025].

**Place the firm on the journey stages** with the stage cards in `onboarding.md` §5, by what you saw or counted:

| Stage | What it looks like in a target firm |
|---|---|
| **Curious** | No approved tools or a ban; personal tools in use; no policy, owner or budget |
| **Experimenting** | Licences issued but the usage report shows few active users; pilots with no baseline or stop decision |
| **Adopting** | AI inside the system of record for a few owned workflows with measures; policy, training, approved-tool list |
| **Scaling** | One stack across offices; reused components; value recorded across workflows; a named central owner |
| **AI-native** | Pricing, services or the cost base changed because of AI, with figures |

Place each dimension, not only the firm: plan against the weakest one that matters (`onboarding.md` §5). An
acquired firm may be at a different stage from the acquirer; plan its foundation work from its own stage, not the
acquirer's (advisor heuristic).

## 4. Red flags

| Red flag | Why it matters | Source |
|---|---|---|
| **Unsanctioned tools** with client data, or a ban with no approved alternative | Use outside approved tools is common; with client data it is an exposure the acquirer takes on (advisor view) | Use patterns: `../library/journey-stages.md` §2 |
| **Data ungoverned:** siloed data, no governance, no cataloguing | Time and money to centralize and govern before any benefit | [RSM-AIDD-2025] |
| **No consent for tax-return information** to reach an affiliate, central team or AI tool | Sec. 7216 consent can be needed for disclosures to affiliates and for uses beyond preparation; a third-party provider that only helps prepare or process the return needs none unless it makes substantive decisions. No authoritative reading of AI tools under 7216 was found, so take counsel's view | [TAXADVISER-7216-2024]; triage in `../../../ai-governance/references/professional-duties.md` §4 |
| **Attest clients that are the sponsor's portfolio companies** or related parties | Proposed AICPA rules would restrict attest services to a sponsor's portfolio companies and tighten who counts as a covered member; conflicts can reach across the sponsor's fund family | [WINSTON-APS-2026; ACCOUNTANCYEUROPE-TPO-2025] |
| **Vendor contracts that do not transfer**, or lock in data | KPMG's diligence case found data-licensing and vendor lock-in risk behind an AI pitch | [KPMG-AIDD-2025]; assignment terms are for counsel (no source found) |
| **Claimed savings with no method or baseline** | KPMG's case found projected AI savings overstated (vendor-published, anonymous software target) | [KPMG-AIDD-2025] |
| **Each office on different tools** | Work cannot move between offices until stack and workflow are common | [WK-PE-2025] (vendor view) |
| Legacy systems, manual pipelines, heavy reliance on outside parties, no upskilling | Remediation before AI | [RSM-AIDD-2025] |
| Roadmap promises beyond demonstrated delivery pace | Aspiration counted as capability | [PWC-AIDD-ND] |

**Independence status changes.** The AICPA exposure draft was released 2025-12-29 with comments due 2026-04-30; if
approved, the rules take effect one year after adoption [WINSTON-APS-2026; NYSSCPA-APS-2025]. In August 2026 the
ethics committee was discussing further changes and whether to issue a second exposure draft, which would open a new
comment period [JOFA-PEEC-2026]. The rules are not final; confirm the current status before relying on them. Portfolios change often, so a one-off screen is not enough; conflicts need monitoring
[ACCOUNTANCYEUROPE-TPO-2025]. In the UK, ICAEW and the FRC urge firms to get in touch early in a transaction [ICAEW-PE-2025;
BLOOMBERGTAX-FRC-2025]; in the US, PCAOB officials said its inspections of firms that audit public companies will
focus on firms that have taken private equity, and on AI use [ATODAY-PCAOB-2025]. Mark any shared AI platform that crosses the attest line for an independence assessment (advisor
rule; no source covers shared AI services across that line).

## 5. Value-creation questions for the thesis

**For the acquirer.**
- Which AI claims are in the base case, and which are upside? Put AI upside outside the base case until it is
  measured (advisor rule; no source sets a threshold).
- Is there a line of sight from each claimed use to EBITDA? RSM's operating-partner framing asks for one within six
  months [RSM-AIDD-2025].
- How were the target's claimed savings measured? Ask for the data before accepting the number [KPMG-AIDD-2025].
- What does integration stabilize, and where does it transform? Writing about large deals, Bain says winners focus
  integration on a short list of value drivers, set an order of operations, and do not get caught up resolving
  internal complexity in the first wave [BAIN-OUTLOOK-2026]. Hold AI to the transform list.
- Does the time to first measurable benefit fit the hold period? 66% of PE leaders in FTI's survey of 555 report
  AI-related benefits within 12 months, but only 25% see M&A results that fast and 35% call M&A implementation
  efficient or very efficient, the lowest of any lever (vendor-published) [FTI-VCI-2026]. PE funds generally work on three-to-seven-year
  horizons [ACCOUNTANCYEUROPE-TPO-2025].
- Is the value planned before signing? Fewer than one-quarter of A&M's respondents embed value-creation planning
  before the letter of intent, and 41% realized below 75% of planned value creation over 12 months (survey of 100,
  vendor-published) [AM-VALUECREATION-2026]. Write the AI business case at underwriting so later claims can be checked:
  Grant Thornton finds PE leaders confident on AI strategy but short of measurable results (vendor-published; PE
  subgroup of 100) [GT-AIIMPACT-2026].
- Is the gain personal productivity or a rebuilt workflow? Baker Tilly's CEO calls personal-productivity AI "table
  stakes", does not expect it to change the P&L materially on its own, and plans to rebuild tax and audit workflows
  with agentic AI embedded [CFOBREW-BAKERTILLY-2026].
- Who reviews AI output, and is reviewer time in the margin case? Human review remains the top requirement for high-stakes
  GenAI use in Deloitte's 2026 M&A study (vendor-published) [DELOITTE-PULSE-2026]; in a Stanford Social Media Lab and
  BetterUp Labs survey of 1,150 workers, 40% said they take on extra work from low-quality AI output (cross-industry,
  relayed by trade press) [TECHCRUNCH-AIROLLUP-2025].
- What happens to freed capacity: redeploy or reduce (rule 2)? What is the plan for junior staff's skills? The PCAOB's
  acting chair said new paths for junior auditors will be needed [ATODAY-PCAOB-2025].
- What are training and migration costs? One practitioner estimates moving a firm to a new IT platform can cost as
  much as USD 10,000 per FTE (an author's estimate, not a measurement) [JOFA-CULTURE-2018].

**For a target weighing a platform.**
- What does the platform's AI do today, and is each tool announced, piloting or in production? What measured result
  is behind each figure, and who measured it? Platform claims are mostly self-reported; it is too early to assess
  roll-up performance as a category [NEWCOMER-ROLLUP-2025].
- What do the reported scale numbers count (firms, offices, employees, revenue), and as of when? Published figures for
  one platform differ in basis across sources [REUTERS-CRETE-2025; CPAPA-CURRENT-2026; ACCTODAY-CURRENT-2026].
- How much of past margin gains came from pricing rather than work change? In health care, an anesthesia study found
  price rises after add-on acquisitions and a gastroenterology study found price rises after PE acquisition; neither
  found a quality gain (adjacent industry, no AI element) [NBER-ANESTHESIA-2025; JAMA-GI-2025].
- What stays local in writing: brand, leadership, client relationships? Ask two previously acquired firms what
  actually changed (advisor move).

## 6. Recording the assessment as a unit

Reuse Break down (`breakdown-and-rollup.md`): the firm becomes a unit of the plan of whoever is asking.

1. **Parent.** Usually the acquirer's or platform's `transformation-plan.md` at organization scope. If none exists,
   run Onboard for the acquirer first; the target inherits its settings. If the user is at the target, the target is
   the scope itself: use the assessment as its Profile.
2. **Unit entry.** Add the firm to the parent's `units` with an id such as `target-<short-name>`, an owner role, and
   `mode: desk-review`, `status: desk-review` while it is a draft. Keep a code name before signing if the deal is
   confidential.
3. **Brief.** Write `units/<target-id>/brief.md` from `references/templates/unit-brief.md`: deal stage, structure and
   thesis in "Why this unit"; the parent's levers, weights and guardrails as inherited settings; the questions this
   assessment must answer.
4. **Draft.** For a first pass from public information and the user's documents, use the `assess-target-firm` brief
   (one subagent per firm). Save its output as `units/<target-id>/evidence/maturity-assessment.md`, labelled
   **"Draft to validate"**.
5. **Unit plan.** Create `units/<target-id>/transformation-plan.md` with a "Draft to validate" banner: the Profile
   holds the stage table per dimension; Map and Diagnose hold what the assessment found, labelled by evidence type.
6. **Fixes as foundation items.** Each red or amber dimension with a remediation becomes an item in
   `units/<target-id>/opportunities.yaml` with `category: foundation`, `label: draft-to-validate`, `prerequisites`,
   cost as a range with assumptions, and `depends_on`. Consent and independence items come first, because they gate
   anything that moves data or tools (advisor rule).
7. **Validate.** After close (or in management sessions before it), replace the three weakest numbers with records,
   confirm ratings with the people who do the work, and move `status` to `in-progress`. Then hand capability rollout to
   **ai-portfolio** (`../../../ai-portfolio/references/method/stage-gates.md` §9).

## 7. Common traps

| Trap | How to avoid it |
|---|---|
| Underwriting AI savings from the target's or a vendor's claims | Ask for method and data [KPMG-AIDD-2025]; keep AI upside out of the base case until measured |
| Scoring the target instead of pricing the fixes | Attach a remediation item, owner and cost range to every red dimension [RSM-AIDD-2025] |
| Counting licences or usage as adoption | Active use by tool, then workflows with owners and baselines; Baker Tilly's CEO calls usage measurement in reviews a "red herring" [CFOBREW-BAKERTILLY-2026] |
| Finding independence conflicts after signing | Screen the sponsor's holdings in diligence and plan monitoring [WINSTON-APS-2026; ACCOUNTANCYEUROPE-TPO-2025] |
| Consent gaps discovered when files move | Map consents before close; written-consent steps for file transfer apply, and Sec. 7216 can require affirmative consent for tax-return information [CAMICO-MERGE-2022] |
| Asking only leaders | One seat's view is not the firm's; ask staff too [RSM-AIDD-2025; `onboarding.md` §5] |
| A 100-day plan with AI as the first wave | Sequence by dependency; stabilize first, transform where the thesis needs it [BAIN-OUTLOOK-2026] |
| Desk assessment treated as fact | "Draft to validate" label; validation list; no big bet rests on it alone |
| Reading other roll-up industries as forecasts | Health-care roll-up evidence is a warning about pricing, not a finding on accounting [NBER-ANESTHESIA-2025] |

## 8. Worked example

*Illustrative; the firm and all figures are invented.* A regional accounting platform's head of AI is in diligence on
a 70-person tax and bookkeeping firm with a small attest practice. The platform's plan is the parent; the target is
`units/target-cedar/`, `mode: desk-review`.

- **Intake.** Merged model (the target will move onto the platform's systems); attest work stays in the licensed firm.
  Thesis: tax-season capacity. One AI claim is in the base case: "AI-assisted return preparation saves 30% of
  preparer time."
- **Draft.** The `assess-target-firm` subagent works from the target's website, job postings and the documents the
  user shared (AI policy, tool list, a usage export). Findings carry evidence types.
- **Ratings.** Data amber (client files in two systems; bookkeeping data clean, tax workpapers scanned). Stack red
  (two offices on different tax software). Talent amber (one part-time analytics role, no training last year).
  Governance amber (policy exists; no human-review rule; no approved-tool list). Culture green from staff
  conversations. Use cases red (the 30% claim has no baseline; the usage export shows 9 of 40 licences active last
  month). Consent red (engagement letters do not mention affiliates). Independence amber (the independence function
  reports two attest clients that are related parties of the sponsor's portfolio; counts only). Vendors amber (one
  extraction tool's licence names the target as sole licensee). Measured results red.
- **Stage.** Experimenting: licences issued, low active use, no owned workflow with a baseline.
- **Thesis.** The 30% claim moves to upside. Base-case capacity rests on the platform's own measured workflows
  once the stack and consent items are done. Reviewer time is added to the margin case.
- **Foundation items** in `opportunities.yaml`, by dependency: consent update for tax clients (counsel's view on AI
  tools) → independence decision on the two attest relationships → one tax system → approved tools and the review
  rule → baseline from last season's time records → first shared workflow.
- **Validation list.** Replace the usage figure with a full-month export; confirm the consent position with counsel;
  ask two senior preparers how returns are really reviewed.

## 9. Output

- Parent plan: the unit in `units` (`mode`, `status`); a line in the Profile or Map section noting the acquisition
  path and deal stage.
- `units/<target-id>/brief.md`, `evidence/maturity-assessment.md` (draft to validate), `transformation-plan.md`
  (banner, Profile stage table, Map and Diagnose), `opportunities.yaml` (foundation items, `label: draft-to-validate`).
- After close: the handoff to ai-portfolio for rollout.

## 10. Sources

- **ACCOUNTANCYEUROPE-TPO-2025**: Accountancy Europe, *Beyond Private Equity: Third-party ownership in the accountancy and audit sector* (professional body information paper, 2025-11). https://accountancyeurope.eu/wp-content/uploads/2025/11/251127-Third-party-ownership-in-accountancy-and-audit-sector.pdf
- **ACCTODAY-CURRENT-2026**: Accounting Today, *Crete rebrands as Current* (trade press, 2026-06-02). https://www.accountingtoday.com/news/crete-professionalls-alliance-rebrands-as-current
- **AM-VALUECREATION-2026**: Alvarez & Marsal, *North America Value Creation Report 2026* (press release, survey of 100, 2026-05-28). https://www.alvarezandmarsal.com/node/95596
- **ATODAY-PCAOB-2025**: Accounting Today, *PCAOB warns auditors about AI and PE* (trade press on regulator speeches, 2025-12-09). https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe
- **BAIN-OUTLOOK-2026**: Bain & Company, *Looking Ahead (Global M&A Report 2026)* (consultancy, 2026-01-27). https://www.bain.com/insights/looking-ahead-m-and-a-report-2026/
- **BAKERTILLY-AIDD-2024**: Baker Tilly, *AI due diligence assessment prepares company for strategic acquisition* (practitioner case, anonymous client, 2024-10-03). https://www.bakertilly.com/insights/ai-due-diligence-assessment-prepares-company-for-strategic-acquisition
- **BLOOMBERGTAX-FRC-2025**: Bloomberg Tax, *UK Watchdog Says Private Equity Poised to Help Audit Quality* (trade press on regulator statement, 2025-02-13). https://news.bloombergtax.com/financial-accounting/uk-watchdog-says-private-equity-poised-to-help-audit-quality
- **CAMICO-MERGE-2022**: CAMICO, *Responsibilities to Clients When a CPA Firm Is Merging or Acquired* (professional-liability insurer guidance, 2022-05-17). https://camico.com/?p=9057
- **CFOBREW-BAKERTILLY-2026**: CFO Brew, *AI is a key ingredient in Baker Tilly's transformation recipe* (trade press interview, 2026-08-25). https://www.cfobrew.com/stories/ai-is-a-key-ingredient-in-baker-tillys-transformation-recipe
- **CPAI-SUCCESSION-ND**: CPA Insurance, *Professional Liability Issues in "Success"ion Planning* (professional-liability insurer guidance, undated). https://www.cpai.com/Education-Resources/my-firm/Firm-Acquisitions-Transitions/Professional-liability-issues-in-succession-planni
- **CPAPA-APRIO-PE-2024**: CPA Practice Advisor, *Aprio Gets Private Equity Infusion* (trade press, 2024-07-11). https://www.cpapracticeadvisor.com/2024/07/11/aprio-gets-private-equity-infusion/107851/
- **CPAPA-CURRENT-2026**: CPA Practice Advisor, *Crete Professionals Alliance Rebrands as Current* (trade press, 2026-06-03). https://www.cpapracticeadvisor.com/?p=184461
- **DELOITTE-PULSE-2026**: Deloitte US, *2026 Generative AI in M&A Pulse Study* (survey summary, undated 2026). https://www.deloitte.com/us/en/what-we-do/capabilities/mergers-acquisitions-restructuring/articles/m-and-a-generative-ai-study.html
- **FTI-VCI-2026**: FTI Consulting, *AI Speeds Up Returns in Private Equity as M&A Becomes Top Value Generator* (press release, survey of 555, 2026-06-04). https://www.fticonsulting.com/about/newsroom/press-releases/ai-speeds-up-returns-in-private-equity-as-ma-becomes-top-value-generator-for-firms
- **GT-AIIMPACT-2026**: Grant Thornton, *Private Equity insights: 2026 AI Impact Survey Report* (consultancy survey, fielded 2026-02/03). https://www.grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey-report
- **ICAEW-PE-2025**: ICAEW, *What private equity might mean for a firm's audit status* (professional body, 2025-02-13). https://www.icaew.com/insights/viewpoints-on-the-news/2025/feb-2025/what-private-equity-might-mean-for-a-firms-audit-status
- **JAMA-GI-2025**: *Private Equity Acquisition of Gastroenterology Practices and Colonoscopy Price and Quality* (academic, abstract page, 2025-06-21). https://petris.org/private-equity-acquisition-of-gastroenterology-practices-and-colonoscopy-price-and-quality/
- **JOFA-CULTURE-2018**: Journal of Accountancy, *After the merger: Creating a culture of success* (practitioner guide, 2018-12-01). https://www.journalofaccountancy.com/issues/2018/dec/after-merger-culture-of-success/
- **JOFA-MA-2017**: Journal of Accountancy, *How to comply with the new AICPA ethics standards for M&A* (professional body, 2017-08-02). https://www.journalofaccountancy.com/news/2017/aug/aicpa-ethics-standards-for-mergers-acquisitions-201717098/
- **JOFA-PEEC-2026**: Journal of Accountancy, *PEEC to continue discussions on alternative practice structures* (professional body news, 2026-08-10). https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures.html
- **KPMG-AIDD-2025**: KPMG Switzerland, *AI Due Diligence* (consultancy one-pager, 2025). https://assets.kpmg.com/content/dam/kpmgsites/ch/pdf/ai-due-diligence.pdf.coredownload.inline.pdf
- **NBER-ANESTHESIA-2025**: NBER, *The Price of Consolidation: Evidence from Anesthesia Practice Rollups* (digest of working paper 33217, 2025-03). https://nber.org/digest/202503/price-consolidation-evidence-anesthesia-practice-rollups
- **NEWCOMER-ROLLUP-2025**: Newcomer, *Inside the VC Roll-up Craze That Has Taken Silicon Valley by Storm* (newsletter, 2025-12-18). https://www.newcomer.co/p/inside-the-vc-roll-up-craze-that
- **NJCPA-PE-2026**: NJCPA, *The Rapid Growth of Private Equity Investment in Public Accounting* (professional-society article, 2026-07-17). https://www.njcpa.org/development/dom-test/2026/07/17/the-rapid-growth-of-private-equity-investment-in-public-accounting
- **NYSSCPA-APS-2025**: NYSSCPA, *AICPA Calls for Comments on Ethics Rules Update for Alternative Practice Structures in Private Equity* (professional body news, 2025-12-22). https://nysscpa.org/news/1045198-aicpa-calls-for-comments-on-ethics-rules-update-for-alternative-practice-structures-in-private-equity-2025-12-22
- **PWC-AIDD-ND**: PwC US, *AI and technology due diligence* (consultancy service page, undated). https://www.pwc.com/us/en/services/consulting/deals/strategy-value-creation/ai-technology-diligence.html
- **REUTERS-CRETE-2025**: Reuters (via AOL), *Thrive-backed accounting firm Crete to spend $500 million in AI roll-up* (news, 2025-06-04). https://www.aol.com/news/thrive-backed-accounting-firm-crete-130200514.html
- **RSM-AIDD-2025**: RSM US, *Artificial intelligence: ready or not?* (consultancy guidance, 2025). https://rsmus.com/insights/industries/private-equity/ai-due-diligence-assessment-private-equity.html
- **TAXADVISER-7216-2024**: The Tax Adviser (AICPA), *The many implications of Sec. 7216* (professional body, 2024-01). https://www.thetaxadviser.com/issues/2024/jan/the-many-implications-of-sec-7216.html
- **TECHCRUNCH-AIROLLUP-2025**: TechCrunch, *The AI services transformation may be harder than VCs think* (trade press, 2025-09-29). https://techcrunch.com/2025/09/28/the-ai-services-transformation-may-be-harder-than-vcs-think/
- **WINSTON-APS-2026**: Winston Taylor (published as Winston & Strawn before the firm's 2026-06-01 combination), *AICPA proposes significant changes to ethics rules governing private equity investments in accounting firms* (law-firm summary, page undated, between 2025-12-29 and 2026-06-01). https://www.winston.com/en/insights-news/aicpa-proposes-significant-changes-to-ethics-rules-governing-private-equity-investments-in-accounting-firms
- **WK-PE-2025**: Wolters Kluwer, *Private equity is reshaping the tax and accounting industry* (vendor article, 2025-09-02). https://www.wolterskluwer.com/en/expert-insights/private-equity-is-reshaping-the-tax-and-accounting-industry
- Journey-stage cards and use patterns: `onboarding.md` §5 and `../library/journey-stages.md` §2, with their own sources.
