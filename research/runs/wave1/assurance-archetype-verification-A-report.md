# Archetype verification report A: assurance

- **Files checked:** `economics.md`, `state-of-ai.md`, `frontier.md`, `disruption.md`, `workforce.md` in
  `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/`.
- **Date:** 2026-10-17.
- **Method:** 118 source keys were mapped to URLs. 117 came from bracketed keys; `CPAPA-GTNM-2024` was found later because
  its brackets wrap across a line. Each source was fetched with curl into a private working folder, with pdftotext for
  PDFs and r.jina.ai when a direct fetch was thin. Every figure, date, attribution, regulatory point and forecast was
  then checked against the source text. Three PDFs were also opened in full to settle specific points:
  FinancialAuditBench, the Stanford "Canaries" paper and the Shen and Tamkin skill-formation paper.
- **Validator:** `python3 scripts/validate.py` gives 0 errors. Its 8 warnings were already there and none is in these
  files. Every bracketed key in the five files resolves to an in-file Sources entry or to `sources.md`, each with a URL
  and a date.
- **Structure:** all five files are over 100 lines and each starts with a table of contents. Sizes: 205, 157, 105, 174
  and 182 lines (limit 300). No build-only references were found or left (research paths, "pilot" in the build sense,
  "wave", "spec").

## 1. Counts

| File | Claims checked (approx.) | Kept | Fixed | Removed |
|---|---|---|---|---|
| economics.md | 83 | 64 | 19 | 0 |
| state-of-ai.md | 60 | 45 | 14 | 1 |
| frontier.md | 47 | 31 | 15 | 1 |
| disruption.md | 45 | 31 | 14 | 0 |
| workforce.md | 60 | 49 | 10 | 1 |
| **Total** | **295** | **220** | **72** | **3** |

A "claim" is one checkable statement: a figure set from one source, a date, an attribution or a regulatory point. Table
rows with several figures from one source count once. "Fixed" includes labels added for provenance: forecast, paywalled
or retold, vendor-authored, inference.

## 2. Fixes and removals

### economics.md

| Where | Was | Now | Reason |
|---|---|---|---|
| §2 table, PwC | Assurance line "Not given" | Assurance US$19.8bn, +1.9% in US dollars | The source gives it |
| §2 table, PwC UK | "PwC UK group" | Adds "(UK, Middle East, Channel Islands)" | The group figure includes the Middle East (UK alone grew 2%) |
| §2 bullet | "Firm leaders attribute AI-linked revenue growth to non-audit lines: EY said..." | EY reported 49% AI-services growth with no split by service line | Unsourced connective claim; the release does not say non-audit |
| §2, §4, §6, §9 | "Small and mid-size US firms", "small firms" (CPA.com) | "54 US CPA firms of varying sizes" or "the 54 benchmark firms" | The report says "varying sizes and maturity levels" and gives no size breakdown |
| §4 bullet | Authors "recommend audit margin per engagement" | List it "among the metrics to track instead" | The report recommends several metrics, not one |
| §5 offshore | "FT figure relayed" | The FT's reading of KPMG UK's transparency report, relayed by trade press | Provenance stated precisely |
| §5 KPMG partners | No paywall note | "paywalled; only the headline and KPMG's statement were read" | Paywalled source |
| §6 table, Deloitte | "More than US$3bn in generative AI through FY2030" | "US$3bn through 2030 to modernise delivery and operations and bring new offerings to market (all businesses)" | Wrong qualifier and wrong purpose |
| §6 GT-CBIZ | "US$5bn including debt" | "a US$5bn deal" | The source does not say "including debt" |
| §6 reasons | "Stated reasons" | "Reasons given by firms or commentators" | "Partner liquidity" is blog analysis, not a firm statement |
| §7 KPMG fee | Second-hand label only | Adds "the FT original is paywalled" | Paywall rule |
| §7 PwC discounts | No provenance label | Bloomberg interview, paywalled, figures from a retelling | "In large part" and "plateaued" come from Scottish Financial News retelling Bloomberg |
| §7 research | "No study measures fees against the audit firm's own AI use" | Law and Shen also examined fees against audit offices' own AI use, but the summary does not report the result | The cited summary contradicts the original sentence |
| §7 channel | "buyers ask 'where are those savings going?'" | FERF's lead researcher says CFOs are asking it | Attribution drift; it is the researcher's framing |
| §8 pulse | 45% and 53% cited only to the JofA article | Adds [OPTRO-IAFUND-2026]; "373 respondents" | Those figures appear only in the Optro blog citing the IAF |
| §9 table | Staff per partner "13-19 in UK firms" | About 9-19 across 12 UK firms; 15-19 at the Big Four (2026) | Misread range: Johnston Carmichael 8.9 and RSM 9.8 were left out |
| §10 OPTRO-IAFUND | "undated", old title | Richard Chambers, *Internal audit's new resource reality...*, 5 May 2026 | The page is dated and titled |

### state-of-ai.md

| Where | Was | Now | Reason |
|---|---|---|---|
| §1 headline | "The Big Four and Grant Thornton US announced firm-wide agent platforms" | KPMG, EY, Deloitte and GT US; PwC has step tools and a planned platform | PwC has announced no firm-wide platform |
| §1 headline | "the best public survey of smaller US firms" | "the main public benchmark of US CPA firms (54 firms of varying sizes)" | Sample description |
| §1 quality | "anywhere in the archetype's modules" | "in public sources" | Self-reference to the knowledge base |
| §2 IFIAR | 2023-2024 data only | Adds that the 2026 report charts 2025 data: largely unchanged or slightly higher, more substantive-procedure use | Newer data exists, though as a chart only |
| §2 CPAB | "the first public inspection finding on such tools" | "2025 inspection cases where tools were the primary source of evidence..." | "First" is unsupported; the finding was about cases, not a single finding |
| §2 CPA.com header | "Small and mid-size US firms" | "US CPA firms of varying sizes", with no size breakdown | As above |
| §2 EY SOC | "drafting the Section 3 system description" | "updating..." | Source wording |
| §3 KPMG row | "controls agents unconfirmed" | "no public confirmation of controls agents found by Oct 2026" | Absence stated as a search result |
| §3 PwC row | Platform "about 18 months after 2026" | Oct 2025 aim for end-to-end tools in 2026 and a platform about 18 months later; labelled a PwC forecast | Forecast labelled and dated |
| §3 GT row | Scale "About 25,000 people across its platform" | "Full US Audit & Assurance practice, phased" | **Removed figure:** not in the cited release |
| §3 in-house | Reddit: 175 controls | Adds: since extended to over 75% of SOX controls | Same source, newer figure |
| §4 tiers | "capital from PE often tied to AI"; small tier presented as small-firm data; IA row cited to two sources | "partly sought for AI (Crowe, Eide Bailly)"; mixed-size proxy flagged; adds the Optro sources | Embellished qualifier; sample; flat headcount and agent testing were unsourced |
| §4 FRC | "an admission that the evidence base on smaller firms is thin" | "a research project to build an evidence base..." | Embellishment |
| §5 AICPA | "first" practice aid; "puts the client's AI into acceptance... reliance on service-organisation reports" | Lists what the aid actually covers; SOC guidance cited separately [DART-TQA-2026] | "First" unsupported; acceptance and SOC reliance are not what the release describes |
| §6 FinancialAuditBench | "some listed authors share names with an AI audit vendor's founders (affiliation unconfirmed)" | Built by Modus: six of eight authors list Modus Audit Inc., which supported the work; best model passed 69% of 90 tasks at first attempt | Confirmed from the PDF's affiliations and acknowledgements |

### frontier.md

| Where | Was | Now | Reason |
|---|---|---|---|
| §2 FRC sandbox | "Jun-Jul 2026... first round closed July 2026" | "4 Jun 2026... opens for applications", plus the smaller-firms research project | **Removed claim:** the closing date is not in the source |
| §2 IAASB | "5 Aug 2026" | "Aug 2026" | Day not confirmed (the exposure draft says August 2026) |
| §2 AICPA | "its first AI practice aid" | "an AI practice aid" | "First" unsupported |
| §2 IESBA | "after its July 2026 technology material"; "including independence and confidentiality" | Overarching piece planned for Q3 2026; AI use generally | The snapshot gives Q3 2026 as a plan and does not list those topics |
| §2 PCAOB Q1 2027 | "Watch for rules touching AI vendors and PE structures" | Same, labelled advisor inference; the agenda does not mention them | Forecast or inference labelled |
| §3 KPMG (WSJ) | Two-to-three-year timeline attributed to the digital chief | A KPMG briefing showed it; his quote is "next to no human beings" | Attribution drift |
| §3 benchmark | "authors may be linked to a vendor" | "built by Modus, an AI audit vendor"; type "Vendor-authored research preprint" | Confirmed vendor link |
| §3 PwC | Dated 7 Oct 2026: "a global agentic platform is still about 18 months away" [CFODIVE] | Savings quote dated 7 Oct 2026; platform plan dated Oct 2025 [PWC-AT-2025] | Wrong date and source: CFO Dive does not say this |
| §3 Thomson Reuters | "2026-2027" | "Undated", vendor plan with no date given | The source gives no date |
| §4 Repodo | "25 Aug 2026"; "small-company audits first" | "27 Aug 2026"; "small and medium-sized companies first" | Article date; source wording |
| §5 AIUC | "KPMG's own agentic platform" | KPMG US's aIQ Capture platform | Precision: US firm, named product |
| §5 SOC AI guidance | "11 Sep 2026 AICPA guidance" | "Sep 2026 AICPA technical Q&As (reported 21 Sep)" | Date not supported |
| §5 KPMG UK | "reasonable-assurance opinion" | "opinion under ISAE (UK) 3000" | The cited page gives no assurance level (the claim came from a different KPMG paper) |
| §6 calendar | "2027 IAASB guides" | "By Jun 2027, remaining guides" | Timetable detail |
| §6 forecasts | "each made by an interested party" | "all but the BLS projection" | The BLS is not an interested party |
| §7 Sources | n/a | Adds PWC-AT-2025 | Needed for the PwC row |

### disruption.md

| Where | Was | Now | Reason |
|---|---|---|---|
| §1 | Audit growth at all four cited to three sources | Adds CPAPA-PWCREV-2025 (PwC assurance +1.9%) | Supports "all four" |
| §1 | "...licensed auditor, which slows entrants" | "That slows entrants (inference)" | Connective claim labelled |
| §1 | "The question leaders are least ready for is pricing" | Labelled advisor's view, tied to "no firm leader has said publicly how audit pricing will change" | Unsourced connective claim |
| §2 Repodo | "small-company audits first" | "small and medium-sized companies first" | Source wording |
| §2 OnlyCFO | "predicts AI-first mid-tier firms will 'significantly cut fees'" | "expects a couple of the top 10 US firms to adopt AI heavily and 'significantly cut fees'" | Misread: the writer meant top-10 firms, not AI-first mid-tier firms |
| §3 | "Firm-wide agent platforms at the Big Four and GT US" | KPMG, EY, Deloitte, GT US; PwC's planned | As in state-of-ai |
| §3, §4 | "54 small US firms" | "54 firms in a US benchmark" or "54 benchmark firms" | Sample |
| §4 | "Two directions, both forecasts"; "buyers ask..." | "both argued; neither is measured across the market"; FERF's lead researcher says CFOs ask | A survey finding was labelled a forecast; attribution drift |
| §5 | GT-CBIZ "US$5bn" | Adds "not closed at the page date" | Status |
| §6 | CAQ unlabelled | "(the US auditing profession's policy body)" | Interested party |
| §6 EU | "eases entry for non-audit assurance providers" | "relaxes approval requirements for audit firms that only provide sustainability assurance" | Misread of recital 3 |
| §7 | KPMG UK "reasonable-assurance opinion" | "opinion under ISAE (UK) 3000" | As in frontier |
| §8 | "In KPMG's own framing, continuous monitoring is first- and second-line and internal audit work, not the external auditor's" | KPMG places monitoring with the first line and testing with internal audit, and says external auditors could also test full populations continuously | Misread: the source says external auditors can do it too |
| §9 | "Frame question F15" | Linked to `method/frame.md` | Navigation |

### workforce.md

| Where | Was | Now | Reason |
|---|---|---|---|
| §1 Director row | "Review of AI output becomes the main control" | "one of four mitigations in regulator guidance" | Embellishment |
| §1 IT audit row | "ITGCs extend to AI components; AI specialists in demand" | "Demand for AI specialists has spiked across audit and consulting" | **Removed claim:** nothing about ITGCs and AI in FRC-ARAQ |
| §2 FRC | "will monitor this for a year" | "will monitor the largest firms' resource models over the next year" | Source wording |
| §2 offshore, pyramid quote | Thin provenance | FT reading of the transparency report; "WSJ, reproduced" | Provenance |
| §3 UK students | "Student numbers rose 0.9%" | "in the UK and Ireland" | Scope |
| §4 UK intake | GT, Azets and Cooper Parry "planned increases" | GT +30% planned; Azets to match or beat 2025; Cooper Parry's largest cohort was in 2025 | Cooper Parry gave no 2026 plan |
| §4 PwC UK | "citing the economy first and AI second" | 1,300 against 1,500; UK head tied it to the economic slowdown while noting AI is reshaping roles | Interpretive ranking not in the source |
| §5 KPMG | Two-to-three-year timeline as the digital chief's | The briefing showed it; quotes labelled "WSJ, reproduced" | Attribution drift |
| §5 graduate programmes | "say they are overhauling" | "have overhauled or are overhauling"; "City AM, relayed" | Wording; provenance |
| §8 shortage | Grade split as fact; Advancetrack "vendor survey, ~500 firms" | Labelled advisor reading, with the FRC's experienced-staff attrition named; Advancetrack is a global outsourcing-vendor survey | Connective claim; scope |
| §10 VI-KGS | "(press, 2025)" | "(press, citing Economic Times, 15 Apr 2025)" | Date |

## 3. Sources that couldn't be fully reached

- **Bloomberg Law** (BBL-KPMGPARTNERS-2026, BBL-PWCPRICE-2025): paywalled. Only the opening and the KPMG statement could
  be read. The PwC figures were confirmed through the Scottish Financial News retelling. Both are now labelled.
- **KPMG UK AI governance assurance page** (KPMGUK-GOVAI-2026): read in full, including via the mirror. It never states
  an assurance level.
- **ICAEW viewpoint** (ICAEW-FRCVIEW-2026): a direct fetch returned only navigation. The mirror worked and confirmed the
  quote from the Chair of the Technology Faculty Board.
- **IAASB exposure draft page:** no exact publication day found, only August 2026.
- **KPMG Future of SOX PDF:** the 24 Sep 2026 date cannot be confirmed from the PDF itself and was kept from `sources.md`.
- **FERF:** read through a republished copy of the press release. The original PRNewswire URL is linked from that copy.
- **IFIAR 2026 technology report:** the 2025 observation shares are in a chart with no extractable numbers.
- No other source was blocked.

## 4. Error patterns seen

1. **Sample embellishment (most frequent).** The CPA.com benchmark, which covers firms of "varying sizes", was called
   "small and mid-size" or "small firms" in 9 places.
2. **Attribution drift.** FERF's researcher was quoted as "buyers"; a KPMG briefing slide was given to the digital chief;
   a CFO Dive date was attached to an Oct 2025 PwC plan.
3. **Embellished qualifiers.** "First" (CPAB, AICPA), "more than" plus "generative AI" (Deloitte), "reasonable assurance"
   (KPMG UK), "main control", "an admission that".
4. **Unsupported or invented details.** GT "about 25,000 people", the sandbox "first round closed July 2026", ITGCs and
   AI, "including debt", the TR "2026-2027" date.
5. **Misread sources.** Recital 3 of the EU directive; KPMG's three-lines framing; the OnlyCFO top-10 point; the UK
   leverage range.
6. **Unsourced connective claims.** EY AI growth "non-audit"; "slows entrants"; pricing readiness; the shortage-by-grade
   split. Each is now labelled inference, or removed.
7. **Vendor link not stated.** FinancialAuditBench is built by Modus (6 of 8 authors, company-supported). It was
   previously "unconfirmed".
8. **Absence claim contradicted by the cited source.** "No study measures fees against the firm's own AI use", while
   Law and Shen examined exactly that.

## 5. Notes for sources.md (not edited; owned by the other verifier)

- **REPODO-2026:** the Crowdfund Insider article is dated 27 Aug 2026, not 25 Aug.
- **ARXIV-FAB-2026:** suggest adding "vendor-authored: six of eight authors list Modus Audit Inc.; Modus supported the
  research" to the entry, and in Part A beside "Check authors' affiliations".
- **FERF-2026:** suggest the original release URL,
  https://www.prnewswire.com/news-releases/audit-fees-stable-but-one-third-of-finance-leaders-are-questioning-the-value-ferf-reports-302740824.html,
  in place of the republished copy.
- **KPMGUK-GOVAI-2026:** the page gives no assurance level. Any "reasonable-assurance" wording elsewhere should cite KPMG
  UK's January 2026 controls paper, or be dropped. None was found in the other archetype files.
- **CPAPA-DELREV-2026:** the US$3bn is "through 2030 to modernize delivery and operations across all Deloitte
  businesses", not generative AI specifically.
