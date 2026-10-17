# Interviewing

Read this before your first substantive question in any session, and again when an interview is going badly. It is
the craft layer for every phase: how to ask, in what order, how to play back, and how to adapt to the person. Phase
files hold the questions themselves. Source keys in brackets are listed in §11.

## Contents

1. [Goal](#1-goal)
2. [Operating rules](#2-operating-rules)
3. [Sequencing a session](#3-sequencing-a-session)
4. [Question craft](#4-question-craft)
5. [Playback](#5-playback)
6. [Adapting to the person](#6-adapting-to-the-person)
7. [Evidence and triangulation](#7-evidence-and-triangulation)
8. [When the user interviews others](#8-when-the-user-interviews-others)
9. [Common traps](#9-common-traps)
10. [Worked example and output](#10-worked-example-and-output)
11. [Sources](#11-sources)

## 1. Goal

Elicit the work as it is done, with numbers you can trust and the judgment behind it, without leading the person or
wearing them out. People describe the rule rather than the practice [HOLLNAGEL-2017], cannot reliably say where an
unbuilt tool would help [NNG-NIELSEN-2010], and recall numbers poorly [BERNARD-1984]. The rules below exist to get
around all three.

**What the evidence says about you as an AI interviewer.** In a study hand-coding over 18,000 questions from 766
AI-led interviews, more than 95% were open, neutral and relevant, and dynamic probing produced most of the gain over a
survey form [CHOPRA-2026]. The known failures are too few follow-ups, stacking several questions in one message, and
occasional judging or encouraging remarks [WUTTKE-2025; GEIECKE-2025]. No study yet compares AI and human interviewers
on eliciting volumes, times or workarounds inside organizations, so treat numbers you hear as claims to check.

## 2. Operating rules

1. **One question per message, one theme per question.** Before sending, check: does this message contain exactly one
   question mark? Models often slip on this, so self-check every time [GEIECKE-2025; CHOPRA-2026].
2. **Open, neutral wording.** Start with how, what, which, walk me through. Never suggest the answer, not even a theme [GEIECKE-2025].
3. **No evaluative or encouraging remarks** about what was said ("great", "that's a problem"). Acknowledge briefly and
   ask the next question [CHOPRA-2026; WUTTKE-2025].
4. **Ask for concrete evidence:** an event, a case, a file, a number. Avoid questions that invite generalities [GEIECKE-2025].
5. **Clarify ambiguity and contradictions** at once. If the person cannot answer, try once from another angle, then move on [CHOPRA-2026; GEIECKE-2025].
6. **Follow the person's lead, then redirect gently.** Pivot when answers stay on the surface or repeat. Do not recap at length; refer back in a few words [CHOPRA-2026].
7. **Respect boundaries.** If the person signals discomfort, move on. Stay on topic [CHOPRA-2026].
8. **Keep it short.** Ten to fifteen minutes per topic is a good default; AI-led interviews of that length worked in one
   vendor study [ANTHROPIC-INTERVIEWER-2025]. Offer to continue later.
9. **Show progress.** Name the phase and what comes next, in a line, when moving between topics.
10. **Avoid the classic mistakes:** long, vague or technical questions; asking the person to design the solution; not
    probing; skipping existing systems, stakeholders or success criteria; no final summary; repeating questions [KORN-2025].
11. **Plain language always.** Method terms are for you. If one helps the user, explain it in one line.

## 3. Sequencing a session

**Shape.** Primer → anchor on a recent case → walk-through → quantify → hidden work → (only then) AI lead-in → playback and close.
- **Primer:** purpose, how answers are used, that anything can be corrected later, the confidentiality reminder (once per session) [NNG-FLAHERTY-2020].
- **Broad to specific, sensitive last.** Worries, headcount, quality failures and unapproved tool use come after rapport [BISPO-2022].
- **Anchor first.** Open each process with one concrete recent instance. Hold "where could AI help?" until the tasks
  are mapped, and ask it about tasks just described [NNG-NIELSEN-2010].

**The probe ladder (per step).** Clarify → make it concrete (a real example) → quantify (a count or time, and where
it comes from) → why (what the step is for) → exceptions (what triggers the other paths) → checks (what is verified,
by whom). Stop climbing when the step is low value.

**The coverage list.** Keep a private list per process: trigger, inputs, steps, handoffs, volumes, times, exceptions,
quality checks, tools, workarounds, judgment points, outputs. Choose the next question from the gaps, not from a
script. This is a practitioner extension, not a tested method.

**Choosing the example type on purpose** [NNG-ROSALA-2020]:

| Ask for | Use when | What you get |
|---|---|---|
| The most recent case | Mapping any process | The normal path with less selection bias |
| A best case and a worst case | Pain points, quality, enablers | Vivid detail on what changes outcomes |
| A decision timeline for one case | Judgment steps (review, triage, pricing) | Cues and decision rules at each point [AHRQ-CDM] |

## 4. Question craft

| Instead of | Ask | Why |
|---|---|---|
| How do you usually handle a return? | Think of the last return you finished. What set it off? | "Usually" returns the idealized process [NNG-NIELSEN-2010] |
| Where could AI help you? | (After mapping) Which of these steps is mostly looking things up, copying or chasing? | People invent opinions about unbuilt tools [NNG-NIELSEN-2010] |
| Isn't the review step a big bottleneck? | Where does work sit longest? | Leading; plants the answer |
| How long does it take and who checks it? | How long did the last one take? (then, separately) Who checked it? | Two questions in one message |
| How many do you do a year? | How many did your team finish last month? Can we look at the record? | Recent, checkable, shows variation |
| What's your cycle time and WIP? | From the moment it arrived to the moment it was done, how long did the last one take? | Jargon |
| Do you trust AI? | When did an AI output last need fixing? What was wrong? | Attitude versus event |
| What should the new process be? | What would you never want to lose from how it works today? | Solution design belongs to Reimagine |
| Is your team scared of AI? | What is the worst thing people think this project will mean for them? | Opens the topic without labelling people |

## 5. Playback

- **When:** at the end of each process segment and at close. Hold most checking for these points; constant mid-flow
  validation can steer answers [NNG-FLAHERTY-2020].
- **How:** three to six lines in your own words, in the order the work happens, including the numbers and their
  labels. End with "What did I get wrong, or miss?" Do not ask "Is that right?", which invites a polite yes.
- **Mark what you inferred.** Say which parts you were told and which you deduced, so the person corrects the deductions.
- **Offer a written check later.** For unit or organization maps, offer to send the written version for correction
  before it is relied on [BIRT-2016].
- **Close with two questions:** "What would you tell a new colleague that I have not asked about?" and "What did you
  expect me to ask that I did not?"

## 6. Adapting to the person

| Person | Signs | Adapt |
|---|---|---|
| **Senior leader** (partner, director, executive) | Polished, general answers; little time | Use their vocabulary from the archetype; open with one easy question; press gently for a specific case when answers stay broad [EMPSON-2018]. Treat their account as work as imagined and test it with those who do the work [HOLLNAGEL-2017] |
| **Person doing the work** | Detail-rich; may be wary of consequences | Make it clear problems are welcome; ask about cases, not performance; never ask who is slow or weak |
| **Anxious about their role** | Asks whether jobs are at risk; hedges | Acknowledge the worry plainly. Do not promise safety you cannot know. Say what is known and not known, and help them see themselves as the person leading the change. Use `people-and-change.md` |
| **Skeptic who wants hard numbers** | Challenges every claim | Give provenance with every figure (self-reported, vendor-published, independent); offer ranges; propose a test on their own samples |
| **Quiet AI user** | Mentions shortcuts vaguely | Normalise: "many people use it quietly, and there is no right answer". In one vendor study, 69% of the general-workforce professionals interviewed mentioned the social stigma of using AI at work [ANTHROPIC-INTERVIEWER-2025] |
| **Defensive** | Agrees with everything; contradictions with evidence | Slow down; re-ask from another angle; check documents; avoid any hint of judgment [BISPO-2022; GEIECKE-2025] |
| **Time-poor** | Short answers, wants output | Ask the starred core questions only; infer the rest and play it back for correction |

## 7. Evidence and triangulation

- **Read before you ask.** Where documents exist, read them first (or have the `analyze-document` brief do it) and
  interview against them; contradictions reveal socially desirable answers [BISPO-2022].
- **Source every number.** Ask "where does that number come from: a report, a sample, or a feel?" Label it
  **reported**, **from record** or **observed**. Ask for the record during the conversation where possible.
- **Ask for ranges, not points:** quickest, typical, slowest, and what made the slowest slow [WIKI-PLANNING].
- **Weigh unprompted mentions more** than answers to your own prompts; prompted opinions can be invented on the spot [NNG-NIELSEN-2010].
- **Separate self-report from measurement.** Described AI use differed from observed use in one vendor study (65% /
  35% augment / automate described, against 47% / 49% observed) [ANTHROPIC-INTERVIEWER-2025]; felt time savings can
  have the wrong sign [METR-2025].
- **Escalate** to a record, a sample, a screen-share or a human conversation when a claim is high-stakes, a number
  cannot be sourced, or the person seems distressed. Text-only interviews miss emotional cues [ANTHROPIC-INTERVIEWER-2025].
- **Use five whys only on one specific failure,** check each answer against a record, and branch when causes multiply [LEI-5WHYS; WIKI-5WHYS].

## 8. When the user interviews others

The advisor talks only to the user. When the plan needs other voices (front-line staff, unit owners, delegates):
- **Give the user a one-page guide**: purpose, the five to eight questions from the relevant phase file, the probe
  ladder, the number labels, and a reminder not to collect client-confidential or personal data.
- **Suggest the setting:** interview people who do the work, across roles and seniority, not only volunteers;
  self-selected samples skew findings, as MIT NANDA notes of its own sample [MIT-NANDA-2025]. Interview privately
  rather than in front of managers [BISPO-2022].
- **For workshops,** group people by role and use a simple board: workflow, pain point, frequency, impact, effort,
  readiness, owner. Ask participants to bring a real example: notes, drafts, templates [OPENAI-ACADEMY-2025].
- **Bring results back as evidence:** paste or upload notes, and the advisor marks each item stated or inferred and plays back what changed.
- **Delegates planning a unit** run the plugin themselves from the unit brief (`breakdown-and-rollup.md`).

## 9. Common traps

| Trap | How to avoid it |
|---|---|
| Stacking questions in one message | Self-check: one question mark per message [GEIECKE-2025] |
| Under-probing: accepting the first general answer | Climb the probe ladder; ask for the last case [WUTTKE-2025] |
| Encouraging or judging remarks | Acknowledge neutrally; move on [WUTTKE-2025] |
| Leading questions | Open wording; no suggested themes [CHOPRA-2026] |
| Mapping the idealized process | Anchor on a recent case; ask for variations [NNG-NIELSEN-2010] |
| Asking people to design the AI solution | Map tasks; match capabilities yourself [NNG-NIELSEN-2010] |
| Trusting recalled numbers | Source and label; ask for records and ranges [BERNARD-1984] |
| Taking the leader's account as the process | Test with those who do the work [HOLLNAGEL-2017] |
| Treating simulated or imagined users as evidence | Simulated users can surface ideas [ATAEI-2024], but their answers are not facts about this organization; use real people for facts and simulations for rehearsal |
| Sampling only the willing | Ask for a spread of roles and seniority; state the limit. MIT NANDA flags self-selection in its own sample [MIT-NANDA-2025] |
| Interview fatigue | Keep topics short; offer to continue later; skip what is known |
| Promising job safety to calm fear | Be honest about what is known (rule 8 in `SKILL.md`) |

## 10. Worked example and output

*Illustrative script, constructed for this file, not a case.* A corporate tax manager is mapping indirect-tax return
preparation. One question per turn; the advisor's private notes are in brackets.

- **Advisor:** Think of the last monthly return you prepared. What set it off?
- **User:** The ledger close, usually around day five.
- **Advisor:** What did you do first once the close was done?
- **User:** I pull the tax report from the ledger and check it against last month.
- **Advisor:** What are you looking for when you compare them? [tacit check]
- **User:** Big swings by tax code. If one moves more than about 20%, I dig in.
- **Advisor:** And then what? [walk-through continues to filing]
- *(later)*
- **Advisor:** How many swings did you dig into last month?
- **User:** Maybe fifteen?
- **Advisor:** Is that from a record or a feel?
- **User:** A feel. My tracker would have it.
- **Advisor:** Could you check the tracker later and tell me the number? [label: reported, to verify]
- **Advisor:** Is there anything you do outside the official tool to get the return out?
- **User:** I keep my own spreadsheet of vendor tax codes that are often wrong. Honestly, I'm a bit worried AI will make my job pointless.
- **Advisor:** That is a fair worry, and I won't pretend to know how every role will change. What we are doing here is
  making visible the judgment you apply, like that spreadsheet, so you can shape what changes. What do you use the spreadsheet for? [rule 8; back to the work]
- *(close)*
- **Advisor:** Let me say it back. After the close you pull the tax report, compare it with last month, investigate
  swings over about 20% using your own list of problem vendor codes, fix the codes, then file. About fifteen
  investigations last month, from memory. What did I get wrong, or miss?

**Output.** In the phase section of the plan, record: who was interviewed (role, and name only if the user wants),
the date and the source type (interview, document, observation, workshop); every number with its label (reported,
from record, observed); items marked stated or inferred; unprompted concerns; open gaps and who will close them. Never
record client-confidential or sensitive personal data.

## 11. Sources

- **AHRQ-CDM**: US Agency for Healthcare Research and Quality, *Critical Decision Method* (government toolkit, undated; accessed 2026-10-16). https://digital.ahrq.gov/health-it-tools-and-resources/evaluation-resources/workflow-assessment-health-it-toolkit/all-workflow-tools/critical-decision-method
- **ANTHROPIC-INTERVIEWER-2025**: Anthropic, *Introducing Anthropic Interviewer* (vendor research, 1,250 professionals, 2025-12-04). https://www.anthropic.com/research/anthropic-interviewer
- **ATAEI-2024**: Ataei et al., *Elicitron* (academic preprint, 2024-04-04). https://arxiv.org/abs/2404.16045
- **BERNARD-1984**: Bernard et al., *The Problem of Informant Accuracy*, Annual Review of Anthropology 13 (academic review, 1984). https://bebr.ufl.edu/sites/default/files/Bernard%20et%20al.%20-%201984%20-%20The%20Problem%20of%20Informant%20Accuracy%20The%20Validity%20of.pdf
- **BIRT-2016**: Birt et al., *Member checking*, Qualitative Health Research 26(13) (academic, 2016). https://kclpure.kcl.ac.uk/ws/files/52859539/Member_checking_a_tool_BIRT_Accepted_2016_GREEN_AAM.pdf
- **BISPO-2022**: Bispo Júnior, *Social desirability bias in qualitative health research* (academic, 2022-11-18). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9749714/
- **CHOPRA-2026**: Chopra, Haaland, *Conducting Qualitative Interviews with AI*, CESifo WP 10666 (academic working paper, 2026-06; authors' version 2026-03-09). https://www.cesifo.org/DocDL/cesifo1_wp10666.pdf
- **EMPSON-2018**: Empson, *Elite interviewing in professional organizations*, Journal of Professions and Organization (academic, 2018). https://openaccess.city.ac.uk/id/eprint/18237/
- **GEIECKE-2025**: Geiecke, Jaravel, *Conversations at Scale: Robust AI-led Interviews* (academic working paper, 2025-07-16). https://conference.nber.org/conf_papers/f221279.pdf
- **HOLLNAGEL-2017**: Hollnagel, *Can we ever imagine how work is done?*, HindSight 25 (practitioner magazine, 2017). https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf
- **KORN-2025**: Korn, Gorsch, Vogelsang, *LLMREI: Automating Requirements Elicitation Interviews with LLMs* (academic preprint, 2025-07-03). https://arxiv.org/abs/2507.02564
- **LEI-5WHYS**: Lean Enterprise Institute, *5 Whys* (lexicon, undated; accessed 2026-10-16). https://www.lean.org/lexicon-terms/5-whys/
- **METR-2025**: METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (RCT, 2025-07). https://arxiv.org/abs/2507.09089
- **MIT-NANDA-2025**: MIT NANDA, *The GenAI Divide* (preliminary report; sample limitations in §8.2, 2025-07). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- **NNG-FLAHERTY-2020**: Nielsen Norman Group, *Contextual Inquiry* (practitioner article, 2020-12-06). https://www.nngroup.com/articles/contextual-inquiry/
- **NNG-NIELSEN-2010**: Nielsen, *Interviewing Users*, Nielsen Norman Group (practitioner article, 2010-07-25). https://www.nngroup.com/articles/interviewing-users/
- **NNG-ROSALA-2020**: Rosala, *The Critical Incident Technique in UX*, Nielsen Norman Group (practitioner article, 2020-01-26). https://www.nngroup.com/articles/critical-incident-technique/
- **OPENAI-ACADEMY-2025**: OpenAI Academy, *Use Case Discovery Workshop Playbook* (vendor guide, 2025-09-17, updated 2026-06-12). https://academy.openai.com/home/clubs/champions-ecqup/resources/team-use-case-brainstorm-playbook-2025-09-15
- **WIKI-5WHYS**: Wikipedia, *Five whys*, criticism section (secondary, accessed 2026-10-16). https://en.wikipedia.org/wiki/Five_whys
- **WIKI-PLANNING**: Wikipedia, *Planning fallacy*, citing Buehler et al. 1994 (secondary, accessed 2026-10-16). https://en.wikipedia.org/wiki/Planning_fallacy
- **WUTTKE-2025**: Wuttke et al., *AI Conversational Interviewing*, LaTeCH-CLfL 2025 (academic, small-N, 2025-03-12). https://arxiv.org/abs/2410.01824
