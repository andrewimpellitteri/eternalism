# Finite phase-ray class sums: membership survives, interference need not

Finite calculation from 21 October 2026, corrected by the coordinator on
22 October. See `research/observer-access-audit/RESULT.md` for proofs and
independent exact witnesses. This is not a physical observer model or a
completed-causet covariance theorem.

## Three different access algebras

At a fixed stage n, partition the orthonormal history register into finite
isomorphism classes b, with projectors Π_b.

- A cardinality-only record has adjoint image {cI}.
- A classical shape record Γ(rho)=sum_b Tr(Π_b rho)|b><b| has adjoint image
  {sum_b f_b Π_b}, the commutative class algebra.
- Class pinching Δ(rho)=sum_b Π_b rho Π_b has the larger block-diagonal
  adjoint image direct-sum_b B(Π_b H). It preserves within-class coherence
  and removes coherence *between* classes. It is not dephasing within a class.

For any union-of-classes event E, the membership projector
D_E=sum_(C in E)|C><C| is in the last two images. The normalized coherent
filter Q_E=|u_E><u_E|/|E|, u_E=sum_(C in E)|C>, has cross-class matrix elements
and is not in Δ's image when E intersects multiple classes. Γ additionally
loses within-class off-diagonal elements. Event membership and coherent event
measurement must be tested separately.

## What the finite amplitude calculation establishes

For complex percolation at p=(1+i)/2, q=1-p, A_p(C)=p^L q^h, where L counts
covers and h incomparable pairs. Both are finite-poset isomorphism invariants.
The subset

    E_n={C : (L(C)-h(C)) mod8 in {0,1}}

is a union of finite isomorphism classes. In the symmetric binary register,
a_w=p^k q^(n-k) has phase (2k-n)pi/4, constant on word-count permutation orbits.
Both subsets are proper at the tested stages. This proves finite class
measurability of the diagonal event, not access to the coherent target.

Exact selected sums S_n=sum_(C in E_n) A_p(C), preserved from the calculation:

| n | selected classes | |S_n|^2 |
|---:|---:|---:|
| 2 | 1 | 1/2 |
| 3 | 2 | 1/2 |
| 4 | 5 | 205/64 |
| 5 | 16 | 461/32 |
| 6 | 85 | 4938221/32768 |

Binary register |S_n|^2 at n=4,6,8,12,20 is respectively
9/4,25/4,81/4,1089/4,263169/4. These are finite values, not an infinite
causal-set divergence proof or an instrument implementation.

## Exact failure of interference access

At n=3 the chosen event consists of V=(0,0,3) and Lambda=(0,1,1), distinct
singleton classes in predecessor-mask notation. The normalized states
(|V>+|Lambda>)/sqrt(2) and (|V>-|Lambda>)/sqrt(2) give identical Δ and Γ outputs,
but their Q_E expectations are 1 and 0. Their membership probabilities both
are 1. Thus neither channel implements a state-independent coherent filter
on this family, even with a fixed positive calibration. The sharp worst-case
probability approximation error is 1/2. No number of identical independent
channel outputs can recover this lost input distinction without extra access.

In the actual normalized percolation register, A(V)=A(Lambda)=(1+i)/4;
<Q_E>=1/4 before Δ and 1/8 after it. Thus the calibrated scalar target
2<Q_E> changes from 1/2 to 1/4 under this channel. Merely noting that the
phase is constant on each finite class does not protect between-class
interference. This corrects the earlier acceptance's operational wording.

Conversely, symmetry alone does not forbid Q_E: it commutes with permutations
within finite classes. A covariant binary filter is possible in the unrestricted
coherent register. The extra irreversible record channel is a separate premise.
A fixed completely known preparation would be a weaker estimation task than
the all-input filter task and does not satisfy the latter automatically.

## Finite isomorphism invariance is not completed-history covariance

The event lifted to completed histories by selecting the first n births can
depend on the natural labeling. The isomorphic four-element causets
(0,0,3,0) and (0,0,0,3), V plus an isolated point, give opposite E_3 values:
their first three elements are V and the antichain. Appending an identical
infinite universal-top chain yields two natural labelings of the same
completed past-finite causet with opposite event values. The cylinder lift
therefore is not covariant in that completed-history sense.

An existential stem question is different. Its measure and realizable quantum
instrument have not been constructed here. The earlier statement that this
finite test witnesses survival under the cosmological label quotient is
withdrawn; finite class measurability is the valid remaining statement.

## Primary correspondence and checks

The correction re-reads Brightwell et al., arXiv:gr-qc/0210061v2, Sections 2–3
(completed-label covariance and stem definition); Mozota Frauca–Sorkin,
arXiv:1610.02087v1, Section 5.2 Eqs42–46 (superposition filter, including its
endpoint labels); Ludescher et al., arXiv:2607.24976v1, Section II.1 (channel
covariance). Full text at these constructions, not full-paper/priority audits.
Exact source URLs and distinctions are in the new audit.

The original check.py still verifies class constancy and finite sums. It does
not test channel recovery. The independent exact operator and relabeling
checks are research/observer-access-audit/check.py. No observer dynamics,
new quantum-growth theorem, temporal ontology or novelty claim follows.
