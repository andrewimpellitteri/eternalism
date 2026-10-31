# Independent adversarial review: matched-cylinder pair

Checked 2026-10-22 against `research/longshots/bc-phase-audit/NEXT_STEP.md`, the preceding phase and all-stage records, and the now-present `RESULT.md`, `DATA_BOUNDARY.md`, `PRIOR_WORK.md`, `sources.jsonl`, and `check.py`. I read and audited the proof and checker source; I did not rerun or duplicate the coordinator's checker. This is an independent analytic review, not a claim that the finite checker proves the all-stage result.

## Narrow verdict

The proposed circle construction appears mathematically sound under the stated recursive, scalar, isomorphism-invariant parametrization. The circle formula matches both |q(C)| and |w(C)| across the two models at every later size; the induced transition rules satisfy MSR and nonzero scalar ratio Bell causality; and path factorization gives equality of each corresponding individual labelled-cylinder norm at every finite size. The large-radius schedule gives summable proper-row mass. Crucially, the timid transition has modulus one by the matched-radius condition but its phase is not arbitrary once MSR is imposed: it lies within the proper-transition mass of 1. This is enough for the atomic total-variation completion argument.

The E2 gap lower bound also checks with the claimed orientation and constants, provided “completion changes either amplitude by at most tau” means the absolute error in each completed event amplitude, as follows from the total-variation bound. The result would be a mathematical pair with the same individual cylinder magnitudes and different rank-one quantum-measure value for E2. It would not establish equality of quantum measures on all finite unions, equality of decoherence functionals, or empirical distinguishability. The square-root circle coordinates require their analytic construction; rational/Gaussian-rational checks can verify bounds and finite examples but cannot by themselves certify the all-stage square roots.

## Seed and cylinder magnitudes

Let u=(3+4i)/5, model A have v=u, and model B have v=conjugate(u), while both use the same antichain parameter u. For the size-two parents,

    q(chain)=v/4,  w(chain)=4/v-2,
    q(anti)=u/4,   w(anti)=4/u-3.

The singleton weight is 1. Since |u|=|v|=1 and Re(v)=Re(u)=3/5, the two models match the moduli of both early q-values and both size-two weights. In particular b(w(chain))=18/5, b(w(anti))=19/5, where b(x+iy)=|x|+|y|. All early weights are nonzero.

For a size-three child of the chain parent, the transition amplitudes are v/4, v/4, and 1-v/2, before multiplying by the parent-cylinder amplitude 1/2; these magnitudes are unchanged under v↔conjugate(v). The antichain parent uses the same u in both models, so all of its child amplitudes agree exactly. This verifies the individual-cylinder match through size three. The size-three amplitude sum by minimum count is

    G3(v,u;z)=[(4-v)z+(4+v-u)z^2+u z^3]/8.

Thus A uses v=u and B uses v=conjugate(u). Correction to the earlier review:
I had mis-added the single-minimum cylinder amplitudes and gave an incorrect
coefficient 3/8 for z. The correct coefficient is (4-v)/8; the three
coefficients now sum to 1 as required by normalized MSR. The E2 coefficient
(4+v-u)/8 is unchanged, so its amplitudes remain 1/2 and 1/2-i/5, with
squared-magnitude gap 1/25. These are sums over disjoint cylinders; their
difference does not contradict the matched magnitudes of each individual
cylinder. Independently, the single-minimum group is the chain-parent pair
v/8 and 1/2-v/4, while the two-minimum group combines v/8 with the two
antichain-parent paths u/8 and the antichain timid path 1/2-3u/8. These give
the stated coefficients directly from the stage-three table.

For later sizes, assume recursively that w(P) is defined on each finite isomorphism type and set

    S_C = sum_(P proper down-set of C) w(P),
    f_C = 1/q(C),   w(C)=f_C-S_C.

The sum counts actual down-set subsets, including distinct isomorphic subsets with multiplicity. If S_C is nonzero, set

    f_C = S_C/2 + i (S_C/|S_C|) sqrt(R_n^2-|S_C|^2/4).

If S_C=0, set f_C=R_n. For nonzero S_C,

    f_C-S_C = -S_C/2 + i (S_C/|S_C|) sqrt(R_n^2-|S_C|^2/4).

The terms in each expression are perpendicular in the complex plane, so |f_C|=|f_C-S_C|=R_n. The S_C=0 rule gives the same result. Thus |q(C)|=1/R_n and |w(C)|=R_n in both models, though their phases and their values of f_C, q(C), and w(C) need not agree.

### Circle existence and recursive consistency

With B2=19/5, R_n=1+2^(2n+10)B_(n-1), and B_n=2R_n, induction gives b(w(P))≤B_(n-1) for every smaller poset P. The base case follows from the early values. If it holds below n, then

    b(S_C) ≤ (2^n-1) B_(n-1) < 2R_n,

so |S_C|≤b(S_C)<2R_n and the circle intersection exists. Since |w(C)|=R_n, b(w(C))≤sqrt(2)R_n<2R_n=B_n, closing the induction. R_n>0, so f and q do not vanish; the equal-radius identity also gives w(C) nonzero.

For isomorphism consistency, take q at sizes zero through two as specified by the seed. At size n, if q and w below n depend only on induced isomorphism type, the actual-subset sum S_C is invariant under every isomorphism of C. The stated rule is a deterministic function of S_C and n, including its explicit S_C=0 branch. Therefore f, q, and w depend only on the isomorphism type of C. This proves recursive consistency provided the construction is defined on each finite isomorphism type; it does not give a closed-form expression for the resulting phases.

For a parent C and precursor P, t(C,P)=q(C)w(P) is nonzero. MSR follows directly:

    sum_(P down-set of C) t(C,P)
      = q(C)(S_C+w(C)) = q(C)f_C = 1.

For a Bell pair with precursors P,Q and union B, the scalar ratio is

    t(C,P)/t(C,Q) = w(P)/w(Q) = t(B,P)/t(B,Q),

with nonzero denominators. This is the specified scalar ratio BC, not a result about operator-valued QBC or general phase-modified Bell causality.

For corresponding labelled paths in the two models, every transition modulus matches: q at a parent of size at least three has modulus 1/R_n in both models; early q moduli match by type; w at a precursor of size at least three has modulus R_k in both models; and all smaller precursor moduli match by the seed calculation. Multiplying transition moduli proves equality of every corresponding individual labelled-cylinder norm at every finite stage. The same path product gives norm covariance over different natural labelings of a fixed finite causet: the q-modulus product depends only on the sequence of parent cardinalities, while the w-modulus product depends only on intrinsic past types. This does not imply equality of amplitudes or of norms of arbitrary finite unions, which involve phase-sensitive cross terms.

## Proper-row and atomic completion audit

At size n, the proper-transition modulus sum obeys

    e(C) = (1/R_n) sum_(P proper down-set of C) |w(P)|
         ≤ (2^n-1)B_(n-1)/(1+2^(2n+10)B_(n-1))
         < 2^(-n-10) = epsilon_n.

The strict inequality follows from 2^n-1<2^n and the dominant 2^(2n+10)B_(n-1) term. Hence sum_(n≥3) epsilon_n=1/4096.

A point worth stating explicitly is that t(C,C)=q(C)w(C)=w(C)/f_C has modulus one, but its phase cannot be chosen freely while preserving this MSR construction. MSR gives

    t(C,C)=1-sum_(P proper down-set of C)t(C,P),
    |t(C,C)-1|≤e(C)<epsilon_n.

Thus |t(C,C)-1|+sum_proper |t(C,P)|≤2e(C). A proof using only |t(C,C)|=1 would not give a summable TV bound; the MSR identity is essential and supplies it.

Let V_n be the sum of |A(C)| over labelled size-n histories. From each parent row, sum_P |t(C,P)|≤|t(C,C)|+e(C)≤1+2e(C), so

    V_n ≤ V3 product_(k=3..n-1)(1+2epsilon_k)
        ≤ V3 exp(2/4096).

At size three the sum of Gaussian norms b of the seven labelled-path amplitudes is 2 in each model: two chain proper paths each have b=7/40, its timid path has b=11/20, three antichain proper paths each have b=7/40, and its timid path has b=23/40. Since complex modulus is at most b, V3≤2.

Complete each finite labelled C by adding universal tops forever and denote the path h_C. The timid child has the same padded path as its parent. Therefore

    ||nu_(n+1)-nu_n||_TV
      ≤ V_n sup_(|C|=n)(|t(C,C)-1|+e(C))
      ≤ 2 epsilon_n V_n.

This remains valid if padded supports from different stages coincide, by applying the triangle inequality after atom aggregation. Summing gives, for each model,

    ||nu-nu_3||_TV
      ≤ 2·2 exp(1/2048) sum_(n≥3)epsilon_n
      = exp(1/2048)/1024
      ≤ 2/2047 < 1/1000.

Here exp(x)≤(1-x)^(-1) for 0≤x<1 gives the rational upper bound. The l1 space on the countable set of padded histories is complete, so summable increments give a countably additive atomic complex measure. Every fixed finite cylinder eventually has its prescribed value by iterated MSR and deterministic padding. This yields a finite scalar measure on the labelled cylinder sigma algebra under these estimates; it does not establish full vector or decoherence-functional covariance.

## E2 gap and constants

Universal tops are nonminimal, so h_C is in E2 exactly when C already has two minimal elements. Consequently nu3(E2) is the size-three E2 amplitude above. Total-variation control implies

    |nu(E2)-nu3(E2)| ≤ ||nu-nu3||_TV ≤ tau,
    tau ≤ 2/2047 < 1/1000.

Set a=nu3_A(E2)=1/2 and b=nu3_B(E2)=1/2-i/5. Then |b|^2-|a|^2=1/25. Reverse and direct triangle inequalities give

    |nu_B(E2)|^2-|nu_A(E2)|^2
      ≥ (|b|-tau)^2-(|a|+tau)^2
      = 1/25 - 2(|a|+|b|)tau
      > 1/25 - (11/5)tau.

The proposal's weaker bound subtracts an additional 2tau^2, so it is valid too. Since |b|=sqrt(29)/10<3/5 and tau<1/1000,

    1/25-(11/5)tau-2tau^2
      > 1/25-11/5000-1/500000
      = 18899/500000 > 0.

The sign is model B minus model A. Thus the completed rank-one quantum-measure values remain separated. The estimate treats the completion errors independently and is conservative; it is not an exact enumeration of the completed event.

## Defeat attempts, interpretation, and limits

I find no algebraic counterexample to the proposed construction in NEXT_STEP.md. The circle formula handles S_C=0 explicitly; the large radius guarantees existence; the deterministic rule on isomorphism types gives isomorphism consistency; the MSR-controlled timid phase permits summable atomic completion; and the E2 gap constants survive the stated error bound.

The narrow verified statement is conditional on defining the recursion for all finite poset isomorphism types, counting actual precursor subsets with multiplicity, and using the same R_n and branch rule in both models. It gives a candidate pair with equal individual labelled-cylinder magnitudes at all finite sizes and unequal completed E2 rank-one quantum-measure values. Equality of individual cylinder norms is weaker than equality of quantum-measure values for finite unions: unions involve phase-sensitive cross terms, and the supplied pair-union counterexample demonstrates this directly. The pair is not shown to have equal decoherence functionals; the early E2 amplitudes already differ in relative phase.

The geometric phase construction, scalar Bell/MSR factorization, and summable-variation/atomic completion are recognizable adaptations of established machinery already discussed in the prior phase audit. This review validates a candidate application, not originality or global priority. An engineered eventually-timid atomic completion is not evidence of a realistic causal-set cosmology. No detector, readout instrument, or operational map is specified, so the E2 measure gap is not a demonstrated empirical prediction. Nor does the construction show a pure gauge transformation or a consequence for temporal ontology.

The supplied checker is appropriately described as bounded support: its exact seed arithmetic and outward-rounded dyadic intervals check the listed finite cases and residuals, while the analytic recursion proves existence and identities at all stages. Code inspection found no contradiction in its interval operations or finite checks. This review did not execute it, so the reported PASS is treated as coordinator-reported rather than independently reproduced. The checker cannot establish the all-stage result by itself, and the proof in `RESULT.md` must carry that burden.

## Phase-retrieval predecessor check

I also read the primary passages listed in the lane’s now-present `PRIOR_WORK.md`. Balan–Casazza–Edidin, published version, Sec. 2 Theorem 2.8 (pp. 351–352), characterizes injectivity of real-frame magnitude measurements by the complement property; Conca–Edidin–Hering–Vinzant, arXiv:1312.0158v1, Eqs. (1)–(2) and Theorem 1.1, defines complex-frame intensity measurements modulo global phase and proves generic injectivity for at least 4M−4 measurements. These results show that magnitude-data reconstruction is governed by the measurement family: magnitude loss can be non-injective in some designs and injective in others. Neither result is directly a theorem about the constrained causal-set cylinder map, its scalar BC/MSR recursion, or completed-history event measures. The proposed pair, if verified, is a concrete ambiguity for its particular family of cylinder measurements, not a general phase-retrieval theorem or an application of the frame thresholds. The primary records and limits are listed in `research/longshots/bc-matched-norms/sources.jsonl`.

The prior `bc-phase-audit/PRIORITY_REVIEW.md` verdict remains the right novelty baseline: scalar factorization and extension are known machinery, and SS already states the norm-only phase option. Adding equal cylinder magnitudes plus an E2 distinction could be a useful constrained counterexample to inferring completed-event values from individual cylinder norms, but it does not establish priority against all measure-theoretic or quantum-history predecessors. No new source search was performed.

## New proof and checker audit

I checked the all-stage proof in `RESULT.md` against the construction rather than relying on the finite enumerator. The induction is coherent: the bound on b(S_C) makes the circle radicand strictly positive; the chosen perpendicular component gives |f|=|f-S|=R_n; the explicit zero-S branch is valid; and actual-ideal multiplicity preserves isomorphism invariance. The seed and the common later radii imply matched |q| and |w| factors, hence matched individual cylinder norms. The displayed scalar BC identity follows from the factorization and nonvanishing. I found no counterexample to those steps.

The proof also correctly treats the timid phase. Its modulus being one would not alone control the padding error. Here MSR gives t(C,C)=1-sum_(P proper)t(C,P), so |t(C,C)-1| is bounded by the proper-row mass. The row variation estimate, product bound on V_n, and summable l1 increments then yield the stated finite atomic extension. The event formula for E2 is measurable because M_N is nondecreasing, and universal tops preserve minima. The tail error is bounded in variation before squaring; the stated lower bound follows from the two amplitude errors. I found no defect in the constants or limiting step.

I also find both new `DATA_BOUNDARY.md` claims valid under their stated hypotheses. For finite complex measures, lambda=|nu_A|+|nu_B| is finite and cylinder-algebra sets approximate every generated measurable set in lambda measure. This makes each nu_j continuous under that approximation, and therefore equality of |nu_j(E)|² on the algebra extends to all generated events. To recover each finite-union value from singles and pair unions, refine to one common-depth disjoint cylinder partition and sum the diagonal terms and pairwise real cross terms; the stated identity is exact. This is stronger than needed for the E2 gap and correctly identifies the information boundary.

The normalized scalar polarization corollary is also sound. Decomposing E,F into the two set differences E without F, F without E, and their intersection gives the displayed real inner product from four diagonal event values. Taking F=X and nu(X)=1 fixes Re nu(E). The same identity then fixes Im nu(E)Im nu(F) for every pair. If all imaginary parts vanish the measures coincide; otherwise one nonzero reference fixes a single common sign, yielding nu_B=nu_A or nu_B=conjugate(nu_A) on every event. Normalization removes a general constant phase. This conclusion requires scalar rank-one measures and equality of diagonal values for all measurable events; it says nothing about a general vector-valued decoherence functional. Since the pair's depth-three union values differ, this uniqueness corollary does not collapse the example into identity or conjugation.

Finally, the unit-timid atomicity claim is valid as stated for an existing finite complex-measure extension. Continuity from above forces the nested-cylinder amplitudes to converge to the singleton mass; unit-modulus timid factors fix that atom's magnitude at |A(C)|, although they do not by themselves force phase convergence. At each fixed depth the padded paths are distinct, so their atom magnitudes sum to V_n. The generating cylinder partitions characterize total variation: approximate any finite measurable partition in |nu|-measure, disjointize the approximants, and refine to one depth. Thus sup_n V_n=||nu||_TV. The countable set of padded paths consequently carries the full variation measure. The necessary caveat is already present: the lemma assumes a finite extension exists; it does not construct one from unit timid modulus alone.

No meaningful defect surfaced in the claimed circle construction, completion, E2 estimate, or these two data-boundary corollaries. The key limitations remain scope limitations: this is a scalar norm-only cylinder match, not equality on all finite unions, not a full decoherence-functional equivalence, and not an operational/empirical prediction without a specified instrument. The checker is bounded finite evidence; all-stage validity rests on the analytic proof.
