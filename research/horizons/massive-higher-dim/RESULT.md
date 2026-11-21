# Massive past-cone fixing in every dimension

11 November 2026. Native Claude research worker (Fable 5.2), task
`novel-massive-higher-dim`. Checked only by the session that wrote it. The mathematics
is a short application of a standard estimate, and the finite-energy case follows at
once from a published statement. No novelty is claimed and no temporal ontology is
selected. Sources: [sources.jsonl](sources.jsonl). Illustration:
[cone_energy_2d.py](cone_energy_2d.py). Extends the
[1+1 note](../massive-minkowski/RESULT.md).

## Verdict

**Proved, in every space dimension n ≥ 1.** Let m > 0. A solution of
(∂ₜ² − Δ + m²)u = 0 on ℝ¹⁺ⁿ that is a tempered distribution and vanishes on the
chronological past of an event is zero.

- **Class covered.** Exactly the solutions whose Cauchy data at one time are tempered
  distributions on ℝⁿ (Lemma 1 shows this is the same as u being tempered on
  spacetime). It contains every finite-energy solution (data in H¹ × L²), data in any
  Sobolev space, polynomially growing data, and plane waves. Real or complex.
- **Tempered distributions do not behave differently.** They give the same answer as
  finite energy. The answer changes only for solutions that grow exponentially in
  space: the smooth counterexamples of the 1+1 note work unchanged in every dimension
  and grow like e^{m|x|}.
- **Weaker hypothesis.** Vanishing on the tail {t < −T₀, |x| < |t|} of the cone is
  enough. By time reversal the same holds for a future cone.
- **Finite energy only.** For that subclass a published statement already suffices:
  Yang (arXiv:2309.15282v1) states and proves that the energy of an H¹ × L² solution
  in {|x| > |t|} tends to zero as t → ±∞ in any dimension. With conservation of energy
  that gives the result in two lines, exactly as in the 1+1 note.

| Law and class on Minkowski spacetime ℝ¹⁺ⁿ, n ≥ 1 | What the past of an event fixes |
|---|---|
| Mass m > 0, finite energy | Everything |
| Mass m > 0, tempered | Everything |
| Mass m > 0, all smooth solutions | The causal past only |

## Proof

Write ω(k) = √(|k|² + m²). Because m > 0, ω is smooth, every derivative of ω of order
at least one is bounded, and ω ≥ m. This is the only place the mass is used, and it is
used three times: to make e^{±itω} act on Schwartz space, to divide by ω, and to keep
group velocities below 1 on compact sets of k.

**Lemma 1 (structure).** Let u ∈ S′(ℝ¹⁺ⁿ) solve the equation. Then there are unique
A, B ∈ S′(ℝⁿ) with spatial Fourier transform

    û(t, k) = e^{−itω(k)} Â(k) + e^{itω(k)} B̂(k).

So t ↦ u(t) is a smooth map into S′(ℝⁿ), and for some N and C, for all Schwartz f,

    |⟨u(t), f⟩| + |⟨∂ₜu(t), f⟩| ≤ C (1 + |t|)^N p_N(f),

where p_N(f) is the supremum of |x^α ∂^β f| over |α|, |β| ≤ N. Conversely any A, B in
S′(ℝⁿ) define a tempered solution.

*Proof.* The partial Fourier transform is an isomorphism of S′(ℝ¹⁺ⁿ), and
(∂ₜ² + ω²)û = 0. The function e^{iωt} is smooth on ℝ¹⁺ⁿ with polynomially bounded
derivatives, so multiplying by it is an isomorphism of S′. A direct computation gives
∂ₜ[e^{iωt}(∂ₜ − iω)û] = e^{iωt}(∂ₜ² + ω²)û = 0. A tempered distribution annihilated by
∂ₜ is 1 ⊗ C₋ with C₋ ∈ S′(ℝⁿ). So (∂ₜ − iω)û = e^{−iωt}C₋, and likewise
(∂ₜ + iω)û = e^{iωt}C₊. Subtract and divide by 2iω. The bound holds because the
Fourier transform is continuous on Schwartz space, Â and B̂ have finite order, and
each k-derivative of e^{±itω} costs at most a factor C(1 + |t|). ∎

**Lemma 2 (no propagation faster than the group velocity; standard).** Let
a ∈ C_c^∞(ℝⁿ) with support in |k| ≤ K, put v₀ = K/√(K² + m²) < 1 and fix
v₀ < v₁ < 1. Let φ(t, x) = (2π)^{−n} ∫ e^{i(k·x ∓ ω(k)t)} a(k) dk. Then for all
multi-indices and all L there is C with

    |x^α ∂ₓ^β ∂ₜ^j φ(t, x)| ≤ C (1 + |t| + |x|)^{−L}   whenever |x| ≥ v₁|t|, |t| ≥ 1.

*Proof.* Derivatives in x and t multiply a by polynomials in k and ω, so take β = 0,
j = 0. The phase ψ = k·x ∓ ωt has ∇ₖψ = x ∓ t k/ω, and |k/ω| ≤ v₀ on the support, so
|∇ₖψ| ≥ |x| − v₀|t| ≥ (1 − v₀/v₁)|x| ≥ c(|x| + |t|) in the region. Integrate by parts
with the operator (i|∇ψ|²)^{−1} ∇ψ·∇ₖ, which fixes e^{iψ}. Second and higher
k-derivatives of ψ are bounded by C|t|, so each step gains a factor C(|x| + |t|)^{−1}.
Repeat L + |α| times. ∎

**Theorem.** Let m > 0, n ≥ 1, and let u ∈ S′(ℝ¹⁺ⁿ) solve the equation and vanish on
{t < −T₀, |x| < |t|}. Then u = 0.

*Proof.* Take a, b ∈ C_c^∞(ℝⁿ) with support in |k| ≤ K, and the test solution φ with
φ̂(t, k) = e^{−itω}a(k) + e^{itω}b(k). Each φ(t) is a Schwartz function. Put

    W(t) = ⟨u(t), ∂ₜφ(t)⟩ − ⟨∂ₜu(t), φ(t)⟩     (bilinear pairing of S′ with S).

*Step 1: W is constant and determines A, B.* Inserting Lemma 1 and Parseval, the terms
in Â·a and B̂·b cancel and

    W(t) = 2i (2π)^{−n} [ ⟨Â, ω b(−·)⟩ − ⟨B̂, ω a(−·)⟩ ],

which does not depend on t.

*Step 2: W(t) → 0 as t → −∞.* Let t < −max(T₀, 1) and T = |t|. Since u is a smooth
function of t with values in S′(ℝⁿ), both u(t) and ∂ₜu(t) vanish on the open ball
|x| < T. Choose v₀ < v₁ < v₂ < 1 and a smooth χ on ℝⁿ with χ = 0 for |y| ≤ v₁ and
χ = 1 for |y| ≥ v₂. The functions (1 − χ(x/T))φ(t) and (1 − χ(x/T))∂ₜφ(t) are smooth
with support in the closed ball of radius v₂T, inside the open ball where u(t) and
∂ₜu(t) vanish. So

    W(t) = ⟨u(t), χ(·/T) ∂ₜφ(t)⟩ − ⟨∂ₜu(t), χ(·/T) φ(t)⟩.

By Lemma 2, p_N of χ(·/T)φ(t) and of χ(·/T)∂ₜφ(t) is at most C_L(1 + T)^{−L} for every
L (derivatives of χ(x/T) are bounded for T ≥ 1). By Lemma 1 the pairings are at most
C(1 + T)^N times that. Take L = N + 1.

*Step 3.* So W = 0 for all a, b ∈ C_c^∞(ℝⁿ). Since ω is smooth and positive, ωa and
ωb range over all of C_c^∞. Hence Â = B̂ = 0 and u = 0. ∎

The proof never uses positivity of the energy. It uses the conserved symplectic
pairing of u with a dense family of rapidly localised test solutions.

**Corollary (exterior energy decay, n ≥ 1).** For a finite-energy solution and any
R, the energy in {|x| ≥ |t| − R} tends to zero as t → ±∞. *Proof.* Solutions with
Â, B̂ ∈ C_c^∞ are dense in the energy norm. For those, Lemma 2 gives decay faster than
any power, because |t| − R ≥ v₁|t| eventually. Energy in a region is at most the total
energy, which is conserved. ∎ This is the n-dimensional form of Burnol's Theorem 1,
and for R = 0 it is the statement in Yang's paper. It gives a second proof of the
theorem for finite energy.

**All smooth solutions.** Let x lie outside the causal past of b; take b = 0, so
t + |x| > 0. With e = −x/|x| (any unit vector if x = 0) put U = t − e·y and
V = t + e·y at a point (t, y). Then U ≤ 0 on the causal past of b and U > 0 at x. The
1+1 solution of the earlier note, read as a function of (U, V) alone, solves the
equation on ℝ¹⁺ⁿ, vanishes for U ≤ 0 and is positive at x. So for smooth solutions
the past fixes the causal past and nothing more, in every dimension. These solutions
are not tempered: on the slice t = 0 they grow like e^{m|e·y|}.

## Attacks on the proof

- *Is a time slice of a distribution meaningful?* Yes, by Lemma 1, which needs
  m > 0 and temperedness. For a non-tempered distribution solution the argument has
  no starting point.
- *Does vanishing on the open cone give vanishing of ∂ₜu(t) on the ball?* Yes: test
  against η(t)f(x) with f supported in the ball and η concentrating at t; continuity
  in t does the rest. The same with η′.
- *Does it secretly prove too much?* At m = 0 it must fail, since the 1+1 note has a
  massless finite-energy counterexample in three dimensions. It does fail: v₀ = 1 for
  every K, so no cutoff χ fits between the group velocities and the cone, and ω is
  not smooth at k = 0. Plane waves are tempered and are not counterexamples because
  they do not vanish on a cone. Solutions with compactly supported data vanish on
  spacelike regions, never on a cone tail.
- *Uniformity in t.* The constant in Lemma 1 grows polynomially in t. Lemma 2 beats
  any polynomial. A merely algebraic decay rate would not be enough for distributions
  of high order, which is why the test solutions have compact support in k.
- *Not re-derived independently.* One session wrote and checked this. The sign and
  constant in Step 1 do not matter to the conclusion; the cancellation of the
  time-dependent terms does, and it was checked term by term.

## Illustration

Fraction of energy in |x| ≥ |t|, two space dimensions, rotationally symmetric Gaussian
data of width 2 (one datum, finite grid, proves nothing; computed total energy agrees
with the exact value to 3 parts in 10⁴):

| m | t = −25 | t = −50 | t = −100 |
|---|---|---|---|
| 0 | 0.356 | 0.355 | 0.354 |
| 0.5 | 0.022 | 0.007 | 0.000 |
| 1 | 0.000 | 0.000 | 0.000 |

## Credits: what is known already and by whom

- **Yang**, arXiv:2309.15282v1 (remark after the Klein–Gordon theorem and the appendix
  "Partition of energy for Klein-Gordon equation: a classical setting", read in the
  TeX source): for m = 1, real data in H¹(ℝᵈ) × L²(ℝᵈ), any d, the energy in
  {|x| > |t|} tends to 0 as t → ±∞. This is the primary source the 1+1 note lacked.
  The proof cites two technical lemmas of the same paper that I did not read.
- **Strichartz** 1981, J. Funct. Anal. 40, 341–357: per Yang, the first study of the
  asymptotic relation behind this, with a "weakened version for the Klein-Gordon
  equation" (journal abstract as reproduced in Yang's bibliography). Yang says the
  proof of its Corollary 2.2 is wrong and repairs the case needed. Not read.
- **S. A. Nelson** 1971, Proc. AMS: an L² asymptote for Klein–Gordon solutions,
  "applied to show how energy distributes among various conical regions". Abstract
  only.
- **Duell**, arXiv:1603.07512v2, Lemma 6 and Corollary 7 (read): Lemma 2 for n = 3,
  stated without proof and attributed to Ruelle 1962, with the non-stationary phase
  proof referred to Reed–Simon III, Appendix 1 to XI.3. Neither of those was read.
- **Burnol**, arXiv:math/0509619v4, Theorem 1: the case n = 1 of the corollary (read
  by the earlier lane, not re-read here).
- **Sadowski and Woronowicz** 1971, Rep. Math. Phys. 2(2), 113–120: the likely quantum
  counterpart. Still not read; only its bibliographic details were confirmed.
- The theorem for tempered distributions, as stated here, I did not find in two
  searches. It is a few lines from Lemma 2 and is very likely known or folklore.

## Limits

- Free field on Minkowski spacetime, m > 0 only.
- The fixing uses the arbitrarily remote past: the proof takes t → −∞ and gives no
  rate. No stability estimate is claimed, and none should be expected.
- Between polynomial growth (fixed) and growth e^{m|x|} (not fixed) the question is
  open here. I did not determine the threshold.
- Self-checked by one model session. No independent reviewer or outside expert.
