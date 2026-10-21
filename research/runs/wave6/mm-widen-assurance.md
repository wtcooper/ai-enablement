# Widen assurance for mid-market firms: quality-management, soc-attestation, assurance-over-ai

Researched 2026-10-21 (combined pass: practice, discourse, governance and evidence). Archetype: assurance (mid-market extension). Modules widened: `quality-management` (small-firm SQMS, peer review, PE and alternative practice structures), `soc-attestation` and `assurance-over-ai` (AICPA practice aid of 13 Oct 2026; AICPA and AIUC joint SOC 2 plus AIUC-1 offering of 19 Oct 2026).

Source keys follow `PUBLISHER-SHORT-YYYY`. Where the archetype's `sources.md` already uses a different key for the same document, section 5 gives the alias so the synthesis can merge them (for example `AICPA-AIPA-2026` = `AICPA-PA-2026`, `PEEC-APS-2026` = `JOFA-PEEC-2026`, `JOFA-PEER-2026` = `JOFA-PRB`).

## 1. Summary

- **No AI-related peer-review finding is public.** I found none in any place a finding could appear: the Tennessee Society of CPAs 2025 annual peer review report (424 firms), the table of contents of six AICPA Reviewer Alert editions (Oct 2025 to Sep 2026), the AICPA Peer Review Conference listing (Aug 2026), and the body of the August 2025 Journal of Accountancy article on the AICPA's quality-management resources. The only peer-review signal tied to technology is indirect: from May to June 2026 the AICPA told reviewers of SOC 2 practices to look at a firm's reliance on third-party SOC platforms, and said weak results there can point to a problem in the firm's system of quality management. Full texts of the Reviewer Alerts and of the AICPA's quality-management peer review report are behind a login, so absence is established for titles and public reports, not for member-only text.
- **Small-firm SQMS is the clock that makes AI governance a peer-review matter.** Firms had to have a system of quality management by 15 Dec 2025; the first annual evaluation falls due by 15 Dec 2026; the first peer reviews of work done under the new standards were expected to begin in 2026. The AICPA practice aid (13 Oct 2026, nonauthoritative) now tells firms to set quality-management policies for AI tools, but the primary document is member-only and only the AICPA release and trade-press summaries were read. No small-firm commentary on the practice aid was found.
- **The AICPA is moving to own assurance over AI.** Six days after the practice aid, the AICPA and AIUC announced a single CPA-led engagement that yields a SOC 2 report and an AIUC-1 certification. Pilots exist at "several CPA firms"; only PwC is named. Full launch is "expected" in early 2027. The one mid-market AIUC-1 accredited auditor found on a primary source is Schellman (described in its own release as a top-50 CPA firm). No measured result for the joint offering exists.
- **PE and alternative practice structures fund AI platforms, but no one has measured the quality effect.** Crowe (No. 12) and Eide Bailly (No. 18) were reported in June 2026 as taking PE money partly to invest in AI. The PCAOB said in Dec 2025 that its inspectors will focus on firms that have taken PE capital, and that it counted more than 90 significant PE-related deals since 2020. The only empirical study found is a 2024 registered-report proposal with no results. The AICPA's independence rewrite for these structures may be re-exposed in Oct or Nov 2026 and adopted in 2027, and one former PCAOB member warns it could catch AI-tool licensing.
- **Evidence grades.** 13 use cases: 0 grade A, 3 grade B, 6 grade C, 4 grade D (labelled ideas). Nothing in these modules has a measured quality outcome (no error rate, override rate or parallel-run result) for mid-market practice.

## 2. Use cases

Mid-market framing: each entry says which kind of firm the example comes from. Larger-firm or public-company examples are included only where they show what is reaching mid-market practice.

```yaml
# Use cases: assurance mid-market extension (quality-management, soc-attestation, assurance-over-ai)
# Ids are placeholders (-new-NN); the synthesis will renumber.
# Existing entries these extend or sit beside: assurance-quality-management-01, -05, -13, -14, -16, -24;
# assurance-soc-attestation-12 to -15; assurance-assurance-over-ai-03, -07, -13, -17 to -19.

- id: assurance-quality-management-new-01
  title: "Idea (standard-setter guidance): put AI tools into the firm's SQMS 1 risk assessment, responses and first annual evaluation, scaled for small and mid-size firms"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    US firms doing audits, reviews or attest work had to have a system of quality management (SQMS No. 1) by 15 Dec 2025
    and must first evaluate it within one year of implementation or by 15 Dec 2026. The AICPA's August 2025 article on
    its quality-management resources does not mention AI, and the firm-size risk libraries it describes were published
    before the October 2026 practice aid. Small and mid-size firms using AI tools therefore have no AI line in the
    generic starting material they were given.
  solution: >-
    The AICPA practice aid (13 Oct 2026) says audit firms should set quality-management policies and procedures for
    AI tools. Per Accounting Today's summary, for AI used to obtain audit evidence a firm may want to set who builds
    or buys tools, a process for authorising them, acceptable-use rules, and periodic revalidation and monitoring.
    A small or mid-size firm would add these as quality risks and responses in the risk-assessment document it already
    keeps, and cover them in the managing partner's annual evaluation conclusion. Whether the AICPA's size-specific risk
    libraries and template (member content) list AI risks was not checked.
  outcomes:
    - {lever: risk, description: "No outcome published. The practice aid is nonauthoritative guidance; no firm reports having done this", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: AICPA-AIPA-2026}
  prerequisites:
    - "A designed and implemented system of quality management with the managing partner holding ultimate responsibility (JOFA-QMRES-2025)"
    - "An inventory of AI tools in use, including features inside software the firm already buys"
  risks_and_guardrails:
    - "The practice aid is nonauthoritative (AICPA-AIPARES-2026); Accounting Today words the policy list as things a firm 'may want to implement' (AT-AICPAPA-2026)"
    - "The practice aid text is member-only; this entry rests on the AICPA release and trade-press summaries"
  human_checkpoints:
    - "Managing partner evaluates the system at least annually and concludes whether it gives reasonable assurance (JOFA-QMPR-2024)"
    - "Engagement partners understand the tools, confirm the firm approved them and check staff use them correctly (AICPA-AIPA-2026)"
  role_evolution: >-
    The managing partner carries explicit accountability for the system; engagement partners take on duties to
    understand and check AI tool use (AICPA-AIPA-2026; JOFA-QMPR-2024).
  evidence_grade: D
  sources:
    - {ref: AICPA-AIPA-2026, title: "AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "section 'Use of AI-related technological resources by audit firms', four bullets"}
    - {ref: AT-AICPAPA-2026, title: "AICPA releases practice guide for auditors dealing with AI", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai", date: "2026-10-14", access: full, locator: "paragraph beginning 'When auditors themselves use AI in an engagement'"}
    - {ref: JOFA-QMRES-2025, title: "AICPA unveils new QM resources to help firms meet Dec. 15 deadline", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2025/aug/aicpa-unveils-new-qm-resources-to-help-firms-meet-dec-15-deadline/", date: "2025-08-12", access: full, locator: "sections 'The evaluation of the system of quality management' and 'A deeper discussion of a QM system's 8 components'"}
    - {ref: JOFA-QMPR-2024, title: "How the new QM standards may affect peer review", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2024/dec/how-new-qm-standards-may-affect-peer-review.html", date: "2024-12-10", access: full, locator: "section 'Updated peer review standards'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea label: a standard-setter recommends it; no firm publication of a worked example was found. Extends
    assurance-quality-management-01 to -03 (large-firm certification and policy) to the SQMS 1 risk-assessment document
    that small and mid-size firms actually keep. Evaluation date wording is the JofA article's ("within one year of
    implementation or by Dec. 15, 2026").

- id: assurance-quality-management-new-02
  title: "AI-driven SQMS 1 and 2 quality-management platform: AI risk assessment, automated monitoring and remediation, EQR workflows (AuditFile QualityLink)"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Firms must keep a risk assessment, monitor controls, track remediation and document engagement quality reviews under
    SQMS Nos. 1 and 2. For a small or mid-size firm this is recurring administrative work done on top of engagements.
  solution: >-
    AuditFile (a cloud audit-automation vendor) announced QualityLink on 4 Dec 2025. The vendor says it combines
    agentic AI with its audit platform to identify firm-level quality risks mapped to SQMS 1 and ISQM 1 components,
    evaluate controls and flag deficiencies, track corrective actions, run engagement quality review workflows and show
    a firm-wide dashboard, with templates for peer review and inspection readiness. It is "available to all AuditFile
    customers". The release names no customer and gives no figures.
  outcomes:
    - {lever: capacity, description: "Vendor says it reduces administrative burden and strengthens consistency across engagements; no figure", figure: "none published", measures: "n/a (vendor statement)", provenance: vendor-published, source_ref: AUDITFILE-QL-2025}
  prerequisites:
    - "Firm already on the vendor's audit platform (the release describes integration with its Advantage Audit Suite)"
  risks_and_guardrails:
    - "SQMS 1 puts ultimate responsibility for the system on the firm's managing partner, so an AI-generated risk assessment still needs the firm's own review (JOFA-QMRES-2025)"
    - "Vendor claims only; no named customer, no test, no peer-review outcome"
  human_checkpoints:
    - "Firm decides which quality risks and responses to adopt and who is responsible (not described in the release; inferred from JOFA-QMRES-2025)"
  role_evolution: "Not described in the release."
  evidence_grade: C
  sources:
    - {ref: AUDITFILE-QL-2025, title: "AuditFile Announces Launch of QualityLink", publisher: "AuditFile", type: vendor, url: "https://auditfile.com/pr/12_4_25", date: "2025-12-04", access: full, locator: "paragraphs 2-3 and 'Key Features Include'"}
    - {ref: JOFA-QMRES-2025, title: "AICPA unveils new QM resources to help firms meet Dec. 15 deadline", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2025/aug/aicpa-unveils-new-qm-resources-to-help-firms-meet-dec-15-deadline/", date: "2025-08-12", access: full, locator: "section 'A deeper discussion of a QM system's 8 components'"}
  last_reviewed: "2026-10-21"
  notes: >-
    This is the "AI does the quality-management work" direction that the existing module holds only as an idea
    (assurance-quality-management-14). Contrast: the CPA.com and FinReg QMCore page (read 2026-10-21) does not mention AI
    in its text (CPACOM-QMCORE-2026), so AI is a differentiator in small-firm SQMS tooling, not a given. Whether
    AuditFile's customers are small or mid-size firms is not stated in the release.

- id: assurance-quality-management-new-03
  title: "Regional firms standardise on one AI-enabled audit platform that carries methodology across audit, review/compilation and benefit plan engagements (Citrin Cooperman, PKF O'Connor Davies)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Regional firms run audit, review/compilation and benefit plan work on different tools and templates, which makes
    consistent methodology and training harder to show to a peer reviewer.
  solution: >-
    Caseware announced that Citrin Cooperman (private, middle-market focus; backed by New Mountain Capital since 2022)
    adopted the full DAS Suite (DAS Audit, DAS PCR, DAS EBP) on 13 Jul 2026, and that PKF O'Connor Davies (described in
    the release as a Top 25 US firm) adopted and implemented the same suite across its audit practice on 8 Oct 2026.
    Per the vendor, the suite embeds methodology and guidance in the engagement, and intelligent checklists and unified
    engagement data let teams "work more consistently". CPA.com acted as implementation partner for planning, data
    migration, training and change management at both firms. The Citrin release also names a disclosure-checklist
    agent inside the engagement workflow.
  outcomes:
    - {lever: quality, description: "Vendor and firm statements of intent on consistency and audit quality; no figure or review result published", figure: "none published", measures: "n/a (press-release statements)", provenance: vendor-published, source_ref: CASEWARE-CITRIN-2026}
  prerequisites:
    - "Migration of engagement data and training, which both firms did with an outside implementation partner (CPA.com)"
  risks_and_guardrails:
    - "Both announcements are vendor-published; neither says engagements have been signed on the platform or reviewed"
    - "A standard platform concentrates methodology risk in one vendor; the existing module covers vendor due diligence (assurance-quality-management-06)"
  human_checkpoints:
    - "Not described; the Citrin quote says the firm wants to preserve 'critical thinking and professional judgment'"
  role_evolution: >-
    Citrin's assurance innovation leader says access to reasoning inside the engagement helps professionals build
    technical knowledge and judgment (CASEWARE-CITRIN-2026).
  evidence_grade: C
  sources:
    - {ref: CASEWARE-CITRIN-2026, title: "Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware to Advance Audit Quality, Professional Development, and Scalable Growth", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: "2026-07-13", access: full, locator: "paragraphs 2-3 and section 'Strengthening Professional Development and Audit Quality'"}
    - {ref: CASEWARE-PKF-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program", date: "2026-10-08", access: full, locator: "section 'Unifying Audit Methodology with DAS'"}
    - {ref: BORYSOFF-PE-2024, title: "Does Private Equity Investment in Accounting Firms Affect Perceived and Actual Audit Quality? (Registered Report Proposal)", publisher: "The Accounting Review (George Mason, Wake Forest, Boston University authors)", type: academic, url: "https://business.gwu.edu/sites/g/files/zaxdzs5326/files/2024-06/maria_nykyforovych.pdf", date: "2024-06", access: full, locator: "p. 1 table of firms that accepted PE investment (Citrin Cooperman, 11 Apr 2022, New Mountain Capital, controlling)"}
  last_reviewed: "2026-10-21"
  notes: >-
    Firm kinds: Citrin Cooperman = PE-backed Top-25-class firm serving private middle-market companies; PKF O'Connor
    Davies = regional firm (the release calls it Top 25). Extends assurance-quality-management-05 and -16 (methodology in
    the tool; a 20-person firm on one platform) to mid-size firms with several engagement types. The platform tooling
    itself belongs to the new private-company-assurance module (routed in section 4). Maturity 'announced': both pieces
    are vendor press releases that say 'adopted' or 'implemented', with no engagement-level evidence.

- id: assurance-quality-management-new-04
  title: "A regional firm builds its own audit agents inside the vendor's governed platform so audit trail and methodology travel with each agent (PKF O'Connor Davies)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Firms that want their own agents risk disconnected one-off tools that carry no audit trail or methodology and are
    hard to defend to a reviewer.
  solution: >-
    Caseware says PKF O'Connor Davies joined its Agentic Pioneer Program on 8 Oct 2026, a co-development initiative that
    gives the firm "priority access" to an agent-builder suite (a workbench with governed MCP interfaces and a no-code
    studio). Per the vendor, agents the firm builds run in the same governed environment as Caseware Verity, so each
    carries the audit trail, methodology and context needed "to stand up to regulatory scrutiny". The release says the
    firm "will" get this access and design agents; no agent in use is described.
  outcomes:
    - {lever: risk, description: "Vendor statement that firm-built agents inherit audit trail and methodology; no agent in production described", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: CASEWARE-PKF-2026}
  prerequisites:
    - "The firm's engagements already run on the vendor platform (DAS Suite)"
    - "In-house capacity to design agents; the release names no staffing"
  risks_and_guardrails:
    - "Plan, not deployment: wording is 'will get priority access' and 'will' design and deploy"
    - "Firm-built agents are exactly the staff-built automations that AICPA-linked practitioners say need review and change management (JOFA-CYBERCHK-2026)"
  human_checkpoints:
    - "Not described"
  role_evolution: "Not described; implies firm staff who can design agents."
  evidence_grade: C
  sources:
    - {ref: CASEWARE-PKF-2026, title: "PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program", date: "2026-10-08", access: full, locator: "section 'Shaping Assurance Through the Pioneer Program'"}
    - {ref: JOFA-CYBERCHK-2026, title: "New checklist helps CPAs manage AI cyber risks", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: "2026-10-01", access: full, locator: "section 'AI and vibe coding'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Distinct from -03: the change is who builds the agents (the firm, not only the vendor). Agent pattern/ladder left at
    augment because no agent is described as operating.

- id: assurance-quality-management-new-05
  title: "Idea: keep a peer-review-ready AI governance file (tool list, approvals, monitoring, who used what) so the system-level review can test it"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    The first peer reviews of work done under the new quality-management standards were expected to begin in 2026, and
    reviewers are asked to understand a firm's use of technology and to speak to the managing partner. No peer-review
    guidance or finding on AI tools has been published, so firms do not know what a reviewer will ask.
  solution: >-
    A firm assembles, before its review, the evidence a reviewer would want if technology reliance is probed: a list
    of AI tools and versions in use, who approved them, how output is reviewed on engagements, and how the firm
    monitors them. The nearest published model is the May 2026 SOC 2 reviewer alert: reviewers are told to understand
    the firm's use of technology (including third-party platforms), the reasonableness of engagement timelines and
    whether engagements are tailored, and to compare about five engagements from different partners when risk looks
    elevated. The same AICPA article says a weak result can point to a problem in the firm's system of quality
    management and lead to follow-up that includes revising that system.
  outcomes:
    - {lever: risk, description: "No AI-related peer-review finding or outcome published", figure: "none published", measures: "n/a", provenance: independent, source_ref: AICPA-REVALERT-2026}
  prerequisites:
    - "An AI tool inventory and approval record (see assurance-quality-management-03 and -new-01)"
  risks_and_guardrails:
    - "Reviewer Alerts carry a disclaimer that they are not Peer Review Board guidance (AICPA-REVALERT-2026, as noted in the archetype's existing source row)"
    - "The SOC 2 alert is about templated reports from platform reliance, not generative AI; applying it to AI tools is an extrapolation"
  human_checkpoints:
    - "Reviewer judges whether engagements are tailored and conforming; managing partner explains the system"
  role_evolution: >-
    Managing partners may be interviewed by reviewers on how the system works (JOFA-QMPR-2024).
  evidence_grade: D
  sources:
    - {ref: JOFA-PEER-2026, title: "AICPA guides peer reviewers to address SOC 2 risks", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/", date: "2026-05-14", access: full, locator: "sections 'A heightened focus on SOC 2 quality' and 'Responding when elevated risks are identified'"}
    - {ref: JOFA-QMPR-2024, title: "How the new QM standards may affect peer review", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/news/2024/dec/how-new-qm-standards-may-affect-peer-review.html", date: "2024-12-10", access: full, locator: "section 'Updated peer review standards'"}
    - {ref: AICPA-REVALERT-2026, title: "Reviewer Alert, editions Oct 2025, Dec 2025, Feb 2026, May 2026, Jun 2026 and Sep 2026 (tables of contents; article text behind a free login)", publisher: "AICPA & CIMA Peer Review Program", type: standard-setter, url: "https://www.aicpa-cima.com/news/download/reviewer-alert-september-2026-edition", date: "2026-09-23", access: full, locator: "list of articles in each edition; none is titled for AI"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea: discussed by AICPA staff for SOC 2 platforms only. Extends assurance-quality-management-13 (inspection-ready
    file per tool, drawn from FRC and PCAOB material) to AICPA peer review of small and mid-size firms.

- id: assurance-quality-management-new-06
  title: "Outside capital funds firm-wide AI investment while the attest practice stays in a CPA-owned entity (Crowe, Eide Bailly)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [coordination-scheduling, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Partner-owned firms distribute most profit and find it hard to fund technology and acquisitions at the scale AI
    platforms need (a registered-report proposal makes this point; the PCAOB lists tech investment and succession as
    PE's upsides).
  solution: >-
    CFO Brew, citing the Wall Street Journal, reported on 26 Jun 2026 that Crowe (No. 12) agreed a majority sale to KKR
    and Eide Bailly (No. 18) to Reverence Capital Partners, with both deals expected to close in the third quarter and
    both firms to adopt alternative practice structures that split audit and attest from tax, consulting and other
    lines. It says both firms also wanted more capital to invest in AI; Eide Bailly's COO named a capital sponsor the
    "No. 1 driver". The deals were announced; this entry has no evidence of an AI programme funded by them.
  outcomes:
    - {lever: risk, description: "Regulator count of PE-related deal volume (context for the model change, not an AI outcome)", figure: "more than 90", measures: "significant PE-related transactions and firm mergers since 2020, of which more than half in 2025 up to 9 Dec 2025 (PCAOB Division of Registration and Inspections director, as reported)", provenance: independent, source_ref: AT-PCAOBPE-2025}
    - {lever: growth, description: "Global count of firms with PE investment", figure: "more than 1,000 firms; fewer than 200 initial investments leading to nearly 900 subsequent transactions", measures: "accountancy firms worldwide that have experienced PE investment over the past ten years, per IFAC research", provenance: independent, source_ref: IFAC-PE-2026}
  prerequisites:
    - "An alternative practice structure: the attest practice stays owned by CPAs and the investor buys into the non-attest entity (BORYSOFF-PE-2024; CFOBREW-PE-2026)"
  risks_and_guardrails:
    - "PCAOB: profitability pressure can reduce audit staffing and specialists and threaten independence and culture; inspectors will focus on quality-control procedures at firms that have undergone PE or APS changes (AT-PCAOBPE-2025)"
    - "No empirical result yet: the one academic study found is a 2024 registered-report proposal on public-company clients, with no findings (BORYSOFF-PE-2024)"
    - "PEEC's first exposure draft (19 Dec 2025) separates 'significant influence' from 'control'; by Aug 2026 it was discussing a ban on attest-client investment and a revised network-firm definition (PEEC-APS-2025; PEEC-APS-2026)"
  human_checkpoints:
    - "CPA owners of the attest entity keep control of the audit practice (BORYSOFF-PE-2024)"
  role_evolution: >-
    Not described for these firms. PCAOB's Botic said the profession will need new routes for junior auditors to build
    skepticism as AI spreads (AT-PCAOBPE-2025).
  evidence_grade: C
  sources:
    - {ref: CFOBREW-PE-2026, title: "10 of the top 20 CPA firms are backed by private equity", publisher: "CFO Brew", type: press, url: "https://www.cfobrew.com/stories/10-of-the-top-20-cpa-firms-are-backed-by-private-equity", date: "2026-06-26", access: full, locator: "paragraphs 2-4 (reports the WSJ)"}
    - {ref: AT-PCAOBPE-2025, title: "PCAOB warns auditors about AI and PE", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe", date: "2025-12-09", access: full, locator: "sections 'Private equity issues' and 'PE warning'"}
    - {ref: IFAC-PE-2026, title: "Private Equity Investment in Accountancy: IFAC Releases Research and Online Resource", publisher: "IFAC", type: professional-body, url: "https://www.ifac.org/news-events/2026-03/private-equity-investment-accountancy-ifac-releases-research-and-online-resource", date: "2026-03-02", access: full, locator: "paragraph 2"}
    - {ref: PEEC-APS-2026, title: "PEEC to continue discussions on alternative practice structures", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/", date: "2026-08-10", access: full, locator: "paragraphs 1-2"}
    - {ref: PEEC-APS-2025, title: "AICPA proposes changes to independence guidelines related to private equity", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/", date: "2025-12-19", access: full, locator: "bullets under 'PEEC seeks comment on'"}
    - {ref: BORYSOFF-PE-2024, title: "Does Private Equity Investment in Accounting Firms Affect Perceived and Actual Audit Quality? (Registered Report Proposal)", publisher: "The Accounting Review (George Mason, Wake Forest, Boston University authors)", type: academic, url: "https://business.gwu.edu/sites/g/files/zaxdzs5326/files/2024-06/maria_nykyforovych.pdf", date: "2024-06", access: full, locator: "Introduction and Background, pp. 1-3"}
  last_reviewed: "2026-10-21"
  notes: >-
    Firm kind: Top 20 regional/national firms, mid-market in client focus (Crowe, Eide Bailly). The CFO Brew account is
    second-hand (WSJ) and says the deals are 'expected to close' in Q3 2026; I did not check whether they closed. Model
    change belongs mainly to the archetype's economics/disruption files; kept here because the brief puts PE and APS in
    quality-management. 'More than 90' and the 'more than half in 2025' split are the PCAOB official's figures as quoted
    by Accounting Today, not read from a PCAOB document.

- id: assurance-quality-management-new-07
  title: "AI-native audit firm built inside an alternative practice structure with venture capital: continuous verification of every record (Oath)"
  archetype: assurance
  module: quality-management
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: model
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Annual, sample-based audits leave long gaps and rely on human checking of human work; the firm argues the model
    "was built for a world that no longer exists".
  solution: >-
    Oath describes itself as a modern audit firm running a "financial proof platform" that verifies every record on an
    ongoing basis; its listed client types are venture capital, private equity, employee benefit plans, non-profits, other
    private companies and other private funds. Its chief assurance officer, a former PCAOB member, told Accounting Today
    the firm is venture-backed (about $10 million raised, a $6.6 million seed per the WSJ), had to set up an attest
    entity in an alternative practice structure, runs each client in its own secure environment that does not train the
    model, and is hiring "accountant engineers". No client, engagement count or result is published.
  outcomes:
    - {lever: quality, description: "No result published; the firm's claim is that every record is checked", figure: "none published", measures: "n/a (marketing statement)", provenance: self-reported, source_ref: OATH-SITE-2026}
  prerequisites:
    - "Continuous access to the client's transaction data"
    - "A CPA-owned attest entity separate from the technology company (the firm's description of APS requirements)"
  risks_and_guardrails:
    - "Christina Ho (Oath's chief assurance officer, a former PCAOB member) warns PEEC's 'closely aligned' technology-entity wording could pull audit-tech companies into the APS rules, and that ambiguity remains about when licensing AI audit tools creates a conflict (AT-PEIND-2026)"
    - "81 comment letters were filed on the proposed rules; none from technology companies (as she described the committee's statistics, AT-PEIND-2026)"
  human_checkpoints:
    - "Site says the firm will 'elevate professionals, not replace them' and that people apply judgment; checkpoints are not specified"
  role_evolution: >-
    New 'accountant engineer' hires (AT-PEIND-2026).
  evidence_grade: C
  sources:
    - {ref: OATH-SITE-2026, title: "Oath | Swear by your numbers", publisher: "Oath", type: firm, url: "https://www.oathverified.com/", date: "2026-10", access: full, locator: "home page sections 'why oath', 'services' and 'how oath works'"}
    - {ref: AT-PEIND-2026, title: "AICPA weighs PE and tech impact on audit independence", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules", date: "2026-08-31", access: full, locator: "paragraphs on Ho's firm, 'Maintaining independence'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Page date is the live site read on 2026-10-21 (no publication date). Firm kind: venture-backed start-up auditor
    serving private funds and private companies, so a signal of where private-company audit may go, not mid-market practice
    today. Fits full-population-testing at the model scope, but the evidence is the firm's own positioning plus one
    trade-press interview with its executive.

- id: assurance-quality-management-new-08
  title: "Idea: a baseline security and AI governance self-assessment for the firm, with a change-management gate for staff-built automations and agents"
  archetype: assurance
  module: quality-management
  function: risk-compliance-legal
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff can now build their own dashboards, automations and agents with AI tools ("vibe coding"). At firms that hold
    client personal and financial data this creates unreviewed software and agent access to data.
  solution: >-
    A named practitioner (Sanjay Chadha, founding partner of SAV Associates, Toronto, with offices in Canada and the
    United States) published a 75-point baseline checklist: a dozen security areas of five to ten checkpoints each,
    including AI governance and responsible use. Interviewees add that firms should set a review and validation process
    for AI-generated software and agents, route widely used agents through formal change management, and give agents
    least-privilege access, restricted tool and API permissions, activity monitoring and human approval for higher-risk
    actions.
  outcomes:
    - {lever: risk, description: "No adoption or outcome data published", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: JOFA-CYBERCHK-2026}
  prerequisites:
    - "An approved list of AI tools; enterprise versions with stronger data protections and contractual terms (JOFA-CYBERCHK-2026)"
  risks_and_guardrails:
    - "Prompt injection: monitor and secure inputs so an attacker cannot inject instructions (JOFA-CYBERCHK-2026)"
    - "Confidential client information: consent and disclosure questions under the AICPA code before client data goes into an AI system (JOFA-ETHICSAI-2026)"
  human_checkpoints:
    - "Human approval for higher-risk agent actions; named ownership and review for agents before they enter workflows"
  role_evolution: >-
    Cherry Bekaert's Steven Ursillo says user-driven development spreads the developer pool to people without a full
    view of what the code does (JOFA-CYBERCHK-2026).
  evidence_grade: D
  sources:
    - {ref: JOFA-CYBERCHK-2026, title: "New checklist helps CPAs manage AI cyber risks", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: "2026-10-01", access: full, locator: "intro and section 'AI and vibe coding'"}
    - {ref: JOFA-ETHICSAI-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "section 'AI can create confidentiality risks quickly'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea: a published checklist exists but no firm reports using it. Firm kinds: SAV Associates (small cross-border
    firm), Cherry Bekaert (PE-backed regional firm; PE investor and 2022 date per BORYSOFF-PE-2024). Adjacent to
    assurance-quality-management-03 (inventory and preventive controls) but extends it to staff-built software and
    agents, which that entry does not cover.

- id: assurance-soc-attestation-new-01
  title: "One CPA-led engagement delivers a SOC 2 report plus an AIUC-1 certification for AI agents and systems (AICPA and AIUC joint offering)"
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Buyers of AI products run slow, bespoke security questionnaires. A SOC 2 report covers controls over a system but,
    as the AIUC case studies argue, was not designed to test hallucinations or adversarial manipulation of an agent.
  solution: >-
    The AICPA and AIUC announced on 19 Oct 2026 a joint offering: one CPA-led engagement that ends with a SOC 2 report
    (an opinion on the design and operating effectiveness of controls) and an AIUC-1 certification. An AICPA spokesperson
    told Accounting Today the entity goes through both processes separately and ends with a single report and both
    outputs, and that one firm doing both gives practitioners more familiarity with the entity. AIUC-1 adds live testing
    of agent behaviour (hundreds of risk and attack combinations, a typical evaluation covering thousands of scenarios,
    per AIUC's cofounder), annual renewal and quarterly technical retesting. Several CPA firms are delivering it now and
    the pilots are collecting feedback; PwC is the only firm named. Full launch is expected in early 2027.
  outcomes:
    - {lever: risk, description: "No result for the joint offering. Adjacent AIUC-1 data point: the first AIUC-1 certification audited by Schellman (UiPath) covered 250+ pieces of evidence and 2,000+ adversarial scenarios and took 8 weeks end to end", figure: "8 weeks; 250+ evidence items; 2,000+ scenarios", measures: "elapsed time from start to certificate for one company's multiple agents, evidence pieces reviewed and adversarial scenarios run, per the AIUC and Schellman release update of 2 Apr 2026", provenance: vendor-published, source_ref: SCHELLMAN-AIUC1-2026}
  prerequisites:
    - "An AI developer or deployer with a system in scope for both a SOC 2 and AIUC-1 (agent configurations supplied for testing; evidence package) (AIUC-SITE-2026)"
    - "A CPA firm licensed for SOC 2 attestation; for AIUC-1, an accredited auditor and AIUC's technical evaluation"
  risks_and_guardrails:
    - "SOC 2 is an attestation, not a certification; the AICPA release itself calls the joint product a 'certification' but defines SOC 2 as an examination with an opinion (AICPA-AIUCPR-2026)"
    - "SOC 2 quality is already under peer-review pressure for templated work and heavy platform reliance (JOFA-PEER-2026)"
    - "Schellman itself calls AIUC-1 'still largely a competitive differentiator' in an early adoption phase (SCHELLMAN-BLOG-2026)"
  human_checkpoints:
    - "CPA firm leads the engagement and issues the SOC 2 opinion; AIUC runs technical evaluations and issues the AIUC-1 certification, with an accredited auditor collecting evidence (SCHELLMAN-AIUC1-2026)"
  role_evolution: >-
    SOC 2 examiners add AI-agent testing outputs from an outside technical evaluator to their evidence base; the
    CPA firm's lead role is the AICPA's selling point (AICPA-AIUCPR-2026).
  evidence_grade: B
  sources:
    - {ref: AICPA-AIUCPR-2026, title: "Auditors Meet Urgent Demand for AI Assurance with New Offering from AICPA and AIUC", publisher: "AICPA & CIMA", type: standard-setter, url: "https://www.aicpa-cima.com/news/article/auditors-meet-urgent-demand-for-ai-assurance-with-new-offering-from-aicpa-and-aiuc", date: "2026-10-19", access: full, locator: "paragraphs 4-9 and last paragraph"}
    - {ref: AT-AIUC-2026, title: "New AI assurance certification combines SOC 2, AIUC-1", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/new-ai-assurance-certification-combines-soc-2-aiuc-1", date: "2026-10-19", access: full, locator: "paragraphs 5-8 (AICPA spokesperson; PwC quote)"}
    - {ref: AICPA-AIUC-2026, title: "AICPA partners on new offering that assures AI systems and agents", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/", date: "2026-10-19", access: full, locator: "paragraphs 1-3, 5-6, 8"}
    - {ref: SCHELLMAN-AIUC1-2026, title: "Schellman becomes the first accredited auditor for AIUC-1 (with 2 Apr 2026 update on the first certification)", publisher: "AIUC (joint release with Schellman)", type: vendor, url: "https://www.aiuc-1.com/research/schellman-becomes-first-accredited-auditor", date: "2026-02-03", access: full, locator: "sections 'AIUC-1 Certification Overview' and 'Update: First certification completed'"}
    - {ref: AIUC-SITE-2026, title: "AIUC-1 Standard (certification process page)", publisher: "AIUC", type: vendor, url: "https://www.aiuc-1.com/", date: "2026-10", access: full, locator: "process section 'Scoping / Evals / Audit / Certification'"}
    - {ref: SCHELLMAN-BLOG-2026, title: "Why One AI Governance Framework Isn't Enough", publisher: "Schellman", type: firm, url: "https://www.schellman.com/blog/ai-governance/why-one-ai-governance-framework-isnt-enough", date: "2026-10-02", access: full, locator: "section 'What is AIUC-1?'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B (not A): a named pilot firm (PwC, per Accounting Today) and a press-release statement that several firms
    deliver it; no measured result. The UiPath figures are for AIUC-1 alone, an adjacent process, and are vendor-published.
    Firm kinds: PwC (Big Four); Schellman (described in the joint release as a top-50 CPA firm focused on IT compliance,
    PE-backed since 2021 per BORYSOFF-PE-2024). No mid-market CPA firm is named as delivering the joint offering. The
    AICPA release page header reads 'Oct 18, 2026' while the dateline reads 19 Oct; I used the dateline and the JofA date.
    AIUC reports typical evaluations of 1,000-3,000 simulations (Q4 2026 release) and red-teaming of 1,000 to 5,000
    scenarios (site); the AIUC cofounder quote says 'thousands'. Extends assurance-assurance-over-ai-19 (AIUC-1 with an
    authorised auditor and insurance) and soc-attestation-12 to -15 (platform-bundled SOC services) by naming the AICPA as
    a party. Search-only lead: a LinkedIn repost reports Sensiba LLP earned provisional AIUC-1 accreditation (not opened;
    SENSIBA-AIUC1-2026).

- id: assurance-soc-attestation-new-02
  title: "A regional firm pairs AI governance advisory (ISO 42001 alignment) with its SOC examination practice and manages the advisory and attest boundary (Kaufman Rossin)"
  archetype: assurance
  module: soc-attestation
  function: service-delivery
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Clients that sell AI products or deploy agents ask their SOC firm for help with AI governance. Doing both for the
    same client raises independence questions, and many mid-size firms have no AI-governance team.
  solution: >-
    A job posting of 7 Oct 2026 shows Kaufman Rossin, a privately owned independent CPA firm of more than 700 employees
    that states it has no outside investors or PE influence, hiring a Senior Manager (CPA required) in Risk Advisory
    Services to support AI governance advisory engagements, including AI risk assessments, policy development and ISO
    42001 alignment, and to partner with the SOC assurance team on SOC 1, SOC 2 and SOC 3 engagements. It asks for the
    ability to use AI tools to improve analysis and documentation and for experience with Fieldguide or similar audit
    management platforms. The AICPA ethics staff warn that AI-related non-attest services such as developing or hosting
    an AI system for an attest client can raise independence concerns.
  outcomes:
    - {lever: growth, description: "No outcome published; a hiring signal only", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: KAUFMAN-JOB-2026}
  prerequisites:
    - "CPA-qualified senior staff with SOC and AI governance framework knowledge (KAUFMAN-JOB-2026)"
    - "Independence evaluation before advisory work for an attest client (JOFA-ETHICSAI-2026)"
  risks_and_guardrails:
    - "Advisory on an AI system, or hosting it, for a client the firm also attests can create threats; use the conceptual framework and document the analysis (JOFA-ETHICSAI-2026)"
  human_checkpoints:
    - "Not stated in the posting"
  role_evolution: >-
    SOC and risk-advisory managers need ISO 42001 and AI governance knowledge on top of Trust Services Criteria and
    SSAE 18 / AT-C 320 experience (KAUFMAN-JOB-2026).
  evidence_grade: B
  sources:
    - {ref: KAUFMAN-JOB-2026, title: "Cybersecurity Risk Advisory Senior Manager (Kaufman Rossin job posting)", publisher: "Kaufman Rossin via Workable", type: job-posting, url: "https://jobs.workable.com/view/1f4ea4b5-e0d5-4cd7-9e2b-4befaf13dad6", date: "2026-10-07", access: full, locator: "'How You'll Contribute' bullets 3-4; 'What Skills You'll Bring'"}
    - {ref: JOFA-ETHICSAI-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "section 'AI services can raise independence concerns for attest clients'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B on the strength of a named firm showing the service in a live posting; the posting does not say how many AI
    governance engagements the firm has done. Firm kind: regional firm of 700+ employees, privately owned (says it has
    no PE or outside-investor influence). The posting only says 'Support AI governance advisory engagements'. Overlaps assurance-assurance-over-ai-13
    (readiness assessment against ISO 42001); the new element is the pairing with SOC attest work and the independence
    boundary. Routed in part to acceptance-independence.

- id: assurance-assurance-over-ai-new-01
  title: "A client's external auditors receive a third-party agent-evaluation attestation as input to a SOX audit, with assurance scaled by agent risk tier (MSCI)"
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    When an AI agent makes decisions that touch SOX systems, auditors ask whether the agent does what its policy says.
    Governance documents, ISO 42001 work and an existing SOC 2 did not answer that for the company's CISO.
  solution: >-
    MSCI's SecOps Agent reviews and approves privileged-access requests. AIUC's red team ran about 1,400 tests against it
    (including testing across 112 privileged roles). A signed evaluation attestation and detailed report went to MSCI's
    external auditors as input to its 2026 SOX audit. MSCI and AIUC also built a risk-tiering framework: top-tier agents
    (customer-facing, or touching regulatory, HR or client data) are planned to be certified against AIUC-1 with an
    independent auditor; lower tiers will apply a defined subset of requirements at build time.
  outcomes:
    - {lever: risk, description: "The agent passed with no major or significant vulnerabilities; remaining low-severity cases were timeouts, upstream platform controls, or the agent being stricter than required", figure: "~1,400 tests; 112 privileged roles", measures: "tests run by AIUC's red team across benign, social-engineering and adversarial risks against one SecOps agent, and privileged roles covered", provenance: vendor-published, source_ref: AIUC-MSCI-2026}
  prerequisites:
    - "Agent scoped with the company's engineers and grading criteria agreed before scaling the tests"
    - "A risk-tiering framework mapping requirements to each tier"
  risks_and_guardrails:
    - "The tests were run by AIUC's own red team and published by AIUC, not by MSCI or its auditors; whether the external auditors relied on the report is not stated"
    - "Quarterly re-testing is required to keep AIUC-1 certification current (AIUC-Q3-2026)"
  human_checkpoints:
    - "External auditors decide how far an evaluation report supports their SOX conclusions (not described in the source)"
  role_evolution: >-
    CISO and security-governance staff run a tiered assurance programme for agents (AIUC-MSCI-2026).
  evidence_grade: B
  sources:
    - {ref: AIUC-MSCI-2026, title: "How MSCI secures its highest-risk AI agents with AIUC-1", publisher: "AIUC", type: vendor, url: "https://www.aiuc-1.com/research/how-msci-secures-its-highest-risk-ai-agents-with-aiuc-1", date: "2026-09-24", access: full, locator: "sections 'Solution' and 'A framework for the next thousand agents'"}
    - {ref: AIUC-Q3-2026, title: "Q3-2026 update: AIUC-1 for coding agents, and technical auditor guidance", publisher: "AIUC", type: vendor, url: "https://www.aiuc-1.com/research/2026-q3-standard-update", date: "2026-07-14", access: full, locator: "section 2 'Re-certification'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B, not A: figures are the evaluator's, published in a vendor case study, with no independent verification and no
    statement from MSCI's auditors. Larger public-company example (MSCI has roughly 6,000 employees); included because it
    shows what a mid-market client's external auditor will increasingly be handed. Extends assurance-assurance-over-ai-03,
    -05 and -07, which hold the auditor's side (extend ITGCs, use management monitoring evidence, vendor AI evidence) as
    ideas.

- id: assurance-assurance-over-ai-new-02
  title: "Scope an AI-agent assurance engagement with a developer-versus-deployer responsibility matrix (AIUC-1 guidance)"
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Agents are often built on a configurable platform (examples named: Cursor, Sierra, ElevenLabs) and run by a different
    organisation on its own data. Each side can assume the other covers a control, leaving gaps, and an assurer must
    decide what the client (the deployer) can evidence.
  solution: >-
    AIUC's 15 Oct 2026 release publishes guidance and a template matrix, drafted by a working group of consortium members,
    on who typically meets each control. Across the 78 core controls in the Q4 2026 standard, where a developer-deployer
    relationship exists, AIUC says typically 33 are met by the developer, 40 by the deployer and 5 by the independent
    evaluator (the technical testing). The split depends on the platform, and the responsibilities are described as not
    legally binding. An assurer would use it to set the engagement's scope and the evidence the deployer must provide.
  outcomes:
    - {lever: quality, description: "Scoping aid; no use reported", figure: "33 developer, 40 deployer, 5 independent evaluator", measures: "of the 78 core controls in the 2026 Q4 AIUC-1 standard, the controls AIUC says are typically met by each party where a developer and deployer exist", provenance: vendor-published, source_ref: AIUC-Q4-2026}
  prerequisites:
    - "Knowing which platform the client's agents run on and what that platform provides"
  risks_and_guardrails:
    - "Guidance is not legally binding; the exact split depends on the platform (AIUC-Q4-2026)"
    - "Authored by AIUC and its consortium, not by the AICPA or an assurance regulator"
  human_checkpoints:
    - "Assurer and client agree the matrix for the specific platform"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: AIUC-Q4-2026, title: "Q4-2026 release: Open-weight model controls and stronger third-party testing", publisher: "AIUC", type: vendor, url: "https://www.aiuc-1.com/research/2026-q4-standard-update", date: "2026-10-15", access: full, locator: "section 'New Guidance for Agent Developers vs. Deployers'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Mid-market relevance: most mid-market clients deploy agents on third-party platforms rather than build models, so the
    deployer column is the part a regional assurer would test. Related to the practice aid's point that when AI is bought
    from a third party an auditor may need a SOC report or other attestation and management representations
    (AT-AICPAPA-2026); that point is routed to existing assurance-assurance-over-ai-07 in section 4.

- id: assurance-assurance-over-ai-new-03
  title: "Idea: CPAs build an audit package that lets reviewers verify AI-generated analysis quickly (math example, offered as a model for business outputs)"
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: model
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    AI agents generate analysis far faster than people can check it; the example comes from mathematics, where a CPA
    says journal peer review takes about a year and cannot scale.
  solution: >-
    Richie Sater, a CPA and software developer, built AI agents that produced an answer to a 1986 open problem over
    about three weeks, then built an "audit package" of supporting materials for the mathematician who maintains the
    problem list. He says it took roughly two weeks of review for other claimants, that his package let reviewers look
    quickly, and that it was endorsed and sent to peer review. He says the last two problems took about three days of
    agent work. He proposes the same service for AI-generated financial analyses and models. No business client is named.
  outcomes:
    - {lever: speed, description: "None published for any business use. In the maths case Sater says review was quicker; these are his statements", figure: "none published", measures: "n/a (recollection of one practitioner)", provenance: self-reported, source_ref: JOFA-MATHEX-2026}
  prerequisites:
    - "Agent-building skill; Sater estimates a CPA with basic computer literacy can start building basic agents in about a week (his estimate)"
  risks_and_guardrails:
    - "The case is mathematics, not an assurance engagement; no professional standard, independence or liability framework applies as described"
    - "A practitioner on Accounting Today warns that independent parties using similar AI can share 'common-mode' failures, and that polished AI output can look like completed professional work (AT-AUDITRISK-2026)"
  human_checkpoints:
    - "Mathematician reviews the package and sends the result to peer review (JOFA-MATHEX-2026)"
  role_evolution: >-
    CPAs move from checking human work to verifying machine output (JOFA-MATHEX-2026; AT-PEIND-2026 quotes Christina Ho
    describing 'a machine checking another machine's work').
  evidence_grade: D
  sources:
    - {ref: JOFA-MATHEX-2026, title: "Problem solved: A math example of CPA-led assurance using AI agents", publisher: "Journal of Accountancy", type: press, url: "https://www.journalofaccountancy.com/news/2026/oct/problem-solved-a-math-example-of-cpa-led-assurance-using-ai-agents/", date: "2026-10-19", access: full, locator: "sections 'Opening doors with new tech, old skills'"}
    - {ref: AT-AUDITRISK-2026, title: "AI didn't invent audit risk, so what actually changed?", publisher: "Accounting Today (AT Think opinion)", type: press, url: "https://www.accountingtoday.com/opinion/ai-didnt-invent-audit-risk-so-what-actually-changed", date: "2026-10-13", access: full, locator: "sections 'Where AI may test our existing approach'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea label: one practitioner's anecdote in a different field plus a proposal; grade capped at D for the business use.
    The delegate ladder reflects the agents building the package; the human reviewer remains the mathematician.
```

## 3. Module notes

### quality-management (small and mid-size firms, peer review, PE and APS)

**Processes and key steps (with work types)**
- Design the SQM: set quality objectives, assess quality risks, design responses (review-assurance; document-production). The managing partner holds ultimate responsibility; the AICPA's guide lists eight components, with the risk-assessment process and information and communication marked new [JOFA-QMRES-2025, "A deeper discussion of a QM system's 8 components"].
- Monitor and remediate (data-reporting; review-assurance). The AICPA issued a second practice aid on monitoring and remediation in Aug 2025 [JOFA-QMRES-2025, "MEMBER RESOURCES"].
- Evaluate the system and conclude, within a year of implementation or by 15 Dec 2026, then yearly (expert-judgment) [JOFA-QMRES-2025, "The evaluation of the system of quality management"].
- Peer review tests the system; the first reviews of work done under the new standards were expected to begin in 2026 [JOFA-QMPR-2024, "Updated peer review standards"].
- AI tool governance at the firm (approve, set acceptable use, revalidate, monitor) is where the practice aid adds new content [AICPA-AIPA-2026; AT-AICPAPA-2026].

**Pain points**
- Staff skills and data: in a survey of 54 US firms, 66% ranked untrained staff as a top blocker to audit transformation and 75% had no formal, documented transformation plan; nearly a quarter reported no use of AI or advanced automation [CPACOM-ATR-2025, pp. 2, 7-8]. The survey is not representative.
- Generic starting material: the AICPA's Aug 2025 guide to QM resources does not mention AI in its body [JOFA-QMRES-2025].
- Mid-tier practitioner worry: at one UK mid-tier firm (Beever and Struthers), 72% of surveyed staff feared incorrect genAI output, 74% said genAI sped certain tasks and 22% saw a marked rise in output; 52% worried about client information [ICAS-AMBS-2026].
- Smaller firms pool knowledge: a Peer Review Board member said her 170-person firm reached out to other firms about the standards [JOFA-QMPR-2024].

**Metrics and benchmarks (no AI-specific quality metric exists)**
- Tennessee 2025 peer review report: 424 firms enrolled (38 with no accounting and auditing work). System reviews 46: 40 pass (87%), 2 pass with deficiencies (4%), 4 fail (9%). Engagement reviews 97: 87 pass (90%), 5 pass with deficiencies, 5 fail. Nonconforming engagements 34 of 448 reviewed (8%); reviews 13 of 99; compilations with disclosures 2 of 44; compilations omitting disclosures 5 of 175; single audits 2 of 11; ERISA 2 of 21; one of 2 SOC reports. System-review deficiency reasons (16): engagement performance 6, monitoring 5, human resources 2, tone at the top 1, ethics 1, acceptance and continuance 1. No AI content [TSCPA-PEERREVIEW-2025, sections II.2.a-c].
- Other state society reports for 2025 (search-result summaries only, not opened, `search-only`): Virginia 61 system reviews, 56 pass, 4 with deficiencies, 1 fail; ERISA 4 of 19 and reviews 7 of 82 nonconforming. Oklahoma 55 system reviews, 35 pass (64%). Georgia 102 system reviews, 68 pass, 25 fail. Minnesota 44, 41 pass. Connecticut 34, 28 pass [STATE-PR-2025]. Do not use these as proof points.
- Reviewer Alert tables of contents, six editions Oct 2025 to Sep 2026: no AI-titled article. Titles of relevance: "AICPA TQAs Issued on Use of Technology in an Audit" (Oct 2025), "Alternative Practice Structures (APS) and Peer Review" and "Peer Review Risk Factor - Engagement Hours for SOC 2 Engagements" (May 2026), "New QM resources" (Jun 2026) [AICPA-REVALERT-2026].
- PE scale: more than 90 significant PE-related transactions and mergers since 2020, more than half in 2025 (PCAOB official, as reported) [AT-PCAOBPE-2025]; IFAC counts 1,000+ firms worldwide with PE investment in ten years [IFAC-PE-2026].
- Independent measurement of AI effect on quality, override rates or parallel-run results at mid-market firms: none found.

**Guardrails and regulatory points**
- Practice aid is nonauthoritative; its audit-firm part stresses QM policies for AI tools, engagement-team competence, planning AI use per engagement and partner duties [AICPA-AIPA-2026]. A second AI tool checking the first "does not reduce or take the place of" the auditor's supervision and review [AT-AICPAPA-2026].
- Engagement letters: AU-C 210 does not require naming AI tools; disclosure may still be required by law, contract or firm policy, and some states require advance disclosure of certain AI uses by licensed professionals [AT-AICPAPA-2026; CFODIVE-AIPA-2026]. Already covered by assurance-quality-management-24; the state-law sentence is the mid-market addition.
- Confidentiality and consent for client data in AI tools; AI-related non-attest services can threaten independence [JOFA-ETHICSAI-2026].
- The ASB sets private-company audit standards and peer review monitors compliance [CFODIVE-AIPA-2026]. The ASB has issued no AI standard that I found.
- APS independence: first exposure draft voted 19 Dec 2025 (control versus significant influence; network-firm definition), effective one year after adoption if approved [PEEC-APS-2025]. In Aug 2026 PEEC discussed a revised network-firm definition and a ban on attest-client investment and agreed to continue at an October interim meeting on a second exposure draft [PEEC-APS-2026]. Accounting Today reports a plan to re-expose in October or November and adopt "next May", and 81 comment letters with none from technology companies [AT-PEIND-2026]. Outcome of the October meeting not found.
- PCAOB: inspectors will look at quality-control procedures at firms that have undergone PE or APS changes and will keep focusing on AI in 2026 [AT-PCAOBPE-2025].
- SOC-platform ethics: terms that shift control or evidence access to a tool provider can create threats [JOFA-SOCETH-2026].

**Frontier signals (dated)**
- 2025-12-04 AuditFile launches an AI-driven SQMS tool [AUDITFILE-QL-2025].
- 2025-12-09 PCAOB officials flag AI and PE as 2026 inspection focus [AT-PCAOBPE-2025].
- 2025-12-19 PEEC exposure draft on alternative practice structures [PEEC-APS-2025].
- 2026-03-02 IFAC publishes PE research [IFAC-PE-2026].
- 2026-05-13 Reviewer Alert includes "APS and Peer Review" [AICPA-REVALERT-2026].
- 2026-06-26 Crowe and Eide Bailly PE deals reported, citing AI investment as a reason [CFOBREW-PE-2026].
- 2026-08-10 to 08-12 AICPA Peer Review Conference includes an APS session; no AI session on the listing [AICPA-PEERCONF-2026].
- 2026-08-14 AICPA report on new QM peer review checklists (member-only) [AICPA-QMPR-2026].
- 2026-10-13 practice aid; 2026-10-08 PKF O'Connor Davies agent programme [AICPA-AIPA-2026; CASEWARE-PKF-2026].
- 2026-12-15 first annual SQM evaluation due [JOFA-QMRES-2025].
- Scheduled: PEEC second exposure draft (Oct or Nov 2026, per Accounting Today) [AT-PEIND-2026].

**Workforce and role effects**
- Managing partner formally accountable for the system and its annual conclusion; reviewers may interview them [JOFA-QMPR-2024].
- Engagement partners must understand AI tools, confirm approval and check use [AICPA-AIPA-2026].
- Engagement teams may need "a blend of auditing expertise, AI knowledge, data skills, professional skepticism and specialist support" [AICPA-AIPA-2026, section one list].
- A PCAOB board member said new paths will be needed for junior auditors to gain skepticism as AI spreads [AT-PCAOBPE-2025].
- New titles: "accountant engineers" at an AI-native firm [AT-PEIND-2026]; SOC managers expected to know ISO 42001 [KAUFMAN-JOB-2026].
- ACCA survey (1,178 professionals, 135 countries): 61% name AI use as the leading ethical challenge (32% in 2024); 72% agree AI tools improve quality and efficiency of their work; 89% say they apply professional skepticism when using AI [AT-ACCAETH-2026]. Global, not mid-market.

**Objections practitioners raise**
- "Platform tools make the work faster." Peer review treats heavy platform reliance as a risk, and a SOC working-group chair says "fast and easy may come at the expense of quality and objectivity" [JOFA-FAST-2026; JOFA-PEER-2026].
- "PE gives us money for AI." PCAOB says the same capital can squeeze staffing and independence [AT-PCAOBPE-2025]. A former PCAOB member says the APS rules, as drafted, could favour large incumbents that build AI in-house over firms licensing it [AT-PEIND-2026].
- "AI risk is just old risk." A practitioner argues technology touching information was always a risk, but that reperformance and common-mode failure are where AI tests existing methods [AT-AUDITRISK-2026].
- "We cannot see the guidance." The practice aid and several AICPA peer-review resources are member-only [AICPA-AIPARES-2026; AICPA-QMPR-2026].

**Interview probes (advisor to firm quality leader or managing partner)**
1. "Open your SQMS 1 risk assessment. Where do AI tools appear, who owns each response, and what will your 15 Dec 2026 evaluation say about them?"
2. "If your peer reviewer asked tomorrow which AI tools staff used on which engagements last year, what could you show, and how long would it take?"
3. "Which of your tools come from software you already buy, from an affiliated entity or from an investor's portfolio? Who decided they were acceptable for attest clients?"
4. "What has a reviewer, inspector or client asked about AI so far, and what could you not answer?"
5. "What do your people build for themselves with AI (dashboards, macros, agents), and what review do those go through?"

### soc-attestation (AI-related changes in SOC 2 practice)

**Processes and key steps**
- New: scoping an AI system for SOC 2 plus AIUC-1 together (expert-judgment); two separate processes ending in one report [AT-AIUC-2026]. AIUC-1 steps: scoping, evals (agent configurations supplied, AIUC writes tests and red-teams, typically 1,000 to 5,000 scenarios), audit by an accredited auditor, certificate and report valid one year, quarterly retests [AIUC-SITE-2026].
- Existing SOC steps stay: planning, walkthroughs, testing, reporting; see the module.

**Pain points**
- Buyers send repeated security questionnaires about AI agents; the joint offering is pitched as ending that cycle [AICPA-AIUCPR-2026].
- Quality pressure on SOC 2: tool vendors "numbering in the dozens", some with referral networks of small CPA firms, drive "fast and easy" expectations [JOFA-FAST-2026]. AI adds an evidence gap: no AI-specific Trust Services Criteria as of 30 Aug 2026 (CSA research note) [CSA-SOC2].

**Metrics and benchmarks**
- More than 40,000 organisations obtained a SOC 2 attestation or AIUC-1 certification "last year" (AICPA and AIUC release; the count does not separate the two) [AICPA-AIUCPR-2026].
- Schellman survey of 500+ enterprise leaders: 74% say they are audit-ready for AI governance and 27% actually are (company summary; full report gated; vendor-published) [SCHELLMAN-AIGOV-2026].
- First AIUC-1 audit by an accredited auditor: 250+ evidence items, 2,000+ scenarios, 8 weeks [SCHELLMAN-AIUC1-2026].
- Tennessee 2025: one of two SOC engagements reviewed was nonconforming (n is too small to generalise) [TSCPA-PEERREVIEW-2025].

**Guardrails and regulatory points**
- SOC 2 is an examination under AICPA attestation standards with an opinion on design and operating effectiveness; the joint product is called a certification in AICPA's release [AICPA-AIUCPR-2026].
- Peer review from 1 Jun 2026: AICPA staff outreach to team captains of SOC 2 firms; about five engagements may be compared; heightened oversight [JOFA-PEER-2026].
- AICPA Aug 2026 ethics article on tool providers: control, financial dependency and evidence access [JOFA-SOCETH-2026].
- The AICPA release names guidance on service organisations' use of AI in SOC 1 and SOC 2 engagements as issued 'in the past year' [AICPA-AIPA-2026]; the TQA is covered in the existing module.

**Frontier signals**
- 2026-02-03 Schellman first accredited AIUC-1 auditor; first certification completed (update 2 Apr 2026) [SCHELLMAN-AIUC1-2026].
- 2026-07-14 AIUC publishes scoping and re-certification guidance as the first annual re-certifications approach [AIUC-Q3-2026].
- 2026-10-15 AIUC Q4 release: third-party testing consolidated into one requirement per principle [AIUC-Q4-2026].
- 2026-10-19 AICPA and AIUC announce the joint offering; full launch "expected" early 2027 after initial engagements conclude [AICPA-AIUCPR-2026].

**Workforce and role effects**
- SOC and risk-advisory managers asked to bring AI governance and ISO 42001 knowledge, plus the ability to use AI tools [KAUFMAN-JOB-2026].
- The CPA role is the AICPA's positioning: CPAs lead, outside technical evaluators test agent behaviour [AICPA-AIUCPR-2026; SCHELLMAN-AIUC1-2026].

**Objections**
- "Is AIUC-1 mainstream?" Schellman says it is "still largely a competitive differentiator" at an early adoption phase [SCHELLMAN-BLOG-2026].
- "SOC 2 is enough." AIUC case material argues SOC 2 validates operational security but was not designed for hallucinations or adversarial attacks (vendor view) [AIUC-FIN-2025].

**Interview probes**
1. "Have clients that build or deploy AI agents asked you for SOC 2 plus something for the AI? What did you say, and who would do the technical testing?"
2. "If a client brings an AIUC-1 evaluation report to your SOC 2 examination, what would you accept as evidence and what would you retest?"
3. "Which AI-related Trust Services Criteria mappings do you use now, and would a peer reviewer see the same engagement design across your AI clients?"

### assurance-over-ai (practice aid and AI-system assurance)

**Processes and key steps**
- Auditor of a client that uses AI: understand AI in reporting; consider acceptance and continuance; assess risks (data, model, hallucination, explainability, bias, drift, AI-enabled fraud); respond by substantive testing of AI outputs, testing controls, or testing AI-related IT controls; use a service auditor's report and AI-related management representations when AI is bought [AICPA-AIPA-2026; AT-AICPAPA-2026]. Work types: review-assurance, expert-judgment.
- Assurer of an AI system: scope agents, rely on technical evaluation, audit evidence and controls, issue report (above).

**Pain points**
- Evidence: "the less insight the auditor has into the process... the more difficult it may be to become comfortable with the output"; third-party AI limits procedures [AT-AICPAPA-2026].
- The practice aid is incomplete: a deeper dive on risk of material misstatement and evidence evaluation for AI-using companies "will be added" [AICPA-AIPA-2026].
- Governance maturity gap: 74% claim audit-ready, 27% are (Schellman survey) [SCHELLMAN-AIGOV-2026].

**Metrics and benchmarks**
- AIUC: 78 core controls in the Q4 2026 standard: 33 met by developer, 40 by deployer, 5 by independent evaluator where both exist [AIUC-Q4-2026].
- MSCI: about 1,400 tests, 112 privileged roles, no major or significant vulnerabilities (vendor-published) [AIUC-MSCI-2026].
- Practice aid length: 51 pages [CFODIVE-AIPA-2026].

**Guardrails**
- Practice aid is nonauthoritative; the auditor remains responsible for the audit and opinion [AICPA-AIPA-2026].
- Auditor cannot rely on tests of controls alone where models drift or are probabilistic [AT-AICPAPA-2026].

**Frontier signals**
- 2026-10-13 practice aid; 2026-10-15 AIUC developer-deployer guidance; 2026-10-19 joint offering [AICPA-AIPA-2026; AIUC-Q4-2026; AICPA-AIUCPR-2026].
- Expected: more practice-aid sections (risk assessment, evidence) and Q&As [AICPA-AIPA-2026].

**Workforce**
- Assurance of AI output pitched as a CPA role (JofA, 19 Oct 2026) [JOFA-MATHEX-2026].
- Engagement-team capability gap: blend of audit, AI, data skills and specialists [AICPA-AIPA-2026].

**Objections**
- "AI risk is not new." Practitioner view [AT-AUDITRISK-2026].
- Governance on paper does not show behaviour: MSCI's CISO says none of ISO 42001 work, governance programme or SOC 2 answered whether the agent "does what the policy says" (his statement as published by AIUC) [AIUC-MSCI-2026].

**Interview probes**
1. "On your last private-company audit where the client used AI in close or controls, what did you do at acceptance and risk assessment, and what did you ask for beyond a SOC report?"
2. "How would you decide whether to test an AI-operated control's outputs or the control itself, and who reviews that choice?"

## 4. Routed to other modules

| Item | Target module | Source and locator |
|---|---|---|
| Client AI reliance as an acceptance and continuance factor; likened to external specialists and complex models; the more the entity relies on AI outputs, the more information the auditor may need | acceptance-independence (extends -10) | [AT-AICPAPA-2026], section one, acceptance paragraphs |
| APS independence rule: attest-client investment ban, network-firm definition, "closely aligned" tech entities, AI-tool licensing ambiguity; comment-letter gap | acceptance-independence | [AT-PEIND-2026]; [PEEC-APS-2026]; [PEEC-APS-2025] |
| AI-related non-attest services to attest clients (developing or hosting AI) | acceptance-independence | [JOFA-ETHICSAI-2026] |
| Understanding the entity's use of AI, AI-enabled fraud (altered training data, fictitious documents), model drift, data governance, human-in-the-loop expectations | planning-risk-assessment (supports -06) | [AT-AICPAPA-2026], section one |
| Substantive testing of AI outputs versus tests of controls; AI-related IT controls | assurance-over-ai-03 and substantive-testing | [AT-AICPAPA-2026], response paragraphs |
| Service auditor's report and AI-related management representations for bought AI | assurance-over-ai-07 | [AT-AICPAPA-2026], service-organisation paragraph |
| Second AI tool checking the first (does not reduce review duties) | quality-management-22 | [AT-AICPAPA-2026] |
| Engagement-letter AI disclosure: AU-C 210 plus state laws | quality-management-24 | [AT-AICPAPA-2026]; [CFODIVE-AIPA-2026] |
| Citrin Cooperman and PKF O'Connor Davies DAS platform adoption (audit, PCR, EBP) | new private-company-assurance (and benefit-plan-audits for DAS EBP) | [CASEWARE-CITRIN-2026]; [CASEWARE-PKF-2026] |
| Peer-review data by engagement type (reviews 13 of 99, single audits 2 of 11, ERISA 2 of 21, GAGAS other 1 of 29) | private-company-assurance, benefit-plan-audits, nonprofit-government | [TSCPA-PEERREVIEW-2025], section II.2.c |
| Oath's service lines (EBP, non-profit, private funds) | benefit-plan-audits; nonprofit-government | [OATH-SITE-2026] |
| PE scale figures and PE funding of AI platforms | archetype economics.md and disruption.md | [AT-PCAOBPE-2025]; [IFAC-PE-2026]; [CFOBREW-PE-2026] |
| Registered-report design on PE and audit quality | archetype sources.md (academic) | [BORYSOFF-PE-2024] |

## 5. Sources

49 rows. Read column: `full` = opened and read (some only in part, noted); `search-only` = seen only in search results.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AICPA-AIPA-2026 (= AICPA-PA-2026) | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| AICPA-AIPARES-2026 | Explore new AICPA guidance on AI and the financial statement audit (resource page; practice aid PDF is member-only and was not read) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/explore-new-aicpa-guidance-on-artificial-intelligence-ai-and-the-financial-statement-audit | 2026-10-12 | full (landing page only) |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| CFODIVE-AIPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 | full |
| CPAPA-AIPA-2026 | AICPA Practice Aid Provides Guidance to Auditors on AI Use in Financial Statement Audits | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191588 | 2026-10-13 | full |
| AICPA-AIUCPR-2026 | Auditors Meet Urgent Demand for AI Assurance with New Offering from AICPA and AIUC | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/news/article/auditors-meet-urgent-demand-for-ai-assurance-with-new-offering-from-aicpa-and-aiuc | 2026-10-19 | full |
| AICPA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/ | 2026-10-19 | full |
| AT-AIUC-2026 | New AI assurance certification combines SOC 2, AIUC-1 | Accounting Today | press | https://www.accountingtoday.com/news/new-ai-assurance-certification-combines-soc-2-aiuc-1 | 2026-10-19 | full |
| JOFA-MATHEX-2026 | Problem solved: A math example of CPA-led assurance using AI agents | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/oct/problem-solved-a-math-example-of-cpa-led-assurance-using-ai-agents/ | 2026-10-19 | full |
| AT-AUDITRISK-2026 | AI didn't invent audit risk, so what actually changed? | Accounting Today (AT Think) | press | https://www.accountingtoday.com/opinion/ai-didnt-invent-audit-risk-so-what-actually-changed | 2026-10-13 | full |
| AT-ACCAETH-2026 | Majority of accountants agree AI is profession's top ethical challenge (ACCA survey) | Accounting Today | survey | https://www.accountingtoday.com/news/majority-of-accountants-agree-ai-is-professions-top-ethical-challenge | 2026-10-15 | full |
| PEEC-APS-2026 (= JOFA-PEEC-2026) | PEEC to continue discussions on alternative practice structures | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/peec-to-continue-discussions-on-alternative-practice-structures/ | 2026-08-10 | full |
| PEEC-APS-2025 | AICPA proposes changes to independence guidelines related to private equity | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2025/dec/aicpa-proposes-changes-to-independence-rules-related-to-private-equity/ | 2025-12-19 | full |
| AT-PEIND-2026 | AICPA weighs PE and tech impact on audit independence | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-weighs-pe-and-tech-impact-on-audit-independence-rules | 2026-08-31 | full |
| AT-PCAOBPE-2025 | PCAOB warns auditors about AI and PE | Accounting Today | press | https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 | full |
| CFOBREW-PE-2026 | 10 of the top 20 CPA firms are backed by private equity | CFO Brew | press | https://www.cfobrew.com/stories/10-of-the-top-20-cpa-firms-are-backed-by-private-equity | 2026-06-26 | full |
| IFAC-PE-2026 | Private Equity Investment in Accountancy: IFAC Releases Research and Online Resource | IFAC | professional-body | https://www.ifac.org/news-events/2026-03/private-equity-investment-accountancy-ifac-releases-research-and-online-resource | 2026-03-02 | full |
| BORYSOFF-PE-2024 | Does Private Equity Investment in Accounting Firms Affect Perceived and Actual Audit Quality? (registered report proposal) | The Accounting Review (authors at George Mason, Wake Forest, Boston University) | academic | https://business.gwu.edu/sites/g/files/zaxdzs5326/files/2024-06/maria_nykyforovych.pdf | 2024-06 (PDF creation date 2024-06-03) | full |
| JOFA-ETHICSAI-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA Professional Ethics Division) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| JOFA-CYBERCHK-2026 | New checklist helps CPAs manage AI cyber risks | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/ | 2026-10-01 | full |
| JOFA-PEER-2026 (= JOFA-PRB) | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 | full |
| JOFA-FAST-2026 (= JOFA-FAST) | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 | full |
| JOFA-SOCETH-2026 | SOC engagements: Ethics risks with tool providers | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/apr/soc-engagements-ethics-risks-with-tool-providers/ | 2026-04-06 | full |
| JOFA-QMPR-2024 | How the new QM standards may affect peer review | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2024/dec/how-new-qm-standards-may-affect-peer-review.html | 2024-12-10 | full |
| JOFA-QMRES-2025 | AICPA unveils new QM resources to help firms meet Dec. 15 deadline | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2025/aug/aicpa-unveils-new-qm-resources-to-help-firms-meet-dec-15-deadline/ | 2025-08-12 | full |
| AICPA-QMPR-2026 | New QM Peer Review Checklists: What Firms Need to Know (CPEA report; member-only, teaser read) | AICPA & CIMA | standard-setter | https://www.aicpa-cima.com/resources/article/new-qm-peer-review-checklists-what-firms-need-to-know | 2026-08-14 | full (teaser only) |
| AICPA-REVALERT-2026 | Reviewer Alert, six editions (Oct 2025, Dec 2025, Feb 2026, May 2026, Jun 2026, Sep 2026); tables of contents only | AICPA & CIMA Peer Review Program | standard-setter | https://www.aicpa-cima.com/news/download/reviewer-alert-september-2026-edition | 2026-09-23 (latest edition; others 2025-10-27, 2025-12-03, 2026-02-16, 2026-05-13, 2026-06-29) | full (titles only) |
| AICPA-PEERCONF-2026 | AICPA Peer Review Conference | AICPA & CIMA | conference | https://www.aicpa-cima.com/cpe-learning/conference/aicpa-peer-review-conference | 2026-08-10 (event start) | full |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities (2025) | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 | full |
| STATE-PR-2025 | 2025 annual peer review reports of VSCPA, MNCPA, CTCPA, OSCPA and GSCPA (figures from search-result summaries; documents not opened) | State CPA societies | professional-body | https://www.vscpa.com/storage/assets/PDFs%20and%20Docs/Annual%20Report%20on%20Peer%20Review%20Activities%202025.pdf (and four others) | 2026 | search-only |
| CPACOM-QMCORE-2026 | QMCore (page text has no mention of AI) | CPA.com (with FinReg Global) | vendor | https://www.cpa.com/qmcore | 2026-10 (HTTP last-modified 2026-10-15) | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (54 US firms) | CPA.com and AICPA | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| AUDITFILE-QL-2025 | AuditFile Announces Launch of QualityLink | AuditFile | vendor | https://auditfile.com/pr/12_4_25 | 2025-12-04 | full |
| CASEWARE-CITRIN-2026 | Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| CASEWARE-PKF-2026 | PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program | Caseware | vendor | https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program | 2026-10-08 | full |
| OATH-SITE-2026 | Oath home page ("Swear by your numbers") | Oath | firm | https://www.oathverified.com/ | 2026-10 (live page, undated) | full |
| KAUFMAN-JOB-2026 | Cybersecurity Risk Advisory Senior Manager (job posting) | Kaufman Rossin via Workable | job-posting | https://jobs.workable.com/view/1f4ea4b5-e0d5-4cd7-9e2b-4befaf13dad6 | 2026-10-07 | full |
| ICAS-AMBS-2026 | ICAS study finds widespread concern over genAI accounting errors (study by Alliance Manchester Business School and Aston Business School at Beever and Struthers) | The Accountant | academic | https://www.theaccountant-online.com/news/icas-study-finds-widespread/ | 2026-03-17 | full (press report; study not opened) |
| CSA-SOC2 | The SOC 2 AI Gap: Auditors Improvise Where AICPA Has Not Acted | Cloud Security Alliance (AI Safety Initiative) | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 | full |
| AIUC-SITE-2026 | AIUC-1 Standard (home and process page) | AIUC | vendor | https://www.aiuc-1.com/ | 2026-10 (live page; latest item listed 15 Oct 2026) | full |
| SCHELLMAN-AIUC1-2026 | Schellman becomes the first accredited auditor for AIUC-1 (AIUC-hosted copy, updated 2 Apr 2026) | AIUC / Schellman | vendor | https://www.aiuc-1.com/research/schellman-becomes-first-accredited-auditor | 2026-02-03 | full |
| AIUC-Q3-2026 | Q3-2026 update: AIUC-1 for coding agents, and technical auditor guidance | AIUC | vendor | https://www.aiuc-1.com/research/2026-q3-standard-update | 2026-07-14 | full |
| AIUC-Q4-2026 | Q4-2026 release: Open-weight model controls and stronger third-party testing | AIUC | vendor | https://www.aiuc-1.com/research/2026-q4-standard-update | 2026-10-15 | full |
| AIUC-MSCI-2026 | How MSCI secures its highest-risk AI agents with AIUC-1 | AIUC | vendor | https://www.aiuc-1.com/research/how-msci-secures-its-highest-risk-ai-agents-with-aiuc-1 | 2026-09-24 | full |
| AIUC-FIN-2025 | Case study: How Fin built enterprise trust for customer-facing AI agents (updated Oct 2026) | AIUC | vendor | https://www.aiuc-1.com/research/case-study-fin | 2025-12-11 | full |
| SCHELLMAN-BLOG-2026 | Why One AI Governance Framework Isn't Enough | Schellman | firm | https://www.schellman.com/blog/ai-governance/why-one-ai-governance-framework-isnt-enough | 2026-10-02 | full |
| SCHELLMAN-AIGOV-2026 | Research Report: 2026 State of AI Governance (landing page; full report gated) | Schellman | survey | https://www.schellman.com/whitepaper/2026-state-of-ai-governance | 2026 (page undated) | full (landing page only) |
| SENSIBA-AIUC1-2026 | LinkedIn repost that Sensiba LLP earned provisional AIUC-1 accreditation, with a first engagement under way (from a search summary; not opened) | LinkedIn (via search) | community | https://ie.linkedin.com/in/doneganshane9 | 2026 | search-only |

Alias note: `AICPA-AIUC-2026` is the landscape's key for the Journal of Accountancy article on the joint offering; the AICPA release itself is `AICPA-AIUCPR-2026`.

Source count by type: press 14, professional-body 10 (incl. 1 search-only group), vendor 10, standard-setter 5, survey 3, firm 2, academic 2, conference 1, job-posting 1, community 1 (search-only). Total 49, of which 47 were opened (three only in part: landing page or teaser) and 2 are search-only.

## 6. Gaps

- **Practice aid text.** The 51-page AICPA practice aid is member-only. I read the AICPA release, the Journal of Accountancy, CPA Practice Advisor, CFO Dive and a long Accounting Today summary, but not the document, so no page locators and no check of what its size-specific guidance says about small firms. No commentary on the practice aid from a mid-market firm was found.
- **AI-related peer-review findings.** None found. Reviewer Alert article text, the AICPA's QM peer review checklist report (Aug 2026), the Peer Review Board's APS item (May 2026 alert), Peer Review Conference session content, and AICPA Peer Review Board minutes were behind logins or not published. The state reports other than Tennessee were seen only in search summaries. An absence of AI in public peer-review data therefore proves little about what reviewers have begun to ask.
- **First QM-era peer reviews.** No source reports what the first reviews under the new standards found.
- **Joint SOC 2 plus AIUC-1 offering.** No mid-market CPA firm is named as delivering it; PwC is the only name. No pricing, scope document, pilot result or timeline beyond "early 2027". The AICPA release wording (certification) versus SOC 2 as an attestation was not resolved with the AICPA. The Sensiba AIUC-1 accreditation was not verified from a primary source. AIUC's page lists Schellman and Coalfire as example accredited auditors; Coalfire's own announcement was not found.
- **PE and APS effects.** No audit-quality measurement exists. The one academic item is a 2024 proposal on public-company clients. PCAOB statements were read through Accounting Today, not from PCAOB text (pcaobus.org returned 403 to direct fetch). The outcome of PEEC's October 2026 interim meeting was not found. Whether the Crowe and Eide Bailly deals closed was not checked. No source ties PE funding to a specific firm AI programme or to quality-management practice.
- **Small-firm AI governance data.** The only firm-size evidence is the 54-firm AICPA and CPA.com survey, which is not representative and has no size breakdown for AI findings. The Karbon 2026 survey figure for firms with an AI policy was not re-verified because the PDF text layer is garbled. No small-firm worked example of an AI risk and response in an SQMS 1 risk assessment was found.
- **Discourse.** No podcast or community discussion on these topics was read (r/taxpros and AICPA communities not reachable; The Accounting Podcast not retrieved). Conference evidence is limited to the Peer Review Conference listing; ENGAGE 2026 and state-society sessions were not re-opened for this module. The Accountancy Europe paper for small and medium practices could not be reached (404).
- **Regulator primary sources.** No direct regulator text was opened: the PCAOB, SEC and ASB statements appear through press only.
- **Mid-market quality evidence.** No error rate, override rate, parallel-run result or independent measurement of AI tools at a mid-market firm exists in any source read; the Schellman 74% and 27% figures are a vendor survey of enterprises, not of assurance firms.
