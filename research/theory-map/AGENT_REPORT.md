# AGENT_REPORT.md — theory-map

Task: `theory-map` — synthesize a broad assumption and observable map
without erasing disagreements. Worker submission for independent review;
not accepted completion. Date: 2026-10-19. Worktree:
`/Users/andrew/eternalism/.worktrees/theory-map`, branch `agent/theory-map`.

## Done / files

Deliverables in the owned path `research/theory-map/`:

| File | Content |
|---|---|
| `README.md` | Scope, method, coverage accounting, non-goals, provenance caveats. |
| `model-graph.md` | 32 model/version/interpretation nodes (`N01`–`N32`) in 6 clusters, each with the six comparison-contract fields (existence/passage/fixed future; state space, dynamics, causal structure, clocks; symmetries, preferred structure, access, boundary conditions; observables and empirical status; bridge premises; equivalences/contradictions/domain restrictions) plus the edge index. |
| `translations.md` | 22 connections (`X01`–`X22`): explicit maps with formulas only from recorded sources, partial maps with domains/failure modes, or `[conjectural]` labels with falsifiers. |
| `disagreements.md` | 9 precise disagreements (`D01`–`D09`) with parties, exact disputed premises, decision procedures, and why averaging is prohibited. |
| `research-contracts.md` | 5 candidate contracts (`RC-1`–`RC-5`) with testable mathematical content, predecessor comparisons, falsifiers, and novelty-kind separation; all flagged unvetted. |
| `sources.jsonl` | 62 records: 59 inherited verbatim from lane files (tagged `inherited_from`), 3 newly checked abstract pages by this worker. |

Done-when criteria: (1) every model node cites source IDs with versions and
read depths — verified mechanically; (2) every connection is an explicit
map or labeled conjectural — enforced by the schema of `translations.md`;
(3) five research contracts with testable mathematical content (brief
required at least three).

## Search capability check

- `websearch` tool (session's configured search integration): **FAILED** —
  two attempts, both returned `{"error":{"type":"unknown","message":"Web
  search cancelled"}}` on map-relevant queries (periodic-clock trinity;
  Chataignier arXiv:2409.06479).
- `web-search-prime` MCP server: not reachable from this session —
  `opencode.list_mcp_resources` returned zero resources and zero templates
  (no server exposes anything here). I could not test that tool directly.
- `webfetch` (direct HTTP): **WORKED** — 3/3 arXiv abstract pages fetched
  (2409.06479, 2107.11452, 2211.15685).
- Consequence: no search-summary leads were used. All content comes from
  (a) the accepted lanes' own checked records, inherited with provenance
  tags, and (b) the three primary pages I fetched and pinned myself. No
  source is cited at a depth it was not read.

## Source coverage

- 62 records total. Inherited: 12 discovery, 22 abstract, 21 full-text,
  4 code-audited. New by this worker: 3 abstract (exact versions pinned in
  the records: 2409.06479v3 / NJP 28 034504; 2107.11452v1; 2211.15685v3 /
  PRL 135, 141402).
- Families mapped: relativistic kinematics and ontological arguments (7
  nodes), causal sets (2), relational quantum clocks (7), QRFs and causal
  order (7), thermal time/records (7 + 2 registered leads),
  formalization/methods anchors (2).
- Known gaps carried forward, not hidden: canonical quantum gravity (one
  routing node), strong growing-block/moving-spotlight (registered as
  explicitly unmapped, N07), collapse and Bohmian preferred-structure
  families (absent), causal-set literature only at abstract depth. This
  matches `knowledge/SEARCH_LOG.md` and the review notes' finding that
  coverage is far under the 60–100 screened target — the map's inputs are
  the lanes, which are seed-stage.

## Verification commands and results

1. `python3 /private/tmp/opencode/build_sources.py` — built
   `sources.jsonl` programmatically from the five lane files (no manual
   transcription), with hard failure on missing/extra IDs. Result: 59
   inherited + 3 new, no errors.
2. `python3 /private/tmp/opencode/verify_map.py` — mechanical checks:
   every JSONL record parses and has the required fields; every
   `read_depth` in the allowed set; no duplicate IDs; every source ID,
   node ID (`Nxx`), edge ID (`Xxx`), and disagreement ID (`Dxx`) cited
   anywhere in the map resolves to its definition; edges defined in
   `translations.md` appear in the model-graph index or the disagreement
   register. Final result: `ALL CHECKS PASSED` — 62 records, 32 nodes, 22
   indexed edges (19 defined in translations + 3 disagreement pointers),
   9 disagreements, 5 contracts. All 62 cited source IDs exist in
   `sources.jsonl`.
3. Grep counts confirm: 32 `### N` node headings; 19 `## X` translations;
   9 `## D` disagreements; 5 `## RC-` contracts.

## Strongest contrary evidence (to the map's own framing and to its main candidates)

- **Against "generic non-ideal-clock equivalence" gaps:** the trinity
  already covers nonorthogonal covariant POVMs and bounded/half-line
  spectra, the relativistic extension handles frequency sectors, and N13
  (periodic clocks) plus N14 (quasi-ideal clocks with interaction) occupy
  adjacent ground (`knowledge/frontier/candidates.md` second-pass
  correction). This is why RC-1/RC-3 are framed as classifications with
  mandatory falsifier searches, not as gaps.
- **Against "frame changes can be physically informative by
  representation":** N21's authors report an observable that does not
  distinguish optical from gravitational quantum switches; N19's record
  states representation change alone changes no prediction. The map
  encodes this as a standing constraint on every conjectural QRF bridge.
- **Against reading definability results as ontology:** Sarkar–Stachel
  show Malament uniqueness is premise-fragile; the audit shows Stein's
  isolated OCR'd theorem is false and its valid reconstruction yields
  causal past, not passage; the project's own checks cases contain the
  countermodels. X16/RC-2 preserve this rather than the folklore slogan.
- **Against thermal time as passage:** Chua's circularity argument plus the
  Martinetti–Rovelli realization-mode open question; the map's D04 keeps
  the disagreement instead of picking a side.

## Limitations

- No source beyond the three abstract pages was read by this worker;
  inherited depths are the lanes' and are tagged as such. The two
  foundations bibliographic corrections (Stein DOI, Maxwell pages) and the
  unresolved print-vs-OCR question are inherited unresolved.
- Malament's primary paper remains unaccessed anywhere in the project;
  N02's premise list is relayed via full-text critics and a secondary
  exposition, and the node says so.
- Nothing is kernel-verified, reproduced, or numerically computed here
  (X22 labels this). All formulas in maps are transcriptions from recorded
  sources, not re-derivations.
- The frontier lane's `frontier-canonical-clock-sectors-2026` record is
  title-only and excluded from ranking, as the lane itself instructed.
- The conjecture labels are my judgments; a reviewer may regrade any edge
  (e.g., X07 may deserve `conjectural` → `no map`).
- Search integration was down; if the coordinator wants search-summary
  leads (forward citations for N13/N14/N15, causal-set observables
  literature for RC-4), that capability must be retested in a session
  where it works.

## Proposed next tasks

1. **novelty-audit (blocking):** treat RC-1/RC-3 as one family against the
   pinned clock sources plus N13/N14 full texts; run the RC contracts'
   falsifier searches before any implementation. Forward citations of N13
   (v3, March 2026) and N19 are the highest-value searches.
2. **baseline-reproduction:** RC-2's finite ablation certificates (cheapest
   to falsify; two countermodels already exist in
   `knowledge/checks/correspondence-cases.jsonl`) or RC-4's n ≤ 6
   enumeration (fully specified mathematically).
3. **Lane expansion for the map's gaps:** strong growing-block/moving-
   spotlight full texts (N07), canonical quantum gravity beyond the routing
   node, causal-set observables literature (RC-4 falsifier), and full-text
   extraction of the four 2026 QRF/clock abstracts now in the map (N15,
   N16, N20, N23).
4. **Coordinator decision requested:** whether `translations.md` X10's
   falsifier (a temporal-QRF transformation moving an N21-type observable)
   should be promoted to a research contract now or after N20/N21 full-text
   extraction.

## Blockers

None material. The `websearch` outage is recorded above and worked around
with primary-page fetches; no task output depended on it.
