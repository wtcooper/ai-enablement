# Profession-specific duties (step 5)

Read this on entering step 5. It applies the duties that sit on top of general governance: confidentiality,
independence when buying or using AI tools, consent for tax-return information, documentation expectations in audit,
and bar guidance for lawyers. The archetypes hold the full detail; this file says how to turn it into policy. It is
not legal advice: where a rule's application to AI is unsettled, say so and suggest the leader takes advice. Source
keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Expert moves](#4-expert-moves)
5. [Checklists and decision rules](#5-checklists-and-decision-rules)
6. [Common traps](#6-common-traps)
7. [Worked example](#7-worked-example)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** For each regime flagged in step 1, a written rule: the duty, the decision it forces, who decides, and what
is recorded. Existing duties continue to apply and the professional stays responsible for the output [JOFA-2026;
IESBA-TECH-2023; ABA-OP512-2024; PCAOB-GENAI-2024].

**Exit when all of these are true:**
- **One subsection per regime** in the policy, each with the decision rule and its owner.
- **Client disclosure and consent principles,** including what consent must say and when it may not be required.
- **Screens** (independence, section 7216, client terms) added to the request path and catalog flags.
- **Open questions** that need counsel or the professional body, written down rather than guessed.

## 2. How to run it

1. **Read the matched archetype's `guardrails.md`** for each regime in play (§5 pointers). Use its principles and
   "checks before a plan goes ahead" as the agenda.
2. **Work one regime at a time**, in the order of exposure the user named in step 3 (R1).
3. **Turn each duty into a decision rule** with an owner. Use the triage orders in §5 for tax and independence.
4. **Write the consent and disclosure principles** (§5). Do not draft engagement-letter wording as final text;
   mark it a draft for the firm's counsel.
5. **Add the screens** to the catalog `flags` and to the request form (step 7).
6. **Record open questions** with who will answer them.
7. **Play back, write section 6 of the policy, and add profession lines to the guardrails.**

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| E1 | Are we building, hosting or configuring AI for any attest client, and do clients receive any tool we buy? | [U/O] |
| E2 | Does any AI step touch tax return information, and does it only process data or does it analyse, interpret or apply the law? | [T] |
| E3 | Is the client's consent specific to this use, or boilerplate in the engagement letter? | [T/U] |
| E4 | How is AI-saved time billed, and do engagement letters say how AI is used and charged? | [U/O] |
| E5 | Where are inference and storage done, and does any regime limit processing outside the country? | [U/O] |

## 4. Expert moves

1. **Apply the section 7216 triage in order.** Tax practice. (a) Is it tax return information? (b) Does a listed
   exception apply? (c) Is the recipient only processing data, in the US, without substantive determinations? (d)
   Otherwise obtain written consent first. Consent must be written, signed and dated, name preparer and taxpayer,
   state purpose and recipient, specify the information, cannot be retroactive, defaults to one year if no duration
   is stated, and uses and disclosures need separate documents [ECFR-7216-2008, 301.7216-3].
2. **Ask "does the AI step analyse, interpret or apply the law?"** Tax and legal AI use. In the regulation's example,
   sending return information to another firm for advice on a deduction needs prior consent, while pure data
   processing in the US does not [ECFR-7216-2008, 301.7216-2(d)(1), Example 4]. Whether an AI vendor counts as a
   preparer or auxiliary-service provider is unresolved; a 2026 ABA Tax Section panel abstract poses that question
   [WINTHROP-2026].
3. **Never make 7216 consent a condition of the engagement.** Tax engagement letters. The regulation treats consent
   conditioned on service as involuntary, with an exception for disclosure to another preparer assisting with the
   return [ECFR-7216-2008, 301.7216-3(a)(1)-(2)].
4. **Run an independence screen on every AI service to, and vendor tie with, an attest client.** Audit and attest
   firms. The AICPA ethics article says AI-related nonattest services such as developing or hosting an AI system for
   an attest client can raise independence concerns [JOFA-2026]; IESBA's technology revisions, effective
   15 December 2024, address technology-related non-assurance services to audit clients [IESBA-TECH-2023].
5. **For lawyers, test consent for specificity.** Legal AI use with client information. ABA Opinion 512 requires
   informed consent before representation information goes into a self-learning tool, and boilerplate in an
   engagement letter is not enough [ABA-OP512-2024].
6. **Ask how AI-saved time is billed.** Hourly work. ABA Opinion 512 allows billing only time actually spent
   [ABA-OP512-2024]; tax and other fee positions are in the archetype guardrails.
7. **Ask where processing happens.** Tax, EU or client-residency limits. Under the tax regulations, disclosure to a
   preparer outside the US needs prior consent and taxpayer SSNs cannot be disclosed offshore under consent
   [ECFR-7216-2008, 301.7216-3(b)(4)].

## 5. Checklists and decision rules

**Where the detail is (read the matched file before writing the subsection):**

| Regime | Archetype file and sections | What to take into the policy |
|---|---|---|
| `tax-7216` | `../../transformation-advisor/references/archetypes/tax/guardrails.md` §3, §4, §9, §12 | 7216 triage; OPR Alert 2026-19 practices (secure, enterprise-approved tools; vet before purchase; output as drafts); fees and disclosure; other jurisdictions |
| `attest-independence` | `../../transformation-advisor/references/archetypes/assurance/guardrails.md` §5, §6, §8, §11 | Documentation central versus file; confidentiality; vendor equity, fee-sharing, referral or control terms as independence items |
| `legal-practice` | `../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §3, §4, §5, §6 | Competence and supervision; consent and privilege; fees; disclosure; following client restrictions |
| `client-terms` | professional-services guardrails §6 | Client AI terms register; disclosure; follow restrictions |
| security providers | `../../transformation-advisor/references/archetypes/security/guardrails.md` §7 | Service providers and client data |

**Tax decision rules**
- Write the 7216 decision per workflow, with the reasoning (tax guardrails §12).
- OPR Alert 2026-19 asks practitioners to use secure, enterprise-approved AI and to vet third-party tools before
  purchase; it does not mention consent, and no IRS guidance on AI and 7216 consent was found (tax guardrails §3)
  [IRS-OPR-2026]. Treat the vendor-as-preparer question as open and route it to counsel [WINTHROP-2026].
- Outside the US, PCRT says client data in a public model without consent is likely a breach, and TPB asks for
  client permission before data goes into third-party AI depending on configuration (tax guardrails §4)
  [PCRT-AI-2026; TPB-GS55-2026].

**Assurance decision rules**
- Any AI service to an attest client, any tool the firm hosts for one, and any vendor relationship with equity,
  fee-sharing, referral or control terms → independence review before commitment (assurance guardrails §8)
  [JOFA-2026; JOFA-SOCETH-2026].
- Re-approve tools when they or their models change (assurance guardrails §5) [IFIAR-TTF-2026].
- Firm-built tools used in audit work: documentation per step 4, tier-4 [FRC-AI-2025].

**Legal decision rules**
- No client information in a self-learning tool without informed consent that explains the risks
  [ABA-OP512-2024]. Ethical walls apply to AI tools too [NYCBAR-OP2024-5-2024].
- Oversight scales with autonomy; agents that reach email, files or calendars need safeguards and human review
  before client information leaves (professional-services guardrails §1, §4) [CALBAR-GENAI-2026].
- UK solicitors: carry out supplier due diligence and review terms; the Law Society notes warranties are often
  limited [LAWSOC-GENAI-2026].

**Consent and disclosure principles (all regimes)**
- Consent is specific: purpose, recipient, information, risks; never boilerplate; never a condition of service where
  the rules forbid it [ECFR-7216-2008; ABA-OP512-2024].
- Opinion 512, as summarised, says consent is not needed when no client-related information goes into the tool
  [ABA-512-2024].
- Disclosure follows the client's terms and the regime; consultants inform clients when AI materially contributes
  (professional-services guardrails §6) [ICMCI-AICODE-2026].

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Blanket boilerplate consent | Opinion 512: boilerplate not sufficient [ABA-OP512-2024]; 7216 consent must be specific, signed, dated and prior [ECFR-7216-2008] | Consent per purpose and recipient, explaining risks |
| Treating AI services to attest clients as "just technology" | [JOFA-2026; IESBA-TECH-2023] | Independence screen on the request form |
| Assuming a summary is never a substantive determination | The line is analysis, interpretation or application of law [ECFR-7216-2008] | Ask E2 per step, not per tool |
| Guessing an unsettled rule | Several questions are open (vendor as preparer; enterprise-tier privilege) | Write the question down; route it to counsel |
| Quoting stale EU dates | Dates moved in 2026 [EU-OMNIBUS-2026] | Quote Regulation (EU) 2026/1744 and re-verify |

## 7. Worked example

Illustrative, not a case study. A US tax practice proposes a shared team skill in its business-tier assistant to
summarise prior-year returns and draft position memos.

- **Triage (move 1):** inputs are tax return information. Summarising a return is processing; drafting a position
  memo applies law [ECFR-7216-2008, 301.7216-2(d)(1), Example 4].
- **Location (move 7):** the entry's processing region is confirmed as US; SSNs are masked before input.
- **Decision:** approve summarisation in the business-tier entry for `regulated` data with US processing and masked
  SSNs; route position drafting to `tier-4` with preparer review, and obtain prior signed consent where the vendor
  step involves a substantive determination. Record prompt, verification and reviewer on the file [CPAI-ND].
- **Open question:** whether the vendor is a covered preparer goes to counsel [WINTHROP-2026].
- **Fees:** the engagement letter and pricing are reviewed against the fee positions in the tax guardrails §9.

## 8. Output

Write section 6 of `overlay/policy.md`. Set `flags` on catalog entries in `overlay/tool-catalog.yaml`. Add profession
lines to `overlay/guardrails.md`. Set `step_completed: 5`, `next_step: 6`.

## 9. Sources

Keys marked † are also cited in the archetype `guardrails.md` files named in §5, where the full context sits.

- **ABA-OP512-2024** †: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **ABA-512-2024**: Ezel, *ABA Formal Opinion 512, Generative AI Tools (summary)* (secondary summary of a professional-body opinion, 2024-07-29). https://ezel.ai/ethics-opinions/aba/512-generative-ai-tools
- **CALBAR-GENAI-2026** †: State Bar of California, *Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)* (regulator, 2026-05-14). https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
- **CPAI-ND**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, undated). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **EU-OMNIBUS-2026**: European Parliament and Council, *Regulation (EU) 2026/1744 amending Regulation (EU) 2024/1689* (regulation, 2026-07-08). https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
- **FRC-AI-2025**: Financial Reporting Council, *FRC publishes landmark guidance providing clarity to audit profession on the uses of AI* (regulator news release, 2025-06-26). https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/
- **ICMCI-AICODE-2026** †: ICMCI, *Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0* (professional body, 2026-05). https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
- **IESBA-TECH-2023**: IESBA, *Final Pronouncement: Technology-related Revisions to the Code* (standard-setter, 2023-04-11). https://www.ethicsboard.org/publications/technology-related-revisions-code
- **IFIAR-TTF-2026** †: IFIAR, *Use of technology in audits: Innovation and audit quality 2026* (regulator forum, 2026-04-20). https://www.fsa.go.jp/ifiar/2026TTFReport.pdf
- **IRS-OPR-2026** †: IRS Office of Professional Responsibility, *Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice* (regulator, 2026-06-24). https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- **JOFA-2026**: Journal of Accountancy, *Accounting ethics in the age of AI* (professional body, 2026-08-05). https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai.html
- **JOFA-SOCETH-2026** †: Journal of Accountancy, *SOC engagements: ethics risks with tool providers* (professional body, 2026-04-06). https://www.journalofaccountancy.com/news/2026/apr/soc-engagements-ethics-risks-with-tool-providers/
- **LAWSOC-GENAI-2026**: Law Society of England and Wales, *Generative AI: the essentials* (professional body, 2026). https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
- **NYCBAR-OP2024-5-2024** †: New York City Bar Association, *Formal Opinion 2024-5* (professional body, 2024-08-07). https://www.nycbar.org/wp-content/uploads/2024/08/20221329_GenerativeAILawPractice.pdf
- **PCAOB-GENAI-2024**: PCAOB staff, *Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting* (regulator staff, 2024-07). https://pcaobus.org/documents/generative-ai-spotlight.pdf
- **PCRT-AI-2026** †: ICAEW for the seven PCRT bodies, *Topical guidance covering the application of PCRT to the ethical use of AI tools* (professional body, 2026-01-19). https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools
- **TPB-GS55-2026** †: Tax Practitioners Board, *TPB(GS) 55/2026 The use of AI and the Code of Professional Conduct* (regulator, 2026-07-22). https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
- **WINTHROP-2026**: Winthrop & Weinstine, *You May Be a Return Preparer: Using AI Without Violating Sections 7216 and 6713* (practitioner talk abstract, 2026-10-06). https://winthrop.com/bold-perspectives/you-may-be-a-return-preparer-using-ai-without-violating-sections-7216-and-6713/
