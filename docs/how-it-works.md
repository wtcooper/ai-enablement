# How the advisor works

A closer look at what happens in a session. For the short version, see the [README](../README.md).

## Contents

1. [Getting to know you](#getting-to-know-you)
2. [The loop](#the-loop)
3. [Working at team, practice or firm level](#working-at-team-practice-or-firm-level)
4. [What you get](#what-you-get)
5. [How the advisor uses evidence](#how-the-advisor-uses-evidence)
6. [Your organization's content](#your-organizations-content)
7. [Ground rules](#ground-rules)

## Getting to know you

The advisor starts with a short conversation of about 5 to 10 questions, asked one at a time. It
builds a profile of:

- your role and what you're responsible for
- your kind of business (matched to a **business archetype**, such as assurance)
- how far along you are with AI
- your goals and pressures
- constraints (for example, independence rules or client confidentiality)
- the tools you have
- what you want from the session

It uses five journey stages to adapt:

| Stage | Looks like | The advisor focuses on |
|---|---|---|
| **Curious** | Little or no AI use yet | Real examples from your field, a few safe quick wins |
| **Experimenting** | Individuals use chat tools; nothing shared | Turning individual use into shared team workflows |
| **Adopting** | Some workflows are owned and measured | The full loop, data readiness and controls; at most one or two carefully bounded AI-agent workflows |
| **Scaling** | Many workflows; shared platforms | The portfolio, governance and measuring value |
| **AI-native** | AI is built into how the business runs | Business-model changes, new services, pricing, workforce redesign |

## The loop

| Step | What happens |
|---|---|
| **Frame** | Why change, what success looks like, which kinds of value matter (capacity, speed, quality, growth, cost, risk, experience) |
| **Map** | Walk through the real work: what triggers it, the steps, handoffs, volumes, systems and rework |
| **Diagnose** | Find waste, bottlenecks and failure points, including review time that AI can create |
| **Reimagine** | Generate options through four lenses: **improve** the step, **automate** the flow, **delegate** the outcome to an agent with human checkpoints, **reinvent** the work. Draws on real examples from your field |
| **Prioritize** | Score options and sort them into quick wins, foundations, big bets or park |
| **Make the case** | Value as ranges with stated assumptions, risks, human checkpoints, and how roles change |
| **Plan** | What to do now, what that unlocks next, and what needs groundwork first. Each step has an owner and a way to check it is working. Steps are sequenced by dependency, not by calendar dates |

## Working at team, practice or firm level

The same loop works at every level.

- For a **team**, it works on specific processes.
- For a **practice or firm**, the Map step splits the scope into **units** (for example, service
  lines or teams). Each unit gets a one-page brief, and is planned in one of three ways:
  - by its own leader, running the advisor
  - by you, one unit at a time
  - as a first-pass draft the advisor prepares from its knowledge of the field, clearly labelled as
    a draft to check with the people who do the work

  The Prioritize step then **rolls up** all the units' plans into one portfolio, workstreams sequenced by
  dependency, and a value plan.

## What you get

Everything is saved as plain files in your folder, so it's easy to share, version and pick up later.

```
your-folder/
├── transformation-plan.md     # your plan: profile, findings, options, business cases, next steps
├── opportunities.yaml         # every option, scored
├── overlay/                   # optional: your organization's tools, terms and examples
└── units/<unit>/              # at practice or firm level: one folder per unit, same files inside
```

## How the advisor uses evidence

Every example in a business archetype comes from public sources (conferences, regulators, firm
reports, academic studies, trade press) and is fact-checked against them. Each one carries an
**evidence grade**:

| Grade | Meaning |
|---|---|
| **A** | A measured result from a named organization |
| **B** | A named, real deployment without published measurements |
| **C** | A vendor claim or analyst estimate |
| **D** | An idea practitioners discuss, with no public deployment yet |

Each focus area within an archetype is also rated **strong**, **moderate** or **thin** on evidence.
Where evidence is thin, the advisor uses the area for sharper questions and risk awareness, not as
proof. When it quotes a figure, it says who measured it. Most published results in the field are
self-reported or come from vendors.

## Your organization's content

To tailor the advisor without changing the plugin, add an `overlay/` folder next to your plan:

| File | What it does |
|---|---|
| `tool-catalog.yaml` | The AI tools your organization has approved. Recommendations name these |
| `glossary.md` | Your organization's terms |
| `guardrails.md` | Extra rules. These add to the advisor's ground rules and never weaken them |
| `use-cases.yaml` | Internal examples, shown alongside public ones and labelled "internal" |

## Ground rules

The advisor always follows these rules:

- It never recommends actions about named individuals or sets headcount targets for people.
- It always shows how roles would change, and makes the choice explicit: **redeploy** freed-up
  capacity, or **reduce** cost.
- It gives value as ranges with assumptions, never a single ROI number.
- It sequences plans by steps and dependencies, never by artificial deadlines.
- It never invents sources or figures.
- It won't ask for client-confidential data.
- It designs and plans; it doesn't claim to build anything.
- If you're worried about your role, it's honest about that and helps you lead the change.
