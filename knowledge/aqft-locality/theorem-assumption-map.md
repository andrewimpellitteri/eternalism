# AQFT locality and time: theorem-assumption map

Status: bounded primary-source audit, 2026-10-19. Full-text means inspected at the cited statement/section locators, not independently reproved. The original Reeh–Schlieder paper and Takesaki monograph were not fully read; their records stay discovery-level. No theorem below concludes a temporal ontology.

## The basic net constraints

For a specified spacetime model, a Haag–Kastler net assigns an algebra of observables `A(O)` to each admissible region `O`. Isotony (`O1 ⊂ O2` implies `A(O1) ⊂ A(O2)`) makes localization monotone. Einstein causality/microcausality (`O1` spacelike to `O2` implies the algebras commute) constrains possible interventions and correlations. Covariance relates algebras under the represented spacetime symmetries. These are structural conditions on observables and their relations. They do not assert that only one time slice exists, that a present advances, or that the whole future is fixed. Haag–Kastler (1964) is the primary framework source; their paper is not treated here as a modern exhaustive axiom list.

`A(O)` is a localization assignment, not a statement that every vector obtainable from the vacuum by an operator in `A(O)` is a state physically preparable by an agent confined to `O`. This distinction is forced into view by Reeh–Schlieder and by the separate operational analysis in Fewster–Rejzner.

## Selected statement audits

### Reeh–Schlieder: cyclicity is not a signaling theorem

**Statement audited in later full-text exposition:** Fewster–Rejzner (2020), Sec. 5.2, Theorem 26. In the stated Poincaré-covariant vacuum net, with positive-energy spectrum condition, invariant vacuum cyclic for the global algebra, weak additivity, and a region containing a smaller open region whose sufficiently small translates remain inside, the vacuum is cyclic for the local algebra. With Einstein causality and a nonempty open causal complement it is separating as well. The original 1961 source is discovery-level in this pass; do not retroactively assign every later exposition hypothesis to the original statement.

**Meaning:** cyclicity says `{A Ω : A ∈ A(O)}` is dense in the representation Hilbert space. It is a mathematical approximation statement. It does not bound operator norm, energy, duration, apparatus complexity, success probability, or resource cost. Nor does it say that those vectors arise from selective operations implementable by a localized observer while leaving spacelike observables unchanged. If `A` is a local unitary and microcausality holds, its adjoint action leaves every observable in a spacelike separated algebra unchanged; state-vector approximation cannot erase that no-signaling constraint. Separation says `A Ω = 0` for `A ∈ A(O)` implies `A=0`, under the stated assumptions; it is not a statement of omniscient access.

### Tomita–Takesaki and Bisognano–Wichmann: modular parameter is not generic clock time

**Mathematical input:** for a von Neumann algebra `M` and a cyclic and separating vector `Ω`, the closure of `S0(AΩ)=A*Ω` has polar decomposition `S=J Δ^(1/2)`. Tomita–Takesaki gives `J M J = M'` and `Δ^(it) M Δ^(-it)=M`. Bisognano–Wichmann (1975), pp. 998–999, states this algebraic result and identifies its special wedge realization using the preceding field assumptions.

**Physical specialization:** for a wedge algebra in the vacuum representation, the modular automorphism group is the boost subgroup preserving that wedge (with a conventional `2π` rescaling); the modular conjugation has the corresponding reflection/TCP action. The 1975 paper works with a Hermitian scalar Wightman field, a separable Hilbert space, strongly continuous Poincaré representation, forward-cone spectrum, and unique translation-invariant vacuum. To pass from field operators to wedge von Neumann algebras, further domain, generation/density, and algebra-existence conditions enter. The authors explicitly say the algebras need not be guaranteed by their minimal assumptions (pp. 986, 1002). This is not a blanket theorem for every net, every state, or every region.

The modular automorphism parameter is intrinsic to the chosen algebra-state pair; the BW theorem identifies it with a geometrical boost parameter in this special vacuum-wedge setting. A boost parameter is not the proper time of an arbitrary observer. The theorem says nothing about objective passage, whether the future is fixed, or the existence of one global now. The KMS/modular relation also must not be conflated with a thermodynamic arrow or the experience of becoming.

### Fewster–Verch natural-state no-go: conditional and state-selection-specific

**Theorem audited:** Fewster–Verch (2012), Theorem 6.13. Let `A` be dynamically local in their category `Loc` and suppose it has a natural state assignment compatible with every spacetime morphism. If there is a spacetime with noncompact Cauchy surfaces on which the state induces a faithful GNS representation and the GNS vector is Reeh–Schlieder cyclic for every relatively compact region, relative Cauchy evolution in that spacetime is trivial. If, in addition, extended locality holds, the theory is equivalent to the trivial theory. The proof uses a region spacelike to the metric perturbation, naturality to leave the state invariant under relative Cauchy evolution, Reeh–Schlieder cyclicity to make the implementing unitary identity on a dense set, and faithfulness to infer triviality on the algebra (Sec. 6.3, theorem and proof).

This is a model-independent conditional constraint on a covariant preferred-state assignment across all spacetimes. It does not rule out ordinary states on one spacetime, local records, observer-relative state assignment, or objective becoming. Nor is it a theorem that all local state assignments are impossible: dynamical locality, naturality, faithfulness, the cyclicity property, noncompact Cauchy surface, and (for the final triviality step) extended locality matter.

### Fewster–Verch scalar example: locality notions can diverge

**Theorem audited:** Fewster–Verch (2012), Theorem 4.3. For their massless minimally coupled scalar theory modulo locally constant solutions, dynamical locality holds in connected `Loc_0` for all `n ≥ 2`; in `Loc` (allowing disconnected spacetimes) it holds for `n ≥ 3` and fails for `n=2`. Their construction identifies a topological obstruction in the disconnected two-dimensional case and the authors conjecture that adding topological charge as background may resolve it. The failure example is explicit (Sec. 4, lines 406-422 in v2 HTML). The massive minimally coupled scalar result is also reported in the abstract of this paper: dynamically local in all dimensions `n ≥ 2` for the specified model.

The lesson is not that locality is arbitrary, but that an equality between kinematic localization and dynamical insensitivity is an additional condition, can be model-dependent, and has domain limits. The authors' topological-charge explanation is their conjecture, not the theorem conclusion.

## What the surveyed results constrain

| Claim under discussion | AQFT constraint | What remains open/underdetermined |
|---|---|---|
| A local event or observable | A net associates an algebra with a region; isotony and microcausality constrain localization and spacelike operations. | Algebra membership alone is not an event-occurrence, presentness, or passage predicate. The bridge from observable to event/record requires interpretation and measurement dynamics. |
| A localized record | Records can be represented by observables/correlations in local algebras and evolved by the theory. Reeh–Schlieder warns that vacuum-generated vectors are not automatically strictly localized preparations. | Whether a record is objective, observer-accessible, persistent, or evidence of becoming is not settled by cyclicity. Need an operational instrument, state class, resource bounds, and record-retention model. |
| Signaling | Spacelike commutativity plus local operations constrains signaling; long-range correlations may still exist. | Correlation is not controllable signaling. No claim here that every interpretive account of no-signaling or measurement is equivalent. |
| Observer access | Algebraic state evaluation gives possible expectation values for chosen observables. State spaces may encode admissibility; local covariance itself does not pick a unique state. | Actual observer access is not represented by the bare net. A restricted-access model must specify instruments, preparation, finite resources, and records. |
| A local present / local becoming | Causal structure and local algebras support covariant, region-indexed physical descriptions without a preferred global foliation. | AQFT locality does not establish a metaphysical local becoming relation. Defining a region/event relation as “present” would need an independent bridge premise and would not by itself prove passage. |
| Modular flow | For a cyclic-separating pair there is a modular automorphism group; for BW wedge-vacuum cases this matches boosts. | No generic identification with clock time, global temporal flow, thermodynamic arrow, or objective passage. |
| Future openness / determinism | These surveyed locality theorems do not determine whether later data are fixed, stochastic, branching, or ontologically actual. | Requires dynamics, state/initial-condition interpretation, and separate bridge premises; causal order is not determinism. |

## Comparison contract: anchor versions

The fuller model-by-model contract is in `comparison-contract.md`. The short diagnosis is that Minkowski vacuum nets, wedge modular theory, and locally covariant curved-spacetime theories are three distinct model/version choices, not interchangeable evidence for one temporal ontology. The reviewed results constrain causal accessibility and the structure of local observables; none independently decides eternalism versus presentism, objective passage, or determinism.
