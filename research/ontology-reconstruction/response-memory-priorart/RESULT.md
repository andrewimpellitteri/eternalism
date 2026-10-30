# RESULT — Prior-result challenge: response-memory support versus small-mass norm contrast

Lane: `ontology-response-memory-priorart`. Date: 2026-10-30.
Bounded prior-result audit for the coordinator contract
(`research/ontology-reconstruction/coordinator/RESPONSE_MEMORY_CONTRACT.md`, 30 Oct 2026).
This is a novelty-challenge submission for independent review, not a verdict.

## 1. The candidate claim audited

Fix r>0; the fixed-r 3+1 retarded channel acting on bounded source histories f:

    h_m(s) = δ(s−r)/(4πr) − θ(s−r)·m·J₁(m√(s²−r²))/(4π√(s²−r²)),

with the three-part claim:
(a) for every m>0 the response has no finite past cutoff (exact support statement);
(b) ‖R_m−R₀‖_{L∞→L∞} ≤ C_*·m/(4π), C_* = ∫₀^∞ |J₁(z)|/z dz < ∞, and for fixed r the
    ratio ‖R_m−R₀‖/m → C_*/(4π) as m→0;
(c) for a fixed finite time-lag window the error is instead O(m²).
Fading-memory realization invariance is already known (Boyd–Chua §8.2, Theorem 6) and is
not treated as a candidate.

## 2. Three nearest primary works, compared at hypothesis/result level

### 2.1 Salnikov–Satunin–Kirpichnikov–Fitkevich 2021 (read: full-text)
- Source: "Examining axion-like particles with superconducting radio-frequency cavity",
  JHEP03(2021)143, DOI 10.1007/JHEP03(2021)143, arXiv:2011.12871 (published 2021-03-15;
  received 2020-12-10). Appendix A "Retarded Green function", printed p. 15, eq. (A.1).
- What it prints: exactly the candidate kernel,
  G_ret = (1/4π)[δ(t−t′−R)/R − θ(t−t′−R)(m_a/u)J₁(m_a u)], u = √((t−t′)²−R²),
  R = |x̃−x̃′|. Attribution in their reference list: [48] A.D. Polyanin, Handbook of
  linear partial differential equations for engineers and scientists, CRC Press (2016);
  the harmonic-source integral (A.2) is attributed to [49] Gradshteyn–Ryzhik (2007).
- Hypothesis level: retarded KG Green function as a tool for harmonic cavity sources.
- Result level: (A.2)–(A.3) integrate the kernel against e^{−iωt′} only. The printed
  phase comparison e^{iRk} vs e^{iRω} (k=√(ω²−m²)) is an O(m²) statement for fixed ω, R —
  consistent with candidate claim (c), but only for harmonic (infinite-duration) sources.
- Match/mismatch: kernel and infinite-tail support (claim a) are **printed here** and are
  classical. No L∞→L∞ norm, no |J₁|/z constant, no worst-case bounded-history statement,
  no support-vs-norm contrast. Claim (b) is **not** in this paper.

### 2.2 Boyd–Chua 1985 (read: full-text, author-hosted published PDF)
- Source: S. Boyd, L.O. Chua, "Fading Memory and the Problem of Approximating Nonlinear
  Operators with Volterra Series", IEEE Trans. Circuits Syst. CAS-32(11):1150–1161,
  Nov 1985, DOI 10.1109/TCS.1985.1085649. Read §III (pp. 1152–1153), Theorems 1–2,
  §8.1 Theorem 5, §8.2 Theorem 6, Conclusion §X.
- Hypothesis level: TI causal continuous operators on C(ℝ); approximation by finite
  Volterra series and by finite-dimensional dynamical systems, over bounded slew-limited
  signal sets, uniformly for all time (peak error, worst case over K).
- Result level: Theorem 5(I) (p. 1157): A: C(ℝ)→C(ℝ) is LTI + fading memory iff it has a
  convolution representation A u(t) = ∫₀^∞ u(t−τ) h(dτ) with **h a bounded measure on ℝ₊**
  (may contain δ-functions). Theorem 6 (§8.2): fading memory is an input/output property,
  independent of realization.
- Match/mismatch: our R_m, R₀ are instances of their class (bounded convolution measures;
  the light-cone δ is a measure atom; the J₁ tail is absolutely continuous with finite
  mass). The paper supplies the framework and the already-known realization invariance —
  but no mass parameter, no kernel-support statement, no small-parameter norm comparison,
  no Bessel kernels. Claim (b) is **not** here; no priority from this paper for (a)–(c).

### 2.3 Dong, arXiv:1905.08620v1 (read: full-text of abstract/intro/Theorem 1.1/§3)
- Source: S. Dong, "The zero mass problem for Klein-Gordon equations",
  arXiv:1905.08620v1 [math.AP], 21 May 2019 (this v1; not the later published version).
- Hypothesis level: coupled wave–Klein–Gordon system (1.1), m∈[0,1], small compactly
  supported Cauchy data at t₀=2, global existence uniform in m; hyperboloidal + flat
  foliations with iteration.
- Result level: Theorem 1.1: |u(t,x)| ≲ 1/(t + m t^{3/2}); Prop. 3.1:
  |w| ≲ ε·min{(t+2)^{−1}, m^{−1}(t+2)^{−3/2}}; Prop. 3.3: L²(ℝ³) estimates uniform in m
  via frequency-space Hardy inequality.
- Match/mismatch: **scope nonmatch** for claims (a)–(b): Cauchy-problem decay in
  L²/Sobolev/pointwise norms for compact free data; no retarded Green function, no
  operator norm of a kernel difference, no support statement, no prescribed-source
  worst-case class. It establishes that "uniform mass estimates" are an established
  research subject — in a different problem class.

## 3. Verdict

1. **Support claim (a): printed predecessor exists.** The infinite tail for every m>0 and
   the light-cone δ for m=0 are printed in Salnikov et al. (A.1) (their authority:
   Polyanin 2016) and are classical. No priority.
2. **Norm claim (b): no exact printed predecessor found; classified as an elementary
   consequence.** Not found in the three nearest works nor in the targeted searches
   (search limits recorded in AGENT_REPORT.md). But the statement follows in three lines
   from the printed kernel plus folklore:
   - For a translation-invariant convolution channel on bounded inputs, the L∞→L∞
     operator norm equals the L¹ mass of the kernel (the surrounding framework is
     Boyd–Chua Theorem 5's bounded-measure class); the extremal input is a sign-chasing
     history, so the bound below is the exact norm, not merely an estimate.
   - Substitute z = m√(s²−r²):
       ‖R_m−R₀‖ = ∫_r^∞ m|J₁(m√(s²−r²))|/(4π√(s²−r²)) ds
                 = (1/4π)∫₀^∞ |J₁(z)|/√(r²+z²/m²) dz ≤ (m/4π)∫₀^∞ |J₁(z)|/z dz,
     since √(r²+z²/m²) ≥ z/m. Finiteness: |J₁(z)| ≤ z/2 for 0≤z≤2 (series first term;
     DLMF 10.7.3 small-z form) and |J₁(z)| ≲ z^{−1/2} at large z (DLMF 10.17.3 Hankel
     expansions), so C_* < ∞. Ratio limit: ‖R_m−R₀‖/m = (1/4π)∫₀^∞ |J₁(z)|/√(r²m²+z²) dz
     → C_*/(4π) by dominated convergence (dominating function |J₁(z)|/z).
   - (c) similarly: |J₁(u)| ≤ u/2 gives window error ≤ m²W/(8π) for a window of width W;
     the harmonic-source phase comparison in Salnikov (A.2)–(A.3) already shows O(m²)
     for single frequencies.
   Accordingly: **do not claim mathematical novelty** for (a), (b), or (c). The exact
   norm statement is an immediate corollary of printed results; the contract's own kill
   criterion ("the exact result is already printed / immediate corollary") is met at the
   level of elementary consequence even though the exact printed string was not found.
3. **Support/norm contrast as a use:** the joint observation — exact support changes
   discontinuously at every m>0 while every bounded-history response stays within
   C_*·m/(4π) — is a repackaging of classical facts. Any novelty can only live in a
   *downstream* use (an independently specified constitutive criterion connecting
   response duration to the sustaining system), not in the mathematics.

## 4. Philosophical linkage check (law-constitutive temporal extent)

Primary accessible and already in the knowledge base at full-text depth:
K. Brading, "Presentism as an Empirical Hypothesis", Philosophy of Science 80(5) (2013)
1101–1111, DOI 10.1086/673897; law-constitutive alternative at pp. 1103–1105 (a system's
present = the spatiotemporal region needed to sustain its dynamics; extent an empirical
matter). Accessibility re-verified this run (public PDF fetched; opening text matches the
KB record `found-brading` in knowledge/foundations/sources.jsonl). This is a prior,
published linkage of *law-grounded, dynamics-sustaining temporal extent*; a response
window is not an ontology by relabeling. Savitt's localized-present/presentism distinction
is also already recorded in the knowledge base. **No philosophical novelty follows from
the linkage alone**; any constitutive claim must additionally satisfy the contract's
requirement of an independently specified organizing criterion.

## 5. Kernel normalization check (contract kill criterion)

Contract kernel vs Salnikov (A.1) with s = t−t′, r = R: δ(s−r)/(4πr) −
θ(s−r)(m/u)J₁(mu), u = √(s²−r²) — **exact match**, including the 1/(4πr) normalization of
the light-cone term. Retarded/no-free-field and point-detector idealizations remain the
coordinator's to handle (outside this lane's scope).

## 6. Numerical sanity check (within budget: 0.06 s)

`python3 /private/tmp/opencode/rm-priorart/verify.py` (series for |z|≤30, DLMF-10.17.3
asymptotic beyond; Simpson):
- C_* ≈ 1.536 on z∈[0,200], analytic tail bound for z>200 ≤ 0.113 ⇒ C_* ≈ 1.5–1.65
  (only finiteness is load-bearing; value not needed for the verdict);
- ratio ‖R_m−R₀‖/m ÷ C_* at r=1: m=0.5 → 0.866; m=0.2 → 0.950; m=0.1 → 0.986;
  m=0.05 → 1.004 (last value within the few-per-mille accuracy of the asymptotic
  approximation used) — consistent with the dominated-convergence limit C_*/(4π).

## 7. Bounded next steps

1. Coordinator may state the benchmark as: "kernel-norm identity applied to the printed
   (A.1) kernel", citing Salnikov et al. (A.1) + DLMF 10.7.3/10.17.3, marked "elementary
   consequence; no exact printed predecessor found within audit limits".
2. The single unchecked printed neighborhood: Polyanin (2016) retarded-solution section
   and Gradshteyn–Ryzhik (2007) §6.6xx Bessel integrals (both paywalled print; locators
   from Salnikov's bibliography [48],[49]). A library/print check for the L¹ constant or
   a related norm there is the highest-value remaining search.
3. If the contrast is promoted philosophically, position it explicitly against Brading
   (2013) and Savitt (both recorded), not as a new bridge.
