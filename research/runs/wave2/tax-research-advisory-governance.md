# Tax / research-advisory: governance and evidence

- **Archetype:** tax. **Module:** research-advisory (tax research, technical memos, planning and advisory by firm advisers and in-house tax counsel).
- **Angle:** governance (regulator and professional-body statements, courts, standards, academic studies, surveys and benchmarks).
- **Prepared:** 2026-10-17 (wave 2). Working folder: private `mktemp -d`; nothing was written to the shared scratchpad.
- **Method:** primary documents were fetched with `curl`, `pdftotext` and the `r.jina.ai` mirror (TPB, Bloomberg Law, preprints.org). Nine web searches were used (the ~800-citations source, M&A tax AI, E&O insurance, HMRC and tribunal material, independent tool evaluations, reasonable-cause reliance, the HMRC guidelines page, Deloitte Australia, Khoja). Sources are marked `access: full` only where the page or document was opened and read.

---

## 1. Summary

- **Every conduct regulator that has spoken says the same thing: existing duties apply, the practitioner is accountable, and there is no AI-specific safe harbour.** IRS OPR Alert 2026-19 (24 Jun 2026) maps AI use onto Circular 230 sections 10.22, 10.27, 10.35, 10.36 and 10.37 (written advice) and section 7216. The UK PCRT bodies (19 Jan 2026) tell members to treat AI output like a junior colleague's work. Australia's TPB Guidance Statement 55/2026 (22 Jul 2026) says AI "cannot be relied on as a replacement for tax knowledge", and HMRC's generative-AI guidelines for software developers (28 Jan 2026) require tools to flag nuanced rules and prompt users to check.
- **Courts, not regulators, are where enforcement has actually happened, and the record now includes professional advisers.** *Clinco* (T.C. Memo. 2026-16) is the first Tax Court case on hallucinated citations by a lawyer, with an admonishment and no formal sanction. *Elden v HMRC* (UK First-tier Tribunal, Jan 2026) criticised an ICAEW-regulated accountancy firm for unverified AI output in a skeleton argument. A *Riddle Aggregates* expert report was challenged over hallucinated citations at trial and is recorded as withdrawn (Mar 2026). Bloomberg Law reports an IRS motion citing a nonexistent case (*Khoja*, Mar 2026). The Charlotin database lists about 2,200 hallucination decisions worldwide, 25 of them tagged tax as primary field.
- **Independent measurement of tax research quality exists but is thin, and it is unflattering.** Vals AI's Tax Agent Bench (updated 2026-10-16) scores models running a research harness on 193 private corporate-tax research questions. The best model on its leaderboard is fully correct on 49.19% (citation-adjusted), and Forms and Filings plus Controversy and Precedence are the weakest categories. Stanford's 2024 study of commercial legal research tools found 17% to 33% hallucination. There is no independent head-to-head test of Blue J, CoCounsel, Bloomberg Tax AI or CCH tools on tax questions, and no regulator inspection findings on AI in tax advice.
- **Governance is the live tension in the business model.** OPR told practitioners to credit clients for AI efficiencies and not bill manual time not spent. The AICPA is asking the IRS to clarify, calling the language "overly simplistic" on value pricing (JofA, 8 Sep 2026). Practitioner surveys show the control gap: Fonoa (indirect tax, n=176) found 57.4% would not be confident defending AI-assisted decisions to a tax authority, and at the TEI Tax Technology Seminar two hands out of more than 50 said tax owns AI implementation.
- **Evidence grades for the 16 candidate use cases:** A 1, B 3, C 4, D 8. Only one use case (agentic research) has a measured outcome for exactly this module's task, and that measurement is of models in a benchmark harness, not of a firm's deployment.

---

## 2. Use cases

```yaml
- id: tax-research-advisory-01
  title: Grounded tax research assistant answering research questions with linked authority
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Advisers spend hours locating the controlling Code section, regulation, ruling or case and reading them
    to answer a technical question. General chatbots return confident citations that may not exist.
  solution: >-
    A research assistant retrieves from a curated tax content set, answers in natural language and links each
    statement to the source so the adviser can open and read it. KPMG describes a GenAI Research Assistant
    for Navigating Tax used in M&A tax that returns targeted research with references to statute and case law.
    Vendor material (Bloomberg Tax) describes retrieval-augmented answers with citations that refrain from
    answering when reliable content is missing. The adviser reads the cited authority before relying on it.
  outcomes:
    - lever: quality
      description: >-
        Independent preregistered study of commercial legal research tools (Lexis+ AI, Westlaw AI-Assisted
        Research, Ask Practical Law AI). Adjacent process (legal, not tax, research) so it caps this entry at B.
      figure: "17% to 33%"
      measures: >-
        share of responses that hallucinate, per tool, on the study's preregistered legal research query set
        (the abstract says each tool hallucinates between 17% and 33% of the time)
      provenance: independent
      source_ref: STANFORD-HALLUC-2024
    - lever: quality
      description: >-
        Independent study of four AI research products on 200 US legal research questions: average weighted
        score of the AI products against a lawyer baseline. Adjacent process (legal research).
      figure: "74%-78% (AI products) versus 69% (lawyer baseline)"
      measures: >-
        average weighted score across accuracy (50%), authoritativeness (40%) and appropriateness (10%) on
        200 US legal research questions
      provenance: independent
      source_ref: VALS-VLAIR-2025
    - lever: speed
      description: >-
        Survey of German corporate tax departments: users of AI tools reporting time savings. Covers all tax AI
        use (including researching tax information), not research alone; sample size not stated.
      figure: "66%"
      measures: "share of AI users in the KPMG quick survey who report noticeable time savings"
      provenance: self-reported
      source_ref: KPMG-DE-2026
  prerequisites:
    - Approved, enterprise-grade tool with client-data protections (OPR names only secure, enterprise-approved AI for client data)
    - Licensed access to authoritative tax content the tool retrieves from
    - A firm AI policy with approved-tool list, named AI lead or committee and training
  risks_and_guardrails:
    - Retrieval does not eliminate hallucination; the Stanford study found 17% to 33% rates for retrieval-based commercial tools (STANFORD-HALLUC-2024, abstract)
    - OPR says practitioners must verify facts, citations and calculations and cannot rely solely on AI (IRS-OPR-2026, Circular 230 section 10.22 discussion)
    - PCRT says output should be regarded as if prepared by a less experienced junior colleague and reviewed with scepticism; confirm that referenced law exists (PCRT-AI-2026, para 3.4)
    - The Bloomberg Tax claims about its own tool are vendor statements without published error rates (BTAX-HALLUC-2026)
    - Tools that restrict sourcing to a proprietary database can lag on very recent guidance (VALS-VLAIR-2025, key finding 2)
  human_checkpoints:
    - Adviser opens and reads each cited authority before it goes into a memo
    - Reviewer confirms the authority is current and applies to the client's facts
  role_evolution: >-
    PCRT frames the adviser as the reviewer of a junior colleague's work (PCRT-AI-2026, para 3.4). KPMG says AI tools free
    practitioners to focus on analysis and client-specific insight (KPMG-MATAX-2025, p. 1).
  evidence_grade: B
  sources:
    - {ref: KPMG-MATAX-2025, title: "How generative AI is transforming mergers and acquisitions tax", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf", date: "2025-06", access: full, locator: "p. 1, 'Tax research with GenAI Research Assistant for Navigating Tax'"}
    - {ref: STANFORD-HALLUC-2024, title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools", publisher: Stanford RegLab / HAI authors (arXiv 2405.20362), type: academic, url: "https://arxiv.org/abs/2405.20362", date: "2024-05-30", access: full, locator: abstract}
    - {ref: VALS-VLAIR-2025, title: "VLAIR - Legal Research", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/industry-reports/vlair-10-14-25", date: "2025-10-14", access: full, locator: "Executive summary and Key findings 1-3"}
    - {ref: BTAX-HALLUC-2026, title: "AI Hallucinations in Tax: The Risks and How to Mitigate Them", publisher: Bloomberg Tax, type: vendor, url: "https://pro.bloombergtax.com/?p=16920", date: "2026-05-11", access: full, locator: "section 'How Bloomberg Tax AI addresses hallucination risks'"}
    - {ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence (KPMG quick surveys)", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-06", access: full, locator: "key findings"}
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 section 10.22"}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "paras 3.4-3.7"}
  last_reviewed: 2026-10-17
  notes: >-
    Measured error rates are from legal research tools (adjacent process), not tax research tools. No tax-specific
    independent test of a commercial research product was found. The KPMG 66% figure is for all AI uses by German tax
    departments, with sample size not stated, and is not specific to research.

- id: tax-research-advisory-02
  title: Agentic multi-step tax research producing a memo-style answer with citations
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: piloting
  problem: >-
    A corporate tax research question usually needs several chained lookups (statute, regulation, guidance, forms,
    prior-year rules) and an early error in a threshold, date or citation carries through to the answer.
  solution: >-
    An agent with tools for authority lookup by citation, web search, document fetch, retrieval and a calculator
    researches a written question over many steps and submits one written answer with citations. Vals AI built a
    benchmark of this task for corporate tax. KPMG announced agent-building inside its Digital Gateway (Claude),
    with an initial focus on tax clients, and says building an agent to help clients adjust to changing tax rules
    went from weeks to minutes.
  outcomes:
    - lever: quality
      description: >-
        Highest score on the Tax Agent Bench leaderboard as read on 2026-10-17 (private test set, models run in the
        Vals harness, not commercial tax products). Accuracy requires every expert rubric check to pass and is
        adjusted for the share of cited sources that resolve to real authorities.
      figure: "49.19%"
      measures: >-
        share of the 193 private test questions answered fully correct (all rubric checks pass), multiplied by
        (0.7 + 0.3 x citation quality); a question not answered within the three-hour limit scores 0
      provenance: independent
      source_ref: VALS-TAXAGENT-2026
    - lever: quality
      description: >-
        Weakest categories by best score on the page: Forms and Filings, and Controversy and Precedence Analysis.
        The page reports category medians of 13.33% and 6.67%.
      figure: "40.00% and 36.67% (best model per category, 30 test questions each)"
      measures: "share of the 30 test questions in the category answered fully correct, citation-adjusted"
      provenance: independent
      source_ref: VALS-TAXAGENT-2026
    - lever: speed
      description: >-
        KPMG US tax vice chair statement about building a client agent for changing tax rules (announcement quote,
        not a measured study).
      figure: "weeks to minutes"
      measures: "time to build an AI agent that helps clients adjust to changing tax regulations, as stated by KPMG US tax leader Rema Serafi; no sample or method given"
      provenance: self-reported
      source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
    - Authority sources the agent can fetch by citation (statutes, regulations, guidance) and a way to check that citations resolve
    - Rubric-based or expert review of outputs, since fully correct answers were the minority on the benchmark
    - Budget for long runs (the leaderboard shows cost per task up to about $15 and run times up to about an hour)
  risks_and_guardrails:
    - Fully correct answers are the minority even for the best model (VALS-TAXAGENT-2026, Results)
    - Agent answers are far longer than expert reference answers (601-word reference mean against 2,366 words for the leading model), which raises review burden (VALS-TAXAGENT-2026, Answer Length)
    - The Vals page text mixes figures from an earlier analysis set with the updated leaderboard; treat the leaderboard table as the current record (VALS-TAXAGENT-2026)
    - Werfel's preparer register lists control dilution (volume and speed outpace review) and agentic AI risk as distinct failure modes, and recommends piloting with limited scope (TAXADVISER-WERFEL-2026, Figure 3 and closing recommendations)
    - PwC says policy interpretation and high-touch consulting remain areas where AI use is limited (PWC-MEGNA-2025)
  human_checkpoints:
    - A qualified adviser reviews the final memo and the authorities before it reaches a client
    - "Phased scope per Werfel: restrict to document summarisation first, authorise position drafting only after verification protocols are tested"
  role_evolution: >-
    Werfel's preparer register lists skill erosion (staff learn the tools, not the law) and institutional knowledge loss
    as workforce risks (TAXADVISER-WERFEL-2026, Figure 3). Thomson Reuters Institute's paper says firms must
    ensure juniors still get structured development before automation erodes it (TR-FOP-2026).
  evidence_grade: A
  sources:
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-16", access: full, locator: "Results, Performance by Category, Scoring, Dataset"}
    - {ref: KPMG-ANTHROPIC-2026, title: "KPMG Partners with Anthropic for Digital Gateway Powered by Claude", publisher: CPA Practice Advisor (KPMG release), type: firm, url: "https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/", date: "2026-05-20", access: full, locator: "Serafi quote, paragraph beginning 'Building an AI agent'"}
    - {ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: "2026-08-31", access: full, locator: "Figure 3 and Tax Preparers register steps"}
    - {ref: PWC-MEGNA-2025, title: "How PwC's Dom Megna is using agentic AI in tax (CFO.com interview)", publisher: CFO.com, type: firm, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: "2025-06-06", access: full, locator: "answer on lines humans only"}
    - {ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: "2026-07-21", access: full, locator: "priority 'Define the role of early-career professionals'"}
  last_reviewed: 2026-10-17
  notes: >-
    Grade A reflects a measured outcome by a named independent evaluator on exactly this task, but the measured
    systems are models in Vals' harness, not a firm's production deployment. Vals sells evaluation services and
    licenses the private validation set. The Vals page is internally inconsistent: narrative paragraphs quote higher
    accuracy figures (for example 65.2% for a model now listed at 30.04%) from an earlier analysis set. Only the
    leaderboard table and the category statements were used here. The task covers corporate tax research (about 60%
    federal corporate income tax) and is not a measure of advisory judgment or opinion quality.

- id: tax-research-advisory-03
  title: Automated authority-existence and citation check on memos, opinions and filings before release
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Fabricated or misdescribed citations reach client memos and court filings. In Clinco, three of four cited cases did
    not exist, and counsel repeated one after the IRS flagged it. Manual cite-checking of every authority is slow.
  solution: >-
    A checker resolves every citation in a draft against authoritative sources and flags those that do not exist or
    do not support the stated proposition, for a person to clear. Charlotin offers PelAIkan, an automated reference
    checker built on his hallucination database. The Vals benchmark penalises answers whose cited sources do not
    resolve, which shows citation resolution can be tested mechanically.
  outcomes:
    - lever: risk
      description: "none published for tax memos; the checker described on the database page has no published error rates"
      figure: "none published"
      measures: "not applicable"
      provenance: vendor-published
      source_ref: CHARLOTIN-DB-2026
  prerequisites:
    - Access to authoritative sources to resolve citations against (Code, regulations, reporters, tribunal databases)
    - Policy requiring a verification log or second-reviewer cross-check for litigation work (JofA suggests both)
  risks_and_guardrails:
    - An existence check does not show the case supports the proposition; the UK tribunal in Zzaman found real cases that did not support the argument (ICAS-TAXTRIB-2026)
    - OPR says citations must be checked and cases read for written advice (IRS-OPR-2026, section 10.37 discussion)
    - JofA recommends citation-verification logs or a second reviewer before filing (TAXCT-CLINCO-2026)
  human_checkpoints:
    - Person clears every flagged citation and reads the authorities that carry the argument
  role_evolution: >-
    Verification becomes an explicit, logged step in the engagement file; the OPR and PCRT guidance both expect documented
    verification (IRS-OPR-2026, best practices; PCRT-AI-2026, para 1.4 safeguards).
  evidence_grade: C
  sources:
    - {ref: CHARLOTIN-DB-2026, title: "AI Hallucination Cases Database", publisher: Damien Charlotin, type: academic, url: "https://www.damiencharlotin.com/hallucinations/", date: "2026-10-16", access: full, locator: "header text on PelAIkan"}
    - {ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: "2026-09-01", access: full, locator: "sections on Clinco and firm policies"}
    - {ref: ICAS-TAXTRIB-2026, title: "AI at the tax tribunal", publisher: ICAS, type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/ai-at-the-tax-tribunal/", date: "2026-01-26", access: full, locator: "Zzaman summary"}
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "section 10.37"}
  last_reviewed: 2026-10-17
  notes: >-
    No tax-specific deployment or accuracy figure for an automated citation checker was found. Graded C because the
    only support is a tool described by its builder.

- id: tax-research-advisory-04
  title: AI-assisted drafting of technical memos and advisory reports from facts and researched authority
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Writing the client memo or advice note from research notes and facts is a large share of adviser time, and quality
    and style vary across teams.
  solution: >-
    The tool produces a first draft or outline from supplied facts and authorities; the adviser edits it and owns the
    conclusion. KPMG describes GenAI tools that prepare an initial due diligence report from jurisdiction, transaction type and
    client constraints, and a Writing Review Assistant that unifies style and defined terms. The PCRT guidance lists
    report writing for tax advisory (for example an inheritance tax overview) as a current use.
  outcomes:
    - lever: speed
      description: "KPMG says its tools compress tax analysis in M&A (marketing statement, no sample or method)"
      figure: "weeks of tax analysis into minutes"
      measures: "not defined in the source; a general statement on the KPMG M&A tax web page"
      provenance: self-reported
      source_ref: KPMG-MATAX-2025
  prerequisites:
    - Facts and authorities are supplied or retrieved from controlled sources, not recalled by the model
    - Engagement-letter language on AI use and a rule on when to disclose actual use (PCRT 1.3)
  risks_and_guardrails:
    - A report prepared for the Australian government by Deloitte Australia contained invented quotes and references to non-existent reports and led to a reported partial fee refund (IRS-OPR-2026, section 'Real-World Consequences')
    - In Elden v HMRC, the tribunal said the human who relies on AI bears responsibility for accuracy, and found failure to verify AI output amounted to professional incompetence for a regulated accountant (ICAS-TAXTRIB-2026; and, for the incompetence finding, Ross Martin's case note, ROSSMARTIN-ELDEN-2026)
    - Written advice under section 10.37 must be based on reasonable assumptions and relate law to facts; opaque logic can make reliance unreasonable (IRS-OPR-2026)
    - PCRT expects the adviser to explain how a conclusion was reached and to keep prompt and source records (PCRT-AI-2026, paras 1.4 and safeguards table)
    - Deliverable text that includes client data must stay inside approved, secure tools (IRS-OPR-2026, sections 6713 and 7216(a))
  human_checkpoints:
    - Named adviser reviews and approves every client-facing memo
    - Second reviewer checks authorities for opinion-level or litigation documents
  role_evolution: >-
    KPMG says practitioners shift from compliance toward deeper advisory roles and compares the change to the introduction of Excel (KPMG-MATAX-2025, p. 1-2).
  evidence_grade: B
  sources:
    - {ref: KPMG-MATAX-2025, title: "How generative AI is transforming mergers and acquisitions tax", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf", date: "2025-06", access: full, locator: "p. 1 use cases; p. 2 'Realigning skills'"}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "Examples of AI usage; paras 1.3-1.4"}
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "sections 10.22, 10.37, Real-World Consequences"}
    - {ref: ROSSMARTIN-ELDEN-2026, title: "Accountants' misuse of AI in FTT case (Elden v HMRC)", publisher: Ross Martin Tax, type: press, url: "https://www.rossmartin.co.uk/sme-tax-news/8799-accountants-misuse-of-ai-in-ftt-case", date: "2026-01-27", access: full, locator: "case summary"}
  last_reviewed: 2026-10-17
  notes: >-
    Grade B rests on KPMG naming its own tools as in use; no measurement was published. The page carries conflicting
    date metadata (a 2025 PDF and a 2026-07-29 JSON-LD date); the PDF creation date (2025-06) is used.

- id: tax-research-advisory-05
  title: "M&A tax due diligence: contract review for tax-relevant clauses and first-draft diligence report"
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Tax diligence on a deal means reading long stock purchase and partnership agreements and writing a structured
    report under time pressure.
  solution: >-
    KPMG describes tools that parse lengthy SPAs and partnership agreements, highlight nonstandard clauses and compare
    language to baselines, and that prepare an initial diligence report from jurisdiction, transaction type and client
    constraints, which professionals then build on with their assessments and recommendations.
  outcomes:
    - lever: capacity
      description: "none published with a sample; KPMG states the tools free time for modelling and risk identification"
      figure: "none published"
      measures: "not applicable"
      provenance: self-reported
      source_ref: KPMG-MATAX-2025
  prerequisites:
    - Data-room documents handled in a secure, approved environment with client authority to process them
    - Baseline clause positions for comparison
  risks_and_guardrails:
    - PCRT flags that client data for a transaction under NDA must not go into public AI tools; anonymise or use closed tools (PCRT-AI-2026, confidentiality safeguards)
    - KPMG describes a human-in-the-loop model where citations and hyperlinks validate all AI outputs, plus regular training on spotting inaccuracies (KPMG-MATAX-2025, p. 2)
    - Tax return information has civil and criminal disclosure penalties (IRC sections 6713 and 7216) (IRS-OPR-2026)
  human_checkpoints:
    - Practitioners add their own assessments and recommendations to the AI first draft
    - Citations and hyperlinks in AI output are checked by the team
  role_evolution: >-
    KPMG says the work moves toward deal structuring and specialised tax strategy, with administrative work automated (KPMG-MATAX-2025, p. 1).
  evidence_grade: B
  sources:
    - {ref: KPMG-MATAX-2025, title: "How generative AI is transforming mergers and acquisitions tax", publisher: KPMG US, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf", date: "2025-06", access: full, locator: "pp. 1-2"}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "Mergers/Demergers and Acquisitions example; confidentiality risk table (acquisition under NDA)"}
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "item 6, sections 6713 and 7216(a)"}
  last_reviewed: 2026-10-17
  notes: >-
    The PCRT guidance describes AI use in M&A (identifying targets, due diligence, valuations) as a current example but
    publishes no outcomes. A search for 2026 surveys on AI in M&A tax or tax structuring found none; the KPMG material is
    the only firm source read. No regulator or professional-body statement specific to AI in tax diligence was found.

- id: tax-research-advisory-06
  title: Tax planning and structuring ideation with client-specific screening
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Finding and testing planning alternatives (structure options, elections, timing) across a large body of authority is
    slow, and advisers may miss options.
  solution: >-
    Idea: an LLM reasons over the law to propose or fill in planning strategies and to test them against authority, with the
    adviser deciding whether any is client-specific, supportable and acceptable. Researchers at Johns Hopkins and the
    University of Maryland evaluated LLMs on interpreting, completing and generating tax-minimisation strategies.
  outcomes:
    - lever: quality
      description: "none published for adviser use; the paper reports that LLM reasoning identified an apparently novel strategy (abstract only was read)"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: JHU-TAXABUSE-2025
  prerequisites:
    - Authority base that is current, since PCRT warns that outdated models can lead to incorrect advice
  risks_and_guardrails:
    - PCRT tax-planning standards require planning to be specific to the client's facts; a tool built for common scenarios may embed assumptions that do not fit (PCRT-AI-2026, objectivity risk table and para 3.2 reference)
    - Where AI output includes items resting on material uncertainty in the law, the member should disclose that to the client (PCRT-AI-2026, para 1.5)
    - Public AI tools may surface sources that promote particular tax planning approaches or schemes (PCRT-AI-2026, competence risk table)
  human_checkpoints:
    - Adviser decides whether any option is client-specific and supportable before it is presented
  role_evolution: >-
    The adviser remains responsible for the planning standard; AI adds options but not accountability (PCRT-AI-2026, introduction).
  evidence_grade: D
  sources:
    - {ref: JHU-TAXABUSE-2025, title: "Can LLMs Identify Tax Abuse?", publisher: Johns Hopkins / University of Maryland authors (arXiv 2508.20097), type: academic, url: "https://arxiv.org/abs/2508.20097", date: "2025-08-10", access: full, locator: abstract (v2 revised 2026-01-21)}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "paras 1.5, 3.7 and objectivity risk table"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The academic work is framed as a tool for tax agencies against abusive planning, not as adviser tooling. Only
    the abstract was read, so no results were extracted. Deloitte's survey line that 10% of respondents experiment with AI
    for tax planning was seen in search extracts only and is not used.

- id: tax-research-advisory-07
  title: LLM-to-rules computation of tax effects in advice (LLM translates, deterministic engine calculates)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Advice often turns on a computation (tax tables, eligibility, multi-step interactions). Language models alone get
    these wrong in ways that are hard to see.
  solution: >-
    Use the model to translate rules or fact patterns into formal logic or inputs for a deterministic engine that does the
    arithmetic, and keep the logic trace as part of the file. JHU researchers tested a hybrid of LLM translation and a
    symbolic solver on the SARA statutory reasoning dataset. Column Tax's benchmark argues tax calculation needs
    deterministic engines and extra infrastructure around LLMs. The Vals harness gives agents a calculator tool.
  outcomes:
    - lever: quality
      description: >-
        Best result for models computing simplified 2024 US federal personal returns, given complete inputs (compliance
        calculation, an adjacent process, so it caps this entry at B). Authors sell deterministic tax-engine technology.
      figure: "32.35% strict (best model); 51.96% lenient (within plus or minus $5 on every line)"
      measures: >-
        share of the 51 test returns computed correctly on every evaluated line (strict) or within plus or minus $5 on every line (lenient), best model
      provenance: vendor-published
      source_ref: COLUMN-TAXCALCBENCH-2025
  prerequisites:
    - A deterministic engine or formalised rule set for the computation
    - Inputs captured completely (the benchmark assumes document collection and preparation are done)
  risks_and_guardrails:
    - JHU argues auditability, not raw accuracy, is the bottleneck, and proposes a cost model based on real penalties for errors (JHU-TAXREASON-2025, abstract)
    - Pure-LLM calculation misused tax tables, mis-calculated and misjudged eligibility in the Column benchmark (COLUMN-TAXCALCBENCH-2025, abstract)
    - TEI attendees flagged errors that fail quietly and politely, and rising token costs (TEI-TAXTECH-2026)
  human_checkpoints:
    - Adviser reviews inputs and assumptions and the explanation of the calculation
  role_evolution: >-
    The calculation trace becomes part of the deliverable; PwC says its effective-tax-rate model is trained to explain inputs,
    outputs and assumptions, and approved logic is locked (PWC-MEGNA-2025).
  evidence_grade: C
  sources:
    - {ref: COLUMN-TAXCALCBENCH-2025, title: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task", publisher: Column Tax (arXiv 2507.16126), type: academic, url: "https://arxiv.org/abs/2507.16126", date: "2025-07-22", access: full, locator: "abstract; results table"}
    - {ref: JHU-TAXREASON-2025, title: "Language Models and Logic Programs for Trustworthy Tax Reasoning", publisher: Johns Hopkins University (arXiv 2508.21051), type: academic, url: "https://arxiv.org/abs/2508.21051", date: "2025-08-28", access: full, locator: "abstract (v3 revised 2026-02-05)"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "paragraphs on quiet failure and human-in-the-loop volume"}
    - {ref: PWC-MEGNA-2025, title: "How PwC's Dom Megna is using agentic AI in tax (CFO.com interview)", publisher: CFO.com, type: firm, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: "2025-06-06", access: full, locator: "answer on explainability of effective tax rate model"}
  last_reviewed: 2026-10-17
  notes: >-
    The benchmark measures return preparation arithmetic, not advisory modelling; no advisory-specific measurement was found.
    Graded C: research results and a vendor-authored benchmark, no named advisory deployment.

- id: tax-research-advisory-08
  title: Law-change and guidance monitoring with client-specific impact notes
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [research-synthesis, client-interaction]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Tax law and guidance change continually; models trained on static data answer with outdated rules, and advisers must
    work out which changes matter to which client.
  solution: >-
    A monitoring agent watches new law and guidance and drafts short impact notes for affected clients or matters for adviser
    review. KPMG announced a platform where clients and professionals build agents to help adjust to changing tax rules.
  outcomes:
    - lever: speed
      description: "KPMG US tax vice chair statement on building such an agent (announcement quote)"
      figure: "weeks to minutes"
      measures: "time to build an AI agent that helps clients adjust to changing tax regulations, per Rema Serafi; no sample or method given"
      provenance: self-reported
      source_ref: KPMG-ANTHROPIC-2026
    - lever: quality
      description: >-
        Independent benchmark category for recent law changes and cross-year or cross-jurisdiction comparison. Best model
        shown for Current and Temporal Analysis (30 test questions).
      figure: "66.67% (best model)"
      measures: "share of the 30 Current and Temporal Analysis test questions answered fully correct, citation-adjusted"
      provenance: independent
      source_ref: VALS-TAXAGENT-2026
  prerequisites:
    - Feeds of primary law and guidance that the agent reads directly, not model memory
    - Version control and update discipline for the underlying tools (HMRC expects continuous monitoring and timely updating of data sources)
  risks_and_guardrails:
    - PCRT says outdated AI models can lead to compliance risks and incorrect advice (PCRT-AI-2026, para 3.7)
    - Bloomberg Tax lists training cutoffs and fast-changing guidance as a cause of confident but outdated answers (BTAX-HALLUC-2026)
    - HMRC expects continuous monitoring, version control and timely updates of code and data sources in tax software using generative AI (HMRC-GENAI-2026)
  human_checkpoints:
    - Adviser confirms each flagged change and its client impact before anything is sent
  role_evolution: "not described in the sources"
  evidence_grade: C
  sources:
    - {ref: KPMG-ANTHROPIC-2026, title: "KPMG Partners with Anthropic for Digital Gateway Powered by Claude", publisher: CPA Practice Advisor (KPMG release), type: firm, url: "https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/", date: "2026-05-20", access: full, locator: "Serafi quote"}
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-16", access: full, locator: "Performance by Category"}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "para 3.7"}
    - {ref: HMRC-GENAI-2026, title: "Guidelines for using generative artificial intelligence if you're a software developer", publisher: HMRC (GOV.UK), type: regulator, url: "https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer", date: "2026-01-28", access: full, locator: "testing and deployment processes paragraph"}
    - {ref: BTAX-HALLUC-2026, title: "AI Hallucinations in Tax: The Risks and How to Mitigate Them", publisher: Bloomberg Tax, type: vendor, url: "https://pro.bloombergtax.com/?p=16920", date: "2026-05-11", access: full, locator: "three reasons hallucinations happen"}
  last_reviewed: 2026-10-17
  notes: >-
    The KPMG quote concerns how fast an agent can be built, not how well the monitoring works. No monitoring-specific
    accuracy figure was found. The Vals category is a research-question proxy, not a monitoring test.

- id: tax-research-advisory-09
  title: Firm- or authority-facing client tax question assistant with escalation to an adviser
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Clients and self-preparers ask routine tax questions that consume adviser time, and many already ask general chatbots.
  solution: >-
    Idea: a chatbot answers routine client questions from the firm's approved content, flags nuanced or high-stakes
    questions and routes them to an adviser. The TPB lists chatbot functionality that can give tailored advice as AI
    capability tax practitioners may use. HMRC's guidelines for tax software with generative AI ask for flags on nuanced
    rules and recommendations to seek a qualified tax professional.
  outcomes:
    - lever: experience
      description: "none published for a firm-deployed assistant"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: ANTINOZZI-2024
  prerequisites:
    - Defined scope of questions the assistant may answer, with an escalation path (Werfel gives the example of a chatbot restricted to filing deadlines versus credit eligibility)
    - Client consent and disclosure of AI use in the engagement terms (PCRT 1.3, 4.3; TPB on client permission)
  risks_and_guardrails:
    - A study of general-purpose ChatGPT found correct responses ranged from 39% to 47% across the 2023 and 2024 filing seasons, and it was less accurate on complex, fact-dependent questions (ANTINOZZI-2024, abstract)
    - Self-preparers are influenced by AI advisors and prefer tax-minimising recommendations (SWIDER-2025, abstract)
    - Werfel's registers list over-trust and unauthorised reliance, and a phased rollout that starts with low-stakes factual queries (TAXADVISER-WERFEL-2026, Tax Authorities register step 4)
    - TPB requires permission from each client before client information is entered into AI tools that act as a third party (TPB-AI-2026, Confidentiality section)
  human_checkpoints:
    - Escalation to a qualified adviser for fact-dependent or advice-level questions
  role_evolution: "not described in the sources"
  evidence_grade: D
  sources:
    - {ref: ANTINOZZI-2024, title: "Is ChatGPT an Accurate Source of Information for Uninformed Taxpayers?", publisher: Antinozzi and Cooper (Wealth Strategies Journal posting), type: academic, url: "https://wealthstrategiesjournal.com/2024/06/30/hannah-smith-antinozzi-lauren-cooper-is-chatgpt-an-accurate-source-of-information-for-uninformed-taxpayers-june-18-2024/", date: "2024-06-18", access: full, locator: abstract}
    - {ref: SWIDER-2025, title: "CPAs vs. AI Tax Advisors: Evaluating Reliance Across Advisory Contexts", publisher: University of Oklahoma (AAA Tax Section meeting paper), type: academic, url: "https://aaahq.org/portals/0/documents/meetings/2025/ATA/Papers/3.02_Swider.pdf", date: "2025", access: full, locator: abstract}
    - {ref: TPB-AI-2026, title: "TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct", publisher: Tax Practitioners Board (Australia), type: regulator, url: "https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct", date: "2026-07-22", access: full, locator: "What is AI; Confidentiality"}
    - {ref: HMRC-GENAI-2026, title: "Guidelines for using generative artificial intelligence if you're a software developer", publisher: HMRC (GOV.UK), type: regulator, url: "https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer", date: "2026-01-28", access: full, locator: "human oversight paragraphs"}
    - {ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: "2026-08-31", access: full, locator: "scope-definition step"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The 39% to 47% figure is for ChatGPT 3.5 and 4 in 2023 and 2024 and is not evidence about a governed firm assistant;
    it shows why scope and escalation are central. Swider is a self-prepared-return experiment, not a firm deployment.

- id: tax-research-advisory-10
  title: In-house tax research and technical-question triage with company-wide enterprise AI assistants
  archetype: tax
  module: research-advisory
  function: finance-accounting
  work_types: [research-synthesis, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Corporate tax teams are under-resourced and spend over half their time on reactive work, leaving little time for research
    and proactive analysis.
  solution: >-
    Tax staff use the company's standard AI assistant, and increasingly tax-specific applications, for researching and
    processing tax information and for communication and collaboration with other functions.
  outcomes:
    - lever: speed
      description: "KPMG Germany quick survey of tax departments (sample size not stated in the release); covers all AI use"
      figure: "66%"
      measures: "share of AI users reporting noticeable time savings"
      provenance: self-reported
      source_ref: KPMG-DE-2026
    - lever: capacity
      description: "Thomson Reuters Institute survey of corporate tax departments; adoption snapshot"
      figure: "67% not using GenAI; 58% under-resourced"
      measures: "share of surveyed corporate tax departments not using GenAI (67%); share of respondents saying their department is under-resourced (58%, up from 51%)"
      provenance: vendor-published
      source_ref: TR-CORPTAX-2025
  prerequisites:
    - IT approval and data protection clearance (the biggest hurdles in the KPMG Germany survey were IT approvals 47%, data protection 41%, lack of AI knowledge 41%)
    - A named owner for AI in the tax function
  risks_and_guardrails:
    - Of more than 50 TEI Tax Tech attendees polled, two said the tax function owns AI implementation at their company (TEI-TAXTECH-2026)
    - More than one-third of tax and audit professionals admit to using unauthorized AI tools (TR-FOP-2026)
    - Fonoa found 57.4% of indirect tax leaders would not be confident defending AI-assisted decisions to a tax authority, and only a third run formal human-in-the-loop review (FONOA-2026-SURVEY)
  human_checkpoints:
    - Tax professional reviews output before it informs a position or goes to the business
  role_evolution: >-
    Sala argues AI will not shrink corporate tax teams much because AI cannot hold regulatory, ethical or financial culpability
    and tax practice is more than preparation (SALA-TAXNOTES-2026). KPMG Germany finds most companies expect stable tax headcount (58% domestic, 72% abroad) (KPMG-DE-2026).
  evidence_grade: C
  sources:
    - {ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence (KPMG quick surveys)", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: "2026-05-06", access: full, locator: "key findings; hurdles paragraph"}
    - {ref: TR-CORPTAX-2025, title: "The GenAI paradox: why most tax departments aren't using AI yet", publisher: Thomson Reuters (State of the Corporate Tax Department 2025), type: survey, url: "https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/", date: "2025-10-22", access: full, locator: "key points"}
    - {ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: "2026-05-04", access: full, locator: "governance paragraph"}
    - {ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: "2026-07-21", access: full, locator: "priority 'Govern the tools being used'"}
    - {ref: FONOA-2026-SURVEY, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: "2026-06-17", access: full, locator: "survey questions on defending decisions and validating outputs"}
    - {ref: SALA-TAXNOTES-2026, title: "AI Won't Shrink Corporate Tax Teams Much. Here's Why.", publisher: Tax Notes State via TaxProf Blog, type: academic, url: "https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/", date: "2026-07-20", access: full, locator: abstract}
  last_reviewed: 2026-10-17
  notes: >-
    Surveys are sponsor-produced (Thomson Reuters, KPMG, Fonoa) and use different samples; do not combine figures. The KPMG
    survey does not state its sample size. The Fonoa survey is indirect tax, so its governance figures are adjacent.

- id: tax-research-advisory-11
  title: AI meeting transcription and minutes feeding the factual section of advice notes
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [document-production]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Advice notes depend on an accurate record of client facts discussed in calls and meetings, which is time-consuming to write up.
  solution: >-
    A transcription tool records and summarises client meetings and the summary informs the factual section of the note. The PCRT
    guidance uses this as a worked scenario.
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: PCRT-AI-2026
  prerequisites:
    - Client permission to record and to process the recording with an AI tool
  risks_and_guardrails:
    - PCRT says minutes should be reviewed to ensure they are complete, accurately reflect the discussion and are professionally worded (PCRT-AI-2026, competence risk table)
    - Recording and uploading client conversations engages confidentiality duties (PCRT-AI-2026, section 4)
    - TPB requires client permission before client information is disclosed to third parties, which can include entering it into AI models (TPB-AI-2026, Confidentiality section)
  human_checkpoints:
    - Adviser checks the minutes against what was discussed before relying on them
  role_evolution: "not described in the sources"
  evidence_grade: D
  sources:
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "competence risk table, meeting-minutes scenario"}
    - {ref: TPB-AI-2026, title: "TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct", publisher: Tax Practitioners Board (Australia), type: regulator, url: "https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct", date: "2026-07-22", access: full, locator: Confidentiality}
  last_reviewed: 2026-10-17
  notes: "Idea. Appears only as a scenario in a professional-body guidance document; no deployment or measurement found."

- id: tax-research-advisory-12
  title: Second-model or multi-tool cross-check of research answers before they are relied on
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    A single tool's confident answer can be wrong. Reviewers cannot easily see which answers need deeper checking.
  solution: >-
    Idea: run the same question through more than one tool or model and treat disagreement as a trigger for a deeper human check.
    A Becker CPE course on choosing and testing tax research tools reportedly teaches comparing tool outputs on the same question and watching for a
    consensus trap where tools agree on a wrong answer (seen in a search extract only). PCRT frames output as junior-colleague work to be reviewed with scepticism.
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: PCRT-AI-2026
  prerequisites:
    - Access to more than one approved tool
  risks_and_guardrails:
    - The Vals benchmark shows more tool calls and longer answers did not translate into accuracy, so effort is not a substitute for verification (VALS-TAXAGENT-2026, Tool Use)
    - A consensus between tools is not verification; authorities still need to be read (PCRT-AI-2026, para 3.4)
  human_checkpoints:
    - Disagreements and consensus answers on material points are both checked against primary authority
  role_evolution: "not described in the sources"
  evidence_grade: D
  sources:
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "para 3.4"}
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-16", access: full, locator: "Tool Use"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The Becker course (https://www.becker.com/cpe/catalog/ai-in-tax-practice-choosing-testing-tax-research-tools) was
    seen in a search extract only and has no date, so it is not listed as a dated source.

- id: tax-research-advisory-13
  title: Authority mapping and drafting support for tax opinions and written advice
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Written advice and formal opinions must relate applicable law to facts on reasonable assumptions, and clients and auditors may rely on them
    (including for penalty protection). Assembling and weighing the authority is slow.
  solution: >-
    Idea: AI assembles the authorities, maps them to the facts and drafts the analysis. A person decides the conclusion and signs. Sala asks whether corporates
    could use a highly technical tax AI for direction instead of deferring to an expensive Big Four opinion, and whether opinions are about more than an accurate
    statement of the law.
  outcomes:
    - lever: quality
      description: "none published; the benchmark's best score on controversy and precedence analysis is a related measure"
      figure: "36.67% (best model, Controversy and Precedence Analysis, 30 test questions)"
      measures: "share of the 30 test questions on audits, penalties, appeals, limitation periods, elections and which rules and rulings apply that were answered fully correct, citation-adjusted"
      provenance: independent
      source_ref: VALS-TAXAGENT-2026
  prerequisites:
    - Firm opinion-review process that stays in force
  risks_and_guardrails:
    - Section 10.37 requires reasonable factual and legal assumptions; if the system's logic is opaque, reliance may be unreasonable; practitioners should treat AI advice as a starting point (IRS-OPR-2026, section 10.37)
    - "OPR on competence: lack of technological competence could lead to improper advice (IRS-OPR-2026, section 10.35)"
    - Werfel's register lists liability ambiguity between the signing preparer and the AI vendor, and malpractice exposure (TAXADVISER-WERFEL-2026, Figure 3)
    - Sala argues AI cannot hold regulatory, ethical or financial culpability (SALA-TAXNOTES-2026)
  human_checkpoints:
    - Signing professional owns the conclusion; normal opinion committee or second-partner review still applies
  role_evolution: >-
    Sala predicts limited headcount effect because opinion work involves accountability that AI cannot take (SALA-TAXNOTES-2026).
  evidence_grade: D
  sources:
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "sections 10.35, 10.37"}
    - {ref: SALA-TAXNOTES-2026, title: "AI Won't Shrink Corporate Tax Teams Much. Here's Why.", publisher: Tax Notes State via TaxProf Blog, type: academic, url: "https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/", date: "2026-07-20", access: full, locator: abstract}
    - {ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: "2026-08-31", access: full, locator: "Figure 3"}
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-16", access: full, locator: "Performance by Category"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea discussed by commentators. A search on reasonable-cause or preparer-penalty reliance on AI-generated advice found no
    authority or guidance on whether AI output counts as reliance on a competent professional; this is an open question,
    not a finding.

- id: tax-research-advisory-14
  title: Automatic AI-use log in the matter file (prompts, sources, verifier, reviewer)
  archetype: tax
  module: research-advisory
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Regulators and tribunals expect practitioners to show how AI output was verified, but manual note-keeping is rarely done.
  solution: >-
    Idea: tooling captures the prompts, tools, sources and sign-offs for AI-assisted research automatically and attaches them to the engagement file.
    Guidance asks for this documentation. The UK tribunal in Elden ordered statements of truth about AI use in the proceedings.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: IRS-OPR-2026
  prerequisites:
    - Approved-tool list and an AI lead or committee (JofA policy article)
  risks_and_guardrails:
    - OPR section 10.36 expects firms to document the steps and processes that show adherence (IRS-OPR-2026, section 10.36)
    - TPB says verification steps should be documented (TPB-AI-2026, Competency)
    - PCRT suggests retaining copies of web pages and screenshots of prompts as an audit trail (PCRT-AI-2026, integrity safeguards table)
    - JofA suggests documenting prompts used, how outputs were verified and who reviewed, in the client file (JOFA-AIPOLICY-2026)
  human_checkpoints:
    - AI lead or committee reviews incident reports and spot-checks compliance
  role_evolution: >-
    Firms designate an AI lead or committee to approve tools and monitor use (JOFA-AIPOLICY-2026).
  evidence_grade: D
  sources:
    - {ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "section 10.36; best practices"}
    - {ref: TPB-AI-2026, title: "TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct", publisher: Tax Practitioners Board (Australia), type: regulator, url: "https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct", date: "2026-07-22", access: full, locator: Competency}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "integrity safeguards table"}
    - {ref: JOFA-AIPOLICY-2026, title: "Drafting an AI policy that actually works", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/", date: "2026-07-01", access: full, locator: "documentation and governance sections"}
    - {ref: CHARLOTIN-DB-2026, title: "AI Hallucination Cases Database", publisher: Damien Charlotin, type: academic, url: "https://www.damiencharlotin.com/hallucinations/", date: "2026-10-16", access: full, locator: "CSV entry for Elden v HMRC (outcome field)"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea. This is a governance control enabled by tooling, not an AI productivity use case. The Elden outcome ("order to include
    statements of truth about AI use") is from the Charlotin CSV outcome field, which was not checked against the judgment itself.

- id: tax-research-advisory-15
  title: Screening AI-generated material supplied by clients, counterparties or opponents
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Clients, counterparties and opposing parties now send positions, research and citations that may be AI-generated and wrong.
    The tax authority and the tribunal, not the filer, found the errors in several cases.
  solution: >-
    Idea: run incoming submissions through the same citation and consistency checks used on the firm's own work. In Clinco the IRS flagged the
    nonexistent cases in its answering brief; in Harber the tribunal and HMRC checked and found nine cited decisions did not exist.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: ICAS-TAXTRIB-2026
  prerequisites:
    - A citation resolution capability (see tax-research-advisory-03)
  risks_and_guardrails:
    - PCRT says members should exercise scepticism where data supplied by a client or third party may have been AI-generated (PCRT-AI-2026, competence risk table)
    - Tribunals treat the rest of a document with great caution once AI-generated flaws are found and not corrected (ICAS-TAXTRIB-2026, Elden summary)
  human_checkpoints:
    - Adviser decides how to respond to flagged material
  role_evolution: "not described in the sources"
  evidence_grade: D
  sources:
    - {ref: ICAS-TAXTRIB-2026, title: "AI at the tax tribunal", publisher: ICAS, type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/ai-at-the-tax-tribunal/", date: "2026-01-26", access: full, locator: "Harber and Elden summaries"}
    - {ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy, type: press, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: "2026-09-01", access: full, locator: "Clinco facts"}
    - {ref: PCRT-AI-2026, title: "Topical guidance covering the application of PCRT to the ethical use of AI tools", publisher: ICAEW for the seven PCRT bodies, type: standard-setter, url: "https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools", date: "2026-01-19", access: full, locator: "competence risk table"}
  last_reviewed: 2026-10-17
  notes: "Idea derived from how errors were detected in reported cases; no firm or authority was found describing a screening workflow."

- id: tax-research-advisory-16
  title: Specialist multi-jurisdiction and state-by-state research workflow
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Multi-jurisdiction questions (for example comparing state pass-through entity tax credits, or 50-state surveys) are where tools do worst and where
    manual work is longest.
  solution: >-
    Idea: a purpose-built workflow that searches each jurisdiction's primary law and compiles a comparison table for adviser review. Vals suggests a
    specialist workflow designed to search all 50 states' laws should yield much better results than basic prompts.
  outcomes:
    - lever: quality
      description: >-
        Legal research study (adjacent process): AI products scored lower on questions that required more than one jurisdiction's law.
      figure: "14 points lower on average (14 multi-jurisdiction questions)"
      measures: "difference in average weighted score between multi-jurisdiction and single-jurisdiction questions among the AI products, in a 200-question legal research set"
      provenance: independent
      source_ref: VALS-VLAIR-2025
  prerequisites:
    - Primary-law access across jurisdictions
  risks_and_guardrails:
    - In the Vals tax benchmark's public SALT question, twelve of eighteen models failed the same must-pass check on New York's treatment of credits from several entities (VALS-TAXAGENT-2026, Trajectories on a Public Question)
    - All participants in the legal research study struggled with the 50-state survey question (VALS-VLAIR-2025, Key finding 3)
  human_checkpoints:
    - Adviser verifies each jurisdiction's result against primary law
  role_evolution: "not described in the sources"
  evidence_grade: D
  sources:
    - {ref: VALS-VLAIR-2025, title: "VLAIR - Legal Research", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/industry-reports/vlair-10-14-25", date: "2025-10-14", access: full, locator: "Key finding 3"}
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: Vals AI, type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-16", access: full, locator: "Trajectories on a Public Question (P-004)"}
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The measured weakness is real; the specialist-workflow remedy is Vals' suggestion, not a tested result. The Vals tax page
    narrative about question P-004 may rest on the earlier analysis set (see tax-research-advisory-02 notes).
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Scope and intake the question** (client or internal-client question, facts, deadline): `client-interaction`, `coordination-scheduling`.
- **Gather and confirm facts**: `research-synthesis`, `data-reporting`.
- **Locate and read authority** (Code, regulations, guidance, cases, treaties, foreign law): `research-synthesis`.
- **Apply law to facts, weigh authority, reach a view or opinion level**: `expert-judgment`.
- **Compute tax effects and model alternatives** (planning and structuring): `data-reporting`, `expert-judgment`.
- **Draft memo, advice note, opinion or diligence report**: `document-production`.
- **Review, cite-check and sign-off** (second reviewer, opinion committee): `review-assurance`.
- **Deliver and handle client follow-up questions**: `client-interaction`.
- **M&A tax diligence and structuring** runs these same steps on a deal clock, with data-room contracts as the main input (KPMG-MATAX-2025).

### Common pain points

- Hallucinated or misdescribed authority reaching memos and filings (Clinco, Harber, Zzaman, Elden); real cases that do not support the proposition (Zzaman) are harder to catch than non-existent ones (ICAS-TAXTRIB-2026).
- Outdated law in model answers (BTAX-HALLUC-2026; PCRT-AI-2026 para 3.7).
- Errors that fail "quietly and politely", and a growing volume of AI-produced work to review (TEI-TAXTECH-2026).
- Tools used without approval: more than one-third of tax and audit professionals (TR-FOP-2026).
- Fee model collision: OPR says do not bill manual time not spent; AICPA objects (IRS-OPR-2026; AICPA-FEES-2026).
- Ambiguity about reliance and liability when an AI-assisted position is challenged (TAXADVISER-WERFEL-2026, Figure 3: liability ambiguity).

### Metrics and benchmarks (with sources)

- **Vals Tax Agent Bench** (updated 2026-10-16): 193 private test questions, 391 expert-written questions in total; best leaderboard accuracy 49.19%; best by category: Rule and Source Lookup 66.67%, Current and Temporal Analysis 66.67%, Forms and Filings 40.00%, Controversy and Precedence 36.67%; leader's weighted-pass (partial credit) 77.64% (VALS-TAXAGENT-2026). Judged by an LLM.
- **Vals TaxEval v2**: 1,500+ question tax Q&A benchmark; top listed score 80.38% on its leaderboard; archived because the benchmark is described as saturated (VALS-TAXEVAL-2026). Shows models answer many tax questions correctly while the research benchmark shows them failing rubric-complete research.
- **Stanford, legal research tools**: 17% to 33% hallucination for retrieval-based Lexis and Westlaw products (STANFORD-HALLUC-2024). **Vals legal research**: AI products 74%-78% weighted score against a 69% lawyer baseline; multi-jurisdiction questions 14 points lower (VALS-VLAIR-2025).
- **Taxpayer-facing accuracy**: ChatGPT 3.5 and 4 gave correct responses 39% to 47% of the time across the 2023 and 2024 seasons (ANTINOZZI-2024). Dated: older models.
- **Calculation accuracy**: best model 32.35% strict on 51 simplified federal returns (COLUMN-TAXCALCBENCH-2025).
- **Incident counts**: Charlotin's database lists about 2,200 decisions where hallucinated content was found (header text says 2,199; the CSV downloaded 2026-10-17 had 2,200 rows). I counted 25 rows with primary legal field "tax" (13 dated 2026, 9 in 2025, 3 in 2024): 11 pro se, 10 lawyer, 2 expert, 1 judge, 1 paralegal-and-lawyer (CHARLOTIN-DB-2026). A Texas A&M-affiliated preprint (not peer reviewed) reports nearly 800 AI citation errors across at least 25 countries by late 2025, more than 85% of them in 2025, with about 90% not producing formal professional sanctions against the filer (PREPRINTS-HALLUC-2026).
- **Judge's view**: Judge Holmes said he had seen fewer than a dozen hallucinated-citation instances in Tax Court and had issued no sanctions (BLOOMBERG-TAXCT-2026, March 2026).
- **Adoption and governance surveys**: Fonoa (176 indirect tax leaders): 92% use AI, 12.5% have specific targets or KPIs, 57.4% would not be confident defending AI-assisted decisions to a tax authority (FONOA-2026-SURVEY). Thomson Reuters: 81% of tax and audit professionals use AI regularly (TR-FOP-2026); 67% of corporate tax departments not using GenAI in the 2025 corporate survey (TR-CORPTAX-2025). KPMG Germany: 71% of tax departments use AI tools (KPMG-DE-2026). Different samples and definitions; do not average.
- **Independent quality evidence is absent for**: error or override rates in firm deployments, parallel-run results, inspection outcomes on AI-assisted tax advice, and any head-to-head test of commercial tax research products. No regulator inspection programme covering tax advice was found.

### Guardrails and regulatory points

- **US**: Circular 230 sections 10.22 (due diligence), 10.27(a) (unconscionable fees), 10.35 (competence), 10.36 (firm procedures), 10.37 (written advice), 10.51(a)(15) and IRC 6713 and 7216 (disclosure of return information) as applied by OPR Alert 2026-19 (IRS-OPR-2026). AICPA Statements on Standards for Tax Services section 1.4 (reliance on tools): may rely on tools but remain responsible, with professional care and judgment (TAXCT-CLINCO-2026, as summarised by JofA). Tax Court Rule 201(a) binds lawyers to the ABA Model Rules (TAXCT-CLINCO-2026). ABA Formal Opinion 512 (29 Jul 2024) is cited by OPR; the opinion itself could not be fetched. Section 6673 (penalty up to $25,000 for frivolous arguments) is the most prominent Tax Court provision for AI misuse, per Judge Holmes, though counsel for the other side questions whether it covers all AI mistakes (BLOOMBERG-TAXCT-2026).
- **UK**: PCRT fundamental principles with AI topical guidance (19 Jan 2026): engagement-letter wording on AI, disclosure of actual use "should be considered", explainability, audit trail, no public tools with client data unless consented or anonymised (PCRT-AI-2026). HMRC's expectations for generative-AI software (28 Jan 2026) (HMRC-GENAI-2026). FTT: AI use "not directly relevant" but the human who relies on it bears responsibility (ICAS-TAXTRIB-2026, quoting Elden).
- **Australia**: TPB(GS) 55/2026: competence, reasonable care (checking output before relying on it is a factor), permission before client information goes to AI models, documentation of verification (TPB-AI-2026).
- **Frameworks, not standards**: Werfel's registers (20 risks for authorities, 15 for preparers) with an eight-step method and a recommendation to start with limited-scope pilots (TAXADVISER-WERFEL-2026). The Council on AI Risk in Tax (AICPA, 23 Sep 2026) will test and refine it (AICPA-CART-2026). Correction to the landscape file: the 20-risk, four-category register is the tax authorities' register; the preparer register has 15 risks in five categories, and the article is dated 2026-08-31 (August issue).
- **Fees**: OPR says savings should be passed on and AI activities disclosed in general or specific terms (IRS-OPR-2026). AICPA says the language is non-authoritative, overly simplistic and may be overstepping, and is working with the IRS on FAQs (AICPA-FEES-2026).
- **Professional liability insurance** (search-only, not read): reported carrier AI exclusions in professional lines and 2026 ISO general-liability endorsements, with possible carve-backs for documented AI governance. Nothing accountant- or tax-specific was found. See Gaps.

### Frontier signals (dated, sourced)

- 2026-01-19: UK PCRT bodies issue AI topical guidance (PCRT-AI-2026). 2026-01-28: HMRC sets expectations for generative AI in tax software (HMRC-GENAI-2026).
- 2026-01 to 2026-03: UK and US tribunals deal with professional advisers' unverified AI (Elden; Clinco; Riddle Aggregates expert report challenged and recorded as withdrawn; Khoja reported by Bloomberg Law as an IRS motion with a nonexistent citation) (ICAS-TAXTRIB-2026; CHARLOTIN-DB-2026; BLOOMBERG-TAXCT-2026).
- 2026-03-20: Judge Holmes says the Tax Court is "feeling our way in the dark" on rules; a rules-committee certification requirement is something it "might" consider but he is unsure it makes sense (BLOOMBERG-TAXCT-2026).
- 2026-05-20: KPMG announces a Claude-based platform for client-built agents, tax first (KPMG-ANTHROPIC-2026).
- 2026-06-24: IRS OPR guidance. 2026-07-22: TPB Guidance Statement. 2026-08-31: Werfel framework. 2026-09-08: AICPA asks IRS to clarify fee language. 2026-09-23: CART launches (sources above).
- 2026-09/10: Independent agentic tax research benchmark published and updated (Vals) with the best fully-correct rate below 50% (VALS-TAXAGENT-2026).
- A model-evaluation page labelling TaxEval v2 saturated (VALS-TAXEVAL-2026) alongside the harder research benchmark signals that simple Q&A tests no longer discriminate.

### Workforce and role effects

- Review of AI output is the central duty: "junior colleague" framing (PCRT-AI-2026), "starting point" framing for written advice (IRS-OPR-2026).
- Risks to development of judgment: skill erosion, institutional knowledge loss (TAXADVISER-WERFEL-2026); structured development before automation erodes it (TR-FOP-2026).
- Headcount: Sala argues limited effect on corporate tax teams (SALA-TAXNOTES-2026); KPMG Germany respondents expect stable headcount (58% domestic, 72% abroad) (KPMG-DE-2026); TR says nearly one-third would consider leaving if AI expectations are unmet within two years (TR-FOP-2026).
- PwC reports 3,200 AI champions, 350,000 US training hours and about 80% of US staff with some AI training (PWC-MEGNA-2025, self-reported).
- New roles: AI lead or committee (JOFA-AIPOLICY-2026); PwC firm-level governance committee (PWC-MEGNA-2025).

### Objections and concerns practitioners raise

- "Fees: efficiency must be passed on" versus value pricing and the cost of implementation, training and liability (AICPA-FEES-2026).
- "Quiet failures": AI claiming to have read a file it could not open; review burden grows (TEI-TAXTECH-2026).
- Nobody owns AI in tax (TEI-TAXTECH-2026); no KPIs (Fonoa: 12.5% have targets).
- Judgment and culpability cannot be delegated (SALA-TAXNOTES-2026; TPB-AI-2026).
- Confidentiality and section 7216 exposure when client data enters tools (IRS-OPR-2026; PCRT-AI-2026).
- A Tax Court certification rule might ban legitimate uses (Holmes, BLOOMBERG-TAXCT-2026).
- Vendors' "hallucination-free" claims: Stanford found such claims overstated for legal research tools (STANFORD-HALLUC-2024).

### Interview probes for an adviser

1. When did an AI-assisted research answer last go wrong in your team, and who caught it: the author, a reviewer, the client or the tax authority? What did the file show about how it was verified?
2. How does your firm decide what to read in the underlying authority when a tool provides a citation? Is that written down, and do you record who checked it?
3. Who owns AI in tax in your organisation, and how would you demonstrate to an examiner, a tribunal or an auditor how an AI-assisted position was reached?
4. How are you handling engagement-letter wording, disclosure of AI use and the OPR fee point: do you pass savings on, move to fixed or value fees, or leave billing unchanged?
5. Which questions do you refuse to put through AI at all (opinion-level, policy interpretation, anything with client-identifying facts in a public tool), and why?

---

## 4. Routed to other modules

- **controversy**: *Elden v HMRC*, *Zzaman v HMRC*, *Harber v HMRC* (taxpayer and representative submissions to tribunals); *Clinco*, *Bauche*, *Moore* and other Tax Court entries; *Khoja* (IRS motion); IRS section 6673 and the Tax Court rules discussion (BLOOMBERG-TAXCT-2026; ICAS-TAXTRIB-2026; CHARLOTIN-DB-2026); IRS "AI-first" and tax-authority AI oversight from the landscape file.
- **transfer-pricing** (and controversy): *Riddle Aggregates* respondent's (IRS) valuation expert report, where hallucinated citations were raised after voir dire; the Charlotin outcome field records 'Report withdrawn' (CHARLOTIN-DB-2026; RIDDLE-TRANSCRIPT-2026, pp. 604-614); IRS LB&I remarks that AI may support but not replace judgment and that expert witnesses must explain inputs, assumptions, methods and AI tools, and the IRS will "want to see the formulas" (IRS-LBI-TP-2026).
- **compliance**: TaxCalcBench return-preparation accuracy (COLUMN-TAXCALCBENCH-2025); Werfel's "incorrect document extraction" risk; PwC K-1 mapping agents (PWC-MEGNA-2025); HMRC's software guidelines for filing products (HMRC-GENAI-2026).
- **indirect-tax**: Fonoa survey details on 10 indirect tax workflows and the validation-process finding (FONOA-2026-SURVEY).
- **provision**: PwC effective-tax-rate model with explained inputs and locked approved logic (PWC-MEGNA-2025); Bloomberg Tax's point that errors compound through provision and ETR calculations (BTAX-HALLUC-2026).
- **tax-data-technology**: TR corporate department resourcing and ERP migration findings; TEI governance and training-rollout failures (TR-CORPTAX-2025; TEI-TAXTECH-2026).
- **Cross-cutting professional responsibility (all modules)**: OPR Alert 2026-19, PCRT, TPB, Werfel framework and CART, the fee dispute.

---

## 5. Sources

Access is `full` unless stated. All were opened in this run.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 |
| PCRT-AI-2026 | Topical guidance covering the application of PCRT to the ethical use of AI tools | ICAEW for the seven PCRT bodies | standard-setter | https://www.icaew.com/technical/tax/working-in-tax/pcrt/topical-guidance-application-of-pcrt-to-ethical-use-of-artificial-intelligence-tools | 2026-01-19 |
| ATT-PCRT-2026 | Professional bodies issue AI advice to members | Association of Taxation Technicians | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 |
| TPB-AI-2026 | TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct (and media release) | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct | 2026-07-22 |
| HMRC-GENAI-2026 | Guidelines for using generative artificial intelligence if you're a software developer | HMRC (GOV.UK) | regulator | https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer | 2026-01-28 |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 |
| BLOOMBERG-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers (partly paywalled; opened via text mirror) | Bloomberg Law | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 |
| RIDDLE-TRANSCRIPT-2026 | Riddle Aggregates v. Commissioner, trial transcript vol. 3 (Docket 31104-21), pp. 527-761 (read pp. 604-614) | US Tax Court (via Charlotin database) | regulator | https://www.damiencharlotin.com/documents/1972/Riddle_Aggregates.pdf | 2026-03-18 |
| JOFA-OPR-2026 | IRS outlines AI risks, Circular 230 duties for tax practitioners | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/ | 2026-06-26 |
| AICPA-FEES-2026 | AICPA seeks IRS clarity on AI guidelines, CPA fees | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/ | 2026-09-08 |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 |
| TAXADVISER-WERFEL-2026 | A risk framework for AI use in tax administration and preparation (Danny Werfel) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08-31 |
| JOFA-AIPOLICY-2026 | Drafting an AI policy that actually works | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/ | 2026-07-01 |
| ICAS-TAXTRIB-2026 | AI at the tax tribunal | ICAS | professional-body | https://www.icas.com/news-insights-events/news/tax/ai-at-the-tax-tribunal/ | 2026-01-26 |
| ROSSMARTIN-ELDEN-2026 | Accountants' misuse of AI in FTT case (Elden v HMRC) | Ross Martin Tax | press | https://www.rossmartin.co.uk/sme-tax-news/8799-accountants-misuse-of-ai-in-ftt-case | 2026-01-27 |
| CHARLOTIN-DB-2026 | AI Hallucination Cases Database (web page and CSV, downloaded 2026-10-17) | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-16 |
| PREPRINTS-HALLUC-2026 | Citing the Unseen: AI Hallucinations in Tax and Legal Practice (preprint, not peer reviewed; opened via text mirror) | Preprints.org (Texas A&M-affiliated author per figure caption) | academic | https://www.preprints.org/manuscript/202601.0187/v1 | 2026-01 |
| VALS-TAXAGENT-2026 | Tax Agent Bench: Agentic US corporate tax research | Vals AI | vendor | https://www.vals.ai/benchmarks/tax_agent_bench | 2026-10-16 |
| VALS-TAXEVAL-2026 | TaxEval v2 leaderboard and methodology (archived benchmark) | Vals AI | vendor | https://www.vals.ai/benchmarks/tax_eval_v2 | 2026-09-01 |
| VALS-VLAIR-2025 | VLAIR - Legal Research | Vals AI | vendor | https://www.vals.ai/industry-reports/vlair-10-14-25 | 2025-10-14 |
| VALS-VLAIR1-2025 | Vals Legal AI Report (first VLAIR) | Vals AI | vendor | https://www.vals.ai/vlair | 2025-02-27 |
| STANFORD-HALLUC-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Magesh et al. (Stanford) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | Column Tax | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning | Johns Hopkins University | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 |
| JHU-TAXABUSE-2025 | Can LLMs Identify Tax Abuse? | Blair-Stanek, Holzenberger, Van Durme | academic | https://arxiv.org/abs/2508.20097 | 2025-08-10 |
| ANTINOZZI-2024 | Is ChatGPT an Accurate Source of Information for Uninformed Taxpayers? | Antinozzi and Cooper | academic | https://wealthstrategiesjournal.com/2024/06/30/hannah-smith-antinozzi-lauren-cooper-is-chatgpt-an-accurate-source-of-information-for-uninformed-taxpayers-june-18-2024/ | 2024-06-18 |
| SWIDER-2025 | CPAs vs. AI Tax Advisors: Evaluating Reliance Across Advisory Contexts | University of Oklahoma (AAA meeting paper) | academic | https://aaahq.org/portals/0/documents/meetings/2025/ATA/Papers/3.02_Swider.pdf | 2025 |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. | Tax Notes State via TaxProf Blog | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 |
| BTAX-HALLUC-2026 | AI Hallucinations in Tax: The Risks and How to Mitigate Them | Bloomberg Tax | vendor | https://pro.bloombergtax.com/?p=16920 | 2026-05-11 |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 |
| TR-CORPTAX-2025 | The GenAI paradox (State of the Corporate Tax Department 2025) | Thomson Reuters | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (quick surveys) | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-06 |
| FONOA-2026-SURVEY | State of Indirect Tax in the AI Era 2026 (176 indirect tax leaders) | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 |
| BLUEJ-CPA-2026 | 2026 AI Tax Research Solution Outlook Report (landing page only; report gated) | Blue J and CPA.com | survey | https://www.cpa.com/whitepapers/2026-ai-tax-research-solution-outlook-report | 2026 |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 |
| KPMG-MATAX-2025 | How generative AI is transforming mergers and acquisitions tax | KPMG US | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/how-generative-ai-transforming.pdf | 2025-06 |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (KPMG release) | firm | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 |
| PWC-MEGNA-2025 | How PwC's Dom Megna is using agentic AI in tax | CFO.com | firm | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 |
| IRS-LBI-TP-2026 | Report on recent US international tax developments, 31 July 2026 | EY Tax News | press | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 2026-07-31 |

Seen in search results only (not opened, not used for claims): Becker CPE course "AI in Tax Practice: Choosing and Testing Tax Research Tools" (https://www.becker.com/cpe/catalog/ai-in-tax-practice-choosing-testing-tax-research-tools, undated); CFO Dive, City AM and other coverage of the Deloitte Australia refund; Insurance Business, Jenner and Insurance Insider pieces on AI exclusions in professional liability; vatcalc and Bloomberg Government coverage of the HMRC guidelines (the gov.uk page itself was read). AICPA "Insights" on the OPR guidelines (https://www.aicpa-cima.com/resources/article/aicpa-insights-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice, 2026-07-02) was opened but is gated to Tax Section members; only the introduction was read.

---

## 6. Gaps

- **No independent measurement of commercial tax research products.** No head-to-head of Blue J, CoCounsel, Bloomberg Tax AI or CCH AnswerConnect/Expert AI on tax questions was found. Vals tests foundation models in its own harness; Stanford and Vals legal-research studies are adjacent (legal, not tax). The Blue J/CPA.com report is gated (landing page only), and aggregator figures from it were not traceable.
- **No inspection or enforcement outcomes for AI in tax advice** from IRS OPR, TPB, HMRC, CIOT/ICAEW or state boards. OPR, PCRT and TPB are guidance; no disciplinary case citing AI was found. The Tax Court has issued an admonishment (Clinco), not a sanction.
- **No firm-deployment error, override or parallel-run data** for research, memo drafting or diligence. KPMG and PwC describe tools and governance but publish no accuracy or time data; the "weeks to minutes" and "weeks into minutes" statements are marketing quotes without method.
- **M&A tax diligence and structuring**: only one firm source (KPMG) and the PCRT example; no survey, regulator or professional-body statement specific to AI in tax diligence; no R&W insurance underwriter view.
- **Reliance and penalty protection**: no authority found on whether AI-generated advice can support reasonable cause or preparer-penalty defenses.
- **Professional liability insurance**: search extracts show AI exclusion trends in professional lines, but nothing for accountants' tax engagements or sample engagement-letter AI clauses; not opened.
- **Not reachable**: ABA Formal Opinion 512 (americanbar.org 403, mirror blocked); AICPA SSTS text (SSTS section 1.4 is cited only through JofA's summary); AICPA FAQs on AI in federal tax practice; the Tax Notes Talk Tax Court chief judge episode (6 Mar 2026); the January 2026 International Tax Journal paper (the ~800 figure appears in a Bloomberg Tax vendor article and in an unreviewed preprint with the same wording; the journal attribution is unverified); full Riddle Aggregates court rulings beyond the transcript; the Elden judgment itself (case notes by ICAS and Ross Martin were used; neutral citation differs between them: [2026] UKFTT 41 (TC) and [2026] TC09742).
- **Date and number conflicts**: the Werfel article is dated 2026-08-31 (August issue), not September as the landscape file records; KPMG Germany release metadata is 2026-05-06 (landscape says 7 May); the Vals Tax Agent Bench narrative text cites figures from an earlier analysis set that do not match its current leaderboard; the KPMG M&A web page shows both 2025 and 2026-07-29 dates (the 2025 PDF was used).
- **Closed or paywalled**: TEI member sessions; Tax Notes and Bloomberg Tax articles beyond the opening; no practitioner forum threads (Reddit r/taxpros, TaxProTalk) were reached.
- **Frontier**: TEI Annual Conference (18-21 Oct 2026), IFA Melbourne (18-22 Oct 2026) and CCH Connections (25-28 Oct 2026) fall after this scan; re-check for AI research governance sessions in November 2026.
