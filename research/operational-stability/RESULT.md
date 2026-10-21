# Finite-observable instability behind scalar history non-extension

Status: coordinator derivation, 21 October 2026. Standard functional-analysis
consequences and an application; no novelty claim. Exact finite checks accompany
this note. Independent review remains required.

## Setting

Let T be a rooted, finitely branching tree with no dead ends and let X be its
infinite-path space, with the cylinder topology. X is compact and metrizable.
Let P_n be the finite partition by length-n prefixes. Assign complex weights
 a_n(C) to its cells, compatible under refinement, with total mass 1.
Let V_n = sum_{C in P_n}|a_n(C)|. Then V_n is nondecreasing.
The cylinder algebra A is the union of the finite partition algebras. Its
simple functions S define L(f)=sum_C f(C)a_n(C), independently of refinement.
S is uniformly dense in C(X): compactness and uniform continuity give a
single finite prefix length approximating each continuous f uniformly.

## Theorem 1: extension and uniform response stability coincide

The following are equivalent:

1. sup_n V_n is finite.
2. There is a finite K such that |L(f)| <= K ||f||_infinity for every f in S.
3. Whenever f_j in S tends uniformly to zero, L(f_j) tends to zero.
4. L has a unique bounded linear extension to C(X).
5. A finite countably additive regular complex Borel measure on X matches
   every prescribed cylinder weight.

Moreover ||L|| = sup_n V_n, equal to the representing measure's total variation.

Proof. At level n, triangle inequality gives |L(f)| <= V_n ||f||.
Choose h_n(C)=conjugate(a_n(C))/|a_n(C)| for a_n(C) nonzero (zero otherwise).
Then ||h_n||=1 and L(h_n)=V_n. This proves the norm assertion and 1 iff 2.
If V_n is unbounded, choose a subsequence V_{n_j}->infinity and set
f_j=h_{n_j}/V_{n_j}. Then ||f_j||=1/V_{n_j}->0 but L(f_j)=1.
This proves 3 implies 1; the converse is immediate. Density gives 2 iff 4.
The standard complex Riesz representation theorem gives 4 implies 5, including
regularity and norm equality. A finite complex measure has finite variation,
so 5 implies 2. Uniqueness follows from density (or agreement on cylinders).
The new derivation here is the explicit finite witness, not a new representation
or extension theorem.

## Quantitative approximation: finite agreement has a cost

On P_n let b_C be any alternative weights with sum |b_C| <= M. Define
E_n(a,b)=sup_{|f(C)|<=1}|sum_C f(C)(a_C-b_C)|.
Phase alignment shows E_n(a,b)=sum_C |a_C-b_C|, and triangle inequality yields

    E_n(a,b) >= max(0,V_n-M).

This bound is sharp without a normalization constraint: if M<V_n use b=(M/V_n)a;
if M>=V_n use b=a. For normalized alternatives it remains a lower bound;
the displayed optimizer generally has the wrong total mass, so sharpness is
not asserted there. The same lower bound applies to any completed measure of
variation at most M when restricted to P_n.

Consequently, if an experimental argument really requires *all* cylinder
controls bounded by one to have response error <= epsilon, its variation
budget must satisfy M >= V_n-epsilon. Unbounded V_n prevents a fixed finite
budget from achieving that requirement at every resolution.

A related calibration bound is precise: for any nonempty class F of allowed
controls at a fixed partition, define d_F(a,b)=sup_{f in F}|sum f(a-b)|.
Shrinking F can remove the obstruction. Divergence of V_n alone says nothing
about d_F unless F contains sufficiently rich phase-aligning controls.

## Exact example: complex binary histories

For a binary tree take p=(1+i)/2 and q=(1-i)/2. A length-n word with k ones has
weight a_w=p^k q^(n-k). Consistency follows from p+q=1. All words have
|a_w|=2^(-n/2), giving V_n=2^(n/2).
Take f_n(w)=conjugate(a_w). Then

    ||f_n||_infinity=2^(-n/2),       L(f_n)=sum_w |a_w|^2=1.

Thus finite, uniformly vanishing functions have a fixed nonzero response.
At n=20, ||f_n||=1/1024 while the response remains exactly 1.
`check.py` verifies the mass, response and squared norms with exact fractions
at n=1,2,4,8,12,20. This is a binary complex process, not a computation of
causal-set percolation.

## Theorem 2: a single finite event can witness divergence

Let B_n=max_{E in algebra(P_n)} |a_n(E)|. Then

    V_n / pi <= B_n <= V_n.

Proof. For theta in [0,2pi], choose E_theta as the union of precisely those
cells with Re(exp(-i theta)a_C)>0. Then
Re(exp(-i theta)a_n(E_theta))=sum_C max(0,Re(exp(-i theta)a_C)).
Averaging over theta gives V_n/pi because the positive part of cosine
integrates to 2. Therefore some theta has |a_n(E_theta)|>=V_n/pi.
The upper bound is triangle inequality. Only finitely many distinct E_theta
occur, so the maximum is an actual finite union of cells.

Hence unbounded variation implies unbounded amplitudes on individual cylinder
unions, not merely on finely programmed complex controls. Select events E_j
with |a(E_j)|->infinity and define real nonnegative functions
f_j=1_{E_j}/|a(E_j)|. Then ||f_j||->0 while |L(f_j)|=1.
This does not require programmable complex-valued coefficients. It still
requires that the selected event unions and their increasingly fine resolution
be physically accessible; the functional remains an amplitude response.

For the binary example at even n, all phases lie in {1,i,-1,-i}. If P,N,I,J
are the total magnitudes on those four rays, then P-N=1 and I-J=0. The event
selecting positive-real and positive-imaginary cells has amplitude P+iI.
This gives an explicit Boolean-event instability witness with rational weights.
The checks below enumerate all 16 unions of these four ray classes and find
the largest amplitude exactly. Other subsets cannot do better: an extremal
projection includes every cell on each positive-projection ray, so a maximizer
is one of these ray-class unions.

## A continuity trap: compact-cylinder tests can be vacuous

If E_j is a decreasing sequence of clopen sets with empty intersection,
compactness implies E_j is empty for some finite j. Hence any finitely additive
complex charge on A, even one with unbounded variation, satisfies continuity
from above at the empty set when tested only inside A.

Likewise, if disjoint A_j in A have union A_0 in A, they form an open cover of
the compact set A_0. A finite subcover exists; disjointness forces all remaining
sets to be empty. Thus every finitely additive charge on A is countably
additive on A in this limited sense. Neither property supplies bounded variation
or a Borel extension. The binary example proves this directly.

This agrees with Surya–Zalel Appendix B's discussion of trivial countable
additivity on the cylinder algebra. It is not a counterexample to their
Theorem 2.1, which requires bounded variation for extension.

## Application to the project's smaller event domain

The full finite-level theorem applies to the labelled growth path space.
For the doubly-principal cylinder subalgebra it is cleaner to use its Stone
space, rather than silently identify all its points with labelled histories.
Its bounded linear functionals have the analogous representation on that
space. Equivalently, for the instability witness alone no compactification is
needed: take disjoint prescribed DP cylinders E_i, put
V=sum_i |A(E_i)|, and define h=sum_i conjugate(A(E_i))/|A(E_i)| 1_{E_i}.
Then ||h||<=1 and L(h)=V. The selected theorem's unbounded finite DP sums
therefore give f=h/V with sup norm tending to zero and L(f)=1 directly.
This argument assumes the matching scalar charge/functional exists on the
finite generated algebra. If its assignments are already inconsistent there,
no extension discussion is needed.

The project's bound V_{k+2} >= |p| (|p|+|1-p|)^k c_s can also be inserted into
the approximation inequality. For a fixed variation budget M and error target
epsilon, matching all such controls must fail once that lower bound exceeds
M+epsilon. This is conditional on that bound's audited assumptions, including
the labelled event domain and exact complex amplitudes.

## Physical interpretation and its strongest objection

A possible bridge is uniform calibration stability: shrinking the uniform
magnitude of any allowed control shrinks its linear amplitude response, across
all finite resolutions. With unrestricted cylinder controls, Theorem 1 makes
this bridge equivalent to bounded variation and completed-measure extension.
This exposes the substantive assumption behind one completion demand.

But complex amplitudes are not outcome probabilities, and arbitrary h_n may
require phase-sensitive control over an enormous number of histories. Neither
causal-set covariance nor an embedded observer model has supplied those
controls. Squaring amplitudes does not itself provide an implementation.
A restricted operational space, a different topology or changed off-diagonal
quantum data can evade this stability demand. Completed-history and growing
interpretations that impose the same functional and control class inherit
the same issue. No ontology is selected.

## Prior work and verdict

Primary text inspected: Surya–Zalel, arXiv:2003.11311v1, Theorem 2.1, Eqs.
(17)–(21), Appendix B; Dowker–Johnston–Surya, arXiv:1007.2725v1, Claims 1–2
and the surrounding bounded-variation necessity argument. Both already place
bounded variation at the centre of extension. The Riesz representation step is
standard mathematics; its original proofs were not newly audited here.

Verdict: KNOWN MATHEMATICS / EXPLICIT STABILITY COROLLARY. The useful question
left for physics is which finite controls are realizable and what norm gives
meaningful approximation error. A model of accessible phase controls would
be required for a stronger physical result. Global novelty was not searched
exhaustively and is not claimed.
