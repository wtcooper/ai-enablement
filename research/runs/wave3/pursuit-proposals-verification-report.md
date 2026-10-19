# Verification report: professional-services / pursuit-proposals

Checked on 2026-10-19 against the sources themselves. These files were edited in place:

- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/pursuit-proposals.yaml`
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/pursuit-proposals.md`

All 80 sources cited in the YAML were opened and read. So were the 10 sources that only the module cites (marked *). Most were fetched directly. The routes for the rest:

- **Through the r.jina.ai mirror:** both ABA Law Practice articles (browser engine), SEC 2024-36, FTC Operation AI Comply and the Federal Register notice.
- **With a plain curl user agent:** the Loopio pages, which block browser user agents.
- **From page renders:** the AutogenAI Big 4 PDF, which contains only images.
- **Through the Crossref API:** the abstract of JBL-MCKINLEY-2026.

One web search was used, to look for a named professional-services firm that would support a B grade for `-11`. It found none: only government contractors.

## Counts

| Action | Entries |
|---|---|
| Kept | 1 (`-17`; the only change was a refreshed locator for LAWFUEL-2025) |
| Fixed | 19 (`-01` to `-16`, `-18`, `-19`, `-20`) |
| Rejected | 0 |

Every source exists, and each one supports the core claim of the entry that cites it. One grade changed: `-13` went from B to C, and its maturity from in-production to emerging.

## Final grade mix

| Grade | Count |
|---|---|
| A | 0 |
| B | 9 (45%) |
| C | 8 |
| D | 3 (`-17`, `-18`, `-19`, all labelled "Idea") |

**Targets:**

- **20 use cases (target 15–25):** met ✔
- **A or B share of 45% (target ≥50%):** **not met** ✘. The module was at exactly 50% before verification. Downgrading `-13` takes it below the target. No entry could honestly be raised: the search for a named professional-services firm doing AI quality review (`-11`) or writing executive summaries with AI (`-10`) found only government contractors.
- **Every source has a URL and an ISO date:** met ✔. The 10 module-only sources now have URLs and dates in a table in §10.
- **Validator:** `validate.py` reports 0 errors. Its only remark on these files is a warning about the 45% share. The module is 299 lines, within the limit of 300.
- **No grade A:** confirmed. Every firm figure is a recollection, estimate, projection or undefined vendor number, so none meets the 2026-10-17 rule for A.

## Fixes

| Entry / section | Problem (error pattern) | Fix |
|---|---|---|
| `-01` solution | "Big 4 firm **replaced** an in-house tool and a private ChatGPT". The PDF says only that these fell short and that the firm then selected AutogenAI (embellished) | Now reads "chose the same platform after finding [they] fell short" |
| `-01` VERSENT source | Date given as "2025", with the title "(page undated; year from image paths)". The page's JSON-LD gives datePublished 2025-08-14 (imprecise date) | Date set to 2025-08-14; title note removed |
| `-01` notes | Attributed "global revenue rose 5%" to "AutogenAI's customer page", which was never cited. The claim is in the Serco PDF's own title (wrong document) | Now cites the PDF title, and contrasts it with the "win rates" figure in the PDF body |
| `-01` source dates | QORUSDOCS-ITBRIEF dated 2026-02-25, but the publisher's date is 2026-02-26 (NZ time). BIDLAB dated "2026-08"; the page was modified on 2026-08-26 and first published on 2024-06-06 | Dates corrected; the BIDLAB locator now records the history |
| `-02` checkpoints | "Practice groups and lawyers decide what to reuse…" is not in TRI. "Reviewed by the marketing team" is not in the Benesch study (unsourced connective) | Replaced with Benesch's actual wording, and the gap is noted |
| `-02` prerequisite | "a tagging scheme someone owns" (embellished) | Now "tagging for reuse" |
| `-03` risk | ABA 512 p.2 n.4 was presented as the ABA's own statement. It is a quoted Pennsylvania and Philadelphia opinion about LLMs without ethical walls (wrong speaker) | Attributed correctly |
| `-03` checkpoints | "Lawyers and consultants maintain entries" was cited to the Neudesic study, which is about consultants only. "Cleared for use" was cited to ABA Cautions, which does not say it (wrong attribution; embellished) | Rewritten to each source; clearance is now cited to ABA 512 p.6 |
| `-03` solution and risk | ABA sentence "and formatting this way" (paraphrase drift). "GRSM says verification remains important" is the vendor's narrative, not a GRSM statement | Reworded to the sources |
| `-04` title, prerequisite and notes | "as the credential feed for pitches": TRI never mentions pitches. "Guardrails agreed with the firm": the source says the data science team set them (unsourced; embellished) | Title trimmed; the pitch use is marked as an inference; guardrail wording corrected |
| `-05` prerequisite | "Named owners who resolve disputed records" (embellished) | Now "staff who can merge, split or correct records" |
| `-06` prerequisite, risk and role_evolution | Unsourced statements were cited to ABA LPMAI item 1 and Cautions: "a defined review step after extraction", "extraction can miss or misread clauses", and "bid coordinators spending less time" | Each restated to the ABA text, with gaps marked |
| `-06` posting title; module §7 | Quoted as "RFX **and** AI Orchestration"; the posting says "RFX **&** AI Orchestration" | Quote corrected |
| `-07` solution | "Practitioners and vendors describe…": only one vendor (Kantiv) does (embellished) | Corrected |
| `-07` Loopio locator | "Ch.7 pp.83-84" for the 60% vs 47% strategic-contributor figure, which is on p.79 (Ch.6) | Now Ch.6 p.79 and Ch.7 p.83 |
| `-08` outcome; module §3 | "24 hours of research **cut by** more than half". TRI says that cutting the time by more than half was the new data scientist's "first task", and reports no result (statistic presented as something it doesn't measure) | The figure is now labelled a goal; the module says the reduction achieved is not reported |
| `-08` problem; module §3 | An unsourced second sentence on competitor knowledge; "-05" was described as "relationship intelligence" when that entry is opportunity scouting | Attributed to ABA item 7; the cross-reference description is corrected |
| `-09` role_evolution; module §7 | "rather than waiting for BD staff" is not in Harvey. The Latham role was described as "works with BD on panels…" | Restated to each source |
| `-10` checkpoints | Exec-summary editing was cited to ABA item 3, which does not mention it. "A person approves the final document" is not in NYREJ (embellished) | Now cites ABA item 3 as written and Loopio blog item 4 (added as a source); NYREJ is quoted as written |
| `-11`, `-13` role_evolution | Unsourced connective claims ("reviewer's job shifts…", "bid writers move from composing…") | Marked as inferences; `-13` now ties its inference to the CUI study |
| `-12` problem and role_evolution | "So staff had no safe way…" (unsourced connective). Loopio's "**may** be because" was rendered as "**is** the reason" (embellished cause) | Both corrected |
| `-13` grade and maturity | Grade B and "in-production" rested on Freelancer.com and labour-platform studies. No professional-services firm is named (grade inflated by an adjacent process) | Now C and emerging; the note explains why |
| `-14` notes | The CERTINIA-SOA-2026 claim was "not checked". It is now read: about 8 hours to 1 and 15 times more RFPs, with no customer named | Notes and locator updated; the claim is still not used as an outcome |
| `-14`, `-15` CALBAR locators | "More autonomy, more oversight" was cited to p.2; it is on p.3 (and p.5) | Locators corrected |
| `-15` outcome | One outcome mixed two sources: Unanet's 17%, and Responsive's 41% vs 17% under a BDC-UNANET ref (format) | Split into two outcomes, each with its own source_ref |
| `-15` checkpoint | "review outputs at defined points" is not in the source | Now reads "people direct the work; no source specifies review gates" |
| `-16` risk | "Win/loss notes are recollections" is a gloss on Kantiv | Restated to Kantiv's advice on hindsight |
| `-18` role_evolution | "Browne Jacobson tells buyers not to score AI-use answers and to plan for more tenders and clarification questions". That advice is in PPN 017 para 9 and Annex B (wrong document) | Re-attributed to PPN 017; Browne Jacobson keeps its own point on evaluation capacity |
| `-18` risk | The California clause was summarised without its "materially impacts" limit | Qualifier added |
| `-19` problem and prerequisite | "AI restrictions" and "reviewed late and by hand" were unsourced; "AI policy" is not in ABA item 6 | Each part attributed or marked as an assumption |
| `-19` LITERA-GCRFP source | Dated "2026", with a note saying the page has no date. The page shows "Fri 24 Jul 2026" | Date set to 2026-07-24 |
| `-20` solution | TGC-WK-2025 was cited for AI comparison of submissions; it covers RFP systems that help legal departments issue targeted requests. The UpperEdge sentence had no ref | TGC now cited for what it says; UpperEdge ref added |
| `-20` outcome and notes; module §5 | "123 State of Ohio **IT** supplier bids". The abstract says "government supplier bids" (embellished) | "IT" removed |
| `-20` risk | "NIH reported **one applicant** submitting more than 40 applications". NIH says AI enabled principal investigators (plural) to do so | Corrected |
| `-11` and other locators | Locators said "as routed from…" for sources not re-read (LAWFUEL, CANBERRATIMES, SOURCE-PRECISION, HARVEY-LPHS) | All were read; real locators added |
| FLBAR-OP241-2024 | Cited from a third-party mirror (ezel.ai) | Switched to the official Florida Bar PDF (p.7) |
| Module header and §3 | Grade mix "B 10, C 7"; `#13` shown as "(adjacent, B)"; GRSM's "more than 50%" | Header reads B 9, C 8; `#13` shown as C; GRSM's figure is now its marketing manager's "over 50%", with no stated baseline |
| Module §3 | Gowling WLG was listed as generating pitches and proposals. Its case study covers experience search only | Gowling restated as "uses the same platform for experience search" |
| Module §2, §9 | "One invented credential can disqualify". The vendor says this about an SF-330 "project citation" | Wording corrected and attributed to the vendor |
| Module §5 | Responsive 2026: "6 in 10 see positive ROI" refers to "Leaders" only (subgroup presented as the whole sample) | Subgroup named |
| Module §6 | "Reusing one client's matter information in another's pitch may breach duties [ABA-OP512]" overstates the opinion | Restated as the quoted state-bar view in note 4 |
| Module §6 | Australian rule summarised as "advise planned AI use in quote responses"; the source says planned AI use "in the delivery of services" | Corrected |
| Module §7 | "BD leaders argue for a seat on the firm's AI council". The show notes say one consultant (Guy Alvarez) wants "a seat at the AI table". "Reviewers become verifiers" was unsourced | Both corrected |
| Module §8 | "84% of partners expect **AI-driven BD** within 18–24 months". The 84% is reaching Stage 3 **or** 4; only 40 of 123 expect AI-driven BD (statistic presented as something it doesn't measure) | Restated |
| Module §9 | "Clients call a product name an unacceptable answer". It was Litera's CEO, in a sponsored post (wrong speaker) | Re-attributed |
| Module §10 | The 10 module-only (*) sources had no URLs | URLs and dates added in a table; all 10 were opened, and their figures confirmed (one was corrected; see §5 above) |

## Confirmed without change (sample)

- **Cherry Bekaert:** 8 to 2 hours, and 2–4 hours; 550 RFPs; 600 professionals; 80%; about 2,500 assets; the "auditor mentality" quote. The case study is dated 2026-10-08.
- **Loopio report (1,533 respondents, with APMP):**
  - adoption: 79/68/34%; tool use 57/57/43%;
  - AI uses: 62/52/39/38/34/28/21%;
  - AI benefits: 47/40/17%;
  - volume and time: 166/153 RFPs; 55% responded to; consulting 229 vs 155; 33 vs 35 hours;
  - outcomes and roles: win rate 39 vs 45%; shortlist rate 46 vs 54%; 32/42/16%; 45% via portals.
- **Other surveys:**
  - QorusDocs: 297 respondents; 60/35%; 48/46/41%.
  - ikaun 2026: 69/27/74/7%. ikaun 2025: 79/68%.
  - Unanet: 71/29/17/13/92/47%; win rates 56/52/50%.
  - Responsive 2025: 41/17, 37/18, 37/26.
  - Introhive: 68%, 6.7, 78%, 63%; 42/42/39 by firm type.
  - Dayshape: 55% (Onrec, 2026-10-13).
- **Case studies:**
  - GRSM: about 60 proposals; 22 hearing types; more than 1,100 matters; go-live November 2025.
  - Neudesic: 75% and 50% are listed under "Solutions powered by ikaun".
  - Arup: more than 12,000, about 7,000 and more than 10,000.
  - Woodard & Curran: 30–40% (an estimate).
  - Benesch: 2 hours vs 6–8.
  - Ballard Spahr: 2,000 documents per instance; 2 hours saved; 900 users.
  - LPHS: under 48 hours.
- **Academic:** Noy & Zhang (0.8 and 0.4 SD; 444 participants); Magesh (17–33%); Cui et al. (51%); Galdin & Silbert (19% and 14%; Freelancer.com coding jobs; AI tool April 2023); NBER 35720 (133 lawyers, senior-concentrated gains).
- **Regulatory:**
  - PPN 017: paras 9 and 15, Annex B; published on GOV.UK 2025-02-17.
  - ABA 512: pp.6–8.
  - California guidance: pp.5–7 (May 2026).
  - Other US bodies: CALDGS 2302 (rev. 02/2025); NSF; SEC ($225k + $175k); FTC (Khan quote).
  - Other bodies and jurisdictions: ICMCI s.11.2; Florida Bar 24-1; JMW (SRA notice published 2026-08-17); BSB via Mondaq.
- **Dates and module-only sources:** Introhive MCP dateline 2026-04-16; Celeste general availability 2026-07-15; ILTACON 54%/18% (Perkins Coie); Legora posting 90% in 6 months; TR AIPS 18%.
- **Cross-references:** all exist and match their topics:
  - client-development -05, -06, -07, -10, -12, -14 to -19;
  - scoping-pricing -02, -03, -05, -09, -10, -12;
  - knowledge-management -04 and -07;
  - acceptance-risk -10 and -11;
  - work-production -11, -22, -25;
  - talent-learning -06, -07, -11.

  No assurance, tax or security ids are cited.
- **Format:** ids are unique, and every quotation is under 25 words.

## Sources that could not be reached directly

- **ABA-LPMAI-2026 and ABA-LPMRFP-2026:** Cloudflare returned 403. Both were read in full through r.jina.ai with the browser engine.
- **LOOPIO-CHERRYBEKAERT-2026 and LOOPIO-BLOG-2026:** HTTP/2 errors with a browser user agent, and the mirror got a captcha. Both were read with a plain curl user agent.
- **JBL-MCKINLEY-2026:** Wiley and doi.org were blocked. Only the abstract was read, through the Crossref API, so the full text was not seen; the claims are limited to the abstract.
- **SEC-2024-36 (403) and FTC-AICOMPLY-2024 (404 to bots):** both read through the mirror.
- **AUTOGENAI-BIG4-2025:** the PDF contains only images, so it was read from page renders.
- **Unresolved dates:**
  - The ikaun case studies (GRSM, Neudesic, Arup, Stinson, Gowling) carry no publication date anywhere, so "2026" is kept.
  - CERTINIA-VEDA, INTAPP-EXPERIENCE and INTAPP-DEALCLOUD are undated product pages, dated by when they were read.
  - The Serco PDF was created 2025-03-27, but its upload path is 2024/09. "2025-03" is kept, and the title notes both.

## Error patterns to fix in the briefs

1. **Statistic presented as something it doesn't measure (3 cases).** Introhive's 84% was read as "AI-driven BD" when it means Stage 3 or 4. Responsive's "6 in 10" applies to Leaders only. Baker Botts's "cut by more than half" was a goal, not a result. Briefs should require the subgroup and the verb tense (goal or achieved) as the source states them.
2. **Claims attributed to the wrong document or speaker (5 cases):**
   - ABA 512 note 4 (actually a quoted Pennsylvania opinion);
   - Browne Jacobson for PPN 017's advice;
   - "clients" for Litera's CEO;
   - "AutogenAI customer page" for the Serco PDF title;
   - TGC for ABA's legal-ops scenarios.

   Rule: name the speaker, and cite the document that actually contains the words.
3. **Embellished qualifiers and causes (about 12 cases).** Examples: "replaced", "practitioners and vendors", "is the reason" for "may be because", "IT bids", "one applicant", "AI council", "named owners", "agreed with the firm", "cleared for use".
4. **Unsourced connective claims in `human_checkpoints`, `role_evolution` and `prerequisites` (about 10 cases).** These were often cited to a nearby section of a real source that does not say them (ABA LPMAI items 1 and 3, TRI, Benesch). Briefs should require the locator to contain the specific assertion, or the text to be marked as an inference.
5. **Grade inflated by evidence from an adjacent process.** `-13` held a B on labour-platform studies, and its own notes said the grade was "capped at B" for that reason. Briefs should state that adjacent-process evidence caps an entry at C unless the archetype itself has a named deployment.
6. **Dates and access.** Undated pages often carry a date in JSON-LD (Versent) or in visible text (Litera). Publisher-local dates differ from UTC (IT Brief). "Routed, not re-read" locators should be replaced by a fresh read before synthesis.
7. **Module-only sources without URLs.** The module's * keys had no URL anywhere in the repository's plugin files. Synthesis should carry the URL and date into the module whenever a key is not in the YAML.
