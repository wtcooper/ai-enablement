# Tax: research-advisory, discourse angle

- **Archetype:** tax
- **Module:** research-advisory (tax research, technical memos, planning and advisory by firm advisers and in-house tax counsel)
- **Angle:** discourse (what practitioners are saying)
- **Prepared:** 2026-10-17 (wave 2)
- **Method note:** Sources were opened with `curl` and text extraction (`pdftotext` for PDFs). Reddit, TaxProTalk, AccountingWEB and the AICPA community sit behind bot walls and could not be read; one AccountingWEB item is search-only and is not used for any outcome. Web search ran out of budget before the last planned directions were run (independent benchmarks of tax research tools; podcasts). Every outcome figure carries its measure and provenance; "none published" means exactly that.

## 1. Summary

- **Use cases:** 17 candidates. Evidence grades: A 0, B 5, C 7, D 5 (17 in total). No entry reaches grade A because no named organization has published a measured quality or time outcome for AI-assisted tax research or advisory work. Every time-saving figure found is vendor-published or an unmeasured quote.
- **The field's argument has moved from "does it work" to "who owns the risk".** Thomson Reuters Institute's account of the April 2026 TEI Tax Technology Seminar says the capability question was effectively settled in the room, and the live concerns were silent failures, no clear AI owner (two hands out of more than 50 said tax owns AI implementation), failed training rollouts and rising token costs (TEI-TAXTECH-2026). The vendor-owned source should be weighed accordingly.
- **Regulators and professional bodies converged on one message: existing duties apply and the signer is accountable.** IRS OPR Alert 2026-19 (24 Jun 2026) maps AI use onto Circular 230 sections 10.22, 10.27, 10.35, 10.36 and 10.37 and IRC 6713/7216 (IRS-OPR-2026); the UK PCRT bodies issued topical AI guidance on 19 Jan 2026 (PCRT-AI-2026). In *Clinco* (T.C. Memo. 2026-16), three of four cases cited for one argument were found to be apparent AI fabrications; the judge said he had seen fewer than a dozen such instances in Tax Court filings and had imposed no sanctions as of March 2026 (BLAW-TAXCT-2026, TAXCT-CLINCO-2026).
- **The sharpest live dispute is billing.** OPR says billing manual time that AI saved may breach the unconscionable-fee rule; the AICPA has asked the IRS to clarify language it says does not appear to allow value pricing (AICPA-CART-2026). Firms such as RSM US and PwC US describe moving toward value-based pricing (BTAX-PRICING-2026).
- **Adoption data are broad but thin and mostly vendor-sourced.** Thomson Reuters-authored material says 34% of tax firms deploy GenAI at organization level, up from 21%, and only 19% of those measure ROI (CPAPA-TR-2026); there is no independent head-to-head benchmark of commercial tax research tools. The one independent accuracy study found is adjacent: retrieval-based legal research tools hallucinated 17% to 33% of the time (MAGESH-2024).
- **Where the field says it is heading:** agentic research that plans and executes multi-step questions (Bloomberg Tax, Thomson Reuters), firm platforms on which clients build their own agents (KPMG with Anthropic, May 2026), a voluntary risk framework and cross-sector council rather than standards (Werfel framework; CART, September 2026), and a Tax Court that says it is still working out its approach. Scepticism about job loss in corporate tax is on record (SALA-TAXNOTES-2026).

## 2. Use cases

```yaml
- id: tax-research-advisory-01
  title: Grounded AI tax research assistant with cited answers for firm advisers
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Advisers at small and mid-size firms research tax questions in keyword databases or general search, which
    is slow and expensive; one vendor-co-produced survey reports that most practitioners still turn to Google even
    when the firm pays for a research platform.
  solution: Adviser asks a question in plain language and a model grounded in a curated tax content set (for example
    Tax Notes and IBFD for Blue J; Checkpoint plus primary sources for CoCounsel Tax) returns a cited answer with
    links to authority, which the adviser then reads and tests before relying on it. Named users include SSC CPAs
    + Advisors, which moved its primary research tool from Checkpoint to Blue J, and RSM US (Washington National
    Tax leader quoted on Blue J's site).
  outcomes:
  - lever: speed
    description: Blue J headlines average weekly time saved per user
    figure: 3 hours per user per week
    measures: Hours saved per user every week, as headlined on Blue J's product page; no sample, period or method
      is stated
    provenance: vendor-published
    source_ref: BLUEJ-2026
  - lever: speed
    description: Report summary states users save about 2.94 hours a week and get an authoritative answer in as
      little as 2.8 minutes
    figure: 2.94 hours per week; 2.8 minutes (fastest case)
    measures: Average hours saved per week as reported by Blue J users per the Blue J/CPA.com report summary; the
      2.8 minutes is the fastest case ('as little as'), not an average
    provenance: vendor-published
    source_ref: CPAPA-BLUEJ-2025
  - lever: speed
    description: Thomson Reuters states average time savings for CoCounsel users
    figure: 32% per task
    measures: Average time savings per task, as stated by Thomson Reuters for users of its CoCounsel solutions;
      the article gives no sample or method
    provenance: vendor-published
    source_ref: CPAPA-TR-2026
  - lever: speed
    description: A named tax partner at Sorren describes one task
    figure: 4 to 5 hours to 15 minutes
    measures: One partner's recollection of how long a type of task used to take versus now, quoted on the vendor's
      page; not a measured sample
    provenance: vendor-published
    source_ref: BLUEJ-2026
  - lever: quality
    description: No error rate, override rate or independent head-to-head result has been published for any tax-specific
      research tool in the sources read
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: BLUEJ-2026
  prerequisites:
  - Licensed authoritative content behind the tool (for example Tax Notes, IBFD, Checkpoint)
  - An approved-tool policy so staff stop using public chatbots (TR reports more than one third of professionals
    admit using unauthorized AI tools)
  - Vendor review of data retention and training terms before client facts are entered (IRC 6713 and 7216 exposure)
  risks_and_guardrails:
  - Grounding reduces but does not remove hallucination; the only independent measurement found is adjacent (legal
    research tools that use retrieval hallucinated 17% to 33% of the time in a 2024 preregistered study), so it
    caps this entry's grade
  - Circular 230 sections 10.22 and 10.35 put verification and technological competence on the practitioner (OPR
    Alert 2026-19)
  - A Drake Software executive warns that AI 'tends to agree with you' and varies by platform
  human_checkpoints:
  - Adviser reads the cited primary authority, not only the generated summary
  - Reviewer or partner sign-off on any conclusion sent to a client
  role_evolution: Research time moves from finding authority to verifying and applying it. RSM's Washington National
    Tax leader says the tool keeps the practitioner 'in the driver's seat'; TR's own paper warns firms to protect
    junior development as routine tasks automate.
  evidence_grade: B
  sources:
  - ref: BLUEJ-2026
    title: 'Blue J AI Tax Research Platform (product page: customer quotes and usage statistics)'
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/events
    date: '2026-10-17'
    access: full
    locator: Customer quotes (Sorren, RSM US, ELO CPAs) and 'Stats that speak for themselves' section
  - ref: BLUEJ-SSC-2025
    title: SSC CPAs + Advisors Elevates Tax Research with Blue J's AI-Powered Platform (customer story)
    publisher: Blue J
    type: vendor
    url: https://www.bluej.com/our-customers/ssc-cpas-advisors
    date: '2025-10-17'
    access: full
    locator: 'Whole page: switch from Checkpoint Tax Research; no figures given'
  - ref: CPAPA-BLUEJ-2025
    title: Blue J and CPA.com Co-Author the AI Tax Research Solution Outlook Report
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2025/09/17/blue-j-and-cpa-com-co-author-the-ai-tax-research-solution-outlook-report-to-set-the-benchmark-for-the-future-of-tax-research/168693/
    date: '2025-09-17'
    access: full
    locator: Bullets on adoption (54.4% / 33.1%), Google use (81.3%), 2.94 hours
  - ref: CPAPA-TR-2026
    title: 'The Real AI Story in Tax and Audit Isn''t Adoption: It''s Impact (Thomson Reuters-authored piece)'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/21/the-real-ai-story-in-tax-and-audit-isnt-adoption-its-impact/181846/
    date: '2026-04-21'
    access: full
    locator: Paragraph on CoCounsel time savings and Checkpoint content
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: Priority 1, govern the tools (unauthorized tools)
  - ref: MAGESH-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (Magesh et al., arXiv
      2405.20362)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract (17% to 33%, adjacent legal-research tools)
  - ref: TAXADV-DRAKE-2025
    title: AI's role in complex tax decisions (advertising supplement, Drake Software)
    publisher: The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/aug/ais-role-in-complex-tax-decisions/
    date: '2025-07-25'
    access: full
    locator: Sapp Q&A
  last_reviewed: '2026-10-17'
  notes: 'Grade capped at B: every figure is vendor-published, and the only independent accuracy measurement found
    concerns legal research tools (MAGESH-2024). The same CPA.com/Blue J report summary gives 54.4% of 150+ surveyed
    practitioners using AI for tax research while 33.1% of firms had formally adopted AI tools (2025 edition; vendor-co-produced).
    The 2026 edition''s landing page says AI adoption among accounting firms has nearly doubled in a single year
    (BLUEJ-CPA-2026; report gated, so no figures used). Blue J''s own comparison page (BLUEJ-ENT-2026, 2026-10-16)
    lists Blue J, CoCounsel Tax, CCH AnswerConnect, Tolley+ with Protege, Bloomberg Tax AI and TaxGPT as the enterprise
    field.'
- id: tax-research-advisory-02
  title: Multi-step 'reason and act' research agent that clarifies the question, plans, and drafts a reviewable
    work product
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - document-production
  pattern: research-brief
  ladder: delegate
  change_scope: process
  runtime_class: personal-assistant
  maturity: announced
  problem: Complex or multi-step tax questions need several rounds of searching, reading and re-framing, and the
    reasoning is rarely preserved in a form a reviewer can follow.
  solution: Bloomberg Tax describes a Deep Thinking Mode that lets users answer clarifying follow-up questions,
    then develops and executes a research plan for multi-step questions. Thomson Reuters positions CoCounsel Tax
    as moving from search-and-find to reason-and-act, with preserved reasoning chains, citations and review-ready
    outputs.
  outcomes:
  - lever: quality
    description: No measured outcome for the multi-step research mode is published in the sources read
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: BTAX-TOOLS-2026
  - lever: capacity
    description: Thomson Reuters-authored piece reports how many tax firms currently use agentic AI and how many
      expect it to be central
    figure: 14% currently; 80% expect central within five years
    measures: Share of tax firms saying agentic AI is currently part of their workflow, and share expecting it to
      be central to how their organization operates within five years; denominator and sample are not stated in
      the article
    provenance: vendor-published
    source_ref: CPAPA-TR-2026
  prerequisites:
  - Licensed authoritative content and citation linking
  - A way to retain the plan and reasoning for the reviewer
  risks_and_guardrails:
  - Reasoning chains can compound errors across steps (Bloomberg Tax lists multi-step reasoning as a hallucination
    amplifier)
  - At TEI Tax Tech 2026, practitioners reported failures that are silent and polite rather than loud, for example
    an agent admitting after challenge that it had not opened the file
  human_checkpoints:
  - Reviewer inspects the research plan and the authorities before the output reaches a client
  - Adviser confirms facts supplied to the agent
  role_evolution: Adviser moves from running searches to setting the question, reviewing the plan and challenging
    the conclusion; TR frames it as amplifying judgment, not replacing it.
  evidence_grade: C
  sources:
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: Bullet 'Deep Thinking Mode'
  - ref: TR-AGENTICBLOG-2026
    title: An evolution of tax tools and how agentic AI will shape 2026
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/an-evolution-of-tax-tools-and-how-agentic-ai-will-shape-2026/
    date: '2026-05-01'
    access: full
    locator: 'Section ''Automating tax workflows with AI: The agentic revolution'''
  - ref: CPAPA-TR-2026
    title: 'The Real AI Story in Tax and Audit Isn''t Adoption: It''s Impact (Thomson Reuters-authored piece)'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/21/the-real-ai-story-in-tax-and-audit-isnt-adoption-its-impact/181846/
    date: '2026-04-21'
    access: full
    locator: Paragraph beginning 'Our research shows that just 14%'
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/?p=16920
    date: '2026-05-11'
    access: full
    locator: Section 'Why does generative AI hallucinate?'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard'
  last_reviewed: '2026-10-17'
  notes: Announced and marketed; no named firm outcome found. Landscape lists Bloomberg Tax's Deep Thinking Mode
    as launched at TEI Midyear (March 2026); the source is a sponsor press release.
- id: tax-research-advisory-03
  title: Firm-built tax research assistant on the firm's own platform (Big Four)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Large firms want research assistance without sending client facts to a public tool, and want consistent
    tools across a national practice.
  solution: KPMG US describes a GenAI Research Assistant for Navigating Tax that analyses complex questions, from
    corporate restructuring to transaction-specific rules, and returns targeted research with references to statutory
    and case law, used inside its M&A tax practice. In May 2026 KPMG and Anthropic announced Digital Gateway powered
    by Claude, with an initial focus on tax clients, and said KPMG's 276,000 people would have access to Claude.
  outcomes:
  - lever: quality
    description: No measured outcome for the research assistant is published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: KPMG-MA-2025
  - lever: capacity
    description: Announced scale of access to Claude across the firm
    figure: 276,000 people
    measures: KPMG global workforce that the announcement says will have access to Anthropic's Claude suite; an
      access figure, not a usage figure
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - Firm-controlled platform so client data stays in the firm's environment (KPMG describes Digital Gateway as built
    on Azure)
  - Standardised technology stack and consolidated national workflows (KPMG says it standardised before scaling)
  risks_and_guardrails:
  - KPMG describes a human-in-the-loop model in which citations and hyperlinks validate AI outputs and regular training
    helps staff spot inaccuracies
  - ICAEW's director of regulatory policy said some firms have built locked-down internal tools while smaller firms
    would be expected to use public ones, so the firm-built route is not open to most practitioners
  human_checkpoints:
  - Practitioner validates each AI output against the cited authority
  role_evolution: KPMG says M&A tax professionals shift from compliance and transactional tasks to deal-structure
    and advisory work as administrative work is automated.
  evidence_grade: B
  sources:
  - ref: KPMG-MA-2025
    title: How generative AI is transforming mergers and acquisitions tax (article and PDF)
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/how-generative-ai-transforming-mergers-acquisitions-tax.html
    date: 2025-06
    access: full
    locator: '''Tax research with GenAI Research Assistant for Navigating Tax'' and ''Balancing risk and innovation'''
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (KPMG/Anthropic release)
    type: firm
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Opening paragraphs and 'Modernizing work with Claude'
  - ref: KPMGUK-BLUEJ-2024
    title: KPMG UK And Blue J To Launch Generative AI Tool To Address Tax Research Questions
    publisher: Crowdfund Insider
    type: press
    url: https://www.crowdfundinsider.com/?p=221784
    date: '2024-02-22'
    access: full
    locator: 'Opening paragraphs (older foundation: KPMG UK exclusive access to Ask Blue J)'
  - ref: ICAEW-POD-2026
    title: How to use AI in tax ethically, and group audit best practice (podcast transcript, Accountancy Insights)
    publisher: ICAEW
    type: podcast
    url: https://www.icaew.com/insights/podcast/accountancy-insights/how-to-use-ai-in-tax-ethically-and-group-audit-best-practice/transcript
    date: '2026-02-04'
    access: full
    locator: Data security answer, Sophie Wales
  last_reviewed: '2026-10-17'
  notes: Named deployment, no published measurement. The 2024 KPMG UK and Blue J item is outside the 12 to 18 month
    window and is used only to show the earlier alliance; its '90%+ accuracy' figure concerns an older outcome-prediction
    tool and is not used here.
- id: tax-research-advisory-04
  title: First drafts of research memos and advice letters with adviser revision
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Drafting memos and letters from research notes takes days of associate time; partners then review a long
    first draft.
  solution: 'Tax lawyers use an LLM to produce a preliminary structure and draft of a memo or letter from issues
    and authorities supplied by the adviser, who revises and verifies it. Peter Lowy of Nelson Mullins writes that
    his firm is piloting two leading generative AI platforms, and that current output resembles the work of an average-performing
    junior associate: useful for issue spotting and drafts, not ready to send to a client.'
  outcomes:
  - lever: speed
    description: A practitioner asserts that a draft that takes a junior attorney days can often be generated in
      minutes
    figure: none published
    measures: Author's unmeasured assertion in an opinion article; no sample or timing data
    provenance: self-reported
    source_ref: BTAX-LOWY-2026
  prerequisites:
  - Approved enterprise tool; no client confidences in unapproved open-system tools
  - Verification of every authority before the draft leaves the firm
  risks_and_guardrails:
  - OPR Alert 2026-19 treats AI output as a starting point and applies due diligence (10.22) and written-advice
    rules (10.37) to it
  - Drake's executive notes AI 'tends to agree with you', so prompts that embed the desired answer can bias the
    draft
  - 'Responsibility for fake authority falls on the signer: in Clinco the Tax Court judge faulted counsel for citing
    nonexistent cases and warned of sanctions, though none was imposed (JofA analysis)'
  human_checkpoints:
  - Author verifies authorities and quotations against primary sources
  - Supervising partner reviews before client delivery
  role_evolution: Lowy argues the lawyer's work shifts to narrowing options, rejecting weak ideas and owning the
    result, and calls AI proficiency a core competency; ICAEW and OPR both say accountability stays with the member.
  evidence_grade: B
  sources:
  - ref: BTAX-LOWY-2026
    title: Tax Lawyers Must Adapt to AI Now. It's Already Changed the Game (Peter Lowy, Nelson Mullins)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/tax-lawyers-must-adapt-to-ai-now-its-already-changed-the-game
    date: '2026-07-31'
    access: full
    locator: Sections 'Quality' and 'Guardrails'; closing note on firm piloting
  - ref: IRS-OPR-2026
    title: 'Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice'
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Items 1 and 5 (sections 10.22, 10.37)
  - ref: TAXCT-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo.
      2026-16)'
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: Sections 'A recipe for sanctions' and 'AI in tax research and drafting'
  - ref: TAXADV-DRAKE-2025
    title: AI's role in complex tax decisions (advertising supplement, Drake Software)
    publisher: The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/aug/ais-role-in-complex-tax-decisions/
    date: '2025-07-25'
    access: full
    locator: Sapp Q&A
  last_reviewed: '2026-10-17'
  notes: Named firm pilot without measurement. Only one firm-level source; many other firms are likely doing the
    same but publish nothing.
- id: tax-research-advisory-05
  title: Internal knowledge assistant over prior memos, precedent and firm guidance
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Institutional tax knowledge sits in senior practitioners' heads and in scattered memos; vendors say it
    is lost as seniors retire and varies by staff experience.
  solution: An assistant that answers from the firm's own memo library and guidance alongside licensed content,
    so juniors reuse prior positions consistently. Thomson Reuters lists retaining and leveraging institutional
    knowledge and reducing variability in work quality as benefits of agentic research tools; KPMG put its tax knowledge
    management practice leader on a Bloomberg Tax forum panel on AI integration in compliance, provisioning and
    risk.
  outcomes:
  - lever: quality
    description: No measured outcome published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: TR-AGENTICBLOG-2026
  prerequisites:
  - Clean, access-controlled memo repository
  - Clear rules on which prior advice may be reused across clients (confidentiality)
  risks_and_guardrails:
  - 'Cross-client leakage: OPR warns that data generated for one client can be repurposed for another'
  - Prior positions may be stale when law changes; Bloomberg Tax cites outdated guidance as a hallucination driver
  human_checkpoints:
  - Reviewer confirms a retrieved precedent still reflects current law and fits the client's facts
  role_evolution: Knowledge-management teams become owners of the corpus and its quality; seniors review less repeated
    work (vendor framing).
  evidence_grade: C
  sources:
  - ref: TR-AGENTICBLOG-2026
    title: An evolution of tax tools and how agentic AI will shape 2026
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/an-evolution-of-tax-tools-and-how-agentic-ai-will-shape-2026/
    date: '2026-05-01'
    access: full
    locator: Section 'What this transformation means for tax and accounting firms'
  - ref: BTAX-FORUM-2026
    title: Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk
    publisher: Bloomberg Tax
    type: conference
    url: https://pro.bloombergtax.com/?p=17345
    date: '2026-06-10'
    access: full
    locator: Paragraph on the 'Emerging Technologies and AI Integration' panel
  - ref: IRS-OPR-2026
    title: 'Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice'
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Introductory section, client privacy example
  - ref: BTAX-HALLUC-2026
    title: 'AI Hallucinations in Tax: The Risks and How to Mitigate Them'
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/?p=16920
    date: '2026-05-11'
    access: full
    locator: Section 'Why does generative AI hallucinate?'
  last_reviewed: '2026-10-17'
  notes: Vendor positioning plus a conference panel listing; no named firm deployment or outcome found.
- id: tax-research-advisory-06
  title: In-house tax department technical research with licensed AI research tools
  archetype: tax
  module: research-advisory
  function: finance-accounting
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: Corporate tax teams must answer technical questions from the business, auditors and executives without
    outside counsel each time; budgets rose for fewer than half of surveyed departments.
  solution: In-house teams trial licensed research assistants and general enterprise assistants. The TEI Midyear
    2026 programme ran hands-on Tax Labs titled 'AI and Tax Research with Thomson Reuters and Co-Counsel' and 'AI
    and Tax Research with Accordance'. Surveyed corporate tax leaders now expect AI to become central to their workflow
    within one to two years, while actual usage is still low.
  outcomes:
  - lever: capacity
    description: Timeframe in which corporate tax professionals expect AI to become central to workflow
    figure: 1 to 2 years
    measures: Timeframe respondents expect for AI to become a central part of their workflow, in the 2026 Corporate
      Tax Department Technology Report (170 tax leaders surveyed); the article says it was longer in the prior year's
      report
    provenance: vendor-published
    source_ref: TR-CORPTECH-2026
  - lever: risk
    description: In a show-of-hands poll at TEI Tax Tech 2026, few attendees said the tax function owns AI implementation
    figure: 2 of more than 50
    measures: Hands raised when the room was polled on whether the tax function actually owns AI implementation
      at their company; an informal poll reported by Thomson Reuters Institute
    provenance: vendor-published
    source_ref: TEI-TAXTECH-2026
  prerequisites:
  - Named owner for tax AI (the TEI poll suggests many departments lack one)
  - IT and legal agreement on approved tools
  risks_and_guardrails:
  - Silent hallucination and rising token costs were the new concerns TEI attendees raised
  - Deloitte's scenario paper suggests investing in AI validation, model governance and expert-in-the-loop capability
  human_checkpoints:
  - Department reviews AI-assisted conclusions before they go to the CFO, auditors or authorities
  role_evolution: Sala argues corporate tax functions will not shrink much because AI cannot hold culpability and
    the work is tax practice (engagement with authorities, auditors and executives), not form preparation.
  evidence_grade: C
  sources:
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 At a Glance agenda
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Sessions tagged TECH: the two ''TEI Tax Lab: AI and Tax Research'' entries'
  - ref: TR-CORPTECH-2026
    title: Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology
      Report)
    publisher: Thomson Reuters Institute with Tax Executives Institute
    type: survey
    url: https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026/
    date: '2026-03-16'
    access: full
    locator: Sections 'Expectations about AI' and budget paragraph
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard' (poll of more than 50)
  - ref: SALA-TAXNOTES-2026
    title: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Michael V. Sala, Tax Notes State 121:189; abstract
      on TaxProf Blog)
    publisher: Tax Notes / TaxProf Blog
    type: academic
    url: https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
    date: '2026-07-20'
    access: full
    locator: Abstract
  - ref: DELOITTE-TTT3-2026
    title: 'Tax Transformation Trends AI report, Part three: Riding the wave: A framework to plan for AI'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: 'Scenario 4: Tax transformed'
  last_reviewed: '2026-10-17'
  notes: Programme listings and surveys only; no in-house case study with metrics. TR search snippets cite 61% expecting
    AI to accelerate technical research; that figure was not on the page read and is not used as an outcome.
- id: tax-research-advisory-07
  title: AI assistance with tax opinion letters (draft, then verify law, facts and authorities)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Opinion letters require a careful legal analysis tied to stated facts and assumptions, and the signer
    carries penalty-protection and liability consequences.
  solution: A law-firm alert states that AI can be a valuable tool in producing a tax opinion letter, provided the
    responsible practitioner verifies the legal analysis, confirms the transaction facts and replaces any fabricated,
    outdated or inapplicable authorities before delivery.
  outcomes:
  - lever: quality
    description: No deployment or outcome published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: KTS-AI-2026
  prerequisites:
  - Secure, firm-approved AI system
  - Documented verification of each authority
  risks_and_guardrails:
  - OPR says reliance may be unreasonable where the system's logic is opaque and the practitioner cannot evaluate
    the output (10.37)
  - Siva argues AI tools do not qualify for Kovel protection and verification of citations is a non-delegable duty
    (Boyle), so opaque reliance could undermine reasonable-cause defences; his Heppner reference was not checked
    here
  - Hallucinated authority led to an IRC 6662 penalty in a case Siva describes without naming it
  human_checkpoints:
  - Signing practitioner verifies law, facts and every cited authority
  - Second-partner review under firm opinion procedures
  role_evolution: Signer's duty is unchanged; verification and facts-gathering gain weight relative to drafting.
  evidence_grade: D
  sources:
  - ref: KTS-AI-2026
    title: 'Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season'
    publisher: Kilpatrick Townsend & Stockton LLP
    type: firm
    url: https://ktslaw.com/insights/alert/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season
    date: '2026-09-29'
    access: full
    locator: Paragraph beginning 'For a tax practitioner, AI can be a valuable tool'
  - ref: IRS-OPR-2026
    title: 'Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice'
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Item 5, section 10.37
  - ref: BTAX-SIVA2-2026
    title: Don't Trust AI, Always Verify. Tax Law Still Needs Humans, Pt. 2 (Pramod Kumar Siva)
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/tax-insights-and-commentary/dont-trust-ai-always-verify-tax-law-still-needs-humans-pt-2
    date: '2026-04-30'
    access: full
    locator: Sections 'Non-delegable duty to verify' and 'The Kovel gap'
  last_reviewed: '2026-10-17'
  notes: 'Idea. Discussed by a law-firm alert and a practitioner article; no firm describes an AI-drafted opinion
    in production. Label: idea.'
- id: tax-research-advisory-08
  title: Adversarial pressure-testing of a tax position (AI argues the other side or plays the examiner)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Positions are often tested only by the author and one reviewer; weaknesses a revenue agent or court would
    see may be missed.
  solution: Adviser asks a model to argue the opposite conclusion, list what an IRS examiner would flag and pressure-test
    the arguments. Lowy lists pressure-testing arguments and exploring planning alternatives as strengths of the
    tools; CPA Practice Advisor's playbook suggests clients ask AI to argue the opposite and identify what an auditor
    would flag.
  outcomes:
  - lever: quality
    description: No outcome published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: BTAX-LOWY-2026
  prerequisites:
  - Approved tool; facts abstracted so no confidential client detail leaves approved systems
  risks_and_guardrails:
  - Lowy notes the tools are better at generating ideas than screening out bad ones, so the adviser must filter
  - Drake's executive says AI tends to agree with the user, which weakens an adversarial test unless prompted to
    oppose
  human_checkpoints:
  - Adviser decides which objections are credible and updates the memo
  role_evolution: The adviser acts as filter and decision-maker over a larger set of machine-generated objections.
  evidence_grade: D
  sources:
  - ref: BTAX-LOWY-2026
    title: Tax Lawyers Must Adapt to AI Now. It's Already Changed the Game (Peter Lowy, Nelson Mullins)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/tax-lawyers-must-adapt-to-ai-now-its-already-changed-the-game
    date: '2026-07-31'
    access: full
    locator: Section 'Quality' (brainstorming and filtering)
  - ref: CPAPA-FIRSTSTOP-2025
    title: 'AI Is Now a First Stop for Tax and Investing Questions: CPAs Need a Playbook Fast'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2025/10/29/ai-is-now-a-first-stop-for-tax-and-investing-questions-cpas-need-a-playbook-fast/171939/
    date: '2025-10-29'
    access: full
    locator: Bullets 'Treat AI's response as a starting point'
  - ref: TAXADV-DRAKE-2025
    title: AI's role in complex tax decisions (advertising supplement, Drake Software)
    publisher: The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/aug/ais-role-in-complex-tax-decisions/
    date: '2025-07-25'
    access: full
    locator: Sapp Q&A
  last_reviewed: '2026-10-17'
  notes: Idea. Recommended by practitioners; no firm reports using it or measures effect.
- id: tax-research-advisory-09
  title: Planning-alternative ideation and anti-abuse screening of structures
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Surfacing alternative structures and testing them against anti-abuse doctrines is slow and depends on
    a few senior people.
  solution: Models generate alternative planning approaches and probe them. Blair-Stanek, Holzenberger and Van Durme
    report that LLM-based reasoning identified an apparently novel tax-minimisation strategy and argue it could
    help tax agencies spot abuse. Practitioners caution that models cannot assess economic substance or step-transaction
    and can script steps a court would collapse.
  outcomes:
  - lever: quality
    description: 'Research result, not a deployment: abstract reports an entirely novel tax strategy was identified;
      no rate or count is given in the abstract'
    figure: none published
    measures: n/a
    provenance: independent
    source_ref: JHU-TAXABUSE-2025
  prerequisites:
  - Expert reviewer able to test the structure against substance doctrines
  risks_and_guardrails:
  - 'Siva: AI can build a ''technically perfect sham'' that meets the text but fails substance; he links reliance
    to IRC 6662 and 6700 exposure'
  - 'ICAEW podcast: a member cannot say the AI came up with a contrived scheme; PCRT planning standards still apply'
  - Siva also describes 'jurisdictional flattening', where federal training data dominates state and international
    answers
  human_checkpoints:
  - Senior adviser tests every AI-proposed structure against economic substance, step transaction and PCRT or Circular
    230 standards
  role_evolution: Planners spend more time dismantling and stress-testing candidate structures than inventing them.
  evidence_grade: D
  sources:
  - ref: JHU-TAXABUSE-2025
    title: Can LLMs Identify Tax Abuse? (Blair-Stanek, Holzenberger, Van Durme; arXiv 2508.20097, v2 21 Jan 2026)
    publisher: arXiv
    type: academic
    url: https://arxiv.org/abs/2508.20097
    date: '2025-08-10'
    access: full
    locator: Abstract
  - ref: BTAX-SIVA1-2026
    title: Don't Trust AI, Always Verify. Tax Law Still Needs Humans, Pt. 1 (Pramod Kumar Siva)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/dont-trust-ai-always-verify-tax-law-still-needs-humans-pt-1-1
    date: '2026-04-28'
    access: full
    locator: Section 'AI Literalism vs. Judicial Doctrine'
  - ref: ICAEW-POD-2026
    title: How to use AI in tax ethically, and group audit best practice (podcast transcript, Accountancy Insights)
    publisher: ICAEW
    type: podcast
    url: https://www.icaew.com/insights/podcast/accountancy-insights/how-to-use-ai-in-tax-ethically-and-group-audit-best-practice/transcript
    date: '2026-02-04'
    access: full
    locator: Answer on professional behaviour
  - ref: BTAX-LOWY-2026
    title: Tax Lawyers Must Adapt to AI Now. It's Already Changed the Game (Peter Lowy, Nelson Mullins)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/tax-lawyers-must-adapt-to-ai-now-its-already-changed-the-game
    date: '2026-07-31'
    access: full
    locator: Section 'Quality'
  last_reviewed: '2026-10-17'
  notes: Idea, with an academic proof of concept on the authority side. No planning firm describes using AI for
    structuring in production.
- id: tax-research-advisory-10
  title: Statutory and legislative-history synthesis without agency deference
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: After Loper Bright, advisers may need to build the case for a statutory reading from legislative history,
    committee reports and floor debate without relying on IRS deference, which is large-volume reading work.
  solution: Siva writes that a retrieval-augmented system can digest a legislative corpus in seconds, but the burden
    of interpretation stays with the lawyer and any hallucinated Senate report or Treasury explanation would be
    irreparable.
  outcomes:
  - lever: speed
    description: No outcome published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: BTAX-SIVA1-2026
  prerequisites:
  - Official legislative records indexed for retrieval
  - Verification against the official record
  risks_and_guardrails:
  - Unverified secondary sources can corrupt the record
  - Models may not distinguish dicta from holdings or binding from persuasive authority
  human_checkpoints:
  - Lawyer reads every record cited for the statutory reading
  role_evolution: Associates read less raw history and verify more synthesised history.
  evidence_grade: D
  sources:
  - ref: BTAX-SIVA1-2026
    title: Don't Trust AI, Always Verify. Tax Law Still Needs Humans, Pt. 1 (Pramod Kumar Siva)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/dont-trust-ai-always-verify-tax-law-still-needs-humans-pt-1-1
    date: '2026-04-28'
    access: full
    locator: Section 'Epistemic Instability Post-Loper Bright'
  last_reviewed: '2026-10-17'
  notes: Idea from a single practitioner article; no deployment found.
- id: tax-research-advisory-11
  title: Citation verification and AI-use documentation in the research file
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Fabricated or misdescribed authorities are the main failure mode of AI-assisted research, and courts
    and regulators say the signer is responsible. Reviewers cannot spot a plausible citation by eye.
  solution: Check every authority in a draft against primary sources, by a second reviewer or an automated reference
    checker, and record prompts, how outputs were verified and who reviewed them. Damien Charlotin, who runs a database
    of hallucination decisions, says he built an automated reference checker (PelAIkan) that detects hallucinations.
    Firm-policy advice from Aon in the Journal of Accountancy asks staff to document prompts, verification and reviewer
    in the client file.
  outcomes:
  - lever: risk
    description: A database of court and tribunal decisions that address hallucinated content shows how widespread
      the failure is
    figure: 2,199 cases identified (as of 16 Oct 2026)
    measures: Decisions worldwide, in all areas of law, in which a court or tribunal addressed hallucinated content
      by a party; not tax-only and not a rate
    provenance: independent
    source_ref: CHARLOTIN-DB-2026
  - lever: risk
    description: US Tax Court judge says how often he has seen hallucinated citations in filings
    figure: fewer than a dozen; no sanctions imposed as of March 2026
    measures: Instances of hallucinated case citations Judge Holmes said he had seen in Tax Court filings, per a
      Bloomberg interview
    provenance: independent
    source_ref: BLAW-TAXCT-2026
  prerequisites:
  - Access to primary-source databases for checking
  - A firm AI policy that defines the verification record
  risks_and_guardrails:
  - No performance figures are published for PelAIkan, and the checker is built for legal decisions, not tax
  - A checker can confirm a case exists but not that it supports the proposition; in Thomas the case names were
    real but the cited reporters and propositions were wrong
  - 'Control dilution: Werfel''s preparer register warns that faster workflows can make partner review less rigorous
    in practice'
  human_checkpoints:
  - Second reviewer or checker confirms existence and support for each authority
  - Signing practitioner certifies the record
  role_evolution: Cite-checking becomes a recorded step with an owner; Werfel's register calls for sign-off that
    requires genuine analysis, not just approval.
  evidence_grade: C
  sources:
  - ref: CHARLOTIN-DB-2026
    title: AI Hallucination Cases Database (Damien Charlotin)
    publisher: Damien Charlotin
    type: academic
    url: https://www.damiencharlotin.com/hallucinations/
    date: '2026-10-16'
    access: full
    locator: 'Header text: count and PelAIkan'
  - ref: BLAW-TAXCT-2026
    title: Tax Court Navigates AI Misuse Rules for Self-Represented Filers
    publisher: Bloomberg Tax Daily Tax Report
    type: press
    url: https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers
    date: '2026-03-20'
    access: full
    locator: Section 'Feeling Our Way' and 'Arrow in Quiver'
  - ref: JOFA-AIPOLICY-2026
    title: Drafting an AI policy that actually works (Professional Liability Spotlight, Nicole L. Graham, Aon)
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/
    date: '2026-07-01'
    access: full
    locator: Sections 'Quality, Accuracy, and Professional Liability' and 'Documentation and Supervision'
  - ref: TAXCT-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo.
      2026-16)'
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: Section 'Practical risk management for tax practitioners'
  - ref: AICPA-WERFEL-2026
    title: 'A Risk Framework for the Use of AI in Tax Administration and Preparation: appendices (Appendix C: AI
      Risk Register for Tax Preparers)'
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C, risks 1, 4 and 6
  - ref: BTAX-LOWY-2026
    title: Tax Lawyers Must Adapt to AI Now. It's Already Changed the Game (Peter Lowy, Nelson Mullins)
    publisher: Bloomberg Tax (Tax Management Memo)
    type: press
    url: https://news.bloombergtax.com/tax-management-memo/tax-lawyers-must-adapt-to-ai-now-its-already-changed-the-game
    date: '2026-07-31'
    access: full
    locator: Discussion of Thomas v. Commissioner
  last_reviewed: '2026-10-17'
  notes: 'Vendor-level claim for the automated tool; the surrounding practices are recommendations. Adjacent: a
    preregistered 2024 study found legal-research tools hallucinated 17% to 33% of the time (MAGESH-2024).'
- id: tax-research-advisory-12
  title: 'M&A tax due diligence: contract review and first-draft diligence report'
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Tax diligence means reading long stock purchase and partnership agreements and writing a report to a
    deadline, leaving less time for structuring and hidden-risk analysis.
  solution: KPMG US describes tools that parse lengthy SPAs and partnership agreements, highlight non-standard clauses
    and compare language with baseline expectations, and a Mergers and Acquisitions Tax Reporting System that drafts
    an initial report from jurisdiction, transaction type and client constraints, which professionals then build
    on. KPMG's M&A tax leader Jim Tod is quoted saying client feedback was a catalyst.
  outcomes:
  - lever: speed
    description: KPMG's web page says the firm is compressing weeks of tax analysis into minutes
    figure: weeks to minutes
    measures: Marketing text on KPMG's page; it does not say which analysis, how measured or over what sample
    provenance: self-reported
    source_ref: KPMG-MA-2025
  prerequisites:
  - Virtual data room with digital, traceable documents
  - Standardised tools and templates across the national practice
  risks_and_guardrails:
  - KPMG describes human-in-the-loop validation with citations and hyperlinks and regular training on spotting inaccuracies
  - Hallucinated or missed clauses can understate exposure; no error rate is published
  human_checkpoints:
  - Practitioner builds on the draft with assessments and recommendations
  - Practitioner validates AI output against the source document
  role_evolution: KPMG says practitioners spend less time on repetitive drafting and more on deal structure, financial
    modelling and hidden risks.
  evidence_grade: B
  sources:
  - ref: KPMG-MA-2025
    title: How generative AI is transforming mergers and acquisitions tax (article and PDF)
    publisher: KPMG US
    type: firm
    url: https://kpmg.com/us/en/articles/2025/how-generative-ai-transforming-mergers-acquisitions-tax.html
    date: 2025-06
    access: full
    locator: 'Section ''GenAI in action: Key use cases in M&A tax'' and ''Balancing risk and innovation''; web page
      opening paragraph'
  - ref: MONDAQ-HORIZON-2026
    title: New Trends And Challenges In Tax Due Diligence On The M&A Market (Horizon Solutions Kft., Hungary)
    publisher: Mondaq
    type: firm
    url: https://webiis10.mondaq.com/tax-authorities/1737066/new-trends-and-challenges-in-tax-due-diligence-on-the-ma-market
    date: '2026-01-28'
    access: full
    locator: Section 'The Rise of Artificial Intelligence (AI)'
  last_reviewed: '2026-10-17'
  notes: 'Named firm and named tools; no published measurement. Date: the PDF metadata shows June 2025 while the
    web page''s JSON-LD shows 2026-07-29 (likely a page update); 2025-06 is used. A Hungarian advisory firm (Horizon
    Solutions, 2026-01-28) says AI tools process contracts and invoices to speed diligence, but gives no data.'
- id: tax-research-advisory-13
  title: Agent-led tax due diligence producing a risk assessment (PE, permanent establishment, intercompany)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Deal tax diligence takes weeks of document analysis across entities and jurisdictions.
  solution: V7 markets an AI agent that analyses financial structures, transfer pricing arrangements, entity hierarchies
    and regulatory filings to identify permanent establishment risks, intercompany issues and compliance gaps, and
    delivers a risk assessment for legal and finance teams.
  outcomes:
  - lever: speed
    description: Vendor page compares traditional and agent time
    figure: 3-4 weeks to 2-3 days; 'average time saved 90%'
    measures: Time comparison on V7's page between the 'traditional way' and V7 Go agents; the demo is labelled
      'Tax Diligence - Meridian Acquisition'; method and sample are not stated
    provenance: vendor-published
    source_ref: V7-TAXDD-2026
  prerequisites:
  - Complete data room and entity charts
  - Reviewer able to test the risk list
  risks_and_guardrails:
  - No accuracy data published; a missed PE or intercompany issue creates unpriced exposure
  human_checkpoints:
  - Deal tax lead reviews the risk assessment before it informs price or structure
  role_evolution: Diligence staff shift from document reading to exception review (vendor framing).
  evidence_grade: C
  sources:
  - ref: V7-TAXDD-2026
    title: AI Tax Due Diligence Agent (V7 Go product page)
    publisher: V7
    type: vendor
    url: https://www.v7labs.com/agents/ai-tax-due-diligence-agent
    date: '2026-10-17'
    access: full
    locator: Hero text and 'Time comparison' block; page undated, date is retrieval date
  last_reviewed: '2026-10-17'
  notes: Vendor claim only. No named customer or outcome found.
- id: tax-research-advisory-14
  title: Tax-law change monitoring and client-specific impact agents
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - research-synthesis
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: After major legislation advisers must track guidance across jurisdictions and explain the effect to each
    client, which is repetitive and urgent.
  solution: KPMG US's tax vice chair says building an AI agent to help clients adjust to changing tax regulations
    used to take weeks and multiple tools, and takes minutes with Claude Cowork and Managed Agents inside KPMG Digital
    Gateway. Bloomberg Tax also describes an AI Assistant in its Compliance Tracker that summarises and analyses
    filings.
  outcomes:
  - lever: speed
    description: KPMG executive on time to build a client agent for changing tax rules
    figure: weeks to minutes
    measures: Time to build an agent that helps clients adjust to changing tax regulations (not time to run an analysis),
      per Rema Serafi, KPMG US Vice Chair, Tax; no sample or method given
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - Platform where firm tax insights, proprietary tools and client data sit together
  - Monitored authority feeds
  risks_and_guardrails:
  - A stale or wrong monitored rule propagates to every client agent
  - KPMG says work is guided by its Trusted AI framework; no further detail
  human_checkpoints:
  - Tax professional reviews agent output before advice reaches the client
  role_evolution: Professionals and clients build agents inside the platform; the adviser's job moves toward specifying
    and supervising them.
  evidence_grade: C
  sources:
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (KPMG/Anthropic release)
    type: firm
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Quote from Rema Serafi
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: Bullet 'AI Assistant in Compliance Tracker'
  last_reviewed: '2026-10-17'
  notes: Announcement-level; the compliance-tracker element is routed to the compliance module.
- id: tax-research-advisory-15
  title: AI-drafted client emails, letters and explanations, reviewed by the adviser
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - client-interaction
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Explaining technical conclusions in plain language and answering client follow-ups is time-consuming;
    clients also arrive with AI-generated questions.
  solution: Advisers use a model to draft client emails and personalised letters, then edit. A 2024 UK survey found
    drafting emails and other communication tasks among planned priorities; a Drake Software executive in an advertising
    supplement says many tax professionals start with emails and client letters.
  outcomes:
  - lever: experience
    description: Share of surveyed UK tax professionals listing client communication drafting as a priority for
      planned generative-AI use
    figure: 80%
    measures: Respondents among the 446 UK tax professionals surveyed by Tolley (2024) who listed drafting emails
      or other communication-based tasks as a priority; a statement of plans, not usage
    provenance: vendor-published
    source_ref: TOLLEY-2024
  prerequisites:
  - No client-identifying detail in public tools (IRC 7216)
  - Tone and content check
  risks_and_guardrails:
  - 'ICAEW: a generated letter to HMRC can mis-state a point or strike the wrong tone'
  - 'JofA: no federal rule mandates disclosure of AI use to clients, but some states require some disclosure and
    voluntary disclosure is suggested'
  human_checkpoints:
  - Adviser reads and edits every client-facing draft
  role_evolution: Less typing, more review; OPR says savings should be reflected in billing.
  evidence_grade: C
  sources:
  - ref: TOLLEY-2024
    title: Trustworthiness is key to adoption of AI in tax, says Tolley (survey of 446 UK tax professionals)
    publisher: Tax Journal (LexisNexis)
    type: survey
    url: https://www.taxjournal.com/articles/trustworthiness-is-key-to-adoption-of-ai-in-tax-but-pricing-potentially-problematic-says-tolley
    date: '2024-06-26'
    access: full
    locator: Paragraph on priorities (91%, 87%, 80%); outside window, used as foundation
  - ref: TAXADV-DRAKE-2025
    title: AI's role in complex tax decisions (advertising supplement, Drake Software)
    publisher: The Tax Adviser (AICPA)
    type: vendor
    url: https://www.thetaxadviser.com/issues/2025/aug/ais-role-in-complex-tax-decisions/
    date: '2025-07-25'
    access: full
    locator: Opening paragraph
  - ref: ICAEW-POD-2026
    title: How to use AI in tax ethically, and group audit best practice (podcast transcript, Accountancy Insights)
    publisher: ICAEW
    type: podcast
    url: https://www.icaew.com/insights/podcast/accountancy-insights/how-to-use-ai-in-tax-ethically-and-group-audit-best-practice/transcript
    date: '2026-02-04'
    access: full
    locator: Answer on professional behaviour
  - ref: JOFA-DISCLOSE-2025
    title: Should I disclose my use of gen AI to clients?
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/
    date: '2025-04-01'
    access: full
    locator: Paragraphs on disclosure requirements
  last_reviewed: '2026-10-17'
  notes: 'Capped at C: planning survey sponsored by a vendor (2024) and an advertising supplement.'
- id: tax-research-advisory-16
  title: Advising clients who bring AI-generated tax answers or positions
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - client-interaction
  - expert-judgment
  pattern: service-agent-escalation
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Clients and taxpayers increasingly ask a chatbot first and then act on or bring the answer to the adviser,
    who must separate sound from unsound points.
  solution: CPA Practice Advisor recommends advisers counsel clients to ask AI for primary sources, assumptions
    and step-by-step calculations, log AI interactions, avoid pasting personal data into public models, and to state
    in engagement letters that the firm's responsibility covers only advice it gives directly.
  outcomes:
  - lever: risk
    description: No measured effect on advisory workload or quality is published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CPAPA-FIRSTSTOP-2025
  prerequisites:
  - Engagement-letter language on AI
  - A standard intake question about client AI use
  risks_and_guardrails:
  - The article says the IRS warns that an AI-advised mistake on a return still falls on the taxpayer
  - Report of a UK tribunal case (Elden, January 2026) where a skeleton argument prepared by accountants had insufficient
    accuracy checks (search-only coverage)
  human_checkpoints:
  - Adviser reviews the client's AI output and its sources before adopting any position
  role_evolution: Advisers add a triage and correction role for client-generated AI content and extend the engagement
    letter to cover it.
  evidence_grade: D
  sources:
  - ref: CPAPA-FIRSTSTOP-2025
    title: 'AI Is Now a First Stop for Tax and Investing Questions: CPAs Need a Playbook Fast'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2025/10/29/ai-is-now-a-first-stop-for-tax-and-investing-questions-cpas-need-a-playbook-fast/171939/
    date: '2025-10-29'
    access: full
    locator: Bullets on provenance, starting point, safe practices and engagement letters
  - ref: ACCOUNTINGWEB-ELDEN-2026
    title: Tribunal slams careless AI use by advisers (Elden v HMRC, FTT)
    publisher: AccountingWEB
    type: community
    url: https://www.accountingweb.co.uk/tax/hmrc-policy/tribunal-slams-careless-ai-use-by-advisers
    date: 2026-01
    access: search-only
    locator: Search extract only; not opened
  last_reviewed: '2026-10-17'
  notes: 'Idea. The article also cites a Pearl.com August 2025 survey (10% of US adults acted on AI tax guidance
    in the prior 30 days) and a Taxpayer Advocate statement of up to 50% inaccuracy on complex questions; both are
    second-hand through a promotional piece and were not verified, so they are not used as outcomes. Label: idea.'
- id: tax-research-advisory-17
  title: Value- and outcome-based pricing for AI-assisted advisory work
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types:
  - coordination-scheduling
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: AI shortens research and drafting time, which erodes revenue under hourly billing, while IRS OPR says
    billing for manual time not spent may violate the unconscionable-fee rule.
  solution: Top accounting firms are developing value- and outcome-based pricing for corporate clients; RSM US says
    it uses multiple pricing models and is increasingly billing on value. OPR Alert 2026-19 says cost savings should
    be passed on openly, and the AICPA has asked IRS to clarify language that does not appear to allow value pricing.
  outcomes:
  - lever: cost
    description: RSM partner's illustration of the pricing question (hypothetical)
    figure: 20 hours to 10 hours (illustrative)
    measures: Illustrative example in the interview of hours for a tax advisory report if generative AI is used
      and outputs are checked; not an observed result
    provenance: self-reported
    source_ref: BTAX-PRICING-2026
  - lever: cost
    description: 'UK survey: share expecting bills to fall because of generative AI'
    figure: 45% of in-house teams; 35% of private practice
    measures: In-house respondents expecting bills to be reduced; private-practice respondents agreeing their clients
      would expect a reduction (Tolley, 446 UK tax professionals, 2024)
    provenance: vendor-published
    source_ref: TOLLEY-2024
  prerequisites:
  - Pricing models not tied to hours
  - Client agreement on scope and outputs
  risks_and_guardrails:
  - 'OPR 10.27: do not bill manual time not spent; disclose AI activity and credit cost reductions'
  - AICPA says OPR's language overlooks implementation costs and risks and does not appear to allow value pricing
  human_checkpoints:
  - Engagement partner sets fee basis; billing review against actual work
  role_evolution: TR reports about one third of tax and audit professionals say their firms have not adapted commercial
    models; PwC US's tax leader says time matters less.
  evidence_grade: B
  sources:
  - ref: BTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: Sections 'Pricing Dilemma' and opening paragraphs
  - ref: IRS-OPR-2026
    title: 'Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice'
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Item 2, section 10.27(a)
  - ref: AICPA-CART-2026
    title: AICPA, former IRS commissioner to lead initiative on AI in tax
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
    date: '2026-09-23'
    access: full
    locator: Final paragraphs on AICPA seeking clarification
  - ref: KTS-AI-2026
    title: 'Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season'
    publisher: Kilpatrick Townsend & Stockton LLP
    type: firm
    url: https://ktslaw.com/insights/alert/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season
    date: '2026-09-29'
    access: full
    locator: Paragraph on section 10.27
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: Paragraph on financial pressures
  - ref: TOLLEY-2024
    title: Trustworthiness is key to adoption of AI in tax, says Tolley (survey of 446 UK tax professionals)
    publisher: Tax Journal (LexisNexis)
    type: survey
    url: https://www.taxjournal.com/articles/trustworthiness-is-key-to-adoption-of-ai-in-tax-but-pricing-potentially-problematic-says-tolley
    date: '2024-06-26'
    access: full
    locator: Pricing paragraph; outside window
  last_reviewed: '2026-10-17'
  notes: 'Pattern: other (a commercial-model change, not an AI workflow). Named firms say they are exploring or
    using value pricing, but no AI-specific pricing outcome is published; hence B with piloting maturity.'
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Scope the question and gather facts** with the client or business owner (client-interaction; expert-judgment).
2. **Research authority**: statute, regulations, rulings, cases, treaties and secondary sources (research-synthesis). Largest AI footprint today (use cases 01, 02, 03, 06, 10).
3. **Analyse and conclude** at a stated confidence level, including planning alternatives and anti-abuse screening (expert-judgment) (use cases 08, 09).
4. **Draft** the memo, advice letter or opinion (document-production) (use cases 04, 07, 15).
5. **Review and sign off**: cite-check, partner review, firm quality control (review-assurance) (use case 11).
6. **Communicate and handle follow-ups** from clients, business units, auditors (client-interaction) (use cases 15, 16).
7. **Transaction work**: diligence document review, issue spotting, structuring and the diligence report (review-assurance; document-production) (use cases 12, 13).
8. **Monitor law changes and keep knowledge current** (research-synthesis) (use cases 05, 14).
9. **Scope and price the engagement** (coordination-scheduling) (use case 17).

### Common pain points

- Slow, costly research platforms: in a vendor-co-produced survey of 150+ practitioners, 81.3% still turn to Google for tax research, with complaints of being time-consuming (42%), expensive (42%) and hard to navigate (37%) (CPAPA-BLUEJ-2025).
- Shadow AI: more than one third of tax and audit professionals admit using unauthorized AI tools (TR-FOP-2026); 54.4% of surveyed practitioners used AI for tax research while 33.1% of firms had formally adopted AI tools (2025 Blue J/CPA.com data, CPAPA-BLUEJ-2025).
- Review capacity: TEI attendees said they struggle to review rising volumes of work when errors are polite, quiet and technical (TEI-TAXTECH-2026).
- Department resourcing: fewer than half of surveyed corporate tax departments received a budget increase last year, and 170 tax leaders reported a gap between what they want to do and what their tools allow (TR-CORPTECH-2026).
- Real-time authority data: TRI reports that tax authorities in mature continuous-transaction-control jurisdictions arrive at audits with data already analysed, compressing corporate roadmaps to 12 to 18 months (TRI-TEIAUDITOR-2026). Routed to indirect-tax and tax-data-technology.

### Metrics and benchmarks (with measures and sources)

| Metric | What it measures | Provenance | Source |
|---|---|---|---|
| 81% | Tax and audit professionals saying they now use AI tools regularly (Thomson Reuters Future of Professionals 2026; sample size for the tax subset not stated in the article) | vendor-owned survey | TR-FOP-2026 |
| More than 1 in 4; almost 1 in 3 | Professionals who would not accept a job at a firm lacking professional-grade AI; professionals who would consider leaving if AI expectations are unmet within two years | vendor-owned survey | TR-FOP-2026 |
| 34% (from 21%); 19% | Tax firms deploying GenAI at an organizational level; share of those firms measuring ROI (the article's wording) | Thomson Reuters-authored | CPAPA-TR-2026 |
| 14%; 80% | Tax firms saying agentic AI is currently part of workflow; share expecting it central within five years | Thomson Reuters-authored | CPAPA-TR-2026 |
| 78%; 6%; 32% | Corporate clients of professional-services providers (not tax-only) rating AI-enabled quality very important or essential; clients saying most or all providers deliver; clients who have reconsidered or plan to reconsider a firm seen as falling behind on AI | vendor-owned survey | TR-ACCURACY-2026 |
| 66%; 79%; 71% | UK tax professionals using or planning to use AI; with concern over free public tools; comfortable with tools grounded in authoritative content (446 respondents, June 2024; older) | LexisNexis/Tolley survey | TOLLEY-2024 |
| 17% to 33% | Hallucination rate of three retrieval-based legal research tools in a preregistered study (adjacent: legal, 2024) | independent | MAGESH-2024 |
| 2,199 | Decisions worldwide addressing hallucinated content by a party (all fields, 16 Oct 2026) | independent | CHARLOTIN-DB-2026 |
| 16% | Firms "very confident" they can adapt to AI over three years, per the 2025 PCPS MAP survey as cited by an Aon risk consultant | secondary citation | JOFA-AIPOLICY-2026 |

**Quality evidence:** none found for this module's use. There is no published error rate, override rate or parallel-run result for CoCounsel Tax, Blue J, Bloomberg Tax AI, CCH tools or Big Four assistants, and no independent comparison of them. Vendors cite verifiable citations and retrieval grounding (BTAX-HALLUC-2026, BLUEJ-2026) but publish no accuracy figures in the pages read. The Magesh et al. study is the only independent number and it concerns legal research tools.

### Guardrails and regulatory points

- **IRS Circular 230 as applied by OPR Alert 2026-19:** due diligence (10.22), fees (10.27), competence (10.35), firm procedures (10.36), written advice (10.37), and IRC 6713/7216 for taxpayer information; AI output is a starting point (IRS-OPR-2026; JOFA-OPR-2026).
- **AICPA SSTS Section 1.4 (reliance on tools):** members may rely on tools, remain responsible for the work product, and may use AI to enhance but not supplant judgment (TAXCT-CLINCO-2026, section on Circular 230 and SSTSs).
- **UK PCRT:** five fundamental principles applied to AI; accountable regardless of AI use; caution with AI-suggested planning that may breach PCRT standards; confidentiality of client data (PCRT-AI-2026; ICAEW-POD-2026).
- **Courts:** Rule 11 and Tax Court Rule 33 apply to filings; UK Upper Tribunal says parties are responsible for the accuracy of what they present and may face sanctions (BLAW-TAXCT-2026; BTAX-LOWY-2026; ICAEW-GUNNARSSON-2025).
- **Privilege and confidentiality:** Siva argues that public AI tools do not fit the Kovel doctrine and that terms of service allowing reuse of prompts can destroy the expectation of confidentiality (BTAX-SIVA2-2026). This is a single practitioner's argument; his *Heppner* reference was not verified.
- **Disclosure:** no federal law or professional standard in the sources mandates disclosure of AI use to clients; some states require some disclosure; JofA suggests voluntary disclosure and engagement-letter language (JOFA-DISCLOSE-2025).
- **Risk framework (voluntary):** Werfel's preparer risk register includes hallucinated advice, incorrect document extraction, failure of professional judgment, control dilution, malpractice exposure and liability ambiguity (vendor terms may disclaim liability for tax advice) (AICPA-WERFEL-2026, Appendix C). AICPA says AI is moving too fast for lasting standards (ACCTODAY-CART-2026).
- **Scope beyond returns:** law-firm commentary reads the OPR alert as applying to corporate, payroll and plan-related tax advice and memoranda, not only to Form 1040 work (NATLAW-OPR-2026).
- **Firm AI policy elements** recommended in the profession's press: approved-tool list, AI lead or committee, de-identification, documented prompts, verification and reviewer, training, engagement-letter language (JOFA-AIPOLICY-2026).

### Frontier signals (dated)

- **9 Mar 2026:** Bloomberg Tax shows Deep Thinking Mode, which plans and executes research for multi-step questions (BTAX-TOOLS-2026).
- **1 May 2026:** Thomson Reuters frames tax research as moving from search-and-find to reason-and-act (TR-AGENTICBLOG-2026).
- **20 May 2026:** KPMG and Anthropic announce Digital Gateway powered by Claude with an initial focus on tax clients (KPMG-ANTHROPIC-2026).
- **Mar 2026:** Tax Court Judge Holmes says the court is "feeling our way in the dark" about AI rules and doubts a no-AI certification would make sense; sanctions so far absent (BLAW-TAXCT-2026).
- **Apr 2026:** Siva proposes amending Circular 230 section 10.22 and a Tax Court standing order requiring certification of verified citations (BTAX-SIVA2-2026). A proposal by one practitioner, not an adopted plan.
- **Mar to Sep 2026:** Werfel framework presented at Duke (26 Mar), published, then the Council on AI Risk in Tax (CART) announced in a 23 Sep 2026 report to test and refine it (TAXPROF-WERFEL-2026; AICPA-CART-2026).
- **16 Mar 2026:** corporate tax leaders now expect AI to be central to workflow within one to two years (TR-CORPTECH-2026).
- **Jul 2026 (PDF metadata date):** Deloitte's scenario paper crosses a company's AI adoption with its tax authority's AI progress and suggests splitting planning between largely automated tax operations and human advisory (DELOITTE-TTT3-2026).
- **21 Jul 2026:** TR's paper sets out three paths for firms: elevate, scale or reimagine (TR-FOP-2026).
- **Jan to Jun 2026 events:** AI is now a hands-on lab format (TEI Midyear, Mar), a task-force town hall (ABA Tax Section, May) and a policy topic with Treasury, OpenAI and a Big Four firm on one stage (D.C. Bar, Jan) (TEI-MIDYEAR-2026; ABA-MAYMTG-2026; DCBAR-TAX-2026). Conference agendas show topics, not findings. IBFD's seminar at IFA Lisbon (6 Oct 2025) put generative AI for tax research and compliance on the programme with the Blue J CEO among the speakers (IFA-LISBON-2025).

### Workforce and role effects

- Talent pressure: more than a quarter of surveyed tax and audit professionals would not take a job at a firm lacking professional-grade AI; TR's paper says to define the role of early-career staff so juniors still build judgment (TR-FOP-2026).
- Reviewer role grows: Werfel's register flags a junior associate accepting a confident-sounding output and partners spending less time per return (AICPA-WERFEL-2026). Lowy writes that overseeing AI output, which he equates to first-year associate quality, becomes part of the job (BTAX-LOWY-2026).
- Headcount: Sala argues corporate tax teams will not shrink much because they do tax practice, not form preparation, and AI cannot bear culpability (SALA-TAXNOTES-2026).
- New roles named: an AI lead or committee in firms (JOFA-AIPOLICY-2026); tax knowledge management practice leaders on AI panels (BTAX-FORUM-2026).
- A Blue J-sponsored Taxposium 2026 session promises to explain the "hyper-augmented" practitioner (NATP-TAXPOSIUM-2026); this is sponsor language.

### Objections and concerns practitioners raise

- **Silent, polite failure:** AI fails quietly and plausibly; the room at TEI Tax Tech heard an agent say it had not opened the file (TEI-TAXTECH-2026).
- **Hallucinated authority and its consequences:** sanction risk, penalties, loss of credibility (BTAX-HALLUC-2026; TAXCT-CLINCO-2026; BTAX-SIVA1-2026).
- **Automation bias and sycophancy:** ICAEW warns against assuming the computer is right; Drake's executive says AI tends to agree with the user (ICAEW-POD-2026; TAXADV-DRAKE-2025).
- **Doctrinal mismatch:** models struggle with economic substance, step transaction and binding versus persuasive authority; "jurisdictional flattening" toward federal rules (BTAX-SIVA1-2026).
- **Confidentiality and privilege** (IRC 7216; Kovel) (IRS-OPR-2026; BTAX-SIVA2-2026).
- **Billing and pricing conflict** between OPR's fee guidance and the AICPA's view (IRS-OPR-2026; AICPA-CART-2026).
- **Liability gap with vendors** whose terms may disclaim responsibility for tax advice (AICPA-WERFEL-2026, risk 7 and 8).
- **No owner and no measurement:** tax rarely owns AI; most firms deploying do not measure ROI (TEI-TAXTECH-2026; CPAPA-TR-2026).
- **Quality ceiling:** current tools produce work like an average junior associate and are better at generating than filtering ideas (BTAX-LOWY-2026).
- **Vendor-owned evidence:** much of the quantitative discourse comes from sellers of the tools (TR, Bloomberg Tax, Blue J).

### Interview probes for an advisor

1. Take the last research memo that used AI. Which steps did the tool do, how was each cited authority checked against primary sources, who signed, and what record exists in the file?
2. How do you decide which questions are eligible for AI (novelty, penalty exposure, jurisdiction)? What triggers escalation to a senior reviewer regardless of the tool's confidence?
3. What have you measured about accuracy or review effort (errors found at review, rework, parallel runs against a human answer)? If nothing, what would you need to start?
4. How have you changed engagement letters and billing since OPR Alert 2026-19: disclosure of AI use, passing on savings, or value pricing?
5. How are juniors learning the research craft if first drafts are machine-made, and who owns tax AI governance in your function or firm?

## 4. Routed to other modules

- **controversy:** *Clinco* sanctions risk, *Khoja* (IRS motion with a nonexistent citation), Tax Court AI rules, and court-filing verification (BLAW-TAXCT-2026; TAXCT-CLINCO-2026). Tax-authority AI risk register (Werfel Appendix A) and AI audit-selection issues. Blair-Stanek et al. on LLMs identifying tax abuse from the authority side (JHU-TAXABUSE-2025).
- **compliance:** Bloomberg Tax Compliance Tracker AI Assistant; document extraction risk in Werfel's preparer register (risk 3); neuro-symbolic tax calculation (JHU-TAXREASON-2025).
- **transfer-pricing:** ABA May Meeting panel "AI and Transfer Pricing Under section 482" with an IRS panelist (ABA-MAYMTG-2026).
- **international-pillar-two:** Tax policy of AI, including nexus, permanent establishment and value creation (DCBAR-TAX-2026; ABA-MAYMTG-2026 PE/AI panel; OXFORD-CBT-2026 Session 4). A frontier advisory topic, not an AI-in-practice use case.
- **indirect-tax and tax-data-technology:** Real-time compliance and continuous transaction controls (TRI-TEIAUDITOR-2026); audit-ready, traceable automation for sales and use tax, VAT and reconciliations at Oxford Industries with Savant (SAVANT-TEI-2026; session description only); OpenAI's tax department automation pipelines (TEI-TAXTECH-2026).
- **Cross-cutting (all modules):** professional-responsibility rules (OPR Alert 2026-19, PCRT, Werfel framework, CART); firm AI policy; shadow AI; the Deloitte Australia report with invented quotes that OPR cites as a non-lawyer example (IRS-OPR-2026).

## 5. Sources

56 distinct sources; by type: press 16, vendor 11, conference 9, firm 5, academic 5, survey 3, professional-body 3, regulator 1, standard-setter 1, podcast 1, community 1. Access is `full` unless marked `search-only`. Dates are publication dates from page metadata or the byline where found; where a page carries no date the retrieval date (2026-10-17) is used and flagged in the use-case locator.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-MAYMTG-2026 | ABA Section of Taxation May Meeting 2026 final program | ABA Section of Taxation | conference | https://sitepilot11.firmseek.com/client/chamberlain/www/media/event/657_ABA_Section_of_Taxation_2026_May_Meeting_Agenda.pdf | 2026-05 | full |
| ACCOUNTINGWEB-ELDEN-2026 | Tribunal slams careless AI use by advisers (Elden v HMRC, FTT) | AccountingWEB | community | https://www.accountingweb.co.uk/tax/hmrc-policy/tribunal-slams-careless-ai-use-by-advisers | 2026-01 | search-only |
| ACCTODAY-CART-2026 | Former IRS commissioner teams with AICPA to form AI tax risk group | Accounting Today | press | https://www.accountingtoday.com/news/former-irs-commissioner-teams-with-aicpa-to-form-ai-tax-risk-group | 2026-10-08 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation: appendices (Appendix C: AI Risk Register for Tax Preparers) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full |
| BLAW-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Tax Daily Tax Report | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 | full |
| BLUEJ-2026 | Blue J AI Tax Research Platform (product page: customer quotes and usage statistics) | Blue J | vendor | https://www.bluej.com/events | 2026-10-17 | full |
| BLUEJ-CPA-2026 | 2026 AI Tax Research Solution Outlook Report (landing page; report is form-gated) | CPA.com (AICPA subsidiary) with Blue J | vendor | https://www.cpa.com/whitepapers/2026-ai-tax-research-solution-outlook-report | 2026 | full |
| BLUEJ-ENT-2026 | Best AI tax research tools for large and enterprise firms (vendor comparison blog) | Blue J | vendor | https://www.bluej.com/blog/best-ai-tax-research-tool-enterprise | 2026-10-16 | full |
| BLUEJ-SSC-2025 | SSC CPAs + Advisors Elevates Tax Research with Blue J's AI-Powered Platform (customer story) | Blue J | vendor | https://www.bluej.com/our-customers/ssc-cpas-advisors | 2025-10-17 | full |
| BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 | full |
| BTAX-HALLUC-2026 | AI Hallucinations in Tax: The Risks and How to Mitigate Them | Bloomberg Tax | vendor | https://pro.bloombergtax.com/?p=16920 | 2026-05-11 | full |
| BTAX-LOWY-2026 | Tax Lawyers Must Adapt to AI Now. It's Already Changed the Game (Peter Lowy, Nelson Mullins) | Bloomberg Tax (Tax Management Memo) | press | https://news.bloombergtax.com/tax-management-memo/tax-lawyers-must-adapt-to-ai-now-its-already-changed-the-game | 2026-07-31 | full |
| BTAX-PRICING-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 | full |
| BTAX-SIVA1-2026 | Don't Trust AI, Always Verify. Tax Law Still Needs Humans, Pt. 1 (Pramod Kumar Siva) | Bloomberg Tax (Tax Management Memo) | press | https://news.bloombergtax.com/tax-management-memo/dont-trust-ai-always-verify-tax-law-still-needs-humans-pt-1-1 | 2026-04-28 | full |
| BTAX-SIVA2-2026 | Don't Trust AI, Always Verify. Tax Law Still Needs Humans, Pt. 2 (Pramod Kumar Siva) | Bloomberg Tax | press | https://news.bloombergtax.com/tax-insights-and-commentary/dont-trust-ai-always-verify-tax-law-still-needs-humans-pt-2 | 2026-04-30 | full |
| BTAX-TOOLS-2026 | Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026 | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026 | 2026-03-09 | full |
| CHARLOTIN-DB-2026 | AI Hallucination Cases Database (Damien Charlotin) | Damien Charlotin | academic | https://www.damiencharlotin.com/hallucinations/ | 2026-10-16 | full |
| CPAPA-BLUEJ-2025 | Blue J and CPA.com Co-Author the AI Tax Research Solution Outlook Report | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/09/17/blue-j-and-cpa-com-co-author-the-ai-tax-research-solution-outlook-report-to-set-the-benchmark-for-the-future-of-tax-research/168693/ | 2025-09-17 | full |
| CPAPA-FIRSTSTOP-2025 | AI Is Now a First Stop for Tax and Investing Questions: CPAs Need a Playbook Fast | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/10/29/ai-is-now-a-first-stop-for-tax-and-investing-questions-cpas-need-a-playbook-fast/171939/ | 2025-10-29 | full |
| CPAPA-TR-2026 | The Real AI Story in Tax and Audit Isn't Adoption: It's Impact (Thomson Reuters-authored piece) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/21/the-real-ai-story-in-tax-and-audit-isnt-adoption-its-impact/181846/ | 2026-04-21 | full |
| DCBAR-TAX-2026 | Rise of the Machines: How Artificial Intelligence Is Changing the Tax World (session page) | D.C. Bar | conference | https://events.dcbar.org/Tax2026/session/3513387/rise-of-the-machines-how-artificial-intelligence-is-changing-the-tax-world | 2026-01-08 | full |
| DELOITTE-TTT3-2026 | Tax Transformation Trends AI report, Part three: Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| ICAEW-GUNNARSSON-2025 | Use of AI criticised in tax case (HMRC v Gunnarsson [2025] UKUT 247) | ICAEW Tax Faculty | professional-body | https://www.icaew.com/insights/tax-news/2025/aug-2025/use-of-ai-criticised-in-tax-case | 2025-08 | full |
| ICAEW-POD-2026 | How to use AI in tax ethically, and group audit best practice (podcast transcript, Accountancy Insights) | ICAEW | podcast | https://www.icaew.com/insights/podcast/accountancy-insights/how-to-use-ai-in-tax-ethically-and-group-audit-best-practice/transcript | 2026-02-04 | full |
| IFA-LISBON-2025 | IBFD Dialogues Seminar at IFA Lisbon 2025: Unlocking the Potential of Generative AI for Tax Professionals | IBFD | conference | https://www.ibfd.org/events/ibfd-dialogues-seminar-ifa-lisbon-2025-0 | 2025-10-06 | full |
| IRS-OPR-2026 | Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| JHU-TAXABUSE-2025 | Can LLMs Identify Tax Abuse? (Blair-Stanek, Holzenberger, Van Durme; arXiv 2508.20097, v2 21 Jan 2026) | arXiv | academic | https://arxiv.org/abs/2508.20097 | 2025-08-10 | full |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning (arXiv 2508.21051, accepted AAAI 2026) | arXiv | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 | full |
| JOFA-AIPOLICY-2026 | Drafting an AI policy that actually works (Professional Liability Spotlight, Nicole L. Graham, Aon) | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/ | 2026-07-01 | full |
| JOFA-DISCLOSE-2025 | Should I disclose my use of gen AI to clients? | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/ | 2025-04-01 | full |
| JOFA-OPR-2026 | IRS outlines AI risks, Circular 230 duties for tax practitioners | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/ | 2026-06 | full |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (KPMG/Anthropic release) | firm | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 | full |
| KPMG-MA-2025 | How generative AI is transforming mergers and acquisitions tax (article and PDF) | KPMG US | firm | https://kpmg.com/us/en/articles/2025/how-generative-ai-transforming-mergers-acquisitions-tax.html | 2025-06 | full |
| KPMGUK-BLUEJ-2024 | KPMG UK And Blue J To Launch Generative AI Tool To Address Tax Research Questions | Crowdfund Insider | press | https://www.crowdfundinsider.com/?p=221784 | 2024-02-22 | full |
| KTS-AI-2026 | Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season | Kilpatrick Townsend & Stockton LLP | firm | https://ktslaw.com/insights/alert/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season | 2026-09-29 | full |
| MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (Magesh et al., arXiv 2405.20362) | arXiv | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full |
| MONDAQ-HORIZON-2026 | New Trends And Challenges In Tax Due Diligence On The M&A Market (Horizon Solutions Kft., Hungary) | Mondaq | firm | https://webiis10.mondaq.com/tax-authorities/1737066/new-trends-and-challenges-in-tax-due-diligence-on-the-ma-market | 2026-01-28 | full |
| NATLAW-OPR-2026 | IRS Office of Professional Responsibility (OPR) Issues AI Guidance: Tax Professionals Also Face AI Ethics and Compliance Obligations | The National Law Review | press | https://natlawreview.com/article/irs-office-professional-responsibility-opr-issues-ai-guidance-tax-professionals | 2026-08-04 | full |
| NATP-TAXPOSIUM-2026 | Future of Tax Research with AI (Taxposium 2026 session page, sponsored by Blue J) | National Association of Tax Professionals | conference | https://taxposium.natptax.com/future-of-tax-research-with-ai | 2026 | full |
| OXFORD-CBT-2026 | Oxford CBT Summer Conference 2026 booklet (Session 4: Tax and Artificial Intelligence) | Oxford University Centre for Business Taxation | conference | https://oxfordtax.sbs.ox.ac.uk/sitefiles/cbt-summer-conference-booklet-2026 | 2026-06-26 | full |
| PCRT-AI-2026 | Professional bodies issue AI advice to members (PCRT topical guidance on AI) | Association of Taxation Technicians for the seven PCRT bodies | standard-setter | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Michael V. Sala, Tax Notes State 121:189; abstract on TaxProf Blog) | Tax Notes / TaxProf Blog | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full |
| SAVANT-TEI-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| TAXADV-DRAKE-2025 | AI's role in complex tax decisions (advertising supplement, Drake Software) | The Tax Adviser (AICPA) | vendor | https://www.thetaxadviser.com/issues/2025/aug/ais-role-in-complex-tax-decisions/ | 2025-07-25 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo. 2026-16) | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| TAXPROF-WERFEL-2026 | Werfel Presents Risk Framework for the Use of AI in Tax Administration and Practice Today at Duke | TaxProf Blog | press | https://taxprofblog.aals.org/2026/03/26/werfel-presents-risk-framework-for-the-use-of-artificial-intelligence-in-tax-administration-and-practice-today-at-duke/ | 2026-03-26 | full |
| TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 At a Glance agenda | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03 | full |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TOLLEY-2024 | Trustworthiness is key to adoption of AI in tax, says Tolley (survey of 446 UK tax professionals) | Tax Journal (LexisNexis) | survey | https://www.taxjournal.com/articles/trustworthiness-is-key-to-adoption-of-ai-in-tax-but-pricing-potentially-problematic-says-tolley | 2024-06-26 | full |
| TR-ACCURACY-2026 | Tax industry trends 2026: Why accuracy is the new standard for AI | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/tax-industry-trends-2026-why-accuracy-is-the-new-standard-for-ai/ | 2026-08-03 | full |
| TR-AGENTICBLOG-2026 | An evolution of tax tools and how agentic AI will shape 2026 | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/an-evolution-of-tax-tools-and-how-agentic-ai-will-shape-2026/ | 2026-05-01 | full |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology Report) | Thomson Reuters Institute with Tax Executives Institute | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026/ | 2026-03-16 | full |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| TRI-TEIAUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en-us/posts/corporates/2026-tei-tax-tech-auditor-already-knows/ | 2026-05-12 | full |
| V7-TAXDD-2026 | AI Tax Due Diligence Agent (V7 Go product page) | V7 | vendor | https://www.v7labs.com/agents/ai-tax-due-diligence-agent | 2026-10-17 | full |

## 6. Gaps

- **Quality evidence is absent.** No error rates, override rates, parallel-run results or inspection findings exist in the public sources read for any tax research tool or Big Four assistant. No independent head-to-head benchmark was found. Web search ran out before a final targeted search for one; a follow-up search for 2026 arXiv or law-review benchmarks of tax research tools is still worth doing.
- **Practitioner communities were not reachable.** Reddit (r/taxpros) returned 403, TaxProTalk and the AICPA community timed out or blocked, and AccountingWEB sits behind a bot wall (the Elden v HMRC item is search-only). The most candid practitioner voices are therefore missing; the TEI recap by Thomson Reuters Institute is the closest substitute and is vendor-owned.
- **Podcasts and webcasts:** only the ICAEW transcript (2026-02-04) was read in full. Thomson Reuters Institute's "Clarity on Tech" landing page was opened but has no transcript or date; Tax Notes Talk 2026 episodes (for example the Tax Court chief judge on AI) were not reached. KPMG's TaxWatch M&A webcast was only available as KPMG's written summary.
- **Conference content:** agendas and sponsor releases show topics and speakers, not what was said. TEI Annual Conference (Nashville, 18 to 21 Oct 2026) and CCH Connections (25 to 28 Oct 2026) had not happened. AICPA ENGAGE (June 2026) recordings and the Blue J session were not read.
- **Paywalled or gated:** Tax Notes, Bloomberg Tax beyond the open article text, the Blue J/CPA.com 2026 report (form-gated; only the landing text and a 2025 summary were read), Thomson Reuters's 2026 AI in Professional Services Report (reached only through a Thomson Reuters-authored article), the January 2026 *International Tax Journal* paper behind the "nearly 800 citation errors" figure (cited in BTAX-HALLUC-2026; preprints.org blocked), The Tax Adviser's Werfel framework text (only the appendices PDF was read).
- **Unverified items:** Siva's references to *Heppner* and to a case with an IRC 6662 penalty; Bloomberg Tax's statement that 81% of Fortune 500 companies and 87% of the top 100 accounting firms use its AI tools (vendor claim, not used); the Pearl.com and Taxpayer Advocate figures quoted in CPAPA-FIRSTSTOP-2025. The publication month of the Werfel article is stated as August in one source and September in another.
- **Unreached or bot-walled products:** CCH AnswerConnect and Axcess Advisor, PwC, EY and Deloitte research assistants (apart from a Deloitte scenario paper), Harvey's tax use (search results were marketing from a competitor and are excluded), Tolley+ AI beyond a 2024 announcement.
- **Topics with no usable discourse found:** malpractice-insurer guidance beyond one broker's column; engagement-letter wording in practice; opinion-letter practice at law firms beyond one alert; in-house tax helpdesk assistants for business stakeholders; any named tax department with metrics for research use.
- **Older material used as foundation only:** Tolley (June 2024), KPMG UK and Blue J (February 2024) and Magesh et al. (May 2024) fall outside the 12 to 18 month window.
