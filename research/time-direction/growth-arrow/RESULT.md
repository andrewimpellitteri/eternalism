# Does causal-set sequential growth have a direction by law?

11 November 2026. Native research worker (Claude Code, Fable 5.2), task
`novel-growth-arrow`. A worker submission, not reviewed. No temporal ontology is
selected. Sources and read depths: [sources.jsonl](sources.jsonl). Check:
[growth_reversal.py](growth_reversal.py).

## Verdict

The reading lane's sentence is half right, and the two halves belong to different
models.

| Question | Answer |
|---|---|
| Transitive percolation | **No direction by law.** At every finite stage the probability of an unlabelled causal set equals that of its reverse, exactly. The only asymmetry is that the grown world has a beginning and no end. Known to the authors. |
| Generic sequential growth | **A direction by law, yes.** The measure is not reversal-invariant. It is reversal-invariant at every stage if and only if the model is transitive percolation (Proposition A, elementary). |
| Birth order | **Label gauge**, on the authors' own account. Only the order relation itself is physical. |
| "Built-in direction, no boundary condition" | True of generic growth as a statement about the law. False of percolation, where the beginning does all the work. In neither case is the direction the growth order: it is an asymmetry in the statistics of the order relation. |

In the terms of Proposition 2 of the [settling note](../../agentic-philosophy/settling/RESULT.md):
that proposition assumes a class of worlds closed under reversal. Generic growth
is not such a class, so it escapes the proposition, and it is an example of the
"exact target" named there. Percolation escapes it only through its one-sided
end.

## 1. The setting

Rideout and Sorkin (arXiv:gr-qc/9904062v3, read in full) grow a causal set one
element at a time. The new element's past is a down-set of what exists. For the
generic family the transition probability is λ(ϖ, m)/λ(n, 0), with
λ(ϖ, m) = Σₖ C(ϖ−m, k−m) tₖ, where ϖ is the size of the new element's past, m the
number of its maximal elements, n the size of the parent and t₀ = 1, tₖ ≥ 0 the
free couplings (their eqs. 12, 17). Transitive percolation is tₖ = tᵏ, with
t = p/(1−p).

The probability of reaching an unlabelled order C of n elements is W(C)·P(C),
where W counts natural labellings up to automorphism and
P(C) = Πₓ λ(ϖ(x), m(x)) / Πⱼ λ(j, 0) (their eq. 18). The reverse C* is C with the
order turned over.

## 2. Percolation is reversal-invariant at every stage

For percolation P(C) = p^L q^(n(n−1)/2 − R), with L the number of links and R the
number of relations (Rideout–Sorkin, §4.2). L, R and W are the same for C and
C*. So the stage-n measure is the same for C and C*.

**This is already in the literature.** Rideout and Sorkin's second paper
(arXiv:gr-qc/0003117, passages read) says percolation has "an underlying
time-reversal invariance" and uses "the time-reversal symmetry of the percolation
dynamics" to equate the abundances of an order and its reverse. Wüthrich and
Callender (arXiv:1502.00018v1, §4, passage read) write that "despite appearances
transitive percolation is perfectly time reversal invariant", and suggest growth
in both directions.

The script confirms it exactly, in rational arithmetic, for p = 1/2, 1/3 and 3/4
and n ≤ 7 (2045 orders at n = 7): the largest difference is 0.

**What asymmetry is left.** The completed causal set is past-finite by
construction (Brightwell et al., arXiv:gr-qc/0210061, §2) and almost surely has
no maximal element (stated by Bento, Dowker and Zalel, arXiv:2109.10749, as
"causal immortality", citing earlier work I did not trace). Its reverse is not in the sample space. So a percolation
world has one end, and "away from the end" is a direction. Three facts show this
is the whole of it:

- Percolation on labels 0, 1, 2, … is percolation on all the integers cut off at
  0. Relations between labels in a stretch depend only on the bonds inside the
  stretch. The model on all the integers is symmetric under reflection.
- Bento, Dowker and Zalel's Lemma 3.4: at any finite stage percolation cannot be
  told from "alternating" percolation, which grows a two-way infinite causal set.
  They say of sequential growth that the universe "must have a beginning, by
  definition of the model".
- Originary percolation, where everything descends from a first element, is
  strongly asymmetric at finite stages (total variation 0.34 at n = 7). Condition
  on a last element above everything as well, and the asymmetry vanishes exactly
  (script, n ≤ 7). This is the stretch between two posts with both posts included,
  and it is symmetric for the reason given above.

So in percolation the direction is the beginning, and the beginning is put in
with the choice to start from the empty set and add elements only upward. That
is a boundary condition in everything but name. One can fairly call it a law of
the model. It is then a law of the same kind as "the universe has an initial
moment", not a dynamical asymmetry.

## 3. Generic growth is not reversal-invariant

**Proposition A.** A generic sequential growth model gives every order the same
probability as its reverse at every stage if and only if it is transitive
percolation.

*Proof.* "If" is §2. For "only if", take the order Kₙ with n unrelated elements
under one top element, and its reverse, one bottom element under n unrelated
ones. Each has exactly one natural labelling up to automorphism. Their
probabilities at stage n+1 are tₙ/D and t₁ⁿ/D with the same denominator
D = Πⱼ λ(j, 0). Equality for all n gives tₙ = t₁ⁿ. ∎

I did not find Proposition A stated in this form. It is a few lines, and it is a
close relative of Bento, Dowker and Zalel's Lemma 3.4 and Claim 3.5 (only
percolation treats births to the past like births to the future). It should be
credited to them in substance and not counted as new.

Numbers from the script (exact fractions computed; decimals shown):

| Model | n | Total variation between μ and its reverse | Divergence, bits |
|---|---|---|---|
| Percolation, any p tried | 7 | 0 | 0 |
| tₙ = 1/n! (Rideout–Sorkin's "more lifelike choice") | 5, 6, 7 | 0.256, 0.339, 0.414 | 0.40, 0.64, 0.93 |
| tₙ = 1, 1, 2, 3, 5, 8, 13 | 7 | 0.175 | 0.14 |
| Forest (t₀ = t₁ = 1 only) | 7 | 0.413 | infinite |
| tₙ = 1/n!, conditioned on a bottom and a top element | 7 | 0.027 | 0.007 |

The divergence is how much an observer handed the world without its orientation
learns about the orientation. In the forest model no element has two parents but
elements have many children, so one branching settles it with certainty.

**Where the asymmetry comes from.** Internal temporality and Bell causality are
stated with respect to the past: the weight of each element depends on its past
alone, and elements that are not ancestors are spectators. Percolation is the
one case where the weight factorises into independent bonds, which have no
direction. Bento, Dowker and Zalel call the other models "non-local"
generalisations of percolation. That fits §2 of the settling note, which says a
lawful arrow needs a failure of locality or of Lorentz invariance. The fit is an
analogy only: growth models are classical and are not quantum field theories.

## 4. Birth order is gauge

Rideout and Sorkin, §1.1: "there is no meaningful order of birth of the elements
other than that implied by the relation ≺", and the labels are an "element of
'gauge'". Sorkin (arXiv:gr-qc/0703098v1, §5, read in full) calls the birth order
"an artifact of the description" and the residue beyond the causal order "pure
gauge". Brightwell et al. (read in full) prove that the physical questions of a
generic model are, up to measure zero, combinations of stem questions: "does the
causal set contain this finite order as a down-set?" Stems are themselves
one-sided. They exist because the world is past-finite.

So the direction is not the direction of growth. What is physical is the order
relation and its statistics. A theory that "grows downward" with the mirrored
rule describes the same unoriented worlds with the same probabilities. Which end
is called the past is convention. That the two ends differ is not.

## 5. So: law, or orientation put in by hand?

- **Percolation.** Orientation put in by hand, in the form of a beginning. On a
  stretch between posts the class is reversal-invariant, Proposition 2 applies,
  and any clock there reads back the orientation it is given.
- **Generic growth.** The class is not reversal-invariant, and not only because
  of the beginning (last table row; forest model). Proposition 2 does not apply.
  An orientation-independent clock exists: the number of elements on the finite
  side of an element. The law itself tells the two directions apart. This is a
  lawful arrow in the sense the settling note asks for. It is not a lawful
  passage or growth: §4.

The settling note's line that growth "has a built-in direction … neither needs a
boundary condition" should be split accordingly.

## 6. The project's causal-set proposition

[becoming_causets.tex](../../what-the-past-can-fix/parts/becoming_causets.tex)
shows that a local, covariant becoming relation on causal sets is the causal
order or the universal relation. Its morphisms preserve the order, so the
orientation is an input, and the non-trivial answer hands it back: on the
reversed causal set the relation is the converse. That proposition is about one
world's structure. The present result is about the measure over worlds. They are
compatible. Together: the order relation is the only candidate for becoming, and
whether its orientation is recoverable from the unoriented world is a question
about the dynamics, answered "only from the beginning" for percolation and
"yes, statistically" for generic growth.

## Credits

Dynamics, gauge status of labels, percolation formula: Rideout and Sorkin.
Time-reversal symmetry of percolation: Rideout and Sorkin (second paper);
Wüthrich and Callender. Observables as stems: Brightwell, Dowker, Garcia, Henson,
Sorkin. The beginning as definitional, two-way growth, and the singling out of
percolation: Bento, Dowker, Zalel. Offered here: the exact small-n table,
Proposition A in the reversal form, and the reading against Proposition 2.

## Limits

- Classical growth models are toy cosmologies. Sorkin says they give regions of
  Minkowski spacetime only with vanishing probability. Nothing here is about a
  quantum dynamics or the actual world.
- Exact computation to n = 7 only. Proposition A is general but covers the
  generic family alone, not originary or other exceptional solutions.
- I have not shown that the asymmetry of a generic model survives far from the
  beginning. The weights depend on the count of all ancestors, so the beginning
  is never fully out of the picture. The work on renormalisation of couplings
  after a post (Martin, O'Connor, Rideout, Sorkin; not read) may show the
  asymmetry fades in late epochs. The forest model is a clean case where it does
  not, but it is degenerate.
- The restriction argument in §2 is about labelled stretches. Labels are gauge,
  so it shows where the asymmetry comes from. It is not a statement about
  covariant observables.
- Wüthrich–Callender, Bento–Dowker–Zalel, Dowker et al. (covtree) and Rideout
  and Sorkin's second paper were read in the passages listed, not whole.
