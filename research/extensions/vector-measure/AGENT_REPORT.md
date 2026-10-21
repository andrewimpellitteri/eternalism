# Vector-valued measures: bounded-variation boundary and a finite conditional-convergence witness

Status: 2026-10-20. Probe `vector-measure-boundary`. This does **not** construct
a countably additive vector-valued counterexample on the infinite
doubly-principal algebra. It proves the bounded-variation no-go, gives an
explicit finite-level `R^2`-valued measure with the prescribed norms, and
isolates the infinite extension as the remaining problem.

## Corrections applied 2026-10-21 (submission for review)

Following the committed independent review
(`research/adversarial-review/AGENT_REPORT.md`, `coordinator/VECTOR_COUNTERMODEL.md`,
`coordinator/BOUNDARIES.md`), dated 2026-10-21, the following corrections are
applied to this report. Historical negative results are preserved; each
correction is also marked in place. Nothing here strengthens a claim beyond the
reviewed material, and the construction remains standard functional analysis
applied to this problem, not a new vector-measure theorem.

1. **The infinite norm-prescribed extension is no longer wholly open.** On the
   circle `|p|²+|1-p|²=1` (with `r=|p|²`), the standard indicator construction
   `mu(E) = 1_E` viewed in `X = L²(P_r)` — where `P_r` is classical labelled
   transitive-percolation probability on the full labelled history space — is a
   **countably additive** `X`-valued measure with `||mu(cyl C)|| = |A_p(C)|` on
   **every** naturally labelled cylinder: `||mu(cyl C)||² = P_r(cyl C) =
   r^{L(C)}(1-r)^{binom-R(C)} = |A_p(C)|²`. Total mass is the constant one
   (norm 1). For disjoint `(E_j)`, `||mu(∪_{j>N} E_j)||² = P_r(∪_{j>N} E_j) → 0`
   gives countable additivity. Semivariation is **one** (disjoint indicators
   are orthogonal: `||Σ α_j 1_{E_j}||² = Σ|α_j|²P_r(E_j) ≤ 1`, attained). For
   **nonreal** p on the circle, total variation is **infinite**: finite
   disjoint doubly-principal cylinder families at level k+2 have norm sums
   `V_{k+2}(p) ≥ |p|(|p|+|1-p|)^k c_s → ∞` (the independently reviewed two-cap
   bound). At the real endpoints p∈{0,1} this is the classical probability
   case. Full analytic proof: `coordinator/VECTOR_COUNTERMODEL.md` (2026-10-21);
   finite exact corroboration: `check_indicator.py` in this directory. This
   example prescribes norms only; it does not preserve complex phases, a common
   direction, a decoherence functional, or any physical dynamics, and it must
   not be described as phase-preserving quantum dynamics.
2. **The blanket semivariation impossibility is replaced.** Theorem 1's argument
   excludes finite **total variation** (always) and finite semivariation
   **in finite dimension** (where the two are equivalent). In infinite dimension
   finite semivariation does not imply finite total variation, and the L²
   indicator construction above has semivariation one with infinite total
   variation.
3. **Fixed-direction reduction (separate statement).** If instead
   `mu(C) = A_p(C) v` for a fixed nonzero v, any continuous scalar functional
   with value one on v reduces the problem to the scalar no-go. This reduction
   is about a fixed common direction; it says nothing about the norm-prescribed
   problem.
4. **Finite-dimensional no-go (separate statement).** Every countably additive
   measure valued in a finite-dimensional space has finite total variation
   (take the finitely many scalar coordinate measures and bound the norm
   variation by a finite weighted sum of their scalar variations). Hence no
   **`R^2`-valued** (or any finite-dimensional) countably additive
   norm-prescribed extension exists off `[0,1]`; the L² counterexample is
   necessarily infinite-dimensional. Finite polygon or Re/Im assignments on
   finite trees are finitely additive only and do not conflict with this.
5. **Finite polygon assignments are demoted.** `(Re A_p(C), Im A_p(C))` already
   gives an exact finitely additive norm-matching assignment on every finite
   tree, so finite existence was never the missing step, and the polygon data
   (or any finite data) are not evidence toward an infinite extension.
   `check_indicator.py` verifies the Re/Im additivity exactly through level 5.
6. **Remaining open problem, restated.** What remains open is the
   classification away from the circle locus: which norm prescriptions
   `||mu(cyl C)|| = |A_p(C)|` (or which weaker data) admit countably additive
   Banach-space-valued extensions, in which spaces. A separate pending GLM task
   studies the standard finite-Lalpha indicator construction's locus; its
   unreviewed result is not assumed here.

Exact-arithmetic and scope corrections to `vector_measure.py` (docstring) and
this report are dated 2026-10-21. The original 2026-10-20 sections follow,
preserved as reviewed.

## Exact formulation

The scalar theorem prescribes complex values `A_p(C)`. A vector-valued
generalisation must say what replaces them. This probe uses the **norm-prescribed**
version:

> Find a countably additive `R^2`-valued measure `mu` on the labelled
> doubly-principal cylinder sigma-algebra with
> `||mu(cyl(C))|| = |A_p(C)|` for every cylinder `C`.

This is not a vector lift of the complex phase. If one instead fixes a vector
`v` and demands `mu(cyl(C)) = A_p(C) v`, the problem reduces to the scalar one
and the scalar no-go applies immediately. The norm-prescribed version is the
non-trivial weakening in which conditional cancellation can occur.

## Theorem 1 — bounded-variation no-go

Let `X` be a Banach space and `mu` a countably additive `X`-valued measure with
finite total variation on the doubly-principal cylinder algebra. Then
`mu(cyl(C))` cannot have `||mu(cyl(C))|| = |A_p(C)|` for `p∉[0,1]`.

**Proof.** At level `k+2`, the doubly-principal cylinders are pairwise disjoint.
Finite additivity gives

`Σ_{|C|=k+2, dp} ||mu(cyl(C))|| = V_{k+2}(p) ≥ |p|(|p|+|1-p|)^k c_s → ∞`,

which contradicts finite total variation. The same argument rules out finite
semivariation in finite dimensions, since total variation and semivariation are
equivalent there. This is the scalar proof with `|mu(·)|` in place of `|mu(·)|`
for a complex measure; it does not use the triangle inequality of the target
space. ∎

So the scalar no-go **does** extend to bounded-variation vector measures; and to
finite-**semivariation** vector measures only in finite dimension.
[Corrected 2026-10-21: the earlier blanket "semivariation" extension was
overbroad — in infinite dimension finite semivariation does not imply finite
total variation, and the L² indicator construction of `coordinator/
VECTOR_COUNTERMODEL.md` has semivariation one with infinite total variation.]
The formerly "open" general countably additive case is realized on the circle
`|p|²+|1-p|²=1` by that construction; the classification away from that locus
remains open. ∎ [marker end]

## Theorem 2 — finite-level norm-prescribed construction

For `p=(1+i)/2`, for every finite level `N` there is a finitely additive
`R^2`-valued measure on the labelled cylinder algebra truncated at `N` with
`||mu(cyl(C))|| = |A_p(C)|` for every cylinder.

**Construction.** Start with `mu(root)=(1,0)`. At a node with parent vector `V`
and children of norms `a_1,…,a_m`, the polygon inequality
`|V| ∈ [max(0, 2 max a_i - Σ a_i), Σ a_i]` is exactly the condition that
vectors of lengths `a_i` can sum to `V`; it holds because `A_p(parent)=Σ A_p(child)`
and `|Σ A_p(child)|` lies in that interval. Choose the child vectors in `R^2` by
the greedy polygon construction in `vector_measure.py` (take the longest child,
pick the intermediate norm in the feasible interval, solve the triangle, and
recurse). Finite additivity and the norm constraints hold by construction.

**Check.** At `p=(1+i)/2`, levels 1–5 (407 nodes):

- maximum norm error: `1.11e-16`;
- maximum child-sum error: `6.21e-17`;
- zero polygon failures;
- level sums of norms: `1, 1.41421, 2.62132, 6.0481, 16.751` (diverging);
- level vector sums: `(1,0), (1,0), (1,0), (1,0), (1,0)` (bounded).

This is a finite-level conditional-convergence witness: the norm series
diverges while the vector series cancels. It shows that no finite-level
total-variation argument can rule out a vector-valued extension.

[Corrected 2026-10-21: finite existence is not a step toward an infinite
extension — `(Re A_p(C), Im A_p(C))` already gives an exact finitely additive
norm-matching assignment on every finite tree (checked in `check_indicator.py`),
and the level norm sums above depend only on the prescribed norms, not on the
polygon directions. Finite data, including these, are not evidence for an
infinite extension. Marker end.]

Reproduce: `python3 vector_measure.py` (floating-point construction;
`python3 check_indicator.py` for the exact finite checks).

## What remains open

[Corrected 2026-10-21: the opening claim of this section — "The infinite
countably additive extension is **not** constructed" — is superseded on the
circle locus: the L² indicator construction of `coordinator/
VECTOR_COUNTERMODEL.md` (summarized in the correction section above) **is** a
countably additive infinite-dimensional norm-prescribed extension for every p
with `|p|²+|1-p|²=1`, with infinite total variation off the endpoints. The
specific construction question below — a strongly-additive infinite choice
extending the *polygon* data — remains open as stated, but it is no longer the
formulation whose affirmative answer was needed; the existence question it
aimed at is answered by the L² example, negatively for `R^2` targets (finite-
dimensional no-go) and affirmatively in infinite dimension on the circle. What
remains genuinely open is the classification away from that locus: which other
norm prescriptions admit countably additive Banach-valued extensions, and in
which spaces. Marker end.]

A finitely
additive vector measure on the clopen algebra of the compact path space extends
to a countably additive vector measure if it is strongly additive (norm-continuous
at `∅`) or if the associated vector martingale converges; neither is proved
here. The path norms decay for `|p|,|q|<1`, but that controls individual
cylinders, not the strong additivity of arbitrary countable partitions. This is
the precise remaining problem:

> Does the finite polygon construction admit a consistent infinite choice that
> is strongly additive (or a bounded vector martingale density), and if so, what
> is the resulting measure?

A yes would be a genuine counterexample to the scalar-total-variation intuition;
a no would be a stronger vector-measure no-go. The finite data do not decide it.

## Known-result reduction and triviality checks

- For a fixed direction `mu(C)=A_p(C)v`, the problem is scalar and the no-go
  applies; the norm-prescribed construction is genuinely different.
- For `p∈[0,1]`, the classical scalar probability measure is a special case of
  the norm-prescribed construction (all vectors collinear); no new result.
- For `p∉[0,1]`, the disjoint level norm sums diverge, so any bounded-variation
  or finite-semivariation vector measure is excluded. [Corrected 2026-10-21:
  "finite-semivariation" here means finite-dimensional targets; in infinite
  dimension the L² indicator construction has semivariation one and realizes a
  countably additive extension on the circle `|p|²+|1-p|²=1`, so infinite
  variation is not merely "possible" there but attained. Marker end.]
- The construction is non-unique; different polygon choices give different
  finite-level measures. No physical or ontological interpretation is claimed.

## Verdict

**Scope boundary, not a counterexample.** The scalar no-go is not about
complexity as such: it is about finite total variation. It extends to
bounded-variation vector measures, but the norm-prescribed
finite-level construction shows the total-variation hypothesis is doing real
work. [Corrected 2026-10-21: with the reviewed L² indicator counterexample, the
norm-prescribed infinite extension exists on `|p|²+|1-p|²=1`; the residual
"publishable remark" content is the bounded-variation and finite-dimensional
no-gos plus the fixed-direction reduction, with the general classification off
the circle still open. Marker end.] This is a
publishable remark/section for the short note, not a headline result.

## Files

- `research/extensions/vector-measure/vector_measure.py` — finite polygon
  construction and checks.
- `research/extensions/vector-measure/check_indicator.py` — exact finite checks
  for the L² indicator counterexample and the Re/Im finite assignment (added
  2026-10-21).
- `research/extensions/vector-measure/AGENT_REPORT.md — this report.

Standard library only; no installs; no board edits.
