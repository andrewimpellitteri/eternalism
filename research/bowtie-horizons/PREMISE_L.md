# Premise L′: source check and a weaker fallback

28 October 2026, native Claude. Status note for SCREENING.md Theorem 3(b).
The GLM reviewer `screening-review` hung twice without producing output, so
this check was done natively.

## Source check

Sbierski, *On the Existence of a Maximal Cauchy Development for the Einstein
Equations – a Dezornification*, arXiv:1309.7591v3 (2 Jul 2015; accepted,
DOI 10.1007/s00023-015-0401-5). Read depth: full text of ar5iv HTML
characters 0–100000 of 122586 (through part of §3.3); the remainder unread.

Found:
- local uniqueness on globally hyperbolic neighbourhoods of the initial
  slice (§1.4.1);
- agreement of isometric immersions on overlaps (Corollary 3.2, §3.1);
- developments of data on partial slices used inside proofs (§1.3; §3.2,
  proof of Theorem 3.6, footnote 32);
- a domain-of-dependence property invoked for local existence and
  uniqueness (§1.4.1, footnote 15).

Not found: any statement that, inside a maximal globally hyperbolic
development M, the domain of dependence D_M(S) of an open or partial
hypersurface S is the maximal development of the restricted data. So L′ is
**not sourced** by this paper, at the depth read. Ringström's monograph is
the remaining lead.

## Weaker fallback

The fallback needs only global CBG uniqueness for the slice data, not L′.
Suppose D_{M₁}(K₁) and D_{M₂}(h(K₁)) are each globally hyperbolic
developments in which the respective slice is Cauchy. Then both embed
isometrically, compatibly with h near the slice, into the single maximal
development N of the K-data. By Theorem 3(a) and continuity at the mark,
J⁺(b₁) and J⁺(b₂) embed into J⁺_N(β), where β is the common image of the
marks.

**Consequence (b′).** Readings at proper time T along matched future
geodesics from (b,u) agree whenever they are defined in both models. The
futures can then differ only by one being a proper part of the other inside
N (truncation). Excluding truncation is exactly what L′ would add.

**Gap in the fallback.** It needs h(K₁) to be a Cauchy surface of int
D_{M₂}(h(K₁)). That holds for open subsets of global Cauchy surfaces, but
for a general acausal partial hypersurface it is the same issue the
coordinator raised (CLAUDE_SCREENING_REVIEW.md, Finding 2). This is still
unproved here.

## Effect on the claims

X4 (rigidity line at the screening boundary) stays conditional, now on one
of: L′; or a proof that h(K₁) lies in a Cauchy surface of M₂; or, for the
weaker no-disagreement-where-defined conclusion (b′), h(K₁) being Cauchy in
its own domain of dependence. Theorem 2 and Theorem 3(a) do not depend on
any of these.
