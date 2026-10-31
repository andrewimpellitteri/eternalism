# A nonvanishing all-stage phase model with an explicit scalar completion

Coordinator construction, 22 October 2026. Extends the fixed phase seed of
`bc-nonzero` under **scalar ratio Bell causality, MSR, and norm-only cylinder
covariance**. It does not impose full vector or decoherence-functional
covariance. Independent analytic reviews confirm the proofs in the stated domains; no novelty claim.

## Prior work and the precise question

Rideout–Sorkin, arXiv:gr-qc/9904062v3, Sections 4.1–4.2 and 4.4, already uses
gregarious-transition factorization and a product over element pasts. Its
classical full-covariance hypotheses are stronger than the norm-only
condition here. Srivastava–Surya, arXiv:2603.25503v1, Section 2.4 Eq. (17),
Section 3.1 and Section 4, explicitly discusses scalar models, then sets aside
the norm-only phase option. These passages were read at full text; not a
full audit of either paper's results or code. Primary URLs:
https://arxiv.org/html/gr-qc/9904062v3 and
https://arxiv.org/html/2603.25503v1 .

Two bounded web queries for norm/Bell phases and complex/gregarious growth
found no independently verified predecessor for this exact construction.
That search is insufficient to establish priority. Surya–Zalel, arXiv:2003.11311v1, Section2.3 Theorem2.1 and
Section3.1 Theorem3.1/Claim3.2, supplies the known bounded-variation and
summable-row-excess criteria (statements/product bound inspected; AppendixB
not newly audited): https://arxiv.org/html/2003.11311v1 . The factorization and
measure-completion techniques are known tools. No assertion of a
new open problem, theorem priority, or physical novelty follows.

The earlier fixed-seed witness was checked only through stage four. We now
ask whether a continuation can keep **every transition nonzero**, preserve
the phase at every later stage, and admit a finite complex measure on the
labelled infinite-history sigma algebra. For the specified weaker covariance,
the construction below gives all three. The first construction below deliberately approaches timid births at late
stages. PERCOLATION_TAIL.md gives a second completion absolutely continuous
with respect to a real-percolation reference, with zero variation on
eventually-timid histories. Neither has a claim to cosmological realism.

## 1. Factorization on finite posets

Work with naturally labelled finite posets C. Every down-set P of C is a
possible precursor for a new maximal element. Let q(C) be a nonzero complex
number depending only on the finite isomorphism type. Define recursively

    w(C) = 1/q(C) - sum_(P proper down-set of C) w(P),
    t(C,P) = q(C) w(P),

where w(P) is evaluated on the induced poset, irrespective of its inherited
labels. The empty poset has q(empty)=w(empty)=1. Down-sets are counted as
actual subsets: isomorphic but distinct subsets appear with their multiplicity.
This recursion is isomorphism invariant by induction on cardinality.

The MSR is immediate: sum_(P down-set C) t(C,P)=1. For precursor pair P,Q and
B=P union Q, both P and Q are down-sets of B and

    t(C,P)t(B,Q) = q(C)q(B)w(P)w(Q)
                 = t(C,Q)t(B,P).

If all w are nonzero, all transitions and ratios are defined, so this is
ordinary scalar ratio spectator-independence without a zero convention.
No operator ordering or noncommutative analogue is claimed.

For a naturally labelled N-element C, multiply transitions along its growth:

    A(C) = [product_(j=0..N-1) q(C_j)]
           [product_(x in C) w(past_C(x))],

where C_j is the initial j-element prefix and the past is the intrinsic
induced past-poset of x. If |q(C_j)| depends only on j, the first product's
modulus is independent of the growth order and the second product is fully
isomorphism invariant. Therefore |A(C)| is constant over all natural
labelings of C at every finite stage. The complex amplitude itself need not
be label independent.

### Restricted parametrization: when is the modulus condition necessary?

Add the hypothesis that a Markov transition rule t(C,P) is invariant under
isomorphisms of the finite parent with its distinguished precursor, and that
every transition is nonzero. Then the displayed recursion is not just an
ansatz: Bell pairing P with the empty precursor gives

    t(C,P)/q(C)=t(P,P)/q(P)=w(P),

where q(C)=t(C,empty), and MSR forces the recursion for w. Conversely that
recursion supplies BC and MSR. All-stage norm covariance is equivalent to
|q(C)| depending only on |C|. Sufficiency is the intrinsic-past product above.

For necessity, let e be any maximal element of C, B=C\{e}, and let P be the
past of e. Add a new isolated f. Compare the two orders B->C->C+f and
B->B+f->C+f. With a=t(B,P), norm covariance and the common nonzero amplitude
of the chosen history to B give

    |a q(C)| = |q(B)t(B+f,P)|.

BC with the gregarious transition gives t(B+f,P)/q(B+f)=a/q(B), hence
|q(C)|=|q(B+f)|. Replace a maximal element having nonempty past by an isolated
element repeatedly. This strictly reduces the number of relations at fixed
cardinality until the antichain is reached. Therefore all |q(C)| at that
cardinality agree. This is the modulus version of the classical
Rideout–Sorkin Section4.1 replacement argument, not an independent novelty
claim. It uses norm covariance one stage beyond the parent under discussion.

Thus, in this restricted scalar, isomorphism-invariant, nonvanishing Markov
class, the free q(C)'s have a common modulus per cardinality and arbitrary
shape phases subject to w(C)!=0. This does not classify rules that retain
label-dependent local transition data, zero amplitudes, phase-modified BC, or
operator-valued QBC. The fixed seed and explicit completion below require no
claim about those larger domains.

## 2. Exact seed and nontrivial phase

Set

    q(singleton)=1/2,
    q(two-chain)=1/4,
    q(two-antichain)=(3+4i)/20.

The moduli at size two both equal 1/4. The recursion gives

    w(singleton)=1,
    w(two-chain)=2,
    w(two-antichain)=(-3-16i)/5.

This exactly reproduces the accepted seed through three births: one-element
outgoing amplitudes 1/2,1/2; two-chain amplitudes 1/4,1/4,1/2; two-antichain
amplitudes (3+4i)/20 on each proper precursor and (11-12i)/20 on the full one.
For the three labelled copies of cp (a two-chain plus isolated point), path
amplitudes are (3+4i)/40,(3+4i)/40,1/8. Their moduli agree and the relative
phase between a complex and real path is (3-4i)/5 in the earlier convention.
The seed is a finite normalization of a complex amplitude process, not an
ordinary probability transition rule or a normalized orthogonal-register state.

## 3. Explicit summable escape, avoiding every zero

Use the Gaussian-rational norm b(z)=|Re z|+|Im z|, an upper bound for |z|.
All weights up to cardinality two satisfy b(w)<=B_2=19/5. For n>=3 recursively
choose

    R_n = 1 + 4^n B_(n-1),       q(C)=q_n=1/R_n  for |C|=n,
    B_n = 1 + (4^n+2^n) B_(n-1).

These are explicit positive rationals; no infinite avoidance search is needed.
An n-element poset has at most 2^n-1 proper down-sets. If
S_C=sum_proper_P w(P), then b(S_C)<=(2^n-1)B_(n-1). Consequently

    |w(C)| >= R_n-|S_C|
            >= 1+(4^n-2^n+1)B_(n-1) > 0,
    b(w(C)) <= 1+(4^n+2^n-1)B_(n-1) <= B_n.

Induction gives nonzero w on every finite poset and hence every transition
nonzero. Moreover the total modulus of non-timid transitions satisfies

    e(C)=sum_(P proper C)|t(C,P)|
        <= (2^n-1)B_(n-1)/(1+4^n B_(n-1)) < epsilon_n=2^-n.

The timid transition is t(C,C)=1-sum_proper_P t(C,P), so

    |t(C,C)-1| <= e(C),
    sum_P |t(C,P)| <= 1+2epsilon_n.

All-stage norm covariance follows from Section 1: the exceptional early q's
have equal modulus at their cardinality and all later q's are common.
The nontrivial cp phase persists on cp with any number of universal tops.
Each extra top's transition is nonzero, and its factor is identical for
isomorphic parent prefixes. Thus the three path-amplitude ratios stay unchanged.

## 4. Direct labelled complex-measure completion

Let X be the infinite naturally labelled history space with its cylinder
sigma algebra. Write V_n=sum_(|C|=n)|A(C)|. Finite branching and the row bound give

    V_n <= V_3 product_(k=3..n-1)(1+2epsilon_k)
        <= V_3 exp(1/2),        since sum_(k=3..infinity)epsilon_k=1/4.

The seed's total Gaussian norm is 8/5, so V_3<=8/5 and all V_n are bounded.
This already meets the familiar scalar extension criterion; the following
construction avoids relying on an unproved extension assertion.

Complete every finite C by adding universal tops forever and call that
infinite labelled path h_C. Define the finite atomic measure

    nu_n = sum_(|C|=n) A(C) delta_(h_C).

Different parents at the same n have different completed labelled paths.
For one more growth step, h_(timid-child(C))=h_C. Other children have distinct
completed paths. Thus even allowing coincidences only improves the triangle
bound

    ||nu_(n+1)-nu_n||_TV
      <= sum_C |A(C)| [|t(C,C)-1|+sum_proper_P |t(C,P)|]
      <= 2epsilon_n V_n.

The right sides are summable. The countable set H={h_C : C any finite poset}
contains all supports. Regard nu_n as l1(H) sequences; they converge in that
complete space. Their limit defines an absolutely summable atomic complex
measure nu on X, with ||nu||_TV<=V_3 exp(1/2). Each nu_n has mass one. Every
fixed cylinder of depth m has its prescribed amplitude for all n>=m, by the
MSR and deterministic padding, so nu has exactly those cylinder values and
nu(X)=1. This is a countably additive labelled scalar measure, not just a
finite experiment or formal path sum.

It is concentrated on histories with finitely many non-timid births. This
is a mathematical feature of the summable escape design, not a claim about
generic causal sets or a continuum limit. The n>=3 decay is essential to
this particular completion proof; no robustness under arbitrary rates is claimed.

One may define D(E,F)=conjugate(nu(E))nu(F). This is a normalized rank-one,
strongly positive, biadditive decoherence functional on this sigma algebra;
its diagonal is the nonadditive quantum measure |nu(E)|^2. The scalar nu
itself is additive. Neither is thereby fully label-gauge-covariant: different
labelings of a finite causet have different cylinder amplitudes, and cross
terms can detect the phase. The proven covariance is precisely the cylinder
norm condition. Restricting a measure to relabeling-invariant measurable events
is also not a proof of full decoherence-functional covariance or observer access.

## What has and has not advanced

Under the named weaker assumptions, neither nonvanishing transitions nor a
labelled scalar completion removes the original phase. The result strengthens
the earlier finite counterexample, rather than extending the scalar-percolation
classification or solving noncommutative QSG. It uses freely engineered,
rapidly shrinking late gregarious amplitudes. A source comparison, exact finite
check and independent review accompany the construction; a systematic novelty
or physical admissibility verdict remains open.
