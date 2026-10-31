# Adversarial review of Repair B

30 October 2026. Claude Code (Opus 5.5), attacking `RESULT.md`, section "Repair B:
u-side third order on compact triangles". Hand derivations here are single-reader
work, not reviewed and not attributed to Luk–Oh–Yang (LOY). Coordinator inspection
is still required. No novelty or ontological claim.

## Verdict

**REPAIRABLE. The estimate survives every attack; its regularity premise does not
stand as written.** No counterexample and no gap in the a priori bound. Points 1,
2, 3 and 5 are VERIFIED, with wording corrections. Point 4 is REPAIRABLE. The
result stays conditional on the inputs listed at the end.

**Strongest problem: Y<∞ is assumed, not derived.** Y(δ)≤a+C∫₀^δ(1+Y) says nothing
if Y=∞. Finiteness of Y is exactly continuity of D²M up to Γ, and RESULT's only
support is "the same persistence claim LOY make at k=2". That claim is one sentence
in §3.8, with its proof omitted, about this same u-side quantity. Proving it from
the a priori bounds of Prop 3.18 would be circular, because Repair B needs the
regularity to reach those bounds. Two non-circular routes are given under point 4.
So Repair B removes the *quantitative* sketch, not the *qualitative* u-side input,
until one of those routes is adopted.

| # | Point | Verdict |
|---|---|---|
| 1 | Curved axis identities and transfers | **VERIFIED**; two reasons in RESULT need correcting |
| 2 | \|D²K′\|≤C(1+Y) | **VERIFIED**; the quadratic term is linear, and avoidable |
| 3 | Closure in δ | **VERIFIED** given Y<∞; not circular |
| 4 | Regularity up to Γ | **REPAIRABLE** |
| 5 | Uniformity in vertex and x | **VERIFIED** on compact triangles |

Notation as in RESULT, plus E=λ⁻¹∂_v, Q=K′/λ=K/ν, P=2m/r², Θ=λ/(1−μ). Then
K′=ΘP, and K,K′=O(r) on compact sets by (3.16) and (1.8).

## 1. Curved axis identities: VERIFIED

Direct commutation gives [D,E]=Q(D−E). Off the axis, exactly,

    EM = Q(φ−M) = −Q r Dφ,      DL = Q(φ−L) = −Q r Eφ.

Both are O(r²), so their first derivatives vanish on Γ. On Γ, E−D is tangential,
so (E−D)^ℓ p=0 for ℓ≤3 (LOY (2.16)).

- ℓ=2: E²p+D²p=EM+DL=0 on Γ, so **DM=−λ⁻¹L_v**.
- ℓ=3: the six mixed words are E(EM), E(DL), D(EM), D(DL), DEL and EDM. The last
  two reduce to the first four plus Q×bounded by the commutator. All vanish on Γ,
  so **D²M=E³p=(λ⁻¹∂_v)³p**.
- Second tangential derivative of Λ−log λ=0, with Λ_v=K′ and (log λ)_u=K:
  Λ_uu−(log λ)_vv=−2K′_u−K′_v+K_u+2K_v=−3λ(Q_u+Q_v)=0 on Γ. Here Q∈C¹ up to Γ and
  vanishes on it, by DP=2G−2P/r and its v analogue. So **Λ_uu=(log λ)_vv**.

The quantity consumed is D²Λ, not Λ_uu. With Λ_u=(log λ)_v on Γ, this gives
D²Λ=E²log λ on Γ, which is the form (3.45) bounds.

**Corrections to RESULT (conclusions unchanged):**

1. "All mixed terms vanish there since K,K′ vanish" is the wrong reason at third
   order. EQ≠0 on Γ in the curved case, so a term such as (EQ)(φ−M) dies because
   φ−M=0 on Γ, not because K′=0. The O(r²) form above is the correct reason.
2. "Confirmed independently" overstates. r_uuu=−r_vvv needs r_uuv+r_uvv=0 on Γ,
   which is λν(Q_u+Q_v)=0, the same input. It is a restatement, not a second proof.

## 2. |D²K′|≤C(1+Y): VERIFIED

RESULT's route is sound. rG″ contains r(D²φ)²=(rD²φ)D²φ and DφrD³φ=Dφ(D²M−3D²φ).
Since rD²φ=DM−2Dφ, |rD²φ|≲ε̃ by (3.37)–(3.38), proved in Prop 3.16 with no third
order input. So the term is linear in Y, with no Riccati growth.

A shorter route needs neither D³φ nor the quadratic term. Integrating by parts once
in t, and using (2.13) and Dr=1:

    DP  = 2G − 2P/r,     DK′ = Θ(Dφ)² − 2K′/r,
    D²P = 2DG − 4∫₀¹t³ DG(tr) dt,
    DG  = −½(2rG−P)(Dφ)² + (1−μ)Dφ D²φ,
    D²K′ = PD²Θ + 2rΘ(Dφ)²DP + ΘD²P,
    D²Θ = Θr²(Dφ)⁴ + Θ(Dφ)² + 2ΘrDφD²φ.

The DK′ formula reproduces LOY's printed ∂_v(ν⁻¹∂_u log ν) identity in the proof of
(3.39). Here P/r=2m/r³ is bounded by (3.16), and |D²φ|≤(1/3)sup_line|D²M|. No
division by r survives: 6P/r²−4G/r is the averaged term above.

## 3. Closure: VERIFIED given Y<∞; not circular

The source can be put in closed form, with no D²K′ at all:

    ∂_vD²M + 3K′D²M = 3DK′Dφ − 2DK′DM + 3K′D²φ
                      − Θr²(Dφ)⁵ − Θ(Dφ)³ − 3Θr(Dφ)²D²φ.

- **Regions.** For (u,v)∈T with v−u≤δ: the fixed-u segment to (u,u) has v′−u≤δ, and
  each fixed-v′ segment from (u,v′) to (v′,v′) has v′−u′≤v′−u. Both stay in T.
- **Integrating factor.** m≥0 from (2.10), with λ>0 and 1−μ>½ from (1.8). So K′≥0
  and exp(−3∫K′)≤1 for transport forward in v from Γ.
- **Form.** The source at (u,v′) sees only a fixed-v′ sup, bounded by Y(v′−u). So
  |D²M(u,v)|≤a+C∫₀^(v−u)(1+Y(s))ds. Y is monotone, hence measurable, and Gronwall
  gives Y(δ)≤(a+Cδ)e^(Cδ). This is a Volterra inequality in δ.
- **Circularity.** a comes from (3.44), whose proof and Lemma 3.19 are printed before
  the sketch and do not use (3.46)–(3.47) or (3.57). C comes from (1.8)–(1.9), (3.16)
  and Prop 3.16. D²Λ then follows from its transport, with data from (3.45).

The dependence is sideways: (u,v) sees (u′,v′) with u′≥u, v′≤v, which is spacelike.
That is legitimate as an estimate on an existing solution, but this inequality
cannot produce regularity, so point 4 cannot be avoided.

**By-product, single-reader.** With the closed source, the weights in (3.17), (3.37),
(3.38) and |rD²φ|≲ε̃ give ∫|source|dv≲ε̃³+ε̃²Y, so absorption yields (3.46) on all of
D(u₀,v₀) with no Gronwall. The D²K′ formulas give min{1,r⁻²} decay and then (3.47).
This suggests the printed sketch is sound at the a priori level. It was checked once,
by hand, and still needs Y<∞.

## 4. Regularity: REPAIRABLE

**What is needed.** RESULT's "C³" means LOY's k=2: L,M,log λ,log ν∈C² and φ∈C² up to
Γ. That is enough. DM∈C¹, and ∂_vDM=−2K′DM+3K′Dφ−Θr(Dφ)³ is C¹ in u, so Peano's
form of Schwarz gives ∂_vD²M and the closed transport. No fourth derivative of p or
r is required.

**What is available.** Only two printed sentences: "routine persistence" in §3.8,
and the local statement after (2.5) with proof omitted. RESULT lists the first as
trusted input 4, so it has not concealed anything, but the claim is unproved in the
source and RESULT gives no argument. `SMOOTHNESS_BOOTSTRAP.md` cannot fill this: it
addresses the selected limit, which is built from compactness that itself consumes
these bounds, so citing it for approximants would be circular.

**Repair R1, continuation by the outgoing norm.** Let u* be the supremum of ū such
that S is k=2 on Q_[u₀,ū]. Prop 3.18's (3.44) proof localizes to {u≤ū}, since both
of its integration lines stay there and the sup is finite on compact pieces. Under
Remark 2.2 with ũ=f(u), ṽ=f(v), f′=2λ(ū,·), we get ∂_ṽ=½E on the new cone, so the
regauged data have C² norm controlled by |L|,|EL|,|E²L| alone. Hence (3.10), (1.9)
and (3.44) bound it uniformly for ū<u*. The printed local theorem at k=2 then gives
a slab of uniform thickness, and Repair A identifies that solution with S, so
u*=∞. No u-side third-order bound is used. Cost: it consumes the printed local k=2
statement, whose omitted proof is where the u-side regularity at Γ now lives.

**Repair R2, u-regularity from v-regularity, for smooth Φ.** This is the sharper
route, and the family is smooth (C11 §3). Use hat variables f̂(u,w)=f(u,u+w). The
same-u identities of Repair A, with M_w=K′(φ−M), M(u,0)=L(u,0), ν(u,0)=−λ(u,0), make
M̂ and ν̂ values of a u-independent map 𝓜 of (L̂,log λ̂)(u,·). It is Fréchet smooth
Cʲ→Cʲ for j≥1 (Hadamard division costs one derivative only in K̂, Cʲ→Cʲ⁻¹). Also

    ∂_uL̂ = ∂_wL̂ + K̂(φ̂−L̂),     ∂_u log λ̂ = ∂_w log λ̂ + K̂.

If L̂ and log λ̂ lie in C⁰_uC³_w, induction gives C^i_uC^(3−i)_w for i≤2, and
composing with 𝓜 gives M̂,Λ̂∈C²(u,w), including w=0. So k=2 up to Γ reduces to pure
v-derivatives through third order of L and log λ. That is an outgoing-only statement,
provable by the linear E^j analogue of (3.44) and Lemma 2.6, with no axis transfer
and no u-side input. Those linear bounds were sketched here, not written out.

Either way the bound is only qualitative, so its size never enters Y's final bound.

## 5. Uniformity: VERIFIED on compact triangles

Take u_n≤a and v₀≥b. Then T⊂D(u_n,v₀) and both line families stay in T. The bound
is sup_T|D²M|≤(a₀+C(b−a))e^(C(b−a)), with a₀≲A+ε̃. Here C depends only on γ and
ε̃≤ε₂, by Remark 1.2 and the "independent of u₀,v₀,A" clause of Prop 3.18, and
A≤4ε sup_x‖f_x″‖∞ on the compact parameter ball.

**Correction to RESULT.** "Because transport starts on Γ, not on the cone" is the
wrong reason: the axis data come through (3.44), which is transported from the
cone. Uniformity holds because A and the lower-order bounds are uniform.

**Lost compared with the printed statement:** smallness ε(A+ε), and uniformity in
b−a. AXIS §1 and C11 consume boundedness on compact sets only, so this is harmless.
The by-product in point 3 would recover both.

## Evidence

- **Hand derivation** of everything above, including the two printed u-side identities
  in the proof of Prop 3.16 as cross-checks. Reader's own work, unreviewed.
- **Exact series check.** A curved formal germ at an axis point, with arithmetic in
  F_P, P=2⁶¹−1, total degree 8, two random data seeds, 0.54 s. Zero residual to the
  accurate degree for: DM+EL, D²M−E³p, Λ_uu−(log λ)_vv and D²Λ−E²log λ on Γ, both
  transports, the closed source, and the DK′, D²P and DG formulas. Six negative
  controls were all nonzero, including wrong signs, coefficient 2 for 3, and EQ on Γ.
  This tests algebra at one germ family. It proves no estimate and says nothing on
  point 4. The script was kept in the session scratchpad, not in the repository.

## Read depth

LOY arXiv:1605.03893v1 HTML. *Full-text at these loci*, read as printed TeX
annotations from the page DOM: Theorem 1.1, Remarks 1.2–1.3, §2.1 Definition 2.1
through Remark 2.4, §2.2 (2.6)–(2.16), §2.3 through (2.22) including Lemma 2.6, Prop
3.16 with proof, Corollary 3.17, all of §3.8, §4 through the opening of the (4.1)
proof. *Statements only:* (3.1), (3.3), (3.9)–(3.13), (3.16)–(3.17), (3.19)–(3.20),
(3.24), (3.31), (3.35). *Model-mediated, for location only:* WebFetch offsets 0 and
100000 of 223,736 characters; the rest of the page was not requested. **Not read:**
proofs of Props 3.3–3.14, §§5–6. Published Ann. PDE version: not read. Reproduced:
the identities above, not LOY's bootstrap.

## Still conditional on

Theorem 1.1; (3.16), (3.36)–(3.39); v-side (3.44)–(3.45), whose Lemma 3.19 is labelled
a sketch; and either the printed local k=2 theorem (R1) or outgoing-only persistence
(R2). R1, R2 and the closed source are this reader's own, and need a second reader.
R2's outgoing step is the place to attack next. Published-version comparison remains
open.

**Suggested text for RESULT.md (not applied).** Replace "Regularity: needs C³ up to Γ,
which follows from smooth Φ by the same persistence claim LOY make at k=2" with an
explicit R1 or R2, and make the three reason corrections above. In the u-side
dependence table, "none (B)" should read "none quantitative; qualitative k=2 via R1
or R2".
