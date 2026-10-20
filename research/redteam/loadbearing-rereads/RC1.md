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
