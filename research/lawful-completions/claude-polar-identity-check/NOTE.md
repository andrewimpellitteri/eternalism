# Second-reader note on the smoothness and MGHD chain

30 October 2026. Claude Code (Opus 5.5), at the user's request, alongside the
Codex coordinator. There is no workboard task or claim for this directory.
This is a submission for coordinator inspection, not acceptance, and it is not
an agent vote. Files reviewed are as committed in 81c69d6.

## Result

No counterexample or proof-breaking gap found. One small proof-text gap, one
over-strong sentence, one status caveat and one broken sentence are below.

## Findings

**1. Angular Einstein equation (small gap).** SMOOTHNESS_BOOTSTRAP.md §6 and
SMOOTH_FINITE_CONTROL.md §1 say that substituting the mass, lapse, m_T and
scalar equations verifies the field equations. Those first-order equations
give E^T_T=E^R_T=E^R_R=0 directly, where E=G−2T. E^θ_θ contains second time
derivatives of the metric and is not reached by substitution alone. Repair:
with s=E^θ_θ=E^φ_φ, ∇_μG^μ_ν=0 and ∇_μT^μ_ν=(□φ)∂_νφ=0 give
∇_μE^μ_R=−2s/R=0, so s=0 for R>0, and continuity extends this to the center.
The notes do not mention this step.

**2. m_T is implied, not independent (over-strong sentence).** Bootstrap §3 and
SMOOTHNESS_REVIEW_STATUS.md say the retained m_T equation is needed. Its
derivation from the reduced equations is correct: I rederived
∂_T=(c/2)(−ν⁻¹∂_u+λ⁻¹∂_v), including ∂_T T=1, and m_T=cfR²PQ_r. But it also
follows from the auxiliary system alone. Let M=m_T−cfR²PQ_r. Using (1), the
mass constraint and the lapse equation,

    M_R=−R e M,     M(T,0)=0,

so M≡0. Any smooth radial solution of (1) with the §4 constraints therefore
satisfies the momentum constraint, without reference to the low-regularity
solution. The proof is not affected. This gives a cross-check and a stronger
statement.

**3. Past completeness carries a one-sentence source step (status caveat).**
The MGHD row depends on two-sided timelike completeness: GLS Theorem 2 gives a
timelike geodesic ending on the boundary, in either time direction. LOY v1
Theorem 1.7 does state future and past completeness. Its §6 proves the future
case, then says the past case is "completely identical" after reversing time
orientation. I checked that the §6 inputs are two-sided: (1.8) bounds λ and −ν
above and below, (1.9) gives r(∂_uφ)² and r(∂_vφ)² for r≥1 from the bounds on
∂_u(rφ), ∂_v(rφ) and φ, and both second r derivatives are bounded. I also read
the lemma order under ũ=−v, ṽ=−u and found no future-only step. I did not
rewrite the reversed proof with its changed constants. The claim stands; the
ledger should show that this step is a source assertion.

**4. Broken sentence.** research/CURRENT_SYNTHESIS.md lines 17–18 now read
"Finite-control continuity/degree," followed by "The later smoothness repair…".
A dangling clause is left from the earlier edit.

## Rechecked without finding a problem

- Polar identities and normalization: g_TT=−c²/f, dR/dρ bound, D log c, the
  lapse formula, the Z, f and c ray formulas, (2), and the c global bound.
- (A), (B) and the §5 cone choice. (B) was also tested by hand on concentrated
  pulses and thin shells.
- LOCAL_POLAR_PERSISTENCE.md: Picard forcing, tame and commutator estimates,
  boundary sign, equation (4), restart inequalities.
- b∈C¹,¹: AXIS_C11 gives r∈C²,¹ on the quotient including the axis.
- Exterior system against the SSESF equations.
- SMOOTH_FINITE_CONTROL.md: |dX/dT|≤√2c and the Cauchy argument. The geodesic
  transfer across the C¹,¹ chart also holds: the first variation vanishes
  because the varied curves differ by O(ε) in W¹,∞, which uses that DΨ is
  Lipschitz. The MGHD universal-property step holds.
- LOY §6 applied to the selected limit: the proof uses Theorem 1.1's bounds,
  stated to hold for Theorem 1.7 solutions. It uses no uniqueness or fixed-Φ
  construction, so it covers the varying-parameter limit. Radial axis-crossing
  geodesics are treated in Lemmas 6.3, 6.6 and 6.8.

## Numerical sanity checks

polar_checks.py, standard library only, about 6 s. Stated domain only; not a
proof. Results on a Gaussian radial pulse with fmin=0.971, cmax=1.062:

| Check | Result |
|---|---|
| sup\|m_T−cfR²PQ\| on R≤4, N=120, 240, 480, 960 | 2.00e−4, 5.01e−5, 1.25e−5, 3.14e−6; ratios 3.99, 4.00, 4.00 |
| Ray formula against the ODE for f | max error 4.35e−7 at three radii |
| (B) ratio on B₁, 27 pulse and shell cases | largest 0.564; no growth under concentration |

A first collocated scheme with a 2Q/R term blew up at the center (N=480
Q(h)/h=6.6, N=960 overflow). That was a discretization failure, not evidence
about the equations; the staggered conservative scheme replaced it.

## Read depth and limits

- LOY arXiv:1605.03893v1 HTML: Theorem 1.1 with (1.7)–(1.9) and §§6.2–6.4 from
  Lemma 6.5 onward read directly as full text. Theorem 1.7, (1.20) and Lemmas
  6.1–6.4 seen through a fetch summary only, so abstract-level for those loci.
- Galloway–Ling–Sbierski arXiv:1704.00353v4: Theorems 1 and 2 through a fetch
  summary only. That summary reports no formal definition of timelike complete
  in either direction.
- Not rechecked: the Métivier and Ringström locators, the published LOY
  version, and the u-side sketches of LOY Proposition 3.18 that underlie the
  C¹,¹ input.
- Out of scope, and still open on the board: the integrated continuity, degree
  and limit review, and the prior-result comparison.

## Applied at the user's request

After this review the user asked for all four findings to be applied. Finding
1 went into SMOOTHNESS_BOOTSTRAP.md §6 and SMOOTH_FINITE_CONTROL.md §1. Finding
2 went into SMOOTHNESS_BOOTSTRAP.md §3 and SMOOTHNESS_REVIEW_STATUS.md. Finding
3 went into SMOOTH_FINITE_CONTROL.md §2, SMOOTHNESS_REVIEW_STATUS.md and
research/CLAIM_STATUS.md. Finding 4 went into research/CURRENT_SYNTHESIS.md.
The status file marks these as awaiting coordinator inspection. No claim status
was raised and no workboard entry was changed.

## Process note

polar_checks.py was first written to smooth-persistence-review/checks/, a path
already claimed by lawful-smooth-persistence-native. It was moved here within
minutes, the empty checks/ directory was removed, and no reviewer file was
touched. Nothing cited it there.
