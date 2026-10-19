#!/usr/bin/env python3
"""Idea grid: enumerate cross-framework cells, pack them into workboard tasks,
and track how far each cell survives. Standard library only.

    python3 scripts/grid.py cells                       # count cells per family
    python3 scripts/grid.py tasks s1 --batch 10         # print task lines
    python3 scripts/grid.py tasks s1 --batch 10 --limit 3 --append
    python3 scripts/grid.py status [--worktrees]        # coverage and survivors

Families: s1 (physics x bridge premise), t1 (physics x physics transfer),
adv (independent kill attempt on advanced cells), s2 (adversary survivors x
ontology package). Cells already named in a WORKBOARD.jsonl grid task are never
reassigned. See grid/CONTRACT.md for the per-cell output contract.
"""

import argparse
import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AXES = ROOT / "grid" / "axes.json"
BOARD = ROOT / "WORKBOARD.jsonl"
CELLS_RE = re.compile(r"^Cells: (.+)$", re.M)

S1_BRIEF = ("Pressure cells. For each cell, take the bridge premise and ask what it "
            "says inside the named framework: give it a precise form, then decide "
            "whether the framework makes it true, false, or undecided as stated, under "
            "which hypotheses.")
T1_BRIEF = ("Transfer cells. For each pair of frameworks, look for a theorem, "
            "construction, or technique native to one that answers a precise question "
            "in the other, or show why the transfer fails.")
ADV_BRIEF = ("Adversary pass. Each cell below advanced at an earlier stage. You are "
             "given only its claim, not the proposer's predecessors or reasoning. Run "
             "your own defeat search and try to kill it: find prior work stating it, "
             "show it is trivial by a definition, find a counterexample in its smallest "
             "instance, or show its ontological relevance rests entirely on a bridge "
             "premise. Use verdict 'kill' or 'survive' (in place of 'advance').")
S2_BRIEF = ("Expansion cells. Each cell crosses a claim that survived an independent "
            "kill attempt with one temporal-ontology package. State exactly what the "
            "claim does to that package: excludes it under named premises, is neutral, "
            "supports it only through a named bridge premise, or forces a revision.")
FAMILY = {"s1": ("S1", S1_BRIEF), "t1": ("T1", T1_BRIEF),
          "adv": ("A", ADV_BRIEF), "s2": ("S2", S2_BRIEF)}


def load_axes():
    ax = json.loads(AXES.read_text())
    ax["by_id"] = {i["id"]: i for k in ("physics", "bridges", "ontologies", "moves") for i in ax[k]}
    return ax


def board():
    if not BOARD.exists():
        return []
    return [json.loads(l) for l in BOARD.read_text().splitlines() if l.strip()]


def assigned():
    """Cell ID -> grid task ID, read from task briefs on the workboard."""
    out = {}
    for t in board():
        if t["id"].startswith("grid-"):
            m = CELLS_RE.search(t.get("brief", ""))
            for c in (m.group(1).split(", ") if m else []):
                out[c] = t["id"]
    return out


def result_dirs(worktrees):
    roots = [ROOT]
    if worktrees:
        roots += sorted((ROOT / ".worktrees").glob("grid-*"))
    for r in roots:
        yield from sorted((r / "grid" / "results").glob("*/cells.jsonl"))


def results(worktrees):
    """Cell ID -> list of (source, record). Later stages are separate cell IDs."""
    out, problems = {}, []
    for f in result_dirs(worktrees):
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                problems.append(f"{f}:{n}: invalid JSON")
                continue
            problems += [f"{f}:{n}: {p}" for p in contract_problems(r)]
            out.setdefault(r.get("cell", "?"), []).append((str(f), r))
    return out, problems


def contract_problems(r):
    p = []
    v = r.get("verdict")
    adv = str(r.get("cell", "")).startswith("A-")
    allowed = {"kill", "hold", "survive"} if adv else {"kill", "hold", "advance"}
    if v not in allowed:
        p.append(f"verdict {v!r} not in {sorted(allowed)}")
    if not r.get("claim"):
        p.append("missing claim")
    if v == "kill" and not r.get("kill_reason"):
        p.append("kill without kill_reason")
    if v in ("advance", "survive"):
        if len(r.get("predecessors") or []) < 3:
            p.append(f"{v} with fewer than 3 predecessors")
        if len(r.get("defeat_queries") or []) < 5:
            p.append(f"{v} with fewer than 5 defeat queries")
        if not r.get("smallest_instance"):
            p.append(f"{v} without smallest_instance")
        if r.get("bridge_premises") is None:
            p.append(f"{v} without bridge_premises (use [] if none)")
    return p


def verdict(recs):
    """Most conservative verdict across duplicate records for one cell."""
    order = ["kill", "hold", "advance", "survive"]
    vs = [r.get("verdict") for _, r in recs if r.get("verdict") in order]
    return min(vs, key=order.index) if vs else "?"


def cells(ax, family, worktrees=False):
    P, B, O = ax["physics"], ax["bridges"], ax["ontologies"]
    if family == "s1":
        return [(f"S1-{p['id']}-{b['id']}", f"{p['label']} || {b['label']}") for p in P for b in B]
    if family == "t1":
        return [(f"T1-{p['id']}-{q['id']}", f"{p['label']} || {q['label']}")
                for p, q in itertools.combinations(P, 2)]
    res, _ = results(worktrees)
    if family == "adv":
        return [(f"A-{c}", recs[0][1]["claim"]) for c, recs in sorted(res.items())
                if not c.startswith("A-") and verdict(recs) == "advance"]
    if family == "s2":
        out = []
        for c, recs in sorted(res.items()):
            if c.startswith("A-") and verdict(recs) == "survive":
                for o in O:
                    out.append((f"S2-{c[2:]}-{o['id']}", f"{recs[0][1]['claim']} || {o['label']}"))
        return out
    raise SystemExit(f"unknown family {family}")


def lanes_for(ax, cell_ids):
    lanes = set()
    for c in cell_ids:
        for part in c.split("-"):
            item = ax["by_id"].get(part)
            lanes.update(item.get("lanes", []) if item else [])
    return sorted(lanes)


def make_task(ax, family, n, batch):
    prefix, intro = FAMILY[family]
    tid = f"grid-{family}-{n:02d}"
    ids = [c for c, _ in batch]
    listing = "\n".join(f"- {c}: {label}" for c, label in batch)
    lanes = ", ".join(f"knowledge/{l}/" for l in lanes_for(ax, ids)) or "knowledge/"
    brief = (f"{intro}\n\nFollow grid/CONTRACT.md exactly and write one JSON line per "
             f"cell to grid/results/{tid}/cells.jsonl, in the order below. Expect most "
             f"cells to be killed; a precise kill is a complete result. Start from "
             f"{lanes} and knowledge/PHILOSOPHY_OF_TIME.md; reuse their source IDs. "
             f"Spend effort in proportion to promise: a few minutes to kill an incoherent "
             f"cell, real reading for a cell that may advance. No novelty claims. Public "
             f"sources only; a blocked page is unread.\n\nCells: {', '.join(ids)}\n\n{listing}")
    return {"id": tid, "title": f"Idea grid {prefix} batch {n:02d}: {len(ids)} cells",
            "priority": 7, "blocked_by": [], "owns": [f"grid/results/{tid}/"],
            "brief": brief,
            "done_when": [f"grid/results/{tid}/cells.jsonl has one contract-valid line per assigned cell",
                          "Every advance (or survive) has 3+ predecessors, 5+ logged defeat queries and a smallest instance",
                          "`python3 scripts/grid.py status --worktrees` reports no contract problems for this batch"]}


def cmd_cells(a, ax):
    taken = assigned()
    for fam in ("s1", "t1", "adv", "s2"):
        cs = cells(ax, fam, a.worktrees)
        free = sum(1 for c, _ in cs if c not in taken)
        print(f"{fam:4} {len(cs):4} cells, {free:4} unassigned")


def cmd_tasks(a, ax):
    taken = assigned()
    free = [c for c in cells(ax, a.family, a.worktrees) if c[0] not in taken]
    existing = {t["id"] for t in board()}
    n = 1 + max((int(t.split("-")[-1]) for t in existing if t.startswith(f"grid-{a.family}-")),
                default=0)
    tasks = []
    for i in range(0, len(free), a.batch):
        if a.limit and len(tasks) >= a.limit:
            break
        tasks.append(make_task(ax, a.family, n + len(tasks), free[i:i + a.batch]))
    if not tasks:
        print(f"no unassigned {a.family} cells", file=sys.stderr)
        return 1
    lines = [json.dumps(t, ensure_ascii=False, separators=(",", ":")) for t in tasks]
    if a.append:
        with BOARD.open("a") as f:
            f.write("".join(l + "\n" for l in lines))
        print(f"appended {len(tasks)} tasks: {tasks[0]['id']} .. {tasks[-1]['id']}", file=sys.stderr)
    else:
        print("\n".join(lines))
    return 0


def cmd_status(a, ax):
    res, problems = results(a.worktrees)
    taken = assigned()
    sym = {"kill": "x", "hold": "h", "advance": "A", "survive": "S", "?": "?"}

    def mark(c):
        if f"A-{c}" in res:
            return sym[verdict(res[f'A-{c}'])]
        if c in res:
            return sym[verdict(res[c])]
        return "o" if c in taken else "."

    P, B = ax["physics"], ax["bridges"]
    print("S1 pressure grid   . unassigned  o assigned  x kill  h hold  A advance  S survived adversary")
    print("      " + " ".join(b["id"][1:] for b in B))
    for p in P:
        print(f"{p['id']}   " + "  ".join(mark(f"S1-{p['id']}-{b['id']}") for b in B) + f"   {p['key']}")
    print("\nT1 transfer grid (upper triangle)")
    print("      " + " ".join(q["id"][1:] for q in P))
    for i, p in enumerate(P):
        row = ["  "] * (i + 1) + [f" {mark(f'T1-{p['id']}-{q['id']}')}" for q in P[i + 1:]]
        print(f"{p['id']}  " + " ".join(r[-2:] for r in row))

    tally = {}
    for c, recs in res.items():
        stage = c.split("-")[0]
        tally.setdefault(stage, {}).setdefault(verdict(recs), 0)
        tally[stage][verdict(recs)] += 1
    print("\nVerdicts by stage:", json.dumps(tally, sort_keys=True) if tally else "none yet")
    reasons = {}
    for recs in res.values():
        for _, r in recs:
            if r.get("verdict") == "kill":
                reasons[r.get("kill_reason")] = reasons.get(r.get("kill_reason"), 0) + 1
    if reasons:
        print("Kill reasons:", json.dumps(reasons, sort_keys=True))
    live = [(c, recs) for c, recs in sorted(res.items()) if verdict(recs) in ("advance", "survive")]
    for c, recs in live:
        print(f"\n{c} [{verdict(recs)}]\n  {recs[0][1].get('claim')}")
    if problems:
        print(f"\n{len(problems)} contract problems:")
        print("\n".join("  " + p for p in problems))
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cells")
    c.add_argument("--worktrees", action="store_true")
    t = sub.add_parser("tasks")
    t.add_argument("family", choices=sorted(FAMILY))
    t.add_argument("--batch", type=int, default=10)
    t.add_argument("--limit", type=int, default=0, help="max tasks to emit")
    t.add_argument("--append", action="store_true", help="append to WORKBOARD.jsonl")
    t.add_argument("--worktrees", action="store_true", help="read results from grid worktrees")
    s = sub.add_parser("status")
    s.add_argument("--worktrees", action="store_true")
    a = ap.parse_args()
    ax = load_axes()
    return {"cells": cmd_cells, "tasks": cmd_tasks, "status": cmd_status}[a.cmd](a, ax) or 0


if __name__ == "__main__":
    sys.exit(main())
