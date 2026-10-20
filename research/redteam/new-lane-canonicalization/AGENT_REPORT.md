# New-lane canonical references

Coordinator: `codex-new-lane-refs`, 2026-10-20. Two native workers handled
disjoint source pairs; a third independently reviewed the two-archive validator
using temporary fixtures. This integrates already accepted literature lanes,
not new theory work.

## Decisions and preservation

The two sector-conditioning payloads for
`frontier-qrf-beyond-subsystems-2026` and
`frontier-relativistic-trinity-2020v1` became references to their existing
frontier homes. The canonical frontier records now retain attributed reading
histories for both lanes, including the later section/example rereads and their
normalization, domain and observable-scope limits. Their original summaries and
versions were retained. The histories use the standard `full-text` depth plus
separate bounded scopes. See `sector/AGENT_REPORT.md`.

The causal-sets discovery payloads for `cs-brightwell-2003-observables` and
`cs-surya-zalel-2020` became references to the CSG-quantum records. This follows
exact work/edition correspondence, the accepted primary extraction and its
review, not an automatic preference for the deepest reader. The CSG records and
extraction remain intact. Each old discovery reading retains its null original
version, date, lane, unknown personal reader identity and explicit not-read
status. See `csg/AGENT_REPORT.md`.

All four removed payloads remain in this task's own snapshot at revision
`c480ff1ce0e9d4f01e5e8f5bdef4af86a7bc3326`. Every reference pins the full
original record by archive/path/line, normalized hash, version/depth/date and
revision. The previous migration's archive, 63 references and accepted audit
artifacts remain unchanged. Existing theory-map and alias targets still resolve.

## Verification

Before: **25 files, 340 records, six strict errors**, from four duplicate IDs
and two discovery/full-text conflicts. After: **25 files, 336 records / 336
unique IDs; zero errors, warnings or info findings** in the whole-project strict
check. This is recorded schema/identity clearance, not source-entailment or
theorem correctness.

The generalized current validator checks both migration archives and reports
**67 references, eight alias groups, no duplicate IDs, pass**. It fails on any
global duplicate, missing explicit canonical target, unpreserved removed copy,
archive digest mismatch, changed seed or altered reference/alias provenance.
An unchanged copy recurring in both snapshots can be preserved by a reference
to either exact matching lane/ID/payload hash; ID-only matching is insufficient.
The previous snapshot-specific validator is preserved as historical evidence;
`knowledge/SOURCE_REFERENCES.md` now points to the current validator.

Eight independent reference-fixture tests and 12 coordination tests pass, as do
the local CSG verifier, board validation and whitespace checks. Commands and
results are in `verification.json`, `*-after.txt`, `reference-integrity.txt`,
`csg-reference-integrity.txt`, `coordination-tests.txt`, `board-validation.txt`
and `review/tests.txt`. Before/after manifests and `dispositions.jsonl` record
exact hashes and the four removals/two attributed-history additions.

## Files changed and limitations

- `knowledge/frontier/sources.jsonl`: two attributed reading histories.
- `knowledge/sector-conditioning/sources.jsonl`,
  `knowledge/causal-sets/sources.jsonl`: two copied records removed from each.
- `knowledge/{sector-conditioning,causal-sets}/source-refs.jsonl`: four new
  references in total.
- `knowledge/SOURCE_REFERENCES.md`: second-archive semantics/current command.
- `research/redteam/new-lane-canonicalization/`: snapshots, manifests,
  dispositions, validator, worker/independent-review reports, tests and results.

No changes to shared seeds, prior migration snapshots, the CSG extraction,
Claude's worktrees, paper, runner or source-alias payloads were needed. Source
identity checks do not independently reproduce the cited physics. The first
migration's dated global-failure report remains accurate for its own cutoff.
Future lane integrations require a new check rather than inheriting this pass.
