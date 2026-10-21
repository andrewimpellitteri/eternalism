# Operator QBC and the BCPH phase seed: a commutative-shadow result

Sole-worker audit, 2026-10-21. Primary: Srivastava–Surya, "Implementing Bell
causality in Quantum Sequential Growth", arXiv:2603.25503v1. Read depth: full
text at Sections 3.2–3.5 and the stated equations; not a full-paper or
appendix audit.

## Question

The scalar BCPH seed has a nontrivial stage-4 `cp` holonomy `(3-4i)/5` under
product Bell causality, MSR and norm-GC. Does that phase freedom survive when
Bell causality is imposed on **operator-valued** transitions in the three
orderings of the primary: TOBC, NTOBC and CPOBC?

## What the primary establishes

- QBC replaces the scalar product equation by a relation among transition
  operators at two stages (Eq. (34)); Lemma 3.1 shows every transition
  operator is generated from the gregarious operators.
- **TOBC** (Sec. 3.3) gives, for the atomisation pair,
  `B_n^(1) G_{n-1}^(0) = G_n^(1) B_{n-1}^(0)` (Eq. (53)).
- **NTOBC** (Sec. 3.4) gives
  `A_n B_n^{-1} = A_m B_m^{-1}` (Eq. (71)).
- **CPOBC** (Sec. 3.5) gives the crossed relations
  `A_n A'_m = A_m A'_n` (Eq. (103)) with the equal-precursor variant (104),
  the gregarious relation (114), and the commutator constraints of
  Corollaries 3.8–3.9, including `[Q_1 Q_2^{-1}, Q_1^{-1} Q_2]=0`.
- The paper's headline result: TOBC and NTOBC reduce the transition-operator
  algebra to a **commutative** one. CPOBC does not imply commutativity, but
  the simplest `d=2` Pauli representation of the antichain subalgebra `Q` is
  inconsistent; any nontrivial representation must be higher-dimensional
  (Abstract and Discussion).

## Scalar reduction and the seed

For a commutative representation, take every transition operator to be
`A = t I` with the scalar BCPH amplitude `t`. Then:

- TOBC (53) becomes `b_n g_{n-1} = g_n b_{n-1}`, i.e.
  `b_n/g_n = b_{n-1}/g_{n-1}`.
- NTOBC (71) becomes `a_n/b_n = a_m/b_m`.
- CPOBC (103) becomes `a_n a'_m = a_m a'_n`.

These are exactly the cross-multiplied scalar product-BC equations for the
seed. The independent `bc-nonzero` certificate verifies all 109 such equations
through the 3-to-4 step, with all amplitudes nonzero, MSR and norm-GC through
stage 4, and the `cp` holonomy `(3-4i)/5`. Therefore the seed satisfies the
**scalar reduction of all three orderings**.

## Verdict

The nontrivial phase **survives operator QBC only as a commutative shadow**.
It is not killed, but it is not a genuinely operator-valued phase witness:

- TOBC and NTOBC force the algebra to be commutative, so any representation is
  a direct sum of scalar ones. The BCPH seed is one such scalar summand; the
  phase lives in the scalar eigenvalues, not in noncommuting operators.
- CPOBC is weaker and permits noncommutativity, but the seed as stated is
  still the commutative solution. The primary's `d=2` Pauli representation of
  `Q` is inconsistent; constructing a higher-dimensional noncommutative lift
  with the same BCPH amplitudes is not done here.
- No ordering-dependent phase value is found for the fixed seed. A claim that
  operator QBC preserves or destroys the phase in general is not supported by
  this audit.

## What would change the verdict

- An explicit higher-dimensional CPOBC representation with noncommuting
  transition operators whose scalar data are the BCPH amplitudes and whose
  holonomy is `(3-4i)/5`.
- A proof that no such representation exists in any dimension (a genuine
  operator-QBC no-go).
- A TOBC/NTOBC representation that circumvents the primary's commutativity
  theorem (which would contradict that theorem, so this is not expected).

## Check

`python3 research/qbc-holonomy/check.py` runs the accepted `bc-nonzero`
certificate and verifies the scalar-reduction mapping: the 109 product-BC
equations, nonzero amplitudes, MSR/norm-GC through stage 4, and the
`(3-4i)/5` holonomy. This checks the scalar seed, not a noncommutative
representation.

## Limits

- The operator algebra is cited from the primary, not reimplemented. The
  audit does not construct transition operators on a nontrivial Hilbert space.
- CPOBC's higher-dimensional representation space is open; the `d=2`
  inconsistency is the primary's result, not independently reproved here.
- No new primary full-text reads beyond the named sections; no novelty or
  ontology claim.
