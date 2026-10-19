# Professional services, work-production, practice angle

Prepared 2026-10-19. Archetype: professional-services. Module: work-production (first drafts, synthesis, review against playbooks or standards, data extraction). Angle: practice (named deployments, firm and vendor announcements, product documentation, job postings).

Method: pages opened with `curl` (some through the `r.jina.ai` text mirror), `pdftotext` for the Cal Bar and ILTA PDFs, and the public Ashby job-board JSON feeds for Harvey and Legora. Eight web searches were used before the shared search budget ran out. Every source below was opened and read unless marked otherwise. Tags: **in-house** marks a corporate legal department example; unmarked examples are firm-side.

## 1. Summary

- **The named, public practice record is almost entirely legal.** Law firms and in-house legal teams account for nearly every named deployment found (Harvey, Legora, Microsoft Copilot customers). Consulting and advisory firms publish very little about substantive work production. The consulting evidence is one field experiment (HBS/BCG, 2023), PwC's Agent OS description (March 2025), and one failure (Deloitte Australia, October 2025). McKinsey, BCG, Bain, Deloitte, EY and KPMG primary pages were blocked or held nothing usable.
- **Measured quality evidence is thin and mostly external to the deployments.** The measured outcomes come from Vals (task benchmarks against a lawyer baseline), an NBER randomised trial (patent drafting), a Stanford preregistered study (research tools), Microsoft's own edit-acceptance telemetry for its Word Legal Agent, and a court-decision database of hallucination cases. Firms themselves publish adoption counts and anecdotes, not error, override or parallel-run rates. At Legalweek a Ropes & Gray technology leader described ROI measurement as resting more on conventional wisdom than hard evidence (TRI-LEGALWEEK-2026).
- **The tool mix is consolidating around a few platforms.** Harvey and Legora dominate the named firm deployments. Hogan Lovells Cadwalader announced both on the same day (2026-10-16). Microsoft, Anthropic and OpenAI each launched legal packages between May and October 2026. Playbook-driven review and drafting inside Word is the shared pattern.
- **What changes in the work.** (1) First-pass review against a playbook becomes review of suggested edits. (2) Extraction and Q&A over large document sets replaces manual abstracting. (3) Drafting starts from precedent and standards rather than a blank page. (4) Lawyers build and own the playbooks and agents ("legal engineers"). (5) Work moves into shared workspaces with clients and co-counsel.
- **Where it fails or is limited.** Vals found lawyers ahead on redlining (79.7% against 59.4% and 53.6% for the two AI tools tested) and on EDGAR research. Stanford found 17% to 33% hallucination in two leading research tools in 2024. A court-decision database counted 2,202 decisions on hallucinated content by 2026-10-19, 872 with a lawyer as a party. Deloitte Australia refunded part of a fee after a government report carried fabricated references. NBER found the durable skill gain from AI drafting help went to senior lawyers, not juniors.

## 2. Use cases

```yaml
- id: professional-services-work-production-01
  title: Playbook-based first-pass contract review and tracked-change redlining inside Word
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Reviewing counterparty paper clause by clause against internal standards and drafting the response redline is slow, and the playbook lives in people's heads or in separate documents."
  solution: "An agent inside the document reviews an agreement against a playbook, flags non-conforming provisions, proposes edits as native tracked changes with citations to the source language, and lawyers accept or reject each edit. Microsoft released its Legal Agent in Word to its Frontier early-access program on 2026-04-30 and made the legal skills generally available on 2026-10-15. Harvey (Playbooks), Legora and Anthropic (legal plugins that start with a setup interview on playbooks) offer comparable functions."
  outcomes:
    - lever: quality
      description: "Users kept roughly seven in ten of the Legal Agent's suggested edits during the Frontier release."
      figure: "about 70% of suggestions kept; nearly 100,000 edits; more than 1,800 users"
      measures: "Microsoft's wording: since the April Frontier release, more than 1,800 users have generated nearly 100,000 edits, choosing to keep roughly seven in ten suggestions. Microsoft did not publish a reviewer-graded error rate, and LawSites notes it released no independent legal benchmark."
      provenance: vendor-published
      source_ref: MSFT-COPILOTLEGAL-2026
    - lever: speed
      description: "A Microsoft in-house senior corporate counsel says a review that might take an hour initially can often take several minutes (in-house, one user's description, not a tracked metric)."
      figure: "an hour to several minutes (one user's statement)"
      measures: "one lawyer's description of his own first-pass review time; no sample size or method given"
      provenance: self-reported
      source_ref: MSFT-COPILOTLEGAL-2026
    - lever: quality
      description: "In the Vals benchmark (February 2025, older tools) the lawyer baseline beat both AI tools that entered the redlining task."
      figure: "lawyer baseline 79.7%; Harvey Assistant 59.4%; Vincent AI 53.6%"
      measures: "accuracy score on the redlining task, share of checks passed against reference answers; lawyer baseline from independent lawyers sourced through an ALSP"
      provenance: independent
      source_ref: VALS-VLAIR-2025
  prerequisites:
    - "A written playbook or approved language the agent can apply (Microsoft: review against a playbook; Anthropic: setup interview learns playbooks, escalation chains and house style)."
    - "Documents in a managed environment (Microsoft says the agent runs within Microsoft 365 security, compliance and governance controls)."
    - "Approved precedents available to draw on (Microsoft: precedents stored in SharePoint)."
  risks_and_guardrails:
    - "Microsoft's notice says the Legal Agent gives no legal advice and users are solely responsible for reviewing and verifying output (MSFT-LEGALAGENT-2026)."
    - "Cal Bar guidance says a lawyer must review, verify and correct AI output and that professional judgment cannot be delegated (CALBAR-GENAI-2026, p. 8)."
    - "Task-level evidence is mixed: Vals found lawyers ahead on redlining with the tools it tested in 2025."
  human_checkpoints:
    - "Lawyer reviews every edit before approving (MSFT-LEGALAGENT-2026)."
    - "Playbook owner maintains the standard the agent applies."
  role_evolution: "Microsoft's in-house counsel describes spending the saved time on legal judgment, negotiation strategy and advising clients (MSFT-COPILOTLEGAL-2026). The first-pass reviewer becomes the approver of suggested edits and, increasingly, the owner of the playbook."
  evidence_grade: A
  sources:
    - { ref: MSFT-COPILOTLEGAL-2026, title: "Introducing Microsoft Copilot for Legal", publisher: "Microsoft Tech Community", type: vendor, url: "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-microsoft-copilot-for-legal/4564246", date: "2026-10-15", access: full, locator: "paragraph on 1,800 users and 100,000 edits; Aneesh Mehta quote" }
    - { ref: MSFT-LEGALAGENT-2026, title: "Word Legal Agent in Frontier", publisher: "Microsoft Tech Community", type: vendor, url: "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/word-legal-agent-in-frontier/4516218", date: "2026-04-30", access: full, locator: "How the Legal Agent works; closing note" }
    - { ref: LAWSITES-MSFT-2026, title: "Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html", date: "2026-10-15", access: full, locator: "section What Microsoft Announced" }
    - { ref: VALS-VLAIR-2025, title: "Vals Legal AI Report", publisher: "Vals AI", type: academic, url: "https://www.vals.ai/industry-reports/vlair-2-27-25", date: "2025-02-27", access: full, locator: "Redlining section" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "p. 8 (Duty of competence)" }
  last_reviewed: 2026-10-19
  notes: "Date for CALBAR-GENAI-2026 is the PDF creation date (2026-05-15); the document text shows no date. The in-house tag applies to the Microsoft legal department and Uniper quotes; the product is sold to firms and in-house teams alike. Named firm customer for the wider Copilot rollout is Clyde & Co (adoption 'approaching 90%', per Microsoft's quote), which is Copilot adoption, not Legal Agent use."

- id: professional-services-work-production-02
  title: Bulk extraction of clauses and fields, and question answering, over contract and document sets
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [data-reporting, research-synthesis]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Pulling clauses, dates and fields out of long agreements and answering questions across document sets is repetitive manual reading, and tables built by hand are slow to check."
  solution: "Tools extract the text or fields a lawyer asks for, answer questions about a document set with citations, and return results in tables for review. Named uses include contract terms extraction (Goodwin), restating a four-year outsourcing agreement with 112 change notes (Dentsu, in-house), and structured issue lists in contract review (CMS)."
  outcomes:
    - lever: quality
      description: "Vals benchmark, February 2025: on document extraction, CoCounsel and Harvey Assistant scored above the lawyer baseline; on document Q&A all four tools tested were reported as above the 70.1% baseline."
      figure: "extraction lawyer baseline 71.1%; Q&A lawyer baseline 70.1%; Q&A Harvey Assistant 94.8%, CoCounsel 89.6%, Oliver 74.0%, Vincent AI 72.7%"
      measures: "accuracy as share of checks passed against reference answers (extraction dataset: 30 questions over 29 documents, 204 checks; Q&A scored the same way). Lawyer baseline from independent lawyers working to the same instructions. Scored by an LLM judge. Vals states it has a customer relationship with one or more participants."
      provenance: independent
      source_ref: VALS-VLAIR-2025
    - lever: quality
      description: "On the hardest extraction question (40 fields across three credit agreements) tool results varied widely and the lawyer baseline was low."
      figure: "CoCounsel 61.7%; Vincent 40%; lawyer baseline 39.2%; Harvey Assistant 36.7%"
      measures: "share of the 40 requested fields extracted accurately"
      provenance: independent
      source_ref: VALS-VLAIR-2025
  prerequisites:
    - "Documents loaded into a controlled workspace or vault."
    - "A defined list of fields or clauses to extract (Vals: tools did well on named clauses, worse on concepts like most-favored-nation that are not stated verbatim)."
  risks_and_guardrails:
    - "Vals error modes: tools often stop at one relevant clause when several are needed, and some miss terms of art (VALS-VLAIR-2025, Data Extraction section)."
    - "Participating vendors could opt out of tasks; Harvey withdrew from EDGAR research, vLex from chronology generation (VALS-VLAIR-2025, methodology section), so published scores are not an all-vendor comparison."
    - "ILTA: share of firms requiring human review of GenAI work product rises from 31% of firms under 50 lawyers to 79% of firms over 700 (ILTA-TECHSURVEY-2026, p. 5)."
  human_checkpoints:
    - "Reviewer checks extracted fields against the source text (citations are returned)."
    - "Spot checks on multi-clause questions, where Vals saw incomplete answers."
  role_evolution: "Goodwin describes dedicated staff building tailored workflows for client requirements (LEGORA-GOODWIN-2025). Junior review time shifts from abstracting to checking tables; no firm publishes how headcount changed."
  evidence_grade: A
  sources:
    - { ref: VALS-VLAIR-2025, title: "Vals Legal AI Report", publisher: "Vals AI", type: academic, url: "https://www.vals.ai/industry-reports/vlair-2-27-25", date: "2025-02-27", access: full, locator: "Data Extraction and Document Q&A sections; vendor and methodology sections" }
    - { ref: HARVEY-DENTSU-2026, title: "How Dentsu's Legal and Compliance Team Turned Pressure Into Strategic Advantage With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/dentsu", date: "2026-05-06", access: full, locator: "Contract Analysis and Vault" }
    - { ref: LEGORA-GOODWIN-2025, title: "Goodwin rolls out Legora firmwide", publisher: "Legora", type: vendor, url: "https://legora.com/customers/goodwin", date: "2025", access: full, locator: "paragraph on use cases" }
    - { ref: HARVEY-CMS-2026, title: "Turning AI Into a Daily Habit: How CMS Reached 95% Adoption With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/cms", date: "2026-03-25", access: full, locator: "Solution: Contract Review and Issue Spotting" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 executive summary", publisher: "ILTA", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "p. 5 policy table (Q3.18)" }
  last_reviewed: 2026-10-19
  notes: "Vals benchmark is older than the 12-18 month window (February 2025) and tests 2024-25 product versions; it is the only independent task-level extraction measurement found. Goodwin date is the 'joined Legora' month shown on the Legora customer page (2025-09), not a confirmed publication date. Dentsu is in-house."

- id: professional-services-work-production-03
  title: Summaries, chronologies and transcript analysis from large document sets
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Summarising long records and building chronologies take the most lawyer time in orientation work, and the output is needed early in a matter."
  solution: "Tools summarise documents and transcripts and draft chronologies that lawyers check and refine. Grant Thornton UK's forensic team uses structured email summaries in a table (sender, recipient, date, short summary) at the start of a case. Microsoft lists case chronologies among the multi-file tasks lawyers can delegate in Cowork."
  outcomes:
    - lever: quality
      description: "Vals benchmark, February 2025: AI tools beat the lawyer baseline on summarisation and transcript analysis, and Harvey Assistant matched it on chronology generation."
      figure: "summarisation: CoCounsel 77.2% (top), Harvey Assistant 72.1%; chronology: Harvey Assistant 80.2% = lawyer baseline 80.2%, CoCounsel 78.0%"
      measures: "accuracy as share of checks passed against reference answers; Vals says summary acceptability is subjective and limited to the firms' reference answers"
      provenance: independent
      source_ref: VALS-VLAIR-2025
  prerequisites:
    - "Source documents in a controlled workspace."
    - "Reviewers who know the matter well enough to judge relevance (Vals: judging whether a fact is relevant is where lawyers did better)."
  risks_and_guardrails:
    - "Vals: chronology required the most lawyer time, and deciding relevance may be easier for practising lawyers (VALS-VLAIR-2025, Chronology section)."
    - "Grant Thornton reports checking AI translations and summaries as part of its normal quality assurance (LEGORA-GRANTTHORNTON-2026)."
  human_checkpoints:
    - "Quality check of generated translations and summaries before analysis relies on them (LEGORA-GRANTTHORNTON-2026)."
  role_evolution: "Grant Thornton's forensic director describes reaching judgment-led analysis earlier instead of 'starting from zero' (LEGORA-GRANTTHORNTON-2026); no headcount effect reported."
  evidence_grade: A
  sources:
    - { ref: VALS-VLAIR-2025, title: "Vals Legal AI Report", publisher: "Vals AI", type: academic, url: "https://www.vals.ai/industry-reports/vlair-2-27-25", date: "2025-02-27", access: full, locator: "Document Summarization, Chronology Generation, Transcript Analysis sections" }
    - { ref: LEGORA-GRANTTHORNTON-2026, title: "How Grant Thornton UK is delivering sharp client insights in high-stakes forensic work", publisher: "Legora", type: vendor, url: "https://legora.com/customers/grant-thornton", date: "2026", access: full, locator: "From pilot to practice" }
    - { ref: LAWSITES-MSFT-2026, title: "Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html", date: "2026-10-15", access: full, locator: "Cowork delegation paragraph" }
  last_reviewed: 2026-10-19
  notes: "Same Vals benchmark and age caveat as use case 02. Grant Thornton date is the 'joined Legora' label (2026-09) on the Legora page, not a confirmed publication date."

- id: professional-services-work-production-04
  title: AI-assisted legal research with citation checking and verification before use
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Research memos need accurate answers with valid sources, but AI research tools can invent or misstate authority, so each answer needs checking."
  solution: "Lawyers use legal-specific or general AI tools for research questions and first-orientation questions in unfamiliar areas, then check citations and conclusions against the sources before relying on them. Deutsche Telekom's general counsel and a Gleiss Lutz partner both describe asking Harvey first in unfamiliar areas, then going deeper."
  outcomes:
    - lever: quality
      description: "Vals research study (published 2025-10-14): four AI products scored above the lawyer baseline on 200 US research questions."
      figure: "AI products 74%-78% average weighted score; lawyer baseline 69%; AI scored higher on 150 of 200 questions (75%)"
      measures: "average weighted score across accuracy (50%), authoritativeness (40%) and appropriateness (10%) on 200 US legal research questions"
      provenance: independent
      source_ref: VALS-VLAIRRES-2025
    - lever: quality
      description: "Multi-jurisdiction questions scored lower: on average 14 points below single-jurisdiction questions."
      figure: "14 points lower on 14 jurisdictionally complex questions"
      measures: "difference in average score between multi-jurisdiction and single-jurisdiction questions, as Vals reports"
      provenance: independent
      source_ref: VALS-VLAIRRES-2025
    - lever: risk
      description: "Preregistered Stanford evaluation (2024): two leading research tools hallucinated in a substantial minority of responses."
      figure: "17% to 33%"
      measures: "share of responses that hallucinated, for Lexis+ AI and Westlaw AI-Assisted Research and Ask Practical Law AI, in the authors' preregistered test set"
      provenance: independent
      source_ref: STANFORD-MAGESH-2024
    - lever: risk
      description: "Court-decision database of hallucinated AI content: decisions found to involve it, as of the page's 'last updated' date."
      figure: "2,202 cases; 872 with a lawyer as the party; 1,267 with a pro se litigant"
      measures: "decisions where a court or tribunal found or implied a party relied on hallucinated content, plus some where AI use was alleged; it is a catalogue of found cases, not an error rate"
      provenance: independent
      source_ref: CHARLOTIN-HALLUCINATIONS-2026
    - lever: speed
      description: "Gleiss Lutz partner says Harvey gives 85% to 90% of the answer when he needs first orientation in an unfamiliar legal area (recollection)."
      figure: "85% to 90% (partner's estimate)"
      measures: "partner's own estimate of how much of an orientation answer Harvey provides; not a tracked metric"
      provenance: self-reported
      source_ref: HARVEY-DTGLEISS-2026
  prerequisites:
    - "Access to authoritative sources the tool can cite (Vals: access to proprietary databases gave legal AI a citation advantage in its 2025 study)."
    - "A firm policy requiring verification (ILTA: 25% of firms under 50 lawyers to 55%-60% of larger firms require outputs to be cited or independently verified)."
  risks_and_guardrails:
    - "Cal Bar: lawyers must review all AI output for accuracy, including citations, before submission to a court (CALBAR-GENAI-2026, Candor to the Tribunal)."
    - "Vals: most participants did worse on multi-jurisdiction questions and 50-state surveys."
    - "Vendor claims of hallucination-free output were found overstated by the Stanford study."
  human_checkpoints:
    - "Lawyer verifies each cited authority and conclusion before it goes into advice or a filing."
  role_evolution: "Research moves from finding to verifying. Cal Bar says the duty of supervision extends to AI output used by subordinates (CALBAR-GENAI-2026)."
  evidence_grade: A
  sources:
    - { ref: VALS-VLAIRRES-2025, title: "VLAIR - Legal Research", publisher: "Vals AI", type: academic, url: "https://www.vals.ai/industry-reports/vlair-10-14-25", date: "2025-10-14", access: full, locator: "key conclusions 1-5" }
    - { ref: STANFORD-MAGESH-2024, title: "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools", publisher: "Stanford RegLab/HAI (arXiv 2405.20362)", type: academic, url: "https://arxiv.org/abs/2405.20362", date: "2024-05-30", access: full, locator: "abstract" }
    - { ref: CHARLOTIN-HALLUCINATIONS-2026, title: "AI Hallucination Cases Database", publisher: "Damien Charlotin", type: academic, url: "https://www.damiencharlotin.com/hallucinations/", date: "2026-10-19", access: full, locator: "header count and Party filter" }
    - { ref: HARVEY-DTGLEISS-2026, title: "How Deutsche Telekom and Gleiss Lutz are Setting the Direction for Legal Collaboration With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/deutsche-telekom-gleiss-lutz-collaboration", date: "2026-02-23", access: full, locator: "How Harvey Is Used Today" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Candor to the Tribunal; Duty to Supervise" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 executive summary", publisher: "ILTA", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "p. 5 policy table" }
  last_reviewed: 2026-10-19
  notes: "The Stanford study is from 2024 and tests then-current products; the Vals research study is the more recent independent measure. The Charlotin figure is a snapshot dated on the page (last updated 19 October 2026); the party counts are the page's own filters. Gleiss Lutz and Deutsche Telekom quote is mixed firm and in-house."

- id: professional-services-work-production-05
  title: First drafts of legal documents and clauses from precedents and approved standards, with lawyer review
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Drafting clauses, memos and agreements from scratch repeats work the firm or department has already done, and consistency with approved language depends on who drafts."
  solution: "Lawyers use AI to produce initial drafts from approved precedents and standards, then edit. Named examples: Goodwin lists initial drafts of legal documents among its Legora uses; a Gleiss Lutz partner says a very good associate uses Harvey two or three hours a day to draft clauses and review diligence reports; BMW Group's legal department (in-house) plans to generate first drafts based on approved internal standards and precedents in Legora; Microsoft's drafting skill can draw on approved precedents stored in SharePoint."
  outcomes:
    - lever: capacity
      description: "ILTA 2026: most GenAI-engaged firms now use generative tools for drafting, research, summarisation and contract review (ILTA's characterisation)."
      figure: "94% of responding firms engaged with GenAI (up 14 points year on year)"
      measures: "ILTA's wording: nearly every responding firm (94%) is now engaged with GenAI; 508 firms responded to the survey"
      provenance: independent
      source_ref: ILTA-TECHSURVEY-2026
    - lever: capacity
      description: "BMW Group's general counsel says Legora expands the department's capacity to handle work in-house (announcement of rollout, no measurement)."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: LEGALIT-BMW-2026
  prerequisites:
    - "Approved precedents and standards in a form the tool can draw on (BMW: approved internal standards and precedents; Microsoft: SharePoint precedents)."
    - "Training before access (ILTA: 11% of firms under 50 lawyers require training before use, rising to 72% of firms over 700)."
  risks_and_guardrails:
    - "Cal Bar: a lawyer must review, verify and correct AI-generated output and may not delegate professional judgment (CALBAR-GENAI-2026, p. 8)."
    - "Dentsu and others report no quality measurements for drafts; none of the firm sources publish error rates for drafted text."
  human_checkpoints:
    - "Lawyer edits and approves every draft before it leaves the firm or department."
  role_evolution: "Associates draft with AI daily (Gleiss Lutz); Reed Smith requires 100% associate AI certification (HARVEY-REEDSMITH-2026). NBER evidence on drafting and juniors is in use case 06."
  evidence_grade: B
  sources:
    - { ref: HARVEY-DTGLEISS-2026, title: "How Deutsche Telekom and Gleiss Lutz are Setting the Direction for Legal Collaboration With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/deutsche-telekom-gleiss-lutz-collaboration", date: "2026-02-23", access: full, locator: "A Clear Position on AI" }
    - { ref: LEGORA-GOODWIN-2025, title: "Goodwin rolls out Legora firmwide", publisher: "Legora", type: vendor, url: "https://legora.com/customers/goodwin", date: "2025", access: full, locator: "use cases paragraph" }
    - { ref: LEGALIT-BMW-2026, title: "BMW Group to roll out Legora across its legal department", publisher: "Legal IT Insider", type: press, url: "https://legaltechnology.com/bmw-group-to-roll-out-legora-across-its-legal-department/", date: "2026-10-08", access: full, locator: "paragraphs 2-3" }
    - { ref: MSFT-COPILOTLEGAL-2026, title: "Introducing Microsoft Copilot for Legal", publisher: "Microsoft Tech Community", type: vendor, url: "https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-microsoft-copilot-for-legal/4564246", date: "2026-10-15", access: full, locator: "skill areas" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 executive summary", publisher: "ILTA", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "pp. 3-5" }
    - { ref: HARVEY-REEDSMITH-2026, title: "Designing the Frontier Firm: How Reed Smith is Rewriting the Playbook With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/reed-smith", date: "2026-05-11", access: full, locator: "Key Highlights; Broad, Fast, and Self-Sustaining" }
  last_reviewed: 2026-10-19
  notes: "BMW Group (in-house) is described as 'rolling out' with planned uses, so the BMW element is an announced rollout. Goodwin date is the 'joined Legora' label (2025-09). No source in this run reports measured draft quality for firm drafting."

- id: professional-services-work-production-06
  title: AI patent-drafting assistant with blinded expert scoring, and its effect on lawyers' own skill
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [document-production, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "AI may raise the quality of drafted work while stunting the expertise professionals would build by drafting it themselves."
  solution: "Researchers gave 133 practising patent lawyers at eleven US IP firms a custom AI patent-drafting assistant for three months in a preregistered randomised trial, scored work blindly with expert patent attorneys, then tested a core task (redlining a patent application) without AI."
  outcomes:
    - lever: quality
      description: "AI access raised the quality of delivered drafting work, with larger gains for junior lawyers."
      figure: "+0.34 SD at 10 days; +0.38 SD at 90 days"
      measures: "standard deviations of blinded expert scores on benchmark patent drafting tasks, treated against control lawyers"
      provenance: independent
      source_ref: NBER-AUTOR-2026
    - lever: quality
      description: "Without AI after three months, treated lawyers outperformed controls on redlining, but the advantage was concentrated in senior lawyers."
      figure: "overall +0.32 SD; seniors +0.45 SD; juniors no average gain (scores bifurcated)"
      measures: "standard deviations on an expert-scored redlining task done without AI"
      provenance: independent
      source_ref: NBER-AUTOR-2026
  prerequisites:
    - "A purpose-built drafting assistant and a blinded expert scoring process (study design)."
  risks_and_guardrails:
    - "Skill erosion and uneven learning for junior lawyers; authors suggest foundational expertise may be a prerequisite for durable skill from AI-assisted practice."
    - "The study was conducted by Google, which also funded the direct costs; several authors are Google employees (NBER disclosure)."
  human_checkpoints:
    - "Lawyers remained the authors and own the drafted work in the trial; blinded attorneys scored it."
  role_evolution: "Evidence that the value of AI drafting help differs by seniority; junior development needs a deliberate design (NBER-AUTOR-2026). Blank Rome frames AI training for juniors as apprenticeship, not replacement (HARVEY-BLANKROME-2026)."
  evidence_grade: A
  sources:
    - { ref: NBER-AUTOR-2026, title: "Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720)", publisher: "NBER", type: academic, url: "https://www.nber.org/papers/w35720", date: "2026-09", access: full, locator: "abstract; disclosures" }
    - { ref: HARVEY-BLANKROME-2026, title: "Developing Lawyers, Not Replacing Them: How Blank Rome Trains the Next Generation With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/blank-rome", date: "2026-08-06", access: full, locator: "Solution: Starting at the Top; Weaving AI Into the Craft" }
  last_reviewed: 2026-10-19
  notes: "Patent drafting is practice-specific (IP), but the task is first-draft production, so it sits here. Maturity is piloting because it is a research trial of a custom assistant, not a firm's production tool. Date is NBER issue date (September 2026; revision October 2026)."

- id: professional-services-work-production-07
  title: Red-teaming a draft position or motion with AI before it goes out
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Authors have blind spots in their own arguments, and a full adversarial read takes hours of colleagues' time."
  solution: "A litigator puts a draft motion to dismiss into Harvey and asks what opposing counsel is likely to argue; O'Melveny partners also use Harvey to check how often a provision appears in a lender's prior loans before arguing that a term is market standard. A Bracewell partner describes Legora as a tool for testing ideas and developing case strategy."
  outcomes:
    - lever: quality
      description: "O'Melveny's Los Angeles managing partner says the tool helps her be more careful and identify her own blind spots (testimony, no measurement)."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: HARVEY-OMELVENY-2026
  prerequisites:
    - "The draft and the relevant record loaded into a secure workspace."
    - "A lawyer skilled enough to judge whether the AI's counter-arguments are real."
  risks_and_guardrails:
    - "Anything drawn from firm data (for example 'last 100 loans' comparisons) depends on data access and confidentiality terms; Cal Bar says confidentiality duties apply to inputs (CALBAR-GENAI-2026)."
  human_checkpoints:
    - "Partner decides which AI-suggested counter-arguments are credible."
  role_evolution: "O'Melveny describes lawyers asking 'Can we use Harvey?' before reaching for associate hours on charts; no headcount effect reported."
  evidence_grade: B
  sources:
    - { ref: HARVEY-OMELVENY-2026, title: "O'Melveny & Myers: Expanding the Art of Possible With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/omelveny-and-myers", date: "2026-08-25", access: full, locator: "Solution: From Brute Force to Thought Partner; Built for the Way Lawyers Work" }
    - { ref: LEGORA-CUSTOMERS-2026, title: "Legora customers", publisher: "Legora", type: vendor, url: "https://legora.com/customers", date: "2026-10", access: full, locator: "Bracewell quote" }
  last_reviewed: 2026-10-19
  notes: "Customers page is undated; 2026-10 is the date read. Evidence is testimonial only."

- id: professional-services-work-production-08
  title: AI-assisted review of large document sets in due diligence and portfolio review (lease abstracts, compliance checklists)
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Diligence means reading hundreds or thousands of documents on a deadline; teams sample or split the work by hand, and issues can be missed or found late."
  solution: "Deal and property teams load the data room into a tool that reads all documents, produces abstracts and issue lists, and builds checklists. O'Melveny used Harvey to scour a newly acquired property portfolio's whole file and build a compliance-audit checklist, surfacing entitlements the client had not known about. CMS says it reviews much larger document sets faster. PwC and IFS describe building due diligence analysis in a shared workspace as issues are found."
  outcomes:
    - lever: speed
      description: "O'Melveny reports lease abstract reviews 'compressed significantly' (no figure)."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: HARVEY-OMELVENY-2026
    - lever: capacity
      description: "CMS lawyers say they can review much larger document sets and take on work previously impractical (testimony, no figure)."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: HARVEY-CMS-2026
  prerequisites:
    - "Data-room documents in a controlled workspace; a defined issue list or playbook per specialty."
    - "Pilot scale and training: Hogan Lovells Cadwalader's Legora pilot covered more than 1,300 lawyers across 18 practice teams, including M&A and real estate."
  risks_and_guardrails:
    - "No source reports recall (missed-issue) rates from real diligence; in Harvey's own synthetic benchmark, base models in the standard tool-loop harness passed no data room on every criterion (use case 09)."
    - "Cal Bar: AI output must be reviewed and verified; agentic tools must not make substantive legal determinations without lawyer supervision (CALBAR-GENAI-2026, Agentic AI section)."
  human_checkpoints:
    - "Specialist lawyers review flagged issues and sign the diligence memo."
  role_evolution: "Hogan Lovells Cadwalader's lawyers built custom agents for knowledge management, capital markets and international arbitration (HARVEY-HLC-2026); junior diligence hours are the work most often cited as compressed, but no firm reports effects on staffing."
  evidence_grade: B
  sources:
    - { ref: HARVEY-OMELVENY-2026, title: "O'Melveny & Myers: Expanding the Art of Possible With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/omelveny-and-myers", date: "2026-08-25", access: full, locator: "Finding What No One Knew to Look For; Impact" }
    - { ref: HARVEY-CMS-2026, title: "Turning AI Into a Daily Habit: How CMS Reached 95% Adoption With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/cms", date: "2026-03-25", access: full, locator: "Solution; Impact" }
    - { ref: HARVEY-SHAREDSPACES-2026, title: "A New Era of Collaboration for Legal and Professional Services", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/a-new-era-of-collaboration-for-legal-and-professional-services", date: "2026-02-19", access: full, locator: "PwC and IFS quote" }
    - { ref: LEGORA-HLC-2026, title: "Hogan Lovells Cadwalader rolls out Legora globally", publisher: "Legora", type: vendor, url: "https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally", date: "2026-10-16", access: full, locator: "paragraph 1" }
    - { ref: HARVEY-HLC-2026, title: "Hogan Lovells Cadwalader adopts Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey", date: "2026-10-16", access: full, locator: "paragraphs 1-2" }
  last_reviewed: 2026-10-19
  notes: "Hogan Lovells Cadwalader announced both Legora (global rollout after a 1,300-lawyer pilot) and Harvey (Corporate & Finance, Litigation & Arbitration, Regulatory/IP) on 2026-10-16; how the two split the work is not stated in either release. No outcome figures were published by any of the firms."

- id: professional-services-work-production-09
  title: Agent that reads a whole data room and writes the diligence memo (benchmark and research stage)
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [review-assurance, research-synthesis, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "A full data room can hold thousands of documents and tens of millions of tokens, more than a single model context; chat tools read only a fraction."
  solution: "Harvey describes a decomposition harness in which a root agent divides the data room by category, sub-agents review each part, and the root assembles a diligence memo with citations and recommended next steps, evaluated against expert rubrics on synthetic data rooms. Harvey's platform menu also lists Agents that 'execute complex legal work end to end' (HARVEY-ORCH-2026, navigation); no named customer describes using such an agent for a whole diligence."
  outcomes:
    - lever: quality
      description: "On Harvey's synthetic diligence benchmark, base models in the standard tool-loop harness passed under a quarter of rubric criteria and none passed every criterion on any data room; the decomposition harness raised the mean sharply."
      figure: "mean pass rate 23.3% (standard tool-loop harness) to 62.4% (decomposition harness) across seven models"
      measures: "mean share of rubric pass-or-fail criteria met by the diligence memo on 50 held-out synthetic data rooms, judged by an LLM against expert rubrics"
      provenance: vendor-published
      source_ref: HARVEY-RLM-2026
    - lever: quality
      description: "Post-training the root agent raised the pass rate further on the same benchmark."
      figure: "29.9% to 63.0%"
      measures: "rubric criteria pass rate, base root model against post-trained root, on 50 held-out data rooms"
      provenance: vendor-published
      source_ref: HARVEY-RLM-2026
  prerequisites:
    - "Reference rubrics and data rooms to test against; secure access to the data room."
  risks_and_guardrails:
    - "Results are on synthetic data rooms judged by an LLM; they say nothing yet about real-matter recall."
    - "Cal Bar: agentic systems must not make substantive legal determinations without meaningful lawyer supervision (CALBAR-GENAI-2026)."
  human_checkpoints:
    - "Deal lawyers review the memo and decide what the findings mean for price, structure, reps and indemnities."
  role_evolution: "If it works, junior diligence review would become supervising agent output; no firm reports having done this."
  evidence_grade: C
  sources:
    - { ref: HARVEY-RLM-2026, title: "Post-Training RLM Agents for End-to-End M&A Diligence", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence", date: "2026-09-08", access: full, locator: "results sections" }
    - { ref: HARVEY-LABDD-2026, title: "Extending Legal Agent Bench to M&A Due Diligence", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/legal-agent-bench-m-and-a-due-diligence", date: "2026-07-17", access: full, locator: "Building a VDR" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Agentic AI section, p. 2" }
  last_reviewed: 2026-10-19
  notes: "Vendor benchmark only; counted as C. Harvey's note that diligence costs 1-4% of deal value is its own estimate and is not used as an outcome."

- id: professional-services-work-production-10
  title: Reusable matter templates where agents execute defined tasks and partners approve at review gates
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [document-production, coordination-scheduling, review-assurance]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Each new matter's process is rebuilt from a checklist, a prior deal or people's memory, and lawyers must brief the AI, move outputs and track status by hand."
  solution: "Harvey's Legal Work Orchestration (announced 2026-10-15, tasks and notifications rolling out, templates in early access) ties phases, tasks, people and review points together. Each task carries its scope, inputs and reviewer, so an agent assigned a change-of-control review can produce a consent matrix and notify the partner, who approves before the next step starts. Harvey says it expects agents to take on an additional 20% of workflow steps over six months and triple that share within a year (a forecast)."
  outcomes:
    - lever: capacity
      description: "No usage results yet; Harvey states an expectation about the share of workflow steps agents will take over."
      figure: "forecast: +20% of workflow steps in six months, tripling within a year"
      measures: "Harvey's forecast of the share of workflow steps executed by agents rather than prompted by lawyers; not a measurement"
      provenance: vendor-published
      source_ref: HARVEY-ORCH-2026
  prerequisites:
    - "Documented repeatable process (phases, tasks, playbooks, reviewers) that innovation or knowledge teams define once."
  risks_and_guardrails:
    - "Harvey says lawyers remain in control through review gates and agent work stays transparent and auditable (HARVEY-ORCH-2026)."
    - "Cal Bar: supervision must scale with agent autonomy (CALBAR-GENAI-2026)."
  human_checkpoints:
    - "Designated reviewer approves each task before the next begins (HARVEY-ORCH-2026)."
  role_evolution: "Innovation and knowledge teams define templates; associates open matters from templates; partners see status without asking for reconstruction (HARVEY-ORCH-2026)."
  evidence_grade: C
  sources:
    - { ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: "2026-10-15", access: full, locator: "How Legal Orchestration Works; The Future" }
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI and Veda agents", publisher: "Certinia", type: vendor, url: "https://certinia.com/solutions/ai", date: "2026-10", access: full, locator: "agent list (PMO Quality, Implementation Plan)" }
  last_reviewed: 2026-10-19
  notes: "Overlaps delivery-management; the work-production angle is agents executing the drafting and review tasks inside the template. Certinia date is the date read (page undated)."

- id: professional-services-work-production-11
  title: Multi-language document triage, structured email summaries and version comparison in forensic investigations
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Forensic teams spent significant time getting oriented in unfamiliar data; foreign-language documents waited on colleagues with the right language skills or on external translators; contract versions were compared side by side by hand."
  solution: "Grant Thornton UK's Forensic and Investigation Services team runs multi-language document sets through Legora for an initial translation followed by a quality check, produces tabular email summaries (sender, recipient, date, summary), and has the tool surface differences between document versions."
  outcomes:
    - lever: speed
      description: "The team says it can move into analysis earlier, with no timing figures published."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: LEGORA-GRANTTHORNTON-2026
  prerequisites:
    - "An established practitioner-led review process that the tool plugs into."
  risks_and_guardrails:
    - "Translations are quality-checked and outputs reviewed within the overall QA process (LEGORA-GRANTTHORNTON-2026)."
  human_checkpoints:
    - "Quality check of each translation for accuracy and context before analysis."
  role_evolution: "Less dependence on scarce language specialists for first-pass reading; reviewers spend more time on interpretation (LEGORA-GRANTTHORNTON-2026)."
  evidence_grade: B
  sources:
    - { ref: LEGORA-GRANTTHORNTON-2026, title: "How Grant Thornton UK is delivering sharp client insights in high-stakes forensic work", publisher: "Legora", type: vendor, url: "https://legora.com/customers/grant-thornton", date: "2026", access: full, locator: "From pilot to practice" }
  last_reviewed: 2026-10-19
  notes: "Advisory (accounting-firm forensic) example, not legal practice. Legora page shows 'joined 2026-09'; exact publication date not confirmed."

- id: professional-services-work-production-12
  title: AI second-reader check for internal inconsistencies in long reports
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "In long reports, keeping facts, dates and figures consistent is hard, and an inconsistent timeline can undermine a report's credibility."
  solution: "Grant Thornton UK's forensic team uses Legora as an additional layer next to its multi-reviewer QC. The firm gives one example where the tool flagged a date in a report that was inconsistent with the documented timeline."
  outcomes:
    - lever: quality
      description: "One reported catch of a timeline inconsistency; no catch rate or false-alarm rate published."
      figure: "none published"
      measures: "anecdote of a single flagged date; no count of issues found"
      provenance: self-reported
      source_ref: LEGORA-GRANTTHORNTON-2026
  prerequisites:
    - "A rigorous multi-reviewer QC process that the tool supplements."
  risks_and_guardrails:
    - "Positioned as an extra set of eyes to support, never replace, human review (LEGORA-GRANTTHORNTON-2026)."
  human_checkpoints:
    - "Existing multi-reviewer QC remains the control."
  role_evolution: "Reviewers receive AI-flagged inconsistencies to confirm or dismiss."
  evidence_grade: B
  sources:
    - { ref: LEGORA-GRANTTHORNTON-2026, title: "How Grant Thornton UK is delivering sharp client insights in high-stakes forensic work", publisher: "Legora", type: vendor, url: "https://legora.com/customers/grant-thornton", date: "2026", access: full, locator: "From pilot to practice (quality assurance paragraph)" }
  last_reviewed: 2026-10-19
  notes: "Single anecdote; grade B on the named deployment alone. Consistency checking of AI-assisted deliverables is the counterpart to the failure in use case 17 (Deloitte Australia)."

- id: professional-services-work-production-13
  title: Shared AI workspaces where clients, co-counsel and advisors work from the same material
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [document-production, client-interaction]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Drafts, diligence analysis and regulatory work move between client, law firm and advisors by email, tracked changes and version control, losing context at each handoff."
  solution: "Harvey Shared Spaces lets internal teams and external parties, including non-Harvey customers, work in one workspace with a shared vault, workflows and permissions. O'Melveny deploys Shared Spaces with clients; Dentsu (in-house) creates a Vault and shares it with law-firm partners; Deutsche Telekom (in-house) and Gleiss Lutz are exploring a move from parallel workstreams to shared work; PwC and IFS describe sharing deal analysis as issues are found."
  outcomes:
    - lever: experience
      description: "Participants describe fewer handoffs and faster visibility; none publish measures."
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: HARVEY-SHAREDSPACES-2026
  prerequisites:
    - "Data residency and privacy assessment (Deutsche Telekom required encryption and storage in Germany as a condition)."
    - "Strict permissions and auditability across organisations."
  risks_and_guardrails:
    - "Client data crossing organisations raises confidentiality and privilege risks; Cal Bar says agentic tools must not send client data externally without safeguards (CALBAR-GENAI-2026, Confidentiality)."
  human_checkpoints:
    - "Each organisation's lawyers review output before relying on it; permissions set by the owner of the matter."
  role_evolution: "In-house teams and outside counsel work 'on the same wavelength' on shared material (HARVEY-DTGLEISS-2026); Dentsu asks outside firms to extract value from the data they hold."
  evidence_grade: B
  sources:
    - { ref: HARVEY-SHAREDSPACES-2026, title: "A New Era of Collaboration for Legal and Professional Services", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/a-new-era-of-collaboration-for-legal-and-professional-services", date: "2026-02-19", access: full, locator: "design partner quotes" }
    - { ref: HARVEY-DTGLEISS-2026, title: "How Deutsche Telekom and Gleiss Lutz are Setting the Direction for Legal Collaboration With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/deutsche-telekom-gleiss-lutz-collaboration", date: "2026-02-23", access: full, locator: "Trust First; From Parallel Work to Shared Context" }
    - { ref: HARVEY-DENTSU-2026, title: "How Dentsu's Legal and Compliance Team Turned Pressure Into Strategic Advantage With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/dentsu", date: "2026-05-06", access: full, locator: "Collaboration With External Law Firms" }
    - { ref: HARVEY-OMELVENY-2026, title: "O'Melveny & Myers: Expanding the Art of Possible With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/omelveny-and-myers", date: "2026-08-25", access: full, locator: "Built for the Way Lawyers Work" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Confidentiality" }
  last_reviewed: 2026-10-19
  notes: "Pattern 'other': multi-party shared workspace with AI, a different shape from the listed patterns. Mixed firm and in-house. All sources are Harvey-hosted."

- id: professional-services-work-production-14
  title: Lawyer-built workflow agents for recurring in-house compliance assessments (in-house)
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Recurring assessments such as data protection impact assessments and non-compete checks consume legal time for each business request."
  solution: "In-house lawyers build agents or workflows in the platform for recurring assessments. Dentsu's legal team says a US-based media lawyer built a Harvey agent for data protection impact assessments, and the team also uses workflows for non-compete checks on new customers and for commercial compliance obligations. Harvey lists self-serve NDA review for business partners as a Shared Spaces use."
  outcomes:
    - lever: speed
      description: "A lawyer-built DPIA agent is reported to have cut the process time."
      figure: "75% reduction"
      measures: "Harvey's case study says the agent 'cut the process by 75%'; it does not state what was timed, the sample, or who measured it"
      provenance: vendor-published
      source_ref: HARVEY-DENTSU-2026
    - lever: capacity
      description: "Dentsu estimates lawyers save time and weekly engagement is high (estimate, not a tracked saving)."
      figure: "93% of lawyers use Harvey weekly; estimated 4 to 10 hours saved per week per lawyer"
      measures: "Dentsu legal team: 93% of lawyers using Harvey weekly across a 250-person legal and compliance function; hours saved are described as an estimate"
      provenance: vendor-published
      source_ref: HARVEY-DENTSU-2026
  prerequisites:
    - "Lawyers with time and skill to build workflows; vendor support (Dentsu says it works closely with Harvey because it has no large R&D team)."
    - "Integration with Outlook, Word and SharePoint so lawyers stay in their tools."
  risks_and_guardrails:
    - "Single anecdote for the 75% figure; method unknown."
    - "Workflows crossing legal and business lines need ownership and review rules."
  human_checkpoints:
    - "Lawyers review assessment outputs; Dentsu describes AI as supporting, not replacing, the work."
  role_evolution: "Lawyers become workflow builders; Dentsu's leaders tell teams that using these tools is part of their career path (HARVEY-DENTSU-2026)."
  evidence_grade: B
  sources:
    - { ref: HARVEY-DENTSU-2026, title: "How Dentsu's Legal and Compliance Team Turned Pressure Into Strategic Advantage With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/dentsu", date: "2026-05-06", access: full, locator: "Key Highlights; Workflows That Cross Functional Lines" }
    - { ref: LEGALIT-LEGALGEEK-2026, title: "Legal Geek: Buy, Build, Bin - what legal is really doing with AI", publisher: "Legal IT Insider", type: conference, url: "https://legaltechnology.com/legal-geek-buy-build-bin-what-legal-is-really-doing-with-ai/", date: "2026-10-15", access: full, locator: "paragraph on Dentsu" }
    - { ref: HARVEY-SHAREDSPACES-2026, title: "A New Era of Collaboration for Legal and Professional Services", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/a-new-era-of-collaboration-for-legal-and-professional-services", date: "2026-02-19", access: full, locator: "use cases list" }
  last_reviewed: 2026-10-19
  notes: "In-house. Not grade A because the figures are vendor-published and the hours are described as estimates. The Legal Geek recap repeats the Harvey figures with 'reportedly'; it is not independent confirmation."

- id: professional-services-work-production-15
  title: AI-first-pass directives and insourcing in corporate legal departments (in-house)
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types: [document-production, review-assurance, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Corporate legal departments face pressure to do more with the same headcount and to reduce outside counsel spend."
  solution: "In-house teams set a default of using AI first on routine work and widen the scope. TC Energy introduced a 'Harvey-First' directive during its pilot, encouraging lawyers to use Harvey as a first pass, and then deployed it across litigation, regulatory, corporate and M&A, commercial contracting and compliance work. GE Aerospace deployed Harvey across Legal & Compliance after a pilot. Dentsu lists reduced reliance on external counsel among its results. BMW Group is rolling out Legora across its legal department."
  outcomes:
    - lever: cost
      description: "Few in-house teams report receiving savings from law firms' AI use, though many have mandated it."
      figure: "48% of in-house teams have mandated their law firms to use AI; only one reported receiving cost savings"
      measures: "RSGI survey of 27 in-house teams (87 respondents across 60 firms and 27 in-house teams in total), fielded April-June 2026, commissioned by Harvey; proportion of in-house teams mandating AI, and teams reporting cost savings from it"
      provenance: vendor-published
      source_ref: LEGALIT-RSGI-2026
    - lever: capacity
      description: "Most in-house respondents expect flat headcount."
      figure: "68% of in-house teams expect headcount to remain flat"
      measures: "share of in-house respondents in the RSGI survey expecting flat headcount"
      provenance: vendor-published
      source_ref: LEGALIT-RSGI-2026
  prerequisites:
    - "Security, privacy and data-location assessment (Deutsche Telekom); governance controls that fit the department's AI policy."
  risks_and_guardrails:
    - "Directives raise the verification burden; TC Energy's GC pairs Harvey with the 'judgment and expertise of our lawyers'."
    - "Survey is vendor-commissioned, with a small in-house sample."
  human_checkpoints:
    - "Lawyer reviews the first pass; complex matters stay with senior lawyers."
  role_evolution: "In-house teams say the aim is more capacity and strategic advice (GE Aerospace, TC Energy). 94% of in-house teams in the RSGI sample are changing hiring criteria to prioritise AI skills (RSGI via Legal IT Insider)."
  evidence_grade: B
  sources:
    - { ref: HARVEY-TCENERGY-2026, title: "TC Energy deploys Harvey across its legal team", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/tc-energy-deploys-harvey-across-its-legal-team", date: "2026-10-05", access: full, locator: "paragraphs 1-2" }
    - { ref: HARVEY-GE-2026, title: "GE Aerospace deploys Harvey across its Legal & Compliance organization", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/ge-aerospace-deploys-harvey-across-its-legal-and-compliance-organization", date: "2026-09-01", access: full, locator: "paragraphs 1-3" }
    - { ref: HARVEY-DENTSU-2026, title: "How Dentsu's Legal and Compliance Team Turned Pressure Into Strategic Advantage With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/dentsu", date: "2026-05-06", access: full, locator: "Key Highlights" }
    - { ref: LEGALIT-BMW-2026, title: "BMW Group to roll out Legora across its legal department", publisher: "Legal IT Insider", type: press, url: "https://legaltechnology.com/bmw-group-to-roll-out-legora-across-its-legal-department/", date: "2026-10-08", access: full, locator: "paragraphs 1-3" }
    - { ref: LEGALIT-RSGI-2026, title: "RSGI's second Harvey report shows jump in adoption", publisher: "Legal IT Insider", type: press, url: "https://legaltechnology.com/rsgis-second-harvey-report-shows-jump-in-adoption/", date: "2026-06-17", access: full, locator: "key findings bullets 6-7" }
  last_reviewed: 2026-10-19
  notes: "In-house. Deployment announcements give no outcome figures. Dentsu's 'reduction in external counsel reliance' is a highlight without a number. BMW is an announced rollout with planned uses; TC Energy and GE Aerospace are described as deployed after pilots."

- id: professional-services-work-production-16
  title: Regulatory horizon scanning and monitoring feeding legal work
  archetype: professional-services
  module: work-production
  function: risk-compliance-legal
  work_types: [research-synthesis]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Tracking regulatory change across jurisdictions is a continuous reading task done by people and bulletins."
  solution: "Hogan Lovells Cadwalader will be a design partner for Legora's Monitors, a regulatory horizon-scanning tool, guiding the sources, jurisdictions and alert logic for its global regulatory practice; BMW Group's legal teams plan to use AI-supported workflows to monitor regulatory developments; Harvey lists Horizon Scanning as a platform product."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "no figure given"
      provenance: vendor-published
      source_ref: LEGORA-HLC-2026
  prerequisites:
    - "Definition of sources, jurisdictions and alert logic by the practice."
  risks_and_guardrails:
    - "Alerts need a lawyer's assessment of relevance before action."
  human_checkpoints:
    - "Practice lawyers decide which alerts matter and what to advise."
  role_evolution: "Regulatory practice leaders shape the product's sources and alert logic as design partners (LEGORA-HLC-2026)."
  evidence_grade: C
  sources:
    - { ref: LEGORA-HLC-2026, title: "Hogan Lovells Cadwalader rolls out Legora globally", publisher: "Legora", type: vendor, url: "https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally", date: "2026-10-16", access: full, locator: "design partner paragraph" }
    - { ref: LEGALIT-BMW-2026, title: "BMW Group to roll out Legora across its legal department", publisher: "Legal IT Insider", type: press, url: "https://legaltechnology.com/bmw-group-to-roll-out-legora-across-its-legal-department/", date: "2026-10-08", access: full, locator: "paragraph 3" }
  last_reviewed: 2026-10-19
  notes: "Announcements only. May belong with knowledge-management; kept here as a research-synthesis task that feeds advice."

- id: professional-services-work-production-17
  title: Consultant analysis and deliverable drafting with firm-approved AI, and the quality failure to design against
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Consulting deliverables combine research, analysis and written output under time pressure, and errors in cited sources can reach the client."
  solution: "Consultants use AI to draft analysis and text. The best field evidence is the HBS/BCG experiment with 758 BCG consultants (2023, GPT-4). A production example is Deloitte Australia, whose revised report for an Australian government department disclosed that Azure OpenAI was used in writing it."
  outcomes:
    - lever: speed
      description: "For 18 tasks within the AI frontier, consultants using AI completed more tasks and did them faster, with quality rated higher."
      figure: "12.2% more tasks completed; 25.1% faster"
      measures: "HBS working paper abstract: average over 18 realistic consulting tasks, 758 BCG consultants randomised to no AI, GPT-4, or GPT-4 with prompt guidance"
      provenance: independent
      source_ref: HBS-DELLACQUA-2023
    - lever: quality
      description: "For one complex task outside the frontier, AI users were less likely to produce the correct solution."
      figure: "19% less likely to be correct"
      measures: "HBS abstract: AI users on the task chosen to be outside AI's frontier compared with the no-AI group"
      provenance: independent
      source_ref: HBS-DELLACQUA-2023
    - lever: risk
      description: "Deloitte Australia agreed to repay the final instalment on a AUD 440,000 contract after the government department found incorrect footnotes and references; quotes attributed to a judge and references to nonexistent reports were removed in a revised version."
      figure: "AUD 440,000 contract (final instalment to be repaid; amount to be made public)"
      measures: "AP report: contract value and the department's statement that Deloitte agreed to repay the final instalment; the 237-page report's 'substance' and recommendations were maintained"
      provenance: independent
      source_ref: CTV-DELOITTE-2025
  prerequisites:
    - "Firm-approved AI tools and disclosure rules for AI use in client deliverables."
    - "A reference-checking step before release."
  risks_and_guardrails:
    - "Fabricated quotes and nonexistent references reached a client report (CTV-DELOITTE-2025)."
    - "Performance varies by task; AI helped inside the frontier and hurt outside it (HBS-DELLACQUA-2023)."
  human_checkpoints:
    - "Engagement team verifies every cited source and quote before release."
  role_evolution: "No primary source on consultant role change. PwC's Agent OS source (use case 18) is the only firm-published description of agent use in advisory."
  evidence_grade: B
  sources:
    - { ref: HBS-DELLACQUA-2023, title: "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality", publisher: "Harvard Business School (HBS Working Paper 24-013)", type: academic, url: "https://www.hbs.edu/faculty/Pages/item.aspx?num=64700", date: "2023-09", access: full, locator: "abstract" }
    - { ref: CTV-DELOITTE-2025, title: "Deloitte to partially refund Australian government for report with apparent AI-generated errors", publisher: "The Associated Press via CTV News", type: press, url: "https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/", date: "2025-10-07", access: full, locator: "paragraphs 1-4 and 9" }
  last_reviewed: 2026-10-19
  notes: "Grade capped at B: the HBS tasks were designed for the experiment with an older model and are not production deliverables, and the Deloitte item is a failure report rather than a measured deployment. Secondary-source claims about McKinsey's Lilli (usage, agents, outcome-based fees) appeared only in search results and conflict in the landscape; they are not used here. HBS paper is forthcoming in Organization Science per the HBS page."

- id: professional-services-work-production-18
  title: Task agents for document extraction and data mapping inside a firm's advisory delivery
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [data-reporting, document-production]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Advisory teams extract information from documents and spreadsheets and move it into target formats by hand."
  solution: "PwC said in March 2025 that it used its Agent OS across tax, assurance and advisory with 250 agents for specific tasks. Named agent types include Document Extraction and Processing agents (vector search plus user-defined search terms, then formatting) and Data Bridge agents that extract data from Excel files or PDFs, map it to a target format, and validate values."
  outcomes:
    - lever: capacity
      description: "PwC reports the number of task agents deployed (a count, not an outcome of work change)."
      figure: "250 agents"
      measures: "PwC technology officer Matt Wood, as reported by Accounting Today: number of different AI agents deployed across the firm for specific tasks, across tax, assurance and advisory"
      provenance: self-reported
      source_ref: AT-PWC-AGENTOS-2025
  prerequisites:
    - "Governance, monitoring and orchestration standards formalised after more than a year of building agents (per PwC)."
  risks_and_guardrails:
    - "PwC found that several agents in one conversation stream could produce inconsistent or unpredictable outputs and introduced deterministic routing between agents and their skills."
    - "PwC found overly negative reinforcement could confuse agents and moved to structured prompts."
  human_checkpoints:
    - "Not described in the source."
  role_evolution: "Not described in the source."
  evidence_grade: B
  sources:
    - { ref: AT-PWC-AGENTOS-2025, title: "PwC announces Agent OS for coordinating AI agents", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/pwc-announces-agent-os-for-coordinating-ai-agents", date: "2025-03-27", access: full, locator: "paragraphs on deployed agents and lessons learned" }
  last_reviewed: 2026-10-19
  notes: "Older than the 12-18 month window (19 months); kept because it is the only firm-described agent deployment in advisory work production. Audit and tax technical agents belong to other archetypes."

- id: professional-services-work-production-19
  title: Firm playbooks, vaults and custom agents built by embedded legal engineers
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [document-production, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "A firm's best precedent and review standards sit with a few experts, and juniors take years to absorb them."
  solution: "Firms package expertise into reusable playbooks, vaults and agents. Hogan Lovells Cadwalader lawyers built custom agents for knowledge management, capital markets and international arbitration, with collaborative playbook building. Blank Rome built a brief-bank vault, an EEOC-charge playbook, a transactions playbook and a civil litigation toolkit for juniors. MinterEllison seconded staff from billable work into an accelerator that produced a network of 'legal engineers' and more than 150 use cases. Job postings show firms and vendors hiring for this role."
  outcomes:
    - lever: capacity
      description: "MinterEllison's accelerator identified use cases and workflows (counts, not results)."
      figure: "more than 150 use cases identified; over a thousand employees logged in on the first day"
      measures: "Legora case study: use cases identified by accelerator participants; employees logging in on day one of the firm-wide rollout"
      provenance: vendor-published
      source_ref: LEGORA-MINTERELLISON-2026
    - lever: cost
      description: "Blank Rome says about 95% of its AI training is built and delivered in-house."
      figure: "roughly 95%"
      measures: "Harvey case study: share of AI training delivered by in-house staff"
      provenance: vendor-published
      source_ref: HARVEY-BLANKROME-2026
  prerequisites:
    - "Dedicated capacity (MinterEllison relieved participants of billable work)."
    - "Innovation, knowledge-management and practice-group sponsorship; a named AI leadership structure (Reed Smith: chief innovation officer, senior director of AI, director of change leadership)."
  risks_and_guardrails:
    - "Quality of the playbook limits quality of output; the Robert Walters and PwC Legal postings both call for evaluation and benchmarking skills."
  human_checkpoints:
    - "Practice experts own and update playbooks."
  role_evolution: "New roles: legal engineers (Harvey has 34 postings with 'Legal Engineer' or 'Legal Engineering' in the title, HARVEY-JOBS-2026, and Legora has 54, LEGORA-JOBS-2026, on their Ashby boards as of 2026-10-19, some duplicates); firm-side postings for 'Legal Engineer' or AI-enabled legal delivery roles ask for prompts, workflows, playbooks, evaluation sets and agentic AI skills (PWC-LEGALJOB-2026, RW-LEGALENGINEER-2026)."
  evidence_grade: B
  sources:
    - { ref: HARVEY-HLC-2026, title: "Hogan Lovells Cadwalader adopts Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey", date: "2026-10-16", access: full, locator: "paragraph 2" }
    - { ref: HARVEY-BLANKROME-2026, title: "Developing Lawyers, Not Replacing Them: How Blank Rome Trains the Next Generation With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/blank-rome", date: "2026-08-06", access: full, locator: "Giving Every Lawyer the Firm's Best Thinking" }
    - { ref: LEGORA-MINTERELLISON-2026, title: "How MinterEllison is investing in its people to build AI capability and transform legal delivery", publisher: "Legora", type: vendor, url: "https://legora.com/customers/minterellison", date: "2026", access: full, locator: "With Legora, MinterEllison; An Accelerator Program" }
    - { ref: HARVEY-REEDSMITH-2026, title: "Designing the Frontier Firm: How Reed Smith is Rewriting the Playbook With Harvey", publisher: "Harvey", type: vendor, url: "https://www.harvey.ai/customers/reed-smith", date: "2026-05-11", access: full, locator: "Solution: A Trio Built for Transformation" }
    - { ref: PWC-LEGALJOB-2026, title: "Legal Engineer - AI-Enabled Legal Delivery (Senior Associate / Manager)", publisher: "PwC (Global Legal), Brussels, via LegalAlphabet", type: job-posting, url: "https://legalalphabet.com/job/legal-engineer-ai-enabled-legal-delivery-senior-associate-manager-job-at-pwc-global-legal-in-brussels", date: "2026-09-16", access: full, locator: "responsibilities and requirements" }
    - { ref: RW-LEGALENGINEER-2026, title: "Legal Engineer lawyer - leading global law firm (London)", publisher: "Robert Walters (for an unnamed law firm)", type: job-posting, url: "https://www.robertwalters.co.uk/legal/jobs/in-housegeneralist/1910788-legal-engineer-lawyer---leading-global-law-firm.html", date: "2026-09-09", access: full, locator: "responsibilities" }
    - { ref: HARVEY-JOBS-2026, title: "Legal Engineer (Law Firm, Corporate) - Harvey job board", publisher: "Harvey (Ashby job board)", type: job-posting, url: "https://jobs.ashbyhq.com/harvey/c3b9e500-dc27-4afe-9b8a-31223c6b18fe", date: "2026-06-17", access: full, locator: "Function overview: legal engineers translate real legal work into Harvey solutions" }
    - { ref: LEGORA-JOBS-2026, title: "Legal Engineer (Accounting) - Legora job board", publisher: "Legora (Ashby job board)", type: job-posting, url: "https://jobs.ashbyhq.com/legora/57ec5894-05b4-4fc7-b4b1-a6892d813134", date: "2026-10-15", access: full, locator: "What you'll do" }
  last_reviewed: 2026-10-19
  notes: "Posting counts come from the public Ashby JSON feeds fetched 2026-10-19 (title match), not an official headcount. MinterEllison date is the Legora 'joined' label (2026-09). Talent-learning aspects of the accelerator route to that module."

- id: professional-services-work-production-20
  title: Evaluation and sampling programme for AI-assisted work product (hiring signal)
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Firms say they cannot yet show clients quality or savings from AI-assisted work, and review of AI output is largely ad hoc."
  solution: "IDEA (labelled): a standing programme that defines accuracy and completeness criteria, runs sampling and testing on AI-assisted work, and keeps traceability. Practitioners are discussing it, and a PwC legal posting and a London law-firm posting ask for exactly these skills, but no public deployment with results was found."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "no figure given"
      provenance: self-reported
      source_ref: PWC-LEGALJOB-2026
  prerequisites:
    - "Evaluation frameworks, evaluation sets and benchmarking skills (RW-LEGALENGINEER-2026)."
  risks_and_guardrails:
    - "ILTA: share of firms requiring human review of AI work product ranges from 31% (under 50 lawyers) to 79% (over 700), so review coverage is uneven (ILTA-TECHSURVEY-2026, p. 5)."
  human_checkpoints:
    - "Human-in-the-loop review, sampling and escalation paths (PWC-LEGALJOB-2026)."
  role_evolution: "Legal engineers take on QA and benchmarking duties."
  evidence_grade: D
  sources:
    - { ref: PWC-LEGALJOB-2026, title: "Legal Engineer - AI-Enabled Legal Delivery (Senior Associate / Manager)", publisher: "PwC (Global Legal), Brussels, via LegalAlphabet", type: job-posting, url: "https://legalalphabet.com/job/legal-engineer-ai-enabled-legal-delivery-senior-associate-manager-job-at-pwc-global-legal-in-brussels", date: "2026-09-16", access: full, locator: "responsibilities: review protocols, sampling and testing" }
    - { ref: RW-LEGALENGINEER-2026, title: "Legal Engineer lawyer - leading global law firm (London)", publisher: "Robert Walters (for an unnamed law firm)", type: job-posting, url: "https://www.robertwalters.co.uk/legal/jobs/in-housegeneralist/1910788-legal-engineer-lawyer---leading-global-law-firm.html", date: "2026-09-09", access: full, locator: "AI quality assurance and benchmarking responsibility" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: "Thomson Reuters Institute", type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: "2026-03-13", access: full, locator: "Polak and Blair paragraphs" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 executive summary", publisher: "ILTA", type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "p. 5 policy table" }
  last_reviewed: 2026-10-19
  notes: "Graded D (idea): job postings show firms hiring for evaluation, but no deployment or result is public. Idea is discussed by practitioners (Legalweek panel; Legal Geek recap says a pilot should have an agreed measure of success)."

- id: professional-services-work-production-21
  title: Delegating multi-file legal tasks to a general-purpose agent workspace (obligation tracking, chronologies, closing checklists)
  archetype: professional-services
  module: work-production
  function: service-delivery
  work_types: [research-synthesis, document-production, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Work that spans agreements, emails, meetings and files requires a lawyer to move between tools and carry context by hand."
  solution: "Three general-purpose AI providers announced legal packages in 2026: Anthropic (Claude for Legal, 2026-05-12: connectors, 12 practice-area plugins starting with a setup interview on playbooks, and cookbooks deployable as Managed Agents), Microsoft (Copilot for Legal, 2026-10-15, with Cowork for multi-file tasks such as obligation tracking, term comparison and chronologies), and OpenAI (Astra for Law, 2026-09-17, a model configuration with a legal search index, offered to Am Law 200 firms through Trusted Access)."
  outcomes:
    - lever: capacity
      description: "Anthropic says legal professionals have become the most engaged Cowork users of any knowledge-work function (LawSites report of Anthropic's statement; no figure)."
      figure: "none published"
      measures: "no figure given"
      provenance: vendor-published
      source_ref: LAWSITES-ANTHROPIC-2026
  prerequisites:
    - "Connectors into document management, research and e-discovery tools; setup of playbooks and escalation chains."
  risks_and_guardrails:
    - "Cal Bar: agentic tools must not send client data externally without safeguards and review (CALBAR-GENAI-2026)."
    - "OpenAI offers a zero data retention policy to the Trusted Access program (LAWSITES-OPENAI-2026)."
  human_checkpoints:
    - "Lawyer supervises and reviews the outputs; vendors state the tools do not replace professional judgment."
  role_evolution: "Lawyers delegate whole workstreams to agents and supervise them; no firm has published results."
  evidence_grade: C
  sources:
    - { ref: LAWSITES-ANTHROPIC-2026, title: "Anthropic Goes All-In on Legal, Releasing More Than 20 Connectors and 12 Practice-Area Plugins for Claude", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html", date: "2026-05-12", access: full, locator: "paragraphs 2-3 and plugin paragraphs" }
    - { ref: LAWSITES-OPENAI-2026, title: "OpenAI Releases Astra for Law, A GPT-6 Model Tailored for Legal Work, Targeting Large Firms and Tech Vendors", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/09/openai-releases-astra-for-law-a-gpt-6-model-configured-for-legal-work.html", date: "2026-09-17", access: full, locator: "paragraphs 3-5" }
    - { ref: LAWSITES-MSFT-2026, title: "Microsoft Launches Copilot for Legal, Becoming the Fourth AI Giant in Five Months to Build Out a Legal Vertical", publisher: "LawSites (Bob Ambrogi)", type: press, url: "https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html", date: "2026-10-15", access: full, locator: "What Microsoft Announced" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: "State Bar of California, COPRAC", type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Agentic AI; Confidentiality" }
  last_reviewed: 2026-10-19
  notes: "Announcements, not deployments. LawSites reports the Anthropic engagement statement as Anthropic's; the statement has no stated basis."
```

## 3. Module notes

**Processes and key steps (with work types)**
- Brief and set up: load documents or precedents into a controlled workspace; choose playbook, template or workflow (document-production, coordination-scheduling).
- First draft: clause, memo, brief or agreement drafted from precedents and approved standards (document-production).
- Synthesis: research answers, summaries, chronologies, issue lists, diligence abstracts (research-synthesis).
- Review against standards: playbook-based contract review, redlining, consistency checks on long reports (review-assurance).
- Extraction: clauses and fields to tables, document Q&A, data mapping (data-reporting).
- Verify and release: citation and quote checking, supervising lawyer sign-off, client disclosure where required (review-assurance).

**Common pain points**
- Firms cannot yet show matter-level savings. Firm-side answers were "still gathering the data" and ROI measurement rested on conventional wisdom (TRI-LEGALWEEK-2026).
- Pilots without a workflow owner or agreed measure of success (Legal Geek recap: "directionless" pilots; LEGALIT-LEGALGEEK-2026).
- Tools in use are often not deployed: among firms using or exploring Microsoft 365 Copilot only 19% had fully rolled it out to lawyers; Harvey and others remain largely in pilot (LEGALIT-LEGALGEEK-2026, citing the ILTA 2026 survey).
- Multi-clause extraction and multi-jurisdiction research are weak spots (VALS-VLAIR-2025, VALS-VLAIRRES-2025).

**Metrics and benchmarks (with sources)**
- Vals Feb 2025: document Q&A lawyer baseline 70.1%, Harvey Assistant 94.8%, CoCounsel 89.6%; redlining lawyer baseline 79.7%, Harvey Assistant 59.4% (VALS-VLAIR-2025). Vals Oct 2025 research: AI products 74-78% against lawyers 69% on 200 questions (VALS-VLAIRRES-2025).
- Microsoft Legal Agent: more than 1,800 users, nearly 100,000 edits, roughly seven in ten suggestions kept, and internal fluency, conciseness and relevance scores above 90%, 95% and 85% (MSFT-COPILOTLEGAL-2026, vendor-published, no independent benchmark per LAWSITES-MSFT-2026).
- Patent drafting trial: +0.34 SD at 10 days, +0.38 SD at 90 days (NBER-AUTOR-2026).
- Stanford 2024: 17%-33% hallucination in two research tools (STANFORD-MAGESH-2024). Court decisions on hallucinated content: 2,202 by 2026-10-19 (CHARLOTIN-HALLUCINATIONS-2026).
- RSGI (Harvey-commissioned, 87 respondents, April-June 2026): power users at law firms save an average of 11 hours a week, up from 8.5; 89% of law firms say they can take on more work; 59% of firms able to track changes report higher lawyer utilisation; 68% of firms and in-house teams deploy Harvey-based agents (LEGALIT-RSGI-2026; self-reported survey).
- Adoption counts, not quality: CMS 95% active use among 3,000+ lawyers, scaled to 7,200 (HARVEY-CMS-2026); Reed Smith 1,400 monthly users out of about 1,800 lawyers (HARVEY-REEDSMITH-2026); Crowell 91% of 700+ attorneys users, nearly 70% weekly (LEGORA-CROWELL-2026, date not confirmed); ILTA 94% of firms engaged (ILTA-TECHSURVEY-2026).
- TR's Steven Petrie, per TRI: firms with a GenAI strategy are 3.9 times more likely to achieve ROI; only 22% have one (TRI-LEGALWEEK-2026).
- Vendor headline stats on pages without method: Harvey customers page (92% monthly adoption, 25+ hours saved per typical user per month; HARVEY-CUSTOMERS-2026) and Legora customers page (labels without stated basis; LEGORA-CUSTOMERS-2026). Treat as vendor claims.

**Guardrails and regulatory points**
- Cal Bar 2026 guidance (replaces 2023 text; adds agentic AI at the California Supreme Court's request): supervise AI at a level that scales with autonomy; do not let agentic systems make substantive legal determinations, give advice, or file pleadings without meaningful lawyer supervision; review all AI output including citations before court submission (CALBAR-GENAI-2026, pp. 2, 8 and Candor to the Tribunal).
- ILTA policy gap by size: formal policy 57% (under 50 lawyers) versus 91%-98% in larger firms; training required before use 11% versus 72% (ILTA-TECHSURVEY-2026, p. 5).
- Client data location can be a condition of adoption (Deutsche Telekom: encrypted, stored in Germany; HARVEY-DTGLEISS-2026).
- Disclosure: Deloitte Australia's revised report disclosed generative AI use after errors were found (CTV-DELOITTE-2025).

**Frontier signals (dated, sourced)**
- 2026-10-15: Harvey launches Legal Work Orchestration and says it expects agents to take on an additional 20% of workflow steps within six months (a forecast) (HARVEY-ORCH-2026).
- 2026-10-15: Microsoft makes Copilot for Legal generally available, 20+ skills, partner plugins including Harvey and Legora (MSFT-COPILOTLEGAL-2026; LAWSITES-MSFT-2026).
- 2026-10-16: Hogan Lovells Cadwalader announces both Legora (global rollout after 1,300+ lawyer pilot) and Harvey (LEGORA-HLC-2026; HARVEY-HLC-2026), a multi-vendor pattern.
- 2026-10-15: Legal Geek recap says progression is "chatbot to workflow to delegated task"; consumption-based pricing is pushing firms to be selective (LEGALIT-LEGALGEEK-2026).
- 2026-09-17: OpenAI's Astra for Law with a Trusted Access programme for Am Law 200 firms (LAWSITES-OPENAI-2026). 2026-05-12: Anthropic's legal plugins and connectors (LAWSITES-ANTHROPIC-2026).
- 2026-09-08 and 2026-06-12: Harvey publishes agent benchmarks for diligence and in-house contracting; the contracting benchmark scores all-or-nothing per task (HARVEY-RLM-2026; HARVEY-LABCONTRACT-2026).
- 2026-05: Cal Bar adds agentic AI guidance (CALBAR-GENAI-2026).

**Workforce and role effects**
- New roles: legal engineers at vendors (34 and 54 postings by title match on 2026-10-19) and at firms (PwC Legal Brussels, a London law firm) (HARVEY-JOBS-2026; LEGORA-JOBS-2026; PWC-LEGALJOB-2026; RW-LEGALENGINEER-2026).
- Hiring criteria: RSGI reports 82% of law firms and 94% of in-house teams are changing hiring criteria to prioritise AI skills; 23% of firms have added AI competency to partner appraisals; 69% of firms are not planning to reduce graduate intake over two years (LEGALIT-RSGI-2026; vendor-commissioned).
- Juniors: NBER finds durable skill gain concentrated in seniors (NBER-AUTOR-2026); Blank Rome and Reed Smith frame the response as training and certification, not cuts (HARVEY-BLANKROME-2026; HARVEY-REEDSMITH-2026).
- Partners: Reed Smith partners are reported to tell teams they cannot work on their matters without AI (HARVEY-REEDSMITH-2026; vendor-published).

**Objections and concerns practitioners raise**
- Clients ask for proof of savings, and some will not pay for AI-done work (TRI-LEGALWEEK-2026).
- Almost half of in-house teams mandated AI at their law firms, but only one reported receiving savings (LEGALIT-RSGI-2026).
- Hallucinated authority and fabricated references (STANFORD-MAGESH-2024; CHARLOTIN-HALLUCINATIONS-2026; CTV-DELOITTE-2025).
- Skill erosion for juniors (NBER-AUTOR-2026).
- Build-versus-buy and platform dependence: the Legal Geek recap cites cross-industry research that bought specialist tools succeed about twice as often as internal builds (LEGALIT-LEGALGEEK-2026; secondary).

**Interview probes for an advisor**
1. Which document types and playbooks do you review or draft most, and which of them are written down well enough for a tool to apply?
2. What fraction of AI suggestions or drafts do your lawyers keep, edit or reject, and does anyone measure it?
3. Where does your verification step sit (citations, quotes, extracted fields), who owns it, and what happened the last time it caught something?
4. Who builds and maintains your playbooks, templates and agents, and are they released from billable or fee-earning work to do it?
5. How do you tell clients (or the business, if in-house) what AI did on a matter, and have they asked for savings you could not show?

## 4. Routed to other modules

- **delivery-management**: Harvey Legal Work Orchestration task, status and review-gate mechanics (HARVEY-ORCH-2026); Certinia PMO Quality, Project Manager and Sales-to-Delivery Handoff agents (CERTINIA-VEDA-2026).
- **pursuit-proposals / scoping-pricing**: Certinia RFP Responder and SOW Drafter agents (CERTINIA-VEDA-2026).
- **acceptance-risk**: Harvey Intake and Legora Intake for routing legal requests; Dentsu non-compete checks on new customers (HARVEY-DENTSU-2026).
- **quality-review**: Deloitte Australia reference errors and disclosure (CTV-DELOITTE-2025); the court-decision hallucination database (CHARLOTIN-HALLUCINATIONS-2026); ILTA human-review and verification policy rates (ILTA-TECHSURVEY-2026).
- **billing-collections / scoping-pricing**: clients' demands for AI line items and refusal to pay for AI-done work; Cal Bar billing rules (TRI-LEGALWEEK-2026; CALBAR-GENAI-2026).
- **talent-learning**: MinterEllison accelerator and legal-engineer cohort (LEGORA-MINTERELLISON-2026); Blank Rome Trial Academy practicums and 300-associate hackathon (HARVEY-BLANKROME-2026); NBER junior-skill findings (NBER-AUTOR-2026).
- **client-relationship-development**: RSGI finding that 61% of law firms proactively discussed Harvey efficiencies with clients while only 4% of in-house teams say their firms approached them (LEGALIT-RSGI-2026); Reed Smith's claim that partners win work through AI-enabled delivery (HARVEY-REEDSMITH-2026).
- **knowledge-management**: Hogan Lovells Cadwalader knowledge-management agents; Harvey Horizon Scanning; Blank Rome brief bank (use cases 16 and 19 touch this).
- **firm-finance**: Harvey Command Center analytics for AI programmes (named on the Harvey platform menu; not read in detail).
- **Assurance and tax archetypes**: EY, KPMG and Deloitte audit-agent announcements and PwC and Legora tax and audit legal-engineer roles appeared in search results and job feeds; audit procedures and tax technical work are not covered here.

## 5. Sources

Types: vendor 25, press 7, academic 6, job-posting 4, survey 2, conference 2, regulator 1 (47 distinct sources, all opened; TRI-LDOR-2026 was read in summary only). Full URLs and locators are in the YAML above for the sources cited there; this list is the complete set opened for the module.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 |
| HARVEY-HLC-2026 | Hogan Lovells Cadwalader adopts Harvey | Harvey | vendor | https://www.harvey.ai/blog/hogan-lovells-cadwalader-adopts-harvey | 2026-10-16 |
| HARVEY-GE-2026 | GE Aerospace deploys Harvey across its Legal & Compliance organization | Harvey | vendor | https://www.harvey.ai/blog/ge-aerospace-deploys-harvey-across-its-legal-and-compliance-organization | 2026-09-01 |
| HARVEY-TCENERGY-2026 | TC Energy deploys Harvey across its legal team | Harvey | vendor | https://www.harvey.ai/blog/tc-energy-deploys-harvey-across-its-legal-team | 2026-10-05 |
| HARVEY-CMS-2026 | Turning AI Into a Daily Habit: How CMS Reached 95% Adoption With Harvey | Harvey | vendor | https://www.harvey.ai/customers/cms | 2026-03-25 |
| HARVEY-REEDSMITH-2026 | Designing the Frontier Firm: How Reed Smith is Rewriting the Playbook With Harvey | Harvey | vendor | https://www.harvey.ai/customers/reed-smith | 2026-05-11 |
| HARVEY-BLANKROME-2026 | Developing Lawyers, Not Replacing Them: How Blank Rome Trains the Next Generation With Harvey | Harvey | vendor | https://www.harvey.ai/customers/blank-rome | 2026-08-06 |
| HARVEY-OMELVENY-2026 | O'Melveny & Myers: Expanding the Art of Possible With Harvey | Harvey | vendor | https://www.harvey.ai/customers/omelveny-and-myers | 2026-08-25 |
| HARVEY-DENTSU-2026 | How Dentsu's Legal and Compliance Team Turned Pressure Into Strategic Advantage With Harvey | Harvey | vendor | https://www.harvey.ai/customers/dentsu | 2026-05-06 |
| HARVEY-DTGLEISS-2026 | How Deutsche Telekom and Gleiss Lutz are Setting the Direction for Legal Collaboration With Harvey | Harvey | vendor | https://www.harvey.ai/customers/deutsche-telekom-gleiss-lutz-collaboration | 2026-02-23 |
| HARVEY-SHAREDSPACES-2026 | A New Era of Collaboration for Legal and Professional Services | Harvey | vendor | https://www.harvey.ai/blog/a-new-era-of-collaboration-for-legal-and-professional-services | 2026-02-19 |
| HARVEY-LABDD-2026 | Extending Legal Agent Bench to M&A Due Diligence | Harvey | vendor | https://www.harvey.ai/blog/legal-agent-bench-m-and-a-due-diligence | 2026-07-17 |
| HARVEY-RLM-2026 | Post-Training RLM Agents for End-to-End M&A Diligence | Harvey | vendor | https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence | 2026-09-08 |
| HARVEY-LABCONTRACT-2026 | Extending Harvey's Legal Agent Bench to In-House Contracting | Harvey | vendor | https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting | 2026-06-12 |
| HARVEY-CUSTOMERS-2026 | Harvey customers page | Harvey | vendor | https://www.harvey.ai/customers | 2026-10 (undated page, date read) |
| LEGORA-HLC-2026 | Hogan Lovells Cadwalader rolls out Legora globally | Legora | vendor | https://legora.com/newsroom/hogan-lovells-cadwalader-rolls-out-legora-globally | 2026-10-16 |
| LEGORA-MINTERELLISON-2026 | How MinterEllison is investing in its people to build AI capability and transform legal delivery | Legora | vendor | https://legora.com/customers/minterellison | 2026 (date unconfirmed) |
| LEGORA-GRANTTHORNTON-2026 | How Grant Thornton UK is delivering sharp client insights in high-stakes forensic work | Legora | vendor | https://legora.com/customers/grant-thornton | 2026 (date unconfirmed) |
| LEGORA-GOODWIN-2025 | Goodwin rolls out Legora firmwide | Legora | vendor | https://legora.com/customers/goodwin | 2025 (date unconfirmed) |
| LEGORA-CROWELL-2026 | Crowell & Moring shares results from firmwide Legora integration | Legora | vendor | https://legora.com/customers/crowell | 2026 (date unconfirmed; text says six months after a January 2026 launch) |
| LEGORA-DKSH-2026 | DKSH selects Legora | Legora | vendor | https://legora.com/customers/dksh | 2026 (date unconfirmed) |
| LEGORA-CUSTOMERS-2026 | Legora customers | Legora | vendor | https://legora.com/customers | 2026-10 (undated page, date read) |
| MSFT-LEGALAGENT-2026 | Word Legal Agent in Frontier | Microsoft Tech Community | vendor | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/word-legal-agent-in-frontier/4516218 | 2026-04-30 |
| MSFT-COPILOTLEGAL-2026 | Introducing Microsoft Copilot for Legal | Microsoft Tech Community | vendor | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-microsoft-copilot-for-legal/4564246 | 2026-10-15 |
| CERTINIA-VEDA-2026 | Certinia AI and Veda agents | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 (undated page, date read) |
| LAWSITES-MSFT-2026 | Microsoft Launches Copilot for Legal... | LawSites | press | https://www.lawnext.com/2026/10/microsoft-launches-copilot-for-legal-becoming-the-fourth-ai-giant-in-five-months-to-build-out-a-legal-vertical.html | 2026-10-15 |
| LAWSITES-ANTHROPIC-2026 | Anthropic Goes All-In on Legal... | LawSites | press | https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html | 2026-05-12 |
| LAWSITES-OPENAI-2026 | OpenAI Releases Astra for Law... | LawSites | press | https://www.lawnext.com/2026/09/openai-releases-astra-for-law-a-gpt-6-model-configured-for-legal-work.html | 2026-09-17 |
| LEGALIT-RSGI-2026 | RSGI's second Harvey report shows jump in adoption | Legal IT Insider | press | https://legaltechnology.com/rsgis-second-harvey-report-shows-jump-in-adoption/ | 2026-06-17 |
| LEGALIT-BMW-2026 | BMW Group to roll out Legora across its legal department | Legal IT Insider | press | https://legaltechnology.com/bmw-group-to-roll-out-legora-across-its-legal-department/ | 2026-10-08 |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors | AP via CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 |
| AT-PWC-AGENTOS-2025 | PwC announces Agent OS for coordinating AI agents | Accounting Today | press | https://www.accountingtoday.com/news/pwc-announces-agent-os-for-coordinating-ai-agents | 2025-03-27 |
| LEGALIT-LEGALGEEK-2026 | Legal Geek: Buy, Build, Bin - what legal is really doing with AI | Legal IT Insider | conference | https://legaltechnology.com/legal-geek-buy-build-bin-what-legal-is-really-doing-with-ai/ | 2026-10-15 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026 | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 (PDF creation date) |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 executive summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 |
| TRI-LDOR-2026 | 2026 Legal Department Operations Report (summary page only) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026 | 2026-09-22 |
| VALS-VLAIR-2025 | Vals Legal AI Report | Vals AI | academic | https://www.vals.ai/industry-reports/vlair-2-27-25 | 2025-02-27 |
| VALS-VLAIRRES-2025 | VLAIR - Legal Research | Vals AI | academic | https://www.vals.ai/industry-reports/vlair-10-14-25 | 2025-10-14 (from URL) |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Stanford RegLab/HAI (arXiv) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? (NBER WP 35720) | NBER | academic | https://www.nber.org/papers/w35720 | 2026-09 |
| HBS-DELLACQUA-2023 | Navigating the Jagged Technological Frontier (HBS WP 24-013) | Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 |
| CHARLOTIN-HALLUCINATIONS-2026 | AI Hallucination Cases Database | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-19 |
| HARVEY-JOBS-2026 | Legal Engineer (Law Firm, Corporate), Harvey job board | Harvey (Ashby) | job-posting | https://jobs.ashbyhq.com/harvey/c3b9e500-dc27-4afe-9b8a-31223c6b18fe | 2026-06-17 |
| LEGORA-JOBS-2026 | Legal Engineer (Accounting) and Legal Engineer - Tax & Consulting, Legora job board | Legora (Ashby) | job-posting | https://jobs.ashbyhq.com/legora/57ec5894-05b4-4fc7-b4b1-a6892d813134 | 2026-10-15 |
| PWC-LEGALJOB-2026 | Legal Engineer - AI-Enabled Legal Delivery | PwC (Global Legal) via LegalAlphabet | job-posting | https://legalalphabet.com/job/legal-engineer-ai-enabled-legal-delivery-senior-associate-manager-job-at-pwc-global-legal-in-brussels | 2026-09-16 |
| RW-LEGALENGINEER-2026 | Legal Engineer lawyer - leading global law firm | Robert Walters | job-posting | https://www.robertwalters.co.uk/legal/jobs/in-housegeneralist/1910788-legal-engineer-lawyer---leading-global-law-firm.html | 2026-09-09 |

Note on refs: `LEGORA-CROWELL-2026`, `LEGORA-DKSH-2026`, `HARVEY-CUSTOMERS-2026`, `LEGORA-CUSTOMERS-2026`, `TRI-LDOR-2026` and `HARVEY-LABCONTRACT-2026` appear in the notes and this list, not in a use-case `sources` block, because they support context statements rather than a use-case claim.

## 6. Gaps

- **Consulting primary sources.** McKinsey (403 on both direct and mirror), BCG, Bain, Deloitte, EY and KPMG pages gave no usable account of internal work-production use. McKinsey's Lilli figures appeared only in search snippets (aggregator sites, conflicting numbers) and were not used.
- **No firm-published quality data.** No error rate, override rate, parallel-run result or inspection finding on firm-deployed AI drafting or review was found. The measured evidence is Vals (external benchmark), NBER (trial), Stanford (2024), Microsoft telemetry (vendor), and the court-decision database. Vendor case studies give adoption counts and testimonials.
- **Vendor-hosted case studies.** Almost all named firm and in-house examples sit on Harvey or Legora pages and are vendor-published; no independently reported firm result beyond Reuters Institute conference coverage, Legal IT Insider and LawSites reporting.
- **Dates.** Legora customer pages show a "joined" month, not a publication date, and the labels conflict with other facts on the pages (for example DKSH). Dates for MinterEllison, Grant Thornton, Goodwin, Crowell and DKSH are therefore given as a year, flagged as unconfirmed. The extra web search needed to date the Crowell release could not run because the shared search budget was used up. The Vals research report date comes from its URL. The Cal Bar PDF date is its file creation date. Microsoft's Legal Agent post date comes from page metadata.
- **Access.** Harvey and Legora posts were read in full; the Fortune McKinsey article was blocked by the mirror; one Legal IT Insider article on Hogan Lovells Cadwalader's firmwide strategy returned a bot check; Orange Rag GC insights were not read; NBER PDF was blocked (abstract page read).
- **Hogan Lovells Cadwalader.** The two same-day announcements (Legora and Harvey) do not say how work is split between the platforms.
- **Thin areas.** Accounting and advisory firms' non-audit, non-tax drafting; in-house teams outside legal; small and mid-size firm results; independent measurement of agentic (multi-step) work production in real matters.
- **Not read.** TRI Legal Department Operations Report beyond its summary page; ILTA full survey (members only); RSGI full report (only Legal IT Insider's summary); Harvey's "Understanding a Law Firm through Study" and LAB law-firm-knowledge posts.
