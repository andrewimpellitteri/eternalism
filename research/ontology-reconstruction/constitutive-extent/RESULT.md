# RESULT — Constitutive temporal extent beyond predictive sufficiency: a Newtonian bound-system test

30 October 2026. Worker `ontology-constitutive-extent-test` (isolated worktree,
branch `agent/ontology-constitutive-extent-test`). This is a submission for
coordinator review, not an accepted result and not a truth claim. It executes
`research/ontology-reconstruction/coordinator/NEXT_PHILOSOPHICAL_TESTS.md` §2
against `CONSTITUTION_IS_NOT_PREDICTION.md` (both at commit `1d1102a`).
Labels: **[A]** analytic argument given here; **[S]** standard or cited
result with locator; **[W]** witness illustration in
`check_constitutive_extent.py` (illustration only, never a proof).

Primary Brading passages were read first-hand this run from hash-verified
public copies (SHA-256 below); Savitt's §3.3 was fetched first-hand from the
live entry. No claim below is a novelty claim.

---

## 0. Verdict in brief

The requested unity criterion **can** be stated for an explicit Newtonian
bound system independently of any desired present region (§2), and its
activity scale is fixed by the system's parameters, not chosen by us [W, C4].
But the test returns a largely **negative** core result: for Markovian
Newtonian dynamics (instantaneous-interaction point mechanics, conservative
or driven), *no* criterion expressible in physical quantities can
discriminate "genuinely constitutive extent" from "predictively sufficient
extent", because every candidate constitutive fact — including interval
activity facts — is reconstructible as a functional of the instantaneous
state plus the law (§4, the **reconstruction dilemma**). Where the physics
*does* force a non-instantaneous sufficient region (the delayed-coupling
boundary case, §3.3), the forced window is a fact about **determination**,
and it comes apart from **unity** (concrete instances α, β); so the forced
window is not thereby constitutive either. Both bridges fail as inferences:
determination neither implies nor is implied by unity (§5.1), and unity
delivers an extent but no anchoring and no concrete-inventory rule (§5.2).
The exact missing premise is isolated in §4: **constitution is process
rather than state+law** — a philosophical bridge premise that no Newtonian
bound system tests. A negative result was acceptable per the brief; this is
that negative result, with the positive residue stated precisely.

---

## 1. Strongest counterexample first: the state–law reconstruction

The strongest rival to any constitutive-extent thesis is the
**instantaneist reconstruction**, on exactly the same physics:

> For each time t, the unity of the bound system is wholly grounded in the
> instantaneous state s_t together with the admitted law L. Every
> "sustaining" fact — mutual forces, binding energy, work, exchange,
> averaged or Floquet stability, loop closure — is a functional of s_t and
> L. Brading's "spatiotemporal region necessary to sustain the dynamical
> system" (2013, 1109) is then either (i) the instantaneous configuration
> of the interacting parts, or (ii) an interval whose claim to be *the*
> constitutive region rests on an additional premise — that sustaining is
> process rather than state+law — which the dynamics itself never tests.

This rival reproduces every physical fact in §3, including all witness
numbers [W]. It is not refuted by the failure of *naive* instant criteria:
§3.2 [W, C2] shows an instantwise sign criterion misclassifying a driven
bound state, but the correct classification (Floquet/averaged) is itself
state+law reconstructible, so the failure is of one instant-level
functional, not of instantaneism. Any successful argument for a
constitutive *interval* must therefore supply the process premise from
outside Markovian dynamics. That is the burden this test clarifies; it is
not discharged here, and §7 shows it is not discharged in the prior
literature either.

---

## 2. The physical system and the unity criterion (criterion before extents)

Per the brief and coordinator §2: one bounded interacting system, Newtonian,
criterion stated before any present region is selected.

### 2.1 Systems (not a universe-wide claim)

Primary system: the **Newtonian gravitational two-body bound pair** (Kepler
ellipse), reduced one-body form r″ = −GM r/|r|³, units GM = 1, a = 1,
e = 0.5, period T = 2π [A: standard conic; W, C1]. Two stress variants of
the same bound-pair template:

- **Kapitza driven inverted pendulum** (pendulum + driven pivot + gravity):
  θ″ = [g/L + (aω²/L) cos ωt] θ near upright; standard stability boundary
  a²ω² > 2gL [S: Kapitza 1951, Soviet Phys. JETP 21, 588; Landau &
  Lifshitz, *Mechanics* (Pergamon 1960); locators verified via the
  reference list of arXiv:2102.12711v1, not collated against the primaries].
- **Delayed-feedback bound oscillator** (particle + feedback actuator):
  x″ + 2γx′ + ω₀² x(t−τ) = 0 — still Newtonian second law, but
  non-Markovian; a laboratory analogue (feedback trap) has physically
  integral delay and update times [S: Jun & Bechhoefer, PRE 86, 061106
  (2012), abstract and §I read first-hand from the author-hosted PDF].

The delay variant marks the boundary of the Newtonian bound-system's
adequacy; it stays Newtonian and subsystem-scale. No global foliation and
no universe-stage extrapolation is used anywhere below.

### 2.2 Criterion U (law-constitutive unity), stated before any extent choice

A composite of parts {p_i} is **one dynamically sustained system** on a
parameter window iff:

- **U1 (interaction):** the parts exert non-negligible mutual forces in the
  model's equation of motion (third-law paired; connected coupling graph).
- **U2 (boundedness):** the relative configuration is bounded, with the
  bound carried by the internal dynamics — Kepler: E_int < 0 with
  conservation [A]; Kapitza: Floquet multipliers of the upright solution
  inside the unit circle [S]; delay loop: sup Re(characteristic roots) < 0
  [S: standard linear-DDE stability; instances W, C3].
- **U3 (activity):** the coupling does work in the window: internal energy
  is exchanged among the parts (gross ∫|F·v| dt > 0), the interaction not
  merely assigning but redistributing the conserved quantities.
- **U4 (autonomy):** external influences are negligible or benign over the
  window, so the model closes on these parts (the composite is a genuine
  subsystem in Brading's 2013, 1110 sense).

**Independence from the desired present region.** U1–U4 mention only the
dynamics: forces, bounds, work, closure. No clause mentions "now",
"present", concreteness, or which region we would like to be real. The
window length w entering U3 is fixed by the system's own activity scale —
orbital period, drive period 2π/ω, or loop latency τ [W, C4] — not chosen
to fit an intended inventory. **Uniqueness is not claimed**: any window
containing a complete activity cycle satisfies U (e.g. [t−T, t] as well as
[t−T, t+T]); Brading's own proposal quantifies over "whatever size is
necessary", and nothing below requires a unique ground.

Criterion U is the coordinator's requested item: "the constitutive
criterion … identify the relevant unity independently of the desired
inventory" (CONSTITUTION_IS_NOT_PREDICTION §3). It exists. The question
the task poses is what it can then *do*. That is tested next.

---

## 3. The comparison: predictively sufficient extents vs. candidate constitutive extents

"Predictively sufficient" region: a region whose data, with the admitted
law, fix all readings of the system's evolution (the coordinator's
determination relation). The test: take two predictively sufficient extents
that criterion U treats differently, and ask whether the physics itself
upholds U's verdict.

### 3.1 Kepler pair (conservative, Markovian)

Sufficient extents: any instantaneous state Σ_t; any trajectory segment
I = [t₀, t₀ + τ]. All determine the whole solution [A: determinism of the
Kepler initial-value problem; W, C1: integration from the periapsis state
and from the half-period state conserve E = −1/2 and L to machine
precision and lie on the same conic].

Criterion U separates them *by construction*: U3's work is an interval
integral, so W(t, t) = 0 for every instant while gross exchange over one
period is positive [W, C1: 2.667 in units, with net work over the closed
orbit exactly 0]. So U says: segments constitute, instants merely carry
data. **But the separation is not physics doing work**: the very same
activity facts are functionals of Σ_t and L (the integral of |F·v| along
the flow from s_t is a function F(s_t)) [A; W, C1 computes all four
quantities from the single periapsis state]. The criterion discriminates;
the physics does not underwrite the discrimination. What the instant
lacks — activity — is definable from the instant plus the law; nothing is
physically present in the segment that is not physically determined by the
instant. Scattering states make the same point for U2: a hyperbolic pair
is equally deterministic while failing U2, so determination never entailed
unity (§5.1).

### 3.2 Kapitza pendulum (driven, Markovian)

Here the naive instant-level criterion demonstrably fails: the
instantaneous stiffness g/L + (aω²/L) cos ωt is positive — destabilizing —
on about 50.4% of the drive cycle *in the stable case* a = 0.2, ω = 20
[W, C2], while the Floquet multipliers sit inside the unit circle
(|Tr M| = 1.308 < 2); in the unstable case a = 0.02 the sign criterion is
right for the wrong reason and |Tr M| = 2.092 > 2 [W, C2]. So "binding" is
*not* readable off the instantaneous force sign [A + W].

One might take this as physics vindicating the activity reading: the
binding fact lives on the drive period. It does not. The correct
criterion — a²ω² > 2gL [S: Kapitza; Landau–Lifshitz], equivalently the
period monodromy — is a function of the law parameters and of one period
of the flow from s_t, hence state+law reconstructible [A]. The interval
object and the parameter inequality agree exactly [W, C2]. The drive
period is where the *computation* lives, not a fact the dynamics marks as
ontologically privileged. This is the sharpest single illustration of the
dilemma: the physically correct binding criterion is period-indexed and
instant-reconstructible at once.

### 3.3 Delay loop (non-Markovian Newtonian boundary case)

For x″ + 2γx′ + ω₀² x(t−τ) = 0, no instantaneous slice is predictively
sufficient: two histories agreeing at t = 0 in (x, x′) = (0, 0) — h₀ ≡ 0
and h₁(t) = ε sin²(πt/τ), which has h₁(0) = h₁′(0) = 0 — have different
futures for t > 0, since the delayed term differs [A: uniqueness of DDE
solutions from segment data; W, C3: sup difference 0.0059 on [0, 2]]. The
minimal sufficient region is the segment [t−τ, t], its length forced by
the coupling latency, not chosen [A: method of steps; W, C3]. This is the
one place in the test where predictive sufficiency itself is
non-instantaneous — Brading's contrast between the "sufficient dynamical
ground of a given unity" and "the abstract spatiotemporal structure within
which the evolution … is completely described" (2013, 1109) acquires a
physical foothold: here there is no sufficient instantaneous description
at all.

But the foothold is a determination fact, not a unity fact. Window-necessity
holds for *all* parameter values, while unity (boundedness) holds only for
some — concrete instances on the same window [W, C3]:

- **α** γ = 0 (pure delayed spring): unstable for every τ > 0 — at τ = 0
  the characteristic roots are λ = ±iω₀ and ∂λ/∂τ = +ω₀²/2 > 0 there
  [A: perturbation of F(λ, τ) = λ² + ω₀²e^{−λτ}; dominant root at ω₀τ = 0.5
  computed: Re λ = +0.2165; trajectory grows, max |x| = 1.45 by t ≤ 20,
  W, C3]. Prediction needs the window; the loop does not bind.
- **β** γ = 2: dominant root Re λ = −0.3185; bounded, decaying
  (max |x|: 0.0059 early → 0.00008 late, W, C3). Prediction needs the
  same window; the loop binds.

So even where sufficiency is forced to be interval-shaped, the unity
criterion U2 does independent work, and determination-to-unity fails as an
inference in both directions (§5.1). The dilemma of §4 then recurs at the
window level: any activity fact over the window is a functional of the
segment data plus the law; a segment-privileging verdict needs the same
philosophical premise as before, one level up.

---

## 4. The reconstruction dilemma — exact statement of the negative result

**Dilemma.** Let a model be Markovian: state s ∈ X, law L, flow φ; call a
quantity *physical* if it is a functional of the model solution. Then any
physical quantity evaluated on any region of the solution — instants,
intervals, works, averages, Floquet objects, loop facts — is a function of
the initial data of that region together with L; for an instantaneous
region, of s and L alone [A: determinism]. A unity criterion C
stating "the parts are one system" is then either:

1. **(State-law evaluable.)** C's satisfaction at t is fixed by (s_t, L).
   Then instantaneous extents satisfy C whenever the constitutive-extent
   candidate does, and C cannot discriminate constitutive from predictive
   extent. (Instances: U1, U2, U4 are of this type; so is the
   period-indexed Floquet binding of §3.2.)
2. **(Primitive-process.)** C contains a predicate — e.g. "*this activity*
   constitutes the unity" — not defined by physical functionals. Then the
   discriminating work is done by that predicate, i.e. by the premise

   > **(P)** The ground of a system's unity at t is the process over an
   > interval of activity, not the instantaneous state under the law,

   which is a philosophical bridge premise, not a result of Newtonian
   dynamics. Adding P to U3 makes the criterion discriminate by fiat of P.

Either way, within Markovian Newtonian physics the contrast between
"genuinely constitutive activity" and "predictively sufficient data" is
not a physics-level distinction. In the non-Markovian delay case the same
argument re-applies one level up, with window data in place of the instant
[A: §3.3]. **The exact missing premise is P.** This records, in the
coordinator's requested form, the finding that no independent criterion is
available at physics level: "If no independent criterion is available,
record that as the exact missing premise" (CONSTITUTION_IS_NOT_PREDICTION
§8).

What the test nonetheless *succeeds* in establishing:

- U1–U4 are statable before extent selection, and U3's scale is
  law-fixed [W, C4] — the physics constrains the *duration scale* of any
  sustaining region (period, drive period, latency). This is a real
  constraint on candidate presents, stronger than the unconstrained
  "any Cauchy slice" family.
- The Kapitza case refutes naive instantaneism (the instantaneous-force
  sign criterion) as a *specific physical criterion*, even though it does
  not touch the reconstruction thesis [W, C2].
- The delay case refutes the assumption that predictive sufficiency is
  always instantaneous: in delayed-coupling systems there is *no*
  sufficient instantaneous description, and the sufficient window's
  length is physics-fixed [A, W, C3].

The question "which reading of sustaining — state+law or process — is
correct" is thus underdetermined by the tested physics, in both the
Markovian and the forced-window case. That is the honest outcome of the
test the brief requested; it is a negative result, recorded rather than
papered over.

---

## 5. The two bridges, separated

### 5.1 Determination → unity: fails in both directions [A]

- **Determination ⊬ unity.** A Kepler scattering pair (E > 0) is
  predictively sufficient — same determinism, same fixity of readings —
  while failing U2; the delay loop of §3.3-α needs its window for
  prediction while diverging. Sufficiency is unity-blind.
- **Unity ⊬ determination(-region identity).** Where unity holds, the
  region U selects (activity scale) is neither the minimal sufficient
  region (the instant, in §3.1) nor determined by sufficiency facts (the
  window in §3.3 is fixed by latency whatever U2 says; instances α/β
  share it with opposite unity verdicts).

So the first bridge of CONSTITUTION_IS_NOT_PREDICTION §1 cannot be crossed
by strengthening the determination theorem; the two families of extents
cross-cut. This sharpens, at subsystem scale, the coordinator's finding
that many regions are predictively sufficient without one of them being
*the* present (ibid. §2): the sufficiency relation is orthogonal to the
constitution relation, not merely non-unique.

### 5.2 Unity → current concreteness: needs anchoring and inventory premises the criterion does not supply [A]

Grant everything in §2: the pair is one system, U-satisfying, with
law-fixed activity window w. What follows about what is *concretely
present* for the system? Three gaps:

1. **Anchoring.** U is time-translation invariant (Kepler flow, Kapitza
   drive, delay loop are all homogeneous in t). The dynamics fixes w but
   does not mark any window as *now*; "current" concreteness needs an
   indexical anchor the criterion does not contain.
2. **Tense asymmetry.** Any U-window straddles earlier and later
   parameter values relative to any anchor. Calling that window "the
   present" requires either rejecting the ordinary asymmetry of past and
   future within the present or adding structure; neither is supplied by
   U1–U4.
3. **Inventory rule.** That the window grounds the system's unity does
   not decide what exists *for* the system now — the window, its
   boundary events, the whole subsystem history, or events outside it.
   The symmetric shortcuts are already blocked at coordinator level
   (CONSTITUTION_IS_NOT_PREDICTION §4: explanatory sufficiency is not
   ontological dispensability; mathematical containment is not
   current existence). §3 confirms this at subsystem scale: derivability
   of the trajectory from Σ_t did not eliminate the trajectory's
   occurrences, and containment of them in the segment does not make them
   the present inventory.

**Independent reasons for the bridge.** The only candidate reason found in
the primary texts is Brading's own grounding claim: "The ground of what is
real is the dynamics" (2013, §8, p. 1110, read first-hand) and her
footnote: "All the ontology is carried by the dynamics" (2013, fn. 7,
p. 1109–1110 area, read first-hand). These are grounding premises, not
physical results; she herself marks the substantive question — whether the
sufficient dynamical ground of a unity is much smaller than the structure
of its complete description, "or it might be the size of the block
universe" — as "an empirical matter, something to be settled by the
progress of science" (2013, 1109, read first-hand). Our test adds a
precise finding she does not make: for Markovian dynamics that empirical
matter is not settled by any dynamical criterion statable in physical
quantities, because of §4; and for delayed systems the empirical matter
splits into a determination half (settled: windows forced) and a
constitution half (still P-dependent). No non-question-begging physical
route from U to concreteness was found. This is a negative finding about
the second bridge, consistent with the coordinator's judgment that
"constitution and the interpretation of actual occurrence now carry the
burden" (CONSTITUTION_IS_NOT_PREDICTION §7).

---

## 6. Rival inventories, assessed symmetrically

All four rivals below accept the same dynamics, the same successful
predictions, and all U1–U4 facts (they are physical). None is selected by
the tested physics. Grounding rules are preserved per rival; no primitive
counting and no weighted scoring (per EXPLANATORY_ROLE_TEST v2, cited by
the coordinator).

| Inventory | Present extent claimed for the pair | What it does with U | Cost it must pay | What would favor it |
|---|---|---|---|---|
| **I** instantaneist stage (the §1 reconstruction) | instantaneous interacting configuration {p₁(t), p₂(t)} (Newtonian instantaneous coupling) | treats "sustaining" as state+law grounding; handles Kapitza via Floquet-as-function | must reclassify Brading's sustaining talk as process-talk without ontological weight; needs P to be *false*, which is also untestable here | if constitution is admitted to be state+law definable, I is the minimal consistent reading |
| **P** process/activity (Brading-style, with P added) | activity window w (law-fixed scale) | U3 read as constitutive work | must assert and defend P (constitution = process); must add an anchoring story for "now" (§5.2.1–2) | if P is independently defended, P explains why the pair is *one* thing persisting rather than recurring stage-wise |
| **W** subsystem block | the pair's entire worldline segment (whole subsystem history) | U facts as internal structure | must explain why *this* extent, not the window, is the present — the same anchoring gap at larger scale; sacrifices locality that motivates Brading's subsystems (2013, 1110) | if concrete relations among all events of the pair need no cutting, W gets maximal relational richness at no physical cost |
| **E** event realism (coordinator framing) | no privileged present; concrete events, "present of a system" derivative | U as ordinary physics | abandons the presentist aim Brading retains | if no anchoring story is defensible for any extent, E avoids the gap by giving up the aim |

The symmetric verdict: I and P are exactly balanced by §4's dilemma — the
difference between them is P, and no tested dynamics bears on P. W and E
each pay an anchoring or aim cost that the others also pay somewhere.
The test's contribution is to make the balance precise, not to break it.
**No conclusion about which inventory is true is drawn.**

---

## 7. Prior-result audit (what is not new here)

- **The constitutive/predictive contrast is Brading's own.** "The
  spatiotemporal extent of the sufficient dynamical ground of a given
  unity might turn out to be much, much smaller than the abstract
  spatiotemporal structure within which the evolution of that unity is
  completely described, or it might be the size of the block universe"
  (2013, 1109; read first-hand from the hash-verified copy) states exactly
  the ground-versus-complete-description distinction this task tests. The
  present-definition "a spatiotemporal region of whatever size is
  necessary to sustain the dynamical system in question" (2013, 1109) and
  the subsystem premise (2013, 1110) are likewise hers. P1** (a)/(b) and
  "In order to avoid the block universe, all we need is (a)" are 2015,
  p. 17 (read first-hand). Nothing in this RESULT improves on her
  statement of the contrast; the delta is only the §4 dilemma and the §3.3
  boundary case.
- **Savitt's objections** (SEP, "Being and Becoming in Modern Physics",
  §3.3, substantive revision 6 Oct 2021; fetched first-hand this run):
  population (every dynamical system past, present, future has a
  sustaining region) and co-presence (undefined when two systems share a
  present) anticipate, respectively, part of §5.1's separation (regions
  are abundant and not present-selecting) and the anchoring gap of §5.2.
  His verdict — "a characterization of a relativistic present, not
  relativistic presentism" — is the bridge-2 negative in prose. §5 confirms
  it at subsystem scale with the two bridges separated; no reply to Savitt
  is attempted or found.
- **Müller 2019** (Found. Phys. 49; DOI 10.1007/s10701-019-00267-x;
  abstract read): defines a relativity-proof dynamic-role present via
  spatio-temporal indeterminism and co-presentness. Different mechanism
  (indeterminism, not sustenance) and global-system scale, but the same
  goal of a dynamics-sensitive present. Any future development of §5.2
  must engage it. Open question (not read at full text): whether his
  indeterminism-based co-presentness can be transposed to the
  sustaining-region setting.
- **Dowe 2000** (Physical Causation, CUP; DOI 10.1017/cbo9780511570650;
  abstract read): conserved-quantity account of causal processes and
  interactions. This is an existing physical explication of "process" that
  a defender of P would reach for; it is not a transposition to
  present-extent, and Dowe does not address unity or the present. Open
  question: whether Dowe-process constitution of U3 escapes §4's dilemma
  or is itself state+law reconstructible (as a worldline property it
  appears to be — flagged for a future lane, not adjudicated here).
- **Kapitza / dynamic stabilization physics**: Kapitza 1951 (Soviet Phys.
  JETP 21, 588; Usp. Fiz. Nauk 44, 7) and Stephenson 1908 (Phil. Mag. 15,
  233) — locators verified via the reference list of arXiv:2102.12711v1
  (abstract + intro + references read); primaries not collated. The
  effective-potential construction is the standard physics behind §3.2;
  no novelty is claimed for it or from it.
- **Feedback-trap physics**: Jun & Bechhoefer 2012 (PRE 86, 061106,
  DOI 10.1103/PhysRevE.86.061106; abstract and §I read first-hand from the
  author-hosted PDF): feedback traps have physically integral delay,
  update time, and exposure time; the trappable size limit is set directly
  by the sampling time. This grounds the §3.3 idealization as a real
  laboratory kind, not a mathematical fiction.
- **Callender's "now patches"** are named by Savitt §3.3 as items on the
  same list of candidate relativistic presents; the project's existing
  `phil-callender` record (publisher-abstract depth) covers it; no
  separate reading this run.

**Not established as new:** the dilemma of §4 is a determinism observation
in the project's own style ("a definition that already assumes … cannot
independently establish it", AGENTS.md research standards) and may exist
in the determinism/emergence literature under other names; the searches
below did not find this exact formulation applied to Brading's
sustaining-region proposal, but absence beyond searched venues is not
evidence of absence (the prior audit hit the same PhilPapers wall:
`paper/reviews/savitt-delta/REVIEW.md` §6). No novelty verdict is claimed.

---

## 8. Falsifier and scope

**Precise falsifier of the central negative claim (§4).** Exhibit a bounded
physical system with Markovian dynamics and a unity criterion C, statable
without reference to any desired present region, such that (i) some region
satisfies C, (ii) C is not equivalent to any state+law functional — i.e.
two systems with identical instantaneous state and law differ in C — and
(iii) the difference is established by the dynamics, not by a philosophical
premise. Within Markovian dynamics (ii) cannot hold, since determinism
makes all physical functionals agree [A]; hence any falsifying instance
must be non-Markovian — and §3.3 shows that there the dilemma re-forms at
the window level. A genuine falsifier would therefore need dynamical facts
that are not functionals of *any* initial-data region, and a demonstration
that those facts constitute unity rather than merely constrain it.

**Sub-falsifiers.** (a) A bounded zero-input solution of ẍ = −ω₀² x(t−τ)
with τ > 0 would falsify instance α's instability (and the dλ/dτ argument)
[W, C3 computes Re λ = +0.2165 at ω₀τ = 0.5]. (b) A law-fixed parameter
set admitting a continuum of equally admissible activity scales would
falsify C4's law-fixed-scale claim. (c) An instant-level physical
criterion that classifies the Kapitza upright state correctly *and* is not
reconstructible from parameters + one period of the flow would break
§3.2's reconstruction point.

**Scope.** Point-mechanical Newtonian systems only, one of them with
engineered delay. Field-theoretic retarded coupling (where particle data
alone is not sufficient even with instantaneous-looking laws) is the
natural next domain and is not tested here. No relativistic, quantum, or
cosmological claim is made, and no universe-stage conclusion is drawn in
either direction.

---

## 9. Non-claims (required by the brief)

1. Not claimed: that every predictively sufficient Cauchy region is
   constitutive. (§3 shows sufficient regions of both kinds and no
   selection by sufficiency.)
2. Not claimed: that failure of a stage/window criterion proves the whole
   history is the sole ground. (§4's failure verdict is symmetric: it
   blocks P-based intervals and I-based instants equally; W and E remain
   open, §6.)
3. Not claimed: uniqueness of grounds. Any complete activity cycle
   satisfies U; multiple adequate grounds are allowed throughout.
4. Not claimed: any temporal ontology, any resolution of the
   whole-history-versus-stage question for the universe, or any novelty.
   Brading owns the contrast; Savitt owns the objections; this test's
   product is the precise location of the missing premise P and the
   demonstration that the Newtonian bound system is adequate to pose but
   not to settle it.

---

## 10. Checks

`python3 check_constitutive_extent.py` — measured total 0.26 s wall
(budget: hard ≤ 15 s/check, actual ≤ 10 s, total ≤ 30 s; the largest
single check is C1 at 0.11 s). Outputs are illustrations of the labeled
analytic claims only; no grid, sweep, or simulation is offered as proof:

- **C1 Kepler**: E = −1/2 conserved (|ΔE| ≈ 1.6e−14) and |ΔL| ≈ 8e−15
  over one period; same-conic from the half-period instant
  (|ΔE| ≈ 6.0e−13); W(t,t) = 0 with instantaneous power 0.166 at t = 0.7T;
  gross exchange 2.667 per period; net work 0 over the closed orbit —
  all computed from the single periapsis state (reconstruction point).
- **C2 Kapitza**: stable case a = 0.2 (a²ω² = 16 > 2): |Tr M| = 1.308 < 2
  while the instantaneous stiffness is destabilizing on 50.4% of the
  cycle; unstable case a = 0.02 (a²ω² = 0.16 < 2): |Tr M| = 2.092 > 2.
- **C3 delay**: two histories agreeing at (0, 0) diverge (sup 0.0059);
  α: Re λ = +0.2165, growth; β: Re λ = −0.3185, decay
  (max |x| 0.0059 → 0.00008). Same window-necessity, opposite unity.
- **C4**: activity scales 2π (Kepler), 0.314 (Kapitza drive), 0.5 (delay
  latency) — all parameter-fixed.

Reproduce: `cd research/ontology-reconstruction/constitutive-extent &&
python3 check_constitutive_extent.py`.

---

## 11. Limitations and unresolved questions

- The "physical = functional of the solution" notion in §4 is itself a
  premise (the standard one). A defender of P who rejects it is outside
  the dilemma's scope; engaging that move requires the philosophy-of-causes
  literature (Dowe/Salmon) at full-text depth, not done here.
- The delay model idealizes the feedback trap; the trap's stochastic
  (Langevin) and sampled-hold structure is not modeled.
- Brading's Newton scholarship (via DiSalle) is not independently
  re-audited; per `paper/SOURCE_AUDIT.md` her historical claim is used
  programmatically and remains at the recorded audit depth.
- Müller 2019 and Dowe 2000 were read at abstract depth only; both are
  flagged as prior-result threats requiring full-text lanes before any
  development of §5.2 or of a Dowe-style P.
- No Lean or other formal verification was used; every analytic claim
  here is elementary (determinism, Kepler integrals, one perturbation
  computation, method of steps) and is argued inline.
- PhilPapers remained unread (HTTP 403 in prior lanes; not retried);
  post-2021 formalizations of the sustaining-region idea were searched
  for (exa + scholar_search) and none was found within those venues.

## 12. Proposed next tasks

1. **Dowe-process lane** (full text): can conserved-quantity process
   constitution supply P without collapsing into state+law functionals?
   Directly tests §4's only exit.
2. **Retarded-coupling lane**: repeat §3 with Maxwell–Lorentz-style
   delayed field coupling, where particle data alone is insufficient —
   the determination half of the question becomes field-extent-sensitive
   and the constitution half can be re-posed with the boundary case
   internal to the physics rather than engineered.
3. **Müller 2019 full-text audit**: transposition test of
   indeterminism-based co-presentness onto sustaining regions.
4. **Anchoring lane**: formalize §5.2's anchoring gap (extent vs. location
   vs. inventory) as three explicit premises, connecting to the sibling
   census/persistence lanes' machinery.
