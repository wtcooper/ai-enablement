# Verification report: ai-governance skill

Date: 2026-10-20 · Brief: `research/runs/suite/briefs/verify-ai-governance.md` · Files checked: every file in
`plugins/ai-transformation/skills/ai-governance/` · Validator after edits: 0 errors; no warnings in this skill (the
run's 25 warnings are archetype use-case grade mixes elsewhere).

## Summary

| | Count |
|---|---|
| Cited statements checked (figures, attributions, regulatory points, dates, named examples) | about 150 |
| Distinct sources opened (direct or through the r.jina.ai mirror) | 50 of 52 cited |
| Kept as written | about 112 |
| Fixed (wording, figure scope, locator, citation, date or label) | 38 |
| Claims removed | 0 |
| Source entries removed (superseded by the primary text or no longer cited) | 4 (Ezel summary ×2, LawSites summary, IESBA in baseline) |

All survey figures now name who ran the survey and its population. No figure was wrong in value; the errors were
scope, attribution and misread locators. The skill cites no archetype use cases, so no evidence grades apply.

## Fixes and removals

| # | File(s) | Was | Now | Reason (error pattern) |
|---|---|---|---|---|
| 1 | baseline §1; professional-duties §1 | "The profession-specific texts all say existing duties continue" citing JOFA, IESBA, ABA, PCAOB | AICPA article and ABA 512 say so; firms told PCAOB staff the same; IESBA dropped | IESBA landing page does not say this; PCAOB reports what firms said (unsourced connective claim, attribution drift) |
| 2 | baseline move 1 | KPMG 48% "uploaded company information"; MSFT 78% with no population | Adds 48,340 people, 47 countries, "sensitive" company information; MSFT survey of 31,000 knowledge workers in 31 markets, fielded by Edelman | Survey population missing; source says "sensitive company information" |
| 3 | baseline move 2; policy-and-data §6; risk-tiers §6 | KPMG 67%/33%, 66%/56%, "two in five" with key only | Names the University of Melbourne and KPMG employee survey and population | Survey population and runner missing |
| 4 | baseline move 5 | IAPP: AI questions "commonly added"; 22% "of respondents" | Qualified to organizations building governance from privacy programs; spring-2024 survey of 670+ people in 45 countries | Embellished qualifier; population missing |
| 5 | baseline §5; risk-tiers §5 | Annex III lists "hiring, work allocation or evaluation of staff" | Recruitment, decisions on terms of work, task allocation based on behaviour or personal traits, monitoring or evaluating staff; tier-4 labelled advisor default | Annex III point 4(b) covers only task allocation based on behaviour or traits (embellished) |
| 6 | all step files | CPAI-ND, "undated" | CPAI-2026, 2026-07 | Page reads "Published July 2026" (wrong date) |
| 7 | policy-and-data §1 and move 5 | "The main exposure is confidential client information entering a tool [CPAI]" | "A central exposure"; quotes what CPAi says ("vital", restrict confidential inputs); move 5 labelled advisor default | CPAi does not rank exposures (embellished, unsourced connective claim) |
| 8 | policy-and-data §5 | Approval-unit and approver rules cited to ANTHROPIC and EY as if sourced | Labelled advisor default, built on those sources and CPAi | Neither source states the rule (defaults shown as sourced) |
| 9 | risk-tiers §1 | "Firms told PCAOB staff" AI augments, member responsible, same diligence | "Firms investing in AI tools … and some said …" | Spotlight attributes these to firms investing and to "some firms" (attribution drift) |
| 10 | risk-tiers §2 step 5 | "Some firms allowed … but not for audit" | "Some firms allowed …, and some did not allow it for audit or attest procedures" | Two different groups of "some firms" merged |
| 11 | risk-tiers §6 | "Firms told PCAOB staff supervision policies had not changed" | "Some firms … supervision and review policies" | Source says "some firms" |
| 12 | risk-tiers §6 | "26% of agentic-AI users surveyed"; "Agents are tier-4 by default" | 202 senior AI executives at large US public companies, those using agentic AI; agents acting on client data or outside the firm are tier-4 | Population misstated; the old line contradicted the pattern map (service-agent tier-3) |
| 13 | risk-tiers move 2; professional-duties §5 | ABA 512 points "as summarised" [ABA-512-2024, Ezel] | Cited to the opinion itself [ABA-OP512-2024]; Ezel entries removed | Primary PDF reached: "regardless of the level of review … fully responsible" (p.4); consent not required for idea generation without client information |
| 14 | records §1 | FRC documentation detail cited to the news release | Adds FRC-AIAUDIT-2025 (the guidance PDF) | The release does not list what to document (attribution drift) |
| 15 | records move 3 | Third-party tools: "document why you can rely" [FRC-AI; KN] | Adds the FRC PDF and its note that firms may rely on independent assurance | Locator to the document that says it |
| 16 | records move 5 | OpenAI deletes within 30 days "unless legally required" | "… unless the law requires longer retention or it is needed to protect its services" | Second exception omitted |
| 17 | records §5 tier-4 row | Approval-record content [FRC-AI-2025] | [FRC-AIAUDIT-2025] | Wrong document |
| 18 | records §5 | "Records scale with the tier" [FRC-AI-2025] | Labelled advisor default, built on the FRC proportionality principle | Tier scaling is the skill's design |
| 19 | records §6; secure-enablement §5 | KPMG monitoring "not intended as discipline" | Adds that KPMG adds AI use to annual performance assessments; records never rate individuals (core rule 1) | Leaving that out made the example misleading |
| 20 | professional-duties move 2, §5, §6, §7 | "Whether an AI vendor counts as a preparer …; the panel abstract poses that question" | Whether the AI provider is only processing or making a substantive determination | The Winthrop abstract asks the processing-or-substantive-determination question (attribution drift) |
| 21 | professional-duties move 2; §7 | 301.7216-2(d)(1), Example 4 | Examples 1 and 4 | "Pure processing in the US needs no consent" is Example 1 |
| 22 | professional-duties move 4 | IESBA revisions "effective 15 December 2024" | Independence changes effective for audits and reviews of periods beginning on or after 15 December 2024 | Effective-date wording made precise |
| 23 | professional-duties move 7 | "SSNs cannot be disclosed offshore under consent" [-3(b)(4)] | Offshore disclosure needs prior consent [-3(a)(3)(i)(D)]; for Form 1040-series returns, SSN consent only with an adequate data-protection safeguard [-3(b)(4)] | Overstated: misses the 1040 scope and the safeguard exception; wrong locator |
| 24 | professional-duties §5 | "No IRS guidance … (tax guardrails §3)" | §3, §4 | That statement is in §4 |
| 25 | professional-duties §7 | "Summarising a return is processing" | A summary that only restates figures is treated as processing, confirmed with counsel | Contradicted the file's own trap ("assuming a summary is never a substantive determination") |
| 26 | vendor-evaluation move 4 | GV-6.1-008 = "records of third-party changes" | "Records of changes third parties make to content"; adds GV-6.1-009 (procurement due diligence covering embedded GAI and ongoing monitoring) | Misread: GV-6.1-008 concerns content provenance, not vendor changes |
| 27 | vendor-evaluation move 5, scorecard `change_control`; secure-enablement triggers | Change notice and re-approval triggers anchored on GV-6.1-008 | Anchored on GV-1.6-003, GV-6.1-005 (monitor third parties, detect unauthorized changes), GV-6.1-009 | Same misread |
| 28 | vendor-evaluation §1 | GV-6.1-004 to -008 | -004 to -009 | Range now matches the actions used |
| 29 | vendor-evaluation §5 | Embedded feature off until catalogued [GV-1.6-001, -002] | Labelled advisor default; NIST asks that inventories and procurement cover embedded GAI (GV-1.6-002, GV-6.1-009) | NIST does not say "switch off" |
| 30 | vendor-evaluation §6 | "The five data-flow facts decide most cases [NIST]" | Labelled advisor default; NIST's third-party actions centre on them | Synthesis shown as a sourced finding |
| 31 | secure-enablement move 6 | Chair hands AI to "respected senior people" | Asked talented senior business leaders, not technologists, to run the business side; "business problem rather than a tech problem" | "Respected" not in source (embellished) |
| 32 | secure-enablement move 7 | ABA 512 "as summarised" places supervision duties [LAWNEXT-2024] | Managerial lawyers must set clear policies on permissible AI use [ABA-OP512-2024]; LawSites entry removed | Primary reached |
| 33 | secure-enablement move 2, §6 | EY 47%/98% with partial population | 202 senior AI executives at US public companies with at least $1 billion revenue, EY-commissioned, self-reported | Population incomplete |
| 34 | secure-enablement §5 | Exceptions rule [EY] | Labelled advisor default, built on EY | EY does not state the rule |
| 35 | baseline §9 | IESBA-TECH-2023 entry | Removed | No longer cited in the file |
| 36 | baseline §9 | IAPP and MSFT-WTI entries | Survey dates and fieldwork firm added | Dates were not stated |
| 37 | vendor-evaluation §7 | Desk evaluation: decision `pending` but catalog `pilot` | Pending for client-confidential data; pilot for firm-internal data once the user confirms the admin switch | Contradicted the vendor schema rule |
| 38 | schemas/vendor.md, schemas/policy.md | Desk evaluation stays `pending` (all data); `decision` values undefined | Pending for client-confidential and regulated data until the contract is checked; `decision` values listed in §3.5 with the mapping to catalog `status` | Made the schemas consistent with the method and the example |

## Kept after checking (main items)

KPMG-MELB-2025 pp.6, 71, 75 (values and pages correct). EY-AIGOV-2026: 202 executives, 98%, 47%, 26%, fieldwork dates.
MSFT-WTI-2024: 78% and 80%. IAPP: 22% and 22%. NIST AI 600-1 GV-1.6-001 to -003 and GV-6.1-004, -006, -007. NIST AI RMF
GOVERN 1.3, 1.7 and 6.2. CSA AICM: 243 objectives in 18 domains. Anthropic: commercial default, feedback stored up to
5 years, owner can disable. OpenAI: no training by default, opt-in feedback. Microsoft: activity history, Purview
retention, non-EU customers' queries may be processed in the US, EU or other regions. 26 CFR 301.7216-3: written,
signed and dated, no retroactive consent, one-year default, separate documents, no conditioning except
preparer-to-preparer. PCAOB Spotlight pp.4-5. FRC release (proportionate, third-party tools, no new requirements)
and FRC PDF ("may well be appropriate to document less"). Mata v. Avianca: $5,000 jointly and severally. Guardian on
Deloitte: final instalment, incorrect references, AI not named as the cause. Regulation (EU) 2026/1744 of 8 July 2026:
Annex III high-risk from 2 December 2027, literacy softened. AI Act Art 26(6): six months. JOFA-2026 on independence.
ABA 512: self-learning consent, boilerplate not enough, actual time billed, managerial duties. OPR Alert 2026-19:
§10.36, enterprise-approved AI, vetting, no mention of consent. ABA Journal on Johnson v. Dunn: firm not sanctioned,
quote. Orrick on Heppner. Microsoft RAI Standard A1.3. SR 11-7: effective challenge and vendor models. OWASP LLM06
Excessive Agency. CPAi: five jobs, three file items, the quote. CIPD: training before use. VinciWorks: supervisors may
face consequences. Jotwell: "Leadership Constellation". Openlayer, Gend and Ampcus (vendor blogs, labelled directional).
Spot-checked archetype-shared sources: CalBar (autonomy quote, agents and email), NYC Bar (ethical screens), ICMCI
("materially contribute"), IFIAR (re-approval on model updates), PCRT ("likely" a breach), TPB (permission by
configuration), Law Society (supplier due diligence, limited warranties).

## Usability fixes (SKILL.md and schemas)

- Every step now has a one-line **Goal** before its "Read now" pointer, alongside the core questions, exit and output
  it already had.
- Step 5 has one "Read now" pointer. The three archetype paths moved into the step file's §5 table, which the
  reference map also reaches through the archetypes index.
- Start or resume: what to do when `next_step` is `null` (evaluate a tool, review against triggers and raise
  `policy_version`, or record approval only when the user says approvers signed off).
- `decision` values (including `pending`) are defined in `schemas/policy.md` §3.5, with how they map to catalog
  `status`. The vendor schema's desk-evaluation rule now matches the method and the worked example.
- Lines introduced by the fixes are wrapped under 120 characters.

Already sound: the description names the moment and all four siblings; state is saved after every step and resumed
from `overlay/policy.md`; handoffs are named with the `../<skill>/SKILL.md` fallback; owners are roles; there are no
calendar deadlines (the annual cadence is a labelled named-company template); grades are not used; the skill designs
and records, and the firm runs tests and approves.

## Formats and structure

- All three schema examples, both template frontmatters and `templates/tool-catalog.yaml` parse with `yaml.safe_load`.
  The template keys match the schema examples exactly (policy, vendor, catalog top level and entry).
- Ids used are in `vocabulary.yaml` (`runtime_classes`, `patterns`, `ladder`) or listed as new in the authoring
  report. One addition: vendor `decision` values, now defined in §3.5 (`pending` is the only value not already a
  catalog status).
- Every cited key in each step file has a §9 entry, and every entry is cited.
- `scripts/validate.py`: 0 errors. The core-rules block matches, backtick paths resolve, and sizes hold (SKILL.md 230
  lines; step files 161-183 lines).
- Sibling links: SKILL.md refers to siblings only by name and the generic `../<skill>/SKILL.md` fallback. All four
  sibling `SKILL.md` files exist, so nothing is unresolved.

## Sources not reached or only partly read

- Direct fetch failed but the mirror worked (counted as reached): EUR-Lex 2026/1744, OpenAI enterprise privacy,
  Microsoft Work Trend Index, Law Society, TPB, Winthrop, Mata v. Avianca.
- Partly read: Insurance Insider (paywalled sample; the vendor-liability line matches the summary); Raji et al.
  (arXiv abstract page only; SMACTR stage names not re-read in the paper); OWASP (index page only).
- Not re-read; cited only through archetype guardrails that have their own verification: JOFA-SOCETH-2026, and the
  tax, assurance and professional-services guardrail sections the skill points to.
- Official Journal publication and entry-into-force dates of Regulation (EU) 2026/1744 were not checked (the text is
  dated 8 July 2026).

## Open questions for the owner

1. **GV-6.1-008 misread upstream.** `research/runs/suite/topic-governance.md` (concept 9, moves 20-21) treats GV-6.1-008
   as records of vendor changes. Sibling skills or method files built from that research may repeat the misread.
2. **CPAi date.** Other files that cite `CPAI-ND` as "undated" should use July 2026.
3. **KPMG monitoring example.** IAB-KPMG-2025 reports AI-use tracking that feeds performance assessments, which sits
   close to core rule 1. Should any skill cite it as a positive example?
4. **Tax worked example.** Treating a summary that only restates figures as processing is the skill's reading.
   Should it stay in an illustrative example, or wait for a tax reviewer?
5. **Vocabulary.** The authoring report's question on moving governance ids into `vocabulary.yaml` stands; add vendor
   `decision` (`pending`) to that list.
6. **Vendor blogs.** Gend, Ampcus and Openlayer remain as labelled, directional evidence. Keep them, or replace them
   when better sources appear?
