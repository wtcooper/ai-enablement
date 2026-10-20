# Records of AI use (step 4)

Read this on entering step 4. It decides what to record about AI use, where, for how long and who keeps it, so that a
reviewer, regulator, client or court can later see which tool was used, on what, what was checked and by whom. Source
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

**Goal.** Records that make AI-assisted work reconstructable, in proportion to the tier. The UK FRC asks audit firms
for proportionate documentation of what an AI tool does, how it was developed and tested, and how the firm knows it
works, including for third-party tools; it says the guidance introduces no new requirements [FRC-AI-2025]. Records
also create obligations of their own, because tools store prompts and responses [MSFT-COPILOT-ND].

**Exit when all of these are true:**
- **Central record per tool:** what it is, when it is appropriate, how it was tested, why the firm relies on it,
  known limits.
- **Per-matter record by tier:** what goes on the engagement or matter file for each tier.
- **AI inventory:** where it lives, its fields, who keeps it current, embedded features included.
- **Logs and retention:** what each tool keeps, the retention setting, who can retrieve it, how it is protected.
- **A check:** for the last few AI-assisted deliverables, could the firm show who reviewed what?

## 2. How to run it

1. **Ask the evidence question** (D1). If the answer is "nothing", that is the gap this step closes.
2. **Split central from file** (move 2). Most of the explanation of a tool belongs in one central record; the file
   holds only what is specific to this use.
3. **Set the per-matter record by tier** (§5 default), starting from the three items practitioners recommend:
   prompt, how the output was verified, who reviewed [CPAI-ND].
4. **Design the inventory** (move 4). Use the catalog for approvals and a separate inventory for every AI system
   and feature in use, including embedded ones.
5. **Settle logs and retention** with IT and records owners (move 5). Ask who can retrieve prompts and responses and
   how long they are kept.
6. **Check against the regimes** flagged in step 1 (§5 regime notes).
7. **Play back, write section 5 of the policy, add `retention` to catalog entries.**

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| D1 | For the last five AI-assisted deliverables, what could we show a regulator, client or court about review? | [T/U] |
| D2 | Where do engagement or matter records live today, and who decides what goes on the file? | [U/O] |
| D3 | What do our tools keep (prompts, responses, files), for how long, and who can retrieve it? | [U/O] |
| D4 | Which firm-built or configured tools are used in client work, and is there a record of how each was tested? | [U/O] |
| D5 | Which assurance or quality reviews have looked at AI use, and what did they find? | [U/O] |

## 4. Expert moves

1. **Require three items on the file for substantive AI-assisted work: prompt, how the output was verified, who
   reviewed.** Records design. Reveals whether review happened; the CPAi guide puts it as "If it isn't documented, it
   didn't happen". A practitioner recommendation, not a mandate [CPAI-ND].
2. **Keep the tool explanation central and the use on the file.** Audit and assurance practices. The FRC's guidance,
   as recorded in the assurance archetype, puts what the tool is, when it is appropriate, how it was built and why the
   firm trusts it centrally, and the tool and model version, configuration, prompts or inputs, why use was
   appropriate, approval and how outputs informed conclusions on the audit file; for a language-model tool whose
   outputs are all checked to cited sources it may be appropriate to document less
   (`../../transformation-advisor/references/archetypes/assurance/guardrails.md` §5) [FRC-AIAUDIT-2025].
3. **For third-party tools, document why you can rely on them where the vendor withholds detail.** Vendor tools in
   regulated work. Reveals the minimum record regulators are signalling [FRC-AI-2025; KN-2025].
4. **Build an inventory with NIST's fields.** Organization scope. NIST lists data provenance, known issues,
   human-oversight roles, IP and sensitive-data considerations, and underlying models and versions as inventory
   fields, and suggests policies define exemptions for embedded generative AI [NIST-600-1-2024, GV-1.6-001 to
   GV-1.6-003].
5. **Ask for retention controls and who holds the activity history.** Before approval. Reveals whether records are
   retrievable for audit: one provider says workspace admins control retention and deleted conversations are removed
   within 30 days unless legally required to retain [OPENAI-ENT-ND]; another says prompts and responses are stored as
   activity history that admins can manage [MSFT-COPILOT-ND].
6. **Design tools to document their source data.** Firm-built tools. PCAOB staff reported some firms design tools to
   document the underlying source data [PCAOB-GENAI-2024, p.5].

## 5. Checklists and decision rules

**Per-matter record by tier (advisor default; adjust with the user):**

| Tier | On the file | Central |
|---|---|---|
| `tier-1` | Nothing beyond tool logs | Catalog entry |
| `tier-2` | Tool used and what was checked, where the work feeds client work | Catalog entry |
| `tier-3` | Prompt or input description, how the output was verified, who reviewed [CPAI-ND] | Catalog entry and vendor evaluation |
| `tier-4` | Tier 3, plus tool and model version, configuration, why use was appropriate, approval, how output informed the conclusion [FRC-AIAUDIT-2025] | Approval record: purpose, appropriate use, development and testing, how the firm knows it works [FRC-AI-2025] |

**AI inventory fields:** tool; vendor; tier and contract; underlying model and version; runtime class; data classes
permitted; data provenance; known issues; human-oversight roles; IP and sensitive-data considerations; retention and
log location; owner; risk tier; consent, 7216 and independence flags; EU high-risk screen; exit plan
[NIST-600-1-2024, GV-1.6-003, with advisor additions].

**Regime notes**
- **EU high-risk uses:** deployers keep automatically generated logs under their control for at least six months
  [AIACT-EXPL-2026, Art 26(6)].
- **Tax:** OPR Alert 2026-19 reads Circular 230 §10.36 as expecting firm procedures on training, secure data handling,
  accuracy monitoring and documentation (`../../transformation-advisor/references/archetypes/tax/guardrails.md` §3)
  [IRS-OPR-2026].
- **Legal:** a policy protects only if it is operated and evidenced; in *Johnson v. Dunn* the firm was not sanctioned,
  the judge finding it acted reasonably to prevent the misconduct
  (`../../transformation-advisor/references/archetypes/professional-services/guardrails.md` §1) [ABAJ-JOHNSON-2025].
- **Privilege:** a US court held a defendant's consumer-AI chats neither privileged nor work product; how enterprise
  tiers fare is untested (professional-services guardrails §4) [ORRICK-HEPPNER-2026].

**Decision rules**
- Records scale with the tier; never ask for more on the file than the tier needs [FRC-AI-2025].
- Logs of prompts and responses are client data when the inputs were: give them the input's data class and retention.
- A tool change that alters the model or configuration is noted in the central record before the next tier-4 use.

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Over-documenting | The FRC seeks proportionate documentation and warns against over-documentation [FRC-AI-2025] | Scale to tier; keep the tool explanation central |
| Records nobody can retrieve | Prompts and responses sit in vendor activity history [MSFT-COPILOT-ND] | Confirm admin retrieval and retention before approval |
| Keeping logs forever | Logs hold client data | Set retention to the matter's records policy; secure the logs |
| Usage tracking read as surveillance | KPMG says it tracks staff AI use and that monitoring is not intended as discipline (secondary) [IAB-KPMG-2025] | Say what records are for (reconstruction, quality) and what they are not |

## 7. Worked example

Illustrative, not a case study. A law firm's litigation group uses a research assistant and a drafting skill. The
general counsel asks what the firm could show a court if a citation were challenged.

- **D1:** for the last five briefs, nothing shows who checked citations.
- **Tier-3 file record:** a short AI-use note in the matter file: which approved entry, what it was asked (described,
  not pasted), "all citations checked at source by" (role), date.
- **Central:** catalog entry and vendor evaluation; the drafting skill has an owner and a version history.
- **Logs:** the business-tier assistant keeps history under admin-set retention matched to the matter records policy;
  IT can retrieve it on a records request.
- **Privilege:** the firm notes the consumer-AI ruling and keeps client work in the business tier only.

## 8. Output

Write section 5 of `overlay/policy.md`. Add `retention` (and `underlying_model` where known) to entries in
`overlay/tool-catalog.yaml`. Set `step_completed: 4`, `next_step: 5`.

## 9. Sources

- **ABAJ-JOHNSON-2025**: ABA Journal, *5 hallucinated cases lead federal judge to kick 3 Butler Snow lawyers off case* (press, 2025-07-30). https://www.abajournal.com/news/article/5-fabricated-cases-lead-federal-judge-to-kick-3-butler-snow-lawyers-off-case
- **AIACT-EXPL-2026**: Future of Life Institute, *EU AI Act Explorer: Article 26* (annotated regulation, accessed 2026-10-20). https://artificialintelligenceact.eu/article/26/
- **CPAI-ND**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, undated). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **FRC-AI-2025**: Financial Reporting Council, *FRC publishes landmark guidance providing clarity to audit profession on the uses of AI* (regulator news release, 2025-06-26). https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/
- **FRC-AIAUDIT-2025**: Financial Reporting Council, *AI in audit: illustrative example and documentation guidance* (regulator, 2025-06). https://media.frc.org.uk/documents/AI_in_Audit.pdf
- **IAB-KPMG-2025**: International Accounting Bulletin, *KPMG to include AI performance reviews* (trade press, secondary, 2025-11-03). https://www.internationalaccountingbulletin.com/?p=44130
- **IRS-OPR-2026**: IRS Office of Professional Responsibility, *Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice* (regulator, 2026-06-24). https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- **KN-2025**: Kingsley Napley LLP, *Tech-driven, ethically bound: new FRC and ICAEW guidance on AI use in the accountancy sector* (law-firm commentary, 2025-07-24). https://www.kingsleynapley.co.uk/our-insights/articles/tech-driven-ethically-bound-new-frc-and-icaew-guidance-on-ai-use-in-the-accountancy-sector/
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/
- **ORRICK-HEPPNER-2026**: Orrick, *Court Rules AI Conversations Are Not Privileged: What United States v. Heppner Means for You* (law-firm alert, 2026-03-25). https://www.orrick.com/Insights/2026/03/Court-Rules-AI-Conversations-Are-Not-Privileged-What-United-States-v-Heppner-Means-for-You
- **PCAOB-GENAI-2024**: PCAOB staff, *Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting* (regulator staff, 2024-07). https://pcaobus.org/documents/generative-ai-spotlight.pdf

Vendor documentation is cited only as evidence of what published terms say; nothing here recommends a vendor.
