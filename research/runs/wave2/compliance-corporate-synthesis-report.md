# Synthesis report: tax / compliance-corporate

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-tax.md`, `tax-compliance-corporate-practice.md`, `tax-compliance-corporate-discourse.md`, `tax-compliance-corporate-governance.md`, plus the "Routed to other modules" sections of every other `tax-*-*.md` file in wave 2.
- **Outputs:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/compliance-corporate.md` (261 lines) and `.../tax/use-cases/compliance-corporate.yaml` (24 entries). `scripts/validate.py`: 0 errors; one expected warning (A/B share below 50%).

## Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 16 (B 3, C 12, D 1) | 16 (B 4, C 8, D 4) | 16 (C 6, D 10) | 48 |
| Out | | | | 24 (B 4, C 16, D 4) |

One candidate was routed out rather than kept: discourse-02 (AI reads tax-authority notices and drafts responses), because the practice angle and tax-data-technology both route notices to controversy.

## Duplicates merged

| Final id | Merged from |
|---|---|
| -01 data import and mapping | practice-01, governance-01 |
| -02 K-1 agents (PwC) | practice-02, discourse-01 |
| -03 year-on-year anomaly flags | practice-03, discourse-09 |
| -07 OpenAI agent-driven computation | discourse-03, practice-09 |
| -08 firm agent platforms | practice-06, discourse-16 |
| -09 R&D credit and Section G | practice-07, discourse-05, governance-02 |
| -10 governed reconciliation (Savant/Oxford) and write-back | practice-08, discourse-04, governance-11 |
| -11 grounded research in compliance tools | practice-10, governance-05 |
| -12 calendar and rule-change monitoring | practice-11, discourse-06, governance-12 |
| -13 pre-filing audit-risk prediction | practice-12, discourse-11, governance-10 |
| -15 AI-enabled managed service and provider disclosure | practice-14, governance-16 |
| -16 value pricing (idea) | discourse-13, governance-06, pricing parts of practice-04 and -14 |
| -17 staff-built pipelines and automations | practice-15, discourse-08, discourse-14 |
| -19 AI-use and verification record | discourse-15, governance-04 |
| -20 approved enterprise tools and vendor terms | governance-07, governance-14 |
| -21 gated rollout, metrics and unaided competence | governance-03, governance-13, governance-15 |
| -24 continuous monitoring (idea) | practice-16, discourse-10 |

Kept as single-source entries: -04 (discourse-07), -05 (practice-04), -06 (practice-05), -14 (practice-13), -18 (discourse-12), -22 (governance-08), -23 (governance-09).

Where the angles disagreed I took the more conservative reading and noted it: OpenAI maturity `piloting` (practice said in production); Savant/Oxford ladder `automate` (discourse said augment; kept automate because the pattern is reconciliation with exception routing, noted in the entry); continuous monitoring scope `process` (practice said model; the vocabulary puts "made continuous" under process).

**Canonical source keys** (two keys for one document in the deep dives): EY-BTAX-2025 (not BLAW-EY-2025), TR-NEOTAX-2025 (not NEOTAX-TR-2025), SALA-TAXNOTES-2026 (not TAXPROF-SALA-2026; typed academic), STRIKETAX-2026 (not STRIKE-6765-2026; date year-only because its metadata conflicts), IRS-F6765-INSTR-2025 (not IRS-F6765INSTR-2025), TR-TENSIONS-2025 (not TR-GENAI-2025), TAXADVISER-WERFEL-2026 (not AICPA-WERFELART-2026), OPENAI-TAXDATAJOB-2025 (not OPENAI-JOB-2025). IRS-OPR-2026 (primary text) replaces JOFA-OPR-2026 (press report of it). Dates harmonised: KPMG-DE-2026 to 2026-05 (6 vs 7 May), CORPTAX-2026 and undated vendor pages to 2026 (a retrieval month is not a publication date).

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 11, 13, 17, 19, 20 | | | 5 |
| augment | 01, 02, 03, 04, 12, 18 | 05, 09, 14, 21, 22 | 16 | 12 |
| automate | 23 (D) | 10 (B), 24 (D) | | 3 |
| delegate | | 06 | 07 (B), 08, 15 | 4 |

All four ladder levels and all three scopes have entries. **Automate is weak**: one grade B entry whose workflows are not stated (Oxford Industries) and two research or practitioner ideas. Delegate rests on announcements (Byron, firm platforms), recruiting copy (OpenAI) and survey-level managed-service evidence. No assist-level process or model change was found, and no evidence was invented to fill those cells.

## Grade mix

A 0, B 4 (17%), C 16, D 4. The four B entries are named organisations without published measurements: PwC K-1 agents (-02) and PwC's explainable ETR model (-18), both in adjacent settings and capped at B; OpenAI's in-house team (-07, job listings and a demonstration); Oxford Industries with Savant (-10, a vendor press release). Grades were not raised to approach the 50% A/B target; the module is honestly rated thin and says so at the top.

## Gaps

- **No measured outcome anywhere.** No error rate, override rate, parallel-run result, review-time change or inspection finding for AI on 1120s, 5471/8858, state returns or Section G. Every number is vendor-published, self-reported, an illustration, or from individual-return benchmarks.
- **Steps with no AI evidence:** Forms 5471/8858 (rules-based bots only), estimated payments and extensions, state apportionment beyond Byron's product description, return-to-provision true-up.
- **In-house voice:** only two named in-house teams (Oxford Industries, OpenAI). Amazon, Walmart, Home Depot and P&G appear only as attendees or panellists. Closed communities (TEI chapters, r/taxpros) were not reached; the TEI Annual Conference (from 17-18 Oct 2026) has no recaps yet.
- **Governance fit:** OPR, PCRT, SSTS and the Werfel register address practitioners; none says how it applies to employees preparing their employer's return.
- **Unresolved dates:** Section G timeline wording (IRS instructions 12/2025 vs practitioner reports of final instructions in Feb 2026); Werfel framework publication date (2026-08-31 page vs "earlier this month" in the 23 Sep release); EY-COMPL-2026 may be a republished older piece.
- **Cross-references:** only the transfer-pricing use-case file existed in `archetypes/tax/` at synthesis time, with no overlap, so overlaps are named by module (compliance individual-business, provision, research-advisory, controversy, indirect-tax, tax-data-technology) rather than by id. Re-link once those files exist: -06 to individual-business agentic return entries; -11 to research-advisory; -14 and -18 to provision; -13 and -24 to controversy and indirect-tax.

## Items routed to compliance-corporate from other files

Picked up and used: KPMG Digital Gateway, EY and PwC platforms, Savant/Oxford (individual-business practice) in -08 and -10; TEI Tax Tech findings and Sala (individual-business discourse) throughout; KPMG Germany survey, TR corporate department reports and TEI material (individual-business governance) in §5; Bloomberg Tax Leadership Forum (controversy governance) in -07; Neo.Tax and Section G (tax-data-technology discourse) in -09; Compliance Tracker AI Assistant, Werfel risk 3 and neuro-symbolic calculation (research-advisory discourse) in -12, -01/-02 and -22; PwC K-1 agents and HMRC software guidelines (research-advisory governance) in -02, -12 and -20; PwC K-1, myRSM Tax and EY compliance agents (research-advisory practice) in -02, -06 and -08.

Not used: HMRC R&D compliance-letter concerns (ICAS-HMRC-2025, routed from controversy discourse; the inputs give no detail beyond a one-line mention and it is authority-side); Avalara property-tax agents (AVALARA-AVI-2025, routed "to compliance" from indirect-tax practice; property tax is outside this module's income-tax scope and no detail was given; suggest tax-data-technology or a SALT sub-topic). Items routed "to compliance" that concern individual returns (TaxGPT, the OpenAI Crete 1040 pilot, IRS Zero Paper, TaxCalcBench as a return benchmark) belong to the individual-business lens; TaxCalcBench is used here only as adjacent evidence in -22.

## Routed from this module's inputs to other modules (for their synthesis)

- **controversy:** AI reading and answering tax notices, including image-to-text extraction of state notices and TEI's "Managing Tax Notices with AI" lab (discourse-02; EY-BTAX-2025, TRINST-TEIAUDITOR-2026, TEI-MIDYEAR-2026); tax-authority AI and audit selection (TIGTA-2025, GAO-2026, IRS-AIFIRST-2026, DELOITTE-TTT-2026 scenarios, BTAX-FORUM-2026); IRS amended-return AI, IRM 10.24.1, CDTFA generative AI, the EY 2025 Tax Risk and Controversy Survey; *Clinco*, *Khoja* and IRC 6673.
- **indirect-tax:** ONESOURCE Sales and Use Tax AI (TR-SUTAI-2026, TR-ONESOURCEPLUS-2025) and the EY sales-and-use lookback example (EY-COMPL-2026); continuous transaction controls and authority-side real-time audits (TRINST-TEIAUDITOR-2026); agentic indirect-tax workflows (TR-READYEXP-2026); Fonoa survey detail (FONOA-2026).
- **compliance (individual and small-business):** Ready to Review and the CLH CPAs quote (TR-COCOUNSEL-2025, TR-R2R-2025); TaxCalcBench (COLUMN-TAXCALCBENCH-2025); The Accounting Podcast episodes on Claude-built workpapers and the Basis 1065 agent (ACCTPOD-SAMLEON-2026, ACCTPOD-477-2026); AICPA tax software survey (AICPA-TAXSW-2026); the Werfel case study.
- **international-pillar-two:** GloBE Information Return and Orbitax XatBot modes (TR-CORPAI-2026); data as the constraint after Pillar Two (KOGNITOS-2026).
- **provision:** Bloomberg Workpapers to Provision (BTAX-ASC740-2026); Neo.Tax live credit data and return-to-provision effects (TR-CORPAI-2026); PwC's explainable ETR model (PWC-MEGNA-2025; also kept here as -18); ASU 2023-09 workload.
- **transfer-pricing:** Orbitax Tax Skills (TR-CORPAI-2026).
- **research-advisory:** CoCounsel Tax and corporate research guidance (TR-CORPAI-2026, WK-CORPRES-2026, TR-AGENTICCORP-2025); Sala's question whether tax AI could displace Big Four planning opinions (SALA-TAXNOTES-2026); R&D credit for clients' own AI projects (CPAPA-RD-2026); hallucination evidence and benchmarks (BTAX-HALLUC-2026, NormBench, TaxPraBen).
- **tax-data-technology:** KPMG Global Tax Readiness Dividend (KPMG-READINESS-2026).
- **cross-cutting professional responsibility:** OPR Alert 2026-19, CART and the Werfel framework (IRS-OPR-2026, AICPA-CART-2026, AICPA-WERFEL-2026).
- **trend context only:** BGOV-TALKINGTAX-2024 (October 2024 podcast with Amazon, Edward Jones and Sabre tax leaders).

## Suggested improvements to the briefs

1. **Fix one canonical source-key registry per archetype before the deep dives run.** The three angles used eight pairs of different keys for the same document and disagreed on dates for four documents; a shared `sources.yaml` would remove most merge work.
2. **Ask each angle to state its ladder and scope reasoning in one line**, so the synthesis can resolve disagreements (three occurred here) without re-reading the sources.
3. **Give the governance angle a "use case or guardrail?" test.** Ten of its sixteen candidates were controls (logging, vendor terms, competence checks) rather than changes to the work; several fit better as guardrails or prerequisites.
4. **Name the in-house versus firm split in the module brief.** Most governance texts address practitioners; ask angles to flag when a source does not apply to in-house teams.
5. **Pre-assign notices and authority-side AI to controversy** in every compliance brief to avoid candidates being built and then routed.
6. **Allow a "thin module" grade target.** The 50% A/B target cannot be met honestly here; the brief should let the synthesis report the shortfall without a validator warning being read as a defect.
