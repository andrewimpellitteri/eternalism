# Exact determination, noisy records, and spectral cutoffs

27 October 2026. Coordinator diagnostic, submitted for independent review.
No manuscript integration or novelty claim. This is an elementary application
of classical regularity and finite-dimensional uniqueness, not a new inverse
problem theorem. It complements, rather than replaces, bounded-ambiguity/RESULT.md.

## 1. Explicit observation and solution contracts

Let M=(0,T)×S³, T=2π, with unit-cylinder equation

    ψ_tt + Λ²ψ = 0,       Λ²=−Δ_S³+1.

Use smooth real solutions. The conserved conformal data norm is

    N² = ||Λψ(t)||_2² + ||ψ_t(t)||_2².

Fix b=(π/3,Y), P=I_s^−(b) in this strip, and x_*=(11π/6,Y).
The manuscript's massless three-diamond result puts x_* in F_0(b): exact
agreement on P entails exact agreement at x_*. This diagnostic assumes that
reviewed classification; the construction below itself works at any target.

Define the particular record-error norm

    R_P(ψ) = [integral_P |ψ|² dt dV_S³]^(1/2).

This measures aggregate field error, not its derivatives or pointwise maximum.
It is a named mathematical observation model, not a model of an actual detector.

## 2. Bounded energy and small records do not control a point value

Let Z_k be the real L²-normalized degree-(k−1) zonal harmonic centered at Y.
The unit-S³ addition identity gives

    Z_k(Y)=k/sqrt(2π²),
    Z_k(r)=sin(kr)/(sqrt(2π²) sin r),     r=d(Y,X).

The endpoint values are smooth limits; these are smooth harmonics, not singular
functions. Different k are orthonormal. For each positive integer K put

    ψ_K(t,X)=sum_(k=K)^(2K−1) cos(k(t−t_*)) Z_k(X)/(k sqrt(K)).    (1)

Each member is a finite sum and hence a smooth exact solution. At every t,
orthogonality gives

    N(ψ_K)² = (1/K) sum_(k=K)^(2K−1) [cos²(k(t−t_*))+sin²(k(t−t_*))] = 1.

At the target, all the position phases align:

    ψ_K(x_*) = sqrt(K)/sqrt(2π²) → infinity.                       (2)

At every time, however,

    ||ψ_K(t)||_2² ≤ (1/K) sum_(k=K)^(2K−1) 1/k² ≤ 1/K².

Integrating over the full period yields the sharper exact identity

    ||ψ_K||_L²(M)² = (π/K) sum_(k=K)^(2K−1) 1/k² ≤ π/K²,          (3)

because each cosine squared integrates to π. Thus R_P(ψ_K)≤sqrt(π)/K→0,
even though (2) diverges. Comparing ψ_K with zero, both alternatives belong
to the unit conformal-energy ball. For every ε>0, the supremum of the target
point differences over this ball subject to R_P≤ε is infinite.

In particular there is no uniform error modulus ω(ε)→0 for this point
observable, record norm and solution class, even at an exactly fixed target.
The sequence does NOT vanish exactly on P. There is no contradiction with
the definition of F_0 or with uniqueness from exact records.

This failure already occurs with noisy records from the ENTIRE strip. It
therefore does not diagnose causal-horizon amplification, refocusing-specific
instability or an inability to reconstruct realistic finite-resolution data.
It is the familiar inadequacy of an H¹ energy bound to control point evaluation
in three spatial dimensions, displayed within the exact solution class.

## 3. Physical field and finite-resolution cautions

For dust g=a(t)²g_E, a(t)=(a_m/2)(1−cos t), write φ_K=ψ_K/a(t).
The physical point value at the fixed interior target is (2)/a(t_*), so also
diverges. If the chosen aggregate record norm instead uses physical volume,

    ||φ_K||_L²(P,dVol_g)² = integral_P a(t)² |ψ_K|² dt dV
                         ≤ a_m² π/K².

This statement is about that spacetime norm; it does not identify N with a
bounded physical dust energy, which can behave differently near the bang.

For any fixed spatial averaging profile χ∈L²(S³), at any time,

    |integral χ(X)ψ_K(t,X)dV| ≤ ||χ||_2/K → 0.                    (4)

The high-frequency construction therefore disappears under such a fixed
finite-resolution observable. Equation (4) does not prove a general stability
estimate from past records to averaged future records. The point counterexample
does not refute such an estimate either. A detector, stronger observation norm,
regularity assumption or ultraviolet restriction requires its own analysis.

As a positive comparison using full-strip records only, an arbitrary massless
solution with data (f,g) at zero satisfies

    ||ψ||_L²(M)² = π (||f||_2²+||Λ^−1 g||_2²),
    ||ψ(t)||_2² ≤ ||f||_2²+||Λ^−1g||_2².

Hence every fixed χ∈L² obeys

    |<χ,ψ(t)>| ≤ ||χ||_2 ||ψ||_L²(M)/sqrt(π).                    (5)

This has ALL-strip records as input. Replacing M by P in (5) is not justified
here. The inequality follows modewise by Cauchy–Schwarz on (cos kt,sin kt);
the period identity uses orthogonality in time for each spatial eigenmode.

## 4. A finite spectral cutoff changes exact fixing itself

Restrict the solution class instead to spatial modes 1≤k≤L for one finite L.
Each solution is a finite linear combination of trigonometric time functions
and spherical harmonics. These functions are real analytic on the connected
cylinder. A difference vanishing on a nonempty open region therefore vanishes
everywhere. In this restricted class,

    F_L(b)=M,

even where the unrestricted smooth-solution theory has unfixed events.
This conclusion is unique continuation for this finite analytic class, not a
claim that all smooth wave solutions are analytic or that all local field laws
have the same property. Numerical mode truncation cannot certify agreement
exactly on a whole open past while retaining a nonzero target difference.

For completeness the finite-dimensional record map also has a stability
constant, which may depend badly on L and P. Choose real orthonormal harmonics
Y_kj and coefficient vector v=(f_kj,g_kj/k). Its design functions are
cos(kt)Y_kj and sin(kt)Y_kj. The Gram matrix

    G_ab = integral_P design_a design_b dt dV

is positive definite by the analytic uniqueness just proved. At any target x,
let ℓ(x) be the vector of design values. Then

    |ψ(x)| ≤ ||ℓ(x)|| / sqrt(λ_min(G)) · R_P(ψ),
    ||ℓ(x)||² = sum_(k=1)^L k²/(2π²).                            (6)

No cutoff-uniform constant or realistic noise tolerance follows from (6).
Our high-frequency sequence evades each fixed L by moving to higher bands.
The choice of spectral cutoff is itself a global restriction on admissible
solutions; it must not be treated as a neutral implementation of the original
smooth local theory or an established physical ultraviolet law.

## 5. Paper-safe consequence and predecessor status

Exact law-relative fixing, stability under changes of the law with exact past
agreement, and stability under errors in observed records are three different
questions. The previous bounded-ambiguity estimate addresses the second. This
note shows why the third needs an explicit observation norm and observable;
it also shows that a finite truncation changes the first question's solution
class. None of these facts selects a temporal ontology.

The relevant predecessors are classical Sobolev regularity, spectral wave
evolution and real-analytic identity theorems. Selected original university
teaching text was read before this construction: Charles H. A. Curry, NTNU
TMA4220 (2017), “Some elements of Sobolev spaces,” definitions and “Inequalities
and embeddings.” It supplies context, not a proof of this exact S³ sequence.
The sequence, constants and finite-band argument above are self-contained.
No exhaustive literature audit or novelty clearance is claimed.

All statements here remain coordinator submissions pending independent review.
