# Next bounded target: two phase choices, all cylinder magnitudes matched

Candidate design, 22 October 2026. **Not yet independently reviewed or
implemented.** The one-parameter family in FIXED_DATA_CHECK.md is insufficient.
The following may provide a sharper existence test. Treat all bounds below as
a proposal to verify before promotion.

## Exact early seed

Keep q(single)=1/2. Set q(chain2)=v/4 and q(anti2)=u/4. Compare

    model A: v=u=(3+4i)/5,
    model B: v=conjugate(u), with the same u on the antichain.

The early weights are w(chain2)=4/v-2 and w(anti2)=4/u-3. Their moduli agree
between A and B, as do all early |q| values. Hence every cylinder through
three births has the same magnitude in the pair. The stage-three minimum-count
two amplitudes are (4+v-u)/8: 1/2 in A and 1/2-i/5 in B, whose squares differ
by 1/25. The two models are not global complex conjugates. The total Gaussian
norm at stage three is 2 in each.

## Proposed geometric completion keeping magnitudes matched

For each later finite C, let S_C=sum_(P proper ideal C)w(P). Choose a common
large R_n at cardinality n, the same for both models. Pick f(C) such that

    |f(C)|=|f(C)-S_C|=R_n,
    q(C)=1/f(C),        w(C)=f(C)-S_C.

If |S_C|<2R_n the two equal-radius circles intersect. For S_C!=0 an explicit
choice is f=S_C/2+i(S_C/|S_C|)sqrt(R_n^2-|S_C|^2/4); for S_C=0 take f=R_n.
Choose the same deterministic branch rule on induced isomorphism types.
Then |q(C)|=1/R_n and |w(C)|=R_n are matched in both models at every later
stage, and all transitions are nonzero. The intrinsic-past product would
therefore give equal magnitudes on every finite cylinder, not just a cutoff.
MSR and scalar ratio BC follow from the same q(C)w(P) recursion.

A candidate rational majorant schedule is B_2=19/5,
R_n=1+2^(2n+10) B_(n-1), B_n=2R_n. Gaussian norms are bounded by 2R_n and
|S_C|<=(2^n-1)B_(n-1). The proper-transition modulus sum is then less than
epsilon_n=2^(-n-10), whose tail sum from n=3 is 1/4096. The previous atomic
padding argument would give labelled finite complex measures, and a TV distance
from each stage-three timid padding bounded by

    tau <= 2*2*exp(1/2048)/4096 <= 2/2047 < 1/1000.

For the intrinsic completed E2 question, its early amplitudes have moduli
1/2 and sqrt(29)/10<3/5. If the completion changes either amplitude by at most
tau, the completed difference of quantum measures would be at least

    1/25 - (11/5)tau - 2tau^2 > 18899/500000 > 0.

If sound, this would produce a matched-cylinder pair with different values
on a completed intrinsic event. It still uses an engineered, atomic,
eventually-timid completion; it supplies no detector instrument or full vector
covariance. Geometric phase retrieval and the earlier scalar-factorization
machinery are known methods, so no novelty follows just from constructing it.

## Required checks / kills

Independently verify the early seed and covariance, circle formula (including
zero S), recursive isomorphism consistency, both all-stage magnitude claims,
nonzero and total-variation bounds, and the completed-event error inequality.
Check that "same data" means individual cylinder norms, not quantum measures
of every finite cylinder union; fixing the latter would be a stronger task.
The coordinates generally involve square roots, so Gaussian-rational finite
code alone cannot certify the whole construction. Analytic proof and exact
algebraic/interval checks must be distinguished. Reject if the common schedule
cannot be maintained or the invariant event gap is not controlled. Do not
promote this candidate as a result before that review.
