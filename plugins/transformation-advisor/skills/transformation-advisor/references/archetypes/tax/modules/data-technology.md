# Tax data and technology (tax)

Last reviewed 2026-10-17. Use cases live in `../use-cases/data-technology.yaml` (24 entries). Ids are shortened here:
`#05` means `tax-data-technology-05`. Source keys in brackets, such as [TEI-TAXTECH-2026], are given in full in the YAML
or in §10. **Evidence is thin.** No entry has a measured outcome from a named organisation (no grade A); 8 of 24 are
grade B (a named deployment without published measurements), two of those are not AI (#04, #05), and the named example behind #23 does not mention AI. Every survey
figure here comes from a firm or vendor that sells tax technology or services. Say so when you quote one.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

In-house tax operations and data architecture: how ERP and ledger data reaches the tax engines, tax data stores,
building and sustaining automation, real-time reporting interfaces (e-invoicing and continuous transaction controls,
where the authority receives invoice data as it is created), agent access to tax platforms through MCP (Model Context
Protocol, a standard way for AI tools to call other systems), and the tax technology team and its governance. Tax
determination engines, GloBE (Pillar Two) XML filing and notice response sit in indirect-tax, provision/Pillar Two
and controversy. A Thomson Reuters Institute recap of the April 2026 TEI seminar says the question of whether the tools work is "effectively settled", and lists the harder problems as silent failures, tax rarely owning AI implementation, failed training rollouts and rising token costs [TEI-TAXTECH-2026].

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Extract and ingest | Pull ERP, ledger and third-party data into a tax data store | data-reporting, software-systems | 51% of tax and finance functions early in data maturity [EY-TFO-2025]; data arrives aggregated or stripped of detail [TR-GOVERNANCE-2026] |
| Map, validate, load | Map accounts to tax categories, reconcile, load provision and compliance engines | data-reporting, transaction-processing | Close-to-provision handoff a common source of delay and error (vendor view) [KOGNITOS-2026] |
| Master data and ERP projects | Keep entities, registrations, locations, products and exemptions aligned between ERP and tax engine | software-systems | Duplicate maintenance causes mismatches [VERTEX-DATASHEET-2025]; tax left out of ERP scoping [VERTEX-S4-2026] |
| Build automations | Pipelines, Alteryx or Power Platform flows, scripts, agents | software-systems | Requests wait about two months in the IT queue (anecdote) [TRINST-TEIAUDITOR-2026] |
| Control and sustain automations | Document, version, approve, monitor, hand over | software-systems, review-assurance | Workflows nobody can explain after the builder leaves [TEI-TAXTECH-2026] |
| Reconcile | Source transactions vs tax engine vs ledger vs returns | review-assurance, data-reporting | Manual month-end spreadsheets [SAVANT-ROVER-2026] |
| Real-time reporting | Validate, submit, handle rejected e-invoices | transaction-processing | In clearance regimes an invoice has no legal force until the authority returns its identifier [TRINST-TEIAUDITOR-2026] |
| Notices and documents | Extract data from notices, statements, contracts | transaction-processing | Notices "never arrive in the same format twice" [TRINST-TEIAUDITOR-2026] |
| Query and report | Dashboards and analysis on tax data | data-reporting | Manual refreshes of dashboards and spreadsheets [SNOWFLAKE-JOB-2026] |
| Agent access | Assistants and agents call tax platforms | software-systems | Custom integration for each system [AVALARA-MCP-2026] |
| Govern AI and automation | Inventory, policy, KPIs, audit trail, provider oversight | review-assurance, coordination-scheduling | 2 of 50+ say tax owns AI [TEI-TAXTECH-2026]; 12.5% have AI KPIs [FONOA-2026] |
| Operating model and sourcing | Team, roles, co-sourcing | coordination-scheduling | 58% of departments under-resourced [TR-CORPTAX-2025] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (the service or operating model changes). Coverage: assist 4, augment 12, automate 5, delegate 3;
step 5, process 14, model 5. **Automate** has one deployed AI case with figures (#09, vendor-published) and a pre-AI baseline (#05); #13 and #16
have no named deployment and #12 is a regulatory regime.
**Delegate** has no deployment: two vendor announcements and an idea. No automate-level single-step entry was found.

**Data foundation (ERP to tax engines)**
- Improve: `#01` tax-owned data layer with lineage and reconciliations (grade B, Snowflake job posting; Fortive,
  Apple roles). `#02` agentic layer that assembles, maps and anomaly-checks ledger data for the engines (vendor and
  scenario evidence). `#03` agent syncs ERP master-data changes into the tax engine, with review of high-impact
  changes (Vertex, announced). `#06` plain-language queries and reusable agents over a semantic layer, a
  business-language map of the data (grade B, Snowflake posting).
- Improve the project: `#04` tax sets data requirements in ERP migrations (grade B, Siemens Energy and Daimler Truck
  talks; not AI).
- Automate (baseline): `#05` Alteryx and Power Query consolidation (DuPont named; 1,100+ and 500+ hours at unnamed
  clients, vendor-published). Not AI; it shows what AI-built pipelines replace and inherit.

**Building and sustaining automation**
- Improve: `#07` analysts build pipelines with AI coding tools ("vibe coding": building software by prompting), about
  15 minutes against about two months in the IT queue as attendees described it. `#08` automations as controlled
  assets: version control, sign-off before production, evidence logs, drift monitoring (grade B, Oxford Industries
  quoted by Savant).
- Automate: `#09` scheduled multi-system reconciliation; Savant reports 80% less close time and 50% lower data handling cost at Rover (grade B; vendor-published, sales tax process, what was timed is unclear).
- Delegate (idea): `#10` multi-agent workflows from provision to return and credits, people on exceptions.

**Real-time reporting interface**
- Improve: `#14` AI field mapping to country e-invoice formats and approved fixes for rejections (Sovos reports
  1.6% rejections in France; AI share not stated). `#15` agent assesses how rule changes affect the company's tax
  configuration and proposes fixes for approval.
- Automate: `#13` validation of invoice and master data before submission, with preventive controls upstream.
  `#16` idea: continuous reconciliation of calculated, invoiced, reported and authority-held data.
- Reinvent: `#12` real-time transaction reporting replaces periodic returns (ViDA cross-border reporting from 2030-07-01; the UK's 2029 e-invoicing mandate initially has no e-reporting to HMRC [FISCAL-UK-2026]).
  The only independent measure in this module is here: Peru's e-invoicing raised reported sales, purchases and VAT
  liabilities by over 5% in the first year [BELLON-PERU-2022]. It measures the regime, not AI.

**Notices and documents**
- Improve: `#11` extraction of notices and documents into tax data, with every value verified against the source.

**Agent access to tax platforms**
- Improve: `#17` read-only MCP access so a general assistant answers from the company's own compliance data
  (Kintsugi, announced).
- Delegate: `#18` company agents call tax engines through vendor MCP servers with least-privilege scopes and logged
  tool calls (Avalara and Anrok list write-capable servers; Sovos gateway in development; no customer use published).

**Governance and evidence**
- Improve: `#19` decision log of AI-assisted determinations, overrides and approvals, recorded as work happens.
  `#21` acceptance thresholds before go-live, then accuracy, override-rate and cycle-time tracking.
- Reinvent: `#20` tax-owned AI inventory, policy and accountability mapped to COSO's framework.

**Operating model and sourcing**
- Reinvent: `#22` AI-first in-house model where tax staff build and review database-driven workflows (grade B,
  OpenAI postings and a live demonstration). `#23` central tax operations and technology team (grade B, Unilever's centralised tax operations centre, from a podcast episode listing; AI is not mentioned). `#24` co-sourced or managed tax operations on a provider's AI
  platform, with AI-use due diligence on providers (delegate; survey evidence only).

**Covered in other tax modules (cross-references, not duplicated):** ledger-to-tax mapping in compliance
(`tax-compliance-corporate-01`), PwC K-1 agents (`tax-compliance-corporate-02`), Oxford Industries' governed
reconciliation (`tax-compliance-corporate-10`), effective-rate modelling (`tax-compliance-corporate-14`), approved
enterprise tools (`tax-compliance-corporate-20`), deterministic engines with a model layer
(`tax-compliance-individual-business-10`, `tax-compliance-corporate-22`), e-invoice rejection handling
(`tax-indirect-tax-08`), engines callable by agents (`tax-indirect-tax-16`), notice triage (`tax-controversy-01`).

## 4. Interview probes

1. **Which system holds tax's single source of financial data, who owns its models and mappings, and what happens
   to them in an ERP upgrade?** Shows whether `#01` exists or tax still extracts by hand, and whether `#04` applies.
2. **Pick one number on a return, provision or real-time submission. Can you trace it to its source field today,
   and how long does that take?** Tests lineage, the record rules in Rev. Proc. 98-25 [IRS-REVPROC-9825] and `#02`.
3. **How many automations does tax run (Alteryx, Power Platform, scripts, agents)? How many have an owner,
   documentation, version history and a review step? What happened when a builder last left?** Reveals key-person
   risk and readiness for `#07` and `#08` [TEI-TAXTECH-2026].
4. **Who decides which AI tools tax may use, and how long do IT approval and data-protection review take?** In
   Germany these are the top hurdles (47% and 41%) [KPMG-DE-2026].
5. **Who owns AI in tax: tax, IT or finance? Is there an inventory and a policy?** Only 2 of 50+ TEI attendees said
   tax [TEI-TAXTECH-2026]; 45% of departments had no relevant policy [TR-TENSIONS-2025]. Points to `#20`.
6. **What accuracy or override rate did you set before go-live, and what do you measure now?** No source measures this; as a proxy, only 12.5% of indirect tax leaders in Fonoa's survey have AI targets or KPIs [FONOA-2026] (`#21`).
7. **When an agent or pipeline changes a number or mapping, where is it logged, who approves it, and is the fix
   written back to the source system?** Tests `#19` and Deloitte's write-back point [DELOITTE-TTT-2026].
8. **In each clearance or real-time reporting country, what is your rejection rate, how many causes are master
   data, and who fixes them how fast?** Sizes `#13` and `#14`; shows whether ViDA has one owner [TR-VIDA-2026].
9. **What would the authority see about your transactions before an audit that you cannot see yourself?** A panel speaker said that in mature continuous-transaction-control regimes authorities arrive at audits knowing more than the company [TRINST-TEIAUDITOR-2026]. Gauges interest in `#16`.
10. **If an agent can call your tax engine, which scopes does it hold, where are tool calls logged, and who reviews
    them?** Separates `#17` (read-only) from `#18` (agents that act) and tests the controls in [AVALARA-MCP-2026].
11. **What have you budgeted for model and token costs against measured time saved?** The TEI recap lists rising token costs as a problem; no source gives figures [TEI-TAXTECH-2026].
12. **Which work do outside providers do with AI on your data, and do you know how?** Thomson Reuters reports that 59% "aren't sure if their companies are using GenAI" and presents it as a provider-transparency gap [TR-TENSIONS-2025]. Relevant to `#24`.

## 5. Metrics and benchmarks

What to measure: hours spent extracting and preparing data before tax work starts; share of tax data with
documented lineage to source; number of automations with an owner, documentation and version history; pipeline
build and change lead time; reconciliation cycle time and exceptions; e-invoice rejection rate and causes; AI
accuracy, override rate and drift; share of AI-assisted decisions with an audit trail; token and run cost per
process. None has a published benchmark for AI in tax data work.

| Figure | What it counts | Source and caveat |
|---|---|---|
| 51%; 44% | Tax and finance functions early in data management maturity; naming the inability to execute on a sustainable data, AI and tech plan as the biggest barrier (1,600 leaders) | [EY-TFO-2025]; firm survey |
| 80%; 91% | See insufficient AI-ready data as a significant barrier; data in too many silos | [BTAX-EYTFO-2026]; write-up of the EY survey, not on EY's release |
| 53% to 21% | Time on routine work now, and the share respondents would like | [BTAX-EYTFO-2026] |
| 58% (51% a year earlier) | Corporate tax departments calling themselves under-resourced | [TR-CORPTAX-2025]; vendor survey |
| 15.4% | Average share of tax department budget spent on technology and software | [TR-CORPTAX-2025] |
| 88% (from 51%); 22% | Departments with a designated tax technology lead; tracking no technology metrics (170 leaders) | [TR-REBRAND-2026] |
| 71%; 89% / 29%; 66% | German departments using AI; using company-wide tools / tax-specific tools; users reporting time savings | [KPMG-DE-2026]; sample not stated |
| 12.5%; 57.4% | Indirect tax leaders with AI KPIs; not confident AI-assisted decisions would survive an authority challenge (176) | [FONOA-2026]; vendor survey, adjacent process |
| 77% | Tax leaders requiring 90%+ accuracy before entrusting AI with tax processes | [DELOITTE-LU-2025]; sample not stated |
| 17% / 21% / 45% | Departments with an AI policy / covered by general policy / no relevant policy | [TR-TENSIONS-2025] |
| 86%; 22% | Familiar with ViDA; with a formal transition programme | [TR-VIDA-2026]; sample not stated |
| 80%; 50% | Rover, as reported by Savant: less month-end close time; lower data handling cost | [SAVANT-ROVER-2026]; vendor-published; what was timed is unclear |
| 1.6% vs ~20% | Sovos invoice rejection rate in France vs an unsourced market estimate | [SOVOS-FRANCE-2026]; AI share not stated |
| 87%; 41% | Automation users with some bot failures; maintenance heavier than expected (2019; 509 RPA users in five industries, none of them tax) | [PEGA-RPA-2019] |
| fewer than 1/3 | Simplified federal returns computed correctly by frontier models | [COLUMN-TAXCALCBENCH-2025]; vendor authors |
| over 5% | Rise in reported sales, purchases and VAT liabilities after e-invoicing, Peru | [BELLON-PERU-2022]; independent, regime-level |

Not found anywhere: error rates, override rates, parallel-run results or inspection findings for AI in tax data
pipelines, mappings, reconciliations or e-invoice interfaces; any figure for agent or token cost.

## 6. Guardrails

- **Records must reconcile and be documented.** Rev. Proc. 98-25: retained machine-sensible records must reconcile
  to the books and the return, carry transaction-level detail, be available to the IRS, and come with documentation
  of data flow, internal controls and field definitions [IRS-REVPROC-9825]. Whether it has since been modified was
  not checked.
- **Internal control over AI.** COSO's generative AI guidance (released 2026-02-23) maps risks to its framework, sets
  a six-step roadmap (govern, inventory, assess, design, implement, monitor) and treats ingestion, transformation and
  posting as capability types [JOFA-COSO-2026; DART-COSO-2026]. SOX-auditable solutions appear in job postings
  [FORTIVE-JOB-2026]. NIST's Generative AI Profile lists confabulation, data privacy and information integrity
  among the risks [NIST-AI600-1].
- **Real-time reporting law.** ViDA (Directive (EU) 2025/516): cross-border digital reporting from 2030-07-01,
  domestic systems aligned by 2035-01-01 [EC-VIDA-2026]. UK mandatory e-invoicing from 2029 [UK-EINV-2025].
  France: receipt from 2026-09-01; penalties from 10% of VAT due for late submissions [SOVOS-FRANCE-GOLIVE-2026].
  Two Thomson Reuters articles give different ViDA dates; use the Commission page.
- **Agent access.** MCP servers must not accept tokens not issued for them, and proxies must guard against the
  confused deputy problem [MCP-SPEC-2025]; vendor advice is least-privilege scopes, consent audits, logging every
  tool call and idempotent filings [AVALARA-MCP-2026]. NIST launched an AI Agent Standards Initiative on
  2026-02-17 [NIST-CAISI-2026].
- **Write-back.** Deloitte says agentic corrections to source data will need to be stored back in the system of record to keep an audit-ready posture [DELOITTE-TTT-2026].
- **Practitioner duties.** IRS OPR Alert 2026-19 applies Circular 230 duties to practitioners using AI (verify
  facts, citations and calculations; vet third-party tools) [IRS-OPR-2026]. It is addressed to practitioners before the IRS, not to in-house departments as such. The UK Senior Accounting Officer regime puts personal accountability on named executives for tax
  accounting arrangements [TR-GOVERNANCE-2026].
- **Risk frameworks, not standards.** The AICPA-published Werfel framework and register [AICPA-WERFEL-2026] and the
  AICPA's Council on AI Risk in Tax, launched 2026-09-23 [AICPA-CART-2026].

Steps that need human judgment: approving a pipeline or automation for production; approving master-data and
configuration changes with tax impact; resolving reconciliation and validation exceptions; approving any agent
correction before it executes; setting acceptance thresholds and acting on drift; granting agent scopes; signing
off data requirements for new business lines; owning each compliance decision and the evidence behind it.

## 7. Roles and how they evolve

- **Tax people as builders.** OpenAI, Snowflake, Fortive and Apple postings combine tax knowledge with SQL, Python,
  data modelling or ERP skills [OPENAI-USTAXOPSJOB-2026; SNOWFLAKE-JOB-2026; FORTIVE-JOB-2026; APPLE-JOB-2026]. The
  recap calls the high-end job "as much a data science problem as an accounting one" [TRINST-TEIAUDITOR-2026].
- **Preparer to reviewer.** OpenAI's 2026 posting says the role is "not a traditional tax role": more review,
  validation and building, less return preparation [OPENAI-USTAXOPSJOB-2026].
- **New owners.** Control owners approve promotion of automations to production [SAVANT-SPRING-2026]; Avalara addresses its scope and logging advice to developers and partners, and no source says who in tax owns agent access [AVALARA-MCP-2026]. PwC Ireland expects tax data leads and model governance leads
  [PWC-IE-2026]. 88% of departments now name a tax technology lead [TR-REBRAND-2026].
- **Hiring and skills.** 73% prioritise hiring data scientists and tax technology experts; 89% upskill existing
  staff [EY-TFO-2025]. 45% name AI skills as their greatest need in one to two years [DELOITTE-LU-2025].
- **Headcount.** 58% of German respondents expect stable domestic tax headcount, 72% abroad [KPMG-DE-2026]. Michael Sala argues in Tax Notes State that teams will not shrink much because AI cannot bear culpability (abstract only) [SALA-TAXNOTES-2026].
- **Change.** "You will not survive in this field if you don't have a change mindset", a senior director said
  [TEI-TAXTECH-2026]. A tool meant to save two hours took a day when users were not consulted [TEI-TAXTECH-2026].

## 8. Frontier

- **2025-06-23:** A2A (agent-to-agent protocol) contributed to the Linux Foundation [LF-A2A-2025].
- **2025-10-06:** Avalara announces MCP servers so third-party agents can call its APIs [AVALARA-AGENTIC-2025].
- **2025-10-08:** Deloitte Tax and Databricks alliance for a unified tax data architecture [DELOITTE-DATABRICKS-2025].
- **2025-11-18:** Vertex Configuration Agent for Dynamics 365 in the Microsoft Marketplace [VERTEX-CONFIGAGENT-2025].
- **2025-11-20:** Heads of 49 tax administrations in the OECD Forum on Tax Administration agree to deepen real-time information sharing and back pilot projects [OECD-FTA-STATEMENT-2025].
- **2025-12-09:** MCP moves to the Linux Foundation's Agentic AI Foundation [LF-AAIF-2025].
- **2026-02-23:** COSO releases generative AI internal-control guidance [DART-COSO-2026].
- **2026-03-24:** Sovos says it is developing an MCP gateway, with A2A expected over time [SOVOS-SOVI-2026].
- **2026-04 (seminar), 2026-05 (recaps):** TEI attendees describe regulators pulling ahead and roadmaps compressed
  to 12-18 month cycles [TRINST-TEIAUDITOR-2026]; most respondents shortened expected AI integration timelines to one
  to two years from three to five [TR-REBRAND-2026].
- **2026-05-27:** Avalara lists MCP servers across its product stack [AVALARA-MCP-2026].
- **2026-07:** Deloitte's four scenarios cross a department's AI adoption with its authority's [DELOITTE-TTT-2026].
- **2026-08-18:** Snowflake's tax posting describes replacing BI workflows with agents [SNOWFLAKE-JOB-2026].
- **2026-09:** France's e-invoicing mandate goes live [SOVOS-FRANCE-GOLIVE-2026]; Kintsugi ships a read-only MCP
  server (2026-09-18) [KINTSUGI-MCP-2026].
- **2026-10-01:** Sovos announces it has acquired Flowie, whose agents run finance processes on ERP systems
  (announced only) [SOVOS-FLOWIE-2026].
- **Ahead:** UK e-invoicing roadmap at Budget 2026 [UK-EINV-2025]; ViDA digital reporting from 2030-07-01
  [EC-VIDA-2026].

Direction: data layers and controls before agents; tax engines exposed to company agents; real-time reporting that
makes master data a legal-validity issue; "continuous audit controls" discussed but not built [INNOVATETAX-VXE-2026].

## 9. Common objections

- **"It fails quietly."** Attendees said AI fails "quietly and even politely" [TEI-TAXTECH-2026]. Response: verify
  extracted values against sources (`#11`), log decisions (`#19`) and track override rates (`#21`).
- **"Nobody owns it."** 2 of 50+ say tax owns AI [TEI-TAXTECH-2026]. Response: an inventory with named owners and
  escalation paths, as COSO recommends (`#20`) [DART-COSO-2026].
- **"Analysts will build things nobody can maintain."** True for some Alteryx estates [TEI-TAXTECH-2026] and
  unreviewed AI-built pipelines [TRINST-TEIAUDITOR-2026]. Response: allow the build, require review, documentation
  and sign-off before production (`#07`, `#08`).
- **"Our data isn't ready."** 80% call insufficient AI-ready data a significant barrier [BTAX-EYTFO-2026].
  Response: that is the first use case (`#01`, `#02`), not a reason to wait.
- **"Probabilistic AI can't do deterministic compliance."** Raised in the EY write-up [BTAX-EYTFO-2026]; models got
  fewer than a third of simple returns right [COLUMN-TAXCALCBENCH-2025]. Response: keep calculation in the engine;
  use AI for data, mapping, monitoring and documentation (`tax-compliance-individual-business-10`).
- **"We can't defend AI decisions to an authority."** 57.4% say so [FONOA-2026]. Response: a BDO partner quoted by
  Fonoa says the task is demonstrating a process, not defending a technology; build the trail (`#19`).
- **"Token costs will kill the case."** Raised at TEI, with no figures anywhere [TEI-TAXTECH-2026]. Response:
  only 20% of organisations across professional services measure ROI [TR-TENSIONS-2025]; set baselines first (`#21`).
- **"The authority will see it first anyway."** A panel speaker said that in mature CTC regimes authorities arrive knowing more than the company;
  padding numbers with a safety margin and accepting the audit drew "Do not do this" [TRINST-TEIAUDITOR-2026].
  Response: validate before submission and reconcile continuously (`#13`, `#16`).
- **"Vendors' governance claims are untested."** Correct: no auditor test was found [SAVANT-SPRING-2026]. Response:
  ask for evidence logs and test them yourself.

## 10. Sources

Full details for every key used in the use cases are in the YAML. Keys cited here that are not in the YAML:

- [SOVOS-FLOWIE-2026] Sovos, Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance
  Orchestration Platform, 2026-10-01, https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/
- [AICPA-CART-2026] The Tax Adviser, AICPA, former IRS commissioner to lead initiative on AI in tax, 2026-09-23,
  https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
- [NIST-AI600-1] NIST, AI Risk Management Framework: Generative AI Profile (NIST AI 600-1), 2024-07,
  https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

Most-used keys: TEI-TAXTECH-2026 and TRINST-TEIAUDITOR-2026 (Thomson Reuters Institute recaps of the April 2026
TEI seminar; vendor-owned), SNOWFLAKE-JOB-2026 and OPENAI-* (job postings), SAVANT-* (Savant releases), AVALARA-MCP-2026
and SOVOS-SOVI-2026 (vendor MCP and AI announcements), EY-TFO-2025 and BTAX-EYTFO-2026 (EY survey), TR-CORPTAX-2025,
TR-TENSIONS-2025 and TR-REBRAND-2026 (Thomson Reuters surveys), FONOA-2026, KPMG-DE-2026, DELOITTE-TTT-2026 (scenarios),
DART-COSO-2026 (COSO), IRS-REVPROC-9825.
