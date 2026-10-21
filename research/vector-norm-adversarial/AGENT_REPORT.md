# Adversarial audit: norm-only Hilbert and Banach classifications

Sole-worker audit, 2026-10-21. Targets:
`research/adversarial-review/coordinator/HILBERT_NORM_BOUNDARY.md` and
`BANACH_NORM_BOUNDARY.md`. Scope: prescribed cylinder **norms** only; not the
fixed complex premeasure, not phases/off-diagonal data, not a physical
dynamics.

## Verdict

**Both candidate classifications survive this audit, with the stated scope.**
I found no counterexample to the Hilbert disk `a^2+b^2 <= 1` or to the Banach
DP domain `p=1` or `|p|<1, |1-p|<=1` (all-cylinder: endpoints or both strict
inequalities). The candidates should not be promoted beyond norm-only
realizations: the Hilbert construction demonstrably changes finite-union
interference.

## Attempted falsifiers and why they fail

1. **Hilbert necessity via disjoint squared sums.** For a Hilbert-valued
   measure of bounded range `M`, average `||sum_j eps_j mu(E_j)||^2` over
   independent signs. Each signed sum is `mu(A)-mu(B)`, norm at most `2M`, so
   the average is at most `4M^2`; the average also equals `sum_j ||mu(E_j)||^2`.
   This does not assume finite total variation, so the usual variation escape
   is unavailable. The two-cap squared level sum then diverges when
   `a^2+b^2>1`. I checked the algebra of the cap exponents:
   `L(G+u+v)=L(G)+M(G)+1`, `h` unchanged.
2. **Hilbert sufficiency.** The random environment `G` has the required first
   two moments (`EG=x`, `EG^2=a^2`, `E(1-G)^2=b^2`) by construction. Conditional
   independence of forward edges gives the cylinder second moment; the tail
   bound `||mu(T_N)||_2 <= P(T_N)^{1/2}` gives norm countable additivity.
   Potential loophole: transitive closure through vertices outside a cylinder.
   It is closed because cylinders are down-sets and outside vertices have
   larger labels, so they cannot mediate between earlier elements.
3. **Banach `c0` construction.** The weight `w_C=a^L b^h` is controlled by
   `rho^{n-1}` with `rho=max(a,b)<1`; each new vertex contributes a cover or an
   incomparable pair. The coordinatewise nesting argument uses the conditional
   factor `r^{Delta L}(1-r)^{Delta h}` with `r<=a`, `1-r<=b`, which compensates
   the larger weight of a shorter cylinder. I found no norm overrun at
   coordinate `C=D`.
4. **Boundary attacks.** At `a=1, b>0`, the disjoint `chain_n + A_2 + u + v`
   family has constant norm `b`; at `b=1, a>0`, the all-cylinder first-edge
   family has constant norm `a`. Both violate countable additivity. At `p=0,1`
   the scalar probability measures exist. These boundary families are the
   places a counterexample would most likely hide; they behave as claimed.
5. **Finite-union witness.** The Hilbert construction gives `221/4096` in the
   original scalar model versus `669/4096` in the realization for the union of
   the three-chain and three-antichain cylinders at `p=1/2+i/4`, while matching
   both diagonal norms. This is a genuine scope limitation, not a refutation
   of the norm classification.

## Checks run

- `python3 research/adversarial-review/coordinator/check_hilbert_environment.py`
  passes the environment moments, 50 cylinder squared norms at four rational
  points, the squared DP level identity through n=5, and the finite-union
  witness.
- `python3 research/adversarial-review/coordinator/check_c0_construction.py`
  passes 12 prescribed norms at two boundary points, conditional
  probabilities, partition bounds, and both disjoint boundary families.

## Limits

- This is a post-hoc audit, not a blind first reconstruction: I read the
  candidate notes before writing this report. The task's original
  blind-first requirement is therefore not met.
- The checks are finite corroboration; the infinite classifications rest on
  the written arguments.
- No global priority search was performed. The notes themselves record only a
  bounded search. The constructions use standard conditional-expectation,
  vector-measure and capacity-style ingredients; that is not a novelty claim.
- The Hilbert and Banach results are realizations of norm data, not extensions
  of the fixed scalar premeasure, not quantum dynamics, and not statements
  about covariance or ontology.
