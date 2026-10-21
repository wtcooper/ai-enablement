# Sources cleanup report: assurance and tax

Done 2026-10-21. This pass follows up the open items in `mid-market-integration-report.md` §6. Files edited: `assurance/` and
`tax/` under `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/`. `advisory/` was not touched.
No grade, provenance, claim or use-case text changed. The only edits are to keys, source-record fields and one URL. A
word diff against a copy taken before editing shows only key tokens and that URL changing outside the two `sources.md`
files. Nothing was committed by this pass. Checkpoint commit 4153817, made by another process during the work, picked up
part of the in-progress `sources.md` edits.

## 1. sources.md entries aligned with the YAML

Where a Part B key also appears in use-case YAML, its title, type, date and URL now match the YAML. Assurance: 48
entries changed. Tax: 29 entries changed. The three named fixes:

- VALS-TAXAGENT-2026 is now dated 2026-10-20.
- JOFA-AIPA-2026 now has type professional-body.
- BOARDMEMBER-CAQ-2026 now uses the YAML URL (`https://boardmember.com/?p=50023`).

Other changes:

- **Types set to the vocabulary term.** Examples: "professional body" became professional-body, and "regulator forum"
  became regulator. A qualifier that carried information was kept as a note after the date, for example "low
  authority", "secondary", "vendor survey", "analyst", "certifier" and "advisory firm".
- **Titles set to the YAML title.** Where the old Part B title had a descriptive suffix, the suffix moved into the note.
  Examples: "Audit Benchmark Survey, 54 firms", "conference highlights", "SAS No. 150", and "preprint, arXiv 2609.32835".
- **Dates set to the YAML date.** This was mostly a month made precise to the day. KPMGUK-GOVAI-2026 is now dated 22
  Sep 2026 with the note "date from page metadata". IRS-RP2013-14 now reads "2013-01; effective 2013-01-14".
  TEI-TAXTECH-2026 and DELOITTE-TTT-2026 keep their seminar and PDF-creation notes.
- **URLs fixed:** BOARDMEMBER-CAQ-2026 and TR-AGENTIC-2025 (the URL now ends in `.html`).

**Not aligned. The YAML entries for these keys disagree with each other, so no value was chosen:**

| Key | YAML disagreement | Part B |
|---|---|---|
| PCAOB-TAA-2024 | Title, date and URL point to two documents: the PCAOB adopting release (2024-06-12) and the Federal Register notice (2024-07-02) | Entry not touched. It names a third page, the PCAOB implementation page |
| CTRLCOUNCIL-WSJ-2026, IAASB-ED500-2026, ICAEW-PIERPOINT-2025, MINDBRIDGE-ARA-2026, VERDANTIX | Title wording | Title not touched. Type and date aligned where the YAML agrees |

The following keys also have disagreeing YAML entries but are not in Part B: BIG4NEWS-2026 (type: press or community),
CAQ-GENAI-2024 (title capitalisation), DATASNIPPER-CONNECT-2026 (title and date), FORVIS-RESERVING-2024 (date),
IVSC-IVSED-2026 (date), and IIAF-AIFRAUD-2026 (title and date: 2026-02-17 or 2026-07; see item 3).

**Key collision in tax, left open.** In `tax/sources.md` (Part A and Part B) and in `disruption.md` §5, AVALARA-AGENTIC-2025 is
the Accounting Today article dated 30 Sep 2025. `disruption.md` quotes that article's "always on, always ready". In the
YAML, AVALARA-AGENTIC-2025 is a different document: Avalara's PR Newswire release of 2025-10-06. The Accounting Today article
is ACCTODAY-AVALARA-2025 in the YAML. Rewriting the Part B entry to match the YAML would change which document the
`disruption.md` citation points to, so the entry was not touched. Suggested fix: change the key to ACCTODAY-AVALARA-2025 in
`disruption.md` and in `sources.md` Part A and Part B, and give the PR release its own Part B entry.

## 2. Part B coverage

Taken literally, the brief covers every key cited in the new and widened modules or their YAML that Part B lacks. That is
373 keys in assurance and 190 in tax. Adding them all would make the two files about 615 and 440 lines long. The
validator fails any reference markdown file over 300 lines, so this conflicts with the brief's 0-error requirement. It
would also break Part B's own stated rule: it lists keys cited in more than one archetype file or in Part A. Every
existing Part B entry meets that rule. Keys used only in a module and its YAML stay in the module's source list and the
YAML.

What was added: keys cited in a new or widened module that are also cited in at least one archetype-level file or in Part
A. The fields were copied from the YAML `sources:` records. Every record for each of these keys agrees on title, type,
date and URL. Where publishers differ, the more common one was used. Entries were inserted in alphabetical order. Both
files are now 249 lines.

- **Assurance (7):** EBSA-AUDITQ-2023, GAO-YBFAQ-2025, PWC-AT-2025, AT-AICPAPA-2026, FIELDGUIDE-JOBS-2026,
  FRC-SUPERVISION-2026, TR-STATE-2026.
- **Tax (11):** TAXNOTES-UNWATCHED-2026, TR-SOTP-2026, ACCRUAL-ARC-2026, ANTINOZZI-2024, BARMORE-OPR-2026,
  CHARLOTIN-DB-2026, CPAPA-TR-2026, HRB-Q4CALL-2026, IRS-I8867-2025, KTS-OPR-2026, OLIVER-BOSUMMIT-2026.

Not added: JOFA-SMALLFIRMS-2026, because it is cited only in module files in each archetype. If full coverage is
wanted, Part B has to be split across files or the line limit raised. Either is a structural decision.

## 3. Older duplicate keys folded

Each pair was checked first: the two records share the same URL. Rule used: keep the key cited in more files. On a tie,
keep the key the YAML uses. Each fold covers YAML, modules, archetype-level markdown and `sources.md`.

| Kept | Replaced | Files (kept : replaced) | Note |
|---|---|---|---|
| KPMG-CLARA-2025 | K-CLARA | 9 : 2 | Identical records |
| MODUS-2026 | AT-MODUS-2026 | 6 : 2 | Identical records |
| UNIQUS-FILER-2026 | UNIQUS | 5 : 3 | The YAML used UNIQUS. File count decided |
| VERDANTIX | VERDANTIX-KPMGFEE-2026 | 4 : 3 | The YAML uses VERDANTIX. The YAML titles still disagree (item 1) |
| CIRCIT-CS-BDONL-2026 | CIRCIT-RABOBANK-BDONL-2026 | 3 : 2 | The YAML used the other key. The Part B title now matches the YAML title |
| IIAF-AIFRAUD-2026 | IIAF-FRAUD | 2 : 2 | Tie, both keys in the YAML. Kept the dated key, which has more citations. The records still disagree on title, date (2026-02-17 or 2026-07) and publisher (AuditBoard or Optro); not chosen |
| IRS-RP2013-14 | IRS-RP201314-2013 | 4 : 2 | The Part B title now matches the YAML title |
| WCG-2026 | WCG-NOTREADY-2026 | 7 : 3 | Fields already agreed |

**Left open:** ACCTODAY-AVALARA-2025 / AVALARA-AGENTIC-2025. The two YAML records name different documents (see item 1).

## 4. Cross-archetype key

Both URLs were fetched. `https://www.journalofaccountancy.com/news/2026/aug/real-life-ways-small-firms-use-ai.html`
redirects to `https://www.journalofaccountancy.com/issues/2026/aug/real-life-ways-small-firms-use-ai/`. That URL is also
the page's canonical link. The page is "Real-life ways small firms use AI" by Anita Dennis, published 2026-08-01. It
contains both cited passages: the One Stop CPA tax-planning section and the remark about keeping client data out of
public AI. It is one article.

- JOFA-SMALLFIRMS-2026, the tax key, was kept because its URL works (it redirects).
- In `assurance/use-cases/private-company.yaml`, JOFA-REALLIFE-2026 became JOFA-SMALLFIRMS-2026 (3 occurrences).
- The tax record now uses the canonical `issues/` URL. The assurance record already used it.
- Both locators are unchanged.

## 5. Validator and greps

`python3 scripts/validate.py`: **1 error, 31 warnings.** The warnings are the existing content-target counts. The error is
outside this pass's scope: `skills/ai-solution-delivery/references/templates/brief.md` has 103 lines and no table of
contents. It does not come from assurance or tax files, and this pass added no errors.

Old keys grepped across the repository outside `research/`, with 0 hits each: IIAF-FRAUD, K-CLARA, UNIQUS,
VERDANTIX-KPMGFEE-2026, AT-MODUS-2026, CIRCIT-RABOBANK-BDONL-2026, JOFA-REALLIFE-2026, IRS-RP201314-2013,
WCG-NOTREADY-2026. They still appear in `research/` run files, which were not edited.
