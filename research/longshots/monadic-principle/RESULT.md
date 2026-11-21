# The monadic principle: does every event's past fix the universe?

10 November 2026. GLM longshot lane, task `longshot-monadic-principle`. A submission for
independent review, not a final truth claim. Read depths are in
[sources.jsonl](sources.jsonl); the verification script is
[compute_conformal.py](compute_conformal.py) (pure stdlib, runs in seconds).

## 1. Exact question and proposed statement

**Question.** Is "the causal past of every event fixes the whole history" already named
and studied, and can it hold as a law of nature in FLRW cosmology?

Two readings, in the notation of `research/what-the-past-can-fix/main.tex` (Theorem
`thm:char`, Corollary `cor:cauchy`):

- **Geometric (G):** for every event b, $I(b)$ contains a Cauchy surface, equivalently
  $\mathrm{Det}(b)=M$ (`cor:cauchy`).
- **Law (L):** for every event b and the standard field classes,
  $F_\mathcal L(I(b))=M$.

**Verdict.** (G) is already in the literature in pieces under other names, with a strong
generic *negative*: observationally indistinguishability results show the observable past
never fixes the global spacetime generically (Malament 1977; Manchak 2009 settles
Malament's conjecture; Norton 2009: "a specification of the observable past always fails
to fix the remainder of a spacetime"). Geroch's domain of prediction is nonempty only in
compact-slice universes (Geroch 1977, Einstein static, Fig. 5; Manchak 2008 theorem:
predicting one's own future requires a compact slice). No source stating the exact
condition "every event's past contains a Cauchy surface" as a named principle was found;
the nearest named relative is Malament's "causally bizarre" class ($I^-(p)=M$ for some
p, which forces closed timelike curves — a stronger and physically excluded version).
(L) in FLRW is **refuted for hot-big-bang-onward histories at every observationally
allowed $\Omega_k$** (section 4); only an emergent (Einstein-static) or cyclic conformal
pre-history rescues it, and inflation does not.

**Surviving residue worth stating.** The monadic principle as a law is equivalent, in
closed FLRW, to: *total conformal past of every event ≥ π in curvature-radius units,
plus no incoming radiation for every event*. The first half is a sharp, testable
cosmological bound; the second half is Weinstein's "lawlike time-asymmetry"
(arXiv:1004.1346), universalized over all events, and for massive finite-energy fields it
is a theorem, not a posit (see `research/horizons/massive-minkowski/RESULT.md`).

## 2. Three nearest predecessors, assumption → result

| Predecessor | Assumptions | Result | Delta over it |
|---|---|---|---|
| Geroch 1977, "Prediction in general relativity" | classical GR, causal-curve notion of prediction | domain of prediction $P(q)$; prediction possible in compact-slice spacetimes (Einstein static, his Fig. 5) | we add the FLRW timing threshold ($\eta>\pi$) and universalize over all events; the repo's `thm:char`/`cor:cauchy` give the slicing form |
| Malament 1977 "Observationally indistinguishable space-times"; Manchak 2009 | pointwise-isometric chronological pasts $I^-(p)$ | every non-causally-bizarre spacetime has a non-isometric observationally indistinguishable twin — the whole past fails to fix the global model generically | their notion is twin-spacetime and epistemic; the principle is ontic and within one history; as a law it would confine the universe to the exception class |
| Weinstein 2011, arXiv:1004.1346 | one observer, classical electromagnetism, past-light-cone access | Maxwell prediction needs no-incoming-radiation; hence "a lawlike time-asymmetry" | we universalize over all events and fields; the massive finite-energy case needs no posit; the condition becomes a quantitative cosmological constraint instead of an unexplained assumption |

Adjacent: Manchak 2008 (prediction ⇒ compact slice), Budic & Sachs 1976 (deterministic
spacetimes), Earman 1995 pp. 125–130 (the Cauchy-surface exception, with an
Ellis–Sciama constraint example), Smeenk & Wüthrich 2021 (global hyperbolicity and
determinism), Penrose 1979 (Weyl curvature hypothesis = no incoming gravitational
radiation at the past boundary), Wheeler & Feynman 1945 (absorber completion of
source-complete pasts, time-symmetrically).

## 3. What would change, and why it matters

If the principle held: space must be compact with a sufficiently long conformal past or
an eternal/emergent one; the horizon problem would dissolve by global geometry rather
than inflation; the Past-Hypothesis could be grounded in geometry instead of posit.
For the repository: `cor:cauchy`'s condition becomes a quantitative budget (conformal
time vs π in curvature-radius units) with a refutation analysis, and the massive-field
theorem ties Part III (`cor:epoch`) to the Sommerfeld / absorber / Weyl-curvature line.

## 4. Smallest reproducible example and independent check

Run `python3 compute_conformal.py`. It computes
$\eta_0=\sqrt{|\Omega_k|}\int_0^1 da/(a^2E(a))$, $E^2=\Omega_r a^{-4}+\Omega_m a^{-3}
+\Omega_k a^{-2}+\Omega_\Lambda$ (Planck 2018 background; closure relation), where η is
conformal time in curvature-radius units:

| Ω_k | η0 since hot BB | η0 + entire future | π needed |
|---|---|---|---|
| −0.001 | 0.101 rad | 0.137 rad | 3.14 |
| −0.010 | 0.319 rad | 0.432 rad | 3.14 |
| −0.044 | 0.674 rad | 0.908 rad | 3.14 |

The session estimate (0.10–0.67 rad for Ω_k between −0.001 and −0.044) **was correct**.
Independent checks: (i) analytic cross-check
$\eta_0[\mathrm{rad}] = 14.2\,\mathrm{Gpc}/R_c$ with $R_c=(c/H_0)/\sqrt{|\Omega_k|}$
gives 0.101 and 0.669 — agrees; (ii) closed dust has the exact threshold η = π at
maximum expansion (repo `prop:dust`; the horizon vanishing there is known:
Grøn & Johannesen 2011, Bolotin & Tanatarov 2013). Model checks: closed de Sitter has
conformal width exactly π, so its past cone never wraps — the principle fails for
*every* event there; closed dust wraps only after η = π, in the collapsing phase; a
hot-BB-only wrap would need $|\Omega_k|\approx 0.97$ (curvature radius ≈ Hubble radius),
far outside all constraints; an Einstein-static past (η unbounded below) satisfies the
principle for every event — which is the emergent-universe route
(Ellis & Maartens 2004); inflation adds only ~10⁻¹⁶ $H_0^{-1}$ of conformal time
($d\eta = N/(a_{\rm end}H_{\rm end})$ with $a_{\rm end}H_{\rm end}\sim 10^{17}H_0$) and
rescues nothing. Rescue budget: the pre-hot-big-bang history must supply ≥ 2.5–3.0 rad
= 52–428 Gpc ≈ 3.7–30× the entire observed conformal age (9.6–84× short even counting
the whole infinite future).

## 5. What would show it wrong, trivial, already known, or irrelevant

- **Already known:** (G) is occupied as above (Malament/Manchak/Geroch/Earman), and the
  FLRW horizon-vanishing at maximum expansion is known; the repo's own `prop:dust`
  already states the η = π threshold. What remains is the joint law formulation, the
  numbers for allowed Ω_k, and the refutation analysis.
- **Wrong (as a law about our universe):** any of — BAO+CMB flatness
  ($|\Omega_k|\lesssim 0.002$ at 95% vs ≈0.97 needed without pre-history; even the CMB-only
  closed central value −0.044 fails by a factor ≈4.7); null matched-circle searches
  (Cornish, Spergel, Starkman, Komatsu 2004, PRL 92, 201302); a confirmed slow-roll
  primordial tensor spectrum would undercut the Einstein-static rescue (emergent models
  predict negligible tensors — the authors' claim, not checked); Borde–Guth–Vilenkin
  2003 rules out past-complete *expanding* pre-histories, but not static ones.
- **Trivial:** if (L) reduces to "globally hyperbolic with a compact slice"
  (Manchak 2008), the geometric content is a corollary.
- **Physically irrelevant:** massive-field fixing uses the arbitrarily remote past (at
  m = 0.3, a quarter of the energy is still outside the cone 200 time units back), so no
  finite observer could use it.
- **Defeat searches run:** for the named condition (none found), for post-2008 prediction
  work (Lesourd 2019 thesis, Smeenk–Wüthrich 2021 — no statement of the principle found
  at abstract depth).

## 6. Kinds of novelty kept apart

- **Mathematical:** none claimed. The slicing characterization is the repo's `thm:char`;
  the wrap criterion is elementary and known; the budget is a numerical corollary.
- **Physical:** the conformal-time budget for observationally allowed Ω_k (deficit
  factors 4.7–31, or 3.5–23 counting the whole future) and the joint statement appear
  not to be stated together in the prediction literature, but each ingredient is standard.
- **Formalization:** none attempted.
- **Philosophical:** the law-promotion move is Weinstein's generalized; the geometric
  version is anticipated by Earman's Cauchy-surface exception and Manchak's theorem.
  Claimed here: at most a sharpened formulation plus the rescue taxonomy (emergent or
  cyclic vs inflation vs hot BB).

**Bottom line.** The idea is already in the literature in pieces, and as a law about our
universe it fails by roughly an order of magnitude unless the pre-hot-big-bang history is
emergent or cyclic. A clear mostly-negative result with a precise surviving residue: the
monadic principle = conformal-past lower bound (≥ π) + per-event no-incoming-radiation,
testable, currently refuted by the data on the standard pre-history assumption.
