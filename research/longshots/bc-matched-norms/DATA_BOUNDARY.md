# Two boundaries: richer data restore rigidity; unit timid modulus forces atoms

22 October 2026. Elementary consequences of finite-variation scalar measures,
stated to prevent overreading the example. No novelty claim for either lemma.

## Finite-union data determine the completed diagonal quantum measure

Let nu_A,nu_B be finite complex measures on sigma(G), where G is the algebra
of finite unions of cylinders. Put mu_j(E)=|nu_j(E)|^2. If mu_A=mu_B on G,
then mu_A(E)=mu_B(E) for every E in sigma(G).

Proof: lambda=|nu_A|+|nu_B| is a finite positive measure. Every E in sigma(G)
can be approximated by G-sets E_k with lambda(E symmetric-difference E_k)->0.
Indeed the class of approximable sets contains G, is closed under complement,
and is closed under countable unions: truncate the increasing finite unions
using finiteness of lambda, then approximate their finitely many constituents.
It therefore contains sigma(G). For either j,

    |nu_j(E)-nu_j(E_k)| <= lambda(E symmetric-difference E_k) -> 0.

Taking squared magnitudes and using equality on each E_k proves the claim.
This argument uses finite-variation continuity, not additivity of mu.

Moreover, agreement on single cylinders and every union of **two distinct
same-depth cylinders**, at every depth, already implies agreement on G. On
any common-depth finite disjoint partition, write a_i=nu(C_i). Then

    |sum_(i in I)a_i|^2
       = sum_(i in I)|a_i|^2
         + sum_(i<j in I)(|a_i+a_j|^2-|a_i|^2-|a_j|^2).

Every finite cylinder union refines to such a partition. Thus any completed
diagonal discrepancy between finite complex measures must already violate
some finite-depth single or pair-union value. The present pair violates a
pair-union value at depth three. Its intrinsic completed E2 gap survives the
tail; it is not a phase effect inaccessible to all finite coherent event data.
For normalized scalar measures, the remaining ambiguity can be identified
exactly: equality on all events forces nu_B=nu_A or nu_B=conjugate(nu_A).
For arbitrary measurable E,F, decompose them into the three disjoint pieces
E\F, F\E, and E intersect F. Expanding squares gives

    Re[conjugate(nu(E))nu(F)]
       = [mu(E union F)+mu(E intersect F)-mu(E\F)-mu(F\E)]/2.

The right side agrees across models. Setting F=X and using nu_A(X)=nu_B(X)=1
fixes Re(nu_A(E))=Re(nu_B(E)). Subtracting the product of these real parts
from the displayed identity fixes the product of the two imaginary parts
for every E,F. If every imaginary part vanishes the measures agree. Otherwise
choose E0 with Im(nu_A(E0))!=0. Its magnitude is fixed, so its sign fixes one
common sign for Im(nu_B(F)) relative to Im(nu_A(F)) for every F. This proves
the identity/conjugation alternative. Normalization has fixed the global phase.
Consequently, full diagonal data still need not determine the imaginary part
of D: global conjugation can reverse it. This corollary concerns scalar
rank-one models, not general vector-valued decoherence functionals.

## Unit-modulus timid transitions force an atomic extension

Consider any nonzero scalar growth rule with a finite complex-measure
extension nu. Suppose every timid transition has modulus 1 after some finite
parent size n0. Let h_C be the eventually-timid continuation of C, and H the
countable collection of those paths.

For any C of size n>=n0, the cylinders along h_C decrease to {h_C}.
Countable additivity of a finite complex measure gives continuity from above:

    nu({h_C})=lim_(m->infinity) A(prefix_m(h_C)).

All timid multipliers have unit magnitude. Consequently this limit must have
modulus |A(C)|, so h_C is a nonzero atom. Existence of the finite extension
itself forces convergence of its accumulated phases; unit modulus alone
would not guarantee that convergence.

For fixed n the h_C are distinct. Hence

    |nu|(H) >= sum_(|C|=n)|nu({h_C})| = V_n.

Finally ||nu||_TV=sup_n V_n. To see the reverse inequality to V_n<=||nu||,
approximate any finite measurable partition by cylinder-algebra sets in
|nu|-measure, disjointize the approximants and refine them to a common-depth
cylinder partition. The resulting partition sums are bounded by sup_n V_n
and approach the original partition sum. Taking its supremum proves equality.
Equivalently, this is the familiar generating-algebra characterization of
variation, with the approximation argument above supplying the needed step.

It follows that |nu|(H)>=sup_n V_n=||nu||_TV, so |nu|(X\H)=0. Thus the
extension is purely atomic on eventually-timid paths. This covers the circle
construction in RESULT.md, where |q(C)w(C)|=1 for every parent size >=3.
A non-atomic variant must relax that unit-timid-modulus condition, as well
as supply a different extension argument. Merely replacing the atomic-padding
proof with another proof cannot remove its atomic support.
