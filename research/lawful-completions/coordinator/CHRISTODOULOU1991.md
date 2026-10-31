# Christodoulou 1991: what the supplied paper actually gives

28 October 2026. Source audit after user supplied cpa.3160440305.pdf.
SHA256 64c3a30309aca30d59e87ee66c2ab098b3966a46036eede0ef75c7600e4e5978.
Printed pp339–373. Read the main-text prose throughout via PDFKit extraction;
selected deep reading of §4 pp354–363 and Theorem5.1 pp363–364 with proof
pp364–372. Inspected page images pp363–364 to recover the formulas missing
or mangled in extraction. This is not a verification of every displayed
field equation or all prior well-posedness results cited by the author.

## Matter model and initial surface

The paper studies spherical Einstein–massless-minimally-coupled-real-scalar:
R_ab=8π(∂_a φ)(∂_b φ), with □_g φ=0 (p339, equations1.1c–d). This is a
specified coupled system, not null dust and not our conformally coupled
massive test scalar on fixed dust. It therefore closes the matter-model
source gap for a scalar-collapse theorem, but does not transfer the earlier
fixed-dust fixing classification to these models.

The centre Γ is a timelike geodesic, parametrized by proper time u with
origin o (p340). C⁺(u) is its outgoing null cone, with generator affine
parameter s=0 at Γ. Scalar derivative data ψ(s)=Dφ are specified on the
initial cone C₀⁺=C⁺(0), and radial constraints determine the other cone
fields (p354). Crucially, the paper explicitly restricts its spacetime
in the following to the FUTURE of C₀⁺ (p356). Initial cone generators are
assumed to extend to affine infinity with r→∞; initial Bondi mass is bounded
(pp361–362). A complete past of o or complete spacelike Cauchy data is not
specified by this formulation.

## Exact quantitative statement used here

Theorem5.1, pp363–364: for an annulus on C₀⁺ with radii R₁=r₁,₀<R₂=r₂,₀,
put

  δ₀=R₂/R₁−1 ∈ (0,1/2),
  η₀=2(m₂,₀−m₁,₀)/R₂,
  E(y)= y/(1+y)² [log(1/(2y))+5−y].

If η₀≥E(δ₀), the outer ingoing hypersurface C₂⁻ meets an outgoing cone
C_*⁺=C⁺(u_*) at a marginal sphere S₂* (outgoing expansion h₂*=0). Among
the conclusions:

- r₂*≥[3δ₀/(1+δ₀)]R₂ and m₂*=r₂*/2, part(b).
- C₁⁻ from the inner sphere meets C_*⁺ at r₁*≥2δ₀R₁>0, part(c).
- u_*≤2(1−2δ₀)R₁, part(d).
- An event horizon is no later than C_*⁺; final Bondi mass M₁≥m₂*>0,
  part(e).
- Every outgoing cone after C_*⁺ has a trapped exterior portion and
  reaches the singular boundary at zero radius, parts(f)–(g).
- The singular boundary is a future boundary, and is strictly spacelike
  away from the central singular set, part(j).

The centre proper-time parameter and initial affine parameter have specific
normalizations. They must not be identified with Vaidya advanced time v.
There is no exact Vaidya logarithmic terminal-time formula in this paper.

## Candidate consequence: a flat region already behind the event horizon

Add the explicit data restriction ψ=0 on the cone interior through S₁,₀,
with a regular centre and scalar constant there. These data have zero inner
mass, and the radial constraints reduce to Minkowski values. Proposition4.1
pp356–358 gives the associated flat constant-scalar diamond D(S₁,₀).
Here D(S₁,₀) denotes the paper's filled-cone diamond, not the domain of
dependence of a bare codimension-two surface under the usual Cauchy
notation. The proof constructs it using the cone interior and its inward
null boundary. In the flat normalization r=s on that initial interior,
the incoming ray from R₁ meets Γ at u=2R₁.

Thus, CONDITIONAL ON admissible smooth initial cone data satisfying both
the zero-interior restriction and Theorem5.1's annular concentration
hypothesis, choose

  2(1−2δ₀)R₁ < u_b < 2R₁.

Then b=Γ(u_b) lies inside that flat diamond, strictly after u_* and the
event horizon's central vertex, yet before the incoming inner boundary
arrives at Γ. In particular a neighborhood of b is exactly Minkowskian,
with constant scalar, even though its outgoing cone is a trapped/singular
cone in the source's future development. This is a source-derived candidate
corollary, not yet independently reviewed. It uses more than a generic
trapped-surface existence theorem: the proper-time and inner-radius bounds
provide the strict gap of width 4δ₀R₁.

The theorem allows zero inner mass; however this audit does not explicitly
construct and globally continue a smooth cone profile realizing all these
hypotheses. Do not replace that obligation by a heuristic pulse argument.

## What remains for the ambitious target and the horizon side-test

1. **Whole-past extension.** Inside the cone-generated spacetime, the past
   of b is truncated by C₀⁺ and fits in the flat diamond. This does not
   establish its full past after extension to a maximal globally hyperbolic
   solution. A compatible backward/exterior characteristic or Cauchy
   construction, with a proof that no new nonflat events enter I⁻(b), is
   required. Agreement only on a finite diamond is insufficient.
2. **Common-future separation.** Parts(g),(j) give much more singular-boundary
   information than mere null incompleteness. To reproduce the Vaidya
   side-test one must still exhibit a particular late exterior x with
   J⁺(x)∩J⁺(b)=∅ in the selected global development. The finite affine length
   of an outgoing cone alone is not a bound on an advanced-time coordinate.
   The source's incoming coordinate is labelled on C₀⁺ and the requisite
   finite-coordinate causal barrier must be derived, not borrowed from
   Vaidya. The causal diagram is suggestive, not a substitute for that proof.
3. **Relational outcome and matched models.** Compare with a trivial-scalar
   development under an explicitly specified marking of b and u. The
   accepted relational lemma supplies invariance only. Existence of the
   future probe through the requested proper time and an actual difference
   of its outcome need a construction.
4. **Regularity and source dependencies.** Prior characteristic well-posedness,
   global structure and event-horizon results are used from the author's
   papers[1]–[4], especially the 1987 *A mathematical theory of gravitational
   collapse*. Those proofs were not audited here. A well-posed scalar model
   does not by itself certify maximal-development matching in our sense.
5. **No novelty inflation.** Black holes with locally flat precursor regions
   are not a new physical phenomenon. This corollary could improve the
   side-test's matter model, while a novel theorem would need a stronger
   completion/control/classification statement and a priority audit.

## Verdict

The supplied paper is the correct scalar-collapse source. It supplies an
exact concentration criterion and quantitative causal structure supporting
a possible flat-observer collapse baseline. It does NOT, by itself, close
the full-past/maximal-development or prescribed future-observable gates.
