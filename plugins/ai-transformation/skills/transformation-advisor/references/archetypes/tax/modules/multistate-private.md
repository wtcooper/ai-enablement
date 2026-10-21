# Multistate tax for growing private companies (tax)

Sources checked 2026-10-21. Use cases live in `../use-cases/multistate-private.yaml` (14 entries). Ids are shortened
here: `#05` means `tax-multistate-private-05`; other modules' ids are in full. Source keys in brackets are given in full
in the YAML or in §10. A mid-market extension of the tax archetype.

**Read this first.** Almost every named example in this module is about **state tax agencies** (the counterparty), not
about accounting firms or in-house teams. No top-100, regional or local firm, PE-backed platform or in-house team was
found describing AI in multistate income, franchise or payroll tax work, and no error rate, override rate,
parallel-run result or time saving exists for any multistate AI tool. Firm-side entries are vendor claims (C) or ideas
(D); say so when you quote one. Evidence is thin: 1 of 14 entries is graded B, none A. Use this module for risk
awareness and interview probes, not as proof points.

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

State and local tax (SALT) work for private companies that grow across state lines: **nexus** (the connection with a
state, from sales, payroll, property or people, that creates a duty to file), registration, **apportionment** (splitting
a company's income among states by sales, payroll and property "factors"), state income, franchise and payroll
withholding exposure, **voluntary disclosure** (coming forward to a state for limited lookback and penalty relief) and
the state **pass-through entity tax (PTET)** election. It also covers how state tax agencies use AI and analytics to
find and select taxpayers, because that sets the pace for every engagement. Sales and use tax sits in
[indirect-tax](indirect-tax.md); state return preparation sits in [compliance-corporate](compliance-corporate.md) and
[compliance-individual-business](compliance-individual-business.md); disputes sit in [controversy](controversy.md).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Nexus identification and monitoring | State-by-state, tax-by-tax review of sales, payroll, property and employee locations against each state's tests | data-reporting, expert-judgment | Thresholds keep changing; in 2026 Kentucky dropped its 200-transaction sales tax test and New Jersey issued bright-line corporation business tax nexus guidance [MTC-NEXUSUPD-2026] |
| Registration and foreign qualification | Register to do business in the state (foreign qualification), then open withholding, unemployment insurance and other accounts | transaction-processing, coordination-scheduling | Portal-by-portal manual work; a payroll vendor says withholding registration is required in 41 states and unemployment insurance in all 50 [WARP-REG-2026] |
| Remote workers and residency | Track where employees and owners actually work and live; apply withholding and residency rules | data-reporting, expert-judgment | One employee in a new state can trigger several obligations that existing tools miss [GUSTO-MOSEY-2026]; New York's "convenience of the employer" rule (taxing remote work for a New York employer) is still litigated [MTC-NEXUSUPD-2026] |
| Apportionment and sourcing | Compute sales, payroll and property factors from ledgers; decide sourcing; consider alternative apportionment | data-reporting, expert-judgment | Factors often computed separately by entity, creating reconciliation work and error risk [ALTERYX-APPORT-2026]; rules in flux [MTC-ANNUAL-2026] |
| PTET election | Model whether an entity-level state tax election helps the owners, state by state | expert-judgment, data-reporting | State treatment differs (New York's credit refundable, California's not, for 2025, per a Vals model answer) [VALS-TAXAGENT-2026] |
| State returns | Corporate, PTET, composite (one return filed for many nonresident owners) and nonresident withholding returns | transaction-processing, document-production | Covered in the compliance modules (`tax-compliance-corporate-06`) |
| Exposure review and voluntary disclosure | Quantify unfiled exposure by state, tax and period; choose voluntary disclosure, amnesty or waiting | expert-judgment, document-production, client-interaction | Eligibility usually needs no prior state contact, per a consultancy (not verified against state rules) [SALESTAX-AIAUDIT-2026] |
| State audits and notices | Answer agency selection, data-matching letters and assessments | review-assurance, document-production | Selection criteria not public; few tools to challenge selection [TAXNOTES-UNWATCHED-2026; NTT-BIAS-2026] |
| Law-change tracking | Follow bills, rulings and cases across states; write updates | research-synthesis | One quarter's MTC update lists amnesties, nexus changes, new taxes and court decisions across a dozen states [MTC-NEXUSUPD-2026] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). Firm-side evidence
covers improve only, plus one vendor automate claim. **Delegate has no evidence in this module**; the nearest are
sales tax registration agents (`tax-indirect-tax-13`) and agent-prepared business returns with state apportionment
(`tax-compliance-corporate-06`). The example type is given in brackets.

**State agencies: selection and detection (the counterparty)**
- Improve (augment, process): `#01` (B) South Carolina's DOR signed a $3.5 million, five-year FAST Enterprises contract
  for audit selection inside its GenTax system, starting with business filings, sales and use tax first; California's
  Franchise Tax Board has used machine-learning models since 2021; New York says its selection system is not AI
  [counterparty]. Overlaps `tax-controversy-15`.
- `#02` (C) States link marketplace, payment, payroll and filing data to find unregistered businesses and non-filers;
  claims come from a sales tax training provider, a consultancy and an accounting firm's recap of eight Southeastern
  agencies [counterparty, via commentary].
- `#03` (C) New York residency and remote-worker audits with analytics and mass letters; the AI label is secondhand
  (2024) and disputed by the department [counterparty].
- Idea: `#12` (D) outside review, inventories and bias testing of agency selection models (see `tax-controversy-14`).

**Nexus, registration and remote workers**
- Improve: `#04` (C) AI-assisted nexus study across income, franchise, sales and payroll taxes; a law firm uses it as
  its example of work the practitioner must verify state by state; vendors advertise agents answering nexus questions
  [law firm, vendors]. Sales tax nexus agents: `tax-indirect-tax-13`.
- Automate: `#05` (C) a new hire's work location triggers withholding, unemployment and foreign-qualification
  registrations handled by a platform; Gusto (with Mosey), Warp and Skyvern claim this, aimed at small business
  [vendors]. Registration does not settle income or franchise tax nexus.
- Improve (idea): `#09` (D) a company scans its own data for the signals states match on before a notice arrives
  [consultancy and firm advice; no AI scan deployed]. Related: `tax-compliance-corporate-13`.

**Apportionment and PTET**
- Improve: `#06` (C) factors computed from reconciled ledgers by rules, checked against prior periods, with optional AI
  commentary; the AI is not the calculation [vendor].
- Improve: `#14` (C) PTET election modelling: an AI-native tax firm's calculator and a vendor's illustrative Maryland
  example [AI-native firm, vendor]. Owner-level S-election modelling sits in research-advisory.

**Research and law-change tracking**
- Improve (assist): `#07` (C) research assistants for nexus, PTET and sourcing questions with authorities checked; the
  only quality evidence is one public benchmark question [vendors; COST workshop with Big Four and company presenters].
  General research tools: `tax-research-advisory-01` to `-08`; state-by-state idea: `tax-research-advisory-04`.
- Idea: `#08` (D) in-house SALT teams draft quarterly updates, compare bill versions and review appeal arguments
  (workshop demonstrations only). General monitoring: `tax-compliance-corporate-12`, `tax-research-advisory-23`.

**Defence and remediation**
- Improve (idea): `#10` (D) defending AI-informed state assessments with data analytics, documentation and human
  judgment (a law firm's conference talk) [law firm].
- Reinvent: `#11` (C) exposure review and voluntary disclosure marketed on the back of state AI enforcement; the work
  is human [consultancy; MTC as baseline].
- Reinvent: `#13` (C) AI companies as a new SALT client segment (digital product classification, cloud nexus, remote
  staff, sourcing): demand created by AI, not AI in the work [accounting firms, vendor].

## 4. Interview probes

1. Where are your people actually working today, who tracks it (HR, payroll or tax), and when did anyone last compare
   that list with your state withholding and unemployment accounts? *Reveals payroll-nexus exposure and whether `#05`
   would have clean location data to work from.*
2. When was the last nexus review that covered income and franchise tax, not only sales tax, and what data fed it?
   *Shows whether nexus work is sales-tax-only and how much of `#04` is data gathering versus judgment.*
3. If a state notice arrived tomorrow citing third-party data, how long would it take to assemble your apportionment
   support, and from which systems? *Measures readiness for data-driven selection (`#01`, `#02`) and the case for `#06`.*
4. Do you compute factors per entity in spreadsheets, and who reconciles them to the ledger and to last year?
   *Reveals the reconciliation burden `#06` targets and whether prior-period checks exist.*
5. Are there states you suspect you should be registered in? What has stopped you from voluntary disclosure, and does
   anyone scan for it? *Tests appetite for `#09` and `#11`, and whether contact with a state could cost eligibility.*
6. If you or your adviser used AI on a nexus or apportionment conclusion, who verifies thresholds, rates and effective
   dates state by state, and where is that recorded? *Shows whether verification is designed in, as KTS describes
   [KTS-OPR-2026].*
7. Which research tool answers your state questions today, and have you caught it wrong on a state rule or a stale
   effective date? *Grounds `#07` in the user's own failure cases; benchmark evidence is one question.*
8. Who builds PTET and entity-election estimates for owners, and are owners arriving with their own calculator
   numbers? *Reveals exposure to `#14` and the written-advice standard applied.*
9. Have you had a state audit or letter in the last two years where you could not tell what triggered it? What did you
   ask for? *Shows how the firm handles opaque selection (`#10`, `#12`).*
10. Are any clients AI companies selling digital products or automated services into many states? *Sizes the
    new-segment opportunity in `#13`.*
11. What would show that AI shortens a nexus study or reduces re-work, and do you collect it today? *Most firms
    cannot answer; this is the measurement gap for the whole module.*

## 5. Metrics and benchmarks

| Metric | Figure | Provenance | Source |
|---|---|---|---|
| State agency AI use | 7 of 36 responding agencies used AI (chatbots to machine learning); 22 none; 6 interested; 49 surveyed (2025) | independent | [TAXNOTES-UNWATCHED-2026] |
| California high-risk automated decision systems (AB 302 inventory, 2025) | 0 agencies reported one; experts told Tax Notes this was not credible given the FTB models | independent | [NTT-BIAS-2026] |
| MTC Multistate Voluntary Disclosure Program, FY2026 | 464 executed agreements; $28,308,873 collected; average $61,010 (FY2025: 498 and $29,083,242); 40 participating states including DC | independent | [MTC-NEXUSDIR-2026] |
| MTC voluntary disclosure applications | 190 taxpayers in calendar 2025; 95 as of 30 Jun 2026; most based on sales tax economic nexus | independent | [MTC-NEXUSDIR-2026] |
| MTC Joint Audit Program, FY2026 | Proposed net assessments $80,563,369 (income tax) and $3,179,204 (sales tax); 13 income tax and 22 sales tax audits in progress | independent | [MTC-AUDITDIR-2026] |
| New York audits, 2022 | 771,000 audits (up 56% on 2021); auditors down 5% to under 200; AI share not stated | self-reported via press (2024) | [YAHOO-NYAI-2024] |
| South Carolina return volume | 5 to 6 million returns (deputy director) | self-reported via press | [SCPOST-AUDIT-2026] |
| Vals Tax Agent Bench, one public SALT question (New York versus California PTET credit) | Leader 91%; three models 76.5%; one passed all checks (2026-10-20 read; `tax-research-advisory-04` reports an earlier reading) | independent (commercial evaluator) | [VALS-TAXAGENT-2026] |
| Vals Tax Agent Bench headline (adjacent, mostly federal corporate) | Best model 49.19% on 193 private questions; no SALT-only score | independent (commercial evaluator) | [VALS-TAXAGENT-2026] |
| Manual registration baseline | 15 to 30 minutes per state filing; no sample or method | vendor-published | [SKYVERN-REG-2026] |
| PTET saving (illustrative) | $22,222 per year for an illustrative Maryland client in a sample report | vendor-published | [FILED-HOME-2026] |

No audit-yield, no-change-rate or false-positive figure has been published by South Carolina, California or New York
[SCPOST-AUDIT-2026]. The MTC figures are a demand baseline, not a measure of AI; agreements and collections fell year on
year, so the sources do not show state AI raising disclosure volume [MTC-NEXUSDIR-2026]. What to measure in an
engagement: hours per nexus study and per state registration, review notes on apportionment, notices received per
year and time to assemble support, and verification findings on AI-assisted state answers.

## 6. Guardrails

**Practitioner rules**
- IRS OPR Alert 2026-19 (released 24 Jun 2026) applies existing Circular 230 duties to AI [IRS-OPR-2026]. A law firm
  applies it to a state nexus study: AI output is a draft, the practitioner verifies thresholds, rates and dates, uses
  only firm-approved systems for client data, and remembers §§6713 and 7216 and §10.36 firm procedures
  [KTS-OPR-2026]. The alert is federal; **no state board of accountancy or state revenue department guidance on
  AI-assisted state tax work was found**. Archetype-level rules are in [guardrails.md](../guardrails.md).
- Written advice (§10.37) applies to PTET and other planning estimates [IRS-OPR-2026].

**Agency AI and its oversight**
- Selection criteria are not public. Tax Notes reporters found no outside audit or legislative report of the FTB
  models, though the FTB runs internal checks for over-selection of certain groups [NTT-BIAS-2026].
- Whether a system "is AI" is contested (New York's CISS), which decides which oversight laws apply; California's AB
  302 inventory reported zero high-risk systems [NTT-BIAS-2026; TAXNOTES-UNWATCHED-2026]. New York's Comptroller found
  no statewide AI inventory in April 2025, in four non-tax agencies [NYOSC-AIAUDIT-2025].
- Experts in the South Carolina story stress human oversight at every step and warn of opaque algorithms and
  unintended discriminatory results [SCPOST-AUDIT-2026; KOGOD-SC-2026].
- California CDTFA: written-advice protections do not extend to verbal advice, so a taxpayer relying on an agent's
  AI-assisted oral answer may not be protected [CDTFA-2025].

**Disclosure and registration**
- Voluntary disclosure normally needs no prior contact; a company that registers or is contacted first can lose
  eligibility. This is a consultancy's statement, not verified against state programme rules [SALESTAX-AIAUDIT-2026].
- A scan that finds exposure (`#09`) can affect that choice; keep disclosure decisions with a professional.

**Steps that need human judgment:** every nexus conclusion and its effective dates; whether and when to register,
disclose or wait (the consultancy lists registering, fixing past periods and judgment calls as things AI cannot do)
[SALESTAX-AIAUDIT-2026]; apportionment and sourcing positions, including alternative apportionment; PTET and entity
advice to owners; the response to any state assessment; on the agency side, every audit conducted (South Carolina's
system suggests, auditors conduct) [SCPOST-AUDIT-2026].

## 7. Roles and how they evolve

- **Practitioners:** remain responsible for the final work whatever the AI did [KTS-OPR-2026]. An accounting firm's
  conference recap advises documentation, accurate reporting and periodic tax health checks as states find issues
  earlier [WITHUM-SEATA-2026].
- **Owners and small businesses:** Gusto positions registration work as moving from the owner or a lawyer to the
  platform [GUSTO-MOSEY-2026]; Gelt describes owners moving from their own estimate to expert execution with the firm
  [GELT-CALC-2025].
- **SALT specialists outside firms:** AI developers recruit SALT experts with five or more years' experience (Big 4,
  national firm, law firm, state revenue department or corporate tax backgrounds preferred) to grade model answers on
  nexus, nonresident withholding and composite filing [MERCOR-SALT-2026].
- **In-house:** an academic argues AI agents will not shrink corporate tax teams much because AI cannot bear
  culpability (abstract only) [SALA-TAXNOTES-2026].
- **State agencies:** the FTA's chief operating officer expects training to be the main workforce need and the tools
  unlikely to take jobs soon [TAXNOTESTALK-2025]. South Carolina says it is unclear whether its system will mean more
  audits; the aim is a better hit rate and fewer no-change audits [SCPOST-AUDIT-2026]. The MTC audit programme reported
  unusually high staff turnover in FY2026 (retirements); no link to AI is stated [MTC-AUDITDIR-2026].

## 8. Frontier

| Date | Signal | Source |
|---|---|---|
| 2025-12 | South Carolina DOR signs a $3.5 million, five-year audit contract; sales and use tax first, then corporate; may extend to individuals with up to three years' lookback | [SCPOST-AUDIT-2026] |
| 2025-12-29 | Gelt, an AI-native tax firm, launches AI calculators including PTET | [GELT-CALC-2025] |
| 2026-03-02 | COST "SALT in a Digital World" workshop opens with a half-day of AI sessions, including building a basic agent | [COST-TECH-2026] |
| 2026-04-13 | Gusto announces its Mosey acquisition; integrated compliance product expected later in 2026 | [FINTECHGLOBAL-GUSTO-2026] |
| 2026-06-23 | FTA podcast from its annual meeting with Wisconsin, Georgia, Tennessee and Nevada revenue officials on AI (description only) | [FTA-TAXBREAKS-2026] |
| 2026-06-24 | OPR Alert 2026-19 | [IRS-OPR-2026] |
| 2026-07-29 | MTC panel on the impact of AI on state tax administration and practice (FTA, Pennsylvania DOR, Blue J); the Nexus and Audit committee materials do not mention AI | [MTC-ANNUAL-2026] |
| 2026-07-31 | A vendor executive says states introduced more than 1,000 AI-related bills in 2025 (commentary, not checked) | [ROUTEFIFTY-REV-2026] |
| 2026-09-17 | Truss and Kintsugi webinar listing promises live AI agents answering nexus questions across a client portfolio | [TRUSS-KINTSUGI-2026] |
| 2026-09-23 | Akerman announces a COST annual meeting session on defending AI-driven assessments (talk content not seen) | [AKERMAN-COST-2026] |
| Later 2026 | Gusto Business Compliance expected to launch | [GUSTO-MOSEY-2026] |

Direction: the landscape scan expects multistate private companies to see earlier, data-driven notices; that is a
reading of the agency signals above, not a measured trend. Not yet moved: any state guidance on AI-assisted state tax
work, any published state audit-yield figure, any firm-side SALT AI deployment.

## 9. Common objections

- **"States aren't really using AI."** Partly right: 22 of 36 responding agencies said none, and the FTA says most
  have used older machine learning for years for processing and fraud [TAXNOTES-UNWATCHED-2026]. But South Carolina
  and California run selection models now [SCPOST-AUDIT-2026; NTT-BIAS-2026]. Prepare for data-matched notices
  without assuming every state does it.
- **"It's a black box, so there's nothing to do."** Criteria are unpublished and taxpayers lack tools to challenge
  selection [TAXNOTES-UNWATCHED-2026; NTT-BIAS-2026]. The practical counter is reconciling your own footprint first
  (`#09`) and keeping documentation ready [WITHUM-SEATA-2026].
- **"The enforcement scare is marketing."** Often true: the strongest detection claims come from firms that sell
  compliance help [SALESTAX-AIAUDIT-2026; STI-AIAUDITS-2026], and MTC disclosure volumes fell year on year
  [MTC-NEXUSDIR-2026]. Use the agency sources, not the sales pages.
- **"AI can do the nexus study."** No source shows it. A law firm treats AI output as a draft that must be verified
  state by state [KTS-OPR-2026], and the only quality evidence is one benchmark question [VALS-TAXAGENT-2026].
- **"Payroll handles registrations now."** Vendors say so for small business, with no accuracy figures, and
  registration does not answer income or franchise tax nexus [GUSTO-MOSEY-2026].
- **"AI will shrink the SALT team."** One academic argues it will not, because AI cannot bear culpability
  [SALA-TAXNOTES-2026]; nothing measured either way.
- **"There's no proof it works for us."** Accurate. Start with a bounded step (factor reconciliation `#06` or a
  research check `#07`), baseline hours and review notes, and keep the professional judgment calls with people.

## 10. Sources

Full titles, URLs, dates and locators are in the YAML. Keys used here but not in the YAML:

- CDTFA-2025: Experts Urge Caution as State Tax Agencies Deploy Generative AI (Tax Notes, copy hosted by Kogod,
  2025-08-26), https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf
- FTA-TAXBREAKS-2026: Tax Breaks LIVE: A Million Ideas, One Question: Where Do You Start? (Federation of Tax
  Administrators podcast, episode description, 2026-06-23), https://rss.com/es/podcasts/taxbreaks/
- SALA-TAXNOTES-2026: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State, abstract on TaxProf
  Blog, 2026-07-20), https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/

Related modules: [indirect-tax](indirect-tax.md) (sales tax nexus and registration), [controversy](controversy.md)
(state notices and authority AI), [compliance-corporate](compliance-corporate.md) (state returns),
[research-advisory](research-advisory.md) (research tools, entity choice).
