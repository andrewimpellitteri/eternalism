# Uniform window mass and a common late compensator

31 October 2026. Coordinator derivation, conditional on the fixed-point
construction, its low-order bounds, finite-cone domain-of-dependence/uniqueness,
the compact-limit passage and the actual incoming-mass identity. No new external
existence theorem, ADM equality, prefix-mass constraint or novelty is asserted.

## 1. Repair the short-window estimate

The rescued worker report, line 96, uses

    M^2(tbar+2)<=3M^2 T_max.

With tbar=3T_max/2 this is false whenever 0<T_max<4/3. A sharper bound uses the
small nonlinear tail, rather than paying amplitude M for the entire cut-off.

Write T=T_max>0 and take 0<eta<min(1/2,T/4). At the fixed point,

    Psi=J_eta^2 f,       f=T_n Psi,
    ||Psi||_infinity<=2M.

For t>=tbar, tau(t)>=T, so the zero-extended target satisfies y(tau(t))=0.
Thus f=-chi I there. The candidate's low-order bound gives
`|I|<=C epsilon_core^3`, uniformly in the cone vertex. Retardation then implies

    |Psi(t)|<=C epsilon_core^3       for t>=tbar+2eta,
    Psi(t)=0                       for t>=tbar+1+2eta.

The actual incoming-profile normalization is E_window=(1/4) integral Psi^2.
The part up to tbar+2eta has length at most 2T; the remaining part has length
at most one. Consequently

    E_window <= 2M^2 T + C0 epsilon_core^6.

Use epsilon_core=2 kappa M, with kappa=max(1,(tbar+3)^gamma), and absorb the fixed
kernel/cut-off constants into C1(T,gamma). Then

    E_window <= 2M^2 T + C1(T,gamma) M^6.

For each T>0 choose M_*(T,gamma) additionally so that
`C1 M_*^4<=T`. This yields

    E_window <= 3M^2 T,

uniformly in n and eta. This repair permits all positive observation-window
lengths; it does not assert a threshold uniform as T tends to zero. M=0 is the
zero-core case and is handled directly.

## 2. Keep one tail family while the core profiles vary

Fix E>=3M^2 T. Reserve half the external small-data budget for the late tail.
Choose a nonzero nonnegative smooth bump g supported in [1,6] and put

    G_K(v)=sum_(k=3)^K g(v-c-2^k),       c>=tbar+2.

The translated bumps are disjoint. Their first two derivative sup norms are
bounded independently of K. The separated-bump argument in LOY section 5,
(5.1), Step 1 supplies the source smallness budget independently of K for
0<gamma<1. Finite truncation only decreases the relevant positive integral.
This is the source's method, not a new construction.

Let b_max>0 be small enough for that reserved budget. Choose K once for this E
so that

    ||G_K||_L2^2 >= 4E/b_max^2.

Such a finite K exists because disjointness gives
`||G_K||_L2^2=(K-2)||g||_L2^2`. For each finite-cone core Psi_n define

    e_n=(1/4)||Psi_n||_L2^2,
    beta_n=2 sqrt((E-e_n)/||G_K||_L2^2),
    Phi_n=Psi_n+beta_n G_K.

Then 0<=beta_n<=b_max, the supports are disjoint, and

    (1/4)||Phi_n||_L2^2=E.

Use the same K, c and G_K for every n. This yields a common compact support and
a common second-derivative bound when the R3 core bound is available. The
amplitude need not be differentiable in the target or in n; compactness is enough.
Finite-cone uniqueness/domain of dependence preserves the original core solution
and its trace identity before the tail begins. No theorem of unique scattering
selection at past null infinity is used by this argument.

After extracting a joint subsequence, C0 convergence on this common compact
support gives Phi_n->Phi_* in L2 and hence `(1/4)||Phi_*||_L2^2=E`. To identify
that quarter integral as the global solution's actual total incoming mass,
retain [INCOMING_MASS.md](../INCOMING_MASS.md): first pass to the global solution
at fixed finite V, then take u to minus infinity, and only then V to plus infinity.
Its uniform remainder and field-convergence hypotheses must hold for this
bounded profile family. This note does not replace that hypothesis check.

Thus choosing the tail after a core fixed point does not require a globally
continuous scattering map or a target-independent unique core. It does require
one common compensator family before the compact limit is taken. Merely choosing
unrelated tails whose supports escape with n would not justify this L2 passage.

## 3. What the mass constraint says

E is the total incoming boundary mass of the selected global solution, not ADM
mass. The mass at an earlier ingoing prefix is not fixed by this construction.
The common K can depend on E; its independence of n does not supply any uniform
large-E support bound. Smooth finite profiles and uniform second derivatives do
not supply a smooth limiting prescribed-history model.
