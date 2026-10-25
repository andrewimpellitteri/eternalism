# Research paths after the Stein-GR theorem

25 October 2026. Big ideas for discussion before narrowing. Arguments marked
[draft] are unreviewed proof sketches written here; nothing below has had an
independent check. Prior work flagged "from memory" is unread.

## The unifying idea: horizons decide what becoming can mean

Three of the paths below turn out to be one subject. In general relativity,
the causal past J^-(b) of an event can (i) swallow whole Cauchy surfaces
(closed universes), (ii) contain pairs of events with no common past
(particle horizons), and (iii) miss whole regions of spacetime that no
matter ever sees (event horizons). Each of these has a precise consequence
for a becoming theory:

- (i) decides whether the future is *settled* from b (Path 1);
- (ii) decides the *logic* of standpoints (Path 2);
- (iii) decides whether the eternalist/fragmentalist dispute about grounding
  has any *structural* content (Path 3).

A second paper, "Horizons and becoming", could unify these. That is the
strongest candidate for the next serious piece of work: it is new, it uses
the Stein-GR framework, it moves the philosophical debate rather than adding a
technicality, and it can be done without an expert collaborator.

---

## Path 1. Settledness and the closing of the future

**Big idea.** "Is the future real from b?" and "Is the future settled from
b?" are different questions (STRONGEST_VIEW R10). The first is always no. The
second has a sharp geometric answer, and in some universes the answer
switches from no to yes at a definite cosmic moment.

**Definition.** x is *settled from b* if every past-inextendible causal curve
from x meets I^-(b). (With deterministic, hyperbolic laws, data in I^-(b) then
fix what happens at x.) Write Set(b) for the set of such x; I^-(b) ⊆ Set(b).

**Theorem 1.1 (characterization)** [draft]. Let M be globally hyperbolic with
Cauchy temporal function t and level sets S_c. Then x ∈ Set(b) iff there is
c < t(x) with J^-(x) ∩ S_c ⊆ I^-(b).

*Proof.* (⇐) Every past-inextendible causal curve from x crosses S_c in
J^-(x) ∩ S_c ⊆ I^-(b). (⇒) Suppose not: for c_n → −∞ pick
y_n ∈ J^-(x) ∩ S_{c_n} outside I^-(b) and causal curves γ_n from x to y_n.
No point z of γ_n lies in I^-(b), since otherwise y_n ∈ J^-(z) ⊆ I^-(b) by
push-up. By the limit curve theorem (globally hyperbolic spacetimes are
strongly causal and non-imprisoning; e.g. Minguzzi 2008 or
Beem–Ehrlich–Easley, locator to be checked) a subsequence converges to a
past-inextendible causal curve γ from x. Its points are limits of points of
the closed set M \ I^-(b), so γ misses I^-(b), and x ∉ Set(b). ∎

**Corollary 1.2.** Set(b) depends only on the conformal class of the metric:
settledness is a causal-structure notion, so conformal diagrams decide it.

**Examples** [draft, all by Theorem 1.1].
- Minkowski spacetime, and flat FLRW with a big bang (conformal to the
  half-space η > 0): Set(b) = I^-(b). Nothing outside the fragment is settled.
- Einstein static universe: Set(b) = M for every b (past cones wrap round the
  3-sphere after conformal time π).
- Closed dust FLRW, a(η) = A(1 − cos η), η ∈ (0, 2π), conformal to a strip of
  the Einstein static universe: Set(b) = I^-(b) if η(b) ≤ π, and Set(b) = M if
  η(b) > π. For η(b) > π, I^-(b) contains the whole slice {η = c} for
  0 < c < η(b) − π. For η(b) ≤ π, the open ball I^-(b) ∩ S_c has radius < π,
  and containment of J^-(x) ∩ S_c reduces to d(X, B) < η(b) − η(x), i.e.
  x ≪ b.
- The transition η = π is the moment of **maximum expansion**. So in a closed
  dust universe, under deterministic laws, nothing beyond an event's causal
  past is settled while the universe expands, and everything is settled from
  every event once it begins to recollapse.
- Closed radiation FLRW (a = sin η, η ∈ (0, π)) and global de Sitter
  (conformal time span π): Set(b) = I^-(b) always. Whether the future ever
  closes depends on the matter content.

**Why it matters.** It gives the open-future debate a criterion that is
precise and physical rather than modal or logical, separates openness from
reality (answering Rakić and the process philosophers), and shows that
"determinism closes the future" is false in general relativity unless past
cones wrap round.

**Prior work (must check first).** Geroch, "Prediction in general relativity"
(1977), defines domains of prediction, and Manchak, "Is prediction possible
in general relativity?" (*Found. Phys.* 2008), studies them; Theorem 1.1 may be
a known characterization of Geroch's domain (from memory, unread). The
closed-universe transition may also be known. If so, the contribution is the
becoming-theoretic reading, not the geometry.

**Difficulty.** Low to moderate. **First steps:** get Geroch 1977 and Manchak
2008; check the limit-curve locator; decide the J^- versus I^- version.

---

## Path 2. The logic of standpoints is the horizon problem

**Big idea.** The modal logic of "from b, it is real that ..." depends on the
spacetime, and the place where it breaks is exactly a famous problem in
cosmology.

**Facts.** The standpoint frame (events, with b R x iff x ≤ b) is reflexive
and transitive, so S4 is valid. The axiom .2 (◇□A → □◇A) is valid on a
reflexive transitive frame iff the frame is directed (standard
correspondence). On the subframe generated by b, directedness says: *any two
events in b's causal past have a common causal past.*
- Goldblatt (1980): in Minkowski spacetime the logic is S4.2.
- The counterexample in `local-fragmentalism/NEW_PAPERS_CHECK.md` (the
  half-space t > 0) is conformally a flat big-bang FLRW universe: .2 fails.
- The **horizon problem** of standard cosmology is the statement that two
  points of the CMB in our past have no common past. So: *without inflation,
  the logic of our own standpoint is S4 but not S4.2; the horizon problem is
  the failure of modal confluence of our standpoint.* Inflation, by giving CMB
  points a common past, restores .2 for the observed pairs (though, given the
  Borde–Guth–Vilenkin incompleteness, perhaps not for all pairs).

**Open questions.** Which modal logics arise from globally hyperbolic
standpoint frames: S4, S4.2, others (e.g. with compact slices, black holes)?
Is the logic of all GH frames exactly S4? Do causal sets give the same
logics?

**Why it matters.** It connects formal metaphysics (standpoint logic, Lipman)
to observational cosmology by a single correspondence fact. It is the kind of
cross-disciplinary bridge a philosopher of time would find surprising.

**Difficulty.** Low for the correspondence and examples; moderate for full
classification results. **Risk:** novelty may be modest; the logic side is
standard. The bridge to the horizon problem is the point.

---

## Path 3. Where the grounding dispute bites: regions real from no one

**Big idea.** The red team's deepest objection (O2) was that local
fragmentalism agrees with eternalism on every truth, differing only in what
is fundamental. This path finds a place where the two orders of grounding
give *different facts*.

**Setup.** Suppose the standpoints that exist are the events on matter
worldlines (a physically motivated restriction: a standpoint is where
something happens). Then every event in J^-(matter) is real from some
standpoint, and nothing else is. In spacetimes with event horizons, some
regions are in the causal past of no matter at all. Example: a single star
in Schwarzschild–de Sitter. Its total causal past is bounded by its
cosmological event horizon, so the region beyond is real from no existing
standpoint.

**Consequence.** On eternalist grounding, that region has a definite geometry.
On local-fragmentalist grounding, where the geometry is the agreement of
standpoints (P5), there is no fact about it beyond what is forced by the
standpoints' fragments and the laws. Earman (2008, §6) already noticed the
epistemic shadow of this (observational indistinguishability, Malament 1977)
and the Broadhead/Blockhead stand-off over "ontic versus epistemic
underdetermination". The new point is that the grounding dispute is not
idle: it differs exactly over horizon-shadowed regions, a structural and
statable difference.

**Caveats.** In a homogeneous universe filled with matter, every event lies
in some matter event's past, so the difference vanishes there. The
restriction to matter standpoints must be reconciled with the theorem, which
uses all events (the relation is defined for all pairs; only which
standpoints *exist* is restricted). Laws may fix the shadowed region anyway
(domains of dependence), which would shrink the difference to regions not
fixed by the laws from seen data.

**Why it matters.** It converts O2 from "a fundamentality dispute, maybe
verbal" into "a dispute with a precise locus". That is a real move in the
debate.

**Difficulty.** Moderate, mostly conceptual, plus horizon geometry.

---

## Path 4. The light cone is physically underdetermined

**Big idea.** The theorem leaves one freedom: whether events on b's past
light cone are real from b. Two physical principles answer it, and they
disagree.
- *Signalling* (P6): light signals from the cone reach b, so the cone is
  real: J^-(b).
- *Algebraic accessibility*: by the timelike tube theorem (Borchers 1961 in
  Minkowski; Strohmaier and Witten 2023 in analytic curved spacetimes, from
  memory), observables localized near an observer's past worldline generate
  the algebra of its causal envelope, which for an inextendible past worldline
  ending at b is I^-(b): open, without the cone.

**Conjecture.** Under natural algebraic conditions, a locally covariant
assignment of "settled observables" to events must be A(I^-(b)), the open
option. If so, operational and causal criteria pick different ends of the
classification, and the light-cone freedom of Theorem 10 is not removable by
physics alone.

**Difficulty.** High (algebraic QFT; analyticity assumptions). **Risk:** the
envelope computation and the exact theorem statements need an expert.

---

## Path 5. Bell nonlocality makes local becoming trivial

**Big idea.** State the falsifier of STRONGEST_VIEW §8 as a theorem.
Formalize Clifton and Hogarth's maxim probabilistically: x has become for b if
the law's probability for what happens at b depends on what happens at x,
not screened off by b's causal past. In a relativistic collapse theory such as
Tumulka's flash ontology (rGRWf), Bell's theorem gives such dependence for
some spacelike x. A spacelike pair in B_M then forces universal becoming
(Theorem 7). So any local becoming theory obeying the maxim is trivial on
rGRWf models.

**Why it matters.** It makes "local becoming needs local (no-collapse or
perspectival) quantum theory" a theorem, not a slogan. **Difficulty:** low
mathematically; the work is a careful definition of probabilistic influence.
**Prior work:** Clifton and Hogarth's own quantum discussion; Maudlin,
*Quantum Non-Locality and Relativity*; Tumulka 2006. Check what is already
there.

---

## Path 6. Stein's theorem on shell (vacuum Einstein equations)

**Big idea.** Prove Theorem 7 in the category of vacuum spacetimes, or of
spacetimes satisfying the dominant energy condition.

**What is known here.** The off-shell auxiliary spacetime is impossible on
shell (Proposition "dec"). Flat pockets cannot be domains of dependence of
patches on the Cauchy surface carrying the curved slab, since disjoint
patches have causally separated domains (STRONGEST_VIEW O4); they must be fed
from other times. The natural tools are recent obstruction-free gluing
results: characteristic gluing (Czimek and Rodnianski) and Mao, Oh and Tao's
solution operators with prescribed support (from memory). An alternative
strategy would avoid flat pockets, using a "seed" class of vacuum spacetimes
where symmetry alone already gives B ⊆ J^- and gluing to those instead.

**Why it matters.** It removes the off-shell premise, the most-cited weakness.
**Difficulty:** very high; frontier mathematical GR; needs an expert
collaborator. **Verdict:** the ambitious long shot.

---

## Path 7. Becoming in causal-set dynamics

**Big idea.** Proposition 19 is kinematic. In classical sequential growth
(Rideout and Sorkin), birth order is gauge (label invariance), and only
covariant facts are physical. Show that the only covariant "has become"
relation compatible with sequential growth is the causal order, a dynamical
Stein theorem.

**Prior work:** Dowker's "birth of spacetime atoms as the passage of time";
Sorkin 2007; Earman 2008 §7. **Difficulty:** moderate; may be close to known
results on covariant observables.

---

## Ranking for narrowing

| Path | Novelty | Moves understanding | Difficulty | Can do alone |
|---|---|---|---|---|
| 1 Settledness | medium (Geroch risk) | high | low–moderate | yes |
| 2 Logic = horizon problem | medium | high (surprising bridge) | low | yes |
| 3 Grounding bites at horizons | high | very high (answers O2) | moderate | yes |
| 4 Light cone underdetermined | high | medium | high | partly |
| 5 Bell triviality | low–medium | medium | low | yes |
| 6 On-shell theorem | high | medium | very high | no |
| 7 Causal-set dynamics | medium | low–medium | moderate | yes |

**Recommendation.** Paths 1–3 together, as "Horizons and becoming". First
check Geroch 1977 and Manchak 2008 (Path 1 priority), then write Path 3
carefully, since it is the one that answers the strongest objection to the
view.
