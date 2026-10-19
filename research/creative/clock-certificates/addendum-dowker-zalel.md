# Independent skeptic addendum: repeated doubly-principal blocks

**Status:** proof audit of a candidate application, not an accepted novelty or a
claim about ontology. The result below is conditional on the extension problem
being exactly the one posed in Dowker–Zalel: extend the prescribed CTP cylinder
pre-measure from doubly-principal cylinder generators to
\(\tilde{\mathcal R}_p\). It does not establish non-extension on the covariant
intersection \(\mathcal R_p\).

## 1. Claim under review

At \(p=(1+i)/2\), \(q=1-p=(1-i)/2\), the suggested finite block family gives
a lower bound growing exponentially in the number of blocks. For the
doubly-principal algebra the block is a five-element principal causet capped
with a universal new maximum, hence has six elements. If the listed finite
enumeration is correct, its total absolute amplitude is
\[
 r_{6,dp}=|p|r_5=\frac9{16}+\frac{105}{128\sqrt2}>1.
\]
Concatenating \(m\) such blocks above one initial element gives a finite,
pairwise-disjoint family of doubly-principal cylinders whose absolute
amplitudes sum to \(r_{6,dp}^{m}\). This contradicts bounded variation of any
finite complex-measure extension.

## 2. Closest primary predecessors and comparison

1. Dowker, Johnston, and Surya, [*On extending the Quantum Measure*,
   arXiv:1007.2725v1 (2010), Sec. 2 and Sec. 4](https://arxiv.org/abs/1007.2725).
   They establish bounded variation as a necessary condition for extension of
   the relevant finite-dimensional vector/complex pre-measure and prove
   non-extension for complex percolation on the full cylinder sigma algebra
   unless the parameter is real and non-negative. That result covers the
   larger unrestricted cylinder algebra; it does not by itself establish
   non-extension on the smaller doubly-principal-generated algebra.
   **Read depth:** full-text; the bounded-variation implication was checked at
   the displayed argument in Sec. 2.
2. Surya and Zalel, [*A Criterion for Covariance in Complex Sequential Growth
   Models*, arXiv:2003.11311 (2020)](https://arxiv.org/abs/2003.11311).
   This supplies the extension/variation criteria used in the later
   application. Its complex percolation result concerns the model's specified
   event algebra and does not provide this repeated doubly-principal block
   certificate. **Read depth:** full-text; the exact original theorem
   hypotheses and all cited proof dependencies were not independently
   reconstructed here.
3. Dowker and Zalel, [*Observables for cyclic causal set cosmologies*,
   arXiv:2212.01149v2 (17 July 2023), Secs. III.3–III.4 and V,
   Theorems 14–15 and Eq. (31)](https://arxiv.org/abs/2212.01149).
   They define \(\tilde{\mathcal R}_p\) from doubly-principal cylinders and
   explicitly leave the complex-CTP extension question inconclusive: the
   valency-one nodes make their minimum-zeta divergence criterion fail, while
   the maximum criterion does not prove extension. The present candidate
   bypasses that extremal-zeta test with a finite disjoint family. Their
   statement \(\mathcal R_p=\tilde{\mathcal R}_p\cap\mathcal R\) also makes
   clear why a result for \(\tilde{\mathcal R}_p\) alone cannot be transferred
   to \(\mathcal R_p\). **Read depth:** full-text at the cited sections.

Targeted searches for the exact phrase combination “doubly principal,”
“complex percolation,” and “bounded variation,” and searches of the papers'
extension discussions, found no matching repeated-block certificate. This was
not a systematic forward-citation or database review and is not evidence of
priority.

## 3. Finite certificate and algebraic check

For a naturally labeled causet \(C\), write \(L(C)\) for its number of links,
\(R(C)\) for its number of related pairs, and \(M(C)\) for its number of
minimal elements. Its intrinsic CTP cylinder amplitude is
\[
 A(C)=p^{L(C)}q^{\binom{|C|}{2}-R(C)}.
\]
When a principal block is appended above an old principal prefix, the seam
contributes \(M(C)\) additional links. Define its seam-inclusive block weight
by \(B(C):=p^{M(C)}A(C)\). This is the factor contributed by the block in an
ordinal sum, not the intrinsic cylinder amplitude of the block by itself.
For a five-element principal gadget \(G\), the supplied finite enumeration
reports 40 labeled gadgets and the following exponent histogram, where
\(E=L(G)+M(G)+10-R(G)\), so that \(|B(G)|=2^{-E/2}\) at the stated \(p\):

| \(E\) | 5 | 7 | 8 | 9 | 10 | 11 | 12 | 14 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 1 | 3 | 6 | 4 | 11 | 8 | 6 | 1 |

I independently checked this histogram by enumerating the 64 possible
directed relation masks on four ordered labels, retaining only transitive
irreflexive relations, and adjoining a new universal maximum. This small check
does not repeat the separate larger enumeration. The histogram therefore gives
exactly
\[
 r_5=\sum_G|B(G)|=\frac{105}{128}+\frac{9}{8\sqrt2}>1.
\]

For each \(G\), let \(H=G\oplus\{t\}\), where \(t\) is a new top above every
element of \(G\). Since \(G\) has a unique maximum, the new top contributes one
link, five relations, and no new minima. Therefore
\[
 L(H)=L(G)+1,\quad R(H)=R(G)+5,\quad M(H)=M(G),\qquad A(H)=pA(G),
 \quad B(H)=pB(G).
\]
The restriction of \(H\) to its first five labels is \(G\), so \(H\) is
doubly principal under the paper's definition. The 40 choices remain distinct
as naturally labeled six-element orders. Thus their absolute-amplitude sum is
\[
 r_{6,dp}=\sum_H|B(H)|=\frac{r_5}{\sqrt2}
 =\frac9{16}+\frac{105}{128\sqrt2}>1.
\]
The last strict inequality is exact: \(105>56\sqrt2\), as follows by
squaring positive sides (11025 > 6272).

## 4. Repeated-block proof and skeptic checks

Start with the one-element labeled order \(C_0\). Given a tuple
\((H_1,\ldots,H_m)\), form the ordinal sum
\(C_m=C_0\oplus H_1\oplus\cdots\oplus H_m\), using fixed consecutive label
intervals for the blocks. Every checkpoint \(C_m\) is principal: the last
block has a unique maximum, above all earlier elements. It is doubly principal
as well: deleting its last-labeled universal top leaves
\(C_0\oplus H_1\oplus\cdots\oplus G_m\), which is principal. Thus every
checkpoint cylinder is among the generators of \(\tilde{\mathcal R}_p\).

At each seam, every old element is below every new element, so all cross-block
pairs are relations and contribute no \(q\) factor. A cross-block pair is a
link exactly when it joins the previous block's unique maximum to a minimal
element of the new block: there are \(M(H_j)=M(G_j)\) such links. Hence, with
the seam-inclusive block weights,
\[
 A(C_m)=A(C_0)\prod_{j=1}^m B(H_j)
\]
with \(|A(C_0)|=1\), and summing absolute values over all block tuples gives
\[
 \sum_{(H_1,\ldots,H_m)}|A(C_m)|=r_{6,dp}^{m}.
\]
The cylinders are pairwise disjoint: all have the same checkpoint size, and
different tuples induce different orders on at least one fixed label interval.
Consequently the sum is a lower bound on the variation over their union (and
on variation over \(\Omega\)). It tends to infinity. Countable additivity of
a complex measure implies bounded total variation, so no finite complex
measure can extend these cylinder assignments on the sigma algebra containing
these cylinders.

The cancellation concern does not invalidate this bound. The CTP child
sum-rule enforces normalization by complex summation over all children; it
does not cancel absolute values on a finite disjoint family. No multiplicity
factor from unlabeled isomorphism classes is used: the paper's principal nodes
are individual labeled causets, and each of the 40 block choices is counted
once. Within a fixed checkpoint, distinct labeled cylinders are disjoint.

The same seam calculation for the un-capped five-element principal blocks,
using \(B(G)=p^{M(G)}A(G)\), gives \(r_5^m\) on
\(\tilde{\mathcal R}_b\), as a useful consistency check.
The capped construction is the relevant strengthening because each endpoint
is doubly principal. Neither statement rules out extension to the covariant
intersections \(\mathcal R_b\) or \(\mathcal R_p\): extension on a subalgebra
does not imply extension on the larger generated sigma algebra.

## 5. Falsifiers and remaining proof obligations

The candidate fails if any of these checks fails: (a) the intended extension
does not prescribe the CTP amplitude on every doubly-principal generator; (b)
the source uses a nonstandard “complex measure” notion not requiring countable
additivity/bounded variation; (c) one of the 40 masks is not a valid naturally
labeled principal causet or the histogram is wrong; (d) a seam creates more
cross links than the previous unique maximum to new minima; (e) a repeated
checkpoint is not doubly principal; or (f) different tuples yield the same
labeled endpoint. Checks (b)–(f) are addressed by the cited definitions and
the finite argument above; (a) should be matched against the coordinator's
precise formulation of the extension problem before acceptance.

For (d), every new non-minimal element has a predecessor in its finite block;
therefore an old element below it is not a cover. For a new minimal element,
the previous maximum is its only old cover, because every other old element is
below that maximum. For (e), removing the final universal top leaves a
principal ordinal sum, as shown above. For (f), restricting to each fixed
label interval recovers the block order, so the tuple is recoverable.

## 6. Novelty boundary and disposition

**Mathematical status:** the repeated-family lower-bound argument is proved
conditional on the finite histogram and the extension domain described above.
The cap and seam identities are exact. The histogram has a small independent
exhaustive check; it has not been formally certified or independently checked
by a second implementation in this addendum.

**What may be new:** an explicit finite, exponentially amplifying
doubly-principal cylinder family could settle the specific
\(\tilde{\mathcal R}_p\) CTP extension question left inconclusive in
arXiv:2212.01149, at the parameter \(p=(1+i)/2\). I found no direct predecessor
in targeted search, but novelty remains unverified pending systematic
forward-citation/search and a second audit of the finite gadget list.

**What is not established:** no theorem for all non-real \(p\); no result for
the covariant algebra \(\mathcal R_p\); no result about all cyclic models;
no new general measure-extension theorem; and no inference about temporal
ontology. This is a mathematical extension obstruction for a particular
prescribed complex cylinder pre-measure, if the domain match is confirmed.
