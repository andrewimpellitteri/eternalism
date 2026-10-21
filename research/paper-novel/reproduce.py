#!/usr/bin/env python3
"""Run the paper's pinned, bounded exact checks. Standard library only.

From any working directory: python3 /path/to/research/paper-novel/reproduce.py
Existing reviewed scripts are run as subprocesses; no builder file is edited.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / "input-manifest.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads(MANIFEST.read_text())
    for name, expected in manifest["input_sha256"].items():
        actual = sha(ROOT / name)
        if actual != expected:
            raise RuntimeError(f"Reviewed input changed: {name}; {actual} != {expected}")

    tex = (HERE / "main.tex").read_text()
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    if len(labels) != len(set(labels)):
        raise RuntimeError("Duplicate manuscript labels")
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", tex)
    missing = set(refs) - set(labels)
    bib = set(re.findall(r"\\bibitem\{([^}]+)\}", tex))
    cites = re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", tex)
    missing_cites = {c.strip() for group in cites for c in group.split(",")} - bib
    if missing or missing_cites:
        raise RuntimeError(f"Unresolved labels {missing}; citations {missing_cites}")

    reports = []
    for spec in manifest["checks"]:
        result = subprocess.run(
            [sys.executable, str(ROOT / spec["script"])],
            cwd=ROOT, text=True, capture_output=True, timeout=60,
        )
        output = result.stdout + result.stderr
        reports.append({"script": spec["script"], "exit_code": result.returncode,
                        "output": output})
        if result.returncode != 0 or spec["required_marker"] not in output:
            raise RuntimeError(f"Check failed: {spec['script']}\n{output}")

    report = {
        "status": "passed", "source_revision": manifest["revision"],
        "python": sys.version.split()[0], "manuscript_sha256": sha(HERE / "main.tex"),
        "input_files_verified": len(manifest["input_sha256"]),
        "labels_verified": len(labels), "bibliography_entries": len(bib),
        "checks": reports,
        "scope": "Exact finite corroboration only; no infinite theorem or global priority is machine-certified.",
    }
    (HERE / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    text = [f"Pinned source revision: {manifest['revision']}",
            f"Input hashes verified: {report['input_files_verified']}",
            f"Manuscript references: {len(labels)} labels; {len(bib)} bibliography entries"]
    for r in reports:
        text.extend(["", f"Script: {r['script']}; exit {r['exit_code']}", r["output"].rstrip()])
    text.extend(["", "PASS: all pinned finite checks and manuscript cross-references verified.", report["scope"]])
    (HERE / "reproduce_output.txt").write_text("\n".join(text) + "\n")
    print("\n".join(text))


if __name__ == "__main__":
    main()
