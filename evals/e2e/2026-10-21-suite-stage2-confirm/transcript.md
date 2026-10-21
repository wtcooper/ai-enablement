### USER
The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: frame it, decide build versus buy, and open the brief as `g1` evidence.

### TOOLS
- Skill: ai-transformation:ai-portfolio
- Write: /tmp/claude-0/-tmp-claude-0--home-user-ai-enablement-807fbf4d-3850-5c6c-82b1-8d3750715cd5-scratchpad-suite-stage2-confirm-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/g0.py
- Skill: ai-transformation:ai-solution-delivery
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Write: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/portfolio.yaml
- Write: /tmp/claude-0/-tmp-claude-0--home-user-ai-enablement-807fbf4d-3850-5c6c-82b1-8d3750715cd5-scratchpad-suite-stage2-confirm-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/check.py

### ASSISTANT
`g0` is recorded as a Go into discover. The brief is open as `g1` evidence. Step 1 and step 2 are both still open, so `step_completed` is 0. Both YAML files parse.

**`g0`: Go into discover (light path)**
- **Decided by:** the portfolio lead, after the integrated-audit manager validated the item.
- **Resources:** the integrated-audit manager's time, released by the practice leader. There is no budget beyond the existing approved assistant. The only data is non-client templates and synthetic examples.
- **Why a low-value item went ahead:** the value index is 2.44 and the readiness index is 4.73. The rules allow a Go only on the light path and only if cheap. This one is cheap because it costs a share-and-review routine on an assistant the firm already has.
- **Kill criteria:**
  - Client data turns up in prompts, templates or practice cases, or wording enters a workpaper without a senior's approval.
  - There is no benefit owner or no baseline from records by the combined `g1`/`g2` gate.
  - The baseline shows template and wording time near zero.
- **Next gate:** `g1`, with `g1` and `g2` combined on the light path. The gatekeepers are the practice leader, the risk lead and the IT/security lead. The seven evidence rows are in the intake record's "Next gate evidence" table.
- **Housekeeping:** the item moved from `intake` and `outline` to `discover` and `active`, and I removed its `provisional` flag. I also copied `tier-2` into `risk_tier` from the draft policy, marked provisional, because the risk lead hasn't confirmed it.

**Brief (`solutions/ct-int-nonclient-drafting/brief.md`)**
- **Frame:** drafted from the portfolio record. It isn't confirmed by anyone yet. The baseline, the benefit owner, a walk-through of the last real instance and the rule/template check are all missing.
- **Build or buy, proposed only:** configure the approved enterprise assistant with shared prompts, templates and a senior approval routine, and build nothing. Sourcing stays `undecided`, because no own-sample test has been run and no maintenance owner is named. There is no `tool-catalog.yaml`, so I could not cite a catalog entry.
- **Hand-back:** the item's `solution` field now points at the brief.

**Things to check**
- **Manager's time:** the amount hasn't been stated. I recorded it as a condition on the Go, not as a number.
- **Validation and scores:** I recorded the validation as you reported it. I didn't change the scores. Value is still 2, and the park rule (value 2 or less) would apply if validation hadn't raised it. The Go rests on the light-path "if cheap" exception, and I flagged this for re-testing at `g1`.
- **Advisor file:** it still carries `draft-to-validate`. I don't edit that file from here.
- **Other items:** `state.step_completed` stays at 2 and `next_step` at 3, because the other items still have no `g0` decision.

Next question for step 1: where could a baseline of template and wording time per control test come from, such as time records or a sample of recent test files?

### USER
Time records won't work, because nobody books template or wording time to its own code. Use a sample instead: have the manager pull about ten recent control-test files and estimate the template and wording time in each. I'd guess it's about 1.5 hours per test, out of roughly 8.

Put the manager's time at about 4 hours a week for six weeks. The benefit owner is the integrated-audit manager, and the practice leader signs off.

### TOOLS
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
I've recorded the benefit owner, the manager's time and the sampling method. Step 1 is still open because the baseline hasn't been taken. Both YAML files still parse.

**Recorded**
- **Benefit owner:** the integrated-audit manager, with the practice leader signing off. That is the same role as the owner, so I noted in the intake record that the practice leader checks the baseline at `g1`.
- **Manager's time:** about 4 hours a week for six weeks, about 24 hours in all. The `g0` decision entry stays as written, since decisions are append-only. The update sits in the intake record's Screen result, and the practice leader's own confirmation of the release isn't recorded yet.
- **Baseline method:** a sample of about ten recent control-test files, with the manager estimating template and wording time in each and recording only the case id and the estimate. Time records are ruled out because there is no booking code for that work.

**Two points to resolve**
- **The base doesn't match.** The item's range is 0 to 15% of a 1.5 h hands-on, so 0 to 0.2 h per test. Your guess of 1.5 h out of roughly 8 is about 19% of a larger base, roughly seven times the top of that range. I haven't changed the value range or the scores. Your figure is logged as a reported guess, and the sample should settle which base is right.
- **Reading past client files.** The sample means the manager looks at past client control-test files. That is the same question `overlay/policy.md` leaves open for the checklist back-test. I added the risk lead's view as a prerequisite row in the evidence table.

Is the roughly 8 hours per test the whole test, with the 1.5 h hands-on in the intake being a part of it, or is it the same base measured differently?

### USER
The roughly 8 hours is the whole control test, and the 1.5 hours hands-on in the intake is a part of it. My 1.5 hours for template and wording is a separate slice, so it isn't the same base measured differently. Keep my figure as a guess, and let the sample show which base is right.

Go ahead and add the risk lead's view on reading past files as a prerequisite before the manager starts pulling them.

### TOOLS
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
The risk lead's view is now a prerequisite for the file sample. The manager doesn't start pulling files until that view is recorded. Both YAML files still parse.

**What changed**
- **Prerequisite:**
  - The intake record's evidence table has its own row, "Risk lead's view on reading past control-test files". It is owned by the risk lead and its status is not presented.
  - The baseline row now says it needs that row first.
  - The brief lists it in the open criteria for step 1 and in the open questions.
  - The brief's handoffs table has a row for ai-governance, marked not yet requested. I haven't asked anyone.
- **Bases:** I recorded your clarification as it stands.
  - A whole control test is roughly 8 hours.
  - The 1.5 hours hands-on is part of it.
  - Your 1.5 hours of template and wording is a separate slice, outside the hands-on.
  - Your figure stays a reported guess.
- **Value range:** the two numbers aren't the same base measured twice, so there is no contradiction. The item's range (0 to 0.2 h per test) covers only the hands-on slice. If the sample finds a separate slice near 1.5 hours, the range was scoped too narrowly. That would also move the value score of 2 that the Go rested on. I haven't changed the range or scores, and I noted the metric's base (whole test or hands-on slice) as an open question.

**Draft ask to the risk lead** (for you to send, since I haven't):

> The integrated-audit manager needs to estimate template and wording time in about ten recent control-test files, as the baseline for `ct-int-nonclient-drafting`. They would read the files inside the firm's own systems and record only a case id and a time estimate per file, with no file content and nothing pasted into any AI tool. Is that permitted, and are there conditions? This is the same question as question 4 in the draft AI policy, so your answer there would cover the checklist back-test too.

Is the whole-test hours figure, roughly 8, what the metric should use, or should the metric be hours per template and wording slice?

### USER
Use hours per template and wording slice as the metric, since that's the work the tool would change. Record the whole-test figure of about 8 hours as context only. Widen the item's value range to match once the sample is in. I'll send the ask to the risk lead myself, so mark that row as requested.

### TOOLS
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
The metric is now hours per template and wording slice. The whole-test figure of about 8 hours is recorded as context only. The risk lead row is marked as requested by you, with no answer yet. Both YAML files still parse.

- **Metric:** it's recorded in the intake record, the brief and the `g1` evidence list. The metric was your choice, so I recorded the owner's confirmation as still outstanding.
- **Value range:** I haven't changed it. It stays at 0 to 0.2 h per control test, grade D, until the sample is in. I added a `g1` evidence row to re-size it on the slice metric and re-check the value score of 2 that the Go rested on. A baseline near zero on the slice would leave the low end of the range as the whole case, which is the third kill criterion. I reworded that criterion to say "per slice".
- **Risk lead ask:** the row now reads "requested by the portfolio lead; no answer yet". The brief's handoff row says the same. The manager still doesn't start pulling files until the risk lead's view is recorded.

The next move is for the integrated-audit manager to confirm the metric. After that, the sample starts once the risk lead answers. Do you want to name the sample's selection rule now, for example the most recent ten control tests in one period? I'd record it so the baseline is checkable.

### USER
Yes, name the rule: the most recent ten completed control tests from the last twelve months, taken in date order from the integrated-audit manager's own engagements. No cherry-picking, and if a file can't be read under the risk lead's conditions, skip it and take the next one. Record that in the brief and the evidence table, and mark the sample as waiting on the risk lead's answer.

### TOOLS
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
I've recorded the sample rule in the brief (§1, success metric and baseline line) and in the intake record's evidence table. Both YAML files still parse.

**Rule as recorded:** the most recent ten completed control tests from the last twelve months, in date order, from the integrated-audit manager's own engagements. There is no cherry-picking. A file that can't be read under the risk lead's conditions is skipped and the next one is taken. The sample is marked as waiting on the risk lead's answer, and no file is pulled before that answer is recorded.

I added two things you didn't ask for:
- **Skipped files:** each skipped file is listed by case id with the reason, so the skips can be checked later. Drop this if you'd rather not.
- **Limits:** the sample covers one manager's engagements, and the manager makes the estimates. So the result is recorded as a sample estimate (reported), not a record, and the practice leader checks it at `g1`.

The sample method is now fully specified. Nothing moves until the risk lead replies, and the manager's confirmation of the metric is also still open.

### USER
Good, the sample method is settled. While we wait on the risk lead, can you prepare the `g1` evidence pack for this item? I want the baseline sample, the re-sized value range and the practice leader's sign-off laid out, so we can run the gate as soon as the numbers are in.

### ASSISTANT
Here is the `g1` pack. It's a layout with the blanks marked, because no numbers exist yet. I haven't written it to a file: gate pre-reads belong in chat or the review pack, and the evidence status already lives in the intake record's "Next gate evidence" table.

## `g1` pack: `ct-int-nonclient-drafting` (discover to prototype and pilot, combined on the light path)

**Gatekeepers:** practice leader (submitting practice), risk lead, IT/security lead. **Outcomes on the table:** Go, Kill, Hold or Recycle. The gatekeepers decide; I record.

### 1. Evidence checklist

| Evidence | Status now | Needed to close |
|---|---|---|
| Metric agreed with the benefit owner (hours per template and wording slice) | partly met | Integrated-audit manager's confirmation |
| Risk lead's view on reading past files | ask requested, no answer | Recorded answer and conditions |
| Baseline sample | waiting on the risk lead | Table in section 2 filled |
| Value range re-sized on the slice metric | not presented | Section 3 completed |
| Three non-client use cases and a share-and-review routine | not presented | Use cases listed, with the senior who approves templates |
| Non-client templates and synthetic examples seen in their real state | not presented | A senior's review of the examples |
| Strategic fit and technical feasibility | not presented | Check with the people who do the work |
| Provisional `tier-2` confirmed | not presented | Risk lead's reaction to the draft policy |
| Build, buy or configure leaning | proposed (configure, no build) | Owner's confirmation; brief step 2 closed |

### 2. Baseline sample (fill from the manager's estimates)

| Case id | Date order | Template and wording hours | Whole-test hours (context) | Skipped? Reason |
|---|---|---|---|---|
| (ten rows) | | | | |

Report the lowest, typical and highest, plus the skipped list. Label it "sample estimate, self-reported, one manager's engagements".

### 3. Re-sized value range

The sample gives the size of the slice. It does not give the saving. So the range needs three inputs:
- **Slice hours per test:** from section 2, as a low and a high.
- **Share of the slice the assistant removes:** nothing supports a figure yet. It needs a small own-sample test, such as drafting the same templates with and without the assistant, with a senior reviewing both. Until then the saving is a hypothesis.
- **Number of control tests a year in integrated audit:** I don't have this. The value range needs it, so I'm asking for it.

The range is saving = slice hours × share removed, then per test and in total. It stays a range with assumptions, with no single-point ROI. Re-check the value score of 2 against it. If the low end is near zero, kill criterion 3 applies.

### 4. Practice leader's sign-off

| Item | Sign-off | Recorded as |
|---|---|---|
| Baseline checked (sample rule followed, skips listed) | practice leader | met / not met |
| Release of the manager's time for the next stage (about 4 hours a week for six weeks so far, still to be confirmed) | practice leader | resources line of the Go |
| Benefit owner and metric | practice leader, with the integrated-audit manager | met / not met |

### 5. Kill criteria check
1. Client data in prompts, templates or practice cases, or wording in a workpaper without a senior's approval.
2. No benefit owner, or no baseline by this gate.
3. Slice baseline at or near zero.

### 6. What the Go has to name
- **People and time for prototype and pilot:** not yet named. The six weeks of manager time may or may not cover it.
- **Budget:** none beyond the existing assistant, to confirm.
- **Data:** non-client material only.
- **Next gate (`g3`):** adoption evidence and benefit rows.
- **Live limit:** the portfolio's `live_limit` is unset. The rules say no Go at `g1` past the live limit, so the steering group has to set it before this gate can run. This one could stop the gate.

I'd like you to answer two things:
1. How many control tests a year does integrated audit run, or who would know?
2. Who sets the live limit, and is it likely to be set before the numbers arrive?

### USER
Integrated audit runs about 40 control tests a year. The integrated-audit manager can confirm the exact count, so use 40 as a placeholder and mark it as a guess.

The steering group sets the live limit, and I chair it. I'll put it on the next agenda and propose a figure. I'd expect it to be set before the numbers arrive, because the sample is waiting on the risk lead anyway. Record the live limit as an open dependency for now.

### TOOLS
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/portfolio.yaml
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
I've recorded both items, and both YAML files still parse.

- **Volume:** about 40 control tests a year, marked as a placeholder guess. It's in the intake record's "How often it happens" section and in the brief's open questions, and the integrated-audit manager confirms the exact count. The yearly count is now listed as an input to the re-sized value range.
- **Live limit:** recorded as an open dependency in three places. These are the intake evidence table (owner: steering group, chair the portfolio lead), the item's `next_gate` evidence in `portfolio.yaml`, and the brief's open questions. The pack already said a Go at `g1` can't pass without it.

**Rough arithmetic on the two guesses**
- **At your guess:** 40 tests × about 1.5 hours of template and wording is about 60 hours a year for the whole slice. That's before counting any share the assistant removes.
- **At the item's current range:** 0 to 0.2 hours per test gives 0 to 8 hours a year.
- **Against the effort:** the manager's time for the baseline is about 24 hours (4 hours a week for six weeks). At your guess that is over a third of the whole slice's yearly hours.
- **What it means for the gate:** this is a sanity check, not a result. It sharpens the "worth a year" question and kill criterion 3. If the sample comes in nearer the item's range, the gatekeepers may reasonably weigh a Hold or Kill against the small pool. The saving will be some fraction of the slice, and nothing supports that fraction yet.

Do you want the manager's six weeks to cover only the baseline sample, or also the small own-sample test of the assistant on templates, which would give the share the assistant removes? That decides what the Go names as resources.

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5