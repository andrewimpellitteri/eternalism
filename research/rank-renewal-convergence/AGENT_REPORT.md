# Agent report: rank-renewal-convergence

Worker submission, 2026-10-21, for review. Task `rank-renewal-convergence`
(workboard priority 10). Verdict: **option (a)** — the weighted
absolute-convergence estimate is true and is proved; the conditional obstruction
becomes a genuine no-go under the stated measure-theoretic hypotheses. No
`STATUS.md` is needed; `RESULT.md` is the deliverable.

This is a verification and write-up of the coordinator's candidate
(`research/adversarial-review/coordinator/RANK_FACTOR_NO_GO.md`), not a new
theorem, not a priority claim and not a physical result.

## Files changed

- `research/rank-renewal-convergence/RESULT.md` — statement, proofs, audits,
  finite values, scope, read depths, falsifiers.
- `research/rank-renewal-convergence/check_weighted.py` — exact finite checks
  (standard library only).
- `research/rank-renewal-convergence/check_output.txt` — captured output of a
  clean run (`exit=0`, 68 lines).
- `research/rank-renewal-convergence/AGENT_REPORT.md` — this report.

Nothing outside `research/rank-renewal-convergence/` was written. No edits to
the workboard, runner, `AGENTS.md`, shared sources, or other task directories.
No commit, push, or agent launch.

## Outcome

The obligation left open by
`research/rank-renewal-followup/STATUS.md` and
`research/adversarial-review/coordinator/RENEWAL_OBSTRUCTION.md` was: do the
weighted series `Σ_j |B_j| |κ_{n+j}|` and `Σ_{j,k} |B_j R_k κ_{n+j+k}|`
converge? They do. The right form is

```
Σ_{j≥0} |B_j| / W_{n+j} < ∞ ,       W_n = Σ_{principal |H|=n} N(H)|A_p(H)|
```

which is condition (6) of `RANK_FACTOR_NO_GO.md` and is a property of `p`
alone. Three regime bounds close it:

- `b=|1-p|<1`: `|B_j|` bounded (inclusion–exclusion product bound) and
  `W_n ≥ a t^{n-2}c_s` with `t=a+b>1` (two-cap), so geometric decay.
- `b=1`: `|B_j| ≤ 4^j` and `W_n ≥ a^m(1+a)^{m²}` at `n=2m+1` (explicit
  bipartite family), so superexponential level growth beats `4^j`.
- `b>1`: `|B_j| ≤ 4^j b^{j(j+1)/2}` against `W_n ≥ a^{n-1}b^{C(n-1,2)}` (star
  family); the `b`-exponents cancel to a linear term and the ratio is
  geometric with `4/(a b^{n-2})<1` for all large `n`.

Consequences (with (R) the rank-only all-principal value rule):

- `p∉[0,1]`, `p≠0`: no finite countably additive normalized complex measure
  (tail-zero then backward propagation of the recurrence, then the laminar
  cover contradiction).
- `p=0`: no normalized measure, via `A_0(H)=0` at ranks `≥2` and the same
  cover; the recurrence is not used, so the `p=0` division failure is bypassed.
- `0<p≤1`: classical construction exists. Hence existence is exactly
  `0<p≤1`, confirming the candidate classification.

## Evidence and checks

`python3 research/rank-renewal-convergence/check_weighted.py`

Standard library only, about 50 s, exact arithmetic (`Fraction`, Gaussian
rationals, `Q(√2)`), zero-tolerance assertions. All passed:

- Labelled-vs-shape multiplicity identity (A1, `n=1..5`) and 71 ordinal-sum
  multiplicity checks `N(H⊕S)=N(H)N(S)` (A2).
- Renewal identity `B_m = Σ_{k=1}^m R_k B_{m-k}`, exact for `m=1..8` at
  `p=0, 1/2, 3/2, 2, -1, (1+i)/2`; plus `B_j=R_k=0` at `p=0`.
- Level bounds: `W_n ≥` star and `V_n ≥` two-cap exactly for `n=2..7` at seven
  parameters; `b=1` bipartite bound at `p=2`, `n=3,5,7`.
- `B_j` computed three independent ways (bridge order sum; endpoint
  inclusion–exclusion; brute-force forward-edge percolation with BFS
  reachability) agree exactly for `j≤7` (`j≤4` brute force at five real
  parameters, `j=5` at `p=1/2`; `j≤6` at `(1+i)/2`); bridge bounds (1a)/(1b)
  hold.
- Exponent identity for the `b>1` ratio, exact `j=0..40`.
- Child-sum decomposition `Σ_J A_p(J) = A_p(H) R_{m-n}`, 426 exact identities
  per parameter at four parameters, `n<m≤7`.
- Endpoints: `A_0(H)=0` for all principal `|H|≥2`; `A_1=δ_chain`.

Recorded quantitative instances of (6):
`p=-1` gives `Σ_j|B_j|/W_{5+j} ≤ 1/32`; `p=5/2` gives `≤0.0657`;
`p=-1/2` gives `≤0.0862`.

## What is proved, what is imported

Proved here (self-contained): Lemma 1 (bridge bound, via the endpoint
inclusion–exclusion), Lemma 2(ii)/(iii) (star and bipartite level bounds),
Theorem 1 (the three-regime estimate), the vanishing Proposition (renewal
inversion under (6)), Corollaries 1–3.

Imported (read, not independently re-proved):

1. the two-cap bound `V_n ≥ a t^{n-2}F_{n-2}` and the ordinal-sum renewal
   decomposition from `research/creative/RESULT.md` and
   `research/adversarial-review/coordinator/RENEWAL_OBSTRUCTION.md`;
2. the covariant posts algebra, countable additivity, laminarity and the cover
   `∪_H D_H = P_∞` from `research/creative/COVARIANT_RESULT.md`.

`research/creative/proof-audit/` (which audited the two-cap proof) was **not**
read; that is the main residual risk for the `b<1` case, though Lemma 2(i) is
also corroborated numerically for `n≤7`.

## Limitations

- The result is conditional on the value rule (R) for **all** principal pasts,
  finite countable additivity and normalization on `P_∞`. It says nothing about
  shape-dependent values, DP-only rules, unnormalized measures, or
  Banach/Hilbert norm-prescription problems (the `L²` indicator construction
  prescribes moduli, not complex values, and is untouched).
- The estimates are not sharp; only summability is used.
- No physical, ontological, novelty or priority claim. The three-case strategy
  and the candidate statement are the coordinator's.
- Finite checks are corroboration of bookkeeping, not proof. No truncated-
  polynomial root is used as evidence anywhere.

## Unresolved questions

1. Whether the *complex* series `R(z)=ΣR_k z^k` has positive radius for
   `0<b<1`. Not needed by the proof, and not decided here. The positive segment
   sums `K_k` grow faster than `t^k` at `p=3/2`, so absolute convergence at
   `1/t` is not available; the bridge sums `B_j` remain bounded there.
2. Whether the two-cap bound can be replaced by a self-contained argument in
   this note (it can probably be inlined; not done to keep the audit trail).
3. Whether the same conclusion holds under a weaker event algebra (e.g. the
   labelled generator algebra) with shape-*dependent* control of the bridge
   terms. Not attempted.
4. Independent review of the imported laminar/cover argument is still required
   before the classification is treated as accepted.

## Read depth of sources

Full text: `AGENTS.md`, `README.md`, `knowledge/NOVELTY.md`, task brief,
`research/rank-renewal-followup/STATUS.md`, `.../AGENT_REPORT.md`,
`coordinator/RENEWAL_OBSTRUCTION.md`, `coordinator/RANK_FACTOR_NO_GO.md`,
`coordinator/BOUNDARIES.md`, `coordinator/REVIEW_HISTORY.md`,
`coordinator/VECTOR_COUNTERMODEL.md`, `creative/COVARIANT_RESULT.md`,
`creative/RESULT.md`, `extensions/rank-factor/AGENT_REPORT.md`,
`extensions/covariant-values/AGENT_REPORT.md`.

Code-audited: `coordinator/check_renewal_series.py`,
`coordinator/check_boundaries.py`, `extensions/rank-factor/check_stationarity.py`,
`extensions/rank-factor/kernel_sequence7.py`,
`extensions/rank-factor/probe.py`, `experiments/baseline/poscau.py` (not
imported by my script).

Not read: `creative/proof-audit/`, `coordinator/BANACH_NORM_BOUNDARY.md`,
`coordinator/HILBERT_NORM_BOUNDARY.md`. No external papers were consulted; the
argument is elementary and self-contained apart from the imported two-cap bound.
