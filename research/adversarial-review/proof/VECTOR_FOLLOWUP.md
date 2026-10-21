# Independent audit of the provisional norm-only vector boundaries

Date: 2026-10-21. I independently checked the arguments in
`research/adversarial-review/coordinator/HILBERT_NORM_BOUNDARY.md` and
`BANACH_NORM_BOUNDARY.md`. I edited only this follow-up. I did not run their
finite-check scripts, alter builders or source results, or make a novelty claim.

## Verdict

I found no mathematical counterexample to either provisional existence domain
under the stated norm-only prescriptions and the ordinary labelled CTP history
space. The Hilbert boundary `|p|²+|1-p|² ≤ 1` survives, for both the DP-only and
all-cylinder prescriptions. The Banach `c0` domains also survive: DP-only gives
`p=1` or `|p|<1, |1-p|≤1`; prescribing every cylinder gives `{0,1}` or
`|p|<1, |1-p|<1`.

These results are existence classifications in a space allowed to depend on
`p`, with cylinder norms prescribed but phases discarded. They do not classify
phase-preserving complex measures or physically specified dynamics. The
arguments use familiar probability/vector-measure constructions; I make no
priority assessment here.

## Hilbert construction and necessity

For `p=x+iy`,

`a²+b² = x²+y²+(1-x)²+y² = 1+2(y²-x(1-x))`.

Thus the proposed disk condition is exactly `y²≤x(1-x)`, which implies
`0≤x≤1`. For `0<x<1`, set `q=y²/[x(1-x)]`. The proposed mixture has
`G=x` with probability `1-q`, and `G∈{0,1}` with Bernoulli-`x` probabilities
with probability `q`. Direct calculation gives

`E G=x`, `E G²=x²+y²=a²`, and `E(1-G)²=(1-x)²+y²=b²`.

Independent copies on forward pairs, followed by conditionally independent
edge choices and transitive closure, define a standard probability model. For
the finite induced-order event `C`, every cover edge must be selected and every
incomparable pair must be absent; any edge between a comparable pair is allowed,
because covers already generate all comparable pairs by transitivity. Conditional
on the environment its probability is therefore the cover/incomparability
product in the proposal. Independence of the environment coordinates gives the
claimed second moment. The formula holds for every labelled finite order, so
restriction to the DP sigma-algebra is valid.

For the vector measure, conditional expectation is a contraction
`L²(joint histories) → L²(environment)`. For disjoint `E_j`, the norm of the
remainder after `N` terms is at most the square root of the joint probability
of the tail union, which tends to zero. This proves norm-countable additivity,
not just finite additivity. The empty history has conditional probability one,
so total mass has norm one. For any finite disjoint family and coefficients of
modulus at most one, the conditional expectation of the corresponding simple
function has pointwise modulus at most one; hence semivariation is at most one,
and the whole space attains one. The construction also works on the circle
boundary, where the environment is Bernoulli and conditioning fixes each edge.

For necessity, norm-countable additivity implies bounded range by applying
uniform boundedness to evaluation maps on the Hilbert dual (the Banach-boundary
report supplies the argument). For any finite disjoint family, averaging over
independent signs yields

`Σ ||μ(E_j)||² = E ||Σ ε_j μ(E_j)||² ≤ 4 M²`,

where `M=sup_E ||μ(E)||`; every signed sum is the difference of values on two
unions. This Hilbert identity remains valid for complex Hilbert spaces using
real signs. If `t=a²+b²>1`, the disjoint DP level has squared-norm sum at least

`a² t^k ∏_(j=1)^k (1-(b²/t)^j)`.

Here `a,b>0`, the infinite product has positive limit, and `t^k` diverges.
This contradicts the uniform bound. The two-cap count and probability product
are the same as the scalar proof, applied to positive weights `a²,b²`; the
normalization `a²+b²=1` is not needed for that product argument. This excludes
the exterior on DP cylinders alone, hence also when all cylinders are
prescribed. Endpoint measures at `p=0,1` are consistent with the claimed disk.

I found no hidden issue from redundant edges: their unconstrained choices sum
out conditionally, leaving exactly cover and incomparable factors. Nor does
conditioning require choosing simultaneous pointwise versions for all events;
the measure is defined by equivalence classes in `L²`.

## Banach construction and boundary exclusions

For the DP `c0` construction, in the nonendpoint candidate region choose
`r∈(0,1)` with `r≤a` and `1-r≤b`. This interval is nonempty because
`a+b≥1`; when `b=1`, choose any positive `r≤a`. Under real CTP probability
`P_r`, every finite cylinder has positive mass. For each DP cylinder `C`, the
coordinate measure `w_C P_r(·|C)` is countably additive, and its weight
`w_C=a^L b^h` tends uniformly to zero with rank: a naturally labelled
principal order of size `n` has at least `n-1` covers and `a<1`. There are only
finitely many coordinates at each rank. Thus the vector lies in `c0`, and for
disjoint tails its finitely many large-weight coordinates tend to zero while
all remaining coordinates are uniformly small. This proves norm-countable
additivity directly.

For a target cylinder `D`, each coordinate cylinder `C` is disjoint from `D` or
nested with it. If `C⊆D` as events, the `C` coordinate of `μ(D)` is `w_C`, and
the extension order has no fewer covers or incomparable pairs than the shorter
order defining `D`; since `a,b≤1`, `w_C≤w_D`. If `D⊆C`, the `C` coordinate is
`w_C P_r(D)/P_r(C)`. Natural-label extension preserves old covers and
incomparabilities, so the ratio is
`r^(L(D)-L(C))(1-r)^(h(D)-h(C))`; the choices of `r` bound this coordinate by
`w_D`. Disjoint coordinates vanish, and the `D` coordinate attains `w_D`.
The separate `Ω` coordinate is bounded by the same probability comparison.
Therefore the prescribed norm is exact. This also resolves a wording ambiguity
in the candidate note: in its `C⊆D` case, the value `w_C` is the coordinate
indexed by `C`, not by `D`.

The c0 semivariation bound is sound coordinatewise: disjointness and
`|α_j|≤1` make each conditional-probability sum at most one in modulus, so its
weighted coordinate is at most `w_C≤1`; the `Ω` coordinate also is at most one.
The whole-space value attains one. Infinite total variation at nonclassical
parameters follows from the previously audited divergent DP level sums; this
does not conflict with finite semivariation in `c0`.

The proposed necessary exclusions check out:

- `a>1` gives unbounded norms on nested chain cylinders; this contradicts
  bounded range (or continuity from above).
- `b>1` gives unbounded norms on antichain-plus-two-cap DP cylinders, since
  their incomparable-pair exponent grows quadratically while the cover factor
  is only exponential.
- If `a=1` and `p≠1`, the cylinders for
  `chain_n ⊕ A₂ ⊕ {u} ⊕ {v}` are DP, pairwise disjoint, and have constant
  positive norm `b`. A disjoint countable series in a norm-countably additive
  measure must have terms tending to zero. The relation first distinguishing
  two such cylinders occurs at different birth indices, so they really are
  disjoint.

These leave exactly `a<1,b≤1`, plus `p=1`; `p=0` is included by its scalar
endpoint measure. The conditions on `r` then give the DP sufficiency throughout.

For the all-cylinder variant, the additional `b=1, p≠0` exclusion also holds:
let `F_n` have an antichain on the first `n` births and one new vertex with
exactly one parent among them. `F_n` and `F_m` for `m>n` disagree on the first
`n+1` vertices (the former has a relation there; the latter's first `m` are an
antichain), hence are disjoint, while each prescribed norm is `a>0`. This
violates countable additivity. The endpoint `p=0` is separate and valid.

For strict `a,b<1`, the `L^α(P_r)` construction is correct: continuity and
strict monotonicity of `a^α+b^α` give a finite `α≥1` with sum one, and the
indicator measure has cylinder norm exactly `a^L b^h`. Tail-union probability
proves norm-countable additivity. The alternative all-cylinder `c0` construction
also has weights vanishing uniformly: each added natural birth contributes a
cover if it has an ancestor, otherwise an incomparable pair, so `L+h≥n-1`.

## Strongest attempted falsifiers and limits

I tried to break the boundary families by checking the actual finite-prefix
events, not just their named orders; each pair is disjoint for the stated
first-difference reason. I checked endpoint zero powers separately, the
`b=1` choices of `r`, the empty/whole-space coordinate, and whether extension
can remove a cover; natural labelling prevents a later vertex from inserting
between two earlier comparable elements. I found no counterexample.

The one correction is editorial precision in `BANACH_NORM_BOUNDARY.md` around
lines 84–90: say explicitly that when `C⊆D`, the coordinate indexed by `C`
equals `w_C`. The inequalities and construction are otherwise sound as written.
The proofs classify only the stated norm prescriptions and depend on ordinary
CTP probability measures and standard conditional expectation. No literature
priority search was performed in this follow-up, and no formal proof kernel was
run.
