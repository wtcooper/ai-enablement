# Tool landscape

As of **2026-10-22**. Which type of tool fits which job, the questions that decide between types, how work moves
from a personal tool to a production platform, and dated examples of current products. Every skill in the suite
reads it. Keys in brackets are listed in §8. Lines marked *(guidance)* are design advice, not findings from a source.

## Contents

1. [How to use this file](#1-how-to-use-this-file)
2. [Jobs to tool types](#2-jobs-to-tool-types)
3. [The deciding questions](#3-the-deciding-questions)
4. [From prototype to production](#4-from-prototype-to-production)
5. [Current products by type](#5-current-products-by-type)
6. [Notes for professional-services firms](#6-notes-for-professional-services-firms)
7. [Refresh](#7-refresh)
8. [Sources](#8-sources)

## 1. How to use this file

- **The firm's catalog wins.** If `overlay/tool-catalog.yaml` exists, recommend tools from it (each entry's
  `use_for` says what it is for) and flag anything outside it. Data rules come from `overlay/policy.md`.
- **Without a catalog, recommend a runtime class** (`index.md` §4). Name products only as dated examples from §5,
  never as endorsements.
- **Statuses change monthly.** Check the vendor page before relying on a name, label or date below.

## 2. Jobs to tool types

| Job, in a practitioner's words | Tool type | Runtime class | What to check |
|---|---|---|---|
| "Ask questions of a team's documents" | Notebook or grounded assistant on a chosen source set | `personal-assistant`; `shared-team-skills` once shared as a team agent | Source permissions are clean; source limits; whether sharing extends access |
| "Draft and edit inside Word, Excel or Docs" | Office-suite assistant | `personal-assistant` | Licence tier; whether it grounds on firm content or only the web |
| "Produce an Office deliverable end to end" | Suite or standalone assistant that writes the file | `personal-assistant` (note 1) | Where the file lands; labels kept; reviewer before it leaves the team |
| "Delegate a multi-step task" | Delegation agent | `personal-assistant`; `background-agent` when scheduled (note 1) | Acts as the user; approval before sending or changing shared systems; audit coverage |
| "An agent that keeps working while you're away" | Always-on personal agent | `background-agent` | Whose identity it uses; off by default; preview status |
| "Run this every Monday" or "when an email arrives" | Scheduled or triggered task | `background-agent` or `workflow-automation` | Which identity the schedule runs as: a user's account or a service account |
| "Everyone should do this task the same way" | Skills, plugins, shared projects | `shared-team-skills` | Portable format (`SKILL.md`); admin curation; where skills are allowed to run |
| "A departmental bot on business systems" | Low-code agent builder | `workflow-automation` or `managed-agent-runtime` | Maker's versus user's credentials; connectors; who maintains it |
| "An agent inside our CRM, IT service or search tool" | SaaS-embedded agent | `managed-agent-runtime` (note 2) | Runs as the user or as a dedicated agent user; the system's own permissions |
| "Analyse a large document set" | Research notebook, deep research or long-context assistant; a platform at volume | `personal-assistant`; `background-agent` or `managed-agent-runtime` at volume | Source limits; citations to passages; retention; pattern `bulk-transformation` at scale |
| "Write or change code" | Coding agent, local or cloud | `personal-assistant` local; `background-agent` cloud (note 3) | Sandbox and network defaults; where code is stored; review of pull requests |
| "A non-developer builds a small internal app" | App builder plus governed app hosting | `personal-assistant` to build; `managed-agent-runtime` nearest for hosting (note 4) | Where the app runs; sign-in; inventory; who supports it |
| "A production agent on private data" | Pro-code agent platform | `managed-agent-runtime` | Own identity; tenancy and region; evaluation and tracing; retention exclusions |
| "Control which models and tools agents may use" | AI or MCP gateway, agent registry, agent identity | None: a control layer (note 5) | Where it runs; audit logs; which edition holds the feature |
| "Connect an agent to a firm system" | MCP server, private registry | None: a protocol (note 5) | Who hosts the server; private registry; access by user or agent |

**Notes on the nearest class**

1. Delegation agents run asynchronously as the user (Copilot Cowork, ChatGPT Work, Claude Cowork): one-off tasks
   are `personal-assistant`; scheduled or triggered ones are `background-agent` [MS-COWORKGOV-2026].
2. SaaS-embedded agents run inside the vendor's system of record and inherit its permissions [GLEAN-MCP-2026].
3. Coding agents: local sessions are `personal-assistant`, cloud agents `background-agent`, and team skills and
   hooks `shared-team-skills` [ANTH-CC-OVERVIEW-2026; GH-DOCS-COPILOT-2026].
4. Copilot Managed Runtime hosts apps, not agents [MS-MRTBLOG-2026]. `managed-agent-runtime` is the nearest class.
5. Gateways, registries, agent identity and MCP govern or connect agents of every class. Record them as
   infrastructure, not a runtime class. A skill tells an agent how to do a task; MCP gives it access to a system.
   A skill does not grant access [SKILLS-SPEC-2026; MCP-INTRO-2026].

## 3. The deciding questions

**Identity: does it act as the user or with its own identity?**
- As the user: it sees only what the user can see, and the user owns its actions [MS-COWORKGOV-2026].
- As the maker: anyone using a shared agent can act with the author's access; avoid for shared agents [MS-CSCUA-2026].
- With its own identity: actions are attributable to a non-human actor, and someone must own its permissions
  [MSFT-ENTRA-AGENTID-2026; GOOG-AGENTID-2026].

**Data: where does the data live?**
- In the suite (Microsoft 365, Google Workspace): the suite's own assistants and agents keep it inside that boundary.
- In a system of record (CRM, IT service): the vendor's embedded agent inherits that system's permissions.
- In the firm's cloud tenant or private network: a pro-code platform in that tenant [MSFT-FOUNDRY-PRIVACY-2025].
- In code repositories: a coding agent; check whether cloud agents store code [CURSOR-DOCS-CLOUD-2026].

**Persistence: in-session or always-on?**
- In-session: a personal assistant is enough; a person is there to review.
- Continues after the user leaves, as the user: a delegation or background agent; check what records it keeps.
- Runs with nobody starting it, or for hours: a background agent or a managed agent runtime, with checkpoints.

**Who builds and maintains it?**
- The user: personal tools and skills; nothing to hand over, and nothing supported when they leave *(guidance)*.
- A business team on a low-code builder: name an owner and a backup before others depend on it *(guidance)*.
- Developers on a platform: needs **ai-solution-delivery**'s full readiness review.

**Which data classes may go in?** Defer to the overlay policy's `data_classes` and the catalog entry's tier.
- Consumer tier: never `client-confidential` or `regulated`, under the policy's own rule.
- Commercial or firm-controlled tier: only the classes the entry lists; read the exclusions in §6 first.

**Cost model: per user or consumption?**
- Per user: seats or licences; spend is predictable and access follows assignment. Microsoft pairs a per-user
  licence with usage billing for agent features, and the licence is required first [MS-USLUBB-2026].
- Consumption: credits, tokens or runtime hours; spend follows use, so set a budget owner and caps
  [MS-COWORKGA-2026; ANTH-PRICING-2026; AWS-AGENTCORE-RUNTIME-2026].

## 4. From prototype to production

Work usually moves up one step at a time. Move only when a trigger appears *(guidance)*.

| Step | Typical tools | Move on when | What the readiness check needs at this step |
|---|---|---|---|
| 1. Personal tool or coding agent | Chat assistant, notebook, delegation agent, local coding agent | Several people repeat the same prompt or procedure; others start to depend on the output | Approved tool and data class for the work; the user reviews every output |
| 2. Shared skill or team agent | Skills, plugins, shared projects, SharePoint or Agent Builder agents | The work must run on a schedule or trigger; it needs business-system data; a team relies on it daily | Named owner; versioned skill; a small test set; permissions on sources checked |
| 3. Department or background agent | Low-code builders, scheduled tasks, cloud coding agents, SaaS-embedded agents | It must act with its own identity; touch private client data in a controlled tenant; run unattended; or produce records an auditor will read | Which identity the schedule uses; approval before external actions; logs mapped to the record each tool keeps |
| 4. Production platform | Pro-code agent platform, governed app hosting, gateway and registry | Scale, many tools or agents under one policy, or measured quality over time | Full review in `../../ai-solution-delivery/references/method/readiness.md`: ownership and support, change control and rollback, monitoring and cost, evidence and documentation |

Microsoft separates "open build and managed run": apps from Cowork, Code and Copilot Studio publish to Managed
Runtime, which adds Entra sign-in, policy and an inventory [MS-MRTBLOG-2026]. Platforms add asynchronous runs,
per-agent identity, isolation and evaluation [AWS-AGENTCORE-DOCS-2026; MSFT-FOUNDRY-AGENTS-2026]. Record any
beta status and its exclusions when a step relies on one *(guidance)*.

## 5. Current products by type

As of October 2026. Vendors' own names; status in the vendor's words, with the date. Examples, not endorsements.

### 5.1 Office suites and their agent builders

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| Copilot Chat | Microsoft | Ask and draft; grounds on Microsoft 365 data with a Copilot licence | Available to eligible Microsoft 365 users (undated docs) | MS-CHAT-2026 |
| Office in Copilot | Microsoft | Create or update a live Word, Excel or PowerPoint file | Rolling out to Frontier customers (2026-10-09) | MS-OFFICE-2026 |
| Copilot Notebooks | Microsoft | Ask questions of a chosen set of files and pages | Available; no preview label (undated docs) | MS-NBHOW-2026 |
| Copilot Cowork | Microsoft | Delegate a multi-step task; scheduled tasks run as the user | GA (2026-06-16); App skill Frontier preview | MS-COWORKGA-2026, MS-COWORKGOV-2026 |
| Copilot Code | Microsoft | Non-developers build small apps and scripts | Frontier preview (docs 2026-10-06) | MS-CODEDOC-2026 |
| Copilot Autopilot (previously Scout) | Microsoft | Always-on agent with its own Entra identity | Private preview (2026-09-25) | MS-NEWCOPILOT-2026 |
| Copilot Managed Runtime | Microsoft | Governed hosting for apps built in Cowork, Code or Copilot Studio | Public preview (2026-09-25) | MS-MRTBLOG-2026 |
| SharePoint agents; Copilot Agent Builder | Microsoft | Team Q&A on SharePoint content, by each user's permissions | `.agent` files stop after March 2027; new agents in Agent Builder from mid-November 2026 | MS-SPAGENT-2026, MS-SPUPGRADE-2026 |
| Copilot Studio | Microsoft | Low-code departmental agents; computer use where no API exists | Current; acts with maker or end-user credentials | MS-CSCUA-2026 |
| Gemini in Workspace | Google | Draft in Docs, Sheets and Slides; ask across Workspace | Current (undated docs); check each new feature | GOOGLE-PRIVHUB-2026 |
| Gemini Notebook; Gemini Notebook Enterprise (formerly NotebookLM) | Google | Ask a document set with cited answers | Renamed (2026-07-16) | GOOGLE-WSUPDATES-NLM-2026, GOOGLE-GEFAQ-2026 |
| Skills in Google Workspace (replacing Gems) | Google | A team's rules and templates, reused | Needs the Gemini Beta setting (2026-09-16); Gems replaced from 2027-03-01 for business | GOOGLE-SKILLS-2026, GOOGLE-GEMTRANS-2026 |
| Google Workspace Studio | Google | No-code agents on Workspace triggers | GA (2025-12-04) | GOOGLE-STUDIO-2025 |
| Gemini Enterprise app (Agent Designer) | Google | Departmental agents on systems beyond Workspace | Current (undated FAQ) | GOOGLE-GEFAQ-2026 |

### 5.2 Standalone assistants and their agents

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| ChatGPT Enterprise (Chat, Space) | OpenAI | Ask, draft, collaborate; Compliance API for conversations | Current; Space sharing an opt-in preview for Enterprise (2026-09-29) | OPENAI-ENTPRIV-2026, OPENAI-HELP-RELNOTES-2026 |
| ChatGPT Work | OpenAI | Delegate a task that ends in a document, sheet or deck | Documented 2026-09; on by default for eligible Enterprise workspaces | OPENAI-HELP-WORKCODEX-2026 |
| Scheduled tasks; Team Tasks | OpenAI | Recurring work; Team Tasks run as the team's service account | Documented (undated) | OPENAI-LEARN-AUTOMATIONS-2026 |
| Deep research in ChatGPT | OpenAI | A cited report from web, files and apps | Current (help article) | OPENAI-HELP-DEEPRES-2026 |
| dots | OpenAI | Always-on agents, each with its own cloud computer | Introduced 2026-09-29; Enterprise beta, off until an admin enables it | OPENAI-HELP-RELNOTES-2026, OPENAI-HELP-DOTSSTART-2026 |
| Claude Enterprise (chat, Projects) | Anthropic | Ask, draft; shared project knowledge; Compliance API | Current; sharing a project with a group is Enterprise beta | ANTH-ENT-2026 |
| Claude Cowork | Anthropic | Delegate a task; scheduled and remote sessions | Remote sessions beta (2026-07-07); unified with chat, beta for Enterprise | ANTH-COWORK-2026, ANTH-HELP-RELNOTES-2026 |
| Claude Duet | Anthropic | Always-on proactive agent for individuals | Research preview, US Pro and Max only (2026-10-21) | ANTH-DUET-2026 |
| Claude Marketplace | Anthropic | Catalogue of connectors, plugins and partner products | Launched 2026-09-23; buying against commitment in limited preview | ANTH-MKT-BLOG-2026 |

### 5.3 Coding agents

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| GitHub Copilot (agent mode, cloud agent) | GitHub | Code locally in the IDE or CLI; assign an issue, get a draft pull request | Current; computer use in public preview (2026-10-01) | GH-DOCS-COPILOT-2026 |
| Third-party coding agents (Claude, Codex) on GitHub | GitHub | Other vendors' agents under one admin policy | Public preview (since 2026-02-04) | GH-DOCS-3P-2026 |
| Codex (CLI, app, Codex Cloud) | OpenAI | Code locally in a sandbox or in the cloud | Codex Cloud introduced 2026-09-29 | OPENAI-HELP-WORKCODEX-2026, OPENAI-HELP-RELNOTES-2026 |
| Claude Code | Anthropic | Code locally or in cloud sessions; team skills and hooks | Documented, no beta label (read 2026-10-22) | ANTH-CC-OVERVIEW-2026 |
| Cursor cloud agents; Projects | Cursor | Parallel agents in cloud VMs; a coordinator over many agents | Projects beta (2026-09-10) | CURSOR-DOCS-CLOUD-2026, CURSOR-CHANGELOG-2026 |

### 5.4 Pro-code agent platforms

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| Microsoft Foundry Agent Service (formerly Azure AI Foundry) | Microsoft | Production agents with an Entra identity per hosted agent, in the firm's Azure tenant | Service not labelled preview (docs 2026-10-15); voice agents and optimizer preview | MSFT-FOUNDRY-AGENTS-2026, MSFT-FOUNDRY-WHAT-2026 |
| Gemini Enterprise Agent Platform (Agent Runtime, ADK) | Google | Production agents in the firm's Google Cloud project; "an evolution of Vertex AI" | Current (docs 2026-10-21) | GOOG-AGENTPLATFORM-2026 |
| Amazon Bedrock AgentCore | AWS | Production agents in the firm's AWS account, any model or framework | GA (2025-10-13); new runtime described 2026-09-18 | AWS-AGENTCORE-GA-2025, AWS-AGENTCORE-RUNTIME-2026 |
| Claude Managed Agents | Anthropic | Hosted long-running Claude agents; managed or self-hosted sandbox | Public beta since 2026-04-08; still beta | ANTH-MA-OVERVIEW-2026, ANTH-RELNOTES-API-2026 |

### 5.5 Gateways, agent identity, MCP and skills infrastructure

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| Microsoft Agent 365 | Microsoft | Agent registry and control plane, including non-Microsoft agents | GA (2026-05-01), per user | MS-A365-2026 |
| Microsoft Entra Agent ID | Microsoft | Agent identities, delegated or autonomous | Available to all Entra customers (2026-06-15) | MSFT-ENTRA-AGENTID-2026 |
| Foundry Toolbox | Microsoft | Tools exposed through one MCP endpoint with central credentials | Skills and tool search in preview (2026-07-28) | MSFT-FOUNDRY-TOOLBOX-2026 |
| Agent Identity; Agent Gateway; Agent Registry | Google | Per-agent identity; all tool traffic blocked until policy allows | Gateway for agents on the platform; other environments early preview | GOOG-AGENTID-2026, GOOG-GATEWAY-2026 |
| AgentCore Gateway, Identity, Policy, Registry | AWS | APIs as MCP tools; rules checked before every tool call | Part of AgentCore (GA) | AWS-AGENTCORE-DOCS-2026 |
| Agent Control Plane; Enterprise AI Controls | GitHub | Policy and audit for coding agents; MCP allowlist | GA (2026-02-26) | GH-ACP-2026 |
| LiteLLM (MCP Gateway); LiteLLM Lens | LiteLLM | Self-hosted model and MCP gateway; trace analysis | Gateway documented; Lens early access (2026-10-01) | LITELLM-MCP-2026, LITELLM-LENS-LAUNCH-2026 |
| TrueFoundry MCP Gateway | TrueFoundry | MCP gateway with registry; VPC, on-premises or air-gapped | Documented (undated) | TF-MCP-DOCS-2026 |
| Bifrost | Maxim AI | Open-source AI gateway with MCP; no tool auto-execution by default | Documented (undated); edition split unclear | BIFROST-MCP-2026 |
| Kong AI Gateway | Kong | LLM, MCP and A2A traffic control | MCP proxy is enterprise-only; MCP Registry tech preview | KONG-MCP-2026 |
| Prisma AIRS with Portkey | Palo Alto Networks | AI gateway inside an AI security platform | Acquisition completed 2026-05-29; integration described in future tense | PANW-CLOSE-2026 |
| Model Context Protocol | Open standard | Connects AI applications to tools and data | Latest spec version 2026-07-28 | MCP-INTRO-2026 |
| MCP Registry | Open standard | Public catalog of MCP servers; no private servers | Preview | MCP-REGISTRY-2026 |
| Agent Skills (`SKILL.md`) | Open standard, from Anthropic | Packaged instructions an agent loads when relevant | Published as an open standard 2025-12-18 | ANTHROPIC-SKILLS-2025, SKILLS-SPEC-2026 |

### 5.6 SaaS-embedded agents

| Product | Vendor | Job it serves | Status (date) | Source |
|---|---|---|---|---|
| Agentforce | Salesforce | Service, sales and employee agents on CRM data | Current; consumption or per-user pricing | SF-AGENTFORCE-2026, SF-PRICING-2026 |
| AI Agents | ServiceNow | Agents on IT, HR, customer and security workflows | Current (undated product page) | SN-AIAGENTS-2026 |
| Glean (MCP server, MCP Gateway) | Glean | Permission-enforced search of company content, served to other hosts | Documented (Oct 2026) | GLEAN-MCP-2026 |
| Dynamics 365 CRM skills | Microsoft | CRM context in Cowork, Code and Autopilot | GA (2026-10-08) | MS-D365SKILLS-2026 |

## 6. Notes for professional-services firms

**Client data and the overlay policy.** The policy's data classes and the catalog decide what goes in, not the
vendor's marketing. Before approving client data, read each product's exclusions:
- Claude Managed Agents is not eligible for Zero Data Retention or HIPAA BAA coverage [ANTH-MA-OVERVIEW-2026].
- OpenAI says residency, EKM and ZDR must be confirmed with the account team before enabling dots, and human
  review "may occur in limited circumstances" [OPENAI-LEARN-DOTSADMIN-2026].
- Anthropic's Compliance API excludes ZDR sessions and shows API activity, "not what occurred on the device"
  [ANTH-COMPSESS-2026].
- Foundry preview features "may not support customer managed keys" [MSFT-FOUNDRY-PRIVACY-2025].
- At general availability Cowork listed DLP as "coming soon" [MS-COWORKGA-2026]. Preview and new features often
  lag on controls; recheck before client use *(guidance)*.

**Questions to ask a vendor on independence and confidentiality** *(guidance)*. Record answers in
`overlay/vendors/` through **ai-governance** (`vendor-evaluation.md`, `professional-duties.md`).
- Is the vendor, its parent or a partner listed in its marketplace an audit or attest client of the firm?
- Does the purchase route (for example partner products bought against committed spend) create a business
  relationship that independence rules restrict [ANTH-MKT-BLOG-2026]?
- Who can see prompts and outputs (human reviewers, sub-processors), and is any content used for training?
- What is retained, in which region, for how long, and who can retrieve it for a regulator, client or court?
- Does the audit record show the agent's identity separately from the user's?
- Will we be told before the model, region or terms change?

**Field-specific tools** (audit, tax, legal) are not listed here; they live in the archetypes' use cases.

**Public examples of firms building on these platforms** (both self-reported announcements):
- EY (2026-04-07): a multi-agent framework "integrated with Microsoft Azure, Microsoft Foundry and Microsoft
  Fabric" in EY Canvas for Assurance; it does not say which Foundry services [EY-AUDIT-2026].
- KPMG (2025-06-18): KPMG Workbench, "built on Microsoft Azure AI Foundry Services" [KPMG-WORKBENCH-2025].
- None verified for an accounting, tax or law firm on Bedrock AgentCore or the Gemini Enterprise Agent Platform,
  for a law firm on any platform, or for a mid-size firm.

## 7. Refresh

Keep the date at the top. Change it only after a full recheck.

| What | How often | What to look for |
|---|---|---|
| Every preview, beta and early-access status in §5 | Monthly | GA, retirement, rename, change of plan eligibility |
| Known dates | When the date passes | SharePoint agents move to Agent Builder (mid-November 2026); Gems replaced (2027-03-01); `.agent` files stop (end of March 2027) |
| Identity and data exclusions in §3 and §6 | Quarterly | ZDR, BAA, residency, compliance-export coverage |
| Pricing models | Quarterly, and at every vendor billing announcement | Per-user versus consumption split; required licences |
| The whole file | Every six months, or when a new tool type appears | New jobs, new types, runtime-class fit |

How: rerun the three research sweeps (suites; assistants and coding; platforms and infrastructure) with a lead
check, keep only confirmed or partly confirmed findings, then update §5 and §8 and the date.

## 8. Sources

All accessed 2026-10-22. Access: `full` = page text read (sometimes via a text mirror); `partial` = part loaded.

| Key | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MS-NEWCOPILOT-2026 | Introducing the new Copilot with Home, Code and Autopilot | Microsoft | vendor blog | https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/ | 2026-09-25 | full |
| MS-CHAT-2026 | Overview of Microsoft Copilot Chat | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/copilot/overview | undated | full |
| MS-OFFICE-2026 | Introducing Office in the new Microsoft Copilot app | Microsoft Tech Community | vendor blog | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-office-in-the-new-microsoft-copilot-app/4561230 | 2026-10-09 | full |
| MS-NBHOW-2026 | How Microsoft Copilot Notebooks works | Microsoft Support | vendor docs | https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works | undated | full |
| MS-COWORKGA-2026 | Copilot Cowork is now generally available | Microsoft | vendor blog | https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/ | 2026-06-16 | full |
| MS-COWORKGOV-2026 | Manage Copilot Cowork for your organization | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | 2026-09-14 | full |
| MS-CODEDOC-2026 | Copilot Code overview (Frontier) | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/copilot/code/overview | 2026-10-06 | full |
| MS-MRTBLOG-2026 | Build where you want, run with confidence | Microsoft | vendor blog | https://aka.ms/CopilotManagedRuntime-Blog | 2026-09-25 | full |
| MS-SPAGENT-2026 | Manage access to agents in SharePoint | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/sharepoint/manage-access-agents-in-sharepoint | undated | full |
| MS-SPUPGRADE-2026 | Upgrade agents in SharePoint and OneDrive | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/sharepoint/upgrade-sharepoint-agents | undated | full |
| MS-CSCUA-2026 | Automate web and desktop apps with computer use | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use | undated | full |
| MS-USLUBB-2026 | Understanding the user subscription license and usage-based billing | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/microsoft-365/copilot/user-subscription-license-usage-based-billing | 2026-10-06 | full |
| MS-A365-2026 | Overview of Microsoft Agent 365 | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/microsoft-agent-365/overview | 2026-08-20 | full |
| MS-D365SKILLS-2026 | Bring Microsoft Dynamics 365 into the flow of work with 30 new CRM skills | Microsoft | vendor blog | https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/10/08/bring-microsoft-dynamics-365-into-the-flow-of-work-with-30-new-crm-skills/ | 2026-10-08 | full |
| MSFT-ENTRA-AGENTID-2026 | What are agent identities? | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id | 2026-06-15 | full |
| MSFT-FOUNDRY-AGENTS-2026 | What is Microsoft Foundry Agent Service? | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview | 2026-10-15 | full |
| MSFT-FOUNDRY-WHAT-2026 | What is Microsoft Foundry? | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-foundry | 2026-08-13 | full |
| MSFT-FOUNDRY-TOOLBOX-2026 | What is Toolbox in Microsoft Foundry? | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/tool-catalog | 2026-07-28 | full |
| MSFT-FOUNDRY-PRIVACY-2025 | Data, privacy, and security for Foundry Agent Service | Microsoft Learn | vendor docs | https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/agents/data-privacy-security | 2025-11-19 | full |
| GOOGLE-PRIVHUB-2026 | Generative AI in Google Workspace Privacy Hub | Google Workspace Help | vendor docs | https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub | undated | full |
| GOOGLE-WSUPDATES-NLM-2026 | NotebookLM is now Gemini Notebook | Google Workspace Updates | vendor blog | https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html | 2026-07-16 | full |
| GOOGLE-GEFAQ-2026 | Gemini Enterprise app FAQs | Google Cloud | vendor docs | https://cloud.google.com/gemini-enterprise/faq | undated | full |
| GOOGLE-SKILLS-2026 | Teach Gemini your team's know-hows with skills in Google Workspace | Google Workspace Blog | vendor blog | https://workspace.google.com/blog/product-announcements/teach-gemini-your-teams-know-hows-with-skills-in-google-workspace | 2026-09-16 | full |
| GOOGLE-GEMTRANS-2026 | About the transition from Gems to skills | Google Workspace Help | vendor docs | https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills | 2026-09-30 | full |
| GOOGLE-STUDIO-2025 | Introducing Google Workspace Studio | Google Workspace Blog | vendor blog | https://workspace.google.com/blog/product-announcements/introducing-google-workspace-studio-agents-for-everyday-work | 2025-12-04 | full |
| GOOG-AGENTPLATFORM-2026 | Agent Platform overview | Google Cloud | vendor docs | https://cloud.google.com/agent-builder/overview | 2026-10-21 | full |
| GOOG-AGENTID-2026 | Use Agent Identity with Agent Runtime | Google Cloud | vendor docs | https://cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity | 2026-10-21 | full |
| GOOG-GATEWAY-2026 | Agent Gateway overview | Google Cloud | vendor docs | https://cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview | 2026-10-21 | full |
| OPENAI-ENTPRIV-2026 | Enterprise privacy at OpenAI | OpenAI | vendor policy | https://openai.com/enterprise-privacy/ | 2026-01-08 | full |
| OPENAI-HELP-RELNOTES-2026 | ChatGPT release notes | OpenAI Help Center | vendor release notes | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | to 2026-10-20 | full |
| OPENAI-HELP-WORKCODEX-2026 | ChatGPT Work and Codex | OpenAI Help Center | vendor docs | https://help.openai.com/en/articles/20001275 | undated | full |
| OPENAI-LEARN-AUTOMATIONS-2026 | Scheduled tasks | OpenAI | vendor docs | https://learn.chatgpt.com/docs/automations.md | undated | full |
| OPENAI-HELP-DEEPRES-2026 | Deep research in ChatGPT | OpenAI Help Center | vendor docs | https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt | undated | full |
| OPENAI-HELP-DOTSSTART-2026 | Getting started with your dot | OpenAI Help Center | vendor docs | https://help.openai.com/en/articles/20001530 | undated | full |
| OPENAI-LEARN-DOTSADMIN-2026 | Manage dots permissions and capabilities | OpenAI | vendor docs | https://learn.chatgpt.com/docs/enterprise/dots-admin-guide.md | undated | full |
| ANTH-ENT-2026 | Claude Enterprise | Anthropic | vendor product page | https://claude.com/solutions/enterprise | undated | full |
| ANTH-COWORK-2026 | Claude Cowork | Anthropic | vendor product page | https://claude.com/product/cowork | undated | full |
| ANTH-HELP-RELNOTES-2026 | Release notes (Claude apps) | Anthropic Help Center | vendor release notes | https://support.claude.com/en/articles/12138966-release-notes | to 2026-10-21 | full |
| ANTH-DUET-2026 | Introducing Claude Duet | Anthropic | vendor announcement | https://claude.com/resources/articles/claude-duet | 2026-10-21 | full |
| ANTH-MKT-BLOG-2026 | Claude Marketplace | Anthropic | vendor announcement | https://claude.com/blog/claude-marketplace | 2026-09-23 | full |
| ANTH-COMPSESS-2026 | Retrieve session transcripts (Compliance API) | Anthropic | vendor docs | https://platform.claude.com/docs/en/manage-claude/compliance-sessions.md | undated | full |
| ANTH-CC-OVERVIEW-2026 | Claude Code overview | Anthropic | vendor docs | https://code.claude.com/docs/en/overview.md | undated | full |
| ANTH-MA-OVERVIEW-2026 | Claude Managed Agents overview | Anthropic | vendor docs | https://platform.claude.com/docs/en/managed-agents/overview.md | undated | full |
| ANTH-RELNOTES-API-2026 | Release notes (Claude Platform) | Anthropic | vendor release notes | https://platform.claude.com/docs/en/release-notes/overview.md | to 2026-10-21 | full |
| ANTH-PRICING-2026 | Pricing (Claude Managed Agents section) | Anthropic | vendor docs | https://platform.claude.com/docs/en/about-claude/pricing.md | undated | full |
| ANTHROPIC-SKILLS-2025 | Introducing Agent Skills (update of 2025-12-18) | Anthropic | vendor announcement | https://www.anthropic.com/news/skills | 2025-12-18 | full |
| GH-DOCS-COPILOT-2026 | GitHub Copilot on GitHub.com | GitHub Docs | vendor docs | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | undated | full |
| GH-DOCS-3P-2026 | Third-party coding agents | GitHub Docs | vendor docs | https://docs.github.com/en/copilot/concepts/agents/about-third-party-agents | undated | full |
| GH-ACP-2026 | Enterprise AI Controls & agent control plane now generally available | GitHub | vendor changelog | https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/ | 2026-02-26 | full |
| CURSOR-DOCS-CLOUD-2026 | Cloud Agents | Cursor | vendor docs | https://cursor.com/docs/cloud-agent | undated | full |
| CURSOR-CHANGELOG-2026 | Cursor changelog | Cursor | vendor changelog | https://cursor.com/changelog | 2026-09-10 to 2026-10-16 | full |
| AWS-AGENTCORE-DOCS-2026 | What is Amazon Bedrock AgentCore? | AWS | vendor docs | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | undated | full |
| AWS-AGENTCORE-GA-2025 | Amazon Bedrock AgentCore: Now generally available | AWS | vendor blog | https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/ | 2025-10-13 | full |
| AWS-AGENTCORE-RUNTIME-2026 | The new AgentCore runtime: Elastic, optimized, and consistently fast starts | AWS | vendor blog | https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/ | 2026-09-18 | full |
| MCP-INTRO-2026 | What is the Model Context Protocol? | modelcontextprotocol.io | standard | https://modelcontextprotocol.io/introduction | spec 2026-07-28 | full |
| MCP-REGISTRY-2026 | The MCP Registry | modelcontextprotocol.io | standard | https://modelcontextprotocol.io/registry/about | undated | full |
| SKILLS-SPEC-2026 | Agent Skills specification | agentskills.io | standard | https://agentskills.io/specification | undated | full |
| LITELLM-MCP-2026 | MCP Overview | LiteLLM | vendor docs | https://docs.litellm.ai/docs/mcp | undated | full |
| LITELLM-LENS-LAUNCH-2026 | LiteLLM Lens launch post | LiteLLM | vendor blog | https://docs.litellm.ai/blog/litellm-lens-launch | 2026-10-01 | full |
| TF-MCP-DOCS-2026 | TrueFoundry MCP Gateway | TrueFoundry | vendor docs | https://docs.truefoundry.com/gateway/mcp-overview | undated | full |
| BIFROST-MCP-2026 | MCP Gateway overview | Maxim AI (Bifrost) | vendor docs | https://docs.getbifrost.ai/mcp/overview | undated | full |
| KONG-MCP-2026 | MCP Traffic Gateway | Kong | vendor docs | https://developer.konghq.com/mcp/ | undated | full |
| PANW-CLOSE-2026 | Palo Alto Networks Completes Acquisition of Portkey | Palo Alto Networks | press release | https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-completes-acquisition-of-portkey-to-secure-ai-agents | 2026-05-29 | full |
| GLEAN-MCP-2026 | About Glean MCP server | Glean | vendor docs | https://docs.glean.com/administration/platform/mcp/about | Oct 2026 | full |
| SF-AGENTFORCE-2026 | Agentforce: The AI Agent Platform | Salesforce | vendor product page | https://www.salesforce.com/agentforce/ | undated | partial |
| SF-PRICING-2026 | Agentforce Pricing | Salesforce | vendor product page | https://www.salesforce.com/agentforce/pricing/ | undated | full |
| SN-AIAGENTS-2026 | AI Agents | ServiceNow | vendor product page | https://www.servicenow.com/products/ai-agents.html | undated | partial |
| EY-AUDIT-2026 | EY launches enterprise-scale agentic AI to redefine the audit experience | EY | firm press release | https://www.ey.com/en_us/newsroom/2026/04/ey-launches-enterprise-scale-agentic-ai-to-redefine-the-audit-experience-for-the-ai-era | 2026-04-07 | full |
| KPMG-WORKBENCH-2025 | KPMG Launches KPMG Workbench: A Multi-Agent AI Platform | KPMG International | firm press release | https://www.newsfilecorp.com/release/255985/KPMG-Launches-KPMG-Workbench-A-MultiAgent-AI-Platform-Transforming-Client-Delivery-and-Ways-of-Working-Across-the-Global-Organization | 2025-06-18 | full |
