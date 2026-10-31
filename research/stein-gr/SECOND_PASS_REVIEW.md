# Second independent proof check

25 October 2026. Checked the revised `main.tex`, rather than treating the
older `DRAFT.md` as current. Source SHA-256:
`33f4a667f9886db61234f10f8c322dadfc01bd47a2828a266238798cc3c1abb6`.
This review does not modify the manuscript being edited in parallel.

## Verdict and scope

The revised proof has incorporated the main repairs from
`INDEPENDENT_REVIEW.md`: spacelike chains, quantitative cone control,
Gaussian coordinates with the whole initial slab in the original Cauchy
surface, escape paths, and an explicit flat detour. I found no additional
counterexample to the central theorem under its stated category of all
globally hyperbolic metrics. Two small but real proof-writing defects remain
below. This is a conditional mathematical assessment, not a novelty verdict
or certification of the energy-condition extension or every subsidiary result.

## 1. Strict chronology must be distinguished from its reflexive closure

**Finding: correct before treating the proof as finished.** The framework
(lines 139–143 in the checked source) takes I^- to be reflexive, but lines
305–307 and 341–345 use openness and Int J^- = I^- from Minguzzi–Sánchez.
Those source statements use *strict* chronology. In a GH spacetime a
diagonal pair (p,p) belongs to reflexive I^- but not to Int J^-: arbitrary
neighborhoods contain spacelike pairs. Thus the displayed equality is false
with the manuscript's convention.

This affects the claim that the diamond at lines 532–534 is open, too:
reflexive chronological intervals include their endpoint, so that diamond
need not be open. The desired conclusion still follows by taking the
*strict* chronological diamond, because p^- << p <= r <= q << q^+.

**Precise repair.** Define I_strict^± by timelike curves and write
I_reflexive^± = I_strict^± ∪ Δ. Keep the becoming classification in terms of
I_reflexive^-. State the imported topological facts as

    Int J^± = I_strict^±,
    closure(I_reflexive^±) = closure(I_strict^±) = J^±   (in GH).

In the regularity proof, openness of B\Δ gives B\Δ ⊆ I_strict^-, hence
B ⊆ I_reflexive^-, and (CB) gives equality. Use strict diamonds when proving
openness in Lemma D. No change to the classification statement is required.

Primary source checked: Minguzzi–Sánchez, arXiv:gr-qc/0609119v3,
Propositions 2.16–2.17. Read depth: the relevant definitions, propositions,
and proofs; not a new whole-paper audit.
https://arxiv.org/html/gr-qc/0609119v3

## 2. Lemma D(ii) omits simultaneous crossing of the shell and t=0

**Finding: small missing case.** At lines 512–517 the first event is either
crossing t=0 *inside* T_{2r}, or meeting the shell at t>0. These do not cover
meeting t=0 and the shell simultaneously. This is geometrically possible:
a causal curve can reach t=0 with |y|=2r, for example.

**Precise repair.** Let τ_0 be the first t=0 crossing and τ_exit the first
shell crossing along the past-directed curve. If τ_0 ≤ τ_exit, including
equality, pull back the segment ending at t=0. Unless it hits Σ', its endpoint
is in S\Σ; extend to the past of S to contradict membership in D_M^+(Σ).
The pullback at a shell point is defined because the chart and metric
agreement extend to a neighborhood of the closed T_{2r}. If
τ_exit < τ_0, then t>0 at the exit and the stated escape path applies.
Reverse the roles of the ambients for the other inclusion.

The separate t=0 case p∈Σ is immediate and may be removed before defining
these stopping events. In the reverse inclusion, the original Cauchy surface
guarantees that a past-inextendible M-curve either exits the tube or reaches
that surface; it is not necessary to assert a global coordinate t on M.

## 3. Future-pair reduction now passes the substantive check

Lemma R, lines 369–390, uses a convex normal U, a causally convex V⊂U,
and a nonzero future causal tangent u from b to b_1. Its first-variation
sign is correct:

    2σ(exp_b(εa), b_1) = g(u,u) - 2εg(u,a) + O(ε²).

The required spacelike a exists for every such u, including a purely temporal
u: in an orthonormal frame write u=(u0,v), u0>0; take
a=(-1,2n) with n parallel to v, or any unit spatial n if v=0. Then
g(a,a)=3 and g(u,a)=u0+2|v|>0. The first variation therefore produces a
future timelike displacement from q_ε to b_1 even when u is null.
For small ε, q_ε∈V; causal convexity promotes its separation from b in U
to separation in M. Push-up gives q_ε << x. This closes the earlier concern
about future null pairs as well as timelike pairs.

## 4. Remaining geometry: what has actually been checked

- The revised longitudinal ranges of T_ρ are nested with compact closure,
  so the stated cutoff exists. The earlier fixed-range cutoff defect is gone.
- The cone thresholds are less than one, give Lorentzian signature by the
  spatial-block/Schur-complement argument, and survive the convex interpolation.
  The estimate 6Kr controls the full support T_{3r}.
- The first-exit escape paths cover lateral, longitudinal, and positive-time
  lid points. Their transverse displacement and containment inequalities have
  the correct direction. The choice of the last crossing before Σ in (i)
  supplies t(q)>0.
- The revised spacelike-chain proof uses only closedness of the pointwise
  sets J^±(z), not the extra closed-relation claim left in the older draft.
- The flat detour lies on a globally Cauchy tilted hyperplane, not merely a
  pointwise spacelike arc. The bound 10 sin(π/8)>3 and 8λr<L suffices.
  For its tubular argument, the flat arc must be extended beyond P,Q and the
  transverse radius taken below its tubular reach and distance to the curved
  support; the revised proof now specifies these choices. This is the same
  escape-path localization mechanism in boosted coordinates.
- Lemma D(iii)'s causal-convexity argument is structurally sound. The openness
  step should use strict diamonds as in finding 1; connectedness then follows
  by paths to the connected relative interior of the initial slab.

## 5. Verification and next gate

The desktop LaTeX compiler reports success for the checked `main.tex`.
A separate label/reference scan found 29 labels, no duplicates, and no
unresolved internal references. These mechanical checks do not establish the
infinite theorem; the mathematical findings above are hand checks.

Next: apply the two precise source repairs, reread the final assembled proof,
and keep the off-shell scope explicit. The interpolation does not establish
the analogous result on a category restricted by Einstein–matter equations
or energy conditions. The energy-condition branch and priority claims require
separate assessment, even if the central kinematic theorem is accepted.
