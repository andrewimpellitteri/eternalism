# Source references and work aliases

`sources.jsonl` contains source records. An inherited source uses a separate
`source-refs.jsonl` entry, resolved by the pair `canonical_file` and `id`.
Resolve that pair directly; do not search for a similarly titled paper or copy
the payload into another source register. A reference has no independent claim
to full-text reading. Existing text citations by source ID remain valid.

Each reference records:

- `id`, `canonical_file`, and `relation: inherited-source` identify its target.
- `decision` names the coordinator policy or primary-backed canonical choice.
- `prior_reading` preserves the original reader attribution, depth, version
  (including null when unrecorded), check date, source path/line, and any map role.
  Its `snapshot`, Git `revision`, and normalized `record_sha256` identify the
  complete old payload in the frozen migration archive. Unknown personal reader
  identity remains unknown; lane attribution is not an invented identity.
- `limits` prevents a current canonical extraction from upgrading an earlier
  reader's scope. The archive retains old errors as historical evidence, not as
  current competing metadata.

The first migration archive is
`research/redteam/source-repairs/before-records.jsonl`; the second is
`research/redteam/new-lane-canonicalization/before-records.jsonl`. Each row has `path`,
`line`, and the original `record`. Its manifest pins the Git revision, original
file byte hashes and archive byte hash. Record hashes use UTF-8 JSON with sorted
keys and `ensure_ascii=False`, with Python's default JSON separators. These are
integrity checks against the recorded snapshot, not signatures or protection
against someone rewriting both archive and manifest.

The three previously reviewed ico-qrf supersessions retain their original
shallow frontier readings in references. The measurement paper also resolves to
ico-qrf: arXiv:2308.10967v1's header supplies Hausmann, Schmidhuber, Castro-Ruiz
and 21 August 2023. This choice follows primary metadata and extraction review,
not equal-depth voting. Theory-map keeps its three original `map-*` records and
references the 59 inherited source IDs. Its old extraction/map annotations are
retained in the archive, including a stale methods copy.

`canonical-aliases.jsonl` groups **different IDs for the same work**. Each group
has a `work_id`, an identifier-backed `identity_basis`, a coordinator-selected
navigation `canonical`, and `members` retaining their file, ID, version and depth.
It is a curated registry, not an exhaustive title-matching result. A canonical
navigation target does not erase another member's edition or source-owner
record. Shared seed records remain historical leads. Singleton groups may attach
separate bounded readings or historical proposal locators; these do not upgrade
the original member. In particular, McTaggart's pp. 458–461 passage check does
not turn its discovery record into a whole-paper reading. Additional readings
and proposals retain their own explicit scope and audit locator.

The second migration retains frontier as the canonical home for the two sector
re-reads, recording their new findings separately in the canonical records'
reading histories. It retains the reviewed CSG-quantum primary records for
`cs-brightwell-2003-observables` and `cs-surya-zalel-2020`, with the earlier
causal-sets discovery readings preserved as references. This removes four new
duplicate payloads without replacing either migration archive or any prior
reference.

Run:

```sh
python3 research/redteam/new-lane-canonicalization/check_references.py
python3 scripts/check_sources.py --strict knowledge research
```

The first checks both archives, explicit canonical targets, prior-reading
fields/hashes, coverage of removed copies, curated aliases, ID preservation and
the unchanged shared seed. A reference can preserve a copy appearing in both
archives only when its lane, ID and exact normalized payload hash agree. This
checker also fails on global duplicate IDs. The second enforces the whole
source-record contract. The first migration's snapshot-specific validator and
saved test results remain historical evidence; it cannot validate new references
to the second archive. Concurrent lanes can introduce further changes requiring
new coordinator decisions. Neither check establishes source entailment, theorem
correctness, priority or temporal ontology.
