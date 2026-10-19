# Time in quantum interpretations: two-state, retrocausal/all-at-once, Everettian, consistent histories, superdeterminism

Status: worker submission for review (kb-time-interpretations lane), 2026-10-19.
Companion file: [sources.jsonl](sources.jsonl) (29 records, prefix `time-`). Reused IDs from
other lanes are cited as-is and not duplicated.

## Scope and reading depth

- 29 source records: 8 full-text, 18 abstract, 3 discovery.
- Full-text anchors: time-tsvf-review-2007 (TeX), time-wharton-argaman-2020 (TeX),
  time-gmh-1994-timesym (TeX), time-hartle-2005-now (TeX), time-sep-everett-2023 (web),
  time-sep-ch-2024 (web), time-thooft-2016 (selected sections, TeX),
  time-hossenfelder-palmer-2020 (TeX).
- The ABL rule itself is read through its reproductions in time-tsvf-review-2007 Sec. II.B and
  time-gmh-1994-timesym Sec. III; the 1964 original (time-abl-1964) was not obtained
  (APS 403). This is recorded per record.

## Distinctions maintained throughout

These are not interchangeable, and the anchors separate them as follows.

| Distinction | How it appears in this lane's anchors |
|---|---|
| Temporal ontology (eternalism vs presentism vs growing block) | Never fixed by the formalisms. TSVF two-boundary descriptions, GMH's rho_i/rho_f, and all-at-once boundary-value solving are formulations; an ontological reading needs extra bridge premises (below). |
| Determinism | Unitary Everettian dynamics is deterministic (SEP Everett Sec. 2, rule 4a); superdeterminism is deterministic by definition (time-hossenfelder-palmer-2020 Sec. III); TSVF and consistent histories are not. Bell: "determinism is not a presupposition of the analysis" (quoted in time-wharton-argaman-2020 Sec. VI.D). |
| Objective passage | No anchor makes passage fundamental. Hartle: "Past, present, and future are not properties of four-dimensional spacetime but notions describing how individual IGUSes process information" (time-hartle-2005-now abstract; Sec. III 'The Present is Not a Moment in Time'; Conclusion labels cognitive universality a conjecture). |
| Causal order / retrocausation | Retrocausation = relaxing no-future-input-dependence (NFID) in a Bell framework (time-wharton-argaman-2020 Sec. I, II); Hossenfelder-Palmer call "retrocausality" misleading for deterministic theories and prefer "Future Input Dependence" (time-hossenfelder-palmer-2020 Sec. III.A). Distinct from the B-theory of time and from ontology. |
| Clock time / proper time | Not the object of this lane; see frontier lane (QRFs, relational clocks). Neither TSVF nor CH requires a preferred clock; GMH note that with a non-indifferent final condition "any notion of a unitarily evolving state at a moment of time" is lost (time-gmh-1994-timesym Sec. III). |
| Thermodynamic/memory arrow | Explicitly separated by the anchors: TSVF's remaining asymmetry is a "fixed 'memory' arrow of time" (time-tsvf-review-2007 Sec. V.C); GMH derive all arrows from rho_i vs rho_f differences (Sec. III); Hartle derives memory asymmetry from boundary conditions (Sec. IV). |

**Standing caveat (our conjecture, flagged as such):** in what follows, "the future is fixed"
is always ambiguous between (i) fixed by boundary conditions in a formulation, (ii) fixed by
deterministic dynamics, (iii) ontologically settled/real in a block sense. Statements in the
anchors cover at most (i) or (ii); (iii) is a bridge-premise conclusion and is labeled ours
wherever asserted.

---

## Theory-comparison contract, per anchor

The unit of comparison is model/version + interpretation (knowledge/README.md contract).
Six items each.

### A. Two-state vector formalism / ABL (time-abl-1964; time-tsvf-review-2007; time-aav-1988; time-apt-2010)

1. **What exists; passage; future fixed.** Authors' claim: ordinary quantum ontology is
   retained; the description of a pre- and post-selected ensemble at time t uses two state
   vectors, |Psi> evolving forward from the pre-selection and <Phi| evolving backward from the
   post-selection (TSVF review Sec. I.B). Passage is not addressed. The future boundary
   (post-selection outcome) is *fixed within the ensemble description*: one selects ensembles
   whose future measurement yields a specified outcome. The authors describe the TSVF as "a
   time-symmetrized approach to standard quantum theory" (abstract), not as a rival ontology.
2. **State space, dynamics, causal structure, clocks.** Ordinary Hilbert-space QM, Schrödinger
   dynamics in both directions; no modified dynamics; ABL rule for intermediate ideal
   measurements: Prob(c_n) = |<Phi|P_{C=c_n}|Psi>|^2 / sum_j |<Phi|P_{C=c_j}|Psi>|^2 (review
   Sec. II.B, eq. labeled (ABL)); generalized to degenerate post-selections (eq. (ABL-new))
   reducing to the Born rule when the final projection is the identity (eq. (ABL-pre)).
3. **Symmetries, preferred structures, access, boundary conditions.** Formally time-symmetric
   probability rules (review Sec. V.D); but creation asymmetry: a forward state can be prepared
   with certainty (failed preparation corrected by a unitary), a backward state can only be
   post-selected with probability; "the difference is due to fixed 'memory' arrow of time: we
   know the past and we do not know the future" (Sec. V.C). Measurement as an operation is
   time-asymmetric even though measurement *outcomes* (effects on other systems) are treated as
   time-symmetric (Sec. V.D).
4. **Observable predictions; empirical status.** Same probabilities as standard QM when both
   boundary conditions are given; new *measurable* quantities appear for pre-/post-selected
   ensembles: weak values (AAV 1988, time-aav-1988), realized experimentally (Ritchie-Story-
   Hulet 1991, time-ritchie-1991). These are predictions *of standard QM* about unusual
   ensembles; no experiment discriminates TSVF from standard QM. Published criticism and
   defense of the time-symmetric formulation is on record (time-apt-2011-exchange).
5. **Bridge premises needed for an ontology.** To claim "the future exists/settled" from TSVF
   one needs: (a) that conditional boundary descriptions of selected ensembles represent
   physical reality rather than information (authors themselves often use epistemic language);
   (b) that a formulation-level symmetry (ABL rules) licenses an ontological symmetry; (c) a
   response to the creation/post-selection asymmetry in Sec. V.C. **Our conjecture:** (a)-(c)
   are independent of the formalism and none is forced by it; block-eternalism does not follow.
6. **Equivalences, contradictions, restrictions.** Classified by Wharton-Argaman as Type IIB:
   future-input dependent but with configuration-space wavefunctions, "no localized screening
   parameters, and so violate the CA locality condition" (time-wharton-argaman-2020 Sec. VI.B).
   Shimony's argument against equal status of forward/backward evolving states is acknowledged
   and discussed in review Sec. V.A (secondary report; Shimony's text not obtained). ABL-rule
   validity conditions were themselves refined after 1964 (Vaidman PRA 57, 2251 (1998); found
   via CrossRef, unread).

### B. Retrocausal and all-at-once formulations (time-wharton-argaman-2020; time-price-wharton-2015; time-wharton-2014-info; time-wharton-2018-retrocausal; time-cramer-1986; time-ssc-rbw-2013)

1. **What exists; passage; future fixed.** Wharton-Argaman framework: spacetime-based
   parameters Q on worldlines; correlations "solved 'all-at-once' rather than unfolding from
   the past to the future" (abstract; Sec. I). Passage not fundamental; no unfolding law.
   The future enters as input/boundary constraints. Price-Wharton: past light-cone zigzag
   influences (time-price-wharton-2015 abstract). RBW: space, time, matter co-constructed by a
   global constraint (time-ssc-rbw-2013 abstract).
2. **State space, dynamics, causal structure, clocks.** Explicit Type IIA toy models use
   local mediating fields with Lorentz-covariant evolution plus constraints (review Sec. IV);
   the framework itself is defined by probabilities over inputs and non-inputs with Local
   Causality decomposed into NFID + lambda-independence + Continuous Action (Secs. II-III).
   All-at-once models may have no dynamical law at all (time-wharton-2014-info abstract).
3. **Symmetries, preferred structures, access, boundary conditions.** Designed for Lorentz
   covariance (review Sec. I); relaxation of the arrow-of-time assumption is the essential
   move: "some of the mediating parameters in these models must functionally depend on
   measurement settings in their future" (abstract). Parameter economy claim: number of
   parameters grows linearly, not exponentially, with entangled particles (abstract, Sec. VII).
4. **Observable predictions; empirical status.** By construction, agreement with QM (same
   inputs, same output predictions) — empirical equivalence is the *entry condition* in this
   framework, not a result. No novel confirmed prediction yet; the authors call generalization
   beyond toy models a "grand challenge" (abstract; Sec. VII). Recent program claims toward
   localized weak-value descriptions of quantum circuits (time-wharton-circuits-2026) are
   within the last 90 days and unrefereed in status of acceptance history — authors' own title
   says "Appear To".
5. **Bridge premises needed for an ontology.** To infer a block universe from all-at-once
   solving one needs at least: (a) that mathematical solution-method (boundary-value problem)
   corresponds to how reality is, not just how models are solved — the stationary-action
   analogy in review Sec. I is explicitly an analogy; (b) that the "one actual history" reading
   of the models is more than instrumental (authors' realist ambition, e.g.
   time-wharton-2014-info); (c) an account of why no retro-signaling is possible given
   future-input dependence (claimed in models; not proven in general). **Our conjecture:**
   even granting (a)-(c), what is obtained is at most a block-*ontology*; nothing here fixes
   eternalism as against, e.g., Stein-style local becoming (found-stein-1991), because causal
   order and ontology remain distinct inputs to the interpretation.
6. **Equivalences, contradictions, restrictions.** Bell's theorem bounds the family: any
   QM-agreeing model violates Local Causality; locally-mediated models exist only by relaxing
   NFID (review Secs. II-III). TSVF and Transactional Interpretation are Type IIB, not
   locally mediated (Sec. VI.B). Wood-Spekkens fine-tuning worry exists for all such models;
   one response by symmetry-robustness is claimed in Almada et al. 2016 (cited in review;
   unread). Transactional interpretation recorded only at abstract/secondary depth
   (time-cramer-1986).

### C. Everettian quantum mechanics (phil-everett; time-sep-everett-2023; time-wallace-2012)

1. **What exists; passage; future fixed.** Pure wave mechanics: universal wavefunction, no
   collapse (SEP Everett Sec. 2-3). What exists, on Wallace's version: one quantum state with
   emergent, approximate, quasiclassical worlds ("mutually dynamically isolated structures
   instantiated within the quantum state", quoted in SEP Sec. 7 from Wallace 2010a); Everett
   himself avoided world-talk and insisted all elements of a superposition are equally real
   because interference between them is always possible in principle (SEP Sec. 5.3, quoting
   Everett 1956, 150). Passage: not fundamental (no anchor claims otherwise; the experienced
   present is handled, if at all, IGUS-style as in the histories lane).
2. **State space, dynamics, causal structure, clocks.** Hilbert-space state, linear unitary
   dynamics only (rule 4a); branching is structure *of the state's decomposition*, not a
   dynamical process; typicality measure m derived from constraints (SEP Sec. 3.2, citing
   Everett 1956, 123-8; 1957, 188-93).
3. **Symmetries, preferred structures, access, boundary conditions.** No physically preferred
   basis needed for Everett's faithfulness argument (SEP Sec. 5.1); decoherence individuates
   worlds on Wallace's version (SEP Sec. 7). Branching is "alien to our experience" but no
   observer would notice it, per Everett's reply to DeWitt (SEP Sec. 5.2, quoting
   Barrett-Byrne 2012, 254).
4. **Observable predictions; empirical status.** Empirical equivalence to standard QM is
   claimed via typicality: typical relative records exhibit the quantum statistics (SEP
   Secs. 5.4, citing limiting-frequency results by Hartle 1968; Farhi-Goldstone-Gutmann 1989).
   The SEP author's assessment: pure wave mechanics "fails to be empirically adequate in any
   standard sense" without auxiliary assumptions, because it lacks forward-looking
   probabilities (Sec. 6); the Deutsch-Wallace decision-theoretic derivation and
   self-location-uncertainty strategies are the modern auxiliary routes (Sec. 7). So:
   *empirical equivalence to standard QM is a contested derivation, not a theorem of the
   formalism.* (This is an authors'-and-encyclopedia claim, not an established result.)
5. **Bridge premises needed for an ontology.** Realism about branches/worlds (or about
   relative records); a probability semantics (decision-theoretic or self-location);
   equivalence-postulate choices about which decompositions are real. **Our conjecture:** the
   deterministic universal dynamics settles nothing about eternalism; a branching ontology
   (worlds-what-and-how-many indeterminate, SEP Sec. 7) is not a single-fixed-future eternalism
   and is closer in formal spirit to Belnap-style branching space-time (phil-belnap) than to a
   block with one worldline per observer; and passage remains unexplained at the fundamental
   level in exactly the way the block-universe literature says it is.
6. **Equivalences, contradictions, restrictions.** In Wharton-Argaman's taxonomy Many-Worlds
   sits "outside the framework": removing the Born rule removes P_I(O) from the fundamental
   description; at the effective level it returns as a Type IB model (Sec. VI.C, citing
   Maudlin 2010). Everett's branches are not causally isolated in his own view (SEP Secs. 5.3,
   7) — a significant difference from DeWitt-style many-worlds. Relativistic Everett remains
   contested in the wider literature (not audited here).

### D. Consistent/decoherent histories (time-griffiths-1984; time-gmh-1990; time-gmh-1994-timesym; time-hartle-2005-now; time-sep-ch-2024)

1. **What exists; passage; future fixed.** Griffiths-CH: quantum histories in frameworks;
   "the absence of a single universally-true state of affairs at each instant of time"
   (SEP CH abstract; Sec. 2.4 "pluricity" vs unicity). No branching worlds (unlike Everett);
   probabilities attach to whole histories. GMH cosmology: closed system with initial and
   final density matrices; time-neutral formulation (Sec. III, Eq. (3.1)). Passage: not
   fundamental; Hartle's IGUS account of the experienced present (time-hartle-2005-now).
2. **State space, dynamics, causal structure, clocks.** Hilbert space; all time dependence
   stochastic; generalized Born rule with chain operators and consistency conditions (SEP CH
   Sec. 4.2, Eqs. (13)-(20)); two-boundary version p(alpha) = N Tr[rho_f P...rho_i P...]
   (GMH 1994 Sec. III).
3. **Symmetries, preferred structures, access, boundary conditions.** "The histories approach
   is time symmetrical in the sense that the rules for assigning probabilities do not single
   out a particular 'direction' or sense of time" (SEP CH Sec. 4.2, from the adjoint-symmetry
   of the chain operator). No preferred framework (R2 "Equality"), though R4 "Utility" orders
   frameworks pragmatically. Boundary conditions: rho_f proportional to identity "seem[s] to
   fit our data well" (GMH Sec. III); a special initial condition plus final indifference is
   "sufficient to explain the observed time asymmetries" (GMH abstract).
4. **Observable predictions; empirical status.** Agreement with standard QM for measurement
   outcomes is built in (SEP CH Secs. 1, 9.2). The two-boundary extension is empirically
   constrained: both boundary matrices pure -> no decoherence, no prediction (GMH abstract);
   rho_f = rho_i -> only trivial dynamics exactly decoheres (GMH Sec. V.B). Kent showed the
   generalized time-neutral theory admits contrary probability-one predictions from different
   consistent sets (time-kent-1997 abstract). Whether any system today can "see" a non-indifferent
   final condition is posed as an empirical question (GMH Sec. III).
5. **Bridge premises needed for an ontology.** CH requires abandoning unicity (SEP CH Sec.
   9.3 acknowledges this as "the principal stumbling block"); a realist reading needs a
   set-selection principle — Dowker-Kent: the approach "illustrates the need to supplement
   quantum mechanics by some selection principle in order to produce a fundamental theory
   capable of unconditional predictions" (time-dowker-kent-1996 abstract). **Our conjecture:**
   CH's pluricity means there is no single fixed future to be eternalist *about*; and the
   time-neutral two-boundary version gives a precise sense in which "the future" is fixed only
   relative to a chosen framework and final boundary — a formulation-level constraint, not a
   block-universe theorem.
6. **Equivalences, contradictions, restrictions.** Kent 1997 contrary-inference result;
   Griffiths-Hartle reply (inference across frameworks illegitimate, PRL 81, 1981); Kent's
   rejoinder (PRL 81, 1982); persistent set-selection problem, recently extended to
   quasi-classical systems with certainty-vs-certainty conflicts (time-zampeli-2026); Bassi &
   Ghirardi critiques answered by single-framework-rule responses per SEP CH Sec. 9.3
   (Bassi-Ghirardi primary texts not obtained; recorded via SEP locators).

### E. Superdeterminism (time-thooft-2016; time-hossenfelder-palmer-2020; time-palmer-2009-isp; time-bell-1977-freevars)

1. **What exists; passage; future fixed.** 't Hooft CAI: a single ontological state evolving
   by local, time-reversible automaton law; "The universe is in a single ontological state,
   never in a superposition of such states" (Sec. 'The CAT and the CAI'); quantum states are
   "templates" (epistemic). Hossenfelder-Palmer: "Psi-epistemic, deterministic theory that
   violates Statistical Independence but is local in the sense of respecting Continuity of
   Action" (Sec. III), explicitly *not an interpretation of QM* but a more fundamental theory
   from which QM is derived (Sec. I). Palmer ISP: states on a non-computable fractal invariant
   set (time-palmer-2009-isp abstract). The future is fixed in the strongest sense in this
   family — by deterministic law from initial state — with the strong initial-state
   correlations doing the Bell-evasion work ('t Hooft Sec. 'Conclusions': "Correlations do not
   require superluminal signals, let alone signals going backwards in time").
2. **State space, dynamics, causal structure, clocks.** CAI: discrete lattice data Q(x,t),
   local evolution laws, time-reversibility conditions (Sec. 'Concise description...', Eqs.
   (Dlattice), (CAevollaw)); continuum limit and Hamiltonian positivity acknowledged
   problematic (same section; Sec. 'Conclusions'). Hossenfelder-Palmer: hidden variables are
   known degrees of freedom resolvable at experiment's energy scale (Sec. VI premise).
3. **Symmetries, preferred structures, access, boundary conditions.** CAI concedes that
   Lorentz invariance of the underlying automaton is unresolved (Secs. 'The CAT and the CAI',
   'Conclusions') — a preferred-frame risk for the temporal-ontology discussion. Lambda-
   independence violated: rho(lambda|a,b) != rho(lambda) (Hossenfelder-Palmer Sec. III).
   Counterfactual definiteness explicitly *not* assumed for non-ontological operators ('t Hooft
   Sec. 'Counterfactual definiteness').
4. **Observable predictions; empirical status.** In-principle empirical equivalence with QM at
   tested precision is required by the derivation ambition (Hossenfelder-Palmer Sec. III:
   wavefunction should reproduce tested QM predictions). Beyond equivalence: the authors
   propose an (almost) model-independent test — near-identical preparations with small cool
   detectors at small time increments should show time-correlations violating Born statistics
   (Sec. VI) — an authors' proposal, not an established result. Wharton-Argaman's analysis
   argues explicit QM-agreeing superdeterministic toy models (Brans 1988; Hall 2016) treat
   future settings as free inputs after all, re-entering the standard framework (Sec. VI.C).
5. **Bridge premises needed for an ontology.** Determinism here is a *stipulated premise*
   (Hossenfelder-Palmer Sec. III.B: "we here assume it is [deterministic]"), not a consequence.
   **Our conjecture:** even a completed superdeterministic theory would fix the future only in
   sense (ii) — deterministic evolution of ontological states; the further step to eternalism
   ('all times exist') requires exactly the bridge premise the relativity literature debates
   (found-stein-1991; found-rietdijk; found-putnam), and CAI's unresolved Lorentz status makes
   that step *harder*, not easier, here.
6. **Equivalences, contradictions, restrictions.** Bell's theorem is not escaped; it is
   re-attributed to lambda-independence violation, whose coherence Bell himself discussed
   (time-bell-1977-freevars; read second-hand). 't Hooft: no-go theorems' "small print" is
   "the assumed absence of strong local as well as non-local correlations in the initial
   state" (Sec. 'Conclusions'). Positivity/Lorentz obstacles recorded by the author himself.
   Free-will objection literature engaged in Hossenfelder-Palmer Sec. IV (cosmic Bell tests:
   they argue far-past setting choices address the locality loophole only "to some extent").

---

## Master comparison table

Fixed-future, branching, and empirical-equivalence claims, with locators. "A" = authors' claim
in the anchor; "R" = reviewer/secondary claim; "ours" = our conjecture (no novelty claim).

| Interpretation (anchor, version) | What fixes the future (claim + locator) | Branching / splitting claim | Empirical-equivalence claim (status + locator) |
|---|---|---|---|
| ABL / TSVF (time-tsvf-review-2007, arXiv:quant-ph/0105101v2; time-abl-1964) | A: both boundaries given: pre-selection and post-selection fix the ensemble's two-state vector; intermediate probabilities by ABL rule (Sec. I.B, II.B). Future "fixed" only for the post-selected subensemble. | A: none; single world, single history per selected system. | A: "time-symmetrized approach to standard quantum theory" (abstract); same predictions, new observables (weak values) for pre-/post-selected ensembles (Sec. III; time-aav-1988; measured: time-ritchie-1991). Status: equivalence by construction; published criticism on record (time-apt-2011-exchange). |
| Retrocausal locally-mediated (time-wharton-argaman-2020, RMP 92, 021002) | A: no past-to-future unfolding; solutions solved all-at-once under boundary constraints; mediating parameters may depend on future settings (abstract; Secs. I, IV). | A: none. One actual history reading intended (Sec. I; time-wharton-2014-info). | A: agreement with QM is the framework's entry condition (Secs. I-III); generalization to all phenomena a "grand challenge" (abstract). Status: equivalence assumed for toy models only; no general model. |
| Transactional (time-cramer-1986, RMP 58, 647) | A (per secondary classification): offer/confirmation wave handshake; future boundary involved (time-wharton-argaman-2020 Sec. VI.B). | A: none. | R: Type IIB (not locally mediated); equivalence to QM claimed by program. Status: primary text unread this pass — abstract/secondary only. |
| Adynamical blockworld / RBW (time-ssc-rbw-2013, FoP 43, 502) | A: global constraint ("NPRF + h") co-constructs space, time, matter; adynamical global constraint rather than time-evolved dynamics (abstract). | A: none; single block. | A: reproduces QM kinematics via principle-theory reconstruction (abstract; program papers unread). Status: authors' claims. |
| Everett / many-worlds (phil-everett; time-sep-everett-2023; time-wallace-2012) | A: unitary dynamics fixes the universal state deterministically (SEP Sec. 2, rule 4a); but *which* branch one is in is not fixed — branch count and individuation are level-dependent (SEP Sec. 7 on Wallace). R: no forward-looking probabilities without auxiliary assumptions (SEP Sec. 6). | A: DeWitt-style splitting rejected by Everett; worlds emergent, approximate (SEP Secs. 5.3, 7); all superposition elements equally real (SEP Sec. 5.3, quoting Everett 1956, 150). | R: typical relative records show quantum statistics (SEP Secs. 5.4); "fails to be empirically adequate in any standard sense" without auxiliary premises (SEP Sec. 6); decision-theoretic route (SEP Sec. 7). Status: equivalence contested, not established. |
| Consistent histories (time-sep-ch-2024; time-griffiths-1984; time-gmh-1994-timesym) | A: no single true state of affairs at a time ("pluricity", SEP CH abstract, Sec. 2.4); two-boundary rho_i/rho_f fix history probabilities within a framework (GMH Sec. III, Eq. (3.1)); time-symmetric probability rules (SEP CH Sec. 4.2). | A: no world-branching; alternative *frameworks*, not worlds (SEP CH Secs. 2.4, 9.3). | A: agrees with standard QM predictions (SEP CH Secs. 1, 9.2); constraints on final conditions: pure-pure impossible, rho_f=rho_i trivial (GMH abstract, Sec. V.B). R: contrary probability-one inferences from different consistent sets, including in the time-neutral theory (time-kent-1997); set-selection problem persists in quasi-classical cases (time-zampeli-2026). Status: equivalence agreed for outcomes; framework-internal inference contested. |
| Superdeterminism / CAI (time-thooft-2016, arXiv:1405.1548; time-hossenfelder-palmer-2020, Front. Phys. 8, 139) | A: single ontological state, deterministic local reversible law fixes all states at all times ('t Hooft Secs. 'The CAT and the CAI', 'Conclusions'); determinism stipulated (HP Sec. III.B). | A: none; single world. | A: QM derived from the deeper theory, reproducing tested predictions (HP Secs. I, III); proposed beyond-equivalence test via time-correlations (HP Sec. VI) — proposal only. R: QM-agreeing toy models covertly restore free settings (time-wharton-argaman-2020 Sec. VI.C). Status: no accepted complete model (acknowledged by both programs). |

---

## Bridge premises: what each family needs to claim an ontology

Collected from items 5 above. A "bridge premise" is an extra philosophical assumption that
converts a formulation-level fact into an ontological conclusion.

1. **Boundary description -> temporal ontology.** From "the description uses conditions at both
   ends" (TSVF, GMH, all-at-once) to "the future exists/is settled" requires: descriptions of
   selected ensembles or boundary conditions are representations of being, not bookkeeping;
   and formulation-level time-symmetry licenses ontological timelessness. None of the anchors
   asserts this step; Hartle's and GMH's own framing (information processing; testable final
   conditions) keeps it open. **Ours:** this premise is exactly where the Rietdijk-Putnam
   literature's contested move recurs (found-rietdijk; found-putnam; found-stein-1991), and it
   is not forced by any quantum formalism.
2. **Determinism -> eternalism.** From "deterministic evolution" (Everett rule 4a; CAI) to
   "all times equally real" requires a separate premise; Bell's caution that determinism is
   not even a Bell presupposition (time-wharton-argaman-2020 Sec. VI.D) shows how easily the
   two are conflated. Everett additionally shows the converse split: a deterministic dynamics
   with no single fixed future-content, because branch individuation is level-relative
   (SEP Sec. 7). **Ours:** keep "deterministic" and "eternalist" as orthogonal axes in any
   synthesis map.
3. **Branching realism.** Everettian ontology needs: realism about emergent worlds (Wallace)
   or about relative records (Everett); a probability semantics; a basis/individuation
   criterion (decoherence, decision-theoretic constraints). Each is an auxiliary assumption
   (SEP Secs. 6-7), so the empirical equivalence of Everettian QM inherits their status.
4. **Unicity abandonment (CH).** Realist CH requires accepting pluricity or finding a
   set-selection principle (SEP CH Sec. 9.3; time-dowker-kent-1996 abstract). Without one,
   "the future is fixed" has no framework-independent meaning in CH.
5. **Statistical-independence violation without conspiracy.** Superdeterminism needs: an
   account of rho(lambda|a,b) != rho(lambda) that supports scientific method (Hossenfelder-
   Palmer Secs. IV, VI) and a local model whose toy versions, per critics, restore free
   settings anyway (time-wharton-argaman-2020 Sec. VI.C). The free-variable assumption itself
   is Bell's (time-bell-1977-freevars, second-hand).
6. **Passage.** No family makes objective passage fundamental; Hartle's IGUS account explains
   its *experience* in a four-dimensional setting and flags the cognitive-universal claim as a
   conjecture (time-hartle-2005-now Conclusion). Any synthesis must therefore not read
   empirical equivalence over outcomes as fixing the passage question.

## Strongest contrary evidence per family (pointers)

- TSVF: Shimony-style objection to equal status of forward/backward states (via review
  Sec. V.A); PT 2011 exchange (time-apt-2011-exchange); Type IIB non-locality classification
  (time-wharton-argaman-2020 Sec. VI.B).
- Retrocausal: Wood-Spekkens fine-tuning argument (review Sec. VI.B discussion; primary
  unread); Bell's theorem itself bounds all families; superdeterminism-vs-retrocausality
  boundary disputes (HP Secs. III.A, III.B).
- Everett: empirical adequacy without auxiliary assumptions (SEP Sec. 6); Maudlin's argument
  that removing the Born rule removes the predictions (review Sec. VI.C).
- Consistent histories: Kent 1997 contrary inferences incl. in the time-neutral theory;
  Dowker-Kent selection-principle requirement; Zampeli et al. 2026 quasi-classical conflict;
  unicity objection acknowledged by the SEP author.
- Superdeterminism: Bell 1977 free-variables defense; Wharton-Argaman's framework argument
  that QM-agreeing superdeterminism re-imports free settings; CAI's own admitted
  Hamiltonian-positivity and Lorentz obstacles.

## Nearest predecessors and defeat conditions (no novelty claims)

This lane makes no novelty claim. For any future synthesis that claims a gap (e.g., "no one
has compared X and Y at assumption level"), the nearest predecessors that would defeat it are:

- Wharton-Argaman 2020 (RMP 92, 021002): already a taxonomy across Bell-compatible
  reformulations, including superdeterminism and MWI treatments — any cross-interpretation
  comparison of *causal* assumptions must differentiate itself from Secs. II-III and VI.
- Gell-Mann & Hartle 1994 (time-gmh-1994-timesym): already connects ABL two-boundary structure
  with histories in a time-neutral cosmological framework — any "two-time meets histories"
  proposal must go beyond Eq. (3.1) and Sec. V.B.
- Kent 1997 + replies: any claim that consistent-histories inference problems are unresolved
  must engage the PRL 78/81 exchange and the 2026 quasi-classical extension.
- SEP entries (2023, 2024): the interpretive-bridge analysis here (items 5, bridge premises)
  substantially overlaps their content; a new contribution would need formal results
  (e.g., explicit boundary-condition -> ontology maps with countermodels), not prose
  synthesis. This is infrastructure for candidate D in knowledge/NOVELTY.md, not itself a
  candidate result.

What would defeat a proposed synthesis gap: a published general mapping from two-boundary or
all-at-once formulations to ontologies with explicit bridge-premise separation; a theorem
showing empirical equivalence/inequivalence of any pair here under stated observables; or a
set-selection principle for CH (which would change item D5 entirely).
