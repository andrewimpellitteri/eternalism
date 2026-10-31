# Red-team review of CONTRACTION.md

31 October 2026. Claude Code (Opus 5.5), as an adversarial reader. A review for
coordinator inspection, not acceptance. Repairs and counterexamples below are this
reader's own, single-reader, and not LOY's. No novelty or ontological claim. LOY means
arXiv:1605.03893v1. "Rederived" means by hand here; it is not evidence of correctness
beyond that one reading.

## Verdict

**The difference estimate survives. No failing line was found in the Lemma, the
same-u table or the absorption. Two headline conclusions are false as literally
stated, and both have cheap repairs.** Consequences 1 and 2 stand, in sup norm and an
integrated class, conditional on Theorem 1.1. Consequences 3 and 4 stand only after
the repairs below.

**Strongest problem: "Φ is unique in the ball for each target y" (Consequence 4 and
§4) is false.** Banach gives one fixed point of 𝒯, which is a different statement.
Take y=0, Φ₁=0, and Φ₂ a small nonzero bump supported in (T_max,t̄+2). Then Φ₂∈B. Data
vanish on v≤T_max, so φ_c=0, Λ=1 and τ=t there, and φ(γ(T))−φ(b)=0 for all
T∈[0,T_max]. Both reach y=0. For y≠0, add such a bump after t_*, where τ(t_*)=T_max,
to any fixed point; the ball has room, since ‖Φ_*‖≤(1+O(M²))M. RESULT.md §1 warns of
exactly this: a fixed point also fixes Φ beyond the window.

Ranked findings:

1. Consequence 4: uniqueness of Φ for y. **False as stated**, R1.
2. Consequence 3: the class omits the gauge. **False as stated**, R2.
3. §4 never states 𝒯_∞:B→B, and Banach needs it. True, but rests on more than §5 says, R3.
4. Line 42 names the wrong place where compactness is decisive, R4.
5. Limit class and the missing M row, R5.
6. Bookkeeping notes, listed at the end.

| # | Item | Verdict |
|---|---|---|
| 1 | Hypotheses (B1)–(B4), K | **VERIFIED**, with wording fixes |
| 2 | Same-u table | **VERIFIED** |
| 3 | δK and the weight | **VERIFIED** |
| 4 | Absorption | **VERIFIED**; one constant is C_ℓ |
| 5 | Different vertices | **VERIFIED**; norm stated below |
| 6 | Density, S_∞ on Lipschitz data | **REPAIRABLE** (R5) |
| 7 | Uniqueness at past null infinity | **REPAIRABLE** (R2) |
| 8 | Contraction | Estimates **VERIFIED**; conclusion **REPAIRABLE** (R1, R3) |
| 9 | Conflicts with known results | **No conflict found**, in the scope read |

## Repairs

**R1. Uniqueness of Φ.** State: 𝒯_∞ has a unique fixed point in B, and two fixed
points obey ‖δΦ‖≤2‖δy‖. For the inverse problem state the causal version. If Φ₁,Φ₂∈B
both satisfy φ_c=y∘τ for τ≤T_max, then Φ₁=Φ₂ on [0,t_*], with one common t_*. Proof:
put T=min(t₁,t₂). On [0,T], Φᵢ=Λᵢy∘τᵢ−Iᵢ. The Lemma on {v≤s}, for each s≤T, gives
sup_{t≤s}|δΦ|≤½sup_{t≤s}|δΦ|. So Φ₁=Φ₂ on [0,T], then τ₁=τ₂ there and t₁=t₂=T. Past
t_* the profile is free, within the ball.

**R2. Gauge in the class.** The line "two solutions in this class ... so they agree"
fails if "exactly flat" means only the geometry, and §1 never defines it. Let f be
increasing, with f(x)=x for x≥A, f(x)=x+1 for x≤A−4, and f′∈[⅔,1]. Put
S̃(u,v)=S(f(u),f(v)), which solves the system by LOY Remark 2.2 and keeps u=v on Γ. On
v≥A, λ̃=λ(f(u),v) and L̃=L(f(u),v), so λ̃→½ and L̃→Φ uniformly on [A,V]. (B1)–(B3) and
flatness on v≤A persist, with λ̃=f′(v)/2 there. But r̃(u,A)=(A−f(u))/2≠(A−u)/2, so
S̃≠S as reduced solutions, and δ does not vanish on v≤A. They are isometric, so this
is a gauge failure. **Repair:** define flat as φ=m=0 and r=(v−u)/2 on v≤A, or require
λ→½ uniformly on all of v≤V. Flat means r=F(v)−F(u), so λ=F′(v)/2, and λ→½ on v≤A
forces F′=1.

With that, the class can be widened. The no-smallness route needs only that (B1)
holds and that L, φ are bounded. A C¹ solution with the stated limits gets (B3) with
some constant: near Γ only u≥A−C occurs, a compact set. Volterra then gives
W≤W₀exp(C_V(1+ℓ)). Line 90's kernel must be read as k(s)=sup_{v∈[max(s,A),V]}r₊(s,v)⁻²
≲min(1,(A−s)⁻²), integrable on (−∞,V]. This works because δ lives on v≥A. Uniqueness
then needs no LOY input at all, only the normalized wedge.

**R3. Invariance.** Add before "B is complete": 𝒯_∞ maps B to B. Support: for t<A+δ,
data vanish on v≤t, so Λ=1, τ=t, y(t)=0, I=0, and 𝒯Φ(t)=0 with no mollifier. Past
t̄+1, χ=0. Norm: RESULT §2's bound holds for smooth Φ uniformly in vertex and passes to
limits, since Lipschitz constants are lower semicontinuous under the sup convergence
of the Lemma. That bound uses |I′|≲ε̃³ and hence K_v, so (3.31) or (3.20), (3.30). So
§5's "Only the first-order bounds (1.8), (1.9) enter here" is true of §§1–3 but not of
Consequence 4. Those §3 bounds do derive from the same bootstrap; REVIEW.md flagged
the same overstatement in RESULT.md.

**R4. Line 42.** "This is the one place where compact data is decisive" is wrong
twice. Printed (3.24) with (3.7) already makes ∫|K|ds finite, so (B4) is not what
decides it; it only changes the drift rate. The decisive use is the left edge of δ, in
the min(r,ℓ) of the δr, δp, δm rows. Without it δm≲ε̃rb, so δm/r²≲ε̃b/r, whose
s-integral diverges logarithmically. Right compactness is not used: on {v≤V} the Lemma
sees only Φ on v≤V. So R2's tails in RESULT.md do not disturb 𝒯, which reads v≤t̄+2.
Across a long tail, C_ℓε̃²≤¼ may fail, and only the Volterra form of line 90 applies.

**R5. Limit class.** For merely Lipschitz Φ, L is not C¹ in v, so S_∞(Φ) is outside
LOY Definition 2.1 and outside the Lemma's literal "C¹ reduced solutions". Restate the
Lemma for the integrated system, which is all the proof uses. Also, M=ν⁻¹p_u is not
"algebraic in" λ, L. It is an integral: p_u=−λL(u,u)+∫_u^vλKφ dv′ for u≥A, and
p_u=∫_A^vλKφ dv′ for u<A. Add that row; δM≲X+C_ℓε̃²b. Then (2.7) and (2.11) pass to the
limit too. Without it, §4 does not cover them.

## Point-by-point audit

**1. Hypotheses: VERIFIED.** (B1): (1.8) gives the lower bound on λ, both bounds on ν,
and 1−μ>½. λ≤½ is (3.4), not (1.8). (B2): (1.9) with λ≥⅓ and (1.7). (B3), r≤1: from
(1.9), |(λ⁻¹∂_v)²p|≲ε, then (2.21) gives |λ⁻¹φ_v|≲ε, and L−φ=rλ⁻¹φ_v by (2.23). This
is (3.12), and it consumes ‖Φ′‖ through ε̃. r≥1: (B2).

(B4): m_v≲ε̃²min(r²,1), from 0 at v=A for u<A, or from m(u,u)=0 for u≥A, a case line
37 omits. Over an interval of length ≤min(3r,ℓ), this gives ε̃²min(r³,ℓ). Bounded for r
large: yes, on v≤V. It is weaker than printed (3.16) for r≲ℓ and stronger for r≫ℓ; no
conflict. Every vertex u₀<A: yes; (1.7) with ε̃=max(1,ℓ^γ)‖Φ‖_Lip is independent of
u₀. The Lemma should say u₀<A. K: |K|≲m/r²≲ε̃²min(r,ℓ/r²)≤C_ℓε̃²min(r,r⁻²), C_ℓ=max(1,ℓ),
including u≥A, where r≤ℓ/2.

**2. Table: VERIFIED, each row rederived.** All rows are at one u, with X(u), Z(u)
treated as given. There is no hidden cycle: r, p, φ, then m by Gronwall in v, then ν,
then K.

- δr, δp: integrals from max(u,A), with |δλ|≤½|δlogλ| since λ≤½. r(u,A) and p(u,A)=0
  match by flatness, and for u≥A both start from Γ.
- δφ: δp/r−φδr/r gives min(1,ℓ/r)b. No loss at r=0.
- δm: m_v=½(1−μ)λ(L−φ)² is linear in δ(L−φ) with weight ε̃ϱ, and (L−φ)² carries ε̃²ϱ².
  Z there is absorbed in ε̃ϱb. m|δr|/r²≤¼|δr|/r≲Z by μ≤½, so large r is safe. The
  Gronwall exponent is Cε̃²∫min(r,1/r)dv≲ε̃²(1+log₊ℓ), bounded uniformly in u, including
  u<A. It belongs in C_ℓ. Forcing integrates to ε̃min(r²,ℓ)b.
- δlog(−ν): for u<A the base is exact and there is **no** Z; for u≥A it is Z from
  ν(u,u)=−λ(u,u). ∫δK′≲C_ℓε̃b.
- min(r,ℓ) and r₊ mix consistently: min(1,ℓ/r²)≤C_ℓr₊⁻².
- u≥A: integrals run from Γ, r≤ℓ/2. Same bounds.

**3. δK: VERIFIED.** r≤1: δm/r²≲ε̃b; (m/r²)δν≲ε̃²r(Z+…); m|δr|/r³≲ε̃²rZ. r~1: no
degeneration. r large: m|δr|/r³≲ε̃²ℓ·min(r,ℓ)Zr⁻³≲C_ℓε̃²Zr⁻², and if r>ℓ it is better,
r⁻³. δν's bare Z is harmless, since it enters with m/r²≲C_ℓε̃²r₊⁻² and gives ε̃²Z. The
ε̃³C_ℓ²b term from δν uses C_ℓε̃²≤¼ to fold in. Weight: ∫_{u₀}^v r₊(s,v)⁻²ds≤C by (3.7)
with k=2; near Γ, r₊=1 on length O(1). Uniform in vertex, and in ℓ. Literal note:
line 71's "δK does not vanish at r=0" is false of δK, since K₁=K₂=0 on Γ. It is the
bound that does not vanish.

**4. Absorption: VERIFIED.** The inequality at (u′,v), u′≤u, has integrand bounded by
X(s), Z(s), and X̄, Z̄ are monotone in u. Finite: |L|≲ε̃ and λ∈[⅓,½]. C_ℓ depends on ℓ
and γ only, not on X, Z, u₀. log λ uses (2.8), L uses (2.6). Z̄ covers all v, since
Z(s) is a sup over v and δ=0 for v≤A. Solving: X̄≤(3/2)X₀+2C_ℓε̃³Z₀ and
Z̄≤(3/2)Z₀+2C_ℓε̃X₀, using C_ℓ²ε̃⁴≤1/16. Line 86's "Cε̃³" should be C_ℓε̃³.

**5. Different vertices: VERIFIED.** On v≤A both solutions are flat with r=(v−u)/2,
so r, ν, p, m match exactly there. No matching on v>A is needed: the table never uses
the gauge on C_{u_n}, and §5's worry on this is empty. Drift: for v≥A,
∫_{u_m}^{u_n}C_ℓε̃²r⁻²ds≲C_ℓε̃²/(A−u_n), and with |φ−L|≲ε̃ the L drift is ε̃³C_ℓ/(A−u_n).
Both agree with LOY's §4 remainders in form. Inserting these in §3 gives
sup|δL|≲C_ℓε̃³/(A−u_n) and sup|δlogλ|≲C_ℓε̃²/(A−u_n) on {u≥u_n}, and r, ν, m, φ follow
by the table. The norm is sup on {u_n≤u≤v≤V}: no S_n is defined on all of {v≤V}, so
"Cauchy on {v≤V}" means this.
The limit has uniform rates λ→½, L→Φ, sharper than LOY's pointwise (4.1) for this class.

**6. Density: REPAIRABLE (R5).** Approximants: J_ηΦ with the retarded mollifier of
REVIEW.md R1 stays in the ball, keeps the wedge and moves the right edge by η, so take
V larger. The bound is in ‖δΦ‖_{C⁰} alone, so S(Φ_k) is Cauchy. (B1)–(B3) are closed.
log(2λ)=∫_{−∞}^uK and L=Φ+∫_{−∞}^uK(φ−L) pass by domination with r₊⁻², and K=O(r) at
Γ. m_v, ν and r pass by the table. So the mollifier moves into the density step
rather than disappearing, which is harmless. Line 20's "replaces ... compactness" holds
only for the integrated class; §5 concedes this.

**7. Uniqueness: REPAIRABLE (R2).** Given the normalized wedge the proof is right:
X̄_{u₀}(u)≤2X(u₀)+C_ℓε̃³Z(u₀)→0. It does not need "conditional on the same inputs".

**8. Contraction: estimates VERIFIED; conclusion REPAIRABLE.** |δΛ|≤Z̄≲C_ℓε̃‖δΦ‖.
δτ integrates only over t≥A+δ, so |δτ|≲ℓC_ℓε̃‖δΦ‖. δI=δΛφ_c+(Λ−1)δφ_c+δ∫K(φ−L), which
is ≲C_ℓε̃²‖δΦ‖ term by term; δφ_c=δL on Γ. The sum is C_{ℓ}(1+ℓ)M²‖δΦ‖ up to κ below.
Two targets: δΦ=[𝒯_{y₁}Φ₁−𝒯_{y₁}Φ₂]+χΛ(y₁−y₂)∘τ₂, and Λ≤1, |χ|≤1 give the factor 2.
Both y need ‖y‖_{C¹}≤M.

M_* is not circular: fix T_max, γ, then ℓ≤t̄+2, then κ=max(1,ℓ^γ), then ε̃=2κM; the four
conditions (ε̃≤ε₁(γ), C_ℓε̃²≤¼, the closure 2M bound, contraction ≤½) are inequalities
in M alone. No A, δ enters, given C_ℓ monotone in ℓ. The O(M²) rate needs ‖y′‖≤M, not
y″. It does need B's Lipschitz bound.

**9. Conflicts: none found.** Examined:

- LOY footnote 11 and (1.20) say the u₀→−∞ procedure needs a Φ″ assumption. That
  concerns their C² compactness and classical limit. Here the limit for Lipschitz Φ is
  integrated, so there is no contradiction.
- Theorem 1.7 asserts existence and states no uniqueness, so Consequence 3 is not
  contradicted. Every compact-limit LOY solution with this data lands in the class, so
  all such limits coincide with S_∞.
- (3.14): L≈Φ/(2λ) amplifies by up to 3/2; X̄≤(3/2)X₀ is consistent.
- Zero-background scale test by hand: Φ₁=0, |Φ₂|≤d, Lipschitz ε, gives
  K₂≈min(ε²r,d²/r), peaking at εd, which saturates the ε̃b bound. So the near-axis rate
  is the true one, not an artifact. ∫K₂≈d²log(ε/d)≪εd.
- Scale invariance: C_ℓ breaks it through r₊, so the ℓ-dependence is non-sharp, as
  RESULT.md §6 item 7 says. Not an inconsistency. C_ℓ≈max(1,√ℓ) looks attainable for
  the δm/r² term; unneeded.
- No collapse example lies in the ball, given Theorem 1.1. Christodoulou 1993 was not
  read, so agreement with BV theory is unchecked.

## Numerics

Scripts were run from the scratchpad with bytecode off; nothing was added to the
repository. **Grid checks on one domain, not proofs.**

`uniformity_check.py`'s output was reproduced, split into runs under 10 s: 1.158, 0.546;
1.161, 0.555; 1.163, 0.561; distances 7.035e−4, 4.864e−4, 2.929e−4. All match §6. Three
notes:

- max|Φ′|≈2.66 for that base profile, far outside any ball where ε̃ is small. §6 says
  "amplitude 0.3", which hides this. The table says nothing about the claimed regime.
- a=2 predicts 1.50 and **1.70**, not 1.69. a≈2.3 fits better: 1.45, 1.67.
- The Lemma's rate is 1/(A−u₀) with A=1 in the script, so a≈2 is plausible only as a
  weighted v. The script does not test the constant.

New adversarial pairs, using `volterra_check.evolve`, in the ratio pair
sup|δφ_c|/sup|δΦ|, sup|δlogΛ|/sup|δΦ|:

| Pair | u₀ | Ratios |
|---|---|---|
| aligned, Φ₂=1.05Φ₁, e=0.4, 0.2, 0.1 | −3 | 1.090, 0.334; 1.021, 0.146; 1.005, 0.071 |
| Φ₁=0, d sin(ωv), dω≈0.1, ω=5…40 | −3 | ≈1.000; 0.0144, 0.0100, 0.0065, 0.0041 |
| fixed Lip 0.64, ω=30 perturbation | −3, −6, −12 | 1.0069, 0.0381; 1.0074, 0.0387; 1.0077, 0.0391 |

The aligned rows halve with e, matching Z̄≍ε̃‖δΦ‖, so that rate looks sharp, not an
overestimate. The drift with u₀ in the last row is about 0.001. Nothing exceeded the
bounds.

## Bookkeeping

- Line 35: "(B1) is (1.8)" needs (3.4). Line 37 needs the u≥A case. Line 28 needs u₀<A.
- "Only the first-order bounds" includes second derivatives in (1.9); the label is
  RESULT.md's, but it reads oddly here.
- CONTRACTION.md has no read-depth label for LOY, as AGENTS.md requires.
- Prior work is not audited. Kehrberger arXiv:2105.08079 stays unread, so the C⁰
  scattering map and uniqueness statements may be known. This review claims nothing there.

## Unresolved

- Theorem 1.1 stays a trusted input, with its omitted local theory, its continuity
  argument and (3.3)'s printed φ. Nothing here reproduces the bootstrap.
- R1–R5 need a second reader, and so does the table: this review is one reading.
- C¹ regularity of the fixed point for y∈C¹ looks immediate from Λ, I∈C¹, in place of
  R4 of REVIEW.md. Not checked in detail.

## Read depth

**LOY arXiv:1605.03893v1 HTML: full-text at these loci**, printed TeX from the page DOM
in the built-in browser (149,840 characters after replacing math by its alttext; the
count depends on extraction). Theorem 1.1, Remarks 1.2–1.3, Theorem 1.7 with footnote
11, §2.1–§2.3 with (2.1)–(2.26), §3.1–§3.6, §3.7 through (3.43) and the start of the
(3.38)–(3.39) proof, §4 through Remark 4.1, §5 through the start of Step 3. The rest of
§3.7 was not read here. **Not read here:** §3.8 (so Prop 3.18 and R3 of REVIEW.md rest
on earlier reads), §6, Appendix A, the published version, Christodoulou 1993, Luk–Oh,
Kehrberger. WebFetch was not used. AGENTS.md research standards read.

**Reproduced by hand:** every table row, (B1)–(B4), absorption, drift, δΛ, δτ, δI and
the two-target bound. **Code-audited:** `uniformity_check.py` and `volterra_check.py`,
read and rerun, with the solver not independently reimplemented.
