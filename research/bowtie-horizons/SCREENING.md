# The causal-potential realm is exactly the screening region of b's future

28 October 2026, native Claude, task `bowtie-horizon-rationale` (addendum).
Answers the request at the end of
`research/lawful-completions/coordinator/PHILOSOPHICAL_SCOPE.md` for "a
precise obstruction to a proposed causal-potential realm". Proofs below are
ours and await independent review. No novelty claim.

> **31 October owner handoff (`claude-native-bowtie`):**
> `screening-review` has returned, but its claimed refutation of (L′) has an
> error: for its hyperbola S, D(S) is the open future light cone, not the
> closed region it reports. See the coordinator's
> [calculation and review disposition](../lawful-completions/coordinator/SCREENING_OWNER_HANDOFF.md).
> Theorem 3(b) remains conditional; neither (L′) nor the review's replacement
> (L″) is established by that handback. The full review is not accepted.

## Setting and definitions

(M,g) is a smooth, connected, time-oriented globally hyperbolic spacetime.
≤ is causal precedence; x ≺ y means x ≤ y and x ≠ y (null pairs included,
following C&R's `prec`). For an event b:

- pointy realm J⁻(b);
- causal-potential realm (RESULT.md §2)
  D_pot(b) = {b} ∪ {x : ¬(b ≺ x) and ∃z (b ≺ z and x ≺ z)};
- bow-tie realm D_BT(b) = M \ (J⁺(b)\{b});
- historical-potential realm H(b) = ⋃_{r≤b} D_pot(r) (coordinator).

Always J⁻(b) ⊆ D_pot(b) ⊆ H(b) ⊆ D_BT(b).

A realm R *screens* b's future if J⁺(b) ⊆ D⁺(Σ ∩ R) for every Cauchy surface
Σ (C⁰ allowed) disjoint from J⁺(b)\{b}. That is, on every slice not cutting
into b's strict future, R's trace meets every past causal curve from every
event of b's future.

## Lemma 1 (identity)

    D_pot(b) = J⁻(J⁺(b)) \ (J⁺(b)\{b}).

*Proof.* ⊆: b qualifies; otherwise x ≺ z with b ≺ z. ⊇: let x ≤ z with
b ≤ z, x ∉ J⁺(b)\{b}, x ≠ b. Then x ≠ z, so x ≺ z. If b ≺ z, z is the witness.
If z = b, pick z′ ∈ I⁺(b); push-up gives x ≺ z′. Also ¬(b ≺ x). ∎

So C&R's "causal potential to shape the future", read pointwise, picks out
exactly the events outside b's strict future that can causally reach some
event of it.

## Theorem 2 (screening characterization)

For R ⊆ D_BT(b): R screens b's future iff D_pot(b) ⊆ R.

*Proof.* (⇐) Let Σ be Cauchy and disjoint from J⁺(b)\{b}, z ∈ J⁺(b), and c
a past-inextendible causal curve from z. Then c meets Σ at some y ≤ z, and
y ∉ J⁺(b)\{b}. By Lemma 1, y ∈ D_pot(b) ⊆ R. So z ∈ D⁺(Σ ∩ R).

(⇒) Let x ∈ D_pot(b), with x ≤ z ∈ J⁺(b). Choose a Cauchy temporal function
t and constants c < min(t(x), t(b)) and C > t(x). Put P = I⁻(x) ∪ I⁻(Σ_c),
where Σ_c = {t = c}. P is an open past set.

*Σ := ∂P is a C⁰ Cauchy surface.*
- Achronal: if u ≪ w with u, w ∈ ∂P, the open set I⁺(u) contains w and so
  meets P at some w′. Then u ∈ I⁻(w′) ⊆ P, but u ∈ ∂P and P is open.
- Met by every inextendible causal curve: the curve has points with t < c,
  which lie in I⁻(Σ_c) ⊆ P, and points with t > C, which lie outside P
  because P ⊆ I⁻(Σ_C). By connectedness it meets ∂P.

*Σ passes through x and avoids J⁺(b)\{b}.* x ∉ P (chronology, and t(x) > c),
but x is a limit of points of I⁻(x), so x ∈ ∂P. Every point of ∂P lies in
J⁻(x) or in {t ≤ c}. Neither meets J⁺(b)\{b}: b ≤ y ≤ x with y ≠ b would put
x in J⁺(b)\{b} (if x = b, y = b), and t ≥ t(b) > c on J⁺(b).

*A curve from z meeting Σ only at x.* Take a causal curve from z to x, then
continue it past-directed and timelike from x; that continuation stays in
the open set I⁻(x) ⊆ P, so it misses ∂P. A point w ≠ x on the z–x segment
satisfies x ≺ w. It cannot lie in J⁻(x) (causality) or in {t ≤ c}
(t(w) ≥ t(x) > c). So the curve meets Σ only at x. If x ∉ R, it misses Σ ∩ R,
and z ∉ D⁺(Σ ∩ R). ∎

The timelike continuation matters: an achronal surface can contain null
segments, so an arbitrary continuation might meet Σ again.

## Theorem 3 (rigidity of the potential realm, no matched slice)

Let W_i = I⁻(I⁺(b_i)) \ J⁺(b_i), the open form of D_pot(b_i) minus the mark,
in globally hyperbolic (M_i, g_i). Suppose h: W₁ → W₂ is a time-orientation
preserving onto isometry carrying the fields, which extends to a
homeomorphism W₁ ∪ {b₁} → W₂ ∪ {b₂} with b₁ ↦ b₂. Let t₁ be a Cauchy temporal
function with t₁(b₁) = 0, Σ₁ = {t₁ = −1} and K₁ = Σ₁ ∩ W₁. Then:

(a) J⁺(b₁) ⊆ D⁺(K₁) and J⁺(b₂) ⊆ D⁺(h(K₁)), with h(K₁) acausal.

(b) Under premise (L) below, h extends to an isometry of J⁺(b₁) onto J⁺(b₂)
carrying the fields. Every well-defined proper-time reading along a
matched future geodesic from (b, u) therefore agrees.

**Premise (L′), localized maximal development for partial hypersurfaces.**
In the fixed deterministic theory, both M_i are maximal globally hyperbolic
developments. For every smooth, spacelike, acausal hypersurface S in such
an M (not necessarily part of a global Cauchy surface), D_M(S) is the
maximal globally hyperbolic development of the data induced on S, unique up
to isometry.

The partial-hypersurface form is needed. Part (a) shows only that h(K₁) is
a smooth acausal hypersurface screening J⁺(b₂), not that it is an open
subset of a Cauchy surface of M₂. A noncompact acausal spacelike
hypersurface need not extend to one: in 1+1 Minkowski space,
t = √(1 + x²) cannot be enlarged to a Cauchy surface (coordinator review,
CLAUDE_SCREENING_REVIEW.md, Finding 2). Two repair routes: prove that h(K₁)
lies in a Cauchy surface of M₂, or source/prove (L′). (L′) is a nontrivial
localization of Choquet-Bruhat–Geroch and is **unverified**. Leads:
Ringström's Cauchy-problem monograph; Sbierski arXiv:1309.7591.

*Proof of (a).*

1. *W is causally convex.* A causal curve from u ∈ W to w ∈ W cannot enter
   J⁺(b), or w would lie in it. Its points are ≤ w, so they lie in the past
   set I⁻(I⁺(b)). Hence causal and chronological relations and time
   separations among points of W are intrinsic to W, and h preserves them.
   In particular h(K₁) is acausal.

2. *h(I⁻(b₁)) = I⁻(b₂).* Let x ≪ b₁. Choose y₁ ≪ y_n on a timelike curve from
   x to b₁ with y_n → b₁. Then h(x) ≪ h(y₁) ≪ h(y_n) → b₂, so h(y₁) ∈ J⁻(b₂)
   (closedness of J⁺ in globally hyperbolic spacetimes). Push-up then gives
   h(x) ≪ b₂. The same argument for h⁻¹ gives equality.

3. J⁺(b₁) ⊆ D⁺(K₁) is Theorem 2 (⇐) applied to R = D_pot(b₁).

4. Let z ∈ J⁺(b₂) and let c be a past-inextendible causal curve from z.
   By non-imprisonment in the compact J⁺(b₂) ∩ J⁻(z), c leaves J⁺(b₂) at a
   last point e₂. Its past tail beyond e₂ lies in W₂ (step 1) and never
   returns. Let γ = h⁻¹(tail).
   - γ is past-inextendible in M₁. A past endpoint p would lie in the past
     set I⁻(I⁺(b₁)). It is not in J⁺(b₁), since then γ would be too. So
     p ∈ W₁, and h(p) would be a past endpoint of the tail in M₂.
   - If γ is also future-inextendible in M₁, it is inextendible and meets
     Σ₁, necessarily inside W₁. That is a point of K₁.
   - Otherwise γ has a future endpoint p ∈ M₁, with p ∉ W₁ (else
     h(p) = e₂ ∈ W₂). Take q_n → e₂ along the tail and p_n = h⁻¹(q_n).
     Since e₂ ∈ J⁺(b₂), we have I⁻(b₂) ⊆ I⁻(e₂). By inner continuity of I⁻,
     every compact C ⊆ I⁻(b₂) lies in I⁻(q_n) for large n. By steps 1–2,
     every compact C′ ⊆ I⁻(b₁) lies in I⁻(p_n) ⊆ I⁻(p). Hence I⁻(b₁) ⊆ I⁻(p),
     so b₁ ∈ cl I⁻(p) = J⁻(p) and p ∈ J⁺(b₁), giving t₁(p) ≥ 0.
     Since t₁ → −∞ along γ to the past, γ crosses Σ₁ at a point of K₁.
   In every case c meets h(K₁), so z ∈ D⁺(h(K₁)). ∎

*Proof of (b).* By (L′), D_{M₁}(K₁) and D_{M₂}(h(K₁)) are both the maximal
development of the same data. So there is an isometry Ψ between them that
agrees with h near K₁, and hence (first-order rigidity of isometries) on the
connected overlap containing J⁻(b₁) near b₁. Continuity gives Ψ(b₁) = b₂.
Domains of dependence are causally convex, so Ψ(J⁺(b₁)) = J⁺(b₂) by (a). ∎

Step 4's last case is what rules out the "boundary swap" worry of the
previous draft. A pulled-back curve cannot end on the horizon part
∂I⁻(I⁺(b₁)) of the realm's boundary. Its exit point in M₂ lies in the future
of b₂, and h transports "contains I⁻(b) in its past" across. The marked
event's chronological past does the work that the whole Cauchy surface does
in the bow-tie case.

The same pull-back argument reproves the coordinator's bow-tie lemma, with
U in place of W. For the historical realm H, the argument needs h(W₁) = W₂,
which is not automatic because W is defined through futures. H-rigidity is
therefore left open; a matched slice suffices as before.

## Classification

| Realm | Screens b's future (Thm 2) | Same realm ⇒ same future under determinism |
|---|---|---|
| J⁻(b) (pointy, Stein) | No (unless D_pot(b) = J⁻(b)) | No: lawful-completion pairs (Vaidya; coordinator scattering pair) |
| D_pot(b) | Yes, and it is the minimal screening realm | Yes, given homeomorphic extension of h to the mark and premise (L) (Thm 3) |
| H(b) | Yes | Yes, given a matched slice; open without it |
| D_BT(b) | Yes | Yes, unconditionally on the slice (BOWTIE_RIGIDITY.md) |
| Any R not containing D_pot(b) | No, by causal structure alone | Not settled by causal structure; dynamics-dependent |

The last row is deliberately weak. Failure of causal screening does not by
itself produce a different future; that needs actual dependence (response),
not mere reachability. In Huygens-type linear theories, for example,
perturbations at some causally relevant points never reach J⁺(b) (cf.
CONSTRAINTS_REVIEW.md §4).

Cross-check: the coordinator's slab condition for H (HISTORICAL_POTENTIAL.md)
d < 2(B − a) + σ − ξ equals RESULT.md Proposition 9's d < R_x + R_s + 2P_s,
since R_x + R_s + 2P_s = (B − ξ) + (B − σ) + 2(σ − a). The two derivations were
independent. The coordinator's a = −∞ case (H = D_BT) is an instance of
RESULT.md Proposition 8 (common past ⇒ x ∈ H(s)).

## What this does to the philosophical fork

PHILOSOPHICAL_SCOPE.md separates three bases: observer-accessible past data,
the ontology's existing concrete realm, and total admitted facts. Theorem 2
locates a **geometric screening boundary** inside the second base. Under the
uniqueness premises it is sufficient for physical determination, but it is
not the minimal physically determining set. Remove one interior point x
from W: smooth data agreeing on W \ {x} agree at x by continuity, so
determination is unaffected, yet screening fails (coordinator review,
Finding 1). With that caution:

- Taken literally, C&R's stated motivation for bow-tie ("what has the causal
  potential to shape the future") defines the minimal realm that screens off
  b's future. Under deterministic globally hyperbolic evolution (with the
  mark-extension and localization premise (L′)), that realm already fixes
  the whole of J⁺(b). So on their
  motivation, "nothing to come" coexists with full nomic determination of
  what is to come by what exists. Openness of the future cannot then be
  physical underdetermination by the existing realm. It must be purely
  ontological (non-existence) or come from non-deterministic dynamics.
- The pointy realm is the one that leaves the future undetermined relative
  to what exists. That is the content of the lawful-completion results.
- The screening boundary falls at D_pot, not at D_BT. Rigidity therefore
  does not favour
  bow-tie over the causal-potential realm or its historical repair H. In
  ΛCDM these three differ (D_pot ⊊ H ⊊ D_BT; RESULT.md §§4, 7), yet all
  screen.

What this does not show: that future events exist; that the physical world
is deterministic or globally hyperbolic; that C&R hold a supervenience thesis
about the realm; or anything about the fusion/location clause. Determination
and existence remain distinct claims.

## Relation to the coordinator's three positions (NEXT_STRONGEST_PATH.md)

By Lemma 1, the bow-tie surplus over the potential realm is exactly

    D_BT(b) \ D_pot(b) = E(b) \ J⁻(J⁺(b)),

the elsewhere events with no causal route to **any** event of b's future.
So the extra events that position 3 adds have, by construction, no role in
shaping, screening or (under determinism) fixing anything in b's future.
No justification phrased in terms of the future can therefore select D_BT
over D_pot. A selection needs a non-causal principle: uniform treatment of
the elsewhere, a spatial analogy, or the location/composition clause.
H's surplus over D_pot is intermediate. It consists of events that once had
potential relative to some r ≤ b, so it is justified by persistence. What
remains, D_BT \ H (nonempty in exact dust + Λ: RESULT.md Prop. 9 and
the coordinator's EXACT_DUST_LAMBDA.md, derived independently), is justified
neither causally nor by persistence.

This sharpens the coordinator's question ("what independently justifies
including every spacelike event?") into a precise one: the events needing
independent justification are exactly
E(b) \ ⋃_{r≤b} (J⁻(J⁺(r)) \ J⁺(r)) (by Lemma 1 applied at each r; x = r
cannot occur for x ∈ E(b)). It also
answers half of "does a causal motivation select one invariant realm?". The
instantaneous motivation selects exactly the minimal screening realm, an
invariant set defined from causal structure alone, but that realm is not
persistent unless spacetime is future-directed (coordinator lemma).

## Review targets

1. Theorem 3, step 2 (closedness and push-up) and step 4 (inner continuity
   of I⁻; the endpoint case analysis).
2. Premise (L′) (or a proof that h(K₁) lies in a Cauchy surface of M₂): locate an exact statement, or a counterexample to it, in
   the MGHD literature (Sbierski 1309.7591; Ringström).
3. Rigidity of H without a matched slice.
4. Whether the matching of the open realm W (rather than D_pot including
   its boundary) is the right formalization of "the same existing realm".
