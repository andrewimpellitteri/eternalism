# Physics source-repair integration

## Disposition

Applied six evidence-backed record repairs in the five assigned source registers. Historical snapshots were retained unchanged in `research/redteam/source-repairs/before-records.jsonl` (manifest revision `edfb80314fe7db51971cadf11f86690da3b71ac9`). Original reader attribution and read depth are preserved; targeted follow-up checks are identified as follow-up checks, not retroactively assigned to earlier readers.

- `axrel-sep-bebecome-2021`: pinned the Fall 2021 SEP archive URL and corrected the metadata to a minor correction, with the archived page's substantive-revision date of 2017-08-21. Kept `full-text` as the depth of the secondary SEP entry only; Stein's primary text remains unread. Evidence: `knowledge/audits/fulltext-spotcheck/physics/findings.jsonl` row for this ID.
- `arrow-wallace-gravity-entropy-2009`: added Sec. 7 to the locator and proof-status text for the matter-entropy decrease/radiation compensation claim. Retained the prior abstract-only first pass and later targeted full-text review as separate stages. No calculation is claimed as reproduced. Evidence: `knowledge/audits/fulltext-spotcheck/foundations/findings.jsonl` row for this ID.
- `cs-wuthrich-callender-2015-v1`: retained the finite counterexample as directly supported; recast population scarcity as the authors' suspicion with limited published evidence; made the Lorentz-invariance consequence conditional on the relevant highly regular structures; kept global becoming as a philosophical compatibility proposal. Evidence: `knowledge/audits/fulltext-spotcheck/physics/findings.jsonl` row for this ID.
- `time-hartle-2005-now`: changed the framework description to four-dimensional spacetime modeling without assuming block ontology; narrowed the result to the IGUS account of subjective temporal organization and removed objective-passage non-fundamentality as a direct Hartle result. Evidence: `knowledge/audits/fulltext-spotcheck/physics/findings.jsonl` row for this ID.
- `fol-dgtz-2014-can-bohmian`: pinned the record to arXiv v2 (24 Dec 2013), the version read in the recorded audit. Evidence: `knowledge/audits/fulltext-spotcheck/physics/findings.jsonl` row for this ID.
- `fol-tumulka-2006-grw-flash`: pinned the current record to arXiv v2 (last revised 16 Sep 2006), which I directly checked at [the versioned arXiv HTML](https://arxiv.org/html/quant-ph/0406094v2) and [versioned abstract metadata](https://arxiv.org/abs/quant-ph/0406094v2). The abstract, Sec. 3 (including the non-interacting-particle restriction and lack of preferred slicing), Sec. 5's foliation-based reformulation, and Sec. 8 support the recorded bounded claims. The prior lane reader's extracted ar5iv text did not specify its version; the record and this report preserve that gap instead of claiming the original reader read v2. This new targeted v2 check is not an audit of every equation or proof.

## Verification and provenance

Ran:

```text
python3 scripts/check_sources.py --strict knowledge/axiomatic-relativity/sources.jsonl knowledge/arrow-cosmology/sources.jsonl knowledge/causal-sets/sources.jsonl knowledge/time-interpretations/sources.jsonl knowledge/preferred-foliation/sources.jsonl
5 files, 95 records: 0 errors, 0 warnings, 0 info

git diff --check -- <the five assigned registers>
(clean)
```

All five before hashes are in `research/redteam/source-repairs/before-manifest.json`; resulting hashes are:

```text
knowledge/axiomatic-relativity/sources.jsonl e868d3b9e6ede3b6d1735adb9061b02063565994d6fc29bac63f21c69fc90427
knowledge/arrow-cosmology/sources.jsonl      2f258762736419319b97adb8cf2581968be7a268252f61959d2f20f28115943b
knowledge/causal-sets/sources.jsonl          10b241266f104c9738de056084f58e1789e179e0743226b3dc0bffd0a292c401
knowledge/time-interpretations/sources.jsonl 249abde28b1c2d6b28489c5414b8ec848a351481e564b892e2fad196d575e583
knowledge/preferred-foliation/sources.jsonl  c00ebb51dea54de6aab3cbf8083b2d5d71fcbd53e188f8c9fbfe678e607d383f
```

No source audit snapshots, shared seeds, other lanes, coordinator files, or workboard state were edited. The strict run covers only these five assigned registers; it does not establish whole-project clearance. Source audit findings are bounded spot-checks, not independent derivations or a complete proof audit.
