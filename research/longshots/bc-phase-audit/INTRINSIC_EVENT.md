# A completed, relabeling-invariant question for the phase family

Coordinator calculation, 22 October 2026. The event is intrinsic; its value
below is a scalar history-measure value and a rank-one quantum-measure value,
not a detector probability or a derived physical observation.

## Model and the comparison being made

Use the non-atomic completion in `../bc-all-stages/PERCOLATION_TAIL.md`.
Let u=(3+4i)/5, or compare the real control u=1. Set

    q(single)=1/2,   q(chain2)=1/4,   q(antichain2)=u/4,
    q(C)=10^(-|C|) for |C|>=3,
    w(C)=1/q(C)-sum_(P proper ideal C)w(P),
    t(C,P)=q(C)w(P).

The existing completion proof also covers u=1: its inverse-weight perturbation
at size two has Gaussian norm <=96 instead of the earlier maximum 504/5.
Early w values are 1,1,2,1 for empty, singleton, chain2, antichain2, all nonzero.
Thus both models have the required nonzero scalar transitions and completion.
For each let nu_u be its additive complex measure and

    D_u(E,F)=conjugate(nu_u(E))nu_u(F),   mu_u(E)=|nu_u(E)|^2.

We compare two different dynamics with the same late q schedule. Changing u
also changes other early transition magnitudes; we are NOT holding all
finite cylinder norms fixed, nor comparing two mere labelings of one model.
The question is whether this parameter change has any effect on a specified
intrinsic completed event. It does. This alone cannot isolate holonomy as a
unique physical resource or exclude other models matching the event's value.

## 1. Intrinsic event and measurability

Let M(C_infinity) count the minimal elements of a completed causet. Existing
elements never acquire a new past. A new birth is minimal exactly when its
precursor is empty. Hence, starting from the initial element,

    M=1+number of gregarious births.

An order isomorphism preserves minimal elements, so E_2={M=2} is invariant
under natural relabelings of the completed causet. It is not a first-three-
birth question. If M_N counts minima after N births, then

    E_2 = union_N intersection_(K>=N) {M_K=2}.

This is a countable combination of finite cylinder unions and is measurable.
It includes completed causets under every natural labeling simultaneously.
The primary distinction between cylinder questions and completed covariant
questions is documented in the observer audit, using Brightwell et al.,
gr-qc/0210061v2 Sections2–3. No quantum stem-generation theorem is assumed.

## 2. Exact pushforward to the minimum-count variable

At two births, the parent is a chain (one minimum) or antichain (two minima),
each with amplitude 1/2. At the next birth, the amplitude for another minimum
is respectively 1/4 or u/4. Summing the non-gregarious transitions by MSR gives
this exact stage-three count polynomial:

    G_3(z)=z[3/8+(5-u)z/8+u z^2/8].

After parent size n>=3, the gregarious amplitude q_n=10^-n is independent
of the finite parent shape. Summing histories of a given minimum count,
the empty precursor contributes q_n and all others contribute 1-q_n.
Therefore, at N>=3 births,

    G_N(z)=G_3(z) product_(n=3..N-1)(1-10^-n+10^-n z).

This is derived by summing complex amplitudes; it does not require treating
complex transitions as probabilities. The tail factors happen to be ordinary
positive Bernoulli factors. Since their parameters have finite sum 1/900,
they define the distribution of a finite tail count K. The completed scalar
pushforward is the convolution of the finite complex vector encoded by G_3
with that real tail law. It has no mass at infinite M. Equivalently, for
|z|<=1 the bounded functions z^(M_N) converge almost everywhere under the
reference measure and hence under |nu_u|; dominated convergence gives

    G(z)=z[3/8+(5-u)z/8+u z^2/8]
         product_(n=3..infinity)(1-10^-n+10^-n z).

For E_2 it also suffices to use dominated convergence of 1_{M_N=2}, which
converges on every history. The complex measure is finite, so both arguments
are legitimate; no conditionally convergent path sum is introduced.

## 3. A strict difference on the same completed event

Let the tail have zero-count probability b0 and one-count probability b1:

    b0=product_(n>=3)(1-10^-n)>0,
    s=sum_(n>=3) 1/(10^n-1),   b1=b0 s.

Extracting the coefficient of z^2 gives

    nu_u(E_2)=[(5-u)b0+3b1]/8 = A-uB,
    A=(5b0+3b1)/8,       B=b0/8.

Both A and B are positive real numbers. Since |u|=1,

    mu_u(E_2)-mu_1(E_2)=2AB(1-Re u).

For u=(3+4i)/5 this is strictly positive, with the exact expression

    gap=b0^2(5+3s)/80.

A simple global bound is b0>=1-sum_(n>=3)10^-n=899/900, so

    gap >= (899/900)^2/16 = 808201/12960000 > 0.

Thus the two models do not assign the same rank-one quantum measure to E_2.
No map preserving the identification of every intrinsic event (in particular
E_2) and these quantum-measure values can identify these two fixed models.
This is narrower than a general no-equivalence claim between all norm-only
and full-covariance models, and it is not a proof of empirical distinguishability.

## 4. Rigorous numerical enclosures rather than a cutoff assumption

For a cutoff L>=3, compute b0_L=product_(n=3..L)(1-10^-n) and
s_L=sum_(n=3..L)1/(10^n-1) using exact fractions. Put

    r_L=sum_(n>L)10^-n = 10^(-L-1)/(1-1/10).

Then

    b0_L(1-r_L) <= b0 <= b0_L,
    s_L <= s <= s_L+r_L/(1-10^(-L-1)).

For both selected u values, the formulas for mu and the gap are increasing
in b0 and s on these positive intervals. Substitution therefore gives rigorous
rational enclosures, not a numerical extrapolation. The checker independently
sums all finite causet amplitudes through five births and reproduces G_N for
both models. It separately verifies the infinite-tail interval bounds.

## What this resolves and what it leaves open

The earlier first-n shape witness was not a completed covariant event.
E_2 is, and its mathematical value differs across the fixed phase family.
The example therefore avoids that specific event-selection failure. However,
nu is an amplitude measure, not a normalized density operator on an orthogonal
history register. Taking its scalar pushforward is not applying a CPTP
class-record channel; that channel could destroy the coherent readout, as the
observer correction proves. No experimental instrument, physical gauge
interpretation, full vector/DF covariance, unique phase diagnostic or new
physics has been established. The primary priority comparison is a separate
part of this lane and may reduce the result to an elementary application.
