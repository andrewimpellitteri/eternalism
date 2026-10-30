# Review disposition and next obligations, 30 October 2026

Three bounded review tasks are integrated and accepted internally. Their
reports are evidence to inspect, not votes establishing the conclusions.
The coordinator re-derived the load-bearing analytic steps, applied the
repairs below, reran the small checks, and preserved raw reviewer errors
with this disposition rather than silently rewriting their reports.

| Review | Raw handback | Integration | Accepted scope |
|---|---|---|---|
| LOY source inputs | a373453 | 2920791 | Printed finite-order inputs, exact mixed-derivative repair and source limitations |
| Cartesian lifting | 0ca5ad1 | 8eb59d6 | Conditional C¹,¹ metric/scalar reconstruction and geodesic IVP |
| Persistence | 12b7a15 | 4311e56 | n≥2 four-case census and its premise table; null-step correction |

Each lane retains AGENT_REPORT.md and the exact root handback as
RUNNER_REPORT.md. The shared pre-existing root report is preserved.

## Corrections needed for use downstream

* O7 is strengthened in AXIS_C11_RECONSTRUCTION.md: w=rc has zero axis
  value from bounded c alone. Its exact integrating-factor solution,
  with K≤0, gives |w|≤Cr². No logarithmic contradiction, unproved parity
  input, or Gronwall growth constant is needed.
* The off-axis gradient is locally Lipschitz, not necessarily C¹. The
  cross-axis proof uses opposite spatial rays, |x|+|y|=|x−y|. The earlier
  spacetime/spatial-coordinate subtraction was ill-typed.
* The full reduced wave equations are explicit hypotheses. The odd-scalar
  counterexample refutes a weaker bounds-and-mass-only lemma; it does not
  satisfy the full coupled equations.
* Raw-TeX and HTML equation numbers differ. The normalized wave/log-λ
  equations used here are HTML v1 (2.6), (2.8); mass is (2.10)–(2.11).
  Source numerical locators in a raw review cannot be transferred blindly.
* The lift report contains unused sign/derivative typos: ρ≥0 corresponds
  to u≤v, r_ρ=λ−ν, and the established general second-mass bound is
  O(r), not an unproved improved m_tt=O(r²). The coordinator proof does
  not consume those erroneous intermediate claims.
* The persistence review's printed fifth-example comparison mislabels
  B/C probe values. Its function and distinctness assertions are correct;
  the earlier inspection records the corrected patterns.

The n≥2 four-case theorem and the finite-order C¹,¹ reconstruction may be
used downstream with their named hypotheses and these corrections. The
Prop 3.18 u-side source estimates remain printed proof sketches; no new
independent reconstruction of those external estimates is claimed. Smooth
MGHD applicability, continuous central curvature and novelty remain open.

## New classification repairs are a separate review target

The later 1+1 sixteen-case extension was outside the accepted persistence
review. The 30 October audit corrects its topology, reflection and premise
conventions: closed cases include two null half-spaces; reflection
invariance gives four rules versus ten mirror classes; P_c+F_t gives nine
cases whereas P_c+F_c gives four. The new exact witness checker passes.
Those completeness/refinement claims are still coordinator deductions,
now assigned a dedicated adversarial review.

## Four next tasks

1. `ontology-null-refinements-review`: independent completeness/converse
   audit of all 1+1 refinements, including the strongest counterexamples.
2. `lawful-finite-control-review`: compactness/uniqueness continuity,
   degree and fixed incoming-mass interpolation, in the actual C¹,¹ class.
3. `lawful-higher-regularity-audit`: check exact published/preprint scope;
   resolve cone-based versus two-sided-scattering hypotheses.
4. `ontology-persistence-priorart`: attack novelty by exact primary
   predecessor/corollary comparison.

These are disjoint GLM tasks. A valid negative result is an acceptable
outcome. The philosophical target is to identify which independently
defensible bridge premises do explanatory work; neither a regular metric
nor a census of consistent inventories supplies those premises.

Checks: integrated lift checker 14/14; persistence and fifth-example exact
witnesses; sixteen-case, P_c+F_c and new refinement witnesses all pass.
These checks corroborate analytic arguments and do not prove continuum
completeness. Workboard validates 198 safe, acyclic tasks. No installation,
large run, manuscript change or source-depth upgrade from an abstract.
