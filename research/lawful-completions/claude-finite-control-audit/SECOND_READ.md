# Second read of the audit repairs

30 October 2026. Claude Code (Opus 5.5), reading RESULT.md in this directory
against the GLM submission on agent/lawful-finite-control-review (5d7e7e5). This
is a record for coordinator inspection, not acceptance. No novelty or
ontological claim.

## Where the two reviews agree

Both found no counterexample, and both name the same hardest point: LOY v1 omits
the characteristic uniqueness proof, and the identification S=S_x depends on it.
Both name the sketched u-side of Proposition 3.18 next. Agreement is not
evidence of correctness.

They differ in handling. The GLM review records uniqueness as an external risk
and lists a published-version comparison as the next task. RESULT.md here
replaces the step with Repair A. RESULT.md also states the scope more narrowly:
§2.1 is local, and Theorem 1.1's "unique" names no class.

## Repair A: checked, holds

Every line of the δ-table was re-derived by hand:

- L_u=K(φ−L), λ_u=λK, ν_v=νK′ and p_uv=λKφ.
- The same-u identities for r, φ, L−φ, m_v and ν, with ν(u,u)=−λ(u,u).
- δφ=O(W) as a ratio of integrals, with no loss at r=0.
- δ(L−φ)=O(rW), which is where δL_v in W and the bound |L_v|≤B are used.
- δm_v=O(r²W)+O(r)δm, hence δm=O(r³W) by Gronwall.
- δK=O(rW) and δK_v=O(W), and δν=O(W) from ∫δK′=O(r²W).

The only u-integrals are the three fixed-v displays, whose integrands at level s
are bounded by CW(s). So W(u)≤C(W(u₀)+∫W) is a genuine Volterra inequality and
not the rejected W≤δ+aW step. H_n is then Lipschitz in ‖Φ‖_(C¹) for fixed n.

Limits: the constant depends on the domain and may blow up in n, which degree
tolerates. The uniqueness class is the narrower one with ν<0 and 1−μ>0, which
both compared solutions satisfy. The bound on L_v comes from (1.9), so Theorem
1.1 stays a trusted input. This is a hand check of one proof, not a source result.

## Repair B: partly checked

Checked by hand: [∂_v,D]=−K′D, all three transport identities, M_v=K′(φ−M),
M=φ+rDφ, rD²φ=DM−2Dφ, rD³φ=D²M−3D²φ and D²φ=∫₀¹t²D²M(tr)dt. In flat space
p=g(v)−g(u) gives DM=−λ⁻¹L_v and D²M=(λ⁻¹∂_v)³p on Γ, as claimed.

Not checked: the bound |D²K′|≤C(1+Y), the closure Y(δ)≤a+C∫₀^δ(1+Y), the curved
axis identity Λ_uu=(log λ)_vv, and the C³-up-to-Γ regularity it assumes. Repair B
remains single-reader work. Until it is checked, or the published version settles
the point, the compact limit in C²/C¹ and the C¹,¹ metric still depend on the
sketched u-side of Proposition 3.18.

## State of the theorem

Conditional on Theorem 1.1, the printed v-side bounds and regularity persistence,
H_n continuity no longer needs the omitted uniqueness proof, given Repair A. The
compact limit, classical equations and C¹,¹ metric stay conditional as above. The
published Ann. PDE version has not been compared.

## Suggested coordinator text changes

These were not applied here.

- C11_FINITE_CONTROL.md §2: separate Theorem 1.1's unqualified "unique" from
  §2.1's local statement, and cite Repair A.
- COMPACTNESS_CONTINUITY_REPAIR.md step 4: point to Repair A.
- AXIS_C11_RECONSTRUCTION.md §6: a u-side failure would remove C11 item 1 unless
  Repair B holds, which is stronger than the current wording.
