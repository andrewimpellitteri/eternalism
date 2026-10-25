# Where the open future lives

Draft research note, 25 October 2026. Status labels on every claim:
**PROVED** (full argument given here), **SKETCH** (argument given, standard
analytic steps not written out or checked), **CONJECTURE**, **LEAD** (prior work
to check, not read). Nothing here has been independently verified yet.

## 0. The idea

The horizons paper separates what is *real* from b (its causal past) from what
is *fixed* from b (determined by that past under the laws). Its red team showed
that "fixed" depends on the law, not only on the geometry. This note asks the
next question: **where, for a given law, does the openness of b's future
live?**

Proposed answer: a law's free data live somewhere on the boundary of
spacetime, and b's future is open exactly as far as b has not yet received
that boundary. Massive fields keep their free data at past timelike infinity,
which every event has received, so they leave nothing open. Massless fields
keep theirs on past null infinity, which no single event has fully received,
so they leave everything beyond the causal past open. In a closed universe,
light refocuses, and a field that travels only on light rays needs only the
hollow surface of a light cone to be received, not the solid cone.

Three new definitions organize this, and they give several results that are
easy to state.

## 1. Definitions

M is globally hyperbolic, b an event, Is(b) its strict chronological past.

**D1. Guaranteed (solid-cone) determination.** Det(b): every
past-inextendible causal curve from x meets Is(b). From the horizons paper;
essentially Geroch's domain of prediction.

**D2. Light-ray (hollow-cone) determination. NEW.** N(b): every
past-inextendible *null geodesic* from x meets Is(b).

Basic facts (PROVED):
- Det(b) ⊆ N(b), since null geodesics are causal curves.
- N(b) is conformally invariant, since null geodesics are, as unparametrized
  curves.
- Once a past-directed causal curve enters Is(b), it stays in it (push-up).
  So x ∈ N(b) iff the past null geodesics from x are all eventually inside
  Is(b). On a Cauchy time function, by compactness of the sphere of
  directions, this holds iff some slice S_c meets the past null conoid of x
  only inside Is(b). (This assumes the past null geodesics run down to every
  slice, which holds in the models below. SKETCH in general.)

**D3. Law-relative determination.** F_L(b): any two solutions of L agreeing
on Is(b) agree at x. From the horizons paper. For a linear L, the **open
future** of b is the kernel

    K_L(b) = { solutions vanishing on Is(b) },

and M \ F_L(b) is the union of the supports of its elements. Along a
worldline γ, K_L(γ(τ)) decreases as τ increases: **becoming is the shrinking
of K_L.** The **residual openness** of γ is K_L(γ) = ∩_τ K_L(γ(τ)).

The grades: Det(b) is what every local law fixes; N(b) is what fields that
propagate only on light rays fix (strict Huygens principle); F_L(b) is what a
given law fixes.

## 2. Results

### T1. Mass closes the future (Minkowski). SKETCH

*Claim.* For the free massive Klein–Gordon field (m > 0) on Minkowski
spacetime, in the finite-energy class, F_L(b) = M for every b. The open future
K_L(b) is zero.

*Argument.* A finite-energy solution has the standard dispersive asymptotics
as t → −∞:

    ψ(t, vt) ≈ |t|^{-3/2} Σ_± c_± e^{±i m|t|√(1−v²)} â_±(p(v)),
    p(v) = m v / √(1−v²),

uniformly for v in compact subsets of the open unit ball (in L² form,
asymptotic completeness). Every point (t, vt) with |v| < 1 lies in Is(b) once
|t| is large, since Is(b) contains {|x − b⃗| < b⁰ − t}. If ψ vanishes on
Is(b), both profiles â_± vanish on p(V) for every compact V, hence
everywhere, so ψ = 0.

*Reading.* Every massive excitation was, in the far past, inside every event's
past light cone, because massive things travel slower than light. The test-dust
observation (every inertial worldline enters Is(b)) is the particle version.
The free data of a massive field live at past timelike infinity i⁻, and every
event has received i⁻.

*Contrast.* For the massless field, F_L(b) = J⁻(b) (horizons paper,
Proposition "sharp", by plane waves). A tempered massive solution supported in
a null half-space must vanish, while a massless one need not: on a line
k + sℓ with ℓ null, the mass hyperboloid meets it at one point, while the
null cone contains the whole line through ℓ. This is the Fourier-side reason.
SKETCH.

### T2. Massless openness is unreceived radiation. SKETCH

*Claim.* For the massless field on Minkowski spacetime, the past light cone of
b meets past null infinity ℐ⁻ in a cut c_b (in Bondi-type coordinates
v = b⁰ − θ·b⃗ for each direction θ). The open future K_L(b) is isomorphic to
the radiation data on the part of ℐ⁻ at or above c_b: what has not yet arrived.

*Argument.* ψ vanishes on Is(b) iff its radiation field on ℐ⁻ vanishes below
c_b. "Only if" is by continuity. "If" holds because, after conformal
compactification into the Einstein static universe (ESU), Is(b) lies in the
domain of dependence of that part of ℐ⁻ together with i⁻. The isomorphism uses
the radiation-field representation of finite-energy solutions (LEAD:
Friedlander's radiation fields; not read).

*Consequences.*
- (PROVED, elementary) c_b ≤ c_b' for all θ iff b ≤ b'. The causal order is
  the order of received news.
- A worldline's residual openness K_L(γ) is the data on the part of ℐ⁻ that γ
  never receives. It is nonzero iff γ has a (future) event horizon: zero for
  inertial observers, nonzero for uniformly accelerated ones. **Event horizons
  are permanent openness.** SKETCH.
- LEAD: Kozameh and Newman reconstruct the conformal metric from light-cone
  cuts of null infinity. In this language, the traces of the fragments at
  infinity determine the spacetime.

### T3. The end is fixed before the middle (closed dust). PROVED

This answers the open question the horizons paper leaves about its echo
proposition: the echo set is not everything that is fixed.

*Setting.* The closed dust model, M = (0, 2π) × S³, conformal to a slab of the
ESU R × S³ (unit sphere). L is the conformally coupled scalar. ψ = aφ solves
ψ_ηη = Δψ − ψ, extends to all of the ESU, and satisfies ψ∘A = −ψ, where
A(η, X) = (η + π, −X); hence ψ∘A² = ψ. Take b = (η_b, Y) with 0 < η_b < π.
Let

    ◇_b   = { (η, X) : d(X, Y) + |η| < η_b }   (ESU double cone through b
             and its mirror image (−η_b, Y)),
    A◇_b  = { d(X, −Y) + |η − π| < η_b },
    A²◇_b = { d(X, Y) + |η − 2π| < η_b }.

**Theorem.** Up to boundary points, F_L(b) = N(b) = M ∩ (◇_b ∪ A◇_b ∪ A²◇_b).

*Sufficiency.* A point z of ◇_b with η < 0 has every future-inextendible
causal curve entering I⁻(b) at small positive η, so two solutions agreeing on
Is(b) agree on ◇_b (ESU domain of dependence, plus continuity). The identities
ψ∘A = −ψ and ψ∘A² = ψ carry the agreement to A◇_b and A²◇_b.

*Necessity.* Take x ∈ M outside the closure of the union. If η_x > π, replace
x by A⁻¹x and use ψ(x) = −ψ(A⁻¹x); so assume 0 < η_x < π. The past null conoid
of x meets η = 0 in the sphere Σ = S(X, η_x). Its complement in S³ consists of
the two open balls B(X, η_x) and B(−X, π − η_x). Let C = B̄(Y, η_b). Since
S³ \ C is a connected open ball, Σ ⊆ C iff one of the two closed balls bounded
by Σ lies in C, i.e. iff d(X, Y) + η_x ≤ η_b (x ∈ cl ◇_b) or
d(−X, Y) + π − η_x ≤ η_b (x ∈ cl A◇_b). Otherwise pick p ∈ Σ \ C.
- Take ESU data (ψ, ψ_η) = (0, g) at η = 0, with g ≥ 0 a bump near p,
  supported outside C, and g(p) > 0.
- The solution vanishes on Is(b). If z ∈ Is(b) lay in its support, then
  w ≤ z ≪ b for some w in the support at η = 0, giving d(w, Y) < η_b.
- ψ(x) > 0. Work in the Penrose patch {d(·, X) + |η| < π}, which contains x
  and the relevant part of the slice. This patch is conformal to Minkowski
  space, with η = 0 going to t = 0. The conformal factor is even in t, so data
  (0, g) map to (0, positive × g). Kirchhoff's formula then gives ψ(x) as a
  positive multiple of the average of the transformed g over the sphere Σ,
  which is positive.

So x ∉ F_L(b). Finally, N(b) equals the same union: by the compactness remark
in D2, x ∈ N(b) iff Σ ⊆ B(Y, η_b), and the same case analysis applies.

*Consequences (PROVED from the theorem).*
1. **Light fixes part of b's timelike future before maximum expansion.** The
   crunch diamond A²◇_b ∩ M = { d(X, Y) < η_b + η_x − 2π } lies in I⁺(b),
   because η_b + η_x − 2π < η_x − η_b when η_b < π. These are the events
   just before the big crunch near b's location.
2. **On b's own worldline, the end is fixed before the middle.** The events
   (η, Y) are fixed for η ∈ (0, η_b] and η ∈ (2π − η_b, 2π), and open for
   η ∈ (η_b, 2π − η_b).
3. The echo set of the horizons paper, A(J⁻(b)) ∩ M, is the upper half of
   A◇_b. The lower half, events at the antipode *before* maximum expansion
   (η ∈ (π − η_b, π)), is also fixed.
4. The guarantee Det(b) is only Is(b) here. So the gap N(b) \ Det(b), the
   Huygens bonus, is three-quarters of the picture, and it comes entirely from
   the refocusing of light on the closed sphere.

*Why it works.* The past light cone of a near-crunch event at b's location
wraps once around the universe and refocuses near b's location at the big
bang, inside b's received ball. A field that travels only on light rays needs
only that hollow trace to be received.

### T4. Light fixes what lies beyond your horizon (global de Sitter). PROVED modulo the same necessity argument

Global de Sitter is conformal to the ESU slab η ∈ (−π/2, π/2). Take
b = (η_b, Y). The analogous diamond ◇_b is centered at (−π/2, Y) with
half-height η_b + π/2, and A◇_b is centered at (π/2, −Y). So

    F_L(b) ⊇ Is(b) ∪ { (η, X) : d(X, −Y) < η + η_b },

with equality up to boundary by the T3 argument. The worldline of the
antipodal observer, X = −Y, is fixed from b for all η > −η_b. Those events
lie beyond b's cosmological event horizon: b's worldline never receives a
signal from them. Yet light already fixes them from b's past. Here
Det(b) = Is(b), so this, too, is pure Huygens bonus.

The closed radiation universe (η ∈ (0, π)) gives
F_L(b) = Is(b) ∪ (A◇_b ∩ M) = Is(b) ∪ { d(X, Y) + η > 2π − η_b }: spacelike
events near b's antipode at late times. No timelike-future events are fixed,
because A²◇_b lies outside the slab.

### T5. Grades of openness and Hadamard's problem. CONJECTURE / programme

- If L obeys the strict Huygens principle (its propagator is supported on the
  null conoid), then N(b) ⊆ F_L(b) (SKETCH, via D2's slice
  characterization). In four dimensions, the conformal scalar and Maxwell
  fields obey it on conformally flat spacetimes, which include every FLRW
  model (LEAD: verify the exact statement and its source).
- Fields with tails (massive fields, curvature scattering) lose the Huygens
  bonus but may gain the massive closure of T1.
- So the question "how open is the future from here?" splits by field type.
  Which spacetimes admit Huygens fields is Hadamard's problem, which is open
  in general (LEAD: McLenaghan; Günther). **A classical open problem in PDE
  becomes a question about the openness of the future.**

## 3. What this would mean, philosophically

1. **The open future of a relativistic standpoint is carried by massless
   radiation.** Free massive matter in Minkowski spacetime leaves nothing
   open (T1). What remains open from b is the radiation that has not yet
   arrived from past null infinity (T2). That is a physical answer to "what
   is the open future made of?"
2. **Openness is not a cone.** In closed universes, the fixed region from b
   is a union of diamonds that includes part of b's own far future while
   leaving its near future open (T3). The order "fixed now, open later" is
   not the temporal order. This undermines any picture on which the future is
   open in proportion to how far ahead it lies.
3. **Horizons are where openness becomes permanent** (T2), and in de Sitter,
   light fixes events beyond the horizon (T4). What you can never see, and
   what is fixed for you, come apart in both directions.
4. **For local fragmentalism.** The fragment of b is real; the open future is
   K_L(b); becoming is the shrinking of K_L. So the view acquires a
   law-relative, quantitative account of what becoming *does*: it resolves
   free data at the boundary.

## 4. Priority risks (must be checked before any claim of novelty)

- **Ellis and Sciama 1972, pp. 41–42, and Earman 1995, pp. 125–130**, which
  Manchak 2008 (n. 15) cites for the view that Maxwell's equations allow
  prediction in some spacetimes. This may anticipate T3/T4 in some form. NOT
  READ.
- **Light-cone algebras in algebraic QFT.** Results on whether the algebra of
  a past light cone generates everything, for massive versus massless free
  fields, would anticipate T1/T2 in quantum form (LEAD: Buchholz on massless
  collision theory and Huygens' principle; Hislop–Longo; the timelike-tube
  theorem of Borchers, and Strohmaier–Witten 2023). NOT READ.
- Klein–Gordon unique continuation from a cone, and Paley–Wiener supports on
  the mass shell: T1 may be a known PDE fact. NOT SEARCHED.
- Friedlander's radiation fields; Kozameh–Newman light-cone cuts. NOT READ.

## 5. Next steps

1. Independent check of T3/T4 (rigorous) and T1 (sketch).
2. Priority search on the four risks above.
3. If T3 survives, it replaces the horizons paper's open question with a
   theorem; consequence 1 (light fixes part of b's timelike future before
   maximum expansion) strengthens the paper's thesis.
4. If T1 survives and is not known in this form, it is a paper on its own:
   "Mass closes the future".
