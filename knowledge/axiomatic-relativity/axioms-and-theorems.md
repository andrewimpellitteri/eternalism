# Axioms and theorems: logical analysis of relativity and the definability of simultaneity

Status: extraction for review, 2026-10-19. Lane `kb-axiomatic-relativity`.
This file states what the sources actually prove, with locators, and marks reading
depth. It contains no novelty claim. Existing knowledge-base IDs
(`seed-axiomatic-relativity`, `seed-besnard-simultaneity`, `found-malament-1977`,
`found-stein-1968`, `found-stein-1991`, `found-sarkar-stachel-1999`,
`found-sep-malament`, `seed-isabelle-relativity`, `seed-einstein-1905`) are
reused, not duplicated; see README.md for the reuse map.

Reading-depth legend for the headline sources of this file:

- FULL: read to full text this pass (arXiv HTML or fetched page image).
- SEC: known through full-text-read secondary sources or through full-text-read
  primaries that quote/state the result; primary not accessed.
- META: bibliographic metadata verified only (Crossref/arXiv landing page).

| ID | Source | Depth this pass |
|---|---|---|
| seed-axiomatic-relativity | Andréka, Németi, Madarász, Székely, arXiv:1105.0885v1 | FULL (arXiv HTML v1) |
| seed-besnard-simultaneity | Besnard, arXiv:1104.1263v1 | FULL (arXiv HTML v1) |
| found-malament-1977 | Malament 1977, Noûs 11(3):293-300 | FULL (JSTOR scan via public course mirror; the prior KB record said abstract — coordinator may upgrade) |
| axrel-giulini-2001 | Giulini, arXiv:gr-qc/0011050v1 / BJPS 52(4) | FULL (arXiv HTML v1) |
| axrel-mamone-capria-2012 | Mamone-Capria, arXiv:1202.6578v3 / Found. Phys. 42 | FULL (arXiv HTML v3) |
| found-stein-1968 | Stein 1968, J. Phil. 65(1):5-23 | UNREAD — SEC via axrel-sep-bebecome-2021 and found-stein-1991 |
| found-stein-1991 | Stein 1991, Phil. Sci. 58(2) | SEC (full text already recorded by foundations lane) |
| found-sarkar-stachel-1999 | Sarkar & Stachel 1999, Phil. Sci. 66 | SEC (full text already recorded by foundations lane) |
| axrel-sep-convensimul-2018 | SEP, Conventionality of Simultaneity (2018) + supplement | FULL (secondary) |
| axrel-sep-bebecome-2021 | SEP, Being and Becoming in Modern Physics (2021) | FULL (secondary) |
| axrel-ben-yami-2006, axrel-hogarth-2005, axrel-grunbaum-2010, axrel-zeeman-1964, axrel-rynasiewicz-2001 | | SEC/META (details per record) |
| axrel-madarasz-nemeti-szekely-2006, axrel-andreka-etal-2012-logic-road, axrel-andreka-etal-2002-report, axrel-spirtes-1981, axrel-robb-1914, axrel-goldblatt-2004 | | META (details per record) |

All DOIs and arXiv IDs below were verified against arXiv landing pages or
Crossref on 2026-10-19 (verification log in AGENT_REPORT.md). Notation follows
each source; cross-source notation is translated explicitly.

---

## Part 1 — The Budapest FOL program: SpecRel, AccRel, GenRel

Source: arXiv:1105.0885v1 (FULL). This is the program's self-description;
its theorems cite deeper sources (Handbook chapter; Székely 2009 thesis; the
2002 report, currently unreachable: axrel-andreka-etal-2002-report).

### 1.1 Language (two-sorted FOL)

`{B, IOb, Ph, Q, +, ·, W}`: bodies `B`; inertial observers `IOb ⊆ B`;
photons `Ph ⊆ B`; quantities `Q` with `+, ·`; worldview relation `W` of arity
`2+d`, where `W(k, b, x̄)` reads "observer k coordinatizes body b at spacetime
location ⟨x₁,…,x_{d−1}, t⟩". Dimension `d ≥ 2` is a parameter. Events are
defined, not primitive: `ev_m(x̄) = {b : W(m,b,x̄)}` (Sec. 5).

### 1.2 Axiom system SpecRel (Sec. 5; exact content)

`SpecRel := {AxFd, AxPh, AxEv, AxSf, AxSm}`.

- **AxFd**: ⟨Q,+,·⟩ is a Euclidean ordered field (field; `≤` defined by
  `x ≤ y ⟺ ∃z x+z² = y` is a linear order; positive elements have square
  roots). Deliberately weaker than ℝ: no Archimedean or supremum property.
  (Sec. 5, axiom box.)
- **AxPh**: for every inertial observer m there is a quantity `c_m` such that,
  for all `x̄, ȳ`: a photon can go from x̄ to ȳ (as m coordinatizes them)
  iff `‖ȳ_s − x̄_s‖ = c_m·|y_t − x_t|`. Note what it does *not* say: `c_m` may
  vary between observers and may be 0 (explicit, Sec. 5, discussion after the
  axiom box); isotropy and finiteness are per-observer only.
- **AxEv**: all inertial observers coordinatize the same set of events
  (`∀m,k ∈ IOb ∀x̄ ∃ȳ ∀b (W(m,b,x̄) ↔ W(k,b,ȳ))`).
- **AxSf**: every inertial observer sees himself on the time axis
  (`W(m,m,x̄) ↔ x₁=x₂=x₃=0`).
- **AxSm**: observers using units in which `c = 1` agree on the spatial
  distance of events simultaneous for both; plus: a photon goes from
  ⟨0,0,0,0⟩ to ⟨1,0,0,1⟩ for every inertial observer (units compatibility).

### 1.3 Theorems in the paper (locators exact)

- **Thm 5.1 (no FTL observers).** `SpecRel ⊢` if `m,k ∈ IOb` and `m` sees `k`
  at two distinct points, then `‖ȳ_s − x̄_s‖ < |y_t − x_t|`. Presented as a
  *theorem*, not an axiom; geometric proof cited to the Handbook chapter.
- **Thm 5.2 (worldview transformations are Poincaré).** `SpecRel ⊢` for all
  inertial `m,k`, the relation `w_mk(x̄,ȳ) ⟺ ev_m(x̄)=ev_k(ȳ)` is a Poincaré
  transformation. Proof cited to [3] Thm 11.10, p. 640 (Handbook of Spatial
  Logics chapter, paywalled, not read) or Székely thesis Thm 3.2.2, p. 22.
  This is the bridge from the FOL axioms to the standard Lorentzian content;
  the paper asserts it and cites, it does not reprove.
- **Prop 6.1 (AxEv ablation).** With `AxMeet_n` = "all inertial observers see
  the same n-meetings of bodies": `AxEv ⊢ AxMeet_{n+1} ⊢ AxMeet_n`;
  `AxMeet_n ⊬ AxMeet_{n+1}` (explicit finite countermodel in the proof);
  `Meet_ω ⊬ AxEv` (countermodel with Q = ℕ). So the finite-meeting hierarchy
  is strictly increasing and does not reach AxEv.
- **Ax(c≠0)** (Sec. 6): no inertial observer sees a stationary photon.
- **Prop 6.2.** `AxMeet_3, AxFd, AxPh, Ax(c≠0) ⊢ AxEv`; but
  `AxMeet_2, AxFd, AxPh, Ax(c≠0) ⊬ AxEv` (countermodel: photons as lines of
  slope 1, bodies seen on horizontal hyperplanes) and
  `Meet_ω, AxFd, AxPh ⊬ AxEv` (countermodel with `c = 0`). So AxEv can be
  weakened to AxMeet_3 at the price of ruling out stationary light.
- **Thm 7.1 (twin-paradox ablations).** With
  `AccRel := SpecRel ∪ {AxCmv, AxEv⁻, AxSf⁻, AxDf} ∪ Cont` (AxCmv: co-moving
  inertial frame at each event; AxEv⁻, AxSf⁻: generalized to all observers;
  AxDf: worldview transformations differentiable; Cont: scheme — every
  definable bounded nonempty set of quantities has a supremum):
  (7) `AccRel ⊢ TwP`; (8) `AccRel − AxDf ⊢ TwP`; (9) `AccRel − Cont ⊬ TwP`;
  (10) `Th(ℝ) ∪ AccRel − Cont ⊬ TwP`. I.e., differentiability is dispensable,
  and the continuity scheme is independent of the whole first-order theory of
  the reals for this purpose. Proofs cited to Madarász–Németi–Székely 2006
  (axrel-madarasz-nemeti-szekely-2006, META) and Székely thesis §7.
- **Thm 8.1 (completeness).** `GenRel := {AxFd, AxPh⁻, AxEv⁻, AxSf⁻, AxSm⁻,
  AxDf} ∪ Cont` is complete with respect to Lorentzian manifolds over real
  closed fields (each model of GenRel comes from such a manifold and vice
  versa). With `GenRel⁺ := GenRel ∪ Compr` (comprehension scheme: definable
  timelike curves are worldlines), timelike geodesic, curvature, and metric
  become definable, and Einstein's equations can be added as definition or
  axiom (Sec. 8). Precise GenRel axiom texts are deferred by the paper to
  axrel-andreka-etal-2012-logic-road (META).
- **Sec. 9**: hypercomputation claims (non-Turing computation in relativistic
  spacetimes) — program-adjacent, cited to Andréka–Németi–Németi 2009; not
  part of the axiom extraction; see seed-isabelle-relativity for the
  machine-verification counterpart.

### 1.4 What this program assumes about observers

Observers are bodies that coordinatize; inertiality is primitive via `IOb`;
an observer's "time" is the last coordinate of its worldview — clock time is
never constructed from proper time, it is stipulated coordinate-wise.
Simultaneity per se is not the program's target: `x_t = y_t` inside one
worldview is available by notation only. Nothing in Secs. 1–8 formulates a
definability or uniqueness question about a simultaneity relation; that is a
different literature (Part 2).

---

## Part 2 — The Malament line: definability of simultaneity

All results in this part are about Minkowski spacetime `M = (ℝ⁴, η)`
(possibly with time orientation `Or`), a distinguished inertial observer
`X` (a timelike straight line), and candidate *simultaneity relations*.
`κ` = symmetric causal connectibility (`η(p−q,p−q) ≥ 0`); `λ` = lightlike;
`⪯` = causal order (κ + time orientation); `Σ_X` = Poincaré–Einstein
simultaneity w.r.t. X (η-orthogonal hyperplanes); `Λ_X^±` = forward/backward
light-cone relations from X; `Γ_{X,v}` = conic relations of "speed" v
(world-histories of constant-v signals from points of X; v = 1 gives `Λ_X^±`,
v = ∞ gives `Σ_X`); `Γ_{X,f̃}` = generalized conic relations for arbitrary
radial profile f (Besnard Sec. 4).

### 2.1 Definability notions (Besnard Def. 2.1, FULL; cf. Malament Sec. 3)

- Explicitly S-definable: `xRy ⟺ Φ(x,y)` for a first-order formula Φ in
  structure S.
- Implicitly S-definable: invariant under all S-automorphisms
  (`Aut_S`-invariance). Explicit ⟹ implicit; Malament's phrase "definable in
  any sense of 'definable' no matter how weak" (Sec. 3, read this pass) means
  the implicit notion. This distinction is the source of much confusion in the
  commentary literature (Besnard Sec. 2; Rynasiewicz 2001 per Besnard).

### 2.2 Malament 1977 (found-malament-1977; FULL this pass, JSTOR scan pp. 293-300)

- **Prop 1(i).** `Sim_O(p,q)` iff there are distinct `r,s ∈ O` with
  `Orth(p,q,r,s)`, where `Orth(p,q,r,s) ⟺ (p−q, r−s) = 0` (Minkowski
  inner product). Plus the ε-calculation: for `q = r + ε(s−r)` on O and
  `p` light-related to both r and s, `(q−p, s−r) = (ε − ½)(s−r, s−r)`, i.e.,
  orthogonality is exactly ε = ½ (Sec. 2).
- **Prop 1(ii).** `Orth` is explicitly first-order definable from κ alone
  ("essentially due to Robb", note 3; the exhibited formula uses triple
  light-cone non-intersection to express collinearity; Malament's formula for
  lightlike `p λ q` in note 3: `p κ q ∧ (p=q ∨ ∃r (r κ p ∧ r κ q ∧ ∀s(s κ p
  ∧ s κ q → s κ r)))`). This is the κ-definability of the light-cone geometry.
- **Prop 2 (the uniqueness theorem).** Suppose `S ⊆ ℝ⁴×ℝ⁴` is (i) implicitly
  definable from κ and O — i.e., invariant under all O-causal automorphisms
  (bijections preserving κ and membership in O); (ii) an equivalence relation;
  (iii) non-trivial: some `p ∈ O`, `q ∉ O` with `S(p,q)`. Then S is either
  `Sim_O` or the universal relation. (Sec. 3, statement and proof read; the
  proof is an orbit argument: the O-causal-automorphism group contains
  rotations, translations, dilations about points of O, and reflections in
  hyperplanes orthogonal to O — i.e., time reversal.)
- **Prop 3.** Implicitly κ-definable (no O) equivalence relation with even one
  distinct related pair is the universal relation: no non-trivial *absolute*
  simultaneity from κ alone (Sec. 3). This is the SR-vs-Newtonian contrast
  (cf. Giulini Thm 3/4, Mamone-Capria Thm 3.3/Cor 3.9).
- Framing (Sec. 1, read): Malament's target is Grünbaum's assertion (1)
  "relative simultaneity is not uniquely definable from κ", and he is
  "entirely sympathetic" with Friedman's skepticism toward assertion (2), the
  causal theory of time. The result is conditional on definability-from-κ
  being the non-conventionality criterion. He does not endorse that criterion
  as a metaphysical thesis.

### 2.3 Later ablations, in parameter order (all FULL sources)

- **Zeeman 1964 / Alexandrov 1975 (axrel-zeeman-1964: META abstract).**
  Causal-order-preserving bijections = inhomogeneous Lorentz group + dilations
  (+ reflections, for the partial order). Without continuity assumptions.
  This is what makes "invariance under causal automorphisms" computable.
  Giulini Sec. 5 and Mamone-Capria Thm 3.16 attribute the orthochronous
  refinement to Alexandrov.
- **Sarkar–Stachel 1999 (found-sarkar-stachel-1999; SEC; also re-derived in
  Giulini Sec. 5 and Mamone-Capria Thm 3.19(1)).** Dropping time-reflection
  invariance: the backward (or forward) half-cone relations satisfy all other
  Malament conditions; and, per Besnard's account of their paper, standard
  synchrony remains unique among relations independent of the observer's
  *position*, half-cones among those independent of the observer's *motion*.
  Besnard (Sec. 2) and the SEP supplement both stress: the half-cone
  construction needs a time orientation, i.e., more than κ; and Giulini found
  a gap in their uniqueness argument (classes of an invariant partition need
  not themselves be invariant sets), repaired in his Thm 6 framework.
- **Giulini 2001 (axrel-giulini-2001; FULL).** Change the invariance group to
  the physical symmetry group `Ilor` (proper orthochronous Poincaré, no
  dilations, no reflections). Req. 1/2 add the soundness condition: classes
  meet any physically realizable trajectory ≤ once. Results:
  - Thm 3: with the inhomogeneous Galilei group, standard Galilean
    simultaneity is the unique absolute simultaneity.
  - Thm 4: with `Ilor`, no non-trivial invariant equivalence relation exists
    (no absolute simultaneity).
  - Thm 5: with `X` = an inertial frame (foliation by parallel timelike
    lines) and `Ilor_X` the stabilizer, the non-trivial invariant equivalence
    relations have classes of exactly four kinds: (i) orthogonal hyperplanes
    Σ; (ii) unions of Σ's modulo a discrete translation λ along the frame
    direction; (iii) the individual line; (iv) unions of lattice points along
    a line. Only (i) passes the soundness condition → Thm 6: Einstein
    simultaneity is unique relative to an inertial frame.
  - Thm 7 + Appendix: re-proof of Malament's Prop 2 from Alexandrov's
    characterization; Sec. 5 exhibits the extra relations (concentric shells,
    tilted half-cones of arbitrary opening) that appear when dilations are
    dropped, and pinpoints the Sarkar–Stachel proof gap.
  - Caveat: Mamone-Capria 2012 corrects Giulini's Thm 2 (Galilean case:
    everywhere-dense additive subgroups of ℝ give further invariant
    relations) and Thm 5 (frame case: same correction; his Thm 3.17 is the
    corrected statement; uniqueness statement survives in the conformal
    case, his Thm 3.17(B)).
- **Ben-Yami 2006 (axrel-ben-yami-2006; SEC via Besnard Sec. 2 + SEP
  supplement).** Take the directed causal order `⪯` (κ + time orientation) as
  primitive instead of κ. Then the `Aut_{X,⪯}`-invariant equivalence relations
  satisfying a soundness condition are exactly the conic relations
  `Γ_{X,v}^{±}`, v ∈ ]0,∞] — a one-parameter family including the light-cone
  relations and (as limit) `Σ_X`. Spirtes 1981 (axrel-spirtes-1981, META) is
  credited (by Ben-Yami and the SEP supplement) with first observing the
  infinity of relations once time reflection is dropped.
- **Hogarth 2005 (axrel-hogarth-2005; SEC via Mamone-Capria Prop 4.1).** With
  invariance under the worldline stabilizer without dilations (but still with
  time inversion) and the strong soundness condition "each class meets X in
  exactly one point", standard synchrony is again unique. The original is
  paywalled; the proposition is re-proved in a FULL-read source.
- **Besnard 2011 (seed-besnard-simultaneity; FULL, arXiv v1).** Explicit-
  definability versions and new ablations:
  - Thm 2.4 (structure equivalences, Sec. 2): `(X,[f]) ↔ (X,<)`;
    `(X,κ,<) ↔ (X,⪯) ↔ (X,κ,Or)`; `(X,κ,T̃) ↔ (X,η,Or)`. Reading: adding a
    monotone chronology ("bad clock" — a clock that may run unevenly but never
    backwards) to κ is equivalent to adding a time orientation; adding a
    proper-time parametrization class T̃ is equivalent to having the full
    metric plus orientation.
  - Thm 3.1 (Sec. 3): with a natural ordering `<` on X, every `Aut_{X,κ,<}`
    invariant equivalence relation satisfying Malament's condition (M) is
    `Σ_X` or `Γ_{X,v}` for some v ≠ 0, and *all of them are explicitly*
    (X,κ,<)-definable — constructive proof via a light-signal lattice
    construction with explicit first-order formulas (e.g. Eq. (10) for
    v = 1/3), rational case built directly, irrationals by two-sided
    rational approximation. This fills the explicit-definability gap left by
    Malament (only Σ_X) and Ben-Yami (only light cones, implicitly).
  - Thm 4.1 (Sec. 4): given a clock T̃ (equivalently `(X,η,Or)`), the
    equivalence relations definable from `(X,κ,T̃)` satisfying criterion (B)
    (each class meets X in exactly one point) are exactly `Γ_{X,f̃}` for
    arbitrary f: [0,∞[ → ℝ with f(0)=0 — arbitrary hypersurfaces of
    revolution translated along X. Explicit definability included (Eq. (12)
    via the two cone-intersection points of each event). This is the
    "arbitrariness" end of the title: with clock data, any time-coordinate
    profile is as definable as any other.
  - Thm 5.1 (Sec. 5): replace global κ by the *local* light-cone structure
    `L_X = {Λ_x : x ∈ X}`: (1) there is *no* non-trivial `Aut_{X,L_X}`-
    invariant equivalence relation satisfying (M) — Σ_X disappears entirely
    (proof uses non-affine causal automorphisms of a 2-plane, propagated by
    rotation; such maps exist only in dimension 2, citing Zeeman); (2) with a
    natural ordering, the only ones satisfying (M) are `Λ_X^±` (explicitly
    definable); (3) with a clock, all `Γ_{X,f}` are explicitly definable.
    Besnard's operational point: κ between events off X is not information the
    observer has; with locally accessible data the privileged status of
    standard synchrony does not survive.
  - Summary table (Sec. 2, end): structures `(η,Or)`, `(X,κ)`, `(Ξ,η,Or)`,
    `(X,⪯)`, `(X,η,Or)` × soundness conditions {none, M, G, B, BY} ×
    {explicit, implicit} — which classification is known from which paper.
- **Mamone-Capria 2012 (axrel-mamone-capria-2012; FULL).** Group-theoretic
  classification via invariant additive subgroups (Thm 2.5). Newton/Galilei:
  classes `x + (ℝ³×H)` for additive subgroups H ⊆ ℝ (Thm 3.3/3.6; corrects
  Giulini). Poincaré: none non-trivial (Prop 3.8, Cor 3.9). Join/meet
  facts: two non-proportional standard synchronies generate the universal
  relation; four independent ones generate the identity (Prop 3.10) — no
  absolute present between one event and everything. Frame case (Thm 3.17)
  and worldline case (Thm 3.19) as above; Thm 3.15: two-way light isotropy
  plus preservation of causal statements across a "resting" coordinate change
  already forces standard synchrony up to scale. Sec. 4 conclusion (paper's
  own position): the invariant-equivalence interpretation "does not cut in the
  debate" because conventionalists reject the equivalence-relation requirement
  and the appeal to one-way light isotropy built into the Poincaré group;
  hence uniqueness arguments are, for that debate, question-begging.

### 2.4 The Stein line (becoming, not simultaneity)

- **Stein 1968 (found-stein-1968; UNREAD — all public routes blocked this
  pass; content below is SEC, from axrel-sep-bebecome-2021 and
  found-stein-1991).** Per the SEP exposition: define a two-place relation
  `R xy` = "y has already become / is already definite with respect to x",
  subject to reflexivity, transitivity, and non-universality (not everything
  has become for everything); the unique answer in Minkowski spacetime is
  `y ∈` past causal cone of x. Consequence noted by Stein (p. 15, as quoted
  by SEP): "in Einstein-Minkowski space-time an event's present is constituted
  by itself alone." Callender (2000, per SEP) objects that this
  "non-uniqueness" of presents is the thinnest possible becoming. Also per SEP
  (Sec. 3.3): Stein 1968 fn 6 on proper time as the physically fundamental
  time along worldlines. **The exact statement, conditions, and proof of
  Stein's theorem have not been audited from the primary and must not be
  quoted as verified.**
- **Stein 1991 (found-stein-1991; SEC, full text recorded by foundations
  lane).** Event-relative becoming/openness; no global-present analogue in GR
  (p. 159 per that record); rebuts the inference "no global present ⟹
  everything fixed".
- Relation to Part 2: Stein's uniqueness theorem has the same logical shape as
  Malament's — a uniqueness result *relative to chosen constraints* on a
  relation (there: becoming; here: simultaneity). Neither yields a physical
  discovery of the relation; both are conditional on the constraint list.

---

## Part 3 — What these results do not show (kept separate by contract)

1. **No temporal ontology follows.** All results in Parts 1–2 are
   classification/definability theorems about relations *inside* a spacetime
   formalism. They do not decide eternalism vs presentism vs growing block vs
   moving spotlight. In particular:
   - Uniqueness of `Σ_X` relative to `(X,κ)` (Malament) is a statement about
     definability given the causal-theory-of-time's own criterion; Malament
     himself does not endorse that criterion (Sec. 1 of his paper). Janis's
     per-observer latitude argument (SEP Sec. 3; Grünbaum 2010) shows the
     theorem leaves the ε-latitude across observers exactly where it was.
   - Mamone-Capria 2012 (read) argues the invariant-equivalence
     interpretation does not bear on conventionality at all.
   - A unique, physically privileged foliation would be a *geometrical*
     structure, not an ontology: presentism needs an additional bridge
     premise ("the foliation's slices are what exists"), which no theorem
     above supplies. Conversely, non-uniqueness does not establish eternalism;
     the Putnam/Rietdijk route needs an extra transitivity-of-reality premise
     (found-putnam; found-stein-1991), and Stein's construction shows a
     non-universal event-relative alternative exists *as a formal option*.
2. **No objective passage.** Nothing in these papers defines or detects
   passage; Besnard's "bad clock" discussion (Thm 2.4 commentary) notes that
   any time-asymmetric process (memory formation included) can orient a
   worldline, but proves nothing about passage itself. The SEP becoming
   entry's Broad/Shimony/Park material is philosophy, not part of the
   theorems.
3. **Determinism is untouched.** None of the results involve dynamics,
   prediction, or fixedness of the future. Chronogeometrical fatalism
   arguments are philosophy built on top of the kinematics; Stein's theorem
   is precisely a formal countermodel to one such argument *given* his
   definitions (SEP Sec. 3.2).
4. **Causal order ≠ simultaneity ≠ clock time.** `⪯` is invariant and
   observer-independent (κ-definable structure; Zeeman/Alexandrov).
   Simultaneity is either frame-relative or observer-relative or conventional,
   depending on structure granted (Part 2). Clock time = proper time along a
   worldline (Stein 1968 fn 6; Besnard's T̃), a different thing from
   coordinate time `x_t` in a worldview (Part 1). These are kept distinct
   throughout; conflation is the main error the ablation table is designed to
   prevent.
5. **The thermodynamic arrow is absent.** No paper in this lane involves
   entropy, boundary conditions, or irreversibility. Besnard's aside that a
   "bad clock" could be an irreversible process is a remark, not a result
   linking the causal/definability structure to the thermodynamic arrow.
6. **Domain restrictions.** Everything in Part 2 is flat Minkowski spacetime
   (Besnard: explicitly `ℝ⁴` with η, Or). Nothing here transfers to curved
   spacetime without new work; GenRel-model results (Part 1 Thm 8.1) do not
   include any simultaneity-definability theorem. Besnard's local-data
   theorem even suggests global causal information is the load-bearing
   assumption, which is exactly what fails locally in GR.

---

## Part 4 — Paper claims vs established results vs our notes

- **Established** (multiple independent proofs in read sources): Zeeman/
  Alexandrov characterization of causal automorphisms; non-existence of
  non-trivial Poincaré-invariant equivalence relations; Malament's Prop 1–3
  (re-proved by Giulini appendix and Mamone-Capria Thm 3.19); the conic-family
  classification under `(X,⪯)` (Ben-Yami implicit, Besnard explicit);
  Giulini's frame classification *as corrected by* Mamone-Capria Thm 3.17;
  Besnard Thms 4.1/5.1 (no independent re-derivation exists in the read
  corpus — single-source results, proof read, not reproduced).
- **Paper authors' claims** (not audited here): the cited deeper proofs
  (Handbook Thm 11.10; Székely thesis; Madarász–Németi–Székely 2006 Thm on
  Cont-independence; Robb's representation theorem; Stein 1968's theorem);
  all hypercomputation claims; Mamone-Capria's and Grünbaum's philosophical
  theses about conventionality.
- **Our notes/conjectures** (this lane): only the cross-program observations
  in ablations-and-temporal-ontology.md §3; nothing there is a claimed
  discovery.
