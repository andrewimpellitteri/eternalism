# observer-growth-channel: agent report

Status: worker submission for review. Not accepted completion. No novelty claim.

## Files written

| path | what |
|---|---|
| `research/observer-growth-channel/RESULT.md` | the result: model, three growth-derived observer algebras/channels, results R1–R6, kill criteria K1–K4, priority audit, access-vs-physics separation, limitations |
| `research/observer-growth-channel/check.py` | exact standard-library checker, 45 assertions, ~30 s at `n = 7` |
| `research/observer-growth-channel/check_output.txt` | captured run of `check.py` (exit 0, `PASS: all checks`) |
| `research/observer-growth-channel/sources.jsonl` | 11 source records with per-record read depth and the inheritance note |
| `research/observer-growth-channel/AGENT_REPORT.md` | this file |

Nothing outside `research/observer-growth-channel/` was written, edited or
committed. `WORKBOARD.jsonl`, `WORKBOARD.md`, `scripts/`, `AGENTS.md`, shared
seed sources and the read-only input task directories were not modified. No
git commit, push, merge, deploy or additional agent launch was performed.

## Read-only inputs consumed

- `research/event-filter-resources/COHERENT_GROWTH.md` (full)
- `research/event-filter-resources/RECORD_LOSS.md` (full)
- `research/event-filter-resources/INDEPENDENT_REVIEW.md` (full)
- `research/covariant-observer-witness/RESULT.md` and `check.py` (full)
- `research/operational-stability/RESULT.md` (full)
- `research/event-filter-resources/{RESULT.md, COORDINATOR_REVIEW.md, AGENT_REPORT.md, check_causal_growth.py}` (full, context)
- `AGENTS.md`, `README.md`, `knowledge/README.md`, `knowledge/NOVELTY.md` (full)
- inherited records in `knowledge/csg-quantum/sources.jsonl` and
  `knowledge/causal-sets/source-refs.jsonl` for the causal-set observables
  literature

## Read depths for cited sources

This is the weakest part of the submission and it is stated plainly in
`sources.jsonl`. **No primary paper was re-read in this task.** The
causal-set results (Brightwell–Dowker–Garcia–Henson–Sorkin 2003; Dowker–Surya
2006; Surya–Zalel 2020; Dowker–Johnston–Surya 2010; Zalel 2023; Frauca–Sorkin
2016) are cited at **abstract depth**, with the project's
coordinator-reviewed full-text records from `knowledge/csg-quantum/`
inherited as the source of the section locators. The locators are therefore
the inherited records' locators, not locators I re-verified.

Two Knuth items are cited at **discovery/abstract depth only** and are
explicitly not load-bearing: they support the "observer = chain of events"
motivation for the clock observer, nothing else.

The project notes (`RECORD_LOSS.md`, `COHERENT_GROWTH.md`, `RESULT.md`,
`INDEPENDENT_REVIEW.md`, `operational-stability/RESULT.md`) were read in full.

Search coverage: the two configured web-search tools were unavailable
(one returned HTTP 429 with a monthly quota exhaustion, one was not
registered). One arXiv API metadata query was run
(`abs:"causal set" AND abs:"observer"`, 20 results) and one arXiv abstract page
was fetched. **No systematic priority search was performed**; no novelty is
claimed and none should be inferred.

## What was done

The brief asked for the arbitrary history-register observer of
`covariant-observer-witness` to be replaced by a finite algebra or channel
derived from an explicit growth/access model, with relabelling covariance
stated, the phase-aligned event tested under quotient and record loss, a
covariant instrument with stated resources or an adjoint-image no-go, a
cardinality-versus-unlabelled comparison, and a scaling or kill criterion.

Delivered:

1. **Model and factorisation.** The level-`n` labelled birth histories of a
   sequential growth process, with the complex percolation amplitude
   `A(C) = p^L q^h`. Proved (and machine-checked for every history at `n ≤ 7`)
   that this is a *product of growth-step amplitudes*
   `p^{m(D_i)} q^{i-|D_i|}`, that `Σ A = 1` and `Σ|A|² = 1`, and that
   `arg A = (L-h)π/4`. The earlier finite comparison used `A` as a poset-level
   weight; it is in fact a growth amplitude, which is what makes the phase a
   birth-order phase.

2. **Three algebras plus the gauge-fixed one.** `A_card` (clock/chain
   observer), `A_k` (bounded-region stem observer), `A_iso` (complete covariant
   observer, proved to be the *maximal* covariant record algebra at fixed `n`),
   and `A_growth` (the diagonal algebra on labelled histories, which is what the
   earlier note actually used and which is not covariant). Covariance is stated
   precisely, including the correction that `S_n` does **not** act on `level_n`,
   so "commutes with relabelling" must be read as "factors through `[C]`".

3. **Recognition threshold.** `E` fails to be measurable for `A_card` at every
   `n ≥ 2` and for `A_k` with `k ≤ n-2`; it becomes measurable exactly at
   `k = n-1` at every tested stage `n = 3,4,5,6` (where the `A_k` partition
   equals the class partition). Explicit witness pairs are printed with covers,
   `L`, `h` and `(L-h) mod 8`. Separately, a **proof** (Identity I1) that `E` is
   measurable by the principal-stem spectrum `{[J^-(x)]}`: `L = Σ_x m(J^-(x))`
   and `h = C(n,2) - Σ_x|J^-(x)|`, both class invariants of the collected pasts.

4. **Adjoint-image no-go, with both channel models separated.** For a classical
   record output, `im(C_r*) = span{P_a}` is commutative and `T_E` (rank 1,
   `|E| ≥ 2`) is not in it, for every record map at every stage. For a
   non-demolition dephasing channel the block-diagonal algebra excludes `T_E`
   whenever the record separates two histories of `E`, which `A_iso` does at
   every `n ≥ 3`; the degenerate single-atom case is flagged as vacuous rather
   than hidden.

5. **Exact visibility theorem.** `Φ_γ = γ·id + (1-γ)·Π`; the compressed 2×2
   block has determinant `η² w₁w₂(1-γ^{-2})`, so exact realisation requires
   `γ = 1` on every class pair met by `E`. Verified exactly at `n = 5`.

6. **What the quotient does to the divergence.** The amplitude is
   class-constant, so the divergence survives the label quotient — but the
   register sum is *not* a function of the class amplitudes alone: it carries
   the labelling multiplicities `m_κ`. Three sums are tabulated
   (`S_reg`, `S_unl`, `S_orb`), and only `S_orb = Σ√m_κ A_κ` has `|·|²` as a
   normalised class probability. `|S_reg|²` reaches 2293.3 at `n = 7`;
   `|S_orb|²` reaches 77.3. So the event survives, at a reduced rate.

7. **No probability diverges.** `P_cl(E)` stays in `[0.24, 0.30]`; the
   efficiency-limited filter probability `|S_reg|²/|E|` decays to 0.093 by
   `n = 7`. The interference share of the register sum is
   0, 0.5, 0.907, 0.983, 0.998, 0.9999.

8. **Kill criteria K1–K4 and survival criterion** as stated in RESULT.md §6.

## Exact checks

`python3 research/observer-growth-channel/check.py` → exit 0, 45 assertions,
`PASS: all checks`, 30.2 s, standard library only, no installs.

Highlights (all in `check_output.txt`):

- level sizes `1, 1, 2, 7, 40, 357, 4824, 96428` (integer enumeration);
- isomorphism-class counts `1, 2, 5, 16, 63, 318, 2045` — equal to the number of
  unlabelled posets (A000112) at every stage, an independent check on the
  enumeration *and* on the canonical form;
- transition factorisation verified for every history, `n ≤ 7`;
- `Σ A = 1` and `Σ|A|² = 1` exactly (rational complex arithmetic) for every
  `n ≤ 7`;
- phase identity `2^{L+h}A² = i^{L-h}` for every history;
- `V_n = 1.0000, 1.4142, 2.6213, 6.0481, 16.7510, 54.2269, 201.0713`;
- stem identities `L = Σ m(J^-)`, `h = C(n,2) - Σ|J^-|` for every history;
- fast canonical form induces **exactly** the brute-force isomorphism partition
  for `n ≤ 5` (validated against `canon_brute`, an all-`n!` minimisation);
- independent brute-force isomorphism test agrees with the class partition on
  sampled intra-class and cross-class pairs at `n = 4, 5`;
- `A`, `L`, `h` constant on every class;
- `P_cl ≤ 1` and `|S_reg|²/|E| ≤ 1` at every stage;
- visibility determinant sign is `≥ 0` exactly at `γ = 1`;
- access table and `k*(n) = n-1` for `n = 3..6`.

### Independent verification

Three independent routes, not one script asserting itself:

1. **Class count vs A000112.** `1, 2, 5, 16, 63, 318, 2045` is the published
   number of unlabelled posets. This cannot be reproduced by a broken
   enumeration or a non-canonical canonical form, so it is a genuine external
   check.
2. **Two canonicalisation algorithms.** The fast form (colour refinement, then
   relabelling cells into blocks) was validated against the all-`n!` brute-force
   form by comparing the *induced partitions* at `n ≤ 5` — not merely the
   counts.
3. **Two amplitude routes.** `A(C)` computed from `(L,h)` and from the product
   of growth-step amplitudes `∏ t(D_i, i)` agree for every history at `n ≤ 7`.
4. **Cross-check against the read-only baseline.** The `|S_reg|²` values
   reproduce `research/covariant-observer-witness/` exactly at `n = 2..6`
   (`0.5, 0.5, 3.2031, 14.4062, 150.7025`), confirming that this task's
   multiplicity convention matches the earlier note's and that the *difference*
   reported in R4 is a difference of convention, not of arithmetic.

## Evidence summary

| claim | evidence | strength |
|---|---|---|
| `A` is a product of growth-step amplitudes | exact check, all histories, `n ≤ 7` | finite; the polynomial identity generalises but was not proved here |
| `E` is determined by the principal-stem spectrum | two-line proof (I1) + exact check | general (proof) |
| `k*(n) = n-1` | exact enumeration `n = 3,4,5,6` | finite; not proved for general `n` |
| `T_E ∉ im(C_r*)` for record channels | structural proof | general |
| `γ = 1` required | 2×2 determinant, exact | general |
| `\|S_orb\|²` diverges | finite values only | **not established** |
| no accessible probability diverges | bounded at every tested stage + `Σ\|A\|² = 1` | general bound to 1; exact values finite |

## Limitations

1. **Finite stage.** Sums to `n = 7`, access thresholds to `n = 6`, brute-force
   isomorphism to `n = 5`. A finite-stage result has that domain only.
2. **Divergence of the covariant sum is not proved.** `|S_orb|²` grows
   `0.5 → 77.3` over `n = 4..7` with ratios `2.8, 4.6, 5.4`. That is a trend,
   not a theorem. The claim actually established is the negative one (no
   accessible probability diverges; `P_cl` bounded, filter probability
   decaying) plus the positive structural one (the effect is outside every
   record channel's image).
3. **`k*(n) = n-1` is measured, not proved.** A uniform witness family for all
   `n` and all `k ≤ n-2` was not found.
4. **The amplitude model is known non-extending.** At `p = (1+i)/2` complex
   percolation has unbounded variation (Surya–Zalel 2020 Thm 2.1;
   Dowker–Johnston–Surya 2010), so in the infinite model the quantum measure
   does not extend to the covariant algebra. Then the infinite covariant event
   has no measure at all and only finite-stage sums exist. This is a property of
   the model, not of the observer analysis, and it bounds what the whole line of
   work can claim.
5. **`A_k` is an assumed access model.** "Collect all partial stems of size
   `≤ k`" is one locality notion among several (interval-based, light-cone,
   poset-distance). A different notion could give a different threshold. The
   threshold result should be read as "for this access model".
6. **Access assumptions are not physics.** The record map, the covariance
   premise, the `1/|E|` all-input efficiency bound, and the visibility `γ` are
   modelling choices. `γ` is not computed from any decoherence model, and the
   record map is not derived from any observer dynamics.
7. **No observer dynamics or region selection.** Nothing here models how a
   record is written, how a region is chosen, or what a cosmological observer's
   actual access is.
8. **Amplitude is not a Bell-causal QSG dynamics.** Bell causality is neither
   imposed nor checked.
9. **The event `E` is tied to `|p| = |q|` and to `p = (1+i)/2`.** A different
   phase gives a different event. Only the structural lesson transfers.
10. **Search coverage is poor** (see above): two search tools unavailable, one
    arXiv metadata query. No priority claim, and the nearest-predecessor
    comparison in RESULT.md §7 is a screening, not a systematic audit.

## Unresolved questions

1. Prove `k*(n) = n-1` for all `n ≥ 3`; ideally exhibit a uniform family of
   pairs with equal `k`-stem spectra and `(L-h)` differing mod 8 for every
   `k ≤ n-2`.
2. Prove or refute divergence of `|S_orb|² = |Σ_κ √m_κ A_κ|²`. A generating
   function in `(L-h mod 8, L+h)` would settle it; the birth-step decomposition
   suggests one exists but it was not found.
3. Is the *correct* covariant amplitude `√m_κ A_κ`, or `√e_κ A_κ` with `e_κ` the
   number of linear extensions? The growth process normalises with `m_κ`; the
   CSG push-forward to unlabelled causets is usually written with `e_κ`. These
   differ by `|Aut_κ|`. R4 uses `m_κ`; the choice should be audited against
   Rideout–Sorkin and Brightwell et al. §6 before the numbers are quoted
   elsewhere.
4. Is there a physically motivated `γ` from a causal-set decoherence model? If
   `γ < 1` is generic, R3 converts the whole line into a no-go.
5. Does the argument survive in an *extending* complex QSG model (Surya–Zalel
   Sec. 3.3, `q ∈ [0,1]`)? Those models have no divergence to explain, so the
   test would become whether a phase-aligned event with bounded measure is
   still invisible to record observers.
6. Is `A_p(C) = p^L q^h` compatible with Bell causality at all? If not, the
   whole amplitude choice is unphysical and only the structural channel results
   survive.

## Checks run (exact command lines)

```
python3 scripts/agents.py brief observer-growth-channel
python3 research/observer-growth-channel/check.py            # 45 checks, exit 0, 30.2 s
python3 research/observer-growth-channel/check.py 6          # reduced depth
python3 -c 'import json; ...'                                # sources.jsonl validity: 0 bad lines
git status --short                                           # only research/observer-growth-channel/ added
```
