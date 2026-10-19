# Verification report: professional-services / knowledge-management

Checked 2026-10-19 against the sources themselves, using the r.jina.ai mirror, direct fetch, pdftotext and PDF
metadata. One web search was used, for a McKinsey fallback. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/knowledge-management.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/knowledge-management.md`

All 116 distinct source URLs in the two files were attempted, and 115 were read. The one exception is
MCKINSEY-LILLI-2023 (see "Sources that could not be reached"). Every figure in a B entry was matched to the source
text. `scripts/validate.py` reports 0 errors.

## Counts

| Action | Entries |
|---|---|
| Kept | 1 (`-14`) |
| Fixed | 22 (all others) |
| Rejected | 0 |

Two grades changed: `-04` and `-15` both went from B to C. The synthesis flagged `-05` and `-19` for a grade check;
both stay at B, with reasons below.

## Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 0 | 0 |
| B | 14 | 12 (`-01`, `-02`, `-03`, `-05`, `-07`, `-11`, `-12`, `-13`, `-17`, `-18`, `-19`, `-22`) |
| C | 8 | 10 (`-04`, `-06`, `-08`, `-09`, `-10`, `-14`, `-15`, `-16`, `-20`, `-23`) |
| D | 1 | 1 (`-21`, labelled "Idea") |

## Grade checks requested by the synthesis

- **`-05` Clifford Chance: kept at B, maturity stays `announced`.** Two sources were read:
  - The Artificial Lawyer article says the firm "has launched" the Knowledge Bank. The platform "already contains"
    400,000+ documents that were reclassified and summarised.
  - The Law360 lead paragraph confirms an internal platform launch.

  The firm's Global Head of Knowledge & Training, a partner, is quoted, so this is a named deployment with no
  measures (B). No source shows lawyers using the platform, so maturity stays `announced`. The release does not say
  how far the reclassification was automated. "AI-assisted" was therefore removed from the title, and the problem
  statement is marked as an inference.
- **`-19` Ascend: kept at B on one basis only.** In the podcast, Ascend's CEO says chat features ("Why did the
  partner make that change?") are already inside the work product at Ascend's own firms. That is a named deploying
  organisation describing itself, with no measures. Three other parts of the entry cannot carry the grade:
  - The "closed loop" is described as a concept.
  - The story about interns reaching staff level is an anecdote.
  - The NBER trials are adjacent processes.

  The title now says unaided skill checks are "recommended", because no firm reports doing them. The trial wording
  is also corrected: the unaided skill advantage was "concentrated entirely" among seniors, not "most of" it.

## Fixes and rejections

Ids are shortened: `-04` means `professional-services-knowledge-management-04`.

| Id | Field | Change | Reason |
|---|---|---|---|
| `-04` | grade, notes, solution | B changed to C. Lilli's expert referral now cites OfficeChai (relaying Business Insider) | McKinsey's page could not be opened, so the B rested on an unconfirmable source plus a secondary relay. Arup People is a named deployment, but the case study claims no AI. Intapp, Litera and NetDocuments items are product claims (blocked source; grade inflated by an adjacent, non-AI process) |
| `-15` | grade, maturity, notes, problem, prerequisite | B changed to C and `in-production` to `announced`. The "decks and heads" quote is now credited to FOIL's Simon Goldsmith, a customer quoted in Kantata's release. The SOW and meeting-notes prerequisite now cites KANTATA-AGENT-2026 (added) | The named firms' KMWorld abstracts describe automated capture and tagging, but not AI-drafted retrospectives. That step exists only in vendor catalogues (grade inflated by an adjacent process). The quote was credited to the wrong speaker, and the claim to the wrong document |
| `-03` | problem, prerequisites, risks, checkpoints, role_evolution, notes, source | McKinsey-only claims are labelled "as read by the deep dive; not re-verified", and the source access is set to `search-only`. "Team grew from three to over 70" is replaced with Börsen-Zeitung's "four-person team, now more than 120 people". The 30% figure is now credited to TheOutpost.ai citing Entrepreneur, not "a Bloomberg interview". The Smaje quote is credited to the AFR via TheOutpost.ai | The source could not be opened. "Three to 70" conflicts with McKinsey's own podcast ("four of us") and with Börsen-Zeitung. The rest was a claim credited to the wrong document. B now rests on the Börsen-Zeitung interview with Erik Roth |
| `-12` | solution, risks, role_evolution, notes | The McKinsey data-steward claim is labelled not re-verified. Draftwise "describes gold-standard collections limited to firm-authored final documents" changed to Draftwise "recommends" filtering, plus curated "gold standard" collections. "Draftwise claims its platform" changed to Draftwise "argues advanced platforms". "KM lawyers become curators" changed to Draftwise "suggests" it | B now rests on Womble Bond Dickinson alone. The other changes fix embellished qualifiers: a vendor recommendation was presented as reported practice |
| `-01` | outcomes, risks, checkpoints, role_evolution, notes | "Knowledge session" changed to "session". The "LLMs aren't search engines" line is credited to Draftwise and Oz Benamram. "Curates, classifies and retires" changed to "assigned owners curate and tag". "Allens' team spends more effort on…" changed to what the team does. An unsourced "regulatory body, 15,000 precedents" note was removed | Embellished qualifiers and an unsourced connective claim |
| `-02` | problem, solution, outcomes, notes | "Returns marked citations" removed. Bicalho Navarro is now described as evaluating the assistant with a select group, not using it. "Staff open files one by one" changed to the partner's own words. "Deployed to everyone" changed to "within a two-month window without staging" | No source says the assistant returns marked citations. Bicalho's evaluation was overstated as use. The other two were embellishments |
| `-05` | title, problem, solution, Law360 source, notes | "Announced" changed to "launched". The problem is marked as an inference. Law360 access set to `full` (lead paragraph) | See the grade check above |
| `-06` | problem, prerequisites, role_evolution | The problem now cites NetDocuments (version notes) and iManage (OCR). "Permissions preserved on derived summaries" changed to "SmartSearch results". The KMWorld session is described accurately | The claims had no source. The other two overstated what the sources say |
| `-07` | problem, role_evolution | "Inboxes, desktops… file servers" changed to the bank's own description. "Librarians move from finding duplicates by hand to…" changed to what the story says | Embellished qualifiers, and a role change with no source |
| `-08` | solution, role_evolution, source date | "iManage Context Fabric GA in October" changed to "next-generation platform built around a context fabric (October GA announced at ILTACON)". Accenture's "firms" changed to "companies". CMR date changed from `2026-03-16` to `2026-03` | ILTACON reported GA for the platform, not for a "Context Fabric" product. Accenture's point is cross-industry. The PDF was created 2026-03-13 and nothing supports 03-16 |
| `-09` | problem, solution, notes, sources | The problem's claims now cite iManage MCP and DeepJudge. NetDocuments MCP "in private preview" changed to MCP via ndConnect with named partners (LAWSITES-ILTACON3-2026 added). The quoted "announced plans to connect" changed to Legora's actual "will be able to". "Sits outside the firm record" removed from the Heppner point | Claims credited to the wrong document, an outdated status, an invented quotation, and an embellished qualifier |
| `-10` | role_evolution | "Harvey names knowledge teams as authors" changed to "can define the structure" | Embellished qualifier: Harvey says knowledge teams can define templates |
| `-11` | risks | "Governing law" changed to "governing rules" | Harvey's wording |
| `-13` | problem, solution, risks, role_evolution, notes | "Legal operations selects and governs the tools" removed. The GSK remark is quoted as said. "AI line items" removed, and the client contradiction is credited to DLA Piper's Barclay Blair. TRI "describes legal ops as its own practice area" changed to "legal ops leaders say". The declined AI module is now identified as a competitor's, in an iManage story | Unsourced claims, a claim credited to the wrong speaker, and a missing qualifier |
| `-16` | risks, locator, notes | Opinion date "2026-08-05" changed to "press release 2026-08-17". The Heppner-to-transcripts link is marked as an inference | The opinion page did not open, so its date is unconfirmed. The other change fixes an embellished qualifier |
| `-17` | solution, outcomes | "Assistant summarises the matter" changed to what Chaffetz says it does. The Basware 4-5 hours figure is credited to the Kantata release, not the executive | Embellished qualifier, and a claim credited to the wrong speaker |
| `-18` | solution, role_evolution | "Firms pair this with policy, approved tools…" changed to California's actual guidance. "Knowledge lawyers as Harvey leads" changed to "knowledge lawyers front and centre; a Harvey Lead in each team" | The guidance and Lewis Silkin's wording were overstated |
| `-19` | title, problem, risks, checkpoints, role_evolution, notes | See the grade check above. The "firm-trained assistant" risk is now credited to High Rock Accounting's CEO | Claim credited without its speaker, and the NBER finding was misstated |
| `-20` | solution, role_evolution | DiDomenico's AI persona is now described as what a knowledge manager "can now" do, not a reported case | Embellished: the article describes a possibility |
| `-21` | problem, role_evolution | "Audit-business manager" changed to "general manager of TR's audit workflow business". The automaker's agents are described accurately | Wrong speaker title, and an embellished qualifier |
| `-22` | solution, risks | STAAR "trained on its AI-risk work" changed to "gives access to anonymised client documents and quotes approved text rather than synthesising". The California risk is restated, and its application to a client portal is marked as not addressed | Statements the source contradicts or does not make |
| `-23` | role_evolution | EDRM "at least 14 sessions" changed to "12 sessions under Validation and Measurement" | Wrong figure: the preview lists 12 |
| Many | source dates and keys | The iManage customer-story pages are undated, so dates now come from their downloadable PDFs: Allens 2025-09, EMEA firm 2025-06, legal operations customer 2025-04, Rio Tinto 2025-06, Chaffetz 2026-07, Digital Commerce Bank 2026-07, Seyfarth 2026-08, Womble 2026-08. Four keys were renamed to match the year: IMANAGE-ALLENS-2025, -EMEAFIRM-2025, -LEGALOPS-2025, -RIOTINTO-2025. ILTA changed from `2026-06` to `2026` (the PDF is undated and was created 2026-08-14). AT-AINATIVE changed from `2026` to `2026-10-19` (page `datePublished`) | Wrong or missing dates: read dates were used as publication dates |
| Module | header, §2, §3 | Grade counts updated. The table no longer rests the "two weeks" figure on the blocked McKinsey page; it now uses NetDocuments and Basware. The "inboxes" wording is fixed. The `#04`, `#05`, `#15` and `#19` descriptions now match the YAML | These follow the YAML fixes |
| Module | §5 | The McKinsey relay is credited correctly, and the OfficeChai 70%/45,000 discrepancy is noted. Womble is described as "users connected to the platform". The APQC 40% figure is restated. The AALL "in 2025" was dropped | Claims credited to the wrong document, and figures reported as something they don't measure |
| Module | §6 | ABA 512 is now cited from the opinion itself (p. 6), read via the LawNext copy, not from "secondary summaries". The Charlotin count is restated as "cases of hallucinated content… some alleged". The EU AI Act scope for expertise finders is marked as an inference | Overstated scope; the AI Act sentence was an unsourced connective claim |
| Module | §7 | Allens, the McKinsey data stewards, Lewis Silkin, Vault and TRI-LDOR claims were fixed in the same way as the YAML. Vault's Engstrom quote is now credited to Axios | Embellished qualifiers, and claims credited to the wrong speaker or document |
| Module | §8, §9 | "SKILLS founder" changed to "Oz Benamram (SKILLS)". The TRI premortem is marked as two fictional scenarios. "Clifford Chance announces" changed to "launches". The unverified "ILTACON 2026-08-23 to 27" changed to the 2026-09-04 article date. The "It costs too much" objection is now identified as a competitor's module in an iManage story | Wrong title, a missing qualifier, and an unverified date |

## Sources that could not be reached

- **MCKINSEY-LILLI-2023.** The mckinsey.com alumni page returned only a tracker frame through the mirror. Direct
  curl failed, and web.archive.org was blocked.
  - What was confirmed instead: one web search snippet confirms "more than 40 carefully curated knowledge sources"
    and experts in 70 countries. OfficeChai, which relays Business Insider, confirms five to seven content pieces,
    expert referral and the two modes.
  - What remains unconfirmed: the two-week kickoff, hundreds of data stewards and the legal and cyber challenge.
    These claims are labelled "not re-verified", and no grade rests on them.
- **NYC Bar Formal Opinion 2026-2.** The opinion page itself did not open through the mirror. The press release was
  read and supports every claim except the opinion's own date.
- **ABA Formal Opinion 512.** americanbar.org blocks downloads, so it was read in full from the LawNext copy.
- **Arxiv (STANFORD-MAGESH-2024).** Blocked by the mirror, but readable by direct fetch.
- **Dates confirmed only to the year or a read date:**
  - iManage Bicalho Navarro story (no PDF version)
  - iManage, NetDocuments, Intapp and Kantata product pages
  - Ikaun Arup case study (`2026`)
  - TR Future of Professionals (`2026`)
  - Law Society "Generative AI: the essentials" (`2026`)
  - Certinia (`2026-10`)
  - California guidance: the PDF is undated, and its metadata is consistent with the 2026-05-14 approval

## Module targets

| Target | Result |
|---|---|
| 15-25 use cases | 23: met |
| At least 50% graded A or B | 12 of 23 (52%): met, narrowly |
| Every source dated | Yes. Some dates are year-only or read dates, as listed above |
| Ids unique; vocabulary values; quotations under 25 words | Yes. Every cross-reference to work-production, scoping-pricing, tax, assurance and security ids names an existing entry |
| Validator | 0 errors |

## Cross-module issues for the coordinator

- **ILTA-TECHSURVEY-2026** still carries `2026-06` in 10 entries elsewhere. This file uses `2026`, as
  work-production's verification recommended.
- **IMANAGE-CHAFFETZ-2026** (also in acceptance-risk) is now dated `2026-07`, from its PDF. **AT-AINATIVE-2026** is now
  `2026-10-19`, from the page's `datePublished`. Other files may use `2026`.
- **Renamed keys** used only in this module: IMANAGE-ALLENS-2025, IMANAGE-EMEAFIRM-2025, IMANAGE-LEGALOPS-2025,
  IMANAGE-RIOTINTO-2025. The deep-dive files still use the -2026 forms.
- **IMANAGE-LEGALOPS** is an iManage story about leaving NetDocuments. Any module that cites "declined an expensive AI
  module" should say that the module was a competitor's.

## Error patterns to fix in the briefs

1. **Blocked primary sources carried as `access: full`.** McKinsey's page was recorded as read, but it cannot be
   re-opened. One figure ("three to over 70") conflicts with McKinsey's own podcast. Ask deep dives to save a copy or
   an exact quote for each blocked-prone domain, so the verifier can re-check it.
2. **A grade inflated by evidence from an adjacent process.** `-04` relied on a non-AI CV platform. `-15` relied on
   automated capture standing in for AI-drafted retrospectives. Add a rule: the named deployment must show the AI step
   named in the title.
3. **A claim credited to the wrong speaker or document:**
   - A customer's quote was credited to Kantata.
   - Release text was credited to an executive.
   - TRI's own framing was credited to legal ops leaders.
   - Relays were credited to Bloomberg instead of Entrepreneur or the AFR.
   - Vault was quoting Axios.
   - A competitor's AI module was not identified.
4. **Embellished qualifiers:**
   - "Returns marked citations"
   - "Trained on its AI-risk work"
   - "Knowledge lawyers are Harvey leads"
   - "Spends more effort on…"
   - "Retires content"
   - "Assistant summarises the matter"
   - Vendor recommendations (Draftwise, DiDomenico) presented as reported practice
5. **Unsourced connective claims** in `problem`, `role_evolution` and `risks_and_guardrails` (`-01`, `-05`, `-06`,
   `-07`, `-13`, `-15`, `-22`). Ask briefs to require a source ref on every such sentence, or to label it
   "(inference)".
6. **Wrong or missing dates.** Vendor pages often carry no date, and read dates were used as publication dates. Ask
   readers to check for a downloadable PDF and its metadata first. Seven of the nine iManage stories had one.
7. **A statistic reported as something it doesn't measure:**
   - The APQC 40% (respondents citing a threat) was presented as "rank as top threat".
   - Womble's 1,250 platform users were presented as "Insight+ users".
   - "At least 14" sessions where the preview lists 12.
8. **Search-only figures in A or B entries.** None remain. The one search-only source, McKinsey, now supports no grade.
