# Explicit smooth initial cone data satisfying the scalar-collapse criterion

28 October 2026. Analytic construction from the source's radial constraints.
Candidate result for independent check. No novelty claim: the source already
states that collapse can begin far from trapped data. This construction makes
the zero-inner-data case explicit for the shared matching problem.

Use the normalized units R₁=1; all s and radii below are dimensionless in
this fixed length unit. Let χ be a nonzero smooth bump supported in (0,1),
and c=∫₀¹χ(t)²dt>0. For 0<ε<1/2 define

  f_ε(s)=χ((s−1)/ε)²/(εc),
  ψ(s)=sqrt(λ/(4πεc)) χ((s−1)/ε),  0<λ<1/4.

Here f_ε and ψ are zero outside (1,1+ε), and ∫ f_ε ds=1.
Let r(s) solve Christodoulou's initial-cone Raychaudhuri equation

  r″=−4πrψ²=−λ f_ε r,   r(0)=0, r′(0)=1.

Put h=r′. For s≤1, r=s, h=1, ψ=0. Thus the initial cone interior has
constant scalar and zero mass. While r>0 through the pulse, concavity gives
h≤1 and r≤s≤1+ε. Integration gives

  h(s)≥1−λ(1+ε)>0,  1≤s≤1+ε.

The estimate closes by continuation: a first zero of r or h cannot occur
under this positive lower bound. Therefore r≥1 there, and at s₂=1+ε:

  1−λ(1+ε)≤h₂≤1−λ,
  1+[1−λ(1+ε)]ε≤R₂=r(s₂)≤1+ε.

In particular δ₀=R₂−1 lies in (0,ε]. Equations(4.2c),(4.3) give

  underline h=−s/r,   m=(r−s h)/2.

Thus m₁=0 and

  η₀=2m₂/R₂=1−(1+ε)h₂/R₂
     ≥1−(1+ε)(1−λ)
     =λ−ε(1−λ).

Choose ε≤λ/[2(1−λ)] and E(ε)<λ/2, where
E(y)=y/(1+y)²[log(1/(2y))+5−y]. Such ε exist since E(ε)→0.
The source states E increasing on (0,1/2). Hence

  η₀≥λ/2>E(ε)≥E(δ₀),

so Theorem5.1 applies with a strict concentration margin.

After s₂, ψ=0, h=h₂>0 and r=R₂+h₂(s−s₂)→∞. Consequently the cone generators
are complete in the prescribed affine parameter, and the Hawking mass is
constant after the pulse: m=(R₂−s₂h₂)/2. From m′=λs f_ε r/2 and the pulse
bounds, λ/2≤m₂≤λ(1+ε)²/2. The initial Bondi mass is therefore finite and
positive. The initial cone is everywhere untrapped, since h>0 while
underline h<0. In fact 2m/r≤λ(1+ε)² on the pulse, decreases after it,
and is zero inside. Taking λ small and ε correspondingly smaller makes
the initial compactness arbitrarily small.

The remaining radial cone constraints are regular ODEs for r>0 and reduce
to the flat solution near the centre; source p354 describes their sequential
solution from ψ. The scalar itself is φ(s)=φ₀+∫₀ˢψ(t)dt, so is smooth and
constant both before and after the pulse, with possibly different constants.
This proves admissibility of smooth cone data for the forward-cone setup;
it does not prove any complete-past extension of that setup.

Example of strict parameter bounds (not a numerical evolution): λ=1/8,
ε=10⁻³. Then η₀≥0.124125, while E(δ₀)≤E(10⁻³)≈0.0112, and h₂≥0.874875.
The exact bump shape does not affect these inequalities.

Combined with Proposition4.1, the flat diamond persists on the centre up
to u=2 in this normalization. Theorem5.1 gives u_*≤2(1−2δ₀)<2. Thus any
u_b in (2(1−2δ₀),2) is a regular flat central event already beyond the
central vertex of the event horizon in the forward-cone development.
The width of this guaranteed interval is 4δ₀>0.

Gate still open: none of the above identifies the full past in a maximal
GH extension, nor proves a no-common-future pair at a selected exterior
point. Those are the separate extension and geometry tasks.
