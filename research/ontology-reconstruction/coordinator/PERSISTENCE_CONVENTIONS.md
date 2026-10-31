# Persistence, null boundaries, and a corrected flat-space census

29 October 2026; reviewed 30 October. **Internally reviewed conditional
census for n≥2**, with the scope and errata recorded in
[the review disposition](REVIEW_DISPOSITION_2026_10_30.md).
This corrects a common premise error in the classification and both
equivalence submissions. No ontology or novelty verdict is claimed.

## 1. The decisive elementary correction

Write x≪b for strict chronological order and x≤b for reflexive causal
order. Let E_b be the events assigned to standpoint b. Distinguish

    S:     b∈E_b,
    P_t:   b≪c  =>  E_b⊆E_c,
    P_c:   b≤c  =>  E_b⊆E_c.

In any causal spacetime (indeed any ordered set),

    S + P_c  =>  J⁻(b)⊆E_b.

Proof: if x≤b then x∈E_x by S, and E_x⊆E_b by P_c. The same proof
with P_t gives chronological-past inclusion. Neither implication needs
Lorentz invariance, field equations, transitivity of E, or an embedding
principle. In particular,

    S + P_c + (E_b⊆J⁻(b))  =>  E_b=J⁻(b).

Thus the equivalence submissions' claimed *two* expansions under those
three clauses are actually *one*. Their other candidate I⁻(b)∪{b} fails
P_c: take b=(0,0,0,0), c=(1,1,0,0). Then b∈E_b but b∉E_c, since b<c
is null. It satisfies P_t. The distinction was absent from the programs'
claimed persistence verification.

The classification worker's I⁻∪{b} row must therefore change from ✓ to ✗
under its explicitly causal A3. Its six-rule table is not a correct
category-wide classification as submitted. The earlier restriction and
domain repairs in BATCH2_INITIAL_REVIEW remain necessary too.

## 2. Prior work before the replacement claim

The project's full-text [Clifton–Hogarth audit](../../../knowledge/audits/clifton-hogarth/AGENT_REPORT.md)
records their 1995 Theorem 1, pp.365–367: under chronological inclusion,
Poincaré invariance and **transitivity**, the candidates are reflexive
chronological past, causal past, or universal. Their chronological relation
is reflexive by convention; that is our I⁻∪{b}. This theorem does not assert
P_c for every candidate. We inherit the audit's precise primary-reading
provenance; the entire scan has not been reread for this note.

Thyssen's [Conventionality and Reality](https://doi.org/10.1007/s10701-019-00294-8)
(2019), §§3.4 and 7–8, read selectively here, already distinguishes
standpoint-relative reality from a single reality value and discusses the
elsewhere present and the disputed transitivity premise. His elsewhere-only
present is not either past-plus-elsewhere realm below. This is prior
philosophical context, not a claim that the following census occurs there.

What follows changes the formal premises: P_t in place of transitivity,
and an explicit future-exclusion clause. Its proof is elementary Lorentz
geometry. A bounded reconstruction of this kind must not be advertised as
new before a dedicated prior-art audit.

## 3. A four-case census without assuming transitivity

Work on all of Minkowski spacetime R^(1+n), n≥2. Assume:

* S and chronological persistence P_t;
* covariance under the proper orthochronous Poincaré group;
* **F_t:** E_b∩I⁺(b)=∅ (no strictly timelike-future member).

No closure, causal boundedness, null-future exclusion, transitivity,
dilation symmetry or cross-spacetime restriction is assumed.

**Internally reviewed theorem at the stated scope.** Exactly the following four assignments satisfy the
conditions:

    I_b = I⁻(b)∪{b},
    J_b = J⁻(b),
    B_b = M\(J⁺(b)\{b}),
    C_b = M\I⁺(b).

B and C include the spacelike elsewhere. They differ on the future null
cone. These are stipulated mathematical candidates, not reconstructions of
every clause of a named ontology. Their labels must not overwrite the
distinct elsewhere-only present in Thyssen or a source author's own null
convention.

### Proof

For a fixed target event 0 put A={b:0∈E_b}. Translation covariance makes
E completely recoverable from A: x∈E_b iff b−x∈A. Lorentz covariance makes
A invariant under the origin stabilizer; P_t makes A a chronological
future set. S+P_t gives I⁺(0)∪{0}⊆A; F_t excludes I⁻(0) from A.

**Spacelike saturation.** If one spacelike q is in A, every spacelike
point is in A. To see this, let R>0 be its spacelike length. For any S>0
Lorentz invariance supplies in A

    q_Z=(−sqrt(Z²−R²), Z, 0,...,0),       Z>R.

Choose Z also larger than S and (R²+S²)/(2S). Then q_Z≪p_S=(0,S,0,...,0),
because the squared positive time difference minus spatial distance squared
is `2ZS−R²−S²>0`. P_t gives p_S∈A. Proper spatial rotations and boosts
carry p_S to every spacelike point of length S; n≥2 permits reversing a
spatial direction by a proper rotation. Since S was arbitrary, saturation
follows. There is no dilation assumption in this argument.

**Spacelike membership forces the future null cone in A.** Once all
spacelike points are in A, each future-null (s,s e), s>0, is chronologically
above the spacelike (0,s e), so lies in A.

**Past-null membership forces spacelike membership in A.** The proper
Lorentz group is transitive on the nonzero past null cone. If that cone
meets A, take q=(−1,−1,0,...,0)∈A. Its chronological future contains the
spacelike p=(−1/4,−1/2,0,...,0), since 3/4>1/2. Saturation follows.

If A has no spacelike member, it therefore contains no past-null member;
the future null cone is one orbit and is either wholly included or wholly
absent. This gives A=I⁺∪{0} or J⁺, hence E=I or J.
If A has a spacelike member, saturation includes all spacelike points and
the future null cone. The past null cone is again all-or-none. Since the
timelike past is excluded, A is M\(J⁻\{0}) or M\I⁻, hence E=B or C.

Conversely all four candidates are covariant and self-inclusive. For I,
chronological persistence follows from causal/chronological composition,
including its diagonal case. J is causally persistent. For B, if x is not
strictly future of b, it cannot be strictly future of a causally later c:
b≤c<x would imply b<x. For C use b≤c≪x⇒b≪x. Thus B and C are also
causally persistent. Each satisfies F_t. This establishes both exhaustiveness
and the converse at the stated Minkowski scope. ∎

## 4. Which additional premise actually selects what?

All statements in this table are relative to the preceding base conditions.
“Closed” means closed in the ordinary spacetime topology at each standpoint.

| Extra conditions | Surviving assignments |
|---|---|
| None | I, J, B, C |
| Causal persistence P_c | J, B, C |
| F_c: E_b∩J⁺(b)={b} | I, J, B |
| P_c and F_c | J, B |
| Closedness | J, C |
| Closedness and F_c | J |
| Transitivity of the existence-at relation | I, J |
| Transitivity and closedness | J |
| Causal boundedness E_b⊆J⁻(b) | I, J |
| Causal boundedness and P_c | J (elementary §1, symmetry unnecessary) |

Checks behind the table: cl(I_b)=J_b and cl(B_b)=C_b, so I and B are not
closed. J and C are closed. B and C fail transitivity on the same triple
b=(0,0), x=(0,2), y=(2,−1), embedded in a timelike two-plane: x∈E_b and
y∈E_x, but y∉E_b. I and J are transitive. The future null cone distinguishes
C from the stricter future-exclusion cases. Nothing here defines those
philosophical premises as neutral.

The n≥2 assumption can be weakened to n=1 if spatial reflection is included
in the covariance group. Without reflection in 1+1 additional assignments
exist, so n≥2 is load-bearing for the census statement itself: the
independent persistence review (29 October 2026,
`ontology-persistence-review`) constructed and machine-checked a fifth
candidate A'={0}∪{a∉I⁻(0): t_a+x_a>0} (with E_b={x:b−x∈A'}), which is
Poincaré-covariant, self-inclusive, chronologically persistent and F_t
because t+x scales by e^η>0 under boosts and grows along timelike futures.
Its standpoint-0 membership pattern differs from I, J, B and C; its mirror
gives a sixth. The later coordinator [complete 1+1 census](ONE_PLUS_ONE_CENSUS.md)
gives sixteen cases and a separate refinement table. That extension was
outside this review and awaits its own audit. Its corrections on 30 October
are essential: reflection invariance versus mirror classes, four closed
rules including two null half-spaces, and nine P_c+F_t cases versus four
P_c+F_c cases. No n≥2 table row should be transferred without checking.

## 5. Removing future exclusion restores many closed persistent rules

F_t is already an ontological restriction. To display its force, for each
a≥0 define, on the same metric Minkowski space,

    E^a_b = M\{x∈I⁺(b): τ(b,x)>a},

where τ is the timelike geodesic proper-time separation. These assignments
are closed, Poincaré-covariant, self-inclusive and causally persistent.
Closedness follows because the removed set is open. For persistence, if
b≤c and x∈I⁺(c), reverse timelike triangle inequality gives
τ(c,x)≤τ(b,x). Consequently τ(c,x)>a would already exclude x from E^a_b.
If x∉I⁺(c), it is automatically in E^a_c. This proves E^a_b⊆E^a_c.
They differ for different a; E^0=C and a>0 allows some timelike-future
events. Whole-history E_b=M supplies another candidate.

Thus covariance, closedness and causal persistence do not select J on their
own. Positive a adds a Lorentz-invariant scale, not a preferred slicing.
These are consistency examples, not defended physical ontologies.

## 6. Philosophical consequence and remaining tests

The sharp disagreement is not resolved by calling persistence reasonable.
One must say whether the growth order includes null advancement, whether
future exclusion includes the null future, and why existence should be
topologically closed or transitive. Each choice eliminates a specific rival
for an identifiable reason. The census exposes these costs; it does not
justify the choices or prove that a changing concrete inventory is needed.

Completed check: independent audit of the saturation proof, quantifiers and
table at n≥2. Next: focused comparison against earlier becoming/persistence results;
then a source-faithful test of which named rival actually accepts which
premise. No curved, on-shell Einstein–matter, or arbitrary enriched-category
classification follows from the flat-space calculation.

The small standard-library [witness check](check_persistence_witnesses.py)
checks the null-step failure, boundary sequences, transitivity triple and
several exact saturation witnesses in four-dimensional Minkowski space.
It is not an enumeration proof of the continuous-domain census.
