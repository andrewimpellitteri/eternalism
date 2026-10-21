#!/usr/bin/env python3
"""Read-only status check for the external GitHub gates.

This script never creates, edits, closes or comments on issues. It only calls
`gh issue view --json` and prints the result. The local workboard remains
authoritative; GitHub is used for release/review gates only.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GATES = HERE / "gates.json"


def gh_issue(number):
    return subprocess.run(
        ["gh", "issue", "view", str(number),
         "--json", "number,title,state,labels,url,updatedAt"],
        capture_output=True, text=True, check=False,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print JSON only")
    args = parser.parse_args()

    if shutil.which("gh") is None:
        print("ERROR: gh CLI not found on PATH", file=sys.stderr)
        return 2
    if not GATES.exists():
        print(f"ERROR: missing {GATES}", file=sys.stderr)
        return 2

    mapping = json.loads(GATES.read_text())["gates"]
    rows, failed = [], False
    for gate in mapping:
        result = gh_issue(gate["issue"])
        if result.returncode != 0:
            failed = True
            rows.append({
                "issue": gate["issue"],
                "name": gate["name"],
                "error": result.stderr.strip() or result.stdout.strip(),
            })
            continue
        data = json.loads(result.stdout)
        labels = [label["name"] for label in data.get("labels", [])]
        rows.append({
            "issue": data["number"],
            "name": gate["name"],
            "state": data["state"],
            "labels": labels,
            "blocked": "status:blocked" in labels,
            "url": data["url"],
            "local_tasks": gate.get("local_tasks", []),
        })

    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        print(f"{'#':>2}  {'STATE':<6}  {'BLOCKED':<7}  {'LABELS':<45}  GATE")
        for row in rows:
            if "error" in row:
                print(f"{row['issue']:>2}  ERROR   {'?':<7}  {'':<45}  {row['name']}")
                print(f"    {row['error']}")
                continue
            labels = ",".join(row["labels"])[:45]
            print(f"{row['issue']:>2}  {row['state']:<6}  "
                  f"{str(row['blocked']):<7}  {labels:<45}  {row['name']}")

    return 3 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
