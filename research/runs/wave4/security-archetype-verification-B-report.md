# Security archetype verification B: report

Date: 2026-10-17. Files checked: `ARCHETYPE.md`, `interview-guide.md`, `value-chain.md`, `guardrails.md`,
`objections.md`, `sources.md` (all in `references/archetypes/security/`). Sources were fetched with curl (text
mirror for blocked sites, pdftotext for PDFs) into a private temporary folder.

## Counts

| | Checked | Kept | Fixed | Removed |
|---|---|---|---|---|
| Prose claims (figures, dates, attributions, regulatory points, forecasts) | 151 | 123 | 27 | 1 |
| Source-list entries and event rows (title, date, URL, descriptor) | 105 | 97 | 8 | 0 |
| **Total** | **256** | **220** | **35** | **1** |

Prose fixes by file: ARCHETYPE 3, interview-guide 1, value-chain 2, guardrails 5, objections 16 (plus one objections
clause removed). Source-list fixes: 8, all in `sources.md`.

Structure: every source key used in the five prose files resolves (in `sources.md` Part B, guardrails §10 or
value-chain §8), and every entry has a URL and a date. Every Part B key is cited in at least two archetype files.
Files over 100 lines have a contents list; `ARCHETYPE.md` stays at 100 lines after the edits. No file is near the
300-line limit. `validate.py`: 0 errors. ARCHETYPE.md's Evidence column matches the validator's A/B counts for all 11
modules (11/21, 20/24, 14/24, 12/22, 16/25, 15/17, 5/24, 11/24, 8/21, 9/18, 20/25), and the strong/moderate/thin
bands are right.

## Fixes and removals

| File | Claim as written | Change | Reason |
|---|---|---|---|
| ARCHETYPE | "In every module almost all A and B figures are self-reported... or published by a vendor" | Now: most are; the independent figures are mostly surveys, benchmarks and lab tests | YAML outcome provenance: ai-security 22 of 65 A/B figures independent, threat-intelligence 11 of 35, vulnerability-exposure 11 of 47, governance-risk 9 of 32 (misread statistic) |
| ARCHETYPE | operations: "Six A grades, all deployers' own figures" | Five on deployers' figures, one on a Microsoft-authored study | operations-12's A rests on MSFT-BONO-2024 (vendor-published) |
| ARCHETYPE | application-security: "A grades come from very large engineering firms" | Cloudflare, Google and one testing firm (Trail of Bits) | One of the four A entries is Trail of Bits |
| interview-guide | 33% of employees in a Gartner survey entered sensitive data into unapproved tools | Added: survey of 175 employees | Small sample stated in the Gartner release |
| value-chain | Huntress managed EDR lists at USD 8.99 per endpoint a month | Added: MSRP at 100 units | Price page qualifier |
| value-chain | Accenture "announced a majority stake in Dragos on 2026-06-18" | Agreed 2026-06-18, closed 2026-09-16 | Press-release closing note |
| guardrails | HIPAA NPRM status "Proposal" in a column headed "Status on 2026-10-17" | Added: no final rule found in the sources read | Current status could not be checked (Federal Register blocks automated access) |
| guardrails | "after the SEC's 2024 clarification" | "after SEC staff's May 2024 clarification" | Debevoise: statement by the Director of the Division of Corporation Finance (attribution drift) |
| guardrails | NYDFS 2024 letter "expects... MFA that deepfakes cannot defeat"; "invites AI for log review" | Expects board understanding, diligence, training; *suggests* deepfake-resistant MFA; *notes* AI's value | Letter says entities "should consider" such factors (embellished qualifier) |
| guardrails | "The application is a signed attestation" | "Know what your insurance application attests to" | Not stated in BIS/FSI paper (unsourced connective claim) |
| guardrails | "Beazley added affirmative AI cover" | Confirmed affirmative AI wording for AI risks it says were already covered | Beazley release wording |
| objections | AIDA cut misses to 3.1% | Added: while escalating 18.4% of alerts to analysts | Abstract; trade-off omitted |
| objections | "No independent production miss or override rate exists" | "was found" | Absence in sources, not proof of absence |
| objections | "The one US test case was dismissed" | The SEC's case against SolarWinds and its CISO was dropped | "The one" is unsourced and overstated |
| objections | "Under NIS2 and DORA liability sits with the management body" | NIS2 lets management bodies be held liable; DORA gives ultimate responsibility for ICT risk | DORA Art 5 says responsibility, not liability |
| objections | "one carrier added affirmative cover" | "confirmed affirmative AI wording" | Beazley release |
| objections | "Headcount risk comes more from budget cuts (36%) than AI" | Budget cuts are common: 36% of ISC2 respondents' organizations had them | Comparison not in ISC2 (unsourced connective claim) |
| objections | "board-level risk, which drove the largest increases" | Board focus on security, which IANS links to the largest average increases (23%) | IANS wording |
| objections | "providers will keep the gains" | Gartner *expects* providers to absorb gains (a forecast, per a vendor summary) | Forecast stated as fact |
| objections | "4,000 investigations per AI analyst a year" | "up to 4,000" | Dropzone price page |
| objections | IBM USD 1.93M lower breach cost | Added: than using none | IBM comparison group |
| objections | "39% report no entry-level reductions yet" | Added: 32% say AI is affecting entry-level SOC analyst roles (SANS/GIAC slide 7) | One-sided reading of the slide |
| objections | "ISC2 withdrew the gap number as a headline in 2025" | ISC2 put the gap at 4.8M in 2024 and published no estimate in 2025 | ISC2 2025: "has not included an estimate"; ISC2 2024: 4,763,963 |
| objections | "A senior shortage can coexist with fewer entry seats [D3]" | Entry-level roles were 6% of 665 US SOC postings (vendor analysis) | Made the D3 support specific; D3 is a snapshot, not a trend |
| objections | "Employers value them, but..." (certifications) | **Removed** the clause | No source |
| objections | "Providers... keep humans in escalation" | Hire experienced analysts (2+ years in one posting) and bring humans in when confidence drops or impact rises | Huntress posting and Arctic Wolf post wording |
| objections | ToB: "human first fixes fail 12.5%... Trail of Bits is a participant" | 12.5% of developers' first fixes in ToB audits failed; 86% blocked the supplied exploit (not proof of full repair); ToB runs its own AI patching programme | ToB post caveats; "participant" was vague |
| objections | GTIG "agent-run campaign"; zero-days only 8 to 11 a month | Agent-enabled campaign; added overall exploitation 10.5 to 18 a month, mostly n-days | GTIG wording; the zero-day-only figure understated the rise |
| sources | SANS AI Summit URL (now 404) | Live URL; fall 2-3 Nov 2026 confirmed; April dates marked not reconfirmed | Page moved |
| sources | S4x27 "dates unverified" | 8-11 Feb 2027, Tampa | s4xevents.com |
| sources | NIST-COSAIS "drafts 2025-08-14 and 2026-01-08" | Concept paper 2025-08-14; annotated-outline discussion draft 2026-01-08 | CSRC project page |
| sources | GOOGLE-AGENTICSCAN title "Using agentic AI to..." | "Using AI agents to secure Google infrastructure" | Page title |
| sources | HELPNET-GARTNER-2026 "headline seen only in search results" | Sponsored article by a Prophet Security product manager quoting a Gartner 2028 forecast | Page now opened |
| sources | YAHOO-CCS-2026 "c. 2026-02-20" | 2026-02-23 | Page metadata |
| sources | ISACA-AIPULSE-2026 "2026-03" | 2026-03-23 | Release date |
| sources | IANS-BUDGET-2026 URL covered only the landing page | Added the press-release URL, which holds the 69% headcount and 91%/81% figures | Claims in objections and economics come from the release |

## Sources that couldn't be reached or confirmed

- Gartner Security & Risk Management Summit page (blocked; mirror returned nothing): dates 1-3 Jun 2026 not reconfirmed.
- Black Hat USA 2026 dates (1-6 Aug) and RSAC 2027 dates (5-8 Apr): not found on the pages reached; left as written.
- SANS AI Cybersecurity Summit spring dates (20-21 Apr 2026): original URL 404; marked not reconfirmed.
- HIPAA Security Rule final status: Federal Register blocks scraping and the API query failed; the NPRM text was read
  through a mirror and supports the AI-inventory claim.
- OWASP LLM Top 10 date (2025-03-12) and IBM CODB date (2026-07-29): no date on the pages; left as written.
- Reached only through the text mirror: CISA, Covington (2), Computer Weekly, Dark Reading, Debevoise, EUR-Lex (NIS2,
  DORA), Gartner newsroom, gov.ie, Hansard, MSSP Alert, RSAC, SEC, CrowdStrike earnings (Morningstar), Torq. The RSAC
  slides PDF was downloaded directly from the session page link.

## Error patterns seen

- **Misread statistics:** the ARCHETYPE bold claim about provenance did not match the YAML.
- **Embellished qualifiers:** NYDFS "expects" for "should consider"; "exists" for "was found"; "the one test case".
- **Attribution drift:** SEC staff statement given to "the SEC"; DORA responsibility called liability.
- **Unsourced connective claims:** budget cuts versus AI as the headcount risk; "employers value" credentials;
  "signed attestation".
- **Forecasts as facts:** Gartner's expectation about MDR providers keeping gains.
- **Selective figures:** zero-days without total exploitation; 39% without the 32%; AIDA's miss rate without its
  escalation rate.
- **Wrong or vague dates:** Yahoo, ISACA poll, S4x27, COSAiS draft labels.
- No wrong ISACA scope found: guardrails and the interview guide use the global figures (8%, 64%) and label them.

## Notes for other files (not edited here)

- `frontier.md` and `state-of-ai.md` call HELPNET-GARTNER-2026 "search-only"; it has now been opened and is a
  sponsored Prophet Security article quoting Gartner. Their labels should change in the other verifier's pass.
- The live CISA page now titles the guidance "Careful Adoption of Agentic SI Services"; the guidance was issued as
  "...Agentic AI Services" (URL and the ACSC document), so `sources.md` keeps the issued title and prose says AI.
