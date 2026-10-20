# extension-search — conditional covariant boundary for the selected contract

Status: 2026-10-20. Claimed by `opencode-coordinator` because the GLM quota was
exhausted. Selected target: the labelled doubly-principal complex-percolation
classification (`research/creative/RESULT.md`), with RC-1 as fallback
(`research/redteam/selection-gate/DECISION.md`). This task extends that contract
to covariant post events, produces an explicit countermodel for a weakened
factorization, and audits the changed assumptions. It claims no new theorem and
no temporal ontology.

## Candidate theorem (conditional)

The extension candidate is the **stationary post-factorization boundary**
already derived in `research/creative/COVARIANT_RESULT.md` and
`research/creative/covariant-boundary/BOUNDARY.md`, and audited in
`research/creative/proof-audit/AUDIT.md`. This task consolidates it and gives a
standalone witness; it does not present it as a new result.

Setting: Dowker–Zalel 2212.01149v2, Sec. V, covariant post algebra `R_p`; a
post is an element comparable with every other. For a principal finite order
`H` (`n=|H|`), `D_H` is the event that the causet has infinitely many posts and
has a post whose inclusive past is `H`; `N(H)` is the number of distinct
naturally labelled representatives and `A_p(H)=p^{L}(1-p)^{binom(n,2)-R}`.

**Assumptions.**

1. `nu` is a finite countably additive **complex** measure on `R_p`.
2. `nu(P_infinity)=1` (cyclic normalization; `P_infinity` is the event of
   infinitely many posts).
3. **Common post factor (T)**: there is one finite complex `kappa`,
   independent of `H` and `n`, with
   `nu(D_H) = kappa N(H) A_p(H)` for **every principal** `H`.

**Claim.** Under (1)–(3), such a measure exists **iff** `0 < p <= 1`.

This is conditional on (T). Covariance and the labelled cylinder values do not
imply (T); (T) is an added renewal compatibility axiom. The theorem says nothing
about measures that use different post amplitudes.

## Explicit countermodel: the Dirac history

Weaken (3) to doubly-principal `H` only. The Dirac history

`H = (A_2 + {z_1}) + (A_2 + {z_2}) + ...`

(`A_2` the two-element antichain, `+` ordinal sum) has infinitely many posts
`z_j`, each comparable with every element. Its inclusive post past
`H_j = B_1 + ... + B_j` is principal (unique maximum `z_j`), but `H_j` minus
`z_j` has two maximal elements, so `H_j` is **not doubly principal**.

The Dirac measure `nu = delta_H` has `nu(P_infinity)=1` and `nu(D_H)=0` for
every doubly-principal `H`. Hence the weakened rule
`nu(D_H)=kappa N(H)A_p(H)` (doubly-principal `H` only) holds with `kappa=0` for
**every** `p`. The weakened rule therefore has no `p`-classification, even with
normalization. This is exactly why the conditional theorem assumes (T) for all
principal `H`; see `countermodel.py`.

The Dirac measure violates (T): at `p=0.5`, `H_1` and `H_2` both occur on the
history (`nu(D_{H_j})=1`), but `N(H_1)A_p(H_1)=0.25` and
`N(H_2)A_p(H_2)=0.015625`, so (T) would require `kappa=4` and `kappa=64`
simultaneously.

## Known-result reduction and triviality checks

- **Reduction to the labelled theorem.** For `p in [0,1]`, the labelled
  amplitudes are a probability pre-measure. At `p in (0,1)`, classical
  transitive percolation restricted to `R_p` satisfies (T) with
  `kappa=c(1-p)=prod_j(1-(1-p)^j)>0`. At `p=1` the history is the infinite
  chain, `P_infinity=1`, `kappa=c(0)=1`.
- **Why `p=0` is excluded here but not in the labelled theorem.** At `p=0`
  the labelled measure is the infinite antichain; it has no posts, so
  `nu(P_infinity)=0`. The conditional theorem's normalization premise fails at
  `p=0`, so its scope is `0<p<=1`, not `[0,1]`. This is a scope difference, not
  a contradiction.
- **Normalization is load-bearing.** Without `nu(P_infinity)=1`, `kappa=0`
  gives the zero measure for every `p`; normalization is what turns `kappa=0`
  into a contradiction.
- **All-principal coverage is load-bearing.** The Dirac history satisfies the
  doubly-principal-only rule for every `p`; the all-principal family is needed
  to exclude `kappa=0`.
- **Shape-dependent factors are vacuous.** For any finite `nu` and any
  principal `H` with `N(H)A_p(H) != 0`, set
  `kappa_H = nu(D_H)/(N(H)A_p(H))`. The factorized form holds by definition.
  A shape-dependent rule therefore has no predictive content; only shape-blind
  (common or rank-only) rules can constrain `p`.
- **Rank-only factors: necessary bound, no classification.** If
  `nu(D_H)=kappa_n N(H)A_p(H)`, the same-rank disjoint events give
  `|kappa_n|V_n <= ||nu||_TV`. Since
  `V_n >= |p|(|p|+|1-p|)^{n-2} c_s` diverges for `p notin [0,1]`, `kappa_n`
  must decay at least exponentially:
  `limsup |kappa_n|^{1/n} <= (|p|+|1-p|)^{-1}`. This is necessary only. An
  exponentially decaying `kappa_n` is not excluded, and no consistent
  rank-dependent measure is constructed. The classification is open.
- **Finite level vs all-level.** The finite values `V_5,V_6` illustrate the
  bound; they do not establish divergence. Divergence is the analytic two-cap
  estimate, not a finite search.

## Philosophical bridge-premise audit

- `P_infinity`, `D_H`, and the post events are **measure-theoretic events in a
  causal-set model**, not operational observer records. Treating them as
  observables requires a separate bridge premise; this task does not supply it.
- Covariance is a **kinematic** invariance of the event algebra. The post factor
  (T) is a **dynamical renewal** compatibility condition; covariance alone does
  not imply it. The Dirac countermodel is precisely a covariant measure that
  fails (T).
- The theorem constrains one scalar complex-measure framework on one event
  algebra. It does not imply a new quantum measure, a decoherence functional, a
  physical dynamics, or an empirical prediction.
- No conclusion follows about temporal ontology, objective passage, determinism,
  causal order, clock time, or the thermodynamic arrow. Eternalism/presentism
  are not selected by a measure-existence result.

## Search bounds and negative results

Changed assumptions examined:

| Change | Result |
|---|---|
| Doubly-principal-only factor | **Countermodel** (Dirac history); no `p`-classification. |
| All-principal common factor + normalization | Conditional theorem `0<p<=1` (existing, audited). |
| Rank-only factor `kappa_n` | Necessary exponential attenuation; no construction; open. |
| Shape-dependent factor `kappa_H` | Vacuous (any measure can be written this way). |
| Drop normalization `nu(P_infinity)=1` | Zero measure always satisfies; no classification. |
| Vector/Banach-valued measure | Proof's total-variation step does not transfer; no construction or counterexample; open scope boundary. |
| Larger labelled algebra | Labelled theorem already excludes it by restriction to doubly-principal cylinders. |

Search bounds: this task did not run a new literature search. The bounded
priority search for the conditional result is `research/creative/priority-audit/POST_TAIL_PRIORITY.md`;
no matching theorem was located there, but global priority remains open. The
rank-dependent and vector-valued boundaries were not searched in the literature.

## Files and commands

- `experiments/extensions/countermodel.py` — constructs the Dirac history,
  checks every post past is principal but not doubly principal, and checks the
  weakened/all-principal rules.
- `experiments/extensions/boundary.py` — rank-factor bound, shape-factor
  vacuity, endpoint reduction, normalization, vector-valued scope.
- `experiments/baseline/` — the reproduced Dowker–Zalel criterion and the
  `V_n` computation used here.

```sh
cd experiments/extensions
python3 countermodel.py
python3 boundary.py
```

Both run with the Python standard library only. `countermodel.py` checks
`j=1..6`; `boundary.py` computes `V_5,V_6` from the baseline enumeration.

## Results and limits

- The countermodel is explicit and reproducible; it defeats the weakened
  factorization for every `p`, not a finite sample.
- The conditional theorem is **not newly proved here**. Its proof, laminar
  family argument, finite-cutoff corollaries and priority search are in the
  creative-pass files and the fresh proof audit. This task independently
  re-checks the countermodel and the boundary statements.
- The rank-dependent and vector-valued cases remain open; they are recorded as
  negative search results, not as claims of existence or nonexistence.
- No external mathematical acceptance, publication priority, physical model or
  ontological conclusion is claimed.
