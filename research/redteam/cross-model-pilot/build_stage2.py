"""Build the Stage 2 blind item set from real past record failures and verified-clean
records. Standard library only. Reads git history; writes items.jsonl (blind) and
labels.jsonl (ground truth) next to this file.

    python3 research/redteam/cross-model-pilot/build_stage2.py
"""
import json
import random
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SEED = 20261020
FIELDS = ("title", "authors", "url", "version")

# (commit, path, id, class, defective fields, ground truth with evidence)
DEFECTIVE = [
    ("23241bb^", "knowledge/foundations/sources.jsonl", "found-stein-1968", "wrong-identifier", ["url"],
     "DOI should be 10.2307/2024512 (J. Phil. 65(1), 1968, 5-23); 10.2307/2023910 is another item. Evidence: commit 23241bb, Crossref."),
    ("23241bb^", "knowledge/foundations/sources.jsonl", "found-malament-1977", "wrong-identifier", ["url"],
     "DOI should be 10.2307/2214766 (Nous 11(3), 293-300). Evidence: commit 23241bb, Crossref."),
    ("23241bb^", "knowledge/foundations/sources.jsonl", "found-deasy-2015", "wrong-identifier", ["url", "title"],
     "DOI should be 10.1007/s11098-014-0398-5 (Phil. Studies 172, 2073-2089); catalog title 'The moving spotlight theory'. Evidence: commit 23241bb, bib-corrections A.2."),
    ("23241bb^", "knowledge/foundations/sources.jsonl", "found-prior-2009", "nonexistent-source", ["url", "title"],
     "No Hawley paper by this title exists; the DOI is J. Fernandez's review in Mind 118(471). Evidence: bib-corrections section C."),
    ("34f0357", "knowledge/aqft-locality/sources.jsonl", "aqft-bisognano-wichmann-1976", "wrong-identifier", ["url", "title"],
     "DOI 10.1063/1.522676 is Wong & Yeh 1975; correct 10.1063/1.522898, title 'On the duality condition for quantum fields'. Evidence: bib-corrections A.1."),
    ("795618a^", "knowledge/arrow-cosmology/sources.jsonl", "arrow-lazarovici-reichert-2018", "wrong-free-text-metadata", ["version"],
     "Not published in SHPS B 69; a 2020 World Scientific chapter. v2 is dated 2019-01-10, not 2018. Evidence: arXiv listing, PhilSci 17468; commit 795618a."),
    ("795618a^", "knowledge/discriminators/sources.jsonl", "disc-mewes-clockcompare-sme-2018", "wrong-authors", ["authors"],
     "Authors are Kostelecky and Vargas, not Kostelecky and Mewes. Evidence: arXiv:1805.04499 listing; commit 795618a."),
    ("HEAD", "knowledge/discriminators/sources.jsonl", "disc-loriani-clock-interferometry-2019", "wrong-authors", ["authors"],
     "Crossref 10.1126/sciadv.aax8966: Sina Loriani, Alexander Friedrich, Christian Ufrecht, Fabio Di Pumpo, Stephan Kleinert, Sven Abend, Naceur Gaaloul, Christian Meiners, Christian Schubert, Dorothee Tell, ...; the record has 8 wrong given names. Found 2026-10-20 while choosing clean controls."),
]
CLEAN = [  # every field checked against Crossref or the arXiv listing on 2026-10-20
    "aqft-fewster-rejzner-2020v2", "aqft-fewster-verch-2012-kg", "arrow-gtz-no-ph-2016",
    "arrow-dks-boltzmann-brains-2002", "arrow-wallace-gravity-entropy-2009",
    "disc-lageos-prl-constraint-2026", "disc-moreva-pagewootters-2017v1", "found-stein-1991",
    "arrow-babar-time-reversal-2012",
]
CLEAN_PATHS = ["knowledge/aqft-locality/sources.jsonl", "knowledge/arrow-cosmology/sources.jsonl",
               "knowledge/discriminators/sources.jsonl", "knowledge/foundations/sources.jsonl",
               "knowledge/bib-audit/proposed-records.jsonl"]  # last wins: canonical Stein 1991 URL
# Hedges that would tip off an auditor without changing the defect.
SCRUB = ["; DOI locator not independently verified in this pass"]


def records(commit, path):
    text = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout
    return {r["id"]: r for r in map(json.loads, filter(str.strip, text.splitlines()))}


def blind(record):
    out = {k: record.get(k) for k in FIELDS if record.get(k)}
    for hedge in SCRUB:
        out["version"] = out.get("version", "").replace(hedge, "") or None
    return {k: v for k, v in out.items() if v}


def main():
    items, labels = [], []
    for commit, path, rid, kind, fields, truth in DEFECTIVE:
        items.append((rid, blind(records(commit, path)[rid])))
        labels.append({"source_id": rid, "label": "defective", "class": kind, "fields": fields,
                       "truth": truth, "from": f"{commit}:{path}"})
    clean = {}
    for path in CLEAN_PATHS:
        clean.update(records("HEAD", path))
    for rid in CLEAN:
        items.append((rid, blind(clean[rid])))
        labels.append({"source_id": rid, "label": "clean", "class": None, "fields": [],
                       "truth": "All four fields verified 2026-10-20.", "from": "HEAD"})
    order = list(range(len(items)))
    random.Random(SEED).shuffle(order)
    with (HERE / "items.jsonl").open("w") as fi, (HERE / "labels.jsonl").open("w") as fl:
        for n, i in enumerate(order, 1):
            rid, item = items[i]
            fi.write(json.dumps({"item": f"R{n:02d}", **item}, ensure_ascii=False) + "\n")
            fl.write(json.dumps({"item": f"R{n:02d}", **labels[i]}, ensure_ascii=False) + "\n")
    print(f"{len(items)} items ({len(DEFECTIVE)} defective, {len(CLEAN)} clean), seed {SEED}")


if __name__ == "__main__":
    main()
