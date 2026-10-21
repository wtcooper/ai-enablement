"""Drive a suite handoff session: advisor plan in the workspace -> ai-portfolio -> ai-solution-delivery.
The assistant runs headless (claude -p, resumed); a simulated user (Sonnet) answers. Fictional persona.

Improved copy of 2026-10-21-suite-handoff/drive.py:
- records tool calls (--output-format stream-json --verbose); Skill and Write calls go into the transcript;
- allows a read-only YAML check (Bash(python3 -c *));
- answers the last question of a stage before the next stage starts;
- writes a run log (drive.log).

Usage: python3 drive_suite.py <workspace> <transcript.md> [<drive.log>]
The log defaults to drive.log next to the transcript."""
import json, subprocess, sys, pathlib, time

WS = pathlib.Path(sys.argv[1]).resolve(); LOG = pathlib.Path(sys.argv[2]).resolve()
RUNLOG = pathlib.Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else LOG.parent / "drive.log"
PLUGIN = "/home/user/ai-enablement/plugins/ai-transformation"
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
STAGES = [
  ("I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. "
   "Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.", 9),
  ("Let's take the highest-priority audit opportunity in the portfolio into prototype. "
   "Help me decide build versus buy and set up the solution brief.", 7),
]
TOOLS = ["Read", "Glob", "Grep", "Write", "Edit", "Agent", "Task", "Skill", "Bash(python3 -c *)"]
TRANSCRIPT_TOOLS = ("Skill", "Write")      # tool calls copied into the transcript; all calls go to drive.log


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
    return sid


RUNLOG.write_text("")
log(f"start: workspace={WS} transcript={LOG} plugin={PLUGIN} tools={TOOLS}")
sid, transcript = None, []
for s, (first, turns) in enumerate(STAGES, 1):
    log(f"stage {s}: {turns} turns")
    msg = first
    for t in range(1, turns + 1):
        sid = turn(msg, sid, transcript, f"stage {s} turn {t}")
        msg = simulated_reply(transcript)
    if s < len(STAGES):
        # Answer the stage's last question before the next stage starts.
        sid = turn(msg, sid, transcript, f"stage {s} closing reply")
transcript.append(("END", f"session {sid}"))
write_transcript(transcript)
log(f"end: session={sid}")
