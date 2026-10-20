# Conditional theorem on covariant post events

Status: 2026-10-19. Coordinator derivation, separately checked during the fresh
proof and covariant-boundary audits. Publication priority is unverified. This
adds an explicit factorization assumption; it is not an unconditional transfer
of the labelled-cylinder theorem.

## Definitions and the added assumption

Use the parameter-independent event algebra called \(\mathcal R_p\) in
[Dowker–Zalel, arXiv:2212.01149v2](https://arxiv.org/html/2212.01149v2),
Sec. V, Eq. (29). The subscript names the posts algebra, not the numerical
coupling. Its events are covariant measurable sets containing either all or
none of \(\mathcal P_\infty^c\), where \(\mathcal P_\infty\) is the event
of infinitely many posts. A post is comparable with every other element.

For **every principal** finite unlabelled order \(H\), let
\(n=|H|\), and let \(D_H\) be the event that:

- the infinite causet has infinitely many posts;
- a post has exactly \(n-1\) ancestors and inclusive past isomorphic to \(H\).

Let \(N(H)\) count distinct naturally labelled representatives of \(H\),
already identifying labelings related by an automorphism. Put
\(A_p(H)=p^{L(H)}(1-p)^{\binom n2-R(H)}\).

The **common tail factor assumption** asks for one finite complex number
\(\kappa\), independent of \(H\) and \(n\), such that
\[
\nu(D_H)=\kappa\,N(H)A_p(H)
\quad\text{for every principal }H. \tag{T}
\]
It says that the amplitude for a finite principal past is multiplied by the
same factor for its maximum to remain a post in a cyclic future. This is an
additional model requirement, not a consequence of covariance or of the
labelled cylinder assignments alone.

## Exact statement

**Conditional theorem draft.** There is a finite-valued countably additive
complex measure \(\nu\) on \(\mathcal R_p\) with
\(\nu(\widetilde\Omega)=\nu(\mathcal P_\infty)=1\), and some
\(\kappa\in\mathbb C\) satisfying (T), **if and only if** the numerical
parameter satisfies \(0<p\le1\).

This is a classification under (T). A covariant measure using different post
amplitudes is outside the statement.

## Proof

The events \(D_H\) are measurable and covariant. A post with \(n-1\)
ancestors has label \(n-1\) in every natural labeling, so its finite past
and the condition that every later element be above it have a countable
cylinder description. Intersecting with \(\mathcal P_\infty\) gives a
covariant event contained in \(\mathcal P_\infty\), hence a member of
\(\mathcal R_p\) by Eq. (29). The raw post event without that intersection
need not belong to this algebra.

At fixed \(n\), different shapes \(H\) give disjoint events. Across ranks,
the family is **laminar**: if \(|H|<|J|\), then \(D_H\cap D_J\) is either
empty or \(D_J\). The later post's inclusive past \(J\) determines whether
the earlier rank contains a post with past \(H\). If it does, all elements
beyond the later post are above that earlier post too, so the determination
holds for every history in \(D_J\).

The countable family of all principal \(H\) covers \(\mathcal P_\infty\).
If \(\kappa=0\), every \(D_H\) has measure zero. Every finite intersection
is empty or one of these zero-valued sets; finite inclusion–exclusion makes
every finite union zero. Continuity from below for a finite complex measure
then gives \(\nu(\mathcal P_\infty)=0\), a contradiction. Thus
\(\kappa\ne0\). This argument does not treat arbitrary zero-valued sets
as null for a complex measure; laminarity supplies the needed intersections.

If \(p\notin[0,1]\), group all doubly-principal naturally labelled
\(n\)-orders by their unlabelled shapes. The amplitudes are identical within
each shape. With \(V_n(p)\) as in the [labelled theorem](RESULT.md), (T)
therefore gives the exact equality
\[
\sum_{\substack{[H]\text{ doubly principal}\\ |H|=n}}|\nu(D_H)|
=|\kappa|\sum_{[H]}N(H)|A_p(H)|
=|\kappa|V_n(p).
\]
These are disjoint covariant events at each rank. But the two-cap bound is
\[
V_n(p)\ge |p|\,(|p|+|1-p|)^{n-2}c_s\longrightarrow\infty,
\quad s=\frac{|1-p|}{|p|+|1-p|},\quad
c_s=\prod_{j\ge1}(1-s^j)>0.
\]
This contradicts finite total variation, since \(\kappa\ne0\).

At \(p=0\), every principal \(H\) of size at least two has a cover, so
\(A_0(H)=0\). The events for those sizes alone still cover
\(\mathcal P_\infty\), because every infinite-post history has a later post.
The same laminar union argument gives a contradiction.

For real \(0<p<1\), classical transitive percolation has infinitely many
posts almost surely, and its restriction supplies the required measure with
\[
\kappa=c(1-p),\qquad c(q)=\prod_{j\ge1}(1-q^j)>0.
\]
The finite past has probability \(N(H)A_p(H)\); conditional on that past,
sequential exposure gives the future-post probability \(c(1-p)\), independent
of its shape. These classical facts and the exposure product are prior work;
see [Bombelli–Seggev–Watson, arXiv:0809.2258v2](https://arxiv.org/html/0809.2258v2),
Sec. 2, Theorem 2.1 and Eqs. (1)–(2). Their discussion attributes the
infinite-post result to Alon et al.; the original proof is not newly reproduced
here. At \(p=1\), the infinite chain and \(\kappa=1\) supply the endpoint.

## Why the assumption matters

If (T) is imposed only for **doubly-principal** \(H\), allowing
\(\kappa=0\) changes the result. Take the infinite ordinal sum
\[
(A_2\oplus\{z_1\})\oplus(A_2\oplus\{z_2\})\oplus\cdots,
\]
where \(A_2\) is a two-element antichain. Every \(z_j\) is a post, but its
strict past has two maximal elements. Thus none of its inclusive post pasts
is doubly principal. The Dirac measure at this cyclic history is normalized,
gives all doubly-principal \(D_H\) value zero, and satisfies that weakened
rule for any numerical \(p\). The all-principal requirement in (T) is
essential for excluding \(\kappa=0\).

More generally, normalized covariant measures without any percolation-matching
rule plainly exist, for example Dirac measures at cyclic causets. Covariance
alone cannot specify their dynamics. The question is which matching or future
factorization requirements they satisfy.

## Finite-cutoff and analytic corollaries

For a principal \(H\) of size \(n\), the finite cylinder-amplitude sum in
which its maximum remains above all vertices through size \(M\) is
\[
N(H)A_p(H)\prod_{j=1}^{M-n}(1-q^j),\qquad q=1-p.
\]
If \(|q|<1\), the limit is \(c(q)N(H)A_p(H)\) with \(c(q)\ne0\).
Prescribing these limits as the values of \(D_H\) is one explicit way to
impose (T). It is not justified by continuity of a labelled measure that has
already been proved not to exist, and removal of finite-post histories is
part of this extra prescription.

Consequently, on a connected open set \(U\subset\{|1-p|<1\}\) intersecting
\((0,1)\), there cannot be a family of such finite measures whose values on
every \(D_H\) are holomorphic in \(p\) and agree with classical percolation
on the real interval. The identity theorem would force the displayed
classical continuation for these events throughout \(U\), including its
nonreal points, contradicting the theorem. This restricted-event corollary
does not claim a new general principle about analytic families of measures.

## What a rank-dependent tail factor would have to do

We can weaken (T) by allowing a factor \(\kappa_n\) that depends on the
number of elements in the principal past, while requiring it to be independent
of shape at that rank:
\[
\nu(D_H)=\kappa_n N(H)A_p(H),\qquad |H|=n.
\]
This weaker rule no longer gives the iff classification above. It does have a
necessary attenuation bound outside the real interval. The doubly-principal
events at rank \(n\) are disjoint, and their absolute values sum exactly to
\(|\kappa_n|V_n(p)\). Hence every finite complex measure extension must
satisfy
\[
|\kappa_n|V_n(p)\leq\|\nu\|_{\mathrm{TV}},\qquad
|\kappa_n|\leq
\frac{\|\nu\|_{\mathrm{TV}}}{|p|c_s}
\bigl(|p|+|1-p|\bigr)^{-(n-2)}.
\]
Here \(c_s=\prod_{j\ge1}(1-s^j)>0\) is defined above. In particular,
\(\limsup_{n\to\infty}|\kappa_n|^{1/n}\leq (|p|+|1-p|)^{-1}\). A
shape-independent correction that decays subexponentially is therefore ruled
out. This is only necessary: it neither constructs an extension for an
exponentially decaying factor nor handles shape-dependent factors. For those,
the necessary condition is boundedness of the weighted sums
\(\sum_{|H|=n}|\kappa_H|N(H)|A_p(H)|\), which also does not by itself
prove countable additivity.

Priority and physical scope remain separate: the possible contribution is the
specific conditional extension obstruction, not classical post probabilities,
general measure theory, a quantum decoherence functional, or temporal ontology.
The [fresh proof audit](proof-audit/AUDIT.md) checked the classification and
counterexample. The [separate priority note](priority-audit/POST_TAIL_PRIORITY.md)
compares classical post probabilities, the 2010 complexification discussion,
and Sorkin's 2011 event-convergence framework. No matching theorem was located
within that bounded search; global priority and external review remain open.
