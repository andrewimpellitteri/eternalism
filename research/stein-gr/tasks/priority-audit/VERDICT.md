# Priority verdict — cross-spacetime becoming classification (stein-gr)

25 October 2026. Lane `stein-priority-audit`. Audited source: `main.tex`
SHA-256 `7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886`
at commit `0c6d2c5`. This is a bounded priority assessment for the exact
repaired claim, not a correctness certification and not global priority.

## 1. The exact candidate audited

The current manuscript's central claim (Theorem `thm:main` and satellites,
with the second-pass review's repairs incorporated in the statement style):
let **GH** be the category of smooth, connected, 4-dimensional, oriented,
time-oriented globally hyperbolic spacetimes with isometric embeddings onto
causally convex open subsets preserving orientation and time-orientation
(this is exactly Brunetti–Fredenhagen–Verch's category Man; see §3). A
*becoming theory* B assigns to each M ∈ GH a relation B_M that is transitive,
satisfies chronological becoming (CB): I_chr ⊆ B_M, and local covariance
(LC): naturality with respect to every GH morphism ψ: N → M,
B_N = (ψ×ψ)⁻¹B_M on N×N. Then:

- (a) if B_Mink ≠ U then B_M ⊆ J⁻_M for every M; (b) if B_Mink = U then
  B_M = U_M for every M; hence either universal everywhere or
  I_chr ⊆ B_M ⊆ J⁻ everywhere;
- corollaries: co-presence is the identity in every GH spacetime (non-universal
  case); worldline-dependent becoming is worldline-independent;
- classification of the residual freedom: the horismos part N = B ∩ E⁻ is
  exactly a locally covariant subrelation of E⁻ satisfying chain-closure (NC)
  (thm:class); it can be Weyl-curvature-dependent (thm:weyl); closedness
  selects J⁻, openness selects I_chr (prop:reg);
- single-spacetime failure (prop:single) and uniformity-without-locality
  failure via cosmological time (prop:nonlocal);
- causal-set analogue: on locally finite posets with convex order-embeddings,
  every becoming theory is the causal order everywhere or universal
  everywhere (prop:causets);
- totally vicious (Gödel-type) spacetimes are isolated (prop:godel);
- under the dominant energy condition the construction provably fails and the
  transfer reduces to a stated open gluing problem (§energy).

Two distinctions the brief requires:

- **CH's pp. 385–386 remark is an observation, not a posed open problem.**
  The passage (as quoted in the manuscript; primary pages not accessed —
  see SEARCH_LOG) says there is *no obvious way* to extend Theorem 1/2.
  That is a difficulty remark, not a formal problem statement with a
  conjectured answer. By contrast, Stein 1970b (Gödel paper, p. 594) *is*
  an explicitly posed question — but about deforming cosmological models to
  Gödel-type relationships, not about becoming relations. The manuscript's
  §energy open gluing problem is a newly posed precise question; searches
  found no earlier posing of a DEC/on-shell transfer of this classification.
- **Off-shell uniform category theorem vs single-spacetime or on-shell
  theorem.** Every predecessor found is a single-structure theorem (Stein
  1968/1991; CH 1995 Theorems 1–2; WC2017's per-causet failure). No
  predecessor states the all-spacetimes, all-GH-metrics (off-shell) theorem,
  and none states an on-shell (Einstein-equation or energy-condition)
  version; the manuscript likewise leaves the on-shell case open.

## 2. Nearest predecessors, assumption by assumption

### 2.1 Stein 1991 (read full-text) — and Stein 1968 behind it

| | Stein 1991 Theorem (p. 149) | Manuscript thm:main |
|---|---|---|
| Domain | one Minkowski space, n ≥ 2 | all globally hyperbolic spacetimes (category GH) |
| Object | one reflexive, transitive relation R on that space | a family B_M, M ∈ GH, transitive, (CB) |
| Symmetry/invariance | invariance under time-orientation-preserving automorphisms *of that one space* | naturality (LC) across spacetimes; no within-spacetime symmetry assumed |
| Trigger | some past-pointing pair (a,b) ∈ R | B_Mink ≠ U (a Minkowski verdict) |
| Conclusion | R = J⁻ (past causal connectibility) | either U everywhere, or I_chr ⊆ B_M ⊆ J⁻ everywhere |

Stein's proof is exactly the symmetry collapse the manuscript describes
(spacelike pair in R → all spacelike pairs in R → transitivity → universal),
plus a spacelike-chain argument. Nothing in Stein 1968 or 1991 constrains a
second spacetime; Stein 1991 explicitly remarks that GR has "no good
analogue" of distant relative simultaneity and discusses only cosmic-
simultaneity proposals skeptically (pp. 159, 166). **No overlap with the
category-wide statement.** Note also Stein 1968's original formulation uses
the *causal* past ("topological closure of the past", p. 14), so the
manuscript's strict/reflexive repair is a genuine clarification relative to
the whole lineage, not an error-fix of Stein.

### 2.2 Clifton–Hogarth 1995, Theorems 1–2 (pp. 364–372)

Verified through Savitt's verbatim rendering with page locators (primary
pages not accessed). Theorem 1 (p. 365): absolute becoming in
time-oriented Minkowski spacetime, definable from time-oriented metrical
relations, transitive, satisfying chronological becoming ⇒ the relation is
past chronological connectibility, past causal connectibility, or universal.
Theorem 2 (pp. 371–372): worldline-dependent version, all relations in the
collection agree on which of the three they are. Hypotheses are still
single-spacetime; the definability base is metric-plus-time-orientation
*within* Minkowski. The manuscript's thm:flat reproduces Theorem 1 from (LC)
restricted to Minkowski (Poincaré morphisms are GH endomorphisms), with the
manuscript's added observation that the proper orthochronous subgroup
suffices — consistent with Savitt's rendering of CH's definability base as
"time-oriented metrical relations" (no reflections needed), though CH's own
proof pages (365–367) were not read at primary level. Corollary cor:worldline
(removing dependence on λ) is a new formal result relative to Theorem 2: CH
fix becoming per worldline and prove a trichotomy *uniform across worldlines
in one spacetime*; the manuscript proves the verdict does not depend on the
worldline at all, as a consequence of (LC) across spacetimes.

### 2.3 Wüthrich–Callender 2017 (read full-text, 2015-01-30 draft = arXiv v1)

WC's result is the per-structure failure: on the diamond causet, an
automorphism-invariant reflexive transitive relation can include the
non-Hegelian pair (b,c). Footnote 5 concedes the causet "could be a small
proper part of a much larger causet" — i.e. they observe the cross-structure
constraint as a possibility but prove nothing with it. The manuscript's
prop:causets is a different theorem: on the *category* of locally finite
posets with convex order-embeddings, naturality collapses the freedom to one
symmetric bit β and then to order-or-universal. Assumptions differ exactly
in the substitution of within-structure automorphism invariance by
cross-structure naturality; conclusions differ (WC: freedom exists; MS:
freedom is one bit and generically collapses). The manuscript's reading of
WC ("true on its own terms") is accurate. The 2023 handbook survey
(Wüthrich) still contains no embedding-based Stein theorem ('convex' has 0
hits in the full text), which strengthens priority for prop:causets.

### 2.4 Brunetti–Fredenhagen–Verch 2003 and Fewster–Verch 2012 — the under-used neighbors

BFV §2 defines Man precisely as the manuscript's GH (isometric embeddings,
causally convex image, both orientations preserved), and defines locally
covariant theories as functors Man → Alg, fields as natural transformations.
**The manuscript's (LC) is BFV naturality; the only novelty in the
hypothesis is applying it to a preorder-valued assignment instead of an
algebra-valued one.** Priority for the theorem therefore rests entirely on
the classification, and the manuscript is right not to claim novelty for the
locality idea — but the paper should say explicitly that the category and
the naturality schema are BFV's (it cites BFV2003 for the hypothesis, which
is fair, though a reader could miss how exact the transfer is).

Fewster–Verch 2012 contains the structurally closest precedent: their
principle S2 demands that subtheories isomorphic in one spacetime be
isomorphic in all — the same "one-spacetime verdict propagates to all
spacetimes" shape as thm:main(a)/(b). Differences: S2 is a *necessary
condition on a notion of sameness*, they prove the class of all locally
covariant theories *fails* it, and rescue it only for dynamically local
theories; the objects are C*-algebra inclusions and isomorphisms, not
transitive relations between events; the mechanism (transitivity + (CB) +
chain propagation along embeddings) is different. Related (1201.3295)
classifies endomorphisms/automorphisms of theory functors — again not
relations. **No defeat, but this comparison should be in the manuscript's
prior-work section; currently it is not.** This is my strongest criticism of
the manuscript's positioning: the paper's framing "the analogue of
Minkowskian symmetry is uniformity and locality across spacetimes" is
essentially FV's SPASs question applied to relations, and the paper would be
stronger (and safer) acknowledging it.

### 2.5 Stein 1970b deformation question and the time-machine program

Stein 1970b (Phil. Sci. 37:589–601, p. 594) asks whether a cosmological
model can be continuously deformed through Einstein-compatible states to a
Gödel-type state — an explicitly posed cross-model question by Stein
himself. Manchak 2017 and the Earman/Smeenk–Wüthrich/Krasnikov program
address it for causal-structure (time-machine) purposes. None of this
formulates naturality for becoming relations or proves any classification.
The manuscript's §godel isolation proposition and §energy open problem are
the first (in searched coverage) to link the Stein-becoming lineage to
cross-model constraints; but Stein's question is a genuine ancestor for the
*idea* of cross-spacetime constraint and should be cited as such.

### 2.6 Conceptual neighbors (screened, no theorem content)

Viglione 2026 (read full-text): CCC is a metaphysical absoluteness condition;
no formalism; never cites CH. Savitt 2005 (abstract): CTCs vs passage.
Aames 2022 (abstract): causal diamonds, Gödel modal step. Dorato 2002
(abstract): cosmic-time becoming. Myrvold 2003 (abstract): Minkowski quantum
becoming. Müller 2019 (abstract): flat definability via indeterminism.
Saunders 2002 / Callender 2000 (via WC2017 and Savitt CDLP): the shared-
present collapse in flat spacetime — the established flat antecedent of the
manuscript's cor:nopresent. Zalel 2023: label-invariance of growth measures,
a different covariance.

## 3. Verdict

**PURSUE — narrow.** Within the coverage documented in SEARCH_LOG and
sources.jsonl, the exact repaired claim — the off-shell, category-wide
dichotomy (thm:main) plus the horismos classification (thm:class,
thm:weyl, prop:reg), the worldline-independence corollary, the causal-set
exact theorem on convex-embedding posets, and the Gödel isolation — has no
located predecessor. The nearest structural precedent (FV 2012 S2/SPASs) is
different in object and outcome and was found adjacent, not prior. The
causal-set proposition is elementary (as the causet-audit lane will judge)
but formulationally new; even the 2023 survey does not have it. Priority is
bounded: single-spacetime results belong to Stein/CH; the locality
hypothesis belongs to BFV; the flat shared-present collapse belongs to
Saunders/Callender; the "curved-spacetime becoming" philosophical program
belongs to Dieks/Savitt/Arthur/Aames/Viglione as concept, not theorem.

Significance, separated as the brief requires:

- **Mathematical novelty**: moderate and real, but of the "right axiom,
  clean collapse" kind: the theorem is short once (LC) is stated, and its
  proof machinery (spacelike chains, convexity push-up, MS topological
  facts) is standard. The classification thm:class is the most theorem-like
  piece (a genuine correspondence between becoming theories and
  locally-covariant horismos subrelations). Risk: an unsearched "natural
  relations on Loc" corner of the mathematics literature could hold a
  statement in different vocabulary (residual risk 2 in SEARCH_LOG).
- **Physical novelty**: none by itself. The result is off-shell: it
  constrains assignments on *all* GH metrics, and the manuscript honestly
  shows the DEC/on-shell transfer is an open gluing problem. No observable
  content is claimed, and the Weyl example is a statement about conformal
  structure, not physics.
- **Philosophical significance**: the robust/fragile reading (nothing
  outside J⁻ has become unless everything has; uniqueness was a Minkowskian
  artefact) is a defensible, publishable contribution to the relativistic
  becoming debate, and the Gödel-isolation proposition is a sharp new move
  in that debate. But the philosophical bridge premise — that a becoming
  relation should be a single natural rule across all spacetimes, off-shell
  — is exactly what a presentist opponent will contest (cf. Crisp-style
  model restrictions; Viglione's CCC is a different, weaker locality
  demand). The manuscript should state this bridge premise as a premise.

## 4. What would defeat (or shift) this verdict

1. **Primary pages**: CH 1995 pp. 385–386. If CH's closing section proposes
   (not merely laments) a locality/uniformity-based extension — e.g. "the
   relation should be the same in every spacetime" as a definition — the
   *diagnosis* in the manuscript's introduction would be anticipated and the
   framing would need rewriting (the theorem would remain new).
2. **A natural-relations theorem in the mathematics literature**: search
   "natural binary relation on the category of globally hyperbolic
   spacetimes", "invariant relations on Loc", natural operators on
   Lorentzian manifolds (searched once, positively negative; repeat with
   different vocabulary before submission).
3. **Fewster–Verch 2012 full text**: if anywhere in its 60 pages a
   relation-valued or preorder-valued functor is classified, the structural
   precedent becomes a priority problem (abstract + S1/S2 + Loc definition
   read; body not read).
4. **Causal-set literature with faithful/convex embeddings**: any statement
   that cross-structure consistency restores the Stein analogue (checked
   WC2017, Wüthrich 2023, Zalel 2023, Rideout–Sorkin lineage — absent; keep
   monitoring, since the causet community works with exactly these
   embeddings).
5. **Preprints after the search cutoff**: alerts on "becoming" +
   "locally covariant" + "Stein" for the submission period.
6. **The published BJPS WC2017** could differ from the 2015 draft read here
   (footnote 5 or a new paragraph); diff before citing page numbers.

## 5. Directly usable manuscript fixes found by this audit

1. §Prior work should cite Fewster–Verch 2012's S2/SPASs and say why
   thm:main is not an instance of it (different objects; their no-go for the
   full class). This closes the manuscript's most exposed flank.
2. §Prior work should cite Stein 1970b (p. 594) as the explicitly posed
   cross-model ancestor (with Manchak 2017 as the survey), and distinguish
   it from CH's non-question "no obvious way" remark.
3. Corollary cor:nopresent should credit the flat-spacetime antecedent
   (Saunders 2002; Callender 2000; Savitt 2011/2020 rendering); currently it
   reads as if new in every part.
4. The claim "no prior extension of Stein's theorem to curved spacetime"
   (§Prior work, Semantic Scholar sweep) is corroborated by this audit's
   OpenAlex sweep, but the sentence should carry the BFV/FV caveat: the
   locality *framework* is prior; the classification is the new part.
5. Verify the CH pp. 385–386 quotations against the primary pages before
   any submission (this audit could not access them).
