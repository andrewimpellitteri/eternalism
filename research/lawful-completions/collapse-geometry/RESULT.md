# Collapse geometry lane: exact source result and construction audit

28 October 2026. Bounded source audit of D. Christodoulou, “The Formation of Black Holes and Singularities in Spherically Symmetric Gravitational Collapse,” *Communications on Pure and Applied Mathematics* 44 (1991), 339–373, DOI 10.1002/cpa.3160440305. The supplied PDF is the primary source; its SHA-256 is `64c3a30309aca30d59e87ee66c2ab098b3966a46036eede0ef75c7600e4e5978`.

## Read depth and scope

The paper's main-text prose was text-extracted throughout. The field equations and source coordinates in §§2–4 (pp. 340–356), Proposition 4.1 and its proof (§4, pp. 356–357), Theorem 5.1(a)–(j) and its proof (§5, pp. 363–372), were selected for full-text audit. Page images for printed pp. 356–357, 363–364 and 372 were inspected to check formulas and Figure 1 where extraction was lossy. Printed pp. 369–371 were checked against the available extraction. This does not audit every derivation, cited existence theorem, or the author's earlier global results [1]–[4]. No result below extends the paper's future-of-the-initial-cone spacetime to a maximal globally hyperbolic development.

## Exact theorem and flat-centre corollary

The model is the spherically symmetric Einstein–massless-minimally-coupled-real-scalar system, `R_ab=8π ∂_aφ ∂_bφ`, `□_gφ=0` (p. 339, (1.1c–d)). The centre Γ is a timelike geodesic parametrized by proper time `u`; the initial outgoing cone is `C⁺(0)`. Its affine generator parameter `s` is normalized by `s=0` at Γ and `Ds=1` (p. 340, §2). The paper restricts the spacetime under study to the future of this initial cone (p. 356). These `u,s` are not Vaidya advanced time.

For `R₁=r₁,₀<R₂=r₂,₀`, Christodoulou defines `δ₀=R₂/R₁−1∈(0,1/2)`, `η₀=2(m₂,₀−m₁,₀)/R₂`, and

`E(y)= y/(1+y)² [log(1/(2y))+5−y]`.

The hypothesis `η₀≥E(δ₀)` gives a marginal sphere on `C₂⁻∩C⁺(u*)`. Theorem 5.1(b)–(e) states `r₂*≥3δ₀R₂/(1+δ₀)`, `m₂*=r₂*/2`, `r₁*≥2δ₀R₁`, `u*≤2(1−2δ₀)R₁`, and an event horizon no later than `C⁺(u*)` with final Bondi mass at least `m₂*>0` (printed pp. 363–364). Parts (g),(j) state that every later outgoing cone intersects the singular boundary at zero radius, that the singular boundary is a future boundary, and that it is strictly spacelike away from its central singular set (p. 364). The argument for (g) uses negative outgoing expansion and gives a finite *affine* distance bound along each affected outgoing cone (pp. 369–370, especially (5.10)–(5.11)); it is not a bound on an incoming coordinate.

Now take zero scalar derivative on the initial cone interior up to `S₁,₀`, with regular centre and constant scalar there. Proposition 4.1 says zero mass there is equivalent to a flat, constant-scalar domain of dependence (pp. 356–357). In its flat normalization `r=s` and the inward null boundary from radius `R₁` reaches Γ at proper time `2R₁`. Thus, conditional on admissible smooth cone data satisfying the annular concentration hypothesis, every

`u_b ∈ (2(1−2δ₀)R₁, 2R₁)`

marks a regular event in that flat region strictly later than the central vertex of the event horizon and strictly before the inner incoming boundary arrives. The interval has width `4δ₀R₁`. This is a statement in the paper's forward-cone development. It does not establish that the event's entire past remains flat in a larger maximal development.

## Independent audit of the smooth bump cone data

I checked `coordinator/SMOOTH_CONE_DATA.md` against the source's cone equations and mass identities. Its estimates are correct, with the construction interpreted in the stated normalization `R₁=1` and on the initial cone only.

Let `χ∈C∞_c((0,1))` be nonzero, `c=∫χ²>0`, `0<λ<1/4`, and `fε(s)=χ((s−1)/ε)²/(εc)`. Then `∫fε ds=1`, and the proposed `ψε` satisfies `4πψε²=λfε` exactly. Christodoulou's equation (3.1e)/(4.1c) is `r''=−4πrψ²`; hence this data give `r''=−λfεr`, `r(0)=0`, `r'(0)=1`. Since the pulse vanishes for `s≤1`, `r=s`, `h=r'=1`, and `φ` is constant there.

On `[1,1+ε]`, as long as `r>0`, concavity gives `h≤1` and `r≤s≤1+ε`. Integrating `h'=-λfεr` yields `h(s)≥1−λ(1+ε)>0`. This lower bound and `r(1)=1` close the continuation argument: neither `h` nor `r` can first reach zero inside the pulse. Integrating once more gives

`1−λ(1+ε)≤h₂≤1−λ`, and `1+ε[1−λ(1+ε)]≤R₂=r(1+ε)≤1+ε`.

Thus `0<δ₀=R₂−1≤ε`. From (4.2c),(4.3), `h̲=−s/r` and `m=(r−sh)/2`; therefore `m₁=0` and `η₀=1−(1+ε)h₂/R₂`. Using `R₂≥1` and `h₂≤1−λ` gives `η₀≥λ−ε(1−λ)`. For `ε≤λ/[2(1−λ)]`, this is at least `λ/2`. Since the source states `E` is increasing on `(0,1/2)` and `E(ε)→0`, one can choose `ε` also small enough that `E(ε)<λ/2`; then `η₀≥λ/2>E(ε)≥E(δ₀)`, as required. For the supplied example `λ=1/8`, `ε=10⁻³`, the displayed lower bound is `0.124125`; direct substitution gives `E(10⁻³)≈0.0112`.

Outside the pulse, `ψ=0`, so `h=h₂>0` and `r=R₂+h₂(s−s₂)→∞`; the cone is complete in the prescribed affine parameter. The mass identity differentiates to `m'=λsfεr/2` on the pulse and `m'=0` outside. Thus `λ/2≤m₂≤λ(1+ε)²/2`, and the initial Bondi mass is finite and positive. The initial cone is untrapped: `h>0` and `h̲=−s/r<0`. The bounds also give `2m/r≤λ(1+ε)²` on the pulse, with this ratio decreasing after it. Because `χ` is supported away from both pulse endpoints, `ψ` and its derivatives vanish in neighborhoods there; `φ=φ₀+∫ψ` is smooth and constant before and after the pulse (the two constants may differ). The source p. 354 says the remaining radial constraints are then solved successively from `ψ`; the coordinator's regular-ODE claim is consistent with the smooth pulse and flat neighborhood of the centre. I did not independently solve those remaining equations or audit their full evolution theory.

This validates the annular data estimate and the strict flat-centre interval at the characteristic-data level. It does not supply a complete past, a Cauchy-data realization, or an entire-`I⁻(b)` matching theorem.

## Causal-separation attempt and exact missing assertion

Theorem 5.1(g),(j) and their proof do not imply the requested pairwise common-future exclusion. In (g), the paper bounds affine distance on outgoing generators after negative expansion is established (pp. 369–370). In (j), it rules out past intersections with the singular boundary and proves strict spacelikeness locally off the central singular set; its proof compares nearby intersections with incoming hypersurfaces and integrates equation (4.7) (pp. 370–371). Figure 1 (p. 372) is a causal sketch. None of these statements gives a finite global range in the incoming label `v`, nor orders a chosen exterior point against the entire future `J⁺(b)`.

The exact additional assertion needed for this route is a **finite incoming-coordinate causal barrier** in a specified continuation: in a regular double-null chart, prove a graph/barrier description of the relevant portion of the singular boundary with finite incoming-coordinate values, and prove that for a selected exterior event `x` its future is cut off by that boundary before it can intersect `J⁺(b)`. This must yield the actual pairwise statement `J⁺(x)∩J⁺(b)=∅`, including exclusion of every alternate future route. A bound on affine `s` alone cannot furnish a bound on the incoming optical label `v`, since converting between them requires control of the metric coefficient/coordinate relation along the relevant region. Likewise, local strict spacelikeness of `B\B₀` does not supply that global comparison. I found no such estimate or barrier in the audited clauses and proof. This identifies the missing assertion; it is not a counterexample showing that no such barrier holds in the constructed solution.

**Lane verdict: PASS** for the bounded analytic audit of the smooth initial-cone data and the resulting flat-centre timing corollary, using Christodoulou's stated characteristic equations and constraint-solving prescription. The estimates and concentration condition close; this PASS does not certify an independent solution of all remaining constraints or a global evolution theorem. **Causal-separation barrier: UNPROVED.** The flat result is confined to the forward-cone development, and the full-past/maximal-development gate remains open.

## Source record

See the lane `sources.jsonl` for the primary source and exact access limits.
