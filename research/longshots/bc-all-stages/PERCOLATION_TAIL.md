# A non-atomic variant: keep a real-percolation reference tail

Coordinator strengthening, 22 October 2026. Same weak norm covariance,
scalar ratio BC, local finite-isomorphism invariance and seed as RESULT.md.
This variant removes that construction's eventual-timid support. Independent
review in PERCOLATION_REVIEW.md confirms the stated proof; no novelty claim.

## 1. Fixed late gregarious values and an exact weight formula

Keep q(empty)=1, q(singleton)=1/2, q(chain2)=1/4,
q(antichain2)=(3+4i)/20. For |C|=n>=3 instead set q(C)=delta^n,
delta=1/10, and retain

    w(C)=1/q(C)-sum_(P proper ideal C) w(P),
    t(C,P)=q(C)w(P).

The factorization and path-product proofs of MSR, scalar BC and norm-only
covariance apply verbatim. Nonvanishing and scalar completion need new checks.

Write f(C)=1/q(C). Möbius inversion on the down-set lattice of a finite C gives

    w(C)=sum_(S subset Max(C)) (-1)^|S| f(C\S).

One can prove the formula directly by interchanging the two finite sums in
sum_(P ideal C) w(P). All terms cancel except f(C): for a proper ideal J,
P=J union S with J=P\S and S subset Max(P) is possible exactly when S is a
subset of the minimal elements of C\J; their alternating subset sum is zero.
For J=C it is one. Thus the expression solves the defining recursion uniquely.
The formula uses actual subsets of maxima, not distinct induced isomorphism types.

Use as reference f0(C)=delta^(-|C|). Its inverse is

    w0(C)=delta^(-n)(1-delta)^m,    m=|Max(C)|,

since deleting a subset of maximal elements reduces cardinality by its size.
The corresponding transitions are ordinary real transitive percolation

    t0(C,P)=(1-delta)^|Max(P)| delta^(n-|P|).

This is a prior-work model, not our new dynamics. Its row sums are one and its
cylinder probabilities define a probability measure P0 on labelled histories.
Reference: Rideout–Sorkin gr-qc/9904062v3, Section2 and Section4.2 Eq.(6).

## 2. Finite early perturbations cannot force a later zero

The difference d=f-f0 vanishes outside sizes one and two (and is zero at the
empty poset). Its Gaussian norms are

    b(d(singleton))=8,
    b(d(chain2))=96,
    b(d(antichain2))=504/5.

In the Möbius expression for w(C)-w0(C), only terms leaving one or two elements
can contribute. There are at most n and binomial(n,2) such choices, respectively.
For every n>=1,

    b(w(C)-w0(C)) <= 8n+(504/5)binomial(n,2) <= 51n^2.

Since m<=n, w0(C)>=9^n. For n>=3, 9^n>51n^2: check n=3, then the ratio of
successive left/right sides increases by 9(n/(n+1))^2>1. Hence

    |w(C)| >= w0(C)-|w(C)-w0(C)| > 0.

The seed weights at sizes zero, one and two are nonzero already. This proves
that every transition of this variant also is nonzero at every stage.

## 3. Summable row distance gives an explicit L1 completion

For a parent of size n>=3, q(C)=delta^n agrees with the reference. Therefore

    sum_(P ideal C) |t(C,P)-t0(C,P)|
        <= delta^n 2^n 51n^2 = zeta_n,
    zeta_n=51n^2/5^n,       sum_(n>=3) zeta_n=4437/800 < infinity.

The crude bound suffices; it is not a sharp variation estimate. Because the
reference transitions are nonnegative and sum to one,

    sum_P |t(C,P)| <= 1+zeta_n,
    V_n <= V_3 product_(k=3..n-1)(1+zeta_k) <= V_3 exp(4437/800).

This falls under the known summable row-excess criterion of Surya–Zalel,
2003.11311v1, Section3.1 Theorem3.1/Claim3.2. The explicit next construction
also supplies a completion without claiming that criterion is new.

Every reference cylinder has positive P0 measure. Define

    nu_n = sum_(|C|=n) A(C) P0(. | cyl(C)).

Equivalently its density is g_n(x)=A(C_n(x))/P0(cyl(C_n(x))). At each fixed
level the cylinders are disjoint, so ||nu_n||_TV=V_n. Conditional on a parent C,
nu_n uses reference transitions t0, while nu_(n+1) uses t then resumes reference
transitions. Consequently

    ||nu_(n+1)-nu_n||_TV
      = sum_C |A(C)| sum_P |t(C,P)-t0(C,P)| <= V_n zeta_n.

These bounds are summable. The densities g_n converge in L1(P0) to g; define
nu(E)=integral_E g dP0. It is a finite countably additive complex measure,
nu(X)=1, and iterated MSR ensures its value on every finite cylinder is A(C).
Moreover |nu| is absolutely continuous with respect to P0. The inherited
nontrivial phase on cp and its universal-top continuations is unchanged.

## 4. This completion has no eventually-timid concentration

For a nonempty parent, every reference transition is <=9/10. A full precursor
has probability (9/10)^m<=9/10 because m>=1. A proper precursor has at least
one missing element and probability <=1/10. Thus all single infinite labelled
paths have P0 measure zero. In particular the countable set of eventually
all-timid labelled histories has P0 measure zero and hence |nu| measure zero.

This contrasts with the explicit atomic construction in RESULT.md. Both have
nonzero finite transitions, norm-covariant cylinders and the same early phase;
only the former is concentrated on timid completions. For the present variant,
nonzero late escapes are not merely a formal finite support issue. No claim is
made about a physically realistic, manifold-like or continuum limit. Absolute
continuity supplies a mathematical null-set comparison, not an identification
of complex amplitudes with ordinary probabilities or Born weights.

## Scope

Full vector covariance still fails at the seed; the same applies to a
label-by-label equality of the rank-one decoherence functional. This is not an
extension of the complex-percolation one-parameter law: the early q's depend
on shape and phase, rather than the reference's cardinality-only values.
The reference is used for completion, not substituted for the seed dynamics.
No noncommutative/operator QBC or empirical/ontological claim follows.
