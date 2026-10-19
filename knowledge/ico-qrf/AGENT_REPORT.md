# AGENT_REPORT — kb-ico-qrf

Task: compare indefinite causal order, process matrices, and temporal
quantum reference frames. Worktree:
`/Users/andrew/eternalism/.worktrees/kb-ico-qrf`, branch `agent/kb-ico-qrf`.
Status: **worker submission for independent review** — not an accepted
completion and not a truth claim.

## Done / files

- Read to full text all four assigned anchors and the process-matrix
  framework paper they cite:
  - arXiv:2211.15685v3 — de la Hamette, Kabel, Christodoulou, Brukner
    (PRL 135, 141402, 2025)
  - arXiv:2603.08845v1 — Baumann, Lock (2026)
  - arXiv:2607.03417v1 — Vanrietvelde (2026)
  - arXiv:2308.10967v1 — Hausmann, Schmidhuber, Castro-Ruiz (published
    Quantum 9, 1616, 2025)
  - arXiv:1105.4464v3 — Oreshkov, Costa, Brukner (Nat. Commun. 3, 1092, 2012)
- Files written (all inside allowed paths):
  - `knowledge/ico-qrf/sources.jsonl` — 18 records, validated unique/required
    fields/honest read_depth (4 reused frontier IDs upgraded to full-text;
    14 new `ico-` records at abstract/discovery depth for the cited
    process-matrix and QRF-adjacent literature).
  - `knowledge/ico-qrf/comparison.md` — theory-comparison contract filled for
    each anchor model/version; transformation rules; the precise divergences
    between frame-relative order and process-matrix indefinite order; concept
    discipline (ontology/passage/determinism/causal order/clock time/
    thermodynamic arrow); nearest predecessors and gap-defeating conditions.
  - `knowledge/ico-qrf/invariants.md` — table of invariant vs frame-dependent
    quantities per anchor with each paper's smallest finite-dimensional
    example.
- Cross-cutting findings (all traced to locators in the sources):
  1. Transformation rules exist only in two of the anchors: A's quantum
     diffeomorphisms `|1⟩⟨1|⊗𝒰1+|2⟩⟨2|⊗𝒰2` (asserted, not cast in QRF
     formalism by the authors) and C's Page-Wootters frame change
     `𝒮_{i→j}=ℛ_j ℛ_i^{-1}`. B has only an ideal-clock TO↔PM equivalence
     map; D and E have none (D explicitly defers; E has no perspectives).
  2. Frame-invariant in every anchor that has frames: the
     definite-vs-indefinite status of order (A proves it for the proper-time
     sign product s^(1)s^(2); C verifies it for its relational quantum
     switch). Frame-dependent: which events are localized/timed, which
     operation appears delocalized, and (A) whether the indefiniteness is
     "due to" delocalized events or a superposed metric.
  3. Frame-relative order differs from process-matrix indefinite order in
     both directions: frame-dependent/approximate order disagreements exist
     with no process matrix at all (C App. A, Hermitian dilations only, and
     only approximately; B's non-ideal-PM "indefinite temporal order" is a
     clock-resource limitation with a unitary TO recasting), while
     frame-invariantly indefinite scenarios (A's optical switch reading; C's
     relational switch) have no established causal nonseparability — no
     anchor computes a process matrix or plays a causal game for them.
  4. Smallest finite examples per paper are tabulated in
     `invariants.md` (A: encoded order qubit + two 2-level registers;
     B: discrete-clock orthonormal basis t_k=kπ/E model and the qubit+ancilla
     non-unitarity example; C: two-qubit signaling gadget, App. B;
     D: position qubit (|x0⟩+|x1⟩)/√2 with one internal register;
     E: the four-qubit process of its Eq. (7)).

## Search capability check

- Tested first with one relevant query ("temporal quantum reference frames
  indefinite causal order process matrix") using the built-in `websearch`
  tool: **failed** twice with `{"error":{"type":"unknown","message":"Web
  search cancelled"}}`. No Z.ai `web-search-prime` MCP tool was exposed in
  this session's tool list.
- Fallback used: direct `webfetch` of arXiv abs pages and arXiv HTML
  (LaTeXML) full texts — **worked** for all five anchors plus the OCB abs
  page. No Cloudflare blocks or other unread-but-needed pages occurred.
- Consequently there is **no independent citation-forward search** this
  session (no Scholar/OpenAlex/Semantic Scholar pass). Coverage is backward
  (references of the anchors) plus records the anchors themselves elevate.
  This is recorded as a limitation, not hidden.

## Source coverage

- Full text (5): the four anchors + OCB 2012. All arXiv HTML versions read
  in full including appendices, except: B's published Quantum 9, 1616 (2025)
  version was not separately read (v1 is the only arXiv version; the journal
  DOI 10.22331/q-2025-01-30-1616 was taken from C's reference [25]).
- Abstract (2): Vilasini–Renner PRA 110, 022227 (via anchors + abstract-level
  statements quoted in them); nothing else at abstract depth.
- Discovery (11): Chiribella et al. switch; Oreshkov 2019; Castro-Ruiz et
  al. PRX 2018; Vilasini–Renner PRL 2024; Baumann et al. PRR 2022;
  Guérin–Brukner 2018; Castro-Ruiz et al. 2020; Apadula et al. 2604.02873;
  Kabel et al. 2025; Ormrod et al. 2023; Araújo et al. 2015; Vilasini et
  al. 2505.21797 — all recorded as leads, flagged as non-load-bearing.
- Existing-ID reuse: the four anchors reuse
  `frontier-qrf-indefinite-order-2022v3`, `frontier-page-wootters-measurements-2023`,
  `frontier-time-delocalization-2026`, `frontier-qrf-operational-meaning-2026`;
  `seed-bell-temporal-order` is cross-referenced, not duplicated.

## Cross-lane correction (needs coordinator action)

`knowledge/frontier/sources.jsonl` record `frontier-page-wootters-measurements-2023`
mislists the authors of arXiv:2308.10967 as "Vincent Baumann, Maximilian
P. E. Lock" and dates v1 "2023-11-10". The actual paper (abs page and HTML,
both fetched this session) is by **Ladina Hausmann, Alexander Schmidhuber,
Esteban Castro-Ruiz**, v1 submitted **2023-08-21**, published as Quantum 9,
1616 (2025). The frontier record's section/equation locators are broadly
correct. My lane record reuses the same ID with corrected metadata; the
frontier file itself was not touched (outside my allowed paths).

## Verification commands and results

```sh
# JSONL validity, required fields, allowed read_depth, unique IDs
python3 -c "..."   # (inline script, see below)
# → records: 18 ok: True
```

Inline script checked per line: JSON parse; presence of id/title/url/
checked_on/read_depth/kind/relevance/limits; read_depth in
{discovery, abstract, full-text, reproduced, code-audited}; ID uniqueness.
All passed. Full-text claims were spot-verified against the fetched HTML:
e.g. A's Def. 1/Def. 2 and Eq. (7); B's Eqs. (15)–(17) and App. G Eq. (108);
C's Eqs. (13)–(15), (68), (75); D's Eqs. (6)–(10); E's Eqs. (3)–(8) and
(20)–(27). No numerical reproduction was attempted or claimed.

## Strongest contrary evidence (to the anchors' strongest readings)

- **Against "QRF frame-change ⇒ order can flip freely":** C's own Sec. VI.3
  (order is the same in both frames for sharply synchronized clocks) and
  App. A (disagreement needs opposing clock signs, approximate agreement, and
  Hermitian dilations) — frame-dependent order is the exception in their own
  model.
- **Against "non-ideal-clock indefiniteness (B) = fundamental ICO":** B's own
  App. F recasts PM probabilities as TO conditional probabilities with
  unitary evolution and time-non-local operators; E's framework has no
  frames; no causal-nonseparability witness is computed for B's scenario.
- **Against "ICO realization certifies quantum spacetime":** A's own no-go
  (no quantum coordinates with localized events + definite metric + ICO) and
  its curvature caveat; consistent with Vilasini–Renner no-gos (abstract
  depth only — flagged).
- **Against "process-matrix ICO is about time":** E is time-free by
  construction; its ICO is signaling-structure nonseparability. Conflating it
  with temporal order is a category error the anchors themselves mostly
  avoid (B and C flag, not claim).

## Limitations

- No citation-forward search (search tool down); novelty-adjacent judgments
  are therefore confined to predecessor lists with defeat conditions, as the
  brief requires — no gap is claimed.
- The 2025 published version of B was not read (arXiv v1 only); C and D are
  single-version preprints not yet peer-reviewed.
- Perturbative/constructive calculations in B (App. E), C (App. C Dyson
  method), A (App. A diffeomorphism constructions), and E (App. .5
  probability computation) were read, not reproduced. No code was run on
  any model.
- Discovery-depth sources are leads only; several are likely to matter
  (especially `ico-oreshkov-time-delocalized-2019` and
  `ico-apadula-frame-process-matrices-2026`) and are flagged as
  top-priority verification reads before anyone treats §4/§6 of
  `comparison.md` as settled.
- Read-depth labels in `sources.jsonl` are honest to this session's access;
  `checked_on` 2026-10-19 for all.

## Proposed next tasks

1. Full-text read of Oreshkov, "Time-delocalized quantum subsystems"
   (Quantum 3, 206, 2019) and Apadula–Grinbaum–Brukner (2604.02873):
   these two most directly bear on whether frame-relative and
   process-matrix order notions have already been equated.
2. Verify at abstract/full depth the Vilasini–Renner pair (PRA 110, 022227;
   PRL 133, 080201) and extract the exact embedding hypotheses relevant to
   A's no-go triple and to C's relational switch.
3. Compute a causal-nonseparability witness (or prove non-existence in the
   relevant scenario class) for C's relational quantum switch and for B's
   non-ideal-PM scenario — small finite-dimensional calculations within
   scope of a follow-up task; this would turn this lane's "unestablished"
   cells into checked ones.
4. Cast A's quantum diffeomorphisms into the perspective-neutral QRF
   formalism for the simplest two-branch, two-qubit instance (A's own stated
   open problem, finite-dimensional version).
5. Coordinator: fix the authorship/version metadata of
   `frontier-page-wootters-measurements-2023` in the frontier lane record.

## Blockers

None outstanding. The assigned deliverables (sources.jsonl with versions and
read depth; comparison contract per anchor; invariants table with smallest
finite examples) are complete within the stated limits above.
