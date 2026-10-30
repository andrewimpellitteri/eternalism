# Where future exclusion enters: a scale-sensitive reconstruction

30 October 2026. Coordinator analytic deduction, pending independent review.
No novelty claim. This extends the internally reviewed n≥2 census rather
than assigning an ontology to its solutions. Nearest formal predecessor:
Clifton–Hogarth 1995 Theorem 1, through the project's inherited full-text
[audit](../../../knowledge/audits/clifton-hogarth/AGENT_REPORT.md). Recovering
its I/J/universal conclusion below is a consistency check, not a new result
attributed to this project. No new full reading of that primary scan is
claimed here.

## 1. Drop the ontological future-exclusion premise

Work on all Minkowski R^(1+n), n≥2. Retain self-inclusion S, chronological
persistence P_t, and proper orthochronous Poincaré covariance, as defined in
[PERSISTENCE_CONVENTIONS.md](PERSISTENCE_CONVENTIONS.md). Do not assume F_t,
closedness, transitivity, dilation invariance, or a preferred observer.

Translation covariance gives E_b=b+P, P=E_0. P is a Lorentz-invariant
chronological past set containing 0. Write C=M\I⁺(0). For a>0 define

    P_a^< = C ∪ {x∈I⁺(0): τ(0,x)<a},
    P_a^≤ = C ∪ {x∈I⁺(0): τ(0,x)≤a}.

**Candidate complete classification.** P is exactly one of

    I=I⁻(0)∪{0}, J=J⁻(0), B=M\(J⁺(0)\{0}), C,
    P_a^< or P_a^≤ for one a∈(0,∞), or M.

This strengthens the earlier collar counterfamily to a proposed complete
list. Its proof is elementary; mathematical priority is not inferred.

## 2. Proof, including the previously uncontrolled case

If P contains no timelike-future member, the internally reviewed four-case
census gives I,J,B,C. Suppose it contains a future-timelike point of proper
length a>0. Lorentz invariance puts (a,0) in P and includes its entire
future-timelike norm-a orbit.

Every future-timelike point of length b<a is included: (b,0)≪(a,0), then
apply Lorentz invariance. All spacelike points are included as well. For
the representative p=(0,R e₁), take

    q_Z=(√(a²+Z²), Z e₁).

It lies on the included orbit, and q_Z−p has positive time component and
Minkowski proper-length square a²+2ZR−R²>0 for large positive Z. Thus p≪q_Z.
Lorentz transformations carry this representative to every spacelike point
of length R; n≥2 allows spatial directions to be reversed without reflection.

Every future-null point is included too. For p=(k,k e₁), k>0, choose
q=(a cosh η,a sinh η e₁). Then q−p has proper-length square
a²−2ak e^(−η)>0 and positive time component for sufficiently large η.
Hence p≪q. Lorentz invariance supplies the full future-null cone. Past
nulls lie chronologically before some included spacelike point, e.g.
(−1,−e₁)≪(0,−e₁), and all chronological pasts plus 0 were mandatory.
Consequently C⊆P whenever any timelike future is admitted.

Future-timelike membership depends only on τ by Lorentz orbit transitivity.
The set of admitted positive τ is nonempty and downward closed. If bounded
above, it is (0,a) or (0,a] at its positive supremum a; if unbounded, it is
all positive reals. These give exactly the remaining candidates.

Conversely each candidate is a past set. The only additional check beyond
the four-case theorem is the collar. If y≪x and y is future-timelike,
then x is future-timelike and τ(0,y)<τ(0,x) by the reverse timelike triangle
inequality. Thus membership below either threshold is preserved. If y is
outside I⁺(0), it is already in C. S and covariance are immediate. ∎

## 3. Two ways to derive future exclusion, each with a substantive cost

**Scale assumption.** Require δ_s(P)=P for all s>0, where δ_s(x)=sx about
the reference standpoint. If p∈P is future-timelike, then sp∈P for every
s>0. For any event x, sp−x is future-timelike for sufficiently large s:
its positive quadratic leading term is s²τ(0,p)². Hence x≪sp, so past
closure gives x∈P. Therefore

    P_t + dilation invariance + P≠M  =>  F_t.

This short implication does not need the full classification, self-inclusion,
or Lorentz invariance. At the homogeneous point-rule level, it replaces
explicit future exclusion by a scale assumption plus nonuniversality.
Under the full base premises it leaves I,J,B,C. Finite collars violate
dilation invariance because δ_s(P_a)=P_(sa).

**Transitivity assumption.** E is transitive exactly when P+P⊆P.
Every finite collar fails: p=(3a/4,0) is admitted but p+p=(3a/2,0) is not.
B and C fail by the previously checked spacelike-sum example. I,J,M are
additive. Thus the extended classification with transitivity gives I,J,M;
nonuniversality removes M and entails F_t. This matches the named
Clifton–Hogarth conclusion at the level of these explicit homogeneous
rules. It does not establish that our premises are identical to every
logical/definability condition of their theorem.

Neither route assumes future exclusion as a displayed axiom. Neither has
established it from Einstein's equations. Transitivity of reality-at is
precisely what some standpoint-relative accounts dispute. Dilation
invariance is stronger than metric-isometry covariance: a fixed nonzero
proper-time collar respects every Poincaré isometry. A physical theory with
mass parameters or Λ may supply scales relevant to an existence rule.
Changing measurement units while transforming all quantities is not the
same requirement as keeping one rule invariant under δ_s at fixed data.
The scale premise therefore needs its own justification and category.

### A further semantic cost: what does nonuniversality mean?

If E_b is intended as the **entire concrete inventory** at b, requiring
E_b≠M already excludes the universal-inventory interpretation of eternalism.
It is therefore not a neutral physical premise from which that interpretation
has been defeated. The scale implication classifies proper inventories;
it supplies no independent reason why the concrete inventory is proper.

If E_b instead denotes events locally available, settled, or having become
for b, nonuniversality can be accepted by an eternalist. One can assign
concrete existence C_b=M and local causal availability A_b=J⁻(b) on the same
physical model. A satisfies all the scale, persistence, exclusion and
closedness clauses selecting J, while C remains universal. This is a
counterinterpretation to an inference from the shape of A to the extent
of C, not a claim that all ontologies are equivalent or a gauge symmetry.

Thus two bridges must be separated: (i) why a proper relation is physically
or explanatorily significant, and (ii) why its members exhaust concrete
existence. An access/determination argument may address (i) without
establishing (ii). The finite-readout programme strengthens a particular
failure of causal-past determination; it cannot supply this identification
by itself. The next positive ontological argument must defend that semantic
and explanatory role against the universal-inventory counterinterpretation.

## 4. What regularity would and would not add

P_a^≤ is closed: its complement {x∈I⁺:τ>a} is open. P_a^< is open: the
excluded set {x∈I⁺:τ≥a} is closed for a>0 (equivalently t≥a and
t²−|x|²≥a²). Both are proper, self-inclusive, causally persistent rules;
causal past steps weakly decrease τ for a timelike-future endpoint.
Thus closedness or openness alone does not supply F_t.

Closedness together with transitivity and nonuniversality leaves J at
this scope. Closedness together with dilation invariance and
nonuniversality leaves J,C; adding causal-future exclusion removes C.
These are different premise packages. All use an ontological boundary or
composition condition in addition to physical symmetries.

The philosophical advance is a more discriminating question: why should an
existence relation be additive/transitive, or insensitive to physical
scales, or stable under limits of existing events? A metric's smoothness
does not answer any of those. A defender should identify the independent
explanatory or semantic role of the chosen premise; an opponent can then
contest that role without contesting Lorentz geometry.

## 5. Audit targets and kill conditions

An omitted Lorentz-invariant past set, a failed saturation step, or a
collar counterexample to a claimed converse would refute this classification.
The direct scale implication can be checked independently of the census.
An existing Lorentz-invariant past-set classification may make the entire
calculation an immediate corollary; the quota-interrupted prior-art lane had begun
searching that lineage but produced no completed review of this later note.
No claim here is accepted from the interrupted dispatch.

No curved-space, matter-enriched, complete free-logic or global temporal
ontology classification follows. In particular the proof says nothing
about objective passage, dynamical determinism, present truth grounds or
what an observer can measure without additional premises.
