# What the past cone fixes for a massive field in Minkowski spacetime

10 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. The mathematics is known or an immediate corollary of known
results. What is offered is its bearing on the paper. No temporal ontology is selected.
Sources: [sources.jsonl](sources.jsonl). Illustration: [cone_energy.py](cone_energy.py).
Paper edits, applied 11 November: [PATCH.md](PATCH.md).

## The claim

The paper's Minkowski row says a deterministic field is fixed from an event's past
exactly on its causal past. Its witness is a plane wave of infinite energy. For a
massive field the verdict depends on the class of solutions:

| Law and class on Minkowski spacetime | What the past of an event fixes |
|---|---|
| Massless, all smooth solutions | The causal past (the paper's result) |
| Massless, finite energy, three space dimensions | Not everything |
| Mass m > 0, all smooth solutions | The causal past |
| Mass m > 0, finite energy | Everything |

A massive field carries nothing in from null infinity. Its energy arrives from past
timelike infinity, which lies inside every past light cone.

## Proofs

**Finite energy, m > 0 (one space dimension).** Let a finite-energy solution vanish on
the past of the origin. At each t < 0 its energy lies in |x| ≥ |t|. By Burnol's
Theorem 1, time-reversed, that energy tends to zero as t → −∞. Energy is conserved and
is a norm, so the solution is zero. The same argument works on the tail of the cone
alone, and in the future direction. In higher dimensions it needs the same decay of
energy outside the light cone, which is standard and which I did not check at a
source. The spherically symmetric case in three dimensions reduces exactly to one
dimension (see the [same-past note](../../lawful-completions/massive-same-past/RESULT.md)).

**All smooth solutions, m > 0.** Let x lie outside the causal past of b. Choose null
coordinates u, v with u negative on the past of b and positive at x. The equation for
functions of (u, v) is 4φ_uv + m²φ = 0, and j(z) = J₀(m√z) is entire with
z j″ + j′ + (m²/4) j = 0. For smooth h ≥ 0 supported in (0, ∞),

    φ(u, v) = ∫₀ᵘ h(s) j((u − s)(v − c)) ds for u > 0, and 0 for u ≤ 0,

is a smooth solution vanishing on the past of b, and it is positive at x for suitable
h and c. A finite-difference check gives a residual of order 10⁻⁸. These solutions grow
like a modified Bessel function and have infinite energy.

**Massless, finite energy.** The spherically symmetric solution with
rφ = f(t + r) − f(t − r), f smooth with support in (1, 2), has finite energy, vanishes
on the past of the central event at t = 0, and is non-zero later.

## Illustration

Fraction of energy outside the past cone, one space dimension, Gaussian data:

| m | t = −50 | t = −200 | t = −700 |
|---|---|---|---|
| 0 | 0.999 | 0.999 | 0.999 |
| 0.3 | 0.750 | 0.251 | 0.007 |
| 1 | 0.029 | 0.000 | 0.000 |

## What it changes

- The paper says of its first row that "determinism does not make the future fixed
  from a standpoint". That holds for the class used. For massive finite-energy fields
  on the same spacetime the future is fixed from every standpoint.
- On an eternal flat background, a past fails to fix the future only through what can
  arrive along null directions, or through solutions a finiteness condition would
  exclude. On a background with a beginning it also fails through what has not yet
  entered the cone, which is the closed dust result.
- Weinstein argues that prediction from a past light cone in electromagnetism needs
  the added assumption of no incoming radiation. For a massive field of finite energy
  that statement is a theorem, and a time-symmetric one.

## Credits

- **Burnol**, arXiv:math/0509619v4, Theorem 1 (read with its proof): the decay lemma in
  one space dimension. He notes it fails at zero mass, follows from Hörmander's
  estimates, and is unlikely to be new.
- **Weinstein**, arXiv:1004.1346v2 (read): the massless case and its philosophical use.
- The quantum counterpart is attributed to Sadowski and Woronowicz (1971), not read.
- Three searches found no statement of the massive case in the prediction literature.

## Limits

- Minkowski spacetime and a free field only.
- The fixing uses the arbitrarily remote past. At m = 0.3 a quarter of the energy is
  still outside the cone 200 time units back.
- With a beginning or a cosmological horizon, massive matter stays outside past cones.
  In a universe like ours it can be news. See [horizons and news](../horizons-and-news/RESULT.md).
- The tempered class was not examined. The thin-tube version is supported by Holmgren
  uniqueness as stated by Strohmaier and Witten; see the
  [quantum companion](../cone-algebras/RESULT.md).
