# Proposed empirical discriminators for temporal-ontology packages

Status: screened source ledger, 2026-10-19. This is a comparison of specified
physical models and observables. It is not a ranking of temporal ontologies.
Primary-source IDs and read depth are in [sources.jsonl](sources.jsonl). Reused
project records are cited by ID; in particular, `found-brading`,
`frontier-relational-trinity-2019v3`, `frontier-relativistic-trinity-2020v1`,
`frontier-page-wootters-measurements-2023`, and `frontier-smith-ahmadi-interacting-2019`.

## Brading's proposal, read narrowly

Brading (2013, `disc-brading-empirical-2013-full`; prior project abstract record
`found-brading`) retains the premise that special relativity gives a complete
account of spatiotemporal structure. Her move is to revise the epistemic versus
ontological role assigned to that account, disputing that its empirical
structure alone settles the ontology in favor of a block. She draws on a
law-constitutive conception of unity: a dynamical system's present region has
the spatiotemporal extent needed to sustain it, without adding a privileged
global simultaneity slice. The distinct 2015 follow-up
(`disc-brading-locating-present-2015-full`) says empirical refutation would
require resources beyond special relativity.

This is not yet a laboratory proposal. Neither paper supplies a new equation,
coupling, parameter, initial-state preparation, detector observable, numerical
bound, or a map from a measurement outcome to the existence/nonexistence of
past or future entities. The 2013 argument retains SR completeness; the 2015
follow-up separately says empirical refutation would require resources beyond
SR, without specifying a signal. Nor does a system-relative region establish
that only the present exists. Both claims need an explicit bridge from physical
theory to ontology.

## Comparison contract: anchor models and versions

| Anchor model/version | What exists; passage/future | State, dynamics, causal structure, clock | Symmetries, preferred structures, access | Observable and empirical status | Philosophical bridge; equivalence and domain |
|---|---|---|---|---|---|
| Special relativity / standard relativistic field theories (Lorentz-invariant matter; Poincaré symmetry), as used by Brading 2013 | Physical ontology is not fixed by the equations. Passage and the future's ontic status are not model parameters. | Minkowski spacetime and relativistic fields; inertial clocks track proper time along worldlines. | No dynamically selected global simultaneity foliation in the standard formulation; local observers access records in their causal past. | Repeated tests constrain Lorentz-violating departures; see SME cavity and clock comparisons below. | Empirical success of Lorentz-invariant dynamics alone does not entail eternalism. Presentist and eternalist interpretations can share predictions if they supply compatible semantics. Ontological underdetermination here is an interpretive claim, not a theorem that all variants are empirically equivalent. |
| Einstein-aether gravity, as analyzed by Foster & Jacobson 2006; 2026 LAGEOS PPN limit | Metric plus a dynamical unit timelike vector; its physical interpretation may be a preferred local frame. Passage and a unique “now” are not established merely by the vector field. | Metric/vector field with dimensionless couplings; vector affects weak-field gravitational dynamics and PPN parameters, including preferred-frame α1. | Local Lorentz symmetry is broken by a real coupled timelike field; CMB frame is used as a candidate asymptotic orientation in the 2026 orbital analysis. Observers access satellite range/orbit data. | The 2026 PRL reports estimates α1=(+2±3)×10^-5 (GEODYN II) and (+1±2)×10^-5 (SATAN), with the quoted ± statistical 1σ; total systematic RSS is 7.7×10^-6. Results are compatible with zero. The PRD abstract summarizes a scale of ~2×10^-5; neither is quoted here as a 95% CL bound. | A positive signal with predicted modulation could favor a coupled preferred-frame gravity package over GR; the reported result is consistent with null. It does not select presentism over eternalism. A bare, uncoupled hidden foliation is not this theory and is not tested by α1. |
| Minimal and nonminimal Standard-Model Extension clock-comparison models; Kostelecký & Vargas 2018 | Fields and ontology remain open; SME coefficients encode specified Lorentz/CPT-violating dynamics, not passage. | Perturbative coefficient insertions shift atomic transition frequencies; clocks/comagnetometers measure transitions. | Coefficients are conventionally reported in a Sun-centered inertial frame; Earth rotation/boost creates sidereal/annual signatures. Laboratory access is to selected coefficient combinations. | Existing fountain clocks, comagnetometers, trapped ions/lattice clocks and antihydrogen spectroscopy are mapped to bounds/sensitivities through stated independent-electron and Schmidt nuclear models. This directly favors allowed/disallowed physical coefficient regions, not ontology labels. | Detection can favor a Lorentz-violating package relative to Lorentz-invariant dynamics. No generic limit on “preferred time” follows: coefficients are sector-specific and correlated, while an uncoupled metaphysical foliation has no signal. |
| Page–Wootters stationary-clock construction; Moreva et al. 2017 experiment; compare relational-trinity model `frontier-relational-trinity-2019v3` | Page–Wootters describes clock-conditioned subsystem change within a globally stationary state. The mathematical split does not choose whether time is fundamental or emergent, nor whether past/future exist. | Constrained/stationary joint state decomposed into clock C and system S; conditional states recover relational evolution. Moreva uses photon position as clock and polarization/measurement correlations for the system. | Clock choice and conditioning matter; the 2019 trinity's equivalence among Dirac, Page–Wootters, and relational-Heisenberg descriptions requires its specified uncoupled constraint and covariant POVM conditions. | Two-time correlations and internal-view Leggett–Garg violation are reported for a narrow-band single photon; external description is approximately time-independent over the experiment. This tests operational correlations. | Relational and external-time accounts are empirically equivalent for the demonstrated predictions, not proven equivalent as complete theories. Experiment does not establish a timeless universe or emergent-time ontology. The full quantum-clock trinity is proved only for stated model hypotheses, not all interacting clocks. |
| Barontini cold-atom entropic-time analog, arXiv:2509.07745v2 / PRR 8 L022047 (2026) | Closed-system analog with a bright observed and dark unobserved sector. Its measured internal ordering is not a claim that laboratory time or cosmological time is unreal. | ~24,000 87Rb atoms in a conservative trap and thin barrier; effective bright-sector gain/loss model. Bright-sector coarse-grained Shannon entropy is S=Ns, where s is entropy per particle. Define signed τ=(σ/kB)∫(dS/dφ)|dφ| along selected φ trajectory. | Total mini-universe entropy (bright plus dark) is reported constant within errors, distinct from the bright-sector S used to define τ. Access uses absorption images and inferred N, center-of-mass φ, width Σ and s. | The paper reports τ grows monotonically almost everywhere and has some wiggles where dS and dφ change sign under coarse sampling. Eq. (3) retains the sign of dS/dφ and does not guarantee monotonicity. The Schrödinger-equation fit additionally assumes M(φ)=αφ and selects positive onward-in-time solutions. | It benchmarks one analog construction and an entropy-linked arrow. It does not distinguish cosmological ontologies or prove the Wheeler–DeWitt interpretation. Coarse-graining, the chosen φ and entropy clock, and analog transfer remain substantive assumptions. No independent reproduction in this lane. |
| Quantum proper-time clock models: Loriani et al. 2019 interferometer proposal; Sorci et al. 2026 optical-ion proposal | Quantum superposition of path/motion with internal clock degrees; neither proposal fixes the ontology of time or objective passage. | Loriani: closed light-pulse atom interferometer, two paths, proper-time phase and visibility. Sorci: harmonically trapped ion, internal/motional Hamiltonian coupling with relativistic corrections, squeezed motion and Ramsey readout. | Local proper time follows relativistic trajectories; accessible observables are fringe visibility/frequency shifts and clock-motion entanglement. Specific pulse geometry, trapping and control matter. | Loriani derive a special-relativistic time-dilation visibility effect in a geometry insensitive to gravitational redshift; Sorci derive projected quantum Doppler shifts/visibility effects within state-of-the-art reach. Proposed signals, not evidence for new ontological physics; no new experiment reported by these papers. | A measured deviation from the classical-proper-time effective model could select a quantum clock-dynamics package. It would not alone establish that time itself is in superposition, that passage is objective, or that the block picture is false. Standard and quantum-relativistic models can share predictions outside the signal-sensitive regime. |

## Proposal-by-proposal discriminator screen

| Proposal/source | Observable, preparation/readout, and dynamics | Model/version and current status | Ontological reach / equivalence verdict |
|---|---|---|---|
| Brading's empirical presentism (`disc-brading-empirical-2013-full`; `disc-brading-locating-present-2015-full`) | No specified measurable quantity, preparation, or readout. The 2013 argument retains SR completeness while revising its epistemic/ontological interpretation; the 2015 follow-up says refutation would require resources beyond SR but supplies no coupling or predicted response. | Philosophical model sketch; no numeric bound or concrete test. | No discriminator yet. Empirical equivalence with eternalism is neither proved nor falsified by this proposal because the physical model and bridge rule are underspecified. The 2013 move is not rejection of SR completeness, and the 2015 beyond-SR remark does not provide positive evidence for an ontology. |
| Preferred-frame gravity / Einstein-aether (`disc-foster-jacobson-einstein-aether-2006`; abstract record `disc-lageos-alpha1-2026`; full review `disc-lageos-prl-constraint-2026`) | Fit annual perturbations in LAGEOS/LAGEOS II mean argument of latitude, with a CMB-aligned frame, to the preferred-frame PPN α1 signature; satellite laser ranging supplies long-baseline orbital data. | Einstein-aether is a named coupled model family. 2026 PRL reports +2±3×10^-5 (GEODYN II) and +1±2×10^-5 (SATAN), statistical 1σ; systematic RSS is 7.7×10^-6. The estimates are compatible with zero, not a stated confidence-level upper bound. | Real discriminatory power for the specified gravity package and parameter region. A signal could favor it over GR's α1=0 prediction. It cannot discriminate a covariant theory plus an inaccessible, causally idle foliation; those are only empirically equivalent by explicit dynamical stipulation. Not an ontological proof. |
| Optical Michelson–Morley / SME cavity tests (`disc-herrmann-cavity-2007`; see `disc-mewes-clockcompare-sme-2018` for coefficient framework) | Rotate orthogonal optical Fabry–Perot and microwave whispering-gallery resonators; compare resonant frequencies/orientation over >1 year. Readout is orientation/time modulation. | Müller et al., PRL 99, 050401 (2007), obtain simultaneous SME limits on 5 electron and 8 photon coefficients down to 10^-16. These are coefficient-specific; the paper assumes a particular simultaneous sector fit, not a single bound on all Lorentz violation. | Can constrain/favor physical anisotropic electrodynamics versus the tested Lorentz-invariant baseline. It does not measure preferred simultaneity or ontology. If a preferred foliation changes propagation, it is in scope only through a specified coefficient; if all observables stay invariant, the instrument has no discriminator. |
| Clock-comparison SME searches (`disc-mewes-clockcompare-sme-2018`) | Prepare clock transitions or nuclear spin states; measure frequency differences and sidereal/annual harmonics as Earth rotates/orbits. Actual extraction uses atomic/nuclear matrix elements and Sun-centered transformations. | Full SME operator analysis up to dimensions d≤8 in cited paper. It converts prior data to bounds, but exact present-day coefficient table values are not repeated here because some are linear combinations and future datasets may supersede them. | Strong discriminator among physical matter-sector packages and parameter values; no direct access to global passage. Nulls don't prove Lorentz symmetry exactly and do not rule out a hidden foliation with no matter coupling. |
| Page–Wootters photon clock (`disc-moreva-pagewootters-2017v1`; predecessor `frontier-relational-trinity-2019v3`) | Prepare a narrow-band single photon with position as clock; measure position-conditioned system correlations, including a Leggett–Garg observable; compare internal conditional and global stationary representations. | Experimental demonstration reported (2017). Operational outcomes are calculated by the same joint quantum state under distinct clock-conditioned/unconditioned descriptions; exact apparatus details and raw data not audited here. | Supports the feasibility of internal clock correlations. It does not empirically favor “fundamental” over “emergent” time if both accounts reproduce the same state and POVMs. Equivalence is demonstrated for those observables, not a global ontological equivalence theorem. |
| Cold-atom internal/entropic time (`disc-barontini-entropic-time-2026v2`) | Isolate condensate; partition with optical barrier; image every 2 ms over 120 ms; infer bright-sector N, φ, width Σ and per-particle coarse-grained Shannon entropy s; set S=Ns and compute signed τ=(σ/kB)∫(dS/dφ)|dφ|; compare φ(τ), Σ(τ) and effective Schrödinger fit. | Published 2026 analog with model-specific mean-field reduction and chosen entropy/clock. No bound; the reported claim is ordering almost everywhere and selected-model data reproduction. | The observed package favors the practical usefulness of this internal coordinate for the prepared sample. The signed formula does not guarantee monotonicity; the paper reports wiggles where dS and dφ change sign. The total mini-universe entropy is separately reported constant within errors. It does not distinguish temporal ontologies or establish the entropy arrow as fundamental; coarse-graining and analog correspondence remain assumptions. |
| Quantum twin-paradox interferometer (`disc-loriani-clock-interferometry-2019`) | Split one clock atom onto two paths with a specified light-pulse sequence; proper-time phase makes internal clock states distinguish paths and reduces output fringe visibility. The analyzed geometry couples to kinematic time dilation and cancels sensitivity to gravitational time dilation. | Proposed geometry and calculation, not claimed experimental realization. Weak-field proper-time expansion and closed phase-space interferometer conditions are stated. | A successful signal would test relativistic clock/path coupling and rule against a purely classical point-clock approximation in that regime. It does not select passage/ontology; conventional relativistic quantum theory can make the same prediction. |
| Squeezed trapped-ion proper-time signatures (`disc-sorci-proper-time-ionclock-2026`) | Squeeze ion motion, apply Ramsey sequence, read clock population/phase and motion-clock correlations; predicted signatures include visibility loss and squeezing/quantum second-order Doppler frequency shifts. | Published proposal, PRL 136, 163602 (2026). Authors say state-of-the-art clocks can reach the regime; no detection yet. | Candidate discriminator between classical-proper-time effective dynamics and a quantum relativistic clock Hamiltonian. It would not distinguish eternalist from presentist/growing-block semantics without a further rule that links one ontology to the Hamiltonian or outcomes. |

## What tests can favor, and what they cannot yet label

The useful counterexample to a blanket “physics constrains only packages, never
prefers one” slogan is Lorentz-violating dynamics. A sufficiently precise
sidereal/orbital/frequency anomaly can prefer a named SME or preferred-frame
gravity model over a Lorentz-invariant baseline, and a null can constrain regions
of that model's parameter space. These are genuine package-level empirical
discriminators. The 2026 α1 central estimates are consistent with zero and have
reported statistical and systematic uncertainties; they are not a detection or
a quoted confidence-level upper bound. The 2007 cavity result is also a null
constraint; neither constitutes positive evidence for a preferred frame.

Now distinguish two often-conflated models. A coupled foliation/vector field
can change orbital, spectral, or propagation observables and is testable. A
hidden foliation appended to otherwise unchanged Lorentz-covariant equations,
with no accessible coupling or record, has no observable discriminator in the
stated domain. That is an empirically equivalent *stipulation for those
observables*, not a general proof that every preferred-foliation theory is
equivalent to special relativity or GR. If a foliation selects a different
state/update law, boundary condition, or measurable event set, equivalence must
be checked again model by model.

Likewise, a quantum or relational clock can outperform or disagree with a
classical-clock approximation under a specified interaction, resolution and
readout. Those outcomes select clock dynamics. A mapping from clock-dynamics
results to eternalism, presentism, growing block, objective passage, or a moving
spotlight requires an additional philosophical bridge premise and may remain
many-to-one. Determinism, causal order, clock time, and thermodynamic arrow are
not substitutes for that bridge.

## Nearest predecessors and falsifiers of possible gaps

- Brading's own 2013 and 2015 papers already provide a law-constitutive,
  relativistic present proposal. The 2013 paper retains SR completeness while
  revising its ontological import; only the 2015 abstract says empirical
  refutation would need resources beyond SR. Malament/Stein and the project sources
  `found-brading`, `found-malament`, and `found-wuthrich-callender` are nearby
  constraints. Any claim that no empirical presentism has been proposed is
  defeated by these sources. A proposed extension would need a physical model,
  invariant observable and an outcome that cannot be absorbed into established
  relativistic dynamics.
- Lorentz tests and coefficient mappings have extensive predecessor literatures:
  SME matter/photon tests, PPN preferred-frame tests, clock-comparison data and
  Einstein-aether parameter studies. Any “first empirical test of preferred
  time” claim is defeated by these unless it identifies a new observable that
  separates a named model from the established parameter bounds.
- Page–Wootters experimental demonstrations and the relational trinity already
  cover clock-conditioned change and equivalences between relational
  descriptions under specified assumptions. The trinity includes broad
  non-ideal clock POVMs but assumes uncoupled clock/system dynamics; the
  relativistic extension adds frequency sectors. Smith–Ahmadi (frontier ID)
  treats interactions and memory kernels. Any new clock claim needs to exceed
  those hypotheses and specify finite resolution, interaction, observer access,
  and a falsifying probability distribution.
- Quantum proper-time interferometry is an active model-testing line. Loriani
  et al. and Sorci et al. already propose visibility/frequency signatures.
  Any claim that proper-time superposition has no testable physical
  consequences is too strong; any claim that it settles temporal ontology is
  also too strong.

No absence of a hit in this bounded screen establishes novelty or
untestability. A stronger audit should inspect full experimental systematics
and coefficient covariance, trace the Einstein-aether/Lorentz-violating bounds
through current data tables, reanalyze the Barontini dataset independently,
and compare all candidate clock observables against explicit rival models.
