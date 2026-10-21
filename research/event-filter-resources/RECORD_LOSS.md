# Record leakage separates filtering from statistical reconstruction

Coordinator derivation, 21 October 2026. Submitted mathematical result;
independent review and exact-priority comparison are pending. No novelty claim.

## 1. Exact access criterion

Let C be the fixed channel from a history register to the observer's accessible
system. Let T>=0 be the desired scalar quantum-measure quadratic form.
A binary success instrument on that accessible system has an effect 0<=Q<=I.
It realizes P(success|rho)=eta Tr(T rho) for every input density matrix iff

    C*(Q)=eta T.

This follows from trace duality and equality of Hermitian quadratic forms.
It includes arbitrary auxiliary systems initially independent of rho, arbitrary
post-channel processing, and any group of success Kraus outcomes: all define
an effect Q. It excludes access to the discarded environment, pre-channel
encoding changes, input-dependent calibration, and dividing two measured
probabilities with an input-dependent denominator.

## 2. Which-history leakage: exact theorem

Suppose |i>|0_env> -> |i>|e_i>, with normalized environment vectors. Tracing the
environment gives a Schur channel C(rho)_ij=G_ij rho_ij, where
G_ij=<e_j|e_i>, G_ii=1 and |G_ij|<=1. Its adjoint multiplies Q_ij by conjugate(G_ij).
For an event E of m basis histories, let u_E=sum_{i in E}|i> and T=u_E u_E^dag.

**Theorem.** An effect satisfying C*(Q)=eta T for eta>0 on all inputs exists iff
|G_ij|=1 for every i,j in E. If it exists, eta<=1/m and that bound is achievable.

Proof. Diagonal equality forces Q_ii=eta for i in E and zero outside.
Positivity forces rows outside E to vanish. If G_ij=0 within E, the required
off-diagonal equality is impossible. Otherwise Q_ij=eta/conjugate(G_ij).
Its 2x2 principal minor requires |Q_ij|^2<=Q_ii Q_jj=eta^2, hence |G_ij|>=1.
Together with the channel bound this gives |G_ij|=1. Conversely these equalities
make the environment vectors parallel within E; the restricted G is rank one.
Choose Q_ij=eta G_ij within E, zero outside. Then C*(Q)=eta T, and Q has only
one nonzero eigenvalue eta m. Thus it is an effect precisely for eta<=1/m.

Any genuine which-history distinguishability inside E therefore prevents this
exact positive filter, regardless of how small a positive eta is chosen.
This theorem assumes all input superpositions in the full history register;
restricted dynamical preparations can evade it. It does not forbid statistical
reconstruction with signed estimators or environment-assisted erasure.

## 3. Exact approximate-recovery error for uniform leakage

Take C_gamma(rho)=gamma rho+(1-gamma) diag(rho), 0<=gamma<=1, on an m-dimensional
record space, m>=2. Its environment Gram matrix has off-diagonals gamma and
unit diagonal, so it is physically realized by
|e_i>=sqrt(gamma)|common>+sqrt(1-gamma)|i_env> with orthogonal environment kets.
Let P=|u><u|/m, u=sum_i |i>. The best observer-only binary approximation has
worst-input probability error

 min_{0<=Q<=I} ||C_gamma*(Q)-P||_op
   = (m-1)(1-gamma) / [m+(m-2)(1-gamma)].

Proof. Average Q over basis permutations and entrywise conjugation. Convexity
of operator norm and invariance of the channel/target imply no increased error.
The result is Q=a P+b(I-P), 0<=a,b<=1. Write c=(1-gamma)/m and
d=(a+(m-1)b)/m. The output eigenvalues are
lambda_parallel=gamma a+(1-gamma)d=Aa+Bb,
lambda_perp=gamma b+(1-gamma)d=Ca+Db,
where A=gamma+c, B=(m-1)c, C=c, D=1-c.
The error is max(1-Aa-Bb,Ca+Db), since the output is an effect.
For gamma>0, increasing a and decreasing b by C/D times the increase, until
one hits a=1 or b=0, preserves lambda_perp while increasing lambda_parallel
(AD-BC=gamma). At b=0 and a<1, lambda_parallel+lambda_perp=(A+C)a<=1;
there the first error dominates and increasing a improves it until a=1.
Thus an optimizer exists at a=1. Balancing the remaining decreasing and
increasing affine errors gives b=(m-2)c/[1+(m-2)c] and the asserted value.
For gamma=0 all output effects are diagonal; Q=I/2 attains error 1/2 and the
same formula holds. For gamma=1, Q=P gives zero error.

At gamma=1/2 the limiting error as m grows is 1/3. This is an error in a
normalized detector probability, not an unbounded-amplitude inference. The
exact arithmetic script verifies the formula and attainability at 30 (m,gamma)
pairs and checks every point of a separate rational grid for each pair.
This finite grid corroborates, but does not replace, the analytic minimization.

## 4. Statistical reconstruction and a precise exponential cost

Take two distinguished n-bit histories |0^n> and |1^n>. Suppose each bit leaks
independently through a dephasing channel with visibility gamma, 0<gamma<1.
On their two-dimensional span, coherence is multiplied by r=gamma^n.
Assume the accessible output preparations are

    rho_x = (I+r x X)/2,       -1<x<1,

coming from the input family (I+xX)/2 in that span. The desired pre-leakage
plus-event probability is theta(x)=(1+x)/2.
Measure X on each of N independently supplied outputs. If outcome s=+/-1,
use Y=(1+s/r)/2. Then E[Y]=theta, while

    Var(Y)=(1-r^2 x^2)/(4r^2).

Y is allowed to be negative or exceed one. Its sample mean is an unbiased
estimate of theta; it is not a single-run positive event filter.
At x=0, variance after N trials is 1/(4N r^2).

This is also a *local unbiased* lower bound for arbitrary collective
measurements on these N output states: the rho_x commute in the X basis, so
any measurement, including a collective POVM, is a classical randomized
processing of N independent X-eigenvalue labels. Their Fisher information is
N r^2/(1-r^2 x^2). The classical information-processing inequality and
Cramer–Rao bound therefore give Var(theta_hat)>=
(1-r^2 x^2)/(4N r^2) for an estimator locally unbiased at x. The direct X
sample-mean estimator saturates it.

At x=0, locally unbiased RMSE<=delta requires

    N >= 1/(4 delta^2 gamma^(2n)).

For gamma=1/2, delta=1/10, this is N>=25*4^n. It applies only to this unknown
input family and the stated independent-copy channel experiment. It is not a
general causal-set resource lower bound, a bound on arbitrary biased/minimax
estimators, or a restriction on coherent access before information leaks.
Different encodings, environment access or a smaller known input family can
change the task.

## 5. Prior-work boundary and next test

Buscemi–Chiribella–D'Ariano, arXiv:quant-ph/0611070v1, Introduction and Sections
2–3, study environment-assisted reversal of decoherence. The environment access
assumption is explicit and differs from the discarded-environment model here.
Buscemi quant-ph/0611111v2, abstract only, relates erasure efficiency to corrected
channel fidelity. Frauca–Sorkin 1610.02087v1 Section 5.2 gives the coherent
history-record projector being targeted here. These are close predecessors;
precise priority for the event-specific criterion and minimax formula is untested.
No new general quantum-error-correction theorem is claimed.

The next decisive step is to derive an actual observer channel C from an
accepted growth model and specified record instrument. Then solve the effect
feasibility problem in Section 1 on the dynamically allowed preparation family.
This replaces a vague appeal to 'finite observers' with a testable mathematical
contract. Whether temporal interpretations differ still depends on their
specified dynamics and access, not their labels.
