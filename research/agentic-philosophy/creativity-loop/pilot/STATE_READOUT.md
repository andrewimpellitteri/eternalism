# A representation change with a checkable access boundary

Coordinator pilot, 22 October 2026. This is an application of standard Hilbert
space and martingale arguments, not a novelty claim or a derived detector.
Prior inputs: the accepted atomless growth pair and its common variation
measure; the repository's membership/coherent-filter audit. Mozota
Frauca–Sorkin, 1610.02087v1 Section 5.2, is a primary comparator for coherent
event filters, with its own ancilla/endpoint assumptions. The projector here
is defined directly in a chosen mathematical representation; we do not import
their experiment as an instrument for causal sets.

## Candidate, failure condition and repair

Try representing nu_j=g_j P0 as a unit vector psi_j proportional to g_j in
L2(P0), then specify the readout effects. **L1 alone is insufficient**: a
normalized density (1/4)x^(-3/4) on (0,1) is not square-integrable. This is a
deliberately seeded negative control, not a failed result discovered by this
pilot. The useful search question is whether this particular model has an
extra L2 bound. It does, as follows. The repair changes the representation
only after proving its extra existence condition; it does not change nu_j.

## 1. A stronger bound for this particular pair

Use the exact constants from `research/longshots/bc-matched-diffuse/RESULT.md`:
L=1000, w0(P)=L^k(1-1/L)^|Max(P)| and

    H_k=L^2 k^2+4k2^k,
    sum_(n>=3) zeta_n=Z<1/8,
    sum_P |t_j(C,P)-t0(C,P)| <= zeta_n.

For k>=3, H_k/(L-1)^k decreases and H_3/(L-1)^3<1/100. Hence
|w_j(P)|/w0(P)<101/100. For k=0 the ratio is 1; for k=1,2 it is less than
1 by the explicit seed (w0 is respectively 999, 999000 or 998001).
For parents of size n>=3, |q_j/q0|=1. Therefore every relative transition
z_P=t_j(C,P)/t0(C,P) has |z_P|<=101/100 and |z_P-1|<3.

Both row sums equal 1 and t0 is positive, so expanding squares gives

    sum_P |t_j(C,P)|^2/t0(C,P)
       =1+sum_P |t_j(C,P)-t0(C,P)|^2/t0(C,P)
       <=1+3 sum_P |t_j(C,P)-t0(C,P)|
       <=1+3 zeta_n.

Let g_(j,n)=A_j(C)/P0(cyl(C)) on each depth-n cylinder. Finite MSR makes
g_(j,n) a complex martingale under P0. Put K_3=||g_(j,3)||_2^2<infinity;
it agrees across models because their cylinder magnitudes match. The row
bound implies

    ||g_(j,N)||_2^2 <= K_3 product_(n=3..N-1)(1+3zeta_n)
                    <= K_3 exp(3Z) < (8/5)K_3.

No martingale convergence theorem needs to be assumed without explanation:
the increments have zero conditional mean, hence are mutually orthogonal in
L2. Bounded squared norms imply their squared norms have finite sum, so the
partial sums are Cauchy in L2. The limit agrees with the previously constructed
L1 limit since P0 is a probability measure and L2 convergence implies L1.
Thus the actual density g_j of nu_j belongs to L2(P0).

The matching-variation theorem gives |g_A|=|g_B| P0-almost everywhere. Hence

    K=||g_A||_2^2=||g_B||_2^2,   1<=K<(8/5)K_3,
    psi_j=g_j/sqrt(K)

are well-defined unit vectors. This is an additional proved mathematical
property of the chosen pair, not a property of arbitrary finite complex measures.

## 2. All multiplication-effect readouts agree

For any measurable 0<=f<=1 define the effect M_f by multiplication in L2(P0).
Then

    <psi_j,M_f psi_j> = integral f |g_j|^2 dP0 / K

agrees across models. Any finite POVM consisting of multiplication effects
with sum f_i=1 therefore has the same normalized outcome probabilities.
This is a precisely specified commutative readout model. It is stronger than
checking individual finite cylinders within this chosen representation.

These probabilities are **not** mu_j(E)=|nu_j(E)|^2. Nor are they asserted to
be the unique or physically prescribed history-record probabilities. Choosing
P0 and this Hilbert representation adds structure; a physical interpretation
would have to justify that structure and the accessible effects.

## 3. A coherent effect distinguishes, conditionally

For an event E with P0(E)>0, define e_E=1_E/sqrt(P0(E)) and
Q_E=|e_E><e_E|. The two-outcome projective instrument {Q_E,I-Q_E} is a valid
mathematical measurement on this Hilbert space. Its first probability is

    <psi_j,Q_E psi_j>=|nu_j(E)|^2/[K P0(E)].

The denominator is essential. Cauchy–Schwarz guarantees the expression is
between 0 and 1; normalization of nu(X)=1 alone would not do so.
For E2, P0(E2)>0: the reference can first produce two minima with positive
probability, and then avoid all further gregarious births with probability
product_(n>=2)(1-L^-n)>0. The accepted completed E2 gap therefore yields a
strict coherent-readout difference in this defined mathematical model.

Finite approximants F_N={M_N=2} satisfy 1_FN->1_E2 pointwise. Thus
e_FN->e_E2 in L2(P0), and the associated rank-one projectors converge in
operator norm. This is an approximation statement, not a certificate that a
finite observer decides E2. At each finite N, <e_FN,g_j> can be calculated
using g_(j,N) since e_FN is measurable at that depth. The infinite state uses
the common normalization K, not the finite K_N unless a finite model is
explicitly being studied.

## 4. What this pilot learned

The representation change produces two sharply different access models:
all multiplication effects agree, while adding a particular coherent effect
can distinguish. It does not show that a causal-set observer can prepare
psi_j, control superpositions of histories, or implement Q_E2. Intrinsic event
membership does not automatically make its coherent projector a physically
covariant instrument. Those are unresolved physical bridge premises.

The finite checker constructs explicit normalized states/effects at depth
three using the actual nonuniform reference weights. It verifies equal
pointer probabilities, unequal coherent probabilities, and loss of the
coherent distinction after dephasing. The completed statement above relies
on the analytic L2 bound. Neither constitutes an experiment or a conclusion
about temporal ontology. The next useful question is which access algebra
can be justified physically, rather than whether another toy phase gap exists.
