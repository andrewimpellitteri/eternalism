# Candidate exact Hilbert boundary for prescribed cylinder norms

Coordinator derivation, 2026-10-21. **Independent analytic audit found no
counterexample; priority review remains pending.** See `../proof/VECTOR_FOLLOWUP.md`.
This concerns prescribed norms only, not prescribed amplitude
vectors, phases, a decoherence functional or physical quantum dynamics.
It constructs a new vector-measure realization of diagonal cylinder data; it
does not extend the fixed scalar complex-percolation premeasure. Vector
covariance, phase-only relations between isomorphic cylinders and Bell causality
are not asserted by the construction.

## Statement

Let a=|p| and b=|1-p|. There is a norm-countably additive Hilbert-valued measure
μ on the labelled DP-cylinder sigma-algebra, with `||μ(Ω)||=1` and
`||μ(cyl C)||=a^{L(C)}b^{h(C)}` for every doubly-principal C, if and only if

`a²+b²≤1`, equivalently `|p−1/2|≤1/2`.

Exactly the same domain results if every labelled cylinder is norm-prescribed.
The target Hilbert space may be infinite dimensional and may depend on p.
At p=0,1 the ordinary scalar probability measures suffice. For nonreal p in
the disk, the constructed measure has semivariation one and infinite total
variation. Finite-dimensional measures remain excluded at nonclassical p.

## Necessity: squared cylinder sums

A norm-countably additive Banach-valued measure has bounded range; the explicit
uniform-boundedness proof is given in BANACH_NORM_BOUNDARY.md. Write
`M=sup_E ||μ(E)||<∞`.

For any finite disjoint family E_j, average over independent signs ε_j=±1.
The Hilbert inner-product identity gives

`sum_j ||μ(E_j)||² = average_ε ||sum_j ε_j μ(E_j)||² ≤4M²`.

Indeed every signed sum is μ of the positive union minus μ of the negative
union, so its norm is at most 2M. This argument works over real and complex
Hilbert spaces. It uses bounded range rather than any finite-total-variation
hypothesis. A finite semivariation bound yields the same conclusion directly.

Suppose t=a²+b²>1. The two-cap argument applies to the positive weights
A=a², B=b², which need not themselves sum to one. Every DP (k+2)-order is
G with two universal caps. With w=L(G)+M(G)≥k and h=h(G),

`sum_{C DP, |C|=k+2} ||μ(C)||²`
`= A sum_G A^w B^h`
`≥ A t^k sum_G (A/t)^w (B/t)^h`
`= A t^k product_{j=1}^k (1−(B/t)^j)`.

Here A,B>0: p=0 or 1 would instead give t=1. The product has a strictly positive
infinite limit. Thus these squared norm sums diverge, contradicting the uniform
Hilbert disjoint-family bound. This excludes the exterior even when only DP
cylinders are prescribed. It is a different obstruction from scalar variation.

## Sufficiency: conditional edge probabilities in a random environment

Put p=x+iy. The disk condition says `y²≤x(1−x)`, so 0≤x≤1. Handle x=0,1
as the deterministic endpoints. For 0<x<1 let

`t=y²/[x(1−x)] in [0,1]`.

Let G be a random variable in [0,1] with this law: with probability 1−t it
equals x, and with probability t it is Bernoulli with mean x. Directly,

`E G=x`, `E G²=x²+y²=a²`,
`E(1−G)²=(1−x)²+y²=b²`.

Take independent copies G_e on all forward pairs of natural-number vertices.
Conditional on this environment, include each forward edge independently with
probability G_e, then form the transitive closure. This is an ordinary joint
probability model on countably many environment and edge variables, not a
complex probability law. Let F be its history sigma-algebra, and define

`μ(E)=E[1_E | environment]` in `H=L²(environment)`.

Conditional expectation here takes equivalence classes; no simultaneous choice
of pointwise versions over every measurable set is needed. It is linear and a
contraction on L². For a disjoint tail union T_N,

`||μ(T_N)||_2 ≤ ||1_{T_N}||_2 = P(T_N)^{1/2} →0`.

Hence μ is countably additive in norm on the full labelled history sigma-algebra.
Its total mass is the constant one. For a finite naturally labelled order C,
its closure event requires the L cover edges present and the h incomparable
edges absent; all remaining comparable edges may be chosen freely. Conditional
on the environment this has probability

`μ(cyl C)=product_{cover e} G_e product_{incomparable e}(1−G_e)`.

Independence of the G_e then gives

`||μ(cyl C)||_2² = (E G²)^L (E(1−G)²)^h = a^{2L} b^{2h}`.

Thus every cylinder has the required norm, and restriction gives the DP result.
For any finite disjoint family and |α_j|≤1, the conditional expectation of its
simple function has modulus at most one almost surely; its L² norm is at most
one. Taking Ω attains one, so semivariation is one.

At nonreal p, the audited scalar modulus sum over DP levels diverges, so the
constructed measure has infinite total variation. It does not take values in a
fixed direction and does not retain p's complex phase. On the boundary circle,
t=1 and G is Bernoulli: conditioning on the environment determines every edge,
so this reduces to the earlier L² indicator construction. For real p, t=0 and
the environment is deterministic, recovering scalar classical probabilities.

## Verification and limits

`check_hilbert_environment.py` checks the finite three-point moment law and all
finite cylinder second-moment identities through rank four at four rational
(x,y) examples, including the real and boundary cases. It independently sums
environment configurations on forced edges and verifies the two-cap squared
level formula through degree five. The infinite construction and divergence
are proved above; finite checks are corroboration only.

The ingredients are standard: conditional expectation, product Bernoulli edges,
the Hilbert sign-average identity, and the existing two-cap probability bound.
No priority claim has been established for this specialization. The earlier
bounded source searches did not audit conditional-probability random-environment
constructions as a potential defeater; that is now a required priority check.
This should not be described as an accepted new quantum dynamics or as a result
about temporal ontology. The scalar theorem retains its original statement.

In particular the constructed decoherence functional
`D(E,F)=E[P(E|environment)P(F|environment)]` is nonnegative on event pairs and
has only constructive interference. On the nonreal boundary circle its diagonal
is an ordinary additive classical probability, whereas at real p it reduces to
the already-known rank-one product probability functional. Preserving single
cylinder norms has not preserved the finite-union or off-diagonal predictions
of the original complex scalar model. This is a substantive scope limitation,
not merely a change of representation.
