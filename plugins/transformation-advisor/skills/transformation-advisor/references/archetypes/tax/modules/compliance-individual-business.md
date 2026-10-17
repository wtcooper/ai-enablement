# Individual and small-business return preparation (tax)

Last reviewed 2026-10-17. Use cases live in `../use-cases/compliance-individual-business.yaml` (25 entries). Ids are
shortened here: `#05` means `tax-compliance-individual-business-05`; other modules' ids are in full. Source keys in
brackets, such as [WCG-NOTREADY-2026], are given in full in the YAML or in §10. **Evidence is thin.** One entry is
grade A, and it rests on vendor-published figures about named firms; 9 are grade B (a named deployment without
published numbers). No independent error rate, override rate or parallel-run result exists for any AI-prepared
return. Say so when you quote a figure.

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

Preparing individual (1040), trust (1041), partnership (1065) and S corporation (1120-S) returns, and UK self
assessment, by CPA firms, enrolled agents and retail preparers such as H&R Block. It runs from engagement and
consent through document collection, extraction, preparation, review, signature and e-file, to pricing and the
advisory conversation built on the return. Corporate and in-house direct-tax compliance is in the compliance-corporate
module; notices after filing are in controversy; research tools are in research-advisory.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Engagement and consent | Engagement letter; section 7216 consent (written client permission to use or disclose return data; Form 1040 wording fixed by Rev. Proc. 2013-14) | document-production, client-interaction | No AI-specific consent guidance; unclear whether an AI vendor is "software" or a third party [BARMORE-OPR-2026] |
| Organizer and document request | Send the organizer, chase missing items, check what arrived | client-interaction, coordination-scheduling | Weeks of manual reminders; one missing brokerage statement can hold up a return; clients text photos [CPAPA-POSTEXT-2026, TAXADVISER-CLIENTS-2026] |
| Intake and extraction | Classify W-2s, 1099s, K-1s, brokerage statements; key or import data | transaction-processing | Importing data is the lowest-rated software attribute (3.4 of 5) [AICPA-TAXSW-2026]; K-1 footnotes defeat template OCR |
| Due-diligence interview | Interview and Form 8867 for earned income, child and education credits and head of household | client-interaction, expert-judgment | Personal, contemporaneous duty; $650 per credit penalty for a 2026 filing [IRS-I8867-2025] |
| Preparation | Federal and state logic, workpapers, depreciation, basis, allocations; trial-balance mapping for 1065 and 1120-S | transaction-processing, expert-judgment | Short season, staff shortage; spreadsheets; tax software re-runs upstream work [WCG-NOTREADY-2026] |
| Research for positions | Schedule C, partnership and S corporation items | research-synthesis, expert-judgment | Hallucinated authority (*Clinco*) [TAXCT-CLINCO-2026] |
| Review | Preparer, manager and partner review | review-assurance | Senior time; review thins as volume rises ("control dilution") [AICPA-WERFEL-2026] |
| Delivery, signature, e-file | Assembly, Form 8879 e-file authorisation, payment, filing | coordination-scheduling, document-production | Signing edge cases; final steps still inside the tax software [TR-TRUST7-2026, WCG-NOTREADY-2026] |
| Billing and advisory | Fee basis; planning conversation from the return | client-interaction, expert-judgment | OPR fee language vs value pricing [AICPA-FEES-2026]; 93% use no tool to find planning opportunities in returns [AICPA-TAXSW-2026] |

**Context on the pain.** A Black Ore launch article attributes about 300,000 net departures from the profession to the
Bureau of Labor Statistics and a 17-year low in CPA exam candidates to the AICPA; its 125-million-hour shortfall is
Black Ore's own unattributed figure [BLACKORE-2026]. For solo practitioners and firms of up to 10 staff, tax law
complexity ranks first in the AICPA's 2026 top-issues survey, ahead of AI [AICPA-TOPISSUES-2026]. The pre-LLM
baseline is scan-and-push extraction (SurePrep into UltraTax); WCG still uses it for about 4,500 1040s at about $25 a
return by its own estimate [WCG-NOTREADY-2026, TR-MADSEN-2026]. A CPA Trendlines teaser (body gated) reported fewer
returns produced, rising salaries and flat-to-down headcount in the 2026 season [CPATL-SEASON-2026].

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). Every ladder level
and change scope has entries, but automate and delegate rest on vendor claims, and model-scope change has one B entry
(`#24`). Seven entries are controls, enablement or ideas rather than AI deployments (`#10`, `#13`, `#18`-`#22`).

**Intake and data capture**
- Improve: `#01` AI-prefilled organizers, tailored request lists, chasing and missing-information questions (Canopy,
  Basis; up to 20 minutes per client, vendor claim). The Form 8867 interview stays personal.
- Automate: `#02` classification, extraction and K-1 footnote mapping with confidence flags; only exceptions reach a
  reviewer (CCH Axcess Scan, PwC, ProConnect). `#03` H&R Block removes manual data entry in pilot offices to free
  appointment time for advice.

**Preparation**
- Improve: `#04` Thomson Reuters Ready to Review drafts simple 1040s for review (about an hour saved per return, one
  partner's estimate). `#07` trial balance mapped to 1120-S and 1065 workpapers (Basis). `#10` idea: a deterministic
  engine calculates, the model handles intake and explanation.
- Delegate: `#05` end-to-end agents for complex, K-1-heavy individual returns (Black Ore, Basis, Accrual; OpenAI's
  7,000-return pilot with Crete firms); the only grade A, all vendor-published. `#06` partnership, S corporation and
  trust returns to K-1s (Accrual at Armanino; Basis 1065 demonstration). `#08` an agent works inside the firm's own
  tax software, one agent per return (TaxGPT). `#09` general agents run taught routines (Accrual Arc; a practitioner
  using Claude Cowork).

**Research and review**
- Improve: `#11` grounded assistant for code changes and return positions (H&R Block Sidekick), every authority
  verified. `#12` AI review with source tie-out, diagnostics, prior-year variance and audit-sensitive flags.
  `#13` idea: decision logs, override-rate monitoring and scaled sampling so review does not thin.
- Automate: `#14` H&R Block's "Second Look" look-back of three prior years for every new client; new clients who got
  it returned at a rate 600+ basis points higher (the service, not the AI, is measured).

**Client communication, delivery and other jurisdictions**
- Improve: `#15` AI-drafted status messages, return explanations and plan comparisons (32% of CPA preparers use AI
  for client communication). `#17` UK self assessment and Making Tax Digital preparation (ApariPro).
- Automate: `#16` assembly, e-signature and Form 8879 routing (SafeSend, vendor claim of 15 minutes per return).

**Adoption and governance (controls that make the rest safe)**
- Improve: `#18` phased adoption: simple returns first, scope gates, parallel runs on last year's returns. `#19` AI
  policy, approved tools under the written information security plan (WISP), vendor diligence. `#20` AI pod,
  champions and failure-mode training that protects the junior pipeline (PwC, WCG). `#21` disclosure and section
  7216 consent.

**Operating and business model**
- Reinvent: `#22` idea: value or bundled pricing as hours fall. `#23` AI replaces offshore and contract first-pass
  preparation. `#24` AI-native roll-ups buy small practices (Multiplier: margins more than doubled at one boutique).
  `#25` taxpayer-side agents draft or check returns (Perplexity), bypassing or auditing the preparer.

## 4. Interview probes

Ask in the person's own setting (small CPA firm, mid-tier firm, enrolled agent, retail office, UK practice).

1. **"Walk me through one 1040 from organizer to e-file. Where do the hours go, and how many returns do you do?"**
   Reveals the baseline and whether the pain is chasing (`#01`), keying (`#02`), preparation (`#04`-`#06`) or review.
2. **"Where does the AI's work end and your tax software's begin? How many times is each return calculated or
   diagnosed?"** Reveals duplicated checks and WCG's "last mile" problem: no vendor completes a return inside the
   firm's software (`#05`, `#08`).
3. **"Do your tools handle K-1s and consolidated 1099s?"** Reveals fit for complex returns; WCG treats it as a
   minimum bar (`#02`).
4. **"Which step would you let run unreviewed, and what evidence did you collect: parallel runs, error counts,
   override rates?"** Reveals whether any quality evidence exists. Usually none does (`#18`).
5. **"When an AI-prepared return reaches your reviewer, what do they see and how long do they get? Have you seen a
   reviewer accept a wrong AI answer or override a right one?"** Reveals control dilution and rubber-stamping (`#12`, `#13`).
6. **"Which returns would you never route to an agent?"** Reveals the complexity line (many states, entity returns,
   novel allocations) and whether intake classifies complexity (`#06`, `#18`).
7. **"Which AI tools touch client return information, where does the data go, and what do your engagement letter
   and 7216 consent say?"** Reveals exposure under sections 7216 and 6713 and readiness for OPR's "secure,
   enterprise-approved AI" (`#19`, `#21`).
8. **"Who owns AI in the firm: a pod, a partner, nobody? What would move you from evaluating to committed?"**
   Reveals governance under Circular 230 section 10.36 and adoption stage (`#20`).
9. **"How do you price returns now, and what happened to hours per return last season? Have you read the OPR fee
   language?"** Reveals business-model pressure and section 10.27 risk (`#22`).
10. **"How do juniors learn to spot a wrong W-2 box 12 treatment or a fake citation if AI does the first pass?"**
    Reveals skill-erosion risk and training design (`#20`).
11. **"How much first-pass work is offshore or contract today, and what happens to it?"** Reveals where labour
    effects land first (`#23`).
12. **"Are clients bringing AI-drafted returns or questions? Are you losing simple returns?"** Reveals
    disintermediation risk and the validation work it creates (`#25`).

## 5. Metrics and benchmarks

**Baselines to ask for first**
- Hours per return by complexity tier; median days from organizer sent to documents complete; days from finished
  return to signed authorisation and paid invoice (the measures CPA Practice Advisor recommends) [CPAPA-POSTEXT-2026].
- Cost per return of the current extraction tool (WCG: about $25 for SurePrep, its estimate) [WCG-NOTREADY-2026].
- Old human-error baseline: in a 2014 GAO study 2 of 19 paid preparers computed the correct refund; GAO estimated
  errors in 60% of preparer-prepared vs 50% of self-prepared returns (tax years 2006-2009) [GAO-14467T-2014].

**Named outcomes (vendor-published or self-reported; time, not quality)**
- Boulay: returns with 60-70+ K-1s from 100+ hours to "maybe 15 or 20" (Basis testimonial) `#05`.
- Crete firms pilot (7,000 returns): about a third less preparation time, up to 97% accuracy, about 50% more
  throughput (OpenAI) `#05`.
- CLH CPAs: about one hour saved per simple 1040 (partner's estimate, vendor release) `#04`.
- Kulangy CPA: returns completed in half the time (ProConnect) `#02`. Whitcomb & Sheridan: 10-20 hours a week (Basis) `#07`.
- Multiplier: one 12-person boutique's margins more than doubled `#24`. H&R Block Second Look: +600 bp return rate `#14`.

**Vendor claims (grade C; ask for named, measured cases)**: Black Ore >99% accuracy across tens of thousands of pilot
returns, up to 98% time saving, review time cut by over 50%, cost per return down up to 80% (`#05`); CCH Axcess Scan
97.5% K-1 extraction accuracy (`#02`); TaxGPT 90% less first-pass time and 45 minutes per 1040 (`#08`); SafeSend 15
minutes and about $12,000 per 1,000 returns (`#16`). Pricing reported by WCG: Black Ore $100-150 per return on average.

**Adoption benchmarks**
- AICPA 2026 tax software survey (1,808 members who prepared 2025 returns for a fee): 65% use AI for tax research,
  32% for client communication, 16% have no plans to use AI (24.3% a year earlier); 41.2% had any training in their
  tax software [AICPA-TAXSW-2026].
- Thomson Reuters (vendor-owned): 81% of tax and audit professionals use AI regularly; more than one-third use
  unsanctioned tools [TR-FOP-2026]. Wolters Kluwer (Jan 2025): 25% of firms had AI policies [WK-FRA-2025].

**Accuracy benchmarks (none tests a commercial preparer)**
- TaxCalcBench (Column Tax authors, who sell a deterministic engine): best mid-2025 model fully correct on 32.35% of
  51 simplified federal returns; 2026 edition (tax year 2025, 50 cases): 0-71.43% strict, 40% best without web
  search `#10`. Columbia's TaxBench (500+ rules, field-level scoring) is unreleased [COLUMBIA-TAXBENCH-2026].
- Consumer chatbots: average error above $2,000 across eight scenarios in a TaxSlayer test `#25`.

**What to measure (recommend these, not hours alone)**: hours per return by tier before and after; reviewer override
and disagreement rates; errors caught in review; notices and amended returns on AI-prepared returns; differences
from prior-year returns in the transition year; cycle times; cost per return including AI licences. Werfel's
illustrative gates (hallucination 2% or less, error rate 1% or less, override rate below 5% triggers review) are a
starting point, not a standard [AICPA-WERFEL-2026].

## 6. Guardrails

**Standards and regulators ("existing duties apply"; no rule bans AI)**
- **IRS OPR Alert 2026-19 (24 Jun 2026)** maps AI onto Circular 230: section 10.22 due diligence (verify facts,
  citations and calculations), 10.27(a) fees (do not bill manual time not spent; credit savings), 10.35 competence
  (understand how the tool works and its limits), 10.36 firm procedures (training, data handling, accuracy
  monitoring, vendor vetting, documented), 10.37 written advice, and 10.51(a)(15) with IRC sections 6713 and 7216
  [IRS-OPR-2026]. It calls itself introductory; the AICPA's CEO called its fee language non-authoritative
  [AICPA-FEES-2026]. Section 10.34(a) (no signing a return with a position lacking reasonable basis) also applies
  [TREAS-C230-2014]. The IRS said it will merge OPR with the Return Preparer Office [JOFA-OPR-2026].
- **Section 7216 and 6713 regulations**: written, signed, dated consent naming purpose and recipient; no retroactive
  consent; limits on disclosure abroad and on SSNs; software developers count as preparers. None of this mentions AI,
  and how it applies to an LLM vendor is unresolved; take advice [TREAS-7216-2008, IRS-RP201314-2013, BARMORE-OPR-2026].
- **IRS operating rules that ignore AI**: Publication 1345 (the taxpayer reviews the return before signing Form
  8879), Form 8867 instructions (personal interview, notes kept 3 years), Publications 4557 and 5708 (FTC Safeguards
  Rule: qualified individual, risk assessment, service-provider contracts, MFA, 30-day breach reporting)
  [IRS-PUB1345-2025, IRS-I8867-2025, IRS-PUB5708-2024].
- **AICPA SSTS 1.4** (reliance on tools): tools may be relied on reasonably but do not remove responsibility
  [TAXCT-CLINCO-2026]. **Werfel's preparer register** (15 risks in five layers; a proposal) will be tested and
  refined by the AICPA's Council on AI Risk in Tax, launched 23 Sep 2026 [AICPA-WERFEL-2026, AICPA-CART-2026].
- **UK**: PCRT AI guidance (19 Jan 2026): members stay responsible; client data in a public model without consent is
  likely a confidentiality breach [PCRT-AI-2026]. HMRC expects monitoring, version control and human oversight in
  generative-AI tax software [HMRC-GENAI-2026]. **Australia**: TPB(GS) 55/2026 (22 Jul 2026): competence, reasonable
  care, client permission (a signed engagement letter can give it), documented verification [TPB-GS55-2026].
- **Courts**: *Clinco* (T.C. Memo. 2026-16): three of four cited cases apparently hallucinated; no sanctions, but "a
  recipe for sanctions" [TAXCT-CLINCO-2026]. OPR notes AI laws in California, Colorado, Illinois and Utah [IRS-OPR-2026].

**Design guardrails seen in products and guidance**
- Every figure linked to its source document; low-confidence extractions routed to a person (`#02`, `#12`).
- The firm's tax software stays the system of record; agents propose changes and wait for approval (`#06`, `#08`, `#09`).
- Calculation in a deterministic engine, not the language model (`#10`).
- Vendor terms: SOC 2, no training on client data, zero data retention, model-change notice (`#05`, `#19`).
- Start with simple returns, run last year's returns in parallel, gate expansion on measured error rates (`#18`).

**Steps that stay with a person**: the Form 8867 due-diligence interview; positions and eligibility judgments;
book-to-tax, allocation and depreciation decisions on entity returns (WCG); verifying every cited authority; partner
review and signature; the taxpayer's review before signing; consent and fee decisions.

## 7. Roles and how they evolve

- **Preparers become reviewers.** Vendors describe "start at review"; an anonymous Juno customer says "I'm reviewing,
  and that's a completely different job" [JUNO-SITE-2026]. WCG says Black Ore "replaces the first-level preparer, not
  the last mile" (`#05`).
- **Review is the new bottleneck.** PwC: one reviewer where three gathered on a K-1 footnote (`#02`); TEI attendees
  worry about "polite, quiet and technical" errors (`#12`); Werfel names control dilution (`#13`).
- **Retail tax pros move to advice.** H&R Block says less collecting and entering, more guidance and planning, and
  year-round associate development (`#03`).
- **New roles**: AI pods and champions (WCG, PwC's 3,200+ champions); accountants hired by vendors to shape agent
  behaviour (Basis); AI leads under section 10.36 (`#19`, `#20`). CPA Trendlines (gated) reports firms adding far
  more sales, finance and systems staff than accountants since 2021 (`#20`).
- **Juniors and skill erosion.** Thomson Reuters tells firms to protect early-career development; Werfel warns staff
  may learn the tool rather than the law (`#20`). More than a quarter of professionals would not join a firm without
  professional-grade AI [TR-FOP-2026].
- **Outsourcing first.** Commentators expect offshore and contract preparers to feel the change before onshore staff (`#23`).
- **AI-informed clients.** Taxfix says accountants will validate, explain and correct what clients bring (`#25`).

## 8. Frontier

- **2025-06-16** RSM launches myRSM Tax on its $1 billion technology and AI investment; no outcomes [RSM-MYRSM-2025].
- **2025-11-05 / 12-15** Thomson Reuters announces Ready to Review; says it is generally available from 15 Dec and
  expects each CPA to pair with at least one virtual agent [TR-COCOUNSEL-2025, TR-R2R-2025].
- **2026-01-19 / 06-24 / 07-22** PCRT, OPR and TPB guidance: existing duties apply [PCRT-AI-2026, IRS-OPR-2026, TPB-GS55-2026].
- **2026-02-05 / 02-26** Accrual launches ($75M, "all forms", complex K-1 work first) [ACCRUAL-LAUNCH-2026]; Basis
  raises $100M and shows an agent completing a 1065 [BASIS-2026].
- **2026-03-24 / 04-02** TaxGPT launches preparation and return-review agents [TAXGPT-2026]; Perplexity launches a
  consumer agent that drafts federal returns [PERPLEXITY-2026].
- **2026-04-29** Black Ore opens Tax Autopilot after a two-year, 75-firm pilot; about 3,700 firms waiting [BLACKORE-2026].
- **2026-06** Black Ore summit: predictions of autonomous individual preparation by 2027, entities soon after
  [BLACKORE-SUMMIT-2026]. Column Tax releases a harder TaxCalcBench (tax year 2025) [COLUMN-TCBREPO-2026].
- **2026-07-24** WCG declines to commit to any AI preparer for 2026; Ready to Review K-1 support reported on a
  November 2026 roadmap; WCG's AI Tax Prep Pod starts November 2026 [WCG-NOTREADY-2026, WCG-PLAYBOOK-2026].
- **2026-08-11** H&R Block will expand its AI-supported office model to a full market in tax season 27 [HRB-Q4CALL-2026].
- **2026-08-20** Runtime Wire reports OpenAI's 7,000-return pilot with Crete firms [RUNTIMEWIRE-2026, OPENAI-CODEX-2026].
- **2026-09-08 / 09-23** AICPA asks the IRS to clarify the fee language [AICPA-FEES-2026]; CART launched [AICPA-CART-2026].
- **2026-09-22** Accrual's Arc: the practitioner sets an objective, approves the plan and reviews the result [ACCRUAL-ARC-2026].
- **Undated** Basis announces an end-to-end tax platform from intake to review [BASIS-E2E-2026]. Watch: TaxBench
  release; IRS answer to the AICPA; any AI-specific section 7216 guidance; WCG's November re-evaluation.

## 9. Common objections

- **"It isn't really end to end."** Often true. WCG found no vendor completes a return inside its tax software, and
  K-1 and consolidated-1099 coverage was missing or on a roadmap. Ask where the handoff is and test with your
  ugliest returns (`#05`, `#08`).
- **"The accuracy claims are unproven."** Correct: every figure is vendor-published or self-reported, and
  TaxCalcBench shows unaided models fail most returns. Even Thomson Reuters tells buyers to ask who checked the
  numbers. Run last year's returns in parallel and track overrides (`#10`, `#18`).
- **"Review will eat the savings."** A real risk (control dilution; the AI had the right figure but lost it in an
  adjacent close study). Design review: source links, decision logs, escalation of novel positions (`#12`, `#13`).
- **"It costs more than what we have."** WCG compares $100-150 per return with about $25 for SurePrep and says AI
  adds about 25% to its technology stack. Price by complexity tier and start where hours are largest (`#05`, `#18`).
- **"OPR says we must pass on the savings."** OPR says billing time not spent may breach section 10.27(a); the
  AICPA disputes the language and is seeking FAQs. Document a fee basis before savings accrue (`#22`).
- **"We can't put client data in AI."** Not in public tools: use enterprise tools with no training and zero
  retention, under the WISP, with a consent decision made with counsel (`#19`, `#21`).
- **"Year-one returns will look different and invite audits."** Firm leaders raised this with Black Ore; review the
  prior-year differences in the transition year (`#05`).
- **"Clients will do it themselves."** Some will try (`#25`), but chatbots erred by $2,000+ on average in one test
  and 81% of UK filers surveyed by Taxfix still want access to a professional. Expect to validate AI-informed clients.
- **"Who is liable?"** The signer. A vendor contract does not move responsibility for positions filed, and provider
  indemnities generally do not cover confidentiality or accuracy exposure (`#19`).

## 10. Sources

Full details (title, publisher, type, URL, date, access) are in the YAML.
- **Regulators and standard-setters:** IRS-OPR-2026; TREAS-7216-2008; IRS-RP201314-2013; TREAS-C230-2014; IRS-I8867-2025;
  IRS-PUB1345-2025; IRS-PUB4557-2024; IRS-PUB5708-2024; GAO-14467T-2014; TAS-AIBLOG-2024; TPB-GS55-2026; HMRC-GENAI-2026.
- **Professional bodies:** AICPA-WERFEL-2026 (appendices); TAXADVISER-WERFEL-2026 (article); AICPA-CART-2026;
  AICPA-FEES-2026; PCRT-AI-2026; ATT-PCRTAI-2026; NAEA-AI-2026; TAXCT-CLINCO-2026.
- **Firms:** WCG-NOTREADY-2026; WCG-PLAYBOOK-2026; WCG-7216-2026; HRB-Q4CALL-2026; PWC-MEGNA-2025.
- **Vendors:** TR-COCOUNSEL-2025; TR-R2R-2025; TR-RTR-2026; TR-TRUST7-2026; TR-CHEAP-2026; BASIS-TAX-2026; BASIS-HOME-2026;
  BASIS-SMALL-2026; BASIS-CAREERS-2026 (job posting); BLACKORE-SITE-2026; ACCRUAL-HOME-2026; ACCRUAL-INDIV-2026;
  ACCRUAL-PARTNER-2026; TAXGPT-SITE-2026; WK-AXCESSSCAN-2026; INTUIT-PROCONNECTAI-2026; CANOPY-SMARTINTAKE-2025;
  APARIPRO-2026; OPENAI-CODEX-2026; COLUMN-TCBREPO-2026.
- **Press, podcasts, community:** BLACKORE-2026; ACCTODAY-BLACKORE-2026; MYCPE-BLACKORE-2026; MYCPE-TAXGPT-2026; TAXGPT-2026;
  BASIS-2026; ACCRUAL-LAUNCH-2026; ACCRUAL-ARC-2026; RUNTIMEWIRE-2026; PERPLEXITY-2026; CNBC-HRB-2025; MULTIPLIER-2025;
  CPAPA-POSTEXT-2026; TAXADVISER-CLIENTS-2026; TECHRADAR-TAXFIX-2025; JOFA-POLICY-2026; JOFA-OPR-2026; LDS-CNBC-2026;
  ACCTODAY-AIBENCH-2026; CPATL-WORKFORCE-2026; CPAPA-BLACKORE-2024; CPAPA-TAXGPT-2026; CPAPA-AILIAB-2026;
  BLACKORE-SUMMIT-2026; ACCTPOD-477-2026; ACCTPOD-SAMLEON-2026; BARMORE-OPR-2026; HN-ASK-2026; VERITO-DISCL-2026.
- **Surveys and academic:** AICPA-TAXSW-2026; TR-FOP-2026; WK-FRA-2025; TEI-TAXTECH-2026 (conference recap);
  COLUMN-TAXCALCBENCH-2025; COLUMBIA-TAXBENCH-2026; JHU-TAXREASON-2025; MAGESH-HALLUC-2024; SWIDER-2025.
- **Not in the YAML (opened by the deep-dive researchers):**
  - AICPA-TOPISSUES-2026: Journal of Accountancy, *CPA Firm Top Issues Survey* (629 respondents), 2026-06-23, https://www.journalofaccountancy.com/news/2026/jun/aicpa-top-issues-survey-firms-focus-on-technology-rises/
  - TR-MADSEN-2026: Thomson Reuters Community, *CPA firm automation case study* (SurePrep/UltraTax baseline), 2026-03-17, https://community.thomsonreuters.com/tax-accounting/f/tax-research-guidance/35077/cpa-firm-automation-case-study-how-one-practice-simplified-1040-tax-prep
  - CPATL-SEASON-2026: CPA Trendlines, *Inside Tax Season's Hidden Shift* (teaser only), 2026-04-05, https://cpatrendlines.com/2026/04/05/inside-tax-seasons-hidden-shift-same-work-fewer-people-higher-cost
  - JUNO-SITE-2026: Juno home page (customer quotes), retrieved 2026-10-17, https://www.juno.tax/
  - BASIS-E2E-2026: Basis, *The future of tax is end-to-end intelligence* (undated), https://www.getbasis.ai/blogs/the-future-of-tax-is-end-to-end-intelligence
  - RSM-MYRSM-2025: RSM US, *RSM Expands AI Commitment with Launch of myRSM Tax*, 2025-06-16, https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html
