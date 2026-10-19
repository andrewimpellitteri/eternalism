# Defeat search: NOVELTY candidate C (minimal assumptions behind time arguments)

Status: 2026-10-19. Independent Claude-subagent pass at abstract or discovery depth
only; no full text read, and several papers were not reached. Evidence for the
novelty gate, not a novelty claim and not the independent audit. Coordinator check:
the seven DOIs marked (V) below resolve to the stated title, authors, year and venue
via Crossref; the rest are as returned by the subagent's metadata fetches.

## Verdicts (subagent)

- (i) Putnam-style ablation of transitivity, definability and global-present
  premises: partly occupied.
- (ii) Definability-of-simultaneity ablation: occupied on the symmetry and structure
  axes, partly on the rest. A claimed new classification theorem here is very likely
  redundant.
- (iii) New countermodel family: open, but weakly.

## Key predecessors

| Work | Identifier | Content (abstract level) | Bears on |
|---|---|---|---|
| Clifton and Hogarth, The definability of objective becoming in Minkowski spacetime | Synthese 103:355-387 (1995); 10.1007/BF01089733 (V) | Extends Stein's uniqueness to worldline-dependent becoming given adequacy conditions and no privileged worldlines | (i), closest "which premises force which becoming relation" |
| Stein 1991 | Phil. Sci. 58(2):147-167; 10.1086/289609 | Becoming relation uniqueness under natural assumptions; relativizes "real for" | (i); known only second-hand by this subagent |
| Czerniawski, formalization of the Putnam argument | Filozofia Nauki 22(1) 2014; Logic and Logical Philosophy 29 (2020); DOIs unverified | Premise-necessity analysis: transitivity may be avoidable with a modest strengthening elsewhere; relativity principle is the weak point | (i), most likely to contain a partial version of the lattice |
| Thyssen, The Rietdijk-Putnam-Maxwell argument | PhilArchive THYTRA (2023) | Eleven objections; validity underdetermined by SR | (i), informal objection map |
| Thyssen, Conventionality and Reality | Found. Phys. 49:1336-1354; 10.1007/s10701-019-00294-8 (V) | Links the argument to conventionality | (i) |
| Del Santo and Gisin, The relativity of indeterminacy | Entropy 23:1326; 10.3390/e23101326 (V); arXiv 2101.04134 | Rejects a shared "present reality" premise | (i), single-premise rejection |
| Sarkar and Stachel, Did Malament prove non-conventionality | Phil. Sci. 66(2):208-220; 10.1086/392684 | Drop time-reversal invariance and a null-cone relation exists | (ii), countermodel |
| Rynasiewicz 2001 | philsci-archive 350 | Replies the counter-relation is not definable in the needed sense | (ii) |
| Giulini 2001 | BJPS 52(4):651-670; arXiv gr-qc/0011050 | Invariant-equivalence classification: unique for Galilei, none for Poincare | (ii) |
| Besnard, Simultaneity in Minkowski spacetime | Found. Phys. 42:1115-1134; 10.1007/s10701-012-9649-5 (V); arXiv 1104.1263 | Definability from purely local observer data, uniqueness to arbitrariness | (ii) |
| Mamone-Capria, Simultaneity as an invariant equivalence relation | Found. Phys. 42:1365-1383; 10.1007/s10701-012-9674-4 (V); arXiv 1202.6578 | Full classification of invariant equivalence relations under Newton, Galilei, Poincare | (ii), strongest |
| Lefever and Szekely; Madarasz, Stannett, Szekely | arXiv 1707.05371; 2507.21180 | Adding an ether class or absolute simultaneity to SR is exactly characterized up to definitional equivalence | (ii) |
| Andreka, Madarasz, Nemeti et al., logical analysis of relativity | arXiv 1105.0885 | Axiom-by-axiom competing systems | method precedent |
| Stannett and Nemeti, Isabelle/HOL first-order relativity | J. Autom. Reasoning 52:361-378; 10.1007/s10817-013-9292-7 (V); arXiv 1211.6468 | Machine-checked no-faster-than-light result; formalization exposed hidden assumptions | machine-checked precedent, not for Putnam |
| Bacelar Valente, Conventionality of simultaneity and conventionality of chronogeometry | Kairos 20:159-180; 10.2478/kjps-2018-0008 (V) | Ties conventionality to chronogeometry | (ii), unclear if it treats Malament |

No Lean, Isabelle or SMT formalization of the Putnam argument, Malament's theorem or
Stein's theorem was found, from web search only.

## Narrowest unaddressed sub-case found (not a novelty claim)

A single parameterized ablation lattice for the Rietdijk-Putnam argument over
Minkowski (or a weaker causal structure) with premises: (a) relativity principle,
(b) transitive or non-transitive "real-for", (c) definability or invariance of
"real-for", (d) global-present or frame-sharing, (e) an ontic bridge premise labelled
philosophical, giving each premise subset a derivation of "all events are real" or a
countermodel, with machine-checked certificates. Czerniawski 2014/2020 is the likeliest
to hold a partial version; Thyssen's eleven objections could probably be recast as such
a lattice, which would reduce the claim to a formalization of known objections.

## Searches most likely to defeat it

Read in full: Czerniawski 2020; Clifton and Hogarth 1995 (adequacy conditions and any
counterexample constructions); Saunders and Callender universality results; Thyssen's
review; the Renyi-group definability literature in SpecRel; Stannett's Isabelle
development for axiom ablation; Sider, Petkov, Rovelli, Arthur, Dieks; Debs and Redhead
ch. 4; plus a Lean, Isabelle or Mathlib repository search.

## Caveat

The arXiv API was unreachable during checking and the subagent's own arXiv queries
failed, so several arXiv IDs here rest on abstract-page fetches only.
