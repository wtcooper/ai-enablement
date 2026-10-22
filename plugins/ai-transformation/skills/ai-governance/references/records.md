# Records of AI use (step 4)

Read this on entering step 4. It decides what to record about AI use, where, for how long and who keeps it, so that
a reviewer, regulator, client or court can see which tool was used, on what, what was checked and by whom (§8 sources).

## 1. Goal and exit criteria

**Goal.** Records that make AI-assisted work reconstructable, in proportion to the tier. The UK FRC asks audit firms
for proportionate documentation of what an AI tool does, how it was developed and tested, and how the firm knows it
works, including for third-party tools, and says this introduces no new requirements [FRC-AI-2025; FRC-AIAUDIT-2025].

**Exit when all of these are true:**
- **Central record per tool** (what it is, when appropriate, how tested, why relied on, limits) and **a per-matter
  record by tier** (what goes on the engagement or matter file).
- **AI inventory:** where it lives, its fields, who keeps it current, embedded features included.
- **Logs and retention:** what each tool keeps, the retention setting, who can retrieve it, how it is protected.
- **A check:** for the last few AI-assisted deliverables, could the firm show who reviewed what?

## 2. How to run it

1. **Ask the evidence question** (D1). If the answer is "nothing", that is the gap this step closes.
2. **Split central from file** (move 2), then **set the per-matter record by tier** (§5), starting from move 1.
3. **Design the inventory** (§5): the catalog holds approvals; the inventory lists every AI system and feature in use.
4. **Settle logs and retention** with IT and records owners (move 3); check against the regimes flagged in step 1.
5. **Play back and write the outputs** (§7).

## 3. Question bank

| # | Question | Scope |
|---|---|---|
| D1 | For the last five AI-assisted deliverables, what could we show a regulator, client or court about review? | [T/U] |
| D2 | Where do engagement or matter records live today, and who decides what goes on the file? | [U/O] |
| D3 | What do our tools keep (prompts, responses, files), for how long, and who can retrieve it? | [U/O] |
| D4 | Which firm-built or configured tools are used in client work, and is there a record of how each was tested? | [U/O] |

## 4. Expert moves

1. **Three items on the file for substantive AI-assisted work: prompt, how the output was verified, who reviewed.** The
   CPAi guide puts it as "If it isn't documented, it didn't happen"; a practitioner recommendation, not a mandate
   [CPAI-2026].
2. **Keep the tool explanation central and the use on the file**, as the FRC's guidance does (§5 tier-4 row;
   `../../transformation-advisor/references/archetypes/assurance/guardrails.md` §5). Where a vendor withholds detail,
   the FRC suggests the firm may rely on independent assurance [FRC-AIAUDIT-2025].
3. **Confirm who holds the activity history and who sets retention, before approval.** One provider says admins
   control retention and deleted conversations are removed within 30 days unless law requires longer or it is needed to
   protect its services [OPENAI-ENT-ND]; another keeps prompts and responses as admin-managed history [MSFT-COPILOT-ND].

## 5. Defaults and decision rules

**Per-matter record by tier (advisor default; adjust with the user):**

| Tier | On the file | Central |
|---|---|---|
| `tier-1` | Nothing beyond tool logs | Catalog entry |
| `tier-2` | Tool used and what was checked, where the work feeds client work | Catalog entry |
| `tier-3` | Prompt or input description, how the output was verified, who reviewed [CPAI-2026] | Catalog entry and vendor evaluation |
| `tier-4` | Tier 3, plus tool and model version, configuration, why use was appropriate, approval, how output informed the conclusion [FRC-AIAUDIT-2025] | Approval record: purpose, appropriate use, development and testing, how the firm knows it works [FRC-AIAUDIT-2025] |

**AI inventory fields:** tool; vendor; tier and contract; model and version; runtime class; data classes; data
provenance; known issues; oversight roles; IP and sensitive-data notes; retention and log location; owner; risk tier;
regime flags; exit plan [NIST-600-1-2024, GV-1.6-003, with advisor additions].

**Regime notes** (archetype files are under `../../transformation-advisor/references/archetypes/`)
- **EU high-risk uses:** deployers keep automatically generated logs under their control for at least six months
  [AIACT-EXPL-2026, Art 26(6)].
- **Tax:** OPR Alert 2026-19 reads Circular 230 §10.36 as expecting firm procedures on training, secure data handling,
  accuracy monitoring and documentation (tax guardrails §3) [IRS-OPR-2026].
- **Legal:** a policy protects only if operated and evidenced; in *Johnson v. Dunn* the firm was not sanctioned, the
  judge finding it acted reasonably to prevent misconduct (professional-services guardrails §1) [ABAJ-JOHNSON-2025].
- **Privilege:** a US court held a defendant's consumer-AI chats neither privileged nor work product; how enterprise
  tiers fare is untested (professional-services guardrails §4) [ORRICK-HEPPNER-2026].

**Decision rules**
- Records scale with the tier; the FRC warns against over-documentation [FRC-AI-2025].
- Logs of prompts and responses are client data when the inputs were: give them the input's data class and retention.
- A change to a tool's model or configuration is noted in the central record before the next tier-4 use.
- Records say what they are for (reconstruction, quality) and never rate individuals (core rule 1).

## 6. Worked example

Illustrative. A law firm finds nothing shows who checked citations in its last five briefs. Tier-3 file record: which
approved entry, what it was asked (described, not pasted), "all citations checked at source by" (role), date.

## 7. Output

Write section 5 of `overlay/policy.md`. Add `retention` (and `underlying_model` where known) to entries in
`overlay/tool-catalog.yaml`. Set `step_completed: 4`, `next_step: 5`.

## 8. Sources

- **ABAJ-JOHNSON-2025**: ABA Journal, *5 hallucinated cases lead federal judge to kick 3 Butler Snow lawyers off case* (press, 2025-07-30). https://www.abajournal.com/news/article/5-fabricated-cases-lead-federal-judge-to-kick-3-butler-snow-lawyers-off-case
- **AIACT-EXPL-2026**: Future of Life Institute, *EU AI Act Explorer: Article 26* (annotated regulation, accessed 2026-10-20). https://artificialintelligenceact.eu/article/26/
- **CPAI-2026**: CPAi, *Drafting an AI Policy that Actually Works* (professional association guide, 2026-07). https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works
- **FRC-AI-2025**: Financial Reporting Council, *FRC publishes landmark guidance providing clarity to audit profession on the uses of AI* (regulator news release, 2025-06-26). https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/
- **FRC-AIAUDIT-2025**: Financial Reporting Council, *AI in audit: illustrative example and documentation guidance* (regulator, 2025-06). https://media.frc.org.uk/documents/AI_in_Audit.pdf
- **IRS-OPR-2026**: IRS Office of Professional Responsibility, *Alert 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice* (regulator, 2026-06-24). https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
- **MSFT-COPILOT-ND**: Microsoft, *Microsoft 365 Copilot privacy and data protection* (vendor documentation, undated, read 2026-10-20). https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- **NIST-600-1-2024**: NIST, *AI RMF: Generative AI Profile, NIST AI 600-1* (standard, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **OPENAI-ENT-ND**: OpenAI, *Enterprise privacy* (vendor documentation, undated, read 2026-10-20). https://openai.com/enterprise-privacy/
- **ORRICK-HEPPNER-2026**: Orrick, *Court Rules AI Conversations Are Not Privileged: What United States v. Heppner Means for You* (law-firm alert, 2026-03-25). https://www.orrick.com/Insights/2026/03/Court-Rules-AI-Conversations-Are-Not-Privileged-What-United-States-v-Heppner-Means-for-You
