# Renewal inversion: a conditional obstruction for the rank probe

Coordinator follow-up, 2026-10-21. This is a routine renewal-series reduction,
not a claimed classification or new general theorem. It gives a sharper target
than roots of truncated polynomials. It has not undergone independent review.

Keep the rank report's first-next-post coefficients R_k, with R_1=p. Let b_k be
the corresponding bridge coefficient allowing intermediate posts: start with a
specified principal past, append k elements, and require its old maximum and
the new maximum to be posts within this finite interval. Divide out the fixed
past amplitude symbolically, rather than dividing a zero numerical value.
Set b_0=1. For k≥2,

`b_k = sum_{naturally labelled T, |T|=k-1} A_p(T) p^{M(T)+min(T)}`.

The formula for R_k is the same sum restricted to T with no posts. The special
k=1 term is p, not the empty-T expression. Natural labels, or equivalently
shape multiplicities, are essential.

Decompose each bridge at its first post after the specified old maximum. This
is unique. The ordinal-sum decomposition has no cross incomparable pairs;
its cross covers are already accounted for by the minimum-element factors.
The two segments' amplitude weights multiply, and labels concatenate without
an interleaving multiplicity. Thus, as formal power series,

`b_n = sum_{k=1}^n R_k b_{n-k}`,
`U(z)=1+sum_{n>=1} b_n z^n`, `R(z)=sum_{k>=1}R_k z^k`,
`U(z)(1-R(z))=1`.

At every z where both series converge absolutely, the same identity holds
numerically. In particular **R(z)=1 is impossible there**. A geometric rank
sequence κ_n=λ^n cannot solve the proposed harmonic recurrence at a point λ in
that common absolute-convergence domain. This does not exclude singular or
boundary cases, and supplies no convergence radii by itself. The classical
R(1)=1 for 0<p≤1 is consistent: U diverges at z=1.

A stronger conditional statement also handles non-geometric sequences. Suppose
κ_n=sum_{k>=1}R_k κ_{n+k} and, for each n, the sums

`sum_{j>=0}|b_j κ_{n+j}|` and
`sum_{j>=0,k>=1}|b_j R_k κ_{n+j+k}|`

are finite. Multiply the recurrence at n+j by b_j and sum j. Absolute
convergence permits rearrangement; the renewal convolution cancels every term
except κ_n. Therefore κ_n=0 for every n. A normalized infinite-post measure
cannot have all these principal-event values zero, by the laminar-cover
argument in the separately audited conditional theorem.

For example, sufficient hypotheses are `|κ_n|≤Cρ^n` and absolute convergence
of U and R at ρ. The existing variation bound supplies an exponential upper
bound on κ, but **does not establish these two series converge at the needed
ρ**. Establishing an appropriate weighted convergence bound, or showing why it
fails, is the substantive next analytic obligation. Do not turn this conditional
obstruction into a no-go for all rank factors.

`check_renewal_series.py` independently enumerates finite forward-edge closures
and verifies the bridge/first-post convolution through degree five at p=0,1,
1/2,(1+i)/2 and −1 with exact rational Gaussian arithmetic. All 25 coefficient
identities passed. It imports only the coordinator's independent finite helpers.
These finite checks corroborate the decomposition; they do not prove convergence
or the infinite measure-extension statement.
