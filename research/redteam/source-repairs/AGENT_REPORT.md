# Audited source repair integration

Coordinator: `codex-source-repairs`, 2026-10-20. Three native workers handled
disjoint source registers; independent content and reference reviews followed.
The frozen input revision is `edfb80314fe7db51971cadf11f86690da3b71ac9`.

## Applied changes

Seventeen records received field or reading-provenance repairs. The exact
per-record fields and 63 removed-copy dispositions are in `dispositions.jsonl`.

- Foundations/discriminators: Janis authors/archived SEP edition; Malament's new
  primary reading with Props. 1–3 and the universal alternative retained;
  Putnam first/second-pass reconciliation; Brading's complete public-copy reading
  with no publisher-file collation claim; Stein's OCR/context/printed-page caveat.
  Stein 1968 stays discovery. Details: `foundations/AGENT_REPORT.md`.
- Methods: source-backed missing assumptions/conclusions/dependencies and
  Ax-Prover metadata/related ID. Author-reported performance and theorem claims
  remain distinct from a local build or axiom audit. Details: `methods/AGENT_REPORT.md`.
- Physics: SEP revision/archive distinction, Wallace Sec. 7 locator,
  Wüthrich–Callender genericity qualifications, bounded Hartle IGUS attribution,
  exact DGTZ/Tumulka versions from explicit follow-up readings. Details:
  `physics/AGENT_REPORT.md`.
- Frontier: Page's time-asymmetry paper has a new targeted v2 reading with the
  original unversioned reading preserved, explicit CPT/decoherence hypotheses,
  Theorem 1/Eqs. (1)–(17) and discussion locators. This does not attribute a
  precise version retroactively to the earlier reader.

Four frontier payloads became references to ico-qrf: the three explicitly
reviewed supersessions and the primary-header-backed measurement-paper choice.
The latter now uses the correct 21 August 2023 v1 date. All 59 theory-map
inherited payloads became references; its three original `map-*` records remain.
The unchanged ico-qrf payloads were reserialized without substantive changes.
Each reference retains its old reader/depth/version/date and a hash-pinned full
snapshot locator. The archive retains erroneous/stale fields as history.

Eight curated work groups associate known different-ID aliases and attach
separate Putnam historical-lead and McTaggart bounded-reading provenance.
McTaggart's discovery record and the shared seed remain unchanged.
`knowledge/SOURCE_REFERENCES.md` defines the reference and alias semantics.

## Verification and independent review

- Repaired registers: **11 files, 171 records; zero strict errors/warnings**.
- Reference integrity: **63 references, eight work groups; pass**. All original
  IDs survive. Every removed copy has its own archived provenance reference.
  Snapshot bytes and unchanged shared-seed bytes match their manifest hashes.
- Independent review: 13 temporary-fixture/live-integrity tests pass. Initial
  review found missing-reference coverage, absent-alias and snapshot-binding
  gaps; all three were corrected and regression-tested. Content review found
  no blocking scope/edition/provenance errors in foundations/discriminators and
  methods; Malament's propositions were rechecked against the primary scan.
- Coordination tests: 12 pass. JSON parsing and whitespace diff checks pass.

Exact commands/results are in `verification.json`, `strict-repaired.txt`,
`strict-before.txt`, `strict-after.txt`, `reference-integrity.txt`,
`coordination-tests.txt`, and `review/tests.txt`. Before/after manifests record
source byte hashes; `before-records.jsonl` preserves original payloads. The
one-time migration script refuses a repeat migration instead of overwriting refs.

## Whole-project result and remaining decisions

The initial live snapshot had **24 files, 380 records, 74 strict errors**.
Claude integrated its CSG lane during this work. At the final source check the
project has **25 files, 340 records / 336 IDs; six strict errors**. This is not
global clearance. Four duplicate IDs remain outside this migration's source
decisions:

- `frontier-qrf-beyond-subsystems-2026` and
  `frontier-relativistic-trinity-2020v1`: frontier/sector-conditioning copies.
- `cs-brightwell-2003-observables` and `cs-surya-zalel-2020`:
  causal-sets/CSG copies, each also contributing a depth-conflict error.

These newer lane copies require a separate canonical decision, preserving their
new readings and earlier shallow provenance. None was silently removed or
overwritten. References resolve explicit file/ID pairs; the integrity checker
reports these global duplicates separately, and the global strict checker stays
nonzero. It must not be interpreted as a source-truth or novelty gate.

Historical audit/proposed-record files, Claude's active lanes, paper files,
runner and shared seed were untouched. No installs, paid runs, builds of cited
research code, theorem reproduction, priority certification or ontology choice
occurred. Stein's printed-page check and the newly user-supplied Clifton–Hogarth
primary are separate tasks; this migration does not claim those gaps closed.

## Exact changed paths

Source payloads: `knowledge/{foundations,frontier,ico-qrf,methods,
axiomatic-relativity,arrow-cosmology,causal-sets,time-interpretations,
preferred-foliation,discriminators}/sources.jsonl` and
`research/theory-map/sources.jsonl`.

References/schema: `knowledge/frontier/source-refs.jsonl`,
`research/theory-map/source-refs.jsonl`, `knowledge/canonical-aliases.jsonl`,
`knowledge/SOURCE_REFERENCES.md`.

Audit artifacts, migration/check scripts and review tests:
`research/redteam/source-repairs/` (file manifest recorded in verification).
