# Prior-work check for "Horizons and becoming" (25 Oct 2026)

Scope: bounded check of claims A, B, C from research/RESEARCH_PATHS.md (Paths 1-3).
Read-depth labels: full-text, abstract, discovery (search snippet only).
Texts were extracted from PDFs with PDFKit; OCR of Geroch is noisy, so definitions
below are cross-checked against Manchak 2008 and Lesourd 2021.

## Sources actually read

- Geroch, "Prediction in General Relativity", in Earman, Glymour, Stachel (eds.),
  Minnesota Studies in the Philosophy of Science 8 (1977), pp. 81-93. FULL-TEXT
  (scan, noisy OCR), via https://personal.lse.ac.uk/robert49/ppb/pdf/GerochPredictnInGRMinnesVol81977.pdf
  (the file begins with Malament's paper; Geroch begins at p. 81).
- Manchak, "Is Prediction Possible in General Relativity?", Found. Phys. 38 (2008)
  317-321, DOI 10.1007/s10701-008-9204-6 (confirmed by Crossref query and by the
  paper's own header). FULL-TEXT, via https://personal.lse.ac.uk/ROBERT49/ppb/pdf/Manchak2008a.pdf
- Lesourd, "Observations and predictions from past lightcones", arXiv:2101.08324v1.
  Sections 1-2 and the (B) part of section 3 read (partial full-text). Secondary
  on Geroch/Manchak, primary on its own results.
- van der Schaaf, "Some Results on Causal Modalities in General Spacetimes",
  arXiv:2601.14029v2 (Mar 2026). Abstract, intro, keyword scans for horizon,
  cosmology, FLRW, big bang, confluence (partial full-text).
- Search snippets only (discovery): Hogarth 1993, Earman 1995, McCoy 2017,
  Malament 1977 (the Malament paper also begins the Geroch PDF, only its tail was
  seen), Norton "Obs_Equiv" and "On under-determination in cosmology" (arXiv:1406.4747),
  Manchak-Barrett "Heraclitus-maximal worlds", Correia-Rosenkranz 2018.
  NOT read: Hogarth 1993, Earman 1995 chapters, McCoy 2017, Norton, Beisbart.

## Claim A: Theorem 1.1 and the examples. Verdict: PARTLY anticipated

### Geroch's exact definitions (full-text, p. 89-91 of the volume)

Geroch defines, for a spacetime M,g and point x, I^-(x) as the set reached by
past-directed timelike curves. Then (his words, from the scan, section 3):
"Now fix any point q of M, and denote by P(q) the set of all points x such that
every past-directed timelike curve from x, without past end point, enters I^-(q),
but such that I^-(x) is not a subset of I^-(q). We shall call this set P(q) the
domain of prediction of q."
He then states an "easily proved" equivalent: x is in P(q) iff I^-(x) is not
contained in I^-(q) and there is a three-dimensional achronal surface S in I^-(q)
with x in D^+(S). Strongly causal spacetimes are assumed throughout.

Manchak 2008 gives a variant (his attribution: Geroch, private communication, with
S spacelike and closed): p is in P(q) iff (i) p not in J^-(q) and (ii) there is an
achronal, closed, spacelike S in J^-(q) with p in D(S). Lesourd (Def. 2.3) states
p in P(q) iff p in D^+(S) for some closed achronal S in J^-(q). The three versions
differ in I^- versus J^-, timelike versus causal curves, and the nonmembership clause.

### Relation to our Set(b)

Our "settled from b" (every past-inextendible causal curve from x meets I^-(b))
is Geroch's first condition with causal curves in place of timelike curves, and
without his second clause (I^-(x) not a subset of I^-(q)). So Set(b) is, up to the
I^-/J^-, timelike/causal differences, I^-(b) union Geroch's P(b) (roughly:
Set(b) = I^-(b) union P(b), modulo the technical variants). Geroch's own equivalence
(existence of achronal S in I^-(q) with x in D^+(S)) is close to the (<=) direction
of Theorem 1.1. So the notion is NOT new; "settled" is the domain-of-prediction
condition. Do not present Set(b) as a new definition.

What was NOT found in Geroch/Manchak/Lesourd (as read):
- a characterization via a Cauchy temporal function t of the form
  "exists c < t(x) with J^-(x) cap {t=c} subset of I^-(b)" (not found at this
  depth; plausibly a short corollary of Geroch's S-characterization plus
  global hyperbolicity, so a modest result);
- the conformal-invariance corollary stated as such (follows from the definitions);
- any FLRW example, in particular the dust closed-universe threshold at maximum
  expansion (conformal time pi). Geroch's only closed example is the Einstein
  static universe (his Figure 5), where "D^+(S) is the entire future of S" and P(q)
  contains points to the future of q. Not found at this depth is not proof of
  absence: Earman 1995 and Hogarth 1993 were not read.

Related known results that the paper must cite:
- Geroch 1977: if P(q) contains a point to the future of q ("directly verifiable
  prediction") then the spacetime is closed (admits a compact spacelike surface);
  he attributes it as a corollary of Earman's theorem that a Cauchy surface to the
  past of a point must be compact. Manchak 2008 footnote 8: Geroch's own 1977
  statement was later shown false (Hogarth 1993, pp. 726-727); Manchak proves the
  conjecture (his Theorem). The closed-universe link of Theorem 1.1's examples is
  therefore anticipated in spirit: Set(b) meets I^+(b) only if M has a compact
  slice.
- Geroch's holes problem and Manchak's "genuine prediction" result (P-bar(q) is a
  subset of the boundary of J^-(q)): this undercuts any claim that, for an
  observer who does not know the spacetime, Set(b) beyond I^-(b) is knowable. This
  is an epistemic caveat only; Set(b) as defined is a metaphysical/nomological
  notion given M. State it as such. McCoy 2017 (Synthese 194) disputes Manchak's
  conclusion (abstract level only).
- Lesourd 2021: results on when past light cones determine M (compact Cauchy
  surface, no null lines, de Sitter observer horizons). Not about settledness
  per se, but the "closed universe" and "observer horizon" themes overlap.

Examples check. The Minkowski, flat FLRW, de Sitter and closed radiation statements
(Set = I^-) are consistent with Geroch's remark that in Minkowski space P(q) is
empty. The dust threshold at eta = pi was not found in any source read; keep it as
a claimed new example but verify it by an independent calculation, and flag that
the Einstein-static statement duplicates Geroch's Figure 5.

### Check on the mathematics of Theorem 1.1 (my reading of the draft)

The draft proof looks sound. Points to tighten (not counterexamples):
1. The limit-curve step needs the curves gamma_n from x to y_n with y_n leaving
   every compact set. Global hyperbolicity (strong causality) suffices for the
   limit-curve lemma giving a limit past-inextendible causal curve; the endpoints
   leave compacta because t(y_n) tends to -infinity and t is continuous. Cite
   Bernal-Sanchez for the existence of a Cauchy temporal function whose level sets
   are Cauchy surfaces (and surjective onto R). Then "c -> -infinity" is
   legitimate. Beem-Ehrlich-Easley / Minguzzi locators must still be checked.
2. "Points of gamma are limits of points of the closed set M \ I^-(b)" needs
   that each point of the limit curve is a limit of points of gamma_n (true for
   the limit-curve lemma convergence in the C^0 topology on compacts). Fine.
3. The statement is for the open I^-(b). With J^-(b) in the definition the
   characterization changes (the complement is open, so the limit argument fails).
   That is the I^- versus J^- decision flagged in the paper's plan, and it is a
   real asymmetry, not a technicality. Geroch's version uses I^-.
4. Time orientation and the existence of x with J^-(x) cap S_c empty (c below the
   range, e.g. a bounded-below t) are excluded when t is onto R.
No known counterexample found. Nothing in the sources contradicts the examples.

## Claim B: modal axiom .2 and the horizon problem. Verdict: NOT FOUND (partly known logic side)

- Goldblatt 1980 (Minkowski causal frame: logic S4.2; directedness gives .2):
  confirmed by the van der Schaaf intro snippet (full-text intro) and by the
  arXiv 1507.04903 snippet (discovery). Shehtman/Shapirovsky: the strict "after"
  relation (logic with a different axiomatization, OI.2 in the 1507.04903 summary).
- van der Schaaf 2026 (arXiv:2601.14029) extends to arbitrary smooth spacetimes:
  proves the after modality satisfies the "after formula", shows 2D spacetimes are
  more expressive than higher-dimensional ones, and studies logic along the causal
  ladder. It mentions confluence ("future-directed confluence property for the
  causal relation", line ~1097) and notes spacetimes where it fails. A keyword scan
  found zero occurrences of "horizon" and no "cosmolog", "FLRW", or "big bang".
  So the general-spacetime logic is being studied, and the correspondence between
  directedness and common causal past is standard modal logic; the cosmological
  reading (particle horizon = failure of .2 on the standpoint frame generated by b)
  was not found in what I read.
- Searches ("modal logic" + "particle horizon" / "horizon problem" / FLRW / S4.2)
  returned nothing linking the two (discovery level; web search only, not exhaustive).
- Caveat on their direction: the usual Kripke-frame convention uses the future
  relation x R y iff x <= y (confluence = common future). Our (B) uses the past-
  directed frame. Directedness of the past-generated subframe is the correct
  analogue, but the logic of the future frame and the past frame can differ; say
  which one models "from standpoint b".
- Still to read before claiming novelty: Phillips, Shehtman, Shapirovsky (full
  papers, only snippets seen), Goldblatt 1980 itself (the project already has
  bf00370321.pdf in the repo root; presumably the Goldblatt paper, unchecked here),
  and any cosmology-side literature on "causal convergence" or the horizon problem
  phrased as a lack of a common causal past (standard: Rindler 1956 for horizons;
  the horizon problem is well known as "no common past", so that half is not new).
  The new content would be the identification, not either side. Also (B)'s inflation
  clause is a cosmology claim that belongs to the cited cosmology, not a result; and
  the Borde-Guth-Vilenkin remark was not checked here.

## Claim C: regions real from no standpoint; grounding disagreement. Verdict: partly (epistemic shadow known), the ontological conclusion not found

- Malament 1977 (observational indistinguishability) -- only the closing example
  and notes were seen in the Geroch PDF (the PDF starts with the end of Malament's
  paper: M and M' observationally indistinguishable but only M' admits a global time
  function). Lesourd 2021 (full-text sections 1-2) summarizes Malament's strong/weak
  observational indistinguishability, with de Sitter observer-horizon examples
  (Malament pp. 65-66 per Lesourd), and Manchak's proposition that every non-causally-
  bizarre spacetime has a weakly indistinguishable non-isometric partner.
- Manchak, "Observational indistinguishability and geodesic incompleteness" and
  Manchak-Barrett "Heraclitus-maximal worlds": discovery only. Norton's reading
  (it is an indeterminism of the observable past, not theory-underdetermination)
  appears in the "On under-determination in cosmology" snippet only; not read.
- Beisbart: nothing relevant found by search. Butterfield: mentioned in snippets as
  discussing the epistemic predicament; not read.
- Earman 2008 section 6: per the project's own earlier audit (not re-read here).
- Growing-block/perspectival literature: Correia-Rosenkranz 2018 (relativistic
  growing block logic) surfaced by search; nothing found on regions beyond all
  matter's event horizons being real from no standpoint (discovery-level negative).
- Interpretation: the epistemic side (observers cannot know what lies beyond their
  past) is heavily anticipated; the new move is the standpoint-first versus eternalist
  grounding disagreement over horizon-shadowed regions. Note Manchak's genuine-
  prediction theorem already shows that for ANY observer the unseen parts are not
  fixed by the seen past plus local laws, which is relevant to the "laws may fix the
  shadowed region" caveat in Path 3: domains of dependence from seen data can be
  shrunk by holes, so "laws fix it" is not robust across the observationally
  indistinguishable class.

## Summary of verdicts

| Claim | Verdict | Main priors | Depth |
|---|---|---|---|
| A (Thm 1.1, concept of settled) | partly anticipated: the concept is Geroch's domain of prediction; temporal-function form and dust-FLRW threshold not found | Geroch 1977 pp. 89-91; Manchak 2008; Lesourd 2021 | full-text |
| A (closed-universe link) | anticipated (compact slice needed for verifiable prediction) | Geroch 1977, Earman 1995 (via Geroch), Manchak 2008 Thm | full-text (Earman/Hogarth unread) |
| B | not found at this depth | Goldblatt 1980, Shehtman/Shapirovsky, van der Schaaf 2026 | intro/keyword + discovery |
| C | epistemic shadow anticipated; grounding-disagreement claim not found | Malament 1977, Manchak, Norton, Earman 2008 | partial / discovery |

Next steps: read Earman 1995 (prediction and closed universes chapters), Hogarth 1993,
and Norton on indistinguishability; compute the dust threshold independently; read
the full Shehtman/Shapirovsky papers and Goldblatt before asserting the horizon-problem
correspondence is unreported.
