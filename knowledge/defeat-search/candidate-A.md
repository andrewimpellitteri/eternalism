# Defeat search: NOVELTY candidate A (growing vs completed history)

Status: 2026-10-19. Independent Claude-subagent pass, abstract-level only. This is
evidence for the novelty gate, not the independent novelty audit, and not a novelty
claim. Coordinator re-verification of identifiers was attempted but the arXiv API was
unreachable; identifiers below are as verified by the subagent via arXiv abstract pages
and Crossref, and are marked pending where the subagent itself did not fetch them.

## Verdict (subagent): partly occupied

- The map from a sequential-growth description to a completed-history (path-space)
  measure, and which covariant observables survive it, is already worked in causal-set
  sequential growth. If a bounded family reduces to a Markov or causal-set growth
  process, the "indistinguishable by construction" half of A looks like an immediate
  corollary of the path-space measure (Ionescu-Tulcea type construction). NOVELTY.md
  says to reject A if its result is an immediate corollary. Proofs not read.
- The philosophy literature argues whether becoming survives covariance but, from
  abstracts, states no operational-equivalence theorem.
- Records formalisms exist; no paper found that uses them to compare growing and
  completed pictures.

## Predecessors (abstract depth)

| Item | Identifier | Relation to A |
|---|---|---|
| Rideout and Sorkin, Classical sequential growth dynamics for causal sets | gr-qc/9904062; 10.1103/PhysRevD.61.024002 | The growing model family; no observer-record comparison |
| Brightwell, Dowker, Garcia, Henson, Sorkin, Observables in causal set cosmology | gr-qc/0210061; PRD 67 084031 | Covariant observables as measurable sets of causal sets: growth-to-path-measure translation within CSG |
| Surya and Zalel, Criterion for covariance in complex sequential growth models | 2003.11311 | When the growth measure extends to covariant observables; measurability, not distinguishability |
| Zalel, Covariant growth dynamics (review) | 2302.10582 | Survey of the dynamical/covariant interface |
| Dowker and Surya, Observables in extended percolation models | gr-qc/0504069 | Title from a search snippet only; abstract not fetched |
| Wuthrich and Callender, What becomes of a causal set | 1502.00018 | Philosophical argument on becoming under covariance |
| Dowker, The birth of spacetime atoms as the passage of time | 1405.3492 | Advocates the growing reading; no distinguishability result |
| Riedel, Zurek, Zwolak, The objective past of a quantum universe | 1312.0331; PRA 93 032126 | Records formalism |
| Hartle, Decoherent histories starting with records | 1608.04145 | Records formalism |
| Earman, Reassessing the prospects for a growing block model | Int. Stud. Phil. Sci. 2008; 10.1080/02698590802496680 | Title and metadata only; content unread |
| Norton, Time really passes | Humana.Mente 4(13); no DOI verified | Not an equivalence result |
| Ellis, Physical time and human time | 2210.10107 | Evolving block universe advocacy |

## Remaining unaddressed sliver (not a novelty claim)

Which access or dynamics assumptions break the equivalence, for example observer
records that are non-covariant or depend on growth order or labelling, and the
classical-to-quantum boundary where the path measure fails to extend (Surya and Zalel's
measurability issue). No observer-access hierarchy for this comparison was found.

## Gaps (so the sliver may be overstated)

Wallden, Sorkin quantum-measure and Dowker records work, Brading, Maudlin, the
Stein/Dieks/Putnam becoming literature, and filtration-based observer-information
formulations were not found or not searched. No full texts were read. One search guess
was a wrong arXiv ID and was corrected by search, which is a reminder to verify IDs.

## Next

Compare with the GLM `kb-novelty-prepass-a` lane when it lands; where they disagree,
record both. A decision on A needs the independent novelty audit.
