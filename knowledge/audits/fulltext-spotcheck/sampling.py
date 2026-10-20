#!/usr/bin/env python3
"""Print a deterministic audit frame; never writes source files or coordination state."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
SEED = 20261020
STRATA = ["aqft-locality", "arrow-cosmology", "axiomatic-relativity", "causal-sets",
          "gr-qg", "preferred-foliation", "thermal-records", "time-interpretations"]
ALIASES = {
    "cs-rideout-sorkin-2000-v3": "frontier-causal-growth-1999",
    "cs-wuthrich-callender-2015-v1": "frontier-causal-becoming-2015",
    "cs-madsen-2026-v1": "frontier-causal-embedding-2026",
}


def build_frame(root=ROOT, revision=None):
    def read(relative):
        if revision:
            return subprocess.check_output(["git", "show", f"{revision}:{relative}"], cwd=root)
        return (root / relative).read_bytes()

    if revision:
        paths = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", revision, "knowledge"], cwd=root, text=True).splitlines()
        paths = [p for p in paths if p.endswith("sources.jsonl")]
    else:
        paths = [str(p.relative_to(root)) for p in (root / "knowledge").rglob("*sources.jsonl")]
    copies = {}
    inputs = {}
    for relative in sorted(paths):
        # Audit artifacts are not a new source register or an input to sampling.
        if "audits" in Path(relative).parts:
            continue
        content = read(relative)
        inputs[relative] = hashlib.sha256(content).hexdigest()
        for line, text in enumerate(content.decode().splitlines(), 1):
            if text.strip():
                record = json.loads(text)
                copies.setdefault(record["id"], []).append({"file": relative, "line": line, "record": record})
    contract_path = "research/theory-map/research-contracts.md"
    content = read(contract_path)
    contract = content.decode()
    inputs[contract_path] = hashlib.sha256(content).hexdigest()
    mentioned = set(re.findall(r"`([a-z][a-z0-9-]+)`", contract))
    full_text = sorted(rid for rid, hits in copies.items()
                       if any(hit["record"].get("read_depth") == "full-text" for hit in hits))
    anchors = sorted(set(full_text) & mentioned)
    selected = list(anchors)
    rng = random.Random(SEED)
    draws = []
    for lane in STRATA:
        eligible = sorted(rid for rid in full_text if rid not in selected and any(
            hit["file"] == f"knowledge/{lane}/sources.jsonl"
            and hit["record"].get("read_depth") == "full-text" for hit in copies[rid]))
        if not eligible:
            raise ValueError(f"No eligible full-text record in stratum {lane}")
        rid = rng.choice(eligible)
        selected.append(rid)
        draws.append({"stratum": lane, "eligible_ids": eligible, "selected_id": rid})
    # RC-4 cites shallow frontier IDs, but later full-text causal-set records
    # cover the same primary works. Include these aliases instead of losing
    # RC-4 from the load-bearing audit merely because its IDs differ.
    for rid in ALIASES:
        if rid not in selected:
            selected.append(rid)
    primaries = ["found-stein-1968", "found-malament-1977"]
    selected.extend(primaries)
    clocks = {rid for rid in anchors if rid.startswith(("frontier-", "meth-"))}
    rows = []
    for rid in selected:
        lane = "clocks-methods" if rid in clocks else "foundations" if (
            rid.startswith("found-") or rid in [d["selected_id"] for d in draws[:2]]) else "physics"
        rows.append({"id": rid, "audit_lane": lane,
                     "selection": "contract-anchor" if rid in anchors else
                                  "required-primary" if rid in primaries else
                                  "contract-alias-anchor" if rid in ALIASES else "stratified-draw",
                     "contract_ids": ["RC-4"] if rid in ALIASES else ["RC-2"] if rid in primaries else
                                     [f"RC-{n}" for n in range(1, 6) if rid in contract.split(f"## RC-{n}", 1)[-1].split("\n## RC-", 1)[0]] if rid in anchors else [],
                     "copies": copies[rid]})
    return {"seed": SEED, "source_revision": revision,
            "frame_rule": "Unique knowledge-register IDs claiming full-text, excluding audit outputs; all exact backtick contract IDs at full-text depth plus three explicit RC-4 same-paper aliases; eight fixed lane strata each contribute one seeded draw; Stein 1968 and Malament 1977 are additional required primaries. Twenty full-text records plus two required shallower primaries.",
            "input_sha256": inputs, "full_text_frame_ids": full_text,
            "contract_anchor_ids": anchors, "contract_alias_ids": ALIASES,
            "stratified_draws": draws, "sample": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="82f1547", help="committed source cutoff; default is the pre-audit snapshot")
    args = parser.parse_args()
    print(json.dumps(build_frame(revision=args.revision), indent=2, ensure_ascii=False))
