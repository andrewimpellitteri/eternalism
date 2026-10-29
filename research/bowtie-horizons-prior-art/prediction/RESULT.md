# Prior-art audit: prediction and domain-of-dependence literature vs screening claims

28 October 2026. Task `prior-art-prediction`, OpenCode GLM headless worker.
Audits the four candidate claims X1-X4 of `research/bowtie-horizons/`
(SCREENING.md, RESULT.md) against the named prior-art sources and a targeted
search. Read-depth labels: discovery, abstract, full-text (coverage stated
where partial). Quotes preserve the source wording; OCR-degraded text is
normalized and marked. Absence of hits is not a novelty claim.

## The claims audited

- **X1** the instantaneous causal-potential domain violates growth (P1R) in
  every connected causally simple spacetime lacking pairwise common futures
  (de Sitter, LambdaCDM).
- **X2** the historical-potential repair H misses spacelike events in exact
  dust+Lambda (threshold d < R_x+R_s+2P_s).
- **X3** the causal-potential realm J^-(J^+(b)) minus the strict future of b
  is exactly the minimal region screening b's future on every Cauchy slice
  avoiding it, so bow-tie surplus events are causally idle.
- **X4** under deterministic MGHD evolution any realm containing that region
  fixes b's future, while the causal past does not.

## Verdict table

Per source and claim: FOUND = a source states (part of) the claim or its
essential content; PARTIAL = a neighbor stating closely related content but
not the claim; NOT-FOUND = no such statement seen at the stated depth.

| Source | Locator | Depth | X1 | X2 | X3 | X4 |
|---|---|---|---|---|---|---|
| Geroch 1977, Minnesota Studies VIII, pp. 81-93 | def. of P(q) p. 89-90; equivalence p. 90; closed-universe result p. 91 (vol. pagination; OCR) | full-text (scan, OCR) | NOT | NOT | PARTIAL (adjacent) | PARTIAL |
| Manchak 2008, Found. Phys. 38, 317-321 | thm. p. 320; def. of genuine prediction p. 320; D(S)-determination remark p. 318 | full-text | NOT | NOT | NOT | PARTIAL |
| Manchak-Weatherall 2018, Found. Phys. 48, art. 24 (DOI 10.1007/s10701-018-0170-3) | abstract | abstract | NOT | NOT | NOT | PARTIAL (context) |
| Smeenk-Wuthrich 2021, Phil. Sci. 88(1) 134-157; arXiv:2009.07555 | ar5iv full text: sec. 2 "Hyperbolic PDEs and Relativity", sec. 4; Choquet-Bruhat-Geroch passage | full-text (partial coverage: intros + secs. 2, 4 + refs) | NOT | NOT | PARTIAL (ingredients) | PARTIAL (components stated) |
| Hawking-Ellis 1973, chs. 6-7 | CUP ch. DOIs 10.1017/CBO9780511524646.007 (pp. 180-225), .008; 2023 ebook ch. abstract | gated (paywall); abstract | NOT | NOT | PARTIAL (ingredients, unverified at full text) | PARTIAL (ingredients, unverified) |
| Earman 1986, A Primer on Determinism | archive.org item (lending); Google Books TOC ch. III secs. 2, 6 | gated; discovery | NOT | NOT | NOT | NOT (unread) |
| Earman 1995, Bangs, Crunches... | author PDF sites.pitt.edu/~jearman/Earman_1995BangsCrunches.pdf (scan, text layer ends after preface); target pp. 125-130 via Manchak 2008 n. 15 | partial (front matter + preface); rest gated (OCR) | NOT | NOT | NOT | NOT (unread at target) |
| Budic-Sachs 1976, Gen. Rel. Grav. 7, 21-29 (DOI 10.1007/BF00762010) | Springer landing page (conclusion para. only) | abstract | NOT | NOT | NOT | PARTIAL |
| Muller-Hoissen 1981, Int. J. Theor. Phys. 20(6), 443-450 (DOI 10.1007/BF00671357) | Springer abstract | abstract | NOT | NOT | NOT | PARTIAL |
| Doboszewski 2019, Eur. J. Phil. Sci. 9, art. 20 (OA) | abstract | abstract | NOT | NOT | NOT | PARTIAL |
| Friedman-Kaiser-Gallicchio 2013, Phys. Rev. D 88, 044038; arXiv:1305.3943 | abstract; secs. I-III (author PDF) | full-text (partial coverage: intro, framework, shared-future criterion) | FOUND (premise) | PARTIAL (single-horizon thresholds) | NOT | NOT |
| van der Schaaf 2026, arXiv:2601.14029v2 | LaTeX source (arXiv e-print), Sections/Discussion, Sections/ModalLogic | full-text (targeted sections; source audited) | FOUND (premise) | NOT | NOT | NOT |
| Lesourd 2021, arXiv:2101.08324 | ar5iv full text: sec. 2 (B), sec. 3 | full-text (partial coverage) | NOT | NOT | NOT | PARTIAL |
| Jaeger 2025, NYU dissertation "Dependencies Across Spacetime" | philpapers.org/archive/JGEDAS.pdf: ch. 1 intro, sec. 1.7.3 | full-text (partial coverage) | NOT | NOT | PARTIAL (concept neighbor) | NOT |
| Dorato-Hoefer 2021, Disputatio 13(63), 373-384 | full text; keyword scan: "potential", "horizon" absent | full-text | NOT | NOT | PARTIAL (weak idle half) | NOT |
| Mariani (ed.) 2021, Disputatio 13(63) symposium intro (DOI 10.2478/disp-2021-0018) | full text (extract) | full-text (partial) | NOT | NOT | NOT | NOT |
| Grandjean 2022, Springer chapter DOI 10.1007/978-3-031-09763-8_4 | search extract (region-III passage) | discovery | NOT | NOT | PARTIAL (weak idle half) | NOT |
| Sbierski 2013, arXiv:1309.7591v3 (Ann. H. Poincare, DOI 10.1007/s00023-015-0401-5) | abstract | abstract | NOT | NOT | NOT | NOT (background only) |
| Ellis-Uzan 2016, C. R. Physique 17(9-10) (DOI 10.1016/j.crhy.2015.07.005) | abstract | abstract | PARTIAL (horizon facts) | NOT | NOT | NOT |
| Smeenk-Wuthrich-cited context: Arageorgis 2016 (DOI 10.5937/bpa1629033a); Teitel 2025 (Phil. Rev., DOI 10.1215/00318108-11873940, review of Belot) | abstracts | discovery | NOT | NOT | NOT | NOT |

Per-claim overall: X1 FOUND at premise level / NOT-FOUND as a claim; X2
NOT-FOUND; X3 NOT-FOUND as stated (two PARTIAL neighbors); X4 PARTIAL
(components standard, realm-wise formulation not found).

## What each source actually says (quotes)

**Geroch 1977** (full-text; OCR normalized). Domain of prediction, pp. 89-90:
"Now fix any point q of M, and denote by P(q) the set of all points x such
that every past-directed timelike curve from x, without past end point,
enters I^-(q), but such that I^-(x) is not a subset of I^-(q). We shall call
this set P(q) the domain of prediction of q." Equivalence, p. 90: "point x is
in P(q) if and only if I^-(x) not a subset of I^-(q), and, in addition, there
is a three-dimensional, achronal surface S in I^-(q) with x in D^+(S)."
Closed universes, p. 91: "Given a space-time M, g, and a point q of M such
that P(q) contains a point to the future of q, then M, g is a closed
universe, in the sense that it admits a compact spacelike surface. (This
result is essentially a corollary of a theorem of Earman's that a Cauchy
surface to the past of a point must be compact.)" Also: P(q) is empty in
Minkowski spacetime; Einstein universe (Fig. 5) gives D^+(S) = entire future.
- vs X1/X2: no domain of existence, no growth axiom, no horizons. NOT.
- vs X3: formally adjacent but different: Geroch characterizes prediction of
  x by membership in D^+(S) for some achronal S inside q's past; he never
  asks for a minimal region that screens a point's future, and never uses
  J^-(J^+(b)). NOT-FOUND (adjacency recorded).
- vs X4: the prediction-vs-determination contrast (his Figs. 3-4 discussion:
  "a retrodiction rather than a prediction") and the compact-slice theorem
  are the classical ancestors of the "causal past does not fix the future"
  half. PARTIAL.

**Manchak 2008** (full-text). P. 318: "It is a theorem that, given the
physical situation on any achronal surface S, the physical situation in all
of D(S) is uniquely determined." Genuine-prediction theorem, p. 320: "Let
(M,g) be any spacetime and let q be any point in M. Then P-bar(q) is a subset
of the boundary of J^-(q)." Abstract: "one may predict one's own future only
in a closed universe ... prediction is essentially impossible in general
relativity."
- vs X4: supplies the "past data do not fix the future" half robustly (the
  genuine-prediction theorem survives any local laws). PARTIAL. No realm
  containing a D_pot-like region is considered. vs X1-X3: NOT.

**Smeenk-Wuthrich 2021** (full-text, partial coverage). "A theorem due to
Choquet-Bruhat and Geroch 1969 establishes that appropriate initial data
(Sigma, h_ab, k_ab), specified on a global time slice Sigma, determine a
unique (up to isometry), maximal globally hyperbolic development, a solution
to vacuum EFE." And: "the result quoted above establishes that appropriate
initial data fix a solution throughout the domain of dependence (up to
isomorphism)". Footnote 13: predictability questions "See, e.g., Geroch
1977. On our view, the fate of determinism does not depend on whether the
input data needed to specify a uniquely solvable problem are accessible to an
embedded observer."
- vs X4: the deterministic-MGHD half is exactly their subject matter
  (FOUND as component); but they never identify a minimal realm that fixes a
  point's future, and never discuss bow-tie domains. PARTIAL overall.
- vs X1-X3: keyword scans over the extracted text find no "screening", no
  minimal-region statement, no existence domains. NOT.

**Hawking-Ellis 1973 chs. 6-7** (gated: CUP paywall; chapter abstract of the
2023 ebook read). Ch. 6 abstract: "The closely related concepts of Cauchy
developments and global hyperbolicity are introduced in sec. 6.5 and sec.
6.6"; ch. 7 is "The Cauchy problem in General Relativity" (pp. 226-255 per
CUP contents). The D(E)/domain-of-dependence machinery is confirmed
secondhand via Geroch 1977 n. 2 (citing HE) and Galloway's Vienna notes
("initial data on S should determine the physics on D^+(S) (in fact on all of
D(S))"). The specific X3/X4 statements were not found and could not be
checked at full text. Access gate recorded.

**Earman 1986** (gated: archive.org lending copy; Google Books TOC read).
Ch. III "Determinism in Special Relativistic Physics" contains sec. 2
"Domains of Dependence" and sec. 6 "Domains of Prediction". Relevant in
structure; text not accessed. NOT (unread).

**Earman 1995** (partial: the author-site scan's text layer yields only front
matter + preface; target pages 125-130, cited by Manchak 2008 n. 15 for
"Maxwell's equations constrain some spacetimes in such a way as to allow for
prediction", were not accessible). NOT (unread at target). Gate recorded.

**Budic-Sachs 1976** (abstract-level: Springer page). Conclusion paragraph:
"The results in Sections 2 and 3 show that demanding determinism is such a
stringent restriction that it would involve a really drastic change in
viewpoint." Their definition of a deterministic spacetime was not accessible
(paywalled). PARTIAL for X4: a dedicated "deterministic spacetimes" literature
exists, anchored to GKP causal structure; exact content unchecked.

**Muller-Hoissen 1981** (abstract). "Generalizing a definition given by
Budic and Sachs we define the set theta(M) of deterministic points of a
space-time M, and show that theta(M) != empty implies that M admits compact
achronal slices. Further we give a new characterization of space-times with
theta(M) = M. The relation between determinism, existence of particle
horizons, and visible Cauchy surfaces is investigated." PARTIAL for X4: the
deterministic-points program links determinism to horizons and compact
slices, parallel to Geroch/Manchak; no per-event realm-fixing claim seen.

**Doboszewski 2019** (abstract): "I discuss candidates for definitions of
determinism in the context of general relativistic spacetimes, and argue that
a definition which does not make recourse to any particular region of
spacetime should be preferred over alternatives". PARTIAL context for X4
(region-relativity of determinism definitions); no screening region.

**Friedman-Kaiser-Gallicchio 2013** (full-text, partial: abstract, secs. I-III
via the author's copy). "We derive criteria for whether two cosmological
events can have a shared causal past or a shared causal future, assuming a
Friedmann-Lemaitre-Robertson-Walker (FLRW) universe with best-fit
cosmological parameters from the Planck satellite." "The late-time
acceleration creates a cosmic event horizon that bounds the furthest
distances observers will be able to see, even in infinite cosmic proper
time." "Events have no shared causal future if their future light cones will
never intersect each other's worldlines before eta = 1" (eta_1: conformal end
of inflationary-hot-big-bang FLRW). "our observable Universe has a finite
conformal lifetime, and hence a cosmic event horizon at current redshift
z = 1.87."
- vs X1: the causal premise (pairwise common futures fail beyond explicit
  comoving-distance thresholds in exact dust+Lambda) is FOUND here as
  established physics, computed for Planck 2013+ parameters. Their purpose is
  cosmic Bell tests; nothing connects to (P1R), growth, or any
  existence-domain. The X1 claim itself (growth violation for a
  causal-potential domain) NOT-FOUND.
- vs X2: their thresholds involve our worldline and the event horizon, not a
  two-sided R_x+R_s+2P_s bound and no historical domain. PARTIAL only in the
  sense that threshold-style horizon arithmetic in exact FLRW is prior art.

**van der Schaaf 2026** (arXiv:2601.14029v2; LaTeX source of Sections/
ModalLogic and Sections/Discussion audited). "a2 := Diamond Box A ->
Box Diamond A, confluence. Confluence is also referred to as the
Church-Rosser property, the diamond property, or being weakly directed."
"Both are globally hyperbolic, but 2^-Minkowski spacetime does not have the
(future-directed) confluence property for the causal relation ..., therefore
exhibiting different modal logics. The logics of the spacetimes under the
causal (chronological) relation are S4.2 (Goldblatt 1980) (OI.2
(Shapirovsky 2002)) and S4 (OI) respectively."
- vs X1: failure of pairwise common futures in connected globally hyperbolic
  spacetimes is prior art on the logic side (FOUND as premise); no growth
  axiom or existence domain anywhere. X1 itself NOT-FOUND.

**Lesourd 2021** (arXiv:2101.08324; ar5iv full text, partial). Definition 2.3:
"p in M is predictable from q, written p in P(q), iff p in D^+(S) for some
closed, achronal set S subset J^-(q)." Proposition 2.4 (Manchak): "If P(q)
intersect (I^+(q)\J^-(q)) != empty, then (M,g) admits an edgless compact
achronal set." Proposition 2.6: P-bar(q) subset boundary J^-(q). Also:
"if M is a globally hyperbolic Cauchy development of vacuum initial data on a
Cauchy surface S and there is a point whose past lightcone contains S, then
the contents of such a lightcone determines all of M (up to isometry)."
PARTIAL for X4 (closed-universe determination results); NOT for X1-X3.

**Jaeger 2025** (NYU dissertation; full-text on philpapers, partial coverage:
abstract, ch. 1 intro, sec. 1.7.3). "the Parental Markov condition: a
region's immediate past screens it off from any other past or present
event." "Strong Boundary Markov: take any spacetime region R and wrap it in a
thin buffer zone - a thick boundary; the state of this boundary alone then
screens off everything inside R from everything outside." "Provided the
background geometry is static ... A generalization to theories with dynamical
spacetime structure (such as general relativity) is a topic for future work."
PARTIAL for X3: the nearest "screening in spacetime" concept found -
Markov-style, probabilistic, about arbitrary regions and their boundaries in
static backgrounds; it does not identify J^-(J^+(b))\J^+(b), does not claim
minimality, and is not deterministic domain-of-dependence screening.

**Dorato-Hoefer 2021** (full-text; the Disputatio symposium critique of C&R's
Nothing to Come). Transitivity objection, p. 381: "the need to reject
transitivity of being re-introduces, in a sense, the solipsism that bow-tie
RGBT seemed able to avoid." Persistence objection, p. 382 (quoting C&R
149-152). Keyword scan of the full extract: "potential" and "horizon" return
zero hits. So their objections are exactly persistence and transitivity; no
horizon or curved-spacetime discussion, nothing like X1-X4. PARTIAL for X3
only in the trivial sense that they note elsewhere points stand in no causal
relation to the point s (cf. Grandjean below); the strong idle-surplus
statement is absent.

**Mariani 2021 (Disputatio 63 symposium introduction)** (full-text extract):
"The two main options for a relativistic GBT are the so-called 'bow-tie' or
'pointy' views ... In NTC the 'bow-tie' view is defended. Dorato and Hoefer
offer a set of criticisms of this choice, in particular pointing out that the
rejection of the transitivity of the existence-as-of relation ... is too high
a price to pay." Contributors: Deng, Dorato, Dyke, Hoefer, Markosian, Miller,
Torre, Wawer; C&R replied in the same issue. No horizons mentioned in the
introduction. Confirms the symposium state of the art around C&R. NOT for
X1-X4 (at this depth; remaining symposium contributions unread, flagged
below).

**Grandjean 2022** (discovery, search extract): "no event in region III can
be the cause or the effect of e (since any influence would have had to travel
faster than light)". This is the weak, standard causal-idleness of the
elsewhere relative to the single event e. X3's surplus-idle claim is stronger
(no causal route to any event of J^+(b)) and was not found. PARTIAL.

**Sbierski 2013** (abstract): "we present a proof that avoids the use of
Zorn's lemma. In particular, we provide an explicit construction of this
maximal globally hyperbolic development." Background for X4's MGHD setting
and for SCREENING.md premise (L); the localization premise itself neither
found nor refuted at this depth (full text unread; already a review target
there).

**Ellis-Uzan 2016** (abstract): horizons review; "event horizons play no role
at all in observational cosmology". Standard horizon background for X1/X2
premises. PARTIAL premise context only.

**Manchak-Weatherall 2018** (abstract): "(Information) Paradox Regained?":
formulates information loss as a predictability failure tied to
non-global-hyperbolicity. Prediction-lineage continuation; nothing like
X1-X4. Ryder 2026 (arXiv:2609.09927, abstract) continues this line.

## Summary verdicts

- **X1** (growth violation in horizons spacetimes): NOT-FOUND as a claim. The
  causal premise is established prior art: explicit shared-causal-future
  criteria in exact FLRW with Lambda (Friedman-Kaiser-Gallicchio 2013) and
  failure of confluence/directedness in globally hyperbolic spacetimes on the
  modal-logic side (van der Schaaf 2026; Goldblatt 1980 via v.d.S.). No
  source read connects horizons to C&R's (P1R) or to a causal-potential
  existence domain.
- **X2** (historical-potential H and the dust+Lambda threshold): NOT-FOUND.
  No source read defines any historical-potential domain; threshold-style
  horizon arithmetic exists only in different guises (FKG 2013, our-worldline
  thresholds).
- **X3** (minimal screening region = J^-(J^+(b))\J^+(b); idle surplus):
  NOT-FOUND as stated. Nearest neighbors: Geroch's achronal-surface
  characterization inside P(q) (formally adjacent, different purpose);
  Jaeger's Strong Boundary Markov (probabilistic, static backgrounds, no
  minimality, no J^-(J^+)); standard "data on S determine D(S)" uniqueness
  ingredients (Smeenk-Wuthrich; Galloway notes; HE chs. 6-7, gated). The weak
  idle half (elsewhere causally unrelated to e) is folklore; the strong
  version (no route to any event of b's future) not found.
- **X4** (realm-rigidity under deterministic MGHD): PARTIAL. Both halves
  circulate separately as standard results: deterministic MGHD evolution
  fixes the future of domains of dependence (Choquet-Bruhat-Geroch via
  Smeenk-Wuthrich; HE ch. 7; Budic-Sachs/Muller-Hoissen deterministic-points
  literature; Doboszewski's definitions), and the causal past alone does not
  fix the future (Geroch 1977; Manchak 2008; Lesourd 2021). No source read
  states the realm-wise formulation: that any realm containing
  D_pot(b) = J^-(J^+(b))\(J^+(b)\{b}) fixes b's future while J^-(b) does not.

Caveat: these are verdicts over a small, targeted search at the stated
depths; absence of hits is not evidence of novelty (project standard).
