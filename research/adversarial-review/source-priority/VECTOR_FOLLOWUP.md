# Adversarial source-priority review: norm-only Hilbert and Banach candidates

Checked 2026-10-21. This is a bounded nearest-prior-art and substantive-scope
review of the two coordinator candidates. It does not certify priority, audit
the full analytic proofs, or imply a physical or ontological result.

## Strongest defeater first: the vector problem is deliberately much weaker than Sorkin's

Rafael D. Sorkin, “Toward a ‘fundamental theorem of quantal measure theory’,”
arXiv:1104.0997v2 (8 April 2011),
[primary arXiv HTML](https://arxiv.org/html/1104.0997v2), is the nearest causal-set
quantal-measure predecessor. I read its Introduction and Section 2, especially
the causal-set discussion at printed pp. 5–7 (not the extension proofs in
Sections 6–7). Sorkin fixes the cylinder vector itself as the complex number
`p^L(1-p)^I` in a one-dimensional Hilbert space and asks how that premeasure can
be extended. He distinguishes labelled histories from physical/covariant
histories and motivates extension partly by the latter. The coordinator's
norm-only candidates do not retain those vectors or their finite-union sums;
they ask for some new measure whose cylinder norms happen to match the
amplitude moduli. No result in the targeted Sorkin read classifies this weaker
problem, but neither construction resolves Sorkin's extension problem.

The Hilbert construction even supplies a different decoherence functional:

`D(E,F) = <mu(E),mu(F)> = E[P_env(E) P_env(F)] >= 0`.

This has nonnegative real off-diagonal terms, so its interference is only
constructive. At `a²+b²=1`, the latent edge probabilities are Bernoulli
0/1; conditional histories are deterministic and `Q(E)=D(E,E)=P_r(E)` is the
ordinary additive classical measure. For real `p∈[0,1]`, the environment is
deterministic and `Q(E)=P_p(E)^2`, a rank-one real decoherence functional.
Interior nonreal parameters give mixtures of such classical rank-one
functionals. These are valid mathematical decoherence functionals if one
chooses to call them that, but they do not reproduce complex-percolation
interference, its off-diagonal data, vector phases, covariance, or Bell
causality. This makes “extension of complex percolation” a misleading
description.

## Hilbert candidate: exact disk is a standard construction plus the project's obstruction

The proposed locus `a²+b²≤1`, equivalently `|p−1/2|≤1/2`, has a transparent
one-edge interpretation. Put `x=Re(p)` and `y=Im(p)`. The construction asks for
a random variable `G∈[0,1]` with `E G=x` and `Var(G)=y²`; then
`E G²=a²` and `E(1−G)²=b²`. Feasibility is precisely
`y²≤x(1−x)`, the bounded-range variance condition. The three-point law in the
candidate is a direct interpolation between deterministic `G=x` and a
Bernoulli-`x` variable. Independent copies per edge, ordinary conditional
probability and the familiar CTP cylinder factorization then give the
Hilbert-valued map. This is a textbook-level moment construction, not a new
random-environment or conditional-expectation principle.

One possible one-edge table is
`[[a²,d],[d,b²]]`, where `d=(1−a²−b²)/2=x(1−x)−y²`.
The disk criterion here is **entrywise nonnegativity** `d≥0`, i.e. feasibility
as a classical paired-outcome kernel or as `E[G(1−G)]`. Positive-semidefiniteness
alone is not a disk criterion: the determinant is `y²` and the Gram matrix can
remain positive semidefinite outside the disk. Likewise the moment matrix's
PSD condition alone says only `Var(G)≥0`; it does not impose the upper bound
from `G∈[0,1]`.

The sufficiency is therefore an immediate application of standard positive
probability machinery. The exact outer no-go is more specific: the candidate
applies the Hilbert signed-sum/Rademacher bound to the already-derived two-cap
level sum with squared weights, obtaining divergence when `a²+b²>1`. That
particular causal-set estimate is a substantive parameter-specific deduction;
it is not supplied by the random-environment construction or by the standard
moment bound. It still looks like a short extension of the project's existing
two-cap calculation, not an independent Hilbert-space method.

The most useful standard vector-measure source found is Diestel and Uhl,
*Vector Measures*, AMS Mathematical Surveys 15 (1977), pp. 2–3 and 7–8
(targeted full-text read via a public scan mirror; the [AMS record](https://doi.org/10.1090/surv/015)
is official). Examples 6–7 distinguish bounded semivariation from bounded
variation; Example 16 gives the countably additive indicator measure into
`L^p`, `1<p<∞`, with infinite variation. This supports the general Hilbert
measure mechanism, not the CTP-specific disk classification.

**Disposition:** mathematically **survives** as an exact classification for
the chosen norm-only Hilbert existence question, assuming the coordinator's
necessity proof. As a contribution to causal-set quantum measure theory it
should **shrink to an appendix or technical scope note**: it uses classical
conditional histories and a new, highly non-unique off-diagonal functional.
It does not merit a separate note on the evidence reviewed. It could be useful
as a compact demonstration that the scalar variation obstruction depends on
phase-preserving scalar/vector data, but should not be marketed as a new
quantum extension.

## Banach candidate: c0 coordinates are a generic representation recipe

The closest read primary mathematical work is José Rodríguez, “On vector
measures with values in `c0(κ)`,” arXiv:2404.05407v1 (8 April 2024),
[primary arXiv HTML](https://arxiv.org/html/2404.05407v1). I read the full
relevant statements and proof passages in §§2–3; this was not a proof audit of
the entire paper. Theorem 3.3(i) states that a map into `c0(κ)` is countably
additive exactly when all coordinate scalar measures are countably additive.
The paper concerns factorization and `L1` spaces of vector measures, not
prescribed norms of causal-set cylinders, so it is not an exact predecessor.
But it confirms that the c0 coordinate framework and its countable-additivity
logic are standard vector-measure structure.

The candidate's
`mu(E)=(w_C P_r(E|C))_C`
is a tailored instance of that familiar method. The role of `c0` is to let
coordinate weights vanish with cylinder rank; finite many large coordinates
are handled by scalar continuity of conditional probabilities, and the tail
coordinates are uniformly small. A coordinate indexed by `C` then witnesses
the required norm on that cylinder, while nesting and monotonicity show other
coordinates do not exceed it. The parameter classification is obtained by
simple disjoint-cylinder obstructions plus this weighted-coordinate
embedding. For the “every cylinder” prescription, the strict interior has an
even simpler indicator-in-`L^α(P_r)` construction with `a^α+b^α=1`; that is
again a direct scalar probability reweighting.

The DP-only boundary difference at `b=1` is the most specific part: retaining
only DP coordinates allows a `c0` construction there, while prescribing all
cylinders creates a disjoint family of fixed positive norm and blocks
countable additivity. This is a clean boundary result for the deliberately
abstract problem. The adapted coordinate witnesses and the event algebra
restriction are project-specific; the underlying Banach-space construction is
not.

**Disposition:** mathematical classification **survives** if the coordinator's
proof is accepted, but novelty is **low and bounded**. Treat the `c0` argument
as a general coordinate representation applied to a causal-set weight system,
not as a new Banach-valued extension principle. It merits **at most an
appendix**, and only if the paper needs to state the distinction between
Hilbert and Banach norm-only domains. It does not merit a separate note absent
a substantive theorem about constrained or phase-preserving measures.

## Source search and read-depth limits

Bounded primary-source routes searched on 2026-10-21: targeted web/arXiv queries
for Sorkin's complex-percolation vector measure and extension, conditional
probability as a vector measure, Hilbert/random-environment representations,
`c0`-valued vector measures, and “prescribed norms” with cylinders. Reads:

- **Sorkin 2011**, arXiv:1104.0997v2, Introduction and Sec. 2 causal-set
  setup, printed pp. 1–7; relevant fixed-amplitude vector and labelled vs
  physical scope confirmed. Sections 6–7 and the journal edition were not
  audited. [arXiv version record](https://arxiv.org/abs/1104.0997v2).
- **Diestel–Uhl 1977**, *Vector Measures*, pp. 2–3 and 7–8; targeted full-text
  through a scan mirror. Standard definitions/examples checked; this is not an
  official publisher PDF route.
- **Rodríguez 2024**, arXiv:2404.05407v1, §§2–3 and Thm. 3.3(i); full text of
  the relevant c0 coordinate result read. It is a functional-analysis result,
  not a causal-set source. [Version record](https://arxiv.org/abs/2404.05407v1).

Search terms included variants of `c0-valued vector measure`, `conditional
probability vector measure`, `Hilbert-valued conditional probability`,
`prescribed cylinder norms`, `complex percolation extension`, and Sorkin's
quantal measure terminology. No exact prior source for either exact parameter
classification or its causal-set two-cap application was located. This was a
small targeted search, not a forward-citation review or a global search of
measure-theory books, theses, or unpublished work. I found metadata for
Bhatia–Davis, “A Better Bound on the Variance,” *Amer. Math. Monthly* 107(4)
(2000), 353–357, DOI 10.1080/00029890.2000.12005203, but could not access its
article body in this pass; I do not rely on it as a read theorem. The bounded
variance condition is also immediate from `0≤G≤1` and can be verified
directly.

## Recommendation

Keep the candidate theorems labeled **norm-prescribed** and strictly separate
them from the scalar complex measure. The Hilbert exact disk and Banach/c0
domains appear mathematically correct but are largely standard constructions
plus a specialized disjoint-family obstruction. Their strongest contribution
is explanatory: they show how much the existence region expands when one drops
phase and finite-union amplitude consistency. Given the strictly constructive
interference, absence of covariance/Bell causality, and arbitrary target space,
place them in a concise appendix/scope section if useful; do not lead a separate
paper with them or imply they are quantum dynamics or evidence for an ontology.

Only this report file was created for the follow-up. No coordinator candidate,
source register, checker, board, or other report was changed.
