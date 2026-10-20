# RC-1 reread: interaction-dependent clocks

Coordinator draft, 2026-10-20, after `kb-clock-interactions` (merge bc4b109).
Passages re-read by the coordinator from arXiv HTML fetched 2026-10-20. Not a
novelty claim.

## Verdict: SHRINK

Remaining case, in one sentence: *for a finite `Z_N` clock with a non-ideal
covariant POVM, a pure physical state on a single constraint surface, and a
clock–system interaction with `[H_int, H_C] ≠ 0` that acts non-trivially on the
physical subspace, do the Dirac, Page–Wootters and relational-Heisenberg
reductions agree?*

## Re-read passages (verbatim, coordinator-checked)

| Source | Passage | What it excludes |
|---|---|---|
| Höhn–Smith–Lock 1912.00033v3 | "we assume that the clock and system do not interact"; the equivalence is shown "for clock Hamiltonians with non-degenerate and continuous spectrum"; "henceforth considering only noncompact clocks"; interactions are "the most pressing generalization" | interacting and finite clocks |
| Chataignier–Höhn–Lock–Mele 2409.06479v3 | "we shall henceforth assume that no interactions between C and S are present"; "this would typically also ruin the periodicity of the clock" | interacting periodic clocks |
| Smith–Ahmadi 1712.00081v3 | footnote 1: time-independent inner product "may severely reduce the size of the physical Hilbert space" | treats interactions, but only in the PW picture |
| Rijavec 2204.11740v3 | Sec. VII: "I leave this problem open for future investigations" (interactions not leaving the clock invariant) | only `[H, V] = 0` treated |

The lane's exact checks reproduce. Smith–Ahmadi Example 3 has
`‖[H_int, H_C]‖ = 0.868`, but `H_int` annihilates the physical span, so its
"no effect" result is degenerate. Rijavec's two-sector mixture gives trace
distance `|cos(θ/2)|`, which is non-monotone.

## Disagreements (unresolved)

1. The existing record `frontier-relational-trinity-2019v3` may overstate its
   coverage of discrete-spectrum clocks (lane's reading). Correcting it is left
   to `rt-source-canonicalization`.
2. The lane reads Mendes et al. 2107.11452 as not showing the claimed
   non-linearity (the potential is defined from the state). Not re-checked.
3. Smith–Ahmadi Eq. (26) sign: the lane's check shows `e^{-iH_S t}` matches,
   not `e^{+iH_S t}`. A typo in the paper, per the lane; not re-checked against
   the published version.

## Combined claim-contract draft (RC-1 and RC-5)

RC-1 and RC-5 now share their smallest open object, so one contract covers both.

- **Question.** In a `Z_3` clock + qubit model with `H_int = g σ_x ⊗ K`,
  `[K, H_C] ≠ 0`, a non-ideal covariant clock POVM, and one constraint surface:
  (a) do the three reductions agree, and where do they first differ; (b) under
  linear conditioning, which memory criteria (semigroup, CP-divisibility,
  backflow, process tensor) fail?
- **Nearest predecessors.** Höhn–Smith–Lock 1912.00033 (non-interacting
  trinity); Chataignier–Höhn–Lock–Mele 2409.06479 (periodic, non-interacting);
  Smith–Ahmadi 1712.00081 (interacting, PW only); Milz et al. 2019 and
  Chruściński–Kossakowski–Rivas 2011 (criterion separations).
- **Delta.** Applying known reductions and criteria to an interacting finite
  clock that the predecessors exclude by assumption. Likely an application.
- **Smallest example.** The one in the question, computed exactly. Compute the
  reading probabilities first: the lane conjectures they become non-uniform when
  `[H_int, H_C] ≠ 0`.
- **Falsifier.** Cafasso et al. 2407.00161 (interacting finite-dimensional PW;
  discovery depth only), Paiva et al. 2022, or a forward citation of Smith–Ahmadi
  or Höhn–Smith–Lock that already computes this.
- **Novelty kind.** At most a worked application. Not a new framework, not an
  ontology result.

Read Cafasso et al. at full text before any computation is presented as new.

## Independent post-claim reread (2026-10-20)

The parent task was claimed after this draft. The coordinator re-fetched the
primary HTML and re-read the decisive passages; all quotes above reproduce.
Additions and corrections:

- **Rijavec 2204.11740v3, Eqs. (46)–(51).** `H = H ⊗ I + I ⊗ h + V`; Eq. (47)
  imposes `[H ⊗ I + I ⊗ h, V] = 0`; Eq. (48) imposes `[I ⊗ h, V] = 0`; together
  they give Eq. (49) `[H ⊗ I, V] = 0` and, with non-degenerate `h`, the
  eigenbasis `{|E>|ε>}`. Eq. (51) is `V = X ⊗ h` with `[X,H] = 0`. Eq. (48)
  alone already forces `V` to commute with the clock Hamiltonian, so the
  `[H_int,H_C] ≠ 0` case is outside this paper's class by construction, not
  merely by choice. Sec. VII: "Finally, it would be interesting to consider
  interactions such that t̂ is not left invariant when moving from the
  Schrödinger picture to the Heisenberg picture... I leave this problem open
  for future investigations." This confirms the lane's reading.
- **Smith–Ahmadi 1712.00081v3.** Eq. (14) is the modified Schrödinger equation
  with the kernel `K(t,t') = <t|H_int|t'>`, derived for general `H_int` in the
  Page–Wootters picture only. Eq. (15) is the isometry/norm-preservation
  condition. Example 3 (Eq. 24) has `||[H_int,H_C]|| = 0.868` and
  `H_int|10> = H_int|01> = 0`; `H` has the physical null space
  `span{|01>,|10>}`. The example is therefore degenerate. Eq. (26) prints
  `e^{+iH_S t}`; the conditional state computed from Eq. (26) matches
  `e^{-iH_S t}`, so the paper has a sign typo (the lane's script reproduces
  this; not checked against the published version).
- **Garmier et al. 2512.19343v2.** The framework is kinematic: a global action
  `U_A ⊗ U_S` (Eq. 1 and the relationalization map Eq. 3), perspective and
  invariance principles, incoherent group averaging. Sec. IV describes the
  superselection range for non-ideal QRFs; the only time-evolution remark in
  Sec. V is qualitative ("the time evolution ... behaves as if A were an ideal
  clock"). Finite Abelian groups, hence `Z_N`, are covered kinematically, but
  there is no Hamiltonian-constraint dynamics or clock–system interaction. This
  is not a three-picture result, so it does not close the RC-1 case.
- **Höhn–Smith–Lock 1912.00033v3.** Verified: Sec. II.2 "we assume that the
  clock and system do not interact"; Sec. V.3 "for clock Hamiltonians with
  non-degenerate and continuous spectrum"; Sec. III.2.3 "henceforth considering
  only noncompact clocks"; Sec. IX calls interactions "the most pressing
  generalization".
- **Chataignier–Höhn–Lock–Mele 2409.06479v3.** Verified: "we assume that there
  are no interactions between the two sets of degrees of freedom, as this would
  typically also ruin the periodicity of the clock"; and Sec. II "we shall
  henceforth assume that no interactions between C and S are present".
- **Cafasso et al. 2407.00161v1 (the named falsifier).** The abstract and Secs.
  I–II were read. This is a finite-dimensional Page–Wootters framework, but the
  system is non-interacting with the (possibly composite) clock: the
  gravitational-like interaction is *inside* the composite clock (time-dilation
  transfer between local clocks). It does not treat a clock–system interaction
  with `[H_int,H_C] ≠ 0`, and it does not compare three reductions. It is not a
  defeater for the remaining case, though a full read is still owed before any
  computation is presented as new.

Correction to the combined contract below: its "nearest predecessors" list
should also name Garmier et al. 2512.19343 for the kinematic finite-Abelian
case, and Cafasso et al. 2407.00161 as a finite-dimensional PaW neighbour that
does not treat the interaction.
