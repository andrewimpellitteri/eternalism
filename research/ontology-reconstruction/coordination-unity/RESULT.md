# Physical carrier organization as a unity criterion: test result

31 October 2026. Task `ontology-coordination-unity`, isolated worker submission
for independent review. Scope: test one independently defended unity criterion
for the finite causal transport/return apparatus of
[FEEDBACK_CONSTITUTIVE_TEST.md](../coordinator/FEEDBACK_CONSTITUTIVE_TEST.md),
stated before any present extent. No novelty claim, no temporal ontology, no
new mathematics: the closure definitions are quoted from primary sources, the
dependency graph is textbook machinery, and the computed contrasts are
elementary delay-line algebra. Primary process/organizational-closure sources
were read before attribution (see [sources.jsonl](sources.jsonl)).

## 1. Result summary

**The intervention battery succeeds as an operational contrast but fails to
license a constitutive attribution.** Concretely:

1. A criterion of *reciprocal physical signal carriage* (C2 below, §4)
   classifies the five interventions with a nonvacuous contrast: physically
   rerouting the return path and replacing it by an unconnected external
   generator produce **identical outputs** (verified: max impulse-response
   difference 0.00e+00 for both) while receiving **different unity verdicts**.
   Organization, not output value, is what the criterion tracks.
2. The source-faithful organizational-closure criterion (C1 below, §3) is
   independently defended (Montévil–Mossio 2015, Definitions 1–4) but
   **classifies the passive carrier loop as a causal cycle, not a unity**:
   its constraints are externally maintained. This is a precise negative
   result with the first exact missing premise (§3).
3. Upgrading either criterion to a *constitutive* verdict — one that fixes a
   temporal extent of concreteness — requires a second premise that no source
   read here supplies (§6): why the organizing activity's duration, rather
   than the whole input ancestry or any subinterval, should be concrete.
4. The strongest same-physics rival, an event realist who accepts every
   carrier, coupling and intervention outcome, appropriates the successful
   contrast at no cost (§7). No ontological preference is earned.

## 2. Apparatus and permitted interventions

Apparatus (inherited, with the coordinator's full-text antecedent
[Smith III, *Physical Audio Signal Processing*, "Feedback Comb Filters" —
provenance inherited at the coordinator's stated depth
`ontology-coord-smith2010-feedback`]): outgoing transport path (transit τ),
return path (transit σ), externally driven mixing junction imposing
q(t,0)=f(t)+g·z(t−σ), 0≤g<1, outlet z(t)=q(t,L); ℓ=τ+σ and the unique
bounded solution z(t)=Σ_{n≥0} gⁿ f(t−τ−nℓ). Discretized on a unit delay grid
(τ=5, σ=15, ℓ=20 samples, g=0.8 unless stated) the recurrence is exact; all
numbers below come from `check_unity_interventions.py` (runtime 0.001 s,
limits respected).

Interventions follow the third absence-test discipline of
[CONSTITUTION_IS_NOT_PREDICTION.md](../coordinator/CONSTITUTION_IS_NOT_PREDICTION.md)
§8: change a **material constituent, interaction or boundary input** while
preserving the transport law, the junction mixing law and the deeper laws;
never delete complete Cauchy data. Held fixed in every case unless stated:
the transport equation q_t+cq_x=0 on each channel, the junction law with its
gain parameter, and the external drive protocol f→z. What varies is which
material carrier realizes the return influence, or whether anything does.

The unity question is stated **before** any present extent: the criteria
classify which carrier parts form one organized system at the marked
standpoint. Nothing below infers a temporal inventory from a unity verdict.

## 3. Criterion C1: organizational closure (source-faithful) — negative verdict

The independently defended criterion in the nearest process literature is
closure of constraints. Montévil–Mossio 2015 (full-text, HAL copy; Definitions
1–4 at their §§3–5): a configuration C is a **constraint** on a process at
time scale τ iff it makes an observable difference to the process (condition
I) while being conserved in its causally relevant aspects at τ (condition II);
a constraint C₁ **depends** on C₂ when C₂ acts, at another scale, on a
process producing the aspects of C₁ relevant to its constraint role; a set C
realizes **closure** when each member depends directly on another member and
is generative for another member. Mossio–Moreno 2010 (full-text, §3) add the
working definition and three glosses: closure is partial (external boundary
conditions remain), must involve constraints and not merely constrained
processes, and must be direct.

Application to the apparatus:

* At the **signal time scale**, the two channels and the junction satisfy
  Definition 1: each is a material configuration, conserved at that scale,
  exerting causal power over the signal processes (the channels fix
  propagation delays; the junction fixes the mixing law).
* At the **maintenance scale**, no constraint in the set depends on another
  set member. The channels' replacement and repair depend on external agents;
  the junction's power supply is external; the circulating signal sustains no
  member's existence. Definition 4 fails for every member.
* Verdict: **no closure; the loop is a causal cycle of constrained
  processes** — exactly the structure Mossio–Moreno's billiard-ball example
  (their §3) and Montévil–Mossio's footnote 25 (hydrologic cycle) exclude.
  Their distinction does the work the "strongly connected component" cannot:
  graph cyclicality holds at g>0, but organizational unity, by the only
  independently defended criterion read here, does not.

**Exact missing premise (1).** For C1 to count the carrier loop as a unity,
one must add a defended principle that either (i) the loop's circulating
activity regenerates or maintains its own material constraints (carrier
self-maintenance — absent in this apparatus), or (ii) closure may be weakened
for externally maintained artifacts in a way that preserves the criterion's
biological work. Neither (i) nor (ii) exists in the sources read here.
This is the first identified gap; it is a fact about the criterion, not a
refutation of closure theory, whose scope is biological.

## 4. Criterion C2: reciprocal carriage (adapted, defended as a proposal)

Because the brief asks for a criterion the *carrier-loop apparatus* can be
tested against, state the adapted criterion explicitly, with its departure
from the source flagged. Borrowed from the closure literature: the constraint
notion (conservation + causal power at the signal scale) and the requirement
that unity involve *constraints* and not merely processes. Departure: what
must be reciprocal is not replacement/repair dependence at a maintenance
scale but **role-carriage dependence at the signal scale**.

> **C2 (carrier-loop unity at the signal time scale).** Fix the apparatus:
> material channels and junction satisfying the transport and mixing laws.
> The carrier parts {outgoing channel, return channel, junction} form one
> organized loop system at standpoint b iff:
> **(U1) reciprocal carriage:** there is a physically realized connecting
> process — material signal carriage with transmission through each channel
> and mixing at the junction — from outlet to inlet and from inlet through
> the outgoing channel to outlet; each channel's carriage role at b
> counterfactually depends on the other's;
> **(U2) interruption contrast:** physically interrupting either carriage
> (material-constituent change, laws held fixed) eliminates the mutual role
> dependence while each channel's one-way carriage survives;
> **(U3) generator contrast:** substituting the return carriage by an
> unconnected device producing the same numerical values does not restore
> unity.

C2 is not organizational closure and must not be attributed to
Mossio–Moreno or Montévil–Mossio: their billiard example and footnote 25
deny that process circulation alone constitutes organization. Its defense is
(a) the physical-carriage requirement, which excludes value-duplication
without a connecting process, and (b) the intervention contrasts below,
which give it content no mere definition has. Whether (a)+(b) suffice to
make C2 a *unity* criterion rather than a diagnostic is examined in §6.

## 5. The intervention battery

Computed contrasts (impulse protocol f→z, g=0.8; full output in the script
run recorded in AGENT_REPORT.md):

| Configuration | Output vs intact | Physical carriage outlet→inlet | C2 verdict |
|---|---|---|---|
| Intact loop | — | yes (return channel) | one loop system (SCC {IN,OUT,RET}) |
| Interruption (return cut at junction) | max diff 0.80 = first echo | severed | unity lost; both channels keep one-way carriage |
| Attenuation g→0.1 | echo train shrinks | yes, weaker | unity persists, graded |
| Equal-delay rerouting (new carrier, same σ) | max diff 0.00e+00 | yes (new carrier) | unity persists (SCC {IN,OUT,RET2}) |
| External model generator | max diff 0.00e+00 | **no** (unconnected device simulating the recurrence) | **no unity** (all components singleton) |
| Backreaction ε>0 (finite-impedance source) | loop response drives source | yes, plus junction→source | boundary shifts; exact criterion merges source |

**The nonvacuous contrast is the generator row.** Output identity and unity
verdict come apart in both directions: rerouting preserves output *and*
carriage (unity kept); the generator preserves output *without* carriage
(unity lost); interruption destroys both. So the verdicts track physical
organization, not output values, and the criterion is not true by
definition — each verdict is fixed by an independently performable
intervention on a named material constituent.

**Robustness of the scripted equivalence.** After a further material change
(outgoing transit 5→6 samples), the physical loop's response moves to taps
{6, 27, 48, …} while the scripted generator still emits {5, 25, 45, …}
(max divergence 1.0000 at sample 5). Any device that reproduces the loop's
output *robustly under material changes* must be causally coupled to the
apparatus — at which point it is a (rerouted) return channel and C2's
verdict flips back to unity. The criterion therefore cannot be satisfied by
coincidence or bookkeeping, only by carriage. This is the interventionist
content that distinguishes loss of unity from a changed output.

**Disabled measurement, distinguished.** Disabling the outlet detector
removes the readout z but not the carriage structure: C2's verdicts are
fixed by the apparatus's couplings (probeable by separate test-signal
experiments on each channel), not by whether anything measures z at b. Loss
of unity, changed output and disabled measurement are three distinct events
in the table above.

**Approximate unity stays live.** The graded internal-cohesion measure —
echo energy share of the impulse response — equals g² exactly (measured
0.640000, 0.250000, 0.010000 for g=0.8, 0.5, 0.1): unity under C2 degrades
continuously to zero at g=0. No sharp exclusion of weakly coupled loops is
claimed, matching the methodological lesson of
[WEAK_COUPLING_AND_TEMPORAL_EXTENT.md](../coordinator/WEAK_COUPLING_AND_TEMPORAL_EXTENT.md).

**Backreaction and the weak-coupling adversary.** With a physically modeled
source (integrator s[k+1]=(1−α)s[k]+ε·w[k], junction loading), the exact
dependency graph merges the source into the loop's strongly connected set
for **every** ε>0 — the "weak bidirectional couplings merge every module"
adversary, confirmed. The graded measure (steady loop→source gain ε/α =
0.1000 at ε=0.01, 0.0100 at ε=0.001) is continuous. Consequence: C2's exact
verdict is boundary-relative, and the one-way-source idealization is an
approximation whose warrant is a stated coupling hierarchy, not a
metaphysical boundary. This is recorded as a limitation of any sharp
exclusion claim, not resolved here.

**Normal modes and the material boundary.** The two transport channels and
the junction are conserved material configurations individuated by
Definition 1 (conservation + causal power at the signal scale) — not by
diagonalizability of the joint description. A modal re-coordinatization of
the channel network re-describes the same conserved configurations; the
interventions that fix C2's verdicts (cutting, rerouting, substituting
carriers) are physical acts, invariant under re-description, and their
outcomes cannot be manufactured or erased by changing coordinates. The
part/input boundary — which signal enters from outside versus circulates —
is fixed by the junction's mixing law and its impedance bookkeeping, not by
the coordinate form of q. What the modal red-team *does* expose is
pretense: any claim that the criterion's nodes are "whatever separates the
equations" would be coordinate-dependent. C2 as stated avoids that by
naming material configurations, at the cost of owing the §3/§6 boundary
justifications.

## 6. What no criterion read here delivers: the second missing premise

C2 classifies carrier organization at b. It supplies **no temporal extent**:

* The response-support selector is already refuted on this apparatus
  (FEEDBACK_CONSTITUTIVE_TEST.md §3): support is unbounded for every g>0,
  jumps discontinuously at g=0, while calibrated responses converge.
  C2's verdicts are invariant under that jump (attenuation row), so unity
  does not inherit the pathology — and also does not select a duration.
* Sustaining-role heredity: the channels sustain the loop on every
  subinterval containing a circulation, so no minimal extent follows
  (same obstruction as WEAK_COUPLING §5); closure theory itself states
  closure "cannot be described at a given point in time" and is
  multiscale (Montévil–Mossio 2015, §5) — so the closure framework, if
  it applied, would locate unity in a network extended over scales, not
  in one concrete interval.
* Brading's own bridge — the present is "the spatiotemporal region that is
  dynamically necessary to sustain" the system (Brading 2015 §5, printed
  pp. 16–17, direct full-text reading) — leaves the sustaining region
  without a criterion, and for this apparatus hereditary sustaining makes
  every candidate extent non-minimal. Her 2013 account (§4, printed
  pp. 1104–1105, direct full-text reading) constitutes composites by
  law-satisfying interaction, but its paradigm is an instantaneous
  third-law collision; a diachronic signal loop is not covered by anything
  she states, and she leaves genuine subsystem existence as an empirical
  question (2015, printed p. 18).

**Exact missing premise (2).** To move from "the activity organizes the
system" to "the activity's duration is the system's concrete present", one
needs an independently defended principle selecting one circulation (or any
fixed number) as constitutively relevant while excluding older echoes —
which the unbounded echo series and heredity obstruct, and which no source
read here supplies. The closure literature, read directly, would need the
additional move from *organizational* individuation to *temporal inventory*
— El-Hani et al. 2025 individuate living systems functionally and grant
that boundaries are functional, not physical; nothing in their account is
about concrete existence. This premise, not organizational language, is
where a constitutive proposal must do its work.

## 7. The same-physics event-realist rival

The rival grants everything physical in this note: both channels, the
junction, g, all carriage facts, all intervention outcomes, every C1 and C2
verdict, and the graded measures. It adds only an unrestricted inventory:
all occurrence times of the apparatus are concrete. Assessment:

* **Everything C2 achieves, the rival can say.** Individuation, boundary
  fixation, intervention contrasts and the generator exclusion are
  organization-level results about which material configurations form one
  system; none restricts what exists. The rival's appropriation costs
  nothing and loses nothing — there is no prediction, explanation or
  intervention whose success requires the restricted inventory.
* **The process rival's remaining asset is missing premise (2).** Under the
  selection principle of ROLE_OF_EXISTENCE.md §2 — an added fundamental
  distinction needs an independently defended explanatory role — the
  process account currently owes exactly the deficit ROLE_OF_EXISTENCE
  records: no exhibited target (experience, persistence asymmetry,
  actualization) that the restriction explains on this apparatus.
* **Symmetric burden.** The event realist owes an account of why
  organization-grade individuation without inventory restriction explains
  everything the restriction was invoked for; on the evidence here, it does.
  Neither side gains a physical preference from the battery. The honest
  verdict is **equally strong on the same physics**, with the process
  account holding an *unpaid* promissory note (§6), not a defeat.

## 8. Falsifiers and limits

Falsifiers for the submission: (i) a defended published criterion that
already classifies passive feedback artifacts as organizational unities
without carrier self-maintenance (would invalidate §3's negative verdict);
(ii) an intervention on this apparatus whose outcome distinguishes
organization-level from event-realist descriptions (would defeat §7);
(iii) a source-faithful reading showing Montévil–Mossio's dependence
notion applies at the operation time scale, not the maintenance scale
(would collapse the C1/C2 distinction). Known limits: linear toy apparatus;
unity ≠ life and no self-maintenance is claimed; g is a boundary-input
parameter, not complete data of one fixed boundary-value problem (inherited
caveat); the SCC machinery is classification only; depths are as recorded
in sources.jsonl — Brading 2013/2015, Mossio–Moreno 2010, Montévil–Mossio
2015, and El-Hani et al. 2025 at full-text (selected-locator for the
formal definitions), Rider 2024 at discovery only; Smith III's antecedent
section is inherited at the coordinator's recorded depth, not reread here.

## 9. Proposed next tasks

1. **Carrier self-maintenance variant.** Add a physically modeled element
   by which the loop's activity maintains a carrier (e.g., signal-powered
   bias restoring a junction parameter) and re-run C1: does minimal closure
   become instantiable in an artifact? This would test missing premise (1)
   directly.
2. **Formalize C2's departure.** A model-theoretic audit (start from
   Rider 2024, discovery-level lead in sources.jsonl) of whether
   role-carriage dependence can be added to autonomy theory without
   collapsing the biological distinction.
3. **Backreaction ledger.** Extend RESPONSE_MEMORY_BENCHMARK.md-style
   norm bookkeeping to the two-channel loop with finite source impedance,
   making the boundary-relativity of §5 quantitative.
4. **Bridge audit.** A dedicated task on missing premise (2): survey
   whether any source defends "only the organizing activity's duration is
   concrete", per CONSTITUTION_IS_NOT_PREDICTION §9's standing offer.
