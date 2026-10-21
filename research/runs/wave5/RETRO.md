# Wave 5 retro: advisory archetype

Date: 2026-10-21 · Feeds: the plan's waves and costs, the brief templates

## Result

**Advisory archetype.** Seven verified modules and 11 archetype-level files. The archetype covers the advisory and
outsourced side of accounting firms that serve private and middle-market companies. It extends professional services
the same way assurance and tax do, and is listed as available in `archetypes/index.md`.

The landscape scan proposed the module set, and the owner chose all seven areas. Client accounting services and risk
and controls had full three-angle dives (practice, discourse, governance). The other five had one combined dive each,
because public detail is thin. Two cross-cutting topics were researched: independence and pricing, and the state of
AI and disruption.

| Module | Use cases | A/B | Evidence | Entries fixed by verifier |
|---|---|---|---|---|
| client-accounting-services | 24 | 50% | strong | 18 / 24 |
| risk-controls | 23 | 50% | strong | 16 / 24 |
| private-client | 17 | 35% | moderate | 13 / 17 |
| forensic-disputes | 15 | 33% | moderate | 11 / 15 |
| transactions | 16 | 31% | moderate | 15 / 16 |
| valuation | 15 | 20% | thin | 7 / 15 |
| fpa-performance | 14 | 14% | thin | 12 / 14 |

**No entry was rejected.** Verification corrected 92 of 125 entries (74%). A few grades moved, mostly from B to C
(one went from C to B), and one unreachable source was removed. Later, the consistency pass merged one risk-controls entry into another
(124 entries now), and the CohnReznick valuation announcement was added as `advisory-valuation-15`.

**Consistency pass.** Duplicate source keys were folded into one, matching assurance and the knowledge base where the
same document already had a key: IESBA, JofA, COSO, IVSC, PCAOB and Karbon records, among others. A script confirmed
that no key carries two titles, dates, types or URLs, and that no URL has two keys. Overlapping entries were
cross-referenced both ways with assurance, tax and professional services. No grade changed.

**Archetype-level verification.** About 420 claims were checked across the 11 files: 77 fixed and 1 removed. The
reports are `advisory-archetype-verification-A-report.md` and `-B-report.md`. The main fixes:
- **Misread statistics:** hours per CAS leader read as hours per CAS person; a truncated QoE price range; a Blue J
  billing figure read as value-pricing intent; "very important or essential" shortened to "essential".
- **Attribution drift:** a global BDO investment credited to BDO USA; a CFO quoted by KPMG credited to KPMG; a JofA
  staff article cited as "the AICPA says".
- **Rules stated too narrowly or too broadly:** AICPA contingent fees, SEC exceptions, AI disclosure.
- **Status drift:** proposed Federal Rule of Evidence 707 still called "proposed" after the committee voted to withdraw
  the published draft. The forensic module was aligned afterwards.
- **Removed:** one unsourced connective claim ("integration, not model quality, is the blocker").

## What the evidence says

Client accounting services has the most public evidence in the field. Firms describe their staffing, pricing and
platform choices in the JofA, CPA Trendlines and vendor case studies, and some report measured close times or hours.
Risk and controls draws on SOX and internal-audit surveys and the COSO generative AI guidance.

Transaction, valuation, forensic and FP&A work is described mostly by vendors and in conference abstracts. No named
firm publishes AI fees, margins or error rates for these services. Rules are moving:
- Rule 707 on machine-generated evidence is unsettled.
- The AICPA's work on private-equity ownership of firms is open.
- Independence limits shape which advisory services can go to attest clients.

The economics questions are the same as in professional services: who keeps the saving, whether fixed fees replace
hours, and how the outsourced model scales.

## Cost and time

| Work | Agents | Model | Tokens (approx.) |
|---|---|---|---|
| Landscape scan, 11 dives, 2 cross-cutting topics | 14 | Sonnet | 4.4M |
| Module synthesis and verification | 14 | Opus | 4.6M |
| Consistency pass, archetype synthesis, two archetype verifiers | 4 | Opus | 1.4M |
| **Total** | **32** | | **about 10.4M** |

Token figures are each agent's final context size, the same measure as earlier retros. With combined dives for five
modules, research cost about 0.6M tokens per module, against about 1M in wave 3.

## What went wrong, and what changed

| # | Problem | Change |
|---|---|---|
| 1 | The plugin was renamed mid-wave, which left stale paths in the synthesis and verification briefs | Fixed with one search-and-replace before any of them launched. Future renames: grep `research/runs/*/briefs` too |
| 2 | Five of seven modules miss the 50% A/B target | No grade was raised to meet it. The modules are rated moderate or thin in `ARCHETYPE.md`, and the advisor says so |
| 3 | The forensic and valuation modules described Rule 707's status differently | Status claims about moving rules now go to the archetype verifiers with the newest primary source, and are aligned across modules afterwards |
| 4 | The archetype-level synthesis cited survey figures beyond the population they measured | Same pattern as every earlier wave; verification stays mandatory |
| 5 | Some primary texts could not be reached (AICPA Code text for private-company attest clients, three BVWire pages, the SBA SOP) | Read through named secondary sources and labelled as such, or flagged as a gap |
