# Defeat check: this phase family has no extra quantum-measure predictions at fixed cylinder norms

Coordinator calculation, 22 October 2026. Same late schedule and all other
parameters fixed as in INTRINSIC_EVENT.md; u varies on the unit circle.

## A single finite cylinder already fixes the real part of u

For the three-element V poset with two minima below one maximum, its only
naturally labelled predecessor-mask representative is (0,0,3). Its amplitude
is obtained from the two-antichain parent:

    A_u(V)=1/2(1-3u/4)=(4-3u)/8,
    c_u=|A_u(V)|^2=(25-24 Re u)/64.

Thus equality of all finite cylinder norms in two members of this fixed
one-parameter family implies Re(u')=Re(u). Since |u|=|u'|=1, this forces
u'=u or u'=conjugate(u).

For a non-real u, the second option has a different relative cp phase, yet
all amplitudes are complex conjugates. The recursion has real coefficients,
q's other than the exceptional antichain q are real, and the reference
percolation measure is real. Induction gives

    w_(conj u)(C)=conjugate(w_u(C)),
    A_(conj u)(C)=conjugate(A_u(C)).

The same relation holds for the L1 completion densities and hence
nu_(conj u)(E)=conjugate(nu_u(E)) for every measurable completed event E.
Consequently every rank-one quantum measure satisfies

    mu_(conj u)(E)=mu_u(E).

All transitions remain nonzero and the completion exists for any unit u:
using the coarse bound b(4/u-100)<=106 gives
b(w-w0)<=8n+106 binomial(n,2)<=53n^2. The earlier proof uses
9^n>53n^2 for n>=3 and the summable row bound 53n^2/5^n instead of 51n^2/5^n.
The early weights are nonzero because |4/u-3|>=1.

## What the completed-event difference actually establishes

The u=(3+4i)/5 versus u=1 comparison in INTRINSIC_EVENT.md changes c_u from
53/320 to 1/64, so the difference of finite cylinder quantum measures is
3/20. Their different completed E_2 values are therefore not hidden from
all finite magnitude data. In fact, with A,B as in that note,

    mu_u(E_2)-mu_1(E_2)
      = (16AB/3) [c_u-c_1].

The completed-event gap is already determined by this finite cylinder value
within the fixed family. The intrinsic nature of E_2 removes the earlier
prefix-covariance mistake, but does not isolate a new phase-only prediction.

## Scope and decision

In this one-parameter family, fixing every cylinder magnitude leaves at most
complex conjugation, and conjugation preserves mu on all completed events.
This is an analytic statement for the whole unit-circle family, not a finite
parameter scan. It does not establish that the decoherence functional itself
is unchanged: its imaginary cross terms conjugate. Nor does it show equivalence
for experiments allowing additional coherent controls or specified readout
instruments. A shared diagonal quantum measure is a narrower assertion.

No new phase-only quantum-measure effect should be claimed for this family.
A stronger next problem would hold all finite cylinder norms fixed while
varying a larger phase family, and either find a difference on a fixed
intrinsic completed event or prove an appropriate rigidity theorem. Such a
problem needs its own bounded claim contract and prior-work audit.
