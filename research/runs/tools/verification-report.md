# Verification report: tool landscape

Verified 2026-10-22 against the cited sources. File:
`plugins/ai-transformation/skills/transformation-advisor/references/library/tool-landscape.md`.

All 66 cited pages were fetched with `curl`. Microsoft blogs and the KPMG release were blocked for direct `curl`, so
they were read through the `r.jina.ai` mirror. Raw HTML was also checked for text the mirror drops (for example,
footnotes and page dates).

## Summary

Each product row in §5 counts as three claim units: name or rename, job or feature, and status with its date. The
counts are approximate.

| | Claim units |
|---|---|
| Checked | ~237 (47 product rows × 3 = 141; ~30 prose claims in §1–§4 and §6; 66 source-table entries) |
| Kept | ~193 |
| Fixed | 40 |
| Removed | 4 |

House style:
- The contents list is present.
- The file is 300 lines.
- No prose line is longer than 120 characters.
- Every cited key resolves in §8, and every source in §8 is cited.

Mapping: the runtime classes match `index.md` §4, and no new vocabulary was added.

Validator: `python3 scripts/validate.py` reports 0 errors (31 warnings, none of them in this file).

## Fixes

| Where | Was | Now | Reason |
|---|---|---|---|
| §1 | "The firm's catalog wins." | "comes first" | Wording the brief bans |
| §1 | "Name products only as dated examples" | "Name current products only…" | Matches the new core rule 6 (coordinator's request) |
| §2 note 1 | Delegation agents (three vendors) "run asynchronously as the user", cited to MS-COWORKGOV | Only Copilot Cowork's automated tasks are said to run as their creator | The source covers Copilot Cowork only |
| §2 note 2 | SaaS agents "inherit its permissions" [GLEAN-MCP] | Run inside the system of record, which "stays the system of action" [MS-D365SKILLS] | The Glean page does not make this claim |
| §2 note 4 | Managed Runtime hosts "apps, not agents" | Hosts "apps and code" | "Not agents" is not stated |
| §2 note 5 | "A skill does not grant access" [SKILLS-SPEC; MCP-INTRO] | Added MS-D365SKILLS (skill = guidance, MCP = tools); last sentence marked *(guidance)* | Neither cited source says this; the spec's `allowed-tools` pre-approves tools |
| §3 identity | "the user owns its actions" | "acts through the user's permissions" | Not stated; the source says tasks run with the user's permissions |
| §3 data, suite | Suite agents "work inside its boundary" (Microsoft and Google) | Cowork stays in the M365 service boundary | The source covers Microsoft only |
| §3 data, system of record | Embedded agent "inherits that system's permissions" (no citation) | "check how it uses its permissions" *(guidance)* | Unsourced |
| §3 data, code | "check whether cloud agents store code" | "check where cloud agents run and what they keep" | The Cursor doc does not discuss storing code; it covers VMs, snapshots and artifacts |
| §4 table | `../../ai-solution-delivery/…/readiness.md` | `../../../ai-solution-delivery/…/readiness.md` | Broken relative link (coordinator's request) |
| §5.1 Copilot Chat | undated docs | docs 2026-09-10 | The page shows a date |
| §5.1 Copilot Notebooks | undated docs | docs 2026-10-05 | The page shows a date |
| §5.1 Copilot Code | docs 2026-10-06 | docs 2026-10-14 | The page has been updated |
| §5.1 Copilot Autopilot | "own Entra identity"; private preview (2026-09-25) | "own identity, memory and computer in the tenant"; private preview (2026-10-08), adds MS-D365SKILLS | The blog does not say Entra. On 09-25 it was "expanding to private preview at the end of the month"; on 10-08 it was "in private preview" |
| §5.1 Copilot Studio | undated | docs 2026-10-20 | The page shows a date |
| §5.1 Gemini in Workspace | undated docs | docs 2026-10-06 | The page reads "Last updated: October 6, 2026" |
| §5.1 Gemini Enterprise app | "(Agent Designer)" | "(no-code agent workbench)" | The FAQ never uses the name "Agent Designer" |
| §5.2 ChatGPT Work | "Documented 2026-09" | "Introduced 2026-07-09" | Release notes, 2026-07-09: "Introducing ChatGPT Work" |
| §5.2 Claude Cowork | "unified with chat, beta for Enterprise" | "merging with chat into one Claude, rolling out to Pro and Max (2026-09-16)" | Release notes and product page ("Claude Cowork is now just Claude"); nothing says "beta for Enterprise" |
| §5.2 Claude Duet | "US Pro and Max only" | "by waitlist, US Pro and Max" | The page says the preview is by waitlist |
| §5.4 Foundry | "Microsoft Foundry Agent Service (formerly Azure AI Foundry)" | "Agent Service in Microsoft Foundry (formerly Azure AI Foundry)" | The rename applies to Foundry, not to Agent Service |
| §5.5 Agent 365 | "including non-Microsoft agents" | "partner agents deployable at launch" | Only partner agents are stated |
| §5.5 Entra Agent ID | "(2026-06-15)" | "(docs 2026-06-15)" | That is the page date, not an availability date |
| §5.5 Google gateway | "other environments early preview" | "Agent Runtime and Gemini Enterprise; GKE, Cloud Run, cross-cloud coming soon (docs 2026-10-21)" | The source says "coming soon" with an early-access sign-up |
| §5.5 AgentCore services | "Part of AgentCore (GA)" | "No preview label (undated docs); AgentCore GA 2025-10-13", adds AWS-AGENTCORE-GA-2025 | The docs give no status for Policy or Registry; GA was announced for AgentCore as a whole |
| §5.5 GitHub | GA (2026-02-26), including MCP allowlist | Adds "MCP allowlists still public preview" | The changelog's heading says "MCP enterprise allow lists remain in public preview" |
| §5.5 Kong | "LLM, MCP and A2A traffic control" | "LLM and MCP traffic control; any API as an MCP server" | A2A is not on the cited page |
| §5.6 Glean | "Permission-enforced search…"; "Documented (Oct 2026)" | "Company search, chat and agents served as MCP tools…"; "docs 2026-10-15" | The source does not describe the search as permission-enforced; the page shows a date |
| §6 dots | "residency, EKM and ZDR must be confirmed" | "residency, EKM or compliance coverage"; adds that Enterprise model controls do not apply to the main dot | ZDR is not in the text; the added point comes from the same page |
| §6 Compliance API | "excludes ZDR sessions and shows API activity only" | "excludes ZDR local sessions; local transcripts omit device activity" | Matches the source's scope |
| §8 dates | MS-CHAT, MS-NBHOW, MS-SPAGENT, MS-SPUPGRADE, MS-CSCUA, GOOGLE-PRIVHUB undated; MS-CODEDOC 2026-10-06; GLEAN "Oct 2026" | 2026-09-10, 2026-10-05, 2026-10-15, 2026-10-16, 2026-10-20, 2026-10-06; 2026-10-14; 2026-10-15 | Dates shown on the pages |

## Removed

| Where | Claim | Reason |
|---|---|---|
| §5.1 Copilot Cowork | "App skill Frontier preview" | Not in MS-COWORKGA, MS-COWORKGOV or any other cited source |
| §5.2 Claude Marketplace | "buying against commitment in limited preview" | The source says the marketplace "is live today"; it does not mention a preview |
| §5.5 Kong | "A2A" | Not on the cited page |
| §6 dots | Human review "may occur in limited circumstances" (quote) | The quote is not in OPENAI-LEARN-DOTSADMIN, or in any fetched page |

## Kept, with notes

- **Gemini Beta setting.** "Skills need the Gemini Beta setting" is confirmed by a footnote in GOOGLE-SKILLS's HTML. The
  text mirror drops that footnote.
- **Cowork DLP.** DLP "coming soon" is kept as dated to GA (2026-06-16). No cited source gives a newer DLP status.
- **Learn page dates.** Learn pages carry more than one date (`ms.date`, `updated_at` and a displayed date). Existing
  dates that match one of these were kept (MS-A365, MSFT-FOUNDRY-AGENTS, MSFT-FOUNDRY-PRIVACY, MSFT-FOUNDRY-WHAT,
  MSFT-FOUNDRY-TOOLBOX).
- **AWS docs date.** AWS-AGENTCORE-DOCS has no visible date (only an HTTP last-modified header), so it stays
  "undated".
- **`use_for` field.** The `use_for` field in §1 was not flagged, as instructed.

## Sources not reached

None. All 66 pages loaded. Direct `curl` was blocked or empty for MS-COWORKGA, MS-MRTBLOG, MS-NEWCOPILOT,
MS-D365SKILLS and KPMG-WORKBENCH; the text mirror served all of them.
