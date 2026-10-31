# Causal potential and the bow-tie domain under horizons

28 October 2026. Task `bowtie-horizon-rationale`, native Claude run.
Bounded analysis of one stated motivation for bow-tie relativistic GBT.
It does not choose an ontology and makes no empirical-discrimination claim.

## 1. The rationale, in the authors' words

**Authors' claims (full-text).** *Nothing to Come* ch. 9 §9.1 p.139 offers a
prerelativistic causal reading of GBT: "what now exists is exhausted by what
happens now and by whatever has the potential to conspire with what happens
now to make or let happen what has not yet occurred." The authors add that in
relativity this criterion "had admitted things located in causal chains not
including anything that happens now". They argue the discovery of an elsewhere
region does not mandate abandoning it (pp.138–139). They contrast this with the
chains-culminating-in-now reading, which would yield the causal past (p.138).

*Replies to Critics* §8 pp.488–489 states that this is "one motivation for the
bow-tie version of relativistic GBT": "what exists in spacetime is what has the
causal potential to shape the future (or else serves as a spatiotemporal
location for things that do)". The authors use it to motivate rejecting
transitivity (TR) of existence-at. They do not discuss horizons, curved
spacetimes or (P1R) there. Ch. 9 p.155 does say a related logical principle
holds in Minkowski spacetime "and presumably in many 'well-behaved' spacetimes
conforming to GR". So they flag GR dependence elsewhere, but not for this
rationale.

Dorato–Hoefer (full text) object to bow-tie RGBT on persistence and
transitivity grounds only; they do not discuss this rationale under horizons.

## 2. Formalization (our reconstruction)

Conventions follow C&R: `prec` is strict causal precedence, so null-related
points lie in the causal past or future, and the elsewhere region is
E(s) = M \ (J⁺(s) ∪ J⁻(s)). Spacetimes are time-oriented and causal.

**Point-level reading.**

    D_pot(s) = {s} ∪ {x : ¬(s prec x) and ∃z (s prec z and x prec z)}.

So x exists at s iff x is not in s's future and x can causally affect something
that, at s, has not yet happened. Every x in J⁻(s)\{s} qualifies, because
I⁺(s) is nonempty. An elsewhere point qualifies iff J⁺(x) ∩ J⁺(s) ≠ ∅.

**Bow-tie domain.** D_BT(s) = M \ (J⁺(s)\{s}), the reading of (P1R)+(P2R)+(BO).

**Location clause.** The parenthetical adds x when x is a location of some
thing that has causal potential. This is treated in §6; it changes the verdict.

## 3. When the rationale recovers the bow-tie domain

**Proposition 1 (exact, elementary).** D_pot(s) = D_BT(s) for every s iff every
two points of M have a common strict causal future (future directedness).
*Proof.* For x in J⁻(s) ∪ {s}, both sides agree. For x in E(s), membership in
D_pot(s) is exactly the existence of z with s prec z and x prec z. ∎

Minkowski spacetime is future-directed, so the rationale recovers bow-tie
there, and D_BT is monotone: s prec s′ ⇒ J⁺(s′) ⊂ J⁺(s) ⇒ D_BT(s) ⊂ D_BT(s′).
Directedness is Goldblatt's .2 condition in the future frame; its failure in
some spacetimes is noted by van der Schaaf (project-recorded). Proposition 1
is a restatement, not a new result.

## 4. Flat FLRW with a finite conformal future, including ΛCDM

Let a flat FLRW spacetime have conformal time η < η_∞ < ∞ (de Sitter flat
slicing, flat ΛCDM, any accelerating end state). It is conformal to the
Minkowski slab η < η_∞, so causal relations are Minkowskian there.

**Lemma 2.** Points x, s at comoving separation d have a common future iff
d < (η_∞ − η_x) + (η_∞ − η_s). *Proof.* The earliest point in both future
cones is the apex at η = (η_x + η_s + d)/2 for spacelike pairs; it must have
η < η_∞. ∎

**Proposition 3 (growth fails for D_pot).** In de Sitter spacetime (H = 1,
η_∞ = 0) take s = (−2, 0), s′ = (−1, 0), x = (−1, 2.5). Then s prec s′,
x ∈ E(s) ∩ E(s′), x ∈ D_pot(s) and x ∉ D_pot(s′). Hence the point-level
domain violates (P1R) E!x → ▾E!x: x exists at s but not at a point in s's
causal future. (Checked analytically and by brute force in `check.py`.)

**Numbers for flat ΛCDM** (H0 = 67.4 km/s/Mpc, Ωm = 0.315 from the Planck
2018 VI abstract; ΩΛ = 1 − Ωm; radiation neglected; `check.py`):

- Age 13.80 Gyr; comoving event horizon η_∞ − η₀ = 16.68 Gly.
- Points on our present cosmic-time slice lack a common future with
  here-now iff comoving d ≥ 33.36 Gly. They are in our elsewhere and in
  D_BT, but not in D_pot.
- After 1 Gyr along our comoving worldline, present-slice points with
  32.39 ≤ d < 33.36 Gly drop out of D_pot; after 5 Gyr, 29.10 ≤ d < 33.36.
  These remain in our later elsewhere, so this is a (P1R) failure, not a
  transition into our past.
- The particle-horizon value printed (51.08 Gly) neglects radiation and is
  only a cross-check; the standard figure with radiation is smaller (~46 Gly).
  No claim here depends on it.

That accelerating cosmologies have event horizons is standard (Rindler 1956,
recorded in the project's prior-work check). The new step is the consequence for
this specific rationale: it does not merely shrink the domain; it makes the
point-level domain non-monotone, contrary to the growth axiom it was meant to
motivate.

## 5. Same past, different verdict: Vaidya collapse

This connects the side test to `research/lawful-completions/`. It uses the
same exact past-preservation as the coordinator's Vaidya baseline, which that
lane owns; nothing here claims the baseline.

Ingoing Vaidya: ds² = −(1 − 2m(v)/r)dv² + 2dv dr + r²dΩ². Since ∇v = ∂_r
is past-directed null, v is nondecreasing along every future causal curve
for any m(v). Outgoing radial null rays obey dr/dv = (1 − 2m/r)/2, and any
future causal curve with dv > 0 satisfies dr/dv ≤ (1 − 2m/r)/2 (radial and
angular terms are nonnegative). A causal segment with dv = 0 is ingoing null,
with r nonincreasing.

Completion I: m ≡ 0 (Minkowski). Completion II: thin shell, m = 0 for
v < v₁ and m = M for v ≥ v₁. Let b be on the regular centre with
v₁ − 4M < v_b < v₁. Both completions agree exactly on {v < v₁} ⊃ J⁻(b),
including the null boundary of the past and all matter (none).

**Lemma 4.** In completion II, every future causal curve from b satisfies
r(v) ≤ r_out(v), the outgoing radial ray from b. That ray enters the
Schwarzschild region at r₀ = (v₁ − v_b)/2 < 2M and reaches r = 0 at

    V_b = v₁ − 2r₀ + 4M ln(2M/(2M − r₀)) < ∞,

so J⁺(b) ⊂ {v < V_b}. (Comparison argument above; closed form agrees with
numerical integration to 10⁻⁵ in `check.py`.)

**Proposition 5.** In completion II every point x with v_x ≥ V_b lies in E(b)
and has no common future with b. This includes exterior points at arbitrarily
large r: distant bodies that will later see the collapse. In completion I,
D_pot(b) = D_BT(b). *Proof.* v_x > v_b excludes x ∈ J⁻(b), and
J⁺(b) ⊂ {v < V_b} excludes x ∈ J⁺(b). Moreover J⁺(x) ⊂ {v ≥ v_x}. ∎

So whether the causal-potential rationale recovers the bow-tie domain at b
is **not fixed by b's entire causal past**. It depends on what happens to b's
future, the region the view itself says does not exist at b.

**Proposition 6 (growth failure from collapse).** In completion II, take
s on the axis with v₁ − 4M < v_s < v₁, and s′ on the axis in J⁺(s) with
V_{s′} < V_s (V_{s′} → v₁ as v_{s′} → v₁; `check.py`: v_s = −2, M = 1,
v₁ = 0 give V_s = 0.773, and v_{s′} = −0.01 gives V_{s′} = 1.3·10⁻⁵).
Choose v_x ∈ (V_{s′}, V_s) and x = (v_x, r_x) with r_x slightly greater than
r_out^s(v_x) > 0. Then x ∈ E(s) and its ingoing ray reaches J⁺(s), so
x ∈ D_pot(s); but x ∈ E(s′) and J⁺(x) ∩ J⁺(s′) = ∅. (P1R) fails for D_pot.

Caveats. Null dust is a weak matter model: no general well-posedness, and a
thin shell gives a C⁰ metric with distributional stress-energy. Smooth ramps
of m(v) can produce a locally naked central singularity in the slow-ramp
Vaidya case, which this construction excludes rather than handles. A
spherically symmetric Einstein–scalar collapse would be the natural
well-posed replacement; not read or done here. Maximal-development status
of completion II is assumed from its Oppenheimer–Snyder-like structure,
not proved.

## 6. The location clause: conditional branches

The quoted rationale also admits x if x "serves as a spatiotemporal location
for things that do" have causal potential. Whether this rescues bow-tie
depends on which things there are. Following the coordinator review
(`research/lawful-completions/coordinator/HORIZON_REVIEW.md`), these are
conditional branches, not an exhaustive dilemma.

- **Unrestricted fusions.** C&R allow mereological fusions (ch. 9 pp.151–152).
  *If* a fusion has causal potential whenever some part does, *and* the
  composition rule licenses fusing with x's occupant before that occupant's
  existence at s is settled, then D_BT is recovered for occupied points. Then
  the composition rule, not causal potential, does the work. An ambient
  mathematical label for the occupant is not enough, and empty points need a
  separate treatment.
- **Restricted things** (e.g., persisting material bodies). Existence of
  elsewhere points then depends on matter histories. In ΛCDM, a comoving body
  has causal potential at s if some stage y of it has a common future with s;
  its earliest stages make this hold iff d < η_total + (η_∞ − η_s), where
  η_total = η_∞ − η_bb is the total conformal time from the big bang to the
  infinite future (strict, since the initial singularity is not a stage).
  Bodies beyond the particle horizon are in our elsewhere at every one of
  their stages, so their drop-out is not entry into our past. As s advances,
  the threshold falls, so bodies near it still drop out: (P1R) fails at a
  larger distance, not never. In Vaidya, long-lived exterior bodies that
  passed through {v < V_b} are restored, but empty regions and late-forming
  bodies are not.

## 7. Monotonicity and its repair by historical potential

**Proposition 7 (coordinator review; independently checked in
`research/lawful-completions/relational/HORIZON_LEMMA_REVIEW.md`, re-traced
here).** In a connected, causally simple spacetime, D_pot is monotone along
every causal advance iff every two points have a common strict causal
future. The converse uses P_x = I⁻(I⁺(x)), a nonempty open past set; a
boundary point p ∉ P_x and a point r ≪ p near p outside the closed set J⁻(x)
give x ∈ D_pot(r) but x ∉ D_pot(p). This resolves the first open question of
the original submission. Credit: Codex coordinator.

So the point-level failures of §§4–5 are not special to the examples:
**every** connected, causally simple spacetime that is not future-directed
violates (P1R) for D_pot.

**Historical closure (coordinator review).** H(s) = ⋃_{r ≤ s} D_pot(r) is
the least monotone enlargement of D_pot, and H(s) ⊂ D_BT(s). It reads
"potential" as potential once possessed relative to some point of s's
causal past. The review left open when H = D_BT. Our answer:

**Proposition 8.** In a causally simple spacetime, let x ∈ E(s). If x and s
have a common future or a common past, then x ∈ H(s).
*Proof.* Common future: x ∈ D_pot(s). Common past: take w ∈ J⁻(x) ∩ J⁻(s) and
a past-directed causal curve γ from γ(0) = s to w. The set {t : γ(t) ∈ J⁻(x)}
is closed (causal simplicity) and nonempty; let t* be its minimum. Then
t* > 0 because s ∉ J⁻(x). Since J⁻(x) ⊂ P_x (push-up, nonempty I⁺(x)) and P_x
is open, γ(t) ∈ P_x \ J⁻(x) for t slightly below t*. Such r = γ(t) satisfies
r ≤ s, ¬(r ≺ x) and has a common future with x, so x ∈ D_pot(r) ⊂ H(s). ∎

**Proposition 9 (exact, flat FLRW).** Let a flat FLRW spacetime have
conformal time η ∈ (η_bb, η_∞), with R = η_∞ − η and P = η − η_bb (either
endpoint may be infinite). For x ∈ E(s) at comoving distance d,

    x ∈ H(s)  iff  d < R_x + R_s + 2P_s.

*Proof.* If x ∈ D_pot(r) with r ≤ s, put λ = η_s − η_r ∈ [0, P_s); then
|x_r − x_s| ≤ λ and Lemma 2 gives d(x,r) < R_x + R_s + λ, so the triangle
inequality yields the bound. Conversely, put r on s's past null cone towards
x at conformal depth λ. Common future and x ∉ J⁺(r) hold iff
(d − R_x − R_s)/2 < λ < (d + R_x − R_s)/2. This interval has width R_x > 0,
its upper end is positive since x ∈ E(s), and it meets [0, P_s) under the
stated bound. ∎ (Checked against brute force on 360 random slab
configurations in `check.py`.)

Consequences:

- **Minkowski:** H = D_pot = D_BT.
- **De Sitter:** in the flat-slicing patch (P = ∞) every elsewhere point is
  in H. In global de Sitter (conformal time interval of length π, spatial
  S³ of diameter π) the same construction gives threshold
  2π + T_s − T_x > π ≥ χ, so again H = D_BT. The historical repair fully
  recovers bow-tie despite the event horizon.
- **Vaidya collapse (§5):** {v < v₁} is a flat past set, and every point has
  a past point in it, so b and every x share a past. By Proposition 8,
  H(b) = D_BT(b) in both completions (modulo causal simplicity of the model,
  which needs the smooth fast-ramp version; the thin shell is C⁰).
- **Flat ΛCDM:** it fails. Points on our present slice with
  d ≥ 2(P₀ + R₀) = 2η_total are in D_BT but not in H. The radiation-neglected
  value is 135.5 Gly comoving, an overestimate. Such points exist because
  flat space is infinite. Failure needs both horizons and enough space.
  With an event horizon alone (de Sitter) or a particle horizon alone,
  Propositions 8–9 show that H still recovers bow-tie.

## 8. Verdict

**The instantaneous reading fails; the historical reading nearly works.**

- D_pot (potential now) recovers bow-tie only in future-directed spacetimes.
  In every other connected, causally simple spacetime it violates (P1R)
  (Proposition 7). Examples: de Sitter, ΛCDM, Vaidya collapse with an exactly
  flat past. Whether it recovers bow-tie at b is not fixed by b's entire
  causal past (Proposition 5). KILL for this reading as a motivation for
  bow-tie growth.
- H (potential once possessed) is monotone by construction. It recovers
  bow-tie wherever every elsewhere pair shares a past or a future, including
  de Sitter and the Vaidya pair. In flat ΛCDM it fails only beyond 2η_total
  on the present slice. CONDITIONAL: the repair is ours (with the
  coordinator's H), not C&R's. It also changes the criterion: existence at s
  then depends on common futures of points in s's past, which are still
  future facts.
- The location clause gives conditional branches (§6), not a refutation.

This does **not** refute the bow-tie view. D_BT itself is monotone in every
causal spacetime. What fails is the instantaneous version of this motivation.
A bow-tie theorist can adopt H, or keep (BO) as primitive.

**Novelty status.** Event horizons, particle horizons and failure of
directedness are standard. No source read connects them to C&R's rationale
or to (P1R); this is a negative result over a small, targeted search, not
evidence that nobody has made the point. If the result has value, it lies in
the gap between instantaneous and historical potential: exact thresholds
(Propositions 7–9) and the same-past dependence (Proposition 5).

**Falsifiers.** (i) A causally simple spacetime where x ∈ E(s) shares a past
with s but x ∉ H(s) would refute Proposition 8. (ii) A flat FLRW
configuration violating the Proposition 9 threshold. (iii) A reading of
"causal potential" that is instantaneous, avoids fusions, and still satisfies
(P1R) in de Sitter would defeat the KILL for the instantaneous reading.

## 9. Open questions

1. (Resolved by Proposition 7 for connected causally simple spacetimes.)
   Causally pathological frames remain open.
2. Necessary condition for H = D_BT beyond FLRW: is "every elsewhere pair is
   joined by a chain r ≤ s with a common future" checkable from conformal
   boundary structure?
3. Is H(b) fixed by b's entire causal past across lawful completions? The
   Vaidya pair agrees; no counterexample pair constructed.
4. Well-posed matter replacement for §5. Christodoulou 1991 (CPAM 44(3)
   339–373, DOI 10.1002/cpa.3160440305; citation verified by coordinator,
   unread) is the lead. Per the coordinator, trapped-surface formation alone
   does not give the late exterior event with no common future.
5. Whether C&R's persistence argument (ch. 9 pp.151–152) needs H rather than
   D_pot; ties to `research/future-domain-persistence/`.
