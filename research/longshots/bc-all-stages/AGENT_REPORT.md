# All-stage scalar phase continuation: reviewed submission

Coordinator, 22 October 2026. Files: RESULT.md, check.py, output.txt,
INDEPENDENT_REVIEW.md, PERCOLATION_TAIL.md, PERCOLATION_REVIEW.md,
check_percolation_tail.py, percolation-output.txt, CLAIM_CONTRACT.md and
sources.jsonl.

## Result

The fixed nontrivial cp phase has a nonzero continuation at every stage under
scalar ratio BC, MSR and norm-only cylinder covariance. An explicit rational
recurrence makes the total non-timid transition modulus less than 2^-n at
parent size n>=3. This avoids all zero weights and bounds total variation.
Completing finite histories by timid tails gives atomic measures whose
successive TV differences are summable; their l1 limit is a countably additive
labelled scalar measure with all prescribed cylinder amplitudes and mass one.

Within locally isomorphism-invariant nonzero scalar Markov rules, BC forces
t(C,P)=q(C)w(P), MSR forces its recursion, and norm covariance is equivalent
to a common |q(C)| per cardinality. Necessity is the modulus adaptation of
the classical maximal-element replacement argument. No unrestricted
classification, full vector/DF covariance or operator QBC claim.

A second explicit variant sets late q_n=10^-n and regards the early shape
phases as a finite perturbation of a real-percolation inverse weight. Ideal-
lattice Möbius inversion bounds its weight correction by 51n^2, while the
reference weight is at least 9^n; hence all weights remain nonzero. The
complete transition-row distance is at most 51n^2/5^n, summable. Conditional
reference continuations give L1(P0)-Cauchy densities. The resulting complex
measure is absolutely continuous with respect to the non-atomic reference,
and |nu| assigns zero mass to all eventually-timid histories. This removes
the atomic-support feature without claiming physical realism.

## Checks and independent review

Own exact Gaussian-rational implementation, without worker/seed imports:
407 nonzero transitions and all 1619 scalar product-BC equations through
parent size four / five births, full finite norm-GC, intrinsic-past product,
seed values, summable proper-transition upper bounds, and persistent cp
holonomy. Atomic-padding differences checked on common finite refinements.
Rerun is byte-identical. This finite enumeration corroborates the proof.

Gibbs independently rederived the recursion, counts, lower/upper bounds,
necessity/sufficiency proposition and the l1 completion argument. It explicitly
checks coincident timid-tail supports and limits the covariance claim. No
fatal flaw found. PERCOLATION_REVIEW.md separately rederives the Möbius
perturbation support, all-stage nonzero and row-distance bounds, L1 density
completion, and zero variation on eventually-timid histories. The separate
finite checker compares ideal recursion and Möbius inversion exactly through
five births, checks all 1619 BC equations and the seed phase, and verifies
the rational series sum 4437/800. Analytic induction and the summable TV estimate establish
infinite-stage statements; no finite sample is offered as their proof.

## Source and novelty boundary

Primary sections and versions recorded in RESULT.md/sources.jsonl. Prior work
already supplies gregarious factorization, the intrinsic-past covariance
argument, norm-only phase freedom, and bounded-variation extension machinery.
The current explicit seed/recurrence combination is not assigned a priority
verdict. Two narrow web queries and reading primary definitions are not a
systematic defeat search. An independent mathematical review does not certify
novelty or physical applicability.

## Limitations

The first construction engineers summable escape and is supported on
eventually-timid histories. The second, percolation-dominated construction
is not; its |nu| gives that set zero mass. Both use deliberately selected
late rates and weaker cylinder norm covariance. No continuum
limit, embedded observer, physical passage, ordinary probability transition
law, normalized orthogonal-history register, empirical discriminator or
philosophical bridge is established. The full scalar-percolation classification
is unchanged. No dependency installs or large computations.
