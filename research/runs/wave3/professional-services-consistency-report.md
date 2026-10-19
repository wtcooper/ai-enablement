# Professional services: consistency report

Prepared 2026-10-19. Scope: the 12 module files and 12 use-case files under
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/`.
Inputs: the 12 synthesis and 12 verification reports, plus the coordinator notes. No other archetype, index or
archetype-level file was edited.

## Summary

| Task | Result |
|---|---|
| Source keys | 13 aliases merged into one key each, plus 1 more alias found (NYC Bar 2024-5). 5 keys that named two or three documents were split. 2 keys renamed because the tax archetype uses them for other documents. Every key now has one title, publisher, type, URL and date in all 12 YAML files (0 conflicting records, down from 29, plus 64 keys whose title or publisher varied). |
| Duplicates | About 50 cross-module pairs reviewed. 1 entry replaced by a cross-reference (`delivery-management-15` merged into `knowledge-management-15`). About 45 other pairs kept, because each module adds something distinct; references now run both ways. |
| Cross-references | 0 broken ids before or after (874 ids checked across 4 archetypes). 39 short ids written out as full ids. Every cross-module reference was read against its target's title, and none points at the wrong entry. |
| Provenance | NBER 35720 is vendor-published everywhere, with the agreed note. 3 more outcome labels were aligned. **No grade changed.** |
| Build words | 203 merge-history sentences removed, plus about 95 other edits in entries, all YAML headers and 10 module lines. |
| Firm type | Added to 12 entries whose notes did not name the kind of organization. |
| Validator | `python3 scripts/validate.py`: **0 errors**, 23 warnings (5 of them professional-services: the A/B share is below target in acceptance-risk, billing-collections, delivery-management, pursuit-proposals and staffing-resourcing). Every module has 300 lines or fewer and has a table of contents. |
| Entry check | Script snapshot before and after: 241 entries before and 240 after. The only entry missing is `delivery-management-15` (task 2). No id, grade, ladder or maturity changed. |

## 1. Source keys

### Aliases merged (one key per document)

| Kept key | Alias removed | Files |
|---|---|---|
| TRI-ONBOARDING-2026 | TRI-ONBOARD-2026 | work-production |
| JOA-TRAINING-2026 | JOFA-LEARN-2026 | knowledge-management |
| TRI-LDEV-2026 | TRI-LAWYERDEV-2026 | scoping-pricing |
| TRI-LEGALWEEK-ASSOC-2026 | TRI-LEGALWEEK-CRISIS-2026 | firm-finance, client-development (module) |
| TRI-DESIGNJUDG-2026 | TRI-JUDGMENT-2026 | work-production |
| CERTINIA-CUSTOMERS-2026 | CERTINIA-PROVING-2026 | billing-collections |
| TXETHICS-OP705-2025 | TXBAR-OP705-2025 | talent-learning |
| AT-PWC-2026 | ATODAY-PWC-2026 | talent-learning |
| AT-AINATIVE-2026 | ATODAY-ASCEND-2026 | talent-learning |
| AL-LAWPUNX-2025 | LAWPUNX-2025 | client-development |
| BLOOMBERGLAW-BILLABLE-2026 | BLAW-ROBB-2026 | scoping-pricing |
| CIVILITY-ABA512-2024 | 2CIVILITY-ABA512-2024 | client-development |
| LAWSOC-AGENTIC-2026 | LAWSOC-AGENTICFUTURE-2026 | knowledge-management |
| NYCBAR-OP2024-5-2024 | NYCBAR-OP2024-5 (landing page of the same opinion) | client-development |

The other aliases on the talent-learning list (TRI-SEYFARTH, TRI-TAX2030, ICAEW-WORRIED, SFN-BIGFOUR, ICO-AIRECRUIT,
NYC-LL144, TRI-TALENT-AI, TRI-GENAI-TALENT, BLAW-FIRSTYEAR, BLOOMBERG-FIRSTYEAR, JOA-LEARN) no longer appear in any file.

### Keys that named more than one document (split; each split is explained in the YAML header)

| Key before | Now |
|---|---|
| LAWSOC-AGENTIC-2026 | LAWSOC-AGENTIC-2026: the report summary page (client-development, knowledge-management, quality-review). LAWSOC-WHATAGENTIC-2026: the explainer "What is agentic AI" (work-production). LAWSOC-AGENTICFULL-2026: the full PDF report (quality-review, and firm-finance, whose locator cites pages 53 and 58). |
| TRI-PREMORTEM-2026 | TRI-PREMORTEM-2026: the feature (2026-02-18; one URL now, out of three). TRI-PILOTFAIL-2026: TRI's article introducing it, "Why your agentic AI pilot probably will fail" (2026-02-20; knowledge-management cited its "big idea" section). |
| TRI-CMBDO-2026 | Kept for the article on talking to clients (client-development). TRI-CMBDOTALENT-2026: the talent article (talent-learning). |
| LAWSITES-LITERA-2026 | Kept for the August drafting release (quality-review, work-production). LAWSITES-LITERARFP-2026: Litera's CEO's sponsored RFP post (pursuit-proposals). |
| TR-AIPS-2026 (pursuit-proposals module) | TR-AIPSBLOG-2026: the Thomson Reuters blog post. TR-AIPS-2026 stays the report PDF. |
| ABA-LPT-PAYKIN / -SC / -WILLIAMS | Separate podcast episodes that share one RSS feed URL. Kept, and noted in the header. |
| ARXIV-ADVERSE / ORBILU-ADVERSE | Two copies of one paper. Kept apart because only the preprint was read. Noted in the header. |

### Collisions with other archetypes (PS key renamed)

- **VALS-VLAIR-2025 → VALS-VLAIRFEB-2025.** The PS files mean the February 2025 report; the tax archetype uses the key
  for the October 2025 report. PS's October report remains VALS-VLAIRRES-2025. Canonical URL `vals.ai/industry-reports/vlair-2-27-25`;
  `vals.ai/vlair` redirects there.
- **TR-FOP-2026 → TR-FOP-REPORT-2026.** This one was not in the coordinator notes. Tax uses TR-FOP-2026, and assurance
  uses TRI-FOP-2026, for TRI's *tax and audit firms paper* (2026-07-21). PS used the key for the full report. The
  2026-07-21 date in acceptance-risk had been copied from that paper.
- The other keys PS shares with tax, assurance and security name the same document: CHARLOTIN-DB, IRS-OPR,
  ANTHROPIC-DELOITTE, FRC-ATT, ICAEW-EXPECT, IESBA-SNAPSHOT, INTAPP-INTAKE and EC-AIACT. BI-PWC-2025 is the same
  Business Insider article; assurance cites its Yahoo syndication. Read dates differ for the living pages: Charlotin,
  and EC 2026-10-17 in security. IESBA was aligned to 2026-06-11, after checking the page.

### Coordinator-flagged dates and fields (settled from the publisher)

| Key | Settled value | Basis |
|---|---|---|
| ILTA-TECHSURVEY-2026 | `2026-08-14`, type survey | The ILTA survey page and the PDF carry no publication date. PDF metadata: created 2026-08-14. The "2606" in the file name is not a date. |
| CALBAR-GENAI-2026 | `2026-05-14` | The State Bar ethics-resources page says the Board approved the revision on May 14, 2026. PDF created 2026-05-15. |
| TR-FOP-REPORT-2026 | `2026-06-22` | Release date confirmed by the staffing verifier. The page itself has no date. Five dates had been in use. |
| EC-AIACT-2026 | `2026-10-19` | The page shows "Last update 19 October 2026". Its title now says it is a living page. |
| CERTINIA-CUSTOMERS-2026 | `2026-09-03` | The byline reads "September 3"; the year comes from its Dreamforce reference. |
| LAWSOC-GENAI-2026 | `2026-06-30` | The page shows "30 Jun 2026". Three files had "2026", one "2026-04". |
| NBER-AUTOR-2026 | nber.org URL, `2026-09-03` | First version 3 Sep 2026; revised Oct 2026. Replaces the EconPapers URL. |
| ACCEVERLAW-2025 | everlaw.com.au release, type survey, 2025-10-14 | Replaces the Business Wire reprint URL. |
| STANFORD-CANARIES-2026 | landing page, `2026-08-12` | "Revised August 12 2026". The old PDF path was from the 2025 version. |
| Others | ERPTODAY-KANTATA (erp.today original), INTAPP-PRACTUS (intapp.com), FLBAR-OP241 (official PDF), ABA-OP512 (LawNext copy, the one actually read), BLOOMBERGLAW-ACC (bgov URL), IMANAGE-CHAFFETZ 2026-07, INTAPP-DEALCLOUD 2026-10-19, INTAPP-TERMS 2026-08-18, LITERA-GCRFP 2026-07-24, NYC-AEDT 2023-07-05, QORUSDOCS-ITBRIEF 2026-02-26, BIDLAB 2026-08-26, EU-AIACT-ANNEX3 2024-06-13, DELTEK-SPI typed vendor, KANTATA-RMI typed survey | Verification-report values, or the page itself. |

Other keys whose titles or publishers differed took their most common form. About 600 source fields were rewritten
with a node-level edit that keeps entries and locators unchanged. Six source records were broken before this work: an
unquoted comma had split a publisher into extra keys (ARXIV-ADVERSE-2025 in acceptance-risk, and CALBAR-GENAI-2026 in
pursuit-proposals five times). They are fixed. One risk item in `staffing-resourcing-14` ("Reviewer note: ...") was
being read as a mapping; it is now quoted.

McKinsey's outcome-fee share was already consistent: "about a quarter" of fees in both files. The "roughly a third"
figure is labelled a different measure (share of work) from a secondary summary. Nothing changed.

## 2. Duplicates across modules

**Replaced: `professional-services-delivery-management-15` (retrospective drafting at close-out, C).** It was a subset
of `knowledge-management-15`: the same Certinia Retrospective Drafter and Knowledge Base agents. Its distinct content
was moved into knowledge-management-15:
- solution: the Moonnox and Automation Consultants items;
- risks: the CalBar p.6 / ABA 512 cross-matter confidentiality point and the Law Society fictional-data advice;
- sources: 5 records.

The delivery-management module and the YAML header now point to the knowledge-management id. The delivery-management
header count reads 15 entries (A 0, B 7, C 5, D 3); A or B is 47%. No other file referenced the removed id.

**Kept, with cross-references in both directions** (each module adds something distinct). References were added to
YAML notes where they were missing:

| Pair | Why both stay |
|---|---|
| client-development-15 / scoping-pricing-09 (/ pursuit-proposals-17) | Same Laurel–Legora evidence. Client conversation vs pricing answer vs RFP answer; each has different sources (GSK, Bloomberg Law). |
| client-development-14 / scoping-pricing-10 | Conversation playbook (B) vs fee and gain-sharing questions (TRI-INTERDEP, C). |
| client-development-21 / scoping-pricing-23 (/ knowledge-management-22) | Relationship asset vs priced service vs the knowledge work behind STAAR. |
| delivery-management-11 / work-production-15 / quality-review-08 | Harvey templates: coordination layer vs agent drafting vs review-gate design. |
| talent-learning-11 / work-production-06 (/ knowledge-management-19) | NBER trial: skill retention vs drafting quality vs capture of senior judgment. |
| delivery-management-02 / client-development-09 | Meeting capture for delivery vs call summaries and coaching for business development. |
| scoping-pricing-01 / delivery-management-01, -02 | Same Spaulding Ridge and Diabsolut results. Scoping-pricing adds Diabsolut's move to fixed-fee contracts; notes now say it is one set of deployments. |
| firm-finance-01 / scoping-pricing-19 | Firm fee mix vs one consultancy's outcome fees (same McKinsey figure). |
| firm-finance-13 / scoping-pricing-13 | Partner pay and credit vs staff metrics off billed hours. |
| quality-review-16 / work-production-25 / acceptance-risk-11 | Disclosure to clients vs per-matter AI records vs client-restriction register. |
| talent-learning-01 / work-production-22 / quality-review-01 / knowledge-management-18 | Training gate vs rollout policy vs enforcement vs curation. |
| billing-collections-01 / firm-finance-03 | Time capture vs leakage and profitability analytics. |
| quality-review-05 / work-production-23 / knowledge-management-23 | Tool benchmarks vs testing on the firm's own work vs measuring the knowledge layer. |
| acceptance-risk-11 / pursuit-proposals-19 | Matter-opening register vs bid-stage term screening. |
| staffing-resourcing-21 / talent-learning-14, -17 | Same employment-AI controls applied to staffing vs hiring and evaluation. |
| delivery-management-16 / staffing-resourcing-16 / talent-learning-20 | Engagement economics vs agents as capacity vs workforce shape. |
| billing-collections-14 / scoping-pricing-06 / firm-finance-12 | AI tagging before billing vs hourly budgets on actual time vs AI cost metering. |
| billing-collections-13 / firm-finance-04 | In-house invoice review vs spend analytics. |
| client-development-07 / pursuit-proposals-12 | BD assistants vs proposal-writing assistants. |
| client-development-17 / scoping-pricing-11 / staffing-resourcing-18 / work-production-19 | AI addenda in OCGs vs AI-savings terms vs in-house sourcing vs AI-first in-house drafting. |
| scoping-pricing-21 / firm-finance-17 | AI-native law firms: pricing vs firm model. |
| delivery-management-07 / staffing-resourcing-08 / scoping-pricing-08 / billing-collections-07 | Margin and burn alerts vs utilisation alerts vs budget-overrun alerts vs fixed-fee scope flags. |
| firm-finance-06 / billing-collections-08; firm-finance-09 / scoping-pricing-17 | Aim AI at written-down work vs pre-bill risk score; tracking freed hours vs deciding the dividend. |
| talent-learning-10 / quality-review-15; talent-learning-12 / staffing-resourcing-15; talent-learning-19 / firm-finance-14 | Different steps of related work. |
| knowledge-management-04 / pursuit-proposals-04; acceptance-risk-10 / billing-collections-03; work-production-17 / knowledge-management-18 | Different steps of related work. |

These pairs were looked at and judged not to be duplicates, with no change:
- acceptance-risk-14 / knowledge-management-14;
- work-production-08 / quality-review-07;
- delivery-management-01 / staffing-resourcing-09;
- firm-finance-07 / quality-review-17;
- knowledge-management-10 / work-production-15;
- client-development-20 against scoping-pricing-09, -11 and quality-review-16.

## 3. Cross-references

A script resolved every `professional-services-…`, `assurance-…`, `tax-…` and `security-…` id, including chained
short forms ("-14, -17") and `#NN` in the modules. It found 0 missing ids, both before and after the edits.

All cross-module references (296 pairs) were read against the target entry's title. None pointed to the wrong or a
renumbered entry. 39 short references ("scoping-pricing-06", "-firm-finance-12") in billing-collections,
firm-finance and quality-review were written out as full ids.

## 4. Provenance and grades

- **NBER 35720.** Taken from the abstract page.
  - It names the authors: Autor, Rodchenko, Martin, Iscenko, Strand, Pearl and Ferere.
  - It says "The study was conducted by Google" and that Google funded "the direct costs of this experiment".
  - Five authors are full-time Google employees and one is a paid Google contractor.
  - Its outcome rows were already vendor-published in all three files that carry figures.
  - The note "run and funded by Google, whose model was tested; NBER working paper" is now in every entry that cites
    it (KM-19, TL-11, TL-12, SR-15, FF-14, WP-06, WP-10).
  - Wording that called it independent was corrected: the work-production YAML header, work-production §5 and §9,
    the knowledge-management "independent evidence" list, and the pursuit-proposals and quality-review source lines.
- **SPI-AI-2026, 84.8%.** Labelled vendor-published in firm-finance-09 and staffing-resourcing-20, but independent in
  scoping-pricing-17. Now **independent** in all three: SPI's page names no sponsor and SPI sells no AI product.
- **BLOOMBERGLAW-ACC-2025, "nearly 60%".** Labelled independent in work-production-25 and vendor-published in
  scoping-pricing-09. Now **vendor-published** in both: the survey was co-run by Everlaw.
- **Grade changes: none.** The grade rules do not depend on provenance, so no grade had to move.

## 5. Build words removed

- **YAML headers.** All 12 were rewritten. Removed: "synthesised … from research/runs/wave3", verification-report
  paths, candidate counts, "deep dives", "angle", "routed", "re-verified", "wave 3 fact-check". Each header now gives a
  check date, the scope, and a source-key note.
- **Entries.**
  - 203 "Merged from practice-NN, discourse-NN…" / "From governance-NN" / "Combined dive use case NN" sentences were
    removed. Six facts inside them were kept in plain words, for example "The SOW part is entry 05".
  - About 95 other phrases were rewritten, such as:
    - "gap noted in the deep dive";
    - "routed from …";
    - "read in full on verification";
    - "Grade C (lowered from B at verification)";
    - "Graded B on verification, down from A";
    - "the discourse dive recorded…";
    - "as read by the deep dive; not re-verified", now "page could not be re-opened";
    - locators "(routed from the … deep dive)".
- **Modules.**
  - "Sources checked and re-verified" in the quality-review and talent-learning headers.
  - "Verification lowered #04 and #15", now the reason itself.
  - "as read by the deep dive", "routed here", and "opened at verification".

Domain uses of "verification", "candidate", "routing" and "research-synthesis" were left alone.

## 6. Firm type

A "Firm kind" or "Organization type" sentence was added, from the entry's own sources, to:
acceptance-risk-07, client-development-11, delivery-management-08, knowledge-management-16 and -21,
pursuit-proposals-11, -13 and -16, and staffing-resourcing-06, -08, -10 and -19.

Entries that already name the type inline were left as they are, for example "Ropes & Gray (US law firm)" in
talent-learning.

## 7. Validator

```
python3 scripts/validate.py  ->  0 error(s), 23 warning(s)
```

Module line counts are at most 300 (billing-collections, delivery-management and firm-finance are at 300). Every
module keeps its table of contents. A script confirmed that every remaining entry has the same id, grade, ladder and
maturity as before.

## Notes for the coordinator

- Delivery-management is now 15 entries (A or B: 47%). Knowledge-management-15 grew by two risks and five sources.
- The verification reports said the ILTA date was unresolved. It is now the PDF date, 2026-08-14, because ILTA's page
  gives no date. The YAML title says so.
- 183 rewritten text fields were re-wrapped into folded blocks so the block-style files keep their layout. Parsed
  values are unchanged; a script checked this.
- Not done: the tax archetype's VALS-VLAIR-2025 and TR-FOP-2026 keep their names. Renaming them would make the cross-archetype keys clearer, but those files are outside this brief.
