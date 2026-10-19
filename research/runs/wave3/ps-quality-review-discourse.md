# Professional services, quality-review: discourse angle

Prepared 2026-10-19. Archetype: professional-services. Module: quality-review (review and sign-off, hallucination and citation checking, quality and risk management systems, professional standards for AI-assisted work). Angle: discourse (what practitioners are saying, last 12-18 months).

Method: pages opened with `curl` (HTML, PDF via `pdftotext`, one RSS feed, one JSON API for a community thread); where a site returned 403 or only headings (White & Case PDF, Best Lawfirms, Management Today) the text mirror was used for the same URL. About 14 rationed web searches were used before the shared budget ran out. Sources are marked `access: full` only if opened and read. Quotations are under 25 words. Public sources only. Items tagged **in-house** come from corporate legal or legal-operations settings. Audit procedures and tax technical work are left to the assurance and tax archetypes.

## 1. Summary

**What practitioners are saying.** The discourse on quality review changed in the last 12 months from "lawyers must verify" to "the firms that sell verification are failing at it in public".

- **Public failures at elite firms.** Sullivan & Cromwell apologised to a US bankruptcy judge on 18 Apr 2026 for AI-generated errors in an emergency motion; its own partner wrote that firm protocols "were not followed" and that ordinary citation checking also missed the errors (CANLAWYER-SC-2026). Between Oct 2025 and Jul 2026, reports from each of the Big Four (two from Deloitte, in Australia and Canada) were publicly questioned for fabricated or unverifiable citations. In the sources read here, outsiders found the problems each time: a Sydney University academic, a Newfoundland news outlet, and GPTZero (CTV-DELOITTE-2025, FORTUNE-DELOITTE-2025, GPTZERO-KPMG-2026, ACS-EY-2026, GPTZERO-PWC-2026).
- **Policy exists; practice lags.** ILTA's 2026 survey shows 57% of firms under 50 lawyers and 91-98% of the largest bands have a formal GenAI policy, but only 31% of the smallest firms and 79-83% of the largest require human review of GenAI work product, and 25-60% require outputs to be cited or independently verified (ILTA-TECHSURVEY-2026, p.4). Morae's own survey of 850 senior legal professionals finds 71% have formal policies but only 30% are confident the policies are applied (MORAE-ILR-2026).
- **The "verification tax" is the new worry.** 67% of Morae's respondents fear that human checking costs outweigh AI's benefits, and 48% must materially fix outputs before use (MORAE-ILR-2026, vendor-published). No published measurement of review time against drafting time saved was found.
- **"Human in the loop" is being redefined.** Practitioners now ask which human, where in the process, and whether review is rubber-stamping (ACCOUNTINGTODAY-HALLUC2-2026). TRI's November 2026 webinar contrasts "in the loop" with "in control" (TRI-BEYONDHITL-2026, scheduled). A researcher analysing New York court documents finds courts calling for error-rate evidence that does not exist and substituting training and checklists (ARXIV-WILLIAMS-2026).
- **Quality evidence is thin.** No firm in the sources read publishes review catch rates, override rates or parallel-run results for AI-assisted deliverables. The measured data are (a) independent tool error rates (Stanford 17-33%, Luxembourg under 10% to nearly half), (b) vendor evaluations (Filevine, GPTZero), (c) court-case counts that vary by tracker, and (d) survey prevalence data.

**Where the field is heading.** Pre-signature citation checkers, review gates inside agent workflows (Harvey, Armanino), AI-specific layers on existing quality-management systems (Forvis Mazars), and pressure from insurers, courts and clients to show documented verification.

**Use-case count:** 17 candidates; grades A=0, B=7, C=7, D=3 (see section 2).

## 2. Use cases

```yaml
- id: professional-services-quality-review-01
  title: Automated cite, quote and authority check before a brief is signed, with a review audit trail
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Fabricated or misdescribed authority keeps reaching courts. Clearbrief's CEO says most partners rely on associates to check citations, so partners are sanctioned for errors they did not personally make (LAWSITES-CLEARBRIEF-2025). Sullivan & Cromwell wrote to the court that its ordinary citation-checking processes also failed to catch invented authorities (CANLAWYER-SC-2026).
  solution: >-
    A checker compares every citation and quotation in a draft or filed brief with a case-law corpus and flags missing cases, altered quotations and authority that does not support the proposition. The signing lawyer clears each flag and saves a report to the file. LawSites describes Filevine's LOIS brief checker (statuses: verified, unverified, suspect, ambiguous, mischaracterized, wrong case name) and Clearbrief's Cite Check Report, which the vendor says uses classic rather than generative AI (LAWSITES-FILEVINE-2026; LAWSITES-CLEARBRIEF-2025). Thomson Reuters describes a Verify function and a Litigation Document Analyzer in CoCounsel Legal (TR-CANTSIGN-2026, vendor).
  outcomes:
    - lever: quality
      description: Filevine's own evaluation, seen by LawSites in an unpublished paper, ran its checker on briefs from 68 attorney-filed federal matters in which a court had already identified possible hallucinated citations. Every document produced at least one flag.
      figure: "61.8% verified; 38.2% flagged for attorney review; 8.4% marked severe (2,073 citations)"
      measures: "Share of 2,073 citations in 68 matters (selected because a court had already flagged problems) that the tool verified, flagged for attorney review, or marked severe (mischaracterized holding, or wrong or non-existent case). Not a detection-accuracy rate; no false-positive rate reported."
      provenance: vendor-published
      source_ref: LAWSITES-FILEVINE-2026
    - lever: risk
      description: Clearbrief says the report gives partners documented proof of verification before signing. No measured outcome published.
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: LAWSITES-CLEARBRIEF-2025
  prerequisites:
    - A case-law corpus to check against. Filevine uses CourtListener plus licensed material and does not yet cover statutes or regulations (LAWSITES-FILEVINE-2026).
    - Handling of proprietary citation formats such as Westlaw cites (LAWSITES-CLEARBRIEF-2025).
  risks_and_guardrails:
    - Filevine's CEO says a human still has to look; the LawSites author had not tested the tool (LAWSITES-FILEVINE-2026).
    - The citator works on text the user highlights, and the company had not tested whether it would miss reversal on an unrelated holding (LAWSITES-FILEVINE-2026).
    - ABA Formal Opinion 512 is cited for the duty to review AI outputs, including citations, before submission to a court (WHITECASE-VERIFY-2026).
  human_checkpoints:
    - Signing lawyer reviews each flag and records why a red flag was ignored (LAWSITES-CLEARBRIEF-2025).
    - Cases the tool cannot confirm are uploaded and checked manually (LAWSITES-CLEARBRIEF-2025).
  role_evolution: >-
    Associates and paralegals still run the check, but the report gives the signing partner a file record instead of trust (LAWSITES-CLEARBRIEF-2025).
  evidence_grade: C
  sources:
    - {ref: LAWSITES-FILEVINE-2026, title: "Filevine Takes On Shepard's and KeyCite With Its Own AI Case Law Citator and Hallucination Checker", publisher: "LawSites", type: press, url: "https://www.lawnext.com/2026/09/filevine-takes-on-shepards-and-keycite-with-its-own-ai-case-law-citator-and-hallucination-checker.html", date: "2026-09-02", access: full, locator: "paragraphs on the evaluation paper (68 matters, 2,073 citations) and closing quotes"}
    - {ref: LAWSITES-CLEARBRIEF-2025, title: "Clearbrief Launches Cite Check Report to Give Law Firm Partners an Audit Trail Against AI Hallucinations", publisher: "LawSites", type: press, url: "https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html", date: "2025-12-16", access: full, locator: "opening paragraphs; 'Providing Verifiable Proof' section"}
    - {ref: TR-CANTSIGN-2026, title: "If You Can't Verify It, You Can't Sign It", publisher: "Thomson Reuters Innovation Blog", type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/if-you-cant-verify-it-you-cant-sign-it/", date: "2026-05-05", access: full, locator: "'Built for Verification at Every Stage' section"}
    - {ref: CANLAWYER-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: "Canadian Lawyer", type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: "2026-04-22", access: full, locator: "paragraphs 4-5"}
    - {ref: WHITECASE-VERIFY-2026, title: "Verify, Guide, Train: Lessons From Emerging Attorney AI-Misuse Caselaw", publisher: "White & Case (James N. Robinson, Zachary B. Dickens, Andrew K. Gershenfeld)", type: firm, url: "https://www.whitecase.com/sites/default/files/2026-04/verify-guide-train-lessons-from-emerging-attorney-ai-misuse-case-law.pdf", date: "2026-04-15", access: full, locator: "'Trust, but Verify' section"}
  last_reviewed: 2026-10-19
  notes: >-
    Vendor products exist and are launched, but no named customer's use or measured outcome was found, so maturity is announced. Other checkers named in search results only (BriefCatch RealityCheck, LawDroid CiteCheck AI) were not opened and are not relied on. Search results also say Cozen O'Connor is testing Clearbrief after sanctions; not opened, so not used.

- id: professional-services-quality-review-02
  title: Source-linked agent output so reviewers can check each assertion against its source
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Reviewers cannot trace a confident AI answer to its source quickly. A TRI webinar speaker notes that AI presents errors in the same assured tone as correct answers, so review needs subject-matter knowledge and not just proofreading (TRI-NEED2KNOW-2026).
  solution: >-
    Research and drafting tools expose their working: Thomson Reuters says CoCounsel Legal shows every assertion alongside source passages (Verify function, launched Feb 2026) and keeps a citation ledger of sources the AI read (TR-CANTSIGN-2026). Harvey says its agent retrieves authority, follows citations and checks treatment, and that it will launch precedent flags and cite checking for US case law over the coming months (HARVEY-GRAPH-2026).
  outcomes:
    - lever: quality
      description: Harvey reports that on its own Legal Agent Bench, giving an agent a graph of matter context improved rubric pass rate and cut task cost. This is agent task accuracy, adjacent to review.
      figure: "rubric pass rate up by up to 30%; task cost down by up to about 50%"
      measures: "Rubric pass rate and task cost on Harvey's Legal Agent Bench tasks, agent with versus without the context graph, under the benchmark's standard grading; 'up to' as stated by Harvey."
      provenance: vendor-published
      source_ref: HARVEY-GRAPH-2026
  prerequisites:
    - Authoritative content the tool can link to (TR-CANTSIGN-2026).
    - Matter data organised so the agent can follow relationships (HARVEY-GRAPH-2026).
  risks_and_guardrails:
    - A TRI Labs scientist says systems that appear to check their own work are still predicting, so no number of verification loops guarantees accuracy (TRI-NEED2KNOW-2026).
    - Source links make checking faster but do not remove the duty to verify (TR-CANTSIGN-2026).
  human_checkpoints:
    - Attorney reviews source passages for each assertion before anything is filed (TR-CANTSIGN-2026).
  role_evolution: >-
    Reviewer effort shifts from locating sources to judging whether a source supports the point, which TRI speakers say needs subject-matter expertise (TRI-NEED2KNOW-2026).
  evidence_grade: C
  sources:
    - {ref: TR-CANTSIGN-2026, title: "If You Can't Verify It, You Can't Sign It", publisher: "Thomson Reuters Innovation Blog", type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/if-you-cant-verify-it-you-cant-sign-it/", date: "2026-05-05", access: full, locator: "'Built for Verification at Every Stage' section"}
    - {ref: HARVEY-GRAPH-2026, title: "Improving Agent Accuracy With Harvey Graph", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph", date: "2026-10-19", access: full, locator: "'What's in Harvey Graph Today' and 'Strong Early Eval Results' sections"}
    - {ref: TRI-NEED2KNOW-2026, title: "What lawyers need to know about AI in 2026: Key lessons on hallucinations, ethics & education", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/what-lawyers-need-to-know-about-ai-2026", date: "2026-10-05", access: full, locator: "sections 'Understanding the black box of AI' and 'Human review is more than proofreading'"}
  last_reviewed: 2026-10-19
  notes: Both product descriptions are vendor-authored; the Harvey cite-checking features are described as upcoming, not released. The Harvey figure is adjacent evidence (agent task accuracy), which caps this entry below B in any case.

- id: professional-services-quality-review-03
  title: Pre-publication gate that verifies every reference and factual claim in reports and client deliverables
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Between Oct 2025 and Jul 2026, reports from each of the Big Four firms (two from Deloitte) were publicly questioned for fabricated or unverifiable citations, and in the sources read the errors were found by outsiders (CTV-DELOITTE-2025; FORTUNE-DELOITTE-2025; ACS-EY-2026; GPTZERO-KPMG-2026; GPTZERO-PWC-2026). GPTZero says that of KPMG's 45 citations only five accurately pointed to real sources, 28 had paraphrased titles or fake components, and 12 were too vague to judge (GPTZERO-KPMG-2026). Press summaries said 40 of 45 were hallucinations, which GPTZero's own breakdown does not state. The Register also reports GPTZero found a KPMG figure that contradicted KPMG's own CEO Outlook (REGISTER-KPMG-2026).
  solution: >-
    Before a report or deliverable leaves the firm, every reference is resolved to a real source and each claim is checked against the passage it cites. Practitioners suggest opening each source and refusing any quote that cannot be found in it (ACCOUNTINGWEEKLY-B4-2026). Hacker News commenters suggested a second agent to validate references, while others said that manual review of a sloppy AI draft cannot catch every error (HN-KPMG-2026). GPTZero sells a Hallucination Check tool used in its own investigations (GPTZERO-KPMG-2026).
  outcomes:
    - lever: quality
      description: GPTZero says its tool catches nearly all flawed citations and that it flags any citation it cannot verify online, so its false-positive rate is higher.
      figure: "catches 99 out of 100 flawed citations"
      measures: "Flawed citations caught out of flawed citations present, as stated by GPTZero; methodology and test set not shown."
      provenance: vendor-published
      source_ref: GPTZERO-KPMG-2026
  prerequisites:
    - A reference list that can be machine-read and a named owner for resolving flagged citations.
    - A rule on what counts as an unverifiable source (GPTZero separates fabricated, fused and paraphrased citations from ordinary typos).
  risks_and_guardrails:
    - GPTZero is a vendor with a commercial interest, and its detections are third-party analyses, not firm admissions (EWEEK-PWC-2026; GPTZERO-KPMG-2026).
    - Deloitte Canada said AI was not used to write its report but was selectively used to support a small number of research citations (FORTUNE-DELOITTE-2025).
    - KPMG and PwC Middle East each said staff are expected to follow responsible-AI guidance and quality-control processes; neither explained how the errors passed them (REGISTER-KPMG-2026; EWEEK-PWC-2026).
  human_checkpoints:
    - Author opens each source; second reader checks the 'top tier' deliverables where a fabricated fact would cost a client (ACCOUNTINGWEEKLY-B4-2026).
    - Named person decides whether to withdraw, correct and disclose.
  role_evolution: >-
    Authors own every citation they include. Rudge, the academic who found the Deloitte Australia errors, said work by his colleagues had been cited as tokens of legitimacy but not read (CTV-DELOITTE-2025).
  evidence_grade: C
  sources:
    - {ref: GPTZERO-KPMG-2026, title: "Chasing the Hallucinations: KPMG's AI-Powered Attempt at Redefining Excellence", publisher: "GPTZero", type: vendor, url: "https://gptzero.me/news/investigations-kpmg/", date: "2026-06-12", access: full, locator: "opening summary (45 citations; five accurate; 28 altered; 12 unclear) and methodology note (99 out of 100)"}
    - {ref: GPTZERO-PWC-2026, title: "Chasing the Hallucinations: PwC report hallucinates product and government customers", publisher: "GPTZero", type: vendor, url: "https://gptzero.me/news/investigations-pwc/", date: "2026-07-29", access: full, locator: "opening summary and four-report table"}
    - {ref: GPTZERO-DELOITTE-2025, title: "The Deloitte Citation Situation", publisher: "GPTZero", type: vendor, url: "https://gptzero.me/news/deloitte-australia-citation-check/", date: "2025-11-27", access: full, locator: "opening paragraphs (141 citations; 30+ issues; 19 hallucinations; more than 50 suspect citations per DEWR review)"}
    - {ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "CTV News (Associated Press)", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: "2025-10-07", access: full, locator: "article body, paragraphs 1-8"}
    - {ref: FORTUNE-DELOITTE-2025, title: "Deloitte allegedly cited AI-generated research in a million-dollar report for a Canadian provincial government", publisher: "Fortune", type: press, url: "https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government", date: "2025-11-25", access: full, locator: "paragraphs 1-4"}
    - {ref: ACS-EY-2026, title: "EY retracts cyber report littered with AI errors", publisher: "Information Age (ACS)", type: press, url: "https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html", date: "2026-05-19", access: full, locator: "paragraphs 2-8"}
    - {ref: EWEEK-PWC-2026, title: "GPTZero Flags Suspected AI Content and False Citations in PwC Reports", publisher: "eWeek", type: press, url: "https://eweek.com/news/gptzero-flags-suspected-ai-content-and-false-citations-in-pwc-reports/", date: "2026-07-30", access: full, locator: "paragraphs 1-12"}
    - {ref: REGISTER-KPMG-2026, title: "KPMG's AI report turns into a demo of AI hallucinations", publisher: "The Register", type: press, url: "https://www.theregister.com/ai-and-ml/2026/06/12/kpmgs-ai-report-turns-into-a-demo-of-ai-hallucinations/5255029", date: "2026-06-12", access: full, locator: "KPMG spokesperson statement near end"}
    - {ref: ACCOUNTINGWEEKLY-B4-2026, title: "Big Four AI Hallucinations: What It Means for Your Practice", publisher: "Accounting Weekly (CIBA)", type: press, url: "https://www.accountingweekly.com/trending-news/big-four-ai-hallucinations-what-it-means-for-your-practice", date: "2026-09-09", access: full, locator: "'The controls that actually stop this' section"}
    - {ref: HN-KPMG-2026, title: "KPMG pulls report on AI usage due to apparent hallucinations (discussion thread)", publisher: "Hacker News", type: community, url: "https://news.ycombinator.com/item?id=48527297", date: "2026-06-14", access: full, locator: "top-level comments on sub-agent validation and on manual review limits"}
  last_reviewed: 2026-10-19
  notes: >-
    No firm was found describing such a gate for published thought leadership or client deliverables, so this is an emerging practice inferred from incidents plus a vendor tool. The Deloitte Australia refund is reported as A$98,000 by GPTZero; the Associated Press says only that Deloitte agreed to repay the final instalment of an A$440,000 contract and the amount would be made public (GPTZERO-DELOITTE-2025; CTV-DELOITTE-2025). GPTZero's marketing claim of about $5,000 saved per citation is not relied on. A KPMG aggregator page and a GPTZero EY page (title only) were opened but not used.

- id: professional-services-quality-review-04
  title: AI-specific layer on the firm quality-management system (planning discussion, reviewer back-tracing, risk-tiered depth, disclosure)
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Review can become what Accounting Today calls accountability theater: reviewers go through the motions and rubber-stamp whatever arrives (ACCOUNTINGTODAY-HALLUC2-2026). A consultant quoted there asks whether the human reviewer is qualified to judge the work at all.
  solution: >-
    Forvis Mazars describes keeping its existing quality-management controls and layering AI-specific requirements on top. Engagement teams discuss planned AI use and professional skepticism at planning; some engagements use checklists asking reviewers to confirm AI outputs were reviewed and AI-identified discrepancies addressed; reviewers must check summaries against source, confirm citations are correct and current, and look for omitted facts; every deliverable still goes through independent review, and an engagement quality reviewer checks whether firm AI policy was followed on higher-risk audits (ACCOUNTINGTODAY-HALLUC2-2026). Schellman's CEO says technical conclusions, citations, regulations and client recommendations must be validated by a human, and review depth rises with the consequence of an error (same source).
  outcomes:
    - lever: risk
      description: Forvis Mazars describes a zero tolerance for skipping the review step and manages occasional human review imperfection through training, supervision, engagement quality review and continuous improvement. No error or catch-rate figures published.
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: ACCOUNTINGTODAY-HALLUC2-2026
  prerequisites:
    - An existing firm quality-management system (SQMS 1 / ISQM 1) that AI can be mapped into; a CIBA author argues an AI tool with no policy, approved list or documented review step is an unmanaged firm resource under ISQM 1 (ACCOUNTINGWEEKLY-B4-2026).
    - A reviewer who is qualified to assess the work (ACCOUNTINGTODAY-HALLUC2-2026).
  risks_and_guardrails:
    - Forvis Mazars says its guidance names AI-specific risks with no clean human analogue: hallucination patterns, overconfidence, automation bias, confirmation bias and anchoring bias (ACCOUNTINGTODAY-HALLUC2-2026).
    - A consultant quoted says a hallucination is a defect and should be handled through quality management, which applies to all CPA services and not only audit (ACCOUNTINGTODAY-HALLUC1-2026).
    - Quoted practitioners say mistakes may still slip through; one notes reviewers are often short of time and trust that colleagues checked every reference (ACCOUNTINGTODAY-HALLUC1-2026).
  human_checkpoints:
    - Planning-stage discussion of AI use; reviewer checklist; independent review of all deliverables; engagement quality review on higher-risk engagements (ACCOUNTINGTODAY-HALLUC2-2026).
    - Disclosure when AI materially contributed to externally facing content, with review against firm standards before release (ACCOUNTINGTODAY-HALLUC2-2026).
  role_evolution: >-
    Forvis Mazars says the professional must be able to defend AI-assisted content to a regulator or in court as if they had drafted it unaided (ACCOUNTINGTODAY-HALLUC2-2026). An AICPA leader says the profession must move from doing everything to supervising more, and supervising a bot requires understanding the underlying procedure (JOA-LEARN-2026).
  evidence_grade: B
  sources:
    - {ref: ACCOUNTINGTODAY-HALLUC2-2026, title: "False info, real problems: The human in the AI loop", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-the-human-in-the-ai-loop", date: "2026-09-02", access: full, locator: "Forvis Mazars (Denny Ard) and Schellman (Avani Desai) sections; 'Accountability and quality control'"}
    - {ref: ACCOUNTINGTODAY-HALLUC1-2026, title: "False info, real problems: Can accountants tame AI hallucinations?", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-can-accountants-tame-ai-hallucinations", date: "2026-09-02", access: full, locator: "Shimamoto and Reyes comments"}
    - {ref: ACCOUNTINGWEEKLY-B4-2026, title: "Big Four AI Hallucinations: What It Means for Your Practice", publisher: "Accounting Weekly (CIBA)", type: press, url: "https://www.accountingweekly.com/trending-news/big-four-ai-hallucinations-what-it-means-for-your-practice", date: "2026-09-09", access: full, locator: "ISQM 1 paragraph"}
    - {ref: JOA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: "2026-03-01", access: full, locator: "Carl Mayes quotes, paragraphs 5-9"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B because Forvis Mazars, Armanino and Schellman are named firms describing their own controls through trade press interviews; no measurements are published. Audit engagement-quality-review specifics belong to the assurance archetype.

- id: professional-services-quality-review-05
  title: Review gates built into AI workflows, with a named reviewer and mandatory sign-off before the next step
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Without forced checkpoints, a staff member can trust an AI output and each later reviewer assumes someone else validated it. Schellman's CEO guesses this is how hallucinated content reached outside audiences at large firms, calling it a control design problem (ACCOUNTINGTODAY-HALLUC1-2026).
  solution: >-
    Armanino says each AI step is designed as a mini use case with its own risk controls and mirrors its manual technical-memo flow: senior sets the facts, staff drafts, manager pre-reviews, partner signs off. The workflow has a step where the senior must tick a box confirming review and agreement before the next step (ACCOUNTINGTODAY-HALLUC2-2026). Harvey announced Legal Work Orchestration on 15 Oct 2026: tasks carry scope, inputs and a named reviewer, an agent produces (for example) a consent matrix, the partner is notified and approves, and only then does the next step begin (HARVEY-ORCH-2026).
  outcomes:
    - lever: quality
      description: No outcome measures published by Armanino. Harvey states an expectation, not a result.
      figure: "Harvey expects agents to take on an additional 20% of workflow steps over six months and triple that share within a year (forecast)"
      measures: "Forecast share of workflow steps executed by agents rather than prompted by lawyers; no baseline given."
      provenance: vendor-published
      source_ref: HARVEY-ORCH-2026
  prerequisites:
    - A defined process template (phases, tasks, reviewers) for the work type (HARVEY-ORCH-2026).
    - Reviewers who understand the procedure well enough to challenge the output (JOA-LEARN-2026).
  risks_and_guardrails:
    - A tick box can become a rubber stamp; MindBridge's methodology lead asks where the human sits and whether the reviewer is independent of the report's author (ACCOUNTINGTODAY-HALLUC2-2026).
    - Harvey says work performed by agents will remain transparent and auditable (HARVEY-ORCH-2026).
    - Cal Bar guidance says greater autonomy calls for stronger supervisory controls (CALBAR-GENAI-2026).
  human_checkpoints:
    - Senior confirms review before progression; partner approves agent outputs at designated gates (ACCOUNTINGTODAY-HALLUC2-2026; HARVEY-ORCH-2026).
  role_evolution: >-
    Harvey expects lawyers to spend more time directing the matter, reviewing consequential outputs and exercising judgment as agents execute more steps (HARVEY-ORCH-2026).
  evidence_grade: B
  sources:
    - {ref: ACCOUNTINGTODAY-HALLUC2-2026, title: "False info, real problems: The human in the AI loop", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-the-human-in-the-ai-loop", date: "2026-09-02", access: full, locator: "Armanino paragraphs (workflow checkbox)"}
    - {ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: "2026-10-15", access: full, locator: "'Keep Reviews and Next Steps Moving' and 'The Future of Legal Work Orchestration'"}
    - {ref: ACCOUNTINGTODAY-HALLUC1-2026, title: "False info, real problems: Can accountants tame AI hallucinations?", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-can-accountants-tame-ai-hallucinations", date: "2026-09-02", access: full, locator: "Desai comment on control design"}
    - {ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Executive Summary, 'Conclusion'; Duties of Competence and Diligence"}
    - {ref: JOA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: "2026-03-01", access: full, locator: "Mayes quotes"}
  last_reviewed: 2026-10-19
  notes: >-
    Armanino's workflow is in production per its AI practice lead; Harvey's feature is rolling out with template early access still by request (HARVEY-ORCH-2026), so the Harvey half is announced. The Cal Bar PDF carries only '2026' in its text; 2026-05 is the file creation date.

- id: professional-services-quality-review-06
  title: Firm AI-use policy with mandatory human review, independent verification, attestation and training, enforced rather than only written
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Policies exist but are not always followed. Sullivan & Cromwell's partner wrote that the firm has comprehensive policies and mandatory training telling lawyers to verify everything, and that the protocols were not followed in the Prince matter (CANLAWYER-SC-2026). Morae's survey finds 71% have formal policies but only 30% are confident they are applied (MORAE-ILR-2026).
  solution: >-
    White & Case recommends AI-use protocols that require verification of outputs, disclosure of AI use to supervising lawyers, safeguards on confidential data, and periodic attestations, plus regularly updated training (WHITECASE-VERIFY-2026). Professional liability insurers for CPA firms say they ask whether a firm uses AI, polices it and has protocols, and expect to formalise questions in a year or two; one recommends engagement-letter disclosure and a client opt-out (ACCOUNTINGTODAY-INSURERS-2026).
  outcomes:
    - lever: risk
      description: ILTA's 2026 survey shows how many firms require human review and verification, rising with firm size. Smallest firms (under 50 lawyers) versus the 350-699 band.
      figure: "Work product must be reviewed by a human: 31% (under 50 lawyers) to 83% (350-699); outputs must be cited or independently verified: 25% to 60%; formal policy in place: 57% to 98%"
      measures: "Share of responding firms in each lawyer-count band that selected each option as describing their official GenAI policy (Q3.18); 508 firms in the survey overall; self-described policies, not tested practice."
      provenance: independent
      source_ref: ILTA-TECHSURVEY-2026
    - lever: risk
      description: Morae survey on policy versus confidence in application.
      figure: "71% have formal policies; 30% confident they are applied"
      measures: "Share of 850 senior legal professionals (US, UK, Australia, Middle East) reporting formal AI policies, and share confident that policies are applied."
      provenance: vendor-published
      source_ref: MORAE-ILR-2026
  prerequisites:
    - Training before access: required by 11% of the smallest firms and 72% of the largest (ILTA-TECHSURVEY-2026, p.4).
    - A way to see actual AI use; 34% of surveyed professionals use AI tools their organisation has not sanctioned (TR-FOP-2026).
  risks_and_guardrails:
    - Static policies are not enough; they must be monitored and enforced (WHITECASE-VERIFY-2026).
    - Insurers have seen no substantive AI claims yet, according to Aon's risk-control lead, so underwriting questions are still informal (ACCOUNTINGTODAY-INSURERS-2026).
  human_checkpoints:
    - Supervisor or partner informed of intended AI use; periodic attestations by legal professionals (WHITECASE-VERIFY-2026).
    - Cal Bar guidance expects managerial lawyers to set AI policies and keep them updated as autonomy increases (CALBAR-GENAI-2026).
  role_evolution: >-
    Managing partners and innovation leads own AI policy and its monitoring; Cal Bar guidance places a duty on managerial and supervisory lawyers to provide training and update controls (CALBAR-GENAI-2026).
  evidence_grade: B
  sources:
    - {ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: "International Legal Technology Association", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "p.4, Q3.18 table and lead-in text"}
    - {ref: MORAE-ILR-2026, title: "The Intelligence Gap: Why AI in Legal Isn't Delivering and What Needs to Change", publisher: "Morae", type: survey, url: "https://www.morae.com/insights/the-intelligence-gap-why-ai-in-legal-isnt-delivering-and-what-needs-to-change/", date: "2026-07-08", access: full, locator: "summary bullets and FAQ"}
    - {ref: WHITECASE-VERIFY-2026, title: "Verify, Guide, Train: Lessons From Emerging Attorney AI-Misuse Caselaw", publisher: "White & Case", type: firm, url: "https://www.whitecase.com/sites/default/files/2026-04/verify-guide-train-lessons-from-emerging-attorney-ai-misuse-case-law.pdf", date: "2026-04-15", access: full, locator: "'Establish Clear AI-Use Guidelines' section"}
    - {ref: CANLAWYER-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: "Canadian Lawyer", type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: "2026-04-22", access: full, locator: "paragraphs 4-5"}
    - {ref: ACCOUNTINGTODAY-INSURERS-2026, title: "Insurers eyeing AI risk at CPA firms", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/insurers-eyeing-ai-risk-at-cpa-firms", date: "2026-04-21", access: full, locator: "Sterna, Raspante and Florian comments"}
    - {ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: "2026", access: full, locator: "opening findings (34% unsanctioned use)"}
    - {ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Duty to Supervise Lawyers and Nonlawyers row"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B, not A: the ILTA data measure adoption of requirements, not quality outcomes. The ILTA PDF's file name suggests June 2026 (as the landscape file recorded) but its file metadata says Aug 2026. TR-FOP-2026 fieldwork was March-April 2026 and the page shows no publication date. Policy-sets differ by firm size sharply, so averages across all firms should not be quoted.

- id: professional-services-quality-review-07
  title: Attorney-led testing and benchmarking of AI tools and workflows before and after deployment
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Vendor claims of hallucination-free output were found overstated, and buyers lack error-rate evidence. Stanford researchers found leading legal research tools hallucinated 17% to 33% of the time (STANFORD-MAGESH-2024). A researcher analysing New York court records reports they repeatedly call for error rates and do-not-use lists that do not exist (ARXIV-WILLIAMS-2026).
  solution: >-
    Firms test tools on their own cases and known answers before relying on them. A firm managing director who sits on bar technology committees described benchmarking AI and legal research tools using questions whose answers are known (ABA-LPT-PAYKIN-2026). ILTACON 2026 listed a session on validating AI workflows in eDiscovery (the abstract asks how to prove it worked) and another, with Littler and Ogletree Deakins speakers, on attorney-led testing of accuracy, reliability and workflow fit (EDISCOVERYTODAY-ILTACONTUE-2026).
  outcomes:
    - lever: quality
      description: Independent evaluation of eight legal retrieval-augmented systems on GDPR (English) and a national civil-law corpus (French).
      figure: "hallucinations in less than 10% of responses for the best systems to nearly half in the worst case"
      measures: "Share of responses with hallucinations across eight legal RAG systems on two corpora, claim-level and answer-level evaluation, validated on 142 expert-written questions; false-premise questions produced high rates."
      provenance: independent
      source_ref: ARXIV-LUX-2026
    - lever: quality
      description: Pre-registered Stanford evaluation of commercial legal research tools (2024, outside the 18-month window; foundation).
      figure: "17% to 33%"
      measures: "Share of queries on which Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI hallucinated, as stated in the abstract."
      provenance: independent
      source_ref: STANFORD-MAGESH-2024
  prerequisites:
    - A known-answer test set built by practising lawyers; re-testing after model or product updates (Cal Bar guidance expects periodic reassessment of the system's capabilities and risks, CALBAR-GENAI-2026).
  risks_and_guardrails:
    - Benchmarks are snapshots; Vals says its first legal AI report is a snapshot that must be repeated, and vendors opted into tasks (VALS-VLAIR-2025).
    - Researchers argue citation-existence and answer-accuracy metrics can miss failures where the cited authority does not support the claim (ARXIV-TARANUKHIN-2026).
  human_checkpoints:
    - Attorneys score outputs and feed results into governance and vendor selection (EDISCOVERYTODAY-ILTACONTUE-2026, session learning objectives).
  role_evolution: >-
    Knowledge-management and innovation staff and practising lawyers become test designers and scorers rather than only tool users (EDISCOVERYTODAY-ILTACONTUE-2026).
  evidence_grade: B
  sources:
    - {ref: ABA-LPT-PAYKIN-2026, title: "Picking the Right Legal Tech Tools Ahead of ABA TECHSHOW", publisher: "Law Practice Today podcast (ABA Law Practice Division)", type: podcast, url: "https://rss.buzzsprout.com/2268467.rss", date: "2026-03-23", access: full, locator: "episode description (feed item dated 23 Mar 2026)"}
    - {ref: EDISCOVERYTODAY-ILTACONTUE-2026, title: "Tuesday Happenings at ILTACON 2026", publisher: "eDiscovery Today", type: conference, url: "https://ediscoverytoday.com/2026/08/25/tuesday-happenings-at-iltacon-2026-ediscovery-trends/", date: "2026-08-25", access: full, locator: "'Trust but Verify' and 'Managing AI Tool Overload' session listings"}
    - {ref: ARXIV-LUX-2026, title: "How Much Do Legal RAG Systems Still Hallucinate? (arXiv 2608.14210)", publisher: "Das, Abualhaija, Bianculli (University of Luxembourg)", type: academic, url: "https://arxiv.org/abs/2608.14210", date: "2026-08-14", access: full, locator: "abstract"}
    - {ref: STANFORD-MAGESH-2024, title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)", publisher: "Stanford RegLab/HAI", type: academic, url: "https://arxiv.org/abs/2405.20362", date: "2024-05-30", access: full, locator: "abstract"}
    - {ref: ARXIV-WILLIAMS-2026, title: "From Process to Evidence: How Computing Can Ground Appropriate Reliance on Legal AI (arXiv 2607.28869)", publisher: "James Bryan Williams", type: academic, url: "https://arxiv.org/abs/2607.28869", date: "2026-07-30", access: full, locator: "abstract"}
    - {ref: ARXIV-TARANUKHIN-2026, title: "Legal LLM Hallucination Should Be Evaluated as Failure of Legal Warrant (arXiv 2609.17546)", publisher: "Taranukhin and Shwartz (AI4Law at ICML 2026)", type: academic, url: "https://arxiv.org/abs/2609.17546", date: "2026-07-15", access: full, locator: "abstract"}
    - {ref: VALS-VLAIR-2025, title: "Vals Legal AI Report", publisher: "Vals AI", type: academic, url: "https://www.vals.ai/vlair", date: "2025-02", access: full, locator: "Executive summary; Introduction"}
    - {ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Duties of Competence and Diligence, last paragraph"}
  last_reviewed: 2026-10-19
  notes: >-
    The outcome figures measure tool accuracy in studies, not the effect of firms' testing programmes, so they are adjacent evidence; the entry stays at B on the basis of the practitioner who describes the practice, and the ILTACON listings are abstracts, not what was said in the room. The arXiv ID 2609.17546 does not match its stated submission date (15 Jul 2026), so that date may be the submission date and not the ID month. Vals is a company with customer relationships with participants, noted in its own acknowledgments. A search summary also attributed the 'attorney-led testing' learning objectives to the validation session; the listing shows they belong to the tool-overload session.

- id: professional-services-quality-review-08
  title: "Idea (in-house): standard verification techniques to cut the review burden on AI output"
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Morae's survey of 850 senior legal professionals finds 67% fear that the cost of human checking outweighs AI's benefits and 48% must materially change outputs before use (MORAE-ILR-2026). A Best Lawfirms writer calls this the verification tax and says no one knows how much firms will actually save (BESTLAWFIRMS-VTAX-2026).
  solution: >-
    Idea discussed by practitioners (not a measured deployment): teach legal teams quick, repeatable ways to verify AI output so review time falls. CLOC's May 2026 'Legal Hacks' item is titled Kill the Verification Burden and promises techniques to verify outputs quickly and consistently, reducing review time (CLOC-VERIFICATION-2026). At CGI 2026 an Anthropic speaker argued for explicit written principles on who is accountable for outputs and where the lawyer intervenes (STENO-CLOC-2026).
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: CLOC-VERIFICATION-2026
  prerequisites:
    - Data readiness; only 26% of Morae's respondents think their information is ready for AI (MORAE-ILR-2026).
  risks_and_guardrails:
    - Morae's author is a legal services provider selling a remedy, so its framing is vendor-published (MORAE-ILR-2026).
    - Faster checks must not lower the bar; courts treat verification as the lawyer's duty (WHITECASE-VERIFY-2026).
  human_checkpoints:
    - Lawyer remains accountable for outputs (STENO-CLOC-2026).
  role_evolution: >-
    Steno's recap says the friction for legal operations leaders is no longer access to tools but whether they have governance, accuracy benchmarks and workflow design (STENO-CLOC-2026).
  evidence_grade: D
  sources:
    - {ref: CLOC-VERIFICATION-2026, title: "Kill the Verification Burden", publisher: "CLOC", type: professional-body, url: "https://cloc.org/blog/legal-hacks/kill-the-verification-burden/", date: "2026-05-13", access: full, locator: "page summary line (page body is a short teaser for a webinar)"}
    - {ref: MORAE-ILR-2026, title: "The Intelligence Gap: Why AI in Legal Isn't Delivering and What Needs to Change", publisher: "Morae", type: survey, url: "https://www.morae.com/insights/the-intelligence-gap-why-ai-in-legal-isnt-delivering-and-what-needs-to-change/", date: "2026-07-08", access: full, locator: "summary bullets"}
    - {ref: BESTLAWFIRMS-VTAX-2026, title: "The Verification Tax: Why AI Might Cost Law Firms More Than It Saves", publisher: "Best Lawfirms (David L. Brown)", type: press, url: "https://www.bestlawfirms.com/articles/ai-verification-tax-tokenization-law-firm-costs/8490", date: "2026-09-23", access: full, locator: "opening and 'A Key Question' sections"}
    - {ref: STENO-CLOC-2026, title: "CLOC Global Institute 2026: Stronger By Design, Built By Community", publisher: "Steno (conference recap by a court-reporting vendor)", type: conference, url: "https://brief.steno.com/cloc-global-institute-2026-recap", date: "2026-06-03", access: full, locator: "Anthropic 'AI Constitution' passage; 'Stronger By Design, In Practice' list"}
    - {ref: WHITECASE-VERIFY-2026, title: "Verify, Guide, Train: Lessons From Emerging Attorney AI-Misuse Caselaw", publisher: "White & Case", type: firm, url: "https://www.whitecase.com/sites/default/files/2026-04/verify-guide-train-lessons-from-emerging-attorney-ai-misuse-case-law.pdf", date: "2026-04-15", access: full, locator: "'Trust, but Verify'"}
  last_reviewed: 2026-10-19
  notes: >-
    In-house. Labelled idea: the CLOC page is a webinar teaser and the session content was not seen. Morae's sample is described as senior legal professionals and legal leaders; whether all are in-house was not confirmed. Search results also described a Lawmatics claim of verification cutting intake review from 30-45 minutes to 5-10; it is marketing with no data and was not opened.

- id: professional-services-quality-review-09
  title: Disclosing AI use and verification to clients, in engagement terms and in the deliverable
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Clients want to know and are not consistently told. Morae finds 73% of respondents say clients deserve full visibility into AI use on their matters but only 21% deliver it (MORAE-ILR-2026). TRI reports clients asking, at Legalweek 2026, for line-item transparency on whether AI was used on a task (TRI-LEGALWEEK-2026).
  solution: >-
    Forvis Mazars' policy requires disclosure when AI materially contributed to externally facing content, with review against its accuracy standards before release (ACCOUNTINGTODAY-HALLUC2-2026). Deloitte Australia's revised report disclosed that a generative AI language system (Azure OpenAI) was used in writing it (CTV-DELOITTE-2025). A CPA liability-insurance risk manager recommends engagement-letter language disclosing AI use and a client opt-out clause (ACCOUNTINGTODAY-INSURERS-2026). Cal Bar guidance asks lawyers to consider disclosing intended AI use and to follow client instructions that limit it (CALBAR-GENAI-2026).
  outcomes:
    - lever: risk
      description: Morae's disclosure gap.
      figure: "73% say clients deserve full visibility; 21% deliver it"
      measures: "Share of 850 senior legal professionals saying clients deserve full visibility into AI use on their matters, and share reporting they deliver it."
      provenance: vendor-published
      source_ref: MORAE-ILR-2026
  prerequisites:
    - Ability to tell which deliverables AI touched (usage logging); a firm rule on what counts as material contribution (ACCOUNTINGTODAY-HALLUC2-2026).
  risks_and_guardrails:
    - Clients are inconsistent: some demand AI use, others send guidelines requiring permission or refusing to pay for AI-done work (TRI-LEGALWEEK-2026).
    - Disclosure does not replace verification; Deloitte Australia's disclosure came after the errors were found (CTV-DELOITTE-2025).
  human_checkpoints:
    - Partner confirms disclosure language and client instructions before delivery (CALBAR-GENAI-2026).
  role_evolution: >-
    DLA Piper's AI innovation head advises firms to lead the client conversation on AI value and terms rather than wait for clients (TRI-LEGALWEEK-2026).
  evidence_grade: B
  sources:
    - {ref: ACCOUNTINGTODAY-HALLUC2-2026, title: "False info, real problems: The human in the AI loop", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-the-human-in-the-ai-loop", date: "2026-09-02", access: full, locator: "Ard comment on acceptable-use policy and disclosure"}
    - {ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "CTV News (Associated Press)", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: "2025-10-07", access: full, locator: "paragraph on revised version"}
    - {ref: ACCOUNTINGTODAY-INSURERS-2026, title: "Insurers eyeing AI risk at CPA firms", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/insurers-eyeing-ai-risk-at-cpa-firms", date: "2026-04-21", access: full, locator: "Raspante comment"}
    - {ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Communication Regarding Generative AI Use row"}
    - {ref: MORAE-ILR-2026, title: "The Intelligence Gap: Why AI in Legal Isn't Delivering and What Needs to Change", publisher: "Morae", type: survey, url: "https://www.morae.com/insights/the-intelligence-gap-why-ai-in-legal-isnt-delivering-and-what-needs-to-change/", date: "2026-07-08", access: full, locator: "summary bullets"}
    - {ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: "2026-03-13", access: full, locator: "'The contradictions in the room' section"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B rests on Forvis Mazars' stated policy and the Deloitte Australia revised report; no firm reports client response to disclosure. Billing and pricing aspects of AI line items are routed to billing-collections.

- id: professional-services-quality-review-10
  title: Tiered oversight for agentic work (lawyer in the loop versus agent in the loop) with defined escalation triggers and no autonomous external action
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Agentic tools can start and finish tasks without human prompting, which Cal Bar says raises the risk that a lawyer relies on automated steps without contemporaneous review (CALBAR-GENAI-2026).
  solution: >-
    Practitioners frame three oversight designs: human in the loop (lawyer does the work), lawyer in the loop (AI does the work, lawyer reviews and decides) and agent in the loop (agent acts; lawyer is called only when defined criteria trigger), as presented at CLOC CGI 2026 by an Anthropic go-to-market lead (STENO-CLOC-2026). Cal Bar's 2026 guidance bars agentic systems from making substantive legal determinations, communicating advice or filing without meaningful lawyer supervision, and says no document may reach a court without lawyer review and approval (CALBAR-GENAI-2026). Harvey's orchestration puts reviews at designated gates (HARVEY-ORCH-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: STENO-CLOC-2026
  prerequisites:
    - Written principles for how AI is deployed, who is accountable for outputs and where the lawyer intervenes (STENO-CLOC-2026).
    - Understanding of the system's autonomy, data access and failure modes (CALBAR-GENAI-2026).
  risks_and_guardrails:
    - Supervision must scale with autonomy; agents with access to email, document systems and client files can disclose confidential material across matters (CALBAR-GENAI-2026).
    - A US law-firm attorney surveyed by TRI said agentic AI removes oversight a step too far, preferring prompt-and-review (TR-AIPS-2026).
  human_checkpoints:
    - Lawyer approval before any filing, court communication or external transmission (CALBAR-GENAI-2026).
    - Defined trigger criteria for escalation to a lawyer (STENO-CLOC-2026).
  role_evolution: >-
    Lawyers shift toward specifying escalation criteria and reviewing consequential outputs, as Harvey expects (HARVEY-ORCH-2026).
  evidence_grade: C
  sources:
    - {ref: STENO-CLOC-2026, title: "CLOC Global Institute 2026: Stronger By Design, Built By Community", publisher: "Steno (conference recap by a court-reporting vendor)", type: conference, url: "https://brief.steno.com/cloc-global-institute-2026-recap", date: "2026-06-03", access: full, locator: "'AI Constitution' passage"}
    - {ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Executive Summary (Agentic AI); Candor to the Tribunal row"}
    - {ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: "2026-10-15", access: full, locator: "'The Future of Legal Work Orchestration'"}
    - {ref: TR-AIPS-2026, title: "2026 AI in Professional Services Report", publisher: "Thomson Reuters Institute", type: survey, url: "https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf", date: "2026-01", access: full, locator: "Agentic AI section, attorney quote on oversight"}
  last_reviewed: 2026-10-19
  notes: >-
    The three-tier framing is a conference presentation by a vendor, not a documented firm deployment. The TR-AIPS date is the PDF file creation date (27 Jan 2026); the survey (1,514 respondents) was fielded in autumn 2025. In-house legal teams (JLL, Delta) were reported at CGI as adopting multi-LLM stacks and Copilot with department use-case sharing; the recap does not describe their review controls (STENO-CLOC-2026).

- id: professional-services-quality-review-11
  title: Error response protocol - disclose, correct, and re-review the whole matter
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    After an AI error is found, the response decides the consequence. White & Case describes a sanctioned large firm that resubmitted a revised brief still containing a half-dozen AI errors and did not disclose AI's role (WHITECASE-VERIFY-2026). An Oregon appeals decision criticised a lawyer for a quiet correction without acknowledgment (ABA-LPT-WILLIAMS-2026).
  solution: >-
    Sullivan & Cromwell's 18 Apr 2026 letter to the court took personal responsibility, filed a corrected motion with a redline and a schedule of corrections, said it had reviewed how the errors occurred and re-reviewed all filings in the matter, and thanked opposing counsel who flagged the errors (CANLAWYER-SC-2026). Deloitte Australia revised its report, replaced the questioned citations and disclosed AI use (CTV-DELOITTE-2025). EY Canada and KPMG withdrew reports pending review (ACS-EY-2026; TECHCRUNCH-KPMG-2026).
  outcomes:
    - lever: risk
      description: Sullivan & Cromwell reported that its re-review of all filings in the Prince matter found no other AI-related issues but did find additional non-substantive or clerical errors. This is a statement in a letter to the court, not a tracked metric.
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: CANLAWYER-SC-2026
  prerequisites:
    - A named owner for incident response and a standing rule to disclose to the court or client.
  risks_and_guardrails:
    - Courts treat concealment as worse than the error (ABA-LPT-WILLIAMS-2026; WHITECASE-VERIFY-2026).
    - Deloitte did not say whether AI generated the errors and said the matter was resolved directly with the client (CTV-DELOITTE-2025).
  human_checkpoints:
    - Partner takes responsibility under the court's Rule 11 equivalent; re-review of every document in the matter (CANLAWYER-SC-2026).
  role_evolution: >-
    Partners, not tools, answer to courts and clients; the S&C partner personally telephoned opposing counsel (CANLAWYER-SC-2026).
  evidence_grade: B
  sources:
    - {ref: CANLAWYER-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: "Canadian Lawyer", type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: "2026-04-22", access: full, locator: "paragraphs 4-8"}
    - {ref: ABA-LPT-WILLIAMS-2026, title: "Avoiding AI Hallucinations in Legal Practice", publisher: "Law Practice Today podcast (ABA Law Practice Division)", type: podcast, url: "https://lawpracticetoday.buzzsprout.com/2268467/episodes/19275322-avoiding-ai-hallucinations-in-legal-practice", date: "2026-06-15", access: full, locator: "episode description"}
    - {ref: ABA-LPT-SC-2026, title: "AI Hallucinations in Court - The Sullivan & Cromwell Lesson", publisher: "Law Practice Today podcast (ABA Law Practice Division)", type: podcast, url: "https://rss.buzzsprout.com/2268467.rss", date: "2026-06-30", access: full, locator: "feed item Buzzsprout-19424504, description"}
    - {ref: WHITECASE-VERIFY-2026, title: "Verify, Guide, Train: Lessons From Emerging Attorney AI-Misuse Caselaw", publisher: "White & Case", type: firm, url: "https://www.whitecase.com/sites/default/files/2026-04/verify-guide-train-lessons-from-emerging-attorney-ai-misuse-case-law.pdf", date: "2026-04-15", access: full, locator: "'Establish Clear AI-Use Guidelines' (Lacey)"}
    - {ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "CTV News (Associated Press)", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: "2025-10-07", access: full, locator: "article body"}
    - {ref: ACS-EY-2026, title: "EY retracts cyber report littered with AI errors", publisher: "Information Age (ACS)", type: press, url: "https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html", date: "2026-05-19", access: full, locator: "paragraphs 2-5"}
    - {ref: TECHCRUNCH-KPMG-2026, title: "KPMG pulls report on AI usage due to apparent hallucinations", publisher: "TechCrunch", type: press, url: "https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/", date: "2026-06-13", access: full, locator: "paragraphs 2-4"}
  last_reviewed: 2026-10-19
  notes: >-
    Grade B on the S&C letter as reported by Canadian Lawyer; the letter itself and Global Legal Post (blocked) were not opened. The ABA podcast attribution to the Oregon Williams decision comes from the episode description only.

- id: professional-services-quality-review-12
  title: Scan incoming third-party work (opposing briefs, contractors, suppliers' reports) for fabricated authority and references
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Errors enter through other people's work. In Deghani v. Castro, a lawyer's contracted freelance attorney returned a brief with hallucinated cases that he did not check, and the court upheld sanctions (TRI-HALLUC-2025). An Alberta appeal decision held counsel bears ultimate responsibility for AI-hallucinated citations in a factum drafted by a third-party contractor (CANLAWYER-SC-2026).
  solution: >-
    Treat contractor, subordinate and counterparty documents as unverified inputs. In practice outsiders have been the detectors: opposing counsel at Boies Schiller flagged the Sullivan & Cromwell errors (CANLAWYER-SC-2026), a Sydney University researcher found the Deloitte Australia errors (CTV-DELOITTE-2025), and The Independent found Deloitte Canada's (FORTUNE-DELOITTE-2025). Thomson Reuters says CoCounsel Legal's Litigation Document Analyzer identifies potential misrepresentations of law across a whole brief, the firm's own or opposing counsel's (TR-CANTSIGN-2026).
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: CANLAWYER-SC-2026
  prerequisites:
    - A routine step to check opposing and third-party filings; access to a checker or corpus (TR-CANTSIGN-2026).
  risks_and_guardrails:
    - Courts apply an objective reasonableness standard: counsel with 'an empty head and a pure heart' is still responsible (TRI-HALLUC-2025, quoting the court).
  human_checkpoints:
    - Supervising lawyer verifies everything a contractor or junior returns before signing (TRI-HALLUC-2025).
  role_evolution: >-
    In the cases read, outsiders (opposing counsel, an academic, a news outlet, GPTZero) found the errors; in-firm detection of incoming work is not documented (CANLAWYER-SC-2026; CTV-DELOITTE-2025; FORTUNE-DELOITTE-2025).
  evidence_grade: B
  sources:
    - {ref: CANLAWYER-SC-2026, title: "Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case", publisher: "Canadian Lawyer", type: press, url: "https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014", date: "2026-04-22", access: full, locator: "paragraphs 5, 9-11"}
    - {ref: TRI-HALLUC-2025, title: "GenAI hallucinations are still pervasive in legal filings, but better lawyering is the cure", publisher: "Thomson Reuters Institute", type: press, url: "https://www.thomsonreuters.com/en-us/posts/technology/genai-hallucinations/", date: "2025-08-18", access: full, locator: "Deghani v. Castro paragraphs"}
    - {ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "CTV News (Associated Press)", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: "2025-10-07", access: full, locator: "paragraphs 2-3, 7"}
    - {ref: FORTUNE-DELOITTE-2025, title: "Deloitte allegedly cited AI-generated research in a million-dollar report for a Canadian provincial government", publisher: "Fortune", type: press, url: "https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government", date: "2025-11-25", access: full, locator: "paragraphs 1-3"}
    - {ref: TR-CANTSIGN-2026, title: "If You Can't Verify It, You Can't Sign It", publisher: "Thomson Reuters Innovation Blog", type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/if-you-cant-verify-it-you-cant-sign-it/", date: "2026-05-05", access: full, locator: "Litigation Document Analyzer sentence"}
  last_reviewed: 2026-10-19
  notes: >-
    The in-production basis is that external detection has happened repeatedly; no firm was found that runs a routine incoming-work scan. The count of court cases in public trackers varies by source and date (see module notes).

- id: professional-services-quality-review-13
  title: AI-assisted firm-level quality-management monitoring and engagement quality review workflow
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    SQMS 1 / ISQM 1 require firms to run a monitored system of quality management, and SQMS 2 / ISQM 2 add requirements on reviewer eligibility, timely performance and documentation (CPAPA-AUDITFILE-2025).
  solution: >-
    AuditFile announced QualityLink on 4 Dec 2025, combining agentic AI with its audit automation to identify firm-level quality risks mapped to SQMS 1 / ISQM 1 components, evaluate controls, flag deficiencies, track remediation and manage engagement quality review workflows (CPAPA-AUDITFILE-2025).
  outcomes:
    - lever: capacity
      description: The vendor says the platform reduces administrative burden and strengthens consistency; no measured result published. QualityLink is stated to be available to all AuditFile customers.
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: CPAPA-AUDITFILE-2025
  prerequisites:
    - Documented risk assessment and controls to monitor (CPAPA-AUDITFILE-2025).
  risks_and_guardrails:
    - The press report is the vendor's release; it does not describe safeguards or limits of the AI (CPAPA-AUDITFILE-2025).
  human_checkpoints:
    - Engagement quality reviewer performs and documents the review (CPAPA-AUDITFILE-2025).
  role_evolution: >-
    Quality leaders spend less time on administration and more on remediation (vendor claim, CPAPA-AUDITFILE-2025).
  evidence_grade: C
  sources:
    - {ref: CPAPA-AUDITFILE-2025, title: "AuditFile Launches New QualityLink Solution for CPA Firms", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2025/12/04/auditfile-launches-new-qualitylink-solution-for-cpa-firms/174297/", date: "2025-12-04", access: full, locator: "paragraphs 1-6"}
  last_reviewed: 2026-10-19
  notes: >-
    Audit-specific quality review is for the assurance archetype; the firm-level quality-management element is retained here. No firm customer was named in the press report.

- id: professional-services-quality-review-14
  title: Idea - AI review tool that preparers run on their own work before it goes to the manager
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Reviewing is normally a senior, manager and partner task and takes training time from managers (JOA-LEARN-2026).
  solution: >-
    A BYU accounting professor described building an AI-based Excel tool that automates parts of the review process and is used by entry-level staff, who see problems and fix them before sending work to their manager, receiving detailed feedback without manager time (JOA-LEARN-2026).
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: JOA-LEARN-2026
  prerequisites:
    - Review criteria that can be encoded in a tool (JOA-LEARN-2026).
  risks_and_guardrails:
    - Not discussed in the source, which frames the tool as pre-manager feedback that compresses learning cycles (JOA-LEARN-2026).
  human_checkpoints:
    - Staff fix flagged problems before sending work to their manager (JOA-LEARN-2026).
  role_evolution: >-
    The source says AI affects every rung of the career ladder at once and may compress learning cycles (JOA-LEARN-2026).
  evidence_grade: D
  sources:
    - {ref: JOA-LEARN-2026, title: "How will accountants learn new skills when AI does the work?", publisher: "Journal of Accountancy (AICPA)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/", date: "2026-03-01", access: full, locator: "section 'AI affects all rungs of the career ladder'"}
  last_reviewed: 2026-10-19
  notes: Labelled idea. An academic describes a tool he built; where it is used and with what results is not stated.

- id: professional-services-quality-review-15
  title: Idea - calibrate reviewer reliance with measured error rates, shared metrics and seeded-error tests
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Review today is process without evidence. An analysis of the New York court system's AI documents finds they call for error rates and do-not-use lists that do not exist and invoke training mandates, checklists and uncalibrated human review instead (ARXIV-WILLIAMS-2026). A TRI webinar speaker notes that when a tool produces 50 pages of confident text, spotting the flaw buried in it is harder than catching one wrong answer (TRI-NEED2KNOW-2026). A Hacker News commenter argued that manual review cannot catch all errors, which many people find unacceptable (HN-KPMG-2026).
  solution: >-
    Researchers propose task taxonomies, shared error metrics, maintained benchmarks and test harnesses for evaluations on private data (ARXIV-WILLIAMS-2026), and a claim-authority warrant metric that scores whether cited authority exists, applies, is current and supports the claim (ARXIV-TARANUKHIN-2026). For firms, this would mean measuring what reviewers catch, not just requiring review.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: independent
      source_ref: ARXIV-WILLIAMS-2026
  prerequisites:
    - Task-level error data from the firm's own reviews and a test harness that does not expose client data (ARXIV-WILLIAMS-2026).
  risks_and_guardrails:
    - Not discussed in the sources read.
  human_checkpoints:
    - Not described in the sources read.
  role_evolution: >-
    Forvis Mazars separates back-tracing against source from a casual read-through with skepticism (ACCOUNTINGTODAY-HALLUC2-2026); no source describes measuring which reviewers do which.
  evidence_grade: D
  sources:
    - {ref: ARXIV-WILLIAMS-2026, title: "From Process to Evidence: How Computing Can Ground Appropriate Reliance on Legal AI (arXiv 2607.28869)", publisher: "James Bryan Williams", type: academic, url: "https://arxiv.org/abs/2607.28869", date: "2026-07-30", access: full, locator: "abstract"}
    - {ref: ARXIV-TARANUKHIN-2026, title: "Legal LLM Hallucination Should Be Evaluated as Failure of Legal Warrant (arXiv 2609.17546)", publisher: "Taranukhin and Shwartz (AI4Law at ICML 2026)", type: academic, url: "https://arxiv.org/abs/2609.17546", date: "2026-07-15", access: full, locator: "abstract"}
    - {ref: TRI-NEED2KNOW-2026, title: "What lawyers need to know about AI in 2026: Key lessons on hallucinations, ethics & education", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/what-lawyers-need-to-know-about-ai-2026", date: "2026-10-05", access: full, locator: "'Human review is more than proofreading'"}
    - {ref: HN-KPMG-2026, title: "KPMG pulls report on AI usage due to apparent hallucinations (discussion thread)", publisher: "Hacker News", type: community, url: "https://news.ycombinator.com/item?id=48527297", date: "2026-06-14", access: full, locator: "comment thread under 'I do not understand how these consultancies continue to mess this up'"}
    - {ref: ACCOUNTINGTODAY-HALLUC2-2026, title: "False info, real problems: The human in the AI loop", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/false-info-real-problems-the-human-in-the-ai-loop", date: "2026-09-02", access: full, locator: "Ard comment on back-tracing"}
  last_reviewed: 2026-10-19
  notes: Labelled idea; discussed by researchers and commenters, with no firm programme found. The Hacker News comment is anonymous and unverified.

- id: professional-services-quality-review-16
  title: Second-agent cross-check of references and figures before human review
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Human checking of every reference is slow, and reviewers skimming browser tabs can miss near-match citations (HN-KPMG-2026).
  solution: >-
    Hacker News commenters proposed a sub-agent that validates references and figures, or adversarial agents that build a reference table and check links, with humans reviewing only low-confidence items (HN-KPMG-2026). Harvey says its agent checks its own work against what the user asked (HARVEY-GRAPH-2026). Counterpoints: a TRI Labs scientist says systems that appear to check their own work are still predicting, so loops give no guarantee (TRI-NEED2KNOW-2026); ABA podcast speakers say to verify citations in Lexis or Westlaw and not with AI (ABA-LPT-SC-2026).
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: HARVEY-GRAPH-2026
  prerequisites:
    - Not described beyond the commenters' suggestions (HN-KPMG-2026).
  risks_and_guardrails:
    - A TRI Labs scientist warns that self-checking loops give no guarantee of accuracy (TRI-NEED2KNOW-2026).
    - GPTZero's KPMG findings include near-match citations a cursory check could pass, per a commenter (HN-KPMG-2026).
  human_checkpoints:
    - Humans verify flagged and low-confidence references (HN-KPMG-2026).
  role_evolution: >-
    Not documented in the sources read.
  evidence_grade: C
  sources:
    - {ref: HN-KPMG-2026, title: "KPMG pulls report on AI usage due to apparent hallucinations (discussion thread)", publisher: "Hacker News", type: community, url: "https://news.ycombinator.com/item?id=48527297", date: "2026-06-14", access: full, locator: "comments by XenophileJKO, figassis, SpicyLemonZest"}
    - {ref: HARVEY-GRAPH-2026, title: "Improving Agent Accuracy With Harvey Graph", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph", date: "2026-10-19", access: full, locator: "'What's in Harvey Graph Today'"}
    - {ref: TRI-NEED2KNOW-2026, title: "What lawyers need to know about AI in 2026: Key lessons on hallucinations, ethics & education", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/what-lawyers-need-to-know-about-ai-2026", date: "2026-10-05", access: full, locator: "Hudzina paragraph"}
    - {ref: ABA-LPT-SC-2026, title: "AI Hallucinations in Court - The Sullivan & Cromwell Lesson", publisher: "Law Practice Today podcast (ABA Law Practice Division)", type: podcast, url: "https://rss.buzzsprout.com/2268467.rss", date: "2026-06-30", access: full, locator: "feed item Buzzsprout-19424504, description"}
  last_reviewed: 2026-10-19
  notes: Grade C rests on a vendor statement; the community suggestions are opinion. Contested in the sources, so no outcome is claimed.

- id: professional-services-quality-review-17
  title: "In-house: clients ask outside firms for matter-level evidence of AI use, quality and savings"
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients and firms diverge. At Legalweek 2026, GSK's chief of staff for legal and compliance said clients now ask what firms use, how, and how it generates savings; firm speakers said they were still gathering the data and ROI measurement rested on conventional wisdom (TRI-LEGALWEEK-2026). A corporate chief legal officer told TRI that quality still has to be checked and humans responsible, as with junior associate work (TR-AIPS-2026).
  solution: >-
    Ropes & Gray's technology innovation director said clients are beginning to ask for line-item transparency on whether AI was used on a task; DLA Piper's AI head said other clients' guidelines require permission or say they will not pay for work done by AI; GSK said it wants to partner with firms on use cases (TRI-LEGALWEEK-2026). TRI's survey finds 78% of corporate clients rate AI-enabled quality improvements very important or essential (TR-FOP-2026).
  outcomes:
    - lever: quality
      description: TRI's client versus provider gap.
      figure: "78% of corporate clients rate AI-enabled quality improvements very important or essential; 6% say most or all providers deliver them"
      measures: "Share of corporate-client respondents (within 1,816 professionals surveyed in March-April 2026) rating AI-enabled quality improvements as very important or essential, and share saying most or all of their providers deliver them."
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - Matter-level tracking of AI use and its effect on cost; firm speakers said they were still gathering the data (TRI-LEGALWEEK-2026).
  risks_and_guardrails:
    - Client guidelines conflict: some demand AI use while others forbid it without permission or demand unbiased-model warrants (TRI-LEGALWEEK-2026).
  human_checkpoints:
    - Client and firm agree measures and how value is shared (TRI-LEGALWEEK-2026).
  role_evolution: >-
    Greenberg Traurig's Chief Pricing and Innovation Officer said clients who had been silent on AI are now asking how it is used on their specific matters (TRI-LEGALWEEK-2026).
  evidence_grade: C
  sources:
    - {ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: "2026-03-13", access: full, locator: "'Proving AI's path to saving clients money'; 'The contradictions in the room'"}
    - {ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: "2026", access: full, locator: "'AI capability is now a procurement criterion' paragraph"}
    - {ref: TR-AIPS-2026, title: "2026 AI in Professional Services Report", publisher: "Thomson Reuters Institute", type: survey, url: "https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf", date: "2026-01", access: full, locator: "client-firm gap section, CLO quote"}
  last_reviewed: 2026-10-19
  notes: In-house. TRI is part of Thomson Reuters, a vendor, so the survey figure is treated as vendor-published. The billing consequences (clients refusing to pay for AI-done work) are routed to billing-collections.
```

## 3. Module notes

### Processes and key steps (with work types)

- **Matter or engagement review and sign-off** (review-assurance): preparer draft, senior set-up, manager pre-review, partner sign-off; Armanino mirrors this in its AI workflow (ACCOUNTINGTODAY-HALLUC2-2026).
- **Citation and authority verification before filing** (review-assurance): read each authority, check the quote and the proposition; Clearbrief and Filevine automate the first pass (LAWSITES-CLEARBRIEF-2025; LAWSITES-FILEVINE-2026).
- **Pre-release review of reports and thought leadership** (review-assurance, document-production): the step that failed in the Deloitte, EY, KPMG and PwC cases (GPTZERO-KPMG-2026; GPTZERO-PWC-2026).
- **Firm-level quality management and engagement quality review** (review-assurance, coordination-scheduling): SQMS 1 / ISQM 1 and SQMS 2 / ISQM 2 (CPAPA-AUDITFILE-2025).
- **AI policy, training, attestation** (coordination-scheduling): ILTA Q3.18 (ILTA-TECHSURVEY-2026).
- **Tool validation before deployment** (data-reporting): attorney-led testing (EDISCOVERYTODAY-ILTACONTUE-2026).
- **Incident response and client or court disclosure** (client-interaction): CANLAWYER-SC-2026.

### Common pain points

- Verification cost: 67% of Morae respondents fear it outweighs benefits; 48% must materially fix outputs (MORAE-ILR-2026).
- Confident wrong answers: errors arrive in the same assured tone as correct ones (TRI-NEED2KNOW-2026).
- At ILTACON 2026 (5,782 onsite attendees), the eDiscovery Today moderator of the AI-validation session reported that 'context' was needed when evaluating generative AI results (EDISCOVERYTODAY-ILTACON-2026).
- Policy not followed under time pressure (CANLAWYER-SC-2026; ABA-LPT-SC-2026, which cites ignored policies, time pressure and overreliance).
- Assumed validation by someone else in the chain (ACCOUNTINGTODAY-HALLUC1-2026, Desai).
- Reviewers stressed and out of time to check every reference (ACCOUNTINGTODAY-HALLUC1-2026, Reyes).
- Accuracy information and verification methods are the top barrier for limited AI adopters among lawyers (TRI-STANDOUT-2026).
- Accuracy and reliability are the first reason professionals give for not applying GenAI to their work (TR-AIPS-2026); in the 2025 report 40% of those who said GenAI should not be part of daily work cited it, nearly double any other concern (TRI-HALLUC-2025).

### Metrics and benchmarks (with sources and provenance)

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| 17% to 33% | Hallucination share for Lexis+ AI, Westlaw AI-Assisted Research, Ask Practical Law AI (2024 study) | independent | STANFORD-MAGESH-2024 |
| under 10% to nearly half | Responses with hallucinations across 8 legal RAG systems, 2 corpora | independent | ARXIV-LUX-2026 |
| 61.8% verified / 38.2% flagged / 8.4% severe of 2,073 citations | Filevine checker run on 68 attorney-filed federal matters already flagged by courts | vendor-published | LAWSITES-FILEVINE-2026 |
| 5 of 45 citations accurate; 28 altered; 12 unclear | GPTZero's analysis of KPMG's Oct 2025 report | vendor-published | GPTZERO-KPMG-2026 |
| 141 citations, 30+ issues, 19 hallucinations | GPTZero's analysis of the Deloitte Australia report | vendor-published | GPTZERO-DELOITTE-2025 |
| 31%-83% of firms require human review of GenAI work product (by size band) | Firms' self-described policy, ILTA Q3.18 | independent (survey of firms' self-reports) | ILTA-TECHSURVEY-2026 |
| 71% policy; 30% confident applied; 67% fear verification cost; 48% fix outputs; 73% vs 21% client visibility | 850 senior legal professionals | vendor-published | MORAE-ILR-2026 |
| 565 US court cases, Apr 2023 to mid-Sep 2026, 328 in 2026; 100+ lawyer sanctions since 2025 vs 2 in 2023-24 | Charlotin database (CHARLOTIN-DB-2026) as summarised by Best Lawfirms | secondary | BESTLAWFIRMS-VTAX-2026 |
| More than 1,500 cases; almost 2,000 recorded instances | Other tallies (scope differs: global, includes pro se litigants) | secondary | ARXIV-WILLIAMS-2026; ACCOUNTINGTODAY-HALLUC1-2026 |
| 0.34 SD (10 days) and 0.38 SD (90 days) quality gain; unaided redlining gain 0.32 SD, concentrated in seniors (0.45 SD) | Field experiment, 133 patent lawyers, blinded expert scoring (drafting, adjacent to review) | independent | NBER-AUTOR-2026 |

**Quality evidence absent:** no firm in the sources publishes reviewer catch rates, override rates, parallel-run results or inspection findings for AI-assisted deliverables. Aon reports no substantive claims activity tied to AI use at accounting firms as of April 2026 (ACCOUNTINGTODAY-INSURERS-2026). The Williams analysis says courts repeatedly call for error-rate evidence that does not exist (ARXIV-WILLIAMS-2026).

### Guardrails and regulatory points

- Cal Bar's 2026 guidance: competence means more than catching hallucinations, lawyers keep strategic control, the duty to verify rises with autonomy, no document goes to a court without lawyer review and approval, and AI systems must be reassessed periodically (CALBAR-GENAI-2026).
- ABA Formal Opinion 512 (2024) is the common reference for reviewing AI output before court submission (WHITECASE-VERIFY-2026; BESTLAWFIRMS-VTAX-2026).
- Courts: some issue standing orders requiring certification or disclosure of AI use; White & Case cites a Florida 11th Judicial Circuit administrative order (No. 26-04, January 2026) (WHITECASE-VERIFY-2026). The Rule 11 standard is objective reasonableness, not good faith (TRI-HALLUC-2025).
- Accounting: ISQM 1 treats technology as a firm resource requiring quality objectives; a CIBA author says a PCAOB inspection focus includes generative AI documentation and control (ACCOUNTINGWEEKLY-B4-2026, secondary).
- Accountancy ethics: 61% of respondents in a 2026 ACCA poll named AI use the profession's leading ethical challenge (32% in 2024), and 89% said they apply professional skepticism and ethical judgment when using AI (self-reported by poll respondents) (ACCOUNTINGTODAY-ACCA-2026).
- Insurers ask whether firms use AI, police it and have protocols; they expect to formalise questions (ACCOUNTINGTODAY-INSURERS-2026).

### Frontier signals (dated and sourced)

1. **2026-10-19** Harvey says over the coming months it will launch precedent flags and cite checking for US case law (HARVEY-GRAPH-2026).
2. **2026-10-15** Harvey announces Legal Work Orchestration with review gates, and expects agents to take another 20% of workflow steps in six months (HARVEY-ORCH-2026).
3. **2026-10-15** TRI webinar 'Trust by Verify' held; webinar on 'human in control' with a framework of AI Literacy, AI Fluency and Professional Discernment scheduled (page shows 18 Nov 2026; the events list shows 11 Nov) (TRI-TRUSTBYVERIFY-2026; TRI-BEYONDHITL-2026).
4. **2026-09-02** Filevine launches an AI citator and brief checker; Accounting Today runs a two-part piece on hallucination control (LAWSITES-FILEVINE-2026; ACCOUNTINGTODAY-HALLUC1-2026).
5. **2026-08-25** ILTACON session 'Trust but Verify: Validating AI Workflows in eDiscovery' (EDISCOVERYTODAY-ILTACONTUE-2026).
6. **2026-05-19 to 2026-07-30** GPTZero investigations of EY, KPMG and PwC Middle East lead to withdrawals and corrections (GPTZERO-PWC-2026; TECHCRUNCH-KPMG-2026; ACS-EY-2026).
7. **2026-07-30** A researcher argues the legal system substitutes process for evidence and sets a research agenda for shared error metrics and benchmarks (ARXIV-WILLIAMS-2026).
8. **2026-04-18** Sullivan & Cromwell apologises to a bankruptcy court (CANLAWYER-SC-2026).
9. **2026 (PDF created May 2026; adoption date not shown)** Cal Bar extends guidance to agentic AI (CALBAR-GENAI-2026).
10. **2025-12-16** Clearbrief launches an audit-trail report for partners (LAWSITES-CLEARBRIEF-2025).

### Workforce and role effects

- Mid- and senior reviewers carry the load: the NBER trial shows the unaided-judgment gain concentrated in senior lawyers while juniors' outcomes split (NBER-AUTOR-2026).
- 71% of professionals believe early-career roles need structured support from experienced peers; 48% worry about AI's effect on independent judgment development (TR-FOP-2026, denominators: professionals surveyed, 1,816).
- An AICPA leader says the profession must move from doing to supervising, and supervising a bot means understanding the procedure (JOA-LEARN-2026).
- TRI-sourced speakers say review must be done with subject-matter expertise, and that training should include reviewing AI-assisted work alongside experienced practitioners (TRI-NEED2KNOW-2026; TR-FOP-2026).
- Practitioners quoted by Accounting Today question whether reviewers are independent of the report's author and qualified to judge the work (ACCOUNTINGTODAY-HALLUC2-2026).

### Objections and concerns practitioners raise

- "In the loop" can be theater; ask who is in the loop, where and with what skill (ACCOUNTINGTODAY-HALLUC2-2026).
- Verification costs may erase savings; nobody can show net benefit (BESTLAWFIRMS-VTAX-2026; MORAE-ILR-2026).
- Self-checking by AI gives no guarantee (TRI-NEED2KNOW-2026).
- Manual review cannot catch everything, and anonymous community commenters doubt that review processes at consultancies work as described (HN-KPMG-2026).
- Firms' own statements after incidents give little detail on how errors passed review (REGISTER-KPMG-2026; EWEEK-PWC-2026).
- Detection tools are commercial and use broad definitions; GPTZero acknowledges its false-positive rate is higher (GPTZERO-KPMG-2026).
- Clients send contradictory instructions (TRI-LEGALWEEK-2026).
- Unsanctioned use: 34% of professionals use unapproved AI tools (TR-FOP-2026).
- Errors can pass into judicial decisions: a Reminger podcast episode traces the problem from Mata v. Avianca to Shahid v. Esaam, where an appellate court found a trial court had unknowingly used faulty AI-generated citations (REMINGER-HALLUC-2026, episode description).

### Interview probes for an advisor

1. Walk me through the last deliverable that went out with AI-assisted content. Who checked what, against which source, and where is that recorded?
2. What does your reviewer checklist ask differently when AI contributed, and how would you know a reviewer back-traced a claim versus rubber-stamped it? Which number do you track (catches per review, corrections after release)?
3. Which three deliverables are 'top tier', where one fabricated fact costs a client? Who decides, and which get a second reader?
4. When a client, opposing counsel or an outsider finds an error, what is the playbook for disclosure, re-review of the whole engagement, and fee adjustment, and who owns it?
5. How do you test a new AI tool before it touches client work (known-answer set, scorer, re-test after model updates), and how do you sample its output after launch?

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| Clients refusing to pay for AI-done work, requests for AI line items, Cal Bar billing rules for reviewing AI output | billing-collections | TRI-LEGALWEEK-2026; CALBAR-GENAI-2026 |
| Training junior lawyers and accountants to review and judge AI output; first-year hiring effects; ABA podcast 'Developing Lawyers in the Age of AI' (13 Oct 2026) | talent-learning | TR-FOP-2026; NBER-AUTOR-2026; JOA-LEARN-2026; ABA-LPT feed |
| Tool sprawl, token costs, no firm-wide ROI proof (ILTACON 2026) | firm-finance | TRI-ILTACON-2026; BESTLAWFIRMS-VTAX-2026 |
| Partners not discussing AI with clients; client reconsideration data | client-development | TRI-STANDOUT-2026; TR-FOP-2026 |
| Confidentiality of client data in agentic tools; privilege and discoverability of client AI chats (Heppner v. Warner rulings discussed on ABA podcast, 30 Mar 2026) | acceptance-risk | CALBAR-GENAI-2026; ABA-LPT feed |
| Certinia 'PMO Quality Agent' that scores project health sentiment | delivery-management | CERTINIA-VEDA-2026 |
| Citator and corpus quality, knowledge assets feeding verification | knowledge-management | LAWSITES-FILEVINE-2026 |
| AI assurance as a service (a CPA Practice Advisor blurb dated 19 Oct 2026 says the AICPA partnered with the Artificial Intelligence Underwriting Company on an assurance certification for AI systems and agents; blurb only, article not opened); PCAOB and FRC audit-quality material; audit engagement-quality-review detail | assurance archetype | CPAPA-AUDITFILE-2025 (related-links blurb) |
| Hallucination management inside courts (judges, clerks) | out of archetype (government and courts) | TRI-COURTS-2026 |

## 5. Sources

Access is `full` unless stated. Types follow the vocabulary.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| ABA-LPT-PAYKIN-2026 | Picking the Right Legal Tech Tools Ahead of ABA TECHSHOW | Law Practice Today podcast (ABA) | podcast | https://rss.buzzsprout.com/2268467.rss | 2026-03-23 |
| ABA-LPT-WILLIAMS-2026 | Avoiding AI Hallucinations in Legal Practice | Law Practice Today podcast (ABA) | podcast | https://lawpracticetoday.buzzsprout.com/2268467/episodes/19275322-avoiding-ai-hallucinations-in-legal-practice | 2026-06-15 |
| ABA-LPT-SC-2026 | AI Hallucinations in Court - The Sullivan & Cromwell Lesson | Law Practice Today podcast (ABA) | podcast | https://rss.buzzsprout.com/2268467.rss | 2026-06-30 |
| ABA-LPT feed (other items) | Developing Lawyers in the Age of AI (2026-10-13); AI and Legal Ethics: Privilege, Discovery, and Risk (2026-03-30); ABA TECHSHOW 2026 Highlights (2026-04-06) | Law Practice Today podcast (ABA) | podcast | https://rss.buzzsprout.com/2268467.rss | 2026-03 to 2026-10 |
| REMINGER-HALLUC-2026 | AI Hallucinations in the Courts: Lessons from Emerging Case Law | The Reminger Report podcast (Reminger law firm) | podcast | https://rss.buzzsprout.com/1745286.rss | 2026-04-08 |
| HN-KPMG-2026 | KPMG pulls report on AI usage due to apparent hallucinations (thread, 154 points) | Hacker News | community | https://news.ycombinator.com/item?id=48527297 | 2026-06-14 |
| CHARLOTIN-DB-2026 | AI Hallucination Cases Database (listing page; counts not read from it) | Damien Charlotin | community | https://www.damiencharlotin.com/hallucinations/ | 2026-10 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| TRI-TRUSTBYVERIFY-2026 | Trust by Verify: Catching Errors in AI Output Before They Reach the Court or Client (webinar page, held 15 Oct 2026; abstract only) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events/trust-by-verify-catching-errors-in-ai-output-before-they-reach-the-court-or-client | 2026-10-15 |
| TRI-BEYONDHITL-2026 | Beyond Human in the Loop: Redefining Accountability in AI-Assisted Legal Work (scheduled; page 18 Nov, events list 11 Nov) | Thomson Reuters Institute | conference | http://thomsonreuters.com/en/institute/events/beyond-human-in-the-loop-redefining-accountability-in-ai-assisted-legal-work | 2026-11 |
| TRI-NEED2KNOW-2026 | What lawyers need to know about AI in 2026 (recap of 17 Sep 2026 webinar) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/what-lawyers-need-to-know-about-ai-2026 | 2026-10-05 |
| TRI-ILTACON-2026 | Ferraris for emails: At ILTACON 2026, the industry starts reading the meter | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter | 2026-09-09 |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 |
| EDISCOVERYTODAY-ILTACONTUE-2026 | Tuesday Happenings at ILTACON 2026 | eDiscovery Today | conference | https://ediscoverytoday.com/2026/08/25/tuesday-happenings-at-iltacon-2026-ediscovery-trends/ | 2026-08-25 |
| STENO-CLOC-2026 | CLOC Global Institute 2026: Stronger By Design, Built By Community | Steno (vendor-authored recap) | conference | https://brief.steno.com/cloc-global-institute-2026-recap | 2026-06-03 |
| CLOC-VERIFICATION-2026 | Kill the Verification Burden (teaser page) | CLOC | professional-body | https://cloc.org/blog/legal-hacks/kill-the-verification-burden/ | 2026-05-13 |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 (PDF creation date; text shows 2026) |
| WHITECASE-VERIFY-2026 | Verify, Guide, Train: Lessons From Emerging Attorney AI-Misuse Caselaw | White & Case | firm | https://www.whitecase.com/sites/default/files/2026-04/verify-guide-train-lessons-from-emerging-attorney-ai-misuse-case-law.pdf | 2026-04-15 |
| CANLAWYER-SC-2026 | Sullivan & Cromwell apologizes to US bankruptcy judge for AI-generated errors in Prince Group case | Canadian Lawyer | press | https://www.canadianlawyermag.com/news/international/sullivan-cromwell-apologizes-to-us-bankruptcy-judge-for-aigenerated-errors-in-prince-group-case/394014 | 2026-04-22 |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (AP) | CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 |
| FORTUNE-DELOITTE-2025 | Deloitte allegedly cited AI-generated research in a million-dollar report for a Canadian provincial government | Fortune | press | https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government | 2025-11-25 |
| GPTZERO-DELOITTE-2025 | The Deloitte Citation Situation | GPTZero | vendor | https://gptzero.me/news/deloitte-australia-citation-check/ | 2025-11-27 |
| GPTZERO-KPMG-2026 | Chasing the Hallucinations: KPMG's AI-Powered Attempt at Redefining Excellence | GPTZero | vendor | https://gptzero.me/news/investigations-kpmg/ | 2026-06-12 |
| GPTZERO-PWC-2026 | Chasing the Hallucinations: PwC report hallucinates product and government customers | GPTZero | vendor | https://gptzero.me/news/investigations-pwc/ | 2026-07-29 |
| ACS-EY-2026 | EY retracts cyber report littered with AI errors | Information Age (ACS) | press | https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html | 2026-05-19 |
| EWEEK-PWC-2026 | GPTZero Flags Suspected AI Content and False Citations in PwC Reports | eWeek | press | https://eweek.com/news/gptzero-flags-suspected-ai-content-and-false-citations-in-pwc-reports/ | 2026-07-30 |
| TECHCRUNCH-KPMG-2026 | KPMG pulls report on AI usage due to apparent hallucinations | TechCrunch | press | https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/ | 2026-06-13 |
| REGISTER-KPMG-2026 | KPMG's AI report turns into a demo of AI hallucinations | The Register | press | https://www.theregister.com/ai-and-ml/2026/06/12/kpmgs-ai-report-turns-into-a-demo-of-ai-hallucinations/5255029 | 2026-06-12 |
| ACCOUNTINGTODAY-HALLUC1-2026 | False info, real problems: Can accountants tame AI hallucinations? | Accounting Today | press | https://www.accountingtoday.com/news/false-info-real-problems-can-accountants-tame-ai-hallucinations | 2026-09-02 |
| ACCOUNTINGTODAY-HALLUC2-2026 | False info, real problems: The human in the AI loop | Accounting Today | press | https://www.accountingtoday.com/news/false-info-real-problems-the-human-in-the-ai-loop | 2026-09-02 |
| ACCOUNTINGTODAY-INSURERS-2026 | Insurers eyeing AI risk at CPA firms | Accounting Today | press | https://www.accountingtoday.com/news/insurers-eyeing-ai-risk-at-cpa-firms | 2026-04-21 |
| ACCOUNTINGTODAY-ACCA-2026 | Majority of accountants agree AI is profession's top ethical challenge | Accounting Today | press | https://www.accountingtoday.com/news/majority-of-accountants-agree-ai-is-professions-top-ethical-challenge | 2026-10-15 |
| ACCOUNTINGWEEKLY-B4-2026 | Big Four AI Hallucinations: What It Means for Your Practice | Accounting Weekly (CIBA) | press | https://www.accountingweekly.com/trending-news/big-four-ai-hallucinations-what-it-means-for-your-practice | 2026-09-09 |
| JOA-LEARN-2026 | How will accountants learn new skills when AI does the work? | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/mar/how-will-accountants-learn-new-skills-when-ai-does-the-work/ | 2026-03-01 |
| CPAPA-AUDITFILE-2025 | AuditFile Launches New QualityLink Solution for CPA Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/12/04/auditfile-launches-new-qualitylink-solution-for-cpa-firms/174297/ | 2025-12-04 |
| BESTLAWFIRMS-VTAX-2026 | The Verification Tax: Why AI Might Cost Law Firms More Than It Saves | Best Lawfirms | press | https://www.bestlawfirms.com/articles/ai-verification-tax-tokenization-law-firm-costs/8490 | 2026-09-23 |
| MORAE-ILR-2026 | The Intelligence Gap: Why AI in Legal Isn't Delivering and What Needs to Change | Morae | survey | https://www.morae.com/insights/the-intelligence-gap-why-ai-in-legal-isnt-delivering-and-what-needs-to-change/ | 2026-07-08 |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 |
| TR-AIPS-2026 | 2026 AI in Professional Services Report | Thomson Reuters Institute | survey | https://tax.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf | 2026-01 (PDF creation date) |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 (fieldwork Mar-Apr 2026; page date not shown) |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 |
| TRI-HALLUC-2025 | GenAI hallucinations are still pervasive in legal filings, but better lawyering is the cure | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/technology/genai-hallucinations/ | 2025-08-18 |
| TR-CANTSIGN-2026 | If You Can't Verify It, You Can't Sign It | Thomson Reuters Innovation Blog | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/if-you-cant-verify-it-you-cant-sign-it/ | 2026-05-05 |
| TRI-COURTS-2026 | Responsible AI use for courts: Minimizing and managing hallucinations and ensuring veracity (summary post) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/ai-in-courts/hallucinations-report-2026/ | 2026-01-28 |
| LAWSITES-FILEVINE-2026 | Filevine Takes On Shepard's and KeyCite With Its Own AI Case Law Citator and Hallucination Checker | LawSites | press | https://www.lawnext.com/2026/09/filevine-takes-on-shepards-and-keycite-with-its-own-ai-case-law-citator-and-hallucination-checker.html | 2026-09-02 |
| LAWSITES-CLEARBRIEF-2025 | Clearbrief Launches Cite Check Report to Give Law Firm Partners an Audit Trail Against AI Hallucinations | LawSites | press | https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html | 2025-12-16 |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 |
| HARVEY-GRAPH-2026 | Improving Agent Accuracy With Harvey Graph | Harvey | vendor | https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph | 2026-10-19 |
| CERTINIA-VEDA-2026 | Veda AI: System of Action for Professional Services | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 (read date) |
| ARXIV-LUX-2026 | How Much Do Legal RAG Systems Still Hallucinate? (2608.14210) | University of Luxembourg authors | academic | https://arxiv.org/abs/2608.14210 | 2026-08-14 |
| ARXIV-WILLIAMS-2026 | From Process to Evidence: How Computing Can Ground Appropriate Reliance on Legal AI (2607.28869) | J. B. Williams | academic | https://arxiv.org/abs/2607.28869 | 2026-07-30 |
| ARXIV-TARANUKHIN-2026 | Legal LLM Hallucination Should Be Evaluated as Failure of Legal Warrant (2609.17546) | Taranukhin, Shwartz | academic | https://arxiv.org/abs/2609.17546 | 2026-07-15 |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (NBER WP 35720) | Autor et al. | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (2405.20362) | Stanford RegLab/HAI | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 |
| VALS-VLAIR-2025 | Vals Legal AI Report | Vals AI | academic | https://www.vals.ai/vlair | 2025-02 |

**Distinct source refs opened: 54** (the ABA podcast feed row also lists three further episodes). By type: press 18, conference 8, vendor 7, academic 6, survey 5, podcast 4, community 2, professional-body 2, regulator 1, firm 1. Not opened and not relied on: BriefCatch, LawDroid, Lawmatics, Cozen O'Connor (appeared in search summaries only).

## 6. Gaps

- **No firm-published quality measurements** for AI-assisted deliverables: no catch rates, override rates, parallel runs, or inspection findings. Evidence is incidents, vendor evaluations, independent tool-accuracy studies and surveys.
- **Search budget ran out** (shared across agents) before searches on UK practitioner and regulator discourse (SRA, Law Society, Bar Council, Ayinde follow-up) and on in-house outside-counsel AI guidelines. The Law Society pages returned 403; the SRA, Legal Geek, MCA, PMI, and AICPA ENGAGE sessions were not reached.
- **Not accessible:** Reddit (blocked), LinkedIn, Above the Law, Law360, Global Legal Post and Legal Technology (bot challenges), Management Today (paywalled; FRC June 2025 audit-quality warning remains unverified), the S&C letter itself, EDRM (403), Elevate recap (403).
- **Session content** for Legalweek and CLOC quality sessions was only seen through recaps or abstracts; ILTACON 'Trust but Verify' was seen as a listing, not a recap of what was said.
- **Podcasts:** only the ABA Law Practice Today feed and one Reminger episode were read; TRI, LawNext and Accounting Today podcasts were not found by search.
- **Date issues:** Cal Bar guidance shows no adoption date in text (PDF creation date used); TR-FOP-2026 page date not shown; ILTA summary date conflicts (June per filename, August per file metadata); TRI 'human in control' webinar is listed as 11 Nov in one place and 18 Nov on its own page; arXiv 2609.17546 ID and submission date do not match.
- **Counts that disagree:** tracker totals (565 US cases to mid-Sep 2026; more than 650 in Dec 2025; more than 1,500 in Jul 2026; almost 2,000 in Sep 2026) differ in scope and date; the Charlotin database was opened but its totals were not read from it. Press said 40 of 45 KPMG citations were hallucinated, but GPTZero's own breakdown differs. The Deloitte Australia refund (A$98,000 per GPTZero) is not confirmed by the department's statement.
- **Provenance limits:** GPTZero, Filevine, Morae, Harvey and Thomson Reuters figures are vendor-published; GPTZero's detections are third-party, not firm admissions. The Filevine evaluation paper was not seen directly.
- **Consulting and engineering/architecture:** no consulting-firm primary documents on internal review processes (the five incidents come from press and GPTZero). No engineering, architecture or PMI quality-review discourse was reached.
