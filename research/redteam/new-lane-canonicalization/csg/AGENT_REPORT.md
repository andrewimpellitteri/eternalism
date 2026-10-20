# Canonical-reference decision: causal-sets / CSG-quantum

Date: 2026-10-20. This report covers only `cs-brightwell-2003-observables` and `cs-surya-zalel-2020`; the other two duplicate IDs in the parent task were outside this worker's assigned files.

## Decision

For both IDs, retain the CSG-quantum record in `knowledge/csg-quantum/sources.jsonl` as the explicit canonical source record and replace the causal-sets copy with a source reference in `knowledge/causal-sets/source-refs.jsonl`. The choice follows source correspondence and extraction provenance, not a rule that the deeper record always wins: the CSG lane has the exact arXiv version and section/equation locators for the same primary work, plus the accepted lane review; the causal-sets records are explicitly marked discovery and “not read in this lane.” The canonical home is suitable for both because these are causal-set sequential-growth papers and the CSG-quantum lane cites them as foundations for its quantum-growth comparison. The CSG extraction/review does not erase the older causal-sets discovery provenance.

| ID | Canonical edition in CSG-quantum | Earlier causal-sets payload |
|---|---|---|
| `cs-brightwell-2003-observables` | Brightwell, Dowker, Garcia, Henson & Sorkin, “Observables” in causal set cosmology, [arXiv `gr-qc/0210061v2`](https://arxiv.org/abs/gr-qc/0210061v2) (submitted 18 Oct 2002, revised 20 Oct 2002); *Physical Review D* 67, 084031 (2003), DOI `10.1103/PhysRevD.67.084031`. Read via arXiv HTML v2. Publisher version not compared. | Discovery, checked 2026-10-19; no version value recorded; causal-sets lane report states it was not read in that lane. |
| `cs-surya-zalel-2020` | Surya & Zalel, “A Criterion for Covariance in Complex Sequential Growth Models,” [arXiv `2003.11311v1`](https://arxiv.org/abs/2003.11311v1) (submitted 25 Mar 2020; only arXiv version listed); *Classical and Quantum Gravity* 37(19), 195030 (2020), DOI `10.1088/1361-6382/ab987f`. Read via arXiv HTML v1; publisher version not compared. | Discovery, checked 2026-10-19; no version value recorded; causal-sets lane report states it was not read in that lane. |

The current CSG-quantum records retain their original authorship, exact versions, statements, assumptions, proof status, section locators, and limitations. In particular:

* Brightwell et al. covers the generic generalized-percolation CSG class described in Sec. 2 (with exceptional dust/forest cases treated separately); the stem-generation and quotient claims are stated at their recorded scope. The article does not supply an embedded observer/record model, and its treatment of relabellings is an assumption whose physical status is discussed by the authors.
* Surya–Zalel's Theorem 2.1 concerns a `C`-valued complex measure on the cylinder-generated algebra and its extension to the generated sigma-algebra under bounded variation. The CSG report preserves the open `k_m-k_{m-1}=1` case and other stated limits. Nonextension to the whole sigma-algebra is not by itself a theorem about failure on a smaller covariant algebra or about observer access.

The accepted CSG report identifies its lane as Claude Opus and calls the work a coordinator-reviewed worker submission; its source records themselves attribute the newer reading to the CSG lane, with `checked_on: 2026-10-20`. The prior causal-sets record did not specify a personal reader. References therefore state that personal identity is not recorded and preserve the lane's explicit statement that it did not read these papers. The references do not promote either original record's depth or version.

## Snapshot and integrity evidence

The source-reference entries point to the captured pre-migration snapshot `research/redteam/new-lane-canonicalization/before-records.jsonl`, revision `c480ff1ce0e9d4f01e5e8f5bdef4af86a7bc3326`, manifest snapshot SHA-256 `c92673e7691b3464b3c87bab9a4344a33274e0a412bc3fa944d93a3d6c81b1f5`. The reference payloads preserve the original causal-set records at lines 6 and 7. Their normalized record hashes (UTF-8 JSON, sorted keys, `ensure_ascii=False`, default separators) are:

* `cs-brightwell-2003-observables`: `ab750596ef6b20ff6711e7cf649e1c87e17729b03a559df3fc1f6847c47b3584`
* `cs-surya-zalel-2020`: `7a3444f7713c234b456d1f245554d2726b105e4a1c924e7988f852accacc0d99`

`verify_refs.py` validates snapshot integrity, exact prior-record hash/fields, one surviving canonical payload per ID, no inherited payload remaining in the causal-sets register, explicit targets, and one reference per removed copy. It passes for these two IDs.

## Changes and checks

Changed only the following owned files:

* `knowledge/causal-sets/sources.jsonl`: removed the two duplicate discovery payloads; all other causal-set records remain in original order and content.
* `knowledge/causal-sets/source-refs.jsonl`: added two exact, pinned inherited-source references to `knowledge/csg-quantum/sources.jsonl`.
* `research/redteam/new-lane-canonicalization/csg/AGENT_REPORT.md` and `verify_refs.py`: recorded the decision and local snapshot validator.

Checks run:

* `python3 research/redteam/new-lane-canonicalization/csg/verify_refs.py` — pass; 2 references and 2 canonical payloads validated.
* `python3 scripts/check_sources.py --strict knowledge research` — pass at time of check: 25 files, 336 records, 0 errors, 0 warnings, 0 info.
* `python3 research/redteam/source-repairs/check_references.py --root .` — reference integrity currently reports false only because that pre-existing checker pins every reference to the older `research/redteam/source-repairs/before-records.jsonl`; it reports the two new CSG references and the other lane's two new references as “Unpinned prior snapshot.” It reports 67 references, 336 records, 336 unique IDs, and no global duplicate IDs. I did not edit that shared checker or its historical migration archive. The local verifier checks this new snapshot's provenance instead.

On 2026-10-20 I directly opened the arXiv abstract/metadata landing pages for [Brightwell et al. v2](https://arxiv.org/abs/gr-qc/0210061v2) and [Surya–Zalel v1](https://arxiv.org/abs/2003.11311v1) to confirm title, authors, version/submission dates, and the listed journal reference for Brightwell; this was metadata verification, not a body reread. No primary article HTML/PDF body was fetched or reread during this canonicalization task. Body-level claims above are carried from the versioned CSG records and the accepted CSG coordinator review, which document the earlier CSG lane's arXiv HTML reads. The decision is an ID/navigation and provenance decision, not an additional source audit. Publisher editions were not compared, and this worker does not make a novelty, correctness, or ontology claim.
