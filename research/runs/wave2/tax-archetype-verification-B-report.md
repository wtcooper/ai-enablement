# Tax archetype verification B: report

Verifier: skeptical fact-check pass, 2026-10-17.
Files checked: `ARCHETYPE.md`, `interview-guide.md`, `value-chain.md`, `guardrails.md`, `objections.md`, `sources.md`
(all under `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/`).
Method: every cited URL (131 source rows) fetched with curl into a private `mktemp -d` folder; PDFs through
`pdftotext`; blocked pages retried through r.jina.ai; two web searches (EU AI Act Omnibus status, OECD FTA plenary).

## Counts

| | Count |
|---|---|
| Claims checked (figures, dates, quotations, attributions, regulatory points, Part A event dates, Evidence column) | 196 |
| Kept as written | 164 |
| Fixed | 31 |
| Removed | 1 (sub-claim that CPA "first-time candidates are rising") |

Evidence column in `ARCHETYPE.md` matches the validator's A/B counts for all eight modules (10/25, 3/24, 0/16, 4/22,
3/22, 10/25, 11/25, 8/24) and the strong/moderate/thin bands. `validate.py`: 0 errors; no warnings in these files.

## Fixes and removals

| # | File | Claim (before) | Action | Reason |
|---|---|---|---|---|
| 1 | ARCHETYPE | Signer carries "primary responsibility ..." "and the preparer penalties" [LII-CFR-SIGN-2026] | Fixed | The cited regulation defines the signer; penalties are in 6694 and apply to any preparer. Now points to guardrails §5 |
| 2 | ARCHETYPE | "12.5% of indirect tax leaders have AI targets" | Fixed | Added base (176) and vendor-survey provenance; wording is "targets or KPIs" |
| 3 | interview-guide | "Blue J lists US$1,498 a year per user" | Fixed | That price is the individual plan ("best for sole practitioners") |
| 4 | interview-guide | "vendors quoted one firm US$100-150 or more per return" | Fixed | WCG reports one vendor's average of US$100-150 and expected to pay US$200-250 |
| 5 | value-chain | "Fee rule now ties AI to billing" | Fixed | The rule did not change; it is OPR's reading, contested by the AICPA |
| 6 | value-chain | Small and mid-size firms "often offshore preparation (68% of IPA 100 firms ...)" | Fixed | IPA 100 are the largest US firms; the figure does not describe small firms |
| 7 | value-chain, guardrails (and economics, disruption) | Key `ECFR-10.27` | Fixed | Key was cited in four files and defined nowhere. Added to sources.md Part B (eCFR, up to date as of 15 Oct 2026) |
| 8 | guardrails §2 | "CART launched 23 Sep 2026" | Fixed | Source reports an announcement on that date |
| 9 | guardrails §2 | EU: "Deferral of high-risk duties provisional" [GIBSON-AIACT-2026] | Fixed | Digital Omnibus adopted: Regulation (EU) 2026/1744, OJ 24 Jul 2026 [CUATRECASAS-AIOMNIBUS-2026, new] |
| 10 | guardrails §4 | 7216 fine US$1,000; 6713 US$250 capped US$10,000 | Fixed | Correct but incomplete: both are higher for identity-theft disclosures (US$100,000; US$1,000 and US$50,000) |
| 11 | guardrails §4 | LLM-vendor consent question "has no IRS answer" [WINTHROP-ABA-2026] | Fixed | Winthrop is a panel notice that frames the question; the "no IRS guidance" point is MYCPE's. Reworded, both cited |
| 12 | guardrails §4 | Consent "cannot be a condition of service" | Fixed | 301.7216-3(a)(2) allows conditioning on disclosure to another preparer assisting with the return |
| 13 | guardrails §4 | Heppner "a securities case" | Fixed | A securities-fraud prosecution (criminal) |
| 14 | guardrails §6 | Khoja: "Judge questioned an IRS attorney"; dated "Mar 2026" | Fixed | Bloomberg says the judge ordered a hearing on the motion; the Mar 2026 date is the report's, not the order's |
| 15 | guardrails §6 | Charlotin: tax entries from "the US, UK, Australia and India" | Fixed | Database CSV shows tax entries also from Brazil, Netherlands, Poland, France, Italy; count dated 16 Oct 2026 |
| 16 | guardrails §6 | Deloitte Australia "repaid part of" the fee | Fixed | The Guardian reports an agreement to repay the final instalment |
| 17 | guardrails §7 | EU AI Act "provisional deal ... formal adoption was not confirmed" | Fixed | Adopted and in force; 2 Dec 2027 confirmed; literacy duty recast as "support" |
| 18 | guardrails §9 | "TPB requires client permission for third-party AI" | Fixed | TPB: permission needed "depending on how these tools are configured and used" |
| 19 | objections §1 | Quote "polite, quiet and technical" | Fixed | Source reads "polite, quiet, and technical" |
| 20 | objections §1 | "there is no IRS guidance on AI and commentators disagree" | Fixed | No cited source shows disagreement; reworded to the open question and the ABA panel |
| 21 | objections §1 | "TPB needs client permission for third-party AI" | Fixed | Same qualifier as #18 |
| 22 | objections §2 | 65%/99% are "from launch releases without ... denominators" | Fixed | 99% comes from press coverage of Black Ore and states "tens of thousands of returns"; TR says "up to 65%" on routine reporting. Reworded |
| 23 | objections §2 | WCG "tested five" vendors | Fixed | Source: months of demos and pricing talks with five vendors ("evaluated") |
| 24 | objections §3 | "Big Four tax lines grew"; "small-firm fees are above 2020 levels" | Fixed | Only EY is cited (tax +6.0% FY2026); NSA says return fees rose 10-30% since the last (2020) survey |
| 25 | objections §3 | "Research AI lists at about US$1,498" | Fixed | One tool's individual plan |
| 26 | objections §4 | "Enrollment and first-time candidates are rising" | Removed (part) | Source covers enrollment (four-year programs +8.9%), not first-time candidates |
| 27 | objections §4 | PwC US "plans a one-third cut in entry-level hiring" | Fixed | Fortune/Business Insider: "almost a third over the next three years" |
| 28 | objections §4 | "Firm-side effects concentrate on junior hiring" [MIT-DOWNING-2026] | Fixed | Misread: the thesis studies corporate accountants at companies, not accounting firms; declines via attrition |
| 29 | objections §4 | "Employers are hiring them and accept tax-adjacent experience" | Fixed | One posting; it asks for six years, two of them tax or tax-adjacent |
| 30 | objections §5 | Agentic commerce raises who-collects questions "for sellers" | Fixed | Bloomberg Tax: liability may fall on the operator of the agent |
| 31 | objections §6 | "no cost-per-return benchmark exists [IRS-BTB-2026]" | Fixed | The IRS page is a survey still collecting responses; reworded as "none found" plus that fact |
| 32 | sources.md | WINTHROP-ABA-2026 dated "event listed 6 Oct 2026" | Fixed | Page published 14 Aug 2026; panel 6 Oct 2026 |

(Row 26 is the removal; the other 31 rows are fixes.)

Verified and kept (selection): TR corporate tax 58%/67%/288 and reactive-time and penalty findings; OPR Alert 2026-19
text for all six provisions, "whether they are aware of it or not", no mention of consent, state laws named; GAO 126
use cases; IRS "AI-first"; TR FOP (more than a third unauthorized tools; more than a quarter would not join); Ignition
219 firms, 3% hourly, 37% fixed, 80% plan rises; IPA 68%; EY 51%; KPMG indirect 58%/61%/23%; Aibidia 79%; GIR more
than 100 data points; FGS XML; TR SOTP 75%/639; TR SOTCD 9 and 36; TR tech report 39% of 170; KPMG Germany 58%; Vals
49.19%; TaxCalcBench "less than a third"; LB&I "shouldn't replace"; 7216 regs (software developers, substantive
determination quotes, SSN rule); 6694 amounts; PCRT (19 Jan 2026, "likely" breach, specialist, explain, risk-based);
TPB (22 Jul 2026, "take actions on behalf of the user", "throughout each step", no new obligations); BStBK (27 Jan 2026,
technology-neutral, EU hosting, liability exclusions, Art. 4 deployers); Clinco (three of four, "Yet."); Riddle
withdrawal of Exhibits 9006-R and 9007-R; Holmes (fewer than a dozen, section 6673 up to US$25,000, certification
quote); Harber (nine cases, decided without them); SSTS 1.4 and effective date; Werfel (20/4 and 15/5, named risks,
phased deployment, author's views); CART participants; Aon, McGowan opt-out, CAMICO; HMRC GBP 10bn; Canaries 19%;
TRI judgment (more than half need remediation); TRI dual roles 57%; Crete over US$300m; CFO Brew 10 of 20; all Part A
event dates that could be reached (ABA 7-9 May confirmed from the programme's day headers despite cover art reading
"May 8-10").

## Sources that could not be reached or fully confirmed

- **AICPA-ENGAGE-2026** (Karbon page behind a captcha; AICPA page returned nothing via proxy): 8-11 Jun 2026 date kept, unconfirmed.
- **ITR-AIFORUM-2025**: speaker and home pages reached, but the 16 Sep 2025 date is not shown; kept, unconfirmed.
- **OECD-FTA-2025**: OECD blocks curl and jina (captcha); dates and Cape Town confirmed by web search (OECD media advisory title).
- **GAO-2026**: gao.gov returns 403; content read through jina; the 24 Mar 2026 date is not printed in that copy.
- **TEI-ANNUAL-2026**: JavaScript page, no content; claim is only "recaps not yet published".
- **BLS-ACCT-2026**, **CAMICO-FAQ-2025**, **STANFORD-AUDIT-2022**, **TPB-GS55-2026**, **WINTHROP-ABA-2026**, **OPENAI-CODEX-2026**: blocked to curl; all but BLS read through jina. BLS is not cited in these six files.

## Error patterns seen

- **Misread statistics or populations:** IPA 100 figure applied to small firms (#6); MIT corporate-accountant study presented as accounting-firm evidence (#28).
- **Attribution drift:** "no IRS answer" and "commentators disagree" pinned on a panel notice (#11, #20); penalties attributed to the signer definition (#1); Big Four generalised from one firm's results (#24).
- **Embellished qualifiers:** "tested" for demos (#23); "repaid" for agreed to repay (#16); "questioned an IRS attorney" (#14); TPB permission and consent rules stated without their conditions (#12, #18, #21); price of an individual plan presented as the general price (#3, #25); one job posting generalised to "employers" (#29).
- **Unsourced connective claims:** "first-time candidates" (#26); "fee rule now ties AI to billing" (#5).
- **Wrong or stale dates:** EU AI Act still described as provisional three months after publication (#9, #17); Winthrop date (#32); Khoja dated by the press report (#14).
- **Forecasts presented as facts:** none found in these files; vendor figures were already labelled as company statements.
- **Structure:** one unresolved source key (`ECFR-10.27`, #7). TOCs present in all files over 100 lines; ARCHETYPE.md held at 100 lines.

## For other agents (files outside this pass)

- `frontier.md` lines 33 and 94 still describe the AI Act deferral as provisional and unadopted; it was adopted
  (Regulation (EU) 2026/1744, OJ 24 Jul 2026). The key `CUATRECASAS-AIOMNIBUS-2026` is now in sources.md Part B.
- The same wording issues recur in `disruption.md:43` and `state-of-ai.md:27` ("tested five vendors"),
  `economics.md:82` ("vendors quoted"), `workforce.md:87` and `modules/compliance-individual-business.md:213`
  (quote punctuation "polite, quiet, and technical"). `economics.md:57,138` says all Big Four tax lines grew; check it
  cites all four.
