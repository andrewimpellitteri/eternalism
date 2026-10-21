# Operator QBC and the BCPH phase seed: a commutative-shadow result

Sole-worker audit, 2026-10-21. Primary: Srivastava–Surya, "Implementing Bell
causality in Quantum Sequential Growth", arXiv:2603.25503v1. Read depth: full
text at Sections 3.2–3.5 and the stated equations; not a full-paper or
appendix audit.

Coordinator erratum, 2026-10-21 (task `refocus-selection-integration`): four
statements below were overclaims and are corrected in place, following
`research/refocus-2026-10-21/cpobc-correspondence/CORRECTIONS.md`. (1)
Commutativity does not imply a direct sum of scalar representations (Jordan
blocks are the elementary counterexample). (2) The seed verifies norm-GC, not
the primary's vector GC; its nontrivial phase obstructs vector path equality.
(3) The primary's `d=2` result is a failed pure-Pauli ansatz, not a general
two-dimensional no-go; the published PRD abstract (7 Oct 2026) drops the
"must be higher-dimensional" inference (abstract-level read). (4) `check.py`
reruns the scalar certificate only; it does not test operator orderings.

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
  algebra to a **commutative** one under its nonsingularity and operator-level
  assumptions. CPOBC does not imply commutativity. Its Appendix tests
  assignments in which each antichain generator is a scalar multiple of a pure
  Pauli matrix; those ansätze fail path consistency or invertibility. This is
  not a general no-go for 2×2 complex representations.

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
stage 4, and the `cp` holonomy `(3-4i)/5`. So the seed satisfies the scalar
product-BC form of all three orderings with **norm** covariance. The primary's
GC is equality of path-generated vectors, and the nontrivial phase obstructs
that equality for the compared paths. The seed is a norm-covariant scalar BC
model, not a verified model of all the primary's assumptions.

## Verdict

The nontrivial phase **survives operator QBC only as a commutative shadow**.
It is not killed, but it is not a genuinely operator-valued phase witness:

- TOBC and NTOBC force the generated algebra to be commutative. Commutativity
  alone does not make a representation a direct sum of scalar ones: a
  commutative algebra can act through nonsplit Jordan or nilpotent extensions.
  The BCPH seed is one scalar representation; non-diagonalizable commutative
  representations are not classified here.
- CPOBC is weaker and permits noncommutativity, but the seed as stated is
  still a commutative solution. The primary's pure-Pauli `d=2` ansatz fails;
  general 2×2 representations are not excluded by it. Constructing a
  noncommutative lift with the same BCPH amplitudes is not done here.
- No ordering-dependent phase value is found for the fixed seed. A claim that
  operator QBC preserves or destroys the phase in general is not supported by
  this audit.

## What would change the verdict

- An explicit CPOBC representation (any dimension) with noncommuting
  transition operators whose scalar data are the BCPH amplitudes and whose
  holonomy is `(3-4i)/5`.
- A proof that no such representation exists in any dimension (a genuine
  operator-QBC no-go).
- A TOBC/NTOBC representation that circumvents the primary's commutativity
  theorem (which would contradict that theorem, so this is not expected).

## Check

`python3 research/qbc-holonomy/check.py` reruns the accepted `bc-nonzero`
certificate and checks its output markers: the 109 product-BC equations,
nonzero amplitudes, MSR/norm-GC through stage 4, and the `(3-4i)/5`
holonomy. It does not construct operator transitions, test each ordering's
reduction independently, or check vector GC.

## Limits

- The operator algebra is cited from the primary, not reimplemented. The
  audit does not construct transition operators on a nontrivial Hilbert space.
- CPOBC's representation space is open, including general 2×2. A restricted
  self-adjoint nonsingular 2×2 obstruction is reproduced in
  `research/refocus-2026-10-21/cpobc-reproduction/`; the non-self-adjoint
  case is not.
- No new primary full-text reads beyond the named sections; no novelty or
  ontology claim.
