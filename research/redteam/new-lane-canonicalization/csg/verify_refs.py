#!/usr/bin/env python3
"""Validate the causal-set -> CSG-quantum source-reference migration only."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SNAPSHOT = Path("research/redteam/new-lane-canonicalization/before-records.jsonl")
MANIFEST = Path("research/redteam/new-lane-canonicalization/before-manifest.json")
SOURCE = Path("knowledge/causal-sets/sources.jsonl")
REFS = Path("knowledge/causal-sets/source-refs.jsonl")
CANONICAL = Path("knowledge/csg-quantum/sources.jsonl")
IDS = {"cs-brightwell-2003-observables", "cs-surya-zalel-2020"}
EXPECTED_VERSIONS = {
    "cs-brightwell-2003-observables": "arXiv:gr-qc/0210061v2 (20 Oct 2002)",
    "cs-surya-zalel-2020": "arXiv:2003.11311v1 (25 Mar 2020; only version listed).",
}


def load_rows(path: Path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def record_hash(record):
    # Contract: sorted keys + ensure_ascii=False + json.dumps default separators.
    payload = json.dumps(record, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate():
    errors = []
    manifest = json.loads((ROOT / MANIFEST).read_text())
    snapshot_bytes = (ROOT / SNAPSHOT).read_bytes()
    if hashlib.sha256(snapshot_bytes).hexdigest() != manifest.get("snapshot_sha256"):
        errors.append("new-lane snapshot digest mismatch")
    archived = {}
    archived_source_rows = []
    for row in load_rows(SNAPSHOT):
        record = row["record"]
        if row["path"] == str(SOURCE):
            archived_source_rows.append(record)
        if row["path"] == str(SOURCE) and record.get("id") in IDS:
            archived[record["id"]] = (row, record)
    if set(archived) != IDS:
        errors.append(f"snapshot coverage mismatch: {sorted(set(archived))}")

    current_source = load_rows(SOURCE)
    current_canonical = load_rows(CANONICAL)
    refs = load_rows(REFS)
    expected_remaining = [r for r in archived_source_rows if r.get("id") not in IDS]
    if current_source != expected_remaining:
        errors.append("non-migrated causal-sets payloads differ from the captured snapshot")
    for rid in sorted(IDS):
        if sum(r.get("id") == rid for r in current_source):
            errors.append(f"inherited payload remains in causal-sets: {rid}")
        targets = [r for r in current_canonical if r.get("id") == rid]
        if len(targets) != 1:
            errors.append(f"expected one CSG-quantum canonical record for {rid}, got {len(targets)}")
        elif not str(targets[0].get("version", "")).startswith(EXPECTED_VERSIONS[rid]):
            errors.append(f"{rid}: canonical arXiv version mismatch")
        matches = [r for r in refs if r.get("id") == rid]
        if len(matches) != 1:
            errors.append(f"expected one causal-sets reference for {rid}, got {len(matches)}")
            continue
        ref = matches[0]
        row, original = archived.get(rid, ({}, {}))
        prior = ref.get("prior_reading", {})
        expected = {
            "snapshot": str(SNAPSHOT),
            "revision": manifest.get("revision"),
            "path": str(SOURCE),
            "line": row.get("line"),
            "record_sha256": record_hash(original) if original else None,
            "read_depth": original.get("read_depth"),
            "version": original.get("version"),
            "checked_on": original.get("checked_on"),
        }
        for key, value in expected.items():
            if prior.get(key) != value:
                errors.append(f"{rid}: prior_reading {key} mismatch")
        if ref.get("canonical_file") != str(CANONICAL):
            errors.append(f"{rid}: wrong canonical target")
        if ref.get("relation") != "inherited-source" or not ref.get("decision"):
            errors.append(f"{rid}: missing relation/decision")
        if not prior.get("reader") or not ref.get("limits"):
            errors.append(f"{rid}: missing reader/limits")

    return {"passed": not errors, "errors": errors, "migrated_ids": sorted(IDS),
            "canonical_records": sum(r.get("id") in IDS for r in current_canonical),
            "source_references": sum(r.get("id") in IDS for r in refs),
            "snapshot_revision": manifest.get("revision"),
            "snapshot_sha256": manifest.get("snapshot_sha256")}


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
