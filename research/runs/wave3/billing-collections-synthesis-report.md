# Synthesis report: professional-services / billing-collections

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-billing-collections-practice.md`, `ps-billing-collections-discourse.md`,
  `ps-billing-collections-governance.md`; the "Routed to other modules" sections of every other `ps-*.md` file in `research/runs/wave3/`
  (items routed to billing-collections); the finished scoping-pricing, firm-finance and acceptance-risk YAML and modules (read for
  cross-references); assurance, tax and security use cases (searched for overlaps).
- **Outputs:** `plugins/.../professional-services/modules/billing-collections.md` (299 lines, contents list at top) and
  `plugins/.../professional-services/use-cases/billing-collections.yaml` (17 entries, built with `yaml.safe_dump`).
- **Checks:** `python3 scripts/validate.py` gives 0 errors; it warns that 5 of 17 entries (29%) are A/B, below the 50% target (see grade
  mix). A script confirmed every source key cited in the module is in the YAML or starred in the module's Sources list (3 starred), every
  YAML source appears in the Sources list, every inline key in a YAML entry is in that entry's sources, each key has one URL, date and type,
  and every cross-referenced id exists. No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed from other modules | Total |
|---|---|---|---|---|---|
| Candidates in | 17 (0 A, 6 B, 10 C, 1 D) | 13 (0 A, 2 B, 8 C, 3 D) | 12 (0 A, 1 B, 7 C, 4 D) | 2 firm-finance ideas (D) + evidence items | 44 |
| Out | | | | | **17 (0 A, 5 B, 9 C, 3 D)** |

## 2. Duplicates merged and cross-referenced

P = practice, D = discourse, G = governance, FF = ps-firm-finance-governance.

| Out | Merged from | Grade decision |
|---|---|---|
| 01 Passive time capture, drafted entries reviewed (law and accounting) | P01, P02, D01, G01 | B (named firms; all figures vendor-published; Big Four control group unnamed) |
| 02 AI-platform work becomes draft entries | P10, D02, G02 | C |
| 03 Guideline rules checked at the point of entry | P03, P04 (billing part), G03 | **C**: P04's B rested on Intapp Terms quotes from Fredrikson & Byron and Dickinson Wright about faster terms review, not billing enforcement; that named use is held in acceptance-risk-10 |
| 04 Linklaters bulk narrative checker | D03 | B |
| 05 Pre-bill review against guidelines | P05, G04, D04, ILTA-RISE-2025 concept (routed) | B (Foley Mansfield, 2024) |
| 06 Proforma prioritisation | P06 | C |
| 07 Fixed-fee scope-creep flags at bill time | P07, D07, G05 | C |
| 08 Idea: pre-bill write-down risk scoring | G12 | D |
| 09 E-billing appeals agent | P08 | C |
| 10 Collections prioritisation and drafted follow-ups | P09, D11 | C |
| 11 Automated overdue-invoice chasing with human collectors (CollBox) | G07 | C |
| 12 Time capture for non-billable staff (GHJ) | P12 | B |
| 13 In-house AI review of every outside-counsel invoice | P13, D05, G06 | B (Albertsons, recalled figure) |
| 14 Idea: AI-use tagging and pre-bill AI fee check | G09, P15, D09 (invoice part), FF-01 and FF-09 (routed ideas) | D |
| 15 Idea: single "services rendered" invoice | G10 | D |
| 16 Consulting PSA timesheet agents | P17, D13, routed delivery-management and staffing items | C (zeb is named but its timesheet agent is not described) |
| 17 Accounting WIP-to-invoice | D12 (+ Uku survey from G) | C |

**Not carried (held in finished modules; cross-referenced by id):** P11 leakage reporting and Elite Data Connect (firm-finance-03); P14 and
D06 in-house spend analytics and query layer (firm-finance-04); P16 Rates Agent (firm-finance-05); D08 aim AI at written-down work
(firm-finance-06); D10 and G11 AI cost metering and pass-through (firm-finance-12); G08 matter-level AI savings statement
(scoping-pricing-09); Intapp Terms OCG categorisation in P04 (acceptance-risk-10); client AI-restriction register at matter opening
(acceptance-risk-11, cross-referenced from 14). Tax billing rules: tax-compliance-corporate-16 and tax-compliance-individual-business-22.

**No grade was raised by merging.** One B was lowered (03, above).

**Source-key canonicalisation (to match existing YAML or resolve clashes)**

| Canonical key | Input variants and reason |
|---|---|
| LAUREL-TONKON-2026 | LAUREL-TONKONTORP-2026 (matches firm-finance) |
| LAUREL-WARREN-2026 | LAUREL-WARRENAVERETT-2026 (matches firm-finance) |
| LAURELSITE-2026 | LAUREL-HOME-2026 (same page; landscape key) |
| TRI-KOPKA-2026 | TRI-BILLING-2026 (matches scoping-pricing) |
| LAUREL-BILLING-2026 | LAUREL-BILLINGBLOG-2026 (same URL) |
| ADERANT-ITIMEKEEPHARVEY-2026 | discourse ADERANT-HARVEY-2026 (avoids a clash with ADERANT-HARVEY-2025, the 2025 partnership release) |
| LAWSITES-LITIFY-2026 | LITIFY-LAWSITES-2026 (typed vendor: a press release carried by LawSites) |
| LAYER3-OCG-2026 | governance LAYER3-AIOCG-2026 (the AI-provisions guide; existing YAML already uses LAYER3-OCG-2026 for it) |
| LAYER3-BILLINGOCG-2026 | governance LAYER3-OCG-2026 (the billing-guidelines guide; renamed to avoid the clash) |
| VACOURTS-LEO1901-2025 | practice VSB-LEO1901-2025 (the petition PDF; existing YAML uses VSB-LEO1901-2025 for a different VSB page, so the court's full text is cited instead) |
| TXETHICS-OP705-2025 | typed professional-body (practice typed regulator; existing YAML uses professional-body) |

**Date conflicts resolved:** Laurel Billing blog 2026-09-17 (two inputs) against 2026-08-19 (governance; a metadata date shared by several
Laurel pages), noted in entries 05 and the module; Litify release 2026-05-19 against 2026-05-21, recorded as 2026-05; Berger Singerman
2026-09-28 (discourse, more precise than practice's 2026-09). Laurel customer pages are dated 2026-08-21 (the page date governance saw);
firm-finance's YAML dates LAUREL-TONKON-2026 and LAUREL-WARREN-2026 as 2026-10 (retrieval month), so the two files differ on those dates.

## 3. Coverage by ladder and change scope

| | step | process | model |
|---|---|---|---|
| assist | 06, 09, 14 (D), 16 | 15 (D) | none |
| augment | 02, 03, 04, 05, 07, 08 (D), 10, 12 | 01, 13, 17 | none |
| automate | 11 | none | none |
| delegate | none | none | none |

- **Delegate: no evidence.** A chain of agents from staffing to billing is a concept only (ILTA-RISE-2025), and 26% of accounting firms in a
  vendor survey say they would hand invoice drafting and sending to an autonomous agent (UKU-AIACCOUNTING-2026). Laurel's and Aderant's
  billing "agents" all stop at a human sign-off, so they are recorded as augment or assist.
- **Automate: one thin entry** (CollBox), whose AI content is unclear in the source.
- **Model scope: none in this module.** The nearest are KPI retainer billing (scoping-pricing-18) and fee-mix change (firm-finance-01).
  The services-rendered invoice idea (15) is recorded as process.

## 4. Grade mix

0 A, 5 B (29%), 9 C, 3 D. The validator's 50% A/B target is not met and was not forced: almost every figure is on a vendor page, the one
controlled comparison (Big Four tax division) is unnamed, and announced agents (Aderant, Laurel Billing, Oddr) have no named users. Merging
the law and accounting time-capture entries (practice 01 and 02) into one also removed a B, because they describe the same change to the
work. No entry reaches A under the 2026-10-17 rule; Lerners' docket time and Albertsons' savings are recollections (B).

## 5. Routed items collected for other modules

| Item | Target module | Sources |
|---|---|---|
| AI-value and ROI measurement from time data (Laurel Signal, Legora-Laurel phase two, Laurel-TR partnership); realization and rate trends; Wells Fargo and LFFI data; consumption-priced AI as a variable cost; rate rises justified by AI; SPI "leak" | firm-finance | LAUREL-SIGNAL-2026, LEGORA-LAUREL-2026, TR-LAUREL-2026, TRI-RATES-2026, TRI-RATES-2024, TRI-PROSPERITY-2025, TRI-COOCFO-MARKET-2025, LAWFUEL-WF-2026, TRI-LFFI-Q1-2026, EDISCOVERYTODAY-ILTACON-2026, TRI-ILTACON-METER-2026, TRI-SOTLM-2026, SPI-AI-2026, BLOOMBERGLAW-GCXAI-2026 |
| Kopka KPI retainer; flat, value and retainer fee rules by state; Norton Rose hourly policy; tax practitioners' billing models; fixed-fee entry points; AFA debate; AICPA contingent-fee rule; consulting pricing map; fee-agreement AI wording | scoping-pricing | TRI-KOPKA-2026, CALBAR-GENAI-2026, NCBAR-FEO1-2024, VACOURTS-LEO1901-2025, TRI-ABA512-2025, BLOOMBERGLAW-TEXAS-2026, ACCTODAY-BLUEJ-2026, TRI-MIDSIZE-2026, TRI-ILTACON-HOUR-2025, AICPA-CODE-2026, STANFORD-DEL-2026 |
| Laurel-Dayshape time-to-resource-planning link; GHJ data for staffing | staffing-resourcing | LAUREL-DAYSHAPE-2026, LAUREL-GHJ-2026 |
| Aderant Talent Agent using time narratives for associate evaluation; associate training and pyramid; talent loss tied to time capture; non-billable learning time | talent-learning | ADERANT-AGENTSEAP-2026, TRI-LEGALWEEK-CRISIS-2026, WJLTA-RAPOPORT-2025, TRI-KOPKA-2026, ABA-BLT-2024 |
| Intapp Terms obligations in intake and conflicts; public-sector AI-use declarations; client-approved tool lists | acceptance-risk | INTAPP-TERMS-2026, CANBERRATIMES-APSAI-2025, LAYER3-OCG-2026 |
| Lead the client AI-ROI conversation; partners not discussing AI with clients | client-development | TRI-LEGALWEEK-2026, TRI-GREATDISCONNECT-2026, TRI-STANDOUT-2026 |
| Kantata and Certinia agents for resourcing and project admin; Harvey Legal Work Orchestration (not read) | delivery-management | ITBRIEF-KANTATA-2026, SILICONANGLE-CERTINIA-2026 |
| Verification burden as the driver of AI return; court rejecting ChatGPT support for billing rates; Deloitte Australia refund | quality-review | TRI-MIDSIZE-2026, DCBAR-OP388-2024, CTV-DELOITTE-2025 |

**Routed in but not used:** Diabsolut's "invoice turnaround 40% faster" (CERTINIA-PROVING-2026) is cited in entry 16's notes only, because
the input does not say what produced it. Deltek Dela timesheet automation and Kantata's calendar-based timesheet completion were not used:
the routing lines give no detail, Deltek's page has conflicting dates across inputs, and KANTATA-SUPERAGENT-2026 is search-only in one
input. Clio realization and flat-fee commentary (CLIO-SOLO-2026, routed from firm-finance) carried no billing-step detail.

## 6. Gaps

- **No measured outcome from any named firm,** and no edit, override, error or false-flag rate for AI-drafted entries, narrative checks,
  pre-bill flags, client-side invoice review or collection agents. The only accuracy figure is a vendor's (Onit).
- **Downstream of the pre-bill is announcement-only:** appeals, collections, scope and write-down agents have no named user.
- **Accounting and consulting are thin:** two named accounting firms (both in Laurel stories), one unnamed Big Four division, one vendor
  article; consulting billing (milestone invoicing, T&M against outcome billing) was not found. No delegate-level evidence anywhere.
- **Not read:** ABA Formal Opinion 512 itself (quoted through two secondary sources), SRA pages, Clio Legal Trends (figures secondhand
  through Oddr and CollBox), the Elite report itself, CLOC spend data, LexisNexis CounselLink, Wolters Kluwer BillAnalyzer, Epiq.
- **Monitoring law untested:** no source says whether passive time capture falls under the EU AI Act's worker-monitoring category or meets
  FAR timekeeping substantiation.

## 7. Suggested improvements to the briefs

1. **Ask angle researchers to check finished modules before drafting.** P04 duplicated acceptance-risk-10, and D06, D08, D10, P11 and P16
   duplicated firm-finance entries; listing the finished ids in each angle brief would save effort.
2. **Publish a shared key registry.** Five inputs used different keys for the same document (Tonkon Torp, Warren Averett, Kopka, Laurel
   home page, Laurel Billing blog) and two keys collided (LAYER3-OCG-2026, VSB-LEO1901-2025). A registry of ref, URL, date and type would stop
   both.
3. **Give a date rule for vendor pages with shared metadata dates** (Laurel's 21 Aug 2026 on many pages): page date shown, metadata date or
   retrieval month. Inputs used all three.
4. **Say how to count the A/B target when evidence is vendor-only.** The 50% target pushes toward splitting one change by firm kind (law and
   accounting time capture); the brief should say not to split for the target.
5. **Ask governance researchers to read routed ideas from sibling modules** (firm-finance's pre-bill AI fee check and client AI-terms
   register came here as ideas without billing-side evidence).
