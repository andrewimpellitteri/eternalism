# Matched cylinder magnitudes with different intrinsic completed values

22 October 2026. Explicit example in the **nonzero, locally isomorphism-invariant,
scalar ratio-BC / MSR / norm-only cylinder-covariance** class. The construction
and all-stage proof below use known factorization and extension tools; see
`PRIOR_WORK.md`. Independent review is recorded separately. This is not a
claim about general operator QBC, full vector covariance, or detector probabilities.

## Statement

There exist two normalized finite complex measures nu_A, nu_B on the sigma
algebra of infinite naturally labelled causal-set growth histories such that:

1. Every transition is nonzero and obeys scalar ratio Bell causality (BC) and
   the amplitude Markov sum rule (MSR).
2. Within each model, the magnitude of a finite cylinder amplitude is
   independent of its natural labeling. Across the pair, the magnitudes of
   **every individual finite labelled cylinder**, at every depth, agree.
3. For the same measurable completed event E2 = “exactly two minimal elements”,
   intrinsic under order isomorphism, their rank-one quantum measures obey

       mu_B(E2) - mu_A(E2) >= 3964839/104755225
                          > 18899/500000 > 0.

Here D_j(E,F)=conjugate(nu_j(E))nu_j(F) and mu_j(E)=|nu_j(E)|^2. The additive
object is nu_j; mu_j is nonadditive. The measures are concentrated on histories
with finitely many non-timid births. Agreement on individual cylinders does
not imply agreement on their unions. A finite union already distinguishes
these models; the effect does not first appear at infinity.

## 1. Factorization and exact two-phase seed

For a finite naturally labelled poset C, count its down-sets P as actual
subsets, including isomorphic duplicates. Induced posets are evaluated without
regard to their inherited labels. Define

    w(empty)=q(empty)=1,
    S_C=sum_(P proper ideal C) w(P),
    f(C)=1/q(C),  w(C)=f(C)-S_C,
    t(C,P)=q(C)w(P).

The empty precursor is gregarious; the full precursor is timid (a new universal
top). MSR follows from q(C)[S_C+w(C)]=1. If B=P union Q, the scalar BC identity is

    t(C,P)t(B,Q)=q(C)q(B)w(P)w(Q)=t(C,Q)t(B,P).

We will prove q,w never vanish, so ordinary ratios are defined. For a finite
N-element C with prefix C_j,

    A(C)=product_(j=0..N-1) q(C_j) * product_(x in C) w(past_C(x)).

Set u=(3+4i)/5. Both models have q(single)=1/2 and q(antichain2)=u/4. On
chain2 take q=v/4, with v=u in A and v=conjugate(u) in B. Thus

    w(single)=1,
    w(chain2)=4/v-2,       w(antichain2)=4/u-3.

All are nonzero. Early |q| agree by cardinality; early |w| agree by induced
shape across the models (the chain weights conjugate). Every early weight has
Gaussian norm b(z)=|Re z|+|Im z| <= B_2=19/5.

The seven stage-three cylinders, written as tuples of predecessor bit masks,
have exact amplitudes:

| C | A(C), using the selected v |
| --- | --- |
| (0,0,0), (0,0,1), (0,0,2) | u/8 each |
| (0,0,3) | 1/2-3u/8 |
| (0,1,0), (0,1,1) | v/8 each |
| (0,1,3) | 1/2-v/4 |

Their sum is 1. Their total Gaussian norm is exactly 2 in either model,
so V_3=sum_C |A(C)| <= 2. The four cylinders with two minima sum to

    a_j=(4+v-u)/8,
    a_A=1/2,   a_B=1/2-i/5,
    |a_B|^2-|a_A|^2=1/25.

For completeness the entire minimum-count polynomial is
G_3(z)=[(4-v)z+(4+v-u)z^2+u z^3]/8. Its coefficient of z depends on v;
the previous one-phase family's 3/8 coefficient cannot be reused here.

These are not globally conjugate dynamics: the antichain phase stays fixed
while the chain phase conjugates. The completed gap below also rules out
identification by a global phase or complex conjugation preserving mu.

## 2. Recursive circle construction for every later parent

For n>=3 choose the same positive rational schedule in both models:

    R_n=1+2^(2n+10) B_(n-1),
    B_n=2 R_n.

Inductively suppose b(w(P))<=B_(n-1) for every smaller P. The B_n increase,
and there are at most 2^n-1 proper ideals, so

    |S_C| <= (2^n-1) B_(n-1) < 2R_n.

If S=S_C is nonzero choose the positive real square root and set

    h=sqrt(R_n^2-|S|^2/4),
    f(C)=S/2 + i(S/|S|)h,
    w(C)=-S/2 + i(S/|S|)h,
    q(C)=1/f(C).

If S=0 take f(C)=w(C)=R_n. For S!=0 the unit vector S/|S| is perpendicular
in the real plane to iS/|S|. Consequently

    f-w=S,    |f|^2=|w|^2=|S|^2/4+h^2=R_n^2.

The strict bound makes the square root well defined. This is an exact
algebraic construction, generally with nested radicals. It is not restricted
to Gaussian rationals. Each step is a deterministic function of S and the
cardinality. Ideal-type multiplicities are isomorphism invariant, so induction
makes f,q,w isomorphism invariant. No label-dependent branch choice or
infinite search is needed. Also b(w)<=2|w|=B_n, closing the induction.

Thus all q,w and every t(C,P) are nonzero at every stage. BC and MSR hold by
Section 1. For n>=3, in both models and for every n-element C,

    |q(C)|=1/R_n,    |w(C)|=R_n.

The path-product formula proves norm covariance within each model: the q
magnitudes depend only on stage, and the past-poset product is intrinsic.
It also proves equality of every cylinder magnitude across models, using
matched early |w| and the common later R_n. This is an all-stage induction,
not an extrapolation from finite enumeration.

## 3. Summable row excess and the timid phase

For any parent C of size n>=3, put e(C)=sum_(P proper C)|t(C,P)|. Then

    e(C) <= (2^n-1) B_(n-1) / R_n < epsilon_n=2^(-n-10),
    sum_(n>=3) epsilon_n = 1/4096.

Although the timid amplitude has modulus exactly 1, its phase need not be
zero. MSR, rather than its modulus alone, supplies the necessary padding bound:

    |t(C,C)-1| = |sum_(P proper C)t(C,P)| <= e(C).

In particular the row variation is 1+e(C), and the looser bound 1+2epsilon_n
suffices below. We do not replace a unit-modulus timid amplitude by 1.

## 4. Direct finite-variation completion

Let X be the infinite labelled-history space. Complete each finite C by
universal tops forever, obtaining h_C. On the countable set H of all such
paths define finite atomic measures

    nu_n = sum_(|C|=n) A(C) delta_(h_C).

Different n-element parents have different h_C. MSR gives nu_n(X)=1 and
V_n=sum_(|C|=n)|A(C)| <= V_3 product_(k=3..n-1)(1+2epsilon_k). Hence

    V_n <= 2 exp(1/2048) <= 4096/2047,

where exp(x)<=1/(1-x) for 0<=x<1. The timid child pads to the same h_C, so

    ||nu_(n+1)-nu_n||_TV
      <= sum_C |A(C)| [|t(C,C)-1|+sum_(P proper C)|t(C,P)|]
      <= 2epsilon_n V_n.

Here TV is the full variation norm (no probability-distance factor of 1/2).
The bound is summable. Completeness of l1(H) gives an absolutely summable
atomic limit nu on X. A singleton h_C is a countable intersection of
cylinders, so the atomic measure is defined on the cylinder sigma algebra.
Every fixed cylinder has its prescribed amplitude under nu_n for all n at
least its depth, by finite MSR. TV convergence preserves those values and
nu(X)=1. This proves countable additivity without a formal infinite path sum.

For either model,

    ||nu-nu_3||_TV <= 2*(4096/2047)*(1/4096)
                   = tau=2/2047 < 1/1000.

The support is eventually timid. This is an engineered completion, with no
assertion of a continuum limit or cosmological realism. `DATA_BOUNDARY.md`
explains why unit-modulus timid transitions force atomicity whenever this
finite complex-measure extension exists; it is not just a proof artifact.

## 5. Same intrinsic completed event, strict gap

Let M_N be the number of minimal elements after N births. Existing pasts never
change. A new element is minimal precisely for empty precursor. Thus M_N is
nondecreasing, and the completed count M is order-isomorphism invariant.

    E2={M=2}=union_N intersection_(K>=N){M_K=2}

is measurable and invariant under natural relabeling of completed causets.
The finite event {M_3=2} is used only to evaluate the padding measure; it is
not itself asserted to be an intrinsic completed event. Adding universal tops
preserves the minima of a nonempty C, so nu_(j,3)(E2)=a_j from Section 1.
TV convergence gives |nu_j(E2)-a_j|<=tau. For any |delta|<=tau,

    ||a+delta|^2-|a|^2| <= 2|a|tau+tau^2.

Using |a_A|=1/2 and |a_B|=sqrt(29)/10<3/5 gives

    mu_B(E2)-mu_A(E2)
      >= 1/25-(11/5)tau-2tau^2
       = 3964839/104755225
       > 18899/500000 > 0.

This is a rigorous infinite-tail inequality, not an infinite-event numerical
evaluation. The same intrinsic event has different diagonal rank-one measure
values even though every individual finite cylinder magnitude agrees.

## 6. Data boundary, evidence and limits

The union of cylinders (0,1,0) and (0,0,1) already has mu_A=1/16 and
mu_B=9/400. These two are natural labelings of the same three-element shape.
All single-cylinder magnitudes match, but coherent finite-union data do not.
`DATA_BOUNDARY.md` proves that matching all finite-union quantum measures
would force equality on every completed measurable event for finite complex
measures. In fact individual cylinders plus pair unions at every depth suffice.

`check.py` independently enumerates all transitive triangular masks through
five births (1,1,2,7,40,357). It uses exact fractions for the seed and norm
factors, and outward-rounded 256-bit dyadic intervals for later radicals.
It checks circle enclosures, isomorphism consistency, nonzero transitions,
MSR/BC residual enclosures, escape/padding bounds, early event sums and the
global rational gap bound. An interval residual containing zero is a bounded
consistency check, not an equality proof; the analytic identities above supply
the exact and all-stage claims. No floating-point equality or Gaussian-rational
claim is used for later coordinates.

Norm-only GC is weaker than equality of complex amplitudes or of the full
decoherence functional under labeling changes. Scalar ratio BC is weaker in
scope than an operator QBC framework. Restricting to an intrinsic event does
not establish that the whole model has full vector covariance. No readout
instrument is provided, so this does not establish empirical distinguishability
or any conclusion about temporal ontology, passage, determinism, or a physical
arrow of time. Priority for this exact example is not established.
