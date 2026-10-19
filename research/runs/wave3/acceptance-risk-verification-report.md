# Verification report: professional-services / acceptance-risk

Checked 2026-10-19 against the sources themselves. Files edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/acceptance-risk.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/acceptance-risk.md`

I opened all 41 sources cited in the YAML and the 14 sources that only the module cites. Most were opened directly; the
rest went through the r.jina.ai mirror. Four more documents were fetched to settle claims:

- the arXiv preprint of the adverse-media paper (arXiv 2602.23373, in full);
- the SRA's own AML report pages (publications.sra.org.uk, via the mirror);
- the NYC Bar landing page for Opinion 2024-5, to confirm its date;
- the National Law Review page metadata for the Swiss Re release date.

No web search was used.

## Counts

| Action | Entries |
|---|---|
| Kept | 0 |
| Fixed | 14 (`-01` to `-14`) |
| Rejected | 0 |

No entry was rejected. Every entry rests on at least one source that exists and was read in full. Most fixes are small:
dates, attribution or wording. No grade changed. No entry claims A. Each B entry rests on a named organization in a source
that was read in full:

- `-03` BakerHostetler. It is now also backed by Legal IT Insider, which was read in full.
- `-06` Pinsent Masons.
- `-08` BDO Canada, Sandberg Phoenix and Loeb & Loeb.
- `-10` Fredrikson & Byron.
- `-12` Nelson Mullins.
- `-14` Carvana and Legora's own legal team.

The only measured figures (in `-08`) come from non-AI workflow platforms and are presented as Intapp's case-study
narrative, so B is the ceiling.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 6 (43%) |
| C | 6 |
| D | 2 (`-07`, `-11`, both labelled idea) |

## Targets

| Target | Result |
|---|---|
| 12–20 use cases | Met: 14 use cases |
| At least 50% graded A or B | **Not met: 43%.** No entry could be raised honestly. `validate.py` also warns, against its own 15–25 count target. |
| Every source dated | Met: every source has a URL and an ISO date |
| `validate.py` errors | None for these files. Before the fixes the module was 304 lines against a 300-line limit; it was trimmed to 300. |

## Fixes

| Entry / section | What was wrong | Fix |
|---|---|---|
| `-01`, `-03`, `-13` source date | INTAPP-CONFLICTSAI-2026 used the access date 2026-10-19 and was called "undated" | JSON-LD `dateModified` 2026-08-17 |
| `-02`, `-05`, `-08`, `-09`, `-13` source date | INTAPP-ONBOARDAI-2026 used the access date | `dateModified` 2026-10-06 |
| `-10` source date | INTAPP-TERMS-2026 used the access date | `dateModified` 2026-08-18 |
| `-12` source date | INTAPP-WALLS-2026 used the access date | `dateModified` 2026-10-08 |
| `-02` risk; module §6 | IESBA locator said Q2, but automation bias is in Q4. The wording "a threat to objectivity" is not the source's: IESBA says a bias that "can impair objectivity". | Locator and wording corrected |
| `-02` risk; module §6 | Oregon III.C was embellished as "disqualifying information … should promptly enter". The opinion says it is "important" that lawyers who obtain "sufficient information" enter the prospect. | Reworded to the source |
| `-03` source | LEGALTECH-CELESTE-2026 was marked search-only and blocked, with date "2026-07" and publisher "Legal Technology". It now opens. | access `full`, date 2026-07-27, publisher Legal IT Insider. The note now cites its statement that intake and conflicts is the use case BakerHostetler "grabbed onto" |
| `-04` checkpoint | "Managing partner decides on flagged matches" is not what the source describes. Red and orange flags go to the responsible partner, and green results are auto-approved. | Restated to the source |
| `-06` source date and ref | XAPIEN-PINSENT-2026 used the access date and was called undated. JSON-LD datePublished is 2025-01-30 (modified 2026-06-18). | Date corrected; ref renamed XAPIEN-PINSENT-2025 in both files (no other file uses it) |
| `-06` problem and prerequisite | Wrong document: the "three hours per client" and false-positive points are in the ebook summary, not the case study. "Xapien's pitch is fewer false positives from name collisions" appears in neither. | Attributed to XAPIEN-PINSENT-EBOOK-2025; the unsupported claim was removed |
| `-06` outcome | The 2.4 million hours problem statement was tagged lever `risk` | Changed to `capacity` |
| `-06`, `-13` risks; module §6 | Wrong speaker: the VinciWorks "roundtable" is an invitation-only AML Core Group meeting, recorded as Q&A | Described as such |
| `-07` source | The ORBilu record failed TLS directly; the mirror showed only a truncated abstract. It was marked `access: full`. "The abstract reports no evaluation" was overstated: the paper evaluates score separation across test populations. | Added ARXIV-ADVERSE-2025 (preprint, read in full: it confirms the justifications and the open-source code). ORBilu is now `search-only`. The measures now state what the paper evaluates. |
| `-08` outcomes and role_evolution; module §7 | Wrong speaker: the BDO Canada 38%, the Sandberg Phoenix 3x, the Loeb 200→800 figures, the "made the human workflow engine obsolete" line and Sandberg's "needed" an intake department are Intapp's case-study narrative, not firm statements. The module also said Sandberg "built" an intake department; the source says it "needed" one. | Attributed to the case studies; "built" changed to "needed" |
| `-09` risk; module §6 | Wrong document and speaker: the engagement-letter disclosure point is the January 2026 PCRT update, as reported in an ACCA In Practice article. It was stated as ACCA's own rule ("belongs"), and the locator pointed to the wrong section. | Reworded ("suggests"), PCRT named, locator now "'Ethical risks'" |
| `-09` risk and checkpoint; module §6 | The Oregon III.D claim was embellished. The engagement-letter example is in the Discussion, and III.D says it "would be prudent" to subject a chatbot's autonomous actions to lawyer approval. | Reworded; the locator now covers the Discussion and III.D |
| `-11` solution | Wrong speaker: "idea discussed by practitioners", but the tool-list check and the record of which tool touched which matter come from a vendor guide (Layer3 Labs) | Attributed to LAYER3-OCG-2026 |
| `-11` checkpoint | Unsourced connective claim: "partner or risk counsel agrees …" is not in ACCA | Restated: the firm agrees the restriction with the client and decides how compliance is monitored; the sign-off role is not in the sources |
| `-11` source date | Layer3 was dated "2026-09" | 2026-09-07 (updated; first published 2026-07-07) |
| `-12` risk; module §6 | Embellishment: "shared knowledge bases that mix clients can breach walls" is not in the NYC Bar opinion | Replaced with the opinion's own point: a firm's AI systems must implement required ethical screens |
| `-12` problem | "Wall policies have historically not extended into AI tools" had no ref | Attributed to INTAPP-HARVEY-2026; the Chaffetz figure was given its ref |
| `-13` note; module §5 | "The SRA page was blocked" | The SRA's own report site was reached via the mirror. It confirms 935 engagements and 270 non-compliant firms (almost a third of those rated). The 92%, 79% and 39% figures were not in the pages reached and stay secondary. |
| `-14` source dates | Legora was dated "2026-10", exact day unconfirmed; Harvey used the access date | Legora 2026-10-13 (date beside the headline); Harvey 2026-10-13 (the product video's JSON-LD uploadDate) |
| `-14` role_evolution; module §7 | Wrong speaker: "Legora says" | Legora's general counsel says |
| Module §7 | BAKERMCKENZIE-CLIENTAIRISK-2026 was search-only. The posting returns 404 directly and 403 via the mirror, so it cannot be confirmed. | Removed from §7 and §10 |
| Module §7 | Embellishment: "firm general counsel take on compliance with client AI guidelines". The source only lists this as a roundtable session topic. | Reworded |
| Module §8 | "2026-10: Legora and Harvey launch" | Dated 2026-10-13, matching the YAML |
| Module §3 | "#07 … research prototype for banks". The paper says financial institutions. | Corrected |
| Module §10 | TR-FOP-2026 had no date; the LEGALTECH and ARXIV keys were missing | Date 2026-07-21 added (matching other professional-services files); keys listed |
| Module header | No A/B share was given | "only 43% are A or B" added |

Checked and confirmed without change:

- Celeste GA (15 Jul 2026), the Jampol 10x quote and the BakerHostetler quote; lateral-hire playbook; walls and need-to-know.
- Celeste for ChatGPT Enterprise (17 Sep 2026).
- California COPRAC guidance (May 2026), pp. 2, 5–7 and 9.
- ABA 512, pp. 2, 7 and 8.
- NYC Bar 2024-5 (7 Aug 2024).
- Oregon 2026-208 (approved Feb 2026).
- Fredrikson & Byron (Numrich quotes) and the Dickinson Wright quote.
- Nelson Mullins (Carrillo quote); Intapp–Harvey (23 Feb 2026); Chaffetz Lindsey 35%.
- ILTA Q3.18 figures; TRI Legalweek (Blair, Hudock); Starbucks (eDiscovery Today); Litera's ACC 59% (secondhand).
- Jenner & Block event; Virtual Vocations posting (22 Sep 2026); TRI premortem (18 Feb 2026); AdAI (23 Feb 2026); Practus (1 Sep 2026).
- BDO Australia (2017 implementation; Olivier quote); Loeb & Loeb quotes.
- Module-only sources:
  - PCAOB QC 1000 (effective 15 Dec 2026); TR FOP 34%; ACC-Everlaw 657/61%/59%; LexisNexis 54% (16 Apr 2026);
  - Fenergo–Grant Thornton (3 Mar 2026); Intapp Q4 Moody's (4 Aug 2026); Global Legal Post excerpt (2 Mar 2026);
  - Accounting Weekly (1 Sep 2026); DWF and the SRA notice (17 Aug 2026); DAC Beachcroft (28 Sep 2026);
  - IA magazine (9 Mar 2026); Swiss Re–Wickard (press release date 08-27-2026); Bloomberg Law "ghost" quote (29 Nov 2023).
- Every cross-reference id (`assurance-acceptance-independence-01` to `-06`, `-08`, `-11`, `-13`, `-16`, `-17`;
  `professional-services-work-production-18`, `-22`, `-25`; `security-ai-security-21`;
  `tax-compliance-individual-business-19`) exists, and the entry's content matches the description.

## Sources that could not be reached

| Source | Status |
|---|---|
| ORBILU-ADVERSE-2025 | TLS failure directly; the mirror showed only part of the abstract. Replaced as the evidence by the arXiv preprint of the same paper. |
| BAKERMCKENZIE-CLIENTAIRISK-2026 | 404 directly, 403 via the mirror. Removed. |
| SRA AML annual report (www.sra.org.uk) | 403 / CAPTCHA. The publications.sra.org.uk version was reached in part, via the mirror. |
| PCAOB release | 403 directly; read via the mirror. The exact day in Aug 2025 is not shown, so it is kept as `2025-08`. |
| ILTA-TECHSURVEY-2026 date | Unresolved. The PDF is undated, its file code is "2606" and its metadata says 2026-08-14. It stays `2026-06` to match the other files; the coordinator should settle it across all files, as the scoping-pricing report also notes. |

## Patterns of error to fix in the briefs

1. **Access date used as the source date.** Five Intapp product pages and the Xapien case study carried 2026-10-19 and
   were called "undated", although each has a JSON-LD datePublished or dateModified. Briefs should require checking the
   JSON-LD (`datePublished`, `dateModified`, video `uploadDate`) before falling back to the access date.
2. **Vendor narration attributed to the customer.** Case-study prose written by Intapp was presented as "BDO Canada
   reports", "Sandberg Phoenix says" and "Loeb & Loeb says". Briefs should require naming the speaker: a quoted person,
   or "the vendor's case study says".
3. **Secondary reports attributed to the reporting body.** PCRT guidance was presented as ACCA's own rule. An
   invitation-only VinciWorks meeting was called a "roundtable" of UK firms. A vendor guide was called "discussed by
   practitioners".
4. **Embellished qualifiers in regulatory text.** "Should" was used where the source says "prudent"; "disqualifying"
   was used where it says "sufficient". The NYC Bar was given an extra clause about shared knowledge bases. The
   engagement-letter example was moved into a section that does not mention it.
5. **Unsourced connective claims in checkpoints and roles.** Examples are "Partner or risk counsel agrees" and "firm
   general counsel take on compliance". Briefs should require that a checkpoint or role statement cites a source or says
   "not described".
6. **Blocked-source status not rechecked.** Legal IT Insider and the SRA report were reachable at verification time.
   Briefs should require one retry, and the mirror, before a source is marked search-only.
7. **Problem statements drawn from a second document but cited to the first.** The Pinsent Masons ebook content was
   cited to the case study.
