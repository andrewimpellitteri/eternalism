# priority lane RESULT — Kill-test of prediction/indistinguishability priors for past-preserving Einstein completions

Task: lawful-completions-priority. Date of work: 2026-10-28. Worker: GLM headless
(opencode, zai-coding-plan/glm-5.3-flash). Scope: primary audit of Manchak 2008
(prediction / genuine prediction), observational-indistinguishability variants and
fixed-matter / topology / nonisometric-future constructions; prior-theorem coverage
check for the spherical incoming Vaidya / null-dust baseline; KILL / PASS /
CONDITIONAL verdict for CONTRACT items A and B.

This is a feasibility-round submission for review, not a final truth claim. Nothing
below is a novelty assertion; verdicts are presence-based (found priors), never
absence-based.

## 0. Search capability check (required by brief)

- Z.ai MCP server `web-search-prime`, tool `web_search_prime`: **FAILED** at first
  use, HTTP/MCP error -429, code 1310, "Weekly/Monthly Limit Exhausted. Your limit
  will reset at 2026-11-17 10:00:29". Recorded per handback requirement.
- Fallback `serpapi_search`: **worked** (results returned; quality mediocre for this
  niche but sufficient for lead discovery).
- Fallback direct HTTP (`webfetch`, `curl`): **worked** throughout.
- Local PDF text extraction: **worked** — Swift + macOS PDFKit
  (`/private/tmp/opencode/lcp/extract.swift`, run via `swift extract.swift <pdf>`),
  same method the horizons lane used. `pdftotext`/`pdftk`/ghostscript absent;
  `/usr/bin/python3` has no PyObjC; `qpdf` present (used for page counts).

## 1. Verdict summary

| Item | Verdict | Strongest prior |
|---|---|---|
| A: one pair of lawful models, same past, different relational future | **KILL** (established, with any local field laws incl. Einstein+matter) | Manchak 2008, genuine-prediction theorem and its proof-construction, pp. 319–321 |
| B: same, inside a fixed matter theory, common Cauchy topology, maximal GH developments, justified full-past matching | **CONDITIONAL** — split; see §3 | CBG 1969 (impossibility within GH); Chruściel–Isenberg 1993 / Taub–NUT / Gowdy / Costa et al. 2015 (possibility via non-GH extensions of a shared MGHD) |
| Cut-paste retains fixed Einstein–matter evolution + maximal GH status? | **No** for all audited cut-paste families | Geroch 1977 pp. 84–86; Manchak 2009 fn. 9–10; Linford 2026 §6 (best case: IJC-glued pieces, still not GH) |
| Spherical Vaidya/null-dust baseline: prior theorem coverage | Extension analysis exists (Israel; Aboelhassan 2023 thesis, embargoed); **no** OI/relational framing found; existence is near-trivial | Aboelhassan 2023 (abstract only); Christodoulou-type center behavior via Dafermos 2014 (abstract) |

Overall: the lane's own target is **not** A or B as stated. The only surviving delta
is a narrow, sharpened form of B specified in §5, which coincides with an open
question already posed in the literature (Doboszewski 2017 §11.3.6). Recommend the
coordinator treat A as baseline-with-citation, use the Vaidya construction only as an
existence trivializer, and evaluate C/D against §5.

## 2. Primary results audited (exact statements, locators, read depth)

### 2.1 Manchak 2008 — "Is Prediction Possible in General Relativity?", Found. Phys. 38 (2008) 317–321, DOI 10.1007/s10701-008-9204-6. Read depth: FULL-TEXT (LSE-hosted Springer PDF, extracted this run; 4 pp.).

- Definition (p. 318, attributed to Geroch priv. comm.; differs from Geroch 1977 by
  requiring S spacelike and closed): p ∈ P(q) iff (i) p ∉ J⁻(q) and (ii) there is an
  achronal, closed, spacelike S ⊆ J⁻(q) with p ∈ D(S).
- **Theorem (p. 319):** "Let (M,g) be a spacetime. If there are points q,p ∈ M such
  that p ∈ P(q) ∩ I⁺(q), then (M,g) admits a compact, spacelike slice." Proof uses
  Hawking–Ellis Prop. 8.3.3 and Prop. 6.6.6; "slice" = closed achronal edgeless set
  (his n. 9). Verified against the draft-3 wording already pinned by
  research/horizons/PRIOR_WORK_CHECK.md — matches.
- Definition of genuine prediction (p. 320): p ∈ P̄(q) iff p ∈ P(q) and, for all
  inextendible spacetimes (M′,g′), if there is an isometric embedding
  φ : J⁻(q) → M′, then there is an isometric embedding
  φ′ : J⁻(q) ∪ J⁻(p) → M′ with φ′|J⁻(q) = φ.
- **Genuine-prediction theorem (p. 320):** for any spacetime (M,g) and any q,
  P̄(q) ⊆ ∂J⁻(q). (Extraction garbled the statement line; proof and his closing
  paragraph confirm it. Matches PRIOR_WORK_CHECK addendum.)
- **Robustness paragraph (p. 321) — the key fixed-law prior:** the partner (M″,g″)
  built in the proof (two copies of M∖S, edges cross-identified, boundary 2-spheres
  excluded) "is locally isometric to the spacetime (M,g). So, the theorem goes
  through even under the imposition of any local conditions (e.g. the energy
  conditions, Maxwell's equations, or Einstein equation)." This is the paper's own
  statement that the pointed same-causal-past / different-future pair exists inside
  any locally specified field theory.
- n. 8: Geroch's original 1977 p. 92 claim "was later shown to be false" — Hogarth
  1993, SHPS 24, pp. 726–727 (Hogarth NOT read; access limit).
- n. 14: prior examples of the same cut-paste type in Hawking–Ellis 1973 pp. 58–59
  and Geroch 1977 pp. 89–90. n. 15: Earman 1995 pp. 125–130 and Ellis–Sciama 1972
  pp. 41–42 for Maxwell-based law-relative prediction (both NOT read).
- Limits: theorem statements are metric-level; no Cauchy/topology matching of the
  CONTRACT B kind is claimed or proved there.

### 2.2 Manchak 2009 — "Can we know the global structure of spacetime?", SHPMP 40 (2009) 53–56, DOI 10.1016/j.shpsb.2008.07.004. Read depth: FULL-TEXT (UCI-hosted PDF, extracted this run).

- Definition (p. 54, = Malament's "weak" OI, asymmetric): (M,g) is observationally
  indistinguishable from (M′,g′) iff for every p ∈ M there is p′ ∈ M′ with I⁻(p)
  isometric to I⁻(p′). "Causally bizarre": ∃p with I⁻(p) = M.
- Lemma (p. 54): if I⁻(p) ⊊ M then I⁻(p) is a proper subset (used to pick escape
  neighborhoods).
- **Theorem (p. 55):** "Let (M,g) be any spacetime which is not causally bizarre
  satisfying any set C of local conditions. There exists another spacetime (M′,g′)
  (one that is not isometric to (M,g)) such that (i) (M′,g′) satisfies C and
  (ii) (M,g) is observationally indistinguishable from (M′,g′)." This settles
  Malament's 1977 conjecture and is the all-observers strengthening of the pointed
  2008 pair. Local conditions are preserved because the partner is locally
  isometric to M (his local-conditions definition, p. 55).
- Construction ("clothesline", pp. 55–56): countably many excised 3-disks in
  disjoint neighborhoods avoiding I⁻(p_i), edges cross-identified "excluding
  boundary points"; the boundary 2-spheres are "necessarily 'left out'" (n. 9,
  citing Hawking–Ellis pp. 58–59); other examples of the type: HE pp. 58–59,
  Geroch 1977 pp. 89–90, Geroch–Horowitz 1979 pp. 220–221 (n. 10).
- Matter fields: §5 says the clothesline "can rule out any objections of this kind"
  and refers to **Malament 1977, pp. 74–76** for details (n. 12) — pp. 61–79 of
  Malament were NOT accessible this run (see §2.3): access gate on the matter-field
  treatment.
- Limits: partner M′ is not globally hyperbolic (excisions/holes), not a maximal
  development of shared data, topology changed drastically; OI matches whole past
  cones pairwise but is one-directional and does not fix a pointed future
  disagreement by itself — the pointed version is what Manchak 2008 supplies.

### 2.3 Malament 1977 — "Observationally indistinguishable space-times", in Minnesota Studies vol. 8, pp. 61–80. Read depth: PARTIAL (p. 80 tail only). ACCESS GATE.

- The public LSE scan
  (personal.lse.ac.uk/robert49/ppb/pdf/GerochPredictnInGRMinnesVol81977.pdf)
  contains only 7 pages (qpdf --show-npages = 7): Malament's last page (printed
  p. 80) plus Geroch's complete paper (pp. 81–92). No other public scan found in
  this run's searches.
- Read from p. 80: his closing example — M and M′ with "excision barriers", M′ the
  unrolling, "observationally indistinguishable since no observational past of any
  future-inextendible curve in either extends beyond the excision barriers. But
  only M′ admits a global time function"; notes: n. 5 countable cover {I⁻(x)} of
  any spacetime (Geroch 1968 Lindelöf argument); n. 9 OI under non-time-orientability;
  n. 10 stable causality / Hawking 1968 equivalence.
- NOT read: pp. 61–79, including the weak/strong OI definitions in his own wording
  (reconstructed here from Manchak 2009 p. 54 and Linford 2026 §3, both read
  full-text) and the pp. 74–76 matter-field construction that Manchak 2009 n. 12
  points to. Flag: any manuscript text must not quote Malament directly beyond
  p. 80 until that page range is obtained (library scan needed).

### 2.4 Geroch 1977 — "Prediction in General Relativity", Minnesota Studies vol. 8, pp. 81–93. Read depth: FULL-TEXT (same scan, noisy OCR; definitions cross-checked against Manchak 2008/2009).

- Domain of dependence and its Maxwell uniqueness reading: pp. 83–84 ("Given the
  electromagnetic field on S, there is at most one extension … to D⁺(S)").
- **Hole example (pp. 84–85):** Minkowski vs Minkowski with a small closed spherical
  hole; Maxwell solutions vanishing on S′ that do not vanish to the future exist in
  M′ ("radiation can emerge from the hole"). **Einstein-equation remark (p. 85):**
  "Even the imposition of Einstein's equation … permits only the determination of
  the geometry in D⁺(S), and hence does not prohibit the construction of similar
  examples by 'cutting holes in spacetime.'" — the earliest explicit statement of
  the CONTRACT's cut-paste trap, at metric level.
- **Hole-freeness (pp. 86–87):** (M,g) is hole-free iff for every achronal 3-surface
  S and every metric-preserving embedding Ψ of D⁺(S) into any (M′,g′),
  Ψ(D⁺(S)) = D⁺(Ψ(S)); Minkowski is hole-free "as, indeed, are the standard exact
  solutions"; and: "'maximally extended' is no substitute for 'hole-free,' for there
  are spacetimes that satisfy the former and not the latter." Also the caveat that
  Minkowski to the past of a null plane is hole-free "by this definition".
- Modified-theory theorem (p. 86): in hole-free spacetimes, a map S → S′ preserving
  ALL FIELDS extends to D⁺(S) → D⁺(S′) — "practically a restatement of the
  definition."
- P(q) definition and equivalent S-characterization: p. 90 (timelike-curve version;
  I⁻-based; differs from Manchak 2008's J⁻/closed-spacelike variant — the three
  definitional variants are already tabulated in research/horizons/PRIOR_WORK_CHECK.md).
- Directly-verifiable-prediction result (p. 92): if P(q) contains a point to the
  future of q then (M,g) admits a compact spacelike surface — "essentially a
  corollary of a theorem of Earman's that a Cauchy surface to the past of a point
  must be compact"; later statement corrected/false-as-stated per Hogarth 1993
  (pp. 726–727), repaired by Manchak 2008's theorem.

### 2.5 Doboszewski 2017 — "Non-uniquely Extendible Maximal Globally Hyperbolic Spacetimes in Classical General Relativity: A Philosophical Survey", ch. 11 of Hofer-Szabó & Wrónski (eds.), Making it Formally Explicit, European Studies in Philosophy of Science 6, Springer, pp. 193–212, DOI 10.1007/978-3-319-55486-0_11. Read depth: FULL-TEXT (LSE-hosted author copy). Secondary for the GR theorems; primary locators recorded below.

- **Choquet-Bruhat–Geroch theorem as she states it (§11.1.4, p. 199):** for an
  initial (vacuum) data set ⟨Σ,g₀,k₀⟩ there exists a unique, up to isometry,
  maximal globally hyperbolic development; generalizable to non-vacuum data (she
  cites Ringström 2009). "This uniqueness result crucially depends on the causality
  condition (global hyperbolicity) and does not establish uniqueness of the maximal
  extension of spacetime simpliciter." Primary: Choquet-Bruhat & Geroch 1969,
  "Global aspects of the Cauchy problem in general relativity", CMP 14(4): 329–335
  (PRIMARY NOT READ — access gate; paywalled).
- Established extendible-MGHD examples with non-isometric extensions (her §11.2,
  pp. 200–202): Misner space (unique extension unless stricter equivalence,
  per Chruściel–Isenberg); Taub–NUT (Taub region = MGHD with two past and two
  future extensions; combined pairs non-isometric, "in both ways" indeterminism);
  polarized Gowdy T³ (vacuum, expanding, non-homogeneous; extendible iff Ω = 0 or 1
  on an interval; Ω constant on TWO disjoint intervals gives 2² = 4 extensions;
  countably many non-isometric extensions possible; all to the past, through the
  t = 0 "Big Bang"); LRS Bianchi IX (Ringström 2009: two non-isometric C²
  extensions); Costa–Girão–Natário–Silva 2015 (Einstein–Maxwell–scalar with Λ > 0:
  spherically symmetric characteristic data with non-isometric, generic C¹
  extensions through the Reissner–Nordström horizon). Primary refs recorded from
  her bibliography: Chruściel & Isenberg 1993, "Nonisometric vacuum extensions of
  vacuum maximal globally hyperbolic spacetimes", PRD 48(4): 1616; Moncrief 1981,
  PRD 23(2): 312; Misner & Taub 1969, Sov. Phys. JETP 28: 122; Costa, Girão,
  Natário, Silva 2015, CMP 339(3): 903–947; Ringström 2009, The Cauchy Problem in
  General Relativity (EMS). All primary GR papers: NOT read (discovery via her
  survey).
- Common features of all known cases (§11.3.1): exact solutions with nontrivial
  symmetries; spatially compact; vacuum (until Costa et al.); fail strong causality
  in the non-isometric regions (assuming a hole-freeness-type nicety condition);
  singular; time-orientation-preserving non-uniqueness comes with disconnected
  Cauchy horizons.
- Physical-equivalence subtleties (§11.3.2, attributing to Chruściel–Isenberg 1993):
  the two future extensions of the Taub region are isometric by a
  time-orientation-preserving isometry but not by one extending the identity on the
  shared region / in the identity component — i.e. "same past, inequivalent future"
  is sensitive to the equivalence relation chosen.
- Her statement (§11.1.3, type 5) and Ringström 2009 quote (p. 210): "The fact that
  there are inequivalent maximal extensions means that the initial data do not
  uniquely determine a maximal development. In this sense, the general theory of
  relativity is not deterministic." Belot 2011 (GRG 43: 2865–2884) quoted (p. 210):
  instances where globally hyperbolic solutions admit non-isometric extensions are
  "genuine indeterminism, not gauge equivalence" — useful anchor against the
  "just coordinates" trap.
- **Open question (§11.3.6, p. 208), quoted:** does there exist a spacetime which is
  maximal globally hyperbolic, satisfies an energy condition, and has ≥ 2
  non-isometric extensions that are (a) hole-free (in a precise sense), (b) not
  Malament–Hogarth, (c) strongly causal, (d) to the future only, (e) with a single
  connected Cauchy-horizon component, (f) satisfying an energy condition? "Is there
  a robust or stable class of such spacetimes?" — this is, at assumption level, the
  nearest published formulation of the surviving B delta (§5 below).

### 2.6 Linford 2026 — "Observational Indistinguishability and the Beginning of the Universe", arXiv:2603.04159v3 (v1 4 Mar 2026; v3 9 Oct 2026; physics.hist-ph). Read depth: PARTIAL FULL-TEXT (HTML §§1–6.1 fully; §6.2 partial; §7–8 and appendices A–C not read). Preprint — claims unrefereed.

- Verified contents: Thm 1 = Manchak 2009 theorem (verbatim restatement);
  Thm 2 attributed to Manchak 2011 ("What is a physically possible spacetime?",
  Phil. Sci. 78: 410–420 — NOT read this run): any non-bizarre spacetime with local
  properties C and global conditions G = {inextendibility, isotropy, global
  hyperbolicity, hole-freeness} is weakly OI from a non-isometric partner violating
  every member of G; Thm 3 attributed to Manchak 2016: every spacetime is weakly OI
  from one without a cosmic time function (his proof cites "Lemma 1 / Proposition 1"
  with a page number, 1057, that does not match Manchak 2016a's pagination
  265–276 — citation defect to flag, not to resolve here); his own Thms 4–5:
  singularity-theorem application conditions (global hyperbolicity, time
  orientability, no CTCs) and everywhere-past-b-incompleteness are each weakly OI-
  invisible.
- §6 (the part closest to our B): **Clothesline-OS model** — clothesline of an
  expanding dust FLRW spacetime with the M(1,β) piece replaced by a time-reversed
  Oppenheimer–Snyder model joined through the timelike worldtube via Israel junction
  conditions with no thin shell; he claims the result satisfies the EFE, the
  standard energy conditions, and ∇_μT^μν = 0. **Clothesline-SM** adds a
  thin-shell piece and a Möbius-strip region, making the model non-time-orientable
  (hence not stably causal). Abstract-level summary: "all past singular dust FLRW
  spacetimes are observationally indistinguishable from counterparts which … either
  do not include a singularity to the past of every point or else do not have the
  sort of time ordering intuitively required for a cosmic beginning."
- Critical assessment (mine): the IJC check covers the OS worldtube only; the
  clothesline seams (excluded 2-spheres of Manchak-type excisions) are not treated
  as junction surfaces, and "both pieces solve the EFE, hence the result does" is
  asserted, not proved, at the seams; no GH/maximality claim is made for the
  nemeses; the OI used is weak/asymmetric, which Cinti–Fano (§4) contest. Do not
  cite Linford as establishing fixed-matter pairs without checking Appendix A
  against the seams.

### 2.7 Manchak 2016 — "Epistemic 'Holes' in Space-Time", Phil. Sci. 83 (2016) 265–276. Read depth: FULL-TEXT (UCI-hosted PDF).

- Conditions taxonomy: geodesic completeness ⊂ hole-free ∧ inextendible (Prop. 1,
  crediting Manchak 2014); Geroch's 1977 hole-freeness is too strong — "Minkowski
  space-time fails to be hole-free under this formulation (Krasnikov 2009)" [PRD
  79: 124041, "Even the Minkowski Space Is Holed"]; Manchak's own repair via
  "effective extensions" (2009, GRG 41: 1639–43, NOT read).
- Example 2: conformal rescaling of Minkowski-minus-a-point that is inextendible
  AND hole-free yet still mutilated — inextendibility + hole-freeness do not
  capture "hole" intuitions.
- Epistemic-hole definitions EH(g)/EH(f) (two future-inextendible timelike curves
  with a common past endpoint and nested observational futures); Minkowski,
  Kruskal–Schwarzschild, de Sitter, AdS, Gödel are EH-free; Prop. 2: EH(f)-free +
  chronological ⇒ not nakedly singular; Example 5: a GH, geodesically complete
  spacetime with both EH(g) and EH(f); n. 6: global hyperbolicity is not equivalent
  to chronology + EH-freeness (universal AdS cover).
- Relevance: supplies the exact "named obstruction" vocabulary for CONTRACT B's
  hole-freeness clause — any B pair must say which hole-freeness variant is
  required, and Example 2-type conformal tricks must be excluded by fiat.

### 2.8 Supporting abstracts/snippets (read depth as marked)

- Dafermos, "Black holes without spacelike singularities", arXiv:1201.1797v2 =
  CMP 332 (2014) 729–757. ABSTRACT. For small spherically symmetric perturbations
  of two-ended RN data (Einstein–Maxwell–real scalar), the spacetime boundary is a
  bifurcate null hypersurface across which the metric extends continuously but
  cannot be extended C² (nor at Christoffel level); Hawking mass blows up
  identically along it. Relevance: the established regularity ceiling for
  extensions in a fixed coupled matter system — any B pair built near RN lives at
  C⁰ metric / non-C² regularity, not smooth.
- Aboelhassan, "On Maximal Extensions of the Vaidya Metric", PhD thesis, Queen's
  University, 2023, hdl:1974/31562. ABSTRACT ONLY; FILE EMBARGOED UNTIL
  2028-04-24 (request-a-copy only). Constructs and analyzes three maximal
  extensions of the Vaidya metric (pure radiation), building Israel's coordinates
  constructively, differentiating extensions by mass function (outflux, influx,
  exploding-to-imploding), and verifying null-geodesic completeness with Penrose
  diagrams. Relevance: spherical null-dust maximal-extension analysis exists; no
  non-uniqueness-of-MGHD-extensions claim is made at abstract level; no OI or
  relational framing anywhere.
- Burnett 1996, CQG 13: 111 (ABSTRACT snippet): maximal hypersurfaces exist in the
  maximal development of any spherically symmetric spacetime with Vlasov matter or
  a massless scalar field. Lead only (for constraints lane).
- Sbierski 2021 (Edinburgh PDF, DISCOVERY snippet): C⁰-inextendibility programme;
  GH + timelike-geodesically-complete ⇒ C⁰-inextendible; mentions spherically
  symmetric weak-null examples. Lead only.
- Lesourd, arXiv:2101.08324. NOT independently read this run; project record at
  research/horizons/PRIOR_WORK_CHECK.md (sections 1–2 and part of 3 full-text
  there): when past light cones determine the model (compact Cauchy surface, no
  null lines, de Sitter observer horizons).
- Cinti & Fano 2021, "Careful with those scissors, Eugene! Against the
  observational indistinguishability of spacetimes", SHPSA (ScienceDirect
  S0039368121001084). DISCOVERY ONLY (philpapers 403; ORA mirror returned HTML, not
  PDF). From snippets: they argue Manchak's weak OI "ensures only that there is a
  counterpart of points of M in M′, not vice versa" and propose a strengthened
  definition. Strongest contrary evidence located; full text needed for the
  coordination review.
- Manchak & Barrett 2023, "A Hierarchy of Spacetime Symmetries: Holes to
  Heraclitus", BJPS (cited by 18); Manchak & Barrett 2024, "Heraclitus-Maximal
  Worlds", J. Phil. Logic 53: 1519–1536; Barrett & Manchak 2024, Philosophy of
  Physics 2:11; Manchak 2025, "Heraclitus + Einstein = ?" (iai.tv popular piece,
  FULL-TEXT read) citing Halvorson–Manchak–Weatherall 2025 "Defining Determinism"
  and Manchak–Barrett–Halvorson–Weatherall 2025, "Determinism and Asymmetry in
  General Relativity", BJPS forthcoming. DISCOVERY for all but the popular piece.
  Relevance: the Heraclitus result "local structure fixes global structure"
  (unique-gluing) is background for D-level classification targets; the 2025
  determinism papers are unchecked leads that may already treat Doboszewski-style
  extension indeterminism.
- Hogarth 1993, SHPS 24: 721–739 and Earman 1995 — NOT read; cited via Manchak 2008
  nn. 8, 15 only.

## 3. CONTRACT A and B against the audited record

### 3.1 Item A — KILL

CONTRACT A asks for one pair of lawful models with isometric ENTIRE I⁻(b)
(preserving matter and observer germ) and different relational future at (b,u).

- Established, pointed version: Manchak 2008 pp. 320–321. For any q and any
  p ∉ ∂J⁻(q) (in particular p on q's future geodesic at proper time T, which is not
  on ∂J⁻(q)), the proof constructs an inextendible (M″,g″) containing an isometric
  copy of J⁻(q) — the CLOSED causal past, stronger than I⁻(b) — such that no
  isometric embedding of J⁻(q) ∪ J⁻(p) into M″ extends it. Agreement of the future
  of the image point with the future of q up to p would induce exactly such an
  embedding, so the futures differ in the strongest sense available.
- Lawfulness: (M″,g″) is locally isometric to (M,g); Manchak states (p. 321) the
  construction goes through "even under the imposition of any local conditions
  (e.g. the energy conditions, Maxwell's equations, or Einstein equation)". Matter
  fields are handled by local pullback; the models are smooth manifolds with smooth
  metrics (the seam 2-spheres are excluded from the manifold).
- All-observers version: Manchak 2009 Thm (settling Malament's conjecture), plus
  Malament's own example tail read on p. 80.
- Prior lineage is explicit in the sources themselves: Hawking–Ellis 1973 pp. 58–59
  and Geroch 1977 pp. 89–90 (both cited by Manchak 2008 n. 14 and 2009 n. 10).
- Falsifier for this KILL: a demonstrated error in Manchak 2008's proof or a
  demonstration that the excluded 2-spheres make (M″,g″) fail the CONTRACT's
  "same laws" requirement in a way local isometry cannot repair (e.g. if matter
  germs at the excluded spheres are essential to the chosen outcome). Neither found.

Conclusion: A is a corollary of published theorems and must be used as cited
background, not as a project result. This matches the CONTRACT's own anticipation
("A may be elementary and already known").

### 3.2 Item B — CONDITIONAL (split)

B adds: one FIXED matter theory, common Cauchy topology, maximal globally
hyperbolic developments, justified matching of full pasts.

**(B-i) Same initial data, two different maximal developments — impossible.** CBG
1969 (CMP 14: 329–335; statement verified at full-text depth only through
Doboszewski 2017 §11.1.4 and Ringström 2009 as cited there; primary unread — access
gate): the MGHD of given data is unique up to isometry. Any project claim of the
form "same data, two non-isometric maximal GH developments" is dead on arrival.

**(B-ii) Same data, unique shared MGHD, ≥ 2 non-isometric inextendible extensions,
b inside the shared region — established in symmetric vacuum / electrovac cases.**
Taub–NUT (Misner–Taub 1969; HE 1973; Moncrief 1981; Chruściel–Isenberg 1993 PRD
48: 1616), polarized Gowdy T³ (countably many non-isometric extensions), LRS
Bianchi IX (Ringström 2009, C²), Einstein–Maxwell–scalar + Λ>0 (Costa et al. 2015,
CMP 339: 903–947, generic C¹ extensions). In these examples the shared region is
the entire MGHD — far more than I⁻(b) — matching of pasts is the identity, Cauchy
topology is common (spatially compact), and matter is fixed (vacuum, or the
EM-scalar system). Belot 2011 and Ringström 2009 explicitly classify this as
indeterminism, not gauge. Any A/B-level project claim inside this territory is a
KILL; the CONTRACT's "nonisometric-future constructions" clause is occupied here.

**(B-iii) The surviving delta.** What the audited record does NOT contain (stated
strictly as "not found at this depth", not as proof of absence):

1. A pair both of whose members are globally hyperbolic models of ONE fixed
   well-posed non-vacuum matter system, agreeing on the ENTIRE pointed past
   (I⁻(b) with matter fields and observer germ), differing in a relational outcome
   along (b,u). The known OI partners are non-GH by construction (holes/excisions;
   Manchak 2011 per Linford Thm 2 even tunes the nemesis to violate GH); the known
   non-unique-extension pairs agree on a whole MGHD but their extensions violate
   strong causality (except possibly Costa et al., unstated in the survey), are
   C¹/C² at best, and are symmetry-generated.
2. Any such pair in a smooth (C^∞) regularity class; Dafermos 2014 shows the
   natural coupled-system examples top out at C⁰ metric extendibility.
3. A fixed-matter (non-vacuum) counterpart of Chruściel–Isenberg; Doboszewski 2017
   §11.1.3 states the extendible-MGHD question "has not been yet investigated
   thoroughly beyond vacuum solutions, and even in that case the analysis is
   restricted to certain special (highly symmetric) cases" (superseded in part by
   Costa et al. 2015 for EM-scalar+Λ, still symmetric and C¹).

This delta coincides with Doboszewski's published open question (§2.5 above) plus
two strengthenings: fixed well-posed matter system instead of an energy condition,
and the CONTRACT's pointed relational-observable formulation instead of abstract
non-isometry. That is a real, narrow gap — but it is a gap relative to a 2017–2015
survey level of audit, not a demonstrated theorem-shaped opening.

## 4. Cut-paste vs fixed Einstein–matter evolution and maximal GH status (CONTRACT trap check)

- Excision/clothesline cut-paste (HE pp. 58–59; Geroch pp. 89–90; Manchak 2008
  proof; Manchak 2009 Thm): preserves LOCAL conditions only (local isometry); the
  excluded boundary 2-spheres are holes; the result is not globally hyperbolic, not
  a development of shared data, and topology is changed drastically (chains of
  copies). Matter is preserved by pullback on the smooth part; nothing like a
  global initial-value solution is claimed.
- Geroch's hole example (pp. 84–85) shows the matter half of the trap concretely:
  in the holed model there are Maxwell solutions vanishing on S′ and nonzero to
  the future — the same matter model does not preserve solution-sets across the
  cut; and his p. 85 remark says Einstein's equation does not prohibit
  hole-cutting either.
- IJC-based gluing (Linford 2026 §6): the best available cut-paste upgrade —
  dust-to-dust (FLRW ↔ time-reversed Oppenheimer–Snyder) through a timelike
  worldtube with no shell; EFE + energy conditions + ∇T = 0 claimed for the result.
  Still: clothesline seams unexamined; not GH; no common Cauchy topology; and his
  nemeses are explicitly not offered as physically reasonable.
- Thin-shell/null-dust junctions: weak (distributional) solutions at best;
  uniqueness of evolution is exactly what fails at shell-crossing/center
  singularities (Christodoulou-type; accessed here only via Dafermos 2014 abstract
  and the survey literature).
- Maximal GH status: none of the audited cut-paste partners is a maximal GH
  development of anything shared. Conversely, Geroch's warning (p. 86) that
  "maximally extended is no substitute for hole-free" and Manchak 2016's Example 2
  (inextendible + hole-free conformal hole) show maximality alone will not police
  the CONTRACT's "no holes" intentions either. A B-candidate must state its
  regularity class and its hole-freeness variant explicitly (Manchak 2016 supplies
  the discriminating examples).

## 5. Spherical Vaidya / null-dust baseline: prior-theorem coverage (lane assignment)

- Direct extension analysis exists: Israel's maximal extension work (as reported by
  Aboelhassan 2023, abstract) and Aboelhassan 2023 (three maximal extensions,
  null-geodesically complete, distinguished by mass function; embargoed thesis —
  ACCESS GATE, abstract only). No source found that frames Vaidya extensions as
  observationally-indistinguishable or pointed-relational pairs; no source found
  that proves non-uniqueness of extensions of the Vaidya MGHD as such (the
  Christodoulou-type non-uniqueness lives in the scalar-field BV framework and at
  center shell-crossings; primary not audited in this lane).
- Existence is near-trivial, as the CONTRACT suspects. Sketch (MY analysis,
  conjecture-level, not sourced; falsifier below): take M₁ = Minkowski and M₂ =
  delayed ingoing Vaidya (m ≡ 0 until advanced time v* > t_b, then a shell of
  energy Δm ≥ 0). For b at (t_b, r = 0), every point of the shell satisfies
  v + r = v₀ > t_b + r_b, hence lies outside J⁻(b); m agrees with 0 on all of
  J⁻(b); both models solve Einstein–null-dust; b's future geodesic meets the shell
  at proper time ≈ v₀ − t_b, where M₁ stays regular and M₂ develops (at best) a
  weak central singularity with non-unique continuation. Both models are globally
  hyperbolic up to that event. So an A-pair inside one fixed matter system with
  EXACT full-past matching exists modulo the center-crossing regularity question —
  which is precisely the Israel/Christodulu/Aboelhassan territory.
- Candidate obstruction L1 (mine, with falsifier): for a CENTERED b, a spherically
  symmetric difference cannot be hidden from I⁻(b) unless it is deferred in
  advanced time v beyond t_b; since m(v) is r-independent, m is fixed on all of
  I⁻(b) iff it is fixed for all v < t_b, so any spherical difference is equivalent
  to a delayed-shell (or delayed-flux) difference, and b's future difference always
  manifests through the center-crossing event. Falsifier: exhibit a spherically
  symmetric pair with centered b, identical I⁻(b) (metric + dust), whose difference
  manifests before any null signal from the shell reaches b. If L1 survives, the
  coordinator's baseline is forced through the center singularity, and the
  "trivializing" baseline inherits exactly the regularity/non-uniqueness machinery
  of §3.2 (B-ii) — i.e. it does NOT trivialize the interesting part.
- Consequence for the coordinator: the spherical null-dust family trivializes
  EXISTENCE of A-pairs (subject to L1) but its pairs are exactly as "lawful" and
  exactly as far from B's smooth/GH/full-matching requirements as the published
  ones. Recommend building it as the kill-baseline only.

## 6. Three closest predecessors, assumption level (deliverable)

1. **Manchak 2008, pp. 319–321** (full-text). Assumptions: smooth time-oriented
   spacetime; arbitrary local field conditions. Result: pointed partner sharing
   J⁻(q), with no extension of the isometry to J⁻(q) ∪ J⁻(p) for any
   p ∉ ∂J⁻(q); plus the closed-universe theorem for directly verifiable
   prediction. Relationship to CONTRACT: kills A outright (and is stronger:
   closed past, all local laws).
2. **Manchak 2009, p. 55** (full-text; completes Malament 1977's conjecture).
   Assumptions: non-causally-bizarre spacetime + any set of local conditions.
   Result: non-isometric partner observationally indistinguishable at every point
   (weak OI). Relationship: kills the all-observers version of A; with Manchak 2011
   (via Linford Thm 2) even GH/inextendible/hole-free/isotropic models have
   partners violating all four.
3. **Chruściel–Isenberg 1993 (PRD 48: 1616) with the Taub–NUT / Gowdy / Costa et
   al. 2015 (CMP 339: 903–947) family** (survey full-text; primaries discovery).
   Assumptions: fixed Einstein–matter system (vacuum; EM-scalar + Λ>0), symmetric
   exact solutions, spatially compact Cauchy topology. Result: same initial data,
   unique shared MGHD, multiple non-isometric inextendible extensions (isometric-
   by-flip but not via identity on the shared region, per Chruściel–Isenberg as
   reported by Doboszewski §11.3.2). Relationship: occupies B-ii; leaves only the
   B-iii delta of §3.2.

Runner-up with a different failure mode: Geroch 1977 pp. 84–87 (hole example +
hole-freeness + maximality caveat) — the origin of the CONTRACT's trap list, and
the correct citation for "cut-paste is lawful only locally".

## 7. Deliverable: candidate lemma, named obstruction, falsifier, verdict

- **Verdict on A: KILL** (established; §3.1).
- **Verdict on B: CONDITIONAL.** Pass conditions: retarget B to the B-iii delta —
  a pair of smooth globally hyperbolic models of ONE fixed well-posed non-vacuum
  system (candidate families already shortlisted by the CONTRACT: Einstein–Vlasov,
  Einstein–massive-scalar), exact equality on I⁻(b) including matter and observer
  germ, difference in a relational observable at (b,u,T), with the hole-freeness
  variant and regularity class stated (§4). Everything left of that line is
  published.
- **Named obstruction:** within GH, CBG uniqueness forces any B-pair to use
  different initial data agreeing only on the cone; the cone contains no Cauchy
  slice, so no published uniqueness theorem forbids B-iii — but equally no
  published construction achieves it: all known constructions buy the disagreement
  either with holes (non-GH partners) or with a shared whole MGHD whose extensions
  break strong causality / regularity. That dichotomy (holes vs horizon) is the
  obstruction to name in any claim contract.
- **Candidate lemma L2 (project-side, falsifiable):** There exist two smooth
  globally hyperbolic solutions (M,g,Ψ) and (M′,g′,Ψ′) of one fixed well-posed
  Einstein–matter system with non-vacuum matter, a pointed isomorphism
  I⁻(b) ≅ I⁻(b′) carrying Ψ and the observer germ, and a scalar observable along
  the geodesic from (b,u) at proper time T whose values differ; with both models
  hole-free in a stated variant (e.g. Manchak's effective-extension version).
  Falsifier 1 (kills as "already known"): a published Einstein–Vlasov or
  Einstein–massive-scalar counterpart of Chruściel–Isenberg (non-isometric smooth
  strongly causal extensions from one data set). Falsifier 2 (kills as "impossible"):
  a uniqueness theorem for smooth strongly causal extensions of MGHDs in the chosen
  system (a CSMC-style result at C^∞/C² regularity for that matter model).
  Falsifier 3 (kills as "trivial"): a spherical null-dust pair with centered b
  violating obstruction L1.
- No novelty claim is made anywhere above; search-based negatives are labeled
  "not found at this depth" (depths: §2; queries logged in AGENT_REPORT.md).

## 8. Strongest contrary evidence located

- Cinti & Fano 2021 (discovery only): the weak-OI definition's asymmetry makes
  "indistinguishability" claims one-directional; they propose a stronger relation.
  Any project use of Manchak-style pairs must confront this critique. Full text
  still needed.
- Doboszewski 2017 §11.3.4–11.3.5: known non-unique-extension pairs are rare,
  symmetric, and CTC-tainted in the extension region; Chruściel-style cosmic
  censorship (genericity in a topology) is compatible with all of them. A
  B-iii claim must therefore also argue the pair is not an isolated symmetric
  artifact.
- Linford 2026's own framing concedes his nemeses are "not intended to be
  physically realistic" — his EFE claim at the seams is unverified (§2.6).

## 9. Access limits (mandatory record)

- Malament 1977 pp. 61–79: no public scan located; LSE file truncated (7 pages).
  Definitions reconstructed from Manchak 2009 + Linford 2026 (both full-text).
  Matter-field construction (Malament pp. 74–76) UNREAD.
- Choquet-Bruhat–Geroch 1969: paywalled; statement taken via Doboszewski 2017
  (full-text) and her Ringström 2009 citation (unread).
- Aboelhassan 2023 thesis: embargoed until 2028-04-24; abstract only.
- Costa et al. 2015, Chruściel–Isenberg 1993, Moncrief 1981, Misner–Taub 1969,
  Ringström 2009/2010, Krasnikov 2009, Hogarth 1993, Earman 1995, Manchak 2011,
  Manchak 2009 (GRG hole-freeness), Manchak 2014: not read (survey/secondary
  reliance, recorded per record in sources.jsonl).
- Cinti–Fano 2021: both public mirrors failed (403 / HTML); abstract-snippet only.
- Linford 2026 §6.2, §7–8, appendices: not read (time-box); §6.1 partial.

## 10. Proposed next tasks

1. Obtain Malament 1977 pp. 61–80 (library scan) and Cinti–Fano 2021 full text;
   audit the pp. 74–76 matter-field construction against the CONTRACT's
   matter-germ requirement before any A-level text is written.
2. Read the primaries behind §6 item 3 (Chruściel–Isenberg 1993; Costa et al.
   2015 §1 and extendibility statement; HE 1973 pp. 170–176 for Taub–NUT) at
   full-text depth; verify the "isometric-but-not-via-identity" claim and whether
   Costa et al.'s extensions satisfy strong causality.
3. Constraints lane: check Christodoulou's two-sided constructions and
   Timofeev-style extendible-MGHD claims in null dust/scalar systems against
   L1/L2 (this lane found only abstract-level traces; exact primaries unlocated
   this run).
4. If B-iii is pursued, write its claim contract against Doboszewski 2017
   §11.3.6 plus the §7 falsifiers; otherwise route the effort to C/D where the
   Heraclitus/gluing-uniqueness line (Manchak–Barrett 2023/2024; Mounoud 2015)
   and the relational lane take over.
