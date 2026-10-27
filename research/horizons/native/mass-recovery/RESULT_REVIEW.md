# Recovery of the interrupted scalar-mass review

27 October 2026. Coordinator technical assessment. This completes bounded
checks abandoned on GLM quota; it is not an external independent referee
acceptance, manuscript integration, or priority clearance.

## 1. Disposition

The analytical constant-cylinder-potential argument and the separate ordinary
physical dust-mass argument survive this inspection within their stated scope.
The interrupted GLM NOTES.md is useful pre-comparison reasoning, but its
unfinished checker was not reliable. The apparent numerical contradiction came
from implementation errors, not a counterexample to the analytical claim.

The precise safe conclusion is existence of data and an interior timelike-future
event fixed in the massless model but unfixed for every sufficiently small
positive ordinary physical mass on the same fixed dust geometry. The data and
target are selected first, then the sufficiently-small mass interval. Neither
a complete classification of massive fixing nor a uniform mass threshold over
targets follows. The constant rescaled-potential family is a separate result;
it is not constant physical mass on dust.

## 2. What was wrong with the unfinished numerical control

The original files remain unchanged in their stopped worktree and in
research/runner-fresh-submission/preserved/horizons-perturbation-referee/.
check_recovered.py is an explicitly derived repair, not a wholly independent
new numerical implementation.

1. **RK4 components:** the intermediate stages used an intermediate position
   as the first derivative component, where the equation requires velocity.
   The repair implements the vector field (v,−(k²+λq(t))u) at each stage and
   checks against exact constant-potential solutions for k=1,7,19.
2. **Potential selection:** the nominal constant-δ checks used q=a² from the
   dust model. The repair supplies a potential argument and explicitly uses
   q=1 for the constant-cylinder-potential family, retaining q=a² for dust.
3. **Finite projection versus local support:** the original check compared a
   finite-mode derivative directly with πh(Y), as if finite projection retained
   exact spatial support. It does not. The repair compares the numerical
   derivative with the exact derivative of the same finite sum,

       sum_k c_k [t_* cos(kt_*)/(2k) − sin(kt_*)/(2k²)].

   The separate limit identity πh(Y) is reported as a convergence reference,
   not an exact finite-sum equality. The first corrected run failed the old
   comparison by approximately 1.37e−7; its original 1e−7 solver tolerance was
   retained and the reference was corrected to the actual finite-sum quantity.

The recovered control also reports the raw unperturbed target residual rather
than hiding it. At 96 modes it is approximately 1.60e−5: larger than the effect
of δ=−1e−4 in this sample, so that raw finite-sum value has the wrong sign.
The signed perturbation increment has the expected sign. This is an explicit
limitation of the finite projection, not numerical verification of exact past
agreement or of the sign at arbitrarily small mass. The exact proof supplies
those statements. Time refinement is checked at fixed cutoff separately
from the combined spectral/time probe; neither certifies the infinite tail.

This distinction is essential: a finite sum cannot certify exact zero on an
open past while remaining nonzero later. Exact past vanishing uses the
infinite-dimensional smooth Cauchy problem and finite propagation analytically.

## 3. Analytical checks, distinct from the numerical controls

### Constant rescaled potential

For g≥0 smooth, nonzero, supported strictly outside the closed cap of radius
τ<π, all perturbed solutions with auxiliary data (0,g) vanish on the strip's
chronological past P by finite propagation, independently of the zero-order
potential. Let h=Λ^−2g. The radial kernel

    G(r)=(π−r)/(4π² sin r)

has the fundamental singularity 1/(4πr), solves the homogeneous radial equation
away from the pole, is smooth at the antipode and has unit total integral.
It is therefore the resolvent kernel and h(Y)>0.

One normalization error in the unfinished NOTES must not be propagated: its
intermediate spectral projector coefficient is written k/(4π²), whereas the
correct coefficient is k/(2π²). Combined with the Fourier sine sum
Σ sin(kr)/k=(π−r)/2, the latter gives the displayed G. The NOTES' final G is
correct despite that intermediate factor error; the radial derivation and
unit-integral check independently fix the normalization.

At T=2π, differentiating the exact propagator gives ∂δSδ(T)|0=πΛ^−2 and
∂δCδ(T)|0=0. The sine subtraction identity then gives

    ∂δψδ(T−s,Y)|0 = πh(Y),       0<s≤τ.

Here Sδ(s)g(Y)=0 for all δ by finite propagation, and C0(s)h(Y)=h(Y) because
Λ²h=g=0 throughout the relevant ball. These support facts apply to full smooth
data, not each spectral projection. The positive derivative and zero
unperturbed value produce a nonzero target difference for every sufficiently
small nonzero δ. On dust this shift is physical potential δ/a², not ordinary
constant physical mass.

### Ordinary physical dust mass

Conformal covariance with φ=ψ/a converts mass m to λ=m² and q=a², not a^−2.
For q=(a_m²/4)(3/2−2cos t+(1/2)cos 2t), the first variation satisfies

    w(T)=integral_0^T q(u)S0(u)²g du.

The two minus signs are from the differentiated equation and
S0(T−u)=−S0(u). Direct trigonometric orthogonality yields weight
5πa_m²/16 for k=1 and 3πa_m²/(8k²) for k≥2. Thus

    w(T)=[(3πa_m²/8)Λ^−2−(πa_m²/16)Π0]g,
    K(r)=a_m²/(32π)[3(π−r)/sin r−1]>0.

The last pointwise inequality, not merely positive-semidefiniteness of an
operator, proves w(T,Y)>0 for g≥0. Since q extends smoothly through T, this
implies positivity at fixed interior times sufficiently near T. Select one
such target inside the massless late fixed interval first. Smooth parameter
dependence then gives ψ_m(x_*)=m²w(x_*)+o(m²)>0 for all sufficiently small m>0,
while all these solutions vanish exactly on P. The target never lies at the
excluded dust crunch; T is used solely in the auxiliary smooth equation.

Every smooth strip solution for these extendible smooth coefficients extends
uniquely from an interior compact Cauchy slice to the cylinder. Consequently
the auxiliary construction does not silently restrict the smooth strip class.
It supplies no physical continuation through a cosmological singularity.

## 4. Evidence and remaining gates

verification.json records the repaired finite-mode controls, exact solver
reference, independent midpoint weights, radial Green normalization, signs,
kernel positivity grid and the spectral/time-resolution probe. Read those
as checks of the displayed formulas, not as proof of all-solution uniqueness,
exact compact support or a general fixing classification.

The original massless fixing result is a stated dependency and was not
re-proved in this recovery. Prior-source and originality questions remain in
the separate source lane. This coordinator authored the original extension,
so completing a stopped referee checker cannot replace independent proof
review. No interacting, quantized, backreacting or observational theorem is
established. Exact loss of fixing does not entail an order-one measured change
or a conclusion about temporal ontology.
