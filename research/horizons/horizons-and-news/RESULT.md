# Horizons and news: when can the past of an event be surprised?

11 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. The proposition is elementary and close to the paper's own
guarantee theorem. The quantum statements belong to the cited authors. No temporal
ontology is selected. Sources: [sources.jsonl](sources.jsonl).

Companion to the notes on [massive fields](../massive-minkowski/RESULT.md) and
[cone algebras](../cone-algebras/RESULT.md). Those found that on Minkowski spacetime a
massive field of finite energy is fixed everywhere by any past light cone. This note
asks what happens with a beginning or a cosmological horizon, which is the case that
applies to us.

## 1. The criterion

Call a non-empty open set K **hidden from** an event b if no event of K has a causal
past meeting the chronological past of b.

**Proposition 1.** Let the spacetime be globally hyperbolic and consider any linear
field equation with finite propagation speed and global solutions for smooth compactly
supported data, for instance the Klein–Gordon equation of any mass. If some open set is
hidden from b, there is a non-zero smooth solution vanishing on the whole chronological
past of b. So the past of b does not fix the field, whatever the mass.

*Proof.* Nothing in the causal future of K lies in the past of b either: if
c ≤ z ≪ b with c in K, then c ≪ b, and then the past of c would meet the past of b.
Take smooth data supported in K on a Cauchy surface through K. The solution is
supported in the causal future and past of K, which do not meet the past of b. ∎

**Where it applies.**

| Spacetime | Is something hidden from b? | Check |
|---|---|---|
| Minkowski | Never. Any two events share a past | The massive result stands |
| Global de Sitter, b at conformal time η_b at one pole | Always. Events near the opposite pole at conformal time below −η_b | Verified from the conformal diagram and by a numerical scan |
| Big-bang FLRW with a particle horizon, b at conformal time η_b | Always. Events at comoving distance beyond η_b + η_c | Immediate in conformal coordinates |
| Closed dust before maximum expansion | Yes | Agrees with the paper's massive-field theorem |
| Closed dust from maximum expansion on | No. The past contains a Cauchy surface | Agrees with the paper |

## 2. What decides it

Three cases, by the shape of the past boundary of spacetime.

| Past boundary | What can be news | Why |
|---|---|---|
| A single point at past timelike infinity, with null infinity around it (Minkowski) | Massless fields only | Massive energy arrives from that one point, which every past cone contains. Massless data arrive along null infinity, which no past cone contains |
| Spacelike: a big bang or the past infinity of de Sitter space | Every field, any mass | Different regions of the boundary are hidden from each other. Proposition 1 |
| None needed: the past contains a Cauchy surface | Nothing | The paper's guarantee theorem |

So the slogan from the earlier note needs its scope stated. "Only light can be news"
is a fact about spacetimes whose past timelike infinity is a point. It is false in
de Sitter space and in every big-bang model with a particle horizon, and so it is false
of a universe like ours.

## 3. A universe like ours

Flat ΛCDM with round Planck values. The past of an observer meets the initial slice in
a ball of comoving radius 46.1 billion light-years today. Because of dark energy that
radius converges to 62.8 billion light-years. Initial data inside the limiting ball and
outside today's ball can still reach the observer. Data outside the limiting ball never
can.

| Share of the limiting ball already in the observer's past | Cosmic age | From now |
|---|---|---|
| 40% | 13.8 Gyr | now |
| 50% | 18.1 Gyr | +4.3 Gyr |
| 90% | 49.3 Gyr | +35.5 Gyr |
| 99% | 90.2 Gyr | +76.4 Gyr |
| 99.9% | 130.6 Gyr | +116.8 Gyr |

The shell of data still to arrive shrinks to nothing, with an e-folding time of
17.5 Gyr. So for one observer the supply of news from the initial slice is finite and
is being used up. This is a statement about nested sets: the shell is non-empty at
every finite time and its intersection over all times is empty. The percentages use
comoving volume, which is one measure among several; the
[finite-openness lane](../../longshots/finite-openness/RESULT.md) records that the
limiting radius and the volume ratio are in Gott et al. (2005), and that proper volume
and arriving signals do not converge.

Two things do not follow. The past of an event never comes to contain a Cauchy
surface, so the whole universe is never fixed from it. And what lies beyond the limiting
ball is not fixed from the observer's past at any time. What becomes fixed, in the
limit, is everything that can ever affect that observer.

## 4. The quantum mirror

For an observer in de Sitter space, Chandrasekaran, Longo, Penington and Witten state
that the algebra of an arbitrarily thin neighbourhood of the worldline equals the
algebra of the observer's static patch, by the timelike tube theorem, and that the
algebra of the complementary patch is its commutant. They add that the observer "has no
way to know what there is beyond the horizon and therefore has no knowledge of a global
quantum state". Nothing in this depends on the mass of the fields.

Set beside the [cone-algebra note](../cone-algebras/RESULT.md):

| Background | Massless | Massive |
|---|---|---|
| Minkowski | Past and future cone algebras commute. The observer's past is a proper subsystem | The past-cone algebra is that of a larger set (unverified whether everything) |
| De Sitter | The observer's whole worldline generates only the static patch algebra, with a non-trivial commutant | The same |

The classical and quantum columns agree again. A horizon makes an observer's history a
proper subsystem for every field, and removes the difference that mass made.

## Limits

- Proposition 1 is close to the paper's guarantee theorem and adds only that hidden
  regions defeat fixing for every linear hyperbolic law at once.
- "Hidden" as defined is sufficient for news, not necessary. Minkowski spacetime has
  nothing hidden and massless fields are still news there.
- Section 3 is standard cosmology. Its reading is the contribution, and the measure is
  conventional.
- Section 4 quotes results for quantum fields on a fixed de Sitter background. The
  cited paper's main subject, the algebra once gravity is included, is not used.
- Linear fields throughout. Nothing here addresses gravity's own degrees of freedom.
