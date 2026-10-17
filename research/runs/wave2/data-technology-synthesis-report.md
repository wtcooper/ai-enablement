# Synthesis report: tax / data-technology

- **Prepared:** 2026-10-17
- **Inputs:** `landscape-tax.md`, `tax-data-technology-practice.md`, `tax-data-technology-discourse.md`, `tax-data-technology-governance.md`, plus the "Routed to other modules" sections of every other `tax-*.md` file in wave 2.
- **Outputs:** `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/data-technology.md` (287 lines) and `.../tax/use-cases/data-technology.yaml` (24 entries). `scripts/validate.py`: 0 errors. One expected warning: the A/B share is below 50%.
- **Naming:** the landscape and deep dives call the module `tax-data-technology`. The output uses module id `data-technology` and ids `tax-data-technology-NN`.

## Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 16 (B 7, C 8, D 1) | 17 (B 2, C 12, D 3) | 15 (B 1, C 12, D 2) | 48 |
| Out | | | | 24 (B 8, C 14, D 2) |

**Dropped as duplicates of entries in other tax modules, with cross-references instead:** practice-13 (PwC K-1 data mapping, same source and change as `tax-compliance-corporate-02`), discourse-17 (effective-rate and deferred-tax scenario modelling, `tax-compliance-corporate-14`), governance-10 (deterministic engine with a model layer, `tax-compliance-individual-business-10` and `tax-compliance-corporate-22`), governance-12 (approved enterprise-standard AI tools, `tax-compliance-corporate-20`). The facts they carried still appear in the module where they matter (for example KPMG Germany's 89% and 29% figures in §5).

## Duplicates merged

| Final id | Merged from |
|---|---|
| -01 tax data layer | practice-01, discourse-01, governance-01 |
| -02 agentic data assembly, mapping and anomaly checks | practice-15, discourse-02, discourse-03 |
| -07 analyst-built pipelines under controls | practice-04, discourse-05, governance-04 |
| -08 automations as controlled assets | practice-05, governance-05 |
| -09 scheduled multi-system reconciliation | practice-06, discourse-04 |
| -11 notice and document extraction with verification | practice-14, discourse-06, governance-11 |
| -13 pre-submission validation and preventive controls | governance-02, discourse-12 |
| -14 e-invoice format mapping and rejection fixes | practice-09, discourse-07 |
| -15 rule-change impact on configuration | practice-08, discourse-10 |
| -16 continuous reconciliation (idea) | practice-10, discourse-11, governance-03 (all ideas) |
| -18 agents call tax engines through MCP | practice-12, discourse-08, governance-09 |
| -19 decision log and audit trail | discourse-09, governance-08 |
| -23 central tax operations and technology team | discourse-14, governance-13 |
| -24 co-sourcing and provider AI due diligence | discourse-15, governance-14 |

Kept as single-source entries: -03 (practice-07), -04 (discourse-16), -05 (practice-16), -06 (practice-02), -10 (discourse-13), -12 (governance-15), -17 (practice-11), -20 (governance-06), -21 (governance-07), -22 (practice-03).

**Where the angles disagreed, I took the more conservative reading and said so in `notes`:**
- -07 graded C, not B. The governance angle argued for B on OpenAI's live demonstration. A demonstration is not a production claim, and the practitioners behind the 15-minute figure are unnamed. OpenAI's team is graded B in -22.
- -22 OpenAI maturity is `piloting`, not `in-production`, to match `tax-compliance-corporate-07`.
- -08 is augment/process, not automate/step. People approve every promotion to production.
- -14 scope is `step`: the flow is not redesigned.
- -02 ladder is augment: two of the three sources describe people reviewing flagged items.
- -13 kept governance's B-capped C. Discourse-12's idea became a sub-point.

**Canonical source keys** (the deep dives used different keys for the same document; I aligned them to keys already used in published tax YAML files):

| Used | Instead of |
|---|---|
| TRINST-TEIAUDITOR-2026 | TR-AUDITOR-2026, TR-TEIAUDITOR-2026 |
| SAVANT-2026 | SAVANT-TEI-2026 |
| DELOITTE-LU-2025 | DELOITTE-TTT-2025 |
| DELOITTE-TTT-2026 | DELOITTE-RIDING-2026 |
| TR-TENSIONS-2025 | TR-GENAI-2025 |
| INNOVATETAX-VXE-2026 | INNOVATETAX-VERTEXEU-2026 |
| SALA-TAXNOTES-2026 | TAXPROF-SALA-2026 (kept as type `press`, as the deep dive typed it) |
| OPENAI-USTAXOPSJOB-2026 | OPENAI-JOB-USTAXOPS-2026 |
| OPENAI-TAXDATAJOB-2025 | OPENAI-JOB-TAXDATA-2025 |
| OPENAI-DIRECTTAXJOB-2026 | OPENAI-JOB-DIRECTTAX-2026 |

BTAX-EYGRIP-2025 is kept as the deep dive and controversy use it; `compliance-corporate.yaml` uses EY-BTAX-2025 for the same article. TEI-TECHTAX-2025 is typed `professional-body` and dated 2025-11-17 (the deep dives disagreed). AVALARA-MCP-2026 uses the practice and governance URL.

## Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 07, 17 | 04 (B) | 20 | 4 |
| augment | 11, 14, 19 | 01 (B), 02, 03, 06 (B), 08 (B), 15, 21 | 22 (B), 23 (B) | 12 |
| automate | none | 05 (B, not AI), 09 (B), 13, 16 (D) | 12 | 5 |
| delegate | none | 10 (D), 18 | 24 | 3 |
| Total | 5 | 14 | 5 | 24 |

Every ladder level and every scope has at least one entry.
- **Automate is thin.** One AI case has figures: Rover (-09), with vendor-published numbers. -05 is a pre-generative-AI baseline. -12 is a regulatory regime, not a tool. -13 and -16 have no named deployment.
- **Delegate has no deployment.** It rests on vendor MCP announcements (-18), survey-level co-sourcing evidence (-24) and a conference idea (-10).
- **No automate-level single-step entry was found.** I did not invent one.

## Grade mix

A 0, B 8 (33%), C 14, D 2.

The eight B entries are all named organisations without published measurements:
- Snowflake (-01, -06), from a job posting.
- Siemens Energy and Daimler Truck (-04), ERP talks that are not about AI.
- DuPont (-05), a pre-AI baseline.
- Oxford Industries (-08), quoted by its vendor.
- Rover (-09), vendor-published figures in an adjacent sales-tax process.
- OpenAI (-22), job postings and a demonstration.
- Unilever Ice Cream (-23), a podcast description.

Two of the eight are not AI deployments. I did not raise grades to approach 50%. The module says at the top that the evidence is thin.

## Gaps

- **No independent quality evidence** for AI in tax data pipelines, mappings, reconciliations or e-invoice interfaces. None of the three deep dives found an error rate, override rate, parallel-run result or inspection finding. The only independent figure (Peru e-invoicing, BELLON-PERU-2022) measures a regime, not AI.
- **No in-house case study with named metrics.** Named organisations appear only through job postings, vendor releases, a podcast listing and conference recaps. The Savant and Oxford Industries TEI session (2026-04-28) has no recap.
- **No customer use of a tax MCP server.** Only vendor documentation exists (Avalara, Kintsugi, Sovos). Thomson Reuters ONESOURCE MCP support was not found.
- **No figures for token or agent run cost**, although TEI attendees raised it.
- **No sustainment practice.** TEI's "Automation Sustainment" session is a title only. Nothing was found on inventories, risk tiering or ownership standards for AI-built tax tools.
- **Real-time reporting outside Europe** (LATAM, India, Saudi Arabia) appears only as a country list.
- **TEI evidence is second-hand.** It comes through Thomson Reuters Institute recaps, which are vendor-owned. The TEI Annual Conference (October 2026) had no recaps yet.
- **Landscape corrections carried from the deep dives:**
  - EY's "80% struggle with foundational data" and "75% earliest stages" are not on EY's release, which gives 51% and 44%. The 80% figure appears in a Bloomberg Tax write-up, framed differently.
  - "OpenAI's tax department (four people)" is not supported. The recap says four members were sent to the seminar.
  - Sovos did not "add" MCP and A2A interoperability. The release says a gateway is in development.
  - Fonoa's "8x" cohort is not precisely defined on the page.

## Routed to other modules (from this module's three deep dives)

| Item | Target module | Source keys |
|---|---|---|
| OpenAI and Crete firms 1040/1041 pilot (7,000 returns; vendor-published accuracy and time figures) | compliance-individual-business | OPENAI-CODEX-2026; RUNTIMEWIRE-2026 |
| Neo.Tax R&D credit data capture and Form 6765 Section G | compliance-corporate | TR-CORPAI-2026 |
| ONESOURCE Sales and Use Tax AI claims; exemption certificates; HS classification and Global Classification AI | indirect-tax | TR-SUTAI-2026; TR-ONESOURCEPLUS-2025; AVALARA-AGENTIC-2025 |
| Indirect-tax determination engines, e-invoicing network scale, Greek and French mandates, Fonoa workflow adoption data, Oxford Nanopore sales-tax saving (recap) | indirect-tax | FONOA-2026; INNOVATETAX-VXE-2026; SOVOS-SOVI-2026 |
| Avalara AI tax research (one user quoted: research time down more than 80%) | research-advisory | AVALARA-AGENTIC-2025 |
| OpenAI tax department's Slack Q&A, daily digest and research-memo agents (demo timings) | research-advisory | SJSU-TEIHTTI-2025 |
| Close-to-provision handoff and provision forecasting; 58% under-resourced in the data-layer argument | provision (provision-pillar-two) | KOGNITOS-2026; PWC-IE-2026 |
| CAQ: tax accounting issues averaged 12% of restatements, 2013-2022 (search-only, via BDO) | provision | CAQ-RESTATE-2024 |
| GIR XML pipeline: country XML variants, business-rule validation, KPMG's report that in some jurisdictions only 20% of GIRs were filed successfully before the initial deadline, 120+ business rules, 19 second-wave jurisdictions; Orbitax XatBot; EY 21% very prepared / 81% most significant change | international-pillar-two | FGS-GIR-2026; BTAX-KPMGP2-2026; LUCANET-2025; TR-CORPAI-2026; EY-TFO-2025 |
| State notice response and drafting; authority-side analytics | controversy | TRINST-TEIAUDITOR-2026; BTAX-EYGRIP-2025 |
| Tax-authority AI: HMRC roadmap and FOI story, OECD real-time sharing pilots and 70% FTA adoption, IRS inventory and staffing (GAO), TIGTA model evaluation, Grant Thornton OECD summary | controversy (tax-authority AI) | ICAS-HMRC-2025; OECD-FTA-2025; GAO-2026; TIGTA-2025; BTAX-OECD-2025; GT-IE-OECDGOV-2025 |
| TP master and local file maintenance (German head of tax interviewed by EY) | transfer-pricing | BTAX-EYTFO-2026 |
| Circular 230 duties, fees, confidentiality; Werfel framework and CART; CIOT DITT episodes on AI liability (2026-06-12) and junior roles (2026-07-03) | x-guardrails-professional-responsibility | IRS-OPR-2026; AICPA-WERFEL-2026; AICPA-CART-2026; CIOT-DITT-2025 |
| TaxCalcBench, TaxBench, JHU neuro-symbolic work | compliance-individual-business | COLUMN-TAXCALCBENCH-2025; COLUMBIA-TAXBENCH-2026; JHU-TAXREASON-2025 |
| Deloitte scenarios on company vs authority AI progress | x-state-of-ai-disruption | DELOITTE-TTT-2026 |
| Microsoft Fabric tax data hub at BMTax (Brazil): search-only, figures not used | data-technology (not used) | BMTAX-MS-2026 |

## Items routed into data-technology from other wave 2 files

| From | Item | Disposition |
|---|---|---|
| compliance-corporate discourse; research-advisory discourse | CTCs, clearance regimes, authority real-time audits | Integrated (-12, -13, -16) |
| compliance-corporate discourse | Agentic indirect-tax workflows (TR-READYEXP-2026) | Left with indirect-tax |
| compliance-corporate governance | KPMG Global Tax Readiness Dividend | Integrated (-23, §5) |
| compliance-individual-business discourse; controversy discourse; controversy governance | TEI themes (ownership, training, silent failure, token cost); Sala; in-house adoption surveys | Integrated (-20, -21, -23, §7, §9). TR-FOP-2026 was not in this module's inputs and is not cited |
| controversy practice; research-advisory discourse and practice | Oxford Industries and Savant TEI session; OpenAI pipelines; TEI tooling lists | Integrated (-07, -08, -09, -22). The key SAVANT-OXFORD-2026 used in research-advisory practice refers to the same release, given here as SAVANT-2026 |
| controversy practice | IRS "IaaP Accelerator" agentic tool for cloud code compliance (TREAS-AIINV-2026) | Held. It is tax-authority IT, and the routing note gives no detail to write from. Suggest controversy (tax-authority AI) |
| indirect-tax discourse | UC10 MCP/A2A, UC13 finance orchestration, UC04/07 e-invoicing data foundations | Resolved by cross-reference. The indirect-tax synthesis already holds these as `tax-indirect-tax-16`, `-18`, `-08`, `-12`. Data-technology -14, -17 and -18 keep the data and access-control side |
| indirect-tax governance | KPMG's ERP and data-quality findings and e-invoicing ownership (KPMG-INDIRECT-2026) | Ownership is covered through TR-VIDA-2026. KPMG-INDIRECT-2026 is held: not in this module's inputs |
| indirect-tax practice | MCP/A2A architecture | Integrated (-18) |
| indirect-tax practice | Customs and HS classification | Held. Outside the module definition; suggest indirect-tax or a customs sub-topic |
| provision-pillar-two combined | Orbitax MCP connections, Lucanet XML backbone, public CbCR | Held. GIR XML is excluded by the module definition, and the routing note has no detail on Orbitax MCP. Revisit next wave |
| research-advisory governance | TR resourcing and ERP migration findings | Integrated (-04, -23) |
| transfer-pricing discourse | Samsung tax manager's op-ed on agentic tax transparency (BTAX-LEE-2025); TPMinds technology panel | Held. The source detail is not in the inputs |
| transfer-pricing governance | Data governance as the constraint (ITR-NEXDIGM-2026, KPMG-GR-2026) | Held, same reason. The theme is already covered by -01 and -20 |
| transfer-pricing practice | Public CbCR and ESG overlap; KPMG Digital Gateway | CbCR held. Firm platforms are cross-referenced to `tax-compliance-corporate-08` |

## Suggested improvements to the briefs

1. **Issue a shared source-key registry before the deep dives.** The three angles gave seven documents two or three different keys, and the published tax YAML files already disagree (for example DELOITTE-LU-2025 vs DELOITTE-TTT-2025, EY-BTAX-2025 vs BTAX-EYGRIP-2025). A registry would stop the drift at the source.
2. **Name one owning module for each shared topic in the brief.** E-invoicing rejection handling, MCP interoperability and audit trails were researched in both indirect-tax and data-technology. The second synthesis has to fall back on cross-references.
3. **Give deep-dive researchers the use-case ids already published in sibling modules,** so they can mark overlaps as they write instead of leaving the work to synthesis.
4. **Set a grading rule for job postings and live demonstrations.** The angles split B against C on the same evidence (OpenAI). Suggestion: postings that describe current practice count as B, intent-only postings count as C, and a demonstration alone counts as C.
5. **Make routed items carry their facts and URL,** not a one-line pointer. Several items routed here (KPMG-INDIRECT-2026, BTAX-LEE-2025, ITR-NEXDIGM-2026) could not be used without re-opening sources, which this step does not allow.
6. **Say in the vocabulary that `provenance` is omitted for "none published" outcomes.** The deep dives variously used `n/a`, `vendor-published` and nothing.
7. **Ask for pre-AI baselines to be labelled as such** and kept out of the A/B share, or counted separately. Two of this module's eight B entries are not AI.
8. **Plan the search budget per angle.** The practice angle ran out after 15 searches, before planned searches on LLM account-mapping accuracy and independent e-invoice rejection data.
