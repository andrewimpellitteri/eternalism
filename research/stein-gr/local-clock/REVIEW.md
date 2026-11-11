# Adversarial review of the local-clock note

10 November 2026. Reviewer: the same Claude Code session (Fable 5.2) that wrote
[RESULT.md](RESULT.md), at the user's request. This is a self-review by the author's
model. It is not independent and confers no acceptance. Every proof step was re-derived
by hand. Nothing was formalised or run.

## Verdict

**No theorem failed.** Two proofs had gaps that are now repaired in RESULT.md. One
novelty statement was wrong and is withdrawn: the repo already contained the seed of
Example 5.

| Item | Verdict |
|---|---|
| Theorem 1 (no spacelike scale) | CONFIRMED. One citation replaced by a proof |
| Theorem 2 (germs), Loc version | CONFIRMED after repair of the shrinking step |
| Theorem 2, connected sketch | NOT REVIEWED. Still a sketch |
| Theorem 3 (classification on Minkowski) | CONFIRMED |
| Corollaries A, B, C | CONFIRMED |
| Theorem 4 (clock criterion), Loc version | CONFIRMED |
| Theorem 4, connected one-way statement | CONFIRMED |
| Example 5 (curvature clock), mathematics | CONFIRMED |
| Example 5, "the repo does not have this" | REJECTED as first stated. See §3 |
| Bigaj and Arthur–Savitt remarks | UNVERIFIED. Now marked as such |

## 1. Theorem 1

| Step | Attack | Result |
|---|---|---|
| f depends only on the interval | Ordered spacelike pairs of one interval form one orbit of the proper orthochronous group in 3+1 | Holds |
| S_i acausal | t increases strictly along future causal curves of the product | Holds |
| π(D_𝕄(S̃_i)) ⊆ D(S_i) | Lifting of inextendible causal curves | Holds |
| D(S_i) ⊆ π(D_𝕄(S̃_i)) | Straight past rays from p meet the Cauchy surface {t = 0} once, so their endpoints lie in S_i. The connected ball lies in one translate of S̃_i | Holds |
| N_i causally convex and globally hyperbolic | The note pointed to Lemma `lem:D`(iii), which concerns a different set | REPAIRED: direct argument added |
| Lifted intervals a and ℓ − a | The second tube runs from θ = a to θ = ℓ, so the lifted displacement has the opposite sign. Rotation by π absorbs it | Holds |
| Hidden transitivity or (CB) | None used | Holds |

The causal-convexity argument now in the note: let S be acausal, p, q ∈ D(S) and
p ≤ r ≤ q, and let λ be an inextendible causal curve through r. The curve that runs
back from q to r and then along the past half of λ meets S. So does the curve from p
to r followed by the future half of λ. If neither meeting point is on λ, there are
s₂ ≤ r ≤ s₁ in S, and acausality gives s₁ = s₂ = r. Interiors follow by taking
p′ ≪ p and q ≪ q′ in int D(S).

Theorem 1 is easy. On the paper's GH it is a short consequence of Reflection. Its
value is the reading it forces on (LC), not its difficulty.

## 2. Theorem 2

**Gap found.** The proof shrank U_x until U_x ≅ U_x′. A causally convex neighbourhood
in M need not have a causally convex image in M′ under a germ isometry φ : V → V′.

**Repair.** Use diamonds. Both spacetimes are strongly causal, so for p ≪ x ≪ q close
to x the diamond I⁺(p) ∩ I⁻(q) of M lies in V, and the diamond of M′ on φ(p), φ(q)
lies in V′. Timelike curves between the endpoints then stay in V and V′, so φ maps one
diamond onto the other. Diamonds are causally convex and globally hyperbolic. The
note now says this.

## 3. Example 5 and the withdrawn novelty statement

The mathematics stands. R is 8πGρ for dust in the paper's signature and decreases in
cosmic time. Each of the three relations is transitive on C_R, contains I⁻ and
satisfies (LC).

**Pre-emption inside the repo.** [DRAFT.md](../DRAFT.md) §4.4 (24 October) already
says: "A pointwise rule such as 'x B b iff R(x) ≥ R(b)' is local, so (LC) alone does
not exclude it", and treats the dust model with R = 4/(3t²). The earlier grep for
this note missed it. So the observation that a curvature ordering is local is **not**
new to the repo.

What the draft concluded was that the rule "is not the restriction of any such
theory" on GH. What RESULT.md adds:

- the rule is a becoming theory on the restriction-closed class C_R, which contains
  every vacuum spacetime, so the theorem and the corollary are false there;
- the variant with shared presents and a non-universal Minkowski verdict;
- the exact criterion of Theorem 4, of which the example is an instance.

**A second, weaker pre-emption.** Proposition `prop:single` already yields a contrived
restriction-closed class on which the theorem fails: the regions of one generic
spacetime together with the regions of 𝕄, with no morphisms between the two families.
So "the off-shell premise is essential" was implicit. C_R improves on it by being
defined by a curvature inequality, by using one formula on every member, and by
including Minkowski and vacuum spacetimes non-trivially.

**Also true, and omitted by the unified paper.** The paper's sentence that
cosmological time "violates only locality" dropped the draft's own §4.4 caveat. That
part of the note's criticism stands.

## 4. Theorem 4

| Step | Attack | Result |
|---|---|---|
| ρ well defined | Needs Theorem 2 on C. Only restriction-closure is used | Holds |
| Left closure of ρ | M₀ ⊔ U_b is a member. (CB) applies inside M₀. w and b are unrelated | Holds |
| Chains | Left closure walks down flat ⊴* g_x. Right closure walks up g_b ⊴* flat | Holds |
| ρ(flat, flat) ⇒ U on 𝕄 | Every spacelike pair related, then (T) | Holds |
| Clock ⇒ theory | (T) uses κ(x) ≤ κ(y) for x ≪ y in the same member, which is the definition of ⊴ | Holds |
| Indicator clocks | Up-set of flat and complement of its down-set are monotone | Holds |
| Connected version | The first draft claimed anchoring is necessary on Loc₀. That was wrong and had already been corrected before this review: an unanchored germ and a flat region may never share a connected member | Corrected statement holds |

Theorem 4 does not prove the on-shell theorem for GH_DEC. It restates what would have
to be shown.

## 5. Remaining weaknesses

1. **Disconnected objects carry Theorems 2 and 4.** If a becoming rule need not be
   defined on a spacetime with two components, the exact criterion is unproved. The
   connected version of Theorem 2 needs a written gluing proof and an audit.
2. **Prior art is thin.** Four snippet-level queries. The Fewster–Verch definitions
   were not read directly. Theorem 1 may be folklore in locally covariant QFT.
3. **Two remarks rest on memory or on the paper's own summaries.** Bigaj's
   "exhaustiveness stipulation" and the Arthur–Savitt diamond present were not reread.
4. **C_R is unrealistic.** Any spacetime with a star is outside it. Which class a
   becoming rule must cover is a philosophical premise that the note does not argue.
5. **Self-review.** An outside reader, or at least a different model family, should
   check §§2 and 5 of RESULT.md before any manuscript change.
