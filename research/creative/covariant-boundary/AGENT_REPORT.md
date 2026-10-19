# Agent report: ctp-covariant-boundary

## Files changed

- `research/creative/covariant-boundary/BOUNDARY.md` — defines a covariant
  all-principal stationary post-factorization premise, proves the conditional
  boundary using a direct two-cap estimate, records a doubly-principal-only
  Dirac counterexample, and gives the cutoff-limit and holomorphic corollaries.
- `research/creative/covariant-boundary/sources.jsonl` — four primary-source
  records with version, targeted locators, read depth, claims, and limits.

## Evidence and derivation

- Read Dowker–Zalel arXiv:2212.01149v2, particularly Sec. V Eqs. (29)–(31)
  and Theorems 14–15. They identify the covariant intersection but leave their
  doubly-reduced-tree complex extension criterion inconclusive.
- Read Dowker–Johnston–Surya arXiv:1007.2725v1 Sec. 4 and Surya–Zalel
  arXiv:2003.11311v1 Secs. 1–3. These establish the nearby full labelled
  algebra obstruction and explain why post-event values need extra treatment.
- Checked the coordinator-proposed finite-horizon post sum, its nonzero limit for
  \(|q|<1\), and the direct all-doubly-principal endpoint bound
  \(V_n\ge |p|(|p|+|q|)^{n-2}\prod_{j\ge1}(1-s^j)\). Grouping by unlabeled
  shape gives exact same-rank covariant variation \(\Gamma_n=|\kappa|V_n\)
  under (S), and \( |c(q)|V_n \) under its cutoff-limit special case (P).

## Checks

- Algebra check: events at a fixed post rank are disjoint. Across ranks the
  all-principal post events form a laminar family; finite unions of zero-valued
  events are handled by inclusion-exclusion, then continuity from below.
- Multiplicity check: `N(H)` counts distinct naturally labelled
  representatives, not raw vertex permutations. Grouping all doubly-principal
  endpoints by shape gives the exact identity in the note; the amplitude is
  isomorphism invariant.
- Renewal check: at step `j`, the new element lies above the candidate post
  exactly when its precursor subset intersects the `j` existing elements
  already in the post's future cone, giving factor `1-q^j`.
- Two-cap check: every doubly-principal `n`-order is uniquely `G ⊕ {u} ⊕ {v}`;
  summing normalized real weights is the probability that the last of `n-1`
  elements is a universal maximum, equal by order reversal to the first
  element being below all later elements.
- No code or numerical tests were run or needed; validation was symbolic
  algebra and standard infinite-product convergence. The endpoint bound is
  independently checkable from the stated sequential-growth transition rule.
- Ran `python3 scripts/check_sources.py research/creative/covariant-boundary`:
  1 file, 4 records, 0 errors, 0 warnings.

## Limits and unresolved questions

- The main result is conditional on the explicit same-factor premise (S) for
  every principal post past. It does not imply that an arbitrary measure on
  `R_p` must satisfy those values. The doubly-principal-only Dirac example
  explains why all-principal coverage is needed for the zero-factor case.
- The cutoff-limit and holomorphic variants are additional value prescriptions
  or regularity assumptions, not consequences of the labelled cylinder data.
- Membership check uses Eq. (29) and Theorem 14: every covariant event D_H is
  a subset of P∞, hence lies in R_p and therefore in the cylinder-generated
  intersection. Coordinator should review whether the stationary factorization
  is the desired physical compatibility axiom.

- **Provenance:** the coordinator proposed the successive conditional routes,
  the all-principal common-factor theorem and the two-cap simplification; this
  lane audited their derivations and compared the primary sources.
