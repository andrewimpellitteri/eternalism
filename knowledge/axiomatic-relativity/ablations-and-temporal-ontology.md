# Ablation table and candidate-C marking: which assumption-dependency results are already settled

Status: review submission, 2026-10-19. Lane `kb-axiomatic-relativity`.
Companion to `axioms-and-theorems.md` (statements and locators live there).
No novelty claim is made anywhere in this file; §3 lists what would defeat any
candidate seam.

## 1. Ablation table — Malament line (simultaneity definability, Minkowski)

"Already settled" = the ablation's outcome is proved in at least one
full-text-read source, or re-derived with an explicit correction in one.

| # | Ablated / varied assumption | Base case | Outcome when varied | Status | Source (ID, locator) |
|---|---|---|---|---|---|
| A1 | Remove observer X (κ alone) | (X,κ): Σ_X unique (M-condition) | Only universal relation definable; no absolute simultaneity | settled | found-malament-1977 Prop 3 (FULL); axrel-giulini-2001 Thm 4; axrel-mamone-capria-2012 Cor 3.9 |
| A2 | Remove time-reflection invariance (= grant time orientation) | Malament base | One-parameter family Γ_{X,v}^{±} (v ∈ ]0,∞]) incl. light-cone relations; Σ_X only as limit | settled | axrel-ben-yami-2006 (SEC via seed-besnard-simultaneity §2); seed-besnard-simultaneity Thm 3.1 (FULL, explicit versions); priority: axrel-spirtes-1981 (META) |
| A2′ | Same, geometric form | — | Translated half-cones of *arbitrary* opening angle on X also satisfy all non-time-reflection conditions | settled | axrel-giulini-2001 §5 Eqs. (25)-(26); axrel-mamone-capria-2012 Thm 3.19(1) |
| A3 | Remove dilation invariance | Malament base (causal automorphisms include dilations) | Uniqueness lost: 4 kinds of invariant classes (hyperplanes, unions mod λ, the line, lattice points), plus pathological "onion"/shell relations | settled | axrel-giulini-2001 Thm 5 + §5 (FULL); corrected by axrel-mamone-capria-2012 Thm 3.17 (everywhere-dense subgroups missed by Giulini) |
| A4 | Replace worldline X by inertial frame Ξ (pencil of parallel lines) | Malament base | Einstein-frame simultaneity unique under soundness condition (classes meet realizable trajectories ≤ once) | settled | axrel-giulini-2001 Thm 6 (FULL); axrel-mamone-capria-2012 Thm 3.17(B); claim originates in found-sarkar-stachel-1999 (SEC) with a proof gap found by Giulini |
| A5 | Replace symmetric κ by directed causal order ⪯ | κ base | Same one-parameter family as A2 (structure equivalence: (X,κ,<) ↔ (X,⪯) ↔ (X,κ,Or)) | settled | seed-besnard-simultaneity Thm 2.4 + Thm 3.1 (FULL); axrel-ben-yami-2006 (SEC) |
| A6 | Add chronology/order on X (a "bad clock": monotone, possibly uneven) | (X,κ) base | Equivalent to adding time orientation; conic family becomes explicitly definable; Σ_X no longer unique | settled | seed-besnard-simultaneity Thm 2.4 (first equivalence) + Thm 3.1 (FULL) |
| A7 | Add clock T̃ (proper-time parametrization up to constant) | A6 base | (X,κ,T̃) ↔ (X,η,Or); definable equivalence relations satisfying (B) are exactly Γ_{X,f̃} for arbitrary radial profile f — complete arbitrariness | settled | seed-besnard-simultaneity Thm 2.4 (third equivalence) + Thm 4.1 (FULL) |
| A8 | Replace global κ by local light-cone data L_X (only cones based on X) | Malament base | *No* non-trivial invariant equivalence relation at all; Σ_X disappears; with ordering only Λ_X^{±}; with clock all Γ_{X,f} explicit | settled | seed-besnard-simultaneity Thm 5.1 (FULL); uses 2-dim-only non-affine causal automorphisms (via Zeeman) |
| A9 | Vary soundness criterion (M / G / B / BY / none) | M | Different classifications per criterion; tabulated | settled | seed-besnard-simultaneity §2 table (FULL); axrel-giulini-2001 Req.1/2; axrel-hogarth-2005 via axrel-mamone-capria-2012 Prop 4.1 |
| A10 | Vary automorphism group systematically (Newton / Galilei / Poincaré / isotropy subgroups / conformal lifts) | Poincaré | Complete classifications; corrections to earlier papers (everywhere-dense subgroups); join of two non-proportional synchronies is universal; meet of four is identity | settled | axrel-mamone-capria-2012 Thms 2.5, 3.3, 3.6, 3.17, 3.19, Props 3.8-3.10 (FULL); axrel-giulini-2001 Thms 2-6 (FULL) |
| A11 | Drop the equivalence-relation requirement itself | all of the above assume equivalence relations | Challenged as question-begging by conventionalists (Grünbaum, Redhead per SEP; Mamone-Capria §4); **no positive classification of non-transitive/non-symmetric simultaneity-like relations found in this lane** | open (as far as sources read show) | axrel-grunbaum-2010 (META+SEC); axrel-sep-convensimul-2018 §3-4 (FULL); axrel-mamone-capria-2012 §4 (FULL) |
| A12 | Relate to physics: two-way light isotropy + causality preservation | — | Already forces standard synchrony up to scale, without ε-choice | settled | axrel-mamone-capria-2012 Thm 3.15 (FULL) |

## 2. Ablation table — Budapest FOL line (relativity axioms)

| # | Ablated / varied axiom | Base | Outcome | Status | Source (locator) |
|---|---|---|---|---|---|
| B1 | AxEv → AxMeet_n hierarchy | SpecRel | Strictly increasing finite-meeting hierarchy; does not reach AxEv even in the limit | settled | seed-axiomatic-relativity Prop 6.1 (FULL; countermodels in proof) |
| B2 | AxEv vs (AxMeet_3 + no stationary light) | SpecRel | AxMeet_3, AxFd, AxPh, Ax(c≠0) ⊢ AxEv; AxMeet_2 insufficient; Meet_ω+AxPh insufficient (c=0 model) | settled | seed-axiomatic-relativity Prop 6.2 (FULL) |
| B3 | Allow per-observer light speed c_m, or c_m = 0 | AxPh | Axiom formulation permits it; c=0 model constructed | settled (at axiom-design level) | seed-axiomatic-relativity Sec. 5-6 (FULL) |
| B4 | Drop AxDf (differentiability) from AccRel | AccRel ⊢ TwP | AccRel−AxDf still ⊢ TwP | settled | seed-axiomatic-relativity Thm 7.1 item (8) (FULL), citing axrel-madarasz-nemeti-szekely-2006 (META) |
| B5 | Drop Cont (definable-suprema scheme) from AccRel | AccRel ⊢ TwP | Independence: AccRel−Cont ⊬ TwP, and Th(ℝ) ∪ AccRel−Cont ⊬ TwP — not repairable by strengthening number theory | settled | seed-axiomatic-relativity Thm 7.1 items (9)-(10) (FULL) |
| B6 | Promote all axioms from inertial-only to all-observers local versions | AccRel | GenRel; completeness w.r.t. Lorentzian manifolds over real closed fields (Thm 8.1) | settled (statement; deeper proofs in cited META sources) | seed-axiomatic-relativity Sec. 8 (FULL); axrel-andreka-etal-2012-logic-road (META) |
| B7 | Comprehension scheme Compr for geodesics | GenRel | GenRel⁺: FOL geodesic = standard geodesic; curvature/metric definable | settled (statement) | seed-axiomatic-relativity Sec. 8 (FULL) |

Caveats: the Budapest table reflects the 19-page introductory paper only. The
school's deeper ablation corpus (2002 report — dead link,
axrel-andreka-etal-2002-report; Székely 2009 thesis; Handbook chapter; the
Studia Logica twin-paradox papers) was not accessible this pass, so B1-B7 is
certainly *not* the complete list of settled FOL ablations.

## 3. Candidate C of knowledge/NOVELTY.md — marking against this corpus

Candidate C asks: which combinations of symmetry, locality, definability,
global foliation, and ontological premises force a disputed conclusion; it
names axiomatic relativity, Malament/Stein, directed-time variants, and
Besnard as nearest predecessors, and rejects mere restatements of known
independence results.

**Already done by the literature (any candidate-C proposal must position
against these, and cannot re-claim them):**

1. The full A1-A10 ladder above: symmetric vs directed causal primitive,
   time-reflection, dilations, worldline vs frame, chronology, clock, global
   vs local data, soundness criteria, automorphism-group systematics. The
   "assumption-dependency graph" for Minkowski simultaneity definability
   essentially exists, scattered across Malament 1977, Ben-Yami 2006, Giulini
   2001, Hogarth 2005, Besnard 2011, Mamone-Capria 2012. Besnard §2's own
   table is a partial version of exactly this.
2. Stein's becoming-side uniqueness (event-relative becoming with an
   event's present = itself) and the Callender objection — the ontological
   analogue of the uniqueness/latitude pair (axrel-sep-bebecome-2021).
3. The FOL ablations B1-B6, including a genuinely subtle one (B5: Cont vs
   Th(ℝ)) that is the kind of result candidate C would want to produce.
4. The meta-lesson that uniqueness results are conditional on the constraint
   list and do not settle conventionality (Janis's latitude; Grünbaum 2010;
   Mamone-Capria's own negative conclusion) — so "new classification theorem"
   alone does not satisfy candidate C's ontology-facing ambition.

**Seams observed but NOT claimed as gaps** (each needs its own
defeat-search before any proposal; stated with explicit defeaters):

- S1. Cross-program composition: no source read runs Besnard-style
  definability questions *inside* non-standard models of the FOL systems
  (e.g., what simultaneity relations are definable in models of
  SpecRel−AxEv, or in GenRel/Lorentzian-manifold models, where global κ is
  not available). Defeater to search first: Besnard's or others' curved-
  spacetime follow-ups; the inaccessible 2002 report and Székely thesis;
  Mamone-Capria's announced future work; anything citing Besnard 2012
  (Found. Phys.) forward in time.
- S2. Machine-verified ablations: no source read machine-checks any of the
  A1-A10 classifications. The nearest prior art in the KB is
  seed-isabelle-relativity (Isabelle/HOL, hypercomputation focus — different
  target). Defeater: any Lean/Isabelle formalization of Malament-type
  theorems; search physlib/PhysLean, Isabelle AFP, and "Malament" in
  formalization repositories before claiming formalization novelty.
- S3. Non-equivalence simultaneity relations (A11): challenged
  philosophically, but no classification found in the read corpus.
  Defeater: Winnie 1970a,b (reformulation of SR in non-standard synchronies)
  and Minguzzi 2002 (one-way speed as scalar field), both flagged by the SEP
  entry but not read this pass; also Reichenbach-ε literature at large.
- S4. Locality/operational access as an explicit axiom: Besnard Thm 5.1 is
  the nearest result; a graded "access hierarchy" (what an observer with
  bounded records can define) is not in the read corpus — but this is close
  to candidate A of NOVELTY.md and must not be double-counted; defeat-search
  in the operationalism literature (Bridgman tradition, per SEP) required.

Nearest predecessors to any candidate-C output, ranked: Besnard 2011 (full
explicit-definability ladder), Mamone-Capria 2012 (group-systematic ladder
with corrections), Giulini 2001 (frame vs worldline, physical group),
Malament 1977 (base uniqueness + κ-alone negative result), Ben-Yami 2006
(directed primitive), the Budapest school (FOL ablations), Stein 1968/1991
(becoming-side uniqueness), Hogarth 2005 (soundness variant), Spirtes 1981
(priority for A2), Robb 1914 (causal axiomatization ancestor).

## 4. Ontology separation checklist (per research standards)

Each row: what it is, and whether any extracted theorem bears on it.

| Notion | Status in this corpus |
|---|---|
| Temporal ontology (eternalism/presentism/GBlock/spotlight) | not decided by any theorem; needs bridge premises; SEP bebecome §3.2 (Sellars/categorial-existence point) is the clearest warning |
| Objective passage | absent from all extracted theorems; Stein's R is a *definition*; Callender objection recorded |
| Determinism / fixedness of future | untouched; Rietdijk-Putnam-Penrose arguments are philosophy over kinematics; Stein's theorem is their conditional countermodel |
| Causal order ⪯ | invariant, observer-independent (Zeeman/Alexandrov); NOT interchangeable with simultaneity |
| Simultaneity | structure-relative; uniqueness always relative to a constraint list (A1-A10) |
| Clock time | proper time T along worldlines (Stein 1968 fn 6; Besnard T̃); distinct from coordinate time x_t of Part 1 and from ⪯ |
| Thermodynamic arrow | entirely absent from this corpus; do not import |
