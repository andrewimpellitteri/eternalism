# Long shot: a growth-versus-completion dilemma for complex percolation

> **Erratum (21 Oct 2026):** Prop. 5's equality `D'_H = N_{H}` is false; the
> correct identity is `N_{H} = D'_{H^-}`. The `D'_H` amplitude formula and the
> non-extension conclusion are unaffected. See `ERRATUM.md` and
> `research/longshots/review/REVIEW.md`.

Task `longshot-growth-completion-dilemma`, Claude subagent, 2026-10-21. Saved by
the coordinator from the subagent's returned text (its file write was refused).
Submission for review; no novelty claim. Sources: `sources.jsonl` (14 records).

## 0. Verdict: KILL as posed; KNOWN in its true core; one small residual not located in print

1. **Clause (c), read literally, is false.** The covariant completed-history
   algebra `R` carries countably additive normalized measures (any Dirac measure
   at an infinite causet). Each is compatible with the complex-percolation
   amplitudes under finite additivity (Prop. 4), because `Z ∩ R = {∅, Ω}`. The
   dynamics fixes no covariant value unless countable additivity (or a limit
   rule) is imposed across the finite-stage/completed boundary.
2. **Repaired (c) is true and published:** no countably additive complex
   measure on `S_Z ⊇ R` extends the amplitudes (Dowker–Johnston–Surya
   1007.2725v1 Lemma 1, Claim 5; Surya–Zalel 2003.11311v1 Thm 2.1). Clauses (a)
   and (b) are in Surya–Zalel Sec. 2, whose abstract frames this as "the
   temporality of the growth process".
3. **The growth horn is kinematic and p-independent.** Clause (b) holds for every
   dynamics and every p. Its classical philosophical reading is published:
   Arageorgis 2016 (Belgrade Philosophical Annual 29:33–55) Sec. 4; Sorkin
   gr-qc/0703098v1 Sec. 5 and Sec. 7 footnote; Wüthrich 2308.05217v1 Sec. 3.3. Only
   the completion horn is specific to `p ∉ [0,1]`.
4. **Escape via covtree.** For `|1−p| < 1`, `p ∉ [0,1]`, stage limits of the
   labelled amplitudes define covariant covtree amplitudes (shown at level 2 and on
   every principal singleton node), so a growth reading can ask covariant
   finite-level questions. But covtree nodes constrain the whole infinite future,
   not "what has grown so far"; for `|1−p| > 1` the construction fails at level 2.
5. **Residual (Prop. 6), priority unverified:** the stage-limit covtree walk
   `W_p` has level-n total variation `≥ |c(q)|·V_n(p) → ∞`, `c(q) = Π_{j≥1}(1−q^j)`,
   so it has no countably additive completion. Elementary corollary of
   `research/creative/RESULT.md` and the finite-cutoff remark in
   `COVARIANT_RESULT.md`. No ontological bearing without the bridges in Sec. 5.

The ontological reading excludes one conjunction per ontology; it does not
discriminate between them. The cheapest revision is to the model or to the
countable-additivity bridge.

## 1. Definitions (Surya–Zalel Sec. 2; Dowker–Johnston–Surya)

`L_n`: naturally labelled n-causets. `Ω`: naturally labelled past-finite causets on
ℕ; cylinders `cyl(c)`. `Z_n`: rank-n cylinder unions; `Z = ∪Z_n`; `S_Z = σ(Z)`.
Covariant: closed under order-isomorphism; `R` = covariant ∩ `S_Z`. Complex
percolation: `q = 1−p`, transition amplitude `p^{|max D|} q^{m−|D|}`, cylinder
amplitude `A_p(c) = p^L q^{C(n,2)−R}`. Covtree node `N_Γ = {C : the n-stems of C are
exactly Γ}` (covariant; Zalel 2302.10582v1 Sec. 3). `Ω` is the path space of a
finitely branching tree, compact, with clopen sets exactly `Z`.

## 2. Theorem A (surviving statement), `p ∈ ℂ ∖ [0,1]`

- (A) `μ_v` is finitely additive and normalized on `Z`. Known.
- (B) `Z ∩ R = {∅, Ω}`: no nontrivial covariant event is decided after finitely
  many births; covariant ∩ clopen is trivial. Kinematic, all p. Known (SZ Sec. 2).
- (C1) No countably additive complex measure on a σ-algebra containing `Z` agrees
  with `μ_v` on `Z`. Known (DJS Lemma 1, Claim 5; SZ Thm 2.1, Eqs. 60–62).
- (C2) For any normalized countably additive `ν` on `R` there is a finitely
  additive `m` on `alg(Z ∪ R)` with `m|_Z = μ_v`, `m|_R = ν`. All p; elementary.
- (C3) For `|1−p| < 1` and principal `H`, the post-tail event `D'_H = N_{{H}}` has
  stage-m amplitudes `N(H)A_p(H)Π_{k=1}^{m−n}(1−q^k) → c(q)N(H)A_p(H)`, `c(q) ≠ 0`;
  no countably additive measure takes these values. For `|1−p| > 1` the stage
  limits diverge already at the 2-chain.

Not claimed: that `R` has no measures; that growth readings must be labelled;
anything on `|1−p| = 1`; failure of Sorkin's 1104.0997 method (untested).

## 3. Proofs (sketch level; see the subagent's text in the session log)

- **Prop. 1 (A):** children's amplitudes sum to `Σ_D p^{|max D|}q^{m−|D|} =
  (p+q)^m = 1`, a polynomial identity. Enumeration to m = 7 (96,428 labelled
  causets) gives total 1 at three complex p.
- **Prop. 2 (B):** for nontrivial `α ∈ Z_n`, take `c ∈ K`, `c' ∉ K`,
  `U = c ⊔ c' ⊔` (infinite chain); labelling c first lies in α, c' first does not,
  and the two are isomorphic.
- **Prop. 3 (C1):** complex measures have finite total variation;
  `sup_n Σ|A_p| = ∞` (DJS, SZ; RESULT.md bound `V_{k+2} ≥ |p|(|p|+|1−p|)^k c_s`).
- **Prop. 4 (C2):** define `φ(f+g) = ∫f dμ_v + ∫g dν` on `S(Z)+S(R)`; well defined
  since `S(Z) ∩ S(R)` are constants; extend via a Hamel complement (uses choice).
  Reading: "completed histories get the dynamics' measure" is a continuity
  postulate, even for real p.
- **Prop. 5:** for principal `H` with top `t`, the n-stem set is `{H}` iff every
  element outside `H` lies above `t`; `t` has label n−1 in every natural
  labelling, so `D'_H = N_{{H}}` is covariant; element j ≥ n lies above t with
  amplitude `1−q^{j−n+1}`.
- **Prop. 6:** level-n stage values are finitely additive (the level-(n+1) stem
  set determines the level-n one); level-2 limits exist for `|q| < 1` by an exact
  recursion; level-n total variation `≥ |c(q)| V_n(p) → ∞`.

## 4. Escape analysis

E1 covariant event decided at finite stage: none (covariant ∩ clopen trivial).
E2 covariant algebra with a measure: yes trivially (Dirac); kills (c) as stated,
gives no dynamical measure. E3 covtree: partial escape for `|1−p| < 1`, but nodes
encode the infinite future and `W_p` has no completion. E4 Sorkin conditional
convergence (1104.0997): untested on complex-percolation stems; DJS's uniqueness
question open. E5 growth without labelled stages: Wüthrich–Callender's
cardinality-gauge growth gives `N(P)A_p(P)` exactly for all p, but is non-covariant
under CST covariance; covtree as in E3. E6 quantum measure instead of amplitude:
does not help (DJS: decoherence functional extends iff the vector measure does).

## 5. Bridge premises

B1 a reading's real propositions are exactly those the dynamics assigns values;
B2 relabelling-dependent events are unphysical (CST orthodoxy; rejected by Earman's
actualised path and energetic causal sets; defined via completed histories); B3 a
growing block's facts at a stage are those settled by finitely many births
(Arageorgis's Condition [N]); B4 a block reading needs a countably additive measure
(weakened by DJS Sec. 5 and by Sorkin 1104.0997); B5 the vector measure is the
relevant object; B6 complex percolation with `p ∉ [0,1]` is admissible (weak).
Growing block ∧ B2 ∧ B3 ⇒ no nontrivial facts (all p; Arageorgis's second reason).
Block ∧ B1 ∧ B4 ⇒ no dynamics-given measure (only `p ∉ [0,1]`).

## 6. Objections

O1 (decisive against the theorem as posed): it confuses "no measure" with "no
measure determined by the dynamics". O2 the gauge horn rests on B2, a block-side
premise. O3 complex percolation with `p ∉ [0,1]` is unphysical. O4 "only |A|²
matters": answered by the DJS equivalence.

## 7. Checks (finite domain)

Stage totals 1 through m = 7 at p = 0.8+0.3i, (1+i)/2, −0.3+0.4i. Level-2 limits
(chain-only, antichain-only, both, TV): p = 0.8+0.3i → 0.851872+0.425522i,
0.247505−0.038720i, −0.099377−0.386802i, 1.602116; p = (1+i)/2 → 0.449222+1.183964i,
0.380039+0.081151i, 0.170740−1.265115i, 2.931513; p = −0.3+0.4i (|1−p| = 1.36)
diverges. Level-3 TV at 0.8+0.3i: 2.13, 2.46, 2.58, 2.58 (m = 4–7).

## 8. Defeat search (verbatim fragments, read depth in sources.jsonl)

- Surya–Zalel 2003.11311v1 abstract: "Because of the temporality of the growth
  process, in this approach," "covariant observables (or beables) are measurable
  only if the quantum measure extends"; Sec. 2: "no event α∈ℨ can be covariant
  unless α=Ω".
- Sorkin gr-qc/0703098v1 Sec. 7 fn: "We meet here with an echo of the
  block-universe idea"; Sec. 5: "stopping the process at a given stage has no
  objective meaning within the theory".
- Arageorgis 2016 conclusion: CSG "cannot be defined with mathematical
  consistency but in the limit of infinite time when causal set growth has reached
  completion ... this makes the growing block imagery ... parasitic on a block
  universe view" (quote from the subagent's own PDF extraction; glyph loss
  possible).
- Wüthrich–Callender 1502.00018v1 Sec. 4: "There is gauge-invariant growth."
- Wüthrich 2308.05217v1 Sec. 3.3: "Thus, we either accept a block interpretation,
  or else we purchase a foreign form of becoming".
- Dowker 1405.3492v1: "A Blockhead can always play the card of 'running the
  process to infinity'".
- Earman 2008: not read (no open copy).

Likely defeaters not searched: INSPIRE forward citations of Surya–Zalel and
Arageorgis; Sorkin–Surya "Constructing covariant observables in complex
percolation" (in preparation, not found); a complex covtree paper.

## 9. Limitations

`W_p` exists only at level ≤ 2 and on principal singletons; uniqueness open;
`|1−p| = 1` open; Sorkin's prescription not computed; level-2 existence proof a
sketch; Arageorgis quotes from a lossy decoder; Props. 2, 4, 5, 6 not independently
reviewed. The scripts quoted in the subagent's text (`level2_exact.py`,
`covtree_limits.py`) were not saved to the repository.
