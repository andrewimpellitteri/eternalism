# Derivation audit: Nandi & Petruccione, arXiv:2606.08595v1

**Status:** worker submission for independent review, not an accepted conclusion. No
novelty or priority claim is made anywhere in this file.

**Audited object:** Partha Nandi and Francesco Petruccione, *Is Exact Markovianity
Fundamental Once Time Is Relational?*, arXiv:2606.08595v1 (submitted 2026-06-07,
only version, no journal ref; DOI 10.48550/arXiv.2606.08595 verified on the
[abs page](https://arxiv.org/abs/2606.08595)). Source record:
`rmark-nandi-petruccione-2026` in [sources.jsonl](sources.jsonl); earlier
abstract-level records `seed-relational-markov-2026` (seed) and
`frontier-relational-markov-2026` (frontier lane) are reused, not duplicated.

**Read depth:** full text via the LaTeXML HTML build
(https://arxiv.org/html/2606.08595v1), main text plus Supplemental Material.
Equation numbering and content were cross-checked against the MathML `alttext`
attributes of the same build (e.g. Eq. (4) microcausality `(x-y)^2<0`, Eq. (33)
second-order term, Eqs. (34)-(35) greater/lesser correlators, Eq. (42) lesser
factorization), which agree with the visible equation tags. No code reproduced
(task forbids it). Not proof-read against the PDF; page locators not recorded.

**Verdict vocabulary.** *Established* = the displayed text supports the statement
at the stated order/assumptions. *Unclear* = asserted but not derived, or
undetermined by the text. *Contradicted* = the text itself conflicts with the
statement. Labels: **[paper]** = authors' claim; **[std]** = established standard
result/background; **[audit]** = this lane's observation or conjecture.

**Scope guard.** This audit concerns the internal consistency and scope of the
derivations. It does not evaluate temporal ontology. In the project's vocabulary:
the paper's "relational time" is an *operational clock time* (a conditioning
parameter extracted from a quantum clock on hypersurfaces), not a thesis about
eternalism/presentism/growing block; *objective passage*, *determinism*, the
*thermodynamic arrow*, and any new *causal order* are neither assumed nor derived.
Causal order is *presupposed*: microcausality (Eq. 4) and the causal-past domain
`J^-(x) ∩ Ω(Σ_0,Σ)` of Eq. (10) import standard relativistic causal structure.
The conclusion's "exact Markovianity may be incompatible with a fundamentally
relational notion of time" is a claim about the approximation structure of
open-system dynamics under clock conditioning; any bearing on temporal ontology
would need bridge premises the paper does not supply. **[audit]**

---

## Summary table: the four coordinator questions

| # | Question (knowledge/COORDINATOR_REVIEW.md) | Verdict | Key locators | One-line finding |
|---|---|---|---|---|
| 1 | How do main-text instrument Eqs. (5)–(7) and supplemental gated interaction Eqs. (23)–(31) describe the same operation? | **Unclear** (identification asserted, never derived); the main text's *description of its own derivation* is **contradicted** by what the supplement actually does | Eqs. (5)-(7); supplement Eqs. (23)-(31), (44) | The supplement never applies the instrument, never normalizes, never postselects; it evolves with a τ-gated Hamiltonian and takes a plain trace, a different operation for each τ. |
| 2 | Which notion of non-Markovianity does Eq. (10) establish? | **Unclear** — none of the four candidate notions is formulated; at most generator-level time-nonlocality of an O(g²) TCL-type equation is established | Eq. (10) (+O(g³)); supplement between Eqs. (43) and (44); line "Equation (44) is generically non-Markovian…" | No semigroup is defined, no divisibility check, no backflow measure, no multi-time/process criterion; the operative definition is "state depends on causal history through a kernel". |
| 3 | How is normalized postselection distinguished from a linear channel, and what role do state-independent outcome probabilities play? | Acknowledged in one sentence **[established]**; consequences **unclear** (never carried through); outcome probabilities **absent from the text** | Eq. (7) + sentence after it; Eq. (10) (for ρ̃, subnormalized); Eq. (31) (normalized, no postselection) | The paper states the normalized conditioned state evolves nonlinearly, but writes no equation for it; the supplement's route is linear and trace-preserving per τ, where the question is vacuous. |
| 4 | Which statements are second-order/weak-coupling rather than exact for all physical clocks? | **Established** precisely from the text; the interpretive claims inherit the restrictions | Eq. (3) (weak g); Eq. (10) (+O(g³)); Eqs. (14), (15), (16); Eqs. (18), (27), (32), (37), (53) | Every dynamical result is O(g²) under factorized initial state, clock-bath independence, and (for GKLS) secular approximation with σ ≫ τ_B; the AH limit additionally fixes foliation and TT gauge. |

---

## Q1. Main-text instrument (Eqs. 5–7) vs supplemental gated interaction (Eqs. 23–31)

**Verdict: Unclear — the equivalence is asserted, not derived; and the main
text's statement of how Eq. (10) was obtained is contradicted by the
supplement's actual steps.** [audit]

What each construction is:

- **Main text.** Eq. (5) introduces a *quantum clock instrument*
  `J^(σ)_{Σ,τ}: T_1(H_tot) → T_1(H_tot)` that "conditions the total state on the
  relational clock reading τ at the hypersurface Σ", declared "completely
  positive and trace nonincreasing" (text after Eq. 5). Eq. (6) defines the
  conditioned reduced state `ρ̃_{S,τ}[Σ] = Tr_{B,C}[J^(σ)(ρ_tot[Σ])]`, and Eq. (7)
  normalizes it: `ρ_{S,τ} = ρ̃_{S,τ}/Tr ρ̃_{S,τ}`. No Kraus operator or
  measurement-coupling realization of `J^(σ)` is ever given — the word
  "Kraus" does not occur in the paper.
- **Supplement.** Eqs. (23)-(26) replace the bath operator by a clock-*gated*
  composite operator `Ê_α(x;τ) = F_σ(T̂(x) − τ(x)) B̂_α(x)` (τ a c-number
  parameter, `F_σ` a Gaussian response of width σ), i.e. the clock gate is put
  *inside the interaction Hamiltonian density* (Eq. 24). Eqs. (28)-(30) evolve
  the total state with this τ-dependent Hamiltonian via a Dyson expansion to
  O(g³), and Eq. (31) obtains the reduced state by a **plain partial trace**
  `ρ_S^I[Σ;τ] = Tr_Ξ(ρ_tot^I[Σ])` with `Ξ = C ⊗ B`.

Concrete differences the text never bridges **[audit]**:

1. **No instrument is ever applied.** The words "instrument", "postselection",
   "outcome", "Kraus" do not occur in the Supplemental Material (verified by
   string search over the full text). The main text says: "Applying the clock
   instrument and tracing over the bath and clock sectors yields a covariant
   time-convolutionless master equation … (see Supplemental Material)" (before
   Eq. 10). The supplement instead applies *no* instrument: it evolves with a
   modified Hamiltonian and traces. So the main text's account of its own
   derivation does not match the displayed supplemental derivation — a textual
   contradiction, even if a deeper equivalence might be repairable.
2. **Different operations for fixed τ.** Since `F_σ(T̂(x)−τ(x))` acts on `H_C`
   and `B̂_α(x)` on `H_B`, `Ê_α(x;τ)` is Hermitian whenever `B̂_α` is; `h_I(x;τ)`
   is Hermitian; Schwinger–Tomonaga evolution is unitary on `H_tot`; hence the
   map `ρ_tot[Σ_0] ↦ ρ_S^I[Σ;τ]` of Eq. (31) is a **linear, trace-preserving
   channel for each τ**. The main-text route (Eqs. 5-7) is **trace-nonincreasing
   followed by nonlinear normalization**. These are inequivalent operations
   **[std: instruments vs channels]**, and the paper never writes the
   correspondence (e.g. no equation identifies `J^(σ)_{Σ,τ}` with an operator
   built from `F_σ`).
3. **Conditioning vs clock-averaging.** The main text conditions on a specific
   reading τ (Page–Wootters-style); the supplement's Eq. (31) *traces over the
   clock*, and the clock enters only through state expectation values
   ⟨F_σ(T̂(x)−τ(x)) F_σ(T̂(y)−τ(y))⟩_C (Eqs. 36, 39). Different clock states
   `ρ_C` give different kernels; no reading is postselected. Also, the main
   text conditions at a hypersurface with a single label τ (Eq. 5), while the
   supplement uses a spacetime *function* τ(x) inside the gate (Eqs. 23, 30, 36).
4. **What the supplement does establish** (at displayed-derivation level, to
   O(g²)): the composite correlator factorizes,
   `W^>(x,y;τ) = χ_σ(x,y;τ) G_{αβ}(x,y)` (Eqs. 36-41; lesser version Eq. 42),
   *given* clock-bath statistical independence (Eq. 37); and it notes the
   factorization `W = χ_σ G` breaks down when clock and bath share microscopic
   degrees of freedom (Eq. 43 and surrounding text). That reproduces the kernel
   Eq. (11)/(20)/(45). This algebraic step looks correct as written **[audit]**;
   minor presentation inconsistency: the supplement's Eq. (40) defines `G` with
   Schrödinger-picture `B̂_α(x)`, while the main text's Eq. (12) defines the same
   symbol with interaction-picture `B̂^I` (and supplement Eq. 36 similarly drops
   the `^I` that Eq. 34 carries).
5. **The bridging assertions** are: supplement opening — "This supplemental
   material derives the relational memory kernel appearing in Eq. (11) of the
   main text from a microscopic system—a clock-bath model" — which is accurate
   *for the kernel* but silently replaces the instrument by a gated Hamiltonian;
   and the main-text "Applying the clock instrument …" sentence quoted above,
   which is not what the supplement does.

So: the *kernel* derivation has displayed support; the *instrument/postselection
structure* of Eqs. (5)-(7) has no microscopic realization anywhere in the paper.
Whether the two describe "the same operation" is undetermined by the text.

## Q2. Which notion of non-Markianity does Eq. (10) establish?

**Verdict: Unclear — none of the four precise notions (semigroup failure,
CP-indivisibility, information backflow, multi-time process criterion) is
formulated or established. What the text establishes is generator-level
time-nonlocality of an O(g²) TCL-type equation for the *subnormalized* state.**
[audit]

Textual facts:

- Eq. (10) is local in the *current* state: `δρ̃^I_{S,τ}[Σ]/δΣ(x)` = an integral
  over the causal past `J^-(x) ∩ Ω(Σ_0,Σ)` of commutators involving
  `A^I_β(y)` and the **same-hypersurface** state `ρ̃^I_{S,τ}[Σ]`, with `+O(g³)`.
  The paper itself calls it "a covariant time-convolutionless master equation"
  (before Eq. 10). Nonlocality lives in the *generator* (the dressed kernel
  `C^(σ)(x,y;τ) = χ_σ G_{αβ}`, Eq. 11), not in the state argument.
- The operative definition in the paper: "Equation (44) is generically
  non-Markovian because the conditioned state at the spacetime point x depends
  on the causal history encoded in the dressed relational kernel."
  (supplement, after Eq. 46). That is a statement about *kernel nonlocality of
  the generator*, i.e. departure from instantaneous (delta-kernel) dissipation.
- Not present anywhere (verified by full-text search): a two-parameter family of
  conditioned maps `Λ(Σ_2,Σ_1)` and a composition law (so *semigroup failure* is
  never stated as such — although the generator's dependence on the absolute
  initial hypersurface via `Ω(Σ_0,Σ)` would obstruct a semigroup structure, the
  paper never formulates this); construction of intermediate maps and a
  positivity check (*CP-indivisibility* is never mentioned; "divisibility" does
  not occur in the paper); a trace-distance or similar backflow measure on the
  normalized state (*information backflow* never mentioned); any process tensor,
  multi-time state, or consistency condition for higher-order correlation
  functions (*multi-time criterion* absent). The RMP colloquium the paper cites
  as [2] (Breuer–Laine–Piilo–Vacchini) is used only as introduction-level
  background; none of its definitions is adopted.
- The step producing the TCL form is asserted, not derived: "Promoting the
  perturbative expansion to a local-in-state time-convolutionless form yields"
  (supplement, between Eqs. 43 and 44). The intermediate manipulations (Born-type
  factorization, replacement of the state inside the integral by the current
  one) are not displayed; this is TCL2-level material, and its validity domain
  (weak coupling, short times, slowly varying states) is not restated there.

Comparison at abstract level (see [sources.jsonl](sources.jsonl) for records):

- **Chruściński, "Dynamical maps beyond Markovian regime" (arXiv:2209.14902v1,
  abstract read).** The review's abstract organizes the field into positive/CP
  semigroups, time-local generators, non-local memory kernels, and
  divisibility-based definitions (CP- vs P-divisibility), plus
  "Markovianity beyond the dynamical map". Within that taxonomy, the audited
  Eq. (10) sits in the *non-local memory kernel / time-local-generator* slot and
  does not engage the divisibility distinctions. Since kernel nonlocality, P- or
  CP-indivisibility, and backflow are inequivalent notions **[std, per that
  review's framing]**, the paper's "generically non-Markovian" label is
  under-specified: the displayed result supports at most "not of GKLS
  instantaneous form", not any of the sharper criteria.
- **Nestmann–Bruch–Wegewijs, PRX 11, 021041 (arXiv:2002.07232v2, abstract
  read).** NBW show Nakajima–Zwanzig kernel and TCL generator descriptions of the
  *same* evolution are connected by a fixed point `G = K̂[G]`, and that Markov
  approximations and semigroup factorization are subtle (the stationary
  generator is not the kernel's low-frequency limit). Relevance: (i) the
  presence of a kernel-shaped generator does not by itself fix which Markovian
  property fails — one must analyze the induced maps; (ii) the audited paper's
  one-sentence TCL "promotion" is exactly the kernel→generator step NBW treat
  nonperturbatively; the audited paper's Eq. (44)/(10) generator is
  kernel-shaped, and its consistency as an exact TCL generator beyond O(g²) is
  unanalyzed in the paper.
- **[audit] consequence for interpretation:** the paper's headline "exact
  Markovianity is effective rather than fundamental" is, at derivation level, the
  statement that the O(g²) conditioned generator contains a non-delta temporal
  kernel. Which operational consequence (irreversibility of intermediate maps,
  backflow of distinguishability, incompatibility of multi-time statistics) that
  entails is not established in the text.

## Q3. Normalized postselection vs linear channel; outcome probabilities

**Verdict: the distinction is explicitly acknowledged in one sentence
[established]; its consequences are never carried through [unclear]; outcome
probabilities are entirely absent from the text [established absence].** [audit]

- The paper states, immediately after Eq. (7): "Complete positivity therefore
  applies at the level of the conditioned map and subnormalized state, while the
  normalized conditioned state evolves nonlinearly due to relational
  conditioning." This matches the standard fact that a postselected instrument
  outcome gives a nonlinear state map `ρ ↦ Φ(ρ)/Tr Φ(ρ)` **[std]**. The paper
  also motivates linearity of the *microscopic* layer: "the present framework
  preserves linear covariant microscopic evolution, with non-Markovianity
  emerging only after relational conditioning and subsystem reduction"
  (Introduction).
- However, **every displayed dynamical equation is for the subnormalized
  `ρ̃`**: Eq. (10) and Eq. (44) evolve `ρ̃^I_{S,τ}`. No equation of motion for
  the normalized `ρ_{S,τ}` of Eq. (7) is ever written; the extra nonlinear terms
  generated by differentiating the normalization denominator are never computed.
  Since the normalized state is what an observer following Eq. (7) would
  propagate, the paper derives dynamics for an auxiliary object and interprets
  it as the physical one **[audit]**.
- **Outcome probabilities.** The denominator `Tr ρ̃_{S,τ}[Σ]` — which for the
  instrument of Eq. (5) is the outcome probability `p(τ|Σ)` — never appears in
  any displayed equation, and no property of it (state-dependence, positivity
  domain, dynamics) is derived; the words "outcome" and "postselection" do not
  occur in the paper. The coordinator's probe about *state-independent* outcome
  probabilities therefore has a crisp textual answer: the concept is absent.
  Note the mathematical hinge **[audit, std]**: normalized postselection
  `ρ ↦ Φ(ρ)/Tr Φ(ρ)` is a linear channel *exactly when* the outcome probability
  is independent of the input state; since the text never evaluates
  `Tr J^(σ)(ρ)`, it never determines whether its conditioned dynamics is
  genuinely nonlinear or secretly linear.
- **The supplement is on the linear side.** Its per-τ map (Eq. 31) is linear and
  trace-preserving (see Q1, item 2), so there `Tr ρ_S^I[Σ;τ] = 1` and the
  normalization of Eq. (7) would be vacuous. I.e., the derivation route that
  actually produces the kernel corresponds to the *linear-channel* case, not to
  the postselected case the main text announces. This sharpens Q1: the two
  constructions differ precisely on the point Q3 asks about.

## Q4. Which results are second-order / weak-coupling?

**Verdict: Established — the text itself fixes the order and the additional
assumptions of each result; the interpretive claims inherit those restrictions,
which the Conclusion does not always restate.** [audit]

- **All dynamical results are O(g²) in a weak coupling.** `g` is introduced as
  "a weak subsystem–environment coupling constant" (after Eq. 3). Eq. (10)
  carries an explicit `+O(g³)`; the supplement's Eq. (30) is likewise to O(g³)
  and Eq. (33) is explicitly the second-order term `ρ_{S,(2)}^I`, with the first
  order killed by vanishing one-point functions (Eq. 32). This is TCL2/Born-type
  material **[std]**; no nonperturbative or resummed result appears.
- **Structural assumptions beyond g²:** initially factorized state (Eq. 27);
  clock-bath statistical independence (Eq. 37), without which the paper itself
  says the factorized kernel `W = χ_σ G` breaks down (Eq. 43 and text after);
  TCL promotion asserted (supplement, before Eq. 44).
- **The GKLS limit (Eq. 16) needs a further chain:** a smooth timelike clock
  flow `u^μ(x)` (Eq. 13); scale separation `σ ≫ τ_B` (Eq. 14); approximate
  stationarity plus *local secular approximation* (Eq. 15 and text); extension
  of the memory integral to infinite relational time (text before Eq. 16);
  and positivity of the rates only "if the dressed kernel is of positive type"
  (text after Eq. 17) — i.e., even the emergent GKLS claim is conditional, and
  the secular approximation is known to be a stronger requirement than weak
  coupling in some systems **[std; the paper cites Trushechkin PRA 103, 062226
  (2021) as its ref. 23]**.
- **The AH limit (Eqs. 19, 61) needs:** Minkowski spacetime with fixed
  `t = const` foliation; the sharp-clock limit (Eq. 18 / Eq. 54); and
  specialization to the TT-gauge matter–graviton coupling (Eq. 53). The
  resulting equation is second order in `κ` in structure (noise/dissipation
  kernels are graviton two-point functions; the nonunitary terms are
  `O(κ)`-prefactored integrals of two-point kernels appearing at the same
  displayed order as Eq. 10's `g²` term). Whether it equals the AH equation
  operator-by-operator was **not verified** (AH read at abstract depth only;
  recorded as an open question in sources.jsonl).
- **Scope of the headline claims.** "Generically non-Markovian even for local
  interactions" holds within the stated model class (local product coupling
  `A_α ⊗ B_α`, factorized initial state, independent clock, finite σ, O(g²)) —
  it is not an exact theorem about all physical clocks, and the paper does not
  claim it as one in the derivation sections. The Conclusion, however, shifts
  register: "demonstrating that temporal nonlocality is not merely a consequence
  of environmental complexity" (unhedged) and "may be incompatible with a
  fundamentally relational notion of time" (hedged) — both beyond what an O(g²)
  TCL2 computation in one model class can demonstrate **[audit]**.
- **Internal tension (minor, caption-level):** Fig. 1's caption says
  "Conventional Markovian evolution emerges only after relational coarse-graining
  *and in the sharp-clock limit* where clock fluctuations become negligible." But
  the sharp-clock limit produces the AH-type equation (Eqs. 19, 61), which
  retains a memory integral `∫_0^t ds` and is not of GKLS semigroup form; the
  AH section itself only claims recovery of "an effectively classical notion of
  time". The caption conflates emergence of coordinate-time *descriptions* with
  emergence of *Markovian* dynamics **[audit]**.

---

## Conceptual placement (per project research standards)

- **Temporal ontology:** untouched by the derivations. The paper's premise "no
  preferred notion of time exists fundamentally in relativistic physics"
  (abstract) is a statement about absence of preferred foliation/parameter, not
  a settled ontological thesis, and the results do not select eternalism,
  presentism, growing block, or moving spotlight.
- **Objective passage:** not modeled; "operational time" is a conditioning
  parameter, not a becoming ontology.
- **Determinism:** irrelevant to and untested by the results; conditioned
  nonlinear state maps do not by themselves bear on determinism of the
  underlying linear ST evolution (which the paper preserves).
- **Causal order:** presupposed, not derived — microcausality (Eq. 4) and the
  causal-past domain in Eq. (10) import standard relativistic structure.
- **Clock time:** the paper's actual subject — a finite-resolution conditioning
  parameter from a quantum clock sector; the finite-resolution smearing `χ_σ`
  is the only genuinely "relational" ingredient in the kernel.
- **Thermodynamic arrow:** not addressed; no entropy production or
  thermodynamic arrow statement is derived (GKLS dissipativity appears only as
  a conditional coarse-grained limit).

## Nearest predecessors and what would defeat the audit verdicts

No novelty claim is made here; the following are the closest works this audit
leaned on, and what would overturn the verdicts above:

1. **Chruściński, arXiv:2209.14902** (review; abstract read): the
   semigroup/divisibility/backflow taxonomy. *Defeats Q2's "unclear" verdict:*
   a section of the audited paper (or a revision) that constructs the
   conditioned map family and certifies CP-indivisibility or a backflow measure
   for it would reclassify the result; conversely, if a reader can show the
   paper's kernel generator is CP-divisible as it stands, the paper's headline
   weakens, not strengthens.
2. **Nestmann–Bruch–Wegewijs, PRX 11, 021041** (abstract read): kernel ↔ TCL
   generator fixed point. *Defeats:* an exact kernel→generator analysis showing
   the audited Eq. (10)/(44) generator is or is not a valid fixed point beyond
   O(g²) would settle what the TCL promotion left asserted.
3. **Gambini–Porto–Pullin PRL 93, 240401 (2004)** (paper's ref. 8; not read
   here) and the Page–Wootters line (refs. 19, 20): finite-clock-resolution
   decoherence and conditional dynamics are established prior art; any claim
   that "clock fluctuation induced memory" is new would need to beat these. This
   audit makes no such claim.
4. **Anastopoulos–Hu, CQG 30, 165007 (2013)** (abstract read): the claimed
   limiting case. *Defeats Q4's conditional finding:* an operator-level match of
   audited Eq. (61) with the AH equation would confirm the AH recovery; a
   mismatch (ordering, kernel definitions, sign of the dissipation term) would
   contradict the paper's consistency check.
5. **Any v2 of the audited paper** that (a) gives the Kraus form of `J^(σ)` and
   derives it from the gated Hamiltonian, (b) derives the normalized-state
   master equation and its outcome probability, and (c) states a precise
   non-Markovianity criterion with proof, would dissolve the Q1-Q3 "unclear"
   verdicts. This audit is of v1 only.

## Limitations of this audit

- HTML (LaTeXML) build of v1 only; PDF not opened; page-level locators not
  recorded; a conversion artifact is conceivable but equations were cross-checked
  against MathML alttext and read coherently.
- The audit inspects displayed equations and surrounding prose; the algebra
  between Eqs. (33) and (44) (TCL promotion) was *assessed*, not re-derived, and
  nothing was numerically or machine verified (no reproduction, per task).
- Comparison papers (Chruściński; Nestmann–Bruch–Wegewijs; Breuer–Laine–Piilo–
  Vacchini; Anastopoulos–Hu) were read at abstract depth only — sufficient per
  the task ("at the abstract level at least") but their section-level criteria
  were not extracted; nothing below rests on their internals.
- The Chruściński landing page shows no journal reference; if a published review
  version exists, the arXiv v1 record here should be updated after verification.
- One page fetched during the Anastopoulos–Hu identifier search
  ( fetzer-franklin-fund.org EMQM slide/PDF page ) was seen only as a search
  snippet and is **not** counted as read.
