# Vector-valued measures: bounded-variation boundary and a finite conditional-convergence witness

Status: 2026-10-20. Probe `vector-measure-boundary`. This does **not** construct
a countably additive vector-valued counterexample on the infinite
doubly-principal algebra. It proves the bounded-variation no-go, gives an
explicit finite-level `R^2`-valued measure with the prescribed norms, and
isolates the infinite extension as the remaining problem.

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

So the scalar no-go **does** extend to bounded-variation/semivariation vector
measures. The open question is general countably additive vector measures,
which may have infinite total variation.

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

Reproduce: `python3 vector_measure.py`.

## What remains open

The infinite countably additive extension is **not** constructed. A finitely
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
  or finite-semivariation vector measure is excluded. The only possible
  extension is a general countably additive vector measure with infinite
  variation, exactly the case the finite witness explores.
- The construction is non-unique; different polygon choices give different
  finite-level measures. No physical or ontological interpretation is claimed.

## Verdict

**Scope boundary, not a counterexample.** The scalar no-go is not about
complexity as such: it is about finite total variation. It extends to
bounded-variation/semivariation vector measures, but the norm-prescribed
finite-level construction shows the total-variation hypothesis is doing real
work. The infinite countably additive extension remains open. This is a
publishable remark/section for the short note, not a headline result.

## Files

- `research/extensions/vector-measure/vector_measure.py` — finite polygon
  construction and checks.
- `research/extensions/vector-measure/AGENT_REPORT.md` — this report.

Standard library only; no installs; no board edits.
