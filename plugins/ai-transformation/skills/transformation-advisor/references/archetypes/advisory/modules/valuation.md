# Valuation (advisory)

Sources checked 2026-10-20; re-checked 2026-10-21. Use cases live in `../use-cases/valuation.yaml` (15 entries).
Ids are shortened here: `#05` means `advisory-valuation-05`; other modules' ids are given in full. Source keys in
brackets, such as [IVSC-IVSED-2026], are in the YAML or in §10. **Read this first: the standards track is rich, the
practice evidence is thin.** No entry is graded A; 3 of 15 are B, resting on named deployments with no published
measurement. No error rate, override rate, parallel run or inspection finding on AI-assisted valuation exists. Every
speed figure is vendor-published or a firm's own claim. The only US accounting firm found describing its own
valuation AI use is CohnReznick (`#15`, a press release). Say so when you quote a figure.

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

Business and asset valuation done by accounting firms, independent valuation firms and in-house teams: valuations for
transactions, disputes and owners; fair value for financial reporting (purchase price allocation, or PPA, which
splits a deal price across acquired assets; impairment testing; Level 3 instruments, valued from unobservable
inputs); recurring portfolio and fund marks; and writing and defending the report. The defining feature is a fast-moving
standards track (IVSC, Appraisal Foundation, AICPA) that keeps the valuer responsible for any AI output. Expert
testimony and damages are in forensic-disputes; quality of earnings is in transactions; how auditors use valuation
specialists is in `assurance-specialists-*`; estate, gift and 409A tax valuations route to tax; the firm's own pricing,
staffing and ownership are in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scoping and acceptance | Purpose, standard of value, scope of work (IVS 101); independence screen for attest clients | document-production, coordination-scheduling | The IVSC draft would add significant AI use to the scope of work [IVSC-IVSED-2026]; SEC audit-client restriction [SEC-RULE2-01-2026] |
| Data intake and normalization | Financials, tax returns, management data, normalizing adjustments | data-reporting, transaction-processing | The IVSC draft adds a section on use of management or client data to IVS 104 [IVSC-IVSED-2026] |
| Market and comparables research | Transactions, guideline companies, multiples, control premiums, marketability discounts (DLOM) | research-synthesis | Manual research for multiples and discount rates is a time drain for small teams [VALUTICO-KRESTON-2025] |
| Modelling and conclusion | Discounted cash flow (DCF), market approach, discount-rate build-up, reconciling methods | expert-judgment | Management forecasts are an inspection theme [BVR-PCAOBINSP-2026]; the draft IVS 200 adds a calibration section [IVSC-IVSED-2026] |
| Fair value for financial reporting | PPA, impairment, Level 3 measurements, reviewed by the auditor | expert-judgment | PCAOB inspections of the six largest audit firms flagged impairment, DCF and Level 3 work [BVR-PCAOBINSP-2026]; a specialist's work is often not entirely transparent to the auditor [PCAOB-SPECIALISTS-2025] |
| Report drafting and quality control | Report assembly, narrative, internal review | document-production, review-assurance | Very long reports, 200 pages in one case [VALUTICO-RXM-2025]; template defaults [AICPA-FVSHOME-2026]; new IVS 107 quality controls [IVSC-IVSED-2026] |
| Defence of the work | Auditor testing, tax examination, cross-examination, client challenge | review-assurance, client-interaction | Clients now run AI over valuers' reports [BVR-NACVA-2026]; prompts may be discoverable [BVR-DISCOVERY-2026] |
| Portfolio and fund valuation cycles | Recurring marks, monitoring, scenario analysis | data-reporting | Bespoke spreadsheets, back offices that did not grow with fund size [STOUT-TECH-2024; S73-HAMLANE-2025] |

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path,
exceptions to people), delegate (an agent owns a multi-step outcome), reinvent (the service or model changes).
**Automate has no evidence in this module.** Delegate has one vendor claim (`#12`). PPA, impairment testing and
fairness opinions have no deployment evidence: the only touchpoints are KPMG naming attrition analysis among its AI
uses and Big Four panellists naming ASC 360 impairment among areas needing fresh guidance [BVR-KPMGTREND-2026;
BVR-BIG4GUIDANCE-2026, summary only].

**Research, comparables and technical knowledge**
- Improve: `#01` KPMG says it is working to embed AI across information requests, technical research, volatility and
  attrition analysis and comparable-company screening (Big Four, trade-press report of a panel). `#02` BVR's
  plain-language agent over transaction and discount datasets, with drill-through to the deals (vendor). `#03` Kreston
  Reeves and Rouse (UK accounting firms) research multiples and discount rates on Valutico; Rouse estimates a third
  off project time (vendor case study; AI use not stated, so grade C). `#04` a grounded assistant over BVR's technical
  library, with juniors sent there first and seniors reviewing how they applied the concept (vendor tip).

**Modelling and projections**
- Improve: `#05` AI inside Excel builds models, audits formulas and runs sensitivities (vendor claims; the 83% figure
  is a general Excel benchmark). `#06` idea: a specialist model forecasts full statements up to 20 quarters ahead and
  beat frontier LLMs on a benchmark (preprint). `#07` idea: LLM property price estimates, overconfident in their
  intervals (preprint; adjacent asset class).

**Report drafting and review**
- Improve: `#08` template-driven report generation at RXM (Singapore) and PKF FI (France); RXM says a 200-page report
  went from months to days (vendor case study; AI use not stated, so grade C). `#09` generative AI drafts sections
  such as market commentary, which the IVSC says some valuers already do (no firm named). `#10` reviewer agents check
  a valuation or report against standards, methodology and the firm's review policy (practitioner idea plus a vendor
  template; no named user). `#11` idea: write and defend reports expecting clients to run AI critiques of them.
- Related: `assurance-specialists-04` (audit-side QC review of valuation reports); `advisory-forensic-disputes-07`
  (verification protocol for expert work); `professional-services-quality-review-02` (citation checks before signing).

**Production end to end (delegate)**
- `#12` AI-native vendors claim documents-to-model-report-and-deck in hours or minutes (directory profile and a home
  page; no customers named). Related: `assurance-specialists-05` (idea: agents build complete valuation models).

**Portfolio and fund valuation (process and model change)**
- Improve (process): `#13` Hamilton Lane (an in-house investment manager, and an investor in the vendor) standardized
  valuations on 73 Strings' AI-assisted platform; qualitative statements only. `#15` CohnReznick's valuation practice
  builds 73 Strings' AI-enabled analytics into its methodology for fund clients (firm release; no figures; also
  `assurance-specialists-02`).
- Reinvent: `#14` independent valuation firms sell recurring valuation as an AI-enabled platform with their opinions
  inside the workflow (Stout Drivr; Kroll REVS for real estate). Announcements; no customers or figures.
- Disputes: `advisory-forensic-disputes-06` covers sandboxed LLM use in IP damages and valuation disputes.

## 4. Interview probes

1. Which valuation steps use AI today (comparables screening, data normalization, drafting, review), and what goes in
   the engagement file? How would you decide whether your use is "significant" under the IVSC draft? *Reveals
   readiness for the proposed disclosure and documentation duties [IVSC-IVSED-2026].*
2. When a tool returns comparables or data, who opens the underlying transactions, and have you tracked how often a
   reviewer changed the AI-assisted result? *No override rate is published anywhere; this tests whether any claim of
   value could be shown (`#02`, `#03`) [BVR-RADATIP-2026].*
3. Are your valuation tools generative AI, rule-based automation or a data platform, and which carry the risk of
   invented output? *Vendor branding blurs this (`#03`, `#08`); the answer sets the review design.*
4. Can each analyst rebuild the key numbers without the tool, and do you re-run a calculation to check it is
   repeatable? *In Weber the court re-ran the expert's Copilot queries and got different numbers [GOLDMAN-WEBER-2024].*
5. As mechanical work moves to AI, how do juniors learn the method, and has your hiring or training plan changed?
   *Big Four panellists report fewer entry-level hires [BVR-KPMGTREND-2026]; see `#04`.*
6. Have clients, auditors or opposing experts challenged a report with AI, and what does your engagement letter say
   about AI use? *Shows exposure to `#11` and to discovery of prompts [BVR-NACVA-2026; BVR-DISCOVERY-2026].*
7. Which tools may touch client financials, on which plan tier, and do you ask whether client consent is needed?
   *Tests the confidentiality question the AICPA Code raises [JOFA-ETHAI-2026; BVR-AICPAREPORT-2026].*
8. For clients you also audit, or whose results go into an audit, which valuation services are off the table, and who
   checks before acceptance? *Valuation for SEC audit clients is restricted [SEC-RULE2-01-2026]; the SEC staff apply a
   rebuttable presumption that it will be subject to audit procedures [PWC-SECFAQ-2019].*
9. Do you sell recurring valuation (fund marks, portfolio monitoring), and could you package it with a platform as
   Stout and Kroll announced? *Tests appetite for `#14` and the in-house alternative (`#13`).*
10. How do your fair-value reports hold up to auditor challenge on assumptions and data today, before any AI?
    *PCAOB findings are the baseline AI will be judged against [BVR-PCAOBINSP-2026].*
11. Does your firm or an affiliate have outside investors, and has that changed which valuation services you can
    offer audit clients? *Routes to professional-services; PE platforms are buying valuation niches
    [CPATRENDLINES-TRACKER-2026].*

## 5. Metrics and benchmarks

| Metric | Figure | Provenance | Source |
|---|---|---|---|
| AI-assisted valuation error, override or parallel-run rate | None found | none | gap |
| Project time, comparables research (Rouse) | About a third less; up to a day per project | vendor-published (firm estimate) | [VALUTICO-ROUSE-2025] |
| Report production, 200-page valuation (RXM) | Months to days; "hundreds of hours" | vendor-published (recollection) | [VALUTICO-RXM-2025] |
| Valutico boilerplate | "3-5 times faster"; "over 90% of users" report time savings; basis not stated | vendor-published | [VALUTICO-PKFFI-2025] |
| Comparables analysis (RADA) | "hours into seconds"; no method | vendor-published | [BVR-RADAPRODUCT-2026] |
| Portfolio valuation (Stout Drivr) | "hours or days, not weeks" (expectation) | self-reported | [STOUT-DRIVR-2026] |
| Excel agent on complex Excel tasks (general, not valuation) | 83%; 5 of 7 Financial Modeling World Cup levels | vendor-published | [ANTHROPIC-FS-2025] |
| Finance Agent benchmark, Claude Opus 4.7 (general) | 64.37% | vendor-published | [ANTHROPIC-FSAGENTS-2026] |
| Practitioner sentiment (BVR polls) | 73% say AI will "significantly" change their work, usage low (2025; sample not visible); 2026 poll "insane" pace, no figures visible | survey (summary only) | [BVR-POLLS-2025; BVR-POLL-2026] |
| IVSC Valuation Pulse sentiment tracker | Opened 2026-05-08; results not published | survey | [IVSC-PULSE-2026] |
| Long-horizon statement forecasting | Specialist model beat frontier LLMs, gap widening with horizon; no numbers in abstract | independent (preprint) | [ARXIV-FORMA-2026] |
| LLM property price estimates | Traditional ML more accurate; LLMs overconfident in intervals | independent (preprint) | [ARXIV-REAPPRAISAL-2025] |
| Repeatability of a chatbot calculation | Court re-ran Copilot and got different numbers | independent (court, via blog) | [GOLDMAN-WEBER-2024] |
| Baseline quality before AI | PCAOB reports for BDO, Deloitte, EY, Grant Thornton, KPMG and PwC flagged assumptions, data and over-reliance on company specialists; no counts | independent (via trade press) | [BVR-PCAOBINSP-2026] |
| Clients asking for proof of AI data protection (all accounting work) | Three in five respondents say always or frequently (n=725) | vendor-published | [INTUIT-ACCTTECH-2026] |

What to measure if a firm pilots: reviewer change rate on AI-retrieved comparables and inputs; hours per report
section before and after; repeatability of key numbers across runs; share of engagements where AI use is recorded
in the file. None of these is published by anyone yet.

## 6. Guardrails

**IVSC exposure draft (not final).** Would add mandatory requirements on significant use of AI or other
technology-based tools to IVS 101 scope of work, IVS 104 data and inputs, IVS 105 models and IVS 106 documentation and
reporting, plus a new quality-controls chapter (IVS 107). Significant use would be disclosed in the scope of work and
the report and documented in the engagement file, with the quality controls applied. It targets opaque tools whose
reasoning the valuer cannot readily explain or verify. Final text planned 2027-01-31, effective 2028-01-31, subject to
responses [IVSC-IVSED-2026; BVR-IVSPODCAST-2026]. Consultation responses were not retrieved.

**IVS in force now.** The IVSC paper says a model using AI cannot produce an IVS-compliant valuation without the
valuer's professional judgement; it may be used as a tool if the valuer understands its design and limits
[IVSC-AI-2025].

**USPAP.** The Appraisal Standards Board adopted Advisory Opinion 41 on 2026-04-23: no new requirements, but it
clarifies competency, confidentiality, scope of work, workfile and reporting duties when appraisers use AI. The
appraiser remains responsible for judging whether output is accurate, relevant and appropriate [BVR-AO41ADOPT-2026;
ISA-AO41-2026].

**AICPA.** The FVS Executive Committee's October 2025 guidelines are members-only and non-authoritative: reminders on
engagement terms, confidentiality and judgment [BVR-AICPAAIGUIDE-2025]. One practitioner, James Ewart, argues there
will be no separate "AI standards"; existing NACVA, AICPA, ASA, USPAP and IVS duties apply [BVR-EWART-2026]. The
proposed Valuation Performance Framework (AICPA, ASA, RICS) takes comments to 2026-12-22; the coverage read does not
mention AI [ACCTODAY-VPF-2026].

**Independence (where the firm also audits the client).** Appraisal, valuation and fairness-opinion services impair
independence for an SEC-registrant audit client unless it is reasonable to conclude the results will not be subject to
audit procedures [SEC-RULE2-01-2026]. The SEC staff apply a rebuttable presumption that it will be, materiality does
not overcome it, and there is no cure for prohibited services in a prior period [PWC-SECFAQ-2019]. Developing or
hosting an AI system for an attest client can raise independence concerns [JOFA-ETHAI-2026]. AICPA treatment of
valuation for private-company attest clients was not confirmed from the sources: confirm per engagement. Related:
`assurance-acceptance-independence-15`.

**Lenders.** For SBA change-of-ownership loans, a vendor (QoEAgent) quotes the SBA rule barring a valuation prepared
for the applicant or seller, with no dollar threshold [QOEAGENT-WHO-2026]; see `advisory-transactions-07`.

**Courts and discovery.** In Matter of Weber (N.Y. Surrogate's Court, 2024) the court found an expert's testimony not
credible, got different numbers when it re-ran his Copilot queries, and required counsel to disclose AI use
[GOLDMAN-WEBER-2024]. Panellists say experts should expect questions on which tools they used and how outputs were
verified, and that prompts and drafts could be discoverable in some circumstances [BVR-DISCOVERY-2026]. A federal
court in Michigan (Warner v. Gilbarco) held a plaintiff's ChatGPT material was protected work product, in contrast to
Heppner [BVR-WARNER-2026]. The evidence committee voted to withdraw proposed Rule 707 (machine-generated evidence) as
published and submit a modified proposal for further study [USCOURTS-EVID-2026]; detail is in forensic-disputes.

**Confidentiality.** Ask whether client consent is needed before client data goes into an AI tool
[JOFA-ETHAI-2026]. Keep confidential client information out of public AI systems [BVR-AICPAREPORT-2026]; the IVSC
flags open or closed AI without safeguards as a confidentiality risk [IVSC-AI-2025].

**Steps that need human judgment:** selecting comparables and inputs [IVSC-AI-2025; BVR-RADATIP-2026];
setting projection and scenario assumptions [BVR-PCAOBINSP-2026]; reconciling methods and the conclusion of value;
deciding on each reviewer-agent flag [BVR-AICPAREPORT-2026]; signing and defending the report, where the valuer
stays responsible [ISA-AO41-2026; BVR-ENDICOTT-2026].

## 7. Roles and how they evolve

- Speakers at a Big Four panel said firms hire fewer entry-level analysts as AI automates mechanical work, raising the
  question of how future valuers will be trained [BVR-KPMGTREND-2026]. See `assurance-specialists-01` for the 2025 and
  2026 Big Four panels and `professional-services-talent-learning-07` for redesigned entry-level roles.
- Roger Grabowski told NACVA attendees AI will not replace judgment and could free analysts from mechanical work to
  understand businesses and advise clients [BVR-NACVA-2026].
- Greg Endicott: "AI literacy" is becoming a required skill, and the signing valuer remains responsible
  [BVR-ENDICOTT-2026].
- An ASA session abstract says value is shifting toward interpretation, judgment and accountability, and asks how the
  next generation builds critical thinking once gained through repetition (abstract only) [ASA-ASAIC26-2026].
- A NACVA panel warned of "cognitive debt": overreliance may erode the skills needed to spot AI errors
  [BVR-COGDEBT-2026]. BVR suggests juniors use its assistant first, then seniors review the application (`#04`).
- A BVR staffing webinar frames the future team as domestic, international and AI team members (summary only)
  [BVR-TRAINSTAFF-2025]. A recruiter's view in April 2026 is that experienced talent is still short and AI had limited
  impact [BVR-APRILPREVIEW-2026].
- Stout describes control of portfolio valuation moving from deal teams to a central valuation team as the process
  is automated (automation, not AI) [STOUT-TECH-2024].

## 8. Frontier

- **2025-07-23:** IVSC paper says some valuers already use AI in data processing and report writing
  [IVSC-AI-2025].
- **2025-10:** AICPA FVS committee issues AI guidelines [BVR-AICPAAIGUIDE-2025].
- **2026-01-07 to 2026-04-23:** AO-41 exposed, then adopted [BVR-TAFAO41-2026; BVR-AO41ADOPT-2026].
- **2026-01-31 to 2026-04-30:** IVS exposure draft consultation; final planned 2027-01-31, effective 2028-01-31
  [IVSC-IVSED-2026].
- **2026-03-03 and 2026-03-26:** Kroll announces REVS (`#14`) [KROLL-REVS-2026]; CohnReznick says its valuation
  practice has built in 73 Strings' AI-enabled analytics (`#15`) [COHNREZNICK-VALUATION-2026].
- **2026-04:** a deal tracker reports EisnerAmper buying KLG Business Valuators & Forensic Accountants and reads this
  as PE-backed platforms buying valuation and forensic niches [CPATRENDLINES-TRACKER-2026]. Ownership routes to
  professional-services.
- **2026-05-05 and 2026-05-19:** Anthropic lists a valuation-reviewer agent template (`#10`); KPMG and Anthropic
  announce Claude access for 276,000+ people [ANTHROPIC-FSAGENTS-2026; ANTHROPIC-KPMG-2026].
- **2026-06 (summaries only):** BVR write-ups describe firms moving from experimenting to integrating AI into research,
  workflows and practice management [BVR-EXPERIMENT-2026].
- **2026-06-10:** BVWire reports Big Four panellists calling AI part of everyday valuation work [BVR-KPMGTREND-2026].
- **2026-06-25:** IVSC dialogue panel says governing the technology may now be harder than adopting it
  [BVR-IVSCDIALOGUE-2026].
- **2026-07-14:** Stout launches Drivr (`#14`) [STOUT-DRIVR-2026].
- **2026-09-16:** BVR extends its research agent to four more valuation datasets (`#02`) [BVR-RADAEXPAND-2026].
- **2026-09-24:** 73 Strings acquires Callisto and says it will make its valuation platforms reachable by agents via
  the Model Context Protocol (a standard way for agents to call tools), with a deterministic core engine
  [S73-CALLISTO-2026].
- **2026-10-04 to 06 (abstracts only):** ASA International Conference sessions on AI ethics, AI in valuation and the
  "Firm of the Future" [ASA-ASAIC26-2026; BVR-ASACONF-2026].
- **Scheduled, not yet given:** AICPA FVS Conference 2026-11-04 to 06, including FVC2640 "Valuation in an AI World"
  and FVC2631, a "MythBusters" session with items on AI disclosure language in business valuation reports and on
  public-company AI disclosure suits [AICPA-FVS-2026]. Valuation Performance Framework comments due 2026-12-22
  [ACCTODAY-VPF-2026].

## 9. Common objections

| Objection | Evidence-based response |
|---|---|
| "AI can't be trusted with numbers." | Partly right for chatbots doing arithmetic: in Weber a court re-ran an expert's Copilot queries, got different numbers and questioned their reliability [GOLDMAN-WEBER-2024], and LLMs trailed specialist models in forecasting and price estimation (`#06`, `#07`). Use deterministic engines for calculations, as 73 Strings describes [S73-CALLISTO-2026], and keep AI to retrieval, drafting and review with checks. |
| "Hallucinations make it unusable." | A practitioner view is that most are preventable through design, source checks and review, and that information overload is the bigger problem [BVR-ENDICOTT-2026]. Grounded tools that show the underlying transactions (`#02`) make checking practical [BVR-RADATIP-2026]. |
| "Clients' data can't go into AI." | Answer the consent question first [JOFA-ETHAI-2026] and keep confidential information out of public tools [BVR-AICPAREPORT-2026]; the IVSC names safeguards as the issue, not AI as such [IVSC-AI-2025]. |
| "The standards will forbid it." | A practitioner view is that existing duties apply and no separate AI standards are coming [BVR-EWART-2026]. AO-41 adds no requirements [BVR-AO41ADOPT-2026]. The IVSC draft asks for disclosure, documentation and quality controls, not a ban [IVSC-IVSED-2026]. |
| "Black-box tools will fail review." | The IVSC draft targets exactly that: tools whose reasoning the valuer cannot explain [BVR-IVSPODCAST-2026]. Choose tools with traceable, source-linked output [STOUT-DRIVR-2026; S73-CALLISTO-2026]. |
| "Everyone using the same tools will think alike." | An "algorithmic monoculture" concern is raised in BVR's coverage (summary only) [BVR-MONOCULTURE-2026]; no evidence either way. Keep independent judgment on selection and conclusions. |
| "Clients will just ask ChatGPT to value the business." | Clients already use AI to attack valuers' assumptions [BVR-NACVA-2026]. Speakers advise expecting it, asking for the client's prompt and output, and replying with evidence (`#11`). |
| "AI will hollow out our juniors." | A real concern for panellists and the NACVA "cognitive debt" session [BVR-KPMGTREND-2026; BVR-COGDEBT-2026]. Design review of AI output into training (`#04`; `professional-services-talent-learning-07`). |
| "The vendor says 3-5x faster." | That wording is repeated across case studies with no stated basis [VALUTICO-PKFFI-2025]. The most specific firm figure is Rouse's own estimate of a third [VALUTICO-ROUSE-2025]. Measure your own. |
| "We'll sell valuations to our audit clients more cheaply with AI." | Tooling does not change the SEC restriction on valuation for audit clients whose results will be audited [SEC-RULE2-01-2026]. |

## 10. Sources

Full details for these keys are in the YAML: AICPA-FVSHOME-2026, AICPA-FVSPODCAST-2026, ANTHROPIC-FS-2025,
ANTHROPIC-FSAGENTS-2026, ANTHROPIC-KPMG-2026, ARXIV-FORMA-2026, ARXIV-REAPPRAISAL-2025, ASA-ASAIC26-2026,
BVR-AICPAREPORT-2026, BVR-BIG4PANEL-2026, BVR-COGDEBT-2026, BVR-DISCOVERY-2026, BVR-ENDICOTT-2026,
BVR-IVSCDIALOGUE-2026, BVR-IVSPODCAST-2026, BVR-KPMGTREND-2026, BVR-NACVA-2026, BVR-PCAOBINSP-2026,
BVR-RADAEXPAND-2026, BVR-RADAJUNIOR-2026, BVR-RADAPRODUCT-2026, BVR-RADATIP-2026, BVR-TRAINPRACTICAL-2025,
BVR-TRAINWORKSNOW-2025, COHNREZNICK-VALUATION-2026, CPAPA-COHNREZNICK-2026, DEALGAUGE-STARTUPHUB-2026,
GOLDMAN-WEBER-2024, HAMILTONLANE-VALTECH-2025, ISA-AO41-2026, IVSC-IVSED-2026, IVSC-AI-2025 (the key
`assurance-specialists-*` also uses), KROLL-REVS-2026, S73-CALLISTO-2026, S73-HAMLANE-2025, S73-HOME-2026,
SEC-RULE2-01-2026, STOUT-DRIVR-2026, STOUT-TECH-2024, VALUTICO-HOME-2026, VALUTICO-KRESTON-2025, VALUTICO-PKFFI-2025,
VALUTICO-ROUSE-2025, VALUTICO-RXM-2025. AICPA-FVS-2026 (the conference agenda, source of the FVC2631 and FVC2640
session codes) is in full in `../use-cases/forensic-disputes.yaml`; AICPA-FVSHOME-2026 is the conference home page.

Cited here only:
- ACCTODAY-VPF-2026: Accounting Today, "AICPA proposes valuation framework", 2026-10-13. https://www.accountingtoday.com/news/aicpa-proposes-valuation-framework
- BVR-AICPAAIGUIDE-2025: BVWire, "AICPA issues AI usage guidelines for valuation and forensic work", 2025-10-15. https://www.bvresources.com/articles/bvwire/aicpa-issues-ai-usage-guidelines-for-valuation-and-forensic-work
- BVR-AO41ADOPT-2026: BVWire, "ASB adopts AO-41 on the use of technology in appraisal", 2026-04-29. https://www.bvresources.com/articles/bvwire/asb-adopts-ao-41-on-the-use-of-technology-in-appraisal
- BVR-APRILPREVIEW-2026: BVWire, "Preview of the April issue of Business Valuation Update", 2026-03-18. https://www.bvresources.com/articles/bvwire/preview-of-the-april-issue-of-business-valuation-update-031826
- BVR-ASACONF-2026: BVWire, "ASA conference spans traditional and emerging valuation issues", 2026-08-19. https://www.bvresources.com/articles/bvwire/asa-conference-spans-traditional-and-emerging-valuation-issues
- BVR-BIG4GUIDANCE-2026: Business Valuation Update, "Big Four Valuation Leaders Point to the Need for Fair Value Guidance", 2026-07 (summary only). https://www.bvresources.com/articles/business-valuation-update/big-four-valuation-leaders-point-to-the-need-for-fair-value-guidance
- BVR-EWART-2026: BVWire, "AI raises the bar for valuation standards compliance", 2026-04-01. https://www.bvresources.com/articles/bvwire/ai-raises-the-bar-for-valuation-standards-compliance
- BVR-EXPERIMENT-2026: Business Valuation Update, "From Experimentation to Integration: AI's Next Phase in Valuation", 2026-06 (summary only). https://www.bvresources.com/articles/business-valuation-update/from-experimentation-to-integration-ais-next-phase-in-valuation
- BVR-WARNER-2026: BVWire, "Court: ChatGPT use does not waive work-product protection" (Warner v. Gilbarco), 2026-05-20. https://www.bvresources.com/articles/bvwire/court-chatgpt-use-does-not-waive-work-product-protection
- BVR-MONOCULTURE-2026: Business Valuation Update, "Are We Headed for an 'Algorithmic Monoculture'?", 2026-08 (summary only). https://www.bvresources.com/articles/business-valuation-update/are-we-headed-for-an-algorithmic-monoculture
- BVR-POLLS-2025: Business Valuation Update, "Recent Polls Reveal AI Usage at BVFLS Firms", 2025-09 (summary only). https://www.bvresources.com/articles/business-valuation-update/recent-polls-reveal-ai-usage-at-bvfls-firms
- BVR-POLL-2026: Business Valuation Update, "BVR Poll: AI Adoption in Valuation Is Moving at an 'Insane' Pace", 2026-04 (summary only). https://www.bvresources.com/articles/business-valuation-update/bvr-poll-ai-adoption-in-valuation-is-moving-at-an-insane-pace
- BVR-TAFAO41-2026: BVWire, "TAF proposes new USPAP guidance on technology use", 2026-01-07. https://www.bvresources.com/articles/bvwire/taf-proposes-new-uspap-guidance-on-technology-use
- BVR-TRAINSTAFF-2025: BVR webinar, "Staffing the BVFLS Firm of the Future", 2025-10-16 (summary only). https://www.bvresources.com/articles/training-event-transcripts/staffing-the-bvfls-firm-of-the-future
- CPATRENDLINES-TRACKER-2026: CPA Trendlines, "CPA PE Deal Tracker" (data to 2026-05-31), 2026-06-09. https://cpatrendlines.com/2026/06/09/cpa-pe-deal-tracker-10-years-466-deals/
- INTUIT-ACCTTECH-2026: Intuit QuickBooks via CPA Practice Advisor, "The 2026 Accountant Technology Survey", 2026-07-02. https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807
- IVSC-PULSE-2026: IVSC with 73 Strings, "The Valuation Pulse: AI & Technology in Valuation Sentiment Tracker", 2026-05-08. https://ivsc.org/the-valuation-pulse-ai-technology-in-valuation-sentiment-tracker/
- JOFA-ETHAI-2026: Journal of Accountancy, "Accounting ethics in the age of AI", 2026-08-05. https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/
- PCAOB-SPECIALISTS-2025: PCAOB staff, "Spotlight: Considerations for Audit Firms Using the Work of Specialists", 2025-02. https://assets.pcaobus.org/pcaob-dev/docs/default-source/documents/use-of-specialist-spotlight.pdf
- PWC-SECFAQ-2019: PwC Viewpoint (SEC staff Audit Independence FAQs), "E. Non-audit services", updated 2019-06-27. https://viewpoint.pwc.com/dt/us/en/sec/sec_faqs/sec_faqs_US/auditor_independence_US/E-Non-audit-services.html
- QOEAGENT-WHO-2026: QoEAgent, "Who Can Prepare an SBA Quality of Earnings Report", 2026-09-05. https://qoeagent.ai/who-can-prepare-sba-quality-of-earnings/
- USCOURTS-EVID-2026: Advisory Committee on Evidence Rules, agenda book for the 2026-10-15 meeting, 2026-10. https://www.uscourts.gov/sites/default/files/document/2026-10_evidence_rules_agenda_book_9-23_final.pdf
