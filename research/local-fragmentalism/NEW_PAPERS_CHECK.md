# Independent check of the four newly supplied predecessors

25 October 2026. Read against the local primary PDFs, not just Claude's
summary. This supplements `COORDINATOR_AUDIT.md`; it does not edit the
concurrently maintained position statement or manuscript.

## Earman: motivation verified, exact-priority inference too strong

Source: Earman 2008, *Reassessing the Prospects for a Growing Block Model of
the Universe*, DOI 10.1080/02698590802496680, published-layout PDF
`02698590802496680.pdf`. Read depth here: selected full-text passages,
especially section 6, printed pp.151–152 (PDF pages 18–19), and related
discussion; not a full-paper audit.

The p.151 passage matches Claude's account: Earman says that the
Minkowski-symmetry-based Clifton–Hogarth uniqueness results do not apply
once that symmetry is lost, and explicitly sets unique definability aside
in favour of studying a natural form of worldline becoming. He then
constructs growing models from causal pasts along worldlines. The p.152
discussion raises the failure of a world's observational past to determine
an entire common block in the presence of horizons.

This verifies a useful predecessor and a stated limitation of the flat
argument. It does not establish that the present result solves the *same*
question under unchanged premises: our theorem adds a single rule over all
GH geometries and reflection/preservation under embedding, permits residual
null freedom, and is off-shell. Nor does the passage establish that no one
addressed the question after 2008. The current paper's restrained wording
(Earman does not pursue a definability result) is preferable to "confirms
the exact open gap we close".

## Goldblatt: relevant semantics, with a curved-spacetime boundary

Source: Goldblatt 1980, *Diodorean Modality in Minkowski Spacetime*,
DOI 10.1007/BF00370321, local `bf00370321.pdf`.
Read depth: abstract and opening definitions/axioms/completeness discussion,
printed pp.219–221; not an independent audit of the full completeness proof.

The S4.2 result is stated for reflexive Minkowski causal-order frames,
including dimensions 2 and 3. This is established prior work for the modal
semantics of the flat standpoint frame, not a classification via gluing of
natural relations on all GH spacetimes. Thus "does not anticipate the
gluing theorem" is defensible at this read depth; "irrelevant" is too broad.

### S4.2 cannot simply be transferred to all GH standpoint frames

Consider the flat, future half-spacetime

    M = (0,infinity) × R^3,   g = -dt^2 + dX^2.

It is GH, with each positive constant-t hyperplane Cauchy. Use the intended
past-directed accessibility R(b,x) iff x≤b, with full causal fragments.
Choose b=(4,0,0,0), p=(1,-2,0,0), q=(1,2,0,0). Both p and q are in b's
strict chronological past. They have no common causal past inside M:
if z=(t,X) were a common past event, the triangle inequality gives

    4 <= |X-(-2,0,0)| + |X-(2,0,0)| <= 2(1-t),

so t<=-1, outside M. Set the propositional valuation V(A)=J^-(p).
Every R-successor of p satisfies A, hence at b the formula diamond box A
is true. But no R-successor of q satisfies A, so at q diamond A is false,
and at b box diamond A is false. Therefore the S4.2 axiom

    diamond box A -> box diamond A

fails on this GH frame. S4 validity follows from reflexivity and transitivity;
no exact modal completeness result for the full GH class is established here.

The current position statement correctly names Minkowski when reporting
Goldblatt. Keep that qualification. The synthesis's suggestion of S4.2
as the general base for the curved-spacetime theory needs this counterexample.

## Belnap: different theorem, still relevant to settledness and history

Source: Belnap 1992, *Branching Space-Time*, DOI 10.1007/BF00414289,
local `bf00414289.pdf`. Read depth here: abstract, introductory discussion,
Definitions 4–5 and Fact 6 (printed pp.392–393); not the whole paper.

Belnap starts with possible point events and defines histories as maximal
directed subsets of a causal ordering. Fact 6 includes downward closure of
histories. These are substantial precedents for causal-order/branching
semantics. They do not by themselves give the cross-spacetime naturality
classification. In particular, the directedness requirement of a history
must not be silently attributed to every GH spacetime (the past-directed
modal counterexample above illustrates why directional confluence matters).

The present reading does not justify certifying whole-paper nonanticipation.
Retain Belnap as a semantics/determinism comparator, especially when the
position invokes settledness or an open future, with read depth labelled.

## Capek: related philosophical content, not an inspected derivation

Source: Capek 1975, *Relativity and the Status of Becoming*,
DOI 10.1007/BF00708432, local `bf00708432.pdf`.
Read depth here: abstract and closing discussion/summary, printed pp.615–616;
not the entire article.

The inspected text argues against postulating pre-existing future events
on observability/methodological grounds. It is pertinent prior philosophy,
but contains bridge premises we must not inherit without argument. For
example, the discussion associates elimination of becoming with rigorous
determinism; our project distinguishes those questions. These inspected
passages do not supply the category-wide gluing theorem. I have not
independently verified every specific Stein/elsewhere attribution in
Claude's fuller reading, so that remains his recorded read-depth claim.

## Disposition

The new sources improve the nearest-predecessor comparison. None of the
passages inspected here states the exact new theorem; that is a bounded
finding, not global priority clearance. Keep three distinctions explicit:
existing causal-past interpretations, existing modal/branching semantics,
and the proposed conditional classification of an all-spacetime assignment.
Goldblatt also supplies a concrete new falsification test for overextending
the semantics from Minkowski to all GH spacetimes.
