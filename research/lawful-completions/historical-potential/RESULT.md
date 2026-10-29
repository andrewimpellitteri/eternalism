# Historical causal potential in conformal slabs

**Disposition: the exact finite-slab formula checks out, and its domain restriction matters.** For a flat conformal slab (M=(a,B)\times\mathbb R^d), (d\ge1), with (a,B) finite, let

\[
D(s)=\{s\}\cup\{x:\not(s\prec x),\ \exists z\ (s\prec z\land x\prec z)\},\qquad H(s)=\bigcup_{r\le s}D(r),
\]

where (\prec) means distinct causal precedence, including null pairs. For (s=(\sigma,0)), (x=(\xi,z)), and (d_x=|z|>|\xi-\sigma|) (the spacelike case),

\[
x\in H(s)\quad\Longleftrightarrow\quad d_x<2(B-a)+\sigma-\xi. \tag{1}
\]

The proof uses only the causal structure, so any smooth positive conformal factor leaves it unchanged. Past/equality points (x\le s) belong to (D(s)\subset H(s)); strict causal-future points (s\prec x), including null-future points, belong to no (D(r)) for (r\le s). Thus (1) classifies the remaining spacelike points.

## Counterexample first: finite slab does not recover bow-tie

Take (a=0,B=1), (s=(1/2,0)), and (x=(1/2,z)) with (|z|=3). The pair is spacelike and lies in the bow-tie realm (D_{BT}(s)=M\setminus(J^+(s)\setminus\{s\})), but the right side of (1) is (2), so (x\notin H(s)). This is a strict finite-horizon gap, not an endpoint convention: equality at the threshold is excluded.

By contrast, with an infinite conformal past (a=-\infty) and finite (B), every finite spacelike separation satisfies the condition for some sufficiently early finite ρ. Hence every spacelike point belongs to (H(s)), and together with the past/equality and strict-future cases this gives (H(s)=D_{BT}(s)). In particular, the flat-slicing de Sitter patch with conformal interval ((-\infty,0)) is **not** a counterexample to the historical repair. A finite-slab counterexample must not be promoted to a universal horizon refutation.

## Proof of the exact slab formula

For (r=(\rho,y)\le s),

\[
a<\rho\le\sigma,\qquad |y|\le R:=\sigma-\rho.
\]

For two events with times \(\rho,\xi\) and spatial separation \(\ell:=|z-y|\), the infimum of the time coordinates of their common-future points is

\[
T_* = \max\left\{\rho,\xi,\frac{\rho+\xi+\ell}{2}\right\}.
\]

This follows by minimizing \(\max\{\rho+|w-y|,\xi+|w-z|\}\) over spatial locations \(w\); the minimizer lies on the segment from \(y\) to \(z\). Since both events lie below \(B\), a common strict future inside the open slab exists exactly when \(T_*<B\). Equivalently,

\[
\ell<2B-\xi-\rho. \tag{2}
\]

For spacelike-related \(r,x\), the average term realizes \(T_*\), giving the familiar sum-of-remaining-conformal-times criterion. If they are timelike or null related, the later endpoint time dominates and (2) is automatic because both times are strictly below \(B\). This distinction matters in the necessity argument, where \(r,x\) need not be spacelike.

**Necessity.** If (x\in D(r)) for some (r\le s), then (x\ne r) in the spacelike-((s,x)) case, and (2) holds. The triangle inequality gives

\[
|z|\le |z-y|+|y|<2B-\xi-\rho+\sigma-\rho
=2B+\sigma-\xi-2\rho<2(B-a)+\sigma-\xi,
\]

using ρ>a. This proves the strict bound in (1).

**Sufficiency.** Suppose (d_x>|\xi-\sigma|) and the right side of (1) is strict. Choose (\rho\in(a,\sigma]\) sufficiently close to (a) that

\[
d_x<2B+\sigma-\xi-2\rho.
\]

As (y) ranges over (|y|\le R=\sigma-\rho), the possible values of ℓ=|z-y| fill the interval

\[
[\max(0,d_x-R),\ d_x+R].
\]

We can choose such an λ satisfying both

\[
|\xi-\rho|<\ell<2B-\xi-\rho. \tag{3}
\]

For clarity, the reachable interval's left endpoint is below the upper bound in (3): if it is positive this is precisely the chosen inequality for ρ; if it is zero, the upper bound is positive since ξ,ρ<B. Its right endpoint exceeds the lower bound: when ξ≥ρ this follows from (d_x>\xi-\sigma); when ξ<ρ, it follows from (d_x>\sigma-\xi\ge2\rho-\xi-\sigma). These strict overlaps imply the intervals intersect. Choose (y) attaining the selected λ, along the ray toward (z). The first inequality in (3) makes (r,x) spacelike, so (r\not\prec x); the second gives a common strict future by (2). Thus (x\in D(r)\subset H(s)).

The strict endpoints matter twice: equality in the upper bound would place the only common-future limit at the excluded boundary (B), while equality in the lower bound would make (r,x) null-related and therefore violate the condition (r\not\prec x).

## Fixed dust-Λ model and checks

The coordinator's exact model is a flat FLRW solution on (t>0):

\[
g=-dt^2+A(t)^2d\mathbf x^2,\quad A(t)=C\sinh(3ht/2)^{2/3},\quad
\rho(t)=\frac{3h^2}{8\pi G}\operatorname{csch}^2(3ht/2),\quad
\Lambda=3h^2>0.
\]

Let (U=\partial_t), (H=\dot A/A), and (x=3ht/2). Direct substitution gives

\[
H=h\coth x,\qquad H^2=h^2+h^2\operatorname{csch}^2x
=\frac{8\pi G}{3}\rho+\frac\Lambda3,
\]

\[
\dot H=-\frac{3h^2}{2}\operatorname{csch}^2x=-4\pi G\rho,
\qquad \dot\rho+3H\rho=0.
\]

These are the flat Friedmann equations and dust conservation for fixed positive Λ; (U) is geodesic and ρ>0. This is pressureless dust+Λ, distinct from the scalar-field scattering model.

Near the bang and at late times,

\[
A(t)\sim C(3ht/2)^{2/3},\quad \rho(t)\sim\frac1{6\pi Gt^2}\quad(t\downarrow0),
\]

\[
A(t)\sim C2^{-2/3}e^{ht},\quad \rho(t)\sim\frac{3h^2}{2\pi G}e^{-3ht}\quad(t\to\infty).
\]

Thus (d\eta=dt/A(t)) is integrable at both endpoints and the conformal interval is ((0,L)) with (0<L<\infty). More explicitly,

\[
L=\frac{2^{2/3}}{3hC}\,\mathrm B(1/3,1/3),
\]

where Β is the Euler beta function. The near-endpoint conformal asymptotics are η proportional to (t^{1/3}) at the bang and (L-\eta\sim2^{2/3}(Ch)^{-1}e^{-ht}) at late times.

Applying (1), (a=0,B=L), choose ξ=σ=L/2 and (|z|=3L). Both events are regular interior events; they are spacelike, but (3L\not<2L), so (x\notin H(s)) while (x\in D_{BT}(s)). At (|z|=3L/2), the point is absent from instantaneous (D(s)), which requires (|z|<L), but present in (H(s)), which requires (|z|<2L). This verifies both non-recovery of bow-tie and genuine enlargement over instantaneous potential in one exact fixed-matter GR model.

No observational parameter fitting, source priority claim, ontological conclusion, or claim about the location/fusion clause is made. The construction establishes a difference between one explicit point-level causal-potential rule and bow-tie existence, conditional on accepting that rule as the intended formalization.
