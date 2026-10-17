"""Drive an end-to-end advisor session: advisor (claude -p, resumed) vs. a simulated audit partner."""
import json, subprocess, sys, pathlib, time

WS = pathlib.Path(sys.argv[1]); LOG = pathlib.Path(sys.argv[2]); MAX = int(sys.argv[3]) if len(sys.argv) > 3 else 40
PERSONA = """You are role-playing a user talking to an AI transformation advisor. Stay in character. Reply ONLY with what
the user would type: short, concrete, 1-5 sentences, no markdown headings.
Persona: audit partner at a mid-tier US accounting firm, leads the SOX/ICFR controls testing practice: 40 people
(4 managers, 10 seniors, 26 staff), about 60 integrated audit clients plus 15 SOX-only internal audit outsourcing
clients. Last year: ~9,000 control tests; staff spend roughly 1.5-2 hours per test on evidence review and documentation;
review notes on ~30% of workpapers; busy season Jan-Mar with heavy overtime; turnover among staff 25%.
Tools: enterprise chat assistant (approved, no client data), audit platform with an analytics module, nothing shared.
Goals: protect margin under fee pressure, handle growth without hiring more staff, cut inspection findings in
controls testing (two PCAOB comments last cycle on ITGC evidence). Constraints: independence, client data only in
approved tools. You are moderately worried about what this means for junior staff. Session goal: a plan to take to
the practice leadership team. Be cooperative; give numbers when asked (invent plausible ones consistent with the
above, never client names). Accept reasonable defaults so the session moves quickly through every phase to a
finished plan. If the advisor asks whether to continue or offers options, choose to continue. If the advisor says the
plan is complete, reply exactly: DONE."""

def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=1500)
    return json.loads(p.stdout) if p.stdout.strip().startswith("{") else {"result": p.stdout + p.stderr}

tools = ["Read", "Glob", "Grep", "Write", "Edit", "Agent", "Task"]
first = "I'm an audit partner leading SOX and ICFR controls testing at a mid-tier firm. Help me figure out where AI could transform how we work, and build a plan I can take to leadership."
sid0 = sys.argv[4] if len(sys.argv) > 4 else None
msg, sid, transcript = (("Let's continue where we left off.", sid0, []) if sid0 else (first, None, []))
for turn in range(MAX):
    cmd = ["claude", "-p", msg, "--output-format", "json", "--max-turns", "60", "--allowedTools", *tools]
    if sid: cmd += ["--resume", sid]
    out = run(cmd, WS); sid = out.get("session_id", sid)
    reply = out.get("result", "")
    transcript += [("USER", msg), ("ADVISOR", reply)]
    LOG.write_text("\n\n".join(f"### {r}\n{t}" for r, t in transcript))
    hist = "\n\n".join(f"{r}: {t}" for r, t in transcript[-8:])
    sim = run(["claude", "-p", f"{PERSONA}\n\nRecent conversation:\n{hist}\n\nWrite the user's next message.",
               "--output-format", "json", "--max-turns", "1", "--model", "sonnet"], "/tmp")
    msg = sim.get("result", "").strip()
    if msg.startswith("DONE") or not msg: break
transcript.append(("END", f"session {sid}, turns {turn+1}"))
LOG.write_text("\n\n".join(f"### {r}\n{t}" for r, t in transcript))
