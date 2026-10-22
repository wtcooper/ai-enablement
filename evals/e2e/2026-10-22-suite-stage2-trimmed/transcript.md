### USER
The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: frame it, decide build versus buy, and open the brief as `g1` evidence.

### TOOLS
- Skill: ai-transformation:ai-portfolio Record g0 as a Go into discover for ct-int-nonclient-drafting: the integrated-audit manager validated it; the manager's time is released by the practice leader.
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/portfolio.yaml
- Write: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md

### ASSISTANT
`g0` is recorded as a Go into discover, and the brief is open as `g1` evidence. The brief is a draft: the baseline, the owner's metric and a sample test are still missing, so step 1 is not ticked and sourcing stays `undecided`.

I ran the ai-portfolio skill, then the ai-solution-delivery steps (frame, build or buy, open the brief), and checked that the YAML files parse.

**The g0 Go (`portfolio/portfolio.yaml`)**
- The item is now in `discover` and active. The provisional flag is gone because the manager validated it.
- **Resources:** the integrated-audit manager's time, released by the practice leader. No budget, since it runs on the existing approved assistant. Data is non-client templates and synthetic examples only.
- **Conditions:** no client data, and a senior approves templates before shared use.
- **Kill criteria:**
  - Client data turns up in prompts or drafts.
  - No baseline can be found from records.
  - The manager's time is withdrawn.
  - A template library alone does the job.
- **Next gate:** `g1`, with `g1` and `g2` combined on the light path. The intake record's evidence table is filled in.
- **Decider:** I recorded the portfolio lead, which is the light-path decider, and noted the practice leader as consulted. Correct that if someone else decided.

**The brief (`solutions/ct-int-nonclient-drafting/brief.md`)**
- **Framing:** the baseline is reported only, grade D, about 0–0.2 hours per control test. The owner hasn't confirmed the metric yet.
- **Build or buy (draft leaning):** configure the approved enterprise assistant with shared prompts and a share-and-review routine. A plain template library is the baseline it has to beat. A build has no owner and isn't warranted.
- **Tool catalog:** no catalog exists, so I recorded the leaning as a draft and requested a catalog entry through ai-governance.
- **Risk tier:** `tier-2` is provisional, copied from the draft policy. I left it null in the portfolio, as the policy asks.
- **Hand-back:** I set the item's `solution` field in the portfolio.

Value is still low (index 2.44). The Go holds only while the routine stays cheap, and the intake record says the quick-win category wouldn't survive a re-score. I left the category as it is. You may want to re-score it at `g1`.

**Question for the integrated-audit manager:** what number would they use to say this helped, and which record shows template and wording time today?