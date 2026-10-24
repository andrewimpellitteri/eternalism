# Energy-condition branch (H1′): status

24 October 2026. Exploratory; unreviewed. Builds on DRAFT.md.

## Question

Does Theorem 2 survive if becoming is required only on spacetimes with
physically reasonable matter? Category GH_DEC: GH spacetimes whose Einstein
tensor satisfies the dominant energy condition (G(X,Y) ≥ 0 for future causal
X, Y). Same morphisms. The class is closed under restriction to causally
convex open subsets, contains Minkowski, and contains every DEC M. A variant
GH_NEC uses the null energy condition.

## Result 0 (why other spacetimes are needed at all)

In a single spacetime M with no isometries, take spacelike x, b and
R = J^- ∪ (J^-(x) × J^+(b)) (pairs (e, z): "e has become for z"). R is
reflexive, contains I^-, relates x to b, and is transitive: J∘J ⊆ J; J∘P and
P∘J land in P by push-up; P∘P would need some q ∈ J^+(b) ∩ J^-(x), forcing
b ≤ x. So transitivity and chronological becoming inside one spacetime never
force collapse. Theorem 2's conclusion comes entirely from requiring the same
rule in other spacetimes. (This generalizes Codex's dust example.)
[Add to the main draft as Proposition 0.]

## Obstruction 1: the off-shell M′ is not available

The off-shell proof uses M′ = (R^4, g′), flat outside the spacetime-compact
set T_{3r}. In GH_DEC this is impossible unless g is flat on T_{2r}:
a slice {t = c} with c < −3r is a Cauchy surface on which g′ is flat and
T = G/8π vanishes. By the conservation theorem (Hawking & Ellis 1973, §4.3:
DEC + T = 0 on a closed achronal S ⇒ T = 0 on D(S); [CHECK exact statement
and hypotheses]), T = 0 on M′. A vacuum GH spacetime with flat data on a
Cauchy surface is flat: it is a development of the flat data, so by
Choquet-Bruhat & Geroch 1969 (CMP 14, 329–335; full text read), Theorem 3
(every development embeds isometrically in the unique maximal development),
it embeds in the maximal development of flat data, which is Minkowski space
(listed among their examples of maximal developments, after Corollary 1).
VERIFIED. The DEC step (Hawking–Ellis §4.3) is still unverified: the book was
not available. Contradiction with curvature on T_{2r}.

For GH_NEC there is no conservation theorem, but rigidity results for
compactly supported NEC perturbations of Minkowski are expected
(null splitting: Galloway 2000, DOI 10.1007/s000230050006; time delay:
Gao–Wald). [Not checked; do not cite as a theorem yet.]

**Linearized NEC rigidity (proved at linear order; likely known).** Let
g = η + h with h compactly supported, and k a constant null vector. Linearized
Ricci: R_kk = (k·∂)(∂_c h^c_k) − ½ □h_kk − ½ (k·∂)² h. Integrating along the
null line x0 + λk, the (k·∂)-derivative terms vanish (compact support), and in
null coordinates □ = −4∂_u∂_v + Δ_⊥ with the line along v, so
∫ R_kk dλ = −½ Δ_⊥ H, where H(u, x_⊥) = ∫ h_kk dv is the light-ray transform.
Linearized NEC (R_kk ≥ 0) gives Δ_⊥ H ≤ 0 with H compactly supported in
x_⊥ ∈ R²; since ∫ Δ_⊥ H dx_⊥ = 0, Δ_⊥ H ≡ 0, so ∫ R_kk dλ = 0 along every null
line, and with R_kk ≥ 0 this forces R_kk ≡ 0 for all null k. Then
R_ab = φ η_ab, and the linearized contracted Bianchi identity gives ∂φ = 0, so
φ = 0 by compact support: R_ab = 0. A compactly supported linearized vacuum
perturbation has R_abcd satisfying □R_abcd = 0 with compact support, so
R_abcd = 0 and h is pure gauge. Conclusion: at linear order, NEC also forbids
curvature confined to a spacetime-compact region of Minkowski, so the off-shell
M' fails in GH_NEC as well, and NEC versions also need pockets. The nonlinear
statement is expected (null splitting / time-delay arguments) but not proved
here. [Check literature before claiming; this is the kind of fact that is
probably standard.]

## Obstruction 2: flat pockets must be fed from the past

Alternative: keep M and insert small flat pockets (near w ≪ x, near b ≪ v,
and along the detour) instead of flattening everything outside the tube.
Conservation theorem again: if, on some Cauchy surface S* below a would-be
pocket U, the original M is vacuum on S* ∩ J^-(U) and S* is unmodified there,
then T′ = 0 on U, so the modified spacetime is vacuum near U with the same
data, hence equal to M there. No pocket can then be inserted. So a pocket in
a vacuum region requires matter brought in from the past along routes
outside D(Σ). Matter cannot vanish afterwards, so its future worldlines must
also be routed around D(Σ).

## Reformulation: the pocket problem

(P) Given a DEC spacetime M, a thin compact acausal slab Σ around a spacelike
curve from x to b, and the three target sites (below x, above b, along a
detour avoiding D(Σ)), find a DEC GH spacetime M′ such that:
(i) a neighbourhood of D_M(Σ) embeds isometrically, and its image is a domain
    of dependence in M′;
(ii) M′ contains exactly flat causally convex regions containing points
    w ≪ x and v ≫ b, joined by a flat domain of dependence of a slab.

Theorem 2 holds for GH_DEC if (P) is solvable for every such configuration
(same proof as DRAFT §3.2, with Lemma D applied to pockets instead of to the
complement of the tube).

## Why (P) is plausible, and what is hard

- Only an inequality (DEC) and the Bianchi identity constrain M′, not field
  equations for a fixed matter model; constructions can be kinematic.
- Explicit DEC models with flat regions adjacent to curved ones exist: Vaidya
  spacetimes are flat before an incoming null-dust shell arrives and, for
  outgoing radiation with dm/du ≤ 0, flat after it leaves.
- Riemannian analogue (time-symmetric data, DEC ⇒ R ≥ 0): flattening a ball
  inside a region with R ≥ 0. The Shi–Tam inequality (DOI 10.4310/jdg/1090425530)
  is a candidate obstruction but is already satisfied by the original metric,
  so it does not obviously forbid flattening. Corvino–Huang (arXiv:1606.03078)
  give DEC-preserving compactly supported deformations of initial data
  (abstract depth only).
- Hard parts: building the pocket and its feeding matter as one global DEC
  geometry, keeping global hyperbolicity, and keeping (i). Null-shell junctions
  need matching intrinsic geometry on the shell, which arbitrary curved regions
  do not have, so thin shells alone will not do; smooth matter layers are
  needed.

## Deliverable options

1. Theorem 2 for GH_DEC conditional on (P), with Obstructions 1–2 explaining
   why (P) is the real content. Achievable now.
2. (P) for a restricted class of starting spacetimes. Correction: this is
   not easier than it first looked. Even if M is symmetric, the pockets are
   local and break the symmetry, so symmetric starting data do not reduce
   (P) to an ODE problem. A genuinely tractable first case is still to be
   identified (candidates: M flat outside the tube's causal shadow; or the
   NEC class, which has no conservation theorem).
3. (P) in general. Genuinely new mathematical GR; uncertain.

## Sources still needed for this branch

Hawking & Ellis 1973, §4.3 (DOI 10.1017/cbo9780511524646): exact statement of
the conservation theorem. Choquet-Bruhat & Geroch 1969
(DOI 10.1007/bf01645389): uniqueness of the maximal development. Shi & Tam
2002 (DOI 10.4310/jdg/1090425530). Galloway 2000 (DOI 10.1007/s000230050006).
