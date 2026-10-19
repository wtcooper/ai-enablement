# Quality review (professional services)

Sources checked 2026-10-19. Use cases live in `../use-cases/quality-review.yaml` (18 entries: A 0, B 11, C 6,
D 1). Ids are shortened here: `#08` means `professional-services-quality-review-08`; other modules' and archetypes'
ids are in full. Source keys in brackets are in the YAML or in §10. The public record is mostly legal (law firms,
courts, bars, in-house legal teams). Accounting and consulting evidence is mostly incidents and trade-press
interviews. No firm or in-house team publishes a reviewer catch rate, an override rate, a parallel-run result
(AI-assisted and conventional review compared on the same work) or an inspection finding for AI-assisted
deliverables. Say so when you quote a figure.

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

How a firm or in-house team checks work before it reaches a client, court or regulator, now that AI drafts much
of it: verification of citations, quotations and figures; supervisory review and sign-off; the firm's quality
system (policy, tool testing, monitoring); disclosure to clients; and what happens after an error is found. The
production of the work itself is in work-production. Audit engagement quality review, tax technical review and
security operations live in the assurance, tax and security archetypes; overlaps are named by id.

A **hallucination** here means AI output that invents a source or misstates what a real source says.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Drafter's own check | The person who used AI checks facts and sources before passing work on | review-assurance | AI states errors in the same assured tone as correct answers [TRI-NEED2KNOW-2026] |
| Citation and reference check | Every authority, quote and figure is matched to its source | review-assurance | Errors are subtle; Sullivan & Cromwell's ordinary cite-check missed invented authority [CANLAWYER-SC-2026] |
| Supervisory review and sign-off | Senior, manager or partner reviews; the signer takes responsibility | review-assurance, expert-judgment | Each reviewer assumes someone else validated; review becomes a rubber stamp [ACCOUNTINGTODAY-HALLUC1-2026; ACCOUNTINGTODAY-HALLUC2-2026] |
| Record of the check | What was checked, by whom, which parts were AI-generated | data-reporting | Partners sanctioned for errors they did not make, with no record [LAWSITES-CLEARBRIEF-2025] |
| Client communication | Disclosure of AI use; answering client AI terms | client-interaction | 73% say clients deserve full visibility; 21% deliver it [MORAE-ILR-2026] |
| Checking incoming work | Opponents' filings, contractors' and juniors' drafts | review-assurance | Errors are found by outsiders, not the firm [CANLAWYER-SC-2026; CTV-DELOITTE-2025] |
| Incident response | Correct, disclose, re-review the wider set | review-assurance, client-interaction | Quiet corrections and concealment draw harsher responses [WHITECASE-VERIFY-2026] |
| Quality system | Policy, training, tool testing, monitoring of AI's effect on quality | coordination-scheduling, data-reporting | 71% have policies, 30% are confident they are applied [MORAE-ILR-2026]; the six largest UK audit firms did not formally monitor tools' quality impact [FRC-ATT-2025] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`). **Coverage:** assist 7, augment 9,
automate 1, delegate 1; step 10, process 8, model 0. The automate entry (`#13`) and the delegate entry (`#09`) are
ideas and announcements (grade C). **No evidence was found for a model-scope change in this module** (for example a
firm selling review as a service); do not invent one.

**Verifying citations, references and figures**
- Improve: `#02` automated cite, quote and proposition checkers before signing (Filevine, BriefCatch, LawDroid,
  Thomson Reuters; Harvey announced). Vendor launches for law firms; no named customer, no false-negative rate.
  Related: work-production-11 (pre-release check, B), tax-research-advisory-20, assurance-quality-management-19.
- Improve: `#03` a verification record on the file showing who checked what and which material was AI-generated
  (Clearbrief product; ABA, Law Society and ICMCI guidance). Related: work-production-25.
- Improve: `#04` pre-issue audit of every reference in consulting and advisory reports, prompted by Big Four
  incidents (Deloitte Australia and Canada, EY, KPMG, PwC Middle East). An idea plus a vendor tool (GPTZero).
- Automate: `#13` a second agent or a deterministic comparison engine checks AI output before a person sees the
  flags (community suggestions; Harvey, Litera, Clearbrief claims). Contested.

**Review and sign-off**
- Improve, process scope: `#08` review gates where a named reviewer signs off each AI step before the next begins
  (Armanino, US accounting firm, in production; Harvey announced). Agent-template version: work-production-15.
- Improve, process scope: `#10` an AI layer on the firm's quality management system: AI discussed at planning,
  reviewers back-trace claims to source, depth rises with consequence (Forvis Mazars, Schellman; accounting and
  advisory). Audit detail: assurance-quality-management-07, -17, -19.
- Delegate: `#09` oversight tiered by agent autonomy, with escalation triggers and no filing, advice or outside
  transmission without approval (CLOC conference framing; California guidance). Related: work-production-16.

**Testing tools and setting review depth**
- Improve: `#05` benchmark tools against expert answers and set review depth task by task (Linklaters' own
  English-law benchmark; Vals with a law-firm consortium; Hogan Lovells Cadwalader's 1,300-lawyer pilot). Related:
  work-production-23, work-production-07.
- Improve, process scope: `#06` validate AI document review inside a matter with test sets, and sample output
  instead of re-reading all of it (Covington & Burling case study; Law Society research on sampling).
- Improve, process scope: `#07` standing evaluation suites and change control run by legal engineers (Latham &
  Watkins job description; Legora and Harvey evaluator roles). Related: work-production-17.
- Improve: `#11` track acceptance, overrides and review findings as a quality signal (Microsoft's in-house legal
  team: about seven in ten suggestions kept). Related: work-production-08, work-production-24.
- Improve: `#12` idea: standard quick-check techniques to cut the "verification tax" (CLOC; in-house).

**Policy, clients, incidents and insurance**
- Improve, process scope: `#01` turn the AI policy into an enforced review rule with attestation (law firms; Butler
  Snow and Sullivan & Cromwell show policy alone failing). Rollout gate: work-production-22, talent-learning-01.
- Improve: `#15` check incoming work: opponents' filings, contractors' and juniors' drafts (US, UK and Canadian
  courts). Junior disclosure loop: talent-learning-10.
- Improve, process scope: `#14` after an error: disclose, correct, re-review the whole matter (Sullivan & Cromwell,
  Butler Snow, Deloitte Australia). Fee recovery: scoping-pricing-12.
- Improve: `#16` tell clients when AI materially contributed and how it was checked (Forvis Mazars, Deloitte
  Australia, ICMCI). Client terms at intake: acceptance-risk-10, -11.
- Improve, process scope: `#17` in-house teams set bounded, reviewable workflows and ask firms for evidence
  (Starbucks, GSK; in-house). Related: scoping-pricing-09, -11.
- Improve: `#18` documented AI governance for professional indemnity insurers (law and CPA firms).

**Juniors as reviewers** are covered in talent-learning: verification-first onboarding (talent-learning-02, -09),
pre-review feedback tools (talent-learning-06) and the patent-drafting trial (talent-learning-11).

## 4. Interview probes

1. **"Take the last AI-assisted deliverable or filing that left your team. Who checked which claims, against which
   source, and where is that recorded?"** Reveals whether review is a real step or a habit (`#01`, `#03`).
2. **"When a partner or engagement leader signs, what do they know about where AI was used?"** Reveals the
   signer's blind spot that led to sanctions for errors partners did not make (`#03`).
3. **"What does your reviewer checklist ask differently when AI contributed, and how would you know a reviewer
   back-traced a claim rather than skimmed it?"** Reveals rubber-stamp risk (`#08`, `#10`).
4. **"Which deliverables are top tier, where one fabricated fact would cost the client? Do they get a second
   reader?"** Reveals whether review depth follows risk (`#04`, `#05`).
5. **"Before you relied on a tool, did you test it on known answers from your own work? When did you last
   re-test?"** Reveals `#05`-`#07`; ABA 512 allows sample-testing and California expects reassessment.
6. **"Do you measure anything about review: suggestions kept or rejected, errors caught at review, errors found
   after release or by outsiders, time spent checking?"** Reveals whether any quality evidence exists (`#11`, `#12`).
7. **"How do you check work that arrives from contractors, other firms or the other side?"** Reveals exposure that
   courts have placed on the signer (`#15`).
8. **"If a client or opposing counsel found a fabricated reference tomorrow, who owns the response, and would you
   re-review the whole engagement?"** Reveals incident readiness (`#14`).
9. **"What do you tell clients about AI use and how it was checked, and what have clients asked for?"** Reveals the
   disclosure gap and client pressure (`#16`, `#17`).
10. **"Do any agents act without a person at each step? What can they send outside the firm?"** Reveals readiness
    for `#09` and confidentiality exposure.
11. **"Consulting and accounting: who checks every reference in reports and thought leadership before
    publication?"** Reveals exposure to a Big Four-type incident (`#04`).
12. **"Have your insurer's proposal or renewal forms asked about AI? Who answers?"** Reveals `#18`.

## 5. Metrics and benchmarks

**What to measure:** flags raised by a checker and how each was resolved; share of AI suggestions kept, edited or
rejected; errors caught at review versus after release versus by outsiders; time spent checking against drafting
time saved; precision and recall (share of flagged items that are right, share of right items found) on a test set
before relying on a tool; attestations completed against policy. None of these is published by a named firm.

**Tool accuracy (tools tested in isolation)**
- Stanford 2024: three commercial legal research tools hallucinated 17% to 33% of the time; versions since
  replaced [STANFORD-MAGESH-2024; LLRX-FARRIS-2026].
- Luxembourg 2026: eight legal retrieval systems, under 10% to nearly half of responses with hallucinations
  [ARXIV-LUX-2026].
- Vals 2025: tools beat lawyers on document Q&A (94.8% vs 70.1%), lawyers led on redlining (79.7% vs 65.0%) and
  EDGAR research [VALS-VLAIR-2025]; legal research 74-78% vs 69%, multi-jurisdiction questions 14 points lower
  [VALS-VLAIRRES-2025].
- Linklaters' own benchmark: best model 6.4 out of 10 (2025), up from 4.4 (2023); self-reported [LINKLATERS-LINKSAI-2025].
- BCG experiment: on a task outside AI's capability, consultants with AI were 19% less likely to be correct
  [HBS-DELLACQUA-2023].

**Checkers and review signals (vendor-published or self-reported)**
- Filevine checker on 2,073 citations in filings already flagged by courts: 61.8% verified, 38.2% flagged, 8.4%
  severe; not an error rate for ordinary work [LAWSITES-FILEVINE-2026].
- GPTZero claims its checker catches 99 of 100 flawed citations; method not shown [GPTZERO-KPMG-2026].
- Microsoft Legal Agent: about seven in ten suggestions kept, about 100,000 edits by 1,800+ users [LAWSITES-MSFT-2026].
- Look-backs: Butler Snow, 2,400+ citations in 330 filings, no further problems [EDRM-JOHNSONDUNN-2025].

**Scale of failure**
- 2,202 court decisions on hallucinated content (1,501 US; 872 with a lawyer as the party), read 2026-10-19; a
  count of decisions, not a rate; other trackers count differently [CHARLOTIN-DB-2026].
- Ayinde: 18 of 45 cited cases did not exist [EWHC-AYINDE-2025]. Noland: 21 of 23 quotations fabricated
  [LAWSITES-NOLAND-2025]. KPMG report: 5 of 45 citations accurate, per GPTZero [GPTZERO-KPMG-2026].

**Policy and burden (surveys)**
- ILTA (508 law firms): human review required 31% (under 50 lawyers) to 83% (350-699); independent verification
  25% to 60%; training before use 11% to 72%; client approval 8% to 38%; tracking tools at fewer than one in five
  firms [ILTA-TECHSURVEY-2026].
- Morae (850 senior legal professionals, vendor): 71% policy, 30% confident it is applied; 67% fear checking costs
  outweigh benefits; 48% materially fix outputs [MORAE-ILR-2026]. 85% of law firms enforce AI policy by manual
  checks [LAW360-GA-2026]. 89% of professional-services leaders spend significant time verifying AI output
  (vendor-sponsored) [KANTATA-SOPSI-2026].
- Clients: 78% of corporate clients rate AI quality gains very important or essential; 6% say most or all providers
  deliver them [TR-FOP-2026].

## 6. Guardrails

- **ABA Formal Opinion 512 (2024-07-29):** verification depth depends on tool and task; testing a tool on a subset
  before relying more on it is acceptable; managers set policy and train; the lawyer is fully responsible
  whatever review is chosen [ABA-OP512-2024].
- **State Bar of California (approved 2026-05-14):** supervision and verification rise with autonomy; agents must
  not make substantive legal determinations, give advice, file or send client information outside without
  meaningful review; reassess tools as they change; supervisors set policy and train [CALBAR-GENAI-2026; CALBAR-ETHICS-2026].
- **Florida:** from 2026-06-15 the signer of any filing represents that cited authorities exist and are accurately
  cited, with sanctions available [LAWSITES-FLRULE-2026].
- **England and Wales:** the Divisional Court expects checks against authoritative sources and may ask what leaders
  did [EWHC-AYINDE-2025]; a County Court referred two solicitors to the SRA, the solicitors' regulator
  [CCDUDLEY-RODNEY-2026]; the SRA issued a warning notice after 42 reports of possible AI misuse in a year
  (secondary report) [LAWSOCIE-SRAWARN-2026]; the Law Society says generative AI cannot audit its own accuracy
  [LAWSOC-GENAI-2026].
- **Management consulting:** the ICMCI code (May 2026) treats unreviewed AI output submitted as finished work as
  misuse and requires verification of facts, calculations and references [ICMCI-AICODE-2026].
- **Accounting:** ISQM 1 and SQMS 1 (the international and US standards for firm-level quality management) frame
  AI tools as firm resources [ACCOUNTINGWEEKLY-B4-2026]; the FRC encourages metrics on tools' quality impact
  [FRC-ATT-2025]; CPA Newfoundland and Labrador opened an investigation of Deloitte over a consulting report
  [INDEPENDENT-CPANL-2026]. Detail: assurance archetype.
- **Standards:** NIST names confabulation (fabricated output) as a generative AI risk [NIST-AI600-2024].
- **Insurers** are starting to ask how AI-enabled work is supervised; cover is uncertain where work was largely
  AI-produced and weakly supervised [DACB-PI-2026; ACCOUNTINGTODAY-INSURERS-2026].

**Steps that stay with a person:** confirming each authority exists and supports the point; signing filings,
advice and reports; deciding review depth for a task; resolving checker flags; approving anything an agent sends
outside; deciding what to tell a client or court; owning the response to an error.

## 7. Roles and how they evolve

- **Signers and supervisors.** Managing and supervising lawyers carry explicit duties to set policy, train and keep
  controls current [CALBAR-GENAI-2026]; courts may ask leaders what they did [EWHC-AYINDE-2025]. Forvis Mazars says
  professionals must defend AI-assisted work as if they drafted it unaided [ACCOUNTINGTODAY-HALLUC2-2026].
- **Reviewers.** An AICPA leader says the profession moves from doing to supervising, which needs understanding of
  the procedure [JOA-TRAINING-2026]. Practitioners ask whether reviewers are independent and qualified
  [ACCOUNTINGTODAY-HALLUC2-2026].
- **New evaluation roles.** Latham & Watkins' Legal Engineering Attorney builds evaluation suites and places review
  gates [LATHAM-JD-2026]; vendors hire lawyer-evaluators [LEGORA-JOB-EVALS-2026; HARVEY-JOB-EVALQ-2026].
- **Juniors.** In a trial of 133 patent lawyers, AI raised quality but the unaided skill gain went to seniors and
  juniors' results split [NBER-AUTOR-2026]. 48% of professionals worry about AI's effect on judgment development;
  legal professionals expect the path to trusted judgment to lengthen by nearly two years [TR-FOP-2026]. Detail:
  talent-learning.
- **In-house teams** set rules for suppliers and ask firms how AI was used on their matters [EDT-CASEPOINT-2026;
  TRI-LEGALWEEK-2026].

## 8. Frontier

- **2026-10-19** Harvey says US case-law cite checking will launch in coming months; Midpage connector lists citation review [HARVEY-GRAPH-2026; LAWSITES-MIDPAGE-2026].
- **2026-10-15** Harvey Legal Work Orchestration with a reviewer per task; Harvey forecasts agents taking 20% more workflow steps in six months [HARVEY-ORCH-2026]. Microsoft Copilot for Legal [LAWSITES-MSFT-2026].
- **2026-11 (scheduled)** Thomson Reuters Institute webinar on accountability "beyond human in the loop" [TRI-EVENTS-2026]. Signal only.
- **2026-09-11** BriefCatch RealityCheck citation checking with a hidden-text scan [LAWSITES-BRIEFCATCH-2026]. **2026-09-02** Filevine brief auditor [LAWSITES-FILEVINE-2026].
- **2026-08** SRA warning notice on AI misuse [LAWSOCIE-SRAWARN-2026]. **2026-08-14** Luxembourg study of legal retrieval systems [ARXIV-LUX-2026].
- **2026-07-30** A researcher argues courts substitute process for error-rate evidence [ARXIV-WILLIAMS-2026].
- **2026-05-19 to 07-30** GPTZero investigations of EY, KPMG and PwC Middle East reports; withdrawals follow [ACS-EY-2026; TECHCRUNCH-KPMG-2026; GPTZERO-PWC-2026].
- **2026-06-22** Thomson Reuters rebuilds CoCounsel Legal around traceable citations ("fiduciary-grade") [LAWSITES-COCOUNSEL-2026].
- **2026-05** California guidance covers agentic AI; Florida citation rule adopted (in force 2026-06-15); ICMCI code [CALBAR-GENAI-2026; LAWSITES-FLRULE-2026; ICMCI-AICODE-2026].
- **2026-04** Sullivan & Cromwell apologises to a bankruptcy court (letter 2026-04-18); County Court refers solicitors to the SRA (2026-04-23); Law Society reports a move toward statistical sampling (2026-04-14) [CANLAWYER-SC-2026; CCDUDLEY-RODNEY-2026; LAWSOC-AGENTIC-2026].
- **2026-03-07** Accountancy regulator to investigate Deloitte over a consulting report [INDEPENDENT-CPANL-2026].

## 9. Common objections

- **"We have a policy, so we're covered."** Butler Snow and Sullivan & Cromwell had policies when errors reached
  courts [EDRM-JOHNSONDUNN-2025; CANLAWYER-SC-2026]; 30% of Morae respondents are confident policies are applied
  [MORAE-ILR-2026]. Answer: enforcement, attestation and a record of the check (`#01`, `#03`).
- **"Checking AI costs more than it saves."** Many fear it (67%) and most spend significant time verifying
  [MORAE-ILR-2026; KANTATA-SOPSI-2026], but no one has measured it. Answer: measure review time and findings
  (`#11`), set depth by task (`#05`), sample where volume is high (`#06`).
- **"Our tool is grounded, so it doesn't hallucinate."** Retrieval-based tools still hallucinated 17-33% in 2024
  and up to nearly half in a 2026 study [STANFORD-MAGESH-2024; ARXIV-LUX-2026]. Answer: test on known answers
  (`#05`) and keep the citation check (`#02`).
- **"Let AI check the AI."** A Thomson Reuters Labs scientist says self-checking loops are still prediction and
  guarantee nothing [TRI-NEED2KNOW-2026]. Answer: a machine pre-filter at most, with people on every flag (`#13`).
- **"Our reviewers will catch it."** In the consulting incidents read, outsiders found the errors
  [CTV-DELOITTE-2025; GPTZERO-KPMG-2026]; reviewers are short of time and trust colleagues
  [ACCOUNTINGTODAY-HALLUC1-2026]. Answer: gates with a named, independent reviewer and back-tracing (`#08`, `#10`).
- **"This is a litigation problem, not ours."** Deloitte, EY, KPMG and PwC reports were questioned, and an
  accountancy regulator opened an investigation [INDEPENDENT-CPANL-2026]. Answer: pre-issue reference audit (`#04`).
- **"Clients don't want to hear about AI."** Clients are asking, inconsistently: some demand AI, some bar it
  [TRI-LEGALWEEK-2026]; 78% want AI quality gains, 6% see them [TR-FOP-2026]. Answer: `#16`, `#17`.
- **"It's an expensive toy until accuracy improves."** An ILTA respondent's view [ILTA-TECHSURVEY-2026]. Answer:
  accuracy varies by task (`#05`); review depth can follow it.

## 10. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML:
- CALBAR-ETHICS-2026 is in the YAML (`#09`).
- LAWSITES-COCOUNSEL-2026: LawSites, Thomson Reuters Opens Early Access to the 'Next Generation' of CoCounsel Legal, 2026-06-22, https://www.lawnext.com/2026/06/thomson-reuters-opens-early-access-to-the-next-generation-of-cocounsel-legal-saying-beta-users-fing-loved-the-product.html
- LAWSITES-FLRULE-2026: LawSites, Florida Supreme Court Tackles AI Hallucinations with New Rule Applicable to All State Courts, 2026-05-28, https://www.lawnext.com/2026/05/florida-supreme-court-tackles-ai-hallucinations-with-new-rule.html
- LAWSOCIE-SRAWARN-2026: Law Society of Ireland Gazette, SRA issues warning notice on use of AI (secondary report; SRA page blocked), 2026-08, https://www.lawsociety.ie/gazette/top-stories/2026/august/sra-issues-warning-notice-on-use-of-ai/
- NBER-AUTOR-2026: NBER Working Paper 35720, Does AI Assistance Enhance or Erode Expertise? (abstract read; conducted by Google), 2026-09, https://www.nber.org/papers/w35720
- NIST-AI600-2024: NIST, AI RMF Generative AI Profile (NIST AI 600-1), section 2.2, 2024-07, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- TRI-EVENTS-2026: Thomson Reuters Institute, events listing (Trust by Verify; Beyond Human in the Loop, scheduled), 2026-10, https://www.thomsonreuters.com/en/institute/events
- TRI-NEED2KNOW-2026 and GPTZERO-PWC-2026: TRI-NEED2KNOW-2026 is in the YAML (`#13`); GPTZERO-PWC-2026: GPTZero, Chasing the Hallucinations: PwC report hallucinates product and government customers, 2026-07-29, https://gptzero.me/news/investigations-pwc/
- TECHCRUNCH-KPMG-2026, ACS-EY-2026, ARXIV-WILLIAMS-2026, CCDUDLEY-RODNEY-2026 and LAWSOC-AGENTIC-2026 are in the YAML (`#14`, `#11`, `#15`, `#06`).
