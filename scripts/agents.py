#!/usr/bin/env python3
"""Claim-based workboard and isolated OpenCode workers. Standard library only."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODEL = "zai-coding-plan/glm-5.3-flash"
REFUSED = 3
# About a dozen simultaneous GLM workers hit z.ai 429 (code 1302) on 2026-10-19.
DEFAULT_MAX_CONCURRENT = 6
RATE_LIMIT_ATTEMPTS = 4
RESUME_NOTE = ("\n\n## Resumed run\n\nYour previous attempt was interrupted (provider rate "
               "limit, usage quota, or a supervisor failure). Inspect `git status`, `git log` and your output paths first; keep "
               "and continue existing work rather than starting over.\n")


def git(*args, cwd=None, check=True):
    return subprocess.run(["git", *args], cwd=cwd or ROOT, text=True,
                          capture_output=True, check=check)


def main_root():
    result = git("rev-parse", "--path-format=absolute", "--git-common-dir", check=False)
    return Path(result.stdout.strip()).parent if result.returncode == 0 else ROOT


def tasks():
    records = [json.loads(line) for line in (ROOT / "WORKBOARD.jsonl").read_text().splitlines()
               if line.strip()]
    book = {row["id"]: row for row in records}
    if len(book) != len(records):
        raise ValueError("duplicate task ID")
    for row in records:
        missing = [key for key in ("id", "title", "blocked_by", "owns", "brief", "done_when")
                   if key not in row]
        if missing:
            raise ValueError(f"task {row.get('id', '?')} lacks {', '.join(missing)}")
        if not re.fullmatch(r"[a-z][a-z0-9-]*", row["id"]):
            raise ValueError("invalid task ID")
        for name in row["owns"]:
            if (Path(name).is_absolute() or ".." in Path(name).parts or not name.strip("/")
                    or "." in name.split("/") or "//" in name):
                raise ValueError(f"unsafe owned path: {name}")
        for dep in row["blocked_by"]:
            if dep not in book:
                raise ValueError(f"unknown dependency: {dep}")
    def visit(tid, trail):
        if tid in trail:
            raise ValueError(f"dependency cycle: {tid}")
        for dep in book[tid]["blocked_by"]:
            visit(dep, trail | {tid})
    for tid in book:
        visit(tid, set())
    return book


def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def atomic_json(destination, value):
    with tempfile.NamedTemporaryFile(mode="w", dir=destination.parent, delete=False) as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")
        temp = handle.name
    os.replace(temp, destination)


def atomic_text(destination, text):
    """Replace destination in one step so concurrent workers never tear it."""
    with tempfile.NamedTemporaryFile(mode="w", dir=destination.parent, delete=False) as handle:
        handle.write(text)
        temp = handle.name
    os.replace(temp, destination)


@contextmanager
def locked_state():
    folder = main_root() / ".agent-runtime" / "coordination"
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / "lock").open("a+") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        target = folder / "state.json"
        state = json.loads(target.read_text()) if target.exists() else {}
        yield state
        atomic_json(target, state)


def snapshot():
    target = main_root() / ".agent-runtime" / "coordination" / "state.json"
    return json.loads(target.read_text()) if target.exists() else {}


def state_of(tid, book, state):
    explicit = state.get(tid, {}).get("status", "open")
    if explicit != "open":
        return explicit
    return "blocked" if any(state.get(dep, {}).get("status") != "done"
                            for dep in book[tid]["blocked_by"]) else "open"


def overlaps(left, right):
    a, b = Path(left).parts, Path(right).parts
    return a[:len(b)] == b or b[:len(a)] == a


def assert_claimable(tid, book, state):
    if tid not in book:
        raise ValueError(f"unknown task: {tid}")
    if state_of(tid, book, state) != "open":
        raise ValueError(f"{tid} is {state_of(tid, book, state)}")
    for other, record in state.items():
        if other not in book or record.get("status") not in {"claimed", "review"}:
            continue  # a claim for a task no longer on the board cannot be overlap-checked
        if any(overlaps(a, b) for a in book[tid]["owns"] for b in book[other]["owns"]):
            raise ValueError(f"file ownership overlaps {other}, held by {record['agent']}")


def transition(action, tid, agent, notes="", extra=None):
    book = tasks()
    if tid not in book:
        raise ValueError(f"unknown task: {tid}")
    with locked_state() as state:
        record = state.get(tid, {})
        if action == "claim":
            assert_claimable(tid, book, state)
            record = {"status": "claimed", "agent": agent, "claimed_at": timestamp()}
        else:
            if record.get("agent") != agent:
                raise ValueError("claim belongs to another agent or does not exist")
            permitted = {"heartbeat": {"claimed"}, "review": {"claimed"},
                         "release": {"claimed", "review"}, "accept": {"review"}}
            if record.get("status") not in permitted[action]:
                raise ValueError(f"cannot {action} a task in {record.get('status', 'open')}")
            if action in {"release", "accept"} and not notes.strip():
                raise ValueError("release/accept requires --notes")
            if action == "accept" and record.get("branch"):
                if git("merge-base", "--is-ancestor", record["branch"], "HEAD",
                       cwd=main_root(), check=False).returncode:
                    raise ValueError("integrate the reviewed branch into the main checkout first")
                dirty = git("status", "--porcelain", "--untracked-files=all",
                            cwd=record["worktree"]).stdout.splitlines()
                if any(line[3:] != "AGENT_REPORT.md" for line in dirty):
                    raise ValueError("worker has uncommitted files; inspect and commit owned outputs first")
                changed = git("diff", "--name-only", record["base"], record["branch"], "--").stdout.splitlines()
                if not changed or any(name != "AGENT_REPORT.md" and not any(name == own.rstrip("/") or
                                              (own.endswith("/") and name.startswith(own))
                                              for own in book[tid]["owns"])
                                      for name in changed):
                    raise ValueError("branch has no committed task output or contains out-of-scope files")
            record["status"] = {"review": "review", "release": "open", "accept": "done"}.get(
                action, record["status"])
        record.update(extra or {})
        record.update(updated_at=timestamp(), notes=notes or record.get("notes", ""))
        state[tid] = record
    event = {"at": timestamp(), "action": action, "task": tid, "agent": agent, "notes": notes}
    folder = main_root() / ".agent-runtime" / "coordination"
    with (folder / "events.jsonl").open("a") as handle:
        handle.write(json.dumps(event) + "\n")


def brief(tid):
    book = tasks()
    row = book[tid]
    text = [f"# {tid}: {row['title']}", row["brief"],
            "## Allowed output paths", *row["owns"], "AGENT_REPORT.md",
            "## Done when", *[f"- {item}" for item in row["done_when"]]]
    return "\n\n".join(text)


def render_board():
    book, state = tasks(), snapshot()
    lines = ["# Workboard", "", "Generated from WORKBOARD.jsonl and central local claims.",
             "Run `python3 scripts/agents.py sync` to refresh; `list` reads live state.", "",
             "First milestone: prior work → theory map → independent novelty audit.", "",
             "| State | Task | Priority | Depends on | Owner |",
             "|---|---|---|---|---|"]
    for tid, row in book.items():
        lines.append(f"| {state_of(tid, book, state)} | `{tid}` — {row['title']} | "
                     f"{row['priority']} | {', '.join(row['blocked_by']) or '—'} | "
                     f"{state.get(tid, {}).get('agent', '—')} |")
    lines += ["", "Agent delivery enters review. Only integrated, reviewed work becomes done.",
              "", "See scripts/agents/README.md for launch, recovery, and review commands.", ""]
    atomic_text(main_root() / "WORKBOARD.md", "\n".join(lines))


def launch_baseline(book, task_ids, from_committed_head=False):
    """Pin the branch input without copying or changing concurrent working files."""
    root = main_root()
    baseline = git("rev-parse", "--verify", "HEAD", cwd=root).stdout.strip()
    if not from_committed_head:
        if git("status", "--porcelain", cwd=root).stdout.strip():
            raise ValueError("commit the coordinator's current changes before branching workers")
    else:
        protected = ["WORKBOARD.jsonl", "AGENTS.md", "scripts/agents.py", "scripts/agents/"]
        protected += [own for tid in task_ids for own in book[tid]["owns"]]
        if git("status", "--porcelain", "--untracked-files=all", "--", *protected,
               cwd=root).stdout.strip():
            raise ValueError("committed-head launch requires clean coordination and task output paths")
    return baseline


def launch(args):
    book, state = tasks(), snapshot()
    if len(args.tasks) != len(set(args.tasks)):
        raise ValueError("duplicate task in launch batch")
    for tid in args.tasks:
        assert_claimable(tid, book, state)
        state[tid] = {"status": "claimed", "agent": f"glm-{tid}"}
        if (main_root() / ".worktrees" / tid).exists():
            raise ValueError(f"worktree for {tid} already exists; inspect and preserve its work first")
        print(f"{'DRY RUN' if args.dry_run else 'PLAN'} {tid}: {args.model}; "
              f"branch agent/{tid}; owns {', '.join(book[tid]['owns'])}")
    if args.dry_run:
        return
    if not shutil.which("opencode"):
        raise ValueError("opencode is not installed")
    baseline = launch_baseline(book, args.tasks, getattr(args, "from_committed_head", False))
    for tid in args.tasks:
        agent = f"glm-{tid}"
        root = main_root()
        wt = root / ".worktrees" / tid
        run = root / ".agent-runtime" / "runs" / tid
        branch = f"agent/{tid}"
        transition("claim", tid, agent, extra={"worktree": str(wt), "branch": branch,
                                              "model": args.model,
                                              "base": baseline})
        try:
            wt.parent.mkdir(parents=True, exist_ok=True)
            git("worktree", "add", "-b", branch, str(wt), baseline, cwd=root)
            run.mkdir(parents=True, exist_ok=True)
            with (run / "worker.log").open("a") as log:
                worker = subprocess.Popen([sys.executable, str(root / "scripts/agents.py"),
                                           "_worker", tid, "--model", args.model],
                                          cwd=wt, stdin=subprocess.DEVNULL,
                                          stdout=log, stderr=log, start_new_session=True)
            atomic_json(run / "process.json", {"pid": worker.pid, "worktree": str(wt),
                                               "task": tid, "started_at": timestamp()})
            print(f"launched {tid}: worker {worker.pid}; logs {run}")
        except Exception:
            transition("release", tid, agent, notes="Launch failed; preserve and inspect any worktree.")
            raise
    render_board()


def resume(args):
    """Restart a claimed task whose supervisor died, in its existing worktree."""
    tid, root = args.task, main_root()
    record = snapshot().get(tid, {})
    if record.get("status") != "claimed" or record.get("agent") != f"glm-{tid}":
        raise ValueError(f"{tid} is not claimed by glm-{tid}")
    wt, run = root / ".worktrees" / tid, root / ".agent-runtime" / "runs" / tid
    if not wt.is_dir():
        raise ValueError(f"no worktree at {wt}; use launch after releasing the claim")
    if (run / "process.json").exists():
        pid = json.loads((run / "process.json").read_text())["pid"]
        alive = subprocess.run(["ps", "-p", str(pid), "-o", "command="], text=True,
                               capture_output=True).stdout
        if f"_worker {tid}" in alive:
            raise ValueError(f"supervisor {pid} is still running")
    busy = subprocess.run(["pgrep", "-f", "--", f"--title time-{tid} "], text=True, capture_output=True)
    if busy.returncode > 1:
        raise ValueError(f"pgrep failed: {busy.stderr.strip()}")
    if busy.stdout.strip():
        raise ValueError(f"an OpenCode run for {tid} is still alive (pid {busy.stdout.split()[0]}); stop it first")
    print(f"{'DRY RUN' if args.dry_run else 'RESUME'} {tid}: {args.model}; worktree {wt}")
    if args.dry_run:
        return
    if (run / "result.json").exists():
        (run / "result.json").rename(run / f"result.{timestamp().replace(':', '')}.json")
    with (run / "worker.log").open("a") as log:
        proc = subprocess.Popen([sys.executable, str(root / "scripts/agents.py"), "_worker", tid,
                                 "--model", args.model, "--resume"], cwd=wt, stdin=subprocess.DEVNULL,
                                stdout=log, stderr=log, start_new_session=True)
    atomic_json(run / "process.json", {"pid": proc.pid, "worktree": str(wt), "task": tid,
                                       "started_at": timestamp(), "resumed": True})
    print(f"resumed {tid}: worker {proc.pid}; logs {run}")


def worker(args):
    tid, root = args.task, main_root()
    wt = root / ".worktrees" / tid
    run = root / ".agent-runtime" / "runs" / tid
    prompt = (root / "scripts/agents/PREAMBLE.md").read_text() + "\n\n" + brief(tid)
    prompt += f"\n\nYour worktree: {wt}\nYour branch: agent/{tid}\n"
    env = {key: os.environ[key] for key in
           ("HOME", "PATH", "LANG", "TERM", "XDG_CONFIG_HOME", "XDG_DATA_HOME",
            "XDG_STATE_HOME", "XDG_CACHE_HOME") if key in os.environ}
    env.update(OPENCODE_CONFIG=str(root / "scripts/agents/opencode-agent.json"),
               GIT_SSH_COMMAND="false", GH_TOKEN="invalid", GITHUB_TOKEN="invalid",
               AWS_SHARED_CREDENTIALS_FILE="/dev/null", AWS_CONFIG_FILE="/dev/null")
    events = run / "events.jsonl"
    slot = acquire_slot(root, tid)
    session, code, limited, quota = None, None, False, None
    for attempt in range(1, RATE_LIMIT_ATTEMPTS + 1):
        message = prompt + RESUME_NOTE if attempt > 1 or args.resume else prompt
        command = ["opencode", "run", "--standalone", "--auto", "--model", args.model,
                   "--title", f"time-{tid}", "--format", "json",
                   *(["--session", session] if session else []), message]
        start = events.stat().st_size if events.exists() else 0
        with events.open("a") as out, (run / "stderr.log").open("a") as err:
            out.write(json.dumps({"type": "runner", "attempt": attempt,
                                  "session": session, "at": timestamp()}) + "\n")
            out.flush()
            process = subprocess.Popen(command, cwd=wt, env=env, stdin=subprocess.DEVNULL,
                                       stdout=out, stderr=err)
            # The supervisor and OpenCode share a process group for explicit stop.
            while True:
                try:
                    code = process.wait(timeout=60)
                    break
                except subprocess.TimeoutExpired:
                    beat(tid)
        session, limited, quota = scan_events(events, start, session)
        if code == 0 or quota or not limited or attempt == RATE_LIMIT_ATTEMPTS:
            break
        delay = 90 * 2 ** (attempt - 1)
        print(f"{tid}: provider rate limit; retry {attempt + 1} in {delay}s "
              f"(session {session})", flush=True)
        for _ in range(delay // 30):
            beat(tid)
            time.sleep(30)
    slot.close()
    report = wt / "AGENT_REPORT.md"
    record = snapshot().get(tid, {})
    outcome, reason = worker_outcome(wt, record.get("base"), tasks()[tid]["owns"],
                                     code, quota, limited)
    atomic_json(run / "result.json", {"exit_code": code, "outcome": outcome, "reason": reason,
                                      "attempts": attempt, "finished_at": timestamp()})
    if outcome == "review":
        transition("review", tid, f"glm-{tid}",
                   notes=f"Inspect {report}; {reason}; not yet accepted.")
    print(f"{tid}: {outcome} ({reason})", flush=True)


def beat(tid):
    try:
        transition("heartbeat", tid, f"glm-{tid}")
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"{tid}: heartbeat failed ({exc}); worker continues", flush=True)


def acquire_slot(root, tid):
    """Hold one of AGENT_MAX_CONCURRENT lock files so the provider is not flooded."""
    limit = int(os.environ.get("AGENT_MAX_CONCURRENT", DEFAULT_MAX_CONCURRENT))
    slots = root / ".agent-runtime" / "slots"
    slots.mkdir(parents=True, exist_ok=True)
    waited = False
    while True:
        for i in range(limit):
            handle = (slots / f"{i}.lock").open("w")
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                handle.close()
                continue
            handle.write(f"{tid} {os.getpid()} {timestamp()}\n")
            handle.flush()
            return handle
        if not waited:
            print(f"{tid}: all {limit} worker slots busy; queued", flush=True)
            waited = True
        beat(tid)
        time.sleep(30)


def scan_events(path, start, session):
    """Session ID, whether a 429 appeared since byte offset start, and any quota message.

    z.ai reports short-window throttling as provider.rate-limit (code 1302) and an
    exhausted plan window as provider.quota (code 1308, with a reset time)."""
    limited, quota = False, None
    with path.open() as f:
        f.seek(start)
        for line in f:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            session = event.get("sessionID") or session
            error = event.get("error") or {}
            if event.get("type") == "error" and (
                    error.get("type") == "provider.rate-limit" or error.get("status") == 429):
                limited = True
            if event.get("type") == "error" and (
                    error.get("type") == "provider.quota" or '"1308"' in json.dumps(error)):
                quota = error.get("message") or "code 1308"
    return session, limited, quota


def submission_problem(wt, base, owns):
    """Fail closed unless this task, not its baseline, supplied a clean handback."""
    if not base or not re.fullmatch(r"[0-9a-f]{40,64}", base):
        return "missing or invalid launch base"
    ancestor = git("merge-base", "--is-ancestor", base, "HEAD", cwd=wt, check=False)
    if ancestor.returncode:
        return "launch base is not an ancestor of the submission"
    status = git("status", "--porcelain", "--untracked-files=all", cwd=wt, check=False)
    if status.returncode or status.stdout.strip():
        return "worktree is dirty or its status is unavailable"
    diff = git("diff", "--name-only", "-z", base, "HEAD", "--", cwd=wt, check=False)
    if diff.returncode:
        return "submission diff is unavailable"
    changed = [name for name in diff.stdout.split("\0") if name]
    if "AGENT_REPORT.md" not in changed or not (wt / "AGENT_REPORT.md").is_file():
        return "no fresh committed AGENT_REPORT.md relative to launch base"
    outputs = [name for name in changed if name != "AGENT_REPORT.md"]
    if not outputs:
        return "no task-owned output changed relative to launch base"
    if any(not any(name == own.rstrip("/") or
                   (own.endswith("/") and name.startswith(own)) for own in owns)
           for name in outputs):
        return "submission includes out-of-scope files"
    if not any((wt / name).is_file() for name in outputs):
        return "submission has no surviving task-owned output file"
    return None


def worker_outcome(wt, base, owns, code, quota=None, limited=False):
    problem = submission_problem(wt, base, owns)
    if problem is None:
        reason = f"exit {code} after fresh committed task output and report; clean tree"
        if quota:
            reason += f"; provider quota reported after handback: {quota}"
        return "review", reason
    failure = (f"provider usage quota exhausted: {quota}" if quota else
               "provider rate limit, retries exhausted" if limited else f"exit {code}")
    return "failed", f"{failure}; incomplete submission: {problem}"


def status():
    state = snapshot()
    for tid, record in state.items():
        if record.get("status") == "open":
            continue
        run = main_root() / ".agent-runtime" / "runs" / tid
        result = json.loads((run / "result.json").read_text()) if (run / "result.json").exists() else {}
        print(f"{tid:24} {record['status']:8} {result.get('outcome', 'no terminal result'):18} "
              f"{record['agent']} updated={record['updated_at']}")


def stop(tid):
    if tid not in tasks():
        raise ValueError(f"unknown task: {tid}")
    run = main_root() / ".agent-runtime" / "runs" / tid
    if (run / "result.json").exists():
        raise ValueError("worker already finished; inspect its report/result")
    record = json.loads((run / "process.json").read_text())
    pid = record["pid"]
    check = subprocess.run(["ps", "-p", str(pid), "-o", "command="], text=True, capture_output=True)
    if check.returncode or f"_worker {tid}" not in check.stdout or str(main_root() / "scripts/agents.py") not in check.stdout:
        raise ValueError("PID no longer identifies this worker; no signal sent")
    os.killpg(pid, signal.SIGTERM)
    print(f"Stopped {tid}; claim, worktree, commits and logs preserved for inspection.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("list", "sync", "status", "validate"):
        commands.add_parser(name)
    command = commands.add_parser("brief")
    command.add_argument("task")
    for name in ("claim", "heartbeat", "review", "release", "accept"):
        command = commands.add_parser(name)
        command.add_argument("task")
        command.add_argument("--agent", required=True, help="claim holder, including for accept")
        command.add_argument("--notes", default="")
    command = commands.add_parser("launch")
    command.add_argument("tasks", nargs="+")
    command.add_argument("--dry-run", action="store_true")
    command.add_argument("--from-committed-head", action="store_true",
                         help="branch from pinned HEAD while preserving unrelated dirty working files")
    command.add_argument("--model", default=DEFAULT_MODEL)
    command = commands.add_parser("resume", help="restart a claimed task whose supervisor died")
    command.add_argument("tasks", nargs="+")
    command.add_argument("--dry-run", action="store_true")
    command.add_argument("--model", default=DEFAULT_MODEL)
    command = commands.add_parser("_worker")
    command.add_argument("task")
    command.add_argument("--model", required=True)
    command.add_argument("--resume", action="store_true")
    command = commands.add_parser("stop")
    command.add_argument("task")
    args = parser.parse_args()
    try:
        if args.command == "list":
            book, state = tasks(), snapshot()
            for tid, row in book.items():
                print(f"{state_of(tid, book, state):8} {tid:24} p{row['priority']} {row['title']}")
        elif args.command == "brief":
            print(brief(args.task))
        elif args.command == "validate":
            print(f"Validated {len(tasks())} tasks, paths and acyclic dependencies.")
        elif args.command == "sync":
            render_board()
        elif args.command == "launch":
            launch(args)
        elif args.command == "resume":
            for tid in args.tasks:
                args.task = tid
                resume(args)
        elif args.command == "_worker":
            worker(args)
        elif args.command == "status":
            status()
        elif args.command == "stop":
            stop(args.task)
        else:
            transition(args.command, args.task, args.agent, args.notes)
            render_board()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return REFUSED
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

