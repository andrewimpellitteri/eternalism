# GLM first review: submissions are not accepted results

2026-10-25. Status check: scalar-priority and echo-robustness have submitted
committed reports and entered review (OpenCode exit 1 after clean committed
handback, not an unfinished-results failure). Echo-exactness remains claimed
and active with a substantial RESULT.md. These are first-pass coordinator
findings, not a completed primary-source/integration audit. Worker files were
read, not edited. Nothing from these lanes is accepted here.

## Exactness: explicit counterexample to the submitted formula

The active exactness worker proposes the union of four inequalities, one being
v=η−d(Z,Y)≤τ. The alleged equality would fix early events near the spatial
antipode. This is false.

Set τ=π/4, b=(τ,Y), and x=(π/8,−Y). Here d=π and v=−7π/8≤τ, so the worker's
formula includes x. Give the Einstein-cylinder wave smooth data at η=π/8:
f≥0 supported in B(−Y,ε), f(−Y)>0, g=0, with ε=π/16. Compare with the zero
solution. The support is disjoint from the entire causal influence of the
chronological past of b: for any (s,Z) in that past, 0<s<τ and d(Z,Y)<τ−s,
so the distance from Z to the data support is greater than

    π − (τ−s) − ε = 11π/16 + s,

whereas |s−π/8|≤π/8. Finite propagation in both time directions therefore
gives zero at every such (s,Z). At x the data give a nonzero value. Dividing
by the positive dust conformal factor yields two admissible dust solutions
agreeing on I_s^-(b) but differing at x. Hence x is not fixed.

The underlying error appears already in identifying A(J^-(b)) with all of
J^-(A(b)): A shifts a truncated past inside M, not an entire past on the full
cylinder. The former has η>π; the latter reaches arbitrarily early slices.
Some of the worker's later spherical-geometry construction also contains
incompatible parameter requirements. Numerical checks cannot rescue the
false stated equality. Preserve any valid late-time lower bound separately.

## Robustness: promising main idea, report needs correction

The all-solution echo being restricted to δ=0 in
ψ_tt=Δψ−(1+δ)ψ is supported by the spectral argument, but the report contains
errors that prevent blanket acceptance:

- Its claim that agreement on I_s^-(b) forces the spatial mean to vanish
  identically on the dust strip is false. The same nonnegative bump data
  above vanish on I_s^-(b) and have nonzero spatial mean at the data slice.
  Orthogonal projection onto the constant mode does not preserve local
  vanishing on a spatial cap.
- The degree-n harmonic multiplicity on S³ is (n+1)², not (n+1)(n+2)/2.
- With the displayed equation, an added ordinary ESU mass has δ=m²,
  not m²=−δ as stated in its setup.
- Its δ=1 homogeneous witness has frequency sqrt(2), not sqrt(5).
- For negative δ the proof uses ω_n+(n+1)≥2(n+1), which is false.
  A safe repair is the weaker denominator bound >n+1 and choosing
  n+1>max(|δ|/2,sqrt(|δ|)), yielding 0<|ω_n−(n+1)|<2. The parity condition
  then forces an impossible nonzero even integer difference.
- Loss of a universal echo identity does not itself disprove a particular
  pointwise fixed-region inclusion. Its final limitations acknowledge this;
  stronger summary statements must be narrowed consistently.

These corrections are elementary and independent of the worker's source
claims. Source correspondence, Huygens classifications and singular-support
assertions still need checking before integration.

## Priority lane: useful source leads, not yet independently verified

The worker reports full-text retrieval of Manchak 2008 and flags the precise
conclusion “compact spacelike slice,” rather than the stronger “compact Cauchy
surface” wording. It identifies Harte–Drivas 2012 as a relevant caustic/Green
function predecessor and recommends treating the flat scalar construction as
an application of standard theory. These are actionable audit leads; they
are not upgraded to independent coordinator full-text verification in this
status note. Wald Appendix D remains explicitly unverified by the worker.

## Current manuscript versus frozen worker input

The live paper has progressed beyond dispatch draft 3. Commit b62a51b adds a
three-diamond theorem reaching late timelike-future events. It is not the same
as the active worker's four-inequality formula. Judge that new theorem on its
own proof and current assumptions; do not import the faulty formula, and do
not treat agreement among reports as proof or novelty certification.
