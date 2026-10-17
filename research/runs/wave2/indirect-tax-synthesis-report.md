# Synthesis report: tax / indirect-tax

- **Date:** 2026-10-17
- **Inputs:** `landscape-tax.md` (sections 1, 7.3, 10-14), `tax-indirect-tax-practice.md`, `-discourse.md`,
  `-governance.md`, and the "Routed to other modules" sections of every other `tax-*-*.md` file in `research/runs/wave2/`.
- **Outputs:** `plugins/.../archetypes/tax/modules/indirect-tax.md` (296 lines) and
  `plugins/.../archetypes/tax/use-cases/indirect-tax.yaml` (22 entries).
- **Validator:** `python3 scripts/validate.py` gives 0 errors for these files. It warns that the A/B share (18%) is
  below the 50% target. No grade was raised to meet it (see section 4). The one error the validator reports at the time
  of writing is another module's file (`compliance-individual-business.md`, 312 lines).

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 20 (0 A, 2 B, 16 C, 2 D) | 15 (0 A, 0 B, 14 C, 1 D) | 16 (3 A, 3 B, 7 C, 3 D) | 51 |
| Out | | | | 22 (2 A, 2 B, 16 C, 2 D) |

Six candidates were not carried into entries here (all are covered elsewhere or folded into text):

| Candidate | Grade in | Where it went |
|---|---|---|
| G04 CDTFA generative AI agent assist (sales and use tax enquiries) | A | Already `tax-controversy-20`; cross-referenced in the module |
| G13 IRAS chatbot with an LLM engine (GST among other taxes) | B | Authority chatbots are `tax-controversy-18`; cross-referenced |
| G06 Authority ML risk scoring on VAT data (Austria, HMRC, ViDA) | B | Already `tax-controversy-15`; ViDA and HMRC points kept in Guardrails and Frontier |
| G16 HMRC guidance for AI-powered products | D | Kept as a dated Frontier line (HMRC-ROADMAP-2025), not an entry |
| D07 Three-way reconciliation of calculated, invoiced and reported tax | D | Same entry exists in `tax-data-technology-discourse.md`; left for that synthesis |
| D14 Tax-team-built AI pipelines | C | Already `tax-compliance-corporate-17`; its state-notice extraction example was merged into `#14` |

Dropping the three authority-side entries removed one A and two B entries from this file. That was done because the
brief asks for cross-references instead of duplicates; the archetype pass can move one back if it prefers.

## 2. Duplicates merged

| Out | Merged from | Decision |
|---|---|---|
| 01 Product tax codes with confidence scores | P01 (C), D01 (C), G10 (A) | **A**, resting only on Dell's measured test set (NATH-DELL-2025). Maturity lowered from in-production to piloting: Vertex's production customers are unnamed. Customs HS evidence (ZHANG-HS-2026) routed out |
| 02 Agent-prepared returns, filed after approval | P02 (C), D03 (C), G01 (C) | C. Delegate/process (governance had augment) |
| 03 Certificate validation at receipt | D02 (C), G14 (C) | C |
| 04 Full-population certificate re-validation | P03 (C) | C. Kept separate from 03: a different change (whole store, process). Maturity lowered to piloting |
| 05 In-platform taxability Q&A | P04 (B), D09 (C) | B (Singer Equipment beta quotation) |
| 06 VAT place-of-supply assistant verified by an adviser | G02 (A) | A (research prototype, real cases) |
| 07 Plain-language rule drafting | P05 (C), D15 (C) | C. Maturity announced (practice had piloting) |
| 08 E-invoice rejection diagnosis | P06 (C), D04 (C), G07 (C) | C. Augment/step: each correction needs approval (discourse had delegate/process) |
| 09 Regulatory-change monitoring | P07 (C), D05 (C) | C |
| 10 Invoice, receipt and expense extraction | P08 (C), P14 (C) | C. Same change (documents into validated tax data). Maturity lowered to piloting |
| 11 Pre-filing anomaly detection and exception triage | P09 (C), D06 (C), G15 (C) | C. G15's nexus pre-screen moved to 13 |
| 12 Data validation and repair at entry | P10 (C), G12 (D) | C |
| 13 Nexus and registration agents | P11 (C), D12 (C), part of G15 | C. Delegate (registration agents) |
| 14 Notice intake and extraction | P12 (C), part of D14 | C |
| 15 Audit-ready decision records | P13 (C), D08 (C), G05 (C) | C. Augment/process (governance had assist) |
| 16 Tax engines callable by customers' agents (MCP, A2A) | P15 (C), D10 (C), G08 (C) | C. Model scope (governance had process) |
| 17 Tax at agent-initiated checkout | P16 (D), D11 (C), G09 (B) | **C. Governance's B downgraded**: the Shopify design is a training provider's second-hand description, and no organization reports tax handling in agent checkout. Practice's D upgraded because practitioners and a vendor describe the architecture |
| 18 Compliance-by-design finance agents (Sovos-Flowie) | P17 (C), D13 (C) | C |
| 19 AI-enabled managed compliance service | P18 (C) | C. In-production (Numeral runs it), graded C because the only evidence is its own release |
| 20 General AI for first-pass analysis in a sanctioned workspace | P19 (B), G11 (C) | B (Plusgrade posting) |
| 21 Exposure, accrual and scenario analysis (idea) | P20 (D) | D |
| 22 Rule engine checks LLM-agent VAT steps (idea) | G03 (D) | D |

**Source-key canonicalisation**

| Canonical key | Input keys |
|---|---|
| AVALARA-AGENTIC-2025 (Accounting Today) | ACCTODAY-AVALARA-2025 (governance) |
| AVALARA-AGENTIC-2025b (iTWire) | ITWIRE-AVALARA-2025 (governance) |
| FONOA-2026 (survey landing page) | FONOA-2026-SURVEY (discourse), FONOA-INDIRECT-2026 (governance) |
| FONOA-176-2026 (Fonoa blog on 176 leaders) | FONOA-BLOG-2026 (governance). Renamed because practice used FONOA-BLOG-2026 for a different page (the blog index), now FONOA-BLOGINDEX-2026 |
| FONOA-CITATION-2026 | FONOA-PRIMARY-2026 (discourse) |
| FONOA-MONITORING-2026 | FONOA-REGMON-2026 (discourse; different page title, same URL) |
| TR-INDIRECT-2026 (typed survey) | TR-INDIRECT-DATA-2026 (practice; governance typed it vendor) |
| TR-AGENTICIT-2026 | TR-READYEXP-2026 (compliance-corporate discourse) |
| BTAX-AGENTICCOMMERCE-2026 | BTAX-AGENTIC-2026 (discourse), BTAX-BAL-2026 (governance) |
| SOVOS-FRANCE-2026b ("Three weeks into France", 23 Sep) | SOVOS-FRANCE-2026 in discourse. Practice used SOVOS-FRANCE-2026 for the 18 Aug release, which keeps that key |
| EC-VIDA-2025 (module sources only) | EC-VIDA-2026 (practice; page date 2026-05-20 vs governance's "undated", adoption 2025-03 used) |
| CDTFA-2025, KPMG-HU-2026 (module sources) | TAXNOTES-CDTFA-2025, KPMGHU-AUDITPLAN-2026; the controversy YAML's keys are used |
| STI-AGENTIC-2026 | Type press (two of three angles; practice said firm); title from practice and discourse (governance had a different title) |

Key inconsistencies seen in other finished tax files, for the archetype pass: the TEI auditor recap appears as
TRINST-TEIAUDITOR-2026 (typed press in some files, conference in others) and TR-TEIAUDITOR-2026; the Werfel appendices
as AICPA-WERFEL-2026 and AICPA-WERFELAPP-2026; the PCRT announcement as PCRT-AI-2026 and ATT-PCRTAI-2026, typed
professional-body or standard-setter.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 05 | none | none | 1 |
| augment | 01, 03, 06, 07, 08, 20 | 09, 11, 12, 15, 21, 22 | none | 12 |
| automate | 10, 14 | 04, 17 | 16 | 5 |
| delegate | none | 02, 13 | 18, 19 | 4 |
| Total | 9 | 10 | 3 | 22 |

- **Assist** is thin because the assist candidates (G05 decision records, G11 sanctioned workspace, P16 checkout review)
  merged into entries where AI gives a first pass. Plain assist use certainly happens (60.8% rely on public tools) but
  the sources describe it as governance risk, not a use case.
- **Delegate** rests on vendor launches (Thomson Reuters, Avalara early access), a Deloitte illustration, an announced
  acquisition (Flowie) and one provider's funding release (Numeral). No measured delegate deployment exists.
- **Model** scope has no evidence beyond announcements and a provider's self-description.
- **Augment/process** entries (six) do not map neatly to a single Reimagine lens; the module lists them under
  "Improve (process)".

## 4. Grade mix

A 2 (9%), B 2 (9%), C 16 (73%), D 2 (9%). A/B share 18%, below the 50% target. Reasons, stated plainly:
- No named organization has published a measured outcome for AI in indirect-tax work. Both A entries are academic:
  Dell's self-reported test-set result for tax-code prediction (a named company, not stated to be in production) and an
  independent Austrian VAT study on 20 real client cases (a research prototype).
- Both B entries rest on thin signals: one beta customer's quotation in a vendor release (Singer Equipment) and one
  employer's job posting (Plusgrade).
- Every commercial figure (Thomson Reuters 65%, 30 to 11 days, 75%; Numeral 30-40% and 80%; Vertex seconds per product;
  Sovos 1.6%) is vendor-published with unnamed customers.
- Three A/B candidates were left to the controversy module to avoid duplication (section 1).
The module says it is thin in its first paragraph.

## 5. Routed items

**Collected from the indirect-tax inputs, for other modules**
- **controversy:** South Carolina DOR's AI audit selection starting with sales and use tax (SCPOST-AUDIT-2026;
  KOGOD-SCDOR-2026), SEATA commissioners on AI audit selection (WITHUM-SEATA-2026), Tax Notes survey of state agencies
  (TAXNOTES-UNWATCHED-2026), Hungary's audit plan (KPMG-HU-2026), the OECD speaker's claim that AI cut some VAT
  investigations from nine months to three (SSL-OECDVAT-2026, second-hand), *Rafique v HMRC* (ROSSMARTIN-RAFIQUE-2026,
  CITYAM-RAFIQUE-2026), Austria's risk models, IRAS chatbot and HMRC roadmap (OECD-GOVAI-2025, HMRC-ROADMAP-2025), EU AI
  Act Recital 59 and Hadwick (HADWICK-EUAIACT). The controversy synthesis already holds the state, Hungary, Austria,
  CDTFA and chatbot items (`tax-controversy-15`, `-18`, `-20`).
- **tax-data-technology:** customs and trade classification (Avalara cross-border agents, TR ONESOURCE Global
  Classification AI, ZHANG-HS-2026); MCP/A2A architecture (overlaps `#16`); e-invoicing data foundations and ownership
  (KPMG-INDIRECT-2026; overlaps `#08`, `#12`); finance orchestration (`#18`); three-way reconciliation (D07). Those
  research entries ("Exposing tax engines to enterprise agents through MCP and A2A", "AI diagnosis and approved
  remediation of failed real-time reporting submissions", "Automatic audit trail for AI-assisted tax determinations",
  "AI-driven preventive controls upstream") duplicate `#16`, `#08`, `#15` and `#12`. The archetype pass should keep one
  of each; tax-data-technology was not synthesised when this was written, so no final ids could be cited.
- **compliance:** Avalara property tax agents (AVALARA-AVI-2025); TaxCalcBench (used here only as adjacent evidence).
- **research-advisory / controversy:** EY India AI Tax Hub research and litigation agents (EY-INDIA-2026); the
  hallucination risk in sales tax advice (FLSALESTAX-AI-2026). EY India's GST platform figures are scale context, not used.
- **tax policy of AI / international:** taxability of AI products (TAXNOTES-AISTATE-2026, INBUSINESS-FLICK-2026), AI
  services under EU VAT (IBFD-AIVAT-2026), marketplace analysis of AI commerce apps (BTAX-AGENTICCOMMERCE-2026).
- **transfer-pricing:** CJEU *Arcomet* VAT consequences of TP adjustments (BTAX-VAT2026).
- **cross-cutting governance and pricing:** IRS OPR Alert 2026-19, PCRT guidance, Werfel framework and CART, NIST AI
  RMF; OPR's fee guidance; Avalara/Censuswide finance-wide governance survey (AVALARA-GOVERNANCE-2026).
- **finance operations (outside the archetype):** Flowie's AP and procure-to-pay agents (SOVOS-FLOWIE-2026).

**Routed to indirect-tax from other wave 2 files, and what was done**
- ONESOURCE Sales and Use Tax AI (compliance-corporate practice, controversy practice, data-technology practice):
  used in `#02` (TR-SUTAI-2026; TR-ONESOURCE-2026 in controversy is the same release).
- CTC, clearance regimes and authority real-time audits (compliance-corporate and research-advisory discourse): used in
  `#08` and the process table (TRINST-TEIAUDITOR-2026). Agentic indirect-tax workflows (TR-READYEXP-2026): used as
  TR-AGENTICIT-2026 in `#02`, `#15`, `#22`.
- Fonoa survey details, the validation-process finding and "10-workflow adoption data" (compliance-corporate
  governance, research-advisory governance, data-technology discourse): survey figures and the process finding used in
  §5 and `#15`. The per-workflow breakdown is not in the inputs (full report gated), so it is not used.
- Exemption certificate validation (data-technology practice): used in `#03`. HS classification and Global
  Classification AI: customs, not used.
- EY sales-and-use lookback example (compliance-corporate practice, EY-COMPL-2026): **not used**. The routing note
  gives no detail, the EY page was not read for indirect tax in the inputs, and adding it would mean adding facts not in
  the inputs. Flag for a follow-up read.
- Oxford Nanopore sales-tax saving ("hundreds of thousands of dollars", data-technology discourse): **not used**. The
  indirect-tax discourse file says companies named at vendor events were using tax engines or automation, not
  AI-specific outcomes.
- Oxford Industries with Savant, audit-ready automation for sales and use tax and VAT (research-advisory discourse,
  SAVANT-TEI-2026): **not used**. Session announcement only, no outcome. A follow-up could turn it into a named in-house
  deployment.
- VAT and customs parts of cross-tax intercompany review (transfer-pricing governance): cross-referenced as
  `tax-transfer-pricing-11`, not duplicated. Customs and tariff interaction with TP (transfer-pricing practice):
  customs, not used.

## 6. Corrections and conflicts carried forward

- ViDA dates: the landscape's "OSS for energy" (Jan 2027) and "OSS expansion" (Jul 2028) do not match the Commission
  page, which gives OSS/IOSS clarifications (1 Jan 2027) and platform deemed-supplier rules plus single VAT registration
  (1 Jul 2028). The module uses the Commission and directive wording.
- Hadwick counts at least 85 AI systems in 26 Member States (landscape said about 70 in 18). OECD: 29 of 38 members
  use AI in tax administration (landscape's "70% of 54 FTA members" is from another report). Neither figure is needed
  in the module except Hadwick's.
- Thomson Reuters savings differ between releases (40-60% vs up to 65%); Sovos transaction volume differs (nearly 20
  billion vs more than 70 billion a year). Both noted in the YAML.
- FONOA-AIERA-2025 has two dates in the inputs (2025-10-23 and 2025-11-19); not used.
- Avalara NEXT: Avalara's own page gives 26 Mar 2026, settling the landscape conflict.

## 7. Gaps

- **No named-customer outcome with measurements** and **no independent quality evidence** (error, override,
  parallel-run or inspection results) for any commercial indirect-tax AI tool.
- **Community, podcast and forum evidence:** none reached in any angle (search budgets ran out; Reddit and LinkedIn
  blocked). Podcasts were read from descriptions only.
- **Exemption-certificate acceptance and good-faith rules** (MTC, Streamlined Sales Tax) were not retrieved, so the
  control standard for automated acceptance (`#03`, `#04`) is unknown.
- **Unreachable primary items:** Avalara's 9 Apr 2026 "AI-executed" release, Fonoa's and Thomson Reuters's gated
  reports, Avalara CRUSH sessions, ITR AI in Tax Forum agenda, OECD VAT forum release.
- **Markets and topics:** India GST, Brazil's reform, Gulf VAT, Peppol, SAF-T, VAT on imports, customs; BPO and
  outsourcing firms' own deployments.
- **Events not yet held:** TEI annual (from 18 Oct 2026), Vertex Exchange (25-28 Oct 2026), IFA Melbourne.

## 8. Suggested improvements to the briefs

1. **Fix module boundaries before the deep dives.** E-invoicing/CTC, MCP/A2A, audit trails and preventive data
   controls were researched in both indirect-tax and tax-data-technology, and authority AI in both indirect-tax and
   controversy. Give each angle brief a short "owned here / owned there" list.
2. **Keep an archetype source-key register.** FONOA-BLOG-2026 meant two different pages, SOVOS-FRANCE-2026 meant two
   different releases, and several documents had two or three keys. A shared register checked before writing would
   stop this.
3. **Define maturity for vendor-reported, unnamed customers.** Angles split between in-production, piloting and
   announced for the same evidence. Suggest: unnamed customers reported by the vendor = piloting.
4. **Give a ladder test for approval loops.** "Executes after a user approves each action" was graded augment by two
   angles and delegate by one. Suggest: approval of every action = augment; approval only at the end of a multi-step
   outcome = delegate.
5. **Reserve search budget for community, podcasts and job postings.** All three angles ran out before these.
6. **Ask practice researchers to chase named in-house speakers** from conference agendas (Oxford Industries, JLL,
   OpenAI, Stripe, Uber) for outcomes; these are the likeliest route to B and A grades.
7. **Order parallel syntheses or share an overlap file.** This synthesis could cite controversy, compliance,
   research-advisory and transfer-pricing ids only because those files landed first; tax-data-technology ids are still
   unknown.
