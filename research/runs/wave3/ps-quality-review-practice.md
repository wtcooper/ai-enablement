# Quality review in professional services: practice angle

Run date 2026-10-19. Archetype `professional-services`, module `quality-review`, angle `practice`. The file holds 19 candidate use cases, module notes, items routed to other modules, a source list and a list of gaps.

## 1. Summary

- **What firms actually do is mostly policy plus citation checking.** ILTA's 2026 technology survey shows formal GenAI policies in 57% of firms under 50 lawyers and 91% to 98% of firms over 350. Policies requiring human review of AI work product range from 31% (smallest firms) to 83% (350-699 lawyers) (ILTA-TECHSURVEY-2026, p.5). The California State Bar's 2026 guidance, the Florida Supreme Court's 2026 rule and the UK Divisional Court's *Ayinde* decision put the duty to verify on the lawyer who signs; California and England also place duties on supervisors and firm leadership.
- **A tool market for verification has formed, with almost no customer evidence.** Clearbrief, Filevine, BriefCatch, LawDroid, Midpage and Harvey each launched or described citation or proposition checking between June 2025 and October 2026 (Harvey's own cite checking is stated as coming). None names a firm customer or publishes a false-negative rate. Filevine's back-test (61.8% of 2,073 citations verified, 8.4% severe) was run on filings already known to be problematic.
- **Only a few named organisations publish measured quality results.** Linklaters ran its own 50-question English-law benchmark (best score 6.4 out of 10 in 2025). A Covington & Burling special counsel published a test-set method for AI document review. Microsoft reports that users kept about seven in ten suggested edits from its Legal Agent. No firm published override rates, reviewer catch rates, parallel-run results or inspection findings for AI-assisted deliverables.
- **The consulting evidence is incident-driven.** Deloitte Australia (October 2025) and Deloitte Canada (November 2025) both delivered government reports with fabricated references that outsiders found. The responses were revision, disclosure of AI use, a refund of the final instalment (Australia) and an accountancy-body investigation (Canada, reported March 2026). No consulting or accounting firm's own description of its review process for AI-assisted deliverables was reachable.
- **Review is being redesigned around gates and evaluation roles.** Harvey's Legal Work Orchestration (2026-10-15) puts named reviewers at gates in an agent workflow. Latham & Watkins' public job description for a Legal Engineering Attorney covers rubric evaluation suites, review-gate placement and change control. Vendors hire lawyers to judge AI output (Legora, Harvey).
- **The apprenticeship question sits inside quality review.** An NBER randomised trial of 133 patent lawyers found AI raised quality, but the skill advantage without AI was concentrated in senior lawyers. Duane Morris and Blank Rome describe onboarding built around verification and apprenticeship.
- **Evidence grades:** 1 A, 9 B, 9 C, 0 D. The A rests on one firm's self-reported benchmark (Linklaters) and its scope is output quality, not review effectiveness.

## 2. Use cases

```yaml
- id: professional-services-quality-review-01
  title: Written firm policy requiring human review and independent verification of AI-assisted work product
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Lawyers and staff use generative AI on client work, and the lawyer who signs a filing or deliverable may not know which parts were machine-generated or who checked them. Courts and regulators place the responsibility on the signer.
  solution: Firms write policies that require human review of AI-assisted work product, restrict use to vetted tools and require outputs to be cited or independently verified against authoritative sources. The California State Bar's 2026 guidance expects supervising lawyers to set such policies, review and approve all AI outputs and filings, and scale oversight to the system's autonomy. One top-10 litigation firm is reported to require three separate sign-offs before any filing, with the briefing associate attesting that every citation and holding was checked (unnamed firm, reported second-hand).
  outcomes:
  - {lever: risk, description: Share of surveyed firms whose policy requires human review of GenAI work product rises with firm size, figure: 31% of firms under 50 lawyers; 59% (50-149); 69% (150-349); 83% (350-699); 79% (over 700), measures: percentage of responding firms in each lawyer-count band that selected 'Work product must be reviewed by a human' as describing their firm's current official policies or guidance on GenAI tools (Q3.18), provenance: independent, source_ref: ILTA-TECHSURVEY-2026}
  - {lever: risk, description: Share of surveyed firms whose policy requires outputs to be cited or independently verified, figure: 25% (under 50 lawyers); 42% (50-149); 40% (150-349); 60% (350-699); 55% (over 700), measures: percentage of responding firms in each lawyer-count band that selected 'Outputs must be cited/independently verified' (Q3.18), provenance: independent, source_ref: ILTA-TECHSURVEY-2026}
  prerequisites:
  - An inventory of approved AI tools and a list of permitted uses
  - A named reviewer for each AI-assisted deliverable or filing
  - Training before access (see professional-services-quality-review-12)
  - A way to record who checked what (see professional-services-quality-review-03)
  risks_and_guardrails:
  - The California guidance says a lawyer remains responsible for all outputs and must not let AI file documents or communicate with a court on the lawyer's behalf (CALBAR-GENAI-2026, p.9).
  - A Florida Supreme Court rule effective 2026-06-15 requires the signer of any filing to represent that cited authorities exist and are accurately cited, with sanctions available (LAWSITES-FLRULE-2026).
  - The UK Divisional Court said heads of chambers and managing partners must take practical and effective measures, and that in hearings of this kind the profession can expect the court to inquire whether they have (AYINDE-EWHC-2025, para 9).
  - ILTA reports that work-product governance still leans on training and leadership pressure, with tracking and compliance tools in use at fewer than one in five firms (ILTA-TECHSURVEY-2026, p.9).
  - A written policy did not prevent a Gordon Rees attorney from denying AI use to a court; the firm later said it had updated its AI policies (GIGALAW-GORDONREES-2025; BESPACIFIC-GORDONREES-2025).
  human_checkpoints:
  - Briefing associate attests that each citation and holding was checked
  - Supervising lawyer reviews and approves AI-assisted output
  - Signing lawyer confirms authorities exist and are accurately cited before filing
  role_evolution: Supervising and managing lawyers carry an explicit duty to set AI policy, train staff and keep controls current (CALBAR-GENAI-2026, p.7). Signing partners can no longer rely on trust that an associate checked the citations.
  evidence_grade: B
  sources:
  - {ref: ILTA-TECHSURVEY-2026, title: The ILTA Technology Survey 2026 Executive Summary, publisher: International Legal Technology Association (ILTA), type: survey, url: 'https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf', date: 2026-06, access: full, locator: p.5 Q3.18 policy table (size bands); p.9 governance paragraph; sample size not stated in the executive summary text (the landscape reports 508 firms)}
  - {ref: CALBAR-GENAI-2026, title: 'Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version)', publisher: 'State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC)', type: regulator, url: 'https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf', date: 2026-05, access: full, locator: p.4 competence and review; p.7 duty to supervise; p.9 candor and filings}
  - {ref: LAWSITES-FLRULE-2026, title: Florida Supreme Court Tackles AI Hallucinations with New Rule Applicable to All State Courts, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/05/florida-supreme-court-tackles-ai-hallucinations-with-new-rule.html', date: '2026-05-28', access: full, locator: 'paragraphs 1-5 (rule text, effective 2026-06-15)'}
  - {ref: AYINDE-EWHC-2025, title: 'R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin)', publisher: 'High Court of Justice, King''s Bench Division (Divisional Court)', type: regulator, url: 'https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf', date: '2025-06-06', access: full, locator: paras 7-9}
  - {ref: LAWSITES-FILEVINE-2026, title: Filevine Takes On Shepard's and KeyCite With Its Own AI Case Law Citator and Hallucination Checker, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/09/filevine-takes-on-shepards-and-keycite-with-its-own-ai-case-law-citator-and-hallucination-checker.html', date: '2026-09-02', access: full, locator: section 'Filevine's Answer to This Need' (three sign-offs anecdote)}
  - {ref: GIGALAW-GORDONREES-2025, title: 'Law Firm Admits Attorney Used AI, Created Fake Citations, Lied to Court (summarising Bloomberg Law)', publisher: GigaLaw, type: press, url: 'https://giga.law/daily-news/2025/10/27/law-firm-admits-attorney-used-ai-created-fake-citations-lied-to-court', date: '2025-10-27', access: full, locator: paragraph 1}
  - {ref: BESPACIFIC-GORDONREES-2025, title: Large US law firm apologizes for AI errors in bankruptcy court filing (excerpting Reuters), publisher: beSpacific, type: press, url: 'https://www.bespacific.com/?p=118478', date: 2025-10, access: full, locator: 'Reuters excerpt, final sentences'}
  last_reviewed: '2026-10-19'
  notes: 'Grade B: the ILTA figures measure policy prevalence among anonymous firms, not an outcome at a named firm. The three-sign-off example comes from one unnamed litigator at a convening Filevine held with about 20 large firms and is not evidence of effect. ABA Formal Opinion 512 could not be opened (blocked).'
- id: professional-services-quality-review-02
  title: Automated checking of citations, quotations and cited propositions in a draft before it is signed
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Fabricated cases, altered quotations and real cases that do not support the proposition are hard to spot by eye, and manual cite-checking is the step that failed in sanctioned filings.
  solution: Checkers extract every citation from a draft and compare it with a case-law corpus. Some also test whether the cited opinion supports the stated proposition or quotation. Filevine's brief auditor reports a status per citation (verified, unverified, suspect, ambiguous, mischaracterized or wrong case name). BriefCatch's RealityCheck reads the cited cases and flags altered quotes, misstated holdings and unsupported citations, and scans for concealed text. LawDroid's CiteCheck AI matches citations against CourtListener. Harvey and Midpage describe a citation-review use through a connector announced 2026-10-19, and Harvey says it will launch cite checking for US case law over the coming months.
  outcomes:
  - {lever: quality, description: Vendor back-test of its checker on filings in which courts had already identified hallucinated citations, figure: 61.8% verified; 38.2% flagged for attorney review; 8.4% marked severe, measures: 'share of 2,073 citations, across 68 attorney-filed federal matters (drawn from a database of 1,314 matters in which a judge identified potentially hallucinated citations), that the tool verified, flagged for attorney review, or marked severe (mischaracterized holding, or wrong or non-existent case)', provenance: vendor-published, source_ref: LAWSITES-FILEVINE-2026}
  - {lever: quality, description: Journalist test of a free citation checker on a known hallucinated filing and on his own brief, figure: 'Flagged the invalid citations in the Mata v. Avianca filing; also marked some valid citations invalid (Westlaw-only citations, case-name mismatch)', measures: single hands-on test by the article's author; not quantified, provenance: independent, source_ref: LAWSITES-LAWDROID-2025}
  prerequisites:
  - Case-law corpus that covers the jurisdictions and citation formats in use (Filevine's corpus excludes statutes and regulations at launch)
  - Drafts in a format the tool can ingest (Word or PDF)
  - A lawyer or paralegal assigned to resolve every flag
  risks_and_guardrails:
  - Filevine's own evaluation used filings already known to contain problems, so the flag rates are not an error rate for ordinary work (LAWSITES-FILEVINE-2026).
  - The LawDroid test produced false alarms on Westlaw-only citations (LAWSITES-LAWDROID-2025).
  - BriefCatch tells users to verify manually any case the tool cannot confirm across its three case-law sources (LAWSITES-BRIEFCATCH-2026).
  - Filevine's CEO said none of this removes the need for lawyers to validate their own work (LAWSITES-FILEVINE-2026).
  human_checkpoints:
  - Lawyer reviews each flagged citation in context
  - Signing lawyer decides whether to file
  role_evolution: Citation validation becomes a required step in any workflow that produces a document relying on case law, as Filevine's CEO put it; the cite-check moves from a manual associate task to resolving tool flags.
  evidence_grade: C
  sources:
  - {ref: LAWSITES-FILEVINE-2026, title: Filevine Takes On Shepard's and KeyCite With Its Own AI Case Law Citator and Hallucination Checker, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/09/filevine-takes-on-shepards-and-keycite-with-its-own-ai-case-law-citator-and-hallucination-checker.html', date: '2026-09-02', access: full, locator: 'sections ''Filevine''s Answer to This Need'' and ''Evaluating the Results''; the evaluation paper was unpublished and read by the author, who had not tested the tool himself'}
  - {ref: LAWSITES-LAWDROID-2025, title: 'LawDroid Launches CiteCheck AI, A Fail-Safe Against AI Citation Hallucinations', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2025/06/lawdroid-launches-citecheck-ai-a-fail-safe-against-ai-citation-hallucinations.html', date: '2025-06-27', access: full, locator: section 'Trying It Out'}
  - {ref: LAWSITES-BRIEFCATCH-2026, title: BriefCatch Launches Unified Legal Writing Suite for the AI Era (press release), publisher: 'LawSites (Robert Ambrogi), reproducing a BriefCatch release dated 2026-09-09', type: press, url: 'https://www.lawnext.com/2026/09/briefcatch-launches-unified-legal-writing-suite-for-the-ai-era.html', date: '2026-09-11', access: full, locator: RealityCheck paragraph}
  - {ref: LAWSITES-MIDPAGE-2026, title: Harvey Now Connects to Legal Research Platform Midpage Through An MCP Connector, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/10/harvey-now-connects-to-legal-research-platform-midpage-through-an-mcp-connector.html', date: '2026-10-19', access: full, locator: list of example uses ('Citation review')}
  - {ref: HARVEY-GRAPH-2026, title: Improving Agent Accuracy With Harvey Graph, publisher: Harvey, type: vendor, url: 'https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph', date: '2026-10-19', access: full, locator: 'section ''What''s in Harvey Graph Today'', final paragraph'}
  - {ref: CHARLOTIN-HALLUC-2026, title: AI Hallucination Cases database, publisher: Damien Charlotin (HEC Paris research fellow), type: academic, url: 'https://www.damiencharlotin.com/hallucinations/', date: '2026-10-19', access: full, locator: 'header paragraph (2,202 cases identified at retrieval)'}
  last_reviewed: '2026-10-19'
  notes: 'All named products are vendor launches; no firm customer is named and no false-negative rate is published. Context counts of court-identified hallucination cases: at least 160 (LawDroid article, 2025-06), more than 650 (Clearbrief article, 2025-12), 2,202 (Charlotin database, retrieved 2026-10-19). The three counts use different sources and definitions and are not a clean time series. LawSites also repeats a 2018 Law Library Journal study (Hellyer) on disagreement between citators; that is second-hand and not used as a figure here.'
- id: professional-services-quality-review-03
  title: Documented verification record attached to the file so the signing lawyer can show what was checked
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Partners are sanctioned for citation errors they did not personally make, often without knowing AI was used on the team, and have no record showing the checks that were done.
  solution: Clearbrief's Cite Check Report, launched in December 2025, lists every legal and factual citation in a Word document, flags missing sources, formatting errors and low semantic-support scores, records how each issue was resolved and by whom, and produces a PDF for the case file. Clearbrief says it uses non-generative AI for the check so the checker cannot add hallucinations.
  outcomes:
  - {lever: risk, description: Audit trail of citation verification for the signing attorney, figure: none published, measures: 'n/a: no usage or effectiveness figure published', provenance: vendor-published, source_ref: LAWSITES-CLEARBRIEF-2025}
  prerequisites:
  - Drafting in Microsoft Word
  - Citation sources reachable by the tool (Westlaw-only citations may need manual PDF upload)
  - A habit of having an associate or paralegal run the check before partner sign-off
  risks_and_guardrails:
  - The record shows a check was run; it does not show the check was right. Clearbrief says AI citation errors can be subtle and hard to see by eye (LAWSITES-CLEARBRIEF-2025).
  - Cal Bar requires the lawyer, not the tool, to verify and correct errors before submitting to a court (CALBAR-GENAI-2026, p.9).
  human_checkpoints:
  - Reviewer adds notes explaining flags that were ignored
  - Partner reviews the report before signing
  role_evolution: Partners who relied on trust in associates' cite-checks get a reviewable record; associates and paralegals run and annotate the report.
  evidence_grade: C
  sources:
  - {ref: LAWSITES-CLEARBRIEF-2025, title: Clearbrief Launches Cite Check Report to Give Law Firm Partners an Audit Trail Against AI Hallucinations, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html', date: '2025-12-16', access: full, locator: sections 'How the Cite Check Report Works' and 'Providing Verifiable Proof'}
  - {ref: CALBAR-GENAI-2026, title: 'Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version)', publisher: 'State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC)', type: regulator, url: 'https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf', date: 2026-05, access: full, locator: p.9 candor and filings}
  last_reviewed: '2026-10-19'
  notes: No named law-firm customer, usage figure or false-negative rate found. The article states more than 650 documented hallucination cases as context.
- id: professional-services-quality-review-04
  title: Benchmarking AI tools against gold-standard answers or a lawyer baseline before deciding how much review they need
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Vendors claim their legal AI is accurate or hallucination-free, and firms need evidence to set review depth and choose tools.
  solution: 'Linklaters built an in-house benchmark of 50 hard English-law questions across 10 practice areas, had senior lawyers mark the answers (5 marks substance, 3 citations, 2 clarity) and re-ran it in 2025 on newer models. It concluded the models still need expert supervision but could help as a first draft or cross-check. Outside the firms, Vals AI ran two vendor-opt-in studies with law-firm-built datasets and a lawyer baseline, and Stanford researchers ran a preregistered test of commercial legal research tools. (Pattern is ''other'': a recurring evaluation exercise, not a production workflow.)'
  outcomes:
  - {lever: quality, description: Linklaters re-test of newer general models on its English-law benchmark, figure: OpenAI o1 scored 6.4 out of 10 and Gemini 2.0 scored 6.0; the best model in the October 2023 round (Bard) scored 4.4, measures: overall mark out of 10 awarded by senior lawyers to model answers on 50 English-law questions across 10 practice areas (aggregation method not stated on the page read), provenance: self-reported, source_ref: LINKLATERS-LINKSAI-2025}
  - {lever: quality, description: Independent legal research study with a lawyer baseline, figure: AI products scored 74%-78% weighted; lawyer baseline 69%; legal AI accuracy 78%-81% against 80% for the generalist tool, measures: 'weighted score (accuracy 50%, authoritativeness 40%, appropriateness 10%) over 200 US legal research questions, four products plus a lawyer control group', provenance: independent, source_ref: VALS-VLAIR-LR-2025}
  - {lever: quality, description: Earlier Vals study across seven tasks, figure: Lawyer baseline ahead of the AI tools on redlining and on EDGAR research; at least one AI tool ahead on four other tasks; Harvey Assistant 94.8% on document Q&A against a 70.1% lawyer baseline, measures: 'accuracy or performance score on predefined criteria per task, four vendor products that opted in per task, lawyer baseline from a control group', provenance: independent, source_ref: VALS-VLAIR-2025}
  - {lever: risk, description: Preregistered test of retrieval-based legal research tools, figure: 'Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI each hallucinated between 17% and 33% of the time', measures: share of tool responses classed as hallucinated in the preregistered query set (denominator not given in the abstract), provenance: independent, source_ref: STANFORD-MAGESH-2024}
  prerequisites:
  - Senior lawyers' time to write questions, reference answers and marking criteria
  - A rubric that scores citations as well as substance
  - A plan to repeat the test when models change
  risks_and_guardrails:
  - Benchmarks measure the tool's answers, not how well reviewers catch errors; no firm published reviewer catch rates.
  - Vals notes that its results are a snapshot, vendors opted in per task and Vals has customer relationships with some participants (VALS-VLAIR-2025).
  - Linklaters recommends against using the tested models for English-law advice without expert supervision (LINKLATERS-LINKSAI-2025).
  human_checkpoints:
  - Senior lawyers mark benchmark answers
  - Firm decides permitted uses and review depth from the results
  role_evolution: Senior lawyers act as markers and question-setters for evaluations; innovation and knowledge teams own the benchmark.
  evidence_grade: A
  sources:
  - {ref: LINKLATERS-LINKSAI-2025, title: UK - The LinksAI English law benchmark (Version 2), publisher: Linklaters, type: firm, url: 'https://linklaters.com/insights/blogs/digilinks/2025/february/uk-the-linksai-english-law-benchmark-version-2', date: '2025-02-10', access: full, locator: sections 'The benchmark' and 'The updated results'}
  - {ref: VALS-VLAIR-LR-2025, title: VLAIR - Legal Research, publisher: Vals AI, type: vendor, url: 'https://www.vals.ai/industry-reports/vlair-10-14-25', date: '2025-10-14', access: full, locator: executive summary and key findings 1-2}
  - {ref: VALS-VLAIR-2025, title: 'Vals Legal AI Report (VLAIR), first report', publisher: Vals AI, type: vendor, url: 'https://www.vals.ai/vlair', date: '2025-02-27', access: full, locator: executive summary and results table}
  - {ref: STANFORD-MAGESH-2024, title: 'Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)', publisher: 'Stanford RegLab / HAI (Magesh, Surani, Dahl, Suzgun, Manning, Ho)', type: academic, url: 'https://arxiv.org/abs/2405.20362', date: '2024-05-30', access: full, locator: abstract (v. updated 2024-05-30)}
  last_reviewed: '2026-10-19'
  notes: Grade A rests on Linklaters, a named firm reporting its own measured benchmark scores. The figures measure model answer quality, not review effectiveness, and the Linklaters round is 20 months old. Vals studies are legal-research or task benchmarks (adjacent evidence) and Vals names vendors; consortium firms in the first study included Reed Smith, Fisher Phillips, McDermott Will & Emery and Ogletree Deakins. The Stanford abstract was read; the full paper was not.
- id: professional-services-quality-review-05
  title: In-firm evaluation suites, gold-standard work product and change control run by legal engineers
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A firm that deploys AI workflows needs to know whether each prompt, retrieval or model change makes the work better or worse, and who owns fixing errors.
  solution: 'Latham & Watkins'' job description for a Legal Engineering Attorney on its AI & Legal Innovation team has the role design rubric-based evaluation suites from real precedents and playbooks, measure performance before and after every change, run structured error analysis across prompt, retrieval, schema, model and data layers, place review gates and exceptions in redesigned workflows, and keep change control, lineage and audit trails. Vendors hire the same skill: Legora''s ''Technical Legal Engineer - Evals'' role has a lawyer review AI output as an experienced lawyer reviews junior work and build gold-standard datasets; Harvey advertises a role to own the quality bar of its human evaluations, saying evaluation volume is growing 10x.'
  outcomes:
  - {lever: quality, description: Evaluation and change-control duties written into a firm role, figure: none published, measures: 'n/a: job description only, no results published', provenance: self-reported, source_ref: LATHAM-JD-2026}
  prerequisites:
  - Exemplar matters and playbooks to turn into gold-standard reference packs
  - Partnership with AI governance, information governance and privacy teams
  - Senior practitioners willing to codify tacit knowledge
  risks_and_guardrails:
  - A job description shows intent and staffing, not results; no evaluation outcome from Latham is public.
  - Evaluations built from the firm's own precedents may not catch errors outside those precedents.
  human_checkpoints:
  - Legal engineers and practice-group lawyers validate solutions against real matters
  - Partners and knowledge lawyers define the quality criteria
  role_evolution: 'New titles appear: Legal Engineering Attorney, Legal Knowledge Engineer, Legal Workflow Engineer (Latham) and lawyer-evaluators on vendor teams, where the lawyer''s job is judging AI output at scale rather than billable work (LEGORA-JOB-EVALS-2026).'
  evidence_grade: B
  sources:
  - {ref: LATHAM-JD-2026, title: 'Legal Engineering Attorney (job description, Technology & Information Services / Legal Innovation)', publisher: Latham & Watkins, type: job-posting, url: 'https://www.lw.com/admin/upload/SiteAttachments/Legal-Engineering-Attorney.pdf', date: '2026-05-13', access: full, locator: 'Role overview and Essential Duties items 2, 8, 9 and 12; last updated 2026-05-13'}
  - {ref: LEGORA-JOB-EVALS-2026, title: Technical Legal Engineer - Evals (job posting), publisher: Legora, type: job-posting, url: 'https://jobs.ashbyhq.com/legora/518304b2-0711-4779-9636-fe54b1272246', date: '2026-08-19', access: full, locator: '''The Role'' and ''What you will be doing'''}
  - {ref: HARVEY-JOB-EVALQ-2026, title: 'Senior Product Operations Manager, Evaluation Quality (job posting)', publisher: Harvey, type: job-posting, url: 'https://jobs.ashbyhq.com/harvey/f0e4e24a-2a7a-4fc4-8872-9a8a762fecf5', date: '2026-08-04', access: full, locator: '''Role overview'''}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": a standing evaluation-and-change-control practice around AI workflows. Latham is the only firm found with a public description of this role. The Legora and Harvey postings are vendor-side and show how the vendors'' own quality work is staffed, not how customer firms review output. A second posting, ''Legal Knowledge Engineer - Litigation'' on an iCIMS site whose address suggests Latham, returned an error when fetched and is not used.'
- id: professional-services-quality-review-06
  title: Test-set validation of AI document-review prompts before relying on them (in-matter quality control)
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: GenAI document review can be wrong in ways that depend on the issue, and formal statistical validation can be too slow for a matter that needs to find key evidence quickly.
  solution: A Covington & Burling special counsel published a case study of a real matter using Relativity aiR for Review on 7,100 documents and nine sub-issues. A senior attorney tagged 10-15 example documents per issue; the set was split into Test Set 1 (to refine prompts) and Test Set 2 (to check for overfitting), and a small random sample formed Test Set 3 for a basic read on the wider set. Prompts went through four rounds, results were tracked as raw counts of true and false positives, and issues where AI did poorly (date- or rule-dependent ones) were supplemented with metadata and keyword searches.
  outcomes:
  - {lever: quality, description: Prompt refinement with measured improvement on curated examples, figure: Two issues (4 and 9) reached perfect performance on Test Set 1 by round four; issue 8 kept a higher false-positive rate, measures: 'counts of true positives and false positives against senior-attorney tags per issue, four prompt rounds, 7,100 documents, nine sub-issues (chart values not read)', provenance: self-reported, source_ref: EDRM-EMORY-2025}
  prerequisites:
  - Senior attorneys able to tag ground-truth examples
  - A review platform that shows per-document predictions and scores
  - A different person for control-set review and prompt writing, where possible, to limit overfitting (EDT-FOLLOWUP-2025)
  risks_and_guardrails:
  - The author says this was not a defensibility-grade validation of recall; her team skipped a random control set to save reviewer time (EDT-FOLLOWUP-2025).
  - A federal e-discovery practitioner worried that without TAR-style statistics a production may be challenged as unverifiable (EDT-CASEPOINT-2026).
  - In the EDRM working-group survey, 14 of 19 respondents had used GenAI for document review and described results as mixed (EDT-EDRMSURVEY-2026).
  human_checkpoints:
  - Senior attorney tags examples and gives feedback on misclassified documents
  - Team decides when prompt iteration shows diminishing returns
  role_evolution: Senior attorneys' time moves upstream into building test sets and prompts; their expertise is scaled across the document set (EDRM-EMORY-2025).
  evidence_grade: B
  sources:
  - {ref: EDRM-EMORY-2025, title: 'Case Study: Practical Testing for Effectively Organizing Documents with GenAI Review (Tara S. Emory, Covington & Burling)', publisher: EDRM, type: professional-body, url: 'https://edrm.net/2025/06/case-study-practical-testing-for-effectively-organizing-documents-with-genai-review/', date: '2025-06-24', access: full, locator: sections B (Curating Strategic Test Sets) and C (Prompt Iteration and Testing); read through a text mirror}
  - {ref: EDT-FOLLOWUP-2025, title: 'Follow-Up to the GenAI Review Case Study: eDiscovery Trends', publisher: eDiscovery Today (Doug Austin), type: press, url: 'https://ediscoverytoday.com/2025/07/07/follow-up-to-the-genai-review-case-study-ediscovery-trends/', date: '2025-07-07', access: full, locator: author's reply on the control set and test sets}
  - {ref: EDT-EDRMSURVEY-2026, title: 'The EDRM GenAI Survey Results: AI and eDiscovery Trends', publisher: eDiscovery Today (Doug Austin), type: press, url: 'https://ediscoverytoday.com/2026/04/01/the-edrm-genai-survey-results-ai-and-ediscovery-trends/', date: '2026-04-01', access: full, locator: sections 'Primary Use Cases' and 'Transparency and Disclosure'}
  - {ref: EDT-CASEPOINT-2026, title: 'From AI Hype to AI Accountability: A New Report from Casepoint', publisher: eDiscovery Today (Doug Austin), type: press, url: 'https://ediscoverytoday.com/2026/07/23/from-ai-hype-to-ai-accountability-a-new-report-from-casepoint-artificial-intelligence-trends/', date: '2026-07-23', access: full, locator: '''Practitioners Are Skittish About Defensibility'''}
  - {ref: EDT-ILTACON-2026, title: My Five ILTACON 2026 Takeaways, publisher: eDiscovery Today (Doug Austin), type: conference, url: 'https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/', date: '2026-09-04', access: full, locator: takeaway paragraph mentioning the AI validation session}
  last_reviewed: '2026-10-19'
  notes: 'Grade B with an adjacent-process cap: this is validation of document organisation in e-discovery, a legal-practice extension rather than review of professional deliverables. Chart values were not read, so no percentages are given. ILTACON 2026 had an AI validation session moderated by the eDiscovery Today author (EDT-ILTACON-2026); a separate preview listing ''Trust but Verify: Validating AI Workflows in eDiscovery'' comes from the landscape file only (not opened).'
- id: professional-services-quality-review-07
  title: Review gates and named reviewers built into AI-orchestrated matter workflows
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Lawyers who delegate steps to agents still reassemble context, move output between people and track who must review what.
  solution: Harvey's Legal Work Orchestration, launched 2026-10-15, captures a recurring matter as a template of phases, tasks, playbooks, agents, collaborators and review gates. Each task carries its scope, inputs and reviewer. In Harvey's example an agent builds a change-of-control consent matrix, Harvey notifies the designated partner, and the next step begins once the partner approves. Latham's legal-engineering role is likewise responsible for placing review gates and handling exceptions when it redesigns workflows for AI-first execution.
  outcomes:
  - {lever: capacity, description: Harvey's stated expectation for agent share of workflow steps, figure: 'none published (forecast: Harvey says it expects agents to take on an additional 20% of workflow steps over six months, and that this share will triple within a year)', measures: share of workflow steps executed by agents rather than prompted by lawyers; baseline not stated, provenance: vendor-published, source_ref: HARVEY-ORCH-2026}
  prerequisites:
  - A repeatable matter type that can be written as a template
  - Innovation or knowledge team to define phases, tasks and reviewers
  - Playbooks and precedent agents can use
  risks_and_guardrails:
  - Harvey says work performed by agents will remain transparent and auditable and lawyers stay in control through defined review gates (HARVEY-ORCH-2026); no review-quality data are given.
  - Cal Bar says the greater the autonomy, the greater the supervision and verification the lawyer must implement (CALBAR-GENAI-2026, p.2 and p.4).
  human_checkpoints:
  - Designated partner approves each reviewed task before the next step
  - Lawyers review consequential outputs and exercise judgment (HARVEY-ORCH-2026)
  role_evolution: Partners see matter status without asking associates to reconstruct it; lawyers shift from prompting every step to directing the matter and reviewing at gates; innovation teams define the templates.
  evidence_grade: C
  sources:
  - {ref: HARVEY-ORCH-2026, title: Making Harvey the Orchestration Layer for Legal Work, publisher: Harvey, type: vendor, url: 'https://www.harvey.ai/blog/legal-work-orchestration', date: '2026-10-15', access: full, locator: sections 'How Legal Orchestration Works' and 'The Future of Legal Work Orchestration'}
  - {ref: LATHAM-JD-2026, title: 'Legal Engineering Attorney (job description, Technology & Information Services / Legal Innovation)', publisher: Latham & Watkins, type: job-posting, url: 'https://www.lw.com/admin/upload/SiteAttachments/Legal-Engineering-Attorney.pdf', date: '2026-05-13', access: full, locator: Essential Duties item 2}
  - {ref: CALBAR-GENAI-2026, title: 'Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version)', publisher: 'State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC)', type: regulator, url: 'https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf', date: 2026-05, access: full, locator: p.2 agentic AI; p.4 supervision}
  last_reviewed: '2026-10-19'
  notes: Rolling out across Harvey workspaces at the time of the post; templates are in early access. No customer is named. The 20% and tripling statements are vendor expectations, not measured results.
- id: professional-services-quality-review-08
  title: Large structured pilot on real matters, with the firm as design partner, before firmwide rollout of an AI platform
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Firms cannot judge AI quality on demos; they need evidence from their own practice areas before licensing a platform to thousands of lawyers.
  solution: Hogan Lovells Cadwalader ran a pilot in which more than 1,300 lawyers in 18 practice teams used Legora on real matters (capital markets, banking and finance, M&A, disputes, real estate, tax and regulatory) across several offices, then agreed a global rollout and a design-partner role for Legora's research and regulatory monitoring tools. Its CEO said the platform supports quality service while maintaining professional judgment.
  outcomes:
  - {lever: risk, description: Scale of pre-rollout trial on live work, figure: 'more than 1,300 lawyers across 18 practice teams', measures: 'number of lawyers and practice teams in the pilot, as stated in the vendor''s announcement; no accuracy or error data published', provenance: vendor-published, source_ref: LEGORA-HLC-2026}
  prerequisites:
  - Practice-group sponsors across several offices
  - Willingness to act as design partner and feed back errors
  - A decision rule for moving from pilot to rollout
  risks_and_guardrails:
  - No pilot quality results were published; the announcement does not say how errors were measured.
  - TRI reports firms attending Legalweek 2026 still answered client questions on AI savings with 'still gathering the data' (TRI-LEGALWEEK-2026).
  human_checkpoints:
  - Lawyers on real matters judge outputs during the pilot
  - Firm leadership decides on rollout
  role_evolution: Practice teams become design partners, with lawyers shaping vendor roadmaps from their own error experience.
  evidence_grade: B
  sources:
  - {ref: LEGORA-HLC-2026, title: Hogan Lovells Cadwalader rolls out Legora globally, publisher: Legora, type: vendor, url: 'https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally', date: '2026-10-16', access: full, locator: opening paragraphs (pilot description and CEO quote)}
  - {ref: TRI-LEGALWEEK-2026, title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide', publisher: Thomson Reuters Institute, type: conference, url: 'https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide', date: '2026-03-13', access: full, locator: section 'Proving AI's path to saving clients money'}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": a staged pilot-to-rollout evaluation. Source is the vendor''s announcement; the firm''s own statement was not found. Named for pilot structure only, not for measured quality.'
- id: professional-services-quality-review-09
  title: Tracking acceptance and override of AI suggestions as a live quality signal
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Firms and departments rarely know how often reviewers accept or reject AI output, so they cannot tell whether review is catching errors or rubber-stamping.
  solution: Microsoft's legal department (an in-house team) is an early user of its Legal Agent for contract review and redlining, where redlines appear as native Word tracked changes. Microsoft reported usage and acceptance data from the tool's first six months in an early-access programme, plus internal evaluations of the edits. TRI recommends that organisations track patterns of professionals overriding AI outputs, because they show whether the system needs retraining or users need guidance. [in-house]
  outcomes:
  - {lever: quality, description: Share of suggested edits kept by users, figure: 'roughly seven in ten suggestions kept; about 100,000 edits generated by more than 1,800 users since April', measures: 'suggested edits that users kept, among edits generated in the Frontier early-access programme (denominator and period as described by Microsoft)', provenance: vendor-published, source_ref: LAWSITES-MSFT-2026}
  - {lever: quality, description: Microsoft's internal evaluation of the edits, figure: over 90% fluency; over 95% conciseness; over 85% relevance, measures: internal Microsoft evaluations of edits on three criteria; no independent legal benchmark released, provenance: vendor-published, source_ref: LAWSITES-MSFT-2026}
  prerequisites:
  - Logging of suggestions and user actions in the editing tool
  - A defined review of override patterns by practice area
  - Agreement on what counts as an accepted edit
  risks_and_guardrails:
  - 'Acceptance is not accuracy: a reviewer can keep a wrong edit. Microsoft released no independent legal benchmark (LAWSITES-MSFT-2026).'
  - TRI says override procedures must be tracked but not burdensome (TRI-ACCOUNT-2026).
  - ILTA found tracking and compliance tools in use at fewer than one in five firms (ILTA-TECHSURVEY-2026, p.9).
  human_checkpoints:
  - Legal reviewer accepts or rejects each tracked change
  - Department reviews override patterns by area
  role_evolution: In-house counsel's first pass moves to reviewing tracked changes; Microsoft's senior counsel says a review that could take an hour can often take several minutes (self-reported quote).
  evidence_grade: B
  sources:
  - {ref: LAWSITES-MSFT-2026, title: 'Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html', date: '2026-10-15', access: full, locator: sections 'What Microsoft Announced' and 'Who Is Using It'}
  - {ref: TRI-ACCOUNT-2026, title: 'Between accountability and chaos: Setting the AI standards that professionals demand', publisher: Thomson Reuters Institute, type: press, url: 'https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos', date: '2026-10-12', access: full, locator: section 'What standards should actually look like' (judgment validation standard)}
  - {ref: ILTA-TECHSURVEY-2026, title: The ILTA Technology Survey 2026 Executive Summary, publisher: International Legal Technology Association (ILTA), type: survey, url: 'https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf', date: 2026-06, access: full, locator: p.9 governance paragraph}
  last_reviewed: '2026-10-19'
  notes: 'Grade B with an adjacent-process cap: figures come from contract redlining, not review of finished deliverables. The TRI item is a recommendation, not a deployment. Clyde & Co is also named in the Microsoft announcement (adoption approaching 90%) but with no quality data.'
- id: professional-services-quality-review-10
  title: 'Post-incident remediation of consulting deliverables: re-verify every citation, correct the report and disclose AI use'
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - client-interaction
  pattern: reconcile-exceptions
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Consulting reports for governments were found to contain fabricated references, and in both cases the errors were found by outsiders after delivery.
  solution: After a university researcher flagged errors in a Deloitte Australia report for the Department of Employment and Workplace Relations, Deloitte published a revised version that removed a fabricated court quote and non-existent references, added a disclosure that Azure OpenAI was used, and agreed to repay the final instalment of the AU$440,000 contract. In Newfoundland and Labrador, after The Independent found non-existent journal papers cited in a 526-page Deloitte health workforce plan, Deloitte said it would revise citations and, per the province, committed to a full review of all citations and to report back. The Independent reported in March 2026 that an accountancy regulator, CPA Newfoundland and Labrador, had decided to investigate Deloitte after a resident's complaint.
  outcomes:
  - {lever: risk, description: Financial and reputational consequence of unverified AI-assisted references in a government report, figure: 'partial refund of a AU$440,000 contract (amount not disclosed in the report; department said the final instalment would be repaid)', measures: 'contract value and the instalment Deloitte agreed to repay, per the department''s statement', provenance: independent, source_ref: CTV-DELOITTE-2025}
  - {lever: risk, description: Scale of citation errors found in the Canadian report, figure: 'at least four citations to non-existent research papers in a 526-page plan; contract fee $1,598,485 (currency as reported)', measures: count of false citations found by The Independent per Canadian HR Reporter; fee from access-to-information records, provenance: independent, source_ref: HRREPORTER-DELOITTE-NL-2025}
  prerequisites:
  - Source-by-source citation check before delivery
  - A client-facing disclosure policy for AI use
  - Engagement-level accountability for what AI tools were used and by whom
  risks_and_guardrails:
  - Deloitte told AP the matter was resolved with the client and did not say whether AI caused the errors; the revised report disclosed Azure OpenAI use (CTV-DELOITTE-2025).
  - Deloitte Canada said AI was used selectively to support a small number of research citations, not to write the report, and that the corrections do not affect findings (CTV-DELOITTE-NL-2025).
  - CPA Newfoundland and Labrador can suspend or restrict a firm's licence, refer to discipline, or counsel the firm after an investigation (INDEPENDENT-CPANL-2026).
  human_checkpoints:
  - Engagement leader confirms every reference exists before release
  - Client reviews the revised report and the firm's citation review
  role_evolution: Engagement partners become accountable for source verification of AI-assisted drafts; clients and professional bodies can now ask for disclosure and review evidence.
  evidence_grade: B
  sources:
  - {ref: CTV-DELOITTE-2025, title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press), publisher: CTV News / Associated Press, type: press, url: 'https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/', date: '2025-10-07', access: full, locator: 'paragraphs 1-6 (refund, revised report, disclosure)'}
  - {ref: CTV-DELOITTE-NL-2025, title: N.L. government pledges strict review on AI use after more false citations found in reports, publisher: CTV News (Canadian Press), type: press, url: 'https://www.ctvnews.ca/canada/newfoundland-and-labrador/article/nl-government-pledges-strict-review-on-ai-use-after-more-false-citations-found-in-reports/', date: '2025-11-29', access: full, locator: opening paragraphs (Deloitte statement)}
  - {ref: HRREPORTER-DELOITTE-NL-2025, title: 'AI errors: Province grapples with Deloitte report marred by false citations', publisher: Canadian HR Reporter, type: press, url: 'https://www.hrreporter.com/focus-areas/automation-ai/ai-errors-province-grapples-with-deloitte-report-marred-by-false-citations/393782', date: '2025-11-25', access: full, locator: paragraphs on false citations and the department's statement}
  - {ref: INDEPENDENT-CPANL-2026, title: Accounting watchdog to investigate Deloitte over fake citations in $1.6M healthcare report, publisher: The Independent (Newfoundland and Labrador), type: press, url: 'https://theindependent.ca/news/lji/accounting-watchdog-to-investigate-deloitte-over-fake-citations-in-1-6-million-healthcare-report/', date: '2026-03-07', access: full, locator: opening paragraphs (investigation decision)}
  last_reviewed: '2026-10-19'
  notes: 'These are incident reports, not planned deployments. Press accounts differ: AP gives a 237-page Australian report; the Canadian report is 523 pages (CTV) or 526 pages (HR Reporter), and The Independent''s count is three examples in CTV and at least four in HR Reporter. A search summary also reported a new provincial contracting rule on AI disclosure and audit rights, but the pages opened here did not confirm it, so it is not used. Deloitte''s primary statements were not opened.'
- id: professional-services-quality-review-11
  title: Verification-first onboarding and supervised review for junior lawyers
  archetype: professional-services
  module: quality-review
  function: people-hr
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI absorbs the routine drafting that taught juniors judgment, while juniors are also the people most likely to produce the first draft with AI and the ones whose review skills the firm relies on.
  solution: 'Duane Morris rebuilt first-year onboarding: a two-day orientation with a live AI-and-library research session, twice-monthly extended sessions from September to June, practice-group AI champions who test tools on real work, and a separate mentorship track. The firm''s one fixed principle is that an AI-assisted first draft is never an acceptable final submission. Blank Rome embeds AI in its apprenticeship programmes and says 95% of its AI training is built in-house. TRI''s webinar ''Trust by Verify'' (listed with a Chief AI Officer of Fredrikson & Byron among faculty) is aimed at teaching early-career lawyers verification habits.'
  outcomes:
  - {lever: quality, description: Randomised field experiment on quality and retained skill (patent drafting), figure: 'AI access raised quality by 0.34 SD at 10 days and 0.38 SD at 90 days; without AI at 3 months, treated lawyers beat controls by 0.32 SD overall, 0.45 SD among seniors; juniors showed no average gain and a split distribution', measures: standard deviations of blinded expert-attorney scores for 133 practicing patent lawyers at 11 US firms in a pre-registered three-month randomised trial, provenance: independent, source_ref: NBER-AUTOR-2026}
  - {lever: quality, description: Professionals who think early-career staff need structured support, figure: 71%, measures: 'share of surveyed professionals (1,816 respondents, 62 countries) who believe early-career roles need structured support from experienced peers to develop the skills AI risks displacing', provenance: independent, source_ref: TR-FOP-2026}
  prerequisites:
  - Practice-group AI champions with early tool access
  - Mentors who can review how juniors used AI
  - Exercises where AI output is wrong
  risks_and_guardrails:
  - 'NBER finds junior outcomes bifurcated: fewer mediocre scores but more poor and more good ones, so a zero average gain hides both risk and benefit (NBER-AUTOR-2026).'
  - TRI says training must include verification steps and human review to be effective (TRI-ONBOARD-2026).
  human_checkpoints:
  - Senior reviewer evaluates junior work without assuming AI use was sound
  - Mentor sessions on when to trust, verify or override outputs
  role_evolution: Juniors shift from producing first drafts to checking AI output; seniors and champions teach verification; the learning pathway is rebuilt rather than left to informal habits.
  evidence_grade: B
  sources:
  - {ref: TRI-ONBOARD-2026, title: Law firms need to redesign new attorney onboarding for the AI era, publisher: Thomson Reuters Institute, type: press, url: 'https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding', date: '2026-10-12', access: full, locator: sections 'What a redesigned onboarding program looks like' and Key insights}
  - {ref: HARVEY-BLANKROME-2026, title: 'Developing Lawyers, Not Replacing Them: How Blank Rome Trains the Next Generation With Harvey (customer story)', publisher: Harvey, type: vendor, url: 'https://www.harvey.ai/customers/blank-rome', date: '2026-08-06', access: full, locator: Key highlights and Trial Academy paragraph}
  - {ref: NBER-AUTOR-2026, title: 'Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720)', publisher: 'NBER (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere); abstract via EconPapers', type: academic, url: 'https://econpapers.repec.org/RePEc:nbr:nberwo:35720', date: 2026-09, access: full, locator: abstract (EconPapers page; full paper not accessible)}
  - {ref: TR-FOP-2026, title: Future of Professionals Report 2026 (4th edition), publisher: Thomson Reuters Institute, type: survey, url: 'https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report', date: '2026-06-22', access: full, locator: paragraph on the cost of experienced professionals leaving (71% figure); report page text}
  - {ref: TRI-TBV-2026, title: 'Trust by Verify: Catching Errors in AI Output Before They Reach the Court or Client (webinar page)', publisher: Thomson Reuters Institute, type: conference, url: 'https://www.thomsonreuters.com/en/institute/events/trust-by-verify-catching-errors-in-ai-output-before-they-reach-the-court-or-client', date: 2026-10, access: full, locator: overview and faculty; event date not shown on the page (an on-demand viewing link is shown)}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": a training and supervision design, not an AI workflow. Grade B with an adjacent-process cap: the NBER trial measures drafting quality and retained redlining skill in patent practice, not review of deliverables. Primarily belongs to the talent-learning module (see Routed). The TRI webinar date is uncertain: the landscape file listed 15 Oct 2026, the page itself does not show a date.'
- id: professional-services-quality-review-12
  title: Training or certification required before access to AI tools
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: People use AI without understanding its failure modes, and policy alone does not change habits.
  solution: Larger firms are more likely to require training before access. Reed Smith's managing partner set a firm-wide expectation of 100% AI certification for every associate, per Harvey's customer story. Cal Bar expects supervising lawyers to train staff and refresh training as tools become more autonomous.
  outcomes:
  - {lever: risk, description: Share of firms requiring specific training before use, figure: 11% of firms under 50 lawyers; 30% (50-149); 47% (150-349); 63% (350-699); 72% (over 700), measures: percentage of responding firms in each lawyer-count band that selected 'Specific training required before use' (Q3.18), provenance: independent, source_ref: ILTA-TECHSURVEY-2026}
  prerequisites:
  - Training content on failure modes and verification, not only tool features
  - A record of who has completed training
  - A mechanism to block access until completed
  risks_and_guardrails:
  - 'TRI reports that unsanctioned use is common: 34% admit using AI tools their organisation has not sanctioned (TRI-ACCOUNT-2026).'
  - Training that only covers tool features does not teach when to trust, verify or override (TRI-ACCOUNT-2026).
  human_checkpoints:
  - Access granted only after training is completed
  - Periodic refresh when policy or tools change
  role_evolution: Training and change-management roles grow; Reed Smith assembled a Chief Innovation Officer, a Senior Director of AI & Innovation and a Director of Change Leadership as one team (HARVEY-REEDSMITH-2026).
  evidence_grade: B
  sources:
  - {ref: ILTA-TECHSURVEY-2026, title: The ILTA Technology Survey 2026 Executive Summary, publisher: International Legal Technology Association (ILTA), type: survey, url: 'https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf', date: 2026-06, access: full, locator: p.5 Q3.18 policy table}
  - {ref: HARVEY-REEDSMITH-2026, title: 'Designing the Frontier Firm: How Reed Smith is Rewriting the Playbook With Harvey (customer story)', publisher: Harvey, type: vendor, url: 'https://www.harvey.ai/customers/reed-smith', date: '2026-05-11', access: full, locator: Key highlights; section on firm-wide expectation}
  - {ref: CALBAR-GENAI-2026, title: 'Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version)', publisher: 'State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC)', type: regulator, url: 'https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf', date: 2026-05, access: full, locator: p.7 duty to supervise (training)}
  - {ref: TRI-ACCOUNT-2026, title: 'Between accountability and chaos: Setting the AI standards that professionals demand', publisher: Thomson Reuters Institute, type: press, url: 'https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos', date: '2026-10-12', access: full, locator: section 'The standards gap is the real problem'}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": an access-control and training gate. Reed Smith evidence is a vendor customer story (2026-05-11). The Harvey page says 100% firm-wide associate AI certification as a highlight and as a managing-partner expectation; it does not say whether certification gates access.'
- id: professional-services-quality-review-13
  title: Checking opposing counsel's and third-party filings for fabricated authority and hidden text
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: A California appellate court declined to award fees to opposing counsel who did not detect or report fabricated citations in the other side's briefs, raising the question of a duty to detect.
  solution: Litigation teams can run the same citation-verification tools on the other side's briefs. BriefCatch markets RealityCheck for catching errors in opponents' briefs and also scans documents for concealed text such as white-on-white type, hidden formatting and zero-width characters.
  outcomes:
  - {lever: risk, description: Court consequence in Noland v. Land of the Free, figure: '$10,000 sanction on the filing attorney; fee request by opposing counsel denied; 21 of 23 case quotations in the opening brief fabricated', measures: 'number of fabricated quotations among 23 case quotations in the opening brief, as found by the Court of Appeal; sanction and fee ruling as reported', provenance: independent, source_ref: LAWSITES-NOLAND-2025}
  prerequisites:
  - Access to a verification tool for incoming briefs
  - A protocol for reporting findings to the court
  risks_and_guardrails:
  - The decision is described as possibly the first to touch on a duty to detect opponents' fake citations; its reach is unsettled (LAWSITES-NOLAND-2025).
  human_checkpoints:
  - Lawyer decides whether and how to raise suspected fabrications with the court
  role_evolution: Reviewing opponents' authorities becomes part of the litigation team's quality routine.
  evidence_grade: C
  sources:
  - {ref: LAWSITES-NOLAND-2025, title: 'A New Wrinkle in AI Hallucination Cases: Lawyers Dinged for Failing to Detect Opponent''s Fake Citations', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2025/09/a-new-wrinkle-in-ai-hallucination-cases-lawyers-dinged-for-failing-to-detect-opponents-fake-citations.html', date: '2025-09-16', access: full, locator: 'sections ''Fabricated Quotations'' and ''The Twist: No Fees for Opposing Counsel'''}
  - {ref: LAWSITES-BRIEFCATCH-2026, title: BriefCatch Launches Unified Legal Writing Suite for the AI Era (press release), publisher: 'LawSites (Robert Ambrogi), reproducing a BriefCatch release dated 2026-09-09', type: press, url: 'https://www.lawnext.com/2026/09/briefcatch-launches-unified-legal-writing-suite-for-the-ai-era.html', date: '2026-09-11', access: full, locator: RealityCheck paragraph and opening statement on opponents' briefs}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": review of incoming opposing documents. No firm is named as using this routine; the evidence is one court decision and a vendor feature. The hidden-text scan is a separate risk (concealed instructions in documents) that BriefCatch mentions without data.'
- id: professional-services-quality-review-14
  title: Project health and quality-risk scoring agent in a professional-services automation platform
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: PMO leaders learn of scope drift and quality risk late, after rework has been done and margin lost.
  solution: Certinia's Veda lists a PMO Quality Agent that scans project scope regularly to score health sentiment, a Retrospective Drafter that captures lessons learned from completed projects, and a PMO Leadership agent for portfolio oversight.
  outcomes:
  - {lever: quality, description: Vendor claim on rework and quality losses, figure: 11-23% less margin lost to rework and quality issues, measures: 'claim on the vendor''s page with no denominator, baseline, period or customer named', provenance: vendor-published, source_ref: CERTINIA-VEDA-2026}
  prerequisites:
  - Project scope, time and communications data held in the platform
  - Defined health criteria that PMO leaders trust
  risks_and_guardrails:
  - The page gives no evidence for the figure or the agent's accuracy; a sentiment score is not a quality review of a deliverable.
  human_checkpoints:
  - PMO leaders act on flagged risk
  role_evolution: PMO staff move from collecting status to acting on agent-surfaced risk.
  evidence_grade: C
  sources:
  - {ref: CERTINIA-VEDA-2026, title: Certinia AI / Veda agents for professional services (solutions page), publisher: Certinia, type: vendor, url: 'https://certinia.com/solutions/ai', date: '2026-10-19', access: full, locator: '''Manage'' agents list and ''More gains across the lifecycle'' panel; page is undated, date shown is retrieval date'}
  last_reviewed: '2026-10-19'
  notes: Partly belongs to delivery-management. Vendor claim only.
- id: professional-services-quality-review-15
  title: Deterministic comparison and redline engines alongside LLM edits to verify what changed
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Lawyers who must recheck every AI-edited clause lose the time AI saved, and a missed change in negotiation carries risk.
  solution: Litera announced in August 2026 that its Lito agent in Word would build AI change management on top of its deterministic redline comparison engine, surfacing risky changes, explaining impact and proposing rewrites, with first drafts built from firm-approved precedent. Litera frames this as closing a 'trust gap' where probabilistic outputs need extensive verification.
  outcomes:
  - {lever: quality, description: 'Vendor claim of repeatable, verifiable comparison results', figure: none published, measures: 'n/a: no accuracy or usage figure published', provenance: vendor-published, source_ref: LAWSITES-LITERA-2026}
  prerequisites:
  - Firm-approved precedent in a searchable content library
  - Document management integration
  risks_and_guardrails:
  - The release is marketing; the Manage Changes workflow was due in late September 2026 and was not shown to be in use.
  human_checkpoints:
  - Lawyer reviews flagged changes and proposed rewrites
  role_evolution: Lawyers spend time on consequences of changes rather than tracking them.
  evidence_grade: C
  sources:
  - {ref: LAWSITES-LITERA-2026, title: Litera Connects Contract Drafting and Negotiation in One Trusted Legal AI Workflow (press release), publisher: 'LawSites (Robert Ambrogi), reproducing a Litera release', type: press, url: 'https://www.lawnext.com/2026/08/litera-connects-contract-drafting-and-negotiation-in-one-trusted-legal-ai-workflow.html', date: '2026-08-18', access: full, locator: opening and 'Act on what matters' paragraphs}
  last_reviewed: '2026-10-19'
  notes: Contract negotiation is substantive work, so this is cited only for the verification design (deterministic comparison as a check on AI edits). BlackBoiler's Veris was seen only in a search listing and not opened.
- id: professional-services-quality-review-16
  title: In-house rules for bounded, reviewable AI workflows and for outside counsel and vendor AI use
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: In-house teams get AI work product from outside counsel and vendors and cannot see how it was checked; they also face internal pressure to adopt AI.
  solution: A Casepoint report, as summarised by eDiscovery Today, says mature legal teams are moving to 'bounded workflows' with known source materials, clear constraints and reviewable outputs, and treats prompts and AI-generated analyses as records. It cites Starbucks as moving from no AI use to controlled internal use while strictly restricting vendor and outside-counsel use. At Legalweek 2026, GSK's chief of staff described asking outside firms what they use, how, and how it generates savings; DLA Piper's senior managing director of AI innovation said some clients still send directives that bar AI without permission or demand warrants that models are unbiased. [in-house]
  outcomes:
  - {lever: risk, description: Control over AI use across the legal supply chain, figure: none published, measures: 'n/a: no measured outcome published', provenance: self-reported, source_ref: EDT-CASEPOINT-2026}
  prerequisites:
  - Records policy that covers AI queries and outputs
  - Outside counsel guidelines that address AI
  - Bounded workflows with source material that can be checked
  risks_and_guardrails:
  - One federal agency leader found Copilot query and response files in mailbox collections during a hold, so AI outputs are discoverable records (EDT-CASEPOINT-2026).
  - Clients' contradictory demands (use AI, but get permission first) land in the same inbox (TRI-LEGALWEEK-2026).
  human_checkpoints:
  - Legal team checks output against the underlying material
  - Department approves vendor and outside-counsel AI use
  role_evolution: Legal operations and legal departments set AI standards for suppliers and ask firms for evidence of AI use on their matters.
  evidence_grade: B
  sources:
  - {ref: EDT-CASEPOINT-2026, title: 'From AI Hype to AI Accountability: A New Report from Casepoint', publisher: eDiscovery Today (Doug Austin), type: press, url: 'https://ediscoverytoday.com/2026/07/23/from-ai-hype-to-ai-accountability-a-new-report-from-casepoint-artificial-intelligence-trends/', date: '2026-07-23', access: full, locator: 'highlights: ''Prompt Engineering is Dead'', ''Your AI Prompts are Now Official Records'', ''Hallucinations Aren''t a Bug'', ''No Broad Permission Slips'''}
  - {ref: TRI-LEGALWEEK-2026, title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide', publisher: Thomson Reuters Institute, type: conference, url: 'https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide', date: '2026-03-13', access: full, locator: sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": supplier and records governance in an in-house team. Grade B with caution: Starbucks is named only in a blog summary of a vendor-sponsored report that was not opened; the report was commissioned by Casepoint and eDiscovery Today discloses Casepoint as a sponsor. Pricing and billing parts of the Legalweek sessions are routed elsewhere.'
- id: professional-services-quality-review-17
  title: Choosing source-linked, retrieval-first research tools so every proposition can be traced
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - research-synthesis
  - review-assurance
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Free-text answers from general models can contain invented authority, and a reviewer cannot tell which statements rest on sources.
  solution: Vendors position source-grounded design as the defence. Thomson Reuters describes 'fiduciary-grade' AI as grounded in authoritative content from the first step with every citation traceable to a linked source. Align Research returns only court opinions with key passages highlighted, 'retrieves rather than generates'. Harvey's Graph maps citations and treatment across US case law so the agent follows and checks citations. Descrybe offers citation checking, treatment analysis and quote verification inside ChatGPT.
  outcomes:
  - {lever: quality, description: Independent comparison of legal AI against a generalist tool on citation support, figure: 'Authoritativeness scores averaged 6 points higher for legal AI products than for the generalist tool; accuracy about the same (legal AI 78%-81%, generalist 80%)', measures: authoritativeness (support by valid primary or secondary sources) and accuracy scores over 200 US legal research questions, provenance: independent, source_ref: VALS-VLAIR-LR-2025}
  - {lever: quality, description: Vendor test of a context graph for matter documents, figure: rubric pass rate improved by up to 30% and task cost fell by up to about 50%, measures: 'pass rate on Harvey''s Legal Agent Bench tasks with and without a context graph, vendor''s own grading set-up', provenance: vendor-published, source_ref: HARVEY-GRAPH-2026}
  prerequisites:
  - Licensed access to authoritative content
  - A review step where the lawyer opens the linked source for each key proposition
  risks_and_guardrails:
  - Stanford found retrieval-based Lexis and Westlaw tools hallucinated 17%-33% of the time despite 'hallucination-free' marketing (STANFORD-MAGESH-2024).
  - Align says its approach can still miss cases or highlight passages a lawyer disagrees with (LAWSITES-ALIGN-2026).
  - TR's CEO argues tools without authoritative content have hallucinated at well-regarded firms; this is a vendor position (LAWSITES-HASKER-2026).
  human_checkpoints:
  - Lawyer opens and reads the linked authority
  - Lawyer decides what to rely on
  role_evolution: Reviewers verify against linked sources rather than re-researching from scratch; the associate's research task shifts to selecting and reading authority.
  evidence_grade: C
  sources:
  - {ref: VALS-VLAIR-LR-2025, title: VLAIR - Legal Research, publisher: Vals AI, type: vendor, url: 'https://www.vals.ai/industry-reports/vlair-10-14-25', date: '2025-10-14', access: full, locator: key findings 1 and 2}
  - {ref: HARVEY-GRAPH-2026, title: Improving Agent Accuracy With Harvey Graph, publisher: Harvey, type: vendor, url: 'https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph', date: '2026-10-19', access: full, locator: sections 'How Harvey Graph Improves Agent Answer Quality' and 'Strong Early Eval Results'}
  - {ref: STANFORD-MAGESH-2024, title: 'Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)', publisher: 'Stanford RegLab / HAI (Magesh, Surani, Dahl, Suzgun, Manning, Ho)', type: academic, url: 'https://arxiv.org/abs/2405.20362', date: '2024-05-30', access: full, locator: abstract}
  - {ref: LAWSITES-ALIGN-2026, title: 'As AI Legal Research Tools Race to Give Answers, This New Product Gives Only Cases', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/08/as-ai-legal-research-tools-race-to-give-answers-this-new-product-gives-only-cases-and-thats-the-point.html', date: '2026-08-03', access: full, locator: opening and interview paragraphs}
  - {ref: LAWSITES-COCOUNSEL-2026, title: Thomson Reuters Opens Early Access to the 'Next Generation' of CoCounsel Legal, publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/06/thomson-reuters-opens-early-access-to-the-next-generation-of-cocounsel-legal-saying-beta-users-fing-loved-the-product.html', date: '2026-06-22', access: full, locator: paragraphs on 'fiduciary-grade AI'}
  - {ref: LAWSITES-HASKER-2026, title: 'Thomson Reuters CEO Steve Hasker on the Next Generation of CoCounsel, the ''Future of Professionals'' Report, and Why TR Is Building Its Own LLM', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/06/thomson-reuters-ceo-steve-hasker-on-the-next-generation-of-cocounsel-the-future-of-professionals-report-and-why-tr-is-building-its-own-llm.html', date: '2026-06-23', access: full, locator: interview answer on hallucination}
  - {ref: LAWSITES-DESCRYBE-2026, title: Descrybe Brings Verified Legal Research to ChatGPT (press release), publisher: 'LawSites (Robert Ambrogi), reproducing a Descrybe release', type: press, url: 'https://www.lawnext.com/2026/07/descrybe-brings-verified-legal-research-to-chatgpt.html', date: '2026-07-02', access: full, locator: opening paragraphs}
  last_reviewed: '2026-10-19'
  notes: Product claims are vendor-made. The Harvey figure is about matter context for agents, not citation checking, and is shown only as a vendor result.
- id: professional-services-quality-review-18
  title: Involving clients in vetting AI tools and deciding on disclosure of AI use on their matters
  archetype: professional-services
  module: quality-review
  function: risk-compliance-legal
  work_types:
  - client-interaction
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients increasingly ask how AI is used on their matters, while firms worry that disclosing prompts could expose work product.
  solution: In the EDRM GenAI working-group survey, 10 of 19 respondents involve clients in vetting tools or give specific details on vendors and use cases; none reported disclosing GenAI use to opposing counsel or courts. At Legalweek 2026, GSK said it asks outside firms what they use and how; Cal Bar tells lawyers to consider disclosing AI use to clients and to check court rules on disclosure.
  outcomes:
  - {lever: risk, description: Client involvement in tool vetting among a small expert survey, figure: 10 of 19 respondents, measures: 'respondents in a 19-person, self-selected, non-random EDRM GenAI working-group survey who involve clients in vetting tools or provide specific details on vendors and use cases', provenance: independent, source_ref: EDT-EDRMSURVEY-2026}
  prerequisites:
  - Outside counsel guidelines or engagement letters that address AI
  - A view on work-product protection for prompts
  risks_and_guardrails:
  - The EDRM sample is small and non-random and its respondents are described as power users (EDT-EDRMSURVEY-2026).
  - Cal Bar says the communication duty depends on the facts and the client's sophistication, and lawyers should check court disclosure rules (CALBAR-GENAI-2026, p.7 and p.9).
  human_checkpoints:
  - Lawyer decides on client communication and any court disclosure
  role_evolution: Partners and innovation leads handle client questions on AI use; TRI reports many partners have not discussed AI with most of their clients (TRI-STANDOUT-2026).
  evidence_grade: C
  sources:
  - {ref: EDT-EDRMSURVEY-2026, title: 'The EDRM GenAI Survey Results: AI and eDiscovery Trends', publisher: eDiscovery Today (Doug Austin), type: press, url: 'https://ediscoverytoday.com/2026/04/01/the-edrm-genai-survey-results-ai-and-ediscovery-trends/', date: '2026-04-01', access: full, locator: section 'Transparency and Disclosure'}
  - {ref: TRI-LEGALWEEK-2026, title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide', publisher: Thomson Reuters Institute, type: conference, url: 'https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide', date: '2026-03-13', access: full, locator: section 'Proving AI's path to saving clients money'}
  - {ref: CALBAR-GENAI-2026, title: 'Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version)', publisher: 'State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC)', type: regulator, url: 'https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf', date: 2026-05, access: full, locator: p.7 communication row; p.9 disclosure of AI use to courts}
  - {ref: TRI-STANDOUT-2026, title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey', publisher: Thomson Reuters Institute, type: survey, url: 'https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice', date: '2026-08-06', access: full, locator: Key takeaways}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": client communication and vetting. Grade C: survey evidence of a tiny sample, no named firm deployment.'
- id: professional-services-quality-review-19
  title: Blind, lawyer-voted model comparisons to inform tool choice
  archetype: professional-services
  module: quality-review
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Lawyers lack neutral, practitioner-judged evidence about which models do legal work best, and public arenas let anyone vote.
  solution: 'Percipient launched Certera.AI in beta in July 2026: a user submits a legal prompt, sees two anonymised model answers side by side, and votes; votes feed an Elo-style leaderboard. Registrants are vetted as legal professionals (bar numbers), 55 general-purpose models were included, and no legal-specific vendor products were included at launch.'
  outcomes:
  - {lever: quality, description: Lawyer-voted ranking of models on legal work, figure: none published (leaderboard not yet showing rankings at launch), measures: n/a, provenance: vendor-published, source_ref: LAWSITES-PERCIPIENT-2026}
  prerequisites:
  - Vetted legal-professional voters
  - Vendor participation for products beyond base models
  risks_and_guardrails:
  - Preference votes measure what lawyers prefer, not correctness; no accuracy audit is described.
  human_checkpoints:
  - Lawyers vote on answer quality
  role_evolution: Lawyers act as crowd evaluators of model output.
  evidence_grade: C
  sources:
  - {ref: LAWSITES-PERCIPIENT-2026, title: 'Percipient Launches Certera.AI, A Blind Head-to-Head Testing Ground for Legal AI, with a Lawyer-Voted Leaderboard On the Way', publisher: LawSites (Robert Ambrogi), type: press, url: 'https://www.lawnext.com/2026/07/percipient-launches-certera-ai-a-blind-head-to-head-testing-ground-for-legal-ai-with-a-lawyer-voted-leaderboard-on-the-way.html', date: '2026-07-13', access: full, locator: 'sections ''Legal Only, Vetted Voters'' and ''An Elo Leaderboard'''}
  last_reviewed: '2026-10-19'
  notes: 'Pattern "other": crowd evaluation of models. Early beta announced 2026-07-13; check whether the leaderboard has since gone live.'
```

## 3. Module notes

### Processes and key steps (with work types)

1. AI-assisted draft or analysis is produced (`document-production`, `research-synthesis`).
2. The drafter checks facts and sources against linked material (`review-assurance`).
3. Tool-assisted verification of citations, quotations and cited propositions (`review-assurance`; use cases 02, 13).
4. Supervisory review by a senior lawyer or engagement leader, increasingly at a named gate in a workflow (`review-assurance`, `expert-judgment`; use case 07).
5. Signer attestation and a file record of what was checked (`expert-judgment`; use cases 01, 03).
6. Client communication and any court or client disclosure of AI use (`client-interaction`; use case 18).
7. Post-delivery correction and incident response (`review-assurance`, `client-interaction`; use case 10).
8. The quality management system around the steps: policy, training before access, tool vetting and benchmarking, in-firm evaluation, override tracking (`review-assurance`, `data-reporting`, `software-systems`; use cases 01, 04, 05, 09, 12).

### Common pain points

- Errors are subtle. Filevine's demonstrations show fabricated support often sits in a dissent or case history rather than in a fake case, and Clearbrief's CEO says many citation errors are not easy to see by eye (LAWSITES-FILEVINE-2026; LAWSITES-CLEARBRIEF-2025).
- Signers lack visibility. Clearbrief says partners have been sanctioned in cases where they did not know AI had been used on the team (LAWSITES-CLEARBRIEF-2025).
- Responsibility without standards. TRI reports 47% of professionals say they hold responsibility for AI-assisted work while two in five lack professional-grade systems, and 34% admit unsanctioned tool use (TRI-ACCOUNT-2026).
- Verification is the top barrier for limited adopters among client-nominated stand-out partners, per TRI's 2026 survey (TRI-STANDOUT-2026).
- Errors are found by outsiders. A university researcher flagged the Deloitte Australia report errors; The Independent flagged the Canadian ones (CTV-DELOITTE-2025; CTV-DELOITTE-NL-2025).
- Small firms lag on controls: human-review policy 31% against 83% at 350-699 lawyers; training before access 11% against 72% at over 700 (ILTA-TECHSURVEY-2026, p.5).
- Validation takes senior time. The Covington case study says prompt development needed substantial upfront attorney investment (EDRM-EMORY-2025).
- Clients want proof: 78% of corporate clients rate AI-enabled quality improvement as very important or essential, but 6% say most or all providers deliver it (TR-FOP-2026).

### Metrics and benchmarks (with sources)

| Metric | Value | What it measures | Provenance | Source |
|---|---|---|---|---|
| Court decisions finding or implying hallucinated content | 2,202 identified at retrieval 2026-10-19 | cases in one researcher's database in which a court or tribunal addressed hallucinated content | independent | CHARLOTIN-HALLUC-2026 |
| Hallucination rate of commercial retrieval-based legal research tools | 17% to 33% | share of responses classed as hallucinated in a preregistered test | independent | STANFORD-MAGESH-2024 |
| Legal research study | four AI products 74%-78% weighted score vs lawyer baseline 69% | 200 US research questions, accuracy/authoritativeness/appropriateness | independent | VALS-VLAIR-LR-2025 |
| Firm's own benchmark | o1 6.4/10; Gemini 2.0 6.0/10 | 50 English-law questions marked by senior lawyers | self-reported | LINKLATERS-LINKSAI-2025 |
| Citation check back-test | 61.8% verified; 38.2% flagged; 8.4% severe | 2,073 citations in 68 filings with known problems | vendor-published | LAWSITES-FILEVINE-2026 |
| Suggestion acceptance | roughly 7 in 10 kept | edits generated by 1,800+ users of a contract-review agent | vendor-published | LAWSITES-MSFT-2026 |
| Policy prevalence | human review 31% to 83% by size; verification 25% to 60% | firms selecting each policy statement | independent | ILTA-TECHSURVEY-2026 |
| Skill retention | juniors no average gain without AI; seniors +0.45 SD | blinded expert scores, 133 patent lawyers | independent | NBER-AUTOR-2026 |

**Quality evidence absent:** no named firm or in-house team has published override rates, reviewer catch rates, parallel-run results (AI-assisted versus conventional review on the same work) or regulator inspection findings for AI-assisted professional deliverables. The only usage ratio found is Microsoft's acceptance rate. Independent measurement exists only for tools (Stanford, Vals) and for patent drafting (NBER).

### Guardrails and regulatory points

- California State Bar (2026): lawyers must review and approve all AI outputs, decisions, advice and filings; oversight must scale with system autonomy; supervisors set policies and train staff; agentic tools must not file or communicate with a court without lawyer review (CALBAR-GENAI-2026, pp.4, 7, 9).
- Florida Rule 2.515(d)(2) as amended, effective 2026-06-15: the signer represents that cited legal authorities exist and are accurately cited; sanctions are authorised (LAWSITES-FLRULE-2026).
- England and Wales: the Divisional Court said leaders in the profession must take practical and effective measures and that courts can inquire whether they have (AYINDE-EWHC-2025, para 9).
- Professional discipline: CPA Newfoundland and Labrador opened an investigation of Deloitte over a consulting report (INDEPENDENT-CPANL-2026). Outcome not known at the time of writing.
- ABA Formal Opinion 512 (2024) is widely cited but could not be opened this run.

### Frontier signals (dated and sourced)

- 2026-10-19: Harvey–Midpage connector includes a citation-review use; Harvey says it will launch precedent flags and cite checking for US case law over the coming months (LAWSITES-MIDPAGE-2026; HARVEY-GRAPH-2026).
- 2026-10-15: Harvey Legal Work Orchestration with reviewer-per-task gates; Harvey expects agents to take on an additional 20% of workflow steps over six months (HARVEY-ORCH-2026). Same day, Microsoft launched Copilot for Legal (LAWSITES-MSFT-2026).
- 2026-09-09/11: BriefCatch RealityCheck citation and proposition verification reaches general availability, with a hidden-text scan (LAWSITES-BRIEFCATCH-2026).
- 2026-09-02: Filevine releases a brief auditor and passage-level citator (LAWSITES-FILEVINE-2026).
- 2026-08-18: Litera pairs deterministic redlines with LLM change management (LAWSITES-LITERA-2026).
- 2026-07-13: Percipient's lawyer-voted blind model arena in beta (LAWSITES-PERCIPIENT-2026).
- 2026-06-22: Thomson Reuters opens early access to a rebuilt CoCounsel Legal under a "fiduciary-grade" standard of traceable citations (LAWSITES-COCOUNSEL-2026).
- 2026-05: California rewrites its AI guidance to cover agentic AI (CALBAR-GENAI-2026); 2026-05-28 Florida adopts its citation-representation rule (LAWSITES-FLRULE-2026).
- 2026-03-07: The Independent reports that CPA Newfoundland and Labrador has decided to investigate Deloitte over AI-related citation errors in a consulting report (INDEPENDENT-CPANL-2026).

### Workforce and role effects

- New roles: Legal Engineering Attorney, Legal Knowledge Engineer and Legal Workflow Engineer at Latham & Watkins (LATHAM-JD-2026); lawyer-evaluators at Legora and an evaluation-quality operations manager at Harvey (LEGORA-JOB-EVALS-2026; HARVEY-JOB-EVALQ-2026).
- Reviewers: partners review at designated gates (HARVEY-ORCH-2026); signing lawyers need a file record (LAWSITES-CLEARBRIEF-2025); supervising lawyers carry a duty to set policy and train (CALBAR-GENAI-2026, p.7).
- Juniors: TR's survey finds legal professionals expect the timeline to trusted judgment to lengthen by nearly two years while tax professionals expect it to shorten by one (TR-FOP-2026). NBER's trial shows split junior outcomes (NBER-AUTOR-2026). Duane Morris keeps a fixed principle that an AI first draft is never a final submission (TRI-ONBOARD-2026).
- Leadership structures: Reed Smith runs a Chief Innovation Officer, a Senior Director of AI & Innovation and a Director of Change Leadership as one team (HARVEY-REEDSMITH-2026).

### Objections and concerns practitioners raise

- Accuracy and cost of checking: an ILTA respondent said that until accuracy and quality improve, AI is an expensive toy (ILTA-TECHSURVEY-2026, p.3). Litera argues lawyers lose AI's value if they must recheck every result (LAWSITES-LITERA-2026, vendor view).
- Vendor claims: Stanford found "hallucination-free" marketing overstated for Lexis and Westlaw tools (STANFORD-MAGESH-2024). TR's CEO says generic frontier-model products without authoritative content hallucinate (LAWSITES-HASKER-2026, vendor view).
- Scrutiny gap: an EDRM panel noted GenAI has been embraced without the peer-reviewed validation that TAR required, and clients push adoption (EDT-EDRMSURVEY-2026).
- Defensibility and disclosure: practitioners worry that unverifiable GenAI review will not survive challenge, and that disclosing prompts could reach work product (EDT-CASEPOINT-2026; EDT-EDRMSURVEY-2026).
- Contradictory client demands: use AI, but seek permission first; demand savings, but refuse to pay for AI-done work (TRI-LEGALWEEK-2026).
- Public criticism of firms: Australian senators criticised Deloitte's use of AI in the welfare report (CTV-DELOITTE-2025).

### Interview probes for an advisor

1. Take the last AI-assisted deliverable or filing that left your team. Who checked which claims, against which source, and what record exists of that check?
2. When a partner or engagement leader signs, what do they know about where AI was used, and how would you find out about use outside policy?
3. What do you measure today: share of AI suggestions reviewers change or reject, error types found at review, errors found after delivery or by a client or opposing party?
4. For which tasks have you decided a second human check is not needed, and what evidence (benchmark, pilot, sample audit) supports that?
5. If AI now produces the first draft, how do juniors learn to review, and what happens to review capacity when output volume rises?

## 4. Routed to other modules

- **pursuit-proposals:** Legora's posting for a Global Services Solutions Expert targets 90% of technical RFP response content automated within six months, with human review and quality oversight (LEGORA-JOB-RFP-2026, "RFP ownership").
- **billing-collections and scoping-pricing:** Clients' requests for line-item AI transparency on invoices and guidelines refusing payment for AI-performed work (TRI-LEGALWEEK-2026); Cal Bar's rules on billing for AI-assisted time (CALBAR-GENAI-2026, p.8, not analysed here).
- **acceptance-risk:** client terms on outside counsel and vendor AI use, including Starbucks' restriction (EDT-CASEPOINT-2026) and clients' pre-approval and "unbiased model" warranties (TRI-LEGALWEEK-2026). Tag: in-house.
- **talent-learning:** the NBER skill-retention trial (NBER-AUTOR-2026), Duane Morris onboarding (TRI-ONBOARD-2026), Blank Rome's apprenticeship approach (HARVEY-BLANKROME-2026) and TR's early-career data (TR-FOP-2026). Use case 11 is kept here only for its verification-training element.
- **delivery-management:** Certinia's PMO Quality and Retrospective Drafter agents (CERTINIA-VEDA-2026); Harvey's matter orchestration beyond review gates (HARVEY-ORCH-2026).
- **client-development:** Reed Smith's claim that AI-enabled delivery wins work (HARVEY-REEDSMITH-2026).
- **work-production (if adopted) or legal-practice extension:** substantive drafting, contract redlining and review (Microsoft Legal Agent, Litera Lito) and e-discovery review methods (EDRM-EMORY-2025). They appear here only for their verification design.
- **assurance archetype:** the accountancy regulator's investigation of Deloitte over a consulting report (INDEPENDENT-CPANL-2026) may inform quality-management and ethics modules there. No audit procedures are covered here.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition, replaces Nov 2023 version) | State Bar of California, Committee on Professional Responsibility and Conduct (COPRAC) | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| AYINDE-EWHC-2025 | R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank [2025] EWHC 1383 (Admin) | High Court of Justice, King's Bench Division (Divisional Court) | regulator | https://www.judiciary.uk/wp-content/uploads/2025/06/Ayinde-v-London-Borough-of-Haringey-and-Al-Haroun-v-Qatar-National-Bank.pdf | 2025-06-06 | full |
| LAWSITES-FLRULE-2026 | Florida Supreme Court Tackles AI Hallucinations with New Rule Applicable to All State Courts | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/05/florida-supreme-court-tackles-ai-hallucinations-with-new-rule.html | 2026-05-28 | full |
| ILTA-TECHSURVEY-2026 | The ILTA Technology Survey 2026 Executive Summary | International Legal Technology Association (ILTA) | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 (4th edition) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-06-22 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TRI-ACCOUNT-2026 | Between accountability and chaos: Setting the AI standards that professionals demand | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/between-accountability-and-chaos | 2026-10-12 | full |
| TRI-ONBOARD-2026 | Law firms need to redesign new attorney onboarding for the AI era | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/redesigning-new-attorney-onboarding | 2026-10-12 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-TBV-2026 | Trust by Verify: Catching Errors in AI Output Before They Reach the Court or Client (webinar page) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events/trust-by-verify-catching-errors-in-ai-output-before-they-reach-the-court-or-client | 2026-10 | full |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| HARVEY-GRAPH-2026 | Improving Agent Accuracy With Harvey Graph | Harvey | vendor | https://www.harvey.ai/blog/improving-agent-accuracy-with-harvey-graph | 2026-10-19 | full |
| HARVEY-REEDSMITH-2026 | Designing the Frontier Firm: How Reed Smith is Rewriting the Playbook With Harvey (customer story) | Harvey | vendor | https://www.harvey.ai/customers/reed-smith | 2026-05-11 | full |
| HARVEY-BLANKROME-2026 | Developing Lawyers, Not Replacing Them: How Blank Rome Trains the Next Generation With Harvey (customer story) | Harvey | vendor | https://www.harvey.ai/customers/blank-rome | 2026-08-06 | full |
| LEGORA-HLC-2026 | Hogan Lovells Cadwalader rolls out Legora globally | Legora | vendor | https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally | 2026-10-16 | full |
| LAWSITES-MSFT-2026 | Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html | 2026-10-15 | full |
| LAWSITES-FILEVINE-2026 | Filevine Takes On Shepard's and KeyCite With Its Own AI Case Law Citator and Hallucination Checker | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/09/filevine-takes-on-shepards-and-keycite-with-its-own-ai-case-law-citator-and-hallucination-checker.html | 2026-09-02 | full |
| LAWSITES-CLEARBRIEF-2025 | Clearbrief Launches Cite Check Report to Give Law Firm Partners an Audit Trail Against AI Hallucinations | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html | 2025-12-16 | full |
| LAWSITES-LAWDROID-2025 | LawDroid Launches CiteCheck AI, A Fail-Safe Against AI Citation Hallucinations | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2025/06/lawdroid-launches-citecheck-ai-a-fail-safe-against-ai-citation-hallucinations.html | 2025-06-27 | full |
| LAWSITES-NOLAND-2025 | A New Wrinkle in AI Hallucination Cases: Lawyers Dinged for Failing to Detect Opponent's Fake Citations | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2025/09/a-new-wrinkle-in-ai-hallucination-cases-lawyers-dinged-for-failing-to-detect-opponents-fake-citations.html | 2025-09-16 | full |
| LAWSITES-ALIGN-2026 | As AI Legal Research Tools Race to Give Answers, This New Product Gives Only Cases | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/08/as-ai-legal-research-tools-race-to-give-answers-this-new-product-gives-only-cases-and-thats-the-point.html | 2026-08-03 | full |
| LAWSITES-MIDPAGE-2026 | Harvey Now Connects to Legal Research Platform Midpage Through An MCP Connector | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/10/harvey-now-connects-to-legal-research-platform-midpage-through-an-mcp-connector.html | 2026-10-19 | full |
| LAWSITES-COCOUNSEL-2026 | Thomson Reuters Opens Early Access to the 'Next Generation' of CoCounsel Legal | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/06/thomson-reuters-opens-early-access-to-the-next-generation-of-cocounsel-legal-saying-beta-users-fing-loved-the-product.html | 2026-06-22 | full |
| LAWSITES-HASKER-2026 | Thomson Reuters CEO Steve Hasker on the Next Generation of CoCounsel, the 'Future of Professionals' Report, and Why TR Is Building Its Own LLM | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/06/thomson-reuters-ceo-steve-hasker-on-the-next-generation-of-cocounsel-the-future-of-professionals-report-and-why-tr-is-building-its-own-llm.html | 2026-06-23 | full |
| LAWSITES-DESCRYBE-2026 | Descrybe Brings Verified Legal Research to ChatGPT (press release) | LawSites (Robert Ambrogi), reproducing a Descrybe release | press | https://www.lawnext.com/2026/07/descrybe-brings-verified-legal-research-to-chatgpt.html | 2026-07-02 | full |
| LAWSITES-BRIEFCATCH-2026 | BriefCatch Launches Unified Legal Writing Suite for the AI Era (press release) | LawSites (Robert Ambrogi), reproducing a BriefCatch release dated 2026-09-09 | press | https://www.lawnext.com/2026/09/briefcatch-launches-unified-legal-writing-suite-for-the-ai-era.html | 2026-09-11 | full |
| LAWSITES-LITERA-2026 | Litera Connects Contract Drafting and Negotiation in One Trusted Legal AI Workflow (press release) | LawSites (Robert Ambrogi), reproducing a Litera release | press | https://www.lawnext.com/2026/08/litera-connects-contract-drafting-and-negotiation-in-one-trusted-legal-ai-workflow.html | 2026-08-18 | full |
| LAWSITES-PERCIPIENT-2026 | Percipient Launches Certera.AI, A Blind Head-to-Head Testing Ground for Legal AI, with a Lawyer-Voted Leaderboard On the Way | LawSites (Robert Ambrogi) | press | https://www.lawnext.com/2026/07/percipient-launches-certera-ai-a-blind-head-to-head-testing-ground-for-legal-ai-with-a-lawyer-voted-leaderboard-on-the-way.html | 2026-07-13 | full |
| LATHAM-JD-2026 | Legal Engineering Attorney (job description, Technology & Information Services / Legal Innovation) | Latham & Watkins | job-posting | https://www.lw.com/admin/upload/SiteAttachments/Legal-Engineering-Attorney.pdf | 2026-05-13 | full |
| HARVEY-JOB-EVALQ-2026 | Senior Product Operations Manager, Evaluation Quality (job posting) | Harvey | job-posting | https://jobs.ashbyhq.com/harvey/f0e4e24a-2a7a-4fc4-8872-9a8a762fecf5 | 2026-08-04 | full |
| LEGORA-JOB-EVALS-2026 | Technical Legal Engineer - Evals (job posting) | Legora | job-posting | https://jobs.ashbyhq.com/legora/518304b2-0711-4779-9636-fe54b1272246 | 2026-08-19 | full |
| LEGORA-JOB-RFP-2026 | Global Services Solutions Expert (job posting) | Legora | job-posting | https://jobs.ashbyhq.com/legora/f7493093-1ae8-4f56-a332-44fccdbb90cd | 2026-07-31 | full |
| LINKLATERS-LINKSAI-2025 | UK - The LinksAI English law benchmark (Version 2) | Linklaters | firm | https://linklaters.com/insights/blogs/digilinks/2025/february/uk-the-linksai-english-law-benchmark-version-2 | 2025-02-10 | full |
| EDRM-EMORY-2025 | Case Study: Practical Testing for Effectively Organizing Documents with GenAI Review (Tara S. Emory, Covington & Burling) | EDRM | professional-body | https://edrm.net/2025/06/case-study-practical-testing-for-effectively-organizing-documents-with-genai-review/ | 2025-06-24 | full |
| EDT-FOLLOWUP-2025 | Follow-Up to the GenAI Review Case Study: eDiscovery Trends | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2025/07/07/follow-up-to-the-genai-review-case-study-ediscovery-trends/ | 2025-07-07 | full |
| EDT-EDRMSURVEY-2026 | The EDRM GenAI Survey Results: AI and eDiscovery Trends | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2026/04/01/the-edrm-genai-survey-results-ai-and-ediscovery-trends/ | 2026-04-01 | full |
| EDT-CASEPOINT-2026 | From AI Hype to AI Accountability: A New Report from Casepoint | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2026/07/23/from-ai-hype-to-ai-accountability-a-new-report-from-casepoint-artificial-intelligence-trends/ | 2026-07-23 | full |
| EDT-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today (Doug Austin) | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| CHARLOTIN-HALLUC-2026 | AI Hallucination Cases database | Damien Charlotin (HEC Paris research fellow) | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 | full |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Stanford RegLab / HAI (Magesh, Surani, Dahl, Suzgun, Manning, Ho) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full |
| VALS-VLAIR-2025 | Vals Legal AI Report (VLAIR), first report | Vals AI | vendor | https://www.vals.ai/vlair | 2025-02-27 | full |
| VALS-VLAIR-LR-2025 | VLAIR - Legal Research | Vals AI | vendor | https://www.vals.ai/industry-reports/vlair-10-14-25 | 2025-10-14 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720) | NBER (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere); abstract via EconPapers | academic | https://econpapers.repec.org/RePEc:nbr:nberwo:35720 | 2026-09 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press) | CTV News / Associated Press | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| CTV-DELOITTE-NL-2025 | N.L. government pledges strict review on AI use after more false citations found in reports | CTV News (Canadian Press) | press | https://www.ctvnews.ca/canada/newfoundland-and-labrador/article/nl-government-pledges-strict-review-on-ai-use-after-more-false-citations-found-in-reports/ | 2025-11-29 | full |
| HRREPORTER-DELOITTE-NL-2025 | AI errors: Province grapples with Deloitte report marred by false citations | Canadian HR Reporter | press | https://www.hrreporter.com/focus-areas/automation-ai/ai-errors-province-grapples-with-deloitte-report-marred-by-false-citations/393782 | 2025-11-25 | full |
| INDEPENDENT-CPANL-2026 | Accounting watchdog to investigate Deloitte over fake citations in $1.6M healthcare report | The Independent (Newfoundland and Labrador) | press | https://theindependent.ca/news/lji/accounting-watchdog-to-investigate-deloitte-over-fake-citations-in-1-6-million-healthcare-report/ | 2026-03-07 | full |
| GIGALAW-GORDONREES-2025 | Law Firm Admits Attorney Used AI, Created Fake Citations, Lied to Court (summarising Bloomberg Law) | GigaLaw | press | https://giga.law/daily-news/2025/10/27/law-firm-admits-attorney-used-ai-created-fake-citations-lied-to-court | 2025-10-27 | full |
| BESPACIFIC-GORDONREES-2025 | Large US law firm apologizes for AI errors in bankruptcy court filing (excerpting Reuters) | beSpacific | press | https://www.bespacific.com/?p=118478 | 2025-10 | full |
| CERTINIA-VEDA-2026 | Certinia AI / Veda agents for professional services (solutions page) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |

Access notes: every source is marked `full` because its page or PDF body was opened and read, with these limits. NBER-AUTOR-2026 is the EconPapers abstract page only (the full paper is subscriber-only). STANFORD-MAGESH-2024 is the arXiv abstract page only. EDRM-EMORY-2025 was read through a text mirror (r.jina.ai) after the direct fetch returned 403, and its chart values were not read. HARVEY-REEDSMITH-2026, HARVEY-BLANKROME-2026 and CERTINIA-VEDA-2026 are vendor-authored pages. CERTINIA-VEDA-2026 and CHARLOTIN-HALLUC-2026 are undated or live pages, so the date shown is the retrieval date. CALBAR-GENAI-2026 shows no date in its text; 2026-05 is the PDF creation date. TRI-TBV-2026 shows no event date.

Source counts by type (distinct sources cited in this file): academic 3, conference 3, firm 1, job-posting 4, press 25, professional-body 1, regulator 2, survey 3, vendor 8; total 50.

## 6. Gaps

- **Consulting and accounting practice.** No Big Four, McKinsey, BCG or Bain primary page describing how AI-assisted deliverables are reviewed was reachable: McKinsey and KPMG returned 403 through the text mirror, the Deloitte Zora URL returned 404, and the PwC and EY pages tried carried no relevant content. Deloitte's own statements were seen only through press reports.
- **Quality measurements.** No named firm or in-house team publishes override rates, reviewer catch rates, parallel-run comparisons or inspection findings for AI-assisted deliverables. The Filevine evaluation paper was unpublished and seen only through a journalist's description; the Casepoint report and the 2018 Hellyer citator study were not opened.
- **Unopened or blocked.** ABA Formal Opinion 512 and the ABA task force report; SRA and BSB texts; the Law Society agentic-AI explainer (403); the EDRM Legalweek preview (403 on direct fetch); Bloomberg Law and Law360 articles on the Gordon Rees and other sanctions (headline or summary only); the full NBER and Stanford papers; later Vals reports; Latham's second posting ('Legal Knowledge Engineer - Litigation', error 410).
- **Search-only items not used as evidence.** A search summary mentioned a Mississippi firm (Christian & Small), a second Gordon Rees incident, an IRS Circular 230 AI policy item and a new Newfoundland contracting rule on AI disclosure. None was confirmed in an opened source, so none appears in the use cases. Only 8 web searches ran: the shared search budget was exhausted before a planned search on KPMG, PwC and EY practice. After that point only known URLs were fetched.
- **Job postings.** Only one firm posting (Latham) shows quality-review practice at a user organisation; others found were from vendors. No in-house department or consulting-firm posting was reached.
- **Dates.** The Cal Bar guidance shows no date in its text (2026-05 is the PDF creation date). The TRI "Trust by Verify" webinar page shows no event date. Certinia's page is undated. The Reed Smith and Blank Rome stories are vendor-authored.
- **Not covered.** Engineering and architecture quality review, non-legal in-house shared services, and mid-size consulting practice.
