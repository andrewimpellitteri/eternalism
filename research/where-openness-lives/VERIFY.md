# Referee report on NOTE.md (where the open future lives)

Referee: Claude, 25 October 2026. Scope: T3, T4, closed radiation, T1, short priority
search. NOTE.md and main.tex not edited. Scripts: `/private/tmp/claude-501/-Users-andrew-eternalism/d5e98293-0eeb-4b2f-b7f5-c15b3beda35c/scratchpad/woL_verify.py`
(and `woL_t1.py`), python3.11 with numpy/scipy/sympy.

## Verdicts

| Result | Verdict |
|---|---|
| T3 (closed dust) | **Correct**, apart from one gap at η_x = π. It is easy to fix. |
| T4 (de Sitter), closed radiation | **Correct.** The closed forms recompute exactly. |
| T1 (massive KG) | **True in the finite-energy class.** The proof needs an L² form. The framing against Prop. sharp is wrong (MUST-FIX). It is **essentially known** in AQFT. |
| Fourier remark | Correct for tempered solutions. It proves something weaker than T1. |

## T3

**ESU identity.** Degree-n harmonics have eigenvalue −n(n+2), so the frequency is n+1 and
the antipodal parity is (−1)^n. Then ψ(η+π, −X) = (−1)^n(−1)^{n+1}ψ = −ψ, and A² is the
shift by 2π. Correct. M is causally convex in the ESU, so I⁻_M(b) = I⁻_ESU(b) ∩ M; smooth solutions
on M extend to the ESU via their data at η = π.

**A cleaner tool (OPTIONAL but recommended).** The ESU conformal scalar has an exact
spherical-means formula. With data (f, g) at η = 0,

    ψ(η,X) = ∂_η[ sin η · M_f(X,η) ] + sin η · M_g(X,η),

M_h(X,r) = mean of h over the geodesic sphere of arc radius r (proof: the degree-n zonal
function is sin((n+1)r)/((n+1) sin r); checked against exact modes n ≤ 4, error 1.5e−15).
It gives strict Huygens with the sign flip directly; sufficiency and necessity each take
one line, without the Penrose patch.

**Sufficiency.** Correct. SHOULD-FIX wording: Is(b) is not achronal; use the ESU domain
of dependence of B(Y, η_b − ε) ⊂ {η = ε} and let ε → 0 (union = ◇_b). A⁻¹◇_b, A³◇_b miss
the slab.

**Sphere-in-ball.** Correct: S³ \ C = B(−Y, π − η_b) is connected and misses Σ, so it
lies in one complementary ball; Lemma balls gives the two conditions. The open-ball
version for N(b) is the same (complement a closed ball; compactness).

**Necessity.** Correct for η_x ≠ π. w ≤ z ≪ b gives d(w, Y) < η_b. The Penrose map
t ± r = tan((η ± χ)/2) sends η = 0 to t = 0 with factor Ω = cos η + cos χ, even in η; data
(0, g) map to (0, positive × g); Kirchhoff positivity applies.

**MUST-FIX (small gap).** "Assume 0 < η_x < π" omits η_x = π, where x is not in the
Penrose patch and data (0, g) give ψ(π, ·) ≡ 0 (numerically 4.5e−17), since
ψ(π, X) = −ψ(0, −X). Fix: data (f, 0) with f a bump at −X off C, so ψ(π, X) = −f(−X) ≠ 0;
legitimate since x ∉ cl A◇_b gives d(−X, Y) > η_b.

**SHOULD-FIX.** F_L(b) is closed in M, so state F_L(b) = M ∩ cl(U), N(b) = M ∩ U
(U = ◇_b ∪ A◇_b ∪ A²◇_b). D3's "union of the supports" is false at boundary points: use the
sets {ψ ≠ 0}.

**Numerics.** (a) Exact formula, η_b ∈ {0.4, 1.3, 2.5}, random x and bumps off C: ψ = 0 at
every sampled point of U; at all 916 points outside cl(U) (margin 0.02) a bump at a point
of Σ \ C gave ψ(x) ≠ 0 with sign sin η_x. (b) Independent: closed-form 1D d'Alembert for
shells radial about random Z ≠ Y avoiding C: ψ = 0 throughout U; 1043/2223 outside points
nonzero untargeted. (c) Analytically, the radial zero set of
H(cos(χ−η)) − H(cos(χ+η)) is exactly U plus the slice η = π.

**Consequences.**
1. Correct: η_b + η − 2π < η − η_b ⇔ η_b < π (0 failures in 20,000 samples). The heading
   is ambiguous (SHOULD-FIX). The *standpoint* is before maximum expansion; the fixed
   events are near the crunch.
2. Correct. The worldline is fixed on (0, η_b] ∪ [2π − η_b, 2π).
3. Correct. The lower half of A◇_b is disjoint from I^±(b) (0 failures), so these events
   are spacelike to b.
4. Correct (Prop. dust). OPTIONAL: "three-quarters" is true only of conformal 4-volume
   (three of four congruent half-diamonds), not physical (a⁴-weighted) volume.

Context: Prop. echo (only ⊆) stays true; T3 answers its open question negatively. The
main.tex prose presenting the comoving flow as the threshold-change example should be
revisited, since F_L(b) for the conformal scalar already reaches the timelike future.

## T4 and closed radiation

**de Sitter.** ◇_b is centred at (−π/2, Y) with half-height η_b + π/2 < π. Then
A◇_b ∩ M = {d(X, −Y) < η + η_b} (0 mismatches in 20,000 samples), and A^{±2}◇_b miss the
slab. Necessity transfers with the data slice at η = −π/2 (ℐ⁻, outside M). The witness
solutions are still smooth on M. Numerics at η_b ∈ {−1, 0, 1.2} gave 0 inside the set and
nonzero at all 525 outside points. The antipodal observer is fixed for η > −η_b, and
{d = π} never meets I⁻ of the comoving line X = Y. Correct.
- SHOULD-FIX: say "the comoving geodesic X = Y" rather than "b's worldline".
- SHOULD-FIX: change the label to PROVED, with the η_x = π fix (here η_x − η_0 = π does
  not occur, since the slab height is π).

**Closed radiation.** A◇_b ∩ M = {d(X, Y) + η > 2π − η_b} (0 mismatches). It is
disjoint from I⁺(b) because that would need η > π. Numerics agree. Correct.

## T1

**Truth.** The conclusion is right for finite-energy (indeed one-particle-norm)
solutions. The argument as written is not yet a proof:

- **SHOULD-FIX.** The uniform pointwise asymptotics hold for Schwartz profiles, not for
  finite energy. Use the L² form: for f ∈ C_c(|v| < 1) and data in the energy space,
  ‖f(x/t)ψ(t)‖² → ‖f(∇ω)â₊‖² + ‖f(∇ω)â₋‖² as t → −∞. The ± cross term carries the phase
  e^{2im|t|√(1−v²)} and tends to 0 by Riemann–Lebesgue, because the phase has a critical
  point only at v = 0. This step is missing: ψ vanishing on a region does **not** make
  ψ₊ = ½(ψ + iω⁻¹ψ_t) vanish there, since ω⁻¹ is nonlocal.
- Stationary phase checks: p = mv/√(1−v²), phase m|t|√(1−v²), amplitude |t|^{-3/2}.

**MUST-FIX (class).** T1 depends on the class, and the "Contrast" compares it with the
wrong result. Prop. sharp uses *smooth*, infinite-energy plane waves. In that class the
massive field is exactly as open as the massless one. Here is an explicit
counterexample. Set u = t − n·x and v = t + n·x, so that KG becomes ψ_uv = −(m²/4)ψ.
Take the Goursat solution

    ψ = Σ_k (−m²u/4)^k/k! · F_k(v),   F_0 = f,   F_k = ∫_0^v F_{k−1},

with f smooth and zero for v ≤ 0. I verified the PDE symbolically.
- ψ vanishes on {t + n·x ≤ 0}, which contains I⁻(0).
- Choosing n = x̂ and f a narrow bump makes ψ(x) ≠ 0 at any x ∉ J⁻(0).
- So for smooth massive KG, F_L(b) = J⁻(b), the same as Prop. sharp.
- ψ grows like e^{m√(|u|v)} (1e69 at |u| = v = 160), so it is neither tempered nor of
  finite energy, which is consistent with the Fourier remark.

So the contrast is about the solution class (decay at ℐ⁻), not mass alone: compare
finite-energy massive (T1) with finite-energy massless (T2), and restate §3 item 1 and
"Mass closes the future" accordingly.

**Fourier remark.** Correct for tempered solutions. Along k + sℓ the hyperboloid meets the
line once. A point-supported distribution in s is the Fourier transform of
polynomial × exponential in τ, which cannot be supported on a half-line. The remark is
still weaker than T1: support in a null half-space is a stronger hypothesis than
vanishing on I⁻(b). Label it a heuristic.

## Priority (bounded search; depth labelled)

- **T1 is essentially known (strong hit).** Camassa, "Relative Haag Duality for the Free
  Field in Fock Representation", arXiv:math-ph/0607057v1 (2006). Read depth: full text of
  §4.4. §4.4.1 (p. 9) says: "In the massive case, the algebra associated to the forward
  (or backward) light-cone is already the total algebra of observables", that is,
  H(V₊) = H₀, citing "Theorems 1 and 2" of Sadowski & Woronowicz, "Total sets in quantum
  field theory", Rep. Math. Phys. 2(2):113–120 (1971). Read depth for Sadowski–Woronowicz:
  discovery only.
  - By symplectic duality, H(V₋) = H₀ is exactly the statement that no nonzero
    one-particle solution vanishes on V₋. That is T1 in a class larger than finite energy.
  - §4.4.2 gives the massless counterpart: Huygens yields H(V₊)′ = H(V₋), the "time-like
    duality" R(V₊)′ = R(V₋), citing Buchholz 1978 (Leipzig proceedings). Read depth for
    Buchholz 1978: discovery.
  - So the T1/T2 contrast is known in quantum form; a classical restatement is exposition,
    not a novelty claim.
- **Ellis & Sciama 1972.** The bibliography is confirmed: "Global and non-global problems
  in cosmology", in *General Relativity: Papers in Honour of J. L. Synge*, ed.
  O'Raifeartaigh, Clarendon, pp. 35–59, via the reference list of Ellis,
  arXiv:gr-qc/0102017. Read depth: discovery. Content NOT READ, so pp. 41–42 remain an
  unresolved priority risk for T3/T4.
- **Earman 1995, pp. 125–130.** NOT READ. Only bibliographic records were found.
- **Explicit ESU formulas.** Lead: Klainerman–Sarnak method, cited via arXiv:2112.00771
  (discovery). The formula is classical in substance; any T3 novelty lies in the
  determination-set statement.

## Other notes

- T2's cut-order claim is correct (b ≤ b′ ⇔ b′⁰ − b⁰ ≥ θ·(b⃗′ − b⃗) ∀θ). The rest of T2
  and T5 were not checked.
- T3's necessity witnesses blow up at the bang (φ ~ 4g/(a_m η)) but are smooth on M, so
  admissible. A stricter physical class can only enlarge F_L.
