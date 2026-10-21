# Synthesis report: assurance / private-company (wave 6, mid-market)

Synthesised 2026-10-21. Outputs:
- Module: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/private-company.md` (under 300 lines, table of contents included)
- Use cases: `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/private-company.yaml` (20 entries; `scripts/validate.py` passes with one warning: 45% A/B is below the 50% target)

Suggested archetype index row (for the coordinator): `private-company` | audits of private middle-market companies and
SSARS preparation, compilation and review at local, regional, top-100 and PE-backed firms; platform choice, client data
and QM-tested-by-peer-review are the constraints; no measured outcome | moderate (9 of 20 A/B).

## 1. Counts in and out

| Input | Entries | A | B | C | D |
|---|---|---|---|---|---|
| Practice (`mm-private-company-practice.md`) | 14 | 0 | 8 | 5 | 1 |
| Discourse (`mm-private-company-discourse.md`) | 11 | 0 | 1 | 9 | 1 |
| Governance (`mm-private-company-governance.md`) | 16 | 0 | 3 | 7 | 6 |
| **In** | **41** | 0 | 12 | 21 | 8 |
| **Out** | **20** | 0 | 9 | 9 | 2 |

41 in, 14 removed by merging within the module, 7 dropped as duplicates of other modules' entries, 20 out.

## 2. Duplicates merged (P = practice, D = discourse, G = governance, numbered as in each input file)

| Output | Merged from | Note |
|---|---|---|
| -01 one platform (DAS + Verity) | P02, G05 | PCR facts of D07 moved to -17 |
| -03 test tools on own files | D05, G06 | |
| -04 gtap and EisnerAI | P11, D04 | |
| -07 policy, approved tools, training | G02, G11 | |
| -09 start with general GenAI on low-risk tasks | G09, D10 | Grade B comes from G09 (named firm, independent study); D10 is advice |
| -12 PBC validation and extraction | P08, D02, D03 | |
| -15 Verity for Excel | P09, D01 | |
| -16 peer-review-aimed gap flagging | P06, D06, G07 | |
| -17 SSARS on the same platform | P14 (D), D07, G16 | Output C; the AI-drafting step is labelled an idea in the entry |
| -18 where AI savings go | P13, G15, D09 | |

Kept as single-source entries: -02 (D08), -05 (P07), -06 (P12), -08 (G08), -10 (P01, trimmed), -11 (P10), -13 (P03),
-14 (P05), -19 (G14), -20 (D11).

**Dropped because another module already holds the same change to the work** (facts folded into cross-references or
the module text):

| Input | Now held by |
|---|---|
| P04 PB&H / Perry Excel agents, single-audit tests | `assurance-nonprofit-government-07` |
| G01 AI in the SQMS risk assessment | `assurance-quality-management-26` |
| G03 engagement letters and consent | `assurance-quality-management-24`, `assurance-acceptance-independence-11` |
| G04 vendor terms review | `assurance-quality-management-06` |
| G10 Fedyk et al. central AI capability (largest 36 firms, pre-GenAI) | `assurance-quality-management-07` (key FEDYK-2022) |
| G12 independence screen of platform and co-development deals | `assurance-acceptance-independence-13` |
| G13 change management for staff-built agents | `assurance-quality-management-27` |

P01 was trimmed to Plante Moran and Harris, Hardy & Johnstone; its small nonprofit-firm material is in
`assurance-nonprofit-government-01`, `-02`, `-05` and `-06`.

## 3. Normalisation changes

- **Ladder re-rated:** -13 proof of cash augment to automate (every transaction reconciled, people take exceptions;
  matches the vocabulary's worked example); -14 sampling augment to automate, to match `assurance-nonprofit-government-06`
  for the same tool. Merged entries with conflicting ratings took one value: -01 augment (P02 said assist), -03 augment
  (D05 said assist), -17 augment/step (D07 said assist/process).
- **Source keys harmonised to existing archetype keys** where the same URL already had one: AICPA-PA-2026 (inputs used
  AICPA-AIPA-2026), CASEWARE-CITRIN-2026 (inputs: CITRIN-DAS-2026), CASEWARE-EISNERAMPER-2026 (inputs also used
  CASEWARE-EISNERDAS-2026 and EISNER-DAS-2026), CASEWARE-PKF-2026 (also PKF-DAS-2026), CASEWARE-LAUNCH-2026 for the
  20 May 2026 Verity release, CASEWARE-RSA-2026, CPAPA-GT-2026, CALCPA-AISTD-2026, TR-SCALING-2026, TR-STATE-2026,
  CPAPA-STOP-2026, CFODIVE-AICPAPA-2026, AICPA-AIPAID-2026, JOFA-CHECKLIST-2026, JOFA-DISCLOSE-2025, JOFA-ETHICSAI-2026,
  TRI-FOP-2026, OSCPA-PR-2026 (Oregon), FEDYK-2022.
- **Key collision avoided:** the archetype's `sources.md` and planning-risk-assessment use CASEWARE-VERITY-2026 for the
  CwX blog, while the landscape and two inputs used it for the launch release. The new files use neither meaning of
  CASEWARE-VERITY-2026: blog = CASEWARE-CWX-2026 (as in completion-reporting), release = CASEWARE-LAUNCH-2026.
- **Oklahoma versus Oregon:** governance used OSCPA for Oklahoma and discourse used OSCPA for Oregon. Now Oklahoma =
  OKSCPA-PEERREVIEW-2025, Oregon = OSCPA-PR-2026 (existing key). Other state reports: CTCPA-, MNCPA-, MOCPA-PEERREVIEW-2025.
- New keys introduced: CASEWARE-WITHUM-2026, CASEWARE-VERITYXL-2026, CASEWARE-DASPCR-2026, CASEWARE-DASUPD-2026,
  GOINGCONCERN-0803-2026 (renamed from GOINGCONCERN-2026-08-03 to fit the format), JOFA-AAFOCUS-2025 (was -2025-09),
  JOFA-REALLIFE-2026 (practice called it JOFA-SMALLFIRMS-2026). JOFA-PEER-2026 follows `sources.md`; three YAML files
  call the same article JOFA-PRB.
- Fixed in passing: 'Sage Intact' in the practice file is written as Sage Intacct (noted in -13). The NYSSCPA SSARS
  webcast is cited as `full` (the discourse researcher opened it; practice had it as search-only).

## 4. Coverage by ladder and change scope

| Ladder \ scope | step | process | model | Total |
|---|---|---|---|---|
| assist | 07, 09, 10, 19 | 02, 06, 08 | 18 | 8 |
| augment | 03, 12, 15, 16, 17 | 01, 04, 05, 11 | none | 9 |
| automate | 14 | 13 | none | 2 |
| delegate | none | none | 20 (idea) | 1 |

- **Delegate:** no evidence. The only entry is a D idea from a machine-written podcast summary (-20). FGMK's background
  agents (-05) run multi-step jobs, but people review every workpaper, so they are augment.
- **Automate:** thin. Two entries, both vendor case material with a named small or regional firm.
- **Model scope:** two entries, both C or D (fees and value reporting; AI-native start-ups).
- No augment or automate entry at model scope was supported by the inputs; none was invented.

## 5. Grade mix

0 A, 9 B (45%), 9 C, 2 D. **No A is supportable**: under the 2026-10-17 rule every figure here is vendor-published, a
firm quote in vendor material (Holbrook & Manter, Sam Brown, Harris Hardy & Johnstone), an adoption count, or a survey.
The best independent material is adjacent: peer-review nonconformance tables (measure the problem, not an AI effect),
the Beever and Struthers study (UK, staff perceptions, press report only; held at B), and FEDYK-2022 (largest firms,
pre-GenAI; left in quality-management). The 50% A/B validator target is missed honestly; raising it would need
re-grading vendor case studies or dropping C entries that carry the only SSARS, intake and pricing evidence.

## 6. Gaps

- No measured outcome (error rate, override rate, parallel run, review notes, peer-review result) for AI in any
  private-company audit, review or compilation.
- SSARS: no AICPA, ARSC or state-board AI guidance and no firm case; DAS PCR makes no AI claim.
- No AI content in any of the six state peer-review reports read (TN, CT, MN/ND, MO, OK/SD/KS, OR); the AICPA QM
  checklist report and the practice aid itself are members-only and were not read.
- Non-ERP client data: only a podcast and a partner quote (Audit Sight); Validis and Inflo not examined.
- Firm size: no named deployment below the top 100 except small local firms inside vendor case studies; size not stated
  for Harris Hardy & Johnstone, Holbrook & Manter, FGMK, GRF, AAFCPAs.
- Practitioner communities (Reddit, TaxProTalk) unreadable (403); ENGAGE 2026 recordings not found.
- Mid-market fee data: none tied to AI.
- Several vendor pages undated (DataSnipper, Thomson Reuters case pages, DAS PCR); years are inferred and flagged in notes.

## 7. Routed to other modules (collected from the three inputs' "Routed to other modules" sections)

**planning-risk-assessment**
- Caseware Risk Suggestion Agent: worldwide launch 2026-10-06, included at no extra cost, GRF partner quoted; CwX demo
  found five risks including a $118,000 gap between trial-balance and board-minutes profit [CASEWARE-RSA-2026;
  CASEWARE-CWX-2026] -> `-09`.
- Practice aid's question on how far the client relies on AI in reporting gives the idea entry `-06` a published source
  [AICPA-PA-2026; AT-AICPAPA-2026] (also assurance-over-ai); gtap any-ERP ingestion -> `-07` [GT-GTAP-2026].

**completion-reporting**
- Disclosure Checklist Agent 2.7 review hours per run (beta, vendor), Withum in testing, used as a second look at a
  completed checklist [CASEWARE-WITHUM-2026; CASEWARE-CWX-2026]; Thomson Reuters Disclosure Review used by roughly 30%
  of eligible customers, about 300 analyses a month, plans for 'no' and 'N/A' determinations [TR-DISCLOSURE-2026]
  -> `-01`, `-03`, `-04`.
- Trullion statement validation (quoted Bennett Thrasher partner) in Guided Assurance [TR-GUIDEDASSURANCE-2026] -> `-06`.

**substantive-testing**
- JofA Excel agent cleaned a simulated 59,157-row ledger in about 10 minutes on average (demonstration) [JOFA-EXCELAGENT-2026] -> `-07`.
- Crunchafi lease recalculation (quoted Hutchinson & Bloodgood partner) [TR-GUIDEDASSURANCE-2026] -> `-14`.
- FGMK and DataSnipper at regional firms -> `-11`, `-12`; Verity for Excel overlaps `-07`, `-11`, `-12`; Document
  Intelligence Agent -> extraction entries; Thomson Reuters Audit Intelligence Test and the Oberlander quote already there.

**quality-management**
- Texas State Board policy elements and documentation advice (Aug 2026) [TSBPA-2026].
- Citrin Cooperman's split of firm-level AI governance (Risk Management Officer) and practice-level policies [CASEWARE-READINESS-2026].
- AICPA QM peer-review checklists; annual practice questionnaire; test-and-learn first year [AICPA-QMPR-2026;
  AICPA-APQ-2026; AICPA-QMPEER-2026; CPACOM-SQMS-2026] -> `-26`.
- Junior development after AI absorbs rote work [CPAPA-STOP-2026] -> `-25`; engagement-letter disclosure with the
  practice aid Q&A [CFODIVE-AICPAPA-2026] -> `-24`; supervision and file documentation -> `-17`, `-19`, `-20`, `-23`;
  RSM Ask Luca -> `-12`; tool certification (FRC) -> `-01` to `-09`.

**acceptance-independence**
- AI-related non-attest services for attest clients [JOFA-ETHICSAI-2026]; PEEC APS drafts and attest-client
  investment ban [JOFA-PEEC-2026]; engagement-letter drafting at Sam Brown CPA (owner's estimate of half an hour to an
  hour saved per letter) [TR-SAMBROWN-2026] -> `-08`.

**controls-testing**
- Walkthrough to draft process documentation and risk-and-control matrix (Accountancy Europe illustration;
  confidentiality of recordings flagged) [ACCTEU-GENAI-2026] -> `-01`.
- Internal audit: Gartner webinar poll of 743 audit professionals, 93% some AI use, 38% an AI strategy (Going Concern;
  sample may lean to enthusiasts) [GOINGCONCERN-2026-08-11 in the discourse file].

**soc-attestation and assurance-over-ai**
- AICPA and AIUC joint SOC 2 plus AIUC-1 engagement, 19 Oct 2026 [AICPA-AIUC-2026]; AICPA peer-reviewer alert on SOC 2
  platforms [JOFA-PEER-2026]; ethics risks with tool providers [JOFA-SOCETH-2026]; Baker Tilly expanded Fieldguide use
  across SOC, PCI, HITRUST, ISO, FedRAMP, SOX and internal audit, 2026-05-27 (search-only) [BAKERTILLY-FIELDGUIDE-2026].

**benefit-plans (benefit-plan audits)**
- DAS EBP inside the Citrin, Withum, EisnerAmper and PKF suites; EBSA 2023 study: 30% of sampled plan audits (2020 form
  year) with major deficiencies, link between plan-audit volume and quality, EBPAQC members lower deficiency rate, and
  peer review did not help identify deficient audits [EBSA-AUDITQ-2023]; a MECPA open-text respondent named Autire for
  EBP audits and a limited-licence ChatGPT pilot (anecdotal) [MECPA-TECHSURVEY-2025]; CalCPA session on AI in plan audits.

**nonprofit-government**
- PB&H single-audit Excel agents; three nonprofit-focused firms; Guided Assurance Single Audit with OMB Compliance
  Supplement content [TR-GAFEATURES-2026]; Yellow Book QM dates [GAO-YBFAQ-2025]; GAQC AI watch item [GAQC-DEV-2026].

**Tax archetype**
- OPR Alert 2026-19 and the section 7216 consent question [IRS-OPR-2026; CPAPA-7216-2026 in the inputs = CPAPA-SETTLE-2026
  elsewhere]; Ready to Advise at a small firm and Blue J at a seven-person firm [TR-SAMBROWN-2026; JOFA-REALLIFE-2026] -> research-advisory.

**Future accounting and client advisory archetype**
- SSARS 27 and statements prepared within advisory work [CPACOM-SSARS27-2025]; bookkeeping and close AI
  [JOFA-REALLIFE-2026]; Choi and Xie field data from 79 small and mid-sized firms on one platform [STANFORD-CHOIXIE-2025].

**Archetype files**
- economics.md and disruption.md: FERF value-perception finding and fee episodes [FEIDAILY-FERF-2026]; Current
  (formerly Crete), Thrive-backed roll-up [CURRENT-2026]; PE and APS ownership.
- workforce.md: ADP payroll data showing employment of 22-25 year olds in AI-exposed occupations 19% below trend
  (economy-wide) [STANFORD-CANARIES-2026]; FEDYK-2022 employment effects.
- value-chain.md section 4 (data acquisition): -12 and -13 belong to that gap.

**Items routed to private-company from other wave 6 files:** nonprofit-government (Citrin and PKF DAS adoption;
Caseware Pioneer Program agents) and widen-assurance (Citrin and PKF DAS adoption; peer-review data by engagement type)
are used in -01, -05 and module §5. benefit-plans, multistate-private and widen-tax routed nothing here.

## 8. Suggested improvements to the briefs

1. **Ship a URL-to-key register with each brief.** The same document had up to five keys across the repo (JofA ethics
   article), CASEWARE-VERITY-2026 means two different documents, and OSCPA meant two states. A generated register
   (URL -> existing key) would remove most normalisation work.
2. **Tell parallel researchers who owns what.** Seven entries (17%) duplicated entries that sibling wave 6 modules
   (nonprofit-government, quality-management widening) or existing modules already held. Pre-assign known overlaps
   (single audits, SQMS, staff-built agents, engagement letters) in each brief.
3. **Cap D ideas that restate existing entries.** Five of the governance file's six D entries were restatements of
   quality-management or acceptance-independence entries at small-firm scale; ask for the mid-market difference only.
4. **Ask researchers to apply the ladder worked examples** and to state the firm type in a fixed form in `notes`
   (two ladder re-ratings; firm type was missing or inconsistent in several entries).
5. **Clarify grade A for independent studies of a named firm's staff** (Beever and Struthers): perception surveys run by
   an academic team are not obviously "a figure the named organization reports as measured".
6. **Let thin modules record a reason for missing the 50% A/B target** in the archetype index instead of a validator
   warning, so synthesis is not pushed to over-grade vendor case studies.
