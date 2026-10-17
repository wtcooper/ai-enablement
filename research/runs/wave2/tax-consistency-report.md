# Tax consistency pass: report

Date: 2026-10-17. Scope: the 8 module files (`modules/*.md`) and 8 use-case files (`use-cases/*.yaml`) under
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/`. I did not touch the
archetype-level files (ARCHETYPE.md, guardrails.md and the rest) or the archetypes index. I did not change what any
source says, I changed no evidence grade, and I deleted no entry. A script compared every id and grade with commit
24e1538 (before this pass): all 183 entries are still there with the same grades.

Result: `python3 scripts/validate.py` reports 0 errors. The 17 warnings are all the existing evidence-target
warnings (8 tax, 7 assurance, 2 security). Module lengths: compliance-corporate 270, compliance-individual-business 297,
controversy 247, data-technology 293, indirect-tax 300, provision-pillar-two 268, research-advisory 271,
transfer-pricing 255. All have a table of contents. Every YAML file loads.

Note on commits: snapshot commits (b82768c, 73887ce, eb29095) picked up some of my in-progress edits. The working tree
holds the final state.

## 1. Build-process references removed

**YAML notes, automated pass (99 entries).** I removed the leading "Merged from practice-NN, discourse-NN and
governance-NN" or "From governance-NN" sentence: compliance-corporate 20, compliance-individual-business 16,
controversy 19, data-technology 22, research-advisory 19, transfer-pricing 3. Where that sentence also held a real
fact, I put the fact back in plain words: ci-01 (what the parts are and which are ideas), ci-04 (Black Ore is in
`tax-compliance-individual-business-05`), co-15 (HMRC caseworker tools are in `tax-controversy-21`), ra-23 (why the
ladder is delegate), tp-10 (the multi-agent version is `tax-transfer-pricing-11`), tp-14 (why it stays at augment).

**YAML notes and fields fixed by hand** (about 110 sentences):
- Grade and ladder history: "Graded B at verification (was A)" became "Graded B, not A" (ra-01, -02, -09) or
  "Graded B" (co-23). "Verification lowered the grade from B to C" became "Graded C, not B" (cc-18). "the governance
  angle graded this A; the synthesis grades it C" became "Graded C because" (ra-03). Angle disagreements on ladder,
  scope or grade were rewritten as the decision and its reason: cc-07, -10, -24; ci-04; dt-07, -22; it-02, -08, -17;
  ra-02; tp-06, -13, -22. The grades are unchanged.
- tp-09 said "Grade A rests on..." and then "Regraded B"; it now says "Grade B rests on..." and "Not graded A because
  no outcome is measured". The grade (B) is unchanged.
- "Verification:", "Verification (2026-10-17):" and "Verification removed..." notes became plain facts: cc-01, -09,
  -10; ci-08, -24; co-22 (the Axios read is now described as "an earlier read through a text mirror, not re-checked").
- "landscape", "deep dive", "researcher", "the scan", "the inputs", "discourse file" and similar: cc-05, -08; ci-09,
  -11, -15, -17, -19, -20, -21, -22, -24; co-01, -02, -13, -16, -23; dt-18, -22; it-01, -09, -15, -20; ra-06, -10,
  -11, -14, -15, -17, -18, -19; tp-01, -03, -05, -07, -08, -11, -15, -16, -17, -18, -20; tp-14 ("Announced two days
  before the scan" became "Announced on 15 October 2026; launch planned for December 2026", the source's date).
- "Routed to X" notes became the id of the entry that holds the item, or "outside this module": cc-06, -11, -13;
  co-16; dt-02, -10; it-01; ra-10, -14, -19; tp-12, -18, -19. tp-12 and tp-18 named an "international-pillar-two"
  module that does not exist; tp-12 now points to provision-pillar-two and tp-18 says the UN item is outside the module.
- Locators: "(routed from the ... deep dive)" removed from 9 source locators (ci-06, -08, -12, -17; ra-01, -03 x2,
  -06, -19); "(opened via text mirror in the landscape scan" became "(opened via a text mirror" (co-12).
- List items: ra-15 "(governance-angle search)" removed; ra-19 "the governance angle counted 25 rows" became "25 rows
  are tagged tax"; co-08 "as counted by the research-advisory deep dive" became "counted from the database"; co-10
  role_evolution now points to the archetype's workforce and economics files instead of "the landscape scan".

**YAML file headers rewritten** for all 8 files to a short description, "Sources checked 2026-10-17", the evidence
caveat and overlaps by full id. Removed: "Merged/Synthesised from three wave-2 deep dives", `research/runs/...` paths,
"see the synthesis report", "verification report", "candidates in, 22 out", the lists of the old keys each input
file used, and "final ids for those modules were not yet published". The indirect-tax header said three-way
reconciliation was "left to tax-data-technology (not yet synthesised)"; it now names `tax-data-technology-16` and
`-09`.

**Modules:** module stamps normalised to "Sources checked 2026-10-17" (6 modules said "Last reviewed";
compliance-corporate also said "Sources re-verified"). Removed: "(opened by the deep-dive researchers)"
(compliance-individual-business §10), "(opened by the wave 2 researchers unless noted)" (indirect-tax §10), "full
details in the wave-2 research files" (provision §10, which now gives each key's publisher, title, date and URL),
"(routed from indirect-tax)" (transfer-pricing §10), "Sibling modules (final ids not yet published at this
synthesis)" (research-advisory §3, now a list of full ids), "conferences after the scan date" (research-advisory §8),
"the capacity asymmetry the discourse describes" (controversy §4), "(not retrieved by the research)" and "Assist
evidence was merged into augment entries" (indirect-tax), "quotation not re-verified" (controversy §7). Kept as
ordinary usage: "second-wave jurisdictions" (Pillar Two), "verification" as a control, "researchers" meaning
academic authors, "routed" for exceptions sent to people, "Riding the wave" (a Deloitte title).

## 2. Source keys

Before the pass, 441 distinct keys were used across the 8 YAML files; now there are 431. Each document now has one
key, and every record of that key has the same title, publisher, type, URL and date (216 source records rewritten). A
script check finds no key with differing metadata and no URL under two keys.

**Same document, two or three keys (merged):** EY-BTAX-2025 into BTAX-EYGRIP-2025; AICPA-WERFELART-2026 into
TAXADVISER-WERFEL-2026; TR-TEIAUDITOR-2026 into TRINST-TEIAUDITOR-2026; HMRC-GENAI-SW-2026 into HMRC-GENAI-2026;
AICPA-FEE-2026 into AICPA-FEES-2026; FONOA-2026-SURVEY into FONOA-2026; MAGESH-HALLUC-2024 into STANFORD-HALLUC-2024;
TPB-AI-2026 and TPB-GS-2026 into TPB-GS55-2026; JOFA-POLICY-2026 into JOFA-AIPOLICY-2026; BLOOMBERG-AFRICA-2026 into
BTAX-AFRICA-2026. In the modules: ARXIV-TAXCALCBENCH-2025 into COLUMN-TAXCALCBENCH-2025 and ARXIV-LAWORDER-2026 into
HAN-LAWORDER-2026 (provision); EU-AIACT into EU-AIACT-2024 (controversy); EC-VIDA-2025 into EC-VIDA-2026
(indirect-tax).

**One key, two documents (split):**
- PCRT-AI-2026 meant three things. It now means only the ICAEW topical guidance page. The ICAEW news item is
  ICAEW-PCRT-2026 (compliance-corporate and compliance-individual-business YAML and modules), and the ATT news item is
  ATT-PCRTAI-2026 (controversy and indirect-tax module source lists).
- AVALARA-AGENTIC-2025: the PR Newswire release (6 Oct 2025) keeps the key; the Accounting Today article (30 Sep 2025)
  in indirect-tax is now ACCTODAY-AVALARA-2025.
- SOVOS-FRANCE-2026: the "three weeks into the mandate" release is SOVOS-FRANCE-2026b (data-technology now matches
  indirect-tax); the go-live release is SOVOS-FRANCE-GOLIVE-2026 (indirect-tax now matches data-technology).
- TR-R2R-2025: the 15 Dec 2025 post keeps the key (compliance-individual-business); the 19 Dec 2025 blog in
  compliance-corporate is now TR-R2RBLOG-2025.

**Metadata choices:** the most common value, or the more specific one where a record was clearly fuller. URLs:
BTAX-HALLUC-2026 and TR-TENSIONS-2025 use the URL that the other form redirects to (checked with one request each).
AICPA-FEES-2026 uses the Tax Adviser copy; research-advisory had cited the Journal of Accountancy copy of the same
AICPA news item under the same slug. Dates: KPMG-DE-2026 2026-05-07 (cc-05's note about citing it by month was
removed), BTAX-ASC740-2026 2026-03-25 and TEI-MIDYEAR-2026 2026-02 (as the provision verification report advised),
BLUEJ-HOME-2026 2026-10-17, OECD-FTA-2025 2025-11-20. Types where records disagreed: PWC-MEGNA-2025 press (CFO.com
interview), TAXCT-CLINCO-2026 press, SALA-TAXNOTES-2026 press, TRINST-TEIAUDITOR-2026 conference, PCRT-AI-2026 and
ATT-PCRTAI-2026 professional-body, DELOITTE-LU-2025 survey, KPMG-ANTHROPIC-2026 firm.

**Module source lists:** every bracketed key in each module resolves to its own YAML or its own §10 (script check, all
8 modules). Each module §10 entry for a key that is also in a YAML file now matches that YAML's metadata (provision
KPMG-DE-2026 date, controversy ATT-PCRTAI-2026 title, indirect-tax EC-VIDA-2026).

## 3. Cross-module overlaps

No entry was an exact duplicate, so none was deleted. Where two entries describe the same change, the thinner one now
names the fuller one by full id in its notes, and the module text does the same where the entry is described:
- compliance-corporate had no full-id references (its notes named modules only). It now points to:
  `tax-compliance-individual-business-02` (K-1 mapping, from -02), `-06` (pass-through returns, from -06), `-12`
  (return review, from -03), `-07` (pass-through mapping, from -01); `tax-research-advisory-01` (-11), `-19` (-19),
  `-07` (-20), `-25` (-16), `-23` and `tax-indirect-tax-09`, `tax-provision-pillar-two-08`,
  `tax-data-technology-15` (-12); `tax-data-technology-07` (-17), `-09` (-10), `-22` (-07), `-02` (-01), `-12` and
  `-16` (-24), `-24` (-15); `tax-controversy-04`, `-13` and `tax-transfer-pricing-15` (-13).
- Others: ra-12 and cc-22 to the deterministic-engine family; ra-20 to ra-19 and co-08; ra-23 to cc-12 and it-09;
  ra-24 to cc-08; it-12 to dt-13 (fuller); it-16 to dt-18 (fuller); it-08 now names dt-14 instead of "research
  entries"; pp-03 to dt-02 and back; co-07 to tp-16; co-12 to dt-12 and dt-13; dt-03 to it-07; dt-16 to it-11;
  tp-02 to ra-06; tp-04 to dt-01; ci-07 to cc-01.
- Bad reference fixed: co-15 cited `tax-transfer-pricing-23`, which does not exist; it now cites
  `tax-transfer-pricing-15`.
- Bare short forms after a full id (`tax-transfer-pricing-08`, `-16`; `tax-research-advisory-19`, `-20`;
  `tax-controversy-13`, `-15`; `tax-controversy-01`/`-02`) were expanded to full ids in the modules. Module headers
  now say "other modules' ids are in full". A script check finds every `tax-<module>-NN` reference in modules and
  YAML resolves (the only non-matches are URL slugs).

## 4. Routed items

I read the routed-out lists in all 8 synthesis reports. Most items were already in their target modules. Added where
missing and supported by a source already in the tax files:

| Item (routed from) | Target | Placed in |
|---|---|---|
| Law and Order neuro-symbolic result (provision) | compliance-individual-business | §5 accuracy benchmarks and §10 (HAN-LAWORDER-2026, from compliance-corporate YAML) |
| Orbitax MCP connections (provision; transfer-pricing) | data-technology | §3 agent access and §10 (ORBITAX-XATBOT-2026, from provision YAML) |
| KPMG indirect-tax data quality and e-invoicing ownership (indirect-tax) | data-technology | §3 data foundation and real-time reporting, §10 (KPMG-INDIRECT-2026) |
| TP data governance as the constraint (transfer-pricing) | data-technology | §3 data foundation, §10 (ITR-NEXDIGM-2026, KPMG-GR-2026) |
| Savant and Oxford Industries (provision) | indirect-tax | §3, as a pointer to `tax-compliance-corporate-10` (no new facts) |
| VAT and customs parts of cross-tax review (transfer-pricing) | indirect-tax | §3, pointer to `tax-transfer-pricing-11` |
| Pillar Two interplay with operational TP | transfer-pricing / provision | tp-12 note now points to the provision module instead of a module that does not exist |

Not added, because no source in the files supports it: "Tax Skills in Orbitax" for transfer pricing (the XatBot
release does not mention TP); the EY sales-and-use lookback (EY-COMPL-2026 is not in any file); the German head of
tax on TP files (BTAX-EYTFO-2026 as cited says nothing about TP); NormBench and TaxPraBen (titles only); BTAX-LEE-2025,
AIBIDIA-PRIORITIES-2026 and AIBIDIA-SERIESB-2025 (not in any file). The IRS "Zero Paper" mail tool and "IaaP
Accelerator" bounced between modules; co-16 now says they are tax-authority intake or IT and are not entries in any
module.

## 5. Professional responsibility

Every module §6 now links to `../guardrails.md` for the shared conduct rules (IRS OPR Alert 2026-19 and Circular
230, section 7216, the UK PCRT guidance, Australia's TPB guidance, AICPA SSTS 1.4, *Clinco*). The duplicated lists
were cut and only the points specific to each module were kept:
- compliance-corporate: OPR addresses practitioners, not in-house teams; preparer reliance; Section G; HMRC software.
- compliance-individual-business: the fee dispute, section 10.34(a), the open question of how 7216 applies to an LLM
  vendor, OPR's merger with the Return Preparer Office, IRS operating rules (Pub 1345, Form 8867, Pubs 4557 and 5708),
  HMRC software, and that a signed engagement letter can give the TPB's client permission.
- controversy: treat AI text as a draft and use enterprise tools only; the fee clarification; courts, evidence and
  authority governance kept in full.
- data-technology: OPR is not addressed to in-house departments as such.
- indirect-tax: OPR does not cover state sales tax or VAT; PCRT applies to UK VAT work; *Rafique* kept.
- provision-pillar-two: a new pointer line; the accounting and filing rules are unchanged.
- research-advisory: written-advice and reasonable-cause points, verification expectations, *Elden* and *Zzaman*,
  HMRC software, client disclosure and fees.
- transfer-pricing: a pointer replaces the conduct bullet; the IRS LB&I, section 6662(e), courts and OECD points are
  unchanged.

## 6. Wording

- "Measured" used for entries graded B or lower was reworded: cc-22 ("published research results", "the system they
  tested"), co-23 ("any published figure"), ra-03 ("the only figure is a benchmark"), ra-04 ("the benchmark
  weakness"), dt-09 risk line ("the process behind the vendor figures"); modules: ci §3 Second Look ("the figure is for
  the service"), controversy header ("almost every figure"), data-technology §3 Peru ("independent figure"),
  indirect-tax header and §5 heading (the synthetic agent pilot behind idea `#22` is no longer grouped as a measured
  result).
- Terms of art explained at first use in each module: OPR, Circular 230, section 7216, PCRT, TPB and SSTS wherever
  they appear; E&P, QREs and FIN 48 (compliance-corporate); K-1 (compliance-individual-business); SPA
  (research-advisory); ADR, TAS, FS2026 and power of attorney (controversy); "PE firms" written as private equity
  firms.

## 7. Files changed

Modules: all 8. Use cases: all 8.
