# Pilot retro: assurance → controls testing

Date: 2026-10-16 · Wave: `pilot` · Feeds: plan M1, spec revision 5, the brief templates

## Result

The pilot produced a module that is credible for use with an audit partner or CAE. The verifier left
it within every target.

| Target | Result |
|---|---|
| 15–25 use cases | **25** |
| At least 50% graded A or B | **64%** (5 A, 11 B, 5 C, 4 D labelled "idea") |
| Every source has a URL and a date | Met. 13 dates were corrected by the verifier |
| Module file ≤ 300 lines, with a table of contents | 293 lines |
| Validator | 0 errors |

**Content highlights**

- Processes are tied to inspection data, for example 213 controls-testing findings at the six largest
  networks in 2025.
- Interview probes an experienced reviewer would ask.
- An honest statement that almost every outcome figure is self-reported or vendor-published, and no
  independent measure of AI test quality exists.
- A new test object: controls that AI itself performs.
- Frontier signals, including the IAASB exposure drafts, FRC guidance and the KPMG view on AI-related
  material weaknesses.

**Still needed:** subject-matter review by an audit professional (spec §13).

## What it cost

| Agent | Tokens | Minutes | Sources read in full |
|---|---|---|---|
| Landscape scan (assurance) | 305k | 16 | 0 (search snippets only, because the network was blocked) |
| Deep dive: practice | 362k | 16 | ~59 |
| Deep dive: discourse | 380k | 14 | ~70 |
| Deep dive: governance & evidence | 385k | 18 | ~64 |
| Synthesis | 321k | 15 | — |
| Verification | 394k | 19 | ~102 |
| **Total** | **~2.15M** | **~67 of wall-clock time** (the stages run one after another) | |

One module costs about **1.85M tokens** without the landscape scan, which is shared across the
archetype. That is about 70% above the plan's earlier estimate of 150k–250k per agent: a deep agent
actually uses 300k–400k.

## What went wrong, and the fixes

| # | Issue | Fix | Where |
|---|---|---|---|
| 1 | The network policy blocked most source sites, so the landscape ran on snippets and copied an extraction error ("50 hours" instead of 850) | The owner opened network access. Briefs require reading the pages themselves | landscape brief |
| 2 | The web-fetch tool fails on DNS. `curl` through the proxy works | Briefs tell agents to use `curl` and `pdftotext` | all briefs |
| 3 | **The verifier corrected 21 of 25 entries** (none rejected). Error types: misread statistics, attribution drift, embellished qualifiers, unsourced connective claims, wrong dates, grades inflated by evidence from an adjacent process, search-only figures inside A or B entries | Precision rules in the deep-dive and synthesis briefs. Error checklist in the verifier brief. New fields: `outcomes[].measures`, `outcomes[].provenance`, `sources[].access`, `sources[].locator` | vocabulary, all briefs, validator |
| 4 | **"Lens" and "ladder" overlapped.** The angles disagreed on lens in 8 of 18 merged clusters, and the "reinvent" rung of the ladder was never used | Split into two independent dimensions: `ladder` (assist → delegate) and `change_scope` (step / process / model). Lenses stay as conversation prompts. Pilot data migrated | spec §6.2, vocabulary, validator |
| 5 | Each deep dive numbered its sources from S01, so the same document had up to four refs | Shared source keys of the form `PUBLISHER-SHORT-YYYY`, set by the landscape | landscape and deep-dive briefs |
| 6 | Some input formats were rejected by the validator ("undated", "FY26", empty outcomes, functions outside the list) | Format rules written into the vocabulary | vocabulary |
| 7 | Out-of-module findings were dropped silently | A "Routed to other modules" section in the deep dives; synthesis collects them | deep-dive and synthesis briefs |
| 8 | Quality evidence (error rates, parallel runs) was only noted as missing at the end | Deep dives must look for it explicitly | deep-dive brief |
| 9 | Four use cases recurred as pattern `other`: assurance over AI-performed controls, multi-agent orchestration, agent evaluation harness, cross-party reliance on AI evidence | Candidates for the pattern library | stream B backlog |

## Decisions for the full build

1. **Keep the recipe:** landscape → three angles → synthesis → verification. Each stage earned its
   place. The angles found different evidence (practice had A/B-heavy deployments, governance had
   regulators and academic work, discourse had the frontier), and the verifier caught material errors.
2. **Scale the angles to the evidence.** The landscape rates each module's evidence density. A
   low-density module gets one combined deep dive. The landscape expects low density for acceptance &
   independence, valuation specialists and sustainability assurance.
3. **Rerun the assurance landscape** with network access, so `sources.md` is built from pages that
   were actually read.
4. **Verification stays mandatory** for every module and archetype-level file.
5. **Cost option to test in wave 1:** run the deep dives on a faster, cheaper model and keep synthesis
   and verification on the strongest one. Compare the verifier's correction rate with the pilot's.
