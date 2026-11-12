# RESULT — Cycle time versus recovery time as candidate constitutive extents

Lane: `ontology-cycle-recovery-test`. Date: 2026-10-31. Branch
`agent/ontology-cycle-recovery-test`. Submission for independent review; not an
accepted completion, not a novelty claim, and not a temporal-ontology verdict.

**Task** (coordinator/NEXT_FRONTIER_TASKS.md §2, brief): use the Stuart–Landau
normal form z′=(μ+iω)z−β|z|²z, μ,β>0, ω≠0, as an explicit *effective open-system*
model; state a unity criterion independently of which interval should be
concrete; derive amplitude, cycle period, transverse recovery rate and phase
neutrality analytically (no grids); decide whether cycle activity or
restoration activity earns a constitutive role; state strong same-physics
process and instant/event-realist rivals with exact falsifiers.

## 1. Strongest counterexample first

The two candidate constitutive extents fail in opposite directions, and the
failures are exact:

- **Restoration has no sharp intrinsic duration.** With E=|z|², the amplitude
  obeys the logistic law Ẋ=2μE−2βE² exactly, so the recovery duration to an
  amplitude tolerance is t_ε = (1/2μ)·ln[c(E*−ε_E)/ε_E] with c=E*/E₀−1 and
  E*=μ/β. This is strictly increasing in the kick size and strictly decreasing
  in the tolerance (verified exactly); two admissible protocols give recovery
  durations of arbitrarily large ratio. What is intrinsic is the **rate** 2μ,
  not any duration. If a tolerance protocol is stipulated (e.g. a noise floor
  σ: t_rec = ln(r*/σ)/(2μ)), the extent depends on an **environmental**
  parameter, not on the system alone.
- **Cycle activity is not necessary for the unity.** The ω=0 member of the same
  normal-form family has a continuum of stable equilibria {r*e^{iθ}} with the
  *same* transverse eigenvalue −2μ and the *same* nonzero dissipative
  throughput 2μ²/β, but no cycle and no clock (family contrast: different
  parameter value = different system, as in the κ-comparison precedent). Any
  criterion under which the system is one self-maintaining unity at ω≠0 is
  satisfied by that sibling; hence no such criterion can yield "the unity's
  present is its cycle period" as a consequence of unity alone.

Consequently, **neither duration is, by the effective dynamics alone, the
extent of a concrete present.** What the analysis does establish is a
structured internal comparison (§6) and the exact bridge premise any
constitutive-extent proposal is missing (§7). Per the coordinator's standing
caution, this is not an impossibility result: multiple intrinsic durations do
not by themselves defeat a constitutive selector, and instantaneous
reconstructibility of the trajectory from (z, law) does not defeat a
region-based criterion (the W(I) counterexample in
CONSTITUTIVE_SUBMISSION_REVIEW.md §1 already shows determination does not
transfer to qualification).

## 2. Effective model, protocol, normalization, scope

**Effective model.** z′=(μ+iω)z−β|z|²z on ℂ, μ,β>0, ω≠0. This is the
second-order truncation of the Hopf normal form: Pietras–Daffertshofer 2019
(printed §4.2, eq. (4.4) with M=2) reduce generic dynamics near a supercritical
Hopf bifurcation to ẇ=αw−β|w|²w, α=u₀+iv₀, β=u₁+iv₁, with u₀(μ)=μ. The model
is valid near the Hopf point (small μ, small amplitude); the discarded
O(|w|⁴) terms are part of its stated scope. It is an **effective open-system**
model: μ parameterizes net gain supplied by an *unmodeled* energy source, β
the nonlinear saturation from *unmodeled* carrier backreaction. It is not a
fundamental relativistic theory and cannot decide universe ontology.

**Physical input/output protocol.** The system is a driven–dissipative device
(e.g. a gain-saturated oscillator mode; Andronov 1929 §1: self-sustaining
oscillations "sustain their oscillations by drawing energy from non-periodic
sources"). Input: continuous power supply (through μ). Outputs: the phase
readout φ=arg z (mod 2π) and the amplitude readout |z|, read by an external
observer with fixed resolution. The protocol is held fixed throughout; varying
it is varying the question, not the physics.

**Clock normalization.** Time t is measured against an external standard
clock, not against ω itself (otherwise T=1 trivially). T=2π/|ω| and 1/(2μ)
inherit that external unit. The scale-free content is the dimensionless ratio
ρ = 2μT = 4πμ/|ω| (cycles completed per amplitude e-folding time), invariant
under both z→az (amplitude rescaling; β→βa², so the operating amplitude r*
itself is convention-relative) and t→bt.

**Dissipative energy supply.** With E=|z|²= x²+y²: Ė = 2μE − 2βE². At the
operating point E*=μ/β the balance 2μE* = 2βE*² holds exactly while both sides
equal 2μ²/β > 0: standing, nonzero throughput. The cycle is maintained by
continuous gain–loss flux, not by conservation (Stuart 1958 abstract states the
hydrodynamic analogue: "the rate of transfer of energy from the (distorted)
mean flow to the disturbance balances precisely the rate of viscous
dissipation").

## 3. Unity criterion, stated before any present extent

Adapted to this effective model, with no mention of present, extent, or
concrete existence:

> **U(S).** A bounded open subsystem with carrier state z is a
> *self-maintaining process unity* iff
> (i) **Operating regime.** S has a nonempty set of stable states maintained
> under continuous nonzero throughput (here 2μE* = 2βE*² = 2μ²/β ≠ 0);
> (ii) **Active restoration.** Deviations of the organization variable (the
> amplitude) are corrected by S's own dynamics at a parameter-fixed rate
> (transverse eigenvalue λ⊥ = −2μ < 0), the correction being implemented by
> the same gain–loss organization that realizes (i);
> (iii) **No temporal presupposition.** The criterion quantifies over states
> and rates only; it does not presuppose which interval, if any, is concrete.

U(S) holds for μ,β>0 and **any** ω, including ω=0. Andronov's "self-sustaining
oscillation" (1929, §2: stable Poincaré limit cycle, amplitude and period
independent of initial conditions) is then exactly U(S) plus ω≠0.

Check against the primary process-unity literature. Montévil–Mossio 2015
require, for closure, entities that (I) causally channel processes and (II)
are conserved through them *at the same time scale* (their Definition 1), with
mutual dependence (their Definition 4); their footnote 14 defines a time scale
as a relaxation exponential t↦exp(−t/τ); their footnote 25 explicitly denies
that a mere "cycle of processes or reactions" (their example: the hydrologic
cycle) is a unity. Two honest consequences: (a) U above is a *minimal*
criterion, weaker than closure; the SL system realizes at most a two-element
organization (gain–loss balance constrains the amplitude; the maintained
operating regime sustains the balance's effectiveness), and whether the SL
*parameters* count as constraints is not licensed by their framework — the
pump and bath are unmodeled. **This submission does not claim the SL
oscillator is a genuine autopoietic unity or that every stable cycle is one.**
(b) Their time-scale concept is exactly the restoration scale: process-unity
theory already distinguishes relaxation scales from activity durations.

## 4. Derivations (analytic; no grids; exact verification in §9)

Write z = r e^{iθ}, E = r². Substituting into the ODE and matching the radial
and angular parts gives

    r′ = r(μ − βr²),      θ′ = ω          (exact, real β>0).

**(a) Amplitude.** Ė = 2μE − 2βE², a logistic law with carrying capacity
E* = μ/β; hence r* = √(μ/β), the supercritical-Hopf amplitude R_c = √(u₀/u₁)
as printed (Pietras–Daffertshofer §4.2). Closed form:
E(t) = E*/(1 + c e^{−2μt}), c = E*/E₀ − 1.

**(b) Cycle period.** θ′=ω exactly ⇒ T = 2π/|ω|, the exact return time of the
standing activity; independent of initial conditions (Andronov 1929 §2).

**(c) Transverse recovery exponent.** Linearizing r′ = r(μ−βr²) at r*:
δr′ = (μ − 3βr*²)δr = −2μ δr. Floquet exponents of the cycle: {0, −2μ}; the
printed statement (Pietras–Daffertshofer §4.4, eqs. (4.22)–(4.23)) is λ₀=0,
λ₁=−2u₁ = −2μ in their notation.

**(d) Phase neutrality.** θ′=ω is amplitude-independent and the radial law is
phase-free: the two modes decouple exactly. Asymptotic phase Θ(z) = arg z:
isochrons are exactly radial rays. For a kick δr₀ (r₀ = r*+δr₀), the clock
reading never shifts. This is the v₁=0 case of the printed general formula
Θ(w) = arg w − (v₁/u₁)·ln(|w|/R_c) (Pietras–Daffertshofer §4.4): with a
complex cubic coefficient the isochrons are logarithmic spirals and an
amplitude kick shifts the asymptotic phase by ≈(v₁/u₁)(δr₀/r*) at first
order. **Exact phase neutrality is thus a scope-limited property of the
real-β truncation mandated here, not a generic fact**; in the generic case the
restoration transient is audible in the clock.

**(e) Recovery duration and its protocol dependence.** |E(t)−E*| ≤ ε_E holds
iff ce^{−2μt} ≤ ε_E/(E*−ε_E), i.e. t_ε = (1/2μ)·ln[c(E*−ε_E)/ε_E]. In
amplitude terms with a standard kick from r₀: c=(r*²−r₀²)/r₀². Monotone in
both arguments (exact, §9); no principled ε follows from the model. With a
noise floor σ and a standard full-amplitude kick: t_rec = ln(r*/σ)/(2μ),
depending on the environment through σ. Note also: at steady state the
restoring *activity* is latent (deviation zero) while the throughput runs;
restoration is actualized only in perturbation-triggered transients, whereas
the throughput is a standing activity.

**(f) Family contrasts (different parameter values = different systems).**
*ω=0 sibling:* continuum of stable equilibria {r*e^{iθ}}, Jacobian at
(r*,0) = diag(−2μ, 0); same throughput, same recovery rate, no cycle, no
clock. *Pump cut (μ→0 member):* Ė = −2βE², algebraic decay with
state-dependent halving time 1/(2βE₀), while θ′=ω continues: **the clock
ticks while the system dies** — restoration, not rotation, is what keeps the
unity alive. *β→0:* Ė=2μE unbounded — the model leaves its validity domain;
no operating regime without saturation.

## 5. The two activities and their durations

- **Cycle activity** (tangential, rate ω): the standing operation; carries the
  clock. Its duration T = 2π/|ω| is **sharp, protocol-independent, exact** —
  the only such duration in the model. Scope: phase readout only. The phase is
  the unique asymptotic-memory variable (phase perturbations are neutral,
  exponent 0); the clock output determines ω but **not** μ or β, so two
  systems with the same clock can differ arbitrarily in restoration capacity —
  restoration is invisible to the clock.
- **Restoration/throughput activity** (radial, gain 2μE vs loss 2βE²): the
  standing throughput plus the perturbation-triggered correction. Its
  **rate** 2μ is intrinsic (a parameter); its **duration** is
  protocol-relative. Scope: amplitude readout only; exactly phase-neutral in
  this truncation.

The two activities are exactly decoupled here (gain and loss act radially,
rotation tangentially, no coupling either way). Their durations are
parametrically independent: ρ = 4πμ/|ω| is a free dimensionless parameter.
This is the precise sense in which "a cycle period and a relaxation time can
both be intrinsic and physically meaningful while doing different work"
(coordinator §2) — and also the precise reason the two *durations* cannot both
be "the" constitutive extent without an added selection premise.

## 6. Constitutive comparison: which activity earns a role?

**Internal verdict (positive).** By the necessity asymmetry of §1, the
restoration/throughput organization is what makes the assembly one
self-maintaining system at all: remove saturation (β→0) or gain (μ≤0) in the
family and U(S) fails, while ω→0 preserves U(S). The cycle activity is what
the system *does* (its operation, its clock); the restoration organization is
what the system *is* (its degree of organization). So, **if** the unity is
specified by U, restoration earns the constitutive role and the cycle is
ancillary; **if** the unity is specified as a clock operation, the cycle earns
the role and is the only sharp intrinsic extent, but then the ω=0 witness
shows that self-maintaining unities need not have any such extent, so
"present = cycle period" is not a consequence of unity but of an extra,
clock-essentialist premise. This gives a **non-vacuous internal
discriminator**: two unities of this architecture with the same ω but
different μ share the same cycle-extent under cycle-selection but have
different restoration extents under restoration-selection; the two proposals
are thus separable inside the model family.

**Ontological verdict (precise failure).** Neither activity earns a
*constitutive-extent-of-the-present* role from the effective dynamics. The
exact missing premises are:
- for restoration-selection: an independently justified tolerance protocol
  (why should the noise floor σ, an environmental parameter, fix the extent of
  concrete existence?);
- for cycle-selection: a warrant that the unity is essentially temporal
  (clocklike), which U does not supply and the ω=0 sibling refutes as a
  general bridge;
- for both: the constitution step itself — an argument that the activity
  which sustains the unity constitutes an extent of concrete existence,
  rather than merely determining it. This is the step the coordinator's review
  found missing before (determination ≠ constitution; W(I) shows region
  verdicts can differ while remaining reconstructible), and the SL model adds
  nothing that licenses it.

Per the explanatory-role discipline (coordinator EXPLANATORY_ROLE_TEST.md
§4): the explananda available inside this model — clock robustness under
amplitude kicks (isochron fact), exact recovery to the operating regime,
throughput balance — are all law-level facts equally available to a rival who
denies any privileged extent. No explanandum was found that the
restricted-extent account explains and the unrestricted one cannot.

## 7. Rivals, with exact falsifiers

**R1 (instant/event-realist rival; same physics).** Grants the same carriers,
the same trajectory, the same throughput and rates, and takes all occurrences
as concrete; nothing is "the present" beyond the standpoint. *Status:* R1
survives at effective-model level (§6). *Exact falsifier:* exhibit one
explanandum, recognizable to both parties, whose explanation essentially
requires an extended activity region and cannot be restated at the level of
(instantaneous state + law) without adding independently unmotivated
commitments. Within this model no such explanandum was found; the isochron
fact, for instance, is a property of the vector field, available to both.

**R2 (same-physics process rival: cycle-selection, "the present is one
cycle").** This is Hestevold's temporal atom in dynamical-systems dress (see
§8). *Exact falsifier:* the ω=0 member of the same family satisfies U with no
cycle; additionally ρ=4πμ/|ω| is free, so two systems with the same T can
differ arbitrarily in organizational robustness — T measures the operation,
not the unity. Any repair must add and independently justify the
clock-essentialist premise.

**R3 (same-physics process rival: restoration-selection, "the present is the
recovery duration").** *Exact falsifier:* t_ε = ln[c(E*−ε_E)/ε_E]/(2μ) is
strictly monotone in both protocol parameters (exact §9); two admissible
protocols yield durations of unbounded ratio, so no unique extent exists
without a stipulated tolerance; and any stipulated tolerance (e.g. σ) makes
the extent environment-relative. A repair must show that one specific
protocol is itself constitutive, not conventional.

## 8. Strongest contrary evidence

1. **Thick presentism (the direct philosophical attack).** The cycle-present
   proposal is already occupied: Hestevold's "limited time-free thick
   presentism" fixes the present's length as a "temporal atom … e.g. a
   butterfly flapping its wings exactly twice" (quoted in Backmann 2025,
   p. 105, from Hestevold 2008, p. 334) — a characteristic-activity duration,
   i.e. precisely a cycle duration. Backmann 2025 (read in full) argues that
   all four thick-presentist views fail: without internal times, intra-present
   change and order are mysterious (McKinnon 2003; Orilia 2012); with real
   times, either compresentness is transitive (present-explosion) or a
   hyper-progression is needed; without overlap, change stutters between
   presents. A cycle-present proposal inherits every horn: intra-cycle times
   ARE ordered (θ is strictly monotone), and consecutive cycle-presents
   overlap (the carrier state passes continuously). The SL analysis sharpens
   but does not answer this dilemma; it is recorded as the strongest
   contrary evidence, not resolved here.
2. **Determination ≠ constitution (project-internal precedent).** The
   coordinator's W(I) harmonic-oscillator counterexample
   (CONSTITUTIVE_SUBMISSION_REVIEW.md §1) already defeats the inference from
   "state+law determine the verdict" to "the instant qualifies"; symmetrically,
   it defeats the mirror inference that a process interval thereby wins. This
   lane's rivals are structured to respect that lesson.
3. **Cycles are not unities (primary process theory).** Montévil–Mossio 2015,
   footnote 25: a closure of constraints must be distinguished from "a cycle
   of processes or reactions such as … the hydrologic cycle", whose entities
   do not act as constraints on each other. This grounds the brief's warning
   that no claim is made here that every stable cycle is a genuine unity.
4. **All the mathematics is printed.** Every quantitative result in §4 —
   R_c=√(u₀/u₁), T=2π/ω, transverse exponent −2u₀, phase map
   Θ = arg w − (v₁/u₁)ln(|w|/R_c), Floquet exponents {0,−2u₁} — is in
   Pietras–Daffertshofer 2019 §4.2/§4.4, and the underlying normal form is
   textbook (their §4.2 derives it via Kuramoto's reductive perturbation,
   Poincaré transforms, and Takens normal form; Andronov 1929 is the
   self-oscillation precedent; Stuart 1960 the amplitude-equation precedent).
   No mathematical novelty is claimed anywhere in this submission.

## 9. Verification commands and results

- `python3 /private/tmp/opencode/cycle-recovery/verify.py` — exact rational
  (Fraction) identity checks of every algebraic claim in §4: logistic closed
  form; steady-state balance with nonzero throughput 2μ²/β; transverse
  eigenvalue −2μ; recovery-time inversion to tolerance; protocol dependence
  (monotonicity in kick size up, tolerance down); polar flow decomposition of
  the ODE; phase-rate independence of r and phase-free radial law; ω=0
  sibling Jacobian {−2μ, 0}; pump-cut halving time 1/(2βE₀) state-dependent
  with clock still running; scale-free invariant ρ=4πμ/|ω|.
  **All 10 checks PASS; elapsed 0.000 s** — exact arithmetic, no grids, no
  search; within the computation budget (hard ≤15 s, actual ≈0 s, total
  well under 30 s). Two earlier script drafts had coding errors in the test
  assertions (wrong dE/ds factor; inverted inversion; misdirected
  inequalities); the analysis was unchanged, the test code was corrected, and
  the final run passes as stated.

## 10. Prior-work verdict (novelty audit)

- **Mathematics:** printed (Pietras–Daffertshofer §4.2, §4.4; standard Hopf
  normal-form theory; Andronov 1929; Stuart 1958/1960 abstracts). Classify
  everything in §4 as elementary consequences of printed results.
- **Philosophical linkage:** occupied on all nearby fronts — Brading's
  law-constitutive present (project full-text record `found-brading`;
  pp. 1103–1105; inherited, not re-read this lane), Hestevold's
  activity-duration temporal atom, Baron 2012, Backmann 2025's negative
  survey, Montévil–Mossio's closure framework with its explicit cycle
  disclaimer and its relaxation-time-scale concept. Within the stated search
  limits (§AGENT_REPORT), **no printed predecessor was found for the specific
  internal comparison assembled here** — exact decoupling of the two
  activities with disjoint readouts, the necessity asymmetry, the
  intrinsicness asymmetry (rate intrinsic / duration protocol-relative vs
  period sharp), and the ρ-discriminator — but each ingredient is elementary
  and the comparison is a juxtaposition, not a theorem. No novelty claim is
  made; only the coordinator can adjudicate whether the juxtaposition earns
  integration.

## 11. Limitations

- Effective-model scope: results hold for the real-β Stuart–Landau
  truncation near a supercritical Hopf bifurcation. Generic Hopf normal forms
  (complex β) couple the modes (spiral isochrons; printed formula cited);
  higher-order terms are discarded. Nothing here transfers to cosmology or
  decides universe ontology.
- `web-search-prime` quota-exhausted (recorded in AGENT_REPORT); discovery
  relied on scholar_search + exa within small batches. "No printed
  predecessor found" means exactly that, within those limits.
- Landau (1944), Hopf (1942), Kuznetsov, Haken, Guckenheimer (1975),
  Hestevold (2008), Baron (2012), Pikovsky–Rosenblum–Kurths ch. 2 were located
  but not read beyond abstract/discovery level (details and limits in
  sources.jsonl); their roles here are attribution and provenance, not
  load-bearing content.
- The unity criterion U is a minimal, model-relative reconstruction; genuine
  process-unity status (Montévil–Mossio closure) was deliberately *not*
  claimed for the SL system.

## 12. Proposed next tasks

1. **Coordinator test of the discriminator:** two SL systems with identical ω,
   different μ — check whether any candidate unity criterion preserves the
   cycle-extent equality while tracking the restoration difference; if none
   does, restoration-selection is the only internally coherent process
   proposal, at protocol-relative extent.
2. **Protocol task:** what could make a tolerance (noise floor σ) physically
   constitutive rather than conventional? This is the exact missing premise
   for any sharp restoration-extent; connect to the coordinator's
   tolerance-dependent extents (RESPONSE_MEMORY_BENCHMARK §4).
3. **Thick-presentism bridge:** state whether a cycle-present proposal can
   answer Backmann's ordering/overlap dilemma by taking intra-cycle phase
   order (θ monotone) as internal times; if it cannot, record thick presentism
   as a standing counter to every cycle-duration constitution proposal.
4. **Generic-cubic correction (small, bounded):** compute the first-order
   phase shift (v₁/u₁)(δr₀/r*) from the printed isochron formula and ask
   whether the clock/restoration decoupling, and with it §6's internal
   verdict, survives weak coupling between the modes.
