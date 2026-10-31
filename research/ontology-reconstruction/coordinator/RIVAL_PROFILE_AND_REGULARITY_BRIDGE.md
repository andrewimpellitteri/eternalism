# The source-faithful point profiles and the missing regularity bridge

29 October 2026. Selected primary-clause check and coordinator argument.
This is a limited point-profile comparison, not a full reconstruction of
C&R's free logic, resident ontology, fusions or grounding semantics.

## 1. The source actually includes null growth

Directly checked the user-supplied Chapter 9 of Correia and Rosenkranz,
*Nothing To Come* (2018), DOI
[10.1007/978-3-319-78704-6_9](https://doi.org/10.1007/978-3-319-78704-6_9).
File SHA-256:
`60a8b4d02d0947ae80790b141c9646e0b56f6b45f5719349ae5ecf445d882a6d`.
Selected text: printed pp.137,144,148–149; page images checked for 148–149.
The chapter has 27 PDF pages, starting with printed p.135.

Their p.137 explicitly places the nonvertex null cone inside the causal
future/past. At p.144 (A23R) a spacetime point exists at itself. At p.148,
(P1R) says that what exists continues to exist everywhere in the causal
future; (P2R) excludes a point's existence at standpoints in its causal
past. At p.149 (PO) excludes the point from its elsewhere standpoints,
whereas (BO) includes it there. The page's prose explicitly distinguishes
the pointy and bow-tie versions of relativistic GBT.

Thus the relevant growth order is the *full causal order*, not only
timelike advancement. This is primary support for the P_c/P_t distinction
in [PERSISTENCE_CONVENTIONS.md](PERSISTENCE_CONVENTIONS.md), and a correction
to our workers' premise bookkeeping, not a newly discovered inconsistency
in the rival.

## 2. A bounded translation of the selected point clauses

For a fixed mathematical causal frame, use a metalinguistic assignment

    E_b = {point x : x exists from standpoint b}.

This represents the point-existence profile; it does not identify the
mathematical domain with the presently concrete inventory, or require a
source author to accept a particular model-theoretic implementation.

At this limited level the selected clauses correspond to:

| Source clause | Point-profile condition |
|---|---|
| (A23R), p.144 | b∈E_b |
| (P1R), p.148 | b≤c ⇒ E_b⊆E_c |
| (P2R), pp.148–149 | E_b∩J⁺(b)={b} |
| (PO), p.149 | No spacelike-elsewhere point belongs to E_b |
| (BO), p.149 | Every spacelike-elsewhere point belongs to E_b |

The elementary consequence of the first two is J⁻(b)⊆E_b. The third
excludes every strict causal-future point, including the future null
cone. In a causal frame the fourfold partition is exhaustive. Consequently
(PO) fixes E_b=J⁻(b), whereas (BO) fixes

    E_b=B_b=M\(J⁺(b)\{b}).

These selected point-profile consequences need no Minkowski symmetry or
new classification theorem. They do not establish a complete interpretation
of all quantified formulas or object-location axioms in the book. In
particular the location relation is not automatically existence-entailing;
the previously audited location/fusion distinction remains intact.

The strongest charitable comparison is therefore J versus B, with both
sharing causal persistence and strict causal-future exclusion. The wrongly
advertised I-versus-J binary does not describe this rival dispute.

## 3. Closedness would do real selecting work

In Minkowski space, B_b is not closed. At b=0 take

    z=(1,1,0,0),       z_epsilon=(1,1+epsilon,0,0), epsilon>0.

Every z_epsilon is spacelike to b and hence in B_b. Its limit z is in
the strict causal future of b and hence absent from B_b. In contrast
J⁻(b) is closed.

Thus one can argue conditionally:

    selected point clauses + closed existence realms => reject (BO).

That conclusion depends on **closed existence realms**. No Lorentzian
regularity theorem supplies it: smooth g and even Minkowski geometry are
compatible with both assignments. It is a philosophical bridge from the
geometry of locations to the behavior of an existence predicate, and must
be defended as such.

A bow-tie defender can accept the sequence and reject its ontological limit
inference: approaching a location does not itself make the limiting point
concrete. A pointy defender must explain why this inference is compelling
despite that response. The formal countersequence exposes the disagreement;
it does not settle it.

## 4. Full continuity would covertly settle a different debate

“Existence should vary continuously” is not a neutral substitute for
closedness. Fix a standpoint b in connected M, and let

    e_b:M→{0,1},       e_b(x)=1 iff x∈E_b,

with the ordinary discrete topology on {0,1}. If e_b is continuous, its
image is connected and hence a singleton. Self-inclusion forces e_b≡1,
so E_b=M. Strict future exclusion is then impossible in any spacetime
with a nonempty timelike future of b.

This is an elementary topological fact, not a new physics result. It shows
why a blanket appeal to continuity would already exclude all the growing
profiles under discussion. It would also exclude an ordinary sharp
presentist slice. Merely renaming this strong premise “robustness” would
not justify it.

Nor does pointy J provide open-neighborhood robustness of existence at b:
every neighborhood of b contains excluded future-timelike points. Its
closedness is one-sided limit stability, not full continuity of a binary
inventory. Causal fronts provide the mathematical distinction; whether
existence should follow that particular form of stability is the remaining
philosophical issue.

## 5. The next question is precise but still open

An affirmative argument for pointy existence could now try to justify a
one-sided limit principle for concrete existence without assuming the
conclusion, conflating existence with information, or smuggling in full
continuity. The best objection is that no physical observable or independent
grounding explanation yet requires that principle. Both sides must address
that objection rather than repeat the geometry.

Conversely, a positive bow-tie defense should explain why coexistence of
spacelike points does indispensable explanatory work, rather than merely
assigning them existence by (BO). The authors' extended-object motivation is
a concrete lead, already under source-faithful study in the project; this
note neither refutes it nor validates its full logic.

Eternalism can reject the shared future-exclusion clause, and a foliation
view can reject the structure-free covariance condition of the separate
Minkowski census. Those are further live philosophical alternatives. The
point-profile translation and closure argument do not eliminate them.
