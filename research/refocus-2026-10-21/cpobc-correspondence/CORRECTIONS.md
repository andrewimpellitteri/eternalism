# Proposed replacements for `research/qbc-holonomy/RESULT.md`

These are replacement passages for coordinator use; the existing lane is left untouched.

## Replace headline / “what the primary establishes” Pauli sentence

> The primary proves commutativity of the transition-operator algebra for TOBC and NTOBC under its nonsingularity and operator-level assumptions. For CPOBC it derives additional commutator constraints but does not prove commutativity. Its Appendix tests a small family of assignments in which each antichain generator is a scalar multiple of a pure Pauli matrix (with four listed patterns for the first generators); those ansätze fail the path-consistency relation or invertibility. This is not a general no-go for all two-dimensional complex matrix representations.

## Replace scalar-reduction / phase-survival conclusion

> For scalar transition amplitudes and nonzero denominators, each of TOBC, NTOBC, and the equal/unequal CPOBC rules reduces algebraically to the same cross-multiplied scalar product-BC equation. The exact `bc-nonzero` continuation checks 49 nonzero scalar transitions, MSR through the 3-to-4 step, 109 scalar product-BC equations, and norm-GC through stage four. It also exhibits a nontrivial path phase (3−4i)/5. Because the primary paper's GC is equality of path-generated vectors, this norm-GC certificate does not establish primary GC: the exhibited phase obstructs vector equality for the compared paths. It is therefore a norm-covariant scalar BC model, not an operator-QBC representation or a verified model of all the primary's assumptions.

## Replace direct-sum inference

> TOBC and NTOBC imply that the generated transition algebra is commutative under the paper's assumptions. Commutativity alone does not imply that a matrix representation decomposes as a direct sum of scalar representations: a commutative algebra may act through nonsplit triangular or nilpotent extensions. The scalar seed is one scalar representation of the equations; the paper's theorem does not classify all representations as scalar sums.

## Replace the “what would change the verdict” Pauli bullet

> A general d=2 no-go would require ruling out arbitrary nonsingular 2×2 complex transition matrices satisfying operator MSR, the chosen covariance condition, and every unequal- and equal-precursor CPOBC equation. The primary's pure-Pauli ansatz does not do this. A higher-dimensional noncommutative representation is also not established by the primary.

## Replace check description

> Running `python3 research/qbc-holonomy/check.py` reruns the scalar `bc-nonzero` certificate and checks output markers for its scalar transition, product-BC, norm-GC, and holonomy results. It does not independently test the claimed reduction of each operator ordering, does not construct operator transitions, and does not verify operator-level covariance. Treat its ordering comparison as an algebraic observation in the scalar nonzero case, not as a checked operator theorem.

## Add explicit assumption boundary

> Keep four notions separate: (i) operator MSR, Σ_j T_j=I, (ii) vector additivity on the actual history vector, (iii) GC as equality of path-generated vectors, and (iv) norm-only covariance. The primary writes an operator MSR and vector GC; the scalar continuation verifies MSR and norm-GC. No result here transfers between these conditions without an explicit argument.
