# A state-defined thick present: what vacuum-correlation decay would and would not buy

10 November 2026. GLM longshot lane `longshot-entanglement-present`, submission for independent
review. No temporal ontology is selected and no priority is claimed. Sources: [sources.jsonl](sources.jsonl),
read depths labelled. Search capability check in [AGENT_REPORT.md](AGENT_REPORT.md).

**Idea under test** (from the brief): `research/stein-gr/local-clock/RESULT.md` proves that no locally
covariant rule defined from the metric can discriminate among spacelike-separated events. A quantum
state can: vacuum correlations of a massive field decay over the Compton wavelength. A present defined
as the region a point's neighbourhood is appreciably correlated or entangled with would then be thick
in space and would evade the theorem by using structure physics already has.

## 1. Exact question and proposed statement

**Question.** Is there a covariantly well-defined relation `P` on causally disjoint regions, defined
from a state `ω` by an entanglement or correlation threshold, such that (i) `P` is selective in space
(defeating the all-or-nothing verdict of the no-spacelike-scale theorem), (ii) its thickness has a
computable scale from known decay results, and (iii) some physically relevant state gives a nontrivial
thickness?

**Known here.** For the free massive scalar in 4d Minkowski vacuum the two-point function at proper
spacelike separation `s` is `W(s) = m K₁(ms)/(4π²s) ~ c·e^{−ms} s^{−3/2}`: exponential decay over the
Compton wavelength, `m⁻¹`. We reproduced the shape numerically (script:
[check_twopoint_decay.py](check_twopoint_decay.py); `W(s)e^{s}s^{3/2} → 0.0314` at `s = 12 m⁻¹`
against the asymptotic `√(π/2)/(4π²) = 0.0317`; `read_depth: reproduced` for this claim only).
Asymptotic clustering in massive Wightman theories is classical (Ruelle 1962, abstract read).
Entanglement between causally disjoint algebras is generic in QFT vacua: the vacuum maximally violates
Bell inequalities for suitable spacelike-separated region pairs (Summers–Werner 1987, abstract).
Mutual information between disjoint regions is finite in the continuum limit (Swingle 2010, abstract)
and, in CFT/massless cases, decays as a power law `Iⁿ ~ C_AⁿC_Bⁿ(R_A R_B/r²)^α` with `α` fixed by the
vacuum-channel operator product expansion; for the free massless scalar `α = (d−1)/2` (Cardy 2013,
abstract; Agón–Cohen-Abbo–Schnitzer 2016, next-to-leading order in 2+1d, abstract).

**Proposed (conjecture).** Define the *ε-present* of a region `O` relative to `ω` as the set of
regions causally disjoint from `O` whose mutual information or relative-entanglement-entropy-type
measure (Hollands–Sanders 2018, abstract: safety corridor, mixed-state measures, relative entanglement
entropy) exceeds `ε` times a reference scale. Claims: (a) `P` is **not** a local relation in the
Stein-gr/Fewster–Verch sense, because `ω` is extra structure: the theorem is evaded, not contradicted;
(b) its thickness is `Θ(m⁻¹·log(1/ε))` for massive vacua — measured against `W(1)`: `3.7 m⁻¹` at
`ε = 10⁻²`, `5.4 m⁻¹` at `10⁻³`, `11.3 m⁻¹` at `10⁻⁶` (reproduced); a few reduced Compton wavelengths,
e.g. `≈ 3.9×10⁻¹³ m` for the electron; power-law and effectively unbounded for massless vacua;
correlation-length `~ min(m⁻¹, β)` for thermal (KMS) states (our elementary Matsubara estimate); long,
state-dependent ranges for light fields in de Sitter (Marolf–Morrison–Srednicki 2013, abstract:
"decay only very slowly"); (c) `P` is objective only relative to `(M, ω)`, and no locally covariant
choice of preferred state exists (Fewster–Verch 2012, abstract: "model independent proof of the
impossibility of making a covariant choice of preferred state in all spacetimes").

## 2. Three nearest predecessors, assumption and result level

1. **Stein-gr note + Fewster–Verch.** Assumption: the relation must be *local* — preserved and
   reflected by every isometric embedding with causally convex image. Result: any such relation is
   empty or universal on spacelike pairs of Minkowski; no nontrivial local clock; no covariant state.
   Ours: drops locality, keeps fixed-`(M, ω)` covariance. Result: selective, state-relative thickness.
2. **State-defined temporal structure: thermal time (Connes–Rovelli lineage) and relational clocks
   (Page–Wootters lineage; Marletto–Vedral 2017).** Assumption: a global state; temporal structure
   (flow, conditioned evolution) read off state-level data. Result: time from the state, no passage
   added. Ours: the same move applied *spatially* — region-to-region correlation decay defines a
   coexistence region, not a flow or clock. No member of this lineage, as far as our searches reached,
   defines a spatial thickness from correlation decay.
3. **Entanglement-between-regions results (Summers–Werner; Cardy; Agón et al.; Hollands–Sanders).**
   Assumptions: AQFT locality, ground or Hadamard states, algebras of causally disjoint regions.
   Results: Bell violation across spacelike separation; power-law MI falloff in scale-invariant
   theories; measure-theoretic constraints (no region density matrices, area-law divergences near
   contact). Ours: repurposes the decay rate as a physical thickness scale of a proposed present —
   an interpretive step absent from this literature.

## 3. What changes and why it matters

The no-spacelike-scale theorem says the metric alone cannot make a present selective in space. The
proposal says the state already carries exactly the missing scale (Compton, thermal, or horizon
length), with no preferred foliation: the relation is between causally disjoint region algebras, not
between simultaneity surfaces. That converts "no local present is definable" into "state-presents of
computable thickness exist; which one is actual depends on which state the universe is in". It also
makes the defect explicit: a present definable only relative to a state that cannot itself be chosen
covariantly is world-relative — argued below to be the point, and simultaneously the price.

## 4. Smallest reproducible example and independent check

`check_twopoint_decay.py` (stdlib only, ~30 lines): trapezoid evaluation of
`K₁(z) = ∫₀^∞ e^{−z cosh t} dt` for the free massive scalar's `W(s) = m K₁(ms)/(4π²s)`; verifies the
`e^{−ms} s^{−3/2}` shape against `√(π/2)/(4π²)` and finds threshold thicknesses by bisection.
Independent checks: (i) Bessel asymptotics (standard reference tables) for the two-point shape;
(ii) the entanglement-measure claim — mutual information between disjoint massive-field regions
decaying exponentially in the separation — is **not** verified in this pass; check against
Casini–Huerta lecture notes (arXiv:2201.13310, lead) and Klich 2012 (dispersive media, lead);
(iii) Hollands–Sanders bounds for a covariantly defined measure.

## 5. What would show it wrong, trivial, already known, or irrelevant

- **Already known.** Any published definition of a present/now/coexistence region from entanglement
  or correlation decay. Defeating searches run: "thick present" + quantum; present from entanglement;
  Ismael/Myrvold/relational-becoming lineages; forward work citing Summers–Werner. Nearest hit found:
  Capurso 2023 (OSF preprint, unrefereed, discovery depth) asserts presentism with a "fundamental
  thick present" and information sampling "through entanglement", with no QFT decay results — a
  fringe neighbour, not occupancy. **Novelty survives these searches only as of 2026-11-10.**
- **Wrong.** If MI between causally disjoint massive-field regions does not decay exponentially
  (massless IR subtleties, or area-law boundary divergences dominating any separation-dependent
  comparison), the thickness formula fails.
- **Trivial.** "Present = correlation length" restates that fields have correlation lengths unless a
  consequence is derived. Worse: `ε` is free, so any thickness is available by choice of threshold or
  reference scale — the proposal has no empirical bite unless the threshold or measure is fixed by
  something independent.
- **Physically irrelevant.** Massive thickness is microscopic (`~10⁻¹³ m` for electrons, less for
  nuclei); massless thickness is unbounded; thermal thickness tracks `β`; de Sitter thickness is
  horizon-scale but vacuum-dependent. If no state of interest yields a mesoscopic or macroscopic
  *selective* thickness, the structure does no physical work.
- **Strongest single failure reason.** At the algebraic level there are no region density matrices
  (type III; Hollands–Sanders: corridors, mixed-state measures, divergences near contact), so
  "appreciably entangled" is not a covariantly well-defined predicate on events — only on algebra
  pairs with a chosen measure and reference scale — and the state itself admits no locally covariant
  choice (Fewster–Verch). The state-present therefore inherits exactly the nonlocality the Stein-gr
  theorem forbids, without a canonical normalization. That may be the point (the state supplies the
  scale the metric lacks), but it means the construction cannot deliver the objective, state-independent
  coexistence relation that presentism wanted; it can only decorate one worldview per `(M, ω)` pair.

## 6. Kinds of novelty, kept apart

- **Mathematical:** none claimed. Decay laws and no-go theorems are the literature's; our only
  computation is the reproduced two-point shape and threshold table.
- **Physical:** candidate novelty is the proposal that correlation-decay scales are the physical
  thickness of a non-metric present, plus the identification of the missing ingredient (an
  exponentially decaying, covariantly defined entanglement measure between disjoint regions).
  Unverified beyond the searches recorded here.
- **Formalization:** none attempted.
- **Philosophical:** the bridge premise "coexistence = appreciable state correlation" is stated with
  its costs (state-relativity via Fewster–Verch, threshold dependence, region-vs-event mismatch).
  It does not select presentism, eternalism, or any other ontology.

**Verdict.** Not found in the literature searched (fringe nearest neighbour noted). The idea survives
screening as a narrow conjecture; as a claim to an *objective* thick present it already fails —
the state-dependence is constitutive, not removable.
