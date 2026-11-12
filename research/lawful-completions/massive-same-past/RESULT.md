# Same past, different futures: what the freedom is, and whether a mass removes it

10 November 2026. Claude Code (Fable 5.2), at the user's request. Checked only by the
session that wrote it. No temporal ontology is selected and no priority is claimed.
Sources: [sources.jsonl](sources.jsonl). Illustration:
[spherical_check.py](spherical_check.py).

The paper's Part III holds the whole causal past of an event and the total incoming
mass fixed and finds an open ball of future readings, for a massless scalar with
gravity in spherical symmetry. This note asks what that freedom is made of.

## Results

| Held fixed | Scalar | Future | Status |
|---|---|---|---|
| Causal past, total incoming mass | Massless | Open ball | The paper's theorem |
| Causal past, entire incoming mass function | Massless | At most a sign pattern | Proved here from the paper's inputs |
| A flat causal past, no incoming mass flux | Any | Flat | Proved here |
| A causal past empty of the scalar | Massive | Scalar absent everywhere | Follows from a 2026 preprint, in its class |
| An arbitrary causal past | Massive | Fixed? | Open |

## 1. The freedom is the incoming mass profile

Spherical symmetry, metric −Ω² du dv + r² dσ², Hawking mass m_H, scalar of mass m ≥ 0.
The double-null equations give

    ∂_v m_H = 8π r² Ω⁻² (T_uv r_v − T_vv r_u),   ∂_u m_H = 8π r² Ω⁻² (T_uv r_u − T_uu r_v),

with T_uu = φ_u², T_vv = φ_v², T_uv = (Ω²/4) m² φ². I derived these from the field
equations as I recalled them. They were not checked against a printed source.

**Proposition 1.** Assume a regular centre and no trapped or anti-trapped surfaces. Let
the past of a central event be flat with φ = 0, and let the mass at past null infinity,
M⁻(v) = lim_{u→−∞} m_H(u, v), be independent of v. Then the spacetime is Minkowski.

*Proof.* m_H is non-decreasing in v and non-increasing in u. It vanishes at the centre,
so it is non-negative, and it is at most M⁻(v), which is zero on the flat past and so
everywhere. Then both derivatives vanish and φ is constant, hence zero. ∎

So with a flat past, every different future is paid for by mass arriving through past
null infinity. That is how the paper's theorem proceeds: it fixes the total and leaves
the profile free.

**Corollary 2.** In the paper's massless class the project's
[incoming-mass formula](../coordinator/INCOMING_MASS.md) is
M⁻(V) = ¼ ∫ Φ² up to V, where Φ is the incoming profile. So fixing M⁻ for every V
fixes Φ². A smooth Φ can change sign only across zeros of infinite order. Given that
the profile determines the solution, which the paper already takes from its source,
the futures left are at most the sign patterns of Φ: one, up to φ ↦ −φ, for a profile
with zeros of finite order, and 2^N for the paper's family of N disjoint bumps.

The accepted finite-prefix corollary matches finitely many values of M⁻ and keeps an
open ball. Its scope note says the entire function "would need a new argument". This
is that argument, and it gives rigidity.

## 2. A massive scalar

**Linear evidence.** For a spherically symmetric massive field on Minkowski spacetime,
p = rφ solves the one-dimensional Klein–Gordon equation with odd data and the same
energy. By Burnol's theorem a finite-energy solution vanishing on the past of any event
is zero. So the central history is fixed by the past. For zero mass
p = f(t + r) − f(t − r), and the incoming f is free.

**No flux at null infinity.** Ionescu and Pausader prove, for small data, that their
Bondi energy never falls below the energy of the massive field. The massive field's
energy does not leave through null infinity. Time-reversed, none enters.

**Corollary 3 (conditional on a preprint).** Ma, Wu and Zhang consider small data that
are Schwarzschild outside a ball with the scalar supported inside. They prove that the
scalar has a profile along every timelike ray, that its limiting energy is an integral
of that profile, and that the initial energy is bounded by the limiting energy. Take
the time reverse of their class and suppose φ vanishes on the past of an event. Every
timelike ray ends up in that past, so every profile is zero, so the energy is zero and
φ vanishes identically. In spherical symmetry the spacetime is then Minkowski.

If the event lies after the data slice and its past covers the scalar's support, this
is just Cauchy uniqueness. It has content when the event is far in the past: the
scalar could otherwise live in the shell between two light cones.

**Open.** Whether two massive solutions with the same non-flat past must agree. That
needs uniqueness of nonlinear scattering from past timelike infinity. Small
non-decaying solutions, which Ionescu and Pausader mention, would have to be handled.

## What it does to Part III

- The freedom in the paper's theorem is the incoming mass profile and nothing else.
  The table "held fixed / future readings" gains a middle row: the entire incoming
  mass function leaves at most a sign pattern.
- The sentence that the moral "is already present for the linear wave equation" should
  say massless.
- The theorem depends on the field being massless. For small data in the preprint's
  class, a massive scalar absent from an event's past is absent everywhere.

## Illustration

Fraction of energy outside the past cone of a central event, spherical reduction:

| m | t = −50 | t = −200 | t = −700 |
|---|---|---|---|
| 0 | 1.000 | 1.000 | 1.000 |
| 0.3 | 0.979 | 0.644 | 0.017 |
| 1 | 0.092 | 0.000 | 0.000 |

## Credits

- **Burnol**, arXiv:math/0509619v4, Theorem 1 (read): the linear decay.
- **Ionescu and Pausader**, arXiv:1911.10652v2 (introduction and theorem statements
  read): global stability and the Bondi limit.
- **Ma, Wu and Zhang**, arXiv:2610.33928v1 (about half read, including the last
  proofs): the profile, energy and observability results. Dated 24 October 2026 and
  not refereed.

The mathematics of section 2 belongs to these authors. This note contributes
Proposition 1, Corollary 2 and the application to the paper.

## Limits

- Corollary 3 rests on an unrefereed preprint whose class is narrow: compactly
  supported scalar data and an exactly Schwarzschild exterior. No proof was re-derived.
- Proposition 1 is two monotonicity inequalities. Its value is the reading it gives.
- Corollary 2 inherits every limit of the paper's source theorem and of the
  incoming-mass note, and gives an upper bound only.
- I did not check that the metric's radiative profiles vanish in spherical symmetry in
  Ionescu and Pausader's decomposition, or that their Bondi energy equals the limit of
  the Hawking mass. They say the second is unclear.
- Everything is for small data on eternal, asymptotically flat spacetimes. With a
  beginning or a cosmological horizon, massive matter can be news.
- The fixing uses the remote past and has little practical content.
- An earlier draft said gravitational radiation can still arrive unannounced. That was
  not a statement about the preprint's class and is withdrawn.
