# Candidate rank-factor classification: renewal inversion with variation control

Coordinator derivation, 2026-10-21. **New proof candidate; independent analytic
and priority review required.** This weakens the value assumption of the
conditional common-factor theorem. It is not an unconditional covariant theorem
or a result about temporal ontology.

## Exact statement

Use the covariant posts algebra and principal-past events D_H of
`research/creative/COVARIANT_RESULT.md`. Write `N(H)` for the number of distinct
natural labelings and `A_p(H)=p^L(1-p)^h`. Require a finite-valued countably
additive complex measure ν with `ν(Ω)=ν(P_infinity)=1` and finite numbers κ_n
such that, for **every principal H** of size n,

`ν(D_H)=κ_n N(H) A_p(H)`.

**Candidate theorem.** Such a measure exists iff `0<p≤1`.

Classical sufficiency uses the already-audited common-factor construction,
which is a special case. The new obligation is nonclassical necessity with
arbitrary rank dependence. All-principal values, finite complex countable
additivity and normalization on infinitely many posts remain essential.

## Notation and finite combinatorics

Put `a=|p|`, `b=|1-p|`, and let

`W_n=sum_{labelled principal H, |H|=n} a^{L(H)} b^{h(H)}`.

Equivalently sum over unlabelled H with N(H) multiplicity. This is a **positive
absolute level sum**, distinct from the complex bridge coefficients below.
For nonclassical p, a,b>0 and t=a+b>1. The existing two-cap bound gives, for n≥2,

`W_n ≥ a t^{n-2} c_s`, `s=b/t`, `c_s=product_{j≥1}(1-s^j)>0`.  (1)

A segment S of k new elements after a specified old post ends in a new post
when S is principal. For it to be the *next* post, S must have no post other
than its maximum. Define the segment weight

`w(S)=A_p(S) p^{min(S)}`,

where the extra power accounts for covers from the old maximum to S's minimal
elements. In particular the singleton segment has weight p. Sum over naturally
labelled segments (or over shapes with multiplicity):

`R_k=sum_{next-post S, |S|=k} w(S)`,
`K_k=sum_{next-post S, |S|=k} |w(S)|`.

Thus `|R_k|≤K_k`. Let B_0=1 and let B_j, j≥1, sum w(S) over **all** principal
segments of size j, allowing intermediate posts; B_1=p. Unique decomposition
at the first new post gives the finite convolution

`B_m=sum_{k=1}^m R_k B_{m-k}`.  (2)

Each decomposition is an ordinal sum, so natural labels concatenate without
an interleaving factor. Cross covers are exactly the minimum-element seam
already included in w. This is the formal identity established separately in
RENEWAL_OBSTRUCTION.md; no convergence is used in (2).

## Variation provides the missing absolute convergence

Let T=||ν||_TV. At a fixed rank n, the D_H are pairwise disjoint, so

`W_n |κ_n|≤T`.  (3)

For each H, its next-post D_J events partition D_H: infinitely many posts
guarantee a next post; the finite J determines its preceding post and hence H.
Across all H of rank n these child events are also disjoint. Ordinal-sum
factorization gives `N(J)=N(H)N(S)` and `A_p(J)=A_p(H)w(S)`. Therefore

`W_n sum_{k≥1} K_k |κ_{n+k}| ≤ T`.  (4)

This is stronger than bounding κ one rank at a time. It sums the absolute
values of the **actual next-post events**, not absolute values of a complex
series inferred from cancellation. Countable additivity likewise gives,
for p≠0 (divide using a chain past at rank n),

`κ_n=sum_{k≥1} R_k κ_{n+k}`.  (5)

The series is absolutely convergent by (4). No assumption that the unweighted
series R(1) converges or diverges has been made.

Suppose, for some n, the deterministic comparison sum is finite:

`sum_{j≥0} |B_j|/W_{n+j}<infinity`.  (6)

Then (3) makes `sum_j |B_j κ_{n+j}|` finite, and (4), with |R_k|≤K_k, gives

`sum_{j≥0,k≥1} |B_j R_k κ_{n+j+k}| ≤ T sum_j |B_j|/W_{n+j}<infinity`.  (7)

Multiply (5) at n+j by B_j and sum. Fubini is now justified by (7). Using (2),

`sum_{j≥0} B_j κ_{n+j}`
`= sum_{m≥1} κ_{n+m} sum_{j=0}^{m-1} B_j R_{m-j}`
`= sum_{m≥1} B_m κ_{n+m}`.

Only the κ_n term differs, so **κ_n=0**. It remains to prove (6), not to assume
it from a root search or an unspecified convergence radius.

## Uniform bridge bounds from inclusion-exclusion

B_j is the complex finite percolation weight on vertices 0,...,j for which 0
is below every vertex and j is above every vertex. In the forward-edge matrix,
this event is exactly: every noninitial column has an incoming edge and every
nonfinal row has an outgoing edge. Induction forward/backward proves these
conditions equivalent to reachability from 0 and to j.

Inclusion-exclusion on zero rows I and zero columns J gives

`B_j=sum_{I,J} (-1)^{|I|+|J|} q^{e(I,J)}`, `q=1-p`,  (8)

where e is the number of forward edges incident to a selected row or column.
Each row/column degree is one of 1,...,j. Since an edge is counted at most twice,

`e(I,J)≥(sum selected row degrees + sum selected column degrees)/2`,
`e(I,J)≤j(j+1)/2`.

The free edges sum to (p+q)=1; thus (8) is a polynomial identity valid for every
complex p, not a positive-probability inference outside the real interval.
Consequently:

- If 0<b<1, `|B_j|≤[product_{d=1}^j(1+b^{d/2})]^2≤C_b<infinity`.
  The infinite product is finite because sum_d b^{d/2} converges.
- If b=1, `|B_j|≤4^j` (there are 2^j row choices and 2^j column choices).
- If b>1, `|B_j|≤4^j b^{j(j+1)/2}`.

All bounds include j=0 with B_0=1.

## Checking the comparison sum in all three regimes

### 0<b<1

Combine bounded B_j with (1). Since t>1, (6) holds for every n≥2. Hence κ_n=0
for all n≥2, and (5) then gives κ_1=0.

### b>1

The principal star on N vertices (an (N−1)-antichain capped once) gives

`W_N≥a^{N-1} b^{(N-1)(N-2)/2}`.

At N=n+j, the inclusion-exclusion bound gives

`|B_j|/W_{n+j} ≤ a^{-(n-1)} b^{-(n-1)(n-2)/2}
                  [4/(a b^{n-2})]^j`.

Choose n large enough that a b^{n-2}>4. Thus (6) holds for **every sufficiently
large n**, proving κ_n=0 on a whole tail. Equation (5) then propagates zero
backward to every smaller positive rank. No nonzero tail survives.

### b=1

Here a>0. Put m=floor((N−2)/2), δ=N−(2m+2) in {0,1}. Choose arbitrary edges
from a fixed m-element lower antichain to a fixed m-element upper antichain,
and append two universal caps plus δ additional caps. Every edge choice gives
a distinct naturally labelled DP order of size N. The bipartite order has
|E| covers and at most 2m maxima. The capped order therefore has
`L=|E|+M+1+δ`. Since b=1, summing positive weights over these orders yields

`W_N ≥ a^{1+δ} min(1,a)^{2m} (1+a)^{m²}`.  (9)

This bound grows like exp(c N²−O(N)) for fixed a>0. It dominates 4^j at
N=n+j, so (6) holds for every fixed n≥2. Thus all κ_n vanish as above.
This step uses only a small explicit bipartite family, not an asymptotic count
of all posets or an extrapolation from finite enumeration.

## Contradiction and endpoints

For every nonclassical p, the appropriate case proves κ_n=0 at every rank.
Hence every D_H has value zero. These events are a countable laminar cover of
P_infinity; finite unions have value zero by their finite intersection formula,
and continuity from below gives ν(P_infinity)=0. This contradicts normalization.
It would be invalid to infer this merely from an arbitrary union of complex
null sets; laminarity is the justification, as in the audited common-factor proof.

At p=0, every principal amplitude at rank n≥2 vanishes. Those D_H still form a
countable laminar cover of P_infinity, so the same normalization contradiction
holds independently of κ_1. For real 0<p≤1, the previously constructed classical
measure with constant κ_n supplies sufficiency. This completes the candidate iff.

## Scope and falsifiers

The indispensable new steps to challenge are (4), the bridge polynomial identity
(8), the rank-offset comparison for b>1, and the bipartite bound (9). A missing
multiplicity, overlap of child events, incorrect interpretation of the first
post, or unjustified interchange would defeat the proof. Equations (3)-(7)
explicitly isolate the absolute-convergence obligation. The elementary finite
checks are corroboration; they do not establish the infinite theorem.

Priority is not established. Renewal identities, inclusion-exclusion and
variation are standard tools. The claimed delta is a classification under the
**rank-only all-principal value rule**, weaker than the existing common-factor
rule. It does not classify arbitrary covariant measures, DP-only rules, or
shape-dependent factors, and supplies no empirical or ontological conclusion.
