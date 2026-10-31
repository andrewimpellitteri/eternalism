# A non-atomic matched-cylinder pair

22 October 2026. Explicit scalar construction and analytic all-stage proof.
Independent disposition is in `INDEPENDENT_REVIEW.md`; finite checks and
rigorous infinite-tail enclosures are separate from the proof. The methods
are known factorization, Möbius inversion and measure extension, with no
theorem-priority claim (`PRIOR_WORK.md`).

## Statement and the change from the atomic pair

There are two normalized finite complex measures nu_A,nu_B on the labelled
infinite-history cylinder sigma algebra whose variation measures are atomless,
whose nonzero transitions obey scalar ratio BC and MSR, and which have
norm-only cylinder covariance. The magnitudes of every corresponding
individual finite labelled cylinder agree across models. Nevertheless, for
the intrinsic completed event E2 = “exactly two minimal elements”,

    mu_B(E2)-mu_A(E2) > 399999/10000000 > 0,
    mu_j(E)=|nu_j(E)|^2.

This is NEW cylinder-magnitude data compared with the earlier atomic pair.
The same atomic data could not have a non-atomic realization: those data
determine the variation measure (`VARIATION_DATA.md`). The new continuation
makes later precursor weights equal across models, instead of making each
timid amplitude have modulus one. Both measures are absolutely continuous
in variation with respect to a specified atomless real-percolation measure.

Atomlessness here concerns the labelled-history sigma algebra. It does not
assert atomlessness of an unlabelled quotient or full vector/DF covariance.
The rank-one quantum measure is nonadditive, and is not a readout probability.

## 1. Scalar rule and unchanged early seed

Work with finite naturally labelled posets. Ideals are counted as actual
subsets, including isomorphic duplicates; their induced isomorphism types
determine the weights. Set

    f(C)=1/q(C),
    w(C)=f(C)-sum_(P proper ideal C)w(P),
    t(C,P)=q(C)w(P).

The empty poset has q=w=1. For both models q(single)=1/2 and q(anti2)=u/4,
where u=(3+4i)/5. Set q(chain2)=v/4 with v=u in A and v=conjugate(u) in B.
Thus w(single)=1, w(chain2)=4/v-2, w(anti2)=4/u-3. All are nonzero.

The **only** unequal early weight is chain2:

    w_A(chain2)-w_B(chain2)=-32i/5.

The chain weights are conjugates, so their magnitudes agree. All other early
weight magnitudes agree, and |q| depends only on parent cardinality. The
stage-three amplitudes are as in `../bc-matched-norms/RESULT.md`: their sum
is 1 and their total Gaussian norm is 2, so V_3=sum_C |A(C)|<=2. Their
minimum-count polynomial is

    G_3(z)=[(4-v)z+(4+v-u)z^2+u z^3]/8.

In particular a_A=G_3[z^2]=1/2, a_B=1/2-i/5 and
|a_B|^2-|a_A|^2=1/25. Coherent finite-union data already differ.

## 2. Opposite parent phases, identical later precursor weights

For n=|C|>=3 set L=1000 and R_n=L^n. Let c(C) be the number of actual
two-element chain ideals of C. Such an ideal consists of an element having
exactly one predecessor together with that predecessor. Therefore
c(C)<=n (in fact <=n-1 for nonempty C), and c is isomorphism invariant. Define

    h(C)=-16c(C)/5,
    x(C)=sqrt(R_n^2-h(C)^2) > 0,
    f_A(C)=x(C)+i h(C),
    f_B(C)=x(C)-i h(C).

Since R_n>=16n>|h(C)|, the positive square root exists. These are exact
algebraic coordinates, generally not Gaussian rationals. Clearly
|f_A|=|f_B|=R_n, so |q_A|=|q_B|=L^-n.

We claim **w_A(C)=w_B(C) for every |C|>=3**. By induction, the only unequal
weights among proper ideals are those of type chain2. Consequently

    sum_(P proper ideal C)[w_A(P)-w_B(P)]=-32i c(C)/5,
    f_A(C)-f_B(C)=2i h(C)=-32i c(C)/5.

Subtracting in the weight recursion proves the claim. The same argument
also verifies the correct distinct-subset multiplicity. All definitions
depend only on induced isomorphism type, so no branch depends on labels.
The common later weight may have a nonzero imaginary part; it is not
replaced by a real weight or by the reference dynamics.

MSR holds exactly by construction. For B=P union Q,

    t(C,P)t(B,Q)=q(C)q(B)w(P)w(Q)=t(C,Q)t(B,P),

which is scalar product BC. Nonvanishing, proved below, makes the usual
ratio form well defined. The path amplitude factors as

    A_j(C)=product_(k=0..|C|-1)q_j(C_k)
           * product_(a in C)w_j(past_C(a)).

Stage-only |q| and intrinsic past weights imply norm covariance within each
model. The matched early weight magnitudes and identical later weights
prove equal magnitudes of EVERY corresponding finite labelled cylinder in
the two models, at every depth. This is an induction, not a finite-cutoff claim.

## 3. Explicit real reference and all-stage nonvanishing

Take f0(C)=L^|C| and q0(C)=L^-|C|. Möbius inversion of the ideal sum gives

    w_j(C)=sum_(S subset Max(C))(-1)^|S| f_j(C\S),
    w0(C)=L^n(1-1/L)^m,    m=|Max(C)|.

For completeness, summing the first expression over ideals P of C cancels
the coefficient of each f(J) for a proper ideal J: it is the alternating
sum over subsets of the nonempty minimal-element set of C\J. Only J=C
has coefficient 1. Thus this expression uniquely solves the recursion.

The positive reference transitions are real transitive percolation:

    t0(C,P)=(1-1/L)^|Max(P)| L^(-n+|P|).

They sum to one and define a probability measure P0 on the labelled path
space. They are a reference, not the proposed complex dynamics.

Put d_j=f_j-f0 and b(z)=|Re z|+|Im z|. At size 0 d=0. At size 1 b(d)=L-2<L;
at size 2 b(d)=L^2+4/5<L^2+1. For n>=3,

    b(d_j(C))=|h|+R_n-sqrt(R_n^2-h^2)
              <= (16/5)n + h^2/R_n
              <= (96/25)n < 4n,

using R_n>=16n. In the Möbius sum, terms leaving one or two elements number
at most n and binomial(n,2); the later terms number at most 2^n. Therefore

    |w_j(C)-w0(C)| <= b(w_j(C)-w0(C))
       <= Ln+(L^2+1)binomial(n,2)+4n2^n
       <= H_n=L^2 n^2+4n2^n.

This bound is valid for every n>=1; H_0=0. Since m<=n,
w0(C)>=(L-1)^n=999^n. At n=3,

    H_3=9000096 < 997002999=999^3.

For larger n, both n^2/999^n and n2^n/999^n strictly decrease, so
H_n<999^n for all n>=3. Thus |w_j(C)|>=w0(C)-H_n>0. The seed weights
are nonzero separately, and all f_j and all transitions are nonzero.

The new timid modulus is below one. For n>=4, H_n<R_n/L (check n=4 and
use the same decreasing-ratio argument). Since m>=1,

    |w_j(C)| <= w0(C)+H_n < R_n(1-1/L)+R_n/L = R_n.

At n=3 the five unlabelled types give common weights
x-12/5, x-14/5, x-14/5+16i/5, R_3-12/5+16i/5, R_3-11/5+48i/5
for the chain, fork with one minimum, chain plus isolated point, two minima
below one maximum, and antichain, respectively; x uses each type's h.
Their moduli are strictly below R_3 (x>R_3/2, real subtraction in (2,3),
imaginary part of modulus <10 suffices). Hence 0<|t(C,C)|<1 for all n>=3.
Small proper/late phase errors, rather than unit timid modulus, will control
extension. No equal-radius circle constraint from the atomic construction remains.

## 4. Summable row distance and explicit L1 completion

For n>=3, |q_j|=1/R_n and

    R_n |q_j-q0| = |f_j-R_n|/R_n <= 4n/L^n.

Since sum_(P ideal C) w0(P)=R_n, the triangle inequality gives

    sum_P |t_j(C,P)-t0(C,P)|
      <= L^-n sum_P |w_j(P)-w0(P)| + R_n |q_j-q0|
      <= zeta_n=L^2 n^2(2/L)^n+4n(4/L)^n+4n/L^n.

This includes the changed q phase; omitting that term would be incorrect.
Define S1(x)=x/(1-x)^2-x-2x^2 and
S2(x)=x(1+x)/(1-x)^3-x-4x^2. Exact rational evaluation gives

    Z=sum_(n>=3)zeta_n=L^2 S2(2/L)+4S1(4/L)+4S1(1/L) < 1/8.

Consequently the row variation is <=1+zeta_n and

    V_n <= V_3 product_(k=3..n-1)(1+zeta_k)
        <= 2 exp(Z) < 16/7.

The extension is explicit. Every P0 cylinder has positive probability. Let

    nu_(j,n)=sum_(|C|=n) A_j(C) P0(. | cyl(C)).

Its density g_(j,n) is constant A_j(C)/P0(cyl(C)) on each level-n cylinder,
and ||nu_(j,n)||_TV=V_n. Refining one step changes reference transitions to
t_j and then resumes the reference law, so

    ||nu_(j,n+1)-nu_(j,n)||_TV
      =sum_C |A_j(C)| sum_P |t_j(C,P)-t0(C,P)| <= V_n zeta_n.

The densities are Cauchy in L1(P0). Their limit g_j defines the finite,
countably additive complex measure nu_j(E)=integral_E g_j dP0. It has mass 1
and its prescribed amplitude on every finite cylinder, by finite MSR and
L1 convergence. In particular |nu_j|=|g_j|P0 is absolutely continuous with
respect to P0. This is an application of known variation methods, not a
new general extension theorem.

## 5. Atomlessness and genuine departure from eventually-timid support

For any nonempty reference parent, a full precursor has probability
(1-1/L)^m<=1-1/L, m>=1. A proper precursor has probability <=1/L.
Thus every reference one-step probability is <=999/1000 after the first
element. Every fixed infinite labelled path has P0 probability zero.

The labelled history space is a closed subset of a countable product of
finite predecessor-mask spaces, with its cylinder Borel sigma algebra. In
particular it is a standard Borel space. To see explicitly why absence of
point masses suffices here, any positive-measure atom would select a unique
full-mass cell of each finite cylinder partition, nested across depths.
Their intersection is one history and would have the atom's positive mass,
a contradiction. Thus P0 is atomless. A finite positive measure absolutely
continuous with respect to atomless P0 is also atomless (split sets using
the reference, or apply the same standard-space point-atom argument).
Hence both |nu_j| are atomless.

As a separate check, zeta_4<1/(2L), and each term of zeta_n decreases for
n>=4. Thus every actual transition modulus for parents of size >=4 is
at most 999/1000+zeta_n<1999/2000. Every fixed path's cylinder amplitudes
therefore decay exponentially to zero. Continuity from above also proves
directly that the extension has no point atoms, consistently with the
absolute-continuity argument and the standard-space qualification above.

The set H of histories with finitely many non-timid births is countable:
each is the universal-top continuation of some finite C. P0(H)=0 and
|nu_j|(H)=0. In particular this completion is not the former atomic padding
measure in disguise. No claim about atoms on the unlabelled quotient is used.

## 6. The intrinsic completed-event gap survives

Let M_N count minimal elements after N births and E2={lim M_N=2}.
Monotonicity makes E2=union_N intersection_(K>=N){M_K=2} measurable;
minimal-element count is intrinsic under completed order isomorphism.
Only the empty precursor changes the count. If a_(j,N) is the amplitude
of {M_N=2}, finite MSR gives the exact increment

    a_(j,n+1)-a_(j,n)
       =sum_(|C|=n) A_j(C) q_j(C)
         * (1_{M(C)=1}-1_{M(C)=2}).

Therefore |a_(j,n+1)-a_(j,n)|<=V_n L^-n. The indicators {M_N=2} converge
pointwise to 1_E2 on every history. Dominated convergence for finite |nu_j|
identifies lim_N a_(j,N)=nu_j(E2). In particular

    |nu_j(E2)-a_(j,3)| <= tau
       = (16/7)sum_(n>=3)L^-n
       = 16/[7 L^2(L-1)] < 1/100000000.

This bound concerns gregarious activity, not all non-timid activity. The
latter need not be summable and is not assumed so. Using |a_A|=1/2 and
|a_B|=sqrt(29)/10<3/5,

    mu_B(E2)-mu_A(E2) >= 1/25-(11/5)tau-2tau^2
                     > 399999/10000000 > 0.

Finite deeper approximants can give much tighter certified intervals with
the same tail estimate starting at N, namely 16/[7 L^(N-1)(L-1)]. This is
a rigorous tail bound, not an assumption that a finite cutoff is completed.

## Scope of the advance

The ambiguity of individual-cylinder magnitude data survives when both
finite complex-measure extensions have atomless variation. It cannot be
attributed solely to eventually-timid atoms. The stronger data of all finite
unions still determine completed diagonal values, as proved in the previous
lane. A two-cylinder union already distinguishes the pair at depth three.

The construction is engineered, scalar, and covariant only in cylinder norm.
No general operator QBC classification, full vector/DF gauge covariance,
unlabelled atomlessness, continuum limit, physical instrument or detector
probability is established. No conclusion about temporal ontology, objective
passage, determinism, or a thermodynamic arrow follows. Priority for the
exact example is unestablished; the extension and factorization tools are known.
