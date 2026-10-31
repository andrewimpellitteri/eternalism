# Exact temporal support can be fragile while response stays close

30 October 2026. Coordinator analytic benchmark under the
[claim contract](RESPONSE_MEMORY_CONTRACT.md). The bounded native analytic
[audit](../response-memory-review/RESULT.md), its
[source-budget extension](../response-memory-review/REVIEW_SOURCE_BUDGETS.md),
and the [prior-result comparison](../response-memory-priorart/RESULT.md)
are integrated. These are internal checks, not external peer review.
This is linear response on fixed flat
spacetime, not the coupled fixed-energy interpolation theorem. Its kernel,
Bessel asymptotics and fading-memory framework are established inputs.
The deductions below carry no mathematical or ontological novelty claim.

## 1. Fix the physical comparison before defining an extent

In units c=1, use P_m=∂_t²−Δ+m² on 3+1 Minkowski spacetime, m≥0. An
ideal point source at rest has prescribed amplitude f(t); an ideal detector
at rest a distance r>0 away measures the classical scalar field. Select
the retarded source response, with no independently added homogeneous
field. The clocks are the pair's rest-frame proper clocks. This apparatus
supplies a physical time standard, not a preferred frame for the universe.

Changing m compares different field operators with the same apparatus and
input. It is not two solutions of one fixed operator with identical full
Cauchy data. Inputs are real bounded continuous functions on R with norm
||f||_∞. Compact smooth inputs form a useful subclass, with no common bound
on support duration, energy or derivatives. No fixed-energy conclusion is
drawn. Point-source singularities are excluded from the detector by r>0.

Write R_m f=h_m*f. The known retarded kernel, as a finite signed measure
in lag s, is

    h_m = δ_r/(4πr) + k_m(s) ds,
    k_m(s) = −1_{s≥r} m J_1(m√(s²−r²))/(4π√(s²−r²)).

The quotient has its continuous limiting value at s=r. For m=0,
k_0=0. AppendixA(A.1), printedp15, of Salnikov etal2021 supplies this
normalization. NIST DLMF10.7.3 and10.17.3 imply

    J_1(z)=z/2+O(z³) near zero,
    J_1(z)=√(2/(πz)) cos(z−3π/4)+O(z^(−3/2)) as z→+∞.

Thus C_*:=∫_0^∞ |J_1(z)|/z dz is finite and strictly positive. All norms
below use these bounded-continuous signals and the supremum output norm;
there is no point-evaluation convention for an L∞ equivalence class.

## 2. Exact lookback is an input/output property

For a causal response measure h supported in [0,∞), define

    H(h)=inf{T≥0 : supp h⊆[0,T]},  inf ∅=∞.

This is the least recent-history cutoff beyond which earlier input changes
cannot change the present output. It is not automatically the thickness
of a present: if h is a single delayed atom, only one past source time is
sampled, not every time in a filled interval.

For the point channel, H(h_0)=r, but H(h_m)=∞ for every m>0. Indeed for
s>r the Bessel factor is analytic and does not vanish on any final open
interval. Its nonzero large-argument oscillations give arbitrarily late
nonzero response. For each proposed finite cutoff choose a smooth source
bump, wholly older than it, on which k_m has one nonzero sign. Its output
at a suitable time is nonzero although its recent input is zero. This is
an exact counterexample to that cutoff; it does not require finite grids.

## 3. Uniformly small response error for every bounded history

Let D_r(m)=||R_m−R_0||_{∞→∞}. The light-cone atoms cancel. For a real
integrable kernel, convolution's supremum-norm operator norm equals its
L¹ norm. The upper bound is the integral triangle inequality. For the
lower bound, fix an output time, approximate the sign of the reversed
kernel on a large finite interval by bounded smooth inputs, and then
let the omitted L¹ tail tend to zero. Each approximant can have compact
support; their durations need not have a common bound.

For m>0 put z=m√(s²−r²). Then

    D_r(m) = (m/(4π)) ∫_0^∞ |J_1(z)|/√(z²+(mr)²) dz
           ≤ m C_*/(4π).

This bound is uniform in r>0 as an *absolute* gain bound. For each fixed
r, dominated convergence, dominated by |J_1(z)|/z, gives the sharp limit

    lim_{m↓0} D_r(m)/m = C_*/(4π) > 0.

Therefore the exact support jumps from bounded to unbounded while the
entire bounded-source response operator converges in norm. The estimate
holds uniformly in output time and in all admitted inputs, not only for
one pulse or one finite observation interval. It does not assert uniform
relative error if r also grows: ||R_0||=1/(4πr), so the relative bound
is C_*mr. Fixed apparatus scales are essential when saying mass is small.

For fixed r≤T<∞, restricting the difference kernel to lags [r,T] gives

    ||(R_m−R_0)_[r,T]|| = m²(T−r)/(8π) + O_{r,T}(m⁴).

This follows by expanding J_1(z)/z=1/2+O(z²), uniformly on that interval;
the tail kernel has one sign there for sufficiently small m. The O(m)
all-history norm therefore cannot be replaced by O(m²) merely because
every fixed finite lag window has the latter order. The classes of
permitted source durations differ. This is a controlled limit distinction,
not an observer-energy or practical-detection theorem.

## 3a. The sharp rate depends on the source budget

The preceding norm controls source amplitude without a duration budget.
The same kernel gives a more informative elementary hierarchy. Define
the difference response first on real compact smooth inputs, with
||f||_q≤1, and use the peak output norm. Let 1/q+1/p=1. For 1≤p<∞ put

    C_p = (∫_0^∞ (|J_1(z)|/z)^p dz)^(1/p).

These constants are finite: the integrand is bounded near zero and
O(z^(−3p/2)) at infinity. Hölder's inequality and its dual approximating
inputs give exactly ||R_m−R_0||_{q→∞}=||k_m||_p. The same substitution gives

    ||k_m||_p^p = m^(2p−1)/(4π)^p
                  ·∫_0^∞ |J_1(z)|^p z^(1−p)/√(z²+(mr)²) dz.

Dominating by (|J_1(z)|/z)^p therefore yields

    ||R_m−R_0||_{q→∞} ≤ C_p m^(1+1/q)/(4π),
    lim_{m↓0} ||R_m−R_0||_{q→∞}/m^(1+1/q)=C_p/(4π)

for fixed r and q>1, including q=∞ with p=1. For q=1, the exact result is

    ||R_m−R_0||_{1→∞}=||k_m||_∞=m²/(8π).

For the last equality, DLMF10.9.4 with ν=1 gives
J_1(z)=(z/π)∫_0^π cos(z cosθ) sin²θ dθ, hence |J_1(z)|≤z/2 for z≥0.
The cone-side limit attains the essential supremum. Compact smooth
inputs concentrated near that lag approach the L¹-budget norm; their
peak amplitudes and bandwidths are not uniformly bounded. For intermediate
q the usual Hölder extremizer can likewise be approximated with smooth
compact inputs. No numerical extremizer is assumed.

Thus a bounded-amplitude budget gives order m, a source L² budget gives
order m^(3/2), and a source L¹ budget gives order m², uniformly in output
time. These are mathematical budgets on prescribed input amplitude; L²
is **not identified with physical field energy**. The latter would require
a model of the source, its work and detector coupling.

The individual point-source response contains a delta term and need not
define a bounded map from L^q to peak output for finite q. The *difference*
has that common delta canceled and has the stated norm, initially on
smooth signals. A physical measurement model may additionally smear source
and detector in space or time. No bound on each individual output is
inferred from the difference bound. This hierarchy is another elementary
kernel-norm consequence, not a new uniform-mass PDE theorem or novelty claim.

## 3b. A physical energy upper budget, without equating it to an input norm

The source norm can be connected to a genuine field-energy bound in one
limited experiment. Let a,b be fixed smooth compact spatial weights with
disjoint supports, let f be compact smooth in time, and solve

    (∂_t²−Δ+m²)φ_m=f(t)a(x)

with zero Cauchy data before the source is switched on. Define the actual
field energy on the apparatus rest-frame slice by

    E_m(t)=(1/2)∫[(∂_tφ_m)²+|∇φ_m|²+m²φ_m²] dx.

The energy identity and Cauchy–Schwarz give

    E_m'(t)=f(t)∫ a ∂_tφ_m dx,
    √E_m(t)≤||a||_2 ||f||_1/√2.

The latter follows by applying the differential inequality first to
√(E_m+η), η>0, and then letting η↓0. Smooth finite-duration forcing and
finite propagation justify the spatial integration. It is uniform in
m≥0 and in output time, including after forcing stops.

For the smeared readout Y_m(t)=∫b(x)φ_m(t,x)dx, cancellation of the direct
kernel and |k_m(s)|≤m²/(8π) imply

    ||Y_m−Y_0||_∞ ≤ m² ||a||_1 ||b||_1 ||f||_1/(8π).

Thus imposing ||f||_1≤√(2E_max)/||a||_2, with a≠0, ensures both
E_m(t)≤E_max for all t and

    ||Y_m−Y_0||_∞ ≤ m²√(2E_max) ||a||_1||b||_1/(8π||a||_2).

This is a common *upper budget*, not equality of actual energies between
models and not the energy of the unmodeled forcing apparatus. The input
condition is sufficient for that budget, not necessary. Different masses
still mean different operators. No ADM mass, incoming Hawking mass,
detector noise threshold or gravitational backreaction is involved. The
unbounded support result for positive smeared weights still holds: an
arbitrarily old finite-duration pulse within the budget can have a nonzero,
arbitrarily small later effect. This gives a physical example of the
sharp-support/controlled-response distinction without a singular source.

## 4. A tolerance-dependent extent with a precise meaning

Define the truncation R_{h,T} by removing the part of h on (T,∞), keeping
the same recent input and the zero remote-input baseline. Its error is

    ||R_h−R_{h,T}|| = |h|((T,∞)),

where |h| is total variation. The error for two inputs of norm≤U which
agree on the recent T interval is at most 2U|h|((T,∞)); the factor 2
must not be lost by confusing uncertainty with truncation against zero.

For an absolute response-gain tolerance δ>0, define

    T_δ(h)=inf{T≥0 : |h|((T,∞))≤δ}.

For the massive point channel, T_δ is finite for every δ>0, despite
H=∞. Also if m C_*/(4π)≤δ, cutoff T=r already suffices. Thus a finite
response-based extent can be warranted at fixed accuracy even though
no exact hard cutoff exists.

This does not prove continuity of the minimizing T_δ under arbitrary
perturbations: atoms, plateaus and threshold choices can make that
minimizer discontinuous. What is stable here is the response-error
guarantee at the fixed reference cutoff. δ is specified by the protocol,
not supplied as a fundamental ontological constant.

## 5. The contrast survives ordinary spatial smearing

Let a,b be nonnegative smooth compact spatial source and detector weights
with disjoint supports, separation 0<r_min≤|x−y|≤r_max, and integrals
A,B>0. Use source f(t)a(x), detector ∫b(y)φ(t,y)dy, at rest in the
same laboratory. The response measure is

    h_m^{a,b}=∫ a(x)b(y) h_m^{|x−y|} dxdy.

For m=0 it is supported in [r_min,r_max]. Fubini and the point bound give

    ||R_m^{a,b}−R_0^{a,b}|| ≤ AB m C_*/(4π).

For fixed m>0, the Bessel asymptotic uniformly over the compact set of
separations gives, at sufficiently late lag s>r_max,

    k_m^{a,b}(s) = −AB √(2m/π)/(4π) s^(−3/2)
                    cos(ms−3π/4) + O_{m,a,b}(s^(−5/2)).

Along arbitrarily late peaks of the cosine the leading term is nonzero.
Thus the smeared massive response also has unbounded support. Positivity
and nonzero A,B prevent cancellation of this leading coefficient; this
assertion is not made for arbitrary signed or specially filtered weights.
No uniform-in-m claim is made for that late-time asymptotic remainder.

## 6. An explicit positive model of a filled response window

The preceding point delay is not itself a thick interval. A simple known
counterpoint is a transport channel of length L with speed c>0:

    q_t+c q_x=0,  0<x<L,  q(t,0)=f(t),
    y(t)=L^(−1)∫_0^L q(t,x)dx.

Use its boundary-driven solution q(t,x)=f(t−x/c), with outflow at L.
Equivalently start at a finite preparation time and wait L/c so that
the original interior data have left the channel. Then with τ=L/c,

    y(t)=τ^(−1)∫_0^τ f(t−s)ds.

The kernel is positive throughout (0,τ); its exact cutoff is τ, and every
smaller cutoff fails on an older compact smooth input bump. Its truncation
error is (1−T/τ)_+ and T_δ=(1−δ)τ for 0≤δ≤1. Geometry and transport
speed fix a genuine filled response window, rather than a chosen number
of oscillations. This is standard delay-line/transport mathematics,
not a newly discovered sustaining mechanism.

The full field q(t,·) is an instantaneous Markov state that encodes this
input history. Consequently instantaneous predictive sufficiency and an
extended physical response window coexist. Changing internal state
representation does not remove the measured response duration. Equally,
the duration is a property of this input/output protocol and boundary
configuration, not every observable of the channel.

## 7. Representation invariance is earned at a restricted level

If two finite response measures produce the same output for every compact
smooth input, testing at time zero shows that their difference annihilates
every reflected test function. They are the same distribution, hence the
same measure. Exact support and truncation error are therefore invariant
under internal realizations preserving the physical input, output, clock
and gain normalization. This is established input/output thinking, already
explicit in Boyd–Chua §8.2, not a new ontological equivalence theorem.

There is also a useful standard boundary case. A finite-dimensional LTI
realization has h(s)=Ce^{As}B for s>0. If this function vanishes past a
finite cutoff, analyticity makes it vanish identically. A nonzero stable
dynamic response of this form therefore has no exact finite horizon,
despite its finite instantaneous state. A feedthrough atom at zero is a
different, memoryless term. Distributed transport evades this observation
by its infinite-dimensional field state.

The equal-response requirement does not identify two complete physical
ontologies. Unobserved carriers or different internal organization may
remain physically real. Changing the measured variable or allowed source
class changes the question. No representation change is called gauge.

## 8. Philosophical payoff and the remaining positive task

This benchmark improves the question “what duration does the dynamics
select?” Physical apparatus and transport can pick a temporal extent
without a preselected metaphysical present. That extent can be invariant
under internal state descriptions. A sharp extent can nevertheless fail
under small physical changes while a fixed-accuracy response description
remains uniformly reliable.

For a proposal identifying a present with response support, this is an
exact robustness challenge: why should a tiny mass tail change exhaustive
concrete existence from a finite region to an unbounded past? A defender
can accept the sharp change, use another constitutive criterion, or give
a scale-relative ontology. The result excludes none of those by itself.
It also gives no argument that the full *future* must be concrete.

The constructive continuation is to identify a specific organizing
transport or feedback activity that makes the system one, then test
whether its temporal extent has the asserted constitutive role. Response
memory alone also belongs to systems that are not plausible composite
unities. It cannot silently replace that criterion.

The proper same-physics rival can grant the channel, carriers, organization
and response duration while treating all its occurrences as concrete. A
process-based account has earned an ontology preference only if its
constitutive explanation adds something this rival cannot equally supply.
Conversely, reconstructing the activity from an instantaneous state does
not prove that this state constitutes it. Neither inference is licensed
by the benchmark. The new research path is a concrete, falsifiable bridge
test, not another name for a present or a completed ontology.
