# Profession-specific duties (step 5)

Read this on entering step 5. It turns the duties on top of general governance into policy. The archetype files in §5
hold the detail and its sources; this is not legal advice (rule 10). Sources are in §8.

## 1. Goal and exit criteria

**Goal.** For each regime flagged in step 1, the duty, the decision it forces, who decides, and the record. Existing
duties continue and the professional stays responsible for the output, as the AICPA ethics article and ABA Opinion
512 say and firms told PCAOB staff [JOFA-2026; ABA-OP512-2024; PCAOB-GENAI-2024].

**Exit when all of these are true:**
- **One subsection per regime** with its decision rule and owner; **consent and disclosure principles** (§5).
- **Screens** (independence, 7216, client terms) in the request path and catalog flags; **open questions** for counsel
  or the professional body written down, not guessed.

## 2. How to run it

1. **Read the matched archetype's `guardrails.md`** (§5); its principles and "checks before a plan goes ahead" are
   the agenda. Work one regime at a time, in the order of exposure named in step 3 (R1), using the §4 triage.
2. **Write the consent and disclosure principles** (§5). Engagement-letter wording stays a draft for counsel.
3. **Add the screens** to the catalog `flags` and the request form (step 7). Record open questions and who answers
   them; then play back and write the outputs (§7).

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| E1 | Are we building, hosting or configuring AI for any attest client, and do clients receive any tool we buy? | [U/O] |
| E2 | Does any AI step touch tax return information, and does it only process data or does it analyse, interpret or apply the law? | [T] |
| E3 | Is the client's consent specific to this use, or boilerplate in the engagement letter? | [T/U] |
| E4 | How is AI-saved time billed, and do engagement letters say how AI is used and charged? | [U/O] |
| E5 | Where are inference and storage done, and does any regime limit processing outside the country? | [U/O] |

## 4. Expert moves

1. **Apply the section 7216 triage in order.** (a) Is it tax return information? (b) Does a listed exception apply?
   (c) Is the recipient only processing data, in the US, without substantive determinations? (d) Otherwise get written
   consent first: signed and dated, naming preparer and taxpayer, purpose, recipient and information; never retroactive;
   one year if no duration is stated; uses and disclosures in separate documents [ECFR-7216-2008, 301.7216-3].
2. **Ask "does the AI step analyse, interpret or apply the law?"** In the regulation's examples, sending return
   information to another firm for advice on a deduction needs prior consent, while pure data processing in the US
   does not [ECFR-7216-2008, 301.7216-2(d)(1), Examples 1 and 4]. Whether an AI provider only processes data or makes
   a substantive determination is unresolved; a 2026 ABA Tax Section panel abstract poses it [WINTHROP-2026]. Ask
   per step, not per tool.
3. **Never make 7216 consent a condition of the engagement.** The regulation treats consent conditioned on service as
   involuntary, except for disclosure to another preparer assisting with the return
   [ECFR-7216-2008, 301.7216-3(a)(1)-(2)].
4. **Run an independence screen on every AI service to, and vendor tie with, an attest client.** Developing or hosting
   an AI system for an attest client can raise independence concerns [JOFA-2026]; IESBA's technology-related
   independence revisions apply to periods beginning on or after 15 December 2024 [IESBA-TECH-2023].
5. **For lawyers, test consent for specificity and ask how AI-saved time is billed.** Opinion 512 requires informed
   consent before client information enters a self-learning tool (boilerplate is not enough) and allows billing only
   time actually spent [ABA-OP512-2024].
6. **Ask where processing happens.** Disclosure of return information to a preparer outside the US needs prior consent
   [ECFR-7216-2008, 301.7216-3(a)(3)(i)(D)]; for Form 1040-series returns, consent to disclose the SSN to a preparer
   outside the US is allowed only with an adequate data protection safeguard [ECFR-7216-2008, 301.7216-3(b)(4)].

## 5. Where the detail is, and decision rules

| Regime | Archetype file and sections | What to take into the policy |
|---|---|---|
| `tax-7216` | `../../transformation-advisor/references/archetypes/tax/guardrails.md` §3, §4, §7, §9, §12 | 7216 triage; OPR Alert 2026-19 practices; fees and disclosure; other jurisdictions (UK PCRT, Australian TPB) |
| `attest-independence` | `../../transformation-advisor/references/archetypes/assurance/guardrails.md` §5, §6, §8, §11 | Documentation central versus file; confidentiality; vendor equity, fee-sharing, referral or control terms as independence items; re-approval when models change |
| `legal-practice` | `../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §1, §3 to §6 | Competence and supervision (oversight scales with autonomy); consent (move 5) and privilege; ethical walls; agents reaching email or files; fees; disclosure; following client restrictions |
| `client-terms` | professional-services guardrails §6 | Client AI terms register; disclosure (consultants inform clients when AI materially contributes); follow restrictions |
| security providers | `../../transformation-advisor/references/archetypes/security/guardrails.md` §7 | Service providers and client data |

**Decision rules**
- **Tax:** write the 7216 decision per workflow, with reasons (tax guardrails §12). OPR Alert 2026-19 asks for secure,
  enterprise-approved AI but does not mention consent; no IRS guidance on AI and 7216 consent was found [IRS-OPR-2026].
- **Assurance:** AI services to or tools hosted for an attest client, and vendor ties with equity, fee-sharing, referral
  or control terms → independence review first (assurance guardrails §8). Firm-built audit tools are `tier-4`.

**Consent and disclosure principles (all regimes)**
- Consent is specific (purpose, recipient, information, risks), never boilerplate, and never a condition of service
  where the rules forbid it [ECFR-7216-2008; ABA-OP512-2024]. Disclosure follows the client's terms and the regime.
- Opinion 512 does not require informed consent when no information relating to the representation goes in, for
  example idea generation [ABA-OP512-2024].

## 6. Worked example

Illustrative. A US tax team wants to summarise prior-year returns and draft position memos. A summary that only
restates figures is treated as processing (US region, masked SSNs), a reading counsel confirms; a position memo applies
law, so it is `tier-4` with preparer review and prior signed consent where the vendor step makes a determination.

## 7. Output

Write section 6 of `overlay/policy.md`; set `flags` on entries in `overlay/tool-catalog.yaml`; add profession lines
to `overlay/guardrails.md`. Set `step_completed: 5`, `next_step: 6`.

## 8. Sources

- **ABA-OP512-2024**: American Bar Association, *Formal Opinion 512: Generative Artificial Intelligence Tools* (professional body, 2024-07-29). https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
- **ECFR-7216-2008**: US Treasury and IRS, *26 CFR 301.7216-1 to -3* (regulation, T.D. 9375 of 2008 as amended). https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-26?part=301&section=301.7216-3
- **IESBA-TECH-2023**: IESBA, *Final Pronouncement: Technology-related Revisions to the Code* (standard-setter, 2023-04-11). https://www.ethicsboard.org/publications/technology-related-revisions-code
- **IRS-OPR-2026**: IRS Office of Professional Responsibility, *Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice* (regulator, 2026-06-24). https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- **JOFA-2026**: Journal of Accountancy, *Accounting ethics in the age of AI* (professional body, 2026-08-05). https://www.journalofaccountancy.com/news/2026/aug/accounting-ethics-in-the-age-of-ai.html
- **PCAOB-GENAI-2024**: PCAOB staff, *Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting* (regulator staff, 2024-07). https://pcaobus.org/documents/generative-ai-spotlight.pdf
- **WINTHROP-2026**: Winthrop & Weinstine, *You May Be a Return Preparer: Using AI Without Violating Sections 7216 and 6713* (practitioner talk abstract, 2026-10-06). https://winthrop.com/bold-perspectives/you-may-be-a-return-preparer-using-ai-without-violating-sections-7216-and-6713/
