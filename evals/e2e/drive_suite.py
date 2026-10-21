"""Drive a suite handoff session: advisor plan in the workspace -> ai-portfolio -> ai-solution-delivery.
The assistant runs headless (claude -p, resumed); a simulated user (Sonnet) answers. Fictional persona.

Improved copy of 2026-10-21-suite-handoff/drive.py:
- records tool calls (--output-format stream-json --verbose); Skill, Write and Edit calls go into the transcript;
- allows a read-only YAML check (Bash(python3 -c *));
- before the next stage starts, answers the stage's open question (up to MAX_CLOSING replies, while the last
  assistant paragraph has a "?"); if one is still open, the next stage's opener parks it first;
- stage 2 names an AI item past g0 (STAGE2_AI), so the handoff to ai-solution-delivery can be exercised;
- runs only the chosen stages (--stages 2) on an existing workspace; stage 2 alone starts a fresh session;
- can copy a workspace first (--copy-from), so the run can sit outside the git repo;
- appends a block to the run log (drive.log) for every launch.

Usage: python3 drive_suite.py <workspace> <transcript.md> [<drive.log>]
                              [--stages 1,2] [--copy-from <source workspace>] [--stage2-opener "<text>"]
The log defaults to drive.log next to the transcript."""
import argparse, json, pathlib, re, shutil, subprocess, sys, time

REPO = pathlib.Path("/home/user/ai-enablement")
PLUGIN = str(REPO / "plugins/ai-transformation")
PERSONA = """You are role-playing a user talking to an AI assistant. Stay in character. Reply ONLY with what the user
would type: short, concrete, 1-5 sentences, no markdown headings.
Persona (fictional): head of AI at a mid-sized accounting and advisory firm (audit, tax, advisory and client
accounting services; a few hundred people across several offices; private-equity backed; recently acquired two
smaller firms). An AI steering group exists; one enterprise AI assistant is approved; adoption is uneven. The audit
practice already built an AI transformation plan in this folder (transformation-plan.md and units/*/opportunities.yaml).
You want one firm-wide portfolio of AI initiatives, and you want to take the strongest audit opportunity toward a
prototype. Constraints: independence, client data only in approved tools, tax-return information consent rules.
Give plausible numbers when asked; never client names or named staff. Accept reasonable defaults so things move.
If asked whether to continue, choose to continue."""
STAGE1 = ("I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. "
          "Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.")
# The first two runs' stage 2 opener. It named a no-AI item still at intake, so delivery was never reached (review N1).
STAGE2_TOP_ITEM = ("Let's take the highest-priority audit opportunity in the portfolio into prototype. "
                   "Help me decide build versus buy and set up the solution brief.")
STAGE2_AI = ("The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into "
             "discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: "
             "frame it, decide build versus buy, and open the brief as `g1` evidence.")
TURNS = {1: 9, 2: 7}
TOOLS = ["Read", "Glob", "Grep", "Write", "Edit", "Agent", "Task", "Skill", "Bash(python3 -c *)"]
TRANSCRIPT_TOOLS = ("Skill", "Write", "Edit", "MultiEdit")   # copied into the transcript; all calls go to drive.log
MAX_CLOSING = 3
PARK = "Let's park that question for now; we'll come back to it. "

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("workspace"); ap.add_argument("transcript"); ap.add_argument("drivelog", nargs="?")
ap.add_argument("--stages", default="1,2", help="comma-separated stages to run, e.g. 2")
ap.add_argument("--copy-from", help="copy this workspace to <workspace> first (<workspace> must not exist)")
ap.add_argument("--stage2-opener", default=STAGE2_AI, help="stage 2's first user message (default: STAGE2_AI)")
args = ap.parse_args()

WS = pathlib.Path(args.workspace).resolve(); LOG = pathlib.Path(args.transcript).resolve()
RUNLOG = pathlib.Path(args.drivelog).resolve() if args.drivelog else LOG.parent / "drive.log"
STAGES = {1: (STAGE1, TURNS[1]), 2: (args.stage2_opener, TURNS[2])}
try:
    RUN = sorted({int(s) for s in args.stages.split(",") if s.strip()})
except ValueError:
    sys.exit(f"--stages: expected numbers such as 2 or 1,2, got {args.stages!r}")
if not RUN or any(s not in STAGES for s in RUN):
    sys.exit(f"--stages: choose from {sorted(STAGES)}, got {args.stages!r}")


def log(line):
    with RUNLOG.open("a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {line}\n")


def short(tool, inp):
    """One line per tool call: the skill name, the file path or the command."""
    if tool == "Skill":
        return f"{inp.get('skill', '?')} {inp.get('args', '')}".strip()
    if tool == "Bash":
        return str(inp.get("command", ""))[:200]
    path = inp.get("file_path") or inp.get("path") or inp.get("pattern")
    if path:
        try: return str(pathlib.Path(path).resolve().relative_to(WS))
        except ValueError: return str(path)
    return json.dumps(inp)[:200]


def run(cmd, cwd):
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=1500)
    except subprocess.TimeoutExpired as e:
        log(f"TIMEOUT after {e.timeout}s: {cmd[:3]}")
        return subprocess.CompletedProcess(cmd, -1, e.stdout or "", e.stderr or "")


def git(*a):
    p = subprocess.run(["git", "-C", str(REPO), *a], capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else "?"


def assistant_turn(msg, sid):
    """One resumed assistant turn. Returns (session id, final text, [(tool, summary)])."""
    cmd = ["claude", "-p", msg, "--output-format", "stream-json", "--verbose", "--max-turns", "60",
           "--allowedTools", *TOOLS, "--add-dir", PLUGIN, "--permission-mode", "acceptEdits"]
    if sid: cmd += ["--resume", sid]
    t0 = time.time(); p = run(cmd, WS)
    result, calls = "", []
    for line in (p.stdout or "").splitlines():
        try: ev = json.loads(line)
        except ValueError: continue
        sid = ev.get("session_id", sid)
        if ev.get("type") == "assistant":
            for block in (ev.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    calls.append((block.get("name", "?"), short(block.get("name", ""), block.get("input") or {})))
        elif ev.get("type") == "result":
            result = ev.get("result") or ""
            log(f"result: subtype={ev.get('subtype')} turns={ev.get('num_turns')} cost={ev.get('total_cost_usd')}")
    if not result:
        result = ((p.stdout or "") + (p.stderr or ""))[-3000:]
    log(f"assistant turn: exit={p.returncode} {time.time() - t0:.0f}s session={sid} tool_calls={len(calls)}")
    for tool, what in calls:
        log(f"  tool {tool}: {what}")
    if p.stderr:
        log(f"  stderr: {p.stderr.strip()[-500:]}")
    return sid, result, calls


def simulated_reply(transcript):
    turns = [(r, t) for r, t in transcript if r in ("USER", "ASSISTANT")][-8:]
    hist = "\n\n".join(f"{r}: {t}" for r, t in turns)
    p = run(["claude", "-p", f"{PERSONA}\n\nRecent conversation:\n{hist}\n\nWrite the user's next message.",
             "--output-format", "json", "--max-turns", "1", "--model", "sonnet"], "/tmp")
    try: reply = json.loads(p.stdout).get("result", "").strip()
    except ValueError: reply = ""
    log(f"simulated reply: exit={p.returncode} {len(reply)} chars")
    return reply or "Please continue."


def open_question(text):
    """True if the last paragraph of the assistant's reply asks something."""
    paras = [p for p in re.split(r"\n\s*\n", text or "") if p.strip()]
    return bool(paras) and "?" in paras[-1]


def write_transcript(transcript):
    LOG.write_text("\n\n".join(f"### {r}\n{t}" for r, t in transcript))


def turn(msg, sid, transcript, label):
    log(f"{label}: user message {len(msg)} chars")
    sid, result, calls = assistant_turn(msg, sid)
    transcript.append(("USER", msg))
    kept = [f"- {tool}: {what}" for tool, what in calls if tool in TRANSCRIPT_TOOLS]
    if kept:
        transcript.append(("TOOLS", "\n".join(kept)))
    transcript.append(("ASSISTANT", result))
    write_transcript(transcript)
    return sid, result


LOG.parent.mkdir(parents=True, exist_ok=True); RUNLOG.parent.mkdir(parents=True, exist_ok=True)
if args.copy_from:
    if WS.exists():
        sys.exit(f"--copy-from: {WS} already exists; give a new workspace path")
    shutil.copytree(pathlib.Path(args.copy_from).resolve(), WS)
if not WS.is_dir():
    sys.exit(f"workspace not found: {WS}")
if 1 not in RUN and not (WS / "portfolio/portfolio.yaml").exists():
    sys.exit(f"stage 1 is not selected, but {WS}/portfolio/portfolio.yaml does not exist")

log(f"=== launch: {' '.join(sys.argv)}")
log(f"start: workspace={WS} transcript={LOG} plugin={PLUGIN} stages={RUN} tools={TOOLS}")
log(f"plugin commit={git('rev-parse', '--short', 'HEAD')} "
    f"uncommitted plugin files={len(git('status', '--short', '--', PLUGIN).splitlines())}")
if args.copy_from:
    log(f"copied workspace from {pathlib.Path(args.copy_from).resolve()}")
try:
    WS.relative_to(REPO)
    log(f"warning: the workspace is inside the git repo {REPO}; copy it outside with --copy-from")
except ValueError:
    pass

sid, transcript, park = None, [], False
for i, s in enumerate(RUN):
    first, turns = STAGES[s]
    log(f"stage {s}: {turns} turns{' (fresh session)' if sid is None else ''}")
    msg = (PARK + first) if park else first
    for t in range(1, turns + 1):
        sid, last = turn(msg, sid, transcript, f"stage {s} turn {t}")
        if t < turns:
            msg = simulated_reply(transcript)
    park = False
    if i + 1 < len(RUN):
        # Answer the stage's open question before the next stage starts.
        n = 0
        while open_question(last) and n < MAX_CLOSING:
            n += 1
            sid, last = turn(simulated_reply(transcript), sid, transcript, f"stage {s} closing reply {n}")
        park = open_question(last)
        log(f"stage {s} closed after {n} closing replies; question still open: {park}")
transcript.append(("END", f"session {sid}"))
write_transcript(transcript)
log(f"end: session={sid}")
