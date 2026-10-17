# Archetype synthesis report: tax

- **Prepared:** 2026-10-17
- **Outputs** (in `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/`):
  `ARCHETYPE.md` (100 lines), `interview-guide.md` (183), `value-chain.md` (180), `economics.md` (188),
  `state-of-ai.md` (145), `frontier.md` (119), `guardrails.md` (220), `workforce.md` (175), `disruption.md` (150),
  `objections.md` (90), `sources.md` (236; `last_researched: 2026-10-17`). Also updated
  `references/archetypes/index.md`: tax moved to "Available archetypes" (link, extends professional-services,
  recognition cues, eight module ids, Available); the professional-services row now says assurance and tax files cover
  the regulated parts of those firms only.
- **Validator:** `python3 scripts/validate.py` reports 0 errors. Warnings are the expected module A/B shortfalls.
- **Sources:** 165 distinct keys cited across the ten files; 119 shared keys are in `sources.md` Part B, the rest at the
  end of the one file that cites them. Every key resolves. Rows were built from the input files' own source tables and
  from the module YAML and module source lists (no new sources were opened).
- **Evidence column** (computed from the validator's counts at the time of writing): compliance-individual-business
  moderate (10 of 25), compliance-corporate thin (3 of 24), provision-pillar-two thin (0 of 16), indirect-tax thin
  (4 of 22), transfer-pricing thin (3 of 22), controversy moderate (10 of 25; 9 of the 10 authority-side),
  research-advisory moderate (11 of 25), data-technology moderate (8 of 24; some B entries not AI). The consistency pass
  running in parallel may change grades; if it does, update the Evidence column in `ARCHETYPE.md` and the counts in
  this report.

## 1. What each file draws on

| File | Main inputs |
|---|---|
| ARCHETYPE.md | Landscape module check and journey markers (§10-11, re-sourced to primary keys); cross-cutting guardrails file (signing rule, OPR, PCRT, TPB); state-of-ai file (TR-FOP, TR-CORPTAX, Fonoa, TEI poll, PwC, roll-ups); validator counts; module headers for one-line summaries; compliance-individual-business `#05` as the delegation reference case |
| interview-guide.md | Assurance guide as the structural model; interview probes in all four cross-cutting files; economics (Ignition, IPA offshoring, Blue J pricing, WCG per-return prices); module §2 tables for the module chooser |
| value-chain.md | Module §2 step tables (stages and work types, not repeated in detail); data-layer figures from EY-TFO, KPMG-INDIRECT, Aibidia, TR-CORPAI, FGS; work-type patterns from the use-case YAML pattern counts; TR-SOTP, TR-SOTCD, IPA for firm and in-house variants |
| economics.md | Cross-cutting economics file almost entirely (Big Four tax lines, MAP, Ignition, NSA, offshoring, PE deals and multiples, AI-native roll-ups, OPR fee rule, in-house budgets) |
| state-of-ai.md | Cross-cutting state-of-AI file (survey table, production versus announced, WCG adopter test, quality evidence, authority adoption) with its two corrections (EY 51%/44%; AICPA Top Issues "top two in five of six"); AICPA tax software survey, Blue J outlook, CPA Practice Advisor TR piece and Vals benchmark from research-advisory; HMRC and H&R Block from controversy and compliance-individual-business YAML |
| frontier.md | Frontier tables in all four cross-cutting files and the landscape; module frontier sections (indirect-tax, provision-pillar-two, transfer-pricing, controversy, data-technology, compliance) for dated product, filing-regime and authority signals |
| guardrails.md | Cross-cutting guardrails and professional-responsibility file (Circular 230 and OPR table, 7216 regulations, signing and penalties, courts, PCRT, TPB, BStBK, EU AI Act, insurance, steps needing a person); IRS-LBI-TP-2026 for TP; IRS-I8867-2025 from compliance-individual-business |
| workforce.md | Cross-cutting workforce file (pipeline, PwC and UK intake, Top 100, Stanford and MIT studies, H&R Block seasonality, offshoring and consent, new hybrid roles and postings, apprenticeship proposals, retention, in-house headcount, IRS workforce) |
| disruption.md | Scenarios A-D in the state-of-AI file, plus PE and roll-ups (economics) and new services (KPMG managed services, OECD intragroup consultation, D.C. Bar, agentic commerce); exposure table is the advisor's reading and is labelled so |
| objections.md | Objection tables in all four cross-cutting files, condensed and re-grouped |
| sources.md | Landscape sections 2-9 for Part A (conferences, regulators, bodies, academic, press, podcasts, communities, vendors, surveys) and the gap list in landscape §14 and the cross-cutting files |

## 2. Gaps

- **No independent quality evidence anywhere in tax.** No production error, override or parallel-run rate for any
  commercial tax AI tool; the only accuracy figures are benchmarks of models (TaxCalcBench, Vals) or vendor claims.
- **No measured fee, hour or margin effect of AI in tax.** The one AI-linked fee cut is an audit fee.
- **In-house evidence is thin.** No named in-house case study with metrics; how Circular 230, PCRT or TPB apply to
  in-house staff, and how auditors review AI-prepared tax balances, were not found.
- **Section 7216 and AI, reasonable cause and AI reliance, and tax-practitioner sanctions:** no authority found.
- **Surveys are mostly vendor- or Big Four-owned, often with unstated samples** (TR-FOP subset, KPMG Germany).
- **Not reached:** TEI Annual Conference (18-21 Oct 2026), IFA Melbourne, CCH Connections and TPMinds West Coast recaps;
  practitioner forums; full TR, Fonoa, Blue J and EY reports. Re-check in November 2026.
- **Dropped for weak sourcing:** a CCH Connections 2026 calendar row (the only URL was the 2025 release); Poland KSeF
  dates (search-only); EY's "80%/75%" and TR's "35%" figures (replaced by verified wording).
- **Open date question:** the Werfel article is cited as the August 2026 issue listed 31 Aug 2026; the appendices PDF is
  dated 2026-06 and the CART release (23 Sep) says "earlier this month". The archetype uses the article date.

## 3. Items routed from modules that I placed

| Item (routed from) | Placed in |
|---|---|
| Professional responsibility: OPR Alert 2026-19, PCRT, TPB, Werfel framework, CART, Clinco, fee dispute (every module) | guardrails.md (home), with pointers from ARCHETYPE, interview guide, objections |
| Werfel register correction: 20 authority risks, 15 preparer risks, article dated 31 Aug 2026 (research-advisory) | guardrails.md §8; frontier.md §2 |
| Shadow AI and firm AI policy (research-advisory, compliance) | state-of-ai.md §1; ARCHETYPE Curious marker; interview guide §2 |
| Deloitte Australia refund cited by OPR (research-advisory) | guardrails.md §6 |
| Fee dispute and AI-native roll-ups (compliance-individual-business) | economics.md §6-7; disruption.md §3-4; objections.md §3 |
| KPMG-Anthropic alliance (provision-pillar-two, to state of AI) | state-of-ai.md §3; frontier.md §3; disruption.md §7 |
| Sala and KPMG Germany headcount (provision-pillar-two, to workforce) | workforce.md §3, §9; objections.md §4 |
| Deloitte company-versus-authority scenarios (data-technology) | disruption.md §1; state-of-ai.md §8; interview guide Frame |
| Landscape corrections (EY 51%/44%; Sovos MCP "in development"; OpenAI tax team size not "four"; Fonoa "8x" undefined) (data-technology, state-of-AI file) | state-of-ai.md §2 corrections; "four people" and "8x" not used |
| Tax policy of AI and TP of AI: nexus, value creation, OECD intragroup consultation, agentic commerce (research-advisory, transfer-pricing, indirect-tax) | disruption.md §7; frontier.md §6 forecasts |
| Authority AI kept in controversy rather than moved back to indirect-tax or TP (indirect-tax, transfer-pricing) | Left in controversy; ARCHETYPE notes the module's A/B entries are authority-side |

**Routed but not placed:** AICPA survey "20% expanding services" and "keep 1040 clients to feed advisory"
(only a routing line, no detail); NIST AI RMF and the Avalara/Censuswide governance survey; CIOT DITT episodes; the
~800 citation-error figure via Bloomberg Tax (unverified); BGOV-TALKINGTAX-2024; PCAOB-GENAI-2024 and the Harris, Hardy
& Johnstone CoCounsel item (assurance, not tax); Flowie finance agents (outside the archetype); GAMMA-JOB-2026 and
TR-JOB-2026 (module detail).

## 4. Suggested module changes

1. **Shorten module §6 guardrails to step-specific items and link `../guardrails.md`.** Every module repeats the OPR
   provision list, PCRT, TPB, Werfel and CART. Keep only what is particular to the step (Form 8867 interview,
   LB&I expert expectations, GIR corrections, e-invoicing penalties) and point to the archetype file.
2. **Settle the remaining key splits.** `ATT-PCRTAI-2026` (ATT news item) and `PCRT-AI-2026` (ICAEW guidance) are both in
   use; check that each citation points to the document that holds the claim. The
   archetype now uses `TAXCT-CLINCO-2026` for the Journal of Accountancy analysis, `CLINCO-OPINION-2026` for the opinion
   text, `TAXADVISER-WERFEL-2026` for the article and `AICPA-WERFEL-2026` only for the appendices,
   `AICPA-FEES-2026`, `EC-VIDA-2026`, `RIDDLE-TRANSCRIPT-2026`, `CHARLOTIN-DB-2026` and `BLAW-TAXCT-2026`, matching the
   modules as they stood at the end of this pass. Module type labels still differ for the same document in places
   (TAXCT-CLINCO-2026 press vs professional-body; PWC-MEGNA-2025 press vs firm; SALA-TAXNOTES-2026 academic vs press).
3. **Apply the 2026-10-17 grade A rule to two A entries.** `tax-compliance-individual-business-05` rests on figures
   published by OpenAI, the co-developer, not reported as measured by the named firms; `tax-transfer-pricing-09` rests on
   customer statements on the vendor's site for rules-based automation. Both look like B under the rule. If either
   moves, update the Evidence column.
4. **Controversy: tag authority-side entries** (for example `actor: authority`) so 9 authority A/B entries do not read as
   practitioner evidence.
5. **Research-advisory §6** says the AICPA says AI moves too fast for lasting standards [ACCTODAY-CART-2026]; the
   cross-cutting professional-responsibility research did not find that statement in the sources it read. Confirm the
   quote against Accounting Today.
6. **Provision-pillar-two:** add an audit-reliance angle next time (PCAOB inspection findings on income taxes, Big Four
   tax accounting publications); it is the module's main open question and the archetype's in-house gap.
7. **Add a one-line pointer in each module header to `../ARCHETYPE.md`** so a reader landing in a module finds the
   value chain, economics and guardrails.
