# Independent audit: rank-dependent post factors

Checked 2026-10-21. Verdict: **CONDITIONAL PASS after repair**. The rank-dependent all-principal classification in `research/rank-renewal-convergence/RESULT.md` survives the concrete counterexample found in its (b=1) level bound, but one displayed lower bound is false as written. A corrected exact bipartite sum still gives the required super-exponential growth. The result is conditional on the literal rank-only equality rule and the stated finite, countably additive complex-measure framework. This is not a global priority finding or a physical result.

## Claim under review

Let (p\in\mathbb C), (q=1-p), (A_p(H)=p^{L(H)}q^{\binom n2-R(H)}), and let (D_H\subseteq P_\infty) be the covariant event that an infinite-post history has a post whose inclusive past has unlabelled principal shape (H), with (|H|=n). (N(H)) is the number of distinct naturally labelled representatives of (H), quotienting labelings by automorphisms. The added value rule is the literal equality

\[
\nu(D_H)=\kappa_n N(H)A_p(H)\quad\text{for every principal }H\text{ of size }n,
\]

for one finite scalar \(\kappa_n\) per rank, together with a finite countably additive complex measure on the posts algebra and \(\nu(P_\infty)=1\). Under exactly this rule, the result claims existence iff (0<p\le 1).

**Verdict: conditional pass.** The no-go argument for (p\notin[0,1]) is repairable and the positive-real construction is the classical one. At (p=0), all rank-(n\ge2) principal amplitudes vanish and their laminar cover contradicts normalization. The (p=1) chain endpoint works. The equality rule is a substantive assumption; covariance and normalization alone do not imply it.

## Defect found and exact repair

Write (a=|p|>0), (b=|1-p|), and (W_n=\sum_{|H|=n,\ H\ principal}N(H)|A_p(H)|). The submitted proof's Lemma 2(iii) says that for (b=1), a lower antichain (A_m), upper antichain (B_m), arbitrary (E\subseteq A_m\times B_m), and universal cap (z), the cover count is (|E|+m). This omits (A\to z) covers for lower vertices with no (E)-neighbor. Those extra factors of (a) invalidate the claimed bound when (a<1).

An exact counterexample is

\[
p=(50+120i)/169,\quad a=10/13,\quad b=1.
\]

At (m=1), the two capped orders (empty (E) and full (E)) each have two covers. These are exactly the two naturally labelled principal 3-orders (the chain and the fork), so (W_3=2a^2=200/169), not merely a subfamily lower bound. The stated lower bound (a(1+a)=230/169) is larger and therefore false. This is a proof-step failure, not a counterexample to the theorem.

For arbitrary (m\), let (z(E)) be the number of isolated lower vertices. The exact cover count is

\[
L(E\cup\{z\})=|E|+m+z(E).
\]

There are no other relevant (q)-factors when (b=1), since all incomparable pairs have modulus (1). Summing row by row, an empty lower row contributes (a) from its direct cover to (z), and each nonempty row contributes \((1+a)^m-1\) from its chosen edges to (B_m). The (m) edges from (B_m) to (z) contribute (a^m). Thus this family of distinct naturally labelled principal orders contributes exactly

\[
W_{2m+1}\ \ge\ a^m\big((1+a)^m+a-1\big)^m.
\]

Appending another universal maximum adds one cover and gives

\[
W_{2m+2}\ \ge\ a^{m+1}\big((1+a)^m+a-1\big)^m.
\]

Equivalently, one may restrict to (E) with every lower row nonempty, obtaining the weaker but also sufficient lower bound (a^m((1+a)^m-1)^m), and its even analogue multiplied by (a). For each fixed (a>0), eventually ((1+a)^m+a-1\ge(1+a)^m/2). Therefore

\[
\log W_N\ \ge\ \frac{(N-O(1))^2}{4}\log(1+a)-O_a(N),
\]

which is enough to sum (4^j/W_{n+j}) for every fixed (n). This restores the (b=1) case of the weighted estimate.

Two smaller textual corrections:

* Lemma 2(ii)'s star family contributes **at least once**, not “(n) times, once per cap label.” A unique maximum is forced to the last natural label, and the antichain relabelings are identified by automorphisms. The claimed inequality remains valid from the single contribution (a^{n-1}b^{\binom{n-1}{2}}).
* In Lemma 1(b), the line bounding the sum of row and column degrees by \(j(j+1)/2\) is false: that degree sum is (j(j+1)). The desired exponent bound is still true because (e(I,J)) counts a subset of the (j(j+1)/2) distinct forward edges. Hence (e(I,J)\le j(j+1)/2), and the stated (4^j b^{j(j+1)/2}) bridge bound follows directly.

## Independent audit of the argument chain

**Posts and event algebra.** Dowker–Zalel v2, Sec. V, Eq. (29), defines the posts algebra by requiring events to contain all or none of (P_\infty^c); Eqs. (30)–(31) identify its doubly-principal generator setting and report that the complex-percolation extension test is inconclusive. The events used here must be explicitly intersected with (P_\infty) so they lie in this algebra. A post of rank (n) is unique: two distinct posts are comparable and the later one has strictly more ancestors. Thus distinct (H)'s of the same size give disjoint (D_H)'s. The family over all principal (H) is countable and covers (P_\infty), since every infinite-post history has a second post with an inclusive past of size at least two.

**Laminarity and the zero factor.** If (|H|<|J|), (D_H\cap D_J) is either empty or (D_J): the unique post with past (J) fixes whether the earlier post of rank (|H|) has past shape (H), and all later elements are above both. Thus if all values \(\nu(D_H)=0\), every finite union has measure zero by laminarity and finite inclusion–exclusion; continuity from below then gives \(\nu(P_\infty)=0\). This establishes \(\kappa_n\ne0\) only in the common-factor proof; it is not used to assert that arbitrary zero-valued complex-measure sets are null.

**Child partition and multiplicities.** For a fixed rank-(n) post with past (H), the next post is unique. The interval before it has a post-free finite order (T), and the next post past has the unique ordinal decomposition (J=H\oplus T\oplus\{x\}). Conversely, post-free (T)'s give exactly the next-post children. Different children for the fixed post are disjoint and partition (D_H); children over distinct rank-(n) parents are disjoint. The seam contributes \(M(T)+\min(T)\) covers, yielding (p^{M(T)+\min(T)}A_p(T)). The ordinal cut at (|H|) is intrinsic, so automorphisms cannot exchange the two pieces; natural-label multiplicities factor (N(J)=N(H)N(T)). The existing script confirms (426) finite child-sum identities for each of four parameters through size 7; it does not replace the structural argument.

**Variation bounds and recurrence.** A finite complex measure has finite total variation (T\). The disjoint rank-(n) events imply (W_n|\kappa_n|\le T). The disjoint next-post children imply (W_n\sum_k K_k|\kappa_{n+k}|\le T), where (K_k) is the positive modulus sum over post-free (T)'s. Dividing the child additivity identity is legitimate for (p\notin[0,1]), because (p,q\ne0) and the chain amplitude (p^{n-1}) is nonzero at every rank. It gives \(\kappa_n=\sum_{k\ge1}R_k\kappa_{n+k}\), absolutely convergent by the child variation bound. This is not justified by convergence of a formal series (R(z)), nor by replacing (K_k) with (|R_k|).

**Bridge convolution.** (B_j) is the weighted probability-generating sum for an order with a universal minimum and maximum, equivalently the event that every noninitial column has an incoming edge and every nonfinal row has an outgoing edge in an independent forward-edge graph on (j+1) vertices. Inclusion–exclusion gives the claimed polynomial identity for all complex (p). For (b\le1), each term is bounded using (e\ge\frac12(\sum_{i\in I}\deg i+\sum_{j\in J}\deg j)); for (b\ge1), use the corrected total-edge bound above. At (b<1), the two-cap bound is valid: every doubly-principal (n)-order is an arbitrary ((n-2))-order with two universal caps, and the normalized modulus sum is the real random-graph probability \(\prod_{r=1}^{n-2}(1-s^r)\), with (s=b/(a+b)<1). At (b>1), the one-capped-antichain star gives the required lower bound. At (b=1), use the repaired bipartite bound. These yield \(\sum_{j\ge0}|B_j|/W_{n+j}<\infty\) on the stated rank tails.

Multiplying the recurrence at ranks (n+j) by (B_j) is justified by

\[
\sum_j |B_j||\kappa_{n+j}|\le T\sum_j |B_j|/W_{n+j}<\infty,
\]

and, using the child bound at each rank,

\[
\sum_{j,k}|B_jR_k\kappa_{n+j+k}|\le T\sum_j|B_j|/W_{n+j}<\infty.
\]

Fubini and the renewal identity (B_m=\sum_{k=1}^m R_kB_{m-k}) then cancel all terms except \(\kappa_n\), forcing it to zero. The renewal identity follows by the unique ordinal decomposition at the first post after the universal minimum; exact checks through (m=8) corroborate it. Zero on the tail propagates downward by the recurrence. This part is independent of convergence or divergence of \(\sum R_k\) at a candidate radius.

**Endpoints and normalization.** At (p=0), (A_0(H)=0) for every principal (H) of size at least two, and these events alone cover (P_\infty) by choosing the second post; no division or renewal equation at (p=0) is used. At (p=1), the chain Dirac measure gives (\kappa_n=1). For (0<p<1), the classical real transitive-percolation measure gives (\kappa_n=\prod_{r\ge1}(1-(1-p)^r)>0), using the classical post-tail probability and almost-sure infinite-post result. For the no-go, (\nu(P_\infty)=1) is a literal complex-number equality. Since (D_H\subseteq P_\infty), no use is made of values outside that event. If also \(\nu(\tilde\Omega)=1\), it follows only that \(\nu(P_\infty^c)=0\); for a complex measure this equality alone does not make arbitrary subsets of the complement null in variation. The proof does not assume that stronger property.

## Priority and exact claim contract

The nearest predecessor is Dowker–Zalel, arXiv:2212.01149v2 (17 Jul 2023 version; paper HTML currently displays Aug. 24, 2026), Sec. V, Eqs. (29)–(31): it defines the posts algebra, identifies its doubly-principal generator analogue, and explicitly leaves the complex-percolation extension question inconclusive. It does not state the rank-only all-principal post-value rule or this renewal obstruction in the sections read. Surya–Zalel, arXiv:2003.11311v1, Sec. 3.1, gives bounded-variation extension criteria for complex sequential-growth cylinder measures on the full labelled event sigma-algebra; that criterion is a method predecessor, not the same covariant event/value problem. Dowker–Johnston–Surya, arXiv:1007.2725v1, Sec. 4, proves nonextension of complex percolation to the full labelled history sigma-algebra except nonnegative real parameters; it does not assign the post events the shape-blind rank factors at issue here. Classical random-graph-order post probabilities and linear-sum decomposition predate the candidate result and are used only for real-parameter sufficiency.

The mathematical delta, if priority survives a broader search, is therefore narrow: under a literal **all-principal, rank-only** complex post-value rule and normalization on (P_\infty), there is no finite countably additive complex measure outside (0<p\le1), even when the factor may vary arbitrarily with rank. It is a measure-extension obstruction, not a classification of covariant measures without that rule, not a classification of shape-dependent factors, and not an ontological or empirical result.

Falsifiers: (1) a counterexample to the child partition/ordinal multiplicity or renewal identity; (2) an error in the corrected (b=1) cover sum or any of the bridge/two-cap/star bounds; (3) a normalized finite complex measure satisfying the exact rule outside the interval; (4) prior work proving the same conditional classification. Small exact checks do not rule out a structural error or establish global priority.

## Checks and limitations

Ran `python3 research/rank-renewal-convergence/check_weighted.py`: all finite exact assertions passed, including natural-label multiplicity checks, renewal identities through degree 8, child sums through size 7, two-cap bounds for the tested parameters, bridge comparisons, and endpoint checks. That script tests the (b=1) bipartite lower bound only at (p=2), so it misses the counterexample above. Added `check_bipartite_bound.py`, which exactly enumerates the capped bipartite family through (m=4), verifies the corrected formula against the rowwise closed form, and reproduces the (m=1) counterexample. The proof beyond finite checks is the corrected row-factorization argument in this report.

Limitations: the full covariant post algebra theorem is imported from Dowker–Zalel; this audit checked its exact definition and relevant generator statements, not every proof dependency. The all-principal factorization is an added mathematical premise, not implied by the algebra. The classical almost-sure infinitely-many-post theorem's original Alon et al. proof was not independently reconstructed. Search was targeted, not exhaustive; the result is not a global novelty certificate. No ontology, passage, determinism, or thermodynamic-arrow conclusion follows.
