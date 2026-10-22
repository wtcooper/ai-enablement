# Tool landscape: enterprise AI assistants, agent features and coding agents

Scope: standalone enterprise AI assistants (browser and desktop), their agent features, and coding agents, local and cloud. Research date: 2026-10-22. Public sources only. Entries are dated, sourced examples and are not endorsements. Runtime classes are those in the library index: personal-assistant, shared-team-skills, workflow-automation, background-agent, managed-agent-runtime.

Sections: 1 Summary; 2 Products; 3 Lead check; 4 How a firm would choose; 5 Gaps; 6 Sources.

## 1. Summary

- Every vendor in this scope now ships the same three layers: a chat assistant, a delegated "do the task" agent, and an asynchronous or always-on agent. They differ on whose identity the agent uses and where its computer runs. OpenAI names them Chat, Work and dots; Anthropic names them Chat, Cowork and (in research preview) Duet. [OPENAI-HELP-WORKCODEX-2026, OPENAI-DOTS-2026, ANTH-HELP-RELNOTES-2026]
- OpenAI dots were introduced on 2026-09-29. Each dot has its own cloud computer. In Enterprise the dots beta is off until a workspace admin enables it. Dots act through the user's connected accounts. "Specialist dots" with their own identity were described as focused enterprise pilots and a planned Microsoft Agent 365 integration, not as generally available. [OPENAI-DOTS-2026, OPENAI-HELP-DOTSSTART-2026]
- Anthropic's always-on analogue, Claude Duet, was opened as a research preview on 2026-10-21 for Pro and Max plans only. No Enterprise availability is stated. [ANTH-DUET-2026]
- Claude Managed Agents is the only product here positioned as a hosted runtime for production agents. It entered public beta on 2026-04-08, not September 2026, and the docs still label it beta. It is not eligible for Zero Data Retention or HIPAA BAA coverage. [ANTH-RELNOTES-API-2026, ANTH-MA-OVERVIEW-2026]
- Audit coverage differs by product. Anthropic's Compliance API returns session transcripts for Cowork, Claude Code and Claude in Chrome (Chrome in beta). OpenAI's Compliance API is documented for ChatGPT Enterprise conversations and GPTs, and its Codex governance page points to it for audit records. GitHub's Agent Control Plane is generally available. [ANTH-COMPSESS-2026, OPENAI-ENTPRIV-2026, OPENAI-DEV-GOV-2026, GH-ACP-2026]
- GitHub hosts Claude and Codex as coding agents beside Copilot, with one admin policy surface. The docs still mark third-party coding agents as public preview. Cursor runs cloud agents in isolated VMs and added Projects (beta) on 2026-09-10. [GH-DOCS-3P-2026, CURSOR-CHANGELOG-2026]
- Several leads were wrong in date or name: GPT-6 Astra (introduced 2026-09-03) and ChatGPT Images 2.5 (2026-09-08) predate DevDay; Managed Agents launched in April; Google's Imagen 4 is shut down in the Gemini API; Nano Banana 2 was deprecated on 2026-10-06 in favour of Nano Banana 2.1. [OPENAI-HELP-RELNOTES-2026, GOOGLE-GEMINI-CHANGELOG-2026]
- Of 27 claims checked: 18 confirmed, 7 partly confirmed, 0 not found, 2 contradicted.

## 2. Products

Field order in each block: 1 what it is; 2 job; 3 runtime class; 4 boundaries (identity, data, persistence); 5 status and date; 6 enterprise controls; 7 pricing model. Where a source does not say, the block says "not stated".

### 2.1 OpenAI

#### ChatGPT Enterprise (Chat, Space, GPT-6 models)

1. The OpenAI workspace product for business accounts. Chat is for "fast, conversational assistance and everyday questions"; Work and Codex sit beside it. [OPENAI-HELP-WORKCODEX-2026]
2. Ask questions of documents and connected apps; draft; collaborate in Space (pages, files, shared context).
3. personal-assistant. Space and shared pages add some shared-team-skills behaviour. Plugin and app connections are shared across Chat, Work, Codex and dots. [OPENAI-HELP-DOTSFAQ-2026]
4. Identity: acts as the signed-in user; apps need the user to authenticate and "ChatGPT respects your organization's existing permissions". Data: uploaded files and connected apps; admins choose enabled apps. Persistence: in-session, plus memory. [OPENAI-ENTPRIV-2026]
5. GPT-6 with Intelligent UI rolled out in the Chat tab from 2026-10-07 for Plus, Pro, Business and Enterprise; "Enterprise availability depends on workspace admin settings". Space: Enterprise sharing is an "opt-in preview" (2026-09-29 note). GPT-6.1 Sol is for Work and Codex, "not yet available in Chat" (2026-09-29). [OPENAI-HELP-RELNOTES-2026, OPENAI-SOL-2026]
6. Enterprise privacy page (updated 2026-01-08): no training on business data by default; admins control retention for Enterprise; deleted conversations removed within 30 days unless legally required; SAML SSO; SOC 2; workspace admins can access an audit log of conversations and GPTs through the Enterprise Compliance API. Model access can be set by role in Workspace settings. [OPENAI-ENTPRIV-2026, OPENAI-HELP-RELNOTES-2026]
7. Per seat for the workspace; credits and "Enterprise pay-as-you-go" for Work and Codex usage; rate cards are on help pages. Figures not recorded here. [OPENAI-HELP-WORKCODEX-2026]

Models named in the leads:
- GPT-6.1 Sol: introduced 2026-09-29, available to Plus, Pro, Business, Enterprise and Edu "in ChatGPT Work and Codex". Enterprise and Edu owners enable it in Workspace settings. Default context in Work and Codex is 500,000 tokens. API ID `gpt-6.1-sol`. The vendor's benchmark claims are its own and are not evaluated here. [OPENAI-SOL-2026, OPENAI-HELP-RELNOTES-2026, OPENAI-HELP-WORKCODEX-2026]
- GPT-6 Astra: introduced 2026-09-03 with access "rolling out to a limited set of organizations"; later available in Work, Codex and GPT-6 Pro (Enterprise depends on model-access permissions). Dots are powered by Astra. [OPENAI-HELP-RELNOTES-2026, OPENAI-HELP-WORKCODEX-2026]
- Image model: the API models page lists "GPT-Image-2.5 Sunburst" and "GPT-Image-2.5 Flare". In ChatGPT the release note on 2026-09-08 calls it "ChatGPT Images 2.5". No source tied either to DevDay. [OPENAI-DEV-MODELS-2026, OPENAI-HELP-RELNOTES-2026]

#### OpenAI dots

1. "Always-on agents in ChatGPT that can take on ongoing work and keep making progress between conversations", powered by GPT-6 Astra, each with its own cloud computer. [OPENAI-HELP-RELNOTES-2026, OPENAI-DOTS-2026]
2. An always-on agent that acts while the user is away: background research, scheduled and event-triggered work, delegation to Work and Codex, messaging via ChatGPT or Slack (Teams is an invite-only alpha).
3. background-agent. The planned specialist dots (own identity, IT-provisioned hardware, systems of record) are closer to managed-agent-runtime but are described only as pilots. [OPENAI-DOTS-2026, OPENAI-LEARN-DOTSADMIN-2026]
4. Identity: a personal dot uses "the connected account" for apps and "the account signed in to the cloud browser" for websites. It can optionally get its own Slack identity. At launch it cannot have its own email address. Specialist dots are described as having "its own identity, credentials, and access". Data: its own cloud computer, connected apps, and optionally the user's computer (off by default; unavailable for dots if any cloud policy has `enforce_residency`). Persistence: always-on; context is kept until the dot is deleted. [OPENAI-LEARN-DOTSADMIN-2026, OPENAI-HELP-DOTSSTART-2026, OPENAI-HELP-DOTSFAQ-2026]
5. Introduced 2026-09-29. Pro and Business Premium: rolling out gradually in eligible markets (Pro excludes the EEA, Switzerland and the UK at launch). "Enterprise users (including Edu and Healthcare) can try the beta when their workspace admin enables it", initially off by default. The Codex work (starting and following Codex threads) is described in the week-of-2026-10-05-to-09 update. [OPENAI-DEVDAY-2026, OPENAI-HELP-DOTSSTART-2026, OPENAI-LEARN-DOTSOCT9-2026]
6. Admin permissions: Use dots; Add dots to Slack and Teams; Allow local computer access; Use custom rules; cloud-computer capabilities (browser, network, computer use, password manager). Enterprise model controls "do not apply to the main dot". Usage visible via the Analytics API (`client_id = DOTS`). Data: no training on Business, Enterprise or Edu content by default. Human review "may occur in limited circumstances" even when model improvement is off. Residency, EKM and ZDR need confirmation with the account team before enabling. Actions pass an automatic "Auto-review"; some steps (for example changing a password) are always handed back to the user. [OPENAI-LEARN-DOTSADMIN-2026, OPENAI-HELP-DOTSFAQ-2026, OPENAI-DOTSSAFETY-2026]
7. First dot included in Pro or Business Premium; usage during the first month "won't count toward" plan allowances, with terms to follow; tasks a dot starts in Codex or Work count toward those limits. Enterprise terms: not stated. [OPENAI-HELP-RELNOTES-2026, OPENAI-DOTS-2026]

Permission model (the "ladder"): custom rules have four behaviours: take action without asking; take action when you say so (the help article says "if pre-approved"); ask before taking action; hand off to you. These sit under mandatory safety requirements that rules cannot override. [OPENAI-LEARN-DOTSCTL-2026, OPENAI-HELP-DOTSSTART-2026]

#### ChatGPT Work and scheduled tasks

1. "Work is an agent designed for longer, multi-step work and finished deliverables", beside Chat and Codex. [OPENAI-HELP-WORKCODEX-2026]
2. Delegate a multi-step task that produces a document, spreadsheet, presentation, report or Site. Scheduled tasks run recurring work and, on eligible plans, work triggered by Gmail, Slack or GitHub events.
3. personal-assistant (Work), background-agent (scheduled tasks and Team Tasks).
4. Identity: Work acts as the user; Team Tasks "run in the cloud through the team's service account and configured app connections". Data: uploaded context and connected tools; local files and desktop apps only in the desktop app with permission. Persistence: cloud Work and scheduled tasks continue without the user. [OPENAI-HELP-WORKCODEX-2026, OPENAI-LEARN-AUTOMATIONS-2026]
5. Present in the 2026-09 documentation. Enterprise and Edu: Work requires Enterprise Key Management (EKM) where it is offered; for eligible workspaces it is "enabled by default for members who use the default workspace role" unless an admin turns it off. [OPENAI-HELP-WORKCODEX-2026]
6. Admin controls: Work Cloud, Work Local and Codex Local are separate permissions; browser use and network access are separate controls. Messages and task context "may be stored in the cloud, even when work runs locally". [OPENAI-HELP-WORKCODEX-2026]
7. Work follows the Codex usage structure (included allowance, then credits); Enterprise pay-as-you-go exists. [OPENAI-HELP-WORKCODEX-2026]

#### Deep Research in ChatGPT

1. Plans, researches and synthesizes a question into a cited report; sources are the public web, uploaded files, chosen sites and enabled apps. [OPENAI-HELP-DEEPRES-2026]
2. Research brief with citations.
3. personal-assistant.
4. Identity: the user's. Data: web plus files plus connected apps; it "does not use app write actions". Persistence: a single run the user can interrupt.
5. Current help article (marked updated 3 days before access).
6. App access follows workspace settings and provider permissions. Retention and training as for ChatGPT Enterprise.
7. Usage varies by plan and is counted in the product.

#### OpenAI Codex: CLI, app and cloud

1. A coding agent for "software development and technical work": a CLI, the ChatGPT desktop app and IDE extension, and Codex Cloud, which runs coding tasks "on OpenAI-managed computers". [OPENAI-HELP-WORKCODEX-2026, OPENAI-LEARN-CODEXCLI-2026]
2. A coding agent working locally (CLI, app) or in the cloud (tasks continue while the computer sleeps).
3. personal-assistant (local CLI and app); background-agent (Codex Cloud and scheduled Codex tasks).
4. Identity: local runs use the user's environment inside a sandbox; cloud tasks use the repositories and access in a published environment. Data: code repositories (GitHub connection) and the environment's secrets and network settings. Locally, "the agent runs with network access turned off" by default, with an OS-enforced sandbox and approval policy. Persistence: in-session locally; asynchronous in the cloud. [OPENAI-LEARN-APPROVALS-2026, OPENAI-LEARN-CODEXCLOUD-2026]
5. Codex Cloud introduced in the 2026-09-29 release notes; available on Plus, Pro, Business, Healthcare, Education and Enterprise per the DevDay recap. [OPENAI-HELP-RELNOTES-2026, OPENAI-DEVDAY-2026]
6. Codex Cloud access is a separate admin permission. Governance page distinguishes analytics (dashboards, Analytics API) from the Compliance API, which "send[s] auditable records to a SIEM or electronic discovery workflow". [OPENAI-DEV-GOV-2026, OPENAI-HELP-WORKCODEX-2026]
7. Included plan allowance then credits; or API pricing when signing in with an API key. [OPENAI-HELP-WORKCODEX-2026]

### 2.2 Anthropic

#### Claude Enterprise (chat, Projects, Compliance API)

1. Anthropic's enterprise plan, bundling Chat, Claude Cowork, Claude Code and connectors with admin controls. [ANTH-ENT-2026]
2. Ask questions of documents and connected sources; produce Office-style deliverables; delegate tasks (Cowork).
3. personal-assistant; Projects add shared-team-skills behaviour (shared knowledge and instructions).
4. Identity: the user's, through connectors with the user's authorization. Data: uploaded files, project files, connected sources. Persistence: in-session; memory off by default for Team and Enterprise (2026-08-25 note). [ANTH-HELP-RELNOTES-2026]
5. Models: Claude Opus 5.5 launched 2026-09-22 (1M-token context by default, 128k max output); Claude Sonnet 5.5 on 2026-09-28; Claude Haiku 5.5 launched 2026-10-07 (1M-token context). Claude Fable 5.1 is also listed as a current model. [ANTH-RELNOTES-API-2026, ANTH-MODELS-2026]
6. Vendor page: "not used to train our models by default"; SSO and domain capture, SCIM and JIT, role-based access control, audit logs, Compliance API, OpenTelemetry and an Analytics API; data retention controls and OTEL monitoring are Enterprise-only; HIPAA-ready configuration (self-serve since 2026-07-14). Projects on Team and Enterprise can be public or private; sharing a project with a group needs Enterprise and is in beta. Claude Design, Slides and Docs are in beta and off by default on Enterprise until an owner enables them. [ANTH-ENT-2026, ANTH-PROJ-2026, ANTH-HELP-RELNOTES-2026]
7. Seat plans; API token prices are published per model (Opus 5.5 $4 / $20 per million input / output tokens; Haiku 5.5 from $0.10 / $0.50). Enterprise seat pricing: not stated on pages read. [ANTH-MODELS-2026]

Compliance API (Enterprise only): session endpoints cover Cowork in Claude Desktop, Claude Code (terminal, Desktop, IDE), Claude for Microsoft 365, Google add-ins, Claude Science and Claude in Chrome. Chrome, Science and Google add-in coverage is in beta. Local-session retention is 6 years by default, or the organization's custom period; 30 days where HIPAA readiness is enabled; ZDR sessions are excluded. Transcripts show requests to the API, "not what occurred on the device". [ANTH-COMPSESS-2026]

#### Claude Cowork, Claude Desktop and computer use

1. "Claude Cowork completes tasks you can steer from anywhere": it works across files and tools and returns work for review. Per the Help Center, "Claude Cowork is now just Claude": a unified chat-plus-Cowork experience, in beta for Enterprise where an admin turns it on. [ANTH-COWORK-2026, ANTH-CUSE-2026]
2. Delegate a multi-step task that produces a deliverable; scheduled recurring tasks; built-in browser.
3. personal-assistant (desktop, local files); background-agent (scheduled and remote Cowork sessions). Runs "remotely (in beta)" on web and mobile since 2026-07-07. [ANTH-HELP-RELNOTES-2026]
4. Identity: the user, through connectors; Claude uses connectors first, then the built-in browser, then screen interaction. Data: the folders and tools the user chooses; "deleting anything needs your approval". Persistence: continues when the laptop closes; scheduled tasks "run with no device online" for remote sessions. [ANTH-COWORK-2026, ANTH-CUSE-2026, ANTH-HELP-RELNOTES-2026]
5. Computer use in Cowork and Claude Code started as a research preview on 2026-03-23; the help article now says "beta for Pro and Max plans" and does not state Enterprise status. The built-in browser is on Pro, Max and Team; Enterprise admins manage it in organization settings. [ANTH-CUSE-2026, ANTH-COWORK-2026]
6. Compliance API session capture for Cowork (local and remote); OpenTelemetry logging; enterprise deployment controls for feature access and spend (blog, 2026-04-09, listed on the product page); private plugin marketplaces. [ANTH-COMPSESS-2026, ANTH-COWORK-2026]
7. Included in plans; usage limits apply. Enterprise terms: not stated.

#### Claude Duet (adjacent, research preview)

1. "A new app where Claude works as a proactive agent", announced 2026-10-21 as a research preview by waitlist, starting with US Pro and Max subscribers; standalone on iOS and Android and on claude.ai. [ANTH-DUET-2026]
2. Always-on assistant for individuals. 3. background-agent. 4. Identity: the user's connected apps; credentials handled "like Claude Managed Agents" so it "never directly sees" passwords. 5. Research preview, 2026-10-21; no Enterprise or Team availability stated. 6. Not stated for enterprises. 7. Included in Pro and Max with shared usage limits.

#### Claude Marketplace

1. A single destination to find "plugins and connectors, agents and products, and service partners", launched 2026-09-23. [ANTH-MKT-BLOG-2026]
2. Procurement and distribution: add connectors and plugins; buy partner agents and products with part of an Anthropic commitment; find consulting partners.
3. Not a runtime class. It is a catalogue. Connectors and plugins feed shared-team-skills; partner products (for example Harvey, Legora, Cursor, Snowflake) are separate products with their own classes.
4. Identity, data and persistence depend on each listing; not stated by the marketplace pages.
5. Launched 2026-09-23. Using Anthropic commitment toward partner products "is in limited preview" and needs eligibility. The product page lists 20 agents and products. [ANTH-MKT-BLOG-2026, ANTH-MKT-PAGE-2026]
6. Admin controls for plugins are in Claude admin settings (private plugin marketplaces, 2026-02-24; skill and plugin security scanning in beta, 2026-08-06). [ANTH-COWORK-2026, ANTH-HELP-RELNOTES-2026]
7. Partner software is bought against committed Anthropic spend ("a portion of your committed Anthropic spend"). [ANTH-MKT-BLOG-2026]

#### Claude Code (Agent Skills and hooks)

1. "An agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools", in the terminal, IDE, desktop app and browser. [ANTH-CC-OVERVIEW-2026]
2. A coding agent working locally or in the cloud; skills and hooks make it consistent across a team.
3. personal-assistant (local); shared-team-skills (SKILL.md skills, hooks, plugins); background-agent (cloud sessions and routines). Managed Agents is the route for hosted production agents.
4. Identity: the user's, with cloud sessions using a GitHub connection the user sets up. Data: the repository and the session transcript; cloud sessions clone the repo into an isolated VM and Anthropic stores the transcript. Persistence: local sessions are in-session; cloud sessions keep running after the laptop closes. [ANTH-CC-WEB-2026, ANTH-CC-DATA-2026]
5. Documented as available; no beta label on these pages (2026-10-22 access). Skills "follow the Agent Skills open standard"; a `SKILL.md` file defines each skill; custom commands have been merged into skills. Hooks are "user-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents" that run at lifecycle events. Cloud sessions: Pro, Max, Team, and Enterprise with premium or Chat + Claude Code seats. [ANTH-CC-SKILLS-2026, ANTH-CC-HOOKS-2026, ANTH-CC-WEB-2026]
6. Commercial terms (Team, Enterprise, API): no training on code or prompts unless the customer opts in; standard retention 30 days; Zero Data Retention available to qualified Enterprise accounts, not included in the standard plan. Session transcripts via the Compliance API. [ANTH-CC-DATA-2026, ANTH-COMPSESS-2026]
7. Included in seat plans, or API tokens on a Console key. [ANTH-CC-WEB-2026]

#### Claude Managed Agents

1. "Pre-built, configurable agent harness that runs in managed infrastructure", "best for long-running tasks and asynchronous work". [ANTH-MA-OVERVIEW-2026]
2. A production agent on private data: sandboxed, stateful sessions with built-in tools, MCP servers, skills, scheduled deployments and permission policies.
3. managed-agent-runtime.
4. Identity: a service identity. Per-user credentials go in workspace-scoped vaults; on Claude Platform on AWS a run can use an IAM role as `execution_identity`. Data: Anthropic-managed cloud sandbox or a self-hosted sandbox "for compliance or data-residency requirements". Persistence: asynchronous, stateful, server-side history, cron-scheduled runs. [ANTH-MA-OVERVIEW-2026, ANTH-MA-SCHED-2026, ANTH-MA-VAULTS-2026]
5. Launched in public beta on 2026-04-08; the overview still says "Claude Managed Agents is in beta" and requires the `managed-agents-2026-04-01` header. Later additions include scheduled deployments, dynamic workflows (beta, 2026-10-09) and the `auto` permission policy (2026-09-10). [ANTH-RELNOTES-API-2026, ANTH-MA-OVERVIEW-2026]
6. Not eligible for ZDR or HIPAA BAA coverage; you can delete sessions and files. Org-level web search and web fetch domain controls apply to sessions (2026-10-20). Permission policies include human approval of tool calls. OpenTelemetry export is in beta (2026-10-14). [ANTH-MA-OVERVIEW-2026, ANTH-RELNOTES-API-2026]
7. Consumption: model tokens at normal rates plus session runtime of $0.08 per session-hour while running. [ANTH-PRICING-2026]

### 2.3 Coding agents

#### GitHub Copilot: agent mode, cloud agent and third-party agents

1. Copilot on GitHub.com can "research a repository, plan changes, and complete multi-step tasks" in a cloud environment (named "Copilot cloud agent" in current docs); agent mode, plan mode and subagents are listed as features in the IDE. Claude and Codex run as additional coding agents. [GH-DOCS-COPILOT-2026, GH-DOCS-3P-2026]
2. A coding agent working locally (IDE agent mode, Copilot CLI, local sandboxing) or in the cloud (assign an issue, get a draft pull request).
3. personal-assistant (agent mode, CLI); background-agent (cloud agent, third-party agents, automations on schedules or repository events).
4. Identity: the agent acts "on behalf of" a user; audit entries carry an agent identifier and the user it acts for. Third-party agents install a GitHub App per agent, visible in the audit log. Data: GitHub repositories. Persistence: cloud sessions are asynchronous; "All agent output appears as draft, reviewable artifacts". [GH-ACP-2026, GH-DOCS-3P-2026, GH-CHANGELOG-2026-02-26]
5. Claude and Codex agents: public preview on 2026-02-04 for Pro+ and Enterprise; expanded to Business and Pro on 2026-02-26; the current docs still say "Third-party coding agents are currently in public preview". Agent Control Plane and Enterprise AI Controls: generally available (changelog dated 2026-02-26). Local sandboxing GA 2026-10-07; computer use in Copilot CLI and the Copilot app in public preview 2026-10-01. [GH-CHANGELOG-2026-02-04, GH-CHANGELOG-2026-02-26, GH-DOCS-3P-2026, GH-ACP-2026, GH-SANDBOX-2026, GH-CU-2026]
6. Admins enable agents at both enterprise and organization level; centralized policy and audit logging via the Agent Control Plane; an enterprise-wide MCP allowlist; agent session activity for the past 24 hours; enterprise-managed settings can require sandboxing. Training and retention terms for Copilot: not retrieved. [GH-CHANGELOG-2026-02-26, GH-ACP-2026, GH-SANDBOX-2026]
7. Seat plans plus AI credits: "Each agent session consumes AI credits based on the model used and the number of tokens processed". During the February preview each session used one premium request. [GH-DOCS-3P-2026, GH-CHANGELOG-2026-02-04]

#### Cursor: cloud agents and Projects

1. An AI coding platform; its cloud agents "run in isolated VMs in the cloud with full development environments". [CURSOR-DOCS-CLOUD-2026]
2. A coding agent working in the cloud (parallel, no need for the laptop) or locally; Projects add a coordinator that delegates to many agents.
3. background-agent. Projects (coordinator, subscriptions to Slack channels or schedules) is the closest to managed-agent-runtime inside a coding tool but is a beta product feature, not a runtime for non-code agents.
4. Identity: the user's source-control connection set up by an account admin; agents work on a separate branch. Data: code repositories, cloned into cloud VMs; "Cloud Agents are the only feature that requires Cursor to store code". Persistence: asynchronous; Projects keep context "over months of work". [CURSOR-DOCS-CLOUD-2026, CURSOR-PRIVACY-2026, CURSOR-CHANGELOG-2026]
5. Projects launched in beta on 2026-09-10 ("rolling out to all users starting today"). Environments API in beta 2026-10-16. Rollouts and Security Review bots for Teams and Enterprise on 2026-09-23. Remote control for local agents 2026-10-06, off by default for Enterprise. [CURSOR-CHANGELOG-2026]
6. Privacy Mode gives ZDR guarantees with most models; "your code is never used for training by Cursor or other AI model providers" under that mode; some models need provider retention and need admin approval for Enterprise; CMEK for Cloud Agent data; US-only data residency for Enterprise at a 10% uplift on eligible model pricing; admin approval needed before cloud agents can start. Enterprise hooks run in the cloud. [CURSOR-PRIVACY-2026, CURSOR-DOCS-CLOUD-2026]
7. Plans with a usage pool; third-party models billed by usage. Figures not recorded here. [CURSOR-PRICING-2026]

### 2.4 Image tools (brief)

- ChatGPT image editing: "ChatGPT Images 2.5", release note 2026-09-08: sharper details, "more precise editing", templates, sketch-to-image, edit and comment on mobile. The API lists GPT-Image-2.5 Sunburst and Flare. Class: personal-assistant. Enterprise: image generation is part of ChatGPT workspaces; image-specific enterprise terms were not retrieved. [OPENAI-HELP-RELNOTES-2026, OPENAI-DEV-MODELS-2026]
- Google Nano Banana: Nano Banana 2 (`gemini-3.1-flash-image`) was deprecated on 2026-10-06 and replaced by Nano Banana 2.1 (`gemini-nano-banana-2.1`), generally available that day. "All generated images include a SynthID watermark." Class: personal-assistant (via the Gemini API); consumer and Workspace surfaces were not checked. [GOOGLE-GEMINI-CHANGELOG-2026, GOOGLE-IMAGEGEN-2026]
- Imagen 4: the Gemini API docs say "Imagen models are shut down"; the changelog announced the 2026-08-17 shutdown on 2026-06-15. Whether Imagen 4 is available elsewhere (for example Vertex AI) was not checked. [GOOGLE-IMAGEN-2026, GOOGLE-GEMINI-CHANGELOG-2026]

## 3. Lead check

Verdicts: confirmed, partly confirmed, not found, contradicted.

| # | Claim | Verdict | Source | Note |
|---|---|---|---|---|
| 1a | DevDay on 2026-09-29; GPT-6.1 Sol introduced | confirmed | OPENAI-DEVDAY-2026, OPENAI-SOL-2026 | The Sol post and recap are dated Sep 29, 2026. |
| 1b | GPT-6 Astra announced at DevDay | partly confirmed | OPENAI-HELP-RELNOTES-2026 | Astra was "introduced" on 2026-09-03 to a limited set of organizations. DevDay material covers Astra Ultrafast and dots powered by Astra. |
| 1c | Image model "GPT-Image-2.5" announced at DevDay | partly confirmed | OPENAI-DEV-MODELS-2026, OPENAI-HELP-RELNOTES-2026 | Model names are GPT-Image-2.5 Sunburst and Flare. ChatGPT Images 2.5 appears on 2026-09-08. No source ties it to DevDay. |
| 2 | Dots launched 2026-09-29 | confirmed | OPENAI-HELP-RELNOTES-2026, OPENAI-DEVDAY-2026 | "Meet your dot" is under September 29, 2026. |
| 3 | 2026-10-09 update lets a dot start Codex threads | confirmed | OPENAI-LEARN-DOTSOCT9-2026 | The page covers "October 5-9, 2026": "Your dot can start work in Codex and follow up on existing threads". The exact day is not stated; the ChatGPT release notes for Oct 9 list only Composer predictions in Codex. |
| 4 | Four-level permission ladder | partly confirmed | OPENAI-LEARN-DOTSCTL-2026, OPENAI-HELP-DOTSSTART-2026 | Four custom-rule behaviours exist, but no source calls them a ladder, and the two sources word the second level differently. Mandatory safety rules sit above them. |
| 5 | Off by default in Enterprise | confirmed | OPENAI-DEVDAY-2026, OPENAI-HELP-DOTSSTART-2026 | "It is off by default"; a beta an admin enables. |
| 6 | ChatGPT Work and scheduled tasks | confirmed | OPENAI-HELP-WORKCODEX-2026, OPENAI-LEARN-AUTOMATIONS-2026 | Work is an agent for multi-step deliverables; scheduled tasks documented, plus Team Tasks. |
| 7 | Deep Research | confirmed | OPENAI-HELP-DEEPRES-2026 | Current help article. |
| 8 | Codex CLI, app and cloud | confirmed | OPENAI-LEARN-CODEXCLI-2026, OPENAI-LEARN-CODEXCLOUD-2026 | Cloud introduced 2026-09-29 in release notes. |
| 9 | Opus 5.5 released 2026-09-22 with 1M-token context | confirmed | ANTH-RELNOTES-API-2026, ANTH-MODELS-2026 | "1M token context window by default". |
| 10 | Haiku 5.5 released 2026-10-07 | confirmed | ANTH-RELNOTES-API-2026, ANTH-HELP-RELNOTES-2026 | Also 1M context. |
| 11 | Claude Projects | confirmed | ANTH-PROJ-2026 | Team and Enterprise visibility and sharing; group sharing is Enterprise beta. |
| 12 | Compliance API audit records for Claude in Chrome and desktop | confirmed | ANTH-COMPSESS-2026, ANTH-RELNOTES-API-2026 | Chrome transcripts in beta from 2026-09-18; Cowork and Claude Code in Claude Desktop are stable. Content is API-visible activity only. |
| 13a | Claude Marketplace launched 2026-09-23 | confirmed | ANTH-MKT-BLOG-2026 | Blog dated September 23, 2026. |
| 13b | 2,000+ MCP connectors and Agent Skills; partner agents | partly confirmed | ANTH-MKT-BLOG-2026, ANTH-MKT-PAGE-2026 | Source says "more than 2,000" connectors and plugins; MCP and Agent Skills are the build standards. Partner agents are bought against committed spend, in limited preview. |
| 14 | Claude Code with Agent Skills (SKILL.md) and hooks | confirmed | ANTH-CC-SKILLS-2026, ANTH-CC-HOOKS-2026 | |
| 15 | Managed Agents launched September 2026 with API beta | contradicted | ANTH-RELNOTES-API-2026, ANTH-MA-OVERVIEW-2026 | Public beta launched 2026-04-08 and remains beta. September 2026 items are feature updates. |
| 16a | Claude Cowork exists | confirmed | ANTH-COWORK-2026, ANTH-HELP-RELNOTES-2026 | Now unified into Claude on some plans. |
| 16b | Claude desktop and computer use | confirmed | ANTH-CUSE-2026 | Beta for Pro and Max in Cowork and Claude Code on the desktop app; Enterprise status not stated. |
| 17 | Copilot issues can be assigned to @copilot, @claude or @codex | partly confirmed | GH-CHANGELOG-2026-02-04, GH-DOCS-3P-2026 | Assign an issue to Claude, Codex, Copilot or all three; PR comments use `@AGENT_NAME`. The literal handles were not confirmed. Still public preview. |
| 18 | Copilot Agent Control Plane | confirmed | GH-ACP-2026, GH-CHANGELOG-2026-02-26 | Generally available per the changelog dated 2026-02-26. |
| 19 | Cursor "background agents" | partly confirmed | CURSOR-DOCS-CLOUD-2026 | Current docs call them "Cloud Agents". The older name was not checked. |
| 20 | Cursor "Projects" beta on 2026-09-10 | confirmed | CURSOR-CHANGELOG-2026 | "Available in beta and rolling out to all users starting today." |
| 21 | ChatGPT image editing | confirmed | OPENAI-HELP-RELNOTES-2026 | Images 2.5 editing, 2026-09-08. |
| 22 | Gemini "Nano Banana 2" | partly confirmed | GOOGLE-GEMINI-CHANGELOG-2026 | Exists; deprecated 2026-10-06; Nano Banana 2.1 is the GA successor. |
| 23 | Imagen 4 | contradicted | GOOGLE-IMAGEN-2026, GOOGLE-GEMINI-CHANGELOG-2026 | Shut down in the Gemini API. Other platforms not checked. |

Totals: 18 confirmed, 7 partly confirmed, 0 not found, 2 contradicted (27 rows).

## 4. How a firm would choose

Questions that separate the products, with the job each one serves.

**Q1. Who is the actor?**
- The user, in their own session: ChatGPT Chat and Work, Claude chat and Cowork, Codex local, Claude Code local, Copilot agent mode. Work product is reviewed by the person who asked for it.
- The user, but while they are away, through their connected accounts: OpenAI dots, Claude Duet (consumer plans only), Cowork scheduled and remote tasks, Codex Cloud, Copilot cloud agent, Cursor cloud agents.
- A named service identity: ChatGPT Team Tasks (the team's service account), Claude Managed Agents (vaults, service credentials, IAM role on AWS), specialist dots (announced as pilots). [OPENAI-LEARN-AUTOMATIONS-2026, ANTH-MA-VAULTS-2026, OPENAI-DOTS-2026]

**Q2. Where must the data live?**
- Microsoft 365 or Google content: Claude connectors (Microsoft 365 write tools from 2026-07-07), ChatGPT apps and plugins. Permission follows the connected account. [ANTH-HELP-RELNOTES-2026, OPENAI-LEARN-DOTSADMIN-2026]
- Uploaded files: Chat, Deep Research, Projects.
- Code repositories: Codex, Claude Code, Copilot, Cursor. Cursor states that cloud agents are the only feature that stores code. [CURSOR-PRIVACY-2026]
- A private network or your own infrastructure: Managed Agents self-hosted sandboxes; Cursor private connectivity and Tailscale; Cursor can route tool execution to hardware you manage. [ANTH-MA-OVERVIEW-2026, CURSOR-DOCS-CLOUD-2026]
- Strict retention requirements: check the exclusions first. Managed Agents has no ZDR or BAA; Claude Code ZDR is arranged per Enterprise organization; dots need residency, EKM and ZDR confirmed with the account team; Compliance API excludes ZDR sessions. [ANTH-MA-OVERVIEW-2026, ANTH-CC-DATA-2026, OPENAI-LEARN-DOTSADMIN-2026, ANTH-COMPSESS-2026]

**Q3. Is the work in-session or must it continue without the user?**
- In-session: Chat, Deep Research, local coding tools.
- Continues while the user is away: Work cloud, scheduled tasks, dots, Cowork remote, Codex Cloud, Claude Code cloud sessions, Copilot cloud agent, Cursor cloud agents and Projects.
- Runs on a schedule with no person starting it: ChatGPT scheduled tasks, Managed Agents scheduled deployments, Cursor Project subscriptions, Copilot automations, Claude Code routines. [OPENAI-LEARN-AUTOMATIONS-2026, ANTH-MA-SCHED-2026, CURSOR-CHANGELOG-2026, GH-DOCS-COPILOT-2026]

**Q4. What can the firm prove afterwards?**
- Transcript export through an API: Anthropic Compliance API (Cowork, Claude Code, Chrome, Microsoft 365 add-ins); OpenAI Compliance API for ChatGPT Enterprise conversations and GPTs; GitHub audit log with agent identifiers. What each export covers differs by product, so a firm should map each tool to the record it keeps before approving it. [ANTH-COMPSESS-2026, OPENAI-ENTPRIV-2026, GH-ACP-2026]
- Dots: the Analytics API reports who uses dots; tasks a dot starts in Work or Codex "appear in their reporting". This page does not say whether the Compliance API captures dot conversations. [OPENAI-LEARN-DOTSADMIN-2026]

**When work should graduate**

- From a personal tool to shared skills: when several people repeat the same prompt, checklist or procedure. Vendors give the packaging: Claude Code skills (`SKILL.md`, Agent Skills standard), plugins and private plugin marketplaces (Claude), ChatGPT plugins and skills, Copilot custom agents and agent skills, Cursor team rules. [ANTH-CC-SKILLS-2026, ANTH-COWORK-2026, OPENAI-LEARN-DOTSADMIN-2026, GH-DOCS-COPILOT-2026]
- From a personal agent to a background agent: when the task is recurring or triggered and the owner is not present. Check that the schedule uses an identity the firm is willing to audit (a user's connected account versus a team service account).
- From a coding or personal tool to a production platform: when the agent needs its own identity, runs on a schedule against client data, must resume after pauses, needs approval checkpoints, or must run in infrastructure the firm controls. The documented hosted options are Claude Managed Agents (beta) and, for dots, the planned specialist dots (pilots). A firm that picks a beta product should record that status and its exclusions (for example no ZDR for Managed Agents). Many agent frameworks sit outside this scope.
- Overlaps: OpenAI's Work and Anthropic's Cowork both deliver multi-step documents; Codex, Claude Code, Copilot and Cursor overlap on cloud coding; GitHub now hosts Claude and Codex agents, and Cursor and Claude Marketplace both appear in the Anthropic catalogue. [ANTH-MKT-PAGE-2026, GH-DOCS-3P-2026]

## 5. Gaps

- openai.com returned HTTP 403 to `curl`; OpenAI pages were read through the `r.jina.ai` text mirror, which dropped the body text of several DevDay recap cards (models, Codex Cloud, Marketplace). The recap's claims were cross-checked against the ChatGPT release notes and learn.chatgpt.com pages. DevDay "ChatGPT Enterprise" announcements beyond dots, Space, Codex Cloud and GPT-6.1 Sol were not read in full.
- No source ties GPT-Image-2.5 to DevDay. No ChatGPT Enterprise terms specific to images were retrieved.
- The ChatGPT Compliance API's coverage of dots, Work and Codex records was not confirmed. The Work cloud security page and Enterprise Work usage pages were not read.
- Claude Enterprise seat pricing and Cowork's Enterprise admin controls page were not read; computer use is not documented for Enterprise.
- Claude Duet's enterprise status is unstated. The Anthropic blog posts for Opus 5.5, Haiku 5.5 and Cowork-chat unification were not opened; release notes and docs were used.
- GitHub: Copilot training and retention terms, agent mode documentation (the guessed page 404ed; only a feature listing was seen), and the literal `@copilot`, `@claude`, `@codex` handles were not confirmed. The preview date for the Agent Control Plane (2025-10-28) came from search-result text, not a page read.
- Cursor: the former name "background agents" was not checked against an older source. Enterprise seat pricing was not recorded.
- Imagen 4 availability on Vertex AI and Gemini consumer or Workspace image surfaces were not checked.
- Two web searches were used (GitHub claims). All vendor claims about performance (benchmarks, cost) are the vendors' own and are not independently evaluated.
- No independent evidence (error rates, override rates, audits) was sought; this file describes product features and stated controls only.

## 6. Sources

All accessed 2026-10-22. Access: full unless noted. Vendor documentation pages without a visible date show the access date as their date.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| OPENAI-DEVDAY-2026 | DevDay 2026 Recap | OpenAI | vendor announcement | https://openai.com/index/devday-2026-recap/ | 2026-09-29 | full via r.jina.ai mirror; some card text missing |
| OPENAI-SOL-2026 | Introducing GPT-6.1 Sol | OpenAI | vendor announcement | https://openai.com/index/introducing-gpt-6-1-sol/ | 2026-09-29 | full via mirror |
| OPENAI-DOTS-2026 | Introducing dots | OpenAI | vendor announcement | https://openai.com/index/introducing-dots/ | 2026-09-29 (date per release notes; page text undated) | full via mirror |
| OPENAI-DOTSSAFETY-2026 | How we build safety, security, and privacy into dots | OpenAI | vendor blog | https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/ | undated | full via mirror |
| OPENAI-HELP-RELNOTES-2026 | ChatGPT release notes | OpenAI Help Center | vendor release notes | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | entries through 2026-10-20 | full via mirror |
| OPENAI-HELP-WORKCODEX-2026 | ChatGPT Work and Codex | OpenAI Help Center | vendor documentation | https://help.openai.com/en/articles/20001275 | undated | full via mirror |
| OPENAI-HELP-DOTSSTART-2026 | Getting started with your dot | OpenAI Help Center | vendor documentation | https://help.openai.com/en/articles/20001530 | undated | full via mirror |
| OPENAI-HELP-DOTSFAQ-2026 | Dots privacy, security, and safety FAQs | OpenAI Help Center | vendor documentation | https://help.openai.com/en/articles/20001529 | undated | full via mirror |
| OPENAI-HELP-DEEPRES-2026 | Deep research in ChatGPT | OpenAI Help Center | vendor documentation | https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt | undated ("updated 3 days ago") | full via mirror |
| OPENAI-ENTPRIV-2026 | Enterprise privacy at OpenAI | OpenAI | vendor policy page | https://openai.com/enterprise-privacy/ | 2026-01-08 | full via mirror |
| OPENAI-DEV-MODELS-2026 | Models (API docs) | OpenAI | vendor documentation | https://developers.openai.com/api/docs/models | undated | full |
| OPENAI-LEARN-DOTSADMIN-2026 | Manage dots permissions and capabilities | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/enterprise/dots-admin-guide.md | undated | full |
| OPENAI-LEARN-DOTSCTL-2026 | Control your dot | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/dots/controls.md | undated | full |
| OPENAI-LEARN-DOTSOCT9-2026 | Create your dot in the ChatGPT mobile app (what's new, Oct 5-9) | OpenAI (learn.chatgpt.com) | vendor release notes | https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026.md | 2026-10-05 to 2026-10-09 | full |
| OPENAI-LEARN-DOTSTASKS-2026 | Tasks and memory (dots) | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/dots/tasks-and-memory.md | undated | full |
| OPENAI-LEARN-AUTOMATIONS-2026 | Scheduled tasks | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/automations.md | undated | full |
| OPENAI-LEARN-CODEXCLOUD-2026 | Codex Cloud | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/cloud.md | undated | full |
| OPENAI-LEARN-CODEXCLI-2026 | Codex CLI | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/cli.md | undated | full |
| OPENAI-LEARN-APPROVALS-2026 | Agent approvals & security | OpenAI (learn.chatgpt.com) | vendor documentation | https://learn.chatgpt.com/docs/agent-approvals-security.md | undated | full |
| OPENAI-DEV-GOV-2026 | Governance (Codex enterprise) | OpenAI developers | vendor documentation | https://developers.openai.com/codex/enterprise/governance.md | undated | full |
| ANTH-RELNOTES-API-2026 | Release notes (Claude Platform) | Anthropic | vendor release notes | https://platform.claude.com/docs/en/release-notes/overview.md | entries through 2026-10-21 | full |
| ANTH-HELP-RELNOTES-2026 | Release notes (Claude apps) | Anthropic Help Center | vendor release notes | https://support.claude.com/en/articles/12138966-release-notes | entries through 2026-10-21 | full |
| ANTH-MODELS-2026 | Models overview | Anthropic | vendor documentation | https://platform.claude.com/docs/en/about-claude/models/overview.md | undated | full |
| ANTH-MKT-BLOG-2026 | Claude Marketplace: one place to discover plugins, agents, and services from our partners | Anthropic (claude.com) | vendor announcement | https://claude.com/blog/claude-marketplace | 2026-09-23 | full |
| ANTH-MKT-PAGE-2026 | Agents and products, Claude Marketplace | Anthropic (claude.com) | vendor product page | https://claude.com/platform/marketplace | undated | full |
| ANTH-COMPSESS-2026 | Retrieve session transcripts (Compliance API) | Anthropic | vendor documentation | https://platform.claude.com/docs/en/manage-claude/compliance-sessions.md | undated | full |
| ANTH-ENT-2026 | Claude Enterprise | Anthropic (claude.com) | vendor product page | https://claude.com/solutions/enterprise | undated | full |
| ANTH-PROJ-2026 | Manage project visibility and sharing | Anthropic Help Center | vendor documentation | https://support.claude.com/en/articles/9519189-what-are-projects | undated | full |
| ANTH-COWORK-2026 | Claude Cowork | Anthropic (claude.com) | vendor product page | https://claude.com/product/cowork | undated; lists posts to 2026-08-26 | full |
| ANTH-CUSE-2026 | Let Claude use your computer in Cowork | Anthropic Help Center | vendor documentation | https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork | undated ("updated over a week ago") | full |
| ANTH-DUET-2026 | Introducing Claude Duet | Anthropic (claude.com) | vendor announcement | https://claude.com/resources/articles/claude-duet | 2026-10-21 | full |
| ANTH-CC-OVERVIEW-2026 | Claude Code overview | Anthropic | vendor documentation | https://code.claude.com/docs/en/overview.md | undated | full |
| ANTH-CC-SKILLS-2026 | Extend Claude with skills | Anthropic | vendor documentation | https://code.claude.com/docs/en/skills.md | undated | full |
| ANTH-CC-HOOKS-2026 | Hooks reference | Anthropic | vendor documentation | https://code.claude.com/docs/en/hooks.md | undated | full |
| ANTH-CC-WEB-2026 | Use Claude Code in the cloud | Anthropic | vendor documentation | https://code.claude.com/docs/en/claude-code-on-the-web.md | undated | full |
| ANTH-CC-DATA-2026 | Data usage (Claude Code) | Anthropic | vendor documentation | https://code.claude.com/docs/en/data-usage.md | undated | full |
| ANTH-MA-OVERVIEW-2026 | Claude Managed Agents overview | Anthropic | vendor documentation | https://platform.claude.com/docs/en/managed-agents/overview.md | undated | full |
| ANTH-MA-SCHED-2026 | Scheduled deployments | Anthropic | vendor documentation | https://platform.claude.com/docs/en/managed-agents/scheduled-deployments.md | undated | full |
| ANTH-MA-VAULTS-2026 | Authenticate with vaults | Anthropic | vendor documentation | https://platform.claude.com/docs/en/managed-agents/vaults.md | undated | full |
| ANTH-PRICING-2026 | Pricing (Claude Managed Agents section) | Anthropic | vendor documentation | https://platform.claude.com/docs/en/about-claude/pricing.md | undated | full |
| GH-CHANGELOG-2026-02-04 | Claude and Codex are now available in public preview on GitHub | GitHub | vendor changelog | https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github/ | 2026-02-04 | full |
| GH-CHANGELOG-2026-02-26 | Claude and Codex now available for Copilot Business & Pro users | GitHub | vendor changelog | https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/ | 2026-02-26 | full |
| GH-ACP-2026 | Enterprise AI Controls & agent control plane now generally available | GitHub | vendor changelog | https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/ | 2026-02-26 (a duplicate post is dated 2026-02-27) | full |
| GH-DOCS-3P-2026 | Third-party coding agents | GitHub Docs | vendor documentation | https://docs.github.com/en/copilot/concepts/agents/about-third-party-agents | undated | full |
| GH-DOCS-COPILOT-2026 | GitHub Copilot on GitHub.com; Copilot features | GitHub Docs | vendor documentation | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | undated | full |
| GH-SANDBOX-2026 | Local sandboxing for GitHub Copilot now generally available | GitHub | vendor changelog | https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available | 2026-10-07 | full |
| GH-CU-2026 | GitHub Copilot can now interact with desktop apps with computer use | GitHub | vendor changelog | https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps | 2026-10-01 | full |
| CURSOR-CHANGELOG-2026 | Cursor changelog (Projects 2026-09-10; Rollouts 2026-09-23; Remote control 2026-10-06; Cloud agent canvases 2026-10-16) | Cursor | vendor changelog | https://cursor.com/changelog | 2026-09-10 to 2026-10-16 | full |
| CURSOR-DOCS-CLOUD-2026 | Cloud Agents | Cursor | vendor documentation | https://cursor.com/docs/cloud-agent | undated | full |
| CURSOR-PRIVACY-2026 | Privacy and data governance | Cursor | vendor documentation | https://cursor.com/docs/enterprise/privacy-and-data-governance | undated | full |
| CURSOR-PRICING-2026 | Pricing | Cursor | vendor product page | https://cursor.com/pricing | undated | full |
| GOOGLE-GEMINI-CHANGELOG-2026 | Gemini API changelog | Google | vendor changelog | https://ai.google.dev/gemini-api/docs/changelog.md.txt | entries 2026-06-15 and 2026-10-06 | full |
| GOOGLE-IMAGEGEN-2026 | Image generation (Nano Banana) | Google | vendor documentation | https://ai.google.dev/gemini-api/docs/image-generation.md.txt | undated | full |
| GOOGLE-IMAGEN-2026 | Imagen | Google | vendor documentation | https://ai.google.dev/gemini-api/docs/imagen.md.txt | undated | full |
