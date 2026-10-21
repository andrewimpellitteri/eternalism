# Empirical discriminators for temporal ontology: an admissibility audit

Status: documentary/analytic audit, 21 October 2026. No new experiment, no new
prediction, no novelty claim. This note classifies proposed tests of temporal
ontology using the manuscript's own standards and states what each test could
and could not establish. It does not edit the manuscript, the workboard, the
source registers, or any other task's files.

## 0. Answer

Across 21 candidate families with a locatable primary source, **none is a
genuine ontology discriminator** in the sense defined in §2. Five are primarily
parameter constraints on named physical models (D1–D3, D7, D17); seven are
primarily model-selection tests between physical theories (D1, D4, D6, D8–D10,
D12); two are positive equivalence results that predict *no* separation (D5,
D11); four constrain a different question — causal order, T symmetry, or an
interpretation (D13, D16, D18, D19); four supply no admissible operational
protocol at all (D14, D15, D20, D21). D1 is counted under two headings
(parameter constraint and model selection); D17 is counted once but also carries
a category-crossing use, marked in its row.

The strongest genuine-discriminator *candidate* is the coupled preferred-frame
route behind the LAGEOS $\alpha_1$ analysis (D1). It is the only candidate with
a named model in which the disputed structure is dynamically coupled, an
existing precision dataset, and a specified signal. It still fails, for a reason
that generalizes: a block/eternalist package can carry the same vector field, so
a detection would select a gravitational model, not an ontology.

Under the manuscript's stated premises no protocol changes the ontology verdict
(§6). What would change it is not a detector reading but an independently
defended **exclusivity premise**: a demonstration that one ontology's
constitutive commitments *entail* a physical structure with a coupling, and that
the rival's commitments *forbid* it. No candidate in the literature screened here
supplies that premise, and for every structure proposed (a foliation, collapse
noise, spacetime discreteness, a cosmological arrow) at least one rival ontology
has an admissible realization that carries it.

## 1. The standard applied

From `paper/main.tex` (line numbers of the working draft):

- **Admissibility conditions (i)–(iv)**, §2 "Constraining admissibility without
  settling the dispute by fiat", lines 139–162: (i) mathematical consistency and
  empirical adequacy in the declared regime; (ii) fidelity to the ontology's
  explicitly stated constitutive commitments rather than its name; (iii) a
  specified dynamics, probability model and operational interface including
  auxiliaries; (iv) independent motivation for additional structure, assessed by
  the same standard as rivals. Constitutive commitments and permitted auxiliary
  changes are to be registered *before* the discriminator is evaluated; a
  comparison must state which conclusions change under reasonable alternative
  admissibility profiles.
- **Three inferential burdens**, §3, lines 204–257: *exclusion*
  ($O\land B\land A\Rightarrow F$, $P\Rightarrow\neg F$), *empirical
  discrimination* ($p(D\mid M_1,e)=p(D\mid M_2,e)$ for all $D,e$ means no
  likelihood discrimination in the declared protocol class), and *representation
  equivalence* (structure-preserving map for a domain; not automatically
  ontological identity, gauge, or equal explanation).
- **Two profiles**, fixed in `research/article-admissibility/PROTOCOL.md`
  lines 45–65: the *empirical and structural* profile (admit a consistent
  package with a shared physical model and an explicit bridge; matched
  likelihoods give no empirical preference) and the *constitutive explanation*
  profile (ask for an independently motivated account; if the verdict needs the
  contested premise, report circularity/underdetermination rather than a score).

Three consequences are used throughout. (a) A bound on a parameter of a named
model is not evidence about an ontology. (b) A likelihood difference between two
physical models is not a likelihood difference between two ontologies unless the
ontologies are tied exclusively to those models. (c) An equivalence proved for a
declared model class is a result about that class, not a global equivalence of
ontologies.

## 2. Classification used in the tables

| Code | Meaning | Test satisfied |
|---|---|---|
| **P** | Parameter constraint | Bounds/fits a parameter of a named model family. No model comparison required. |
| **M** | Model selection | Two or more named physical models assign different likelihoods to a common protocol. |
| **O** | Ontology discriminator | **M** plus an independently defended *exclusivity premise*: the admissible realization classes of the rival ontologies have essentially disjoint model supports (or a bridge changes the probability law). |
| **E** | Equivalence / no-discrimination result | A proof or construction showing identical predictions in a declared class. |
| **N** | Not admissible / no protocol | No specified preparation, observable, dynamics or probability model. |
| **X** | Category crossing | Constrains causal order, fundamental symmetry, or an interpretation, not temporal ontology. |

**O is not a stronger M.** It is M plus a separate philosophical premise. This is
the audit's central bookkeeping claim and it is a consequence of the manuscript's
own definition, not a new theorem (§6).

## 3. Master table

Read-depth codes: **A** = abstract/metadata verified by this audit on 21 Oct 2026
(arXiv abstract page fetched, or DOI metadata already checked in the cited
project record); **R-F** = project record states full-text, primary *not*
re-read here (inherited); **R-A** = project record is abstract-level, primary not
read here. "Excl." = does an admissible realization of a rival ontology carry the
same structure? Full locators and what was actually read are in §9.

| ID | Candidate and primary locator | Depth | Verdict | Bridge premise the inference needs | Excl. |
|---|---|---|---|---|---|
| D1 | Preferred-frame PPN $\alpha_1$ / LAGEOS: Lucchesi et al., PRL 137, 051401 (2026), arXiv:2501.10588v2 Eq. (12); Foster–Jacobson, PRD 73, 064015 (2006), Eqs. (10)–(12) | A + R-F | **P** on Einstein-aether couplings (an $\alpha_1$ slice); **M** aether vs GR | "presentism constitutively requires a *coupled* foliation" | Yes — block + aether is coherent |
| D2 | SME clock comparisons: Kostelecký–Vargas, PRD 98, 036003 (2018), arXiv:1805.04499v1, Tables 5–6, 9–10, 13–14 | R-F | **P** | "a preferred now entails Lorentz-violating matter coefficients" | Yes |
| D3 | Rotating optical/microwave cavities: Müller et al., PRL 99, 050401 (2007) | R-A | **P** | same as D2 | Yes |
| D4 | Quantum clock interferometry: Zych et al., Nat. Commun. 2:505 (2011), arXiv:1105.4531; Loriani et al., Sci. Adv. 5:eaax8966 (2019); Sorci et al., PRL 136, 163602 (2026) | A + R-F | **M** (quantum proper-time dynamics vs classical clock) | "objective passage requires definite classical proper time" | Yes |
| D5 | Page–Wootters / relational trinity: Moreva et al., PRD 96, 102005 (2017), arXiv:1710.00707; Höhn–Smith–Lock, PRD 104, 066001 (2021), arXiv:1912.00033v3 | A + R-F | **E** (conditional dynamics reproduced; two descriptions share the state) | "conditional dynamics *exhausts* temporal reality" (a sufficiency premise) | Yes — the construction is shared by both readings |
| D6 | Interacting / non-ideal clocks: Smith–Ahmadi, Quantum 3:160 (2019); Chataignier et al., NJP 28, 034504 (2026), arXiv:2409.06479 | A + R-F | **M** among clock formulations | "a formulation failure is an ontology failure" | Yes |
| D7 | Collapse models GRW/CSL/DP: Vinante et al., PRL 119, 110401 (2017); Donadi et al., Nat. Phys. 17, 74–78 (2021); Dai–Miao–Ma, arXiv:2411.17588; Bassi et al., RMP 85, 471 (2013) | R-A | **P**; **M** only if frame-dependent collapse statistics exist (no published result) | "collapse = objective becoming" | Yes — block + stochastic collapse is admissible |
| D8 | Everpresent $\Lambda$: Ahmed–Dodelson–Greene–Sorkin, PRD 69, 103523 (2004), astro-ph/0209274 | A | **M** (cosmological, statistical) | "a $\Lambda$ fluctuation evidences becoming" | Yes |
| D9 | Causet-induced diffusion ("swerves"): Dowker–Henson–Sorkin, MPLA 19, 1829 (2004), gr-qc/0311055 | A | **M**, proposed, no detection | "discreteness = becoming" | Yes |
| D10 | Light blurring from discreteness: Dowker–Henson–Sorkin, PRD 82, 104048 (2010), arXiv:1009.3058 | A | **M**; model predicts *no significant* deviation | same | Yes |
| D11 | Causal-set growth vs completed order: Rideout–Sorkin, PRD 61, 024002 (2000); Brightwell–Luczak, Ann. Appl. Prob. 21, 1493 (2011); Surya–Zalel, CQG 37, 195030 (2020); Wüthrich–Callender, BJPS 68, 907 (2017) | R-F | **E** for covariant records in classical CSG | "records are covariant events" vs "records are stage-relative" | Yes — the tenseless reading uses the same measure |
| D12 | Cosmological/thermodynamic arrow: Goldstein, cond-mat/0105242; Goldstein–Tumulka–Zanghì, PRD 94, 023520 (2016); Earman, SHPMP 37, 399 (2006); Carroll–Chen, hep-th/0410270 | R-F / R-A | **M** (cosmology); **N** for ontology | "an arrow requires becoming" | Yes |
| D13 | BABAR T violation: PRL 109, 211801 (2012), arXiv:1207.5832 | R-A | **X** (fundamental symmetry) + **P** | "T violation = an open future" | Yes — distinct questions |
| D14 | Cold-atom entropic-time analog: Barontini, PRR 8, L022047 (2026), arXiv:2509.07745v2 Eq. (3) | R-F | **N** for ontology; analog benchmark only | "an internal entropy clock is cosmological time" | Yes |
| D15 | Thermal time / modular flow: Connes–Rovelli, CQG 11, 2899 (1994), gr-qc/9406019; van Neerven–Portal, arXiv:2306.13774v2 | R-F / R-A | **N** (no protocol); **M** only in principle | "the modular flow *is* physical time" | Yes |
| D16 | Indefinite causal order / quantum switch: Procopio et al., Nat. Commun. 6:7913 (2015), arXiv:1412.4006 | A | **X** / **M** for causal-order models | "causal order = temporal ontology" | Yes |
| D17 | GRB dispersion / linear LIV: Fermi GBM/LAT, Nature 462, 331–334 (2009), arXiv:0908.1832 | A | **P**; **X** with respect to causal sets | "discreteness entails LIV dispersion" | Yes — causets are Lorentz-invariant (D9–D10) |
| D18 | Delayed-choice quantum eraser: Kim et al., PRL 84, 1–5 (2000), quant-ph/9903047; Ma et al., PNAS 110, 1221–1226 (2013), arXiv:1206.6578 | A | **X** (interpretation-level; identical predictions) | "retrocausal readings make different predictions" | Yes |
| D19 | Definability theorems: Clifton–Hogarth, Synthese 103, 355–387 (1995), Thm 1 pp. 360–365, Cor. 1(A) p. 367; Stein, Phil. Sci. 58, 147–167 (1991) pp. 148–150; Malament, Noûs 11, 293–300 (1977) | R-F | **X** as an empirical test; structural *exclusion* argument | "the theorem's premises are ontological commitments" | n/a (not empirical) |
| D20 | Brading's "empirical hypothesis": Phil. Sci. 80, 1101–1111 (2013); SHPSA 50, 13–19 (2015) | R-F / R-A | **N** (no protocol despite the title) | law-constitutive unity $\Rightarrow$ system present extent | Yes |
| D21 | Relational becoming as a third option: Rovelli, Found. Phys. 49, 1325–1335 (2019), arXiv:1910.02474 | A | **N** (no test proposed) | "local becoming entails some observable" | Yes |

## 4. Load-bearing rows

**D1, LAGEOS / preferred frame.** The 2026 analysis fits a phase-sensitive
annual signal in the LAGEOS and LAGEOS II mean argument of latitude, with the
candidate preferred direction taken from the CMB, and reports
$\alpha_1=(+1\pm2)\times10^{-5}$ (SATAN) and $(+2\pm3)\times10^{-5}$ (GEODYN II),
$\pm$ statistical, with a systematics RSS near $8\times10^{-6}$ (arXiv v2
Eq. 12; PRL Table II gives $7.7\times10^{-6}$). These are estimates compatible
with zero, not a confidence-level upper bound and not a detection. Two further
limits matter and are usually dropped in popular retellings. First, the two
values come from two orbit-determination packages applied to the same LAGEOS
laser-ranging programme, not from two independent experiments.
Second, $\alpha_1$ is one PPN combination: Foster–Jacobson show that nonzero
aether couplings can yield vanishing preferred-frame parameters, so even a null
constrains a slice of the coupling space rather than excluding the model family.
The ontological step needs "presentism requires *this* coupled foliation". That
is not a consequence of presentism; it is an extra constitutive claim, and its
rival — a block with an aether field — is a perfectly admissible eternalist
package. Verdict: parameter constraint with genuine model-selection power, not an
ontology discriminator.

**D4, clock interferometry.** Zych et al. propose that a clock in spatial
superposition loses fringe visibility in a way "that cannot be explained without
the general relativistic notion of proper time" (authors' abstract claim).
Loriani et al. derive a concrete closed light-pulse geometry sensitive to
kinematic time dilation and insensitive to gravitational redshift in the freely
falling frame. Sorci et al. propose a trapped-ion protocol with squeezing and
Ramsey readout. All three are tests of *quantum clock dynamics* against a
classical point-clock effective description. A confirmed signal would be a
success of standard relativistic quantum theory, not evidence for or against
eternalism; a null or anomalous result would constrain a Hamiltonian. The bridge
needed for ontological import — "objective passage requires definite classical
proper time" — is neither stated nor defended by these papers, and is
independent of the physics.

**D5, Page–Wootters and the trinity.** Moreva et al. implement a narrow-band
single photon with position as clock and report two-time correlations and an
internal-view Leggett–Garg violation while the external description is
time-independent over the experiment. Höhn–Smith–Lock prove an equivalence among
Dirac-observable, Page–Wootters and relational-Heisenberg descriptions under
stated hypotheses (notably no clock–system interaction). This is the clearest
case in the set where the correct verdict is *equivalence*: both a "time is
fundamental" and a "time is relational" reading can use the same state, the same
POVMs, and the same numbers. The experiment demonstrates feasibility of internal
clock correlations; it does not favour fundamental over emergent time. What the
relational reductionist still needs is the sufficiency premise that conditional
dynamics exhausts every temporal role — a philosophical premise the manuscript
already isolates (main.tex lines 369–375).

**D7, collapse models.** Non-interferometric bounds (cantilever heating,
underground shielding, kilogram masses) constrain CSL/DP parameters; Donadi et
al. exclude the parameter-free Diósi–Penrose model specifically, which is not a
general refutation of collapse models. A confirmed collapse signal would be new
physics and would make the future genuinely stochastic. It would not make the
future *ontologically open* in the sense at issue: an eternalist block can
contain stochastic transitions, and the manuscript is explicit that eternalism
does not entail determinism (main.tex lines 101–107). The one place where
collapse could yield a model-selection test with a foliation flavour is
frame-dependent collapse statistics: a covariant model and a foliated model can
in principle differ in event rates as a function of velocity relative to the
foliation. The project's preferred-foliation lane searched for a published
positive result and found none; that is a search-scope statement, and it is the
most interesting genuinely open empirical question in this table.

**D11, causal-set growth.** Classical sequential growth (Rideout–Sorkin) is a
probability measure on labelled, future-infinite causets. Conditional on the
unlabelled poset, compatible generation orders are equiprobable
(Brightwell–Luczak), and covariant events have the same measure whether narrated
as growth or as a completed ensemble. The project's own exact check (n ≤ 5,
`knowledge/defeat-search/csg_ancillarity_check.py`) confirms that birth-order data
are ancillary to the coupling parameters given the unlabelled causet. This is a
positive no-discrimination result for covariant records in that model class. The
tempting escape — a stage-relative record — is an *access* assumption, and a
block can host a bounded observer with stage-indexed records. So even the escape
does not reach ontology (§5, Protocol B).

**D12, arrows.** The Past Hypothesis is a low-entropy boundary condition plus a
typicality measure; Goldstein–Tumulka–Zanghì argue in a simple model that it is
not needed; Carroll–Chen produce a two-sided arrow in a different model class;
Earman questions whether a cosmological Boltzmann entropy is even well defined
in GR. These are disputes inside cosmology. "An arrow requires becoming" is a
bridge premise, and the reverse implication fails: a block history can be
entropy-increasing. BABAR's T violation (D13) belongs to a different question
again and is a good example of a real result routinely over-read.

**D17, discreteness and Lorentz invariance.** A common inference is
"discrete spacetime ⇒ Lorentz-invariant dispersion ⇒ Fermi/GRB bounds apply".
Dowker–Henson–Sorkin argue the opposite for causal sets: discreteness is locally
Lorentz invariant, and they build a Lorentz-invariant diffusion model; their
later transmission calculation finds predictions that "do not differ
significantly" from the continuum. So the GRB bound constrains a different
(class of) quantum-gravity phenomenology. Using it as a causal-set or
"discrete-time" test crosses categories.

**D18, delayed choice.** Kim et al. and Ma et al. are real, well-known
experiments, and they are predicted by ordinary quantum mechanics; the
"causally disconnected choice" version confirms no-signalling. Retrocausal and
block readings do not differ in their predicted coincidence rates. This is the
cleanest example of an experiment whose *interpretation* is disputed while its
*predictions* are not — exactly the pattern the manuscript's likelihood criterion
rules out as a discriminator.

**D19, definability.** Clifton–Hogarth classify absolute becoming relations in
time-oriented Minkowski spacetime under implicit definability, transitivity and
inclusion of chronological connectibility; adding distinguished worldlines or
changing the automorphism group changes the survivor set. These are structural
exclusion results: they constrain which relations a package can use, given
premises. They are not measurements, and the manuscript already refuses to read
them as excluding their own premises.

### Conditions (i)–(iv) applied to the two strongest candidates

| Condition | D1 (coupled preferred frame) | D11 (causal-set growth) |
|---|---|---|
| (i) consistency and empirical adequacy | Yes for Einstein-aether in an allowed coupling region; the PPN fit is a standard weak-field analysis | Consistent as classical CSG; the authors do not claim it recovers GR |
| (ii) fidelity to stated constitutive commitments | **Fails for the ontological step.** Presentism's stated commitments do not include a unit timelike vector; the vector is stipulated, not derived | Ambiguous. Sorkin's growth reading is faithful; Wüthrich–Callender show a tenseless reading of the same measure is equally faithful, so the model does not fix the ontology |
| (iii) dynamics, probability model, operational interface | Yes for the gravity model. No operational interface connects the foliation to an ontological predicate | Yes for the measure and transition probabilities; **no observer/record model** is supplied |
| (iv) independent motivation for the extra structure | The aether is motivated inside its own research programme, not as a requirement of presentism; a block advocate may adopt it on the same grounds | The growth dynamics is motivated by covariance, not by an ontological need; the same motivation is available to the tenseless reading |

Both candidates pass (i) and (iii) at the level of the physical model and fail
(ii)/(iv) at the level of the ontological bridge. That pattern — physical model
admissible, ontological bridge stipulated — recurs in every row of Table 1 and is
the concrete content of the "no genuine ontology discriminator" verdict.

## 5. What observation would change what

Table 2 separates the *model* verdict from the *ontology* verdict. "None" in the
last column means: no outcome of that protocol, by itself, changes the
underdetermination conclusion.

| ID | Observation that changes the model verdict | Effect on ontology verdict |
|---|---|---|
| D1 | Confirmed $\alpha_1\neq0$ with the predicted annual phase and CMB-aligned axis, stable across both orbit-determination packages and across targets, in an aether coupling region with $\alpha_1\neq0$ | None. Selects a gravity model. Becomes an **O** only with the exclusivity premise of §6. |
| D2 | A sidereal/annual frequency modulation matching a named SME coefficient combination, reproduced across clock species | None |
| D3 | Orientation-dependent resonance shift above systematics, matching a sector fit | None |
| D4 | Visibility loss (or its absence) matching the proper-time prediction in a geometry that isolates the effect | None; constrains clock Hamiltonians |
| D5 | A violation of the trinity's stated hypotheses (e.g. interaction-induced failure of the reduction maps) | None; would scope a representation equivalence, not choose an ontology |
| D6 | A norm-preserving interacting construction outside the current hypotheses, or a demonstrated failure of one | None |
| D7 | A heating/radiation signal above background; or velocity-dependent collapse rates | None for the signal; the velocity-dependent case would be **M** between covariant and foliated collapse, still not **O** |
| D8 | $\Lambda$ fluctuation statistics distinguishable from a fixed $\Lambda$ | None |
| D9 | Lorentz-invariant diffusion signature in UHECR propagation | None |
| D10 | Anomalous blurring of distant sources above the model's small predicted level | None |
| D11 | A physically realizable stage-relative record not expressible as a covariant event | Changes **E** to **M**; still not **O** (a block hosts stage-indexed observers) |
| D12 | A two-sided arrow, or a measured low-entropy boundary disfavouring one cosmological model | None |
| D13 | A failure of T symmetry in a new sector | None |
| D14 | Robustness of the internal clock under independent coarse-graining choices | None |
| D15 | A demonstrated protocol in which modular flow is measured as an unsharp observable | None; would make "thermal time" operational, not ontological |
| D16 | A causal-order effect not reproducible by a fixed-order model | None; causal order ≠ temporal ontology |
| D17 | A dispersion anomaly with the predicted energy dependence | None |
| D18 | Any deviation from ordinary quantum predictions | Would revise quantum mechanics, not temporal ontology |
| D19 | n/a (no measurement) | Changing a premise changes the classification, not the data |
| D20 | n/a (no protocol) | n/a |
| D21 | n/a (no protocol) | n/a |

### Protocol A (concrete, near-term): coupled-foliation adjudication

1. **Models.** $M_{\rm GR}$: $\alpha_1=0$. $M_{\rm ae}(\mathbf{c})$: Einstein-aether
   with couplings $\mathbf{c}=(c_1,c_2,c_3,c_4)$ and predicted $\alpha_1(\mathbf c)$
   (Foster–Jacobson Eqs. 10–12), restricted to a coupling region with
   $\alpha_1(\mathbf c)\neq0$ and otherwise consistent with existing bounds.
2. **Preparation/observable.** Satellite laser ranging to LAGEOS/LAGEOS II;
   phase-sensitive fit of the annual term in the mean argument of latitude with
   the CMB-aligned candidate direction (the paper's choice, not a derived
   prediction); both orbit reductions; full systematic budget.
3. **Decision rule.** A nonzero $\alpha_1$ at high significance, with the
   predicted phase and axis, stable under reduction package and target choice,
   and consistent with an aether region whose other PPN predictions survive,
   favours $M_{\rm ae}$ over $M_{\rm GR}$.
4. **Ontological step.** This is where the protocol stops. To convert (3) into an
   ontology verdict one must add: *"presentism (or growing block) has exactly one
   admissible realization, and it requires a coupled foliation of this kind"* and
   *"no admissible eternalist realization can carry such a field"*. The second
   premise is false as stated: a block with a dynamical unit timelike vector is a
   coherent eternalist package. So Protocol A changes the model verdict and leaves
   the underdetermination conclusion intact. This is the concrete protocol this
   audit can offer, together with its exact stopping point.

### Protocol B (would break the causal-set equivalence, not the ontology verdict)

Exhibit a physically realizable instrument whose outcome distribution depends on
the growth order or labelling beyond the unlabelled poset — e.g. a detector
reading "how many elements were added before event $x$" in a way not expressible
as a covariant event. Success would scope out the classical equivalence theorem
and create a genuine growth-vs-completed *model* difference, requiring a fresh
admissibility defence for the non-covariant access (condition iv). It would not
create an ontology discriminator, because an embedded observer in a block can
have stage-indexed records; the block reading then predicts the same stage-relative
statistics with a different global story. Verdict: **E → M**, never **O**.

### Protocol C (the only schema that would change the underdetermination verdict)

A protocol changes the ontology verdict only if all four of the following are
independently defended and pre-registered:

1. a formulation of $O_1$ whose stated constitutive commitments **entail** (not
   merely permit) a physical structure $S$ with coupling $g$;
2. a formulation of $O_2$ whose stated commitments entail $\neg S$;
3. a protocol measuring $g$ with a likelihood ratio between the two packages;
4. independent motivation for $S$ under conditions (i)–(iv), assessed against the
   same standard as rivals.

Then a detection or bound on $g$ is a likelihood test between $O_1$ and $O_2$,
and the underdetermination claim fails for that pair. **No candidate in this
table supplies (1) and (2).** Every proposed $S$ — a foliation, collapse noise,
spacetime discreteness, a cosmological arrow, an entropy clock — has at least one
admissible realization in the rival ontology. That is the audit's substantive
finding, and it is a finding about the literature, not a theorem of physics.

A concrete hypothetical shows the shape: if someone proved that presentism
entails a unit timelike vector with a specified nonzero coupling, and that no
eternalist package can include a unit timelike vector, then the existing LAGEOS
bound would already constrain that presentist realization, and a detection at the
predicted $\alpha_1(g)$ would favour it over the eternalist class. The second
conjunct is the weak link, and it is a philosophical claim, not an empirical one.

## 6. Why no protocol in the declared class changes the verdict

This is bookkeeping on the manuscript's definitions, not a new theorem. Write
$\mathcal R(O)$ for the admissible realization class of an ontology, as in
main.tex §2.

**Premises.**
(P1) Empirical discrimination is a difference in $p(D\mid M,e)$ over a declared
protocol class (main.tex §3.2).
(P2) A bridge premise is *probabilistically inert* when it adds no parameters,
changes no state space, and enters no probability assignment. This is the default
for a bridge that says what a model's structures *mean* rather than what they *do*.
(P3, checked per row) In every ontology pair examined, at least one physical model
is shared by an admissible realization of each; column 6 of Table 1 records this.

**Lemma 1.** If $(M,B_1)\in\mathcal R(O_1)$ and $(M,B_2)\in\mathcal R(O_2)$ with
$B_1,B_2$ inert, then $p(D\mid M,B_1,e)=p(D\mid M,B_2,e)=p(D\mid M,e)$ for every
$D,e$. No protocol separates the two packages at those realizations.

**Lemma 2.** If a protocol separates $\mathcal R(O_1)$ from $\mathcal R(O_2)$,
then some model in the support of $\mathcal R(O_1)$ and some model in the support
of $\mathcal R(O_2)$ have different likelihoods. Hence every ontology
discriminator is a model-selection test **plus** an exclusivity claim.

**Corollary.** Given (P1)–(P3) and no exclusivity premise, no protocol in the
declared class changes the underdetermination verdict. The two escapes are the
negations of (P2) and (P3): a bridge that changes the probability law (then the
"ontology" is a physical hypothesis and should be assessed as one), or an
exclusivity premise (then the ontological import rests on that premise, which must
be defended independently).

**Scope.** (P2) is a substantial assumption, not a theorem. A proponent may hold
that a bridge *does* change the law — e.g. that a presentist world assigns zero
probability to records of non-present events. That is testable in principle (our
records would refute it) and no serious defender holds it; but the schema is
available. Lemma 2 also does not say ontology is epiphenomenal; it says the
empirical route runs through model selection and an exclusivity premise. Priors
over realization classes can still differ; the manuscript already rules that a
prior preference is not an empirical likelihood advantage (main.tex lines 235–246).

## 7. Verdicts

1. **Strongest genuine-discriminator candidate: D1 (coupled preferred frame /
   LAGEOS).** It has the three things the others lack: a named model with the
   disputed structure dynamically coupled, an existing precision dataset, and a
   specified signal. It remains a parameter constraint plus a model-selection
   test. Runner-up: **D11** (causal-set growth), the only place where a
   growth-vs-completed difference is even definable; it is currently a proved
   equivalence, and its escape route is an access assumption rather than an
   ontology.
2. **Best-resourced tests:** parameter bounds with current data are D1–D3 and D7;
   model comparisons are D4, D6, D8–D10, D12, D16, several proposed rather than
   performed.
3. **Positive equivalence results:** D5 (relational clocks) and D11 (classical
   covariant growth). These are the rows that most directly support
   underdetermination, and both are scoped to declared model classes.
4. **Category crossings that should not be cited as ontology tests:** D13
   (T violation), D16 (causal order), D17 (discreteness/LIV), D18 (delayed
   choice), D19 (definability read as measurement).
5. **No admissible protocol:** D14, D15, D20, D21.
6. **Bottom line.** The underdetermination conclusion survives the audit, and it
   survives for a structural reason: every proposed discriminator separates
   physical models, and ontologies cut across physical models. The load-bearing
   work is done by the exclusivity premise, which is philosophical, currently
   undefended, and in the one case where it looks tempting (D1) false as stated.

## 8. Defeat search

I searched for prior claims of a decisive empirical test of temporal ontology,
because a claim that "none exists" is itself defeatable. Search capability and
results:

- `serpapi_search` (Google) worked throughout. Queries: `"presentism"
  "eternalism" empirical test underdetermination physics`; `can presentism be
  empirically tested experiment physics philosophy`; `empirical evidence growing
  block universe test observation`; `experimental test openness of the future
  physics ontology`; `temporal ontology empirical equivalence eternalism
  presentism indistinguishable`; `site:philsci-archive.pitt.edu presentism
  empirical test`; `site:arxiv.org physics.hist-ph presentism eternalism empirical
  discrimination`; `"testing presentism" physics`.
- `web-search-prime` (Z.ai MCP) **failed**: `MCP error -429` "Weekly/Monthly Limit
  Exhausted", reset 2026-11-17. Recorded, not worked around silently.
- PhilArchive (`philarchive.org/archive/TREQPPv1`) returned **HTTP 403** behind a
  Cloudflare challenge; unread. A philarchive preprint titled "Quantum Physics
  Prefers the Present" appeared only as a search snippet and is therefore a
  **lead, not a source**; it is not used for any verdict.
- Outcome: no peer-reviewed claim of a decisive experiment surfaced. The results
  were popular, pedagogical, or philosophical. This is a bounded negative search,
  not proof of absence. The stronger basis for §7 is the project's own
  full-text lanes (`knowledge/discriminators`, `knowledge/preferred-foliation`,
  `knowledge/arrow-cosmology`, `knowledge/causal-sets`,
  `knowledge/thermal-records`, `knowledge/clock-interactions`), which had already
  screened these families at the stated depths.
- Nearest prior statement of the conclusion inside the project:
  `research/conclusions/SYNTHESIS.md` §5 ("No experiment in this project
  distinguishes the ontological readings") and §7. This audit does not claim that
  conclusion as new; it adds the P/M/O/E classification, the exclusivity
  argument, and per-candidate decision rules.
- What would defeat this audit: a published argument establishing (1)+(2) of
  Protocol C for some ontology pair, or a demonstration that a bridge premise
  changes the probability law in a defensible formulation. Neither was found.

## 9. Source and read-depth ledger

What this audit actually did, as distinct from what the project's records say.
"Fetched A" means the arXiv abstract page was retrieved on 21 Oct 2026 and title,
authors, journal reference and abstract were read. No PDF of any primary was
downloaded or read by this audit.

| Source | Locator used | This audit |
|---|---|---|
| Lucchesi et al., LAGEOS | PRL 137, 051401 (2026), DOI 10.1103/v88p-965w; arXiv:2501.10588v2 | Fetched A; numerical values inherited from project full-text record and main.tex, not re-read |
| Foster–Jacobson | PRD 73, 064015 (2006), arXiv:gr-qc/0509083 | Project R-A; Eqs. (10)–(12) cited via main.tex; not read here |
| Kostelecký–Vargas | PRD 98, 036003 (2018), arXiv:1805.04499v1 | Project R-F (Secs. II–III, Tables 5–6, 9–10, 13–14); not read here |
| Müller et al. | PRL 99, 050401 (2007) | Project R-A; not read here |
| Zych et al. | Nat. Commun. 2:505 (2011), arXiv:1105.4531 | Fetched A |
| Loriani et al. | Sci. Adv. 5, eaax8966 (2019) | Project R-F (PMC full text); not read here |
| Sorci et al. | PRL 136, 163602 (2026), arXiv:2509.09573v2 | Project R-F (APS full text); not read here |
| Moreva et al. | PRD 96, 102005 (2017), arXiv:1710.00707 | Fetched A |
| Höhn–Smith–Lock | PRD 104, 066001 (2021), arXiv:1912.00033v3 | Fetched A |
| Smith–Ahmadi | Quantum 3:160 (2019) | Project record via main.tex; not read here |
| Chataignier et al. | NJP 28, 034504 (2026), arXiv:2409.06479 | Fetched A |
| Vinante et al. | PRL 119, 110401 (2017) | Project R-A |
| Donadi et al. | Nat. Phys. 17, 74–78 (2021) | Project R-A |
| Dai–Miao–Ma | arXiv:2411.17588 (2025 update) | Fetched A |
| Bassi et al. | RMP 85, 471 (2013) | Project R-A |
| Ahmed et al. | PRD 69, 103523 (2004), astro-ph/0209274 | Fetched A |
| Dowker–Henson–Sorkin (swerves) | MPLA 19, 1829 (2004), gr-qc/0311055 | Fetched A |
| Dowker–Henson–Sorkin (transmission) | PRD 82, 104048 (2010), arXiv:1009.3058 | Fetched A |
| Rideout–Sorkin | PRD 61, 024002 (2000) | Project R-F |
| Brightwell–Luczak | Ann. Appl. Prob. 21, 1493 (2011) | Project record via main.tex; not read here |
| Surya–Zalel | CQG 37, 195030 (2020), arXiv:2003.11311v1 | Project R-F (Thm 2.1, App. B) |
| Wüthrich–Callender | BJPS 68, 907 (2017), arXiv:1502.00018v1 | Project R-F (Secs. 1–5) |
| Goldstein | cond-mat/0105242 | Project R-F |
| Goldstein–Tumulka–Zanghì | PRD 94, 023520 (2016), arXiv:1602.05601v3 | Project R-F |
| Earman | SHPMP 37, 399–430 (2006) | Project R-A |
| Carroll–Chen | hep-th/0410270 | Project R-A |
| BABAR | PRL 109, 211801 (2012), arXiv:1207.5832 | Project R-A |
| Barontini | PRR 8, L022047 (2026), arXiv:2509.07745v2 | Project R-F (Eqs. 1–6, discussion) |
| Connes–Rovelli | CQG 11, 2899 (1994), gr-qc/9406019 | Project R-F |
| van Neerven–Portal | arXiv:2306.13774v2 | Project R-A |
| Procopio et al. | Nat. Commun. 6:7913 (2015), arXiv:1412.4006 | Fetched A |
| Fermi GBM/LAT | Nature 462, 331–334 (2009), arXiv:0908.1832 | Fetched A |
| Kim et al. | PRL 84, 1–5 (2000), quant-ph/9903047 | Fetched A |
| Ma et al. | PNAS 110, 1221–1226 (2013), arXiv:1206.6578 | Fetched A |
| Clifton–Hogarth | Synthese 103, 355–387 (1995) | Project R-F; theorem locators from main.tex |
| Stein | Phil. Sci. 58, 147–167 (1991), pp. 148–150 | Project printed-page verification (`knowledge/audits/stein-printed-pages/`) |
| Malament | Noûs 11, 293–300 (1977) | Project R-F |
| Brading 2013 | Phil. Sci. 80, 1101–1111 (2013) | Project R-F |
| Brading 2015 | SHPSA 50, 13–19 (2015) | Project R-A |
| Rovelli | Found. Phys. 49, 1325–1335 (2019), arXiv:1910.02474 | Fetched A |

## 10. Limitations

- **No primary PDF was read by this audit.** The classification rests on the
  project's existing lane records (whose depths are stated above) plus
  abstract-level verification of 14 primaries. Where a lane record says
  full-text, that is the lane's claim, not a fresh check here.
- **Numerical values** (LAGEOS $\alpha_1$, systematic RSS) are inherited. The
  revision-2 review already flagged that the PRL body and the orbit reduction were
  not independently audited; that limitation is unchanged.
- **Schematic families, not a full taxonomy.** The audit compares the manuscript's
  schematic families (presentism, eternalism, growing block, moving spotlight) and does not
  attempt a full taxonomy of hybrid or deflationary views. A view that defines
  itself by a physical structure (e.g. "presentism just is the aether theory")
  would convert D1 into an **O** trivially — and thereby stop being a distinct
  ontological hypothesis, which is the manuscript's point about labels.
- **Search is bounded.** `web-search-prime` was unavailable (quota); PhilArchive
  blocked; philosophy-of-physics coverage by general web search is poor. No claim
  of absence is made beyond the screened set.
- **No experiment was designed or simulated.** Protocol A is a reading of an
  existing published analysis, not a new proposal; its decision rule is stated at
  the level of the published statistic and would need a full systematics study
  before use.
- **The exclusivity lemma is bookkeeping.** It is a consequence of the
  manuscript's definition plus elementary conditional probability. It is not
  offered as a novel formal result, and the manuscript's own 2026-10-21
  independent review already contains the pieces (matched likelihoods, the
  sufficiency premise, the warning that representation equivalence is not
  ontological identity).

## 11. Unresolved questions

1. **Frame-dependent collapse statistics.** Is there a published calculation of
   velocity-dependent event rates in a foliated collapse model, and do existing
   data bound it? The preferred-foliation lane found none; this is the most
   promising place for a genuine **M** with a foliation signature, and it would
   still need Protocol C's exclusivity premise for **O**.
2. **Causal-set $\Lambda$ phenomenology.** The everpresent-$\Lambda$ proposal makes
   a statistical prediction; a dedicated observational audit (not performed here,
   not covered by `knowledge/causal-sets`) is needed before any model verdict is
   stated.
3. **Definability as constraint.** Can Clifton–Hogarth/Stein/Malament be recast as
   an *exclusion* argument with premises a presentist must accept? The manuscript
   says no without further bridge defence; a full assumption-dependency analysis
   is a separate task (`knowledge/axiomatic-relativity`).
4. **Does any ontology actually carry an exclusivity commitment?** The audit found
   none in the screened literature. A defender may have a version that does; the
   test is whether the commitment is stated as constitutive (condition ii) and
   independently motivated (condition iv), not asserted after the fact.
5. **The "quantum physics prefers the present" preprint.** Blocked (403) and
   snippet-level only. It should be retrieved and read before any claim that the
   literature is uniformly on the underdetermination side.
