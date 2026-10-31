# Bounded arithmetic checks and rigorous completed-value enclosures

Run `python3 research/longshots/bc-matched-diffuse/check.py` from the project.
`output.txt` records the run. The independent reviewer also ran it. Standard
library only; no installs or large searches.

The dyadic interval engine and finite-poset utilities are read from
`../bc-matched-norms/check.py`, present at project commit c6d31f5. The run
records SHA256 c1d1ebbf13757001d57b87e8d4f93d3e4956a8c678015f46d03b1364247dc17d.
Bytecode writes are disabled before loading; no predecessor output is edited.
New model, formal-radical weights, Möbius comparison, row estimates and
completed-event bounds are implemented in this lane's checker.

Real weights are formal linear combinations of square roots of positive
integers, with exact rational coefficients; imaginary parts are exact
fractions. Equality of coefficient expressions is a sufficient algebraic
identity; linear independence of the radicals is not assumed. This verifies
exact recursive-versus-Möbius weight agreement and common later weights on
all enumerated posets. Actual two-chain ideal counts are independently checked
against the number of elements with exactly one ancestor. Direct triangular-
mask enumeration gives labelled counts 1,1,2,7,40,357 through five births.
Their within-level isomorphism counts are 1,1,2,5,16,63.

Outward-rounded 256-bit dyadic intervals enclose the radicals and path
calculations. Per model, the checker verifies 51 MSR rows, 407 strictly
nonzero transitions and 1619 scalar BC pair residual enclosures, for parents
through size four. It also checks nonzero weights through size five, their
reference perturbation bounds, the strict subunit timid modulus, isomorphism
consistency, matched cylinder norm enclosures and minimum-count flow.
Interval residuals containing zero are consistency checks, not equality
proofs. The analytic argument supplies every exact and all-stage claim.

The infinite row-distance series is evaluated as the exact rational

    Z=7715823102531768444113/106782186928294326375000 < 1/8.

Its outward decimal enclosure is [0.072257586442887214,
0.072257586442887215]. The global E2 amplitude error bound is
tau=1/437062500. Starting the same proven tail bound after depth five gives
the following completed-event enclosures (outward, 18 decimal places):

| Quantity | Certified interval |
| --- | --- |
| mu_A(E2) | [0.249999999924922712, 0.249999999924927289] |
| mu_B(E2) | [0.289999999804801796, 0.289999999804808204] |
| mu_B(E2)-mu_A(E2) | [0.039999999879874507, 0.039999999879885491] |

These include infinite-tail error; they are not finite-cutoff predictions.
The simpler all-stage lower bound is >399999/10000000. As an independent
atom check, zeta_4<1/(2L), with decreasing later terms, bounds every actual
transition modulus after parent size four by 1999/2000.

Finally a counterfactual naive tail with shared real f=L^n fails the match:
the size-three chain-plus-isolated precursor has a weight-square difference
1024/25 between models. The proposed opposite parent phases remove that
specific incompatibility exactly. Atomlessness, countable additivity and
priority are not inferred from the finite enumeration.
