# Second GLM batch: initial coordinator review

29 October 2026. Both workers finished successfully and entered review. Neither submission is accepted by this note. Branch outputs remain preserved in their isolated worktrees. These are direct checks of submitted arguments, not a full source or proof audit.

## Continuity: claimed gate closure rejected as written

Submission: agent/lawful-finite-cone-continuity, commit b808729, RESULT.md.

At lines 215–218, the worker derives the algebraic inequality

    W <= C_n delta + a_n W,

where a_n can exceed 1, and calls it a Gronwall inequality yielding an exponential bound. That inference is invalid. For delta=0 and a_n>=1, any nonnegative W satisfies the displayed inequality. Monotonicity of W does not repair it. A genuinely causal integral inequality or a justified local contraction/patching argument is required, including the instantaneous axis-average terms.

There is an earlier subtraction omission at lines 191–193: subtracting phi_i=(1/r_i) integral theta_i lambda_i requires a denominator-difference term. A similar term is retained in the q calculation but missing for phi. The intended estimates may be repairable; their current presentation is not a proof of continuous dependence.

Status: Theorem 2 NOT ACCEPTED. Per-cone continuity remains an open gate. The conditional finite-dimensional degree argument is separate; no assertion that it is refuted follows from failure of this continuity proof. The source extraction and some regularized identities may remain useful after audit.

## Scalar common extension: promising source result; geometric objection needs correction

Submission: agent/lawful-scalar-common-extension, commit 779cc91, RESULT.md.

The worker provides a precise source chain for field-preserving smooth Einstein–scalar common development in Ringstrom's correction note. Its report distinguishes a common subdevelopment from a larger development containing both. This source chain deserves direct coordinator inspection before incorporation.

Three problems already block adopting the geometric audit verbatim:

1. Section 3.2 substitutes Sigma_1 subset I^-(b_1) for our K_1=Sigma_1 intersect W_1. A full earlier Cauchy level is not generally contained in the causal past of one point. In Minkowski space, sufficiently distant points on any earlier constant-time slice are spacelike to b. This substitution is not available in the horizon case.
2. Global closedness of K is not a necessary condition for D(K) to be open globally hyperbolic with K Cauchy. For an open unit spatial ball K at t=0 in Minkowski spacetime, the full domain is the OPEN diamond |t|+||z||<1. K is not closed in ambient Minkowski, but is Cauchy in that diamond. The worker's open-disk example does not demonstrate the asserted obstruction. This elementary counterexample does not by itself prove the general domain theorem our repair needs; exact general-source hypotheses still require checking.
3. Lemma D chooses w in I^+(b_2) and then applies h^(-1)(w). But h is defined only on W_1 -> W_2, and W_2 excludes J^+(b_2), so w is outside the range. The compactness proof is invalid as written.

Section 3.3 also gives the wrong reason for requiring scalar rather than stress-tensor preservation: an open-realm metric isometry already transports the induced metric AND extrinsic curvature of the hypersurface. The actual matter issue is that matching stress tensors does not match the scalar's value (constant shifts and sign choices can remain). Keep that legitimate issue distinct.

Status: common-development primary-source claim awaits direct inspection; assembled scalar corollary and alleged new closedness gate NOT ACCEPTED from this submission. Earlier vacuum repair is not overturned by the flawed objection, nor is it strengthened by dismissing that objection. Verify the standard domain theorem independently.

## Queue

Four ontology tasks are prepared and still dependency-gated pending proper disposition of these submissions. A reviewed negative result can satisfy the scheduling gate when integrated and accepted as a bounded report with corrections; an invalid theorem cannot be accepted as proved simply to start the next batch.

## Coordinator repair follow-up, 29 October

[COMPACTNESS_CONTINUITY_REPAIR.md](COMPACTNESS_CONTINUITY_REPAIR.md) replaces the invalid estimate with compactness plus source uniqueness. [SMOOTH_SCALAR_REPAIR.md](SMOOTH_SCALAR_REPAIR.md) directly checks Ringstrom's scalar-preserving common-extension chain and the standard domain statement, corrects the geometric objection, and assembles the bounded smooth scalar corollary. Both are coordinator integrations awaiting independent review. The user subsequently authorized launching all four ontology workers immediately; their scheduling dependencies were removed without accepting either flawed technical submission.
