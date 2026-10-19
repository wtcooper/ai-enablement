# Professional services, pursuit-proposals: discourse angle

Prepared 2026-10-19. Archetype: professional-services. Module: pursuit-proposals (RFP and RFI responses, proposals, pitches, credentials, win/loss analysis). Angle: discourse (what practitioners are saying: conference sessions, podcasts, practitioner articles, community and newsletter commentary, from roughly the last 12-18 months).

Method: `curl` for pages, the `r.jina.ai` text mirror where `curl` was blocked (ABA Law Practice, UpperEdge, LMA and Stanford session pages), the podcast RSS feed for Passle's CMO Series, and the Crossref API for the abstract of one journal article. 37 distinct sources are listed; 36 were opened and 1 was seen only in search results. 22 web searches were used (the brief's ration was not stated as a number; see Gaps). Public sources only. The working files stayed in a private `mktemp -d` folder.

---

## 1. Summary

- **The conversation has moved from "can we use AI on bids" to "what do we do with the time, and can we trust the data".** Practitioners in the ABA's Law Practice magazine, SMPS programmes, an LMA26 session and a firm's op-ed repeat one point: use the time saved to tailor to the client, not to send more generic bids (STINSON-LAW360-2026; NYREJ-SMPSNY-2026; LMA-DECENT-2026). The one law-firm RFP story in the window with a clear outcome is a Litera CEO's account of sending an RFP to three firms. The firm that cited relevant matters, matched lawyers to the work and grounded price in comparable engagements was hired (LAWSITES-LITERA-2026; sponsored post, one anecdote).
- **Finding the firm's own experience data is described as the bottleneck, not writing.** In ikaun's July 2026 survey of Am Law 100/200 and NLJ 500 marketing, BD and proposal leaders, finding experience and matter data ranked first among the stages that consume time, ahead of writing; 74% said they have no single current source of truth for matter experience, and only 27% of firms actively use AI in proposals (IKAUN-BENCH-2026; vendor-published, sample size not stated). Unanet's AEC benchmark reports that only 29% of firms have high confidence in the data feeding their AI tools (BDC-UNANET-2026). Several practitioners and vendors therefore push data reconciliation and a governed library before drafting tools (KANTIV-TRUST-2026; IKAUN-BENCH-2026).
- **More bids, flat or falling win rates.** Unanet reports 71% of AEC respondents submitting more proposals than the year before, with win rates of 56% (2024), 52% (2025) and 50% (2026) (BDC-UNANET-2026). ikaun reports 69% of law firms saying proposal volume rose and none saying it fell (IKAUN-BENCH-2026). No source in this angle shows AI raising win rates.
- **Buyers are using AI to read proposals too.** The ABA's July 2026 article, a Wolters Kluwer piece, and an advisory firm's August 2026 article all describe buyers using AI to summarise and compare submissions (ABA-LPMRFP-2026; TGC-WK-2025; UPPEREDGE-PROPTRAP-2026). The only independent measurement found is a 2026 journal study of AI scoring of 123 government IT supplier bids: AI matched people on compliance checks but was volatile on value-add claims (JBL-MCKINLEY-2026). It is adjacent to professional-services pursuit, so it caps related grades below A.
- **RFPs now ask firms about their own AI use, and practitioners disagree on how to answer.** The ABA lists five question categories now appearing in RFPs (ABA-LPMRFP-2026). A Parker Poe interview hosted by Thomson Reuters advises buyers to ask for a matter-level description of tool, workflow, human review and guardrails (PARKERPOE-TR-2026). A Litera survey post says clients want metrics and proof (LAWSITES-LITERA-2026).
- **Evidence quality is weak.** Of the 16 use cases, 4 are grade B (named firms describing deployments at a conference panel), 8 are C and 4 are D ideas. None reaches A. No error rate, override rate, parallel run, inspection result or independent win-rate study was found for any pursuit use case.

Use cases: 16 (grade A: 0, B: 4, C: 8, D: 4).

---

## 2. Use cases

```yaml
- id: professional-services-pursuit-proposals-01
  title: Chat and tagging over a firm-wide archive of past RFPs
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [research-synthesis, document-production]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    In a large law firm, RFPs differ by client, practice area and office, so there is little standardisation and no easy way
    to pull useful data out of any one response. Partners and marketing teams re-find old answers by hand.
  solution: >-
    Ballard Spahr's technology team built "X-Ray" on Microsoft cloud and generative AI. It is a repository of RFP documents
    (up to 2,000 per instance) with a chat feature so users can ask questions of the documents. Tagging lets people find
    relevant documents and reuse newly written ones across the firm. The IP group, the firm's smallest department, wanted to
    keep control of its own RFPs rather than route them through Marketing, and the tool gave it access to firm-wide knowledge.
    Other practice groups then asked for the same.
  outcomes:
    - lever: speed
      description: >-
        Ballard Spahr's senior director of technology innovation said partners estimate they save about two hours per RFP
        because of the tagging. This is an estimate relayed at a conference panel, not a tracked measure.
      figure: "about 2 hours saved per RFP (partner estimate)"
      measures: >-
        Hours per RFP that partners estimate they save, as stated by Lisa Mayo Haynes, senior director of technology
        innovation at Ballard Spahr; no baseline method or sample is given.
      provenance: self-reported
      source_ref: TRI-INSIDELEGALAI-2025
    - lever: growth
      description: >-
        The same speaker said the IP department is the firm's smallest but had the highest win rate on RFPs. The article does
        not say AI caused this, and gives no win-rate figure.
      figure: "none published"
      measures: "Not applicable: a ranking statement only, with no number given."
      provenance: self-reported
      source_ref: TRI-INSIDELEGALAI-2025
  prerequisites:
    - A consolidated set of past RFP documents that people are willing to share across practices.
    - A tagging scheme owned by someone in marketing or knowledge management.
    - A tool run in the firm's own cloud environment; the article's key insights say proprietary tools such as X-Ray and Ask Ellis give insight into data while addressing privacy concerns.
  risks_and_guardrails:
    - Privacy is handled by building proprietary tools rather than using open public ones (TRI-INSIDELEGALAI-2025, key insights and Use case 2 section).
    - ikaun's survey says 74% of firms have no single current source of truth for matter experience, so a repository is only as reliable as what is loaded into it (IKAUN-BENCH-2026).
  human_checkpoints:
    - Practice groups and lawyers decide what to reuse and edit the response for the client.
  role_evolution: >-
    A practice group (IP) took more ownership of its own RFP responses while still drawing on firm-wide knowledge
    (TRI-INSIDELEGALAI-2025). The article does not describe changes to marketing roles.
  evidence_grade: B
  sources:
    - { ref: TRI-INSIDELEGALAI-2025, title: "Beyond legal practice: How GenAI is transforming law firm business operations", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en-us/posts/technology/inside-legal-ai-genai-transformation/", date: "2025-12-15", access: full, locator: "Use case 1: RFP repository" }
    - { ref: IKAUN-BENCH-2026, title: "ikaun Releases The State of Winning Work in Law Firms: A 2026 Benchmark Report", publisher: ikaun, type: survey, url: "https://www.ikaun.com/news/ikaun-releases-the-state-of-winning-work-in-law-firms-a-2026-benchmark-report", date: "2026-07-14", access: full, locator: "paragraphs 3-5" }
  last_reviewed: 2026-10-19
  notes: >-
    Reported by a Thomson Reuters Institute writer from a panel at the Inside Legal AI conference moderated by Nexl's chief
    revenue officer. The panel gave no date for when X-Ray went live. The partner time saving is an estimate, so the grade is B.

- id: professional-services-pursuit-proposals-02
  title: Reconcile duplicate and stale people and project records before AI retrieval
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [data-reporting, research-synthesis]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    The same person, project or client appears under different names and dates across resumes, case studies and
    qualification forms. A retrieval tool then returns stale or duplicate records, such as the resume of someone who has
    left. In US federal AEC work, an invented project citation on a qualification form can disqualify a bid.
  solution: >-
    Before retrieval, extract roles, timelines and costs from each document, match records that describe the same real-world
    person, project or client (exact match first, then similarity search, then a second AI pass that gives a verdict and a
    confidence score), and check against the firm's systems of record. Thresholds are set separately for people, projects and
    clients. Staff can merge, split or correct any record, and a detail a person has verified is not overwritten.
  outcomes:
    - lever: risk
      description: >-
        The vendor says one large contractor group used its platform on a bid that had already been disqualified and it caught
        a disqualifying issue the team had missed. The customer is not named and no count is given.
      figure: "none published"
      measures: "A single unnamed-customer anecdote told by the vendor; no numerator or denominator."
      provenance: vendor-published
      source_ref: KANTIV-TRUST-2026
  prerequisites:
    - Access to the firm's proposals, resumes, case studies and the systems of record (the vendor names Deltek, Vantagepoint, Unanet and a CRM).
    - Named owners who will resolve disputed records.
  risks_and_guardrails:
    - The vendor states that every large-language-model system can hallucinate, and positions its tool as "a first-draft accelerator, not a final-product generator" (KANTIV-TRUST-2026, hallucination section).
    - Wrongly merging two people is treated as worse than leaving two records apart, which is why thresholds differ by record type (KANTIV-TRUST-2026).
    - Only 29% of AEC firms report high confidence in the data underneath their AI tools (BDC-UNANET-2026, data paragraph).
  human_checkpoints:
    - Staff review and correct merges and splits; verified details are locked.
    - A human reviews every draft before it goes out.
  role_evolution: >-
    The source does not describe role changes; it implies pursuit staff move from searching for records to correcting them.
  evidence_grade: C
  sources:
    - { ref: KANTIV-TRUST-2026, title: "What's Under the Slab: How AI Trust Actually Gets Built in AEC", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/ai-trust-ai-proposal-software-for-aec", date: "2026-07-21", access: full, locator: "sections on hallucination and reconciliation" }
    - { ref: BDC-UNANET-2026, title: "AEC report reveals firms are in the throes of AI transition", publisher: Building Design + Construction (by Unanet), type: survey, url: "https://www.bdcnetwork.com/aec-tech/news/55386606/aec-report-reveals-firms-are-in-the-throes-of-ai-transition", date: "2026-06-25", access: full, locator: "data confidence paragraph" }
    - { ref: IKAUN-BENCH-2026, title: "ikaun Releases The State of Winning Work in Law Firms: A 2026 Benchmark Report", publisher: ikaun, type: survey, url: "https://www.ikaun.com/news/ikaun-releases-the-state-of-winning-work-in-law-firms-a-2026-benchmark-report", date: "2026-07-14", access: full, locator: "paragraph 4" }
  last_reviewed: 2026-10-19
  notes: >-
    Vendor blog describing its own product, with quotes attributed to unnamed customers (for example a CIO at a large A/E firm
    complaining that AI picks resumes of people who no longer work there). Maturity is "announced" because no customer is
    named.

- id: professional-services-pursuit-proposals-03
  title: Client and prospect research brief with a needs score for pitch preparation
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [research-synthesis, client-interaction]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Preparing to talk to a client or prospect meant hours of gathering documents and data, and lawyers started conversations
    with less authority than they could have had.
  solution: >-
    Baker Botts's data science team built a tool inside Google's environment using Gemini. It combines public information,
    financial data and proprietary firm information to produce background on a client and a low, medium or high score for the
    client's or prospect's anticipated legal needs in a given practice area. Business developers and lawyers run the search
    themselves.
  outcomes:
    - lever: speed
      description: >-
        Baker Botts's associate director for competitive intelligence, data science and analytics said the preparation work
        previously took 24 hours of research and that the team's first task was to use generative AI to cut that by more
        than half. She said users get a readout with a score after about two minutes of querying.
      figure: "24 hours of research cut by more than half; readout in about 2 minutes"
      measures: >-
        Hours of research to prepare, as recalled by Lynne Kilgore (Baker Botts) at a conference panel; the article does not say
        what the 24 hours covered precisely or how the later figure was measured.
      provenance: self-reported
      source_ref: TRI-INSIDELEGALAI-2025
  prerequisites:
    - A data science or competitive-intelligence team able to join public, financial and internal firm data.
    - Access to firm proprietary information inside a secured environment.
  risks_and_guardrails:
    - The needs score is a model output; the article gives no accuracy check on the score.
  human_checkpoints:
    - The lawyer or business developer reads the readout and decides how to use it in the conversation.
  role_evolution: >-
    Lawyers and business developers can run the search themselves, which moves some research from specialists to the
    pursuit team (TRI-INSIDELEGALAI-2025). The article does not describe job changes.
  evidence_grade: B
  sources:
    - { ref: TRI-INSIDELEGALAI-2025, title: "Beyond legal practice: How GenAI is transforming law firm business operations", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en-us/posts/technology/inside-legal-ai-genai-transformation/", date: "2025-12-15", access: full, locator: "Use case 3: Opportunity spotting" }
    - { ref: LMA-DECENT-2026, title: "From Decent to Great: How to Develop a Compelling Proposal Response", publisher: Legal Marketing Association, type: conference, url: "https://www.legalmarketing.org/Purchase/from-decent-to-great-how-to-develop-a-compelling-proposal-response-mch", date: "2026-05-01", access: full, locator: "session description and learning outcomes" }
  last_reviewed: 2026-10-19
  notes: >-
    The article is ambiguous about whether the 24-hour preparation work was for onboarding a new attorney or for client
    preparation; the wording above stays with what the article states. The LMA26 session abstract supports the discourse
    point that AI should be used as a fact-finding tool without losing the human narrative; it does not describe a deployment.
    Overlaps with client-development (prospect needs scoring).

- id: professional-services-pursuit-proposals-04
  title: Regenerate attorney and expert bios from time records, knowledge systems and public sites
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Baker Botts's COO searched the web for the best lawyers in Houston and found the firm listed alongside attorneys who had
    retired from it more than five years earlier. Generic bios also did not surface well in search.
  solution: >-
    The data science team built a tool, using secure and vetted AI tools, that draws on lawyer time sheets, the Foundation
    knowledge management platform and public websites to build a fuller picture of what each lawyer actually does. The
    team set guardrails and asked the tool to optimise the output for answer engines.
  outcomes:
    - lever: quality
      description: >-
        The speaker said the firm went from "really generic bios" to bios more likely to be picked up through answer engine
        optimisation. No measurement of search or answer-engine visibility is reported.
      figure: "none published"
      measures: "Qualitative statement by Lynne Kilgore (Baker Botts); no measure of how often bios are surfaced."
      provenance: self-reported
      source_ref: TRI-INSIDELEGALAI-2025
  prerequisites:
    - Time-sheet data, a knowledge management platform and a current lawyer roster.
    - Guardrails agreed with the firm, which the article does not detail.
  risks_and_guardrails:
    - The ABA column warns that compiled bios must not pull out-of-date information and that awards and success stories must be verified (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
    - The article does not say who approves a generated bio; this is a question to ask.
  role_evolution: "The article does not describe role changes."
  evidence_grade: B
  sources:
    - { ref: TRI-INSIDELEGALAI-2025, title: "Beyond legal practice: How GenAI is transforming law firm business operations", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en-us/posts/technology/inside-legal-ai-genai-transformation/", date: "2025-12-15", access: full, locator: "Use case 4: Website bio generation" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "Cautions" }
  last_reviewed: 2026-10-19
  notes: "Reported at a conference panel; the bio system serves the website and search visibility, and is also the credential feed for pitches. The visibility goal overlaps client-development."

- id: professional-services-pursuit-proposals-05
  title: First-draft proposals from prior submissions, tailored by lawyers
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Proposal volume is rising and teams are small and time-boxed. Responses are still mostly built in Microsoft Word from
    scattered content.
  solution: >-
    Tools review prior submissions, extract relevant experience and language, and assemble a structured starting draft that
    lawyers refine for the client. The ABA's marketing column says the draft can prioritise content from proposals that won over
    those that lost. Practitioners say the time saved should go into understanding the client and tailoring.
  outcomes:
    - lever: capacity
      description: >-
        The ABA article, citing the 2025 Responsive and APMP report, says some organisations have reduced 30-40 percent of
        the manual effort of preparing proposals so teams can pursue more opportunities without more staff. The ABA article
        does not give the sample or definition.
      figure: "30-40% of manual proposal effort reduced (some organisations)"
      measures: >-
        Share of manual effort in preparing proposals that "some organizations" report having reduced, as relayed by the ABA from
        the Responsive/APMP 2025 report; the denominator and respondent count for this item are not given.
      provenance: vendor-published
      source_ref: ABA-LPMRFP-2026
    - lever: speed
      description: >-
        ikaun's July 2026 survey of senior marketing, BD and proposal leaders at Am Law 100, Am Law 200 and NLJ 500 firms
        found only 27% of firms actively using AI in proposals, concentrated on drafting and rewriting.
      figure: "27% of firms"
      measures: >-
        Share of surveyed law firms that are "actively using AI in proposals today"; sample size not stated in the release.
      provenance: vendor-published
      source_ref: IKAUN-BENCH-2026
  prerequisites:
    - A current, searchable record of past submissions and experience (the ikaun release concludes firms need this first).
    - A secure tool that does not train on firm inputs.
  risks_and_guardrails:
    - Do not draft RFP responses in public language models that train on the data entered (ABA-LPMAI-2026, Cautions).
    - Check every word, including success stories, awards and bios (ABA-LPMAI-2026, Cautions).
    - Past-win data can skew toward low-profit work, so the firm should know when to ignore it (ABA-LPMAI-2026, Cautions).
    - Selection committees are said to recognise generic AI output; a Kantiv summary of the SMPS Foundation Q2 2026 report calls this the "AI slop" backlash (KANTIV-SMPSQ2-2026, secondary).
  human_checkpoints:
    - Lawyers tailor strategy and nuance; the ABA column advises disclosing AI assistance and making clear it was overseen.
    - Final draft is checked so it is more than AI boilerplate (ABA-LPMAI-2026, Cautions).
  role_evolution: >-
    Stinson partners argue the saved time should be reinvested in understanding the client and developing a tailored
    proposal (STINSON-LAW360-2026). The NYREJ account of an SMPS New York programme says AI streamlines compliance review,
    outlining and copy editing so proposal professionals can focus on higher-value work (NYREJ-SMPSNY-2026).
  evidence_grade: C
  sources:
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "section 'How Law Firms Are Using AI in RFP Responses'" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 3 and Cautions" }
    - { ref: IKAUN-BENCH-2026, title: "ikaun Releases The State of Winning Work in Law Firms: A 2026 Benchmark Report", publisher: ikaun, type: survey, url: "https://www.ikaun.com/news/ikaun-releases-the-state-of-winning-work-in-law-firms-a-2026-benchmark-report", date: "2026-07-14", access: full, locator: "paragraphs 2, 5" }
    - { ref: STINSON-LAW360-2026, title: "Scheck and Valdivia Examine How AI Is Reshaping Law Firm RFPs in Law360", publisher: Stinson LLP, type: firm, url: "https://www.stinson.com/newsroom-news-scheck-and-valdivia-examine-how-ai-is-reshaping-law-firm-rfps-in-law360", date: "2026-09-11", access: full, locator: "second paragraph" }
    - { ref: NYREJ-SMPSNY-2026, title: "SMPS NY hosts 'Humans at the Helm: Guiding AI in Proposal Management' virtual program", publisher: New York Real Estate Journal, type: press, url: "https://nyrej.com/smps-ny-hosts-humans-at-the-helm-guiding-ai-in-proposal-management-virtual-program", date: "2026-06-30", access: full, locator: "paragraph 4" }
    - { ref: KANTIV-SMPSQ2-2026, title: "What the SMPS Q2 AI Report Means for AEC Pursuit Teams", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/smps-q2-ai-report", date: "2026-07-13", access: full, locator: "second finding (AI slop)" }
  last_reviewed: 2026-10-19
  notes: >-
    No named deployment is cited in this angle's sources, so maturity is "emerging". The ABA column's claim that AI can
    produce a "70-80% complete first draft in minutes" is an assertion in a marketing column, not a measurement, and is not
    used as an outcome. Named deployments (for example Cherry Bekaert, Gordon Rees Scully Mansukhani) are in the practice-angle
    file, not read here. The SMPS Foundation report itself is members-only and was not seen; Kantiv's summary is secondary.
    The ABA piece also gives illustrative scenarios (a global firm, a mid-sized firm) that are generic examples, not reports of named firms.

- id: professional-services-pursuit-proposals-06
  title: RFP and work-statement review agent that flags restrictive requirements with citations
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Teams can spend weeks on a proposal before learning that requirements favour an incumbent or are otherwise a poor fit.
    Manual reading of long RFPs misses mandatory clauses and small details.
  solution: >-
    An agent reads RFPs and performance work statements and extracts requirements, deadlines and mandatory clauses into a
    matrix. In a government-contracting workshop it also flags requirements tied to a particular vendor's tools,
    certifications or agency experience, unusually specific key-personnel requirements, tight response windows and heavy emphasis
    on transition risk; cites the page or section for each flag; and drafts clarification questions for the capture team.
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable: workshop description and magazine column, no results reported."
      provenance: vendor-published
      source_ref: G2X-CAPTURE-2026
  prerequisites:
    - Digitised RFP and work-statement documents.
    - A capture or bid team that will investigate flags.
  risks_and_guardrails:
    - The workshop states that a red flag is a reason to investigate, not proof that an award is predetermined (G2X-CAPTURE-2026).
    - The agent is built to separate a signal worth investigating from a conclusion the documents do not support (G2X-CAPTURE-2026).
  human_checkpoints:
    - Capture team investigates each flag and decides whether to pursue.
  role_evolution: "Not described beyond capture teams using the output to decide where to spend proposal resources."
  evidence_grade: C
  sources:
    - { ref: G2X-CAPTURE-2026, title: "Capture Agent Build-Along: Is This RFP Wired?", publisher: G2X and ProposalTeam Partners (Luma), type: conference, url: "https://luma.com/xcwn65gt", date: "2026-10-07", access: full, locator: "What you'll build" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 1" }
  last_reviewed: 2026-10-19
  notes: >-
    The workshop was held on 2026-10-07 (the event page is marked past) and is a vendor-led training; no recap or results were
    available. It targets US government contracting, which is adjacent to professional services.

- id: professional-services-pursuit-proposals-07
  title: Go/no-go qualification scored against a firm's own win and loss history
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [expert-judgment, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Most firms say they have a go/no-go step but few follow a formal one, and criteria are rarely tested against what has
    actually separated wins from losses. Volume is rising while win rates fall.
  solution: >-
    Hand past proposals, debriefs and win/loss notes to an AI assistant to produce a first-pass score of 30 to 40 past pursuits
    against the firm's criteria, compute average scores for wins and losses, and reweight criteria by how strongly they separate
    outcomes; people check the output. The ABA column adds a predictive version that compares a new RFP against past performance,
    client history and resource availability.
  outcomes:
    - lever: quality
      description: >-
        Responsive and APMP's 2025 survey of 726 respondents says "Leaders" (over 25% year-on-year revenue growth) were more
        likely than "Novices" to use AI for go/no-go decisions (37% vs 26%). The release does not show that this causes better
        decisions.
      figure: "37% vs 26%"
      measures: >-
        Share of Leaders vs share of Novices that use AI for making go/no-go decisions; respondents were 726 global revenue
        leaders and practitioners across industries (not professional services only).
      provenance: vendor-published
      source_ref: RESPONSIVE-SRM-2025
    - lever: quality
      description: >-
        Unanet's 2026 AEC survey found 92% of firms have some go/no-go process but fewer than half (47%) say they follow a formal one.
      figure: "92% have a process; 47% formal"
      measures: >-
        Share of surveyed AEC firms with "some kind of go/no-go process" and share saying they follow a formal process; sample
        size not given in the article.
      provenance: vendor-published
      source_ref: BDC-UNANET-2026
  prerequisites:
    - A record of 30 to 40 formally pursued opportunities from the last two or three years, including losses, scored on what was known at decision time.
    - Debriefs and win/loss notes in a form an assistant can read.
  risks_and_guardrails:
    - Past-win data can be incomplete or biased toward low-profit work (ABA-LPMAI-2026, Cautions).
    - Thirty pursuits give a firmer starting point, not scientific certainty (KANTIV-GONOGO-2026).
    - Hindsight can inflate the scores of winning pursuits, so score on what was known at the go decision (KANTIV-GONOGO-2026).
  human_checkpoints:
    - People sanity-check the AI's scoring and own the judgement calls (KANTIV-GONOGO-2026).
    - Leadership decides whether a low-probability, high-effort bid is worth the cost; the ABA column gives an illustrative 8% win chance against $35,000 of partner time.
  role_evolution: >-
    Marketing and BD staff become owners of the pursuit dataset and the scorecard; the sources do not describe job-title
    changes.
  evidence_grade: C
  sources:
    - { ref: KANTIV-GONOGO-2026, title: "How to calibrate your go/no-go matrix using your own wins and losses", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix", date: "2026-10-15", access: full, locator: "section on weighting using past pursuits" }
    - { ref: RESPONSIVE-SRM-2025, title: "B2B Revenue Leaders Are Winning Big With AI, And They're Hiring, Not Downsizing (release for the 2025 State of Strategic Response Management Report)", publisher: Responsive with APMP (via Silicon UK), type: survey, url: "https://www.silicon.co.uk/press-release/b2b-revenue-leaders-are-winning-big-with-ai-and-theyre-hiring-not-downsizing", date: "2025-05-08", access: full, locator: "Key findings, third item" }
    - { ref: BDC-UNANET-2026, title: "AEC report reveals firms are in the throes of AI transition", publisher: Building Design + Construction (by Unanet), type: survey, url: "https://www.bdcnetwork.com/aec-tech/news/55386606/aec-report-reveals-firms-are-in-the-throes-of-ai-transition", date: "2026-06-25", access: full, locator: "highlights list" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 4 and Cautions" }
  last_reviewed: 2026-10-19
  notes: >-
    The Kantiv article's table of win and loss scores is a hypothetical example ("say your analysis looks like this") and its
    numbers are not used. The Responsive survey is cross-industry, so the figures are context rather than professional-services
    evidence.

- id: professional-services-pursuit-proposals-08
  title: Win/loss insight mining from proposals, debriefs and client feedback
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [data-reporting, research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Firms judge proposal success by whether they won. Debrief notes, client feedback and past responses sit in separate places,
    so the lessons rarely reach the next bid.
  solution: >-
    Use an assistant to read proposals, debriefs and win/loss notes together and surface what separated wins from losses.
    A 2026 Legal Marketing Association (LMA) session teaches methods to judge proposal success beyond winning (client feedback,
    message resonance, internal alignment) and to use that to improve later responses.
  outcomes:
    - lever: quality
      description: >-
        Responsive and APMP's 2025 survey says Leaders were more likely than Novices to use AI to surface insights from
        win/loss data (37% vs 18%). It is a usage difference, not a result.
      figure: "37% vs 18%"
      measures: >-
        Share of Leaders vs share of Novices that use AI for surfacing insights from win/loss data; 726 global revenue leaders
        and practitioners across industries.
      provenance: vendor-published
      source_ref: RESPONSIVE-SRM-2025
  prerequisites:
    - Debrief and win/loss notes captured consistently.
    - Client feedback programmes (a CMO Series guest argues these matter more as AI levels the expertise playing field).
  risks_and_guardrails:
    - Win/loss notes are recollections; scoring should reflect what was known at the time (KANTIV-GONOGO-2026).
  human_checkpoints:
    - People interpret the pattern and decide what changes in the playbook.
  role_evolution: >-
    LMA's session description speaks of developing team capabilities from proposal learning (LMA-DECENT-2026). No source
    describes job changes.
  evidence_grade: C
  sources:
    - { ref: RESPONSIVE-SRM-2025, title: "B2B Revenue Leaders Are Winning Big With AI, And They're Hiring, Not Downsizing (release for the 2025 State of Strategic Response Management Report)", publisher: Responsive with APMP (via Silicon UK), type: survey, url: "https://www.silicon.co.uk/press-release/b2b-revenue-leaders-are-winning-big-with-ai-and-theyre-hiring-not-downsizing", date: "2025-05-08", access: full, locator: "Key findings, third item" }
    - { ref: LMA-DECENT-2026, title: "From Decent to Great: How to Develop a Compelling Proposal Response", publisher: Legal Marketing Association, type: conference, url: "https://www.legalmarketing.org/Purchase/from-decent-to-great-how-to-develop-a-compelling-proposal-response-mch", date: "2026-05-01", access: full, locator: "learning outcomes, third item" }
    - { ref: PASSLE-EP203-2026, title: "Episode 203 - Roanne Neuwirth on What Separates a Market Position from a Service List", publisher: Passle CMO Series Podcast, type: podcast, url: "https://passle.podbean.com/e/episode-203-roanne-neuwirth-on-what-separates-a-market-position-from-a-service-list/", date: "2026-06-10", access: full, locator: "show notes" }
    - { ref: KANTIV-GONOGO-2026, title: "How to calibrate your go/no-go matrix using your own wins and losses", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix", date: "2026-10-15", access: full, locator: "paragraph after the weighting steps" }
  last_reviewed: 2026-10-19
  notes: >-
    The podcast was read from show notes only; audio was not heard. The LMA source is a session abstract (recordings are
    members' content). No named firm is shown using AI for win/loss. AI-moderated post-pitch interviews are marketed by vendors
    (seen in search only) and are not included here.

- id: professional-services-pursuit-proposals-09
  title: Pre-submission consistency, tone and disqualification-risk review
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Proposals written by several partners across departments read like "Frankenstein" documents. In some formal bids a single
    wrong or invented credential on a standard form is disqualifying.
  solution: >-
    An assistant rewrites sections into a consistent voice and level of formality, checks compliance against requirements,
    and checks grounded claims against source records before submission. Speakers at an SMPS New York programme described AI
    streamlining compliance review, outlining and copy editing.
  outcomes:
    - lever: risk
      description: >-
        The vendor says one customer used its platform on a bid that had already been disqualified and it caught a disqualifying
        issue the team had missed (one anecdote, customer not named).
      figure: "none published"
      measures: "A single unnamed-customer anecdote told by the vendor; no count."
      provenance: vendor-published
      source_ref: KANTIV-TRUST-2026
  prerequisites:
    - Requirements captured as a checklist or matrix.
    - Source records that can verify credentials and project citations.
  risks_and_guardrails:
    - "In an SF-330, one invented project citation can mean disqualification, per the vendor (KANTIV-TRUST-2026)."
    - Check every claim, award and bio (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
    - A person approves the final document; AI cannot replace human interpretation of client expectations, differentiators and authenticity (NYREJ-SMPSNY-2026).
  role_evolution: >-
    SMPS New York presenters encouraged proposal professionals to build skills in strategic thinking, storytelling, quality
    control and creative problem-solving (NYREJ-SMPSNY-2026).
  evidence_grade: C
  sources:
    - { ref: NYREJ-SMPSNY-2026, title: "SMPS NY hosts 'Humans at the Helm: Guiding AI in Proposal Management' virtual program", publisher: New York Real Estate Journal, type: press, url: "https://nyrej.com/smps-ny-hosts-humans-at-the-helm-guiding-ai-in-proposal-management-virtual-program", date: "2026-06-30", access: full, locator: "paragraphs 3-4" }
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 5" }
    - { ref: KANTIV-TRUST-2026, title: "What's Under the Slab: How AI Trust Actually Gets Built in AEC", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/ai-trust-ai-proposal-software-for-aec", date: "2026-07-21", access: full, locator: "hallucination section" }
  last_reviewed: 2026-10-19
  notes: >-
    The SMPS NY programme is a virtual follow-up to a session at the 2026 SMPS Northeast Regional Conference, reported in a
    trade-press item; it contains no figures.

- id: professional-services-pursuit-proposals-10
  title: Buyers read, summarise and compare professional-services proposals with AI (in-house)
  archetype: professional-services
  module: pursuit-proposals
  function: procurement-supply-chain
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Corporate legal departments and enterprise buyers receive long responses with experience, staffing and pricing narratives
    from many firms. Reading and comparing them by hand is slow, and scopes are often unclear enough that bids are not comparable.
  solution: >-
    In-house legal operations teams use AI to summarise and compare submissions, flag pricing outliers and staffing differences,
    structure the matter scope before the RFP is issued, and generate follow-up questions for panel interviews. For IT
    systems-integrator bids, advisers recommend using AI to audit compliance and consistency, then applying experienced
    commercial judgement to check commitments, economics and protections.
  outcomes:
    - lever: quality
      description: >-
        A 2026 journal study compared three reasoning models with human procurement professionals on 123 State of Ohio supplier
        bids from 31 projects. The models were consistent and aligned with humans on compliance signals, and showed high scoring
        volatility on competitive signals such as value-add propositions; the authors suggest AI for compliance screening and
        humans for differentiation.
      figure: "123 bids, 31 projects, 3 models; no accuracy percentage in the abstract"
      measures: >-
        Consistency and human alignment of model scores on compliance signals, and scoring volatility on competitive signals, across
        123 government supplier bids (State of Ohio IT projects, January 2023 to December 2024).
      provenance: independent
      source_ref: JBL-MCKINLEY-2026
  prerequisites:
    - Proposals in a readable format and a clear scoring framework.
    - Staff who can apply commercial judgement to what the model summarises.
  risks_and_guardrails:
    - Polished AI-assisted proposals can hide weaker economics; an LLM reading an SOW rated "off-ramps" as client-friendly without testing whether they could be used (UPPEREDGE-PROPTRAP-2026; one practitioner's example).
    - UpperEdge's 2025 advice to buyers: require disclosure of AI use, validate in live discussion, bind AI-written commitments into the SOW, and train procurement staff (UPPEREDGE-SI-2025).
    - UpperEdge sells project-execution advisory services, so its advice is not neutral (UPPEREDGE-SI-2025, closing line).
  human_checkpoints:
    - Humans assess differentiation, value-add and commercial terms; the study's authors treat scoring volatility as the signal that human oversight is needed (JBL-MCKINLEY-2026).
  role_evolution: >-
    Legal operations staff are described as moving from reading to analysing structured outputs and focusing on strategic differences
    between firms (ABA-LPMRFP-2026). Proposal writers face two audiences, a human panel and a model, per UpperEdge (UPPEREDGE-PROPTRAP-2026).
  evidence_grade: C
  sources:
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "section 'How Legal Departments Are Using AI in the RFP Process'" }
    - { ref: JBL-MCKINLEY-2026, title: "Do Humans and GAI See Eye to Eye? Implications of LLM Scoring Volatility in Supplier Evaluations", publisher: Journal of Business Logistics, type: academic, url: "https://doi.org/10.1111/jbl.70072", date: "2026-05-14", access: full, locator: "Abstract (Crossref record)" }
    - { ref: UPPEREDGE-PROPTRAP-2026, title: "The AI Proposal Trap: How to Evaluate SI Proposals When Vendors Optimize for Machines", publisher: UpperEdge, type: firm, url: "https://upperedge.com/artificial-intelligence/the-ai-proposal-trap-how-to-evaluate-si-proposals-when-vendors-optimize-for-machines/", date: "2026-08-25", access: full, locator: "sections 'How Vendors Are Optimizing' to checklist" }
    - { ref: UPPEREDGE-SI-2025, title: "6 Ways to Stay Protected When System Integrators Use AI in RFP Responses", publisher: UpperEdge (reprinted from CIO), type: firm, url: "https://upperedge.com/erp-program-management/6-ways-to-stay-protected-when-system-integrators-use-ai-in-rfp-responses/", date: "2025-07-08", access: full, locator: "the six numbered rules" }
    - { ref: TGC-WK-2025, title: "How AI Is Modernizing Responses to Requests for Proposals", publisher: Today's General Counsel (summarising Wolters Kluwer), type: press, url: "https://todaysgeneralcounsel.com/how-ai-is-modernizing-responses-to-requests-for-proposals/", date: "2025-07-11", access: full, locator: "paragraphs 2-3" }
  last_reviewed: 2026-10-19
  notes: >-
    In-house. The independent study is on government IT supplier bids, so it is adjacent evidence and caps the grade; no named
    legal department reports using AI to evaluate bids in these sources. The ABA article's legal-department scenarios (ten firms,
    an employment portfolio) are illustrative examples, not named users. Other pursuit-side evaluator concerns (undisclosed
    AI use in federal evaluations) are covered in the practice-angle file.

- id: professional-services-pursuit-proposals-11
  title: Matter-level evidence pack of AI use and savings for RFP and pitch answers (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [data-reporting, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    RFPs now ask which AI tools a firm uses, how they are governed and whether they produced measurable savings for clients.
    Clients describe a product name as an unacceptable answer, and say they want metrics, outcomes and proof.
  solution: >-
    Idea discussed by practitioners: assemble, per practice or matter type, a short evidence pack (tool, workflow, human review,
    guardrails, measured effect) so proposal teams can answer AI questions with specifics. Time capture tied to AI-assisted
    work (landscape signals on Legora-Laurel) is one possible data source; this entry does not rely on it.
  outcomes:
    - lever: growth
      description: "none published"
      figure: "none published"
      measures: "Not applicable: advice and session descriptions, no measured results."
      provenance: self-reported
      source_ref: PARKERPOE-TR-2026
  prerequisites:
    - Matter-level data on where AI is used and what review took place.
    - Agreement on which claims about savings the firm can defend.
  risks_and_guardrails:
    - A Litera post says firms invested in AI because of perceived client pressure (85%) or competitors (53%), and that if you cannot measure it, "You have just spent money" (LAWSITES-LITERA-2026; vendor survey cited, not independently verified).
    - Clients have heard hype and may discount firm-wide adoption claims; a Parker Poe partner says firms that cannot answer at matter level can only talk about policy (PARKERPOE-TR-2026).
  human_checkpoints:
    - Partners and risk leaders approve statements about AI use and savings before they enter a bid.
  role_evolution: >-
    Chief marketing and business development officers are described as partners in shaping the firm's AI story and taking it into
    pitches and proposals, in a scheduled session at the January 2027 TRI forum (TRI-CMBDO34-2027; scheduled, not yet given).
  evidence_grade: D
  sources:
    - { ref: PARKERPOE-TR-2026, title: "From permission to performance: What clients now expect from AI-enabled law firms", publisher: Thomson Reuters (interview with Parker Poe), type: vendor, url: "https://legal.thomsonreuters.com/blog/from-permission-to-performance-what-clients-now-expect-from-ai-enabled-law-firms/", date: "2026-08-14", access: full, locator: "sections 'Building client trust' and 'Assessing meaningful AI integration'" }
    - { ref: LAWSITES-LITERA-2026, title: "I Sent Three Law Firms an RFP. There's Clearly a Client Experience Gap.", publisher: LawSites (sponsored post by Litera CEO), type: press, url: "https://www.lawnext.com/2026/10/i-sent-three-law-firms-an-rfp-theres-clearly-a-client-experience-gap.html", date: "2026-10-08", access: full, locator: "sections 'Checking a Box' and 'Clients Want Metrics'" }
    - { ref: ABA-LPMRFP-2026, title: "How AI Is Changing the Process of Law Firm Request for Proposals (RFP)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals", date: "2026-07", access: full, locator: "section 'AI Questions Being Asked of Law Firms in RFPs'" }
    - { ref: TRI-CMBDO34-2027, title: "The 34th Annual Chief Marketing & Business Development Officer Forum", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/events/the-34th-annual-chief-marketing-business-development-officer-forum/", date: "2027-01", access: full, locator: "Day 1 breakout 'From Silicon Valley to sea change' (scheduled)" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea label: practitioners discuss the need (RFP question lists, client demands for metrics), but no firm is shown running an
    evidence pack. The CMBDO forum is scheduled for 2027-01-27 to 2027-01-29; the session description is a signal only. The
    Litera post is sponsored content from a vendor CEO and the survey it cites is Litera's own, with no sample size given.

- id: professional-services-pursuit-proposals-12
  title: Agentic pursuit workflows where people direct agents across multi-step proposal tasks
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    AI help is mostly one paragraph at a time. Pursuit work spans qualification, requirements, drafting, review and handoff,
    and context built in one person's AI session does not reach the rest of the team.
  solution: >-
    Agents carry out multi-step proposal and content tasks, with people directing the work rather than doing it by hand. A
    Kantiv summary of the SMPS Foundation Q2 2026 report says agentic AI for proposals was the highest-scored trend in the
    report's AI section and that shared team memory and tool consolidation are open problems.
  outcomes:
    - lever: capacity
      description: >-
        Unanet's 2026 AEC survey found 17% of firms are developing their own agentic workflows. Responsive and APMP's 2025
        survey found Leaders more likely than Novices to use AI to orchestrate workflows and assignments (41% vs 17%).
      figure: "17% of firms (AEC); 41% vs 17% (Leaders vs Novices)"
      measures: >-
        Unanet: share of respondents saying their firms are developing their own agentic workflows (sample size not stated).
        Responsive: share of Leaders vs Novices using AI for orchestrating workflows and assignments, from 726 respondents across industries.
      provenance: vendor-published
      source_ref: BDC-UNANET-2026
  prerequisites:
    - Structured firm knowledge ("context engineering" in the SMPS report's words, per Kantiv): capability files, project data taxonomies, win and loss intelligence.
    - Shared memory or shared context across the pursuit team.
  risks_and_guardrails:
    - Vendor view: a home-built tool needs someone to own prompt governance, permissions and data freshness, and token-based AI pricing can produce unexpectedly high bills (KANTIV-TRUST-2026; vendor opinion).
    - Hinz Consulting's newsletter reports attendees at APMP BPC Nashville moving away from do-it-yourself GenAI solutions as too costly and unfocused (HINZ-BPCNASHVILLE-2025).
  human_checkpoints:
    - People direct the agents and review outputs at defined points; the sources do not specify the gates.
  role_evolution: >-
    Proposal staff move from doing tasks to directing and reviewing agents, per the Kantiv summary of the SMPS report
    (KANTIV-SMPSQ2-2026, secondary).
  evidence_grade: C
  sources:
    - { ref: KANTIV-SMPSQ2-2026, title: "What the SMPS Q2 AI Report Means for AEC Pursuit Teams", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/smps-q2-ai-report", date: "2026-07-13", access: full, locator: "first finding and AI-memory finding" }
    - { ref: BDC-UNANET-2026, title: "AEC report reveals firms are in the throes of AI transition", publisher: Building Design + Construction (by Unanet), type: survey, url: "https://www.bdcnetwork.com/aec-tech/news/55386606/aec-report-reveals-firms-are-in-the-throes-of-ai-transition", date: "2026-06-25", access: full, locator: "paragraph on in-house models and agentic workflows" }
    - { ref: RESPONSIVE-SRM-2025, title: "B2B Revenue Leaders Are Winning Big With AI, And They're Hiring, Not Downsizing (release for the 2025 State of Strategic Response Management Report)", publisher: Responsive with APMP (via Silicon UK), type: survey, url: "https://www.silicon.co.uk/press-release/b2b-revenue-leaders-are-winning-big-with-ai-and-theyre-hiring-not-downsizing", date: "2025-05-08", access: full, locator: "Key findings, third item" }
    - { ref: HINZ-BPCNASHVILLE-2025, title: "Volume 78: Special Edition. BPC Nashville - More Than Just a Conference!", publisher: Hinz Sight newsletter (Hinz Consulting), type: community, url: "https://hinzsight.beehiiv.com/p/volume-78-special-edition-bpc-nashville-more-than-just-a-conference-a-time-to-reconnect-reflect-and", date: "2025-06-02", access: full, locator: "paragraph after 'What people were saying'" }
  last_reviewed: 2026-10-19
  notes: >-
    The SMPS Foundation report is members-only and was not seen; the finding is relayed by a vendor. No named firm is shown
    running a pursuit agent in these sources. The Hinz newsletter concerns a mostly government-contracting audience.

- id: professional-services-pursuit-proposals-13
  title: Firm-approved internal assistant for awards, survey and directory submissions
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [document-production]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Leadership at Ballard Spahr would not allow open public chat tools, so staff had no safe way to use AI for everyday writing
    such as answering surveys and awards submissions within a text limit.
  solution: >-
    The firm built "Ask Ellis", a proprietary assistant that began as chat with drafting and analysis and has grown to include
    other uses. It is used for emails, converting legalese to plain language, and answering surveys and awards submissions within a text limit.
  outcomes:
    - lever: experience
      description: >-
        The firm said Ask Ellis has 900 active users and is growing. The count covers all uses of the tool, not only
        awards and surveys.
      figure: "900 active users"
      measures: "Number of active users of Ask Ellis across the firm, as stated by Lisa Mayo Haynes (Ballard Spahr); period and definition of 'active' not given."
      provenance: self-reported
      source_ref: TRI-INSIDELEGALAI-2025
  prerequisites:
    - A secured firm-owned environment.
    - Practical, role-specific use cases and training; the speaker says the team tells staff the tool is not a legal research tool.
  risks_and_guardrails:
    - Not a legal research tool, per the firm (TRI-INSIDELEGALAI-2025, Use case 2).
  human_checkpoints:
    - Staff review output before submitting; the article does not describe the gate.
  role_evolution: "The article does not describe role changes."
  evidence_grade: B
  sources:
    - { ref: TRI-INSIDELEGALAI-2025, title: "Beyond legal practice: How GenAI is transforming law firm business operations", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en-us/posts/technology/inside-legal-ai-genai-transformation/", date: "2025-12-15", access: full, locator: "Use case 2: AI assistant" }
  last_reviewed: 2026-10-19
  notes: >-
    A usage count for a general tool, not an outcome of pursuit work; grade B for this module. Awards and survey answers are the
    only pursuit-adjacent uses named.

- id: professional-services-pursuit-proposals-14
  title: Competitor and client-reward intelligence for pitch positioning (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [research-synthesis]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Teams rarely know which firms currently handle a client's major matters, or whether the client rewards low cost or premium expertise,
    so positioning is guesswork.
  solution: >-
    The ABA marketing column suggests AI analyse market data and public filings to show which firms handle the client's significant
    matters, how the client has rewarded work, and where to contrast, and to inform competitive pricing. The Kantiv go/no-go
    article similarly points to competitive position as a go/no-go criterion.
  outcomes:
    - lever: growth
      description: "none published"
      figure: "none published"
      measures: "Not applicable: the column lists a capability and reports no result."
      provenance: self-reported
      source_ref: ABA-LPMAI-2026
  prerequisites:
    - Public filings and market data on the client.
    - Firm win/loss and matter history.
  risks_and_guardrails:
    - Output must be checked; the ABA column's cautions apply (ABA-LPMAI-2026, Cautions).
  human_checkpoints:
    - Pursuit lead decides how to use the intelligence in positioning.
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 7" }
    - { ref: KANTIV-GONOGO-2026, title: "How to calibrate your go/no-go matrix using your own wins and losses", publisher: Kantiv, type: vendor, url: "https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix", date: "2026-10-15", access: full, locator: "section 'Which go/no-go criteria are must-haves'" }
  last_reviewed: 2026-10-19
  notes: "Idea label: discussed in a practitioner column; no deployment found. Baker Botts's client needs score (use case 03) is the nearest deployed example."

- id: professional-services-pursuit-proposals-15
  title: Outside counsel guideline and RFP term flagging against the firm's standard terms (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Client guidelines and RFP terms carry billing, travel, staffing, data-security and indemnity provisions that put obligations on the
    firm, and are easy to miss in a short turnaround.
  solution: >-
    The ABA column suggests AI cross-reference a client's outside counsel guidelines against the firm's standard terms and
    produce a dashboard separating standard clauses, clauses needing review and potential deal-breakers (for example indemnifying
    the client beyond the firm's control).
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable: a listed capability with no result."
      provenance: self-reported
      source_ref: ABA-LPMAI-2026
  prerequisites:
    - The firm's standard terms in machine-readable form.
    - Client guidelines supplied with the RFP.
  risks_and_guardrails:
    - Legal and risk staff must review flagged clauses; a Litera post separately urges general counsel to add AI-disclosure, data-handling and accuracy questions to RFP technology sections (LITERA-GCRFP-2026; date not confirmed on the page).
  human_checkpoints:
    - Risk or general counsel reviews flagged clauses before the firm accepts terms.
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 6" }
    - { ref: LITERA-GCRFP-2026, title: "What General Counsel Should Ask About AI in Legal Vendor RFPs", publisher: Litera, type: vendor, url: "https://www.litera.com/node/1585", date: "2026", access: full, locator: "TL;DR and 'Why AI Belongs in Your Legal Vendor RFP'" }
  last_reviewed: 2026-10-19
  notes: "Idea label. Overlaps acceptance-risk. The Litera page date is not on the page (a search result suggested July 2026); the year is used."

- id: professional-services-pursuit-proposals-16
  title: Auto-populate team diversity and compliance data in RFP responses (idea)
  archetype: professional-services
  module: pursuit-proposals
  function: sales-marketing-bd
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Some clients still ask for granular data about the team assigned to their matter, and assembling it by hand from HR and
    practice systems is slow.
  solution: >-
    The ABA column suggests AI pull and format current diversity metrics from the firm's HR and practice management systems to
    meet RFP reporting requirements, noting that the political environment has changed while many clients still demand the data.
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable: a listed capability with no result."
      provenance: self-reported
      source_ref: ABA-LPMAI-2026
  prerequisites:
    - Reliable, consented HR data and a team-assignment record linked to the matter.
  risks_and_guardrails:
    - Data accuracy and employee privacy; the column does not discuss these, so confirm with HR and counsel.
  human_checkpoints:
    - HR or the proposal lead confirms figures before submission.
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: ABA-LPMAI-2026, title: "Leveraging AI to Respond to Requests for Proposals (RFPs)", publisher: ABA Law Practice magazine, type: professional-body, url: "https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps", date: "2026-03", access: full, locator: "item 9" }
  last_reviewed: 2026-10-19
  notes: "Idea label: one item in a practitioner list; no deployment found. The guardrail line is the analyst's reminder to ask, not a statement from the source."
```

---

## 3. Module notes

### Processes and key steps (with work types)
Synthesised from the sources in this file; none gives one canonical list.

- Opportunity qualification and go/no-go (expert-judgment, data-reporting). 92% of AEC firms have some go/no-go process, 47% a formal one (BDC-UNANET-2026).
- RFP and work-statement review, requirements and red-flag detection (review-assurance) (G2X-CAPTURE-2026; ABA-LPMAI-2026, item 1).
- Finding experience, matter data, bios and past answers (research-synthesis). ikaun's respondents ranked this first among time-consuming stages, ahead of writing, tailoring or formatting (IKAUN-BENCH-2026).
- Drafting and tailoring (document-production), with SME and partner input (coordination-scheduling).
- Consistency, compliance and credential checking before submission (review-assurance).
- Pricing and staffing in the proposal (expert-judgment) (routed to scoping-pricing).
- Pitch and orals preparation, including client and prospect research (research-synthesis, client-interaction) (TRI-INSIDELEGALAI-2025).
- Debrief, win/loss and library update (data-reporting).
- In-house buyer side: scoping the RFP, comparing responses, panel questions (review-assurance) (ABA-LPMRFP-2026). Tagged in-house.

### Common pain points
- Volume without proportional capacity: 69% of surveyed law firms say proposal volume rose and none say it fell; of the 76% of firms that reported not pursuing work, 30% gave lack of time or resources as the reason (IKAUN-BENCH-2026, paragraphs 2-3). The release headline words this differently ("over 25% of RFPs not pursued"); the body is used here.
- Experience and credential data are scattered. Only 7% say it is "very easy" to find relevant experience for a proposal, and a third say experience data is not centralised at all (IKAUN-BENCH-2026).
- Stale records: "AI keeps picking great resumes of people who don't work here anymore" was said by an unnamed CIO at a large A/E firm, as reported by a vendor (KANTIV-TRUST-2026).
- Win rates flat or falling while output rises (BDC-UNANET-2026).
- Burnout is on conference agendas: a VisibleThread Optimize26 session on preventing and reversing burnout was led by a vice president of proposal development at Aetna (VT-OPTIMIZE26-2026).
- Clients see little change from firms' AI investment (LAWSITES-LITERA-2026; sponsored vendor view).

### Metrics and benchmarks (with sources)
All are survey or vendor figures; none is an independent outcome measure for pursuit work.
- ikaun (law firms, Am Law 100/200 and NLJ 500; sample size not stated): 69% say volume rose; 27% actively use AI in proposals; 74% lack a single current source of truth for matter experience; over 50% still build proposals in Word; investment priorities were reduced manual work (60%), better win rates (48%), better data accuracy (44%) (IKAUN-BENCH-2026).
- Unanet AEC Inspire Report 2026 (sample size not stated): three-quarters of AEC firms use AI, up about 20% on last year; BD and marketing is the most common function; 27% build in-house AI models, 17% integrations to generic models, 17% agentic workflows; 29% have high confidence in their AI data; 71% submit more proposals; win rates 56%, 52%, 50% for 2024-2026; 13% expect workforce reductions (BDC-UNANET-2026).
- Responsive and APMP 2025 (726 respondents, cross-industry): 54% trialling or deployed AI in strategic response workflows; Leaders vs Novices on workflow orchestration (41% vs 17%), win/loss insights (37% vs 18%), go/no-go (37% vs 26%); more than half of AI adopters increasing staffing against 27% of non-adopters (RESPONSIVE-SRM-2025).
- Ballard Spahr: partners estimate about two hours saved per RFP; Ask Ellis 900 active users (TRI-INSIDELEGALAI-2025). Both self-reported.
- Projectworks (consulting vendor) quotes averages of 91 proposals a year at about 24 hours each and a 266% rise in project count against a 56% drop in average budget, without naming sources; treat as unverified vendor figures (PROJECTWORKS-BD-2026).
- Thomson Reuters Institute's 2026 AI in Professional Services report, as summarised on a vendor blog: only 18% of organisations measure AI return on investment and about 40% are unsure whether it is tracked (TR-AIPS-2026). Cross-field, not pursuit-specific.
- Independent evidence: only JBL-MCKINLEY-2026 (123 government IT supplier bids; AI consistent on compliance, volatile on value-add). Adjacent to this module.
- **Quality evidence for pursuit outputs: none found.** No error rates, override rates, hallucination counts in proposals, parallel runs, inspection findings or win-rate studies of AI-assisted bids.

### Guardrails and regulatory points
- Do not use public models that train on firm inputs; verify every success story, award and bio; disclose AI assistance with a note of oversight (ABA-LPMAI-2026, Cautions).
- RFPs ask about AI tools, governance, data use for training, safeguards, savings and roadmaps (ABA-LPMRFP-2026, section on AI questions). That article cites ABA Formal Opinion 512 for the duty to understand tools and protect confidentiality (ABA-LPMRFP-2026, introduction).
- Buyer-side advice for IT services: require disclosure, live validation, written commitments, AI literacy for procurement (UPPEREDGE-SI-2025).
- One Litera post cites an Association of Corporate Counsel finding that 59% of in-house counsel do not know whether outside counsel use generative AI on their matters (LITERA-GCRFP-2026; relayed secondhand, original not checked, page date not confirmed).
- In US federal AEC qualification forms (SF-330) an invented project citation can mean disqualification, per a vendor (KANTIV-TRUST-2026).

### Frontier signals (dated and sourced)
- 2026-10-08: A legal-technology CEO tells firms that RFPs are the first place clients see whether AI investment translated into something they can feel and measure (LAWSITES-LITERA-2026; sponsored).
- 2026-10-07: Capture-agent build-along workshop for RFP and work-statement review (G2X-CAPTURE-2026).
- 2026-09-11: Stinson partners publish in Law360 that AI helps firms move through RFPs better and faster but that the time saved should be reinvested in client understanding (STINSON-LAW360-2026).
- 2026-08-25: An advisory firm argues vendors are optimising proposals for both human and machine evaluators and clients should audit with AI then apply commercial judgement (UPPEREDGE-PROPTRAP-2026).
- 2026-07-13: Kantiv summarises the SMPS Foundation Q2 report: agentic AI for proposals scored as the top AI trend (KANTIV-SMPSQ2-2026; secondary).
- 2026-07-08: IBA webinar on the future of pitching covering AI in proposal development, credential capture and pitch personalisation, value-based pricing and procurement-led evaluation (IBA-PITCHING-2026; abstract only).
- 2026-06-18: IBA Business Development and Marketing subcommittee podcast episode on how AI will affect marketing, BD and client relationships (IBA-BDPODCAST-2026; episode description only).
- 2026-05-14: Journal of Business Logistics publishes the study of AI scoring of supplier bids (JBL-MCKINLEY-2026).
- 2025-03-21 and 2025-06-02 (background, 16-19 months old): VisibleThread's recap of APMP BPC Dublin says AI dominated the event and human expertise stays critical (VT-BPCDUBLIN-2025); Hinz Consulting's BPC Nashville recap says the fear of AI replacing proposal staff had faded, with at least one AI session in every time block (HINZ-BPCNASHVILLE-2025).
- 2026-04-14 to 2026-04-16: VisibleThread's Optimize26 bid conference, with sessions on AI, data readiness and the human nuance of bidding (VT-OPTIMIZE26-2026).
- 2026-04-17: Stanford's Generative Legal panel asked how in-house leaders evaluate law firms' AI capabilities in pitches and panels (STANFORD-GENLEGAL-2026; abstract only).
- 2026-03-10 (search-only): Legalweek session "RFP 3.0: How Firms and Clients Co-Create AI-Powered Proposals and Pick Winners" (LEGALWEEK-RFP3-2026). The page could not be opened and no recap was found.
- Scheduled, not given: Thomson Reuters Institute CMBDO Forum, 2027-01-27 to 2027-01-29, with a session on taking the firm's AI story into pitches and proposals and another on winning visibility in AI-driven discovery (TRI-CMBDO34-2027).

### Workforce and role effects
- Staffing is not shrinking in the surveys: Responsive reports more than half of AI adopters increasing staffing against 27% of non-adopters (RESPONSIVE-SRM-2025); Unanet reports 13% anticipating workforce reductions from AI (BDC-UNANET-2026). Hinz Consulting's newsletter reports talk at APMP BPC Nashville of companies reducing full-time headcount alongside the view that AI will not replace BD people (HINZ-BPCNASHVILLE-2025; government-contracting context).
- Skill emphasis is shifting to strategy, storytelling, quality control and problem-solving (NYREJ-SMPSNY-2026).
- Marketing and BD leaders argue they belong on the firm's AI council (PASSLE-EP177-2025, show notes).
- Senior time: Projectworks says senior staff spend about 11 hours per proposal and that 40% of firms have seniors contributing over 60% of development time; unsourced vendor figures (PROJECTWORKS-BD-2026).
- Pursuit staff are described as owners of the knowledge base and as moving from searching to reviewing (KANTIV-TRUST-2026, vendor). A VisibleThread speaker bio describes work on preparing bid writers for an AI-enabled future through APMP UK career-path initiatives (VT-OPTIMIZE26-2026, speaker list).

### Objections and concerns practitioners raise
- Sameness: selection committees may recognise generic AI output, and prospects receive many near-identical AI messages, per a vendor summary of the SMPS report (KANTIV-SMPSQ2-2026).
- Accuracy and invented credentials (KANTIV-TRUST-2026; ABA-LPMAI-2026).
- Process and culture before technology; pitching is treated as a process problem when it is strategic (PASSLE-EP191-2026, show notes).
- AI use without proof: clients "have watched announcements that looked more like positioning than practice" (PARKERPOE-TR-2026, quoting a Parker Poe partner); firms bought AI to match competitors, not to follow a strategy (LAWSITES-LITERA-2026, vendor survey).
- Polished proposals can hide weaker deals (UPPEREDGE-PROPTRAP-2026).
- No win-rate proof: output is rising while Unanet's win rate falls (BDC-UNANET-2026).
- ROI is rarely measured (TR-AIPS-2026), and CMOs are told to prepare for conversations with CFOs on rationalising AI cost, per the show notes of a 2025 CMO Series Live session with a Reed Smith CFO and a Ford legal-operations executive among the speakers (PASSLE-CMOLIVE-2025; audio not heard).
- Do-it-yourself builds are costly; build versus buy is contested, and most voices are vendors with a product to sell (HINZ-BPCNASHVILLE-2025; KANTIV-TRUST-2026).

### Interview probes for an advisor
1. When your last proposal was written, where did the experience, bios and past answers come from, and who is accountable for them being current?
2. After AI, did the saved hours go into more bids, deeper tailoring or senior review? What do you track to know, and has your win rate moved?
3. A client asks "how do you use AI on our matter, and what does it save us?" Who writes that answer, and what evidence sits behind it?
4. Do you know or suspect that buyers use AI to read your submissions? Have you changed how you write, or how you check what you submit?
5. Who in the firm can run client and prospect research or red-flag an RFP without going through marketing, and how do you stop that producing inconsistent claims?

---

## 4. Routed to other modules

- **scoping-pricing:** fee-scenario modelling from historical billing data and alternative-fee options inside proposals (ABA-LPMAI-2026, item 8; ABA-LPMRFP-2026, pricing and staffing paragraph; Projectworks pricing section, PROJECTWORKS-BD-2026); the LMA26 session "Priced to Win: How AI Is Reshaping the Firm-Client Value Conversation" (Jones Day and Wilson Sonsini presenters; session abstract only, LMA-PRICED-2026); UpperEdge's point that an LLM can be swayed by discount framing (UPPEREDGE-PROPTRAP-2026).
- **client-development:** AI-search visibility and "agent-to-agent discovery" sessions (TRI-CMBDO34-2027, scheduled; LMA26 session titles on AI search visibility in LMA-RECORDINGS-2026); cross-selling and revenue intelligence themes (PASSLE episodes, TRI-CMBDO34-2027); prospect needs scoring (use case 03 overlaps); Projectworks' claim that over half of proposals are for existing clients (PROJECTWORKS-BD-2026, unsourced).
- **staffing-resourcing:** matching team members to bids and selecting attorneys by experience (STINSON-LAW360-2026; PROJECTWORKS-BD-2026).
- **knowledge-management:** the experience, bio and records-reconciliation layer (use cases 01, 02, 04) is a knowledge-management asset as much as a pursuit tool.
- **acceptance-risk:** outside counsel guideline and RFP-terms review (use case 15) and Litera's advice on AI disclosure questions (LITERA-GCRFP-2026).
- **quality-review:** verification of AI-written claims and evaluator-side scoring volatility (JBL-MCKINLEY-2026).
- **talent-learning:** skills for proposal professionals (NYREJ-SMPSNY-2026; VT-OPTIMIZE26-2026).
- **firm-finance:** AI investment ROI and measurement (TR-AIPS-2026; LAWSITES-LITERA-2026; PATTERN-ALVAREZ-2025 on ROI and time-to-value for legal marketing AI).

---

## 5. Sources

All were opened (access: full) unless marked search-only. "Mirror" means `curl` was blocked and the page was read through r.jina.ai. "Abstract only" means the page is an abstract or show notes. Dates are publication or event dates taken from page metadata unless noted.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| IKAUN-BENCH-2026 | ikaun Releases The State of Winning Work in Law Firms: A 2026 Benchmark Report | ikaun | survey | https://www.ikaun.com/news/ikaun-releases-the-state-of-winning-work-in-law-firms-a-2026-benchmark-report | 2026-07-14 |
| TRI-INSIDELEGALAI-2025 | Beyond legal practice: How GenAI is transforming law firm business operations | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/technology/inside-legal-ai-genai-transformation/ | 2025-12-15 |
| ABA-LPMRFP-2026 | How AI Is Changing the Process of Law Firm Request for Proposals (RFP) (mirror) | ABA Law Practice magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/july-august-2026/how-ai-is-changing-the-law-firm-request-for-proposals | 2026-07 (July/August issue) |
| ABA-LPMAI-2026 | Leveraging AI to Respond to Requests for Proposals (RFPs) (mirror) | ABA Law Practice magazine | professional-body | https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/leveraging-ai-to-respond-to-rfps | 2026-03 (March/April issue) |
| STINSON-LAW360-2026 | Scheck and Valdivia Examine How AI Is Reshaping Law Firm RFPs in Law360 | Stinson LLP | firm | https://www.stinson.com/newsroom-news-scheck-and-valdivia-examine-how-ai-is-reshaping-law-firm-rfps-in-law360 | 2026-09-11 |
| LAWSITES-LITERA-2026 | I Sent Three Law Firms an RFP. There's Clearly a Client Experience Gap. (sponsored post, Litera CEO) | LawSites | press | https://www.lawnext.com/2026/10/i-sent-three-law-firms-an-rfp-theres-clearly-a-client-experience-gap.html | 2026-10-08 |
| PARKERPOE-TR-2026 | From permission to performance: What clients now expect from AI-enabled law firms | Thomson Reuters (Legal blog) | vendor | https://legal.thomsonreuters.com/blog/from-permission-to-performance-what-clients-now-expect-from-ai-enabled-law-firms/ | 2026-08-14 |
| UPPEREDGE-PROPTRAP-2026 | The AI Proposal Trap: How to Evaluate SI Proposals When Vendors Optimize for Machines (mirror) | UpperEdge | firm | https://upperedge.com/artificial-intelligence/the-ai-proposal-trap-how-to-evaluate-si-proposals-when-vendors-optimize-for-machines/ | 2026-08-25 |
| UPPEREDGE-SI-2025 | 6 Ways to Stay Protected When System Integrators Use AI in RFP Responses (mirror; reprinted from CIO) | UpperEdge | firm | https://upperedge.com/erp-program-management/6-ways-to-stay-protected-when-system-integrators-use-ai-in-rfp-responses/ | 2025-07-08 |
| JBL-MCKINLEY-2026 | Do Humans and GAI See Eye to Eye? Implications of LLM Scoring Volatility in Supplier Evaluations (abstract only, via Crossref API) | Journal of Business Logistics (McKinley, Dohmen, Castillo) | academic | https://doi.org/10.1111/jbl.70072 | 2026-05-14 |
| BDC-UNANET-2026 | AEC report reveals firms are in the throes of AI transition (Lucas Hayden, Unanet; on the 2026 AEC Inspire Report) | Building Design + Construction | survey | https://www.bdcnetwork.com/aec-tech/news/55386606/aec-report-reveals-firms-are-in-the-throes-of-ai-transition | 2026-06-25 |
| RESPONSIVE-SRM-2025 | B2B Revenue Leaders Are Winning Big With AI, And They're Hiring, Not Downsizing (release for the 2025 State of Strategic Response Management Report) | Responsive with APMP, via Silicon UK | survey | https://www.silicon.co.uk/press-release/b2b-revenue-leaders-are-winning-big-with-ai-and-theyre-hiring-not-downsizing | 2025-05-08 |
| KANTIV-SMPSQ2-2026 | What the SMPS Q2 AI Report Means for AEC Pursuit Teams | Kantiv | vendor | https://www.kantiv.com/blog/smps-q2-ai-report | 2026-07-13 |
| KANTIV-TRUST-2026 | What's Under the Slab: How AI Trust Actually Gets Built in AEC | Kantiv | vendor | https://www.kantiv.com/blog/ai-trust-ai-proposal-software-for-aec | 2026-07-21 |
| KANTIV-GONOGO-2026 | How to calibrate your go/no-go matrix using your own wins and losses | Kantiv | vendor | https://www.kantiv.com/blog/blog-go-no-go-scorecard-matrix | 2026-10-15 |
| NYREJ-SMPSNY-2026 | SMPS NY hosts "Humans at the Helm: Guiding AI in Proposal Management" virtual program | New York Real Estate Journal | press | https://nyrej.com/smps-ny-hosts-humans-at-the-helm-guiding-ai-in-proposal-management-virtual-program | 2026-06-30 |
| VT-OPTIMIZE26-2026 | Optimize26 - The Bid Conference (agenda and speakers) | VisibleThread | conference | https://www.visiblethread.com/events/optimize26-the-bid-conference/ | 2026-04-14 to 2026-04-16 (page published 2026-01-16) |
| VT-BPCDUBLIN-2025 | Reflections on APMP BPC Dublin 2025: Key Takeaways from VisibleThread | VisibleThread | vendor | https://www.visiblethread.com/blog/reflections-on-apmp-bpc-dublin-2025-key-takeaways-from-visiblethread/ | 2025-03-21 |
| HINZ-BPCNASHVILLE-2025 | Volume 78: Special Edition. BPC Nashville - More Than Just a Conference! | Hinz Sight newsletter (Hinz Consulting) | community | https://hinzsight.beehiiv.com/p/volume-78-special-edition-bpc-nashville-more-than-just-a-conference-a-time-to-reconnect-reflect-and | 2025-06-02 |
| G2X-CAPTURE-2026 | Capture Agent Build-Along: Is This RFP Wired? | G2X and ProposalTeam Partners (Luma event page) | conference | https://luma.com/xcwn65gt | 2026-10-07 |
| LMA-RECORDINGS-2026 | 2026 LMA Annual Conference Recordings Bundle (session list; mirror) | Legal Marketing Association | conference | https://www.legalmarketing.org/Details/2026-lma-annual-conference-recordings-bundle-mch | 2026-05-01 (page date) |
| LMA-DECENT-2026 | From Decent to Great: How to Develop a Compelling Proposal Response (abstract only; mirror) | Legal Marketing Association | conference | https://www.legalmarketing.org/Purchase/from-decent-to-great-how-to-develop-a-compelling-proposal-response-mch | 2026-05-01 (page date) |
| LMA-PRICED-2026 | Priced to Win: How AI Is Reshaping the Firm-Client Value Conversation (abstract only; mirror) | Legal Marketing Association | conference | https://www.legalmarketing.org/Purchase/priced-to-win-how-ai-is-reshaping-the-firm-client-value-conversation-mch | 2026-05-01 (page date) |
| IBA-PITCHING-2026 | The future of pitching: AI, innovation and evolving client expectations (webinar abstract) | International Bar Association | conference | https://prod-bo.ibanet.org/conference-details/CONF2897 | 2026-07-08 |
| STANFORD-GENLEGAL-2026 | Panel: The Client Perspective, Generative Legal 2026 (abstract only; mirror) | Stanford Law School | conference | https://conferences.law.stanford.edu/generative-legal-2026/sessions/panel-the-client-perspective/ | 2026-04-17 |
| TRI-CMBDO34-2027 | The 34th Annual Chief Marketing & Business Development Officer Forum (agenda; scheduled event) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/events/the-34th-annual-chief-marketing-business-development-officer-forum/ | 2027-01-27 to 2027-01-29 (page read 2026-10-19) |
| LEGALWEEK-RFP3-2026 | RFP 3.0: How Firms and Clients Co-Create AI-Powered Proposals and Pick Winners (search-only; session page returned "not found" when opened) | Law.com Legalweek | conference | https://www.event.law.com/legalweek/session/3412999/rfp-3.0-how-firms-and-clients-co-create-ai-powered-proposals-and-pick-winners | 2026-03-10 (per search result) |
| IBA-BDPODCAST-2026 | Business Development and Marketing Subcommittee Podcast: Martijn Lesterhuis (episode description only) | International Bar Association | podcast | https://www.ibanet.org/LFMC/MBD-Podcast/Martijn-Lesterhuis | 2026-06-18 |
| PASSLE-EP191-2026 | Episode 191 - Patrick Johnson of Honigman on Rethinking How Law Firms Pitch and Win Work (show notes) | Passle CMO Series Podcast | podcast | https://passle.podbean.com/e/pitch-perfect-how-honigman-rewrites-the-law-firm-playbook/ | 2026-01-28 |
| PASSLE-EP203-2026 | Episode 203 - Roanne Neuwirth on What Separates a Market Position from a Service List (show notes) | Passle CMO Series Podcast | podcast | https://passle.podbean.com/e/episode-203-roanne-neuwirth-on-what-separates-a-market-position-from-a-service-list/ | 2026-06-10 |
| PASSLE-EP177-2025 | Episode 177 - Guy Alvarez of InnovAItion Partners on AI & Legal Marketing: Where Are We and What Comes Next? (show notes) | Passle CMO Series Podcast | podcast | https://passle.podbean.com/e/unlocking-ai-in-legal-marketing-insights-with-guy-alvarez/ | 2025-08-12 |
| PASSLE-CMOLIVE-2025 | CMO Series Live Special: The AI Revolution and What it Means for CMOs (show notes; session of 2025-06-05, New York) | Passle CMO Series Podcast | podcast | https://passle.podbean.com/e/ai-in-law-revolutionizing-legal-cmos-and-client-engagement/ | 2025-07-09 |
| PATTERN-ALVAREZ-2025 | Measuring AI Value in Legal Marketing and Business Development | Pattern Recognition newsletter (Guy Alvarez) | community | https://pattern-recognition.beehiiv.com/p/measuring-ai-value-in-legal-marketing-and-business-development | 2025-09-17 |
| PROJECTWORKS-BD-2026 | Using AI to Win More Client Work: A Guide for Consulting Business Development | Projectworks | vendor | https://www.projectworks.com/blog/using-ai-to-win-more-client-work-bd-guide | 2026-06-23 |
| TGC-WK-2025 | How AI Is Modernizing Responses to Requests for Proposals | Today's General Counsel | press | https://todaysgeneralcounsel.com/how-ai-is-modernizing-responses-to-requests-for-proposals/ | 2025-07-11 |
| LITERA-GCRFP-2026 | What General Counsel Should Ask About AI in Legal Vendor RFPs | Litera | vendor | https://www.litera.com/node/1585 | 2026 (month not on page) |
| TR-AIPS-2026 | Highlights from the 2026 AI in Professional Services report and what it means for legal teams | Thomson Reuters (Legal blog) | vendor | https://legal.thomsonreuters.com/blog/highlights-from-the-2026-ai-in-professional-services-report-and-what-it-means-for-legal-teams-tri/ | 2026-02-26 |

Counts by type (37 listed; 36 opened, 1 search-only): conference 9 (one is the search-only Legalweek session), vendor 8, podcast 5, press 4, survey 3, firm 3, professional-body 2, community 2, academic 1.

Sources seen only in search results and not listed above because no claim depends on them: Amplyfi webinar on AI account research (January 2026); Stargazy Brief podcast episode of 2026-03-05 (page returned an error); Inventive AI "Inventor Podcast" episode with Darrell Woodward (undated); AGC Massachusetts listing of an SMPS Foundation webinar on 2026-08-11; APMP Asia Pacific "Proposal Management in the Age of AI" event (page undated).

---

## 6. Gaps

- **Quality evidence.** None for pursuit work: no error rates, override rates, hallucination counts in proposals, parallel runs, inspection results, or independent win-rate studies. The only independent measurement is the Ohio supplier-bid study, which concerns buyer-side scoring of government IT bids.
- **Source mix.** Most items are vendor-authored or vendor-sponsored (ikaun, Kantiv, Unanet, Responsive, Litera, Projectworks, Passle, VisibleThread, Thomson Reuters blog). Treat survey figures as vendor-published; sample sizes are not stated for the ikaun and Unanet surveys.
- **Conference content.** Several sessions could only be read as abstracts: LMA26 (recordings are members' content), IBA webinar, Stanford panel, TRI CMBDO forum (scheduled for 2027), and the Legalweek "RFP 3.0" session (search-only; the session page returned "not found"). No recaps of these were found. The searches run did not surface pursuit-specific sessions at ILTACON, CLOC, Legal Geek, AICPA ENGAGE or PMI events (these were not searched individually), and the APMP BPC 2026 agenda and an SMPS Build Business 2026 recap were not found.
- **Consulting and accounting.** Very little practitioner discussion of AI in consulting or accounting pursuits was found: the consulting sources are a vendor guide (Projectworks, with unsourced figures) and a UK buyer-side adviser (UpperEdge); no accounting-firm pursuit discussion in the window was found (an Accounting Today piece on pursuits is from 2023 and was not used). No Big Four, McKinsey, BCG or Bain primary statement on proposal tooling was found.
- **Community discussion.** Reddit returned 403 through `curl` and the mirror, LinkedIn was not tried, Hacker News had nothing relevant. The community items here are two consultant newsletters (Hinz Sight, Pattern Recognition).
- **Podcasts.** Show notes only; no audio or transcripts. The Stargazy Brief episode on AI and bid teams as revenue partners (2026-03-05, seen in search) could not be opened.
- **Date caveats.** VT-BPCDUBLIN-2025 (2025-03-21) is about 19 months before today and is used only as background. LITERA-GCRFP-2026 has no date on the page, and a search result suggested July 2026. The LMA pages carry a page date of 2026-05-01, not the conference date.
- **Kantiv SMPS PRC recap.** Kantiv's 2026-04-08 post on SMPS PRC 2026 (Seattle) returned only its opening paragraph; the body was not retrievable through `curl` or the mirror, so no claim relies on it.
- **Win/loss.** No named professional-services firm using AI for win/loss analysis was found; vendors sell AI-moderated debrief interviews, but those claims were not opened.
- **Discrepancies.** ikaun's release headline says over 25% of RFPs go unpursued for lack of time or resources, while the body says 30% of the 76% of firms that skipped RFPs cite that reason; the body is used. The Kantiv go/no-go table is hypothetical. The ABA column's "70-80% complete first draft" is an assertion.
- **Search use.** 22 web searches were used. The brief says searches are rationed and shared but gives no number, so the shared budget may be tighter than this run assumed.
