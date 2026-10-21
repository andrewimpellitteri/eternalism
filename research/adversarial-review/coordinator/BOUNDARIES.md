# Additional boundary corrections

Coordinator review, 2026-10-21. These findings concern extension-probe reports;
they do not refute the selected labelled scalar theorem.

## Local-renewal indexing: shrink the literal statement

In `research/extensions/covariant-values/AGENT_REPORT.md`, assumption (A) applies
only to doubly-principal H. There is no singleton doubly-principal H: deleting
its maximum gives the empty order, which has zero maxima. Consequently κ_1 is
unconstrained. The comparison on doubly-principal chains proves κ_n=κ_{n+1}
only for n≥2. The full principal formula follows with common factor κ_2,
including the singleton via local renewal. The classification for p≠0 survives.

A literal counterassignment to “κ_n is a constant” for all n≥1 is p=1, Dirac
measure on the infinite chain, κ_n=1 for n≥2, κ_1=17. Both assumptions hold and
normalization holds. The independent fixture checks finite instances and the
singleton edge case. State “constant for n≥2”, or explicitly extend the sequence
to κ_1 by convention; do not treat that convention as a derived constraint.

The shape-dependent-factor table also needs a qualification. Division by A_p(H)
is available for p≠0,1. At either endpoint some amplitudes vanish, so arbitrary
measures cannot be factored by division; the zero-amplitude events impose actual
zero-value conditions. Likewise, the DP-only rule admits the exhibited κ=0
countermodel for every p; that does not mean every measure satisfies the rule.

## Rank-factor report: preserve the reduction, not an existence claim

In `research/extensions/rank-factor/AGENT_REPORT.md`:

- State whether the sum defining R_k is over naturally labelled T, or over shapes
  with N(T) multiplicity. The displayed derivation requires that multiplicity.
- The scalar recurrence follows by dividing a nonzero N(H)A_p(H); for p≠0 a chain
  supplies one at every rank. At p=0, ranks ≥2 do not permit this division.
- The assertion “for p in [0,1], R(1)=1” needs p=0 removed. At p=0 every R_k=0:
  R_1=p and each other term contains a positive power of p. The classical
  infinite-post probability is not one at p=0.
- The scalar measure no-go does not itself prove divergence of the complex
  scalar series R(1). Absolute variation can diverge while complex sums cancel.
  Supply a separate convergence proof or withdraw the asserted equivalence.
- Floating checks with maximum error zero are finite numerical corroboration;
  their existence neither proves the analytic lemma nor establishes newness.

The finite stationary factorization is plausible and independently interpretable
by ordinal-sum decomposition, but global rank-only measure existence remains
unresolved. Neither truncated polynomial roots nor a necessary attenuation bound
settles countable additivity and normalization. The claim of a “new structural
lemma” remains unverified as a priority claim.
