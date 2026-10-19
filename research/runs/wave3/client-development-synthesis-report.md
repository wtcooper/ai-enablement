# Synthesis report: professional-services / client-development

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-client-development-practice.md`, `ps-client-development-discourse.md`,
  `ps-client-development-governance.md`, plus the "Routed to other modules" sections of every other `ps-*.md` file in
  `research/runs/wave3/` (items routed to client-development or client-relationship-development).
- **Outputs:** `plugins/.../archetypes/professional-services/modules/client-development.md` (300 lines, contents list at
  top) and `plugins/.../archetypes/professional-services/use-cases/client-development.yaml` (22 entries).
- **Validator:** `python3 scripts/validate.py` reports 0 errors for these files; 22 entries, 50% graded A/B (meets the
  15-25 and 50% targets, just). A script check confirmed every source key cited in the module is in the YAML or in the
  module's Sources list (11 keys marked *), every outcome `source_ref` is in its entry's sources, and every inline key in
  an entry is in that entry's sources.
- No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed from other modules | Total |
|---|---|---|---|---|---|
| Candidates in | 16 (0 A, 8 B, 7 C, 1 D) | 17 (0 A, 2 B, 12 C, 3 D) | 16 (0 A, 3 B, 10 C, 3 D) | evidence items only (no entries) | 49 |
| Out | | | | | **22 (0 A, 11 B, 10 C, 1 D)** |

No candidate was dropped; each was merged into an output entry (one, practice-05, was split across two).

## 2. Duplicates merged

P = practice, D = discourse, G = governance.

| Out | Merged from | Grade decision |
|---|---|---|
| 01 Zero-entry capture into the CRM (Schneider Downs, KSM, LBMC, Grassi, Howes Percival) | P01, D01 (capture), G01 (privacy, accuracy) | B (P01); D01 and G01 were C |
| 02 Relationship maps, warm paths, succession (Thomson Snell & Passmore) | P02, G01 (mapping) | B (P02) |
| 03 Client-health scores and at-risk alerts (Howes Percival) | P04, D02, G03 (alert part) | B (P04) |
| 04 Key-account plans and cross-sell lists, with CPA independence checks | P09, D03, D08, D11, G02 | C |
| 05 Opportunity scouting (Akin Gump, Quinn Emanuel) | P06 | B kept |
| 06 Pre-meeting briefs and client intelligence from matters | P03, D04, D07, G07 | B (P03) |
| 07 BD assistants: general-purpose chatbots to grounded assistants (Introhive MCP, Celeste Q&A) | G05, P05 (Q&A part), D01 (MCP part) | C |
| 08 Nudges and drafted client notes and alerts (Activator, Harvey) | P07, P08, D05, D09, G03 (nudge part) | C |
| 09 Call and meeting summaries and coaching (Certinia) | G06 | C |
| 10 Agentic origination and BD playbooks (Celeste) | D06, P05 (playbook part) | C; ladder delegate describes the product claim |
| 11 Idea: agent-run outbound sequences | G14 | D, labelled idea |
| 12 AI claims in marketing and thought leadership | G12 | B (ILTA measured prevalence) |
| 13 Website intake chatbots | G13 | C |
| 14 Partner-led AI value conversations | D12 (C), G08 (B) | B (G08: named firms and client, TRI frequency data) |
| 15 Matter-level evidence of AI use shown to clients (Legora-Laurel) | P14 (C), D13 (D), G10 (D) | C (announced tooling); reporting to clients is an idea |
| 16 AI terms in engagement letters | G11 | B (ILTA measured prevalence) |
| 17 In-house AI addendum to OCGs | G16 | C |
| 18 AI-analysed client listening (Shoosmiths), incl. AI-service feedback and in-house variant | P15 (C), P16 (D), D10 (C), G15 (D) | C; the two D parts stay labelled ideas in notes |
| 19 Revenue attribution of BD | P10, G04 | C |
| 20 Co-creation with key clients (Parker Poe, Fasken; GSK) | P11 (B), D14 (B), G09 (C) | B |
| 21 Firm-built tools and portals offered to clients (Debevoise, Cooley, A&O Shearman, Legora Portal) | P12 (B), D15 (B), D16 (D) | B; shared-workspace part labelled idea |
| 22 Client AI enablement roles and AI advisory (Latham & Watkins; accounting) | P13 (B), D17 (D) | B (opened Latham job description); accounting part is an idea |

**No grade was raised by merging.** Each merged entry carries the highest grade one of its inputs already had for a
named deployment. Overlaps with other modules are cross-referenced, not duplicated: scoping-pricing-07, -09, -10, -11,
-23; work-production-20, -21, -25; assurance-acceptance-independence-11 and -15; tax-compliance-individual-business-15;
tax-research-advisory-24.

**Source-key canonicalisation**

| Canonical key | Input keys or variants |
|---|---|
| BLOOMBERG-AICOST-2026 | BLOOMBERGLAW-MYSTERY-2026 (discourse); same URL; matches scoping-pricing |
| TRI-INTERDEP-2026 | TRI-INTERDEPENDENT-2026 (practice, discourse); matches scoping-pricing |
| SJ-LFMC-2026 | SJ-CLIENTS-2026 (discourse), LFMC-SJ-2026 (governance); date 2026-04-10 (governance had 2026-04-09); typed press |
| ACCEVERLAW-2025 | EVERLAW-ACC-PR-2025 (governance). Same press release; this file keeps the Business Wire reprint URL governance read, while scoping-pricing uses an everlaw.com.au URL. Harmonise the URL |
| SOURCE-PRECISION-2026 (module only) | SOURCE-INSIGHTS-2026 (practice, landscape) for the same article |
| CALBAR-GENAI-2026 | typed regulator, date 2026-05 (governance: professional-body, 2026-05-14), as in other module files |
| PARKERPOE-LAWSITES-2026 | typed firm (practice typed press): the firm's own release carried by LawSites |

**Provenance normalised.** Discourse marked TR-FOP-2026, TRI-STANDOUT-2026 and TR-AIPS-2026 figures `independent`;
practice and governance marked them `vendor-published` because Thomson Reuters sells AI products. All are
`vendor-published` here. ILTA figures stay `independent`. Discourse outcomes with `provenance: n/a` and
`source_ref: n/a` were rewritten as "none published" with a real source.

**Unresolved dates and keys:** TR-FOP-2026 is dated `2026` (practice and discourse: page shows no date; governance:
2026-06-22 from a companion article; scoping-pricing and talent-learning use 2026-09 or 2026). ILTA-TECHSURVEY-2026 is
typed `survey` here and `professional-body` in scoping-pricing. JOA-ETHICS-2026 (Journal of Accountancy, `/issues/`
URL) appears to be the same article as assurance's JOFA-ETHAI-2026 (`/news/` URL). Undated vendor pages carry the read
month `2026-10`.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 1 (16) | 3 (14, 17, 20) | 1 (22) | 5 |
| augment | 8 (02, 03, 06, 07, 08, 09, 12, 18) | 4 (04, 05, 15, 19) | 1 (21) | 13 |
| automate | 1 (13) | 1 (01) | 0 | 2 |
| delegate | 0 | 2 (10, 11) | 0 | 2 |
| **Total** | 10 | 10 | 2 | 22 |

- **Automate** has one in-production entry (01, B) and one with no named firm (13, C).
- **Delegate** rests on a vendor announcement (10, C) and an idea (11, D). No firm runs client development through an
  agent; no delegate entry at step or model scope exists, and none was invented.
- **Model** scope: two B entries (21, 22) with no usage, revenue or retention figures.

## 4. Grade mix and maturity

- Grades: A 0, B 11, C 10, D 1. **No A is possible:** no named organisation reports a measured outcome for any
  client-development use. Every outcome figure is vendor-published or a survey perception, except ILTA prevalence data
  (independent) and qualitative firm statements (Akin Gump, Parker Poe; self-reported).
- B grades rest on named deployments without measurement (01-03, 05, 06, 20-22) or on ILTA's measured prevalence of a
  practice (12, 16) and TRI's measured conversation frequency with named firms and client (14).
- Maturity: in-production 10, piloting 1, announced 7, emerging 4.
- Firm kinds: law dominates; accounting appears through Introhive and Intapp stories, Journal of Accountancy, Intuit and
  Woodard; consulting only through ICMCI, Certinia, Source Global Research and Stanford. In-house items: 17 (entry),
  parts of 14, 15, 18, 20, 21 (tagged in notes).

## 5. Items routed from other modules

| Item | From | Used in |
|---|---|---|
| ILTACON "two-way door" reversibility test; Introhive speaker's partner-departure agent example (TRI-AGENTIC-2026) | delivery-management discourse | 03, 10, 11; module §6, §8 |
| RSGI: 61% of law firms say they raised Harvey efficiencies vs 4% of in-house teams approached (LEGALIT-RSGI-2026) | work-production practice | 14; module §5, §9 |
| BigHand: 35% name partner discomfort as top barrier; 56% see more client demand (BIGHAND-LF-2026) | scoping-pricing discourse | 14; module §5 |
| 85% of law firms and 75% of legal departments not collecting AI ROI data (TRI-GREATDISCONNECT-2026) | firm-finance discourse | 15; module §5 |
| Introhive MCP server commercial preview, 2026-04-16 (INTROHIVE-MCP-2026) | pursuit-proposals practice | 07; module §8 |
| Reed Smith says AI-enabled delivery wins work (HARVEY-REEDSMITH-2026) | quality-review and work-production practice | module §9 only (*) |
| Corporate legal clients say judgment, transparency and speed separate firms (TRI-AIFORUM-2026, in-house) | talent-learning discourse | module §8 only (*) |
| Litera BD intelligence from siloed firm data (LAWSITES-ILTACON4-2026) | knowledge-management discourse | module §8 only (*) |
| CMBDO Forum 2027 sessions on AI story in pitches and AI-driven discovery (TRI-CMBDO34-2027, scheduled) | pursuit-proposals discourse | module §8, labelled scheduled (*) |
| TR-FOP-2026 client figures; TRI-STANDOUT-2026 partner figures | firm-finance, quality-review, scoping-pricing, talent-learning, work-production | already in the module's inputs |
| Kantata: RFP buyers ask how the firm uses AI to cut cost (UNITEAI-KANTATA-2026) | staffing-resourcing discourse | Not used: pitch-stage question; belongs to pursuit-proposals |
| LMA26 session titles and Passle episodes on AI search visibility and cross-sell; Projectworks "over half of proposals are for existing clients" | pursuit-proposals discourse | Not used: show notes or an unsourced vendor claim |
| Paravo and Introhive items in the LawSites feed | firm-finance practice | Not used: not read by the routing file |

## 6. Routed out from client-development inputs (for the target modules' synthesis)

- **pursuit-proposals:** Lynn Pinker Hurst & Schwegmann answered an urgent prospect request in under 48 hours with
  Harvey and won the work (HARVEY-LPHS-2025; HARVEY-BD-2026); Harvey mining prior pitches for RFP drafting
  (HARVEY-BD-2026); Latham role supporting panels, pitches and RFPs (LATHAM-INNOVATIONATTY-2026); Source buyer
  segmentation, 60% of enterprise tech buyers citing data quality and governance as the main bottleneck
  (SOURCE-INSIGHTS-2026 / SOURCE-PRECISION-2026); clients adding AI clauses to RFPs (LAWFUEL-2025); Florida and ICMCI
  limits on AI claims in proposals and credentials (FLBAR-OP241-2024; ICMCI-AICODE-2026).
- **acceptance-risk:** Celeste for intake and conflicts at BakerHostetler, lateral hiring (LAWSITES-CELESTE-2026);
  Practus/Auxana Intake and Conflicts (INTAPP-PRACTUS-2026); Baker McKenzie Client AI Risk Lead
  (BAKERMCKENZIE-CLIENTAIRISK-2026, search-only); conflict-system entry of chatbot prospects (OSB-FO-2026-208,
  section III.C); Harvey and Legora intake products (landscape).
- **billing-collections:** Legora-Laurel time capture (LEGORA-LAUREL-2026); line-item AI transparency and California
  rule 1.5 cost pass-through (TRI-LEGALWEEK-2026; CALBAR-GENAI-2026, p. 8; LOUBAR-2025).
- **scoping-pricing:** AI fee discussions and refusals to pay for AI-done work (TRI-LEGALWEEK-2026); Kopka Law KPI
  pricing (TRI-KOPKA-2026); CLOC "Great Pricing Reset" (STENO-CLOC-2026); Citi: three-quarters of 57 firms expect AI
  to affect the billable hour by 2028 (BLOOMBERG-AICOST-2026); Saul Ewing view that clients are not driving AFAs
  (TRI-LEGALWEEK-CRISIS-2026); productised tools and revenue-sharing licences (ABAJ-SHARE-2026); Stanford framework
  (STANFORD-DEL-2026).
- **firm-finance:** 18% collect AI ROI metrics (TR-AIPS-2026); ROI ranked last among AI investment drivers
  (LITERA-LAWSITES-2026); demand growth against savings (BLOOMBERG-AICOST-2026); rate growth and AI-bubble warning
  (TRI-SOTLM-2026); private-equity pressure on partners for pipeline (INTROHIVE-LAWSITES-2026).
- **talent-learning:** one-to-one partner AI training (TRI-CMBDO-2026); associate pyramid as work moves in-house
  (TRI-LEGALWEEK-CRISIS-2026); stand-out lawyers' low weighting of change leadership (TRI-STANDOUT-2026); 24% of
  professionals with an AI value gap considering leaving (TR-FOP-2026).
- **quality-review:** KPMG report pulled over apparent hallucinations (HN-KPMG-2026, community thread); Deloitte
  Australia refund (CTV-DELOITTE-2025); NBER patent-drafting trial (NBER-AUTOR-2026); accuracy as top barrier for
  limited adopters (TRI-STANDOUT-2026).
- **knowledge-management:** Latham's client AI capability catalogue (LATHAM-INNOVATIONATTY-2026); making firm knowledge
  AI-accessible (LAWPUNX-2025); "legal memory" ownership (BLOOMBERGLAW-GCXAI-2026).
- **In-house flag (not a module):** TRI-VISIBILITY-2026, AL-INHOUSE-2026, STENO-CLOC-2026, TRI-INTERDEP-2026,
  BLOOMBERGLAW-GCXAI-2026.

## 7. Judgment calls and corrections

- Laing O'Rourke (a construction company) is used only for a guardrail quote, not as a professional-services deployment.
  The Bridgenext figure (financial-services data firm) is labelled adjacent.
- Introhive's "up to 90% of firms fail to grow key accounts" claim moved from outcomes to risks (no source or method).
- Unverified pay ranges from search-only job postings (practice-13) were not carried over.
- The practice file's concern that activity leaderboards "may be read as surveillance" had no source; it is restated as
  "not addressed in the sources".
- The landscape file attributes the ENGAGE 2026 "AI conversations and integration" session to an AICPA speaker; the
  discourse file found the presenters are from Karbon, GW CPA and Weaver & Tidwell. The landscape entry should be
  corrected.

## 8. Gaps

- **No measured outcome anywhere:** no revenue, retention, win-rate, accuracy, override or parallel-run figure for
  relationship intelligence, briefs, alerts, outreach or client-facing AI. Independent evidence is adjacent only (retail
  sales experiments, patent-drafting trial).
- **Consulting:** no consulting firm's own AI-assisted account management, account planning or client feedback was found;
  Big Four and strategy-firm pages were not reached.
- **Accounting:** evidence is vendor case studies and sponsored surveys; AICPA pages, ENGAGE recordings and the VSCPA
  summary were not reachable.
- **Delegate and automate:** no firm runs autonomous outreach or BD agents; intake chatbots are described by bar bodies,
  not named firms.
- **Privacy law** on firm-wide email-metadata capture rests on a vendor statement; no regulator analysis found.
- **Not opened or paywalled:** Law.com originals (Cooley, Debevoise, A&O Shearman), The Lawyer on Akin, Introhive's full
  partner report and Forrester TEI study, ClearlyRated buyer report, TRI 2026 AI in Professional Services Report (read
  by discourse only), podcast audio (show notes only).

## 9. Suggested improvements to the briefs

1. **Ship a shared source registry per wave** (key, title, URL, date, type). This module had to reconcile three keys for
   one Solicitors Journal article and conflicting dates and types for TR-FOP-2026, ILTA and the ACC-Everlaw release;
   other synthesis files made different choices.
2. **State the provenance rule for publisher-vendors.** Say explicitly that Thomson Reuters Institute, Introhive and
   similar survey publishers that sell AI are `vendor-published`, so angle agents stop splitting them.
3. **Forbid `n/a` in outcome fields.** Require "none published" with a real `source_ref` and a vocabulary provenance.
4. **Give consulting and accounting their own search budget.** The practice angle ran out of searches before the
   accounting and consulting queries; the module is skewed to law as a result.
5. **Fix module boundaries for the AI value conversation.** Client-development, scoping-pricing and billing-collections
   all collected the same Legalweek and Stand-out material. Name one owner for the conversation (client-development),
   one for fee design (scoping-pricing) and one for invoice mechanics (billing-collections).
6. **Require a source row for every routed key.** Some routing notes (Paravo, LMA, Passle) name items without a read
   source, so the target module cannot use them.
7. **Ask governance angles to name deployments when they can.** Governance entries graded only the rules, so merges
   relied on practice for named firms; one line per entry pointing to the practice id would speed merging.
