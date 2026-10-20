# Backbone library: agentic patterns for knowledge work (research-brief, grounded-knowledge-assistant, draft-review-loop)

Stream B, patterns and knowledge. Prepared 2026-10-20. Public sources only. Tools are described by runtime class, not by vendor.

**How to read this file.** Every attributed claim carries a source ref (`PUBLISHER-SHORT-YYYY`, listed in section 7) and a locator. Statements marked **(S)** are the analyst's synthesis or design judgment, not claims from a source. Statistics say what they measure and who measured it: `self-reported` (the deploying organization), `vendor-published`, or `independent` (academic, regulator or third-party). Evidence grades follow the vocabulary (A measured outcome from a named organization; B named deployment without published measurements; C vendor claim; D idea). Where a source is an experiment or study rather than a deployment, that is stated in the grade note.

## 1. Summary

- **All three patterns share one weakness: the human checkpoint is where the value is won or lost, and it is the least measured part.** Studies show reviewers anchoring on AI drafts (MGB simulation: LLM-assisted replies resembled the AI drafts more than the clinicians' own replies, LANCET-CHEN-2024), over-trusting persuasive output (BCG experiment: warned consultants still did not challenge wrong answers, BCG-2023), and gaining no time once checking is counted (Stanford Health Care in-basket drafts: no significant change in time, JAMA-GARCIA-2024; ASIC proof of concept: assessors thought AI summaries could create more work, ASIC-AWS-2024). Design the checkpoint and measure it before you scale the draft.
- **"Grounded" and "cited" do not mean "correct".** Independent tests found retrieval-grounded legal research tools hallucinating 17% to 33% of the time on a 202-query set (STANFORD-LEGAL-2024), generative search engines with only 51.5% of sentences fully supported by their citations (STANFORD-LIU-2023), and 45% of 2,709 assistant news answers with at least one significant issue (BBC-EBU-2025). Citation checking has to be a built step, not a hope.
- **Where grounded assistants work, the owners measure accuracy against expert-scored samples and keep re-measuring.** GOV.UK Chat reports accuracy rising from 76% to 90% on expert-plus-automated scoring over 18 months, with 508 jailbreak attempts logged (GDS-GOVUKCHAT-2026A); Morgan Stanley describes a daily regression suite (OPENAI-MORGANSTANLEY-n/d). The failures that made news (NYC MyCity, Air Canada) were public-facing bots that gave wrong answers on rules; MyCity's owners later added disclaimers and narrowed the questions it would answer, and neither case published an accuracy measurement (MARKUP-MYCITY-2026, GUARDIAN-AIRCANADA-2024).
- **Draft-review-loop value is real but narrow and uneven.** Controlled evidence: a 55.8% faster task completion for coders in a 2022-era experiment (MSR-PENG-2023), a 19% slowdown for experienced open-source developers in 2025 who expected a 24% speedup (METR-2025), a 9.5% time-in-note reduction for one of two ambient scribes and none for the other in a 238-physician randomized trial (NEJMAI-LUKAC-2025), and burnout-measure gains with no time gain in a hospital in-basket pilot (JAMA-GARCIA-2024). Benefit depends on the task sitting inside what the tool does well (BCG-2023).
- **Quality metrics are rare in published case studies.** Vendor stories give speed and adoption figures (Novo Nordisk "90%" writing-time cut, ANTHROPIC-NOVO-n/d; Morgan Stanley 98% adoption, OPENAI-MORGANSTANLEY-n/d) but no override, escalation or error rates. The best quality data come from regulators, universities and evaluation teams (ASIC-AWS-2024, ACE-TREASURY-2025, GDS-GOVUKCHAT-2026A, DSIT-CONSULT-2025).
- **Governance is converging on the same asks.** Human oversight defined and documented (NIST-RMF-2023 MAP 3.5), citation and source verification during pre-deployment and monitoring (NIST-AI600-2024 MS-2.5-003), automation-bias awareness for overseers (EU-AIACT-2024 Art. 14(4)(b)), prompt and output logging with model-version tracking (FINRA-OVERSIGHT-2026), and disclosure unless a licensed human has read and reviewed the output (CALEG-AB3030-2024 s.1339.75(b); EU-AIACT-2024 Art. 50(4)). The EU timetable for Annex III high-risk duties moved to 2 December 2027 under the AI Omnibus, per a law-firm summary (KLGATES-OMNIBUS-2026).
- **Anti-pattern signal:** each pattern fails when the reader cannot or will not check. Deloitte Australia agreed to repay the final instalment of its contract for a A$440,000 government report that contained nonexistent references (GUARDIAN-DELOITTE-2025); a court-decision database lists 2,202 cases where courts addressed hallucinated content (CHARLOTIN-DB-n/d, count as of retrieval 2026-10-20).
- **Evidence gaps:** no retail or manufacturing example with measured outcomes for these patterns was found (manufacturing has one vendor claim of 25% reactive-maintenance time saved on unnamed pilots, SIEMENS-COPILOT-2025); no source publishes override or escalation rates for research briefs.

## 2. Item profiles

### 2.1 `research-brief`

**What it does and where it fits.** Gathers sources, compares them and writes a cited brief; the expert reads the sources behind the key claims (library index s.3, working definition). Work types: `research-synthesis`, `expert-judgment`. Fit is strongest for open-ended, breadth-first questions where the path cannot be fixed in advance and the value per task is high: Anthropic describes research as "open-ended problems" where steps cannot be predicted, says multi-agent research "excel[s] especially for breadth-first queries", and notes multi-agent runs use about 15x the tokens of a chat, so the task must be worth that cost (ANTHROPIC-MULTIAGENT-2025, "Benefits of a multi-agent system").
*Cues in a user's description of their work (S):* "I spend two days reading before a client call or decision"; "we need a landscape, competitor or regulatory scan"; "the question needs forty documents read"; "juniors build the background pack"; "we re-do the same scan every quarter." The archetype entries show the same cues in pursuit research, pre-meeting briefs, tax authority research and threat reporting (e.g. `professional-services-pursuit-proposals-08` B, `professional-services-client-development-06` B, `tax-research-advisory-02` B, `security-threat-intelligence-10` B).

**Ladder range and runtime class by rung.**

| Rung | What it looks like | Runtime class | Archetype anchor |
|---|---|---|---|
| assist | The expert runs research in a chat session and checks the output | `personal-assistant` | `tax-research-advisory-02` (B, tagged augment), `tax-research-advisory-06` (C) |
| augment | A standard brief with enforced citation check inside a team workflow | `shared-team-skills`; `workflow-automation` | `professional-services-pursuit-proposals-08` (B), `security-threat-intelligence-10` (B) |
| delegate | An agent works a question end to end and submits a cited memo; the expert reviews it | `background-agent`; `managed-agent-runtime` | `tax-research-advisory-03` (C) |

Usual range per the library is assist to augment; the one delegate entry in the archetypes is grade C (vendor-described). Rung choice should follow how cheaply claims can be verified **(S)**.

**How it is built.**
- *Inputs:* the question, the allowed source set (web, licensed, internal), the output format and the criteria. Anthropic's lead agent gives each subagent "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries"; without that, agents "duplicate work, leave gaps" (ANTHROPIC-MULTIAGENT-2025, "Prompt engineering and evaluations").
- *The AI's role:* plan the research, search wide then narrow, run subagents in parallel, synthesise, then pass the draft to a separate citation step that identifies specific locations for each claim (ANTHROPIC-MULTIAGENT-2025, "Architecture overview"). Effort is scaled by rule: simple fact-finding 1 agent with 3 to 10 tool calls; comparisons 2 to 4 subagents with 10 to 15 calls each; complex research more than 10 subagents (same source, "Scale effort to query complexity"). A research prototype for article-length briefs separates pre-writing (perspective-guided question asking, then outline) from writing (STANFORD-STORM-2024, abstract and Fig. 1).
- *Human checkpoints:* the expert opens the sources behind key claims (library index s.3). NIST asks organizations to "review and verify sources and citations" during pre-deployment measurement and ongoing monitoring (NIST-AI600-2024, MS-2.5-003).
- *Thresholds and sampling:* no published threshold for briefs was found. **(S)** Verify 100% of the claims that drive a decision or leave the team; sample the rest, as in lot acceptance sampling, the "middle of the road" between no inspection and 100% inspection (NIST-SEMATECH-ACCEPT, s.6.2.1). Raise the sample while the observed unsupported-claim rate is above target.
- *Logging and audit trail:* Anthropic added full production tracing to diagnose why agents "were not finding obvious information" (ANTHROPIC-MULTIAGENT-2025, "Production reliability"). FINRA lists stored prompt and output logs and tracking which model version was used and when (FINRA-OVERSIGHT-2026, GenAI "Monitoring").
- *Evaluation:* Anthropic started with about 20 real queries, then an LLM judge scoring factual accuracy, citation accuracy, completeness, source quality and tool efficiency, plus human testers who found early agents preferred SEO content farms over authoritative sources (ANTHROPIC-MULTIAGENT-2025, "Effective evaluation of agents"). GOV.UK Chat's three pillars (automated evaluation, manual expert review, live monitoring) are a usable template (GDS-GOVUKCHAT-2026B). Practitioner guidance: label outputs good or bad (binary labels were easier to manage than scores) and track how well model-based evaluation agrees with human evaluation before relying on it (HUSAIN-2024, "Level 2: Human & Model Eval").

**Prerequisites.** *Data and access:* sources the tool may lawfully read and the user may see; tools that fit the source (Anthropic notes an agent searching the web for context that exists only in Slack "is doomed", ANTHROPIC-MULTIAGENT-2025, "Tool design"). *Policy:* what may be sent to an external tool; for GOV.UK Chat, GDS put in safeguards to stop users submitting personal data, removed pages containing personal data and conducted a data protection impact assessment (GDS-GOVUKCHAT-2024, "Protecting users' privacy and security"). *Skills:* experts who can judge sources; an evaluation set; training. In the UK government Copilot trial, users with lower familiarity and confidence saw lower savings (GDS-COPILOT-2025, s.4.2 and s.6).

**Failure modes and controls.**

| Failure mode | Evidence | Control |
|---|---|---|
| Fabricated or misattributed citations | Deloitte Australia report with nonexistent references (GUARDIAN-DELOITTE-2025); 51.5% of generated sentences fully supported and 74.5% of citations supporting their sentence in four search engines (STANFORD-LIU-2023, abstract); 31% of 2,709 news answers with a significant sourcing issue (BBC-EBU-2025, High-level findings) | Separate citation step; open every cited source for load-bearing claims; spot-check the rest |
| Confident wrong answers instead of "not found" | Eight generative search tools were collectively wrong on more than 60% of 1,600 citation-retrieval queries and rarely signalled doubt (CJR-TOW-2025) | Require "could not find" as an allowed output; reward it in evaluation (S) |
| Weak source selection | Early agents chose SEO farms (ANTHROPIC-MULTIAGENT-2025); expert editors found "source bias transfer" and "over-association of unrelated facts" (STANFORD-STORM-2024, abstract) | Source-quality rules in the prompt; allow-lists for regulated work |
| Lost nuance | ASIC assessors: summaries missed nuance or context (ASIC-AWS-2024, s.1); UK policy teams struggled where sources held contrasting opinions (GDS-COPILOT-2025, s.4.2) | Expert reads the primary text for contested points |
| Over-trust | Higher confidence in GenAI associated with less critical thinking in a 319-person survey (MSR-LEE-2025, abstract); consultants on a task outside the tool's range performed 23% worse than controls (BCG-2023) | Task-fit map; require the reviewer to form a view first (S) |
| Runaway effort and cost | Early agents spawned 50 subagents for simple queries (ANTHROPIC-MULTIAGENT-2025) | Effort-scaling rules; token budget per brief |
| Non-repeatable results | Agents are "non-deterministic between runs, even with identical prompts" (ANTHROPIC-MULTIAGENT-2025, "Production reliability") | Save the sources and plan with the brief |

**Value levers and metrics.** `capacity` and `speed` (hours or days to a first brief), `quality` (coverage; accuracy), `risk` (fewer missed sources). Candidate metrics, all **(S)** unless cited: time to first usable brief; share of claims supported by the cited source (the citation precision and recall used in STANFORD-LIU-2023, abstract); expert edit or override rate (share of claims changed or removed); escalation rate (share of briefs sent back for deeper human research); material errors found after release; token cost per brief. What is published: 90.2% better than a single agent on Anthropic's internal research evaluation (vendor, self-reported, benchmark rather than work outcome, ANTHROPIC-MULTIAGENT-2025, "Benefits"); more than 70% of 7,115 survey respondents agreed Copilot reduced time spent searching for information (self-reported by government trial users, GDS-COPILOT-2025, s.1.2).

**Governance points.**
- NIST AI RMF: oversight processes "defined, assessed, and documented" (NIST-RMF-2023, MAP 3.5); confabulated citations "may further mislead humans" (NIST-AI600-2024, s.2.2).
- EU AI Act: Annex III point 8(a) lists AI used by or for a judicial authority "to assist ... in researching and interpreting facts and the law" as high-risk (EU-AIACT-2024, Annex III); AI literacy duty for providers and deployers (Art. 4); automation-bias awareness for overseers of high-risk systems (Art. 14(4)(b)); disclosure for AI-generated text published to inform the public on matters of public interest unless it has had human review or editorial control and a person holds editorial responsibility (Art. 50(4)). The AI Omnibus (Regulation (EU) 2026/1744) moved Annex III application from 2 August 2026 to 2 December 2027, while the transparency duties (telling users they are interacting with an AI system; labelling certain AI-generated content) stay on the 2 August 2026 timetable with a four-month grace period for certain machine-readable marking, per a law-firm summary (KLGATES-OMNIBUS-2026; official text not retrieved).
- ISO/IEC 42001: management-system controls on impact assessment, lifecycle monitoring and use of AI; read here only through a secondary guide that counts 38 Annex A controls in eight domains, A.2 to A.9 (AIGL-ISO42001-2026); other guides surfaced in search list nine objectives, so check the grouping against the standard (ISO text paywalled; search-only for those guides).
- Sector: FINRA says its rules apply to GenAI use, including supervision, communications and recordkeeping (FINRA-RN2409-2024, Summary). Professional duty: Deloitte's partial refund (GUARDIAN-DELOITTE-2025).

**How it evolves up the ladder.** Assist: the expert prompts a chat tool and owns every check. Augment: the team standardises the brief (template, approved source set, enforced citation pass), as in the pursuit-brief and pre-meeting-brief entries. Delegate: an agent runs standing or end-to-end research and an expert reviews the final memo (`tax-research-advisory-03`, C). Each step needs a gold set of questions with expert-checked answers, an automated citation check, and logs, before the reviewer's share of attention is reduced **(S)**. Scheduled briefs on a feed (`security-threat-intelligence-02`, B) shade into `monitor-diagnose-act`.

**Anti-patterns.**
- No one will open the sources, or the brief is published unreviewed (Deloitte Australia, GUARDIAN-DELOITTE-2025).
- The question needs weighing nuanced qualitative and quantitative evidence outside the tool's reliable range (BCG-2023: business problem solving, 23% worse than controls).
- The brief replaces the judgment in a high-risk decision (EU-AIACT-2024, Annex III 8(a), Art. 14).
- Tasks of low value per token or a single known fact where a search is cheaper (ANTHROPIC-MULTIAGENT-2025: about 15x chat tokens for multi-agent).
- Learning tasks where the junior's own research is the point (`professional-services-talent-learning-09` C, `professional-services-talent-learning-11` A).

### 2.2 `grounded-knowledge-assistant`

**What it does and where it fits.** Answers questions from an approved body of knowledge, with citations; content owners keep the knowledge current (library index s.3). Work types: `client-interaction`, `research-synthesis`, `expert-judgment`, `physical-field`. Cues **(S)**: "people keep asking the same questions and the answers are in documents nobody can find"; "new joiners ask seniors"; "the policy manual is 400 pages"; "we answer security questionnaires from last year's answers"; "technicians search manuals on the shop floor." Cross-industry anchors: advisers querying the firm's research (Morgan Stanley, OPENAI-MORGANSTANLEY-n/d), citizens querying government guidance (GDS-GOVUKCHAT-2026A), support agents served documentation links (NBER-BRYNJOLFSSON-2023, s.2.3), maintenance staff (SIEMENS-COPILOT-2025).

**Ladder range and runtime class by rung.**

| Rung | What it looks like | Runtime class | Archetype anchor |
|---|---|---|---|
| assist | Staff ask an approved assistant and check the cited passage | `personal-assistant`; `shared-team-skills` | `professional-services-knowledge-management-01` (B), `tax-research-advisory-05` (C) |
| augment | Answers appear inside the working tool; a person decides | `shared-team-skills`; `workflow-automation` | `security-operations-02` (A), `tax-indirect-tax-06` (A) |
| automate | Answers go out without a person on the normal path; uncertain ones go to an analyst | `workflow-automation`; `managed-agent-runtime` | `security-governance-risk-01` (A) |

The library's usual rung is assist. When the audience is the public or clients and the assistant hands off to people, the work becomes `service-agent-escalation` **(S)**. The Air Canada and MyCity cases sit at that boundary.

**How it is built.**
- *Inputs:* a curated corpus with owners, dates and permissions. GOV.UK Chat draws "exclusively" on published GOV.UK guidance and rates an answer accurate only if it meets all the standards of that content (GDS-GOVUKCHAT-2026A, finding 2). The UK Copilot trial assistant adopts the user's permissions and retrieves only documents the user could open, and the report warns this can expose over-shared files (GDS-COPILOT-2025, s.2.1).
- *The AI's role:* retrieve, answer, cite, and decline when outside scope ("by design GOV.UK Chat won't provide answers outside the scope", GDS-GOVUKCHAT-2026A, finding 4). Retrieval design carries the load. Seven RAG failure points were reported from three case studies: missing content, missed top-ranked documents, not in context, not extracted, wrong format, incorrect specificity, incomplete (DEAKIN-BARNETT-2024, s.4). A legal-tool evaluation traced errors to naive retrieval, inapplicable authority, sycophancy and reasoning errors (STANFORD-LEGAL-2024, s.6.3).
- *Human checkpoints:* content owners approve what enters the corpus and retire what is stale (library index s.3); users check the cited source (the GOV.UK pilot found users appreciated features that make it easy to double-check at source, GDS-GOVUKCHAT-2026A, finding 2); an analyst takes uncertain answers where the assistant is automated (`security-governance-risk-01`, A).
- *Thresholds and sampling:* GOV.UK measured accuracy by expert scoring plus automated evaluation: 419 conversations and 1,084 question-answer pairs reviewed manually in the web pilot, and 1,338 in-scope questions in the app pilot (GDS-GOVUKCHAT-2026A, "Our research methods"). Morgan Stanley runs a daily regression suite of sample questions (OPENAI-MORGANSTANLEY-n/d, "Strengthening trust with controls"). Brynjolfsson's tool gave no suggestion when it had insufficient training data (NBER-BRYNJOLFSSON-2023, s.2.3), an abstain threshold.
- *Logging and audit trail:* GOV.UK adds automated live monitoring that flags issues for human review (GDS-GOVUKCHAT-2026B). FINRA lists stored prompt and output logs, model-version tracking and regular error checks (FINRA-OVERSIGHT-2026).

**Prerequisites.** *Data:* an owned, current, permissioned corpus; Morgan Stanley describes moving from 7,000 answerable questions to a 100,000-document corpus through retrieval tuning (OPENAI-MORGANSTANLEY-n/d, quote by David Wu). *Access:* identity-aware retrieval. *Policy:* acceptable-use rules including "the kinds of queries GAI applications should refuse" (NIST-AI600-2024, GV-3.2-003); disclosure and recourse. *Skills:* content curation, evaluation design and a place for user feedback. *Cost of getting it wrong in public:* see failure table.

**Failure modes and controls.**

| Failure mode | Evidence | Control |
|---|---|---|
| Wrong or invented answers despite retrieval | 17% to 33% hallucination across three legal research tools; accurate (correct and grounded) on 65%, 42% and 20% of queries (STANFORD-LEGAL-2024, s.6.1, Fig. 4; independent) | Gold-set testing before launch; scope limits; abstain rule |
| Illegal or harmful advice from a public bot | NYC MyCity told businesses employers could take workers' tips and landlords need not accept Section 8 vouchers (MARKUP-MYCITY-2024); the next administration said it plans to take the bot down (MARKUP-MYCITY-2026) | Narrow scope; live monitoring; named owner; disclaimers are not a control (S) |
| Inconsistent answers to the same question | Ten Markup staff asking one housing question all got "no" while an earlier query got "yes" (MARKUP-MYCITY-2024) | Test repeats; log and compare answers |
| Organization held to what the bot said | Tribunal ordered Air Canada to pay C$650.88 plus interest and fees after its chatbot misstated bereavement-fare rules; the airline had argued the bot was a "separate legal entity" (GUARDIAN-AIRCANADA-2024) | Treat bot output as published policy; single source of truth |
| Stale or unapproved content | Library index s.3 (working definition); users over-trusting a trusted brand (GDS-GOVUKCHAT-2024, "Our early findings") | Content owner and review date per document |
| Over-exposure of files | Permission-following retrieval surfaces files users should not have had (GDS-COPILOT-2025, s.2.1) | Fix permissions before indexing |
| Agents cannot show which document was used | Agents built on a OneDrive folder "struggled to identify the exact documents" used (GDS-COPILOT-2025, s.4.5) | Require source passages in every answer |
| Low take-up of suggestions | Agents followed AI suggestions 38% of the time on average (NBER-BRYNJOLFSSON-2023, s.5.1) | Treat adherence as a quality signal; investigate declined answers |

**Value levers and metrics.** `capacity`, `speed`, `quality`, `experience`, `risk`. Published: 14% more issues resolved per hour on average and 34% for novice and low-skilled agents, 5,179 agents, independent academic study of a firm's tracked metrics (NBER-BRYNJOLFSSON-2023, abstract); 73% found GOV.UK Chat useful and 64% were satisfied (app survey, self-reported, GDS-GOVUKCHAT-2026A); 26 minutes a day saved (self-reported, from range midpoints, 7,115 respondents, GDS-COPILOT-2025, s.4.2). Quality metrics worth tracking **(S)**: expert-scored accuracy on a held-out set, answer rate for in-scope questions (GOV.UK reports 88%), share of answers with a valid citation, escalation rate, stale-document share, adherence or override rate, repeat-question consistency.

**Governance points.**
- NIST: confabulation and automation bias are named GAI risks (NIST-AI600-2024, s.2.2 and s.2.7); verify that RAG data are grounded (MS-2.5-005).
- EU AI Act: users must be told they are interacting with an AI system unless obvious (EU-AIACT-2024, Art. 50(1)); AI literacy (Art. 4). A customer-facing answer assistant is not listed in Annex III by itself; use in essential services, employment or justice contexts may be **(S)**. Annex III timing per KLGATES-OMNIBUS-2026.
- ISO/IEC 42001: impact assessment, operational monitoring and use-of-AI controls (AIGL-ISO42001-2026, secondary).
- Sector and law: FINRA says communications, supervision and recordkeeping rules apply to GenAI (FINRA-RN2409-2024); California requires a GenAI disclaimer and instructions to reach a human on AI-generated patient clinical communications unless a licensed provider has read and reviewed them (CALEG-AB3030-2024, s.1339.75(a)-(b)); tribunal liability (GUARDIAN-AIRCANADA-2024).

**How it evolves up the ladder.** Assist: staff chat with an approved corpus. Augment: answers are placed in the work step (suggested replies, precedent retrieval, VAT place-of-supply answers verified by an adviser). Automate: questionnaire or buyer-facing answers released automatically when confident, uncertain ones routed to an analyst (`security-governance-risk-01`, A; `assurance-soc-attestation-11`, C). Each rung needs the corpus owner role, a gold set, a refusal rule, and live monitoring. GOV.UK Chat moved from a July 2023 prototype to public pilots and, per its March 2026 post, GDS said it would begin opening access more widely, starting with all users of the GOV.UK app (GDS-GOVUKCHAT-2026A; GDS-GOVUKCHAT-2026B).

**Anti-patterns.**
- Public-facing, with wrong answers about rules and no published accuracy measurement (MyCity, MARKUP-MYCITY-2024; Air Canada, GUARDIAN-AIRCANADA-2024).
- Over a corpus nobody owns, or with permissions nobody cleaned (GDS-COPILOT-2025, s.2.1).
- For questions needing personal case data the assistant cannot see: GOV.UK pilot users wanted an adviser with access to their information, which the tool did not support (GDS-GOVUKCHAT-2026A, finding 4).
- When the answer is a legal or clinical decision that nobody will verify (STANFORD-LEGAL-2024; NIST-AI600-2024, s.2.2 healthcare example).
- Replacing the learning path of juniors who need to build their own judgment (`professional-services-knowledge-management-19` B; MSR-LEE-2025).

### 2.3 `draft-review-loop`

**What it does and where it fits.** Drafts a deliverable from inputs and templates; a reviewer edits and approves; nothing leaves the team before sign-off (library index s.3). Work types: `document-production`, `review-assurance`, `software-systems`. Cues **(S)**: "first drafts take days and reviewers fix the same things"; "we write the same report for every trial, client or period"; "the note is written after the meeting from memory"; "the partner rewrites what the associate drafted." Cross-industry anchors: clinical study reports (Novo Nordisk, ANTHROPIC-NOVO-n/d), patient-message replies and visit notes (JAMA-GARCIA-2024; NEJMAI-LUKAC-2025), client meeting notes and follow-ups (OPENAI-MORGANSTANLEY-n/d), code changes (GOOGLE-CODEREVIEW-2023), professional writing (MIT-NOY-2023).

**Ladder range and runtime class by rung.**

| Rung | What it looks like | Runtime class | Archetype anchor |
|---|---|---|---|
| assist | Person drafts with a chat tool and owns the text | `personal-assistant` | `professional-services-work-production-09` (B), `tax-transfer-pricing-02` (C) |
| augment | Draft appears inside the workflow; review is mandatory and logged | `shared-team-skills`; `workflow-automation` | `professional-services-work-production-05` (B), `security-incident-response-14` (A) |
| automate (low risk, after proof) | Review shrinks to sampling for categories with demonstrated error rates | `workflow-automation`; `background-agent` | `tax-compliance-corporate-05` (C, tagged augment: fewer review layers where outputs are consistent); `professional-services-quality-review-13` (C, tagged automate) |
| delegate | Agents draft and check each other; named human gates | `managed-agent-runtime` | `professional-services-work-production-15` (C), `assurance-quality-management-18` (B) |

Usual range per the library: assist to augment.

**How it is built.**
- *Inputs:* a template, approved source text and case-specific facts. NovoScribe combines retrieval with "domain expert-approved text and case-specific variables" (ANTHROPIC-NOVO-n/d, "How Novo uses Claude").
- *The AI's role:* produce a first pass; sometimes a second pass checks the first. Anthropic's evaluator-optimizer pattern has one model generate and another critique in a loop, suited to cases with clear criteria where "LLM responses can be demonstrably improved when a human articulates their feedback" (ANTHROPIC-AGENTS-2024, "Workflow: Evaluator-optimizer").
- *Human checkpoints:* a named reviewer decides before release. Morgan Stanley's Debrief: advisors "review and adjust" notes and follow-ups before finalising (OPENAI-MORGANSTANLEY-n/d). Clinician in-basket drafts are visible only to the clinician, who sends or rewrites (JAMA-GARCIA-2024, Methods). Brynjolfsson's tool output "is shown only to the agent" (NBER-BRYNJOLFSSON-2023, s.2.3).
- *Thresholds and sampling:* Google calibrated its suggested-edit model to a target precision of 50%, filtered low-confidence suggestions and found 40% to 50% of previewed suggestions applied (GOOGLE-CODEREVIEW-2023, "Serving infrastructure and user experience" and "Results"; self-reported). The Consult tool for consultation analysis showed officials the AI themes and recorded no change for 60% of responses and a median 23 seconds review per response (DSIT-CONSULT-2025 via AIGOVUK-CONSULT-2026). **(S)** Where a sampling plan is needed, lot acceptance sampling gives the language: sample size and accept or reject limits set from an acceptable defect level (NIST-SEMATECH-ACCEPT, s.6.2.1), tightened when defects appear and relaxed when they stay low.
- *Logging and audit trail:* draft utilization per clinician (drafts used divided by reply actions with a draft available) was the primary outcome of the Stanford pilot (JAMA-GARCIA-2024, Methods); FINRA lists prompt and output logs, model version, and human-in-the-loop review with regular error and bias checks (FINRA-OVERSIGHT-2026). **(S)** Keep draft, edits and final together so override rate and edit size can be computed.

**Prerequisites.** *Data:* templates and approved text to draft from. *Access:* systems where the draft lands (EHR, CRM, repository). *Policy:* disclosure and review rules; California's exemption turns on a licensed provider having "read and reviewed" the AI draft (CALEG-AB3030-2024, s.1339.75(b)). *Skills:* reviewers with domain competence and time budget. In the Stanford pilot, 25% of messages had no draft available (20% by exclusion criteria, 5% technical limits, JAMA-GARCIA-2024, Results), so coverage is a prerequisite too.

**Failure modes and controls.**

| Failure mode | Evidence | Control |
|---|---|---|
| Reviewer anchors on the draft and misses errors | Assessing physicians judged 11 of 156 LLM-draft responses (7.1%) as posing a risk of severe harm and 1 (0.6%) death, mostly from wrong acuity; assisted replies resembled drafts (LANCET-CHEN-2024; simulation, independent academic) | Review checklist on severity; reviewers form their own view first (S) |
| Checking cancels the time saved | No significant change in read, write or reply time in a 5-week pilot (JAMA-GARCIA-2024); AI summaries judged able to create more work (ASIC-AWS-2024, s.1) | Measure time end to end; stop if no gain |
| Perceived gain differs from real gain | Developers forecast 24% faster, afterwards estimated 20% faster, and were 19% slower (METR-2025, abstract; independent, 16 developers, 246 tasks) | Measure, do not rely on self-estimates |
| Over-trust of persuasive output | Warned consultants still accepted wrong output on a task outside the frontier (BCG-2023); automation bias is "a fairly robust and generic effect" across fields (JAMIA-GODDARD-2012, Results; 74 studies included) | Task-fit map; accountability; show confidence (JAMIA-GODDARD-2012, abstract lists mitigators) |
| Uniform drafts reduce diversity | 41% less diversity of thought in the BCG experiment (BCG-2023); LLM-assisted replies converged (LANCET-CHEN-2024) | Keep independent first drafts for judgment-heavy work (S) |
| Unreviewed drafts shipped | Deloitte report with fabricated references (GUARDIAN-DELOITTE-2025) | Named reviewer; pre-issue reference check (`professional-services-quality-review-04`, C) |
| Low use of drafts | Mean draft utilization 20% (JAMA-GARCIA-2024); 38% adherence (NBER-BRYNJOLFSSON-2023, s.5.1) | Treat low use as a diagnostic, not a target to force up |
| Skills erosion | Reduced critical-thinking effort reported with higher confidence in the tool (MSR-LEE-2025); archetype entries on unaided checks (`professional-services-talent-learning-11`, A) | Unaided skill checks |

**Value levers and metrics.** `capacity`, `speed`, `quality` (consistency), `experience` (burnout). Published: Novo Nordisk writers averaged 2.3 CSRs a year and its digitalization director says writing time was cut 90% (vendor-published customer story, quotation, ANTHROPIC-NOVO-n/d); one ambient scribe cut time-in-note 9.5% (95% CI -17.2% to -1.8%) against controls in a 238-physician randomized trial, the other -1.7% not significant (independent, NEJMAI-LUKAC-2025, abstract); workload and burnout survey measures improved with scribes, subject to confirmation (same source); inter-physician agreement rose from kappa 0.10 to 0.52 with LLM assistance in a simulation (LANCET-CHEN-2024). Quality metrics to track **(S)**: first-pass acceptance (utilization); edit size; downstream returns from the next reviewer; defects found after release; severe-error catch rate on seeded or sampled drafts; reviewer time per item; zero-edit rate as a rubber-stamp warning.

**Governance points.**
- NIST: automation bias "can exacerbate" confabulation and bias risks (NIST-AI600-2024, s.2.7); oversight processes defined (NIST-RMF-2023, MAP 3.5).
- EU AI Act: Art. 14(4)(b) automation-bias awareness; Art. 6(3) and recital 53 describe cases that may not be high-risk even in Annex III areas, including improving language of a previously drafted document, narrow procedural tasks and preparatory tasks (EU-AIACT-2024); Art. 50(4) editorial-control exemption; Annex III timing per KLGATES-OMNIBUS-2026.
- ISO/IEC 42001 (secondary): lifecycle monitoring and human oversight controls (AIGL-ISO42001-2026).
- Sector: California AB 3030 (health communications); FINRA supervision, communications and recordkeeping (FINRA-RN2409-2024; FINRA-OVERSIGHT-2026, which reports summarization and information extraction as the top GenAI use case among member firms, from FINRA's survey of firms and engagement with other regulators).

**How it evolves up the ladder.** Assist to augment: move the draft into the system of record and log draft and final. Augment to automate for narrow categories: only after tracked error and override rates meet written thresholds (`tax-compliance-corporate-21` is a phased, gated example, graded C, currently tagged `other`); reviewers move from every item to risk-tiered sampling (`professional-services-quality-review-10`, B). Delegate: agents draft and cross-check and humans approve at named gates (`professional-services-work-production-15`, C; `assurance-quality-management-18`, B). Independent machine cross-checks (`professional-services-quality-review-13`, C) are a growing idea, but the evidence found here that checker models are reliable is thin **(S)**.

**Anti-patterns.**
- Review volume exceeds reviewer capacity or skill, so sign-off becomes a stamp.
- High-severity content where a human cannot spot the failure (wrong acuity, MGB simulation).
- Drafting is the learning (juniors' first drafts).
- Content that must be original or varied for judgment tasks (BCG-2023 diversity finding).
- No baseline measure of time and error before launch (METR-2025: perceived and measured effect disagreed).

## 3. Examples

Grades follow the vocabulary. "Study" entries are experiments or evaluations rather than deployments; the note says so. Figures say what they measure.

### 3.1 `research-brief` (6 examples)

**RB-1. Anthropic (technology): multi-agent research feature.**
- *What changed:* a research question is planned by a lead agent, worked by parallel subagents with their own context windows, then passed to a citation step before the answer is returned (ANTHROPIC-MULTIAGENT-2025, "Architecture overview").
- *Ladder / scope:* augment / step.
- *Outcome:* a lead agent with sub-agents outperformed a single agent by 90.2% on Anthropic's internal research evaluation (what the 90.2% is a percentage of is not defined beyond "internal research eval"); multi-agent runs use about 15x the tokens of a chat; parallel calls cut research time by up to 90% for complex queries (ANTHROPIC-MULTIAGENT-2025, "Benefits" and "Parallel tool calling"). Provenance: vendor-published.
- *Grade:* B. The figure is a benchmark of the vendor's own product, so it is not graded A. Value for the advisor is the design lessons: effort scaling, rubric evaluation, tracing.

**RB-2. Stanford University researchers (academia): STORM, research before writing a cited article.**
- *What changed:* the system simulates perspective-guided question asking against sources, builds an outline, then writes (STANFORD-STORM-2024, abstract, Fig. 1).
- *Ladder / scope:* assist / step.
- *Outcome:* in feedback from experienced Wikipedia editors, more articles were rated organized (25% absolute increase) and broad in coverage (10% increase) than an outline-driven retrieval baseline; editors also flagged source bias transfer and over-association of unrelated facts (STANFORD-STORM-2024, abstract; feedback from 10 experienced editors in the human evaluation section). Provenance: self-reported (authors evaluating their own system).
- *Grade:* A for the study; note research prototype, not a deployment.

**RB-3. Boston Consulting Group (professional services): GPT-4 on a business problem-solving task.**
- *What changed:* more than 750 consultants did a task from interviews and performance data to find a company's root cause, with or without GPT-4 (BCG-2023, "The Value at Stake").
- *Ladder / scope:* assist / step.
- *Outcome:* with GPT-4 the group performed 23% worse than controls; 85% of the control group got the right answer; participants who were warned about wrong answers still did not challenge the output; on a creative task the same tool group performed 40% higher (BCG-2023, same section; measure is the study's performance score). Provenance: self-reported (BCG; academic co-authors analysed the data).
- *Grade:* A for the study; note a 2023 model and a controlled task.

**RB-4. Australian Securities and Investments Commission, with AWS Professional Services (financial regulator): summarising public submissions with questions about them.**
- *What changed:* a five-week proof of concept had a model summarise submissions to a parliamentary inquiry and answer prompts such as mentions of ASIC with page numbers, compared against summaries written by ASIC staff and scored by three ASIC assessors (ASIC-AWS-2024, s.1 and s.4).
- *Ladder / scope:* assist / step.
- *Outcome:* of a maximum 75 points, the aggregated human summaries scored 61 (81%) and the AI summaries scored 35 (47%); assessors generally agreed AI outputs could create more work because of fact-checking; the PoC was not used for regulatory work and tested one model at one point in time (ASIC-AWS-2024, s.1). Provenance: self-reported (ASIC assessors; report authored by AWS).
- *Grade:* A for the PoC; note early-2024 model, one use case.

**RB-5. UK Department for Science, Innovation and Technology (public sector): Consult, analysis of public consultation responses.**
- *What changed:* the tool proposes themes for every response; officials review themes in a dashboard; evaluated on a Scottish Government consultation of more than 2,000 responses (DSIT-CONSULT-2025; AIGOVUK-CONSULT-2026).
- *Ladder / scope:* augment / process (all responses analysed, not a sample).
- *Outcome:* F1 score of 0.76 against reviewers; no changes to the themes for 60% of responses; median 23 seconds to review a response; differences had negligible impact on overall theme rankings; the 75,000-day and £20m figures are a projection across about 500 consultations a year, not a measurement (DSIT-CONSULT-2025, notes and body; AIGOVUK-CONSULT-2026, "The results"). Provenance: self-reported (government).
- *Grade:* B. A measured result, but theme classification is an adjacent process to a cited brief, so the grade is capped at B. Status in July 2026: limited live testing, wider rollout planned for 2027 (AIGOVUK-CONSULT-2026).

**RB-6. Deloitte Australia (professional services): consulting review report for a government department.**
- *What changed:* a report on a welfare compliance framework was produced with help from generative AI; after press reports of nonexistent references and citations, it was re-uploaded and Deloitte was to repay the final instalment of its contract (GUARDIAN-DELOITTE-2025).
- *Ladder / scope:* assist / step. Failure case.
- *Outcome:* A$440,000 contract; refund of the final instalment confirmed by the department; the number of errors is not stated in the source. Provenance: independent (press; the department confirmed the repayment).
- *Grade:* B (named case, no published error rate).

*Archetype use cases already showing `research-brief`* (id and grade only; 43 entries: 1 A, 17 B, 14 C, 11 D): see list R at the end of this section.

### 3.2 `grounded-knowledge-assistant` (9 examples)

**G-1. UK Government Digital Service (public sector): GOV.UK Chat.**
- *What changed:* citizens ask questions in plain language of the more than 700,000-page GOV.UK estate; answers draw only on published GOV.UK guidance (GDS-GOVUKAI-2024; GDS-GOVUKCHAT-2026A).
- *Ladder / scope:* automate (public-facing pilots; no person on the normal path) / step.
- *Outcome:* accuracy 76% at the earliest benchmark to 90% latest "across all topics", assessed by subject matter experts plus automated tools, where an answer is accurate only if it meets all standards of published content; 73% of app survey respondents found it useful and 64% were satisfied; in-scope answer rate 88%; 508 jailbreak attempts all blocked; more than 10,000 users asked 26,000 questions across two pilots over 18 months; average 10.7 seconds per answer (GDS-GOVUKCHAT-2026A, findings 1 to 5 and methods). The January 2024 phase found answers "did not reach the highest level of accuracy" and a few hallucinations, mostly for ambiguous queries (GDS-GOVUKCHAT-2024). Provenance: self-reported.
- *Grade:* A.

**G-2. A Fortune 500 enterprise software company, anonymised (technology): suggested replies and documentation links for support agents.**
- *What changed:* a real-time assistant suggests responses and links to internal documentation, shown only to the agent, who may ignore it; staggered rollout after a seven-week randomized pilot of 50 agents (NBER-BRYNJOLFSSON-2023, s.2.3 and s.3.1).
- *Ladder / scope:* augment / step.
- *Outcome:* issues resolved per hour up 14% on average and 34% for novice and low-skilled agents (5,179 agents, 3 million chats); agents followed suggestions 38% of the time on average; adherence rose over time (NBER-BRYNJOLFSSON-2023, abstract and s.5.1). Provenance: independent (academic analysis of the firm's tracked metrics; a co-author disclosed other relationships).
- *Grade:* A; note the firm is not named.

**G-3. Morgan Stanley Wealth Management (financial services): AI @ Morgan Stanley Assistant.**
- *What changed:* financial advisors ask questions of the firm's knowledge base; retrieval was tuned from answering 7,000 questions to a 100,000-document corpus; summarization and translation evaluations and a daily regression suite were run (OPENAI-MORGANSTANLEY-n/d).
- *Ladder / scope:* assist / step.
- *Outcome:* "over 98% of advisor teams" use the assistant; "access to documents has jumped from 20% to 80%" (the story does not define the measure) (OPENAI-MORGANSTANLEY-n/d, final section). Provenance: vendor-published, with named Morgan Stanley executives quoted.
- *Grade:* B.

**G-4. New York City government (public sector): MyCity business chatbot.**
- *What changed:* a Microsoft-powered chatbot launched in 2023 to answer business owners' questions about city rules (MARKUP-MYCITY-2024).
- *Ladder / scope:* automate / step. Failure case.
- *Outcome:* in tests by journalists the bot said employers could take workers' tips and that landlords need not accept Section 8 vouchers, both wrong; the city called it a pilot and later added disclaimers and narrowed the questions it would answer; in January 2026 the new mayor said he planned to take it down, calling it "functionally unusable" and citing a cost of about half a million dollars (MARKUP-MYCITY-2024; MARKUP-MYCITY-2026). Provenance: independent (press testing); cost is the mayor's statement.
- *Grade:* B (named deployment, no published accuracy measurement).

**G-5. Air Canada (airline): website chatbot.**
- *What changed:* the chatbot told a customer a bereavement fare could be claimed within 90 days after ticketing; the airline's policy said otherwise (GUARDIAN-AIRCANADA-2024).
- *Ladder / scope:* automate / step. Failure case.
- *Outcome:* the tribunal ordered C$650.88 plus C$36.14 interest and C$125 in fees; the member wrote that the airline is responsible for all information on its website, whether static or from a chatbot (GUARDIAN-AIRCANADA-2024). Provenance: independent (tribunal decision as reported; decision text not retrieved).
- *Grade:* B.

**G-6. Australian Department of the Treasury (public sector): Copilot trial evaluation.**
- *What changed:* 218 staff used a retrieval-grounded assistant for 14 weeks (20 May to 23 August 2024) for structured content, knowledge management, synthesis and process tasks (ACE-TREASURY-2025, Background).
- *Ladder / scope:* assist / step.
- *Outcome:* usage lower than expected, most participants 2 to 3 times a week or less; clearest benefits in basic administrative tasks; no clear evidence of improved work outcomes in the short trial; the evaluation did not measure time saved and estimated about 13 minutes a week redirected to offset the licence cost for a mid-level officer (ACE-TREASURY-2025, Summary of findings). Provenance: self-reported (internal evaluation by the Australian Centre for Evaluation).
- *Grade:* A for the evaluation.

**G-7. Twelve UK government organizations (public sector): cross-government Copilot experiment.**
- *What changed:* 20,000 staff used an assistant over 30 September to 31 December 2024; it retrieves with the user's permissions (GDS-COPILOT-2025, s.1 and s.2).
- *Ladder / scope:* assist / step.
- *Outcome:* average 26 minutes a day saved, self-reported from range midpoints (7,115 survey responses); 17% noticed no clear saving; drafting documents saved 24 minutes; policy and HR concerns about nuance and accuracy; confidence and familiarity correlated with savings (GDS-COPILOT-2025, s.4 and s.6). Provenance: self-reported (survey of users, published by GDS).
- *Grade:* A for the trial data; time figures are user estimates.

**G-8. Stanford and Yale researchers (legal): evaluation of three commercial legal research tools.**
- *What changed:* preregistered test of retrieval-based legal research tools on 202 queries (STANFORD-LEGAL-2024, abstract and s.6).
- *Ladder / scope:* assist / step.
- *Outcome:* hallucination rates 17% (two tools) and 33% (one tool); accurate answers 65%, 42% and 20%; inter-rater agreement 85.4%, kappa 0.77 on a 48-response sample (STANFORD-LEGAL-2024, s.5 to 6.1). Provenance: independent.
- *Grade:* A.

**G-9. Siemens (manufacturing): Industrial Copilot for maintenance.**
- *What changed:* a generative assistant for maintenance staff offered as part of a predictive maintenance package (SIEMENS-COPILOT-2025).
- *Ladder / scope:* assist / step.
- *Outcome:* "first pilot use cases" are said to have saved on average 25% reactive maintenance time; pilots and method not described (SIEMENS-COPILOT-2025). Provenance: vendor-published.
- *Grade:* C.

*Archetype use cases already showing `grounded-knowledge-assistant`* (56 entries: 4 A, 29 B, 21 C, 2 D): list G below.

### 3.3 `draft-review-loop` (9 examples)

**D-1. Novo Nordisk (pharmaceuticals): clinical study report drafting.**
- *What changed:* a platform drafts clinical study reports from approved text and trial variables; people review and approve; expansion to device protocols and patient materials (ANTHROPIC-NOVO-n/d).
- *Ladder / scope:* augment / process.
- *Outcome:* writing time on CSRs cut 90% (a director's statement); headline "10+ weeks to 10 minutes" for clinical study documentation; review cycles "cut in half"; staff writers had averaged 2.3 CSRs a year; regulators gave positive feedback, per the story (ANTHROPIC-NOVO-n/d). Provenance: vendor-published customer story. No error or override rates.
- *Grade:* B. A director's quoted percentage in a vendor story is a recollection or estimate, so not A.

**D-2. Stanford Health Care (healthcare): drafted replies to patient in-basket messages.**
- *What changed:* an LLM drafts replies; 162 clinicians analysed over a 5-week pilot (JAMA-GARCIA-2024).
- *Ladder / scope:* augment / step.
- *Outcome:* mean draft utilization 20%; no significant change in read, write or reply time; burden and burnout score derivatives improved; 25% of messages had no draft available (JAMA-GARCIA-2024, Results). Provenance: independent of vendor (academic quality-improvement study by the health system).
- *Grade:* A.

**D-3. UCLA Health (healthcare): ambient AI scribes, randomized trial.**
- *What changed:* two commercial ambient scribe applications draft visit notes for physicians to review (NEJMAI-LUKAC-2025).
- *Ladder / scope:* augment / step.
- *Outcome:* 238 physicians in 14 specialties; scribes used in 33.5% and 29.5% of visits; time-in-note down 9.5% for one scribe and -1.7% (not significant) for the other; burnout-related scores improved; clinically significant inaccuracies noted "occasionally" (Likert 2.7 and 2.8 of 5); one mild adverse event (NEJMAI-LUKAC-2025, abstract). Provenance: independent.
- *Grade:* A; note only the abstract was read.

**D-4. Mass General Brigham and Dana-Farber researchers (healthcare): LLM drafts of patient-message replies, simulation.**
- *What changed:* six radiation oncologists wrote replies, then edited GPT-4 drafts for 100 simulated cancer-patient messages (LANCET-CHEN-2024).
- *Ladder / scope:* augment / step.
- *Outcome:* reviewers judged drafts as posing risk of severe harm in 7.1% (11 of 156) of survey responses and death in 0.6% (1); drafts improved subjective efficiency in 76.9% (120 of 156); assisted replies were more similar to drafts than to manual replies (LANCET-CHEN-2024, Results). Provenance: independent.
- *Grade:* A for the study; note it is a simulation, not a deployment.

**D-5. Google (technology): suggested code edits that resolve reviewer comments.**
- *What changed:* a model proposes the edit for each reviewer comment; authors apply it in the review tool or IDE (GOOGLE-CODEREVIEW-2023).
- *Ladder / scope:* augment / step.
- *Outcome:* calibrated to 50% target precision; offline, 52% of comments addressed at that precision; suggestions shown for around 50% of relevant comments; 40% to 50% of previewed suggestions applied; authors needed about 60 minutes average active shepherding time per change (before). Google expects savings of "hundreds of thousands of hours annually" (an expectation, not a result) (GOOGLE-CODEREVIEW-2023, "Results"). Provenance: self-reported.
- *Grade:* A.

**D-6. Morgan Stanley (financial services): Debrief, client-meeting notes and follow-ups.**
- *What changed:* recordings, with client consent, become notes entered into the CRM and draft follow-ups that advisors refine and send (OPENAI-MORGANSTANLEY-n/d).
- *Ladder / scope:* augment / step.
- *Outcome:* a Morgan Stanley executive says follow-ups that took days now take hours; evaluation datasets of meeting types were used to test action-item capture without errors; no figures (OPENAI-MORGANSTANLEY-n/d). Provenance: vendor-published.
- *Grade:* B.

**D-7. METR (research nonprofit): experienced open-source developers, randomized trial.**
- *What changed:* 16 developers did 246 tasks on mature projects, each randomly allowed or not allowed to use AI coding tools (METR-2025, abstract).
- *Ladder / scope:* assist / step.
- *Outcome:* tasks took 19% longer with AI allowed; developers had forecast 24% faster and afterwards estimated 20% faster (METR-2025, abstract). Provenance: independent.
- *Grade:* A for the study; note early-2025 tools, a specific population.

**D-8. Microsoft Research, GitHub and MIT Sloan authors (technology): controlled experiment with an AI pair programmer.**
- *What changed:* 95 professional developers implemented an HTTP server in JavaScript with or without the tool (MSR-PENG-2023, abstract).
- *Ladder / scope:* assist / step.
- *Outcome:* treated group 55.8% faster (average 71.17 vs 160.89 minutes; 95% CI 21% to 89%) (MSR-PENG-2023, results). Provenance: vendor-published (authors include employees of the tool's maker).
- *Grade:* A for the study; note one task, 2022 tool.

**D-9. MIT researchers (professional writing): ChatGPT on occupation-specific writing tasks.**
- *What changed:* 444 college-educated professionals wrote incentivized tasks, half exposed to the tool (MIT-NOY-2023, abstract).
- *Ladder / scope:* assist / step.
- *Outcome:* time taken down 0.8 SD, output quality up 0.4 SD; effort shifted toward idea generation and editing and away from rough drafting; gap between low- and high-ability workers narrowed (MIT-NOY-2023, abstract). Provenance: independent.
- *Grade:* A for the study; note a preregistered online experiment, not a deployment.

*Archetype use cases already showing `draft-review-loop`* (124 entries: 8 A, 43 B, 58 C, 15 D): list D below.

### 3.4 Archetype use cases already carrying these patterns (id and grade only)

**R. `research-brief`:** 
assurance-completion-reporting-09 (C); assurance-completion-reporting-12 (D); assurance-substantive-testing-19 (D); assurance-sustainability-assurance-04 (D); assurance-sustainability-assurance-12 (C); assurance-planning-risk-assessment-01 (B); assurance-planning-risk-assessment-04 (C); assurance-planning-risk-assessment-12 (D); tax-controversy-25 (D); tax-research-advisory-02 (B); tax-research-advisory-03 (C); tax-research-advisory-04 (D); tax-research-advisory-10 (D); tax-transfer-pricing-05 (C); tax-transfer-pricing-06 (C); tax-transfer-pricing-18 (D); tax-transfer-pricing-19 (C); professional-services-pursuit-proposals-08 (B); professional-services-pursuit-proposals-09 (B); professional-services-pursuit-proposals-16 (C); professional-services-client-development-04 (C); professional-services-client-development-06 (B); professional-services-knowledge-management-04 (C); professional-services-knowledge-management-17 (B); professional-services-scoping-pricing-03 (C); professional-services-acceptance-risk-06 (B); professional-services-acceptance-risk-07 (D); professional-services-work-production-01 (B); professional-services-work-production-02 (B); security-vulnerability-exposure-23 (D); security-incident-response-04 (B); security-incident-response-08 (B); security-governance-risk-10 (C); security-identity-access-13 (C); security-data-privacy-04 (C); security-ai-security-18 (A); security-human-risk-11 (B); security-human-risk-18 (D); security-threat-intelligence-02 (B); security-threat-intelligence-10 (B); security-threat-intelligence-19 (B); security-threat-intelligence-24 (B); security-operations-10 (B)

**G. `grounded-knowledge-assistant`:** 
assurance-substantive-testing-06 (C); assurance-soc-attestation-10 (C); assurance-soc-attestation-11 (C); assurance-quality-management-12 (B); assurance-planning-risk-assessment-02 (B); assurance-planning-risk-assessment-20 (B); assurance-controls-testing-22 (D); assurance-specialists-12 (C); assurance-specialists-13 (B); tax-compliance-corporate-11 (C); tax-controversy-06 (C); tax-controversy-20 (B); tax-controversy-22 (C); tax-provision-pillar-two-01 (C); tax-provision-pillar-two-14 (C); tax-research-advisory-01 (B); tax-research-advisory-05 (C); tax-research-advisory-06 (C); tax-research-advisory-07 (B); tax-research-advisory-08 (B); tax-research-advisory-16 (B); tax-indirect-tax-05 (B); tax-indirect-tax-06 (A); tax-transfer-pricing-01 (C); tax-data-technology-06 (B); tax-data-technology-17 (C); tax-compliance-individual-business-11 (B); professional-services-pursuit-proposals-01 (B); professional-services-pursuit-proposals-02 (B); professional-services-pursuit-proposals-12 (B); professional-services-client-development-07 (C); professional-services-client-development-21 (B); professional-services-delivery-management-04 (B); professional-services-knowledge-management-01 (B); professional-services-knowledge-management-02 (B); professional-services-knowledge-management-03 (B); professional-services-knowledge-management-08 (C); professional-services-knowledge-management-09 (C); professional-services-knowledge-management-12 (B); professional-services-knowledge-management-13 (B); professional-services-knowledge-management-19 (B); professional-services-knowledge-management-22 (B); professional-services-staffing-resourcing-09 (C); professional-services-scoping-pricing-04 (B); professional-services-scoping-pricing-23 (B); professional-services-acceptance-risk-11 (D); professional-services-work-production-17 (B); security-incident-response-06 (C); security-governance-risk-01 (A); security-identity-access-09 (C); security-data-privacy-12 (C); security-data-privacy-19 (C); security-threat-intelligence-11 (B); security-operations-02 (A); security-operations-11 (B); security-operations-12 (A)

**D. `draft-review-loop`:** 
assurance-completion-reporting-07 (C); assurance-completion-reporting-08 (C); assurance-completion-reporting-13 (C); assurance-completion-reporting-14 (B); assurance-completion-reporting-17 (D); assurance-substantive-testing-23 (D); assurance-acceptance-independence-08 (C); assurance-soc-attestation-02 (C); assurance-soc-attestation-09 (B); assurance-quality-management-18 (B); assurance-quality-management-19 (C); assurance-quality-management-20 (D); assurance-quality-management-21 (B); assurance-quality-management-22 (D); assurance-sustainability-assurance-05 (D); assurance-sustainability-assurance-08 (C); assurance-planning-risk-assessment-09 (B); assurance-planning-risk-assessment-10 (C); assurance-planning-risk-assessment-14 (C); assurance-planning-risk-assessment-16 (D); assurance-planning-risk-assessment-18 (B); assurance-planning-risk-assessment-25 (B); assurance-controls-testing-01 (B); assurance-controls-testing-02 (B); assurance-controls-testing-10 (B); assurance-controls-testing-12 (C); assurance-controls-testing-16 (B); assurance-specialists-03 (C); assurance-specialists-06 (D); tax-compliance-corporate-04 (C); tax-compliance-corporate-05 (C); tax-compliance-corporate-18 (C); tax-compliance-corporate-19 (C); tax-controversy-02 (C); tax-controversy-07 (C); tax-controversy-08 (C); tax-provision-pillar-two-06 (D); tax-research-advisory-09 (B); tax-research-advisory-11 (D); tax-research-advisory-14 (B); tax-research-advisory-15 (D); tax-research-advisory-19 (B); tax-indirect-tax-07 (C); tax-indirect-tax-20 (B); tax-transfer-pricing-02 (C); tax-transfer-pricing-07 (C); tax-transfer-pricing-10 (C); tax-transfer-pricing-11 (C); tax-transfer-pricing-16 (C); tax-transfer-pricing-17 (D); tax-transfer-pricing-21 (B); tax-compliance-individual-business-12 (B); tax-compliance-individual-business-15 (C); professional-services-pursuit-proposals-10 (C); professional-services-pursuit-proposals-11 (C); professional-services-pursuit-proposals-13 (C); professional-services-pursuit-proposals-14 (C); professional-services-pursuit-proposals-17 (D); professional-services-client-development-08 (C); professional-services-client-development-09 (C); professional-services-client-development-12 (B); professional-services-client-development-16 (B); professional-services-delivery-management-01 (B); professional-services-delivery-management-02 (B); professional-services-delivery-management-03 (B); professional-services-knowledge-management-14 (C); professional-services-knowledge-management-15 (C); professional-services-talent-learning-06 (C); professional-services-talent-learning-07 (B); professional-services-talent-learning-09 (C); professional-services-talent-learning-10 (C); professional-services-talent-learning-11 (A); professional-services-talent-learning-17 (C); professional-services-quality-review-03 (C); professional-services-quality-review-04 (C); professional-services-quality-review-08 (B); professional-services-quality-review-10 (B); professional-services-quality-review-12 (D); professional-services-quality-review-13 (C); professional-services-billing-collections-02 (C); professional-services-billing-collections-03 (C); professional-services-billing-collections-09 (C); professional-services-scoping-pricing-01 (B); professional-services-scoping-pricing-02 (C); professional-services-scoping-pricing-05 (B); professional-services-work-production-05 (B); professional-services-work-production-06 (A); professional-services-work-production-07 (A); professional-services-work-production-08 (B); professional-services-work-production-09 (B); professional-services-work-production-10 (D); professional-services-work-production-11 (B); professional-services-work-production-15 (C); professional-services-work-production-19 (B); security-vulnerability-exposure-04 (A); security-vulnerability-exposure-12 (A); security-vulnerability-exposure-14 (C); security-vulnerability-exposure-19 (B); security-vulnerability-exposure-20 (B); security-incident-response-02 (C); security-incident-response-09 (C); security-incident-response-14 (A); security-incident-response-15 (C); security-incident-response-16 (B); security-governance-risk-08 (B); security-governance-risk-14 (C); security-governance-risk-15 (B); security-identity-access-11 (D); security-data-privacy-15 (C); security-human-risk-03 (C); security-human-risk-06 (C); security-threat-intelligence-12 (B); security-threat-intelligence-13 (B); security-threat-intelligence-14 (C); security-operations-13 (B); security-operations-15 (A); security-cloud-infrastructure-06 (B); security-cloud-infrastructure-11 (C); security-cloud-infrastructure-13 (C); security-cloud-infrastructure-15 (C); security-cloud-infrastructure-18 (C); security-application-security-04 (A); security-application-security-05 (B); security-application-security-12 (B)

## 4. Expert moves and probes

Probes are the analyst's synthesis **(S)** from the evidence in sections 2, 3 and 5; the "reveals" column says what the answer tells the advisor.

### 4.1 `research-brief`

| # | Ask or do | What it reveals |
|---|---|---|
| 1 | "Walk me through the last brief. Who reads the sources behind the key claims, and how long does that take?" | Whether review exists and its true cost; if nobody opens sources, the pattern is unsafe (Deloitte case, GUARDIAN-DELOITTE-2025) |
| 2 | "Which claims would hurt you if wrong, and which are background?" | The split between 100% verification and sampling; decision-driving claims need full checks |
| 3 | "What corpus may the tool read, and who owns it?" | Access, licensing, confidentiality and whether an approved source list is possible |
| 4 | "Give me ten past briefs with the answer you now know to be right." | Whether a gold set exists for evaluation; if not, the first project is building one (ANTHROPIC-MULTIAGENT-2025 started with about 20 queries) |
| 5 | "Is the question breadth-first (many independent angles) or one deep judgment?" | Fit: breadth-first favours the pattern; nuanced weighing of mixed evidence sits outside the reliable range (BCG-2023) |
| 6 | "What does the brief feed: a meeting, a client deliverable, a public document, a regulated decision?" | Risk tier and disclosure duties (EU-AIACT-2024 Art. 50(4), Annex III 8(a)) |
| 7 | "What happens today when you cannot find an answer?" | Whether "not found" is an acceptable output; tools that guess rather than decline are a known failure (CJR-TOW-2025) |
| 8 | "How many hours go to gathering versus judging?" | The capacity lever and where the freed hours would go (business-case rule: hours are not value until they have a destination, library index s.5) |
| 9 | "Would you let a junior do this unaided first?" | Whether the research itself is the learning path (`professional-services-talent-learning-09`) |
| 10 | "How often is the same scan repeated?" | Whether a scheduled background brief (higher rung) is justified |

### 4.2 `grounded-knowledge-assistant`

| # | Ask or do | What it reveals |
|---|---|---|
| 1 | "Which document is the single source of truth for this answer, and who owns it?" | Content ownership; the stale-content failure mode (library index s.3) |
| 2 | "Show me five answers staff gave last month that were wrong or out of date." | Real error classes and a seed for the gold set |
| 3 | "Who asks, and who bears the cost of a wrong answer: staff, client, citizen?" | Audience risk: public-facing answers become published policy (GUARDIAN-AIRCANADA-2024) |
| 4 | "What should it refuse, and where does the person go instead?" | Scope and handoff design (NIST-AI600-2024 GV-3.2-003; GDS-GOVUKCHAT-2026A finding 4) |
| 5 | "Are document permissions clean?" | Over-sharing risk when retrieval follows user access (GDS-COPILOT-2025 s.2.1) |
| 6 | "How will you score accuracy, how often, and with whom?" | Whether an evaluation plan exists; GOV.UK scored hundreds of conversations manually and added live monitoring (GDS-GOVUKCHAT-2026A, 2026B) |
| 7 | "Ask the same question ten times. Do you get the same answer?" | Consistency; MyCity gave inconsistent answers to one question (MARKUP-MYCITY-2024) |
| 8 | "Does every answer show the passage it came from?" | Checkability; reduces the verification tax |
| 9 | "What share of suggestions do people use, and why do they decline the rest?" | Adherence as a quality signal (38% in NBER-BRYNJOLFSSON-2023 s.5.1) |
| 10 | "Is this really a client-facing agent in disguise?" | Whether the work belongs to `service-agent-escalation` with escalation rules and sampling |

### 4.3 `draft-review-loop`

| # | Ask or do | What it reveals |
|---|---|---|
| 1 | "Who signs off, what do they check, and how much time do they have per item?" | Whether review is real or a stamp; reviewer capacity |
| 2 | "What is the worst error that could pass review, and would the reviewer see it?" | Severity: wrong acuity passed the physicians' notice in 7.1% of drafts in a simulation (LANCET-CHEN-2024) |
| 3 | "How long does the whole task take now, end to end, including checking?" | A baseline; perceived and measured effects can disagree (METR-2025) |
| 4 | "What share of drafts are used as is, edited, or discarded today?" | Utilization or override rate as the primary quality metric (20% in JAMA-GARCIA-2024) |
| 5 | "Does the reviewer form a view before seeing the draft?" | Anchoring risk (LANCET-CHEN-2024) and automation bias (JAMIA-GODDARD-2012) |
| 6 | "What approved text and templates will drafts draw on?" | Grounding and consistency (Novo Nordisk, ANTHROPIC-NOVO-n/d) |
| 7 | "Would any category of item be safe to move to sampled review? What error rate would you accept?" | Whether thresholds can be written down; precondition for automate (NIST-SEMATECH-ACCEPT) |
| 8 | "Who learns from drafting today, and what replaces that?" | Skills erosion and junior-role effects (MSR-LEE-2025; archetype `professional-services-talent-learning-*`) |
| 9 | "Do you have to tell the recipient the draft was AI-generated?" | Disclosure rules and review exemptions (CALEG-AB3030-2024; EU-AIACT-2024 Art. 50) |
| 10 | "Where is the draft, the edit and the final stored?" | Whether override and edit metrics can be computed and audit trails kept (FINRA-OVERSIGHT-2026) |

## 5. Evidence on what works and what fails

Provenance column says who measured. "n" is the sample.

| Ref | Study or analysis | What it measures | Result | Provenance | Pattern |
|---|---|---|---|---|---|
| STANFORD-LEGAL-2024 | Preregistered evaluation of three retrieval-based legal research tools, n=202 queries | Share of responses correct and grounded, incomplete, hallucinated (labels by humans; kappa 0.77 on 48-response check) | Hallucinated 17% to 33%; accurate 65%, 42%, 20% | independent | grounded; research-brief |
| STANFORD-LIU-2023 | Human evaluation of four generative search engines | Citation recall (share of sentences fully supported by citations) and citation precision (share of citations supporting their sentence) | 51.5% and 74.5% on average | independent | research-brief |
| CJR-TOW-2025 | Eight generative search tools, 1,600 queries | Whether the tool identified the correct article, publisher and URL for a quoted excerpt | Collectively incorrect on more than 60%; premium tools more confidently wrong; fabricated links | independent | research-brief |
| BBC-EBU-2025 | 22 public service media organizations, 14 languages, 2,709 evaluated core responses from four assistants | Share of responses with at least one significant issue on five criteria, rated by journalists | 45% any issue; sourcing 31%; accuracy 20%; BBC-only comparison improved 51% to 37% | independent | research-brief; grounded |
| BBC-IPSOS-2025 | Survey of 2,000 UK adults (May 2025) | Trust in AI summaries and effect of errors on trust | Just over a third trust AI to produce accurate summaries; 84% say a factual error would have a major impact on trust | independent | all |
| BCG-2023 | Experiment, more than 750 consultants | Performance on a task inside and a task outside GPT-4's range | +40% inside; -23% outside; warned users did not challenge; diversity of ideas -41% | self-reported (firm, with academics) | research-brief; draft |
| ASIC-AWS-2024 | PoC, three ASIC assessors, human vs AI summaries | Rubric score out of 75 | Human 61 (81%), AI 35 (47%) | self-reported | research-brief |
| NBER-BRYNJOLFSSON-2023 | Staggered rollout, 5,179 agents | Issues resolved per hour; adherence | +14% (34% for novices); adherence 38% | independent | grounded |
| GDS-GOVUKCHAT-2026A | Two public pilots, more than 10,000 users | Expert and automated accuracy scoring; survey | Accuracy 76% to 90%; 73% useful | self-reported | grounded |
| GDS-COPILOT-2025; ACE-TREASURY-2025 | Cross-government trial (n=7,115 survey) and Treasury evaluation (218 staff) | Self-estimated time saved; usage; quality ratings | 26 min/day self-reported; Treasury found no clear quality gain and lower-than-expected use | self-reported | grounded; draft |
| LANCET-CHEN-2024 | Simulation, six oncologists | Risk of severe harm per physician judgment; agreement | 7.1% severe-harm risk; kappa 0.10 to 0.52 | independent | draft |
| JAMA-GARCIA-2024 | 5-week QI pilot, 162 clinicians | Draft utilization; reply, read and write time | 20% utilization; no significant time change | independent of vendor | draft |
| NEJMAI-LUKAC-2025 | Randomized trial, 238 physicians | Change in time-in-note; burnout scales | -9.5% and -1.7% (ns); burnout measures improved | independent | draft |
| METR-2025 | Randomized trial, 16 developers, 246 tasks | Completion time with vs without AI | 19% slower; forecast 24% faster | independent | draft |
| MSR-PENG-2023 | Controlled experiment, 95 developers | Task completion time | 55.8% faster | vendor-published | draft |
| MIT-NOY-2023 | Preregistered experiment, 444 professionals | Time and graded quality | -0.8 SD time; +0.4 SD quality | independent | draft |
| DSIT-CONSULT-2025 | Live evaluation, over 2,000 responses | F1 vs human themes; share unchanged by reviewers; review time | 0.76; 60% unchanged; 23 s median | self-reported | research synthesis |
| JAMIA-GODDARD-2012 | Systematic review, 74 studies of 13,821 retrieved | Frequency, mediators and mitigators of automation bias | Effect "fairly robust and generic"; mitigators include training, accountability and how advice is displayed | independent | all |
| MSR-LEE-2025 | Survey, 319 knowledge workers | Self-reported critical thinking effort | Higher confidence in GenAI associated with less critical thinking | independent academic survey (Carnegie Mellon and Microsoft Research authors) | all |
| DEAKIN-BARNETT-2024 | Experience report, three RAG case studies | Failure points | Seven; validation "only feasible during operation" | independent | grounded |
| MCKINSEY-STATEOFAI-2026 | Survey, 1,719 respondents, May to June 2026 | Self-reported EBIT impact; practices of high performers | 37% attribute some EBIT impact; about 6% are high performers; high performers redesign workflows rather than insert AI into existing ones | survey (consultancy-published) | all |
| CHARLOTIN-DB-n/d | Database of court decisions on hallucinated content | Count of decisions | 2,202 cases as of 2026-10-20 retrieval | independent (individual researcher; counts only cases courts addressed) | research-brief; draft |

**What the evidence says works (S, drawn from the rows).**
- Narrow scope and measured accuracy before wide release (GOV.UK Chat's phased pilots; Morgan Stanley's evaluations).
- Expert-scored samples with continuing monitoring, rather than one-off tests (GDS-GOVUKCHAT-2026B; ANTHROPIC-MULTIAGENT-2025).
- Tasks inside the tool's reliable range, with the reviewer able to tell right from wrong (BCG-2023).
- Beneficiaries are often less experienced staff (NBER-BRYNJOLFSSON-2023: 34% novices; MSR-PENG-2023 and MIT-NOY-2023 heterogeneity), which is also where over-trust and skill erosion risks concentrate (MSR-LEE-2025).

**What fails.**
- Public bots with no scope limit or measured accuracy (MARKUP-MYCITY-2024; GUARDIAN-AIRCANADA-2024).
- Unreviewed outputs reaching clients or the public (GUARDIAN-DELOITTE-2025; court decisions in CHARLOTIN-DB-n/d).
- Checking costs that wipe out time gains (JAMA-GARCIA-2024; ASIC-AWS-2024; METR-2025).
- Review that anchors on the draft (LANCET-CHEN-2024; JAMIA-GODDARD-2012).

**Quality evidence is thin.** Direct override, escalation and error rates in production are published only in a few places (draft utilization 20% in JAMA-GARCIA-2024; adherence 38% in NBER-BRYNJOLFSSON-2023; accuracy 90% in GDS-GOVUKCHAT-2026A; suggestion-applied 40% to 50% in GOOGLE-CODEREVIEW-2023). No source gave an escalation rate for a research-brief deployment, and none gave a parallel-run error comparison for a drafted deliverable against a human-only baseline in a regulated document workflow. The nearest are ASIC-AWS-2024 (human vs AI summaries) and the randomized trials in healthcare and software.

## Routing note: archetype use cases tagged `pattern: other` that should carry one of these ids

From titles and problem statements only; details were not re-researched. Verify before changing.

| Use-case id | Suggested pattern | Reason |
|---|---|---|
| `professional-services-billing-collections-01` | `draft-review-loop` | Capture layer drafts time entries and narratives; the professional reviews, edits and releases them |
| `tax-compliance-corporate-21` | `draft-review-loop` | Gated rollout of AI-drafted return work with 100% logging, override-rate review and error-rate thresholds; it is the control loop around the pattern and would carry the pattern with a note |
| `professional-services-knowledge-management-21` | `draft-review-loop` | Idea: AI-drafted stories reviewed by the expert who holds the knowledge |
| `professional-services-knowledge-management-20` | `grounded-knowledge-assistant` | Per-person AI personas answering colleagues from that person's work product; note the corpus owner is an individual |
| `professional-services-delivery-management-11` | none of these (consider `end-to-end-case-agent`) | Template that routes tasks to agents and people with review gates; the drafting inside is a `draft-review-loop` but this entry holds the coordination layer |

Others skimmed (for example the governance and policy entries `assurance-quality-management-01`, `-02`, `professional-services-quality-review-01`) describe controls around all patterns rather than a pattern of their own and were left as `other`.

## 6. Gaps

- **Retail.** No measured outcome for any of these three patterns in retail was found. Retail material surfaced was vendor product pages and Walmart's own 2025 announcement of associate tools for task management and translation, which fall under other patterns (WALMART-2025). Retail is therefore absent from the graded examples.
- **Manufacturing.** One vendor claim (SIEMENS-COPILOT-2025, grade C). A search for a named manufacturer's measured result (for example Schaeffler) found none.
- **Override and escalation rates.** Almost no organization publishes them for these patterns; see section 5.
- **Not retrieved or partial.** ISO/IEC 42001 text (ISO-42001-2023, paywalled and blocked; covered only by a secondary guide, AIGL-ISO42001-2026, with search-only snippets from other guides disagreeing on the Annex A grouping); the Air Canada tribunal decision text (reported via the press); the official text of Regulation (EU) 2026/1744 (reported via a law-firm summary); the NEJM AI scribe trial beyond its abstract; Kaiser Permanente's NEJM Catalyst ambient-scribe report (blocked); the HBS working paper behind the BCG experiment (figures taken from BCG's own page); the Australian DTA whole-of-government Copilot evaluation (DTA-COPILOT-2024; search-only snippets, not used for figures); Gartner's abandonment forecast (blocked); Fed SR 11-7 and ABA Formal Opinion 512 (fetch returned no usable text, so not cited).
- **Undated pages.** The OpenAI Morgan Stanley story, the Anthropic Novo Nordisk story and FINRA's 2026 oversight report page show no publication date; they are marked n/d and should be dated before use in client material. The Charlotin database is a live count.
- **Vendor and study limits.** Several controlled studies use 2022 to early-2025 models (MSR-PENG-2023, BCG-2023, METR-2025, ASIC-AWS-2024); results may not carry to current models. Stanford and BCG figures concern specific tasks.
- **Cost evidence.** Apart from Anthropic's token multiples and the Treasury evaluation's licence break-even estimate, no source gives cost per item.
- **Cross-industry balance.** Healthcare, public sector and technology are well evidenced; financial services and professional services have more vendor-published and regulatory material than measured outcomes; no example from education, energy or insurance was found.

## 7. Sources

"Gov" in the type column means a government body acting as deployer or evaluator; the controlled type is shown first. Access `full` means opened and read (the NEJM AI trial and the ISO text are noted).

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| NIST-RMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| NIST-AI600-2024 | AI RMF: Generative AI Profile, NIST AI 600-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| EU-AIACT-2024 | Regulation (EU) 2024/1689 (AI Act), consolidated text as retrieved from EUR-Lex | European Union | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689 | 2024-06-13 (regulation date; original text, before the 2026 omnibus) | full |
| KLGATES-OMNIBUS-2026 | EU Digital Omnibus on AI Enters Into Force (Regulation (EU) 2026/1744) | K&L Gates LLP via National Law Review | professional-body (law-firm alert) | https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force | 2026-07-31 | full |
| FINRA-RN2409-2024 | Regulatory Notice 24-09: FINRA Reminds Members of Regulatory Obligations When Using Generative AI and LLMs | FINRA | regulator | https://www.finra.org/rules-guidance/notices/24-09 | 2024-06-27 | full |
| FINRA-OVERSIGHT-2026 | 2026 FINRA Annual Regulatory Oversight Report: GenAI, Continuing and Emerging Trends | FINRA | regulator | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai | n/d (page shows no date; accessed 2026-10-20) | full |
| CALEG-AB3030-2024 | AB 3030 (chaptered), Health and Safety Code s.1339.75 | California Legislature | regulator | https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB3030 | 2024 (chaptered 2023-24 session; month not shown) | full (via text mirror) |
| ISO-42001-2023 | ISO/IEC 42001:2023 Artificial intelligence, management system | ISO/IEC | standard-setter | https://www.iso.org/standard/81230.html | 2023-12 | search-only (publisher page blocked; text paywalled) |
| AIGL-ISO42001-2026 | AIMS Simplified: What ISO 42001 Actually Requires (review of a practitioner guide) | AI Governance Library (J. Szarmach) | community | https://www.aigl.blog/aims-simplified-iso-42001-annex-a-controls-guide/ | 2026-08-31 | full (secondary summary) |
| NIST-SEMATECH-ACCEPT | NIST/SEMATECH e-Handbook of Statistical Methods, 6.2.1 What is Acceptance Sampling? | NIST Information Technology Laboratory | standard-setter | https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm | n/d (foundation text; accessed 2026-10-20) | full |
| STANFORD-LEGAL-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | V. Magesh, F. Surani, M. Dahl, M. Suzgun, C. Manning, D. Ho (Stanford, Yale) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 (text updated 2024-06-03) | full |
| STANFORD-LIU-2023 | Evaluating Verifiability in Generative Search Engines | N. Liu, T. Zhang, P. Liang (Stanford) | academic | https://arxiv.org/abs/2304.09848 | 2023-04 (v2 2023-10-23) | full |
| STANFORD-STORM-2024 | Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models | Y. Shao et al. (Stanford) | academic | https://arxiv.org/abs/2402.14207 | 2024-02 (v2 2024-04-08) | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work, NBER Working Paper 31161 | E. Brynjolfsson, D. Li, L. Raymond | academic | https://www.nber.org/papers/w31161 | 2023-04 (revised 2023-11) | full |
| MIT-NOY-2023 | Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence (working paper, not peer reviewed) | S. Noy, W. Zhang (MIT) | academic | https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf | 2023-03-02 | full |
| MSR-PENG-2023 | The Impact of AI on Developer Productivity: Evidence from GitHub Copilot | S. Peng, E. Kalliamvakou, P. Cihon, M. Demirer (Microsoft Research, GitHub, MIT Sloan) | academic (vendor-affiliated) | https://arxiv.org/abs/2302.06590 | 2023-02-13 | full |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | J. Becker, N. Rush, B. Barnes, D. Rein (METR) | academic | https://arxiv.org/abs/2507.09089 | 2025-07 (v2 2025-07-25) | full |
| MSR-LEE-2025 | The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers (CHI '25) | H.-P. Lee, A. Sarkar, L. Tankelevitch et al. (Carnegie Mellon, Microsoft Research) | academic | https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf | 2025-04 (CHI '25, 26 April to 1 May 2025) | full |
| JAMIA-GODDARD-2012 | Automation bias: a systematic review of frequency, effect mediators, and mitigators | K. Goddard, A. Roudsari, J. Wyatt (JAMIA) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ | 2011-06-16 (print 2012) | full |
| DEAKIN-BARNETT-2024 | Seven Failure Points When Engineering a Retrieval Augmented Generation System | S. Barnett et al. (Deakin University) | academic | https://arxiv.org/abs/2401.05856 | 2024-01-11 | full |
| LANCET-CHEN-2024 | The effect of using a large language model to respond to patient messages | S. Chen et al., Lancet Digital Health 6(6):e379 | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC11829255/ | 2024-04-24 | full |
| JAMA-GARCIA-2024 | Artificial Intelligence-Generated Draft Replies to Patient Inbox Messages | P. Garcia et al., JAMA Network Open | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC10955355/ | 2024-03-04 | full |
| NEJMAI-LUKAC-2025 | Ambient AI Scribes in Clinical Practice: A Randomized Trial | P. Lukac et al., NEJM AI | academic | https://europepmc.org/article/MED/41497288 | 2025-11-26 | full for the abstract and metadata only (full text not retrieved) |
| CJR-TOW-2025 | AI Search Has a Citation Problem | Tow Center for Digital Journalism, Columbia Journalism Review | academic | https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php | 2025-03 | full (via text mirror) |
| BBC-EBU-2025 | News Integrity in AI Assistants: An international PSM study | BBC and European Broadcasting Union | professional-body | https://www.bbc.co.uk/aboutthebbc/documents/news-integrity-in-ai-assistants-report.pdf | 2025-10 | full |
| BBC-IPSOS-2025 | Audience Use and Perceptions of AI Assistants for News | BBC and Ipsos | survey | https://www.bbc.co.uk/aboutthebbc/documents/audience-use-and-perceptions-of-ai-assistants-for-news.pdf | 2025-10 | full |
| MCKINSEY-STATEOFAI-2026 | The state of AI in 2026: On the road to ROI | McKinsey and Company | survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026-08-25 | full (via text mirror) |
| BCG-2023 | How People Can Create, and Destroy, Value with Generative AI | Boston Consulting Group (with academic co-authors) | firm | https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai | 2023-09-21 | full (via text mirror) |
| GDS-COPILOT-2025 | Microsoft 365 Copilot Experiment: Cross-Government Findings Report | UK Government Digital Service | regulator (gov) | https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html | 2025-06-02 | full |
| GDS-GOVUKAI-2024 | Experimenting with how generative AI could help GOV.UK users | UK Government Digital Service (C. Bellamy) | regulator (gov) | https://insidegovuk.blog.gov.uk/2024/01/18/experimenting-with-how-generative-ai-could-help-gov-uk-users/ | 2024-01-18 | full |
| GDS-GOVUKCHAT-2024 | The findings of our first generative AI experiment: GOV.UK Chat | UK Government Digital Service | regulator (gov) | https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | 2024-01-18 | full |
| GDS-GOVUKCHAT-2026A | 5 things we learned testing GOV.UK Chat: an AI assistant for government | UK Government Digital Service | regulator (gov) | https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/ | 2026-03-16 | full |
| GDS-GOVUKCHAT-2026B | Developing GOV.UK Chat: our data science and AI engineering journey | UK Government Digital Service | regulator (gov) | https://insidegovuk.blog.gov.uk/2026/05/15/developing-gov-uk-chat-our-data-science-and-ai-engineering-journey/ | 2026-05-15 | full |
| DSIT-CONSULT-2025 | Government-built Humphrey AI tool reviews responses to consultation for first time (press release) | UK Department for Science, Innovation and Technology | regulator (gov) | https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions | 2025-05-14 | full |
| AIGOVUK-CONSULT-2026 | Consult: processing consultation responses to support policymaking (project page, archived copy) | UK i.AI | regulator (gov) | https://tnaqa.mirrorweb.com/ukgwa/20260902044439mp_/https://ai.gov.uk/knowledge-hub/tools/consult | 2026-07-23 (last updated; created 2025-05-09) | full |
| ACE-TREASURY-2025 | Evaluation of a trial of generative AI (Copilot) in the Department of the Treasury: Summary report | Australian Centre for Evaluation | regulator (gov) | https://evaluation.treasury.gov.au/sites/evaluation.treasury.gov.au/files/2025-02/evaluation-generative-artificial-intelligence-summary.pdf | 2025-02 | full |
| DTA-COPILOT-2024 | Microsoft 365 Copilot trial: summary of evaluation findings | Australian Digital Transformation Agency | regulator (gov) | https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary | 2024-10 | search-only (not cited for any figure) |
| ASIC-AWS-2024 | ASIC Gen AI Document Summarisation PoC, draft report as at 21 May 2024 (answer to Senate question on notice 002, received 5 July 2024) | ASIC and AWS Professional Services, via Parliament of Australia | regulator | https://www.aph.gov.au/DocumentStore.ashx?id=b4fd6043-6626-4cbe-b8ee-a5c7319e94a0&subId=766627 | 2024-07 | full (via text mirror) |
| MARKUP-MYCITY-2024 | NYC's AI Chatbot Tells Businesses to Break the Law | The Markup and THE CITY (C. Lecher) | press | https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law | 2024-03-29 | full |
| MARKUP-MYCITY-2026 | Mamdani to kill the NYC AI chatbot we caught telling businesses to break the law | The Markup and THE CITY (C. Lecher, K. Honan) | press | https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law | 2026-01-30 | full |
| GUARDIAN-AIRCANADA-2024 | Air Canada ordered to pay customer who was misled by airline's chatbot | The Guardian (L. Cecco) | press | https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit | 2024-02-16 | full |
| GUARDIAN-DELOITTE-2025 | Deloitte to pay money back to Albanese government after using AI in $440,000 report | The Guardian (K. Dhanji) | press | https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report | 2025-10-06 | full |
| CHARLOTIN-DB-n/d | AI Hallucination Cases Database | D. Charlotin | community | https://www.damiencharlotin.com/hallucinations/ | n/d (live count of 2,202 at retrieval 2026-10-20) | full |
| ANTHROPIC-MULTIAGENT-2025 | How we built our multi-agent research system | Anthropic Engineering | vendor | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | full |
| ANTHROPIC-AGENTS-2024 | Building effective agents | Anthropic Engineering | vendor | https://www.anthropic.com/engineering/building-effective-agents | 2024-12-19 | full |
| ANTHROPIC-NOVO-n/d | Novo Nordisk accelerates clinical documentation and drug development with Claude (customer story) | Anthropic | vendor | https://claude.com/customers/novo-nordisk | n/d (page shows no date; accessed 2026-10-20) | full |
| OPENAI-MORGANSTANLEY-n/d | Morgan Stanley uses AI evals to shape the future of financial services (customer story) | OpenAI | vendor | https://openai.com/index/morgan-stanley/ | n/d (page shows no date; accessed 2026-10-20) | full (via text mirror) |
| GOOGLE-CODEREVIEW-2023 | Resolving code review comments with ML | Google Research (A. Frommgen, L. Kharatyan) | firm | https://research.google/blog/resolving-code-review-comments-with-ml/ | 2023-05-23 | full |
| SIEMENS-COPILOT-2025 | Siemens expands Industrial Copilot with New generative AI-powered Maintenance Offering (press release) | Siemens | vendor | https://press.siemens.com/global/en/pressrelease/siemens-expands-industrial-copilot-new-generative-ai-powered-maintenance-offering | 2025-03-24 | full |
| WALMART-2025 | Walmart Unveils New AI-Powered Tools To Empower 1.5 Million Associates | Walmart | firm | https://corporate.walmart.com/news/2025/06/24/walmart-unveils-new-ai-powered-tools-to-empower-1-5-million-associates | 2025-06-24 | full |
| HUSAIN-2024 | Your AI Product Needs Evals | Hamel Husain | community | https://hamel.dev/blog/posts/evals/ | 2024-03-29 | full |

Source count: 51 sources, 49 opened and read (`full`) and 2 `search-only` (ISO-42001-2023 and DTA-COPILOT-2024, neither used for any figure). By type: academic 14, regulator 14 (including government bodies), vendor 5, standard-setter 4, press 4, community 3, firm 3, professional-body 2 (the law-firm alert and the BBC/EBU study), survey 2. Five or more distinct source types are covered.
