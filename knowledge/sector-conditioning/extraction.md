# Sector-coherence and normalization literature behind RC-3: full-text extraction

Lane `kb-sector-conditioning`, 2026-10-20. Completed by a Claude subagent after the GLM worker
stopped on a provider quota. This is a worker submission for review, not accepted completion.
It makes no novelty claim. Source records are in `sources.jsonl` (lane prefix `sector-`; two
records reuse existing `frontier-` IDs).

Quotation conventions: the words are verbatim from arXiv LaTeXML HTML. Math is transcribed from
the HTML `alttext` in simplified plain notation, for example `|psi_phys>` for
`\left|\right.\!{\psi_{\text{phys}}}\!\left.\right\rangle`. Equation, footnote and section numbers
are the arXiv HTML numbers. No PDF was checked (no PDF renderer is installed and none was added).

Labels used below:
- **[A]**: the paper authors' claim.
- **[R]**: a result proved in the source. Read, not re-derived.
- **[C]**: this run's own observation or conjecture. It is not in any source read and has not been
  verified.

## 1. Sector-wise reduction maps and partial isometries

**Höhn–Smith–Lock (HSL), arXiv:2007.00580v1** (`frontier-relativistic-trinity-2020v1`).

The constraint is `C_H = s p_t^2/2 + H_S`, which factors as `s C_+ C_-` (Eq. 11). Eq. (14) gives
`delta(C_H) = (1/(2(-s H_S)^{1/2})) sum_sigma delta(C_sigma)`. Then "The form of `delta(C_H)`
implies the decomposition of the physical Hilbert space into a direct sum of positive and negative
frequency sectors `H_phys ≃ H_+ ⊕ H_-`" (Sec. III.0.2).

- **Clock POVM.** Eq. (24) is `E_T(dt) = (1/2pi) sum_sigma dt |t,sigma><t,sigma|`. Eq. (25) is
  `|t,sigma> = ∫ dp_t sqrt|p_t| theta(-sigma p_t) e^{-i t s p_t^2/2} |p_t>`. Lemma 5 [R] says
  "The effect density `E_T(dt)` of the covariant clock POVM and the projectors onto the
  `sigma`-sectors commute". The text explains: "they permit us to condition on the time indicated
  by the clock and the frequency sector simultaneously" (after Corollary 1).
- **Reduction maps (Eq. 38).** These are `R_PW^sigma(tau) := <tau,sigma| ⊗ I_S`, "one per
  `sigma`-frequency sector" (Sec. V.1.2).
- **The 1/sqrt 2 factor (Eq. 39).** This is `(1/sqrt2)|psi_S^sigma(tau)> := R_PW^sigma(tau)|psi_phys>`.
  After Corollary 2 the authors say: "The reason for introducing the normalization factor
  `1/sqrt2` in Eq. (39) is now clear: it permits us to work with normalized states
  `<psi_S^sigma(tau)|psi_S^sigma(tau)> = 1 = <psi_phys|psi_phys>_phys` in each reduced
  `sigma`-sector and in the physical Hilbert space simultaneously." That normalisation holds only
  for a state lying entirely in one sector.
- **Inverses (Eqs. 42–44).** `(R_PW^sigma(tau))^{-1} = delta(C_H)(|tau,sigma> ⊗ I_S)` and
  `sum_sigma (R^sigma)^{-1} R^sigma ≈ I_phys`.
- **Corollary 2, Eq. (47) [R].** `<psi_phys|phi_phys>_phys = (1/2) sum_sigma <psi_S^sigma(tau)|phi_S^sigma(tau)> = sum_sigma <psi_phys|(|tau,sigma><tau,sigma| ⊗ I_S)|phi_phys>_kin`.
- **Heisenberg version.** The same factor 1/2 appears in Eqs. (52)–(54), Lemma 8, Theorem 4 and
  Corollary 3.
- **Footnote 13** is attached to Eq. (33). It is not the superselection statement. It says the
  G-twirl "can on each `sigma`-sector be weakly rewritten as a reduced `G`-twirl `G_sigma`" when 0
  is not in the spectrum of `H_S`.

**Hosseini–Lock (HL), arXiv:2604.00092v1** (`sector-hosseini-lock-toa-2026`).

- **Sec. II.2.** "In the case where the clock Hamiltonian `H_C` is degenerate, the physical Hilbert
  space decomposes into a direct sum of degeneracy-sectors, and the reduction maps `R_C(t)` must be
  defined sector-wise [32]. In that case these maps are partial isometries, and the physical inner
  product is recovered after summing the corresponding reduced inner products over sectors."
- **Sec. III.1, Eq. (25).** `|x0,sigma>_S = ∫ dp Theta(sigma p) sqrt(sigma p/m) e^{-i x0 p} |p>_S`,
  "giving a partial isometry `R_sigma(x0): H_phys → H^sigma_{C|S}`". Eq. (26) is
  `R_sigma(x0)^{-1} = delta(C)(1_C ⊗ |x0,sigma>_S)`, with
  `sum_sigma R_sigma(x0)^{-1} R_sigma(x0) = 1_phys`.
- **Footnote 1.** "the reduction map `R_sigma(x0)` can also be obtained by projecting from `H_phys`
  onto a `sigma`-sector `H^sigma_phys`, applying `1_C ⊗ <x0|_S` and then normalising the result."
- **Appendix A, Eqs. (40)–(46) [R].** This is the general sector-wise map
  `R_sigma(y) = 1_C ⊗ <y,sigma|_S`. The text says "`R_sigma(y)` is an isometry if and only if"
  `|y,sigma>_S = ∫ dp Theta(sigma p) sqrt(sigma p/m) e^{i phi_sigma(y,p)} |p>_S` (Eq. 42). The
  inverse is Eq. (46), "as in Eq. (42) in [32]".
- **Setting difference.** In HL the sector label is the sign of the *system* (particle) momentum.
  The clock is non-degenerate, and the conditioning is on a system property (position). HL also use
  a different sign convention for sigma than HSL (Sec. II.3).

**Chataignier–Höhn–Lock–Mele, arXiv:2409.06479v3** (`sector-chataignier-periodic-2024`).

- **Clock degeneracy.** Degenerate clocks are only mentioned. Footnote 10 says the construction
  "can be readily generalised to the case where each eigenvalue of spec(H_C) has the same degree of
  degeneracy by repeating the formalism described here per degeneracy sector, as in [11, 16]"
  ([11] = HSL, [16] = De Vuyst et al. 2412.15502).
- **Left and right movers.** In Example 9 (oscillator clock plus free particle) the sectors sit in
  the system, and a single non-sector-wise map `R_S(tau) = <tau| ⊗ I_S` (Eq. 91) is used.
  Corollary 3 [R] states that it "preserves the physical inner product".

**Ludescher–Mekonnen–Galley–Müller, arXiv:2607.24976v1, Example 30**
(`frontier-qrf-beyond-subsystems-2026`).

- **Combined Kraus seed.** They combine the HSL sector maps into one Kraus seed:
  `M_t := (|t,+><t,+| + |t,-><t,-|) ⊗ 1_S ↾ H_phys`. Then "This result shows how the two reduction
  maps for the frequency sectors are combined into a single isometry in our generalization of the
  PN framework. The two solutions `|psi_S^sigma(t)>`, obtained separately in [100], are now jointly
  encoded into the two orthogonal frequency sectors (since `<t,+|t,->=0`)."
- **Scope.** They describe the example as "slightly beyond our mathematical framework" and say they
  "will ignore all normalization factors".

## 2. Normalization failure of the plain (single, non-sector-wise) reduction map

**HSL footnote 16** (attached to Eq. 40; also footnote 16 in the Frontiers version):

> "Note that we could also define linear combinations of clock states `|tau> := sum_sigma c_sigma
> |tau,sigma>`. [...] However, it is straightforward to check, using Lemma 1, that these new clock
> states do not give rise to a resolution of the identity, `∫ dtau |tau><tau| ≠ I_C` and so
> `|psi_phys> ≠ ∫ dtau |tau>|psi_S(tau)>`. In fact, if `c_sigma ≠ 0` for `sigma=+,-`, then
> `|psi_S(tau)>` will mix contributions from the positive and negative frequency sectors such that
> it will become impossible to reconstruct (either of the positive or negative frequency part of)
> the physical state from it. That is, a reduction map `<tau| ⊗ I_S`, which only conditions on the
> clock time, would not be invertible. This is another consequence of the superselection rule
> discussed above which entails that superpositions and mixtures across `sigma`-sectors are
> indistinguishable through Dirac observables."

HSL do not state a state-dependent normalisation for that map. Their objection is non-invertibility
and the missing resolution of the identity.

**HL Sec. III.1, paragraph 2.** This is the state-independent normalisation failure, quoted
exactly:

> "However, from Eq. (19), one finds that the resulting state coherently combines the different
> superselection sectors in `H_phys`, encoding symmetry-forbidden phase information between
> sectors. Crucially, `R~(x0)` is not invertible, and the relational clock states, and therefore
> the arrival time probability distribution derived therefrom, cannot be normalised in a
> state-independent manner, and we must therefore find another solution."

HL Sec. IV, after Eq. (32): "Integrating over `t` gives the norm of the output of the 'naive'
reduction map `R~(x0)` discussed in Sec. III.1. As noted earlier, this is neither unity nor
normalisable in a manner independent of `|psi_phys>`."

**HL Appendix A [R]** concerns one map `R(y) = 1_C ⊗ <y|_S`.

- After Eq. (36): "we see that `R(y)` is many-to-one, and therefore not invertible."
- After Eq. (39): the isometry condition "can only be satisfied on one momentum sector `H^sigma_phys`
  of the physical Hilbert space. [...] From Eq. (37), we see that a violation of this sector-wise
  reduction results in the reduced space `H_{C|S}` encoding information about coherences between
  superselection sectors of `H_phys`, which is forbidden by the constraint."
- Scope: the proof constrains a single rank-one conditioning map per value of `y`. It does not
  consider a family of maps `{R_b(y)}_b` that are jointly, but not individually, isometric (see §6).

**2409.06479 Lemma 10 and Eq. (106)** report a different normalisation failure. For a periodic
clock and a constraint generating R, the kinematical conditional inner product diverges. This is
unrelated to sectors.

**HSL Sec. VI, Eq. (61).** This is the non-covariant Minkowski-time rule
`prob(x when t) = |psi_phys(t,x)|^2 / ∫ d^3x' |psi_phys(t,x')|^2`. The text continues: "apart
from not separating positive and negative frequency modes, which is necessary for a probabilistic
interpretation (e.g., if `psi_phys` contains both positive and negative frequency modes then the
denominator in Eq. (61) is not conserved)". Footnote 22 adds that the denominator equals the
physical inner product only for the covariant POVM, because `delta(C_H)(e_C(tau) ⊗ I_S) ≈ I_phys`.

## 3. Sector-mixed normalized rules actually stated

- **HSL Eq. (62).** `prob(x when tau) = (1/2) sum_sigma |psi_S^sigma(tau,x)|^2 = <psi_phys|F_{e_x,T}(tau)|psi_phys>_phys`,
  with `e_C(tau) = sum_sigma |tau,sigma><tau,sigma|`. "Eq. (62), in contrast to Eq. (61), does
  admit the interpretation as a valid, yet approximate localization probability for the
  relativistic particle per frequency sector".
- **HL Eq. (28).** `Pr[t|x0] = sum_sigma <psi^sigma_{C|S}(x0)|E(t)|psi^sigma_{C|S}(x0)>`, which is
  "normalised by construction". Eq. (30) is the Kijowski form.
- **2409.06479 Sec. VI.2.4.** `P(f_S|tau)` is the ratio of a relational-observable expectation
  value to the norm in the physical inner product. For the left/right-mover examples this rule is
  not sector-mixed, since no sector split is imposed there.
- **2607.24976 Example 30.** Its combined frame `M_t` gives the same sector-mixed statistics,
  because the outputs live in orthogonal clock states.

## 4. The inaccessibility (superselection) claim

**HSL Sec. V.1.1, after Eq. (33).** Exact wording, identical in the Frontiers version:

> "While there do exist states in the physical Hilbert space that exhibit coherence across the
> `sigma`-frequency sectors, for example `|psi_phys> ~ |psi_+> + |psi_->`, where
> `|psi_sigma> ∈ H_sigma`, such coherence is not physically accessible because it does not affect
> the expectation value of any relational Dirac observable on account of the decomposition in
> Eq. (33). In other words, superpositions and classical mixtures across the `sigma`-frequency
> sectors are indistinguishable. Hence, superpositions of physical states across `sigma`-sectors
> are mixed states and the pure physical states are those of either `H_+` or `H_-` (see also
> [92, 94] for a discussion on superselection in group averaging)."

The basis is the operator `Q = theta(-p_t) - theta(p_t)`, a strong Dirac observable that commutes
with every `F_{f_S,T}(tau)` "on account of Lemma 5". Eq. (33) is `F = F^+ ⊕ F^-`.

**HL Sec. II.3, after Eq. (20).** "In particular, physical expectation values are insensitive to
coherence between the `sigma=±` components. In other words, the constraint enforces a superselection
rule between the two sectors (see, e.g., [7, 32])." ([7] = Bartlett–Rudolph–Spekkens.)

**HL footnote 3 (Sec. V)** qualifies this:

> "Somewhat counter-intuitively, the Page-Wootters formalism nonetheless permits such coherences
> when describing the system relative to the clock, while still respecting the superselection rule
> at the level of the physical Hilbert space. In particular, any observable on the relational space
> `H_{S|C}` which encodes phase information between positive- and negative-momentum contributions
> to the particle's wavefunction, is equivalent to an observable on the physical Hilbert space
> which satisfies the superselection rule there, as can be seen directly from Eq. (43) of [33]."

**HSL Sec. VII.1** (after Eq. 68) has a "double superselection rule": "any reduction map is only
invertible on its associated `sigma`-sector [...] This is a manifestation of the superselection
across both the `sigma_1`- and the `sigma_2`-sectors."

**2607.24976 Example 30** repeats the claim: "it is shown in [100] that Dirac observables are
superselected across the frequency sectors; hence coherences [...] do not influence expectation
values".

**Contrast in 2409.06479.** In Example 14 (qubit clock plus free particle) the text says: "Given
that `H_phys ≃ C^2` (cf. Example 10), it is clear, however, that the algebra
`A_phys = L(H_phys)` of Dirac observables is four-dimensional." That algebra includes operators
mixing the left- and right-mover sectors. Example 13, Eq. (81) builds the physical position
projection with a coherent sum over `mu = ±1`. HL Sec. V, however, cites this paper's Example 9 for
"the absence of interference between these sectors persists". Example 9 only states the direct sum.

My reading [C] is that this is not a contradiction. The two papers attach the sector label to
different subsystems (system versus conditioning reference). HL footnote 3 itself admits coherence
relative to the clock. The texts read do not settle it explicitly.

[C] HSL's claim is made for relational Dirac observables of the Eq. (31) form. The clock reflection
`P_C: |p_t> → |-p_t>` commutes with `C_H`, because `H_C` depends on `p_t^2`. It maps
`|t,sigma>` to `|t,-sigma>` and `H_+` to `H_-`, preserving the physical inner product (Eq. 18).
`P_C ⊗ I_S` is therefore a strong Dirac observable that does not commute with `Q`. Its expectation
value distinguishes `|psi_+> + e^{i phi} P|psi_+>` for different `phi`. So "superselection" here is
relative to the chosen observable algebra, not a property of `H_phys` alone. Footnote 16's wording
("indistinguishable through Dirac observables") is broader than the main text's "relational Dirac
observable". Unverified. The abstract of Marolf gr-qc/9508015 says RAQ superselection laws depend
"on the choice of auxiliary structures", so it is the likeliest prior treatment.

## 5. External or internal phase reference

**HSL Sec. V.1.1** gives the complete paragraph, citing BRS as [117] (arXiv) or [130] (Frontiers).
It is not cut off:

> "Superselection rules induced by the `G`-twirl are often interpreted as arising from the lack of
> knowledge about a reference frame, and that if an appropriate reference frame is used the
> superselection rule can be lifted [117]. This interpretation seems unsuitable here. Firstly,
> lifting the superselection rule would entail undoing the group averaging, in violation of gauge
> invariance. Secondly, such an interpretation is usually tied to an average over a given group
> action which parametrizes one's ignorance about relative reference frame orientations. By
> contrast, the origin of the superselection of Dirac observables here is not the group generated
> by the constraint, but is a consequence of a property of the constraint, i.e. the group
> generator. Indeed, the superselection rule above originates in the factorizability of the
> constraint and the ensuing decomposition of the projector onto the constraint, Eq. (14). Both
> these properties rely on the absence of a `t`-dependent term in the constraint Eq. (13); if such
> a term is introduced, one generally finds `[C_+, C_-] ≠ 0`, where the `C_sigma` are the
> quantization of the classical factors, but we emphasize that `C_H ≠ s C_+ C_-` in that case.
> While such a modified constraint may generate the same group,[fn 14] no superselection rule
> across the `sigma`-sectors would arise. The above superselection rule can thus not be associated
> with the lack of a shared physical reference frame. This resonates with the interpretation of the
> physical Hilbert space as a clock-neutral, i.e. temporal-reference-frame-neutral structure (see
> Sec. II.2)."

Footnote 14 in full: "E.g. when `C_H = p_t^2 - H^2(q_i,p_i,t)` and `H^2 > 0 ∀ t ∈ R`."

[C] There is a tension inside this paragraph. The first reason treats the superselection rule as
G-twirl-induced ("undoing the group averaging"). The second reason says it does not come from the
group. The G-twirl over the R generated by `C_H` does not remove the off-diagonal sigma blocks,
because `H_C` is degenerate across sectors. The `(1/2pi)∫dt|t,-><t,+|` twirl gives a non-zero
sector-swapping operator. Unverified sketch.

**Bartlett–Rudolph–Spekkens (BRS), arXiv:quant-ph/0610030v3** (`sector-brs-reference-frames-2007`).

- **Scope (Sec. II.3).** BRS "restrict our attention to Lie groups that (i) are compact [...] Many
  of the techniques in this review can be applied to other groups with some modification, but
  there are many technical difficulties which are beyond the scope of this review." Footnote 4
  extends this to finite groups.
- **The rule restricts preparers, not the theory (Sec. II.2).** "the SSR only restricts preparations
  and operations by Alice (or any party who does not share Charlie's phase reference). The SSR does
  not forbid states with coherence between different total photon-number eigenstates from existing
  within the theory".
- **Observables-only reading (Sec. II.3).** "(Occasionally, this restriction is argued to hold for
  the observables alone, but in this case every state that is not restricted in this way is
  operationally indistinguishable from a state that is, so one may as well assume this restriction
  for the states also.)"
- **Internal phase reference (Sec. IV.1.1).** "if we incorporate the phase reference as an internal
  system (and we do not compare our internal systems to any other external phase reference), then
  the only empirically meaningful states and operations are invariant under phase shifts of the
  entire system (including the internalized phase reference)."
- **Lifting (Sec. IV.2).** "although a SSR for G applies to the entire composite system RS, the RF
  allows us to effectively describe the system as if the SSR did not exist [118]". The $-map
  (Eq. 100) is `A ↦ ∫_G dg |g><g| ⊗ U_S(g) A U_S(g)^†`. Eq. (106) reproduces `Tr_S[rho E_k]`.
- **Conclusion (after Eq. 106) [A/R].** "It proves that superselection rules cannot provide any
  fundamental restrictions on quantum theory. [...] It also proves that all superselection rules
  associated with unitary representations of compact groups result from a lack of an appropriate
  reference frame".
- **Non-compact groups (Outlook).** "non-compact groups (such as the Lorentz or Poincaré groups)
  may require more general mathematical tools than those discussed here."
- **Global descriptions (Sec. IV.3).** "If one seeks to describe the entire universe quantum
  mechanically [...] then it is natural to assume SSRs for all global transformations".

**Answer to the coordinator's question.** A gauge-invariant internal reference system has been
treated, by BRS Secs. IV.1–IV.2, but only for superselection rules generated by twirling over a
compact or finite group, outside any Hamiltonian-constraint setting. In none of the sources read
has an internal reference system that *carries the sigma (frequency-sector) label* been treated in
the constrained, Page-Wootters setting.

- HSL reject the lifting reading by argument; they do not construct anything.
- HL never model a phase reference.
- 2607.24976 Example 30 builds a single frame for both sectors, but its outputs are
  sector-orthogonal. It also states that the coherent seed `(|t,+> + |t,->)/sqrt2` "is not a
  coherent seed state any more".
- [C] Formally, the sigma rule has the shape of a Z2 superselection rule generated by the unitary
  `Q` (with `Q^2 = I`). BRS footnote 11 (finite groups) would then supply a formal Z2 lifting. Whether
  such a reference system can be added while keeping the composite inside `ker C_H` is not
  addressed anywhere read.

**Time-dependent constraint (footnote 14 case).** No normalised conditioning rule was found in any
source read. HSL give only the example constraint and the claim that no sector superselection would
arise; they derive nothing for it. 2607.24976 Example 29 has time dependence through interaction,
which is a different mechanism with no sector structure. Not read: Bogoliubov-type mixing of
frequencies for Klein-Gordon equations with time-dependent mass (standard QFT in curved spacetime),
the `kb-clock-interactions` lane sources, and Chataignier 2006.05526 (HSL ref. [34]).

## 6. Does a normalized sector-coherent conditional probability, distinct from the sector-mixed rule, appear?

**Not in any source read** (HSL, HL including Appendix A, BRS Secs. II and IV, 2409.06479
Secs. IV–VI, 2607.24976 Example 30).

- HSL footnote 16 rejects a single coherent clock state.
- HL Appendix A rules out a single isometric map with support on both sectors. HL footnote 1
  normalises only after projecting into one sector.
- 2607.24976 reaffirms the superselection rule.

**[C] Unverified sketch, not a literature result.** Complete the coherent clock state into a
two-outcome covariant POVM, `E_b(tau) = (1/2pi)|tau,b><tau,b|` with
`|tau,b> = (|tau,+> + b|tau,->)/sqrt2` and `b = ±`.

- Because `<tau,+|tau,-> = 0` and `U_C` acts identically on both sectors,
  `sum_b ∫ dtau E_b(tau) = I_C` and the POVM is covariant.
- Conditioning on `(tau,b)` gives
  `P(f|tau,b) = |<f|(psi_S^+(tau) + b psi_S^-(tau))>|^2 / ||psi_S^+(tau) + b psi_S^-(tau)||^2`.
- The denominator does not depend on `tau`: both sector states obey the same Schrödinger equation
  (HSL Eq. 40), so `<psi_S^+(tau)|psi_S^-(tau)>` is conserved. It does depend on the state.
- Summing over `b` recovers HSL Eq. (62). The rule is a ratio of expectation values of G-twirled
  operators that commute with `C_H` but not with `Q`.
- None of the sources read rules this out. HL's Appendix A no-go concerns individually isometric
  single maps.
- Status: a calculation sketch by this run, not checked numerically (numpy is not installed and
  nothing was installed). It needs an independent derivation before use.
- **Likely defeaters:**
  - Marolf gr-qc/9508015 or Giulini–Marolf on algebra- or rigging-dependent superselection.
  - de la Hamette et al. 2110.13824 on non-ideal and incomplete frames.
  - De Vuyst et al. 2412.15502 on degenerate clocks.
  - An argument that `Q` must be imposed as a gauge or superselection charge, which would make the
    refined effects unphysical by fiat.

**Narrowest unaddressed case per source.** None of these is a novelty claim.

| Source | Narrowest case it leaves open | Read most likely to defeat it |
|---|---|---|
| HSL 2007.00580 | Expectation values of Dirac observables outside the Eq. (31) algebra, such as `P_C ⊗ I_S` or twirls of `\|tau,+><tau,-\| ⊗ f_S`, and the conditioning rule they would give; any rule for the t-dependent constraint of footnote 14 | Marolf gr-qc/9508015 full text; 2110.13824 Secs. on isotropy and incomplete frames |
| HL 2604.00092 | Jointly isometric families `{R_b(y)}` with support on both sectors; conditioning on clock time with a *degenerate* clock (HL condition on position with a non-degenerate clock) | HSL Appendices; Trinity 1912.00033 Eq. (43) (HL footnote 3) |
| BRS RMP 79, 555 | Superselection rules not generated by twirling over a compact or finite group, and any setting with a Hamiltonian constraint | Literature on reference frames for non-compact groups; Aharonov–Susskind-type constructions in canonical gravity |
| 2409.06479 | Degenerate periodic clocks (deferred to footnote 10) | De Vuyst et al. 2412.15502 full text |
| 2607.24976 Ex. 30 | Instruments whose Kraus operators are not block-diagonal in sigma | Its Example 26 (finite Abelian smearing) read in full |

## 7. Confirmations and corrections relative to `knowledge/defeat-search/rc3-and-clifton-czerniawski.md`

- **Confirmed verbatim:** the HSL inaccessibility quote, the 1/2 normalisation (Eqs. 39, 47, 62,
  and also Theorems 2 and 4 and Corollary 3), the non-invertibility of conditioning on `tau` alone
  (located: HSL footnote 16), the Sec. VI Eq. (61) statement about the denominator not being
  conserved, and the HL phrases ("insensitive to coherence", "coherently combines the different
  superselection sectors", "cannot be normalised in a state-independent manner").
- **Corrected:** the "can be lifted" sentence is not cut off. The full paragraph is quoted in §5,
  and the Frontiers version cites it as [130].
- **Corrected:** footnote 13 is attached to Eq. (33) but is about reduced G-twirls. The
  inaccessibility statement is in the main text of Sec. V.1.1.
- **Corrected:** 2409.06479 does more than list left/right movers "only as a direct sum". It treats
  the full `L(H_phys)` as the Dirac algebra (Example 14) and uses a single isometric non-sector-wise
  reduction map.
- **Now read:** HL Appendix A, which was "not read closely" before.
- **Confirmed for the sources read:** no normalised sector-coherent rule distinct from the
  sector-mixed rule was found.

**Disagreements with the coordinator lead.**

1. The lead says footnote 14 says "no superselection rule across the sigma-sectors would arise".
   That clause is in the main-text sentence. The footnote contains only the example constraint.
2. The lead names "non-twirled conditioning with an explicit external phase reference" as the
   narrowest open case. HSL already address and reject the *reference-frame interpretation*
   (by argument, §5), so the "external frame" sub-case is partly occupied at the level of
   interpretation, which agrees with commit c29b1c0. No construction exists in what was read.
   My view [C] is that the narrower open case does not need an external reference at all. It is
   G-twirled, `C_H`-commuting effects that are off-diagonal in sigma (for example the two-outcome
   refinement in §6), together with the question whether they belong to the physical algebra.

## 8. Temporal-concept separation

- **Clock time and the sectors.** In HSL the covariant clock reading "runs 'forward' in both
  sectors" (after Eq. 40). The coordinate `t` runs forward on one sector and backward on the other
  (Sec. IV.1). This is a fact about *clock time and orientation along the gauge flow*.
- **What it is not.** It is not a thermodynamic arrow, not objective passage, and not causal order.
- **No ontology follows.** Sector superselection, or its lifting, decides which correlations are
  physical observables. It does not decide between temporal ontologies. HL's empirical falsifier
  (no interference of counter-propagating wavepackets in arrival times) is a claim about clock-time
  statistics only. Nothing here bears on determinism.
