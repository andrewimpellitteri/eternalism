# Prior work audit: scalar sharpness and antipodal echo

Task: `horizons-scalar-priority`. Date: 2026-10-25. Worker: GLM headless
research agent in worktree `.worktrees/horizons-scalar-priority`.

## 1. Scope and inputs

Audited the prior-work status of the scalar propositions in the frozen draft
`research/horizons/coordinator-review/dispatch-2026-10-25/main.tex`
(SOURCE.md records SHA-256 `bbd5926…c84bbe`; re-verified during this task):

- **Prop sharp** (lines 227–247): on the flat FLRW slab
  `M=(η_-,η_+)×R³`, the conformally coupled scalar has
  `F_L(b) = J⁻(b)` for every `b`.
- **Prop echo** (lines 283–309): in the closed dust model
  `a = ½a_m(1−cos η)`, `η ∈ (0,2π)`, solutions satisfy
  `ψ(η+π,−X) = −ψ(η,X)`, hence
  `J⁻(b) ∪ (A(J⁻(b)) ∩ M) ⊆ F_L(b)`, with the echo region nonempty and
  disjoint from `Det(b)` when `η_b < π`.
- **Thm char** (lines 147–171): slicing characterization of `Det(b)` via
  Cauchy time functions.
- **Prop dust** (lines 250–276): the closed-model threshold at
  `η_b = η_- + π`; ESU case; and the manuscript's two appeals to
  Manchak (2008).

`REVIEW.md` and `DRAFT3_FOLLOWUP.md` were read as leads; every argument
below was reconstructed from primary or directly accessible texts, not from
those reviews.

Reading-depth labels follow `knowledge/README.md`: discovery, abstract,
full-text, reproduced, code-audited.

## 2. Claim-by-claim audit

### 2.1 Prop sharp — `F_L(b) = J⁻(b)` for the conformal scalar on a flat slab

**Draft's assumptions:** smooth solutions of `□_g φ − ⅙Rφ = 0` on a
spatially flat FLRW slab; determination = agreement of all solutions on
`I⁻_s(b)` implies agreement at the target.

**Nearest antecedents found:**

1. *Conformal invariance of the conformally coupled wave equation* (the
   step `φ` solution `iff ψ=aφ` solves the flat wave equation, cited in the
   draft to `[app. D, Wald 1984]`). **Wald 1984 was not accessible** to this
   worker (archive.org item `generalrelativit0000wald` is
   lending-restricted; search-inside returned "Item not available"). Two
   citing-source leads were found at discovery depth only: a citing
   bibliography note locating "Appendix D, p. 445 of R. M. Wald", and a
   hosted lecture-notes file stating "Wald (1984, Appendix D) contains some
   useful…". **The exact equation number and content of Wald's Appendix D
   are therefore UNVERIFIED here.** What *was* verified at full-text depth:
   Harte & Drivas (2012), PRD 85, 124039, arXiv:1202.0540v3, p. 28 (Sect.
   V.B "Examples"): for conformally flat spacetimes their Penrose-limit
   theory fixes the leading singular structure of retarded scalar Green
   functions universally, and they note explicit computations in "the
   Einstein static universe and Bertotti-Robinson spacetimes". The
   conformal reduction itself is textbook material (Birrell & Davies 1982;
   Parker & Toms 2009 were named by searches but **not accessed**).
2. *Domain of dependence / finite propagation speed for the wave equation*
   (the sufficiency direction). Verified full-text at
   Baskin & Mazzeo, "Some global aspects of linear wave equations",
   arXiv:1210.8053v1, §2.1 (pp. 4–5): the energy-integral proof, the
   backward domain of dependence `D⁻_{t1,x1}`, and support propagation
   within speed-1 neighborhoods. They credit the standard references
   (Friedlander 1975 *The Wave Equation on a Curved Space-Time*; Wunsch's
   CMI lecture notes); Friedlander was **not accessed** directly.
3. *Sharpness* (the traveling-wave construction `ψ = f(u)`,
   `u = η − η_b − k̂·(Z−Y)`, vanishing on the strict past). This is the
   standard PDE demonstration that the light cone is the optimal domain of
   dependence in 3+1 dimensions (Huygens regime). **No exact printed
   locator for this construction was verified in the bounded search**;
   textbook locators (e.g., F. John; Evans; Friedlander) were not
   accessible as full text here.

**Verdict: NEEDS NARROWING (not a candidate for mathematical novelty).**
The proposition is an immediate composition of (1) and (2)–(3): two lines
from standard, published results. Under `knowledge/NOVELTY.md`'s reject
gate ("already an immediate corollary of a known equivalence"), the
mathematical content should be treated as known. What is not established
either way in this audit is *expository packaging* (event-relative
determination sets `F_L(b)` in a cosmological setting); no printed source
stating exactly `F_L(b) = J⁻(b)` was found in the bounded search, but the
search surface was thin (see §4). Recommended manuscript posture: present
it as an application of standard results, citing a verified conformal
transformation reference once the Wald locator is pinned (§5, task 1).

### 2.2 Prop echo — antipodal refocusing of the conformal scalar in closed dust

**Draft's assumptions:** same solution class on the closed dust model;
`A(η,X) = (η+π,−X)`; conclusion is an inclusion
`J⁻(b) ∪ (A(J⁻(b)) ∩ M) ⊆ F_L(b)`, nonempty and `Det`-disjoint for
`η_b < π` (not exactness — the draft leaves that open).

**Nearest antecedents found:**

1. *Closed-model horizons and the π-geometry* (prior work, verified):
   Grøn & Johannesen, arXiv:1103.4753v1 (2011), §2.2, eqs. (11)–(15)
   (`a = α(1−cos η) + β sin η`; maximum expansion
   `η₂ = π − arctan(β/α)`); p. 4: "In a matter dominated universe the Big
   Crunch occurs at η = 2π. Then the whole universe can be seen at the
   moment of maximum extension. At this moment the particle horizon
   vanishes"; p. 6: "In a dust dominated universe the horizon exists
   during the expansion era, and vanishes as the universe reaches its
   maximum size." Corroborated full-text by Bolotin & Tanatarov,
   arXiv:1310.6329v3, §1.4 problem 40(b) (p. 23): the dust particle
   horizon "encloses the full Universe at the moment of maximal expansion
   η = π and for later times does not exist"; Fig. 1.10 (p. 22) draws the
   two light paths "that realize the first and second images of a galaxy
   … from opposite directions". The antipodal map appears in GJ §2.4 (p.
   10) explicitly, but only as a coordinate reflection ("This is an
   antipodal transformation, i.e. a reflection through the origin in S³"),
   with no wave content. **The geometric half of the echo proposition is
   standard prior work**, exactly as the draft says.
2. *Caustic sign flip for waves in conformally flat spacetimes* (published,
   full-text verified): Harte & Drivas 2012, pp. 2, 17, 22, 28: retarded
   Green functions in conformally flat spacetimes "have a 2-fold pattern"
   `δ(σ) → −δ(σ) → …` at each perfect (anastigmatic) caustic; "Such
   patterns have indeed been observed in scalar Green functions for both
   the Einstein static universe and the Bertotti-Robinson spacetime [9]"
   where their ref [9] is "M. Casals, **private communication (2012)**" —
   i.e., the ESU observation itself is not a published computation in that
   paper; it is predicted there by general theory and attributed to
   private communication. The multiplicity-2 conjugate structure of
   antipodal refocusing is the geometric input; their §III G example
   computes conjugate hyperplanes and the `(−1)ⁿ`-type sign structure in
   the plane-wave model.
3. *Mode parity and frequencies on the Einstein cylinder* (elementary,
   standard): spatial degree-n harmonics on unit S³ have Laplace
   eigenvalue `−n(n+2)`, antipodal parity `(−1)ⁿ`, so ESU modes have
   frequency `n+1` and every mode — hence every smooth solution of
   `∂²_η ψ = Δψ − ψ` — satisfies `ψ(η+π,−X) = −ψ(η,X)`. Verified
   computationally in this task on explicit harmonic polynomial modes for
   `n = 0…10` (see AGENT_REPORT.md verification commands). **No printed
   ESU-specific locator stating this parity/π-shift identity was found in
   the bounded search**; QFT-in-curved-space texts (Birrell & Davies;
   Parker & Toms) were named by searches but not accessed.
4. *Huygens failure / tails on ESU-type backgrounds*: Harte & Drivas 2012,
   p. 17: Huygens' principle holds for massless scalars in 4-d plane wave
   spacetimes; "In almost all other cases, retarded Green functions have
   support inside the light cone", citing Friedlander (1975) and **Günther,
   *Huygens' Principle and Hyperbolic Equations*, Academic Press, 1988**
   (both unread here; discovery level). This matters as context: influence
   spreads inside the cone on ESU/closed FLRW, while the echo is a
   value-determination statement at a re-focused region — the two are
   compatible but belong to different formulations (support of the
   fundamental solution vs solution-agreement classes).

**Verdict: NEEDS NARROWING / UNDETERMINED within bounded search.** The
inclusion follows in a few lines from standard spectral facts plus the
conformal reduction, and the *nearest published result* (caustic sign flip
in conformally flat spacetimes, incl. ESU) is one formulation away from it.
No verbatim printed statement of the determination claim was found; the
bounded search could not rule one out in the QFT-on-ESU/closed-FLRW
literature that was inaccessible. The manuscript's own caution (exactness
left open; echo pre-threshold is spacelike to `b`, per DRAFT3_FOLLOWUP) is
correct and should be preserved. Recommended: cite Harte & Drivas (2012)
as the nearest published neighbor and label the echo an observation-level
reformulation, not a new mechanism.

### 2.3 Thm char — slicing characterization of `Det(b)`

**Antecedents verified at full text:**

- Geroch, "Prediction in general relativity" (1977), Minnesota Studies viii,
  printed pp. 81–93; LSE scan read in full. Printed p. 91 (§3): `P(q)` is
  the set of x such that "every past-directed timelike curve from x,
  without past end point, enters I⁻(q), but such that I⁻(x) is not a
  subset of I⁻(q)"; and the equivalent form (same page): x ∈ P(q) iff
  `I⁻(x) ⊄ I⁻(q)` and there is a three-dimensional achronal surface
  `S ⊆ I⁻(q)` with `x ∈ D⁺(S)` (OCR of the second passage is partially
  garbled; wording reconstructed from context and consistent with
  Manchak's restatement). The draft's "Relation to Geroch" paragraph
  matches the printed definition, and its description of the equivalent
  achronal-surface form is accurate.
- Manchak 2008, p. 318 (Definition) restates a Geroch-type domain of
  prediction with an achronal, **closed, spacelike** surface `S ⊆ J⁻(q)`
  (his fn. 6: private communication; differs slightly from Geroch's
  printed definition).

**Bounded novelty search:** serpapi query for "domain of prediction" +
slicing/Cauchy-time-function characterization returned **zero relevant
results**; arXiv API queries likewise. Nothing found stating a
level-set/Cauchy-slice characterization of a prediction domain.

**Verdict: UNDETERMINED within bounded search; plausibly a new
formulation.** The theorem is a new *slicing form* inside Geroch's
framework; its content is an inverse-limit compactness argument using
standard globally hyperbolic slicing theory (the draft cites MS2008 for
those facts; **MS2008 itself was not accessed** here). No global priority
claim is made or certified by this audit. Note the caution from REVIEW.md
item 4: describe the slicing statement as the proposed contribution
subject to this bounded audit, not a certified new open-problem solution.

### 2.4 Prop dust, the Geroch attribution, and the closed-model threshold

Verified:

- The threshold computation is a standard conformal-diagram consequence;
  the draft itself only claims the consequence for determination
  (`Det(b) = M` after the threshold) via Cor. cauchy.
- "The Einstein static case is Geroch's [Fig. 5]" — verified. Geroch 1977
  printed p. 89: "Let the space-time M,g be the Einstein universe, so the
  spatial sections are three-spheres and time is the real line (Figure 5)
  … Thus all the experiences of the observer beyond q could have been
  predicted at q." Figure 5 (cylinder with `D⁺(S)`) is on printed p. 91.
- "The known moment at which the particle horizon disappears [max
  expansion]" — verified prior work (Grøn & Johannesen §2.2; Bolotin &
  Tanatarov §1.4, locators above).

The draft's Manchak sentence ("This is consistent with Manchak's result
that prediction of events to the future of an observer requires a compact
Cauchy surface") needs correction — see §2.5.

### 2.5 Manchak 2008 — exact hypotheses and safe replacement wording

Retrieved and read in full: the author's copy at
`https://sites.socsci.uci.edu/~jmanchak/ippigr.pdf` (HTTP 200 on
2026-10-25; the coordinator's earlier timeout was transient). It is the
**published version** (Found. Phys. 38: 317–321; DOI
10.1007/s10701-008-9204-6). A PhilSci-Archive preprint
(`philsci-archive.pitt.edu/archive/00003836/`, NoPredGR.pdf) was also
downloaded as a backup copy (not text-compared page-by-page).

Exact statements (printed page numbers 317–321):

- **Definition (p. 318).** `p ∈ P(q)` iff (i) `p ∉ J⁻(q)` and (ii) there
  is an **achronal, closed, spacelike** surface `S ⊆ J⁻(q)` with
  `p ∈ D(S)`. Fn. 6: private communication; "differs slightly from the
  one given in [4] [Geroch 1977]"; the spacelike requirement and closedness
  are Manchak's additions/conveniences.
- **Theorem 1 (p. 319).** Hypothesis: there exist `q, p` with
  `p ∈ P(q) ∩ I⁺(q)` — i.e., an event in one's own **timelike future**
  lying in the Geroch-style domain of prediction. Conclusion: "(M,g)
  **admits a compact, spacelike slice**." Fn. 9: a slice is "a closed,
  achronal set without edge". **The conclusion is not "compact Cauchy
  surface."**
- **Fn. 8 (p. 318).** Geroch's printed claim — "Given a space-time M,g,
  and a point q of M such that P(q) contains a point to the future of q,
  then M,g is a closed universe, in the sense that it admits a compact
  spacelike surface" (Geroch 1977, printed p. 92, attributed by Geroch
  there as "essentially a corollary of a theorem of Earman's") — "**was
  later shown to be false** [6, pp. 726–727]", where [6] is Hogarth,
  "Predicting the future in relativistic spacetimes", *Stud. Hist. Philos.
  Sci.* 24 (1993) 721–739. Hogarth 1993 was **not accessed** here.
- **Genuine prediction (p. 320) and Theorem 2 (p. 320–321).** Redefining
  prediction to require embeddability of `J⁻(q) ∪ J⁻(p)` into *every*
  inextendible spacetime containing an isometric copy of `J⁻(q)`,
  Manchak proves `P(q) ⊆ ∂J⁻(q)`: "the only possible predictions are
  those 'on the verge' of being retrodictions", robust under any local
  field conditions since the constructed competitor spacetime is locally
  isometric.

Assessment of the draft's two paraphrases:

1. "consistent with Manchak's result that prediction of events to the
   future of an observer requires a compact Cauchy surface" — **NEEDS
   NARROWING.** Two inaccuracies: the hypothesis is Manchak/Geroch-style
   `P(q)`-membership with an achronal closed spacelike surface in the
   causal past (not the draft's `Det(b)` criterion), and the conclusion is
   a compact spacelike slice, not a Cauchy surface. Safe replacement:
   "This is consistent with Manchak's theorem (2008, p. 319) that if some
   event in an observer's timelike future lies in the Geroch-style domain
   of prediction — data on an achronal, closed, spacelike surface in her
   causal past — then the spacetime admits a compact spacelike slice; the
   closed dust and Einstein static models satisfy the conclusion."
2. "Manchak shows that an observer who does not already know the
   spacetime cannot verify such predictions" — **SUPPORTED in substance**
   by Theorem 2 and the embedding argument (pp. 319–321), with the caveat
   that Manchak's notion is "genuine prediction" defined by embeddability
   into all inextendible completions. Safe replacement:
   "Manchak (2008, pp. 320–321) shows that 'genuine' prediction —
   verifiable from the observer's causal past regardless of which
   inextendible spacetime contains it — is confined to the boundary of the
   causal past; `Det(b)` and `F_L(b)` are nomological notions given `M`,
   not epistemic ones."

Also relevant and verified: Geroch §2 (printed pp. 84–85) is explicit that
the detailed determination statement "depends on the type of matter or
fields considered" (his example is Maxwell uniqueness in `D⁺(S)`), and §2
(pp. 86–87) introduces "hole-free" spacetimes — useful attribution anchors
for the REVIEW.md sufficient/necessary distinction that the frozen draft's
`F_L(b)` repair resolves.

## 3. Verdict summary

| Claim | Status | Basis |
|---|---|---|
| Prop sharp (flat slab, `F_L = J⁻`) | needs narrowing — immediate application of known results | conformal invariance (standard; Wald App. D locator unverified) + sharp domain of dependence (Baskin–Mazzeo §2.1 verified; sharpness folklore) |
| Prop echo (closed dust) | needs narrowing / undetermined within bounded search | geometric half = verified prior work (GJ §2.2; BT §1.4); nearest published wave result = Harte–Drivas caustic sign flip (full-text verified; ESU observation itself a private communication there); parity identity elementary, computationally confirmed |
| Thm char (slicing characterization) | undetermined within bounded search; plausibly new formulation | closest antecedent Geroch's equivalent achronal-surface form (printed p. 91, verified); no identical statement found; search surface thin |
| Prop dust threshold + ESU attribution | supported as prior work / attribution verified | GJ, BT verified; Geroch Fig. 5 + p. 89 verified |
| Draft's Manchak paraphrase (compact Cauchy surface) | needs narrowing | Manchak Thm 1 concludes compact spacelike slice; hypothesis is `P(q) ∩ I⁺(q) ≠ ∅` |
| Draft's Manchak paraphrase (verification impossibility) | supported with narrowing | Thm 2 `P(q) ⊆ ∂J⁻(q)`; embeddability definition |
| Geroch printed closed-universe claim (p. 92) | false as stated (per Manchak fn. 8) | do not lean on it; cite Manchak's corrected theorem |

## 4. Search and access limitations

- `web-search-prime` (Z.ai): quota exhausted ("Weekly/Monthly Limit
  Exhausted", resets 2026-11-17). No retry loops used. Fallbacks:
  serpapi_search and the built-in websearch both worked; all searches below
  used those plus direct public URLs.
- Not accessed (unread): Wald 1984 (lending-restricted; locator
  unverified); Friedlander 1975; Günther 1988; Hogarth 1993; Rindler 1956
  (ADS scan returned HTTP 504); Minguzzi–Sánchez 2008; Birrell & Davies;
  Parker & Toms; Manchak's "Global Spacetime Structure" survey
  (core.ac.uk PDF returned HTTP 403).
- Unproductive searches: "Gott closed universe lens antipode" (no
  verifiable hit; the remembered "closed universe as a lens" paper was not
  confirmed and is **not** cited in my outputs); ESU mode-function arXiv
  query (empty); "domain of prediction" + slicing (empty).
- Coverage is therefore bounded: strong on the prediction/prior-work line
  (Geroch, Manchak) and the closed-model horizon line (GJ, BT), moderate on
  the wave-propagation line (Harte–Drivas, Baskin–Mazzeo full text), thin
  on QFT-in-curved-space textbooks where an ESU mode-parity locator might
  exist.

## 5. Proposed next tasks

1. Pin the Wald Appendix D locator (exact equation numbers for the
   conformal transformation of `□φ − ⅙Rφ`) from a physical copy or an
   equation-precise citing source; or switch the manuscript's citation to a
   fully verified reference.
2. Retrieve Hogarth (1993) pp. 726–727 to characterize the counterexample
   to Geroch's printed p. 92 claim before the manuscript cites that page.
3. A library/publisher-access pass over QFT-in-curved-space texts
   (Birrell & Davies; Parker & Toms) and the Casals–Dolan–Ottewill–Wardell
   Green-function papers for any printed ESU/closed-FLRW mode-parity or
   "antipodal echo" statement — this is the likeliest place a verbatim
   antecedent for Prop echo could live.
4. A PhilPapers/PhilSci/MathSciNet pass on "domain of prediction"
   reformulations to firm up (or narrow) the Thm-char novelty question.
5. Optional bounded check: compute the retarded Green function sign flip
   numerically on an ESU conformal-time slab and compare with the
   Harte–Drivas conformally-flat prediction; label as a bounded numerical
   illustration only.
