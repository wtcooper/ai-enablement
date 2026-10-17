# Tax guardrails

Last researched 2026-10-17. This is the home of professional responsibility for the tax archetype: module files keep
only the guardrails specific to their own steps and link here for the rest. Use it in Frame (constraints), in
Reimagine (fit checks), and in Make the case (risks). It is not legal advice: where a rule's application to AI is
unsettled, say so and suggest the leader takes advice. Source keys in brackets resolve in §13 or in
[sources.md](sources.md).

## Contents

1. [Principles](#1-principles)
2. [Who sets or enforces what](#2-who-sets-or-enforces-what)
3. [Circular 230 and OPR Alert 2026-19](#3-circular-230-and-opr-alert-2026-19)
4. [Client and taxpayer data](#4-client-and-taxpayer-data)
5. [Signing, positions and penalties](#5-signing-positions-and-penalties)
6. [Courts and fabricated authority](#6-courts-and-fabricated-authority)
7. [Other jurisdictions](#7-other-jurisdictions)
8. [Standards and frameworks](#8-standards-and-frameworks)
9. [Fees, disclosure, liability and insurance](#9-fees-disclosure-liability-and-insurance)
10. [In-house departments](#10-in-house-departments)
11. [Steps that need human judgment](#11-steps-that-need-human-judgment)
12. [Checks before a plan goes ahead](#12-checks-before-a-plan-goes-ahead)
13. [Sources](#13-sources)

## 1. Principles

- **Existing duties apply.** Every practitioner regulator found (IRS OPR, the UK PCRT bodies, Australia's TPB, Germany's
  Bundessteuerberaterkammer) applies its existing conduct rules to AI. None has created an AI-specific rule,
  certification or disclosure form [IRS-OPR-2026; PCRT-AI-2026; TPB-GS55-2026; BSTBK-KI-2026].
- **Governance comes first, not after the pilot.** OPR's reading of section 10.36 expects firm procedures, training and
  documentation as AI is introduced, and notes firms use AI "whether they are aware of it or not" [IRS-OPR-2026].
- **The human step must be a control with evidence**, not an intention: "carefully review", "verify and review ...
  throughout each step", documented [IRS-OPR-2026; TPB-GS55-2026]. Werfel names "control dilution": volume rises while
  review capacity does not [TAXADVISER-WERFEL-2026].
- **Embedded AI counts.** OPR names AI inside research platforms; TPB's definition includes tools that "take actions on
  behalf of the user". A tool inventory must include embedded features [IRS-OPR-2026; TPB-GS55-2026].
- **Decide data use per workflow and per tool**: what the tool does (summarise, extract, or make a substantive
  determination), where data goes, and whether it trains on inputs all change the answer (§4).

## 2. Who sets or enforces what

| Body | What it covers | Status for AI |
|---|---|---|
| IRS Office of Professional Responsibility (Treasury) | Circular 230: practice before the IRS | Alert 2026-19 (24 Jun 2026), introductory, does not amend the rules [IRS-OPR-2026] |
| Treasury regulations, IRC sections 7216 and 6713 | Use and disclosure of return information by preparers | No AI-specific guidance found [ECFR-7216-2026] |
| FTC Safeguards Rule (via IRS Publication 4557) | Preparers as financial institutions: written security plan, MFA, oversight of service providers | Predates AI; applies to AI vendors as service providers (advisor inference) [IRS-P4557-2024] |
| US Tax Court | Filings, sanctions, practitioner admission | No AI rule; proposed 2026 rule amendments contain no AI text [TAXCT-ANNOUNCE-2026] |
| AICPA | SSTS (members); CART; independence for PE structures | SSTS 1.4 on reliance on tools; CART launched 23 Sep 2026 [TAXCT-CLINCO-2026; AICPA-CART-2026] |
| UK PCRT bodies (AAT, ACCA, ATT, CIOT, ICAEW, ICAS, STEP); HMRC | Members' conduct; software that interacts with HMRC | PCRT topical guidance 19 Jan 2026; HMRC software guidelines [PCRT-AI-2026; HMRC-GENAI-2026] |
| Tax Practitioners Board (Australia) | Code of Professional Conduct under the Tax Agent Services Act | TPB(GS) 55/2026, 22 Jul 2026 [TPB-GS55-2026] |
| Bundessteuerberaterkammer (Germany) | Steuerberater professional rules | FAQ dated 27 Jan 2026 [BSTBK-KI-2026] |
| EU (AI Act; data protection) | Deployers' literacy duty; high-risk systems; GDPR | Deferral of high-risk duties provisional [GIBSON-AIACT-2026] |
| Professional liability insurers | Underwriting and claims | Asking about AI policies; no substantive claims at accounting firms reported in Apr 2026 [DIGIN-INSURERS-2026] |

State AI laws (California, Colorado, Illinois, Utah) are named by OPR but were not read; no state board of accountancy
guidance was found [IRS-OPR-2026].

## 3. Circular 230 and OPR Alert 2026-19

| Provision | What the alert says it means for AI |
|---|---|
| §10.22 due diligence | Verify facts, citations and calculations produced by AI; do not rely solely on it |
| §10.27(a) fees | Billing manual time not spent, or double billing AI-assisted tasks, may violate the rule "depending on the facts"; credit savings openly and disclose AI activities "in general or specific terms as needed" |
| §10.35 competence | Understand the law and the technology: how the tool works, its limits and risks |
| §10.36 procedures | Firm policies on training, secure data handling, accuracy monitoring and documentation; discipline for principal-authority individuals turns on willfulness, recklessness or gross incompetence |
| §10.37 written advice | Do not rely on AI projections or representations without verification; opaque logic may make reliance unreasonable |
| IRC §§6713, 7216; §10.51(a)(15) | Use secure, enterprise-approved AI; willful mishandling can lead to discipline |

All from [IRS-OPR-2026]. The alert's best practices add vetting third-party tools before purchase and treating output as
drafts; it does not mention consent [IRS-OPR-2026]. Section 10.22(b) presumes due diligence when relying on another
person's work with reasonable care in supervising them; the sources do not say whether an AI tool counts [ECFR-C230-2026].
A commentator argues untraceable output forces a manual verification layer ("paying twice") [CPAPA-OPACITY-2026].

## 4. Client and taxpayer data

- **Section 7216 and 6713.** Knowing or reckless disclosure or misuse of return information by a preparer is a
  misdemeanour (fine up to US$1,000, or one year, or both), and section 6713 imposes US$250 per disclosure, capped at
  US$10,000 a year [LII-USC-7216-6713]. Both refer to chapter 1 income-tax returns; no source settles VAT or sales tax.
- **"Preparer" includes software developers.** The regulations count anyone providing auxiliary services, including a
  person who develops preparation software [ECFR-7216-2026].
- **The consent line.** Disclosure to another US preparer without consent is allowed only where the services "are not
  substantive determinations or advice affecting the tax liability"; a substantive determination is "an analysis,
  interpretation, or application of the law" [ECFR-7216-2026]. Whether an LLM vendor makes such determinations, and
  which consent applies, has no IRS answer [WINTHROP-ABA-2026]. A CPE vendor says consent is the default for AI; that is
  broader than the regulation's exceptions [MYCPE-7216-2026].
- **Consent rules.** Written, knowing, voluntary, signed and dated; cannot be a condition of service; required before
  disclosure to a preparer outside the US, with special rules for SSNs [ECFR-7216-2026; IRS-RP2013-14].
- **Unnamed prompts can still be return information.** A law firm says combined figures can identify a taxpayer even
  without a name (its reading, not the alert's text) [KTS-OPR-2026]. CAMICO says written consent "may be required" for
  certain AI platforms [CAMICO-FAQ-2025].
- **Elsewhere.** PCRT: client data in a public model without consent is "likely" a breach [PCRT-AI-2026]. TPB:
  permission from each client before data goes into third-party AI, depending on configuration; an engagement letter
  can give it [TPB-GS55-2026]. BStBK: confidentiality continues; prefer EU-hosted providers and a processing contract
  [BSTBK-KI-2026].
- **Privilege (adjacent).** A US court held a defendant's chats with a consumer AI tool were not privileged or work
  product (a securities case, not tax) [ORRICK-HEPPNER-2026].

## 5. Signing, positions and penalties

- The signing preparer is the individual with "primary responsibility for the overall substantive accuracy" of the
  return and signs before it goes to the taxpayer; nonsigning preparers who prepare a substantial portion can carry
  exposure too [LII-CFR-SIGN-2026].
- Section 10.34 bars signing a return with a position lacking reasonable basis when done willfully, recklessly or
  through gross incompetence; reliance on client information is allowed but implications cannot be ignored
  [ECFR-C230-2026].
- Preparer penalties: section 6694(a), the greater of US$1,000 or 50% of income from the return; 6694(b), US$5,000 or
  75%; section 6695 penalties for failure to sign and for due-diligence failures on certain credits [LII-USC-PREP-2026].
- **Unresolved:** whether reliance on AI supports reasonable cause or a preparer-penalty defence. No US decision was
  found; a UK tribunal applied the usual reasonable-excuse test and gave the invented cases no weight [FTT-HARBER-2023].
- **Unresolved:** whether an AI agent's drafting is "mechanical assistance" or makes a vendor a preparer [LII-CFR-SIGN-2026].

## 6. Courts and fabricated authority

| Case | What happened | Source |
|---|---|---|
| *Clinco v. Commissioner* (Tax Court, 9 Feb 2026) | Three of four cited cases apparently hallucinated; counsel did not correct the record; admonishment, no sanction; "Tax Court has not done so. Yet." | [CLINCO-OPINION-2026; TAXCT-CLINCO-2026] |
| *Riddle Aggregates* (Tax Court trial, 18 Mar 2026) | IRS withdrew two expert rebuttal reports after AI-related errors were raised; cause disputed | [RIDDLE-TRANSCRIPT-2026] |
| *Khoja* (Tax Court, Mar 2026) | Judge questioned an IRS attorney over a motion citing a nonexistent case (Bloomberg's account; order not read) | [BLAW-TAXCT-2026] |
| *Harber v HMRC* (UK FTT, 4 Dec 2023) | Taxpayer cited nine non-genuine decisions; appeal decided on the merits | [FTT-HARBER-2023] |

- Judge Holmes had seen fewer than a dozen hallucinated cases, issued no sanctions, called section 6673 (up to US$25,000)
  the main existing tool, and doubted an AI certification rule "would make any sense" [BLAW-TAXCT-2026].
- A public database lists 2,199 decisions on hallucinated content across all fields, with tax entries from courts and tribunals in
  the US, UK, Australia and India (a single-person compilation) [CHARLOTIN-DB-2026].
- Outside tax, Deloitte Australia repaid part of a A$440,000 government report fee after fabricated references; OPR
  cites it as an analogy [GUARDIAN-DELOITTE-2025; IRS-OPR-2026].
- **No sanction against a tax practitioner for AI misuse was found.** OPR says such cases are "slowly emerging" [IRS-OPR-2026].

## 7. Other jurisdictions

- **UK (PCRT, 19 Jan 2026).** Members are responsible for work whatever the tool; those unfamiliar with AI may need a
  specialist; integrity includes transparency and being able to explain a conclusion; risk-based review; extra caution
  on planning advice [PCRT-AI-2026]. HMRC expects monitoring, version control and human oversight in generative-AI tax
  software [HMRC-GENAI-2026].
- **Australia (TPB(GS) 55/2026).** Competence, record-keeping, supervision and a documented quality system; verify AI
  content "throughout each step of the workflow"; no new legal obligations beyond the Act [TPB-GS55-2026].
- **Germany (BStBK FAQ).** Decisions and responsibility "remain in human responsibility"; rules are technology-neutral;
  vendors often exclude liability; firms carry the AI Act literacy duty as deployers [BSTBK-KI-2026].
- **EU AI Act.** A provisional deal (May 2026) would defer stand-alone high-risk duties to 2 Dec 2027 and soften the
  literacy duty; formal adoption was not confirmed in the sources [GIBSON-AIACT-2026]. How tax authorities' own systems
  are classified is unclear [HADWICK-EUAIACT].

## 8. Standards and frameworks

- **AICPA SSTS 1.4 (reliance on tools)**, as summarised by the Journal of Accountancy: members may rely on tools but are
  not absolved, must use professional care, and may use AI to improve understanding but not to supplant judgment
  [TAXCT-CLINCO-2026]. SSTS took effect 1 Jan 2024 [AICPA-SSTS-2024].
- **Werfel's risk framework** (The Tax Adviser, Aug 2026 issue): 20 risks for authorities in four categories and 15 for
  preparers in five layers, including hallucinated advice, client data leakage, incorrect document extraction, control
  dilution, liability ambiguity, skill erosion and vendor dependence; phased deployment, for example summarisation
  before position drafting. The author's views, not AICPA policy [TAXADVISER-WERFEL-2026].
- **CART** will test and refine the framework with accounting, law, technology, government and academic members,
  including the National Association of Enrolled Agents and the Federation of Tax Administrators [AICPA-CART-2026].

## 9. Fees, disclosure, liability and insurance

- **Fees.** OPR's section 10.27 reading (§3) is contested: the AICPA says it implies efficiencies must be passed on,
  overlooks AI costs and appears not to allow value pricing; its CEO called it non-authoritative and possibly
  "overstepping"; no IRS clarification was found by 17 Oct 2026 [AICPA-FEES-2026]. Contingent fees remain barred for most
  IRS matters [ECFR-10.27]. Review the pricing model, engagement letter and AI records together.
- **Disclosure.** No universal US duty to disclose AI use in most tax matters is stated in the sources; PCRT asks
  members to consider transparency; TPB requires client permission for third-party AI [TAXCT-CLINCO-2026; PCRT-AI-2026;
  TPB-GS55-2026]. A broker recommends engagement-letter disclosure with an opt-out [DIGIN-INSURERS-2026].
- **Liability.** Werfel lists "liability ambiguity" between the signing preparer and the vendor; BStBK notes vendors
  often exclude liability [TAXADVISER-WERFEL-2026; BSTBK-KI-2026].
- **Insurance.** Aon reported no substantive AI claims at accounting firms (Apr 2026); underwriters ask about AI
  policies; CAMICO distinguishes supervised use (lower exposure) from AI that advises clients autonomously (heightened
  controls) and suggests no-training contract terms [DIGIN-INSURERS-2026; CAMICO-FAQ-2025]. Generative AI exclusions
  reported in other lines were not verified for accounting forms [INS-EXCLUSIONS-2026].

## 10. In-house departments

- No source found says how Circular 230, PCRT or TPB rules apply to employees preparing their employer's return, or how
  officers' signing duties interact with AI.
- No source found covers auditing AI-prepared tax balances; the provision's auditor is the practical reviewer (see
  [provision-pillar-two](modules/provision-pillar-two.md)).
- Ownership is the usual gap: two of more than 50 attendees at TEI's 2026 technology seminar said tax owns AI
  implementation (a reporter's account) [TEI-TAXTECH-2026]. Agree with IT, finance, legal and internal audit who owns
  AI risk for tax data and positions.

## 11. Steps that need human judgment

| Step | Why a person is required | Source |
|---|---|---|
| Signing or approving a return or claim | Signer carries primary responsibility; sections 6694 and 10.34 attach to the practitioner | [LII-CFR-SIGN-2026; ECFR-C230-2026] |
| Positions: reasonable basis, substantial authority, disclosure | Tested against the practitioner's judgment | [ECFR-C230-2026; LII-USC-PREP-2026] |
| Verifying facts, citations and calculations | Section 10.22 due diligence | [IRS-OPR-2026] |
| Written advice and opinions | Reasonable assumptions; opacity can make reliance unreasonable | [IRS-OPR-2026] |
| Deciding what data goes to which tool; obtaining consent | Section 7216's substantive-determination line; TPB permission | [ECFR-7216-2026; TPB-GS55-2026] |
| Form 8867 due-diligence interview | Personal, contemporaneous duty (see compliance-individual-business) | [IRS-I8867-2025] |
| Expert and TP analysis | AI "shouldn't replace" legal, economic and factual judgment; experts explain AI use | [IRS-LBI-TP-2026] |
| Court filings | Model Rule 3.3 and court rules | [CLINCO-OPINION-2026] |
| Billing | Section 10.27 | [IRS-OPR-2026] |
| Scope and phase of deployment | Limited scope first; scale after verification controls pass | [TAXADVISER-WERFEL-2026] |

## 12. Checks before a plan goes ahead

- An approved-tool list that includes embedded AI, with vendor terms on training, retention, location and model change.
- A per-workflow decision on section 7216 or local consent, written down with the reasoning.
- A named reviewer and a review record for each AI-assisted workflow, with an override or correction rate tracked.
- Citation verification for anything that reaches a client, court or authority.
- A pricing and disclosure position for AI-assisted work, read against section 10.27 or the local equivalent.
- Training that covers the tool's limits (section 10.35), and a check that the insurer has been told.

## 13. Sources

Keys not listed here are in [sources.md](sources.md).

- **AICPA-SSTS-2024**: AICPA & CIMA, *Statements on Standards for Tax Services landing page* (professional-body, SSTS effective 1 Jan 2024; page viewed Oct 2026). https://www.aicpa-cima.com/resources/landing/statements-on-standards-for-tax-services
- **CAMICO-FAQ-2025**: CAMICO (CPA professional liability insurer), *Generative AI: Frequently Asked Risk Management Questions on CAMICO's Advisory Hotline* (vendor, 12 Nov 2025). https://www.camico.com/blog/generative-artificial-intelligence-ai-frequently-asked-risk-management-questions-faq-on-camicos-advisory-hotline/
- **CHARLOTIN-DB-2026**: Damien Charlotin, *AI Hallucination Cases Database (web page and CSV)* (academic, 2026-10-16). https://www.damiencharlotin.com/hallucinations/
- **GUARDIAN-DELOITTE-2025**: The Guardian, *Deloitte to pay money back to Albanese government after using AI in $440,000 report* (press, 6 Oct 2025). https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- **HADWICK-EUAIACT**: European Papers, *Slipping Through the Cracks: the Carve-outs for AI Tax Enforcement Systems in the EU AI Act* (academic, undated). https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act
- **IRS-I8867-2025**: Internal Revenue Service, *Instructions for Form 8867: Paid Preparer's Due Diligence Checklist (Rev. November 2025)* (regulator, 2025-11). https://www.irs.gov/pub/irs-pdf/i8867.pdf
- **IRS-P4557-2024**: IRS, *Publication 4557, Safeguarding Taxpayer Data (Rev. 6-2024)* (regulator, Jun 2024). https://www.irs.gov/pub/irs-pdf/p4557.pdf
- **KTS-OPR-2026**: Kilpatrick Townsend (Hughes, Andres), *Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season* (firm, 29 Sep 2026). https://ktslaw.com/blog/kilpatricks-state-and-local-tax-blog/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season
- **LII-USC-7216-6713**: Cornell LII (US Code), *26 USC §§7216, 6713* (regulator, current). https://www.law.cornell.edu/uscode/text/26/7216
- **LII-USC-PREP-2026**: Cornell LII, *26 USC §§6694, 6695* (regulator, current). https://www.law.cornell.edu/uscode/text/26/6694
- **MYCPE-7216-2026**: MYCPE ONE (CPE vendor), *AI Compliance for CPA and Accounting Firms: Client Consent Rules Under IRC §7216, AICPA, and FTC* (vendor, published 6 May 2026; updated 26 Jun 2026). https://my-cpe.com/blogs/using-ai-cpa-accounting-firms-irc-7216-aicpa-ftc-compliance-guide
- **ORRICK-HEPPNER-2026**: Orrick, *Court Rules AI Conversations Are Not Privileged: What United States v. Heppner Means for You* (firm, Mar 2026 (ruling 13 Feb 2026 per Orrick)). https://www.orrick.com/Insights/2026/03/Court-Rules-AI-Conversations-Are-Not-Privileged-What-United-States-v-Heppner-Means-for-You
