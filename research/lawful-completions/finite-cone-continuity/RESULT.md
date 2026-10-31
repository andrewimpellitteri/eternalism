# Finite-cone continuous dependence: the missing gate-1 lemma for the degree route

29 October 2026. Worker lane `lawful-finite-cone-continuity`.

**Disposition.** Gate 1 of `coordinator/DEGREE_ROUTE.md` (continuity of each
finite-cone readout map `H_n` on the parameter ball) is **closed at the reduced
(1+1) solution level by a proved difference estimate**, conditional only on
(i) the printed Luk–Oh–Yang (LOY) results being correct — statements checked at
full-text depth this session, selected proofs re-derived — and (ii) the
coordinator's data-family hypotheses (H1) below, which `FINITE_CONTROL.md`
already arranges. No differentiable, continuous, or even unique global
scattering selection is used or asserted. Four-dimensional axis regularity is
**not** addressed and remains open per `regularity/RESULT.md`.

The primary source states local well-posedness **without proof and without
continuous dependence**: arXiv:1605.03893v1, §2.1 (after (2.5)): *"This problem
is locally well-posed for C^k data (k≥1) … there exists a unique C^k solution …
We omit the proof, which is a routine iteration argument."* Uniqueness alone is
not continuous dependence, so the estimate below is genuinely the missing step,
not a restatement.

---

## 1. Setting and standing hypotheses

**Source system.** (SSESF) in double-null gauge as in LOY §2.1–2.2: unknowns
`(r, φ, m)` on `Q = {(u,v): v ≥ u}`, axis `Γ = {u=v}`, `λ = ∂_v r`,
`ν = ∂_u r`, `μ = 2m/r`, `ϑ := λ⁻¹∂_v(rφ)`, `ϖ := ν⁻¹∂_u(rφ)`. Axis conditions
(2.1)–(2.3): `r = m = 0` on `Γ` and `(∂_v+∂_u)^ℓ r = (∂_v+∂_u)^ℓ (rφ) = 0` there,
which imply the exact axis identities (used repeatedly):

  (A1) `ν = −λ` on `Γ`;  (A2) `μ = 0` on `Γ`;
  (A3) `ϑ = φ` on `Γ`  (since `∂_v(rφ) = λφ + r∂_vφ` and `r = 0`);
  (A4) `χ := ϑ − φ = 0` on `Γ`, where `χ := r λ⁻¹∂_v φ` by (2.23).

Data on the cone `C_{u₀}`: gauge `λ = 1/2` (2.5), scalar data
`ϑ|_{C_{u₀}} = Φ` (2.4), `r(u₀,u₀) = m(u₀,u₀) = 0`. For `ε` below LOY's
smallness `ε₁(γ)` (independent of `u₀`, Remark 1.2), Theorem 1.1 gives a unique
global `C¹` solution on `Q_{[u₀,∞)}`; for `C²` data the persistence sentence
before Proposition 3.18 makes it `C²`, and all §3 estimates then hold
**unconditionally** on `Q_{[u₀,∞)}` (§3.5 closure paragraph: the solution
"exists globally … and satisfies the bootstrapped bounds (3.1)–(3.3) as well as
the estimates derived in this section").

**Profile class (H1).** A compact family `𝔽 = {Φ_{ε,x} : x ∈ B̄_ρ ⊂ R^N}` with:

1. Each `Φ ∈ 𝔽` is smooth, supported in a **common** interval `[A₁,B₁]`, and
   satisfies LOY's data hypotheses with a **common** smallness parameter
   `ε̃ ≤ min(ε₁(γ), ε₂(γ))`: the integral condition (1.7) and
   `|Φ| + |Φ′| ≤ ε̃`, and `Ã := sup_{𝔽} sup_v |Φ″| < ∞` (condition (1.20) asks
   only finiteness; footnote 11: `ε` is independent of it).
2. `x ↦ Φ_{ε,x}` is `C^∞` into `C^k(ℝ)` for every `k`, with
   `‖Φ_{ε,x} − Φ_{ε,y}‖_{C⁰} ≤ L₀ |x − y|` on the ball.

`FINITE_CONTROL.md`'s family `ε(Σ_k x_k F_k + β(x)G)` satisfies (H1): common
support, `β` smooth and bounded away from `0` on the closed ball, amplitude
`≤ C₀ ε` for a fixed class constant `C₀` (this is the "replace ε by C₀ε"
renormalization noted in `CUBIC_TRACE.md`), so `L₀ = C(N, F_k, G, β, ρ)`.

Fix `u₀ = u_n` (cone n), a launch event `b = (t_b, t_b)` with `t_b > u₀`, a
readout window `T_j ∈ (0, T_max]`, and a coordinate cutoff
`t* := t_b + 2T_max + 1`. Write `T_n := t* − u₀` (triangle size; grows with n).

**Standing class bounds.** For every `x ∈ B̄_ρ`, the solution `S_x` obeys, with
constants depending only on `γ` and `(ε̃, Ã)` — **uniformly in `u₀`** (all
printed in LOY, §3–§4; locators in §7):

  (B1) geometry: `λ ∈ (1/3, 1/2]`, `ν ∈ (−2/3, −1/6)`, `1−μ ≥ 1/2` (3.1),
       `(1/3)(v−u) ≤ r ≤ (1/2)(v−u)` (3.5), `λ ≥ ½e^{−Cε̃²}` (3.25),
       `−ν ∈ [½e^{−Cε̃²}, ½e^{Cε̃²}]` (3.27);
  (B2) kernels: `|K| ≤ Cε̃² r₊^{−1−γ}` pointwise (Lemma 3.7 (3.24)), where
       `K := 2mν/((1−μ)r²)`, `κ := −K ≥ 0`;
  (B3) scalar: `|ϑ| ≤ C(|Φ(v)| + ε̃r₊^{−γ}) ≤ Cε̃` (3.10),
       `|λ⁻¹∂_vφ| ≤ Cε̃` (3.12),
       `|g| ≤ Cε̃` for `g := (λ⁻¹∂_v)²(rφ)` (3.32);
  (B4) mass: `m ≤ Cε̃²min{r³, r₊^{1−γ}}` (3.16),
       `m/r^k ≤ Cε̃²r₊^{−k+1−γ}`, `0 ≤ k ≤ 3` (3.17), so
       `q := 2m/r² ≤ Cε̃²`;
  (B5) transport identities: `∂_u ϑ = κχ` (2.6), `∂_u log λ = −κ` (2.8),
       `∫_{u₁}^{u₂} κ(u′,v)du′ = log(λ(u₁,v)/λ(u₂,v)) ≤ log(3/2)` (3.9),
       `2m(u,v) = ∫_u^v (1−μ)χ²λ dv′` (2.10 + (2.23)),
       `log((−ν)/(1−μ))(u,v) = log λ(u,u) + ∫_u^v χ²λ/r dv′` (3.28, using (A1)–(A2)).

Only (B1)–(B5) are used below; every item is a printed locator.

## 2. Main result

**Lemma 1 (cone traces are Lipschitz in the profile).** Under (H1), for
`x, y ∈ B̄_ρ` the cone traces obey, on `[u₀, ∞)`:

  `|Δϑ|(u₀,v) = |Φ_{ε,x}(v) − Φ_{ε,y}(v)| ≤ ‖ΔΦ‖_∞`,
  `Δλ(u₀,v) = Δr(u₀,v) = 0`,
  `|Δφ|, |Δm|, |Δν|, |Δμ|, |Δχ|, |Δq|(u₀,v) ≤ C_{u₀} ‖ΔΦ‖_∞`,

where `Δf := f_x − f_y`, `‖ΔΦ‖_∞ := ‖Φ_{ε,x} − Φ_{ε,y}‖_{C⁰([A₁,B₁])}`, and
`C_{u₀}` also depends on `(A₁, B₁, ε̃, γ)`.

*Proof.* On `C_{u₀}`: `λ = 1/2`, `r = (v−u₀)/2`, and by (2.17)
`φ(u₀,v) = ∫_{u₀}^v Φ / (v−u₀)`, so `|Δφ| ≤ ‖ΔΦ‖_∞`. With `f := Φ − φ` (so
`λ⁻¹∂_vφ = 2f/(v−u₀)` on the cone), (2.10) gives
`∂_v m = ¼(1−μ)f²` and (2.12) gives
`∂_v log((−ν)/(1−μ)) = f²/(v−u₀)`, both started from the flat vertex values
`(−ν)/(1−μ)(u₀,u₀) = 1/2`, `m(u₀,u₀) = 0`. Since
`|f| ≤ min{2ε̃, ‖Φ′‖(v−u₀)}` (the second bound from `Φ(v) − avg`), the pair
`(m, log((−ν)/(1−μ)))` is a 1D transport with forcing Lipschitz in `Φ` and
integrable coefficient (`f²/(v−u₀) ≤ min{4ε̃²/(v−u₀), ‖Φ′‖²(v−u₀)}`); a 1D
Grönwall argument gives `|Δm| + |Δlog((−ν)/(1−μ))| ≤ C_{u₀}‖ΔΦ‖_∞`, and
`|Δν| ≤ (−ν)̄(1−μ)⁻¹(|Δlog((−ν)/(1−μ))|) ≤ C_{u₀}‖ΔΦ‖_∞`;
`|Δμ| ≤ 2|Δm|/r + 2m|Δr|/r²` with `Δr = 0` gives the rest. ∎

**Theorem 2 (finite-cone continuous dependence; gate 1).** Under (H1), fix
cone vertex `u₀` and cutoff `t*`. Then for all `x, y ∈ B̄_ρ`, on the closed
readout triangle `D_n := {(u,v) ∈ Q : u₀ ≤ u ≤ v ≤ t*}` (axis included):

  (2.1) `sup_{D_n} ( |Δϑ| + |Δλ| + |Δφ| + |Δr| + |Δq| + |Δν| + |Δμ| )
        ≤ C_n ‖ΔΦ‖_∞`,

  (2.2) `sup_{t ∈ [u₀,t*]} |φ_x(t,t) − φ_y(t,t)| + |λ_x(t,t) − λ_y(t,t)|
        ≤ C_n ‖ΔΦ‖_∞`,

where `C_n = C(γ, ε̃, Ã, T_n, B₁ − u₀)` and `‖ΔΦ‖_∞ ≤ L₀|x−y|`. In particular
each parameter map below is Lipschitz, hence continuous, on `B̄_ρ`:

  1. `x ↦ (φ_x, ∂_v(r_xφ_x), ∂_u(r_xφ_x), r_x, m_x) ∈ C⁰(D_n)`;
  2. the **proper-time clock** `τ_x(t) := ∫_{t_b}^t 2λ_x(s,s)ds` (for
     `t ∈ [t_b, t*]`; `dτ_x/dt = 2λ_x(t,t) ∈ [1−Cε̃², 1]` by (A2), (A3)-region
     flatness and (B1)), whose inverse `t_x(T)` exists on `[0, τ_x(t*)]` and
     satisfies `|t_x(T) − t_y(T)| ≤ C_n T_max ‖ΔΦ‖_∞`;
  3. the **readout map**
     `H_n(x) := ( φ_x(t_x(T_1;x), t_x(T_1;x)), …, φ_x(t_x(T_N;x), t_x(T_N;x)) )`
     with `|H_n(x) − H_n(y)| ≤ C_n ‖x − y‖`.

Moreover, by (A3) the readings are axis traces: `φ_x(t,t) = ϑ_x(t,t)` exactly,
and `d/dt[ϑ_x(t,t)] = λ_x(t,t) g_x(t,t)` with `|g| ≤ Cε̃` (B3), since
`∂_u ϑ = κχ` vanishes on `Γ` by (A4).

**Constants.** `C_n` is allowed to depend on the cone n through `T_n` and
`B₁ − u₀`. For the degree argument **only per-n continuity is needed**, so this
n-dependence is harmless; nothing below asserts continuity uniform in n. The
separately required **uniform** remainder `sup_{n,x}|ε⁻¹H_n(x) − x| ≤ Cε²`
is not re-proved here; it comes from LOY §4's uniform estimates as recorded in
`CUBIC_TRACE.md` (see §5).

## 3. Proof of Theorem 2

Fix two parameters `x, y`, write `Δ` for differences and `S₁ = S_x`,
`S₂ = S_y`. All quantitative input is (B1)–(B5) plus Lemma 1.

**Step 1 (Volterra system for the differences).** On `D_n`, integrate (B5)
along `{u′ : u₀ ≤ u′ → u}` at fixed `v` (the integrands extend continuously to
an axis endpoint because `κ(t,t) = 0` — `m/r² ≤ Cε̃²r₊^{−1−γ}`·(decay (3.17)) —
and `χ(t,t) = 0` by (A4)):

  `Δϑ(u,v) = ΔΦ(v) + ∫_{u₀}^u [κ₁Δχ + Δκ·χ₂](u′,v) du′`,   (3.1)
  `Δlog λ(u,v) = −∫_{u₀}^u Δκ(u′,v) du′`,                  (3.2)

using `Δϑ(u₀,v) = ΔΦ(v)`, `Δλ(u₀,v) = 0`, and
`ϑ_i(u,v) = Φ_i(v) + ∫ κ_iχ_i`, `log λ_i(u,v) = −log 2 − ∫κ_i`.

**Step 2 (the remaining unknowns from averaging identities).** For each
solution, with `f′ := (1−μ)χ²λ`:

  `φ(u,v) = (1/r)∫_u^v ϑλ dv′`                (2.17), `φ = ϑ` on `Γ` (A3);
  `r(u,v) = ∫_u^v λ dv′`                      (r(u,u) = 0);
  `q(u,v) = (1/r²)∫_u^v f′ dv′`               (2.10 + (2.23), `m(u,u) = 0`);
  `log((−ν)/(1−μ))(u,v) = log λ(u,u) + ∫_u^v χ²λ/r dv′`   (3.28);
  `μ = qr`,  `κ = q·(−ν)/(1−μ)`,  `χ = ϑ − φ`.

**Step 3 (causal-past sup and Grönwall).** Define, for `(u,v) ∈ D_n`,

  `W(u,v) := sup { |Δϑ|+|Δλ|+|Δφ|+|Δr|+|Δq|+|Δν|+|Δμ|+|Δχ| (u′,v′) :
                   (u′,v′) ∈ T(u,v) }`,

where `T(u,v) := {(u′,v′): u₀ ≤ u′ ≤ v′ ≤ v, u′ ≤ u}` is the causal past.
`W` is nondecreasing in the causal order and, by Lemma 1,
`W(u₀,v) ≤ C_n‖ΔΦ‖_∞` on the cone. Note `|Δχ| ≤ |Δϑ| + |Δφ|` is already in `W`.

*Pointwise bounds at `(u,v) ∈ D_n`, all with `r ≥ (v−u)/3` (B1):*

  (a) *ϑ.* From (3.1), `|Δϑ| ≤ ‖ΔΦ‖_∞ + ∫[κ̄₁ W + |Δκ|·|χ₂|]du′`, where
  `κ̄ := sup_{D_n}κ ≤ Cε̃²` by (B2) (note `r₊ ≥ 1`). Moreover
  `|Δκ| ≤ |Δq|·|−ν|/(1−μ) + q̄·|Δ((−ν)/(1−μ))| ≤ C(γ)W` using (B1), (B4)
  (`q̄ ≤ Cε̃²`), and `|Δ((−ν)/(1−μ))| ≤ C(|Δν| + |Δμ|)`. And
  `|χ₂| ≤ r₂ sup|λ⁻¹∂_vφ| ≤ Cε̃ r₂` (B3). Since
  `∫_{u₀}^u r₂(u′,v)du′ ≤ T_n²`, we get
  `|Δϑ| ≤ ‖ΔΦ‖_∞ + [Cε̃²T_n + C(γ)Cε̃T_n²] W`.

  (b) *λ.* From (3.2), `|Δλ| ≤ λ̄ |Δlog λ| ≤ ½ e^{∫κ₁} ∫_{u₀}^u |Δκ| du′ ≤
  C(γ) T_n W`.

  (c) *φ.* From (2.17): `|Δφ| ≤ (1/r)∫_u^v [|Δϑ|λ₂ + |ϑ₁||Δλ|]dv′ ≤
  ((v−u)/r)(½ + Cε̃) W ≤ (3/2)(½ + Cε̃) W`. At axis points `φ = ϑ` (A3), so
  (2.1)'s sup including `Γ` is covered.

  (d) *r.* `|Δr(u,v)| = |∫_u^v Δλ dv′| ≤ (v−u) W ≤ T_n W`. (The sharper
  `(v−u)`-scaling, not `T_n`, is what makes (e) close at the axis.)

  (e) *q — the axis step.* Subtract the averaging formula (Step 2):
  `Δq = (1/r₁²)∫(f′₁ − f′₂)dv′ + 2m₂·(1/r₁² − 1/r₂²)`, using
  `∫_u^v f′₂ dv′ = 2m₂(u,v)`. For the first term, on the segment
  `{u}×[u,v]`: `|Δf′| = |Δ[(1−μ)χ²λ]| ≤ C[|χ̄||Δχ| + χ̄²(|Δλ|+|Δμ|)] ≤
  C[ε̃(v−u)W + ε̃²(v−u)²W]` (using `|χ| ≤ Cε̃ r ≤ Cε̃(v′−u)` from (B3), and
  `|Δr| ≤ (v−u)W`), hence `(1/r₁²)∫|Δf′|dv′ ≤ Cε̃ W` after `r₁ ≥ (v−u)/3`.
  For the second term:
  `2m₂|1/r₁² − 1/r₂²| = q₂ r₂²|r₂²−r₁²|/(r₁²r₂²) ≤ q̄·C|r₂−r₁|max(r)/min(r)² ≤
  Cε̃²·(v−u)·(v−u)W·C/(v−u)² ≤ Cε̃²W`. Sum: `|Δq| ≤ C_n ε̃ W`.

  (f) *ν, μ.* From Step 2: `|Δlog((−ν)/(1−μ))| ≤ |Δlog λ(u,u)| +
  ∫_u^v |Δ[χ²λ/r]|dv′`; with `|λ/r| ≤ 3/(2(v−u))`,
  `|Δ(λ/r)| ≤ CW/(v−u)` (using (d)'s `|Δr| ≤ (v−u)W`), and
  `|Δχ²| ≤ 2|χ̄|W ≤ Cε̃(v−u)W`, the integrand is `≤ CW(Cε̃ + Cε̃²(v−u))`, so
  `|Δν| ≤ (−ν)̄(1−μ)^{−1}[C T_n W + C_nε̃T_n W] ≤ C_n W`; and
  `|Δμ| ≤ r|Δq| + q̄|Δr| ≤ C_nε̃W`.

Assembling: `W(u,v) ≤ C_n‖ΔΦ‖_∞ + a_n W(u,v)` with `a_n = C(γ)(1+T_n²+ε̃T_n³)`
finite for fixed n. This is a Grönwall inequality in the causal order
(evaluate along any path from the cone; `W` monotone), giving
`W ≤ C_n‖ΔΦ‖_∞ e^{a_n T_n} =: C_n‖ΔΦ‖_∞`. This proves (2.1); (2.2) is the axis
restriction of (2.1) plus (A3).

**Step 4 (clock and readings).** By (A2), `dτ_x/dt = 2λ_x(t,t)/√(1−μ_x(t,t)) =
2λ_x(t,t)` ∈ `[e^{−Cε̃²}, 1]` by (B1) and `λ ≤ 1/2` (`∂_u log λ = −κ ≤ 0` from
the cone). Hence `|τ_x(t) − τ_y(t)| ≤ 2(t−t_b)·C_n‖ΔΦ‖_∞`, the inverses
`t_x(·)` are bi-Lipschitz uniformly in `x`, and
`|t_x(T;x) − t_y(T;y)| ≤ 3T_max·C_n‖ΔΦ‖_∞` for `T ≤ T_max`. Finally, for
`H_n`:

  `|H_n(x)_j − H_n(y)_j|`
  `≤ |ϑ_x(t_x, t_x) − ϑ_x(t_y, t_y)| + |Δϑ(t_y, t_y)|`
  `≤ sup_axis|d/dt ϑ_x(t,t)|·|t_x − t_y| + C_n‖ΔΦ‖_∞`,

and `d/dt ϑ_x(t,t) = ∂_uϑ + ∂_vϑ|_Γ = 0 + λ g` by (B5)/(A4) and
`∂_vϑ = λ·(λ⁻¹∂_v)ϑ = λg` exactly, `|g| ≤ Cε̃` by (B3). Substituting the clock
bound and `‖ΔΦ‖_∞ ≤ L₀|x−y|` gives the Lipschitz claim. ∎

**Remark (exact flat wedge).** Taking `ΔΦ ≡ 0` on a common pre-support interval
and the two solutions flat there, the same Grönwall (all forcings vanish)
re-proves characteristic uniqueness on the corresponding sub-triangle; in
particular, since `Φ_{ε,x} = 0` on `[u₀, A₁]` for every x, the launch event
`b = (t_b,t_b)` (any `t_b < A₁`) lies in an **exactly flat** wedge common to
all `x ∈ B̄_ρ`, where `φ ≡ 0` and `τ(t) = t − t_b`. This is DEGREE_ROUTE item 1's
"flat proper-time normalization … the same for all x".

## 4. Use in the degree route (red-team of DEGREE_ROUTE/FINITE_CONTROL)

1. **Degree step.** For each n, `H_n : B̄_ρ → R^N` is continuous (Theorem 2) on
   the *closed* ball, and `CUBIC_TRACE.md`'s uniform estimate
   `sup_{n, |x|≤ρ} |ε⁻¹H_n(x) − x| ≤ Cε²` holds (from §4's printed uniform
   bounds; constants independent of n and x). For `|z| < ρ/2` and
   `Cε² < ρ/2`, the homotopy `x ↦ x + s(ε⁻¹H_n(x) − x) − z` never vanishes on
   `|x| = ρ` (its norm is `≥ ρ − |z| − s·Cε² > 0`), so the Brouwer degree of
   `ε⁻¹H_n(·) − z` equals that of `x ↦ x − z`, namely 1, and a root
   `x_n ∈ B̄_ρ` with `H_n(x_n) = εz` exists **for every n individually**. The
   degree step needs no uniformity in n and no derivative of `H_n`. This
   confirms `energy/REVIEW_DEGREE.md` §"Degree before the joint limit".
2. **Readings are honest axis quantities.** `H_n` is built from `ϑ` on `Γ` via
   the exact identity (A3) and from the clock with `dτ/dt = 2λ` via (A1)–(A2);
   no 1/r or axis-reconstruction estimate is invoked. The central clock uses
   only that `μ = 0` and `ν = −λ` on `Γ`, both printed.
3. **Signed scalar.** `H_n` is not invariant under `φ ↦ −φ` (`Φ_{ε,x} ↦
   −Φ_{ε,x}` gives `H_n ↦ −H_n`); the degree argument uses the real scalar
   without quotienting its sign, as `FINITE_CONTROL.md` prescribes. Changing
   the sign of the whole family changes `z` to `−z`; no rank-two statement is
   claimed from one scalar.
4. **What Theorem 2 does not give:** no continuity of a *limiting* solution
   map in x, no uniform-in-n modulus for `H_n − (linear)`, no uniqueness of
   global limits, no smooth 4D axis metric, no ADM statement. Each is a
   separate gate (`FINITE_CONTROL.md` gates 2–5).

## 5. Passage of roots to the global limit (audit, not a new proof)

This is `FINITE_CONTROL.md` gate 2 / `REVIEW_DEGREE.md` obligation 3. The
printed §4 machinery extends verbatim to **n-dependent profiles within (H1)**,
because every §3–§4 constant depends on the data only through `ε̃` and `Ã`
(common on the class), never on the individual profile:

- §4's displayed uniform bounds (`Σ_{k≤2} sup(|∂^kφ|), sup(|∂^{k+1}(rφ)|) ≲
  Ã + ε`, `sup|∂^{k+1}r| ≲ ε(Ã+ε)`, `m`'s C² bounds on compacts) hold for
  `S_{n,x_n}` uniformly in `(n, x_n)`; Arzela–Ascoli then gives a subsequence
  converging on every compact `Ω ⊆ Q` — including axis points of Ω — in the
  printed modes: `(φ, ∂_v(rφ), ∂_u(rφ))` in `C¹(Ω)`, `r` in `C²(Ω)`, `m` in
  `C¹(Ω)`. (Q contains `Γ`; the displayed bounds are suprema on `Q_{[u_n,∞)}`,
  so axis points are controlled.)
- Clock/readout passage: `λ_n = ∂_v r_n → λ` uniformly on the readout window
  (`C²` convergence of r), with `2λ_n` uniformly in `[1−Cε̃², 1]`; hence
  `τ_n → τ` uniformly and inverses `t_{n_k}(T; x_{n_k}) → t_∞(T; x*)`
  converge uniformly. Axis scalar convergence uses `C⁰` convergence of
  `∂_v(rφ)_n` and `λ_n` plus `φ_n = λ_n^{-1}∂_v(rφ_n)` on `Γ` — both uniform
  limits, `λ` bounded below.
- Radiation recovery: first `n → ∞` at fixed `(u,v)` in §4's printed estimates
  `|log λ_n − log ½| ≲ ε²(max{v−u,1})^{−γ}` and
  `|ϑ_n(u,v) − (λ_n(u_n,v)/λ_n(u,v))Φ(v)| ≲ ε³(max{v−u,1})^{−2γ}`, with
  `Φ_{ε,x_{n_k}}(v) → Φ_{ε,x*}(v)` pointwise (H1), identifies the limiting
  incoming data with `Φ_{ε,x*}` — the identification REVIEW_DEGREE demands.
- Root passage: `H_{n_k}(x_{n_k}) = εz` passes to
  `H_∞(x*) := (ϑ_∞(t_∞(T_j;x*), t_∞(T_j;x*)))_j = εz`, where `H_∞(x*)` is
  defined by the **actual subsequential limit solution**; no selection map over
  targets is asserted, matching the existential form of the route.

**Residual gate-2 checks for the reviewer** (none blocking): confirm the §4
Arzela–Ascoli extraction is applied to the double family
`(n, x_n) ∈ N × B̄_ρ` (the printed proof already only uses `(ε̃, Ã)`); confirm
the mixed-derivative bounds used for `m`'s C² compact bounds are the §4
"corresponding number of mixed derivatives" sentence, which cites the wave
equations.

## 6. Strongest contrary evidence and falsifiers for this lemma

- LOY print no continuous-dependence statement; if the §2.1 "routine iteration"
  failed to be contractive on the class, Lemma 1 would be an *additional*
  structural fact, not a citation. Our proof does not rely on their iteration.
- Falsifier 1: a pair of distinct solutions with the same cone trace
  (`ΔΦ = 0` but `Δϑ ≠ 0` somewhere) would contradict (B5)+(3.1) integration;
  this is just characteristic uniqueness, printed in §2.1.
- Falsifier 2: breakdown of any printed input (B1)–(B5) on the class — e.g., if
  Lemma 3.7's `|K| ≤ Cε̃²r₊^{−1−γ}` failed near the axis, Step 3(a)'s kernel
  bound would fail. (3.24) is derived from (3.16)/(3.17) (mass `≈` cubic
  vanishing at the axis), whose proof uses only (3.10)–(3.12) and (1.7) —
  re-derived here and consistent.
- Falsifier 3: profile families violating (H1) (e.g., supports moving with x,
  or `β` approaching its square-root branch point) can make `C_n` or `L₀`
  blow up; the theorem is silent there.

## 7. Source verification (exact locators; arXiv:1605.03893v1 only)

Fetched `https://arxiv.org/html/1605.03893v1` (LaTeXML HTML of v1; the abs page
shows exactly one version, v1, 12 May 2016). Published version exists (Annals
of PDE 3 (2017), doi:10.1007/s40818-017-0038-4) but was **not** compared;
all locators below are v1 numbering. Read this session (full-text, selected):
§1.2 Thm 1.7 + (1.20) + fn. 11; §2.1 Def. 2.1, (2.1)–(2.5), LWP sentence;
§2.2 (2.6)–(2.16), Remark 2.5; §2.3 (2.17)–(2.26), Lemma 2.6/2.7; §3.1 (3.1)–(3.3);
§3.2 (3.4)–(3.9), Lemma 3.1/3.2; §3.3 Prop. 3.3 (3.10)–(3.15); §3.4 Prop. 3.4
(3.16)–(3.18), Prop. 3.5 (3.19)–(3.21 partial); §3.5 Cor. 3.6, Lemma 3.7 (3.24),
Prop. 3.8 (3.25), Lemma 3.9 (3.26), Prop. 3.10 (3.27)–(3.28), Prop. 3.11 (3.29),
Lemma 3.12 (3.30)–(3.31), Prop. 3.13 (3.32)–(3.34), closure paragraph; §3.6
Prop. 3.14 (3.35), Cor. 3.15; §3.7 Prop. 3.16 (3.36)–(3.39) — **statement
only**, proof not read (not used above); §3.8 Prop. 3.18 (3.44)–(3.47) —
statement only (used only in §5 audit); §4 (entire passage incl. the uniform
bounds, Arzela–Ascoli conclusion, (4.1) and its two displayed estimates,
Remark 4.1). Theorem 1.1 (1.7)–(1.9) and Remark 1.2 re-read.

Verification commands (run in this worktree session): curl of the arXiv HTML;
local tag-stripping to `loy_text.txt`; grep checks for (1.8) —
`2m/r < 1/2` confirmed; (1.20) — `sup|Φ″| < ∞` confirmed; Lemma 3.7 (3.24),
(2.6), (2.8), (3.9), (3.28), §4's two estimates — all confirmed verbatim in the
extracted text. Full command transcript in `AGENT_REPORT.md`.

Search capability check: `scholar_search` worked (server tool, 2026-10-29);
`web-search-prime` not retried (quota exhausted until 2026-11-17, per brief).
No exact primary continuous-dependence theorem for this system was found;
nearest discovery-level leads recorded in `sources.jsonl` (Goursat-problem
preprints arXiv:2605.05381v2, arXiv:2605.03122v1; Mars–Sánchez-Pérez
arXiv:2205.15267 for the vacuum characteristic problem — abstracts only,
different system, no continuous-dependence claim).

## 8. Limitations and next tasks

Limitations: (i) constants are per-n (finite but growing like `poly(T_n)`);
(ii) the result lives at the reduced-quotient level — no statement about the
four-dimensional axis chart; (iii) (H1) is assumed, not re-derived from
`FINITE_CONTROL.md`'s `β`-construction (that family plainly satisfies it; the
audit trail should record the constants `C₀, L₀, Ã` once and for all);
(iv) v1 numbering only; published-version comparison outstanding; (v) the
Prop 3.16 proof and the Prop 3.18 proof were not read (their statements are not
load-bearing for Theorem 2; (3.16)–(3.17), which are load-bearing, were).

Proposed next tasks: (1) audit gate 2 with the double-family Arzela–Ascoli
argument written out (§5 residual checks); (2) record the class constants
(`C₀, L₀, Ã, ε̃ ≤ min(ε₁, ε₂)`) explicitly for the `FINITE_CONTROL` family;
(3) after gates 1–2 close, re-audit INCOMING_MASS transport in the
n-dependent class; (4) separately: 4D axis reconstruction stays untouched.
