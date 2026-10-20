# Professional-services guardrails

Last researched 2026-10-19. This is the home of professional conduct for the professional-services archetype: module
files keep only the guardrails specific to their own steps (§6 in each) and link here for the rest. Audit
independence and standards are in [assurance](../assurance/guardrails.md); tax practice rules (Circular 230, section
7216) in [tax](../tax/guardrails.md); security reporting duties in [security](../security/guardrails.md). Use this file
in Frame (constraints), Reimagine (fit checks) and Make the case (risks). It is not legal advice: where a rule's
application to AI is unsettled, say so and suggest the leader takes advice. Source keys in brackets resolve in §12 or in
[sources.md](sources.md).

## Contents

1. [Principles](#1-principles)
2. [Who sets or enforces what](#2-who-sets-or-enforces-what)
3. [Competence, verification and supervision](#3-competence-verification-and-supervision)
4. [Confidentiality and privilege](#4-confidentiality-and-privilege)
5. [Fees and billing for AI-assisted work](#5-fees-and-billing-for-ai-assisted-work)
6. [Client AI terms and disclosure](#6-client-ai-terms-and-disclosure)
7. [Courts, sanctions and incidents](#7-courts-sanctions-and-incidents)
8. [Liability and insurance](#8-liability-and-insurance)
9. [People data and employment AI](#9-people-data-and-employment-ai)
10. [Steps that need human judgment](#10-steps-that-need-human-judgment)
11. [Checks before a plan goes ahead](#11-checks-before-a-plan-goes-ahead)
12. [Sources](#12-sources)

## 1. Principles

- **Existing duties apply; none of the texts read bans AI.** Bar opinions in California, Texas, DC, New York City and
  the ABA apply existing rules on competence, confidentiality, supervision, communication and fees to generative AI
  [CALBAR-GENAI-2026; TXETHICS-OP705-2025; DCBAR-OP388-2024; NYCBAR-OP2024-5-2024; ABA-OP512-2024]. Consulting's global
  body took the same line: AI use "does not reduce, transfer or extinguish" accountability [ICMCI-AICODE-2026].
- **Oversight scales with autonomy.** "The greater the level of system autonomy, the greater the lawyer's obligation to
  implement oversight mechanisms" (California, 2026). Agentic systems must not make substantive legal determinations,
  give advice, file or act in a representative capacity without meaningful supervision [CALBAR-GENAI-2026].
- **Leaders are named.** England's Divisional Court expects heads of chambers and managing partners to take "practical
  and effective measures", and says future hearings will ask whether they did [EWHC-AYINDE-2025].
- **A policy protects only if it is operated and evidenced.** In *Johnson v. Dunn* three lawyers were removed and
  referred although the use breached firm policy; the firm itself was not sanctioned, the judge saying it "acted
  reasonably in its efforts to prevent this misconduct" [ABAJ-JOHNSON-2025].
- **Consulting and engineering have fewer binding texts.** Their exposure is mostly commercial and procurement-led
  (refunds, supplier disclosure rules) rather than disciplinary [GUARDIAN-DELOITTE-2025; CP-DELOITTECANADA-2025].

## 2. Who sets or enforces what

| Body | What it covers | Key texts |
|---|---|---|
| US state bars and the ABA | Competence, confidentiality, supervision, fees, candour for lawyers | [CALBAR-GENAI-2026; TXETHICS-OP705-2025; DCBAR-OP388-2024; NYCBAR-OP2024-5-2024; ABA-OP512-2024] |
| UK: SRA, Bar Standards Board, Law Society; courts | Solicitors' and barristers' duties; court expectations on citations | [SRA-WARNING-2026; BSB-AIGUIDANCE-2026; LAWSOC-GENAI-2026; EWHC-AYINDE-2025; CJC-AI-2026] |
| Accounting bodies (ACCA, ICAEW, IESBA, AICPA) | Ethics surveys (61% of ACCA respondents rank AI use their top ethical challenge); fee and independence rules in assurance and tax | [ACCA-ETHICS-2026; AICPA-CODE-2026] |
| Consulting: ICMCI and member institutes | Code mandatory for individual certified consultants; firms expected to align | [ICMCI-AICODE-2026] |
| Engineering: NSPE, ACEC | Responsible charge over AI-assisted sealed work; firm governance guidelines (not a standard of care) | [NSPE-BER24-2; ACEC-AIGUIDE-2024] |
| EU and US states (employment AI) | AI used to hire, allocate work or evaluate staff | [EC-AIACT-2026; COLORADO-SB26189-2026; ILLINOIS-HB3773-2024] |
| Clients and public buyers | Outside-counsel guidelines, procurement clauses, AI-use declarations | [HAQQ-CONFID-2026; CP-DELOITTECANADA-2025; CANBERRATIMES-APSAI-2025] |
| Insurers | Policy wording, exclusions, renewal questions | [OLSHAN-AIEXCL-2026; IAMAG-LAWPL-2026] |

## 3. Competence, verification and supervision

- **Competence has two parts** in California: understanding the system's capabilities, data and limits, and
  independently reviewing, verifying and correcting outputs; it "requires more than" spotting hallucinations, and
  includes reassessment as models change [CALBAR-GENAI-2026]. Texas: lawyers are responsible for work product
  "regardless of who (or what)" drafted it [TXETHICS-OP705-2025].
- **Supervision is a management duty.** Managers should set policies (including for agentic tools), train lawyers and
  staff, and update both as systems become more autonomous [CALBAR-GENAI-2026]. DC extends supervisory duties to
  supervised lawyers' AI use [DCBAR-OP388-2024].
- **Consultants verify too.** ICMCI requires independent verification of facts, calculations, citations and references;
  submitting unreviewed outputs is misconduct comparable to traditional breaches [ICMCI-AICODE-2026].
- **Engineers keep responsible charge.** Using AI drafting tools is not unethical in itself, but sealing work without
  responsible charge over the tool and its output was (NSPE case 24-2, facts may be hypothetical) [NSPE-BER24-2].
- **No document to a court without review.** AI may not file or communicate with a court on its own [CALBAR-GENAI-2026].
- **Checking others' work.** A California appellate court declined to award fees to opposing counsel who had not
  flagged an opponent's fabricated quotations; a commentator reads this as a possible emerging competence standard
  (commentary, not a holding) [LAWSITES-NOLAND-2025].
- **Governance is uneven by firm size.** Law firms requiring training before use: 11% (under 50 lawyers) to 72% (over
  700); requiring human review of work product: 31% to 83% (350-699) [ILTA-TECHSURVEY-2026].

## 4. Confidentiality and privilege

- **Consent before self-learning tools.** ABA 512 requires informed consent before representation information goes into
  a self-learning tool; boilerplate in an engagement letter is not enough [ABA-OP512-2024]. New York City: no
  confidential information into a system without adequate protections absent informed consent; ethical walls apply
  even in closed systems, and the opinion reaches in-house legal departments [NYCBAR-OP2024-5-2024].
- **Agents with access raise "acute" questions.** Agentic systems that reach email, documents, client files or
  calendars must not send client information outside without safeguards and human review [CALBAR-GENAI-2026].
- **Privilege is unsettled.** In *United States v. Heppner* (S.D.N.Y., February 2026) a defendant's own consumer-AI
  chats were held neither privileged nor work product; Orrick notes enterprise platforms with negotiated terms "may
  present a different picture", untested in court [ORRICK-HEPPNER-2026]. Another court protected a self-represented
  litigant's chatbot use as work product [BROWNING-ARMFOR-2026]. No ruling on consultants' or accountants' AI chats
  was found.
- **In-house view.** 56% of respondents to an ACC survey (2024) believed AI tools could compromise privilege
  [LEXPERT-ACC-2024].
- Module detail: ethical walls for AI tools ([acceptance-risk](modules/acceptance-risk.md) `#12`); what AI may see
  ([knowledge-management](modules/knowledge-management.md)).

## 5. Fees and billing for AI-assisted work

- **Hourly: bill time actually spent, not time saved.** California, Texas, DC and the ABA agree; time spent prompting
  and reviewing is billable [CALBAR-GENAI-2026; TXETHICS-OP705-2025; DCBAR-OP388-2024; ABA-OP512-2024].
- **Flat and value fees: positions differ by state.** California allows flat fees that build AI savings into
  competitive rates, with fee agreements explaining how AI factors in [CALBAR-GENAI-2026]. ABA 512 says the same flat fee
  may be unreasonable when AI makes work much faster [ABA-OP512-2024]. Virginia (approved November 2025) says value-based fees can reflect
  AI efficiency gains and stay reasonable, and disagrees with opinions suggesting otherwise [VSB-LEO1901-2025]. Detail: [scoping-pricing](modules/scoping-pricing.md) §6.
- **AI costs.** General AI subscriptions are overhead; matter-specific costs only if disclosed in the fee agreement, at
  actual cost, and with no markup without informed written consent [CALBAR-GENAI-2026]. Texas limits recovery to the
  amount actually incurred [TXETHICS-OP705-2025].
- **Learning time.** ABA 512 says lawyers may not charge clients to learn a tool they will regularly use for clients
  [ABA-OP512-2024; CIVILITY-ABA512-2024].
- **Accounting and tax.** The AICPA bars contingent fees for attest clients and for tax-return preparation
  [AICPA-CODE-2026]; IRS guidance on billing AI-assisted tax work is in the tax archetype [IRS-OPR-2026].
- **Consulting.** No body-issued billing rule for AI-assisted consulting work was found; ICMCI covers disclosure and
  engagement terms, not billing [ICMCI-AICODE-2026].
- **So:** a pricing change is also an engagement-letter change ([economics.md](economics.md) §4).

## 6. Client AI terms and disclosure

- **Disclosure duties are fact-specific for lawyers:** required if the client asks, the agreement requires it, consent
  is needed, the fee is affected, or the output influences a significant decision (ABA 512) [ABA-OP512-2024].
- **Consultants must inform clients** when AI materially contributes to analysis, recommendations or deliverables;
  routine productivity tools need not be disclosed one by one; explicit agreement is expected for personal data and
  high-impact uses [ICMCI-AICODE-2026].
- **Engineers:** no ethical duty to disclose AI use unless the contract requires it, though transparency is favoured
  where AI plays a substantial role [NSPE-BER24-2].
- **Follow the client's restriction.** California and ICMCI both require following client instructions that restrict
  AI [CALBAR-GENAI-2026; ICMCI-AICODE-2026].
- **What clients ask for.** 82% of 468 general counsel in KPMG's survey expect firms to track and share AI use (figure
  seen only in a press summary) [ATL-STATS-2026]. One consultancy's count found 20 of 1,054 published outside-counsel
  guidelines mention AI, 12 requiring disclosure (secondary, via a vendor blog) [HAQQ-CONFID-2026]. Some clients demand
  AI use and savings; others bar AI without permission or will not pay for AI-done work [TRI-LEGALWEEK-2026].
- **Public buyers.** Canada now requires suppliers to identify AI use in advance [CP-DELOITTECANADA-2025]; Australia
  will ask consulting-panel suppliers to declare planned AI use in quotes [CANBERRATIMES-APSAI-2025].
- Module detail: client AI-terms register ([acceptance-risk](modules/acceptance-risk.md) `#11`); disclosure
  ([quality-review](modules/quality-review.md) `#16`).

## 7. Courts, sanctions and incidents

- **Scale.** 2,202 court decisions worldwide on hallucinated content as of 19 October 2026 (1,501 US, 76 UK; 872 with a
  lawyer as the party); a count of decisions, not a rate, and the compiler calls it a work in progress that grows as
  cases are found [CHARLOTIN-DB-2026].
- **Named firms.** K&L Gates and Ellis George: $31,100 jointly (May 2025) [ABAJ-KLGATES-2025]. Butler Snow lawyers
  removed from a case and referred (July 2025) [ABAJ-JOHNSON-2025]. Sullivan & Cromwell apologised to a court in April
  2026, listing about three dozen errors, some of which it said were clerical [ABAJ-SC-2026].
- **UK.** Courts list admonition, costs, strike-out, regulator referral, contempt and police referral; placing false
  material before a court is likely to merit a regulator referral [EWHC-AYINDE-2025]. In *Rodney* both solicitors and their
  firm were referred to the SRA, the court citing "reckless disregard" for accuracy [CCDUDLEY-RODNEY-2026].
- **Consulting and advisory.** Deloitte Australia agreed to repay the final instalment of an AUD 440,000 government
  contract after errors, including non-existent references; the revised report disclosed AI use, and Deloitte did not
  say AI caused the errors [GUARDIAN-DELOITTE-2025].
- **What a good response looks like:** disclose, correct and re-review the wider set; Butler Snow's outside review of
  2,400+ citations in 330 filings found no further errors (self-reported) [EDRM-JOHNSONDUNN-2025]. Steps:
  [quality-review](modules/quality-review.md) `#14`.

## 8. Liability and insurance

- **Policy wording is moving.** ISO generative-AI endorsements for general liability took effect 1 January 2026; some
  carriers are reported to use "absolute" AI exclusions in D&O and E&O lines. A policyholder lawyer warns an insurer may
  argue unverified AI output was never a "professional service" [OLSHAN-AIEXCL-2026].
- **Law-firm market.** A broker says the vast majority of law-firm professional liability policies have no express AI
  exclusion, and expects firms without documented AI protocols to drop out of preferred tiers within 12-18 months
  [IAMAG-LAWPL-2026]. Other brokers report sweeping AI exclusions on some lawyers' E&O policies, with the wording said
  to be spreading to architects [INSINSIDER-LAWYERS-2026].
- **Vendors transfer liability.** Legal AI vendors are reported to place liability on the deploying firm
  [INSINSIDER-LAWYERS-2026]. The Law Society tells solicitors to check liability and insurance cover and to negotiate
  warranties and indemnities with vendors [LAWSOC-GENAI-2026].
- No data on AI-related claims paid or declined was found.

## 9. People data and employment AI

AI used to screen candidates, allocate work, monitor or evaluate staff is a high-risk use under the EU AI Act, with
obligations from 2 December 2027 [EC-AIACT-2026]. Illinois rules apply from 1 January 2026, Colorado developer duties
from 1 January 2027 [ILLINOIS-HB3773-2024; COLORADO-SB26189-2026]. California's bar flags bias risk in AI-assisted
employment actions and in screening clients or candidates [CALBAR-GENAI-2026]. Step-level detail:
[staffing-resourcing](modules/staffing-resourcing.md) §6 and [talent-learning](modules/talent-learning.md) §6.

## 10. Steps that need human judgment

- Accepting a client or matter, clearing conflicts and setting walls.
- The final price, its reasonableness, and what AI cost or saving reaches the client.
- Advice to a client and any recommendation that drives a significant decision.
- Signing, sealing, filing or sending anything to a court, regulator or client.
- Verifying citations, figures and sources before release, and deciding what to disclose.
- Staffing, hiring, evaluation, promotion and pay decisions about people.
- Responding to an AI error: correction, disclosure and re-review.
- Setting what any agent may send, file, book or access without approval.

## 11. Checks before a plan goes ahead

1. Which rules apply to each workflow (bar, institute, code, client terms, employment AI law)? Who has read them?
2. Does the policy cover agents that act (send, file, read email), not only chat tools [CALBAR-GENAI-2026]?
3. For each AI step: who reviews, what they check, and where that is recorded?
4. Which account tier and contract terms apply to client data in each tool [ORRICK-HEPPNER-2026]?
5. Do engagement letters and RFP answers describe AI use, consent and AI cost treatment?
6. Has the broker confirmed cover for AI-assisted work, and are vendor warranties and indemnities negotiated?
7. Is there an incident plan: correct, disclose, re-review?
8. Are training records kept, and is training required before access?

## 12. Sources

Keys not listed here are in [sources.md](sources.md).

- **ABAJ-KLGATES-2025**: ABA Journal, *Sanctions imposed for 'collective debacle' involving AI hallucinations and 2 firms, including K&L Gates* (press, 2025-05-14). https://www.abajournal.com/web/article/judge-imposes-sanctions-for-collective-debacle-involving-ai-hallucinations-and-2-law-firms-including-k
- **ABAJ-SC-2026**: ABA Journal, *Elite Wall Street law firm apologizes for error-laden motion created by AI* (press, 2026-04-22). https://www.abajournal.com/news/article/elite-wall-street-law-firm-apologizes-for-error-laden-motion-created-by-ai
- **BROWNING-ARMFOR-2026**: J. Browning and R. Brescia, US Court of Appeals for the Armed Forces conference, *Lawyers Behaving Badly in the Age of AI (conference slides)* (academic, 2026-03-27). https://www.armfor.uscourts.gov/ConfHandout/2026ConfHandout/PPBrowningBresciaTheEthicalAILawyer7a.pdf
- **EDRM-JOHNSONDUNN-2025**: EDRM (Hon. Ralph Artigliere, ret.), *When AI Policies Fail: The AI Sanctions in Johnson v. Dunn* (community, 2025-07-31). https://edrm.net/2025/07/when-ai-policies-fail-the-ai-sanctions-in-johnson-v-dunn-and-what-they-mean-for-the-profession/
- **IRS-OPR-2026**: Internal Revenue Service, Office of Professional Responsibility, *Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert, Issue 2026-19)* (regulator, 2026-06-24). https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- **LAWSITES-NOLAND-2025**: LawSites (Robert Ambrogi), *A New Wrinkle in AI Hallucination Cases: Lawyers Dinged for Failing to Detect Opponent's Fake Citations* (press, 2025-09-16). https://www.lawnext.com/2025/09/a-new-wrinkle-in-ai-hallucination-cases-lawyers-dinged-for-failing-to-detect-opponents-fake-citations.html
- **LEXPERT-ACC-2024**: Lexpert (reporting an ACC survey), *Survey reveals in-house counsel concerns over AI's risks to legal privilege and data security* (press, 2024-09-25). https://www.lexpert.ca/news/features/survey-reveals-in-house-counsel-concerns-over-ais-risks-to-legal-privilege-and-data-security/388738
- **VSB-LEO1901-2025**: Virginia State Bar, *Legal Ethics Opinion 1901, Reasonable Fees and the Use of Generative Artificial Intelligence* (regulator, 2025-11-25). https://vsb.org/Site/news/rules-news/20250327-prop-1901-fees-ai.aspx
