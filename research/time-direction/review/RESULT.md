# Bounded contract review: time direction

Reviewed inputs (SHA-256, as read):

| Input | SHA-256 |
|---|---|
| `research/time-direction/ARROW_READ.md` | `4f71d21314fabf6314fec60c98f6908adddf7d93710021400eb85016ebba0a4b` |
| `research/what-the-past-can-fix/main.tex` | `9d103bb5b71d6e573ec97a471fa7136849962705bf13aee912d2a172715804b9` |

## Finding

The exact mirror proposition is correct once “law invariant under pullback” means the **entire comparison class** is carried bijectively to itself by the isometry. Here `F_L(S)` quantifies over globally admissible solutions on the fixed spacetime `M`, so invariance of field equations alone is insufficient when boundary conditions, regularity restrictions, topology, or a selected solution subclass break that closure. The same proviso applies to the claims about Einstein–scalar twins and all Part II/III results. For `Det`, the geometry alone suffices; an orientation-reversing isometry maps past-inextendible curves to future-inextendible curves.

There is also a quantifier shift in the prose. The isometry formula compares `F^-_L(b)` with `F^+_L(theta(b))`, not generally with `F^+_L(b)`. A same-event equality needs a reversing isometry fixing `b`, or a separate theorem. Likewise, without a spacetime isometry, reversing the time orientation gives a paired description on the reversed-oriented spacetime; it does not establish a same-event equality between the two cones in the original oriented model. This is a representational symmetry of the mathematical contract, not by itself a claim about ontology or objective passage.

The smallest clear overreach is the Past-Hypothesis conjecture that exact fixing “barely changes” because a macrocondition does not fix exact values. A boundary restriction changes the quantifier domain defining `F_L`, and a coarse boundary condition can, together with the equations and global admissibility, imply exact values. For a minimal illustration, take histories on `M=R` satisfying `q'=0` and `q(q-1)=0`. The unrestricted admissible class consists of the two constant histories `q=0` and `q=1`. Add the coarse boundary bin

\[
q(0)\leq \tfrac12.
\]

The boundary bin selects only `q=0`, so it fixes an exact value despite being stated as a coarse inequality over the ambient variable. This toy example does not model cosmological thermodynamics, and because both histories are already fixed by agreement on any open past interval, it does not show that the fixing set itself changes in this particular model. It shows that “macrocondition” alone supplies no general bound on how much exact information the restricted admissible class contains. Whether a particular Past-Hypothesis class changes exact fixing little, much, or not at all requires its actual equations, phase space, measure and admissibility conditions. Probabilities over completions are a distinct construction and do not follow from the exact-fixing definition.

## Proposed replacement: proposition and consequences

Replace the proposition and proof in `sec:direction` with:

> **Mirror proposition.** Fix a spacetime `M`, event `b`, and a class `L` of fields on `M`. Let `theta:M -> M` be an isometry reversing time orientation. Assume pullback by `theta` maps `L` bijectively onto itself (including its boundary and global-admissibility conditions). Then
> \[
> \theta(F^-_{\mathcal L}(b))=F^+_{\mathcal L}(\theta(b)),\qquad
> \theta(\operatorname{Det}^-(b))=\operatorname{Det}^+(\theta(b)).
> \]
> Here `F+` is defined by agreement on `I+(b)`, and `Det+` by future-inextendible causal curves meeting `I+(b)`. The first equality follows by pulling back each pair of comparison solutions; the second follows because `theta` exchanges the two curve orientations. Without such an isometry, the same argument relates the theory on `(M,g,orientation)` to the paired theory on `(M,g,reversed orientation)`, provided the admissible solution class is transported with it. It gives no equality between `F-_L(b)` and `F+_L(b)` in the original model unless an appropriate symmetry fixes `b`.

Replace “Under equal bases each side is as fixed or unfixed from the other” and the categorical conclusion around it with:

> The mirror proposition gives an exact correspondence at symmetry-related bases (or at the same base when the reversing isometry fixes it). Thus the fixing definition itself privileges neither orientation: reversing the orientation and transporting the entire model class transports the fixing result. This covariance alone does not imply that past- and future-based fixing sets coincide at an arbitrary event in one fixed model, nor that records, chances, causal direction, or what exists are symmetric. Any inference from “past fixed, future open” to an ontology needs additional premises about those matters.

For the examples, qualify the Einstein–scalar sentence as conditional on the complete globally admissible class used in Theorem `same-past` being preserved by reversal, and call the consequence a **paired future-base theorem** at `theta(b)` (or the corresponding event in the reversed-oriented model). The stated closed-dust consequence `Det+(b)=M` for `eta_b<pi` is consistent: it uses the reflection and the past guarantee at `theta(b)`, rather than a fixed-base equality. “Every fixing result has an exact mirror” should be read with the same model-class closure hypothesis.

## Proposed replacement: Past-Hypothesis paragraph

Replace the final paragraph of `sec:direction` and the corresponding “open question” in `ARROW_READ.md` with:

> A Past-Hypothesis restriction generally makes the admissible class non-invariant under time reversal, so the mirror proposition cannot be applied to that restricted class unless the boundary condition is also transported and the resulting comparison is stated explicitly. No general conclusion about exact fixing follows from the condition being macroscopic: intersecting a coarse boundary set with the global solution space can either leave many exact completions or select exact data. The outcome depends on the specified dynamics, boundary set and admissibility class. Conditional probabilities over completions require, in addition, a measure and conditioning rule; they are distinct from exact fixing. Determining the fixing sets or probabilities for a physical Past-Hypothesis model remains open here.

This keeps the proposed “chance given a base” distinction as a possibility, not a result. The sentence that entropy/statistics “make entropy higher on both temporal sides” and the claims about records and prediction are inherited summaries of Albert at the partial depths tabulated in `ARROW_READ.md`; this review did not inspect the cited originals. They should remain attributed and qualified as such. The mathematical mirror argument and the counterexample above do not verify those thermodynamic claims.

## Scope and first open obligation

This is a local analytic review of the definitions and passages in the two hashed inputs. It is not a literature audit or a reproduction of the physical examples. The review inherits the source-depth limits recorded in `ARROW_READ.md`: Albert and Price are partial reads, Tooley 1997 is not closely read, and the account itself says the new section was not yet red-teamed. The paper’s own appendix labels `sec:direction` elementary and based on partial reading; that label is appropriate only after the class-closure and quantifier qualifications above.

The first open obligation for any stronger Past-Hypothesis claim is to state one explicit dynamical model, its phase space and globally admissible solution class, the precise boundary subset, and (if chance is claimed) the measure and conditioning event. Then compute both exact fixing sets under that restricted class and the relevant conditional distributions. No such model-specific conclusion is established here.
