# Source-priority and adversarial claim review

Status: 2026-10-21. This is a bounded independent review of the primary-source
correspondence and novelty strength for the selected labelled theorem and the
current extension probes. It is not a global priority certificate.

## Findings

**Selected doubly-principal scalar theorem — survives as a narrow solution of a
named open case; novelty/significance claim should stay modest.** Dowker–Zalel,
arXiv:2212.01149v2 (17 July 2023), Sec. V, addresses the same labelled
doubly-principal cylinder algebra (their doubly-reduced poscau). It supplies a
finite-level variation criterion, explains why the earlier minimum criterion
is inconclusive due to valency-one nodes, and leaves the relevant
doubly-principal/valency-one absolute-amplitude sum for future computation.
Zalel’s 2021 thesis, Ch. 6 §6.2.3, printed pp. 89–90, independently records
the same unresolved calculation. The project's cap decomposition and
percolation lower bound evaluate that omitted contribution and yield the
claimed classification. I found no identical proof in the screened sources.

The strongest surviving objection is significance, not direct mathematical
duplication: the proof is a short application of the predecessor's criterion
to a specifically named open remainder, using an elementary weighted-sum
bound. Recommend describing it as an explicit solution of that case, subject
to bounded priority review, rather than a new extension criterion or general
method. Failure of extension on the full labelled cylinder algebra does not
itself prove failure on the smaller doubly-principal algebra. The target
algebra is not the covariant intersection in Dowker–Zalel.

**Conditional covariant common-factor theorem — survives only with its added
all-principal factor rule and normalization.** The literature checked does not
turn it into an unconditional covariant classification. The double-principal
rule alone is defeated by the already-recorded Dirac-history example. Keep the
conditional theorem separate from the labelled classification.

**Rank-only probe — remains unresolved.** The stationary kernel identity and
convolution are a useful reduction, but finite root truncations do not settle
existence or nonexistence of a decaying factor. Do not state a classification.

**Covariant local-renewal refinement — survives as an elementary conditional
boundary lemma, not a headline classification.** For nonzero p, the local rule
and doubly-principal rule force the all-principal factor; p=0 retains the
Dirac exception. No ontology follows.

**Vector-measure probe — prior “infinite extension open” disposition is now
false for the norm-prescribed variant.** For any complex p with
`|p|^2 + |1-p|^2 = 1`, set `r=|p|^2` and let `P_r` be ordinary real CTP on the
full labelled history space. The Hilbert-valued measure
`mu(E)=1_E` in `L^2(P_r)` is countably additive in norm: for disjoint `E_j`,
the squared norm of the remainder after N terms is
`P_r(union_{j>N} E_j)`, which tends to zero. For every cylinder C,
`||mu(C)||_2 = sqrt(P_r(C)) = |A_p(C)|`; this holds on the full algebra,
therefore on the doubly-principal subalgebra. In particular `p=(1+i)/2`
and `r=1/2` give a nonreal example. This is an explicit extension, not merely
a finite-level witness.

Its semivariation is exactly one: for any dual unit vector `h` in `L^2(P_r)`,
the scalar measure is `h mu(E)=integral_E h dP_r`, whose variation is at most
`||h||_1 <= ||h||_2 <= 1`; the constant function realizes one. Its total
variation is infinite, since sums of cylinder-vector norms over a level equal
the scalar level sum `V_n(p)`, which diverges by the project's lower bound.
Thus bounded-semivariation no-go is false in infinite-dimensional Hilbert
space. A fixed-direction vector lift remains scalar-equivalent and is excluded.
In finite dimensions, bounded semivariation does imply bounded variation:
choose finitely many coordinate functionals controlling the norm and bound
each coordinate's scalar variation by the semivariation. The finite-dimensional
no-go remains valid.

## Read scope and limits

Primary-source reads: Dowker–Zalel arXiv:2212.01149v2, Secs. III.2, III.4 and
V; Zalel, *Discrete random spacetimes: covariance and quantization in growth
dynamics for causal sets* (Imperial College London thesis, 2021), Ch. 6
§6.2.3, printed pp. 89–90. The relevant claims/criterion/open remainder were
read; no full proof audit of those sources was done. The direct primary
references and exact version/locator records are in `PRIMARY_EVIDENCE.md`.

For the vector-measure correction I checked Diestel and Uhl, *Vector Measures*,
AMS Mathematical Surveys 15 (1977), pp. 2–3 and 7–8 (pagination in the book):
the text defines countable additivity in norm, gives the indicator-map
construction via a bounded operator from L1 as a countably additive vector
measure, and gives the finite-p indicator measure in Lp as countably additive
by the tail-set estimate. The accessible full-text route was a public scan
mirror; AMS's official book record is linked in `PRIMARY_EVIDENCE.md`. I have
not treated the book as proving this project's cylinder identity: that
identity and the semivariation calculation above are checked directly here.

No source search can establish global priority. This review used the existing
bounded forward-citation and alternative-terminology audit rather than
re-running its searches. I did not independently execute the proof scripts or
the rank/vector programs. No source-register, theorem, or extension file was
changed.

## Severity / recommendations

- **No direct prior-art blocker** found for the selected scalar classification;
  keep the priority caveat and frame as a short solution of a stated open case.
- **Scope-critical** if the scalar result is called an unconditional covariant
  theorem, or if it is used to infer a temporal ontology.
- **Correction required** before citing the vector probe: record an infinite
  Hilbert-valued norm-prescribed extension at the stated locus, with infinite
  variation but bounded semivariation. Do not call all vector extensions open.
- **Unresolved** rank-only classification; truncated roots are not evidence.

Files changed: this report and `PRIMARY_EVIDENCE.md` only.
