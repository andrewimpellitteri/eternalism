# Red-team review of RESULT.md

30 October 2026. Claude Code (Opus 5.5), as an adversarial reader. This is a
review for coordinator inspection, not acceptance. The repairs below are this
reader's own single-reader derivations, not LOY's. No novelty or ontological
claim.

## Verdict

**The proof fails as written at one step and the Claim overreaches at another.
Both are repairable. No counterexample was found.** With R1 and R2 below the
candidate survives, conditional on LOY Theorem 1.1, §3 and Repair A, for a limit
in the integrated class only. It does not reach the C¹,¹ category of C11 at the
stated C¹ hypothesis, and it cannot.

**Strongest problem: "J_η𝒯_nJ_η maps B to B" (§4) is false.** The term −I is not
supported after A+2δ. It switches on where the data do, so 𝒯_nJ_ηΦ starts at the
left edge of J_ηΦ, and a symmetric J_η moves that edge left again. B is not
invariant, so Schauder does not apply and §5's flat wedge has no support. R1 fixes
this with a retarded mollifier.

Ranked findings:

1. §4: B is not invariant (R1). A real error, with a cheap fix.
2. Claim: E has no ceiling, but a fixed tail G counts toward LOY's parameter (R2).
3. Gap 1 is misdescribed. For y∈C¹∖C¹,¹ the C11 category is impossible, not merely
   unproved. For y∈C¹,¹ the C² bound is not circular: put it in the ball (R3).
4. Smooth category for smooth y stays open. This is the real content left of Gap 1.

| # | Item | Verdict |
|---|---|---|
| 1 | Axis identity, clock, fixed-point equivalence | **VERIFIED**, one direction only |
| 2 | K_v, φ_v, I′, uniformity in vertex | **VERIFIED**; attribution note |
| 3 | Repair A′ | **VERIFIED** on second read; not needed by §4 |
| 4 | Schauder step | **GAP as written; REPAIRABLE** (R1) |
| 5 | Limit, wedge, mass, regularity | **VERIFIED** for the integrated class, given R1; strengthened by R4 |
| 6 | Quantifiers | **REPAIRABLE** (R2 and bookkeeping) |
| 7 | Gap list | **Incomplete**; see the end |

## Point-by-point audit

**1. Axis identity: VERIFIED.** From λ_u=λK and p_uv=r_uvφ=λKφ, (λL)_u=λKφ.
Integrating with λ=½ and L=Φ on the cone gives 2λL=Φ+∫2λKφ. The factor 2 is right:
the flat case gives Λ=1, I=0, φ_c=Φ, matching RESPONSE_REDUCTION.md. It also agrees
with LOY (3.14). On Γ, p_v=λφ, so L=φ. log(2λ)=∫K gives Λ. Since ν=−λ and μ=0 on Γ,
Ω=2λ, so dτ/dt=Λ. Causality: Λ, I, τ at t use only v≤t, which needs domain of
dependence on sub-triangles (Repair A). Division by Λ is safe: Λ>⅔ by (1.8) and
Λ≤1 by (3.4), both closed under limits. τ≥⅔t gives τ(t̄)≥T_max, and the hypothesis
that y vanishes near T_max makes the zero extension C¹.

Note: "exactly when" is too strong. A fixed point implies the trace, not
conversely: it also forces φ_c=0 on T_max≤τ(t), t≤t̄, and fixes Φ past t̄. Only the
needed direction is used.

**2. Section 2: VERIFIED, and better than stated.** LOY v1 prints what §2 derives:

- (3.24) |K|≲ε²r₊^(−1−γ), exactly the cited bound. This closes Gap 4. Compact data
  are covered, since (3.16)'s proof only uses (1.7). The fetch-tool report that
  (3.16)'s statement and proof differ is empty: the two minima coincide.
- (3.12), (3.19), (3.20), and **(3.31) |λ⁻¹∂_vK|≲ε²min{1,r⁻²}+ε⁴min{r²,r⁻²}**, which
  is stronger than §2's r₊^(−1−γ).
- (3.35) |λ⁻¹∂_v log λ|≲ε², which is |Λ′|≲ε̃² at once, since λ_u=0 on Γ.
- (3.25) gives |Λ−1|≲ε̃², and (3.29) gives |I|≲ε̃³.

For I′, the boundary term vanishes since K=0 on Γ. Using (3.7) with k=2, which needs
only −ν≥⅙:

    ∫|λ_vKφ|≲ε̃⁵,   ∫|λK_vφ|≲ε̃³,   ∫|λKφ_v|≲ε̃³,

all independent of u₀. So ‖𝒯Φ‖≤(1+Cε̃²)‖y‖+Cε̃³ holds, with Λ²≤1 on the y′ term and
χ′ meeting only −I past the window.

*Does anything hide L_v?* In the expressions for r>0, no. In the bounds, yes: the
r≤1 estimates consume sup|L_v| through (3.12), so ε̃ must include ‖Φ′‖. On the axis
φ_v=L_v/2, and K_v=−L_v²/12 by a direct expansion. So 𝒯 is bounded Lip→Lip, not
C⁰→Lip. The gain holds off the axis, because the s-integral does not see Γ. It is a
gain in the *Φ-dependence* only. y↦Φ has order zero: Φ is exactly as regular as y.
The accurate statement is that the trace map is a reparametrized identity plus a
smoothing correction, not that "inversion gains one derivative".

*Only Theorem 1.1 bounds?* True of the second-order bounds, as RESULT.md literally
says. But K, I and φ_v use §3 estimates not in the theorem statement. No Prop 3.18
is used. §5 uses the u-side second-order bounds of (1.9), which Prop 3.16 and Cor
3.17 prove, so that is fine. Constants see no Φ″: (3.32) depends on ε alone.

**3. Repair A′: VERIFIED.** Each line rederived, in this order at fixed u:

- δr=O(rW). δφ=O(W), as a ratio with no loss at r=0. δ(L−φ)=O(W), with no rate.
- δm_v=O(r²W)+O(r²)(|δm|/r+r²W)+O(rW), so δm=O(r²W) by Gronwall in r.
- δμ=O(rW), δK′=O(W), δν=O(W) with δν(u,u)=−δλ(u,u), then δK=O(W).

Each term of δK: δm/r², (m/r²)δν, (m/r²)δμ, mδr/r³. RESULT.md omits δν, but it
closes without circularity since K′ has no ν. At fixed v, δK(φ−L)=O(W) and
Kδ(φ−L)=O(W), so W(u)≤C(W(u₀)+∫W) is a true Volterra inequality. The extra factor
of r claimed in §3 is true and unneeded. No loss at r=0.

**Simplification.** For fixed η, J_η is bounded C⁰→C¹, so Repair A alone gives §4's
continuity. A′ is dispensable there, and Gap 3 can shrink to Repair A. A′ is
essential only if the mollifier is dropped (R1, variant).

**4. Section 4: GAP as written; REPAIRABLE.** B is convex, and compact in C⁰ by
Arzelà–Ascoli with lower semicontinuity of Lip. Schauder is the right theorem, and
blow-up of continuity constants in n is harmless. The n, η order is sound: the
trace bound is uniform, so any η_n→0 works. The failure is invariance:

- Take Φ∈B, Φ≥0, nonzero near A+δ. On supp J_ηΦ, once m>0, K<0 and φ>0, so I<0.
  With y∘τ=0 for t<A+2δ, 𝒯_nJ_ηΦ=−I>0 from the left edge A+δ−η on.
- J_η then gives support to A+δ−2η. "η<δ/4" does not help: it protects y, not I.
- The right edge t̄+1 fails the same way.

Numerical sign check, not a proof, script of §7, N=420, Φ=ε bump on [1,1.6]:
I=−2.76e−3 at t=1.3 and −2.80e−3 at t=1.8 for ε=0.3. For ε=0.15 they are −3.38e−4
and −3.38e−4. The ratio is 8, as a cubic term should give.

A smooth cut-off ζ on the left would restore support, but costs Lip≈ε̃³/δ, so
M_* would see δ, contradicting the Claim. Use R1 instead.

**R1. Retarded mollifier.** J_ηf(t)=∫₀¹ρ(σ)f(t−ησ)dσ, with ρ smooth, supported in
(0,1). It preserves the norm and never moves a left edge. Let B be supported in
[A+δ,t̄+2], with χ and η<½ as before. For Φ∈B and t<A+δ, data vanish on v≤t, so
Λ=1, τ=t, y(t)=0, I=0. Hence J𝒯_nJ maps B to B. |Ψ−𝒯_nΨ|≤2ηLip(𝒯_nΨ) survives, and
the construction stays causal. The threshold sees no δ. *Variant:* A′ extends 𝒯_n
to B by uniform continuity, so Schauder applies with no mollifier.

**5. Section 5: VERIFIED for the integrated class, given R1.** Equicontinuity of r,
λ, ν, L, M, φ, m follows from (1.8), (1.9), (3.12), (3.37), (3.19) and the transport
equations. |K|≲r controls the axis, so integrated equations pass. Trace error →0.
Uniformity of (4.1)-type remainders with Ψ_n→Ψ_* gives the incoming limit.

*Mass:* RESULT.md's hedge can be removed. m_v=(λ(1−μ)/2)(L−φ)² is algebraic in
quantities converging uniformly, so the integrated identity holds with no Φ′. The
INCOMING_MASS.md argument runs unchanged at Lipschitz regularity. *Wedge:* holds
for each approximant by the C11 §4 lemma, hence in the limit, once R1 holds. Under
the symmetric mollifier the sentence in §5 is unsupported. *Tail:* decoupling is
Repair A on {v≤t̄+2}, in its narrower class.

*Regularity gain:* correct. K_v, λ_v, φ_v are continuous off Γ, bounded, and tails
are uniform, so Λ, I∈C¹ by dominated convergence.

**R4. Stronger than §6 says.** The same domination gives (𝒯_nΨ_n)′ uniformly
convergent, so **Ψ_n→Ψ_* in C¹**, not merely C⁰. Then the linear transport (3.33)
and its u-side analogue from Γ make L, M continuous-differentiable in the limit.
So for y∈C¹ the limit should be a C¹ solution in the sense of Definition 2.1, not
just Lipschitz. Sketch only.

**6. Quantifiers: REPAIRABLE.**

*M_* and fine structure:* holds. With ℓ≤t̄+2, ε̃=max(1,ℓ^γ)M, since
M min(a,ℓ)≤Mℓ^γa^(1−γ). Only T_max and γ enter. A is not needed, and δ is not after
R1. The Claim never quantifies δ.

*Norm bookkeeping:* the Claim has ‖y‖≤M, while §2 needs ‖y‖≤M/2. Use a ball of radius
2M.

*E floor:* fine. Window mass is at most 1.5M²T_max, and the cut-off part is O(ε̃⁶),
absorbed for M_*(T_max) small. *Scope:* E is total, tail included; mass received by
readout time varies with y, as C11's banner says.

*E ceiling: false as proved.* The Claim says "E exceed", with no upper bound. The
tail is on the same cone, so it counts in (1.7). For fixed G, the proof reaches
only E below an E_*(G). Nothing in §5 addresses this.

**R2.** Tail G_K=Σ_{k=3}^Kχ(v−c−2^k), the finite truncation of LOY (5.1), with
c≥t̄+2 and amplitude β∈[0,ε′]. LOY's Step 1 gives parameter ≲_γ ε′ independent of K.
(1.7) is additive, so the total is ≲ε̃+ε′. Energy grows linearly in K, so every E
above the floor is reached with M_* and ε′ independent of E. G then depends on E.
Without R2, state E<E_*.

*Counterexample search:* none. Every y in the ball yields Φ in the ball by the
closure in §2, so no collapse occurs. Large |y′| at small scales is excluded by the
ball: this is why ε=0.6, ω=6π failing in §7 is not a counterexample. M_*→0 as
T_max→∞ is an artifact of (1.7), and it looks non-sharp.

**R3. C¹,¹ by a larger ball** (this is the repair of Gap 1 for y∈C¹,¹). Add
Lip(Φ′)≤a to B. It is still convex and compact, and J preserves it. LOY Prop 3.18
is linear in A=4sup|Φ″|, with ε₂ independent of A. By (3.44), (3.45), (3.49), (3.50),
(3.31), (3.55):

    Λ″=2λ_vv+2λK_v on Γ,  |Λ″|≲ε̃(A+ε̃),   |I″|≲ε̃²(A+ε̃).

Therefore |(𝒯Φ)″|≤‖y″‖+Cε̃²A+Cε̃³, and a=2‖y″‖+1 closes. The threshold does not see
y″. So Ψ_n is uniformly C¹,¹, and §4 of LOY plus AXIS_C11 applies, conditional on
Lemma 3.19 (sketched) and (3.46)–(3.47) (sketched), or on Repair B, which is
itself only partly checked. No order-by-order bootstrap and no circularity at this
level.

Sanity check, N=420, one domain, fixed |Φ′|≈1.88, ω=12.6, 25.1, 50.3. max|Φ″|=23.6,
46.5, 88.9. max|Λ″|=1.35, 1.20, 0.84. max|I″|=0.144, 0.069, 0.032. No growth, and
the last row has only about 7.5 points per wavelength. Not a proof.

**Why C¹ cannot suffice.** If g, φ are C¹,¹ near γ, then γ∈C²,¹ and φ∘γ∈C¹,¹. So
y∈C¹∖C¹,¹ admits no model in C11's category. C11 item 1, including unique central
geodesics from ODE theory, needs y∈C¹,¹. At bare C¹ the Claim's γ must be read as
the symmetry axis with clock τ; uniqueness among geodesics is then not available.

**7. Is the §6 gap list complete?** No. Ranked, with changes to RESULT.md's list
marked:

1. **New.** §4 invariance (R1).
2. **New.** E ceiling and tail in LOY's parameter (R2).
3. **Gap 1, revised.** C¹ y: impossible for C¹,¹. C¹,¹ y: R3. Lipschitz L: R4.
4. **Remaining from Gap 1.** Smooth y to smooth Ψ_*. SMOOTH_FINITE_CONTROL.md
   assumes smooth profiles; R3 stops at C¹,¹ since LOY has no uniform bounds past
   third order. Order-k bounds, linear at top order, are the missing input.
5. **New, trusted-input list.** RESULT.md understates this. Global existence rests
   on the omitted local theory and the continuity argument of §3.5. LOY's (3.3)
   prints φ where Prop 3.13 closes (rφ). The published version is uncompared.
6. **Gap 5, likely closable.** On compactly supported data A′ seems uniform in n:
   δ vanishes for v<A, so δm, δr are O(ℓW) rather than growing, and δK is integrable
   in s with weight r₊^(−1−γ). That would give a C⁰ contraction, no subsequences and
   continuity of y↦Φ. Not proved here; this is the best next target.
7. **Gap 3** shrinks to Repair A, per item 3 above.
8. **Gap 4 closed**; **Gap 2** closed for the first-order input: (3.32) sees no Φ″.
9. **New, minor.** "Exactly when", δ unquantified, the M/2 factor, wording of the
   gain, and §8's "small BV": ½∫|Φ′|≤½Mℓ needs M≲1/T_max, stricter than ε̃ small.
10. **Prior work.** AGENTS.md puts the audit first. Kehrberger arXiv:2105.08079 is
    unread and the nearest-predecessor question is open.

Proposed Claim, conditional on R1–R3 and the inputs above: fix T_max, γ. There is
M_*(T_max,γ) such that for δ>0 and y∈C¹,¹ vanishing on [0,A+2δ] and near T_max,
with ‖y‖_(C¹)≤M≤M_* and **no size condition on y″**, and every E≥cM²T_max, there
is a C¹,¹ model as in C11 with the tail R2. For y merely C¹ the conclusion is a C¹
reduced solution, subject to R4.

## Numerics

Reran volterra_check.py unchanged, 8.9 s: every row of RESULT.md's table reproduced.
Three cautions. It uses one domain, u₀=−4, so it says nothing about uniformity in n,
which is the point of the Claim. "Last ratio" is not a stable rate: row 4 gives
0.0030, 0.0013, 0.0091 in sequence. A rerun of row 4 at N=1120 gave the same early
residuals. The ω=18π row has about 9 points per wavelength at N=560.

## Read depth

- **LOY arXiv:1605.03893v1 HTML: full-text at these loci**, read as printed TeX from
  the page DOM (156,863 characters) in the built-in browser. Theorem 1.1, Remarks
  1.2–1.3, Theorem 1.7, §2.1 with Definition 2.1, (2.8)–(2.26), all of §3.1–§3.8
  including Lemma 3.19 and the (3.46)–(3.47) sketch, §4 through Remark 4.1, §5 Steps
  1–2 and the start of Step 3.
- WebFetch of the first 100,000 characters returned paraphrase, so it is not relied
  on, except that its report on (3.16) was checked against the DOM and rejected.
- **Not read:** §6, Appendix A, the published Ann. PDE version, Christodoulou 1993,
  Luk–Oh, Kehrberger. §8 of RESULT.md was audited only for the BV remark.
- **Reproduced by hand:** §1 identity, §2 bounds, §3 δ-table. R1–R4 are new, single
  reader, unreviewed. R3 and R4 are sketches.
