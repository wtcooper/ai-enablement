# Synthesis report: tax / controversy

Prepared 2026-10-17. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/modules/controversy.md` (248 lines)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/tax/use-cases/controversy.yaml` (25 entries)

`scripts/validate.py`: 0 errors; one warning for this file (40% A/B, below the 50% target). Not inflated, per the wave note.

## Counts in and out

| Input | Candidates |
|---|---|
| tax-controversy-practice.md | 20 (1 A, 8 B, 10 C, 1 D) |
| tax-controversy-discourse.md | 18 (1 A, 6 B, 5 C, 6 D) |
| tax-controversy-governance.md | 19 (6 A, 4 B, 2 C, 7 D) |
| landscape-tax.md | 0 candidates (context, leads, frontier) |
| Routed from other tax deep dives | about 20 items; folded into existing entries as sources, none made a new entry |
| **Total in** | **57 candidates** |
| **Out** | **25 entries** (12 practitioner or in-house side, 13 tax-authority side) |

## Duplicates merged

- Notice triage `#01`: practice-01, discourse-01 (intake part), governance-16 (triage part).
- Notice drafting `#02`: practice-02, discourse-01 (drafting part), governance-16 (drafting part); plus Blue J Tax Writing (routed).
- Pre-filing exposure review `#04`: practice-04, discourse-02, governance-17.
- Citation verification `#08`: practice-08, discourse-03, discourse-16 (pro se filers), governance-14; plus UK tribunal cases, Charlotin database, Riddle Aggregates, Buckeye Trust (routed).
- Risk register `#11`: discourse-15, governance-15.
- IRS selection `#13`: practice-09, discourse-05, governance-01; plus IRS distributor-loss algorithms (routed).
- Selection-model monitoring and disparity testing `#14`: governance-02, governance-03.
- Other authorities' risk targeting `#15`: discourse-10, discourse-12, governance-09 (targeting), governance-13, discourse-18 (Austria); plus South Carolina, Tax Notes state survey, SEATA, Hungary, HMRC ICTS, South Africa/Nigeria (routed).
- Fraud screening `#16`: practice-13, governance-06.
- Amended returns `#17`: practice-12, discourse-07, governance-05.
- Bots `#18`: discourse-08, governance-04, discourse-18 (Singapore, Korea).
- ATO filing prompts `#19`: practice-15, governance-11, discourse-18 (ATO).
- Service-staff agent assist `#20`: practice-11, discourse-09, governance-19 (Archie); practice-18, discourse-11 (CDTFA); governance-10 (HMRC); discourse-18 (France).
- Examiner and caseworker assistants `#21`: practice-14 (ATO), practice-19 (TAS drafting), discourse-17, governance-08 (IRS revenue agents), governance-09 (caseworker tools).
- Agentforce `#22`: practice-10, discourse-06, governance-07.
- Agentic case management `#24`: practice-16 (ATO), practice-17, discourse-13 (HMRC); plus CIAT blog (routed).
- Kept single: `#03`, `#05`, `#06`, `#07`, `#09`, `#10`, `#12`, `#23`, `#25`.

Grade conflicts resolved downward or by the vocabulary: IRS selection (A/B/B → B; TIGTA figures redacted, NTA figures not attributed to AI); amended returns (B/B/A → B; one spoken remark, no method); HMRC targeting (B/A → A on the annual report); ATO prompts (B/A/C → A on the OECD primary).

## Coverage

| | step | process | model |
|---|---|---|---|
| assist | 06, 08, 09, 11, 25 | – | 10 |
| augment | 01, 02, 04, 05, 20, 21, 22 | 03, 07, 13, 14, 15, 19, 23 | 12 |
| automate | 16, 17, 18 | – | – |
| delegate | – | 24 | – |

- **Delegate:** only `#24`, announced by authorities (ATO, HMRC), graded C. No practitioner-side delegate evidence; the nearest is Accrual Arc (routed; it sits in `tax-compliance-individual-business-09`).
- **Automate:** authority side only (IRS fraud screens, amended returns, bots). No practitioner automate evidence.
- **Model scope:** two ideas only (`#10` pricing, `#12` preventive controls). No deployed change in service or operating model.
- **Appeals:** one measured item (`#23` Brazil, classification trial) and one announcement (`#22`). No taxpayer-side Appeals or protest AI at all.

## Grade mix

A 4 (15, 18, 19, 23) · B 6 (03, 13, 16, 17, 20, 21) · C 9 · D 6. A/B = 40%. Nine of the ten A/B entries are authority-side; the only practitioner-side B is a 2019 transcript-monitoring practitioner (`#03`). Every practitioner-side figure is vendor-published or a firm survey.

## Gaps

- No named firm or in-house controversy deployment with a measured outcome (error, override, cycle time, fee impact) for notice response, IDR handling, Appeals or litigation drafting.
- No taxpayer-side Appeals, Fast Track or protest AI evidence; no IRS document on Agentforce in Appeals.
- No primary IRS source on revenue-agent GenAI drafting (EisnerAmper only); no Tax Court AI rule; no Circular 230 discipline for AI misuse; no insurer or malpractice-carrier view.
- Primary documents not reached: TIGTA's Sept 2026 AI risk report (403; figures via Accounting Today), HMRC roadmap text, the Khoja hearing record, Axios full text for some researchers, OECD Tax Administration 2025, IMF note, Stanford No. 124.
- Practitioner communities (r/taxpros, TaxProTalk, TEI member sessions) unreachable; TEI annual conference (18-21 Oct 2026) recaps not yet published. Re-check November 2026.
- Unverified commentary excluded: ACCTODAY-2026 claims about GAO findings and TIGTA workforce numbers; EisnerAmper's DIF claim; Cassidy and CleverX vendor claims (pages unreachable).
- Source conflicts noted in the YAML: ATO transparency statement date (Feb vs Jul 2026, year only used); IRM 10.24.1 URL (opened by discourse, 404 for others on a variant URL); EU AI Act recital (59, not 38 as in the landscape); OECD ATO figures (636,000 and AUD 78.9 million in the primary; Grant Thornton rounds them).

## Routed to other modules (from the controversy deep dives)

| Item | Target | Source |
|---|---|---|
| TaxGPT Tax Prep Agent and 'Agent Andrew' return review (vendor claims: 45 minutes saved per 1040; 90% less first-pass prep time) | compliance | TAXGPT-2026 |
| TaxCalcBench (models compute under a third of simplified returns correctly); IRS Zero Paper AI routing; HMRC R&D letter concerns; OPR fee guidance for preparation; Bloomberg Tax Leadership Forum panel | compliance | COLUMN-TAXCALCBENCH-2025; TREAS-AIINV-2026; ICAS-HMRC-2025; IRS-OPR-2026; BTAX-FORUM-2026 |
| ONESOURCE Sales and Use Tax AI (up to 65% less routine reporting time; up to 75% lower audit exposure, vendor claims) | indirect-tax | TR-ONESOURCE-2026 |
| Exactera ExactMatch/ExactReport; IRS LB&I expert-witness and formula remarks; KPMG TP GenAI claims; PwC exam focus areas (TP, financing, economic substance, credits) | transfer-pricing | EXACTERA-2025; IRS-LBI-TP-2026; KPMG-TP-2025; NYSSCPA-PWCWEBCAST-2026 |
| Oxford Industries/Savant TEI session; IRS IaaP Accelerator; TEI themes (silent hallucination, ownership poll, token costs); in-house adoption surveys and Sala's headcount argument | tax-data-technology | SAVANT-TEI-2026; TREAS-AIINV-2026; TEI-TAXTECH-2026; TR-FOP-2026; KPMG-DE-2026; TR-CORPTAX-2025; SALA-TAXNOTES-2026 |
| Hallucinated research and SSTS 1.4; ChatGPT 39-47% correct on tax questions; LLM plus symbolic solver | research-advisory | TAXCT-CLINCO-2026; ANTINOZZI-2024; JHU-TAXREASON-2025 |
| 92% expect a global minimum tax to increase disputes | international-pillar-two (now provision/Pillar Two) | EY-PAPERJAM-2026 |
| OPR Alert 2026-19 and SSTS 1.4 | cross-cutting professional responsibility | IRS-OPR-2026 |

Items routed **to** controversy from other deep dives were picked up as sources in `#02`, `#07`, `#08`, `#13`, `#15` and `#24` (see "Duplicates merged"). Not used: Indian ITAT recall details beyond the digest line, proposed FRE 707 (used in module guardrails only), floridasalestax.com hallucination warning (no controversy-specific content).

## Suggested improvements to the briefs

1. **Split or tag authority-side use cases.** Half this module is tax-authority AI. A field such as `actor: authority | practitioner` (or a separate `tax-authority-ai` module, as the landscape proposed) would stop authority A grades from masking a thin practitioner evidence base.
2. **Give researchers one canonical ref list per archetype before deep dives start.** The three files used three keys for one Bloomberg article, two for the Wolters Kluwer notice page and three for the EY Bloomberg piece.
3. **State a grading rule for spoken or relayed figures** (an executive's remark reported by press; an authority's figure relayed by the OECD). Researchers split A/B on identical evidence.
4. **Share the web-search budget plan.** Two of three researchers ran out before job postings, the Khoja record and the HMRC annual report; the governance researcher then found the HMRC report the discourse researcher could not.
5. **Ask for practitioner-side measurement leads explicitly** (firm case studies, conference recaps, malpractice insurers), and schedule a re-check after TEI Annual and CCH Connections (Oct 2026).
6. **Have routed items carry a one-line fact and full source row**, not only a key, so the receiving synthesis does not need to search other files.
