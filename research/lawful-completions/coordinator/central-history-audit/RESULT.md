# Central-history candidate: disposition of the rescued review

31 October 2026. Direct coordinator review of the quota-interrupted GLM draft.
This accepts bounded algebraic corrections, not the complete interpolation theorem.
The original worker files and Claude's candidate are preserved. No novelty or
ontological conclusion is asserted.

## Decision and controlling files

The worker's principal assembly objection is rejected. Its weaker-data objection
is also misplaced at the finite-cone Schauder step. Two useful components now have
explicit conditional proofs here; final integrated review remains open.

| Obligation | Disposition |
|---|---|
| Smoothing residual | Correct in the original candidate when its variables are kept distinct; proof below |
| Smooth finite-cone inputs | Supplied by the smooth convolution; no extension to all Lipschitz trial data is needed at this step |
| Second-derivative ball, R3 | Expanded in [SECOND_DERIVATIVE.md](SECOND_DERIVATIVE.md), conditional on the listed external estimates and the stated low-order operator bounds |
| Window mass and arbitrarily large finite total mass | Expanded in [MASS_ASSEMBLY.md](MASS_ASSEMBLY.md); uses the actual incoming-mass identity and a common late-tail family |
| Bare C1 target, R4 | Not accepted here; a separate weaker-category argument is still needed |
| Smooth target gives smooth prescribed-history model | Not established; the smooth finite-sample result does not supply uniform all-order profile bounds for this inverse problem |
| Entire-past matching, four-dimensional C1,1 reconstruction, completeness | Retain the named C11/source inputs; not reproved here |
| Uniqueness of all profiles producing the target | Not asserted; late profiles can differ without changing the observation window |
| Source registry in the rescued worker lane | Missing despite its report; this audit has its own register and does not invent the missing file |

Original versions checked:
[Claude candidate](../../claude-central-history/RESULT.md) section 4, lines 84–99;
[worker objection](../../central-history-review/RESULT.md) section 1, lines 40–82.
Hashes and pinned repository revisions are in [PROVENANCE.json](PROVENANCE.json).
The branch-preservation check is in [RESCUE_AUDIT.json](RESCUE_AUDIT.json).

## 1. The residual estimate uses the smoothed profile

Write J for the retarded mollifier and T_n for the candidate's trace operator.
Rename the fixed point Z. The original candidate's construction is

    Z = J T_n J Z,       Psi = J Z.

Consequently

    Z = J T_n Psi,       Psi = J^2 T_n Psi.

No nonlinear operators have been commuted. For a nonnegative normalized smooth
kernel rho supported in (0,1), and f=T_n Psi with Lipschitz constant L,

    J^2 f(t) = integral_0^1 integral_0^1
                 rho(s)rho(q) f(t-eta(s+q)) ds dq,

    |Psi(t)-T_n Psi(t)| <= 2 eta L integral_0^1 s rho(s) ds <= 2 eta L.

Use zero extensions and the corresponding retarded interval. On the observation
window chi=1, the axis identity is

    Psi - T_n Psi = Lambda (phi_c - y composed with tau).

With Lambda>=2/3 and Lip(T_n Psi)<=2M this bounds the physical trace error by
6M eta. Thus any eta_n->0 suffices for this residual, subject to the separate
compactness and a priori bounds. No continuity modulus uniform in n is consumed.

The worker instead assumes `Psi=J T_n J Psi`, which is the equation for Z.
Its extra term `T_n J Psi-T_n Psi` results from confusing the two variables.
Failure of uniform C1 approximation on a Lipschitz ball is a valid general
observation but does not refute the construction actually used.

## 2. Smoothness, support and continuity at the finite-cone step

For fixed eta>0, convolution with the smooth compact kernel sends bounded
zero-padded data to C-infinity data. The derivative bound is

    ||partial^k J_eta f||_infinity
        <= eta^(-k) ||rho^(k)||_L1 ||f||_infinity.

The constant may grow as eta shrinks. Existence for each finite n needs no uniform
bound at every order. The solution operator inside `J T_n J` is evaluated at
`J Z`, so its input is smooth even when the trial Z is merely Lipschitz. The
worker's claim that J Z is C1 at best is false for this kernel. This removes that
specific smooth-data objection; it does not prove the limiting regularity.

For arbitrary trial Z supported in [A+delta,tbar+2], J Z can extend eta farther
right. Use the harmless common length bound Lhat=tbar+3 for eta<1/2 when verifying
the source smallness condition. This changes a constant depending on T_max only.
For the constructed fixed point there is more slack: T_n Psi vanishes past
tbar+1, Z past tbar+1+eta, and Psi past tbar+1+2eta<tbar+2. Retardation preserves
the left zero interval. Therefore the actual profile has the required support.

At each fixed n and eta, J is bounded from C0 to C1; the candidate's named finite-
cone C1-data continuity input, Repair A, suffices for continuity of `J T_n J`.
This input is retained conditionally here. No C0 continuity of T_n on every
unsmoothed Lipschitz trial profile is needed for this route.

## 3. What is stronger, and what remains

The expanded R3 proof isolates the boundary term in I-double-prime, separates the
axis and large-radius estimates, and shows how the target's second derivative
enters linearly. The mass proof handles all positive window lengths without
using the worker's false bound `tbar+2<=3T_max`.

These are explicit project deductions from named source bounds. Some source
proofs are sketches, as the source itself states; those have not been silently
replaced by a claim of independent reconstruction. The complete global theorem
still requires inspection of the combined continuity, compact-limit, axis and
completeness chain. A finite-sample theorem does not prove a function-space
inverse theorem, and smooth finite approximants do not prove a smooth limit.

The changed philosophical conclusion is limited: this review supplies no reason
to abandon the whole-window candidate on the worker's two stated objections.
Even a completed control theorem would concern past-relative determination in a
specified physical class; it would not settle which temporal events exist.
