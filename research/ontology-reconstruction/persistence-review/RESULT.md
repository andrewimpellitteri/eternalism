# Line-by-line proof-obligation audit: PERSISTENCE_CONVENTIONS.md

29 October 2026. Independent adversarial review (worker
`ontology-persistence-review`). Target:
`research/ontology-reconstruction/coordinator/PERSISTENCE_CONVENTIONS.md`
at commit `634988e` ("Correct causal persistence premise and derive bounded
flat-space census"). Verdicts are mine; the coordinator owns acceptance.
Read-depth labels: **A** = analytic re-derivation by me; **W** = exact
finite witness check (scripts in this directory); **S** = source-correspondence
check. No claim below is a novelty claim; see §6.

Verdict summary: **every analytic obligation of the coordinator's §1, §3, §4
and §5 verifies; no material error found; the n≥2 hypothesis is necessary,
not merely convenient — a fifth covariant persistent assignment exists in
1+1 without parity (constructed and checked below).** Four precision notes
(N1–N4) and the required retractions (R1–R3) are listed.

Notation follows the coordinator: x≪b strict chronological, x≤b reflexive
causal, S: b∈E_b, P_t: b≪c ⇒ E_b⊆E_c, P_c: b≤c ⇒ E_b⊆E_c,
F_t: E_b∩I⁺(b)=∅, F_c: E_b∩J⁺(b)={b}. Candidates
I=I⁻∪{b}, J=J⁻, B=M\(J⁺\{b}), C=M\I⁺.

## 1. The collapse claim (§1)

| Obl | Statement | Verdict | Route |
|---|---|---|---|
| O1 | S + P_c ⇒ J⁻(b) ⊆ E_b, in any reflexive transitive order | **verified** | A, W |
| O2 | S + P_c + (E_b ⊆ J⁻(b)) ⇒ E_b = J⁻(b) | **verified** | A (from O1) |
| O3 | I fails P_c at b=(0,0), c=(1,1): null step, b∈E_b, b∉I⁻(c)∪{c} | **verified** | A, W |
| O4 | I satisfies P_t (≪ transitivity + diagonal case) | **verified** | A, W |
| O5 | Classification row I⁻∪{b} under causal A3 must flip ✓→✗; two-case bounded census collapses to one | **verified** | A (from O2–O3) |

O1 is one line: x ≤ b gives x ∈ E_x (S) and E_x ⊆ E_b (P_c). No Lorentz
symmetry, field equations, transitivity of E, or embedding principle is
used — confirmed. The same argument with P_t gives I⁻(b)∪{b} ⊆ E_b, which
is exactly why I is the least S+P_t assignment (checked as a least-fixed-point
computation on the witness grid, `check_independent.py` O1/O1b).

Precision note N3: "any ordered set" should read "any set with a reflexive
transitive relation"; causal order in a time-oriented spacetime is a partial
order, so the claim stands as applied.

## 2. Prior-work placement (§2)

| Obl | Statement | Verdict | Route |
|---|---|---|---|
| O22 | CH 1995 Theorem 1 (pp. 365–367) gives {I, J, U} under definability + transitivity + reflexive-chronological inclusion; their I⁻ is reflexive by convention (= our I); it does not assert P_c | **verified** | S (inherited audit) |
| O23 | Thyssen 2019 distinguishes standpoint-relative reality and discusses the elsewhere bowtie present and the transitivity objection; his elsewhere-only present is **not** B or C | **verified** | S (open-access HTML fetch) |
| O24 | The census changes formal premises (P_t for transitivity, explicit F_t) and must not be advertised as new before a dedicated prior-art audit | **verified** | S (searches, §6 here) |

Consistency cross-check (mine, stronger than the coordinator states): CH
Theorem 1 and the census do not merely fail to conflict — they *interlock*.
Our S+P_t implies CH's chronological becoming; adding CH's transitivity to
the census eliminates B, C (they fail transitivity, exact triple checked),
leaving {I, J} (census table row 7); CH lacks F_t, which is exactly why U
survives there and not here. The two classifications are restriction and
extension of each other along the transitivity and F_t axes. Read depth:
CH via the project's full-text audit (primary scan not reread this task);
Thyssen 2019 at abstract + outline + §2 + bowtie-passage depth of the
open-access article (§§3.4, 7–8 not fully read); see sources.jsonl limits.

## 3. The four-case census (§3)

| Obl | Statement | Verdict | Route |
|---|---|---|---|
| O6 | Translation + Lorentz covariance reduce E to E_b = b−A, A Lorentz-invariant; the sign x∈E_b ⇔ b−x∈A is correct | **verified** | A |
| O7 | P_t makes A a chronological future set | **verified** | A |
| O8 | S + P_t ⇒ I⁺(0)∪{0} ⊆ A | **verified** | A |
| O9 | F_t ⇒ A ∩ I⁻(0) = ∅ | **verified** | A |
| O10 | SO⁺(1,n), n≥2: transitive on each fixed-norm spacelike shell (de Sitter homogeneity), on each null nappe, and SO(n) on S^{n−1} | **verified** | A (standard facts; explicit boost construction) |
| O11 | q_Z ≪ p_S ⇔ 2ZS > R²+S², with q_Z = (−√(Z²−R²), Z, 0…), p_S = (0,S,0…) | **verified** | A, W (exact, iff both directions) |
| O12 | One spacelike member ⇒ all spacelike members (no dilation used) | **verified** | A, W |
| O13 | Spacelike saturation ⇒ A-space future null ⊆ A (i.e. past-null membership of each standpoint) | **verified** | A, W |
| O14 | A-space past null (future-null member) ⇒ spacelike saturation, witness (−1,−1) ≫ (−1/4,−1/2) | **verified** | A, W |
| O15 | Case analysis exhaustive: A ∈ {I⁺∪{0}, J⁺} (no spacelike) or {M\(J⁻\{0}), M\I⁻} (spacelike), by the five-region partition and orbit all-or-nothing | **verified** | A |
| O16 | Back-translation yields exactly I, J, B, C | **verified** | A (all four recomputed through the sign flip) |
| O17 | Converse: each of I, J, B, C satisfies S, P_t, Poincaré covariance, F_t | **verified** | A, W |
| O18 | No fifth assignment under the stated premises, n ≥ 2 | **verified** | A (attempts below) |
| O19 | n ≥ 2 caveat: without parity in 1+1 "the orbit argument changes; no census asserted" | **verified and strengthened** — the 1+1 statement itself fails: a fifth assignment exists (§5 here) | A, W |

Notes on O17: B's persistence one-liner in the coordinator's text
("b≤c<x would imply b<x") silently assumes x ≠ b; the x = b edge case also
works (c ≤ b with b ≪ c would give b ≪ b), but a final writeup should state
it. J and C are the two-line compositions; I needs the diagonal case. All
four pass S, P_t and F_t on the full witness grid
(`check_independent.py` O17a–d).

Notes on O10: the saturation step implicitly uses single-orbit transitivity
of the norm-R shell ("Lorentz invariance supplies q_Z"). That is correct for
n ≥ 2 and has an explicit constructive form — a boost of rapidity η with
cosh η = |v_space|/R and a spatial rotation generate every spacelike vector
of proper length R, negative rapidity handling the past-leaning ones — but
the final writeup should cite the construction rather than "invariance
supplies". Precision notes N1–N2.

## 4. The added-premise table (§4)

Row-by-row, all verified (failure witnesses exact; survival proofs analytic):

| Row | Extra premise | Claimed survivors | Verdict | Key check |
|---|---|---|---|---|
| 1 | none | I, J, B, C | **verified** | census |
| 2 | P_c | J, B, C | **verified** | I fails (O3); J,B,C persistence re-proved |
| 3 | F_c | I, J, B | **verified** | C keeps N⁺ ⊆ J⁺\{b}; I,J,B cut down to {b} |
| 4 | P_c ∧ F_c | J, B | **verified** | rows 2∩3 |
| 5 | closedness | J, C | **verified** | cl(I)=J, cl(B)=C; boundary sequences exact |
| 6 | closed ∧ F_c | J | **verified** | rows 5∩3 |
| 7 | transitivity | I, J | **verified** | exact triple b=(0,0), x=(0,2), y=(2,−1) kills B and C; I,J transitive on witness set |
| 8 | transitivity ∧ closed | J | **verified** | rows 7∩5 |
| 9 | causal boundedness | I, J | **verified** | B,C hold spacelike members |
| 10 | boundedness ∧ P_c | J only | **verified** | O1/O2; "symmetry unnecessary" confirmed |

Row 3 wording check: F_c is E_b∩J⁺(b)={b}; I survives because I⁻∩J⁺=∅
(were x ≪ b and b ≤ x, x ≪ x). Row 7's triple: x spacelike from b, y
spacelike from x, y strictly timelike future of b — B and C fail, I and J
survive, exactly as claimed.

## 5. Red-team: strongest attempted counterexamples

**(a) Fifth assignment in the asserted scope (n ≥ 2): failed, as the proof
predicts.** Attempts: (i) norm-bounded elsewhere (spacelike members of
bounded proper length) — dies by the saturation bridge, exact negative
controls in `check_independent.py` O11 (large S breaks the chronological
step); (ii) one-sided null additions — impossible, each nappe is a single
SO⁺ orbit for n ≥ 2; (iii) mixed wedge assignments — the π-rotation about a
coordinate axis (det +1, orthochronous) reverses any spatial direction,
killing one-sidedness; (iv) collar-style F_t violators — excluded by F_t
by design (they are exactly §5's family). Each failure instantiates a
necessity step of the census, which is the expected signature of a correct
exhaustiveness argument.

**(b) Fifth assignment in 1+1 without parity: exists.** This is my positive
result and it *confirms* the coordinator's scoping rather than refuting the
census (which is asserted only for n ≥ 2). Define, in (t,x) coordinates,

    A' = {0} ∪ {a ∉ I⁻(0) : t_a + x_a > 0},      E_b = {x : b − x ∈ A'}.

Proof sketch (full analytic case analysis in `check_1plus1_fifth.py`):
t+x is rescaled by e^η under boosts, so its sign is boost-invariant; I⁻ and
{0} are invariant, so E is Poincaré-covariant (boosts + translations). Every
a ∈ A' has t_a+x_a ≥ 0, equality only at 0; if d ≫ a then t_d+x_d >
t_a+x_a, so the future of A' never meets the left wedge (t+x<0), the left
null branch (t+x=0), or the timelike past (t+x<0); the remaining regions
are precisely A', so A' is a future set, equivalent to P_t for E. S holds
(0 ∈ A'), F_t holds (A' ∩ I⁻ = ∅). At standpoint 0 the membership pattern
(left-spacelike, future-null, past-null x<0, past-null x>0) is
(T, F, T, F), whereas I is (F,F,F,F), J and B are (F,F,T,T), C is
(T,F,T,F with future-null T) — distinct from all four. By the parity mirror
there is a sixth; combinations of null branches generate further cases, so
a full 1+1 census is a different, larger classification. **Consequence: the
n≥2 hypothesis is load-bearing for the census statement itself. The
coordinator's hedge was necessary and should be upgraded from "the orbit
argument changes" to "additional assignments exist" (N4).**

## 6. The collar counterfamily (§5) and interpretation scope (§6)

O21, all verified: E^a_b = M\{x ∈ I⁺(b) : τ(b,x) > a} is covariant (τ is
Poincaré-invariant), self-inclusive, closed (removed set is open; τ
continuous on I⁺), causally persistent (reverse triangle inequality
τ(b,x) ≥ τ(b,c)+τ(c,x); exact witnesses), E⁰ = C (full test set), E^a ⊋ E^a'
for a > a' (exact collar points at τ = 1, 3/2, 5), E^∞ = M, and a > 0
violates F_t by construction. Hence covariance + closedness + causal
persistence do not select J — C alone is a counterexample witness — and the
collar family shows F_t is doing real restrictive work. The coordinator
correctly labels these consistency examples, not defended ontologies, and
correctly observes that a > 0 adds a Lorentz-invariant scale, not a
preferred slicing.

Scope and interpretation, verified: B and C are past-plus-elsewhere realms;
Thyssen's bowtie present is elsewhere-only, a strictly different region
(primary passage fetched: "the present for b … is just the absolute
elsewhere of b — a spatially extended bowtie-shaped region"). No claim of
the file asserts a metaphysical selection, a curved/on-shell
classification, or novelty; §6's "remaining tests" list matches what this
review performed.

## 7. Retractions and repairs required elsewhere

R1. Any row or clause presenting I⁻∪{b} as causally persistent (the
classification submission's causal A3 row) must flip ✓→✗ (O3).
R2. The equivalence submissions' two-case census under S + P_c + causal
boundedness is one case, J (O2). BATCH2_INITIAL_REVIEW §1's warning stands
and is now verified.
R3. Any suggestion that covariance, persistence and closedness select J
must be dropped: C and the collar family survive those three (§6).
No retraction needed for PREMISE_STRESS_TEST §1 (it assumes no F_t; its
E_all/E_past lesson is complementary to, not contradicted by, the census),
nor for BATCH2's witness repair, restriction-compatibility scope, sign
convention fix, or bow-tie row (the project's bow tie B matches the census
candidate exactly).

## 8. Novelty posture

No prior statement of this four-case census was found; nearest formal
relatives are CH 1995 Theorem 1 ({I,J,U} under transitivity, no F_t),
Stein's J⁻ theorem, Thyssen 2019's elsewhere-present discussion (different
region), Thyssen 2025's four *degrees* (conceptual taxonomy, not a
classification theorem), Bigaj's B/O incompatibility (different statement),
and Placek's co-presence incoherence result (symmetric relation). This is a
discovery-level negative search, not a novelty verdict; the coordinator
claims none, and none should be inferred. Prior-art audit remains a
separate open task.

## 9. What was checked and what was not

Checked analytically and by exact witnesses: everything in §§1, 3, 4, 5 of
the coordinator file, at the level of individual proof obligations
(O1–O24). Not done: a Lean formalization; a complete 1+1 no-parity census
(only one explicit fifth/sixth family); rereading the CH primary scan
(inherited full-text audit used); full reading of Thyssen §§3.4, 7–8;
exhaustive search of the growing-block and "wide present" literatures.
Finite checks are witness checks; the census exhaustiveness remains an
analytic claim, which I have re-derived and here report as sound at its
stated scope.
