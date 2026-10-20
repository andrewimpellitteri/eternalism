# RC-1 neighbours at full text: interacting and non-ideal clocks

Status: 2026-10-20. Lane `kb-clock-interactions`, completed by a Claude subagent after the
GLM worker stopped on a provider quota. This is a reading audit, not a novelty claim.
Source records: `sources.jsonl` in this directory, plus two existing records reused by id
(`frontier-relational-trinity-2019v3`, `frontier-smith-ahmadi-interacting-2019`).

## Question

The RC-1 case recorded in `knowledge/defeat-search/fulltext-reads-clocks.md` and the
contracts crosswalk: a finite-dimensional `Z_N` clock with a non-ideal covariant POVM and
a clock-system coupling with `[H_int, H_C] != 0`. Do the three trinity reductions agree?
The three are relational Dirac observables, Page-Wootters (PW) conditioning, and the
relational Heisenberg picture by quantum symmetry reduction. Does any of the papers below
answer that case or a strict superset of it?

## Short answer

None of the five named papers answers it, and neither does a strict superset. The same
holds for the periodic-clock trinity paper 2409.06479, read only at abstract depth plus
located passages. Every paper that compares pictures assumes no interaction. Every
paper that has an interaction stays in the PW picture, or in Rijavec's case a formal
unitary "Heisenberg picture" that is not the trinity's symmetry reduction. Each also
either restricts the interaction to commute with the clock Hamiltonian or works one
example. Smith-Ahmadi's qubit-clock example is the one worked case inside the
`[H_int, H_C] != 0` class. There the interaction annihilates the physical subspace, so
the case is degenerate. See the check below.

## Per-paper table

| Paper (id, version) | Interaction class | Clock | Physical inner product | Pictures | Proved vs illustrated | Answers RC-1? |
|---|---|---|---|---|---|---|
| Höhn, Smith, Lock 1912.00033v3 (`frontier-relational-trinity-2019v3`) | None. Constraint `C_H = H_C + H_S` (Eq. 4) | Covariant POVM, non-ideal allowed. Equivalence proved only for non-degenerate continuous-spectrum (noncompact) clocks. Periodic clocks deferred to [84] | Group-averaging inner product (Eq. 26). PW inner product (Eq. 38) shown equal (Corollary 1) | Dirac, PW, relational Heisenberg | Theorems 1-6, proofs in App. C (not re-checked here) | No. Interaction is named "the most pressing generalization" (Sec. IX) |
| Chataignier, Höhn, Lock, Mele 2409.06479v3 (`clockint-periodic-clocks-2024`, abstract + passages) | None (Sec. II.2) | Periodic, U(1)-covariant POVM. Includes a finite-dimensional two-level non-ideal clock (Ex. 6) | Not read | All three, per abstract claim (3) | Claimed in abstract. Theorems unread | No. Gives the uncoupled periodic baseline |
| Smith, Ahmadi 1712.00081v3 (`frontier-smith-ahmadi-interacting-2019`) | General `H_int` in the kernel equation (Eq. 14). Worked: `f(T) (x) S` (Eq. 20), `H_C (x) H_S` gravity (Sec. 4.2), qubit `a(XX-YY)+b(ZZ+II)` (Eq. 24) | Ideal `L^2(R)` clock for Exs. 1-2. Qubit periodic non-ideal covariant clock for Ex. 3 | Chosen conditional inner product (Eq. 11), with t-independence demanded (Eq. 12, footnote 1) | PW only | Kernel equation and norm condition derived (Eqs. 13-15). Examples illustrative | No. PW only. Ex. 3 is a degenerate member of the class |
| Rijavec 2204.11740v3 (`clockint-rijavec-pw-robustness-2023`) | Only `[H+h, V] = 0` and `[h, V] = 0` (Eqs. 47-48), hence `V = X (x) h`, `[X,H]=0` (Eq. 51) | Ideal, `[t,h]=i`, projective readings (footnote 7). One uncoupled qubit-clock example | PW conditional scalar product (footnote 3). Mixed-state normalization t-independent "due to Eqs. (1) and (7)" (footnote 4) | PW and a formal unitary picture change (Eq. 11). No Dirac comparison except a group-average remark (App. A.1) | Explicit derivations. Examples illustrative | No. The opposite regime. The non-commuting case is left open (Sec. VII) |
| Mendes, Brito, Soares-Pinto 2107.11452v1 (`clockint-mendes-quasi-ideal-2021`) | `H_I = -G H_S (x) H_C` (Eq. 20), which commutes with `H_C` | Finite d-dimensional quasi-ideal clock on a Z_d time basis. Only approximately covariant | Not stated | PW only | Perturbative and approximate. Lemma 1 bounds clock error | No |
| Garmier, Hausmann, Castro-Ruiz 2512.19343v2 (`clockint-garmier-nonideal-qrf-2026`) | None. Global action is a product `U_A (x) U_S` (Sec. II) | Any covariant POVM, non-ideal. Explicit for Abelian G with rank-one POVMs, finite Abelian groups included (App. F) | Not a constraint framework. Restricting to `r=0` gives perspective-neutral reduction maps (Prop. 16) | Kinematic perspectives only, no dynamics | Theorem 1 (rigorous for finite dim., compact G). Proofs in appendices, not read here | No. Kinematics only |

## Verbatim findings with locators

Prose is quoted verbatim from the arXiv HTML. Inline mathematics is transcribed from the
HTML's LaTeX alt-text into plain notation, so symbols are faithful but not typographically
identical.

### Höhn, Smith, Lock, arXiv:1912.00033v3 (PRD 104, 066001), reread of passages

- Sec. II.2, after Eq. (4): "That is, we assume that the clock and system do not interact."
- Sec. II.2: "(see [50] in which this assumption is relaxed in the context of the
  Page-Wootters formalism)". Ref. [50] is Smith-Ahmadi, Quantum 3, 160 (2019).
- End of Sec. III.2.3: discrete-spectrum clocks are discussed "in detail in the context of
  relational quantum dynamics in [84], henceforth considering only noncompact clocks."
  Sec. V.1.1 repeats: "(recall that we have restricted to noncompact clocks for the
  remainder)". Ref. [84] is Chataignier, Höhn, Lock, "in preparation (2021)". It appears
  to be the later 2409.06479 (identification by authors and topic only).
- Sec. V.3: "This completes the proof of the formal equivalence of the three elements of the
  trinity of relational quantum dynamics depicted in Fig. 3 for clock Hamiltonians with
  non-degenerate and continuous spectrum."
- Sec. V.2.1, Lemma 2, Eq. (47): the trivialization map `T_T` of Eq. (45) satisfies
  `T_T C_H T_T^{-1} = (H_C - eps_*) (x) I_S`. The construction uses the separable form
  of `C_H`. This is our reading of why interactions are outside this proof route.
- Sec. IX: "the most pressing generalization of our work is to explore the validity of the
  trinity in the context of interactions between the chosen clock and the evolving system."
  The same section continues: "As shown in [50], certain interactions will lead to a
  modified Schrödinger equation in the Page-Wootters formalism, which still generates an
  isometry."
- App. A argues that interaction-free partitions are impossible for non-integrable
  (generic) systems. This is the authors' argument, not a theorem.

Proposed correction to the existing record (not edited here): its `assumptions` field
says the spectral cases were "developed for non-degenerate continuous/discrete spectra".
Discrete-spectrum clocks are described in Sec. III.2.2. The trinity theorems are proved
only for noncompact, continuous-spectrum clocks.

### Chataignier, Höhn, Lock, Mele, arXiv:2409.06479v3 (NJP 28, 034504 (2026)), passages only

- Sec. II.2: "we shall henceforth assume that no interactions between C and S are present.
  While we are therefore not covering the general case, we will be able to prove many
  explicit results which would be rather challenging in the presence of interactions".
  Also: "interactions, unless fine-tuned, would typically ruin the periodicity of the
  dynamics."
- Abstract, claim (3): the trinity holds relative to periodic clocks, "implying that the
  dynamics in all three is necessarily periodic". Claim (4): the original PW definition of
  conditional probabilities "fails for systems that have a continuous energy spectrum".
- Sec. III, before Ex. 6: "the formalism of periodic, covariant POVMs encompasses both
  infinite-dimensional and finite-dimensional quantum clocks". Ex. 6 is a two-level clock.
  Its footnote says the clock states are "not all orthogonal/perfectly distinguishable.
  That is, the clock is not an ideal reference frame."
- Unread: whether a Z_N-covariant POVM with discrete readings is covered as a special
  case, and the theorem statements themselves.

### Smith and Ahmadi, arXiv:1712.00081v3 (Quantum 3, 160), reread in full

- Eq. (5): `(H_C (x) I_S + I_C (x) H_S + H_int)|Psi>> = 0`, with `H_int` general (Sec. 2,
  item 1).
- Eq. (14): `i d/dt |psi_S(t)> = H_S|psi_S(t)> + ∫dt' K(t,t')|psi_S(t')>` with
  `K(t,t') = <t|H_int|t'>`. The derivation inserts the clock resolution of identity
  `I_C = ∫dt |t><t|` (Sec. 3.1). Clock states only need to be covariant and to resolve the
  identity (below Eq. 8), so the equation is not limited to ideal clocks.
- Eq. (11) and footnote 1: the physical inner product is chosen as
  `<<Psi|(|t><t| (x) I_S)|Phi>>` and "demand that the inner product is independent of the
  choice of t". Footnote 1: "this is a choice of inner product and normalization of the
  physical states, which may severely reduce the size of the physical Hilbert space."
- Below Eq. (15): Eq. (15) "is equivalent to demanding that the physical inner product is
  independent of t".
- Sec. 4.3: qubit clock `H_C = Ω σ_z`, clock states `e^{-iH_C t}|+>`, resolution
  `I_C = (Ω/π)∫_0^{2π/Ω} dt' |t'><t'|`, and `H_int = a(σx⊗σx − σy⊗σy) + b(σz⊗σz + I⊗I)`
  (Eq. 24). Conclusion: "the coupling ... has no effect on the relational dynamics".
  Sec. 5: "an interaction between the clock and system doesn't necessarily modify the
  relational dynamics".
- Sec. 5 lists as future work: "replacing the infinite dimensional clock Hilbert space with
  a finite dimensional one", and generalizing to mixed states.

Our exact check (`sa_example3_check.py`, standard library) gives:
- `||[H_int, H_C ⊗ I]|| = 0.868 != 0`;
- `H_int|10> = H_int|01> = 0`, and the null space of `H` is exactly `span{|01>,|10>}` for
  the generic parameters tested;
- the conditional state equals `exp(-i H_S t) psi(0)`. The paper prints `e^{iH_S t}` in
  Eq. (26), which looks like a sign typo and does not affect the conclusion.

So Ex. 3 is a finite, periodic, non-ideal, covariant clock with `[H_int, H_C] != 0`. But
`H_int Π_phys = 0`, so the interaction never acts on physical states, and the case is
degenerate. It treats only the PW picture.

### Rijavec, arXiv:2204.11740v3 (PRD 108, 063507), read in full

- Footnote 7 (Sec. III): "the time measurements in [22, 20] are represented, in general, by
  a POVM while I restrict, for simplicity, to projective measurements."
- Sec. V.1, Eq. (47): "I will only consider interactions V such that
  [H⊗1_C + 1_S⊗h, V] = 0". Eq. (48): "[1_S⊗h, V] = 0. This is the same as requiring that
  dV/dt̂ = 0, that is, t̂ must not appear in V."
- Eq. (51): "all the allowed system-clock interactions are of the form: V = X⊗h, where X
  is a self-adjoint operator of the system such that [X, H] = 0."
- After Eq. (59): "If Eq. (49) does not hold, the effective Hamiltonian will be, in general,
  non-self-adjoint [40]." Ref. [40] is Paiva et al., Commun. Phys. 5 (2022).
- Sec. V.4: "if V does not commute with h — that is, t̂ appears in V — then the effective
  Hamiltonian of the system will be time-dependent [15]." Ref. [15] is Smith-Ahmadi.
- Sec. V.3 after Eq. (70): "if the state of the universe consists of eigenstates of H with
  different eigenvalues, the evolution of the system is no longer unitary overall".
  Footnote 21: the map "preserves the positivity and the trace". With equal `ρ_k(0)` it is
  "the CPTP map ... with Kraus operators B_k(t) := sqrt(p_k) e^{-iH_eff(E_k)t}".
  Footnote 22: "For a different kind of non-unitarity due to a non-ideal clock see [41]".
  Ref. [41] is Mendes et al.
- Sec. VII, last paragraph: "it would be interesting to consider interactions such that t̂
  is not left invariant when moving from the Schrödinger picture to the Heisenberg
  picture. ... I leave this problem open for future investigations."

The paper's "Heisenberg picture" is the formal kinematical unitary `exp(-i H⊗t̂)`
(Eq. 11). It is not the trinity's constraint trivialization with gauge fixing, and the
paper makes no Dirac-observable equivalence claim for the interacting case.

### Mendes, Brito, Soares-Pinto, arXiv:2107.11452v1, read in full

- Sec. III, Eq. (12): the quasi-ideal clock is "a coherent superposition of time states"
  `|θ_k>`, the Z_d Fourier basis of the SWP clock (Eqs. 9-11).
- Eq. (13): `e^{-iH_C t}|ψ_QI(k_0)> = |ψ_QI(k_0 + td/T)> + |ε>`. The error norm is
  "exponentially small with dimension".
- Eq. (20): `H_I = −𝔾 H_S ⊗ H_C`. This commutes with `H_C`.
- Sec. V after Eq. (25): "the interaction between clock and system state does not induce a
  non-unitary behavior in the evolution of the system state, provided that Eq.(23) holds."
- After Eq. (35): "in Eq.(33) there are two new terms, the second and the third ones, both
  dependent on the initial system state ρ_S(0). Given the dependence on initial conditions
  this shows that this equation of motion is non-linear in nature".
- Sec. V end: "the non-unitary and non-linear effects arise due to the non-ideal nature of
  the chosen clock model".
- App. A: the QIC POVM is covariant only "in the limit of large dimension"
  ("approximately").

Our reading, labelled as such: `V` in Eq. (52) is defined with the conditioned state
`|ψ_S(τ)>_e` inside it, while the conditioning in Eq. (15) is linear in the global state.
The derivation therefore does not show that the map `ρ_S(0) → ρ_S(τ)` is non-linear.
App. A also builds the global state from the non-interacting expansion (Eqs. 36-37), and
we did not find where the interaction-modified constraint is imposed on it.

### Garmier, Hausmann, Castro-Ruiz, arXiv:2512.19343v2, main text and App. I read

- Sec. II, footnote 2: "G is taken to be a finite-dimensional, unimodular Lie group, where
  discrete groups are included as Lie groups of dimension zero". The global action is
  `Û^{|L} := Û_A ⊗ Û_S` ("G-Invariant Operators").
- Sec. II after Theorem 1: the theorem "holds rigorously if dim H^{|L} < ∞ and if G is
  compact".
- Sec. IV, Eq. (25): `R_A[A_S] R_A[B_S] ≠ R_A[A_S B_S]` in general. Equality for all `S`
  "requires" orthogonal orientation POVM elements, "which implies that A must be ideal."
- Sec. V, periodic clock: "In this case, the time evolution of S:A|A behaves as if A were an
  ideal clock. Conversely, for general states with support on 'high energy' sectors,
  deviations from ideal time evolution will be detected from the perspective of A." No
  Hamiltonian, constraint or equation is given for this statement.
- Sec. VI: "It is interesting future work to study more concretely when these phenomena
  occur and what their dynamical causes are."
- App. I, Proposition 16: "we can mathematically think of the perspective-neutral approach
  as our approach restricted to r = 0".

## Bearing on RC-5: does an interacting finite clock produce reading-dependent memory?

1. **No source computes divisibility, backflow, or process-tensor memory for any
   interacting clock-conditioned map.** Smith-Ahmadi, Rijavec and Mendes report
   non-locality, non-unitarity or "non-linearity". None uses a memory criterion.
2. **Smith-Ahmadi's isometry condition is load-bearing.** With interaction, the PW map is
   norm-preserving only if `<<Ψ|(|t><t|⊗I)|Ψ>>` is independent of t (below Eq. 15). The
   paper demands this and does not derive it. Our conjecture, not a paper's claim: when
   `[H_int, H_C] != 0`, the clock-reading marginal of a physical state need not be uniform
   in the reading. In RC5's uncoupled `Z_N` check that marginal is constantly `1/N`. If it
   is non-uniform, normalized conditioning becomes reading-dependent and state-dependent.
   This is the most direct mechanism for RC-1/RC-5 effects, and the exact `Z_3` example in
   RC5 should compute this marginal first.
3. **Rijavec shows a second route to non-unitarity that does not need `[H_int, H_C] != 0`.**
   It uses a commuting interaction `V = f(H)⊗h` with a stationary mixed universe state
   spread over several total-energy eigenvalues (Eq. 70). In his two-sector qubit model
   (Eq. 90) our check `rijavec_backflow_check.py` gives a trace distance between the
   images of `|0><0|` and `|1><1|` equal to `|cos(θ/2)|`, with `θ` linear in t. That is
   non-monotone, so there is information backflow and the family is not CP-divisible.
   This is our consequence, not the author's claim. Rijavec states only the
   maximally-mixed time τ_D (Eq. 91). The route needs the universe state off a single
   constraint surface. On a single eigensector the evolution is unitary (Eq. 58).
   **Implication for RC5.md:** its sentence "requires either a clock–system interaction
   with `[H_int, H_C] ≠ 0` … or a non-covariant, degrading clock POVM" holds only if
   the state is restricted to one constraint surface (`H|Ψ>> = 0`). That premise should be
   stated, or Rijavec's mixed-sector route added as a third option.
4. **Mendes et al. attribute non-unitary, initial-state-dependent terms to clock error.**
   Their clock is only approximately covariant and their interaction commutes with `H_C`.
   The finding sits under RC5's "non-covariant POVM" branch. Its "non-linearity" is not
   established by the derivation; see above.

## Narrowest unaddressed case after this lane, and what would defeat it

Refined case: a finite-dimensional clock with an exactly `Z_N`-covariant non-ideal POVM,
a single constraint surface `(H_C + H_S + H_int)|Ψ>> = 0`, and an `H_int` with
`[H_int, H_C] != 0` whose compression to the physical subspace is non-trivial. This
excludes Smith-Ahmadi Ex. 3, where `H_int Π_phys = 0`. The question is whether the
Dirac, PW and relational-Heisenberg reductions agree, and under which inner product.

This is not shown to be open. The reads or searches most likely to defeat it:
1. 2409.06479v3 in full (periodic trinity). Check whether discrete `Z_N` readings and any
   interacting remark appear beyond Sec. II.2.
2. Cafasso et al., PRD 110, 106014 (2024), arXiv 2407.00161. This is a finite-dimensional
   interacting PW model, unread.
3. Forward citations of Smith-Ahmadi 1712.00081 and of the trinity, using a citation
   database (Semantic Scholar or INSPIRE). This lane ran only two general web searches.
4. Paiva, Te'eni, Peled, Cohen, Aharonov, Commun. Phys. 5 (2022), Rijavec's ref. [40]:
   non-self-adjoint effective Hamiltonians for interactions outside his class. Unread.
5. Ludescher et al. 2607.24976 App. B (already read by another subagent). Its interacting
   example commutes with the clock generator.
6. Singh-Friedrich 2304.01263 (abstract only). Its interaction class needs confirming.

## Distinctions kept

Everything here concerns clock time in constrained quantum models: which reduction of a
timeless physical state yields which conditioned dynamics. None of it bears on temporal
ontology, objective passage or the thermodynamic arrow without bridge premises. Rijavec's
"time inversion" (Sec. VI.3-VI.4) is a sign change of an effective frequency under strong
coupling. It is not a thermodynamic or causal arrow claim. Non-unitarity or memory in a
conditioned map is a property of the chosen reduction and state class, not evidence about
determinism of the underlying constrained dynamics.

## What remains unread and why

- Garmier et al. Apps. B-H proofs: time budget. Theorem 1 is taken at statement level.
- 2409.06479v3 beyond the four located passages: not a named paper in the brief. It was
  added as the trinity's own deferred periodic-clock extension.
- Proofs in trinity App. C: not in scope ("interaction passages and conclusions").
- Cafasso et al. 2407.00161, Paiva et al. 2022, Singh-Friedrich 2304.01263 beyond the
  abstract: leads only.
- No paywalled or blocked pages were encountered. All reads used arxiv.org HTML (v3, v3,
  v1, v2, v3 as recorded).
