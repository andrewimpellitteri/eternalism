# Prior-art audit: BST settledness and horizons vs. the four screening claims

28 October 2026, task `prior-art-bst`, OpenCode GLM worker. Scope: whether
Branching Space-Time (BST) sources already contain (X1) the growth failure of a
causal-potential domain under lack of pairwise common futures, (X2) the
historical-potential repair H and its dust+Λ threshold, (X3) the definition of
what is settled/real at a point event via events that can influence its future,
or the minimal-screening-region theorem, and (X4) the claim that a realm
containing that region fixes the future under deterministic evolution while the
causal past does not. This is a prior-art audit; absence of hits is not
novelty. No novelty claim is made.

## Search capability check (required by brief)

- `scholar_search` (MCP): worked on first try, 2026-10-28 (queries: Belnap
  settledness; Müller/Placek; Earman pruning; "settledness"). Used for Crossref
  and OpenAlex verification of DOIs.
- `exa web_search_exa` / `web_fetch_exa` (MCP): worked; used for locating and
  reading full texts. PhilSci-Archive rejects `curl` ("Request Rejected"); the
  same PDFs were read via exa fetch instead.
- `web-search-prime`: not used (quota exhausted until 2026-11-17, per brief;
  not retried). `serpapi_search`: not needed.
- Belnap 1992 was read from the exa cache of a JSTOR scan whose live mirror
  URL (homepages.uc.edu) now returns 404; JSTOR stable URL in sources.jsonl.

## Sources read

All named sources were located and read full-text except as marked. Read depth
labels follow the knowledge-base contract.

| Source | Locator basis | Read depth |
|---|---|---|
| Belnap 1992, Synthese 92(3): 385–434, DOI 10.1007/BF00414289 | JSTOR scan, printed page headers | full-text (OCR-noisy scan) |
| Belnap, Müller, Placek 2022, *Branching Space-Times*, OUP, DOI 10.1093/oso/9780190884314.001.0001 | KOPS OA PDF, 456 pp., printed page = PDF − 15 | full-text (chs. 1–3, 9, 10 targeted) + whole-book keyword scan |
| Earman 2008, in *The Ontology of Spacetime II*, ch. 10, pp. 187–205, DOI 10.1016/S1871-1774(08)00010-7 | author PDF (sites.pitt.edu), 19 pp. | full-text |
| Placek & Belnap 2012, Synthese 187(2): 441–469, DOI 10.1007/s11229-010-9846-8 | PhilSci preprint v. 2011-02-01 | full-text (preprint pagination) |
| Müller & Placek 2018, BJPS 69(1): 215–252, DOI 10.1093/bjps/axv049 | PhilSci accepted-version preprint | full-text (preprint) |
| Placek 2014, "Branching for general relativists", in Müller (ed.), *Nuel Belnap on Indeterminism and Free Action*, Springer | PhilSci preprint 2013 | full-text (preprint) |
| Müller 2013, Phil. Sci., DOI 10.1086/673895 | OpenAlex abstract | discovery |
| Dorato & Hoefer 2021, Disputatio, DOI 10.2478/disp-2021-0025 | sibling lane's full-text record | discovery (here) |

## Verdict table (X1–X4 per source)

FOUND = the claim, or an immediate corollary, is stated. PARTIAL = an
ingredient or a weaker overlapping statement is present. NOT-FOUND = nothing
overlapping found at the stated read depth.

| Source | X1 (growth failure without common futures) | X2 (historical repair H, threshold) | X3 (influence-based settledness / minimal screening realm) | X4 (realm fixes future under determinism, causal past does not) |
|---|---|---|---|---|
| Belnap 1992 | PARTIAL | NOT-FOUND | PARTIAL | NOT-FOUND |
| BMP 2022 | PARTIAL | NOT-FOUND | PARTIAL | PARTIAL (premise only) |
| Earman 2008 | NOT-FOUND | NOT-FOUND | NOT-FOUND (one adjacent remark) | NOT-FOUND (standard IVP remark only) |
| Placek & Belnap 2012 | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Müller & Placek 2018 | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND (adjacent definitions) |
| Placek 2014 | PARTIAL | NOT-FOUND | NOT-FOUND | NOT-FOUND |

No source states any of X1–X4 as such. The PARTIAL entries are ingredient-level
overlaps, quoted below.

## Quotes and locators

### Belnap 1992 (full-text, OCR-noisy; repaired readings marked)

X1 ingredient — the horizon caveat, printed p. 395, third of three
"substantive commitments" following Definition 7 (compatibility):

> "(3) If there are 'event horizons' such as are postulated near black holes,
> then it would appear that there can be compatible point events without a
> common causal future as required by the definitions. I ask that such
> difficult physical questions be tabled in the belief that the present theory
> can nevertheless serve as a useful approach."

[OCR repair: scan reads "as such are postulated" and scrambles the last
sentence's word order; sense confirmed against context. Definition 7, p. 394:
point events are compatible iff they share a history, and two points share a
history iff they have a common upper bound in Our World.]

X3 ingredient — elsewhere events are treated modally, not causally.
Definition 11, printed p. 397 (OCR repaired):

> "If e1 and e2 are (i) incomparable by ≤ but (ii) compatible, then they are
> space-like separated. We may also call them causal contemporaries (provided
> we bear in mind the failure of transitivity)."

The "wings" problem, printed p. 400:

> "The status of the areas — the 'wings' — indicated by the question marks —
> appears not to be settled by stipulations to date. Some of the literature
> treated by Stein (1991) asks whether events in the wings are 'ontologically
> definite or indefinite', either absolutely or relatively."

Resolution by the Prior Choice Principle, Fact 31, printed pp. 411–412 (OCR
repair of "hx D h2" to h1 ∩ h2):

> "In the presence of the prior choice principle, however, it must be that the
> 'wings' are in the intersection h1 ∩ h2 of the two histories."

So BST's answer to "what is real/settled at a point event" is modal: all
compatible elsewhere events belong to every history through the event. No
definition via influence on the event's future, no screening region, no Cauchy
slices anywhere in the paper (keyword checks: "potential" 0 relevant hits,
"horizon" only in the p. 395 caveat, "Cauchy" 0).

### BMP 2022 (full-text; clean extraction; printed page = KOPS PDF − 15)

X1 ingredients — the "later witness" (common causal future) criterion and its
acknowledged GR failures. Ch. 1, pp. 10–11:

> "We follow what we call the later witness intuition, according to which two
> events are compatible only if they belong to the past of some really
> possible event."

Ch. 2, p. 28:

> "…it is easy to construct a truncated Minkowski space-time, or a more
> sophisticated space-time of general relativity, which violates this
> implication (cf. Müller, 2014). Nevertheless, we assume here the
> strengthened intuition of a later witness in the form of an equivalence:
> 'two point events have a common later point event iff they share a
> history'." (their footnote 5: the one-way alternative is Placek 2011)

Fact 9.14, §9.3, p. 316:

> "Let ⟨M,g⟩ be a GR space-time that is (1) time-orientable, (2) without
> closed causal curves, and (3) subject to the condition that for any x,y ∈ M
> there is z ∈ M that is reachable from x and from y by future-directed causal
> curves. Then ⟨M,g⟩ induces a one-history BSTNF structure W = ⟨M,<⟩ …"
> (proof sketch: "M is directed by (3), so it is a single BST history.")

Whole-book keyword scan (456 pp.): "horizon" 0, "de Sitter" 0, "black hole" 0,
"causal potential" 0, "growth" 0, "MGHD" 0, "Correia" 0, "Rosenkranz" 0.
"Settled" (38 hits) is uniformly modal: e.g. Def. 10.1 desideratum D4, p. 354:
"Past(e) is settled in the modal sense that if a possible scenario includes e,
it also includes Past(e)."

X3 ingredients — elsewhere events again get a modal treatment, and causal
reach is explicitly allowed to fail across space. Ch. 3.4.2–3.4.3, pp. 54–56
(Fig. 3.2 "'Wings' ('elsewhere') belong to the intersection"):

> "…the difference made by the choice at c pertains only to the future of
> possibilities of c. It does not pertain to the causal contemporaries of c."

§10.5, p. 362 (dynamic time via causae causantes):

> "…so-called elsewhere (i.e., a portion of the events SLR to it), will be
> neither dynamically past, nor present, nor future. In terms of causae
> causantes, the reach of causation in such structures does not extend far
> enough across space to allow one to classify these events one way or
> another."

This is the closest BST-side statement to "bow-tie surplus events are causally
idle": the causae causantes construction leaves elsewhere events unclassified
because causal reach does not span them. It is not a screening/minimality
theorem, mentions no Cauchy slices, and does not define an existence domain.

X4 premise — the determinism side is present as standard GR. §9.3.1,
Theorem 9.2, pp. 319–320 (Choquet-Bruhat–Geroch):

> "Let ⟨Σ, g̃, k̃⟩ be an initial vacuum data set. Then there is a unique, up
> to isometry, maximal VCD ⟨M,g⟩ of ⟨Σ, g̃, k̃⟩."

and p. 320 quotes Ringström 2009, p. 188: "for generic initial data to
Einstein's equations, the maximal globally hyperbolic development has no
extension" — the same monograph our SCREENING.md names as a lead for premise
(L). §9.3.5, p. 330, states global determinism as:

> "…a theory is deterministic iff whenever two models of the theory agree on
> initial segments, they agree as wholes."

The conditioning region is always a whole initial segment / Cauchy data set.
No statement that a proper sub-slice realm (causal-potential realm or any
realm containing it) fixes the future, and none that the causal past fails to.
"The known non-trivial cases of indeterminism in GR are global, not local"
(§9.3.7, p. 339).

### Earman 2008 (full-text, author PDF, printed pp. 187–205)

X1/X2/X3: nothing on horizons, de Sitter, causal potential, or
influence-based settledness. The two adjacent remarks:

- p. 191, on Broad's growing block: "…I think it should be [rejected] since it
  is difficult if not impossible to reconcile it with the relativistic
  conception of spacetime…" — asserted without any horizon-based argument.
- p. 192, footnote 12 (X3-adjacent picture of influence):
  "…members of the Belnap school speak of 'choice points,' which are to be
  thought of as the loci of indeterministic influences that radiate outwards
  along or within the future null cones of these loci. On this way of
  conceptualizing indeterminism, the members of the ensemble of physically
  possible models will typically agree at all points except those that lie on
  or inside the future null cones of the choice points. I know of no theory in
  modern physics which will produce this kind of indeterminism."

X4: only the standard IVP determinism remark, p. 201: "the basic theorem on
the initial value formulation of Einstein's field equations shows that
corresponding to appropriate initial data on a three manifold …, there exits
[sic] a unique (up to diffeomorphism) maximal solution for which the initial
value hypersurface is a Cauchy surface (see Theorem 10.2.2 of Wald (1994))."

### Placek & Belnap 2012 (full-text, PhilSci preprint v. 2011-02-01)

X3-adjacent phrase, preprint p. 8 (§2.1): "Our World, denoted by OW, is the
totality of point events, partially ordered by a causal-temporal ordering ≤,
with the ordering e ≤ e′ understood as 'e′ is in a possible future of e' and,
equivalently, 'e is in the (settled) causal past of e′'." Settledness of the
past is the causal order itself — the opposite pole from our D_pot-based X3,
and again no screening region. Keyword check over the whole text: "horizon"
0 hits. The GR gap is explicit, preprint p. 40 (§6 Final):

> "An open task looms large: construct BST-like models that take into account
> the fundamental ideas of GR."

### Müller & Placek 2018 (full-text, PhilSci accepted-version preprint)

Determinism via branching, §4 (DBRN): "a system is assessed as indeterministic
iff some initial segment of its evolution can be continued in more than one
alternative way." GR section: globally hyperbolic spacetimes, Cauchy surfaces,
and the Choquet-Bruhat–Geroch uniqueness of the maximal vacuum Cauchy
development are quoted as the starting point of the determinism/IVP question.
Keyword checks: "horizon" 0, "de Sitter" 0, "settled" 0. No causal-potential
realm, no sub-slice fixing claim.

### Placek 2014 (full-text, PhilSci preprint, §1, preprint p. 3)

X1 ingredient, with de Sitter named:

> "…the BST1992 criterion for historicity (or, belonging to one BST
> spacetime), i.e., being maximally upward directed, flies in the face of some
> well-studied GR spacetimes, like the Schwarzschild spacetime or the de Sitter
> cosmological model. The criterion rules out as well some intuitive, although
> non-physical, candidates for a spacetime since it implies that for two
> events x and y to belong to some one spacetime, there should be a 'later
> witness', that is, some z such that x ≤ z and y ≤ z."

The paper's response is to generalize the historicity criterion (choice pairs,
generalized manifolds), not to derive any existence-domain or growth
consequence. Keyword check: "horizon" 0 hits.

## Answers to the focus questions

1. Does BST define what is settled/real at a point event via the events that
   can influence its future (X3)? **No.** Settledness in BST is modal
   (true in all histories through the event); the status of elsewhere events is
   settled by the Prior Choice Principle (wings in the intersection: Belnap
   1992 pp. 400, 410–412; BMP pp. 54–56). The causal-influence notion exists
   only as *causae causantes* (causes of transitions into an event), used for
   co-presentness in BMP ch. 6 and ch. 10, with the explicit remark that causal
   reach may not extend across space (BMP p. 362). No minimal screening
   region, no Cauchy-slice characterization, no "causally idle surplus" claim
   exists in the sources read.
2. Do BST sources discuss horizons (X1/X2)? **Only glancingly.** Belnap 1992
   p. 395 tables event horizons as a threat to the common-causal-future
   requirement of his definitions; Placek 2014 names Schwarzschild and de
   Sitter as failing the BST92 historicity criterion and generalizes the
   criterion. BMP 2022 (2022, post-*Nothing to Come*) contains zero occurrences
   of horizon, de Sitter, growth, causal potential, or Correia/Rosenkranz. No
   source connects horizons to a growth axiom (P1R), to an existence domain, to
   a ΛCDM threshold (X2), or to a determinism-fixing realm (X4).

## Strongest contrary evidence (against treating X1–X4 as unanticipated)

- BST already contains, in its own vocabulary, exactly the pairwise-common-
  future ingredient of X1, with GR failures acknowledged in print: BMP p. 28
  (GR spacetimes violating the later-witness implication), Fact 9.14 p. 316
  (directedness yields a one-history structure), Placek 2014 p. 3 (de Sitter,
  Schwarzschild). Anyone claiming X1's ingredient as new must position it
  against these.
- The BST wings/intersection answer (elsewhere events real in every compatible
  history) is a rival, worked-out treatment of "what is real at a point event"
  that includes *all* spacelike events — i.e., closer to the bow-tie domain
  than to D_pot — and must be engaged by X3, even though it is modal rather
  than causal.
- BMP §9.3 already connects GR determinism to MGHD uniqueness (Theorem 9.2)
  and quotes Ringström on generic inextendibility of the maximal globally
  hyperbolic development — the same anchors our X4 uses — so X4's premise
  cannot be presented as new; only the realm-level claim could be.
- Earman 2008 p. 191 already asserts (without horizons) that a growing block
  is "difficult if not impossible to reconcile" with relativity; horizon-based
  arguments must be shown to add something to this debate.

## Coverage, negative results, and their limits

- Whole-book keyword scans (BMP 2022) and whole-text keyword checks (Belnap
  1992, Placek-Belnap 2012, Müller-Placek 2018, Placek 2014) are reported with
  counts above; they bound the vocabulary, not the ideas — a discussion using
  different words would be missed.
- exa searches for horizon discussions in the relativistic growing-block /
  RGBT literature returned no horizon-based analysis of growth axioms (search
  terms: growing block + event horizon / de Sitter / spacelike existence;
  Nothing to Come reviews). The horizons lane's PRIOR_WORK_CHECK had already
  flagged the physics-side material (Rindler etc.) as standard.
- Not read here: Earman 1995, Hogarth 1993 (covered by the horizons lane as
  unread leads), Müller 2013 full text, Müller 2011, Placek 2011, Müller 2014
  (cited by BMP for GR violations of the later-witness implication — worth a
  follow-up), Nothing to Come itself (owned by the bowtie-horizons lane).

## Limitations

- Belnap 1992 was read from an OCR-scanned JSTOR copy via the exa cache;
  quotations from it are repaired readings, marked as such. The live mirror
  URL is dead (recorded in sources.jsonl).
- Two sources were read in PhilSci preprint versions; published pagination was
  not verified (Synthese 187(2) for Placek-Belnap; BJPS 69(1) and the Springer
  volume for Müller-Placek 2018 and Placek 2014).
- BMP close reading was limited to the sections quoted; the rest of the book
  is covered only by the keyword scan (counts reported).
- exa text extraction of PDFs preserves text but not always layout; section
  headings for one Müller-Placek 2018 passage are only partially pinned.

## Proposed next tasks

1. Read Müller 2014 (cited by BMP p. 28 for GR counterexamples to the
   later-witness implication) and Müller 2011 / Placek 2011 (the generalized
   historicity criteria), then map them against Proposition 7 of
   research/bowtie-horizons/RESULT.md.
2. A short companion audit: Stein 1968/1991 definite-at-a-point and the
   Malament–Stein literature, against X3/X4 (the causal past as the settled
   region), which this BST-focused pass only touched via Belnap's citations.
3. Check whether any post-2022 review of Correia & Rosenkranz raises horizons
   (an NDPR review exists, ndpr.nd.edu, located but not read here).
4. If X1's wording is kept, cite Belnap 1992 p. 395 and Placek 2014 p. 3 as
   named prior art for the ingredient, and BMP Fact 9.14 as the one-history
   consequence, in the claim contract.
