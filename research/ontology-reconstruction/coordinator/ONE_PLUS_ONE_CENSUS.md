# The complete 1+1 no-parity census: exactly sixteen assignments

29 October 2026; corrected 30 October. Coordinator deduction, **pending
independent review of the complete census and its refinements**. This
closes the gap flagged by `ontology-persistence-review` ("a complete 1+1
no-parity census not completed; only one explicit fifth family"). It extends
that lane's fifth-assignment finding; it is conditional mathematics on flat
1+1 Minkowski space with the boost subgroup only, and carries **no novelty
claim** — nearest predecessors are named in §6 and a discovery-level
prior-art sweep is recorded in §7.

## 1. Reduction to a boost-invariant past set

Fix the reference standpoint 0 and write P := E_0. Poincaré covariance
(translations plus boosts, no spatial reflection) gives E_b = b + P, so

* S holds iff 0 ∈ P;
* P_t holds iff P is a past set (d ≪ x ∈ P ⟹ d ∈ P);
* F_t holds iff P ∩ I⁺(0) = ∅.

This is the same reduction as PERSISTENCE_CONVENTIONS §3, in the E-space
sign convention; the coordinator file's A := −E₀ is the mirror (a future
set), and the review's A′ for its fifth family is exactly that mirror
object. Everything below is stated in E-space.

Use null coordinates u_L = t−x, u_R = t+x. Boosts act by
(u_L,u_R) ↦ (e^{−η}u_L, e^{η}u_R), and d ≪ x iff both null coordinates
strictly increase. The eight regions are: I⁻, I⁺, the right and left
wedges RW = {u_L<0<u_R}, LW = {u_R<0<u_L}, and four null branches
N⁺R = {u_L=0<u_R}, N⁺L = {u_L>0,u_R=0}, N⁻R = {u_L<0=u_R},
N⁻L = {u_L=0,u_R<0} — the origin apart.

## 2. Mandatory, forbidden, and all-or-nothing regions

* I⁻(0) ∪ {0} ⊆ P: past-closure plus 0 ∈ P. Past nulls are not yet
  forced; they become mandatory under causal persistence or closedness.
* I⁺(0) ∩ P = ∅: F_t.
* Null branches are single boost orbits, so P meets each in all or none.
* Wedge membership is all-or-nothing. Given p=(−a,b) in RW and any
  q=(−A,B) in RW, all a,b,A,B>0, a boost sends p to (−a/h,bh).
  Choose h>max(a/A,B/b); then q≪(−a/h,bh). Boost invariance and past
  closure put q in P. The left wedge follows by the same calculation
  with the two null coordinates interchanged. No dilation is used.


## 3. Chain implications (no cross-side coupling)

Exact timelike witnesses (null coordinates):

* N⁺R ⇒ RW: (0,2a) has (−a,2a′) ∈ RW in its timelike past whenever
  −a < 0 < 2a′ < 2a; saturation upgrades one point to all of RW.
* RW ⇒ N⁻R: (−2a,0) ∈ N⁻R is timelike-past of (−a′,u_R) ∈ RW whenever
  −2a < −a′ < 0; boost invariance upgrades to the whole branch.
* N⁺L ⇒ LW ⇒ N⁻L by the mirror.
* No cross-side implication: the chronological past of a right-wedge
  point can meet only I⁻, RW and N⁻R; the chronological past of N⁺R can
  additionally meet N⁺R. The past of N⁻R is contained in I⁻. These sign
  statements follow directly from both coordinates strictly decreasing.
  The left-side statement is identical with coordinates interchanged.
  They prove sufficiency of every pair of monotone triples, not merely
  absence of a cross-side witness on a finite grid.

Hence, writing each side's triple as (future-null, wedge, past-null) ∈
{0,1}³, a valid assignment satisfies n⁺ ≤ w ≤ n⁻ per side: including the
future-null branch drags in the whole wedge and then the past-null branch
(J⁻-style), while including a past-null branch alone is free. That is the
exact 1+1 shadow of the n≥2 saturation bridge.

## 4. The census

Per side there are exactly four monotone triples
(0,0,0), (0,0,1), (0,1,1), (1,1,1), and the sides are independent, so
**exactly 16 assignments** satisfy S, P_t, F_t and boost+translation
covariance on 1+1 Minkowski space:

| pattern (R, L) | region set | relative to the census |
|---|---|---|
| (000\|000) | I⁻∪{0} | I (Stein/CH survivor) |
| (001\|001) | I⁻∪N⁻∪{0} | J |
| (011\|011) | I⁻∪N⁻∪RW∪LW∪{0} | B (bow tie) |
| (111\|111) | M∖I⁺ | C |
| (000\|011) | I⁻∪LW∪N⁻L∪{0} | review's fifth family (E-space form) |
| (011\|000) | mirror | review's sixth |
| remaining 10 | mixed per-side chains | new enumerations |

Verification: `check_1plus1_census.py` (exact rational arithmetic, 0.03 s)
checks that the 16 are pairwise distinct, boost-invariant, past-closed,
self-inclusive and I⁺-free on a witness grid; that all 8 non-monotone
triples per side break past closure on explicit timelike pairs; wedge
all-or-nothing witnesses; and pointwise agreement of the (000|000),
(001|001), (011|011), (111|111) patterns with the coordinator census
candidates and of (000|011) with the review's in_A construction. Two
checker defects during development are recorded honestly: bit-index
constants from an abandoned flat layout, and causal past/future initially
written as Δx ≤ 0 instead of Δt² ≥ Δx² — both caught by the candidate
cross-check, neither affecting the census. The completeness claim rests on
the analytic orbit/chain argument of §§2–3; the grid is witnesses only.

### Additional premises: hold the exclusion convention fixed

Every row below starts with S, P_t, F_t and boost+translation covariance.
F_c means no nonzero causal-future member; P_c includes null advancement.

| Additional premise | Number | Surviving patterns |
|---|---:|---|
| None | 16 | four monotone triples independently on each side |
| Reflection invariance | 4 | identical right/left triples: I, J, B, C |
| P_c | 9 | past-null bit 1 on each side; 001, 011 or 111 per side |
| F_c | 9 | future-null bit 0 on each side; 000, 001 or 011 per side |
| P_c and F_c | 4 | 001 or 011 per side; J, J+RW, J+LW, B |
| Closedness | 4 | 001 or 111 per side; J, two null half-spaces, C |
| Closedness and F_c | 1 | J |

Reflection **invariance** requires equal triples and gives four assignments.
Merely identifying each assignment with its mirror produces ten equivalence
classes among the sixteen; it does not make the asymmetric rules invariant.

For P_c, J⁻(0) is mandatory by S. Conversely, once both past-null bits
are present, the chronological past-set rule is causally past-closed: a
causal past of an included N⁺R can add RW and N⁻L, and a causal past of an
included RW can add N⁻R; all are present. The mirror cases are the same.
Thus there are nine cases with F_t retained. F_c removes both future-null
bits and leaves four. The earlier claim that a script refuted the count
nine changed F_t to F_c at the same time; it was not a refutation under
fixed premises. `check_1plus1_pc_census.py` checks the four-case P_c+F_c
statement only. The separate refinement checker records both counts.

For closedness, cl(I⁻) forces both past-null branches. Inclusion of a wedge
forces its future-null boundary; conversely a future-null branch already
forces its wedge by past closure. Hence each side must be 001 or 111.
The two asymmetric closed cases have particularly simple descriptions:

    P_L={u_L≤0},       P_R={u_R≤0}.

They are closed null half-spaces, boost-invariant, causally past-closed,
self-inclusive and F_t. Each contains one future-null branch, so both fail
F_c. These counterexamples correct the earlier claim that only J and C
were closed among all sixteen. They also show why the n≥2 transitivity
row cannot be transferred to the asymmetric 1+1 family: a null half-space
is additive, hence its relation E is transitive, while distinct from I,J.
Indeed E is transitive iff P+P⊆P by translation covariance.

The uniqueness of J under closedness+F_c is an assumption-sensitive
corollary here. It is not evidence that existence realms must be closed.

## 5. What this does and does not show

It does show: the persistence review's n≥2 warning is sharp in the
strongest form — outside parity, the census statement fails not by one
exception but by a controlled 16-fold family, and the mechanism (per-side
monotone chains where saturation used to kill all freedom) explains both
the failure and the n≥2 classification's correctness.

It does not establish a curved-spacetime or on-shell Einstein–matter
classification, a philosophical selection, or novelty. Refinements in §4
have a coordinator analytic proof and exact finite witnesses; they still
need an independent review. The n≥2 transitivity/closedness rows apply to
that four-case family, not to this sixteen-case family.

## 6. Nearest predecessors

1. The persistence review's fifth family (this lane, 29 October 2026) —
   the (000|011) pattern; this note generalizes it to a classification.
2. Clifton–Hogarth 1995, Synthese 103:355–387, Theorem 1 — {I, J, U} under
   definability + transitivity + reflexive-chronological inclusion; the
   census and this 1+1 variant drop transitivity and add F_t.
3. Bigaj 2008 (see §7) — considers the complement-of-causal-future
   relation (our B) as a becoming relation under weakened "cumulativity"
   instead of transitivity, with two surviving pairs; a conceptual, not
   census-form, relative.

## 7. Discovery-level prior-art sweep (29 October 2026, this session)

Queries on the becoming/classification lineage (Thyssen four-degrees 2025,
Bigaj 2008 cumulativity, Clifton–Hogarth descendants, BST settled sets,
light-cone partition material). Findings: Bigaj 2008 discusses exactly the
B-type relation under weakened requirements (already flagged by the review
as a near miss at different statement level); Thyssen 2025 remains a
taxonomy, not a classification theorem; no source found stating a
classification of covariant existence assignments, in any dimension, at
census depth. This is a discovery-level negative result feeding the
dedicated prior-art audit the review proposed; it is not a novelty
verdict and does not close that audit.

## 8. Falsifiers

* A 17th assignment: would need a boost-invariant past-closed P meeting a
  region partially, or a valid non-monotone triple — both excluded by
  §2–§3; a concrete witness would refute the census.
* An error in the chain witnesses (e.g. a cross-side timelike pair
  escaping the wedge saturation) would shrink or reshape the 16.
* An earlier statement of the 16-fold census in print would remove any
  residual interest; the dedicated prior-art audit remains open.

## 9. Correction provenance, 30 October

The continuation audit found a duplicated future/past null definition, a
"J⁻ core" label where only I⁻+self was forced, an unjustified grid-based
sufficiency sentence, the reflection-invariance/mirror-quotient confusion,
the closed-half-space omissions, and an implicit transfer of the n≥2
transitivity row. These are corrected above. The sixteen-case base count
is unchanged. The causal-persistence refinement must specify F_t (nine)
versus F_c (four); the earlier nine-to-four correction was a premise change.
No version of this note supplies a novelty verdict.
