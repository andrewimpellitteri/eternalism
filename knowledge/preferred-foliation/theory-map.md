# Preferred foliation and relativistic collapse theories (first-pass map)

Status: screening map, 2026-10-19. Source records in `sources.jsonl` (lane
prefix `fol-`, plus reused IDs from `knowledge/philosophy/`, `knowledge/seed-sources.jsonl`,
and `knowledge/foundations/`). This map records what each model/version posits,
not which is true. Paper claims, established results, and our notes are labeled.
Read depths are stated per source; nothing here rests on a source marked
`discovery` unless explicitly flagged as a lead.

## 0. Vocabulary kept separate (per AGENTS.md)

- **Preferred frame / foliation**: extra spacetime structure: a global family of
  spacelike hypersurfaces or a distinguished inertial frame. A mathematical
  posit of a model, distinct from any coordinate choice.
- **Objective passage**: a mind-independent coming-to-be of events. No theory
  in this map *measures* passage; at most some are *compatible* with it. A
  foliation is not automatically a "moving now" — that identification is a
  bridge premise (and one this map does not make).
- **Determinism**: uniqueness of evolution from a complete initial state. GRW/
  CSL models are indeterministic; Bohmian and Lorentzian electrodynamics are
  deterministic. Both groups can carry a foliation; determinism and preferred
  frame are independent axes.
- **Causal order**: event-relative past/future of the light cones (or, in
  collapse models, a stochastic dependence structure). Not interchangeable
  with ontological status of the future.
- **Clock time**: proper time along worldlines; every theory here keeps the
  standard clock behavior, so nothing in this map differentiates theories via
  clocks.
- **Thermodynamic arrow**: entropy gradient; separate from all of the above
  (see `phil-price-arrow` in the philosophy lane). No foliation theory in this
  map derives its foliation from the entropy gradient — that is a possible
  *extra* hypothesis, listed as such in §8.

## 1. Lorentz-Poincaré (neo-Lorentzian) interpretations

**What it is.** Special relativity's kinematics accepted as a dynamical
theorem about matter moving in a privileged frame (ether frame): rods contract
and clocks desynchronize because of their constitution, not because "space"
is Minkowskian. Originals: Lorentz 1904 (`fol-lorentz-1904`), Poincaré 1906
(`fol-poincare-1906`); modern programmatic defense: Craig & Smith 2008
(`fol-craig-smith-2008`); standard critique: Balashov & Janssen 2003
(`fol-balashov-janssen-2003`); Lorentzian pedagogy: Bell, "How to teach
special relativity" (`fol-bell-2004-speakable`, ch. 9).

| Question | Record |
|---|---|
| What is the foliation | The rest frame of the ether / of the quantum vacuum state; equal-time hyperplanes of that frame. |
| Fixed or dynamical | Fixed background structure; not a dynamical variable in the theory itself. |
| Empirically detectable | No, by construction: predictions are empirically equivalent to Einsteinian SR for all inertial experiments. Only *additional* Lorentz-violating terms would be detectable; those are bounded, not found, by SME-style tests (`phil-sme`, `seed-lorentz-data-2026`). A purely hidden frame is *not* constrained by those tests — the Data Tables constrain observable anisotropies, not unobservable ontology. |
| Simultaneity arguments | **Accepts** the mathematical relativity of simultaneity (coordinate fact). **Blocks** Rietdijk–Putnam (found-rietdijk, found-putnam) by denying the bridge premise that frame-relative "determinate" relations can be chained across frames: there is one fact about which spacelike event is ontologically earlier. **Accepts** Malament-style definability limits (found-malament-1977) as showing the frame is *extra*, non-causal structure — the theory never claimed the frame is causally definable. Stein's event-relative becoming (found-stein-1991) is an alternative it does not need. |
| Passage / determinism | Usually packaged with presentism + objective passage + deterministic Lorentzian electrodynamics, but each package element is optional; the package is a metaphysical add-on, not a consequence of the dynamics. |
| Status of claims | Established: empirical equivalence to SR for the covered experiments (mathematical). Interpretive claims (the frame "really exists") = paper/advocate claims. "Ad hoc/implausible" = Balashov-Janssen's philosophical assessment, unread this pass (discovery) — lead only. |
| Open questions | Whether any *internal* dynamical reason could single out the frame (analogue: DGTZ 2014's wave-function-determined foliation, §3). What a quantum theory written natively in the Lorentzian frame would add (Bell ch. 9 and ch. 19 are the leads; unread). |

## 2. Bohmian mechanics with a preferred foliation

**What it is.** Particle ontology with guiding equation for N>1 relativistic
particles. Baseline: Bohm-Dirac model = equal-time hyperplanes of one
distinguished frame; generalization: hypersurface Bohm-Dirac models
(`phil-bohm-foliation`, reused: PR A 60, 2729–2736 (1999); arXiv:quant-ph/9801070;
DOI 10.1103/PhysRevA.60.2729 — DOI added this pass, verified via Crossref).
Review of beable QFT: `fol-dgtz-2005-belltype-qft`. Central modern analysis:
`fol-dgtz-2014-can-bohmian` (Dürr, Goldstein, Norsen, Struyve, Zanghì 2014,
**full-text read**).

| Question | Record |
|---|---|
| What is the foliation | In HBD: a foliation supplied as "additional dynamical space-time structure" (full-text quote); for the special case of one frame's equal-time hyperplanes it reduces to Bohm-Dirac. N=1 needs none. |
| Fixed or dynamical | The HBD foliation is itself part of the dynamics (can be configuration-dependent); in DGTZ 2014 the *proposed* foliation is determined covariantly by the wave function (their §4-5 construction via integrable vector fields). Both are model choices, not forced. |
| Empirically detectable | No, under quantum equilibrium: the |ψ|² distribution on the leaves makes all statistics Lorentz invariant (established in the equilibrium setting; Sec. 6 of DGTZ 2014 skimmed). Detectable only outside equilibrium — in-principle deviations like GRW's but with no current channel to probe them. |
| Simultaneity arguments | **Accepts** relativity of simultaneity as geometry; **blocks** Rietdijk–Putnam via the foliation ordering of spacelike events (there is a fact of the matter about which collapse/particle event is earlier). **Accepts** Bell-type nonlocality (violates Bell inequalities) while **blocking** the signalling inference through equilibrium statistics. DGTZ 2014 additionally argues (hedged claim, not theorem) that a wave-function-determined foliation preserves "fundamental" Lorentz invariance — i.e., they try to *reframe* rather than accept the "extra structure = anti-relativistic" objection. |
| Passage / determinism | Deterministic particle motion; no passage posited; eternalism-compatible but not entailing (block representation ≠ ontological thesis — same distinction the foundations lane draws). |
| Status of claims | HBD covariance + equilibrium = published results (paper claims, math not reproduced here). "Foliation can be wave-function-determined and remain fundamentally Lorentz invariant" = authors' explicitly hedged argument. "Bohmian mechanics needs a foliation for N>1 interacting particles" = consensus claim in this literature; the *interacting* case is exactly where it bites. |
| Open questions | Dynamical stability of wave-function-determined foliations under interactions; whether any foliation choice is observationally distinguishable from another given equilibrium (expected: no); QFT extension beyond lattice Bell-type models (ch. 19 lead). |

## 3. Relativistic GRW — flash ontology (GRWf)

**What it is.** Tumulka 2006 (`fol-tumulka-2006-grw-flash`, **full-text
read**): stochastic collapse dynamics whose local beables are discrete
spacetime points ("flashes") where collapses are centered; probability law
determined by the initial multi-time wave function; three equivalent
formulations, one of which uses an arbitrary foliation *as a description* —
the model itself needs none.

| Question | Record |
|---|---|
| What is the foliation | None required (full-text: "does not make use of a preferred slicing of space-time or any other sort of synchronization of spacelike separated points"). The theory also does not group flashes into generations — no ordering of spacelike-separated flashes is presupposed. |
| Fixed or dynamical | Not applicable: no foliation is posited. A foliation appears only in one equivalent Markov-process representation, as an arbitrary parameterization. |
| Empirically detectable | In principle yes: like GRW, deviates from unitary QM (spontaneous radiation etc., §7); no experiment has detected it. The *absence* of a foliation means there is no extra frame-effect channel. |
| Simultaneity arguments | **Accepts** full relativity of simultaneity; **blocks** the Rietdijk-Putnam inference differently: objective events (flashes) exist without a global now, giving a model where "objective happening" ≠ "global present" (our reading of the model's ontology; the paper itself makes no ontological passage claim). **Accepts** Bell inequality violation; **blocks** signalling (same statistical structure as GRW; the explicit no-signalling argument lineage is GRW 1980 `fol-grw-1980-nosuperluminal`, discovery). |
| Passage / determinism | Indeterministic (stochastic jumps); no passage claim; the flash set is a completed spacetime structure — nearest existing model to "local becoming without foliation", relevant to Stein (found-stein-1991). |
| Status of claims | Model existence + equivalence of formulations = published construction (read, not reproduced). "Works on curved backgrounds" = author claim for well-behaved backgrounds. **Domain restriction (established): non-interacting spin-1/2 particles; interactions need creation/annihilation and are explicitly out of scope.** |
| Open questions | Interacting GRWf; whether the flash ontology survives the empirical bounds of §7; whether "no foliation" generalizes beyond flash ontologies (§4 suggests not, per Myrvold 2017's scope). |

## 4. Relativistic GRW/CSL with mass-density or field ontology

**What it is.** The mass-density (GRWm) and CSL family where collapse acts on
a continuous density/field. Standard CSL (`fol-gpr-1990-csl`) is
nonrelativistic; its noise correlator is defined in a frame, so the baseline
theory implicitly fixes one. Relativistic continuations:

- **The frame-conflict problem**: Bedingham, Dürr, Ghirardi, Goldstein,
  Tumulka, Zanghì 2014 (`fol-bdg-tgz-2014-matter-density`, abstract read):
  even with a relativistic wave-function law, different Lorentz frames assign
  **conflicting matter densities** at a spacetime point; a frame-independent
  matter-density rule is proposed.
- **Covariant mediating field**: Bedingham 2011
  (`fol-bedingham-2011-relativistic-reduction`, abstract read): adds a
  relativistic field mediating stochastic collapses; equations stated Lorentz
  covariant and frame independent.
- **Black-hole application**: Bedingham, Modak, Sudarsky 2016
  (`fol-bedingham-modak-sudarsky-2016-bh`, discovery — Crossref-verified;
  search-snippet characterization only): covariant collapse dynamics applied
  to black hole information loss, characterized in the snippet as lacking
  foliation dependence.
- **Recent frontier**: Bedingham & Pearle 2025
  (`fol-bedingham-pearle-2025-quantised-time`, abstract read, preprint):
  Poincaré-covariant collapse with quantized per-particle time variables and
  an evolution parameter; and Piccione 2026
  (`fol-piccione-2026-flash-qft`, abstract read, preprint): a flash-based
  relativistic collapse model for QFT using a history-dependent
  Aharonov-Albert update prescription, addressing signalling/foliation
  dependence at the cost of a new, incompletely characterized state space.
- **Structural constraint**: Myrvold 2017
  (`fol-myrvold-2017-nonstandard-dof`, abstract read): relativistically
  invariant Markovian collapse theories **must employ nonstandard degrees of
  freedom**; with only standard fields (forward-light-cone spectrum), a
  stable vacuum plus relativistic causality force deterministic evolution.
  Scope: Markovian, standard-DOF assumptions as stated in the abstract — it
  does not by itself cover flash-type or non-Markovian dynamics.

| Question | Record |
|---|---|
| What is the foliation | Either a chosen frame for the noise (CSL baseline, implicit), or — for genuinely covariant versions — nonstandard DOF replacing/encoding the foliation's role (Myrvold 2017's characterization). |
| Fixed or dynamical | CSL baseline: fixed by fiat (typically the CMB frame in phenomenology). Bedingham-type: replaced by covariant structure; not a dynamical foliation variable. |
| Empirically detectable | Collapse itself: yes in principle (§7 tests bound parameters). The frame: only if collapse dynamics produce frame-dependent observable statistics — none found; hidden-frame choices with Lorentz-invariant statistics are not testable by Lorentz-violation searches. |
| Simultaneity arguments | **Accepts** relativity of simultaneity; **blocks** signalling via the GRW-1980-style statistical argument; the frame-conflict result shows the naive matter-density ontology *fails* to be frame-indifferent — so this family either changes the ontology (mediating field / distributional, per `fol-myr-2019-ontology`) or accepts a foliation. Rietdijk-Putnam: blocked as in §3 for covariant versions; for foliated versions blocked as in §2. |
| Passage / determinism | Indeterministic; no passage claim; future openness of the wave-function evolution is a stochastic-law feature, distinct from any ontological thesis. |
| Status of claims | Frame-conflict observation = published (paper claim with construction). Myrvold 2017 theorem-scope = paper claim, proof unaudited. Bedingham-Pearle 2025 = unrefereed preprint claim. |
| Open questions | Exact parameter space left by §7 tests for GRWm/CSL; whether the frame-independent matter-density rule of BDGTZ 2014 preserves GRWm's empirical equivalence; classification of allowed "nonstandard DOF". |

## 5. Tomonaga-Schwinger formulations

**What it is.** Covariant evolution of a state functional Ψ[σ] on arbitrary
spacelike hypersurfaces (Tomonaga 1946 `fol-tomonaga-1946`; Schwinger 1948
`fol-schwinger-1948`; both discovery — landing pages blocked/unread, metadata
Crossref-verified). Mathematical modernization of hypersurface-consistency:
Lienert & Tumulka 2020 (`fol-lienert-tumulka-2020-born`, abstract read) —
Born rule for arbitrary Cauchy surfaces.

| Question | Record |
|---|---|
| What is the foliation | None in the formulation: Ψ is defined on *any* spacelike hypersurface; TS evolution is the tool, not a frame choice. |
| Fixed or dynamical | n/a. The family matters here because collapse rules *defined via TS* inherit hypersurface-relativity of the state while predictions can remain foliation-independent (Lienert-Tumulka's curved Born rule; Myrvold's program, §6). |
| Empirically detectable | Nothing extra to detect: TS covariance is standard QFT machinery. |
| Simultaneity arguments | **Accepts** relativity of simultaneity fully — different hypersurfaces carry different state descriptions with the same observable content (the framework behind Aharonov-Albert 1981 `fol-aharonov-albert-1981` and the Hellwig-Kraus discussion `fol-hellwig-kraus-1970`; both discovery). The H-K reduction's acausal collapsed states are the standard caution: a *naive* collapse-on-hypersurfaces rule produces frame-leaning artifacts; fixing that is the "Myrvold-style" project (§6). |
| Passage / determinism | Neutral: a formulation, not an ontology. |
| Status of claims | TS covariance = established textbook physics (historical papers unread this pass — flagged). Curved Born rule = paper claim with proofs unaudited. |
| Open questions | Extract the exact H-K construction and A-A 1981 argument at full-text stage; connect the curved-Born-rule conditions to the consistency conditions of multi-time systems. |

## 6. Myrvold-style relativistic collapse results (and the unresolved "Hubert-style" item)

- `fol-myrvold-2002-peaceful` (SHPMP 33:435-466, 2002; **discovery** —
  Crossref-verified; author's public PDF located but not fetched): collapse
  postulate, formulated as hypersurface-relative state update, is not
  incompatible with relativity; collapse is not a physical process in
  spacetime that could signal. [Characterization from secondary reputation —
  full text pending.]
- `fol-myrvold-2017-nonstandard-dof` (abstract read): the structural no-go of
  §4.
- `fol-myr-2019-ontology` (chapter, discovery): ontology question for
  relativistic collapse (flash vs matter density vs distributional
  ontologies).

**Unresolved brief item.** The task brief's "Hubert-style relativistic
collapse results" could not be matched to any located publication. Findings
across three search rounds (arXiv author search; Crossref author search; full
fetch of Mario Hubert's publication list; three `web-search-prime` queries):
arXiv's "Hubert, M" is the statistician Mia Hubert; Mario Hubert's
publication list contains no relativistic-collapse paper; his nearest
relevant items are ontology papers, e.g. Esfeld, Hubert, Lazarovici, Dürr
2014 (`fol-esfeld-hubert-lazarovici-durr-2014`, discovery), and a 2025 talk
"The Multi-Time Multi-Field" (workshop listing only; no paper located). No
claim of absence is made — this is a search-scope limit. Candidate
resolutions for the coordinator: (a) the brief meant
Esfeld-Hubert-Lazarovici-Dürr ontology work; (b) a mis-expansion of another
name (e.g., Pearle-style or Bedingham-style results, both covered in §4);
(c) grey literature outside arXiv/Crossref.

| Question | Record |
|---|---|
| What is the foliation | Myrvold's position (per abstract of 2017 + reputation of 2002): either none (hypersurface-relative collapse) or nonstandard DOF; no privileged frame posited. |
| Fixed or dynamical | n/a (no foliation posited). |
| Empirically detectable | Same collapse-test channel as §3/§4. |
| Simultaneity arguments | **Accepts** relativity of simultaneity; **accepts** that collapse is nonlocal; **blocks** the incompatibility argument by (i) separating state description (hypersurface-relative) from observable content (foliation-independent), (ii) the no-signalling structure. This is the most direct published answer to "which simultaneity arguments does collapse accept". |
| Passage / determinism | Collapse is indeterministic; no passage commitment. |
| Status of claims | 2017 = paper claim with theorem-level abstract (proof unaudited). 2002 = unread lead. 2019 chapter = unread lead. |
| Open questions | Full-text audit of 2002 and 2017; whether the 2017 no-go applies to flash models (scope condition analysis). |

## 7. Empirical detectability ledger

What could make a preferred structure observable:

1. **Collapse dynamics itself**: spontaneous radiation and mechanical noise.
   Bounds: `fol-vinante-2017-cantilever` (PRL 119:110401, abstract read),
   `fol-carlesso-2016-gwd-bounds` (PRD 94:124036, discovery),
   `fol-donadi-2021-underground` (Nature Physics 17:74-78, abstract read —
   excludes the parameter-free Diósi-Penrose model specifically; NOT a
   general collapse-model refutation). Review: `fol-bassi-rmp-2013`.
2. **Lorentz-violating observables** (anisotropies, dispersion): bounded by
   SME and Data Tables (reused `phil-sme`, `seed-lorentz-data-2026`). These
   constrain *observable* anisotropic structure. **They do not constrain a
   hidden foliation whose statistics are Lorentz invariant** — an important
   asymmetry the map keeps explicit.
3. **Frame-dependent collapse statistics**: no published positive result
   known to this pass; if a collapse model produced frame-dependent event
   statistics (e.g., collapse rates depending on velocity relative to the
   chosen frame), existing data could bound it — a proposed extraction task,
   not a found result.
4. **Bohmian equilibrium channel**: none known; deviations require
   non-equilibrium initial distributions (in-principle only).

## 8. Cross-theory comparison (contract questions in one table)

| Theory/model | Foliation posited | Fixed/dynamical | Detectable | Blocks Rietdijk-Putnam by | Accepts | Determinism |
|---|---|---|---|---|---|---|
| Neo-Lorentzian | Yes (ether frame) | Fixed | No (hidden by equivalence) | Real frame ordering of spacelike events | Relativity of simultaneity as coordinate fact; Malament definability limits | Yes (Lorentzian dynamics) |
| Bohm-Dirac / HBD | Yes (extra dynamical structure) | Model choice (dynamical in HBD) | No under equilibrium | Foliation ordering | Bell nonlocality; relativity of simultaneity | Yes |
| DGTZ 2014 variant | Yes, but wave-function-determined | Determined by wave function | No under equilibrium (hedged) | Same as HBD + "fundamental Lorentz invariance" reframe | Same as HBD | Yes |
| GRWf (Tumulka 2006) | **No** | n/a | Collapse channel only | Objective flash events without global now | Bell violation; full relativity of simultaneity | No (stochastic) |
| CSL baseline | Implicit frame for noise | Fixed by fiat | Collapse channel only | n/a (nonrelativistic) | — | No |
| Relativistic CSL variants (Bedingham; BDGTZ 2014; Bedingham-Pearle 2025) | No (replaced by covariant structure / nonstandard DOF) | n/a | Collapse channel only | As GRWf | Bell violation | No |
| Tomonaga-Schwinger | No (formulation-level) | n/a | Nothing extra | — | Hypersurface-relativity of state descriptions | n/a (framework) |
| Myrvold 2002/2017 program | No (or nonstandard DOF) | n/a | Collapse channel only | Hypersurface-state vs observable-content separation | Bell nonlocality; relativity of simultaneity | Collapse indeterministic |

**Equivalences and domain restrictions worth keeping in view.** GRWf's
foliation-freedom is proven for non-interacting particles only; the interacting
case is open (paper's own statement). Bohmian foliation-freedom fails for
N>1 without added structure (consensus; HBD's own framing). Myrvold 2017's
no-go has Markovian + standard-DOF scope conditions (abstract-level). These
scope conditions mean the families are *not* interchangeable: "collapse
without foliation" (flash) and "guidance without foliation" (Bohmian) are
different open problems, and §4's tradeoff (covariance ⇔ nonstandard DOF) is
the sharpest published structural constraint this pass found.

**What would defeat a suggested gap.** Any future claim that "relativistic
collapse without foliation (or with dynamical foliation) is an open structural
question" is defeated if: (a) an interacting relativistic GRWf appears
(Tumulka's own program or successors); (b) a Lorentz-covariant GRWm with a
frame-independent density and preserved empirical equivalence appears
(Bedingham 2011 + BDGTZ 2014 already claim fragments); (c) a proof that
Myrvold-2017-style nonstandard DOF are unnecessary for Markovian collapse; or
(d) a demonstration that wave-function-determined foliations (DGTZ 2014) are
dynamically unstable, killing the "fundamentally Lorentz invariant Bohmian"
route. Conversely, a novel contribution in this space must state its scope
against all four.
