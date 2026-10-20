#!/usr/bin/env python3
"""Read-only source-copy inventory. JSON output goes to stdout; no files are written.

python3 research/redteam/source-canonicalization/inventory.py --format summary
python3 research/redteam/source-canonicalization/inventory.py --format inventory
python3 research/redteam/source-canonicalization/inventory.py --format canonical-map
python3 research/redteam/source-canonicalization/inventory.py --incoming incoming.jsonl
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
ANNOTATIONS = {"inherited_from", "map_role"}
# Explicit coordinator review, not an automatic deepest-reader-wins rule.
SUPERSEDES = {
    "frontier-qrf-indefinite-order-2022v3": "knowledge/ico-qrf/sources.jsonl",
    "frontier-time-delocalization-2026": "knowledge/ico-qrf/sources.jsonl",
    "frontier-qrf-operational-meaning-2026": "knowledge/ico-qrf/sources.jsonl",
}
POLICY_LOCATOR = "knowledge/REVIEW_NOTES.md:131-134, 179-183"


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def payload(record):
    return {k: v for k, v in record.items() if k not in ANNOTATIONS}


def load_file(path, relative):
    hits = []
    for line, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not text.strip():
            continue
        record = json.loads(text)
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            raise ValueError(f"{relative}:{line}: record needs a string id")
        hits.append({"file": relative, "line": line, "record": record})
    return hits


def collect(root):
    by_id, inputs = {}, {}
    for directory in ("knowledge", "research"):
        for path in sorted((root / directory).rglob("*sources.jsonl")):
            relative = str(path.relative_to(root))
            inputs[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
            for hit in load_file(path, relative):
                by_id.setdefault(hit["record"]["id"], []).append(hit)
    return by_id, inputs


def differences(hits):
    fields = sorted(set().union(*(hit["record"] for hit in hits)))
    return [{"field": field, "values": [
        {"file": hit["file"], "line": hit["line"], "present": field in hit["record"],
         "value": hit["record"].get(field)} for hit in hits]}
        for field in fields if len({encoded([field in hit["record"], hit["record"].get(field)])
                                    for hit in hits}) > 1]


def classify(rid, hits):
    knowledge = [hit for hit in hits if hit["file"].startswith("knowledge/")]
    reason = ""
    if len(hits) == 1:
        category, canonical = "unique", hits[0]
        reason = "Only one record; identity and reading claims remain unaudited."
    elif rid in SUPERSEDES and any(hit["file"] == SUPERSEDES[rid] for hit in hits):
        category = "depth-superseding"
        canonical = next(hit for hit in hits if hit["file"] == SUPERSEDES[rid])
        reason = "Explicit coordinator supersession in " + POLICY_LOCATOR + "; depths are reader provenance, not votes."
    elif len(knowledge) == 1:
        canonical = knowledge[0]
        same = len({encoded(payload(hit["record"])) for hit in hits}) == 1
        category = "identical-copy" if same else "stale-copy"
        reason = "Canonical knowledge-lane copy per " + POLICY_LOCATOR
        if same:
            reason += "; source payloads match after excluding inherited_from/map_role annotations."
        else:
            reason += "; research copy differs and must not overwrite it."
    else:
        category, canonical = "true-conflict", None
        reason = "Multiple knowledge copies without explicit supersession, or no unique knowledge owner. Primary-field review and coordinator choice required."
    selected = None if canonical is None else {
        "file": canonical["file"], "line": canonical["line"],
        "read_depth": canonical["record"].get("read_depth"),
        "record_sha256": hashlib.sha256(encoded(canonical["record"]).encode()).hexdigest()}
    return {"id": rid, "classification": category, "canonical": selected, "reason": reason,
            "copies": hits, "field_differences": differences(hits),
            "decision_needed": None if canonical else "Reconcile editions, authors and extraction against the primary text; designate one canonical record and preserve separate reading provenance."}


def inventory(root):
    by_id, inputs = collect(root)
    rows = [classify(rid, by_id[rid]) for rid in sorted(by_id)]
    duplicates = [row for row in rows if len(row["copies"]) > 1]
    counts = {}
    for row in duplicates:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1
    return rows, {"input_sha256": inputs, "files": len(inputs),
                  "records": sum(map(len, by_id.values())), "unique_ids": len(by_id),
                  "duplicated_ids": len(duplicates),
                  "surplus_copies": sum(len(row["copies"]) - 1 for row in duplicates),
                  "depth_conflicts": sum(len({hit["record"].get("read_depth") for hit in row["copies"]}) > 1
                                         for row in duplicates), "classifications": counts}


def incoming_gate(incoming, rows):
    index = {row["id"]: row for row in rows}
    results = []
    for hit in incoming:
        row = index.get(hit["record"]["id"])
        if row is None:
            results.append({"id": hit["record"]["id"], "action": "review-new-id",
                            "reason": "New ID still needs identifier, evidence and claim review."})
            continue
        canonical = row["canonical"]
        match = next((c for c in row["copies"] if canonical and c["file"] == canonical["file"]
                      and c["line"] == canonical["line"]), None)
        diffs = [] if match is None else differences([match, hit])
        results.append({"id": row["id"], "action": "hold-existing-id", "canonical": canonical,
                        "reason": "Keep an ID reference; existing source payloads require explicit coordinator resolution, even if unchanged.",
                        "changed_fields": [item["field"] for item in diffs],
                        "field_differences": diffs, "unresolved": canonical is None})
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--format", choices=("summary", "inventory", "canonical-map"), default="summary")
    parser.add_argument("--incoming", type=Path)
    args = parser.parse_args(argv)
    rows, summary = inventory(args.root)
    if args.incoming:
        results = incoming_gate(load_file(args.incoming, str(args.incoming)), rows)
        print(json.dumps(results, indent=2, ensure_ascii=False))
        # Neither a new ID nor a copied ID is scientific/merge clearance.
        return int(bool(results))
    if args.format == "summary":
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        for row in rows:
            if args.format == "inventory":
                if len(row["copies"]) > 1:
                    print(encoded(row))
            else:
                print(encoded({"id": row["id"], "classification": row["classification"],
                               "canonical": row["canonical"], "decision_needed": row["decision_needed"],
                               "unresolved_copies": [] if row["canonical"] else [
                                   {"file": hit["file"], "line": hit["line"]} for hit in row["copies"]],
                               "superseded_copies": [] if not row["canonical"] else [{"file": hit["file"], "line": hit["line"],
                                                       "read_depth": hit["record"].get("read_depth")}
                                                      for hit in row["copies"] if (hit["file"], hit["line"]) !=
                                                      (row["canonical"]["file"], row["canonical"]["line"])]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
