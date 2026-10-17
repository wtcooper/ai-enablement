# Synthesis report: tax / research-advisory (wave 2)

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-tax.md` (section 13 leads, no candidates), `tax-research-advisory-practice.md`, `tax-research-advisory-discourse.md`, `tax-research-advisory-governance.md`, plus the "Routed to other modules" sections of every other `tax-*-*.md` file in this folder.
- **Outputs:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/research-advisory.md` (270 lines) and `.../tax/use-cases/research-advisory.yaml` (25 entries). `scripts/validate.py`: 0 errors; one expected warning (A/B share 44%, below the 50% target).

## 1. Counts in and out

| | Count |
|---|---|
| Candidates in: practice / discourse / governance | 18 / 17 / 16 = 51 |
| Routed-in items used (from other tax modules) | 6 (see section 6) |
| Use cases out | 25 |
| Candidates absorbed by merging | 23 (48 candidates map onto 25 entries) |
| Candidates dropped outright | 1 (discourse-10) |
| Candidates kept only as a note in another entry | 2 (governance-11, governance-14) |

## 2. Duplicates merged

| Final id | Built from |
|---|---|
| 01 Cited conversational research assistant | practice-01, discourse-01, governance-01 (+ routed Avalara item) |
| 02 Multi-step research plans for gray-area questions | practice-02, discourse-02 |
| 03 Research agent submits a cited memo-style answer | governance-02 (+ routed OpenAI demo, EY India hub) |
| 04 Multi-jurisdiction research workflow (idea) | governance-16 |
| 05 Knowledge assistant over own memos | discourse-05, knowledge-base part of practice-08 |
| 06 In-house research and question triage | practice-08, discourse-06, governance-10 (+ routed OpenAI Slack Q&A demo) |
| 07 Firm-wide approved tool, named tax AI owner, governance | practice-07, practice-15, discourse-03 |
| 08 Junior research training | practice-13 |
| 09 Planning blueprints | practice-03 |
| 10 Planning ideation and anti-abuse screening (idea) | practice-17, discourse-09, governance-06 |
| 11 AI challenge / second-tool cross-check (idea) | discourse-08, governance-12 |
| 12 LLM translates, deterministic engine calculates | practice-18, governance-07 |
| 13 Document-grounded analysis | practice-06 |
| 14 Drafting memos, letters and client emails | practice-04, discourse-04, discourse-15, governance-04 (governance-11 meeting minutes as a note) |
| 15 Opinions, written advice, in-house preliminary positions (idea) | discourse-07, governance-13, practice-16 |
| 16 Answering during the client call | practice-05 |
| 17 Client-facing assistant with escalation (idea) | governance-09 |
| 18 Triage of client- or opponent-supplied AI material (idea) | discourse-16, governance-15 |
| 19 Citation verification and AI-use record | practice-09, manual part of discourse-11, governance-14 (automatic logging idea as a note) (+ routed WK-CORPRES-2026) |
| 20 Automated citation existence-and-support check | governance-03, checker part of discourse-11 |
| 21 M&A contract review and first-draft diligence report | practice-11, discourse-12, governance-05 |
| 22 Agent-led diligence risk assessment | practice-12, discourse-13 |
| 23 Law-change monitoring with client impact notes | discourse-14, governance-08 |
| 24 Client-specific agents sold as a service | practice-14 |
| 25 Value-based and fixed-fee pricing | practice-10, discourse-17 |

**Dropped:** discourse-10 (statutory and legislative-history synthesis after *Loper Bright*, grade D) rests on one
practitioner article and describes no deployment; it was the weakest idea once the set reached 25.

**Grade and classification decisions to review**
- Entry 03: governance graded A (independent benchmark). Regraded **C**: the measurement is of models in Vals' harness, not an outcome from a named organization's deployment, and no named delegate-level research agent is in production in the sources.
- Entries 01, 02, 09 kept at **A** as the practice angle graded them, although the discourse and governance angles graded the same evidence B. The figures are named firms' own estimates published by vendors. Notes in each entry say so. If the verifier reads "measured outcome" strictly, all three fall to B (A/B share unchanged at 44%).
- Entry 02 placed at **augment**; discourse-02 had Bloomberg Deep Thinking Mode and TR reason-and-act at delegate. Entry 23 placed at **delegate** (discourse) rather than augment (governance).
- Entry 12 kept at **C** (governance) rather than D (practice).
- Source keys unified: KPMG-MA-2025 (= KPMG-MATAX-2025), STANFORD-HALLUC-2024 (= MAGESH-2024), TAXCT-CLINCO-2026 (= JOFA-CLINCO-2026), TEI-TAXTECH-2026 (= TR-TEITAXTECH-2026), BLAW-TAXCT-2026 (= BLOOMBERG-TAXCT-2026), BLUEJ-ENTERPRISE-2026 (= BLUEJ-ENT-2026), DELOITTE-TTT-2026 (= DELOITTE-TTT3-2026), IFA-LISBON-2025 (= IBFD-IFA-2025). PCRT-AI-2026 now means the full ICAEW guidance (governance read it); the ATT news page is not cited. KPMG-DE-2026 dated 2026-05-06 (page metadata) rather than 05-07.

## 3. Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 05, 06, 08, 10, 11, 15, 16, 19 | none | 25 |
| augment | 01, 12, 13, 14, 17, 18, 21 | 02, 04, 07, 09 | none |
| automate | 20 | **none** | none |
| delegate | (n/a) | 03, 22, 23 | 24 |

- **Automate** has one entry, and it is grade C. No source describes a research or advisory flow with no person on the normal path. That fits the guardrails (every regulator requires the practitioner to verify), so it is a real absence, not a search gap.
- **Delegate** has four entries, all grade C: a benchmark, a vendor demo and two announcements. No named organization is shown running one.
- **Model** has two entries (pricing B; agent platforms C), plus Sala's in-house-instead-of-external-opinion question inside entry 15 (idea).

## 4. Grade mix

A 3 (12%), B 8 (32%), C 8 (32%), D 6 (24%). A/B = 44%, below the 50% target. Grades were not raised to reach it. The
module says plainly that this is a thin-evidence module. Every A figure is vendor-published; the only independent
measures are benchmarks of models or adjacent legal-research tools.

## 5. Gaps

- No independent test, error rate, override rate or parallel-run result for any commercial tax research tool (Blue J, CoCounsel, Bloomberg Tax AI, CCH, Big Four assistants).
- No named in-house tax department with a measured research outcome.
- M&A tax diligence: one firm source (KPMG) and one vendor demo (V7); no measurements.
- No enforcement or inspection outcome for AI in tax advice. *Clinco* was an admonishment; *Elden* is a tribunal criticism.
- No authority on reasonable cause or preparer-penalty reliance on AI-generated advice; nothing on professional liability insurance or engagement-letter wording in practice.
- Thin outside the US: UK and Australia appear only through PCRT, TPB, HMRC and tribunal case notes. SALT and trusts-and-estates advisory appear only in passing.
- Practitioner communities (Reddit r/taxpros, TaxProTalk, AccountingWEB, AICPA community) were unreachable. Search budget ran out in the practice and discourse angles before their accuracy-test searches were run.
- Sibling tax modules had no synthesized YAML in `references/archetypes/tax/use-cases/` at the time of writing, so cross-references name modules, not final ids.

## 6. Routed-in items (from other tax modules)

| Item | From | Used |
|---|---|---|
| OpenAI tax department research memo agent and Slack Q&A agent (demo timings) [SJSU-TEIHTTI-2025] | tax-data-technology discourse | Notes in 03 and 06 (not outcomes) |
| Avalara AI tax research, one user quoted at >80% time cut [AVALARA-AGENTIC-2025] | tax-data-technology practice | Note in 01 |
| EY India AI Tax Hub with research agents [EY-INDIA-2026] | indirect-tax practice | Solution in 03 |
| AICPA tax software survey: 65% use AI in tax research [AICPA-TAXSW-2026] | compliance (individual-business, corporate) | Module metrics |
| Wolters Kluwer guidance on documenting AI-assisted research [WK-CORPRES-2026] | compliance-corporate discourse | Entry 19 |
| TP of AI transactions (OECD Chapter VII examples, AstraZeneca) [OECD-INTRAGROUP-2026]; R&D credit for clients' AI projects [CPAPA-RD-2026] | transfer-pricing; compliance-corporate practice | Module frontier, as advice topics |
| Not used: NormBench and TaxPraBen (routed as titles only, no findings); TR-CORPAI-2026, TR-CHEAP-2026, CPAPA-TAXGPT-2026, FLSALESTAX-AI-2026 (no research-specific detail in the routing line); IBA-TAXAI-2025, BTAX-ZERBE-2026, KPMG TP podcasts, TPMINDS-WC-2026 (TP-of-AI advice topics; one representative item used) | various | Pick up in a later pass if the TP-of-AI advisory angle is wanted |

## 7. Routed to other modules (from this module's inputs)

- **controversy:** *Clinco* as litigation conduct, *Khoja* (IRS motion with a nonexistent citation), *Elden*, *Zzaman*, *Harber*, *Bauche*, *Moore*, Tax Court rules and section 6673 [TAXCT-CLINCO-2026; BLAW-TAXCT-2026; ICAS-TAXTRIB-2026; CHARLOTIN-DB-2026]; drafting responses to IRS notices (Blue J Tax Writing) and TEI's "Managing Tax Notices with AI" lab [BLUEJ-WRITING-2026; TEI-MIDYEAR-2026]; tax authorities arriving at audits with data already analysed [TR-TEIAUDITOR-2026]; LLMs identifying abuse from the authority side [JHU-TAXABUSE-2025]; Werfel's tax-authority risk register (Appendix A).
- **transfer-pricing (and controversy):** *Riddle Aggregates* IRS expert report challenged over hallucinated citations and recorded as withdrawn [CHARLOTIN-DB-2026; RIDDLE-TRANSCRIPT-2026]; IRS LB&I remarks on AI and expert witnesses [IRS-LBI-TP-2026]; ABA May Meeting panel "AI and Transfer Pricing Under section 482" [ABA-MAYMTG-2026].
- **compliance:** TR Ready to Review and the CLH CPAs quote [TR-COCOUNSEL-2025]; PwC K-1 mapping agents [PWC-MEGNA-2025]; RSM myRSM Tax [RSM-MYRSM-2025]; EY compliance agents [EY-TAXLABS-2025]; Bloomberg Tax Compliance Tracker AI Assistant [BTAX-TOOLS-2026]; TaxCalcBench [COLUMN-TAXCALCBENCH-2025]; Werfel's document-extraction risk; HMRC's software guidelines for filing products [HMRC-GENAI-2026].
- **provision:** PwC's explainable effective-tax-rate model with locked logic [PWC-MEGNA-2025]; Bloomberg Tax on errors compounding through provision and ETR [BTAX-HALLUC-2026].
- **international-pillar-two:** tax policy of AI (nexus, permanent establishment, value creation) [DCBAR-TAX-2026; ABA-MAYMTG-2026; OXFORD-CBT-2026].
- **indirect-tax:** Fonoa survey details on ten indirect tax workflows [FONOA-2026-SURVEY]; continuous transaction controls [TR-TEIAUDITOR-2026].
- **tax-data-technology:** Oxford Industries and Savant audit-ready automation [SAVANT-OXFORD-2026]; TEI data-pipeline tooling and vibe-coding control gaps [TR-TEIAUDITOR-2026]; OpenAI's automation pipelines [TEI-TAXTECH-2026]; KPMG Germany adoption survey and TR resourcing data [KPMG-DE-2026; TR-CORPTAX-2025].
- **audit (outside tax):** Harris, Hardy & Johnstone using CoCounsel on board minutes, leases and contracts [TR-HHJ-2026].
- **cross-cutting (all tax modules):** OPR Alert 2026-19, PCRT, TPB, Werfel framework and CART, the fee dispute, firm AI policy, shadow AI, the Deloitte Australia report cited by OPR.
- **Landscape correction (from governance):** Werfel's 20-risk, four-category register is the tax-authority register; the preparer register has 15 risks in five categories, and the article is dated 2026-08-31.

## 8. Suggested improvements to the briefs

1. **Define grade A for vendor-published named-firm estimates.** The three angles disagreed on the same evidence (practice A, discourse and governance B). State whether a named firm's before-and-after estimate in a vendor case study is a "measured outcome".
2. **Add a rule for benchmark-only evidence.** An independent benchmark of models (Vals) is not a deployment outcome. Say whether it can support A or B, or only context.
3. **Give angle researchers a shared source-key register** before they start. Eight documents had two keys across angles, and several had different types (PWC-MEGNA-2025: press or firm; KPMG-ANTHROPIC-2026: press or firm; SALA-TAXNOTES-2026: press or academic; TEI-TAXTECH-2026: press or conference) or dates.
4. **Add a worked ladder example for interactive multi-step tools** (an adviser answers clarifying questions, the tool runs a plan). Angles split between augment and delegate.
5. **Require routed items to carry a full source row** (title, URL, date, what it shows). NormBench and TaxPraBen arrived as titles only and could not be used.
6. **Sequence or pre-number sibling syntheses** so cross-references can use final ids.
7. **Ration search across angles** or give each a reserved budget for the accuracy-evidence searches, which ran out in two of three angles here.
