# A norm-prescribed infinite-dimensional counterexample

Coordinator analytic check, 2026-10-21. This corrects the scope of the vector
probe without editing its historical builder report. The construction is a
standard indicator-valued vector measure; applying it here is not a new general
vector-measure theorem. See the source-priority review for Diestel–Uhl (1977),
Example 16, pp. 7–8, and its access/read-depth limitations.

Let `q=1-p` and suppose `|p|²+|q|²=1`. Set `r=|p|²`. On the full labelled
history space take ordinary classical transitive-percolation probability `P_r`.
Let `X=L²(Ω,P_r)` and define `μ(E)=1_E`, with equality understood modulo null
sets. Restrict this map to the doubly-principal cylinder-generated sigma-algebra
when that is the target domain.

For pairwise disjoint `E_j`, the difference between the indicator of their union
and the sum of the first `N` indicators has squared norm
`P_r(union_{j>N} E_j)`, which tends to zero. Thus μ is norm-countably additive.
Its total mass is the constant function one, of norm one. For any naturally
labelled cylinder C, with L covers and h incomparable pairs,

`||μ(cyl C)||² = P_r(cyl C) = r^L (1-r)^h = |p^L q^h|²`.

This matches the prescribed norms on all cylinders, not just doubly-principal
ones. In particular `p=(1+i)/2` gives a nonreal example with `r=1/2`.

For any finite disjoint family and coefficients `|α_j|≤1`,
`||Σ α_j μ(E_j)||² = Σ |α_j|² P_r(E_j) ≤1`. Taking Ω attains one. Under the
usual norm-of-simple-integral definition, the semivariation is therefore one.
For nonreal p on the displayed circle, total variation on the restricted domain
is infinite: its finite disjoint doubly-principal cylinder families have norm
sums equal to the scalar modulus sums `V_n`, which diverge by the independently
reviewed two-cap bound. Finite semivariation does not imply finite total
variation in infinite dimension.

This does not contradict the scalar theorem. It prescribes norms, and does not
preserve complex phases, a common vector direction, a decoherence functional or
an interpretation as a physical dynamics. If instead `μ(C)=A_p(C)v` for a fixed
nonzero v, a continuous scalar functional with value one on v reduces the
problem to the scalar no-go.

Every countably additive measure with values in a finite-dimensional space has
finite total variation: choose a basis, take its finitely many scalar coordinate
measures, and bound the norm variation by a finite weighted sum of their scalar
variations. Thus the proposed infinite R² norm-prescribed extension is already
excluded outside `[0,1]`. Finite polygon constructions cannot establish it.
Indeed `(Re A_p(C), Im A_p(C))` already supplies a finitely additive norm-matching
assignment on each finite tree; finite existence is not the missing step.

The general infinite-dimensional classification away from this particular locus
has not been established by this proof. A separate GLM task is examining the
standard finite-Lalpha indicator construction; that is a restricted construction
problem, not a classification of every Banach-valued extension.

`python3 research/adversarial-review/coordinator/check_boundaries.py` independently
enumerates forward-edge masks and their closures, without importing builder
code. For p=(1+i)/2 it checks 407 cylinder identities through n=5 using exact
rational Gaussian arithmetic, as well as partition normalization. These finite
identities corroborate the formula; countable additivity and the infinite
variation conclusion are justified by the analytic arguments above.
