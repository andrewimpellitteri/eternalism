# Prior-work audit for the central-history and contraction notes

31 October 2026. Claude Code (Opus 5.5), at the user's request. A bounded comparison
with the nearest works, not a survey and not a novelty claim. Absence from this
search proves nothing. Read depth is stated per source.

## Result

**Nothing here should be presented as a new idea.** The setting, its global
regularity statement and the core difference method are in print. The only piece
with no match found is the inverse statement itself, prescribing a whole central
history, and that is the kind of consequence a specialist may regard as routine
once the scattering map exists. Its flat linear version is elementary.

| Our item | Nearest source | Verdict |
|---|---|---|
| Past does not fix later readings | Manchak 2008; Geroch 1977 | **Known in general.** Ours is a worked coupled example |
| The class: compact ℐ⁻ data, vanishing center, flat cone | Kehrberger, Remark 6.1 | **In print** |
| Small data give a complete, globally regular solution | Kehrberger, Remarks 2.4 and 6.1, citing Christodoulou 1993; also LOY Theorem 1.7 | **Stated in print**, as a remark |
| Exterior existence and uniqueness of the scattering solution | Kehrberger, Theorems 2.5(b), 6.1 | **In print**, exterior only and in a fixed gauge |
| Grönwall on differences, Cauchy sequence, uniqueness of the limit | Kehrberger §2.1 | **Same method**, in a different setting |
| Finite control by disjoint bumps and a topological theorem | Kehle–Unger | **Same toolkit**, different target |
| Mass does not restore determination | Carlotto–Schoen | **Answered in a different category**, abstract only |
| Vertex-uniform Lipschitz bound through the regular center | none found | Not found. Expected to be routine |
| Whole central history prescribed | none found | Not found. Linear case elementary |
| Prefix masses fixed at finite cuts | none found | Not found. Rests on the flux identity |

## The sources

**Kehrberger, *The Case Against Smooth Null Infinity I*, arXiv:2105.08079.** Read in
the ar5iv rendering, which gives no version: Theorems 2.4, 2.5, 6.1, Remarks 2.4, 6.1,
and the §2.1 limiting passage, at full-text depth for those loci. Remark 5.7's text
as extracted is not the uniqueness statement Theorem 6.1 points to, so the exact
uniqueness sense was not confirmed.

- Theorem 2.5(b) treats a Minkowskian i⁻ with smooth compactly supported rφ=G(v) on
  ℐ⁻, and gives "a unique smooth semi-global solution".
- Remark 6.1 describes vanishing data on the center with compact data on ℐ⁻, with a
  backwards null cone carrying rφ=0 by domain of dependence.
- Remark 2.4 and Remark 6.1 say that small data give a causally geodesically complete,
  globally regular solution, attributed to Christodoulou 1993, with LOY Theorem 1.7
  also cited.
- §2.1 describes "a careful Grönwall-type argument on the differences of two
  solutions", establishing a Cauchy sequence and uniqueness of the limit. That passage
  concerns its timelike-boundary construction.

Differences: Kehrberger's solutions are semi-global, the regular center appears only
in that remark, and the paper's aim is asymptotics at ℐ⁺. No continuity of the data
map was seen in the loci read, and no central trace. Normalization also differs:
rφ=G on ℐ⁻, against our 2∂_v(rφ)=Φ.

**Kehle–Unger, arXiv:2211.15742.** Fetch summary of the first 100,000 characters only.
Characteristic gluing in spherical symmetry with ϕ_α=Σα_jϕ_j, disjoint supports, and
Borsuk–Ulam on the finite conditions. The target is gluing to Reissner–Nordström, not
readings at a center. C11's note that its degree step may be familiar is right as to
method.

**Manchak 2008 and Geroch 1977.** As read in
research/bowtie-horizons-prior-art/prediction/RESULT.md, full-text there. Manchak's
theorem places genuine prediction on the boundary of J⁻(q), for any spacetime. This
is a stronger general conclusion than ours on a narrower notion of prediction. Ours
adds only a specific coupled model class. Not reread here.

**Carlotto–Schoen, arXiv:1407.4766.** Abstract and search summaries only. Positive-ADM
data exactly trivial outside a cone. This is a Cauchy-data statement, without
spherical symmetry.

**Christodoulou 1993, CPAM 46.** Not read. Known here only through Luk–Oh and
Kehrberger. LOY v1 and Luk–Oh: as listed in the other notes.

**Linear case.** rφ=F(v)−F(u) gives φ(t,0)=2F′(t) directly. Searches on
Lax–Phillips and radiation fields found no statement of this value at the origin,
which says little, since it is a two-line computation.

## Consequences

**For CONTRACTION.md and RESULT.md.** Their scheme is standard. What remains is a
specific small application: closing the difference estimate through the regular
center, uniformly in the vertex, and reading off a central trace. Any write-up should
cite Kehrberger and treat this as a routine corollary unless a specialist says
otherwise.

**For the coordinator's notes.** SMOOTH_FINITE_CONTROL.md works in the setting of
Kehrberger Remark 6.1, and no coordinator note read here cites it. The remark asserts
regularity and completeness without proof, resting on Christodoulou 1993. The project's
bootstrap is therefore a detailed route to a stated result, not a new conclusion, and
this should enter the prior-result comparison. Whether "globally regular" there means
smooth was not determined. Christodoulou's text is needed for that.

**For the narrow rival in CARD.md.** The view that coupling and mass tie later readings
to the past is already undercut by Carlotto–Schoen at the level of initial data, on an
abstract-level reading, and by the existence of this very class. The Einstein-coupled
case adds no philosophical content not available from those sources.

## Limits

- The four searches were targeted and few. Russian-language and control-theory
  literature on Einstein systems was not searched in depth.
- The published versions of LOY and Kehrberger were not compared.
- Kehrberger's §§4–6 proofs, Christodoulou 1993 and Kehle–Unger's later sections were
  not read.
- A specialist could settle this in minutes. No agent-based audit replaces that.
