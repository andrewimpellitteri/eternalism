# Independent analytic review: all-stage scalar continuation

## Verdict

I find no fatal flaw in the proposed all-stage construction under its stated
assumptions: nonzero scalar transitions, scalar ratio Bell causality, MSR,
and norm-only covariance of finite labelled cylinders. The recursion, the
all-stage norm argument, and the timid-padding total-variation estimate are
valid. The result should remain explicitly limited to a labelled scalar
complex measure and norm covariance. It proves neither full vector nor
decoherence-functional covariance, nor an operator/noncommutative QBC claim.

## Recursion, ideal multiplicities, and phase seed

Write `b(z)=|Re z|+|Im z|`, so `|z|<=b(z)` and `b` is subadditive. The
initial values follow directly from the recursion:

* `w(empty)=1` and `w(single)=2-1=1`;
* for the two-chain, the proper-ideal sum is `1+1=2`, giving `w=4-2=2`;
* for the two-antichain, the proper-ideal sum is `1+1+1=3`. The two
  singleton ideals are distinct subsets and both count, so
  `w=20/(3+4i)-3=(-3-16i)/5`.

Multiplying by `q` gives the stated transitions, including the two-antichain
full transition `(3+4i)(-3-16i)/100=(11-12i)/20`. Thus the prescribed
recursion recovers the fixed seed through the two-element parents. In the
three-element `cp` class the three natural labelings have amplitudes
`(3+4i)/40`, `(3+4i)/40`, and `1/8`: the first two extend an antichain
parent through one of its two distinct singleton ideals, and the third
extends the chain parent through its empty ideal. The first two terms are
equal because the singleton ideals have the same induced type, but they must
still be counted twice in ideal sums and in event sums. The common modulus is
`1/8`, and the real-to-complex ratio is `(3-4i)/5`.

This verifies the claimed past/ideal multiplicities and confirms that the
later common `q_3` rescales all transitions out of three-element parents; it
does not alter these three seed amplitudes.

## Nonzero and tail bounds

For an `n`-element parent, let `S_C` be the sum over its proper down-sets.
Inductively `b(w(P))<=B_(n-1)` for every proper ideal type, and there are at
most `2^n-1` actual proper ideals, counted with multiplicity. Therefore

\[
b(S_C)\le (2^n-1)B_{n-1},\quad
|w(C)|\ge 1+(4^n-2^n+1)B_{n-1}>0,
\]

and

\[
b(w(C))\le 1+(4^n+2^n-1)B_{n-1}\le B_n.
\]

These estimates use the fact that `q_n` is the positive real reciprocal of
`1+4^n B_(n-1)`. They prove inductively that every `w(C)` and hence every
transition `q(C)w(P)` is nonzero. The same multiplicity bound yields

\[
e(C):=\sum_{P\subsetneq C}|t(C,P)|
\le \frac{(2^n-1)B_{n-1}}{1+4^nB_{n-1}}<2^{-n}.
\]

MSR follows from the defining recursion because the full ideal contributes
`q(C)w(C)=1-q(C)S_C`. There is no division by a transition in the proof
except when defining `q` or deriving a ratio, and both are nonzero by the
construction. The cross-multiplied BC equation is exactly
`q(C)q(B)w(P)w(Q)` on either side: `P,Q` are down-sets of `B=P union Q`,
and the induced types (including their multiplicities as selected subsets)
are unchanged. Since all factors are nonzero, the ratio form is also defined.

The displayed early values and bounds check exactly: `B_2=19/5`,
`B_3=1373/5`, `q_3=5/1221`, and `q_4=5/351493`.

## Norm covariance and persistence

Multiplying the transition factors along a natural labeling gives

\[
A(C)=\left(\prod_{j=0}^{N-1}q(C_j)\right)
      \left(\prod_{x\in C}w(\operatorname{past}_C(x))\right).
\]

The modulus of the first product depends only on prefix sizes: the empty and
one-element values are fixed, both two-element `q` values have modulus
`1/4`, and all later `q_n` are common at a given size. An order isomorphism
maps each element's induced past to an isomorphic induced past. Thus the
second product, with one factor for every element (so repeated past types
remain repeated), is invariant under relabeling. This proves finite
norm-GC at every stage, while allowing a phase difference in the amplitude.

The additional necessity proposition in the coordinator's Section 1 is also
valid in the stated restricted class. Assume every transition is nonzero,
`t(C,P)` is invariant under isomorphisms of the parent/precursor pair, BC is
the scalar ratio (equivalently cross-product) spectator condition, and
norm-GC holds at every finite stage. First, taking the BC pair `empty,P` at
parent `C` gives

\[
t(C,P)=q(C)w(P),\qquad q(C)=t(C,empty),\quad
w(P)=t(P,P)/q(P),
\]

with `w(empty)=1`. MSR then gives
`w(C)=1/q(C)-sum_(P proper ideal of C)w(P)`. Local isomorphism invariance
makes these functions of the respective unlabelled types. This is a
necessity statement for this parametrization, not just a convenient ansatz.

For the modulus claim, fix an `n`-element `B`, a down-set `P`, and form
`C=B+e` with new maximal `e` and past `P`. Compare two growth orders for
`C` plus an isolated point `f`: (i) add `e` with past `P`, then add isolated
`f`; (ii) add isolated `f`, then add `e` with the same past `P`. These are
natural labelings of the same `(n+2)`-element poset. With `a=t(B,P)` their
amplitudes are

\[
A(B)a q(C),\qquad A(B)q(B)t(B+f,P).
\]

BC at parent `B+f` for precursors `empty,P` gives
`t(B+f,P)=q(B+f)a/q(B)`. All factors being nonzero, norm-GC and cancellation
therefore imply `|q(C)|=|q(B+f)|`. If `P` is nonempty, the number of
relations in `C` exceeds that in `B+f` by exactly `|P|`: deleting a maximal
element with nonempty past and replacing it by an isolated element strictly
reduces the relation count while preserving cardinality. Repeating reaches
the antichain, so `|q|` is constant on every fixed-cardinality isomorphism
class. The case `P=empty` is simply the same type and adds no step.

Conversely, the path-product argument above shows that cardinality-only
`|q|` is sufficient within this factorized, locally isomorphism-invariant
class. Thus the necessity/sufficiency proposition is sound with the
all-stage norm-GC and nonzero assumptions; it does not establish phase
invariance of `q`, full vector covariance, or necessity outside this class.

For `cp`, the three seed amplitudes above have relative phase
`1,1,(3-4i)/5`. A universal-top continuation has the same parent isomorphism
type and the same transition factor for each of the three labelings at every
added stage. The ratio therefore persists. This statement concerns those
natural labelings of `cp` followed by universal tops; it is not a claim that
the amplitudes become label invariant.

## Atomic completion and coincident supports

The potential support collision is handled correctly. At a fixed depth `n`,
the map `C -> h_C` is injective because the first `n` labels recover `C`.
Across depths it is not injective: if `D` is obtained by a timid birth from
`C`, then `h_D=h_C`. This is the only collision relevant when comparing
`nu_n` and `nu_(n+1)`. On that common atom, the coefficient changes from
`A(C)` to `A(C)t(C,C)`. All non-timid children give different depth-`n+1`
prefixes and hence different atoms. If
`s_C=sum_(P proper) t(C,P)`, MSR gives `t(C,C)-1=-s_C`, so the total
variation contribution from the parent is bounded by

\[
|A(C)|\left(|t(C,C)-1|+\sum_{P\subsetneq C}|t(C,P)|\right)
\le 2|A(C)|e(C).
\]

Summing gives the claimed `2 epsilon_n V_n` estimate. Even if one describes
the support comparison without enumerating collisions, the triangle
inequality gives the same upper bound; it is important that the timid atom
not be treated as a fresh disjoint atom with coefficient `A(C)t(C,C)`.

The row bound
`sum_P |t(C,P)| <= |1-s_C|+e(C) <= 1+2 epsilon_n` implies
`V_(n+1)<=V_n(1+2epsilon_n)`. Since
`sum_(n>=3)epsilon_n=1/4`, `V_n<=V_3 exp(1/2)`, and
`sum_n 2epsilon_n V_n<infinity`. Thus `nu_n` is Cauchy in the `l1` space
over the countable set `H={h_C}`. The limit is an absolutely summable atomic
complex measure. For a fixed depth-`m` cylinder `C`, every `nu_n` with
`n>=m` assigns it the sum of amplitudes of its depth-`n` extensions; iterated
MSR makes that sum exactly `A(C)`. Total-variation convergence preserves
this value, and also the total mass `1`.

The checker corroborates the finite parts through five births: 407 nonzero
transitions, 1619 cross-multiplied BC equations, norm-GC through stage five,
and the exact product formula. The checker is finite corroboration; the
inductive bounds and `l1` argument, not the enumeration, establish the
all-stage statements. I independently recomputed the seed weights,
`q_3`, `q_4`, and phase ratio with exact rational complex pairs.

## Precise scope limits

The limit measure is on the labelled cylinder sigma algebra and is supported
on the countable family of histories that become all-timid after some finite
prefix. This explicit concentration is part of the construction. The
argument does not establish an extension on an unlabeled quotient, full
relabeling invariance of `A(C)`, full covariance of
`D(E,F)=\overline{nu(E)}nu(F)`, or physical admissibility. It also gives no
robustness result for other late-stage rates or for noncommuting/operator
Bell-causality constraints. These are necessary scope restrictions, not
counterexamples to the proposed scalar theorem.

The cited prior sources and any priority question were not re-audited in this
bounded proof review. No novelty claim is made.
