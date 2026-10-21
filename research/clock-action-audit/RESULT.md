# Clock comparison: match the charge before comparing the physics

Coordinator derivation, 21 October 2026. Elementary finite spectral and
linear-algebra results applied to our model; no novelty claim. Independent
review and full source correspondence remain pending.

## Primary reading and scope

Read Boette–Rossignoli, arXiv:1806.00956v2, Section II, Eqs. (1)–(9), and
Ludescher et al., arXiv:2607.24976v1, Section IV.1 and Appendix B.2,
Example 32, Eqs. (58)–(60), as primary HTML. Read depth: full text at these
constructions, not full-paper or code audit. Sources:
https://arxiv.org/html/1806.00956v2 and
https://arxiv.org/html/2607.24976v1 .

The first construction imposes a product-of-steps closure. The second supplies
an explicitly cyclic finite-group action and a frame instrument. Neither
licenses assigning an arbitrary interacting real-spectrum Hamiltonian to a
finite-group action without checking its period. The following audit concerns
our proposed translation, not a refutation of those papers. Not all printed
intermediate generator identities in Example 32 have been independently
reconstructed here; use its explicit position action as the source anchor.

## 1. Representation, energy origin and aliases are different tests

Let H be finite-dimensional Hermitian, N>=2, and

    U_lambda = exp[-2 pi i (H-lambda I)/N].

The powers U_lambda^k define a unitary representation of Z_N on the stated
kinematic space iff U_lambda^N=I, equivalently

    spectrum(H) is contained in lambda + Z.

Proof: diagonalize H. The Nth power has eigenvalues
exp[-2 pi i(E-lambda)], which equal one precisely under this condition.
Existence of *some* scalar energy-origin repair is equivalent to every energy
gap being an integer. A single common scalar phase in U^N can therefore be
removed; a nonscalar U^N cannot. A projective action on rays must be
separated from the specified linear action on vectors.

Regardless of whether this is a group action, its fixed space is

    Fix(U_lambda) = direct sum over k in Z of V_(lambda+kN),

where V_E=ker(H-E I). It equals the desired Dirac surface V_lambda iff no
other occupied energy is congruent to lambda modulo N. These are aliases of
the finite sampling, not an extra dynamical prediction. Spectral width <N is
a sufficient condition excluding aliases, not a necessary condition.

Thus three failures must not be conflated: an unremoved scalar energy origin,
a genuine failure of finite-group closure, and choosing a different or aliased
charge sector. Selecting charge zero in one model and a free eigenvalue in
another does not hold the physical constraint fixed.

## 2. Explicit model and an exact interacting classification

Use our clock H_C=diag(0,1,2), qubit H_S=(eps/2) sigma_z and
H=H_C tensor I + I tensor H_S + g |1><1| tensor sigma_x, g real.
Its spectrum, with multiplicities, is

    +/- eps/2,  1 +/- sqrt((eps/2)^2+g^2),  2 +/- eps/2.

At eps=1,g=0 all energies are half-integers. The unshifted generator has
U^3=-I, while lambda=1/2 repairs closure on the entire kinematic space.
Fix(U_(1/2))=V_(1/2), dimension two. That removes the supposed disagreement
between an empty unshifted fixed space and this particular Dirac surface.
The boundary energies -1/2 and 5/2 instead alias for lambda=-1/2: the fixed
space has dimension two while the Dirac surface has dimension one.

At eps=2,g=0 the spectrum is {-1,0,1,1,2,3}. The unshifted action is valid,
but Fix(U_0)=V_0 plus V_3, while Fix(U_1)=V_1. Both have dimension two but
are different subspaces. Matching only dimension is insufficient.

For eps=2 and arbitrary g, a scalar origin repair exists iff

    sqrt(1+g^2) is an integer,
    equivalently g^2=k^2-1, k=1,2,3,... .

Necessity: an untouched energy is -1, so any common fractional energy origin
must be integer; the two interacting energies must then be integers.
Sufficiency follows directly from the displayed spectrum. Generic g fails;
g=1/2 has sqrt(5)/2 irrational, so no energy shift repairs it. At g=sqrt(3)
the spectrum is {-1,-1,1,1,3,3}: a valid interacting cyclic action exists.
At g=sqrt(8), V_-2, the two-dimensional V_1 and V_4 alias modulo three,
so the fixed space has dimension four instead of one, despite a valid action.
This is a complete analytic classification for this commuting clock projector
and eps=2 only, not for arbitrary interactions or all clock models.

## 3. The relevant representation domain includes the frame outputs

It can be unnecessarily strong to require a representation on all of an
unused kinematic space. Let V be a chosen physical input subspace and M_0 a
seed. The minimal invariant output domain is

    W = span{ U^k M_0 v : k in Z, v in V }.

The cyclic representation needed for the orbit instrument exists on W iff
(U^N-I)M_0|V=0. Indeed the same equality then holds on each orbit vector;
necessity follows since the seed image lies in W. Restricting to Fix(U)
alone is insufficient: M_0 generally leaves that space.

For eps=2,g=1/2 above, V_1=span{|0,up>,|2,down>} remains two-dimensional.
The local clock seed M_0=sqrt(3)|tau_0><tau_0| tensor I maps V_1 onto
|tau_0> tensor C^2 (up to a nonzero scale). This range has nonzero projections
onto the n=1 interacting energies 1 +/- sqrt(5)/2. U_1^3 is not identity
on those projections. The seed-orbit action therefore fails even on W;
restricting only the physical inputs does not rescue this particular frame.
This does not exclude a different non-local seed or a continuous group.

## 4. Reading covariance and unitary conditioning need their own checks

A cyclic action alone does not imply it shifts the specified clock readings.
For P_k=|tau_k><tau_k| tensor I, the local seed orbit requires

    U^k P_0|V = P_k|V             (for V fixed by U),

not merely [H_int,H_C tensor I]=0. In our energy-projector example at
(eps=2,g=sqrt(3),lambda=1), an initial |0,up> lies in V_1. Its seed slice
contains n=1 with spin up. The interacting block rotates that spin with
nonzero off-diagonal coefficient proportional to
sin[(2pi/3)*2]*g/2, while P_1|0,up> has spin up only. Thus even this valid
cyclic action fails local reading covariance on V_1. Commutation with H_C
preserves energy blocks; it does not by itself translate clock readings.

There is also a direct criterion independent of a proposed group. For an
isometric embedding J:C^d->V define R_k=sqrt(N)(<tau_k| tensor I)J.
A state-independent isometry T_k:ran(R_0)->ran(R_k) satisfying
T_k R_0=R_k exists iff

    R_k^dag R_k = R_0^dag R_0.

Proof: the equality makes R_0 v -> R_k v well-defined and preserves every
inner product; conversely an isometry preserves the Gram matrices. It is
onto ran(R_k). If d equals the system dimension and R_0 is invertible, this
is precisely unitarity of R_k R_0^-1. If R_0 has a kernel, this gives dynamics
on the accessible range only, not all physical degrees of freedom.

All-reading uniform probability for every normalized physical input is the
stronger-looking but equivalent normalized statement R_k^dag R_k=I for every
k: equality of all Gram matrices implies I by summing them, since the
readings resolve the identity and J is an isometry. One trajectory's equal
norms cannot establish this all-input property.

## Consequence for integration

Keep the worker's finite numbers as provisional diagnostics. Remove any
claim that generic exp[-2pi i H/3] is automatically a Z3 action. Recompute
comparisons at matched lambda, check aliases, and test the seed's output
domain plus actual reading covariance. Explicitly chosen step kicks and a
closure-adjusted final kick describe an additional model choice unless an
intertwiner preserving the states and instruments is supplied. Some earlier
mismatches vanish under the first repair; genuine obstructions survive the
second and third tests. No temporal ontology follows from any of them.
