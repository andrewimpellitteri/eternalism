# Prior-art audit: relativistic becoming vs horizon and causal-potential claims

28 October 2026, task `prior-art-becoming` (GLM worker). Audit of the named
relativistic-becoming sources against the four candidate claims X1–X4 of
`research/bowtie-horizons/SCREENING.md` and `RESULT.md`:

- **X1** the instantaneous causal-potential domain violates growth (P1R) in
  every connected causally simple spacetime lacking pairwise common futures
  (de Sitter, ΛCDM);
- **X2** the historical-potential repair H misses spacelike events in exact
  dust+Λ (threshold d < R_x + R_s + 2P_s);
- **X3** the causal-potential realm J⁻(J⁺(b)) \ (J⁺(b)\{b}) is exactly the
  minimal region screening b's future on every Cauchy slice avoiding it, so
  bow-tie surplus events are causally idle;
- **X4** under deterministic MGHD evolution any realm containing that region
  fixes b's future, while the causal past does not.

Focus per brief: cosmological/event horizons in relativistic becoming (X1/X2)
and influence-based existence criteria (X3). **No novelty claim is made.
Absence of hits in this small, targeted search is not evidence of absence in
the literature.** Verdicts: FOUND / PARTIAL / NOT-FOUND, judged on whether a
source contains the specific claim content (mathematical statement, criterion,
or explicit consequence), not merely an adjacent theme.

## Search capability check

- `scholar_search` (openalex + crossref): **worked**; used for bibliographic
  identification (crossref rate-limited twice, HTTP 429; recovered via direct
  Crossref REST queries).
- `web-search-prime`: **not retried** per brief (quota exhausted until
  2026-11-17).
- `exa web_search_exa` / `web_fetch_exa`: **worked** for search and for PDF /
  ar5iv full-text extraction. Failures recorded: arXiv PDF `gr-qc/0605049`
  failed extraction at `/pdf` and legacy paths (succeeded only at the old
  `arxiv.org/vc/.../0605049v3.pdf` URL); `philpapers.org/archive/STEOES.pdf`
  is a **mis-filed student essay, not Stein 1968**; `philsci.org/docs/*.pdf`
  (Savitt 2000 manuscript) timed out in the crawler three times.
- `serpapi`: **quota exhausted** mid-task ("Your account has run out of
  searches"); not available as fallback.

## Named-source coverage

| Source | Locator | Access | Read depth |
|---|---|---|---|
| Stein 1968 | "On Einstein–Minkowski Space–Time", J. Phil. 65(1): 5–23, DOI 10.2307/2024512 | paywalled (JSTOR/pdcnet); PhilArchive copy corrupted | **discovery** (metadata only; content known only via secondary statements) |
| Stein 1991 | "On Relativity Theory and Openness of the Future", Phil. Sci. 58(2): 147–167, DOI 10.1086/289609 | JSTOR scan, strangebeautiful.com/other-texts/stein-rel-open-fut.pdf | **full-text** (noisy OCR; line-break hyphens removed in quotes) |
| Clifton–Hogarth 1995 | "The definability of objective becoming in Minkowski spacetime", Synthese 103(3): 355–387, DOI 10.1007/BF01089733 | authors' abstract (Springer); full text paywalled; both theorems read via Savitt 2020's statement (C&H pp. 365, 371–72) | **abstract** (authors' abstract verbatim; theorems at secondary depth) |
| Dieks 1988 | "Discussion: Special Relativity and the Flow of Time", Phil. Sci. 55(3): 456–460, DOI 10.1086/289452 | authors' abstract (Cambridge/OpenAlex); full text paywalled | **abstract** |
| Dieks 2006 | "Becoming, Relativity and Locality", in The Ontology of Spacetime (Phil. & Found. of Physics 1), Elsevier, ch. 8, pp. 157–176, DOI 10.1016/S1871-1774(06)01008-4 | PhilSci-Archive preprint 2533 (Dec 2005), philsci-archive.pitt.edu/2533/1/becoming.pdf | **full-text** (preprint; published chapter not compared) |
| Arthur 2006 | "Minkowski Spacetime and the Dimensions of the Present", same volume, ch. 7, pp. 129–155, DOI 10.1016/S1871-1774(06)01007-2 | author PDF, humanities.mcmaster.ca/~rarthur/papers/Mink.pres.final.pdf (states "Published as pp. 129–155") | **full-text** |
| Arthur 2019 | The Reality of Time Flow: Local Becoming in Modern Physics, Springer, Frontiers Collection, DOI 10.1007/978-3-030-15948-1; ch. 7 "Time in General Relativity", pp. 179–217, DOI 10.1007/978-3-030-15948-1_7 | chapter abstract only (Springer) | **abstract**; full text gated |
| Savitt 2000 | "There's No Time Like the Present (in Minkowski Spacetime)", Phil. Sci. 67(S3): S563–S574, DOI 10.1086/392846 | abstract (PhilSci/Cambridge); PSA'98 manuscript located at philsci.org/docs/savitt.pdf but crawler timed out ×3 | **abstract**; access gate recorded |
| Savitt 2009 | "The Transient Nows", in Myrvold & Christian (eds.), Quantum Reality, Relativistic Causality, and Closing the Epistemic Circle, Springer (Western Ontario Series), pp. 349–362, DOI 10.1007/978-1-4020-9107-0_18 | PIRSA 2006 talk abstract (pirsa.org/06070042); slides PDF did not extract; SEP describes its content | **abstract**; full chapter gated |
| Ellis 2006 | "Physics in the real universe: time and spacetime", Gen. Rel. Grav. 38(12): 1797–1824, DOI 10.1007/s10714-006-0332-z | arXiv:gr-qc/0605049 **v3** (arxiv.org/vc/gr-qc/papers/0605/0605049v3.pdf); v5 is a "Major revision", 28 pp., not compared | **full-text** (v3) |
| Ellis 2014 | "The evolving block universe and the meshing together of times", Ann. N.Y. Acad. Sci. 1326(1): 26–41, DOI 10.1111/nyas.12559 | arXiv:1407.7243 (full text) | **full-text** (arXiv version) |
| Ellis–Rothman 2010 | "Time and Spacetime: The Crystallizing Block Universe", Int. J. Theor. Phys. 49(5): 988–1003, DOI 10.1007/s10773-010-0278-5 | arXiv:0912.0808v2 (full text) | **full-text** (v2) |
| Rovelli 2019 | "Neither Presentism nor Eternalism", Found. Phys. 49: 1325–1339, DOI 10.1007/s10701-019-00312-9 | arXiv:1910.02474 via ar5iv (render stamp 2024-03-07; published pagination not checked) | **full-text** |

Additional sources read for the claim focus (not named in the brief):
Savitt 2020 "Chronogeometrical Determinism and the Local Present" (Zeta Books,
pp. 143–180, DOI 10.5840/zeta-time20207; PhilSci 8481 preprint, **full-text**);
Savitt, SEP "Being and Becoming in Modern Physics" (current version,
**full-text keyword-scanned**); Ben-Yami 2019 (abstract); Dorato 2010
(PhilSci 5096, **full-text targeted scan**); Romero–Pérez 2014 (abstract);
Riggs 2024 (discovery). Leads not read: Callender–Wüthrich 2016 (causal-set
becoming); Muller 1992 "Worldlines are Growing!" (C&H's refuted proposal);
Davis–Lineweaver 2004 (horizons physics).

## Verdict table (X1–X4 per source)

Legend: FOUND / PARTIAL / NOT-FOUND. "—" = source not read at any depth
beyond the stated one; the verdict reflects the depth read, not a thorough
negative.

| Source | Depth | X1 | X2 | X3 | X4 |
|---|---|---|---|---|---|
| Stein 1968 | discovery | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Stein 1991 | full-text | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Clifton–Hogarth 1995 | abstract (+thms via Savitt 2020) | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Dieks 1988 | abstract | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Dieks 2006 | full-text (preprint) | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Arthur 2006 | full-text | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Arthur 2019 | abstract | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Savitt 2000 | abstract | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Savitt 2009 | abstract | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Ellis 2006 | full-text (v3) | NOT-FOUND | NOT-FOUND | PARTIAL | PARTIAL |
| Ellis 2014 | full-text (arXiv) | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Ellis–Rothman 2010 | full-text (v2) | NOT-FOUND | NOT-FOUND | NOT-FOUND | PARTIAL |
| Rovelli 2019 | full-text (ar5iv) | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| Savitt 2020 (extra) | full-text | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |
| SEP survey (extra) | full-text scan | NOT-FOUND | NOT-FOUND | NOT-FOUND | NOT-FOUND |

**No named source contains any of X1–X4.** The two PARTIAL cells are
influence/determinism background statements quoted below; neither contains the
realm constructions, thresholds, or minimality/screening claims.

## X1 — instantaneous causal-potential domain violates growth (P1R)

**NOT-FOUND.** No source read connects event or cosmological horizons to a
becoming-domain growth condition, or states any non-monotonicity of an
existence/becoming domain under advancement along a worldline.

- Stein 1991 (the definitional anchor) makes the domain **monotone by
  construction** through an influence premise, in Minkowski spacetime only.
  His stated principle (p. 149): the Einstein–Minkowski structure "depends
  critically upon the principle that the state at any point a is subject to
  influence by the states at all points in the 'causal past' of a; …
  Therefore the states at all such points should be supposed definite as of a;
  in other words, Rab must hold whenever the vector ab is past-pointing."
  His theorem (pp. 149–150, as printed): if R is reflexive and transitive,
  invariant under time-orientation-preserving automorphisms, and holds for
  some past-pointing (timelike **or null**) nonzero pair, "then for any pair
  of points (x,y), Rxy holds if and only if xy is a past-pointing vector."
  (Reflexivity at x=y is condition (iii) on p. 148; the zero vector is not
  itself past-pointing.) No curved spacetime, no growth axiom, no horizons.
  His only GR remark (p. 160): "there are cosmological solutions that do, and
  others that do not, have such systems of hypersurfaces" — context:
  Maxwell's quantum-probabilism proposal, not becoming domains.
- Clifton–Hogarth 1995 (authors' abstract, Springer): extend Stein's
  uniqueness to worldline-dependent becoming; "we show that Stein's
  uniqueness proof can be extended in a natural way to cover this more
  general kind of becoming, provided one does not enrich standard Minkowski
  spacetime by privileging certain sets of worldlines over others in an
  unwarranted manner." Their theorems (as stated in Savitt 2020, pp. 365,
  371–72) admit only "past chronological connectibility, or … past causal
  connectibility, or the universal relation" — i.e. the pointy causal past is
  the sole nontrivial definable option, **in Minkowski spacetime**. No
  horizons, no curved spacetimes, no (P1R).
- Ellis 2006 §3.3 and Ellis 2014 grow the block **along worldlines** by
  proper time; Ellis 2014 (arXiv abstract): the EBU is "bounded to the future
  by the present time … This future boundary is defined at each time by
  measuring proper time along Ricci eigenlines from the start of the
  universe." No monotonicity axiom, no horizon discussion (zero "horizon"
  occurrences in Ellis 2014 and Ellis–Rothman 2010 full texts; Ellis 2006 has
  one, "Cauchy horizon", in a determinism remark, quoted under X4).
- Rovelli 2019: zero occurrences of "horizon"; treats the elsewhere as real
  relative to suitably located events (§V, quoted under X3). No growth
  condition. The SEP survey (current) also has zero "horizon" occurrences.

## X2 — historical-potential repair H misses spacelike events (dust+Λ threshold)

**NOT-FOUND.** No source read defines any historical/persistent enlargement
of an instantaneous becoming domain, and none states a distance threshold
beyond which spacelike events are excluded from existence-at-b. The H
construction (⋃_{r≤s} D_pot(r)) and the threshold d < R_x + R_s + 2P_s are
absent from the literature read. Nearest contrasts:

- Ellis 2014: growth "takes place along preferred timelike world lines";
  the block's future boundary is proper-time-based, and no discussion of
  spacelike regions the boundary never reaches (0 "horizon" hits).
- Ellis 2006 §3.5 ("The Far Future Universe"): the final block contains
  everything that ever happens — "The moving finger has ceased writing; all
  that will ever be written has been written" — with no exclusion of any
  spacelike-separated region.
- Ellis–Rothman 2010: crystallization "incorporates ever more events"; no
  horizon discussion.

## X3 — causal-potential realm = minimal screening region; bow-tie surplus idle

**NOT-FOUND** as a claim; **the family of influence-based existence/simultaneity
criteria is well occupied** — this is the strongest adjacent prior art:

- Stein 1991 p. 149: definite-as-of-a is grounded in past influence ("Rab
  must hold whenever the vector ab is past-pointing") — influence-received,
  past-directed; the realm is J⁻(a), not J⁻(J⁺(b))\J⁺(b).
- Stein 1991 (specious-present passage): "let us call an event e
  'contemporaneous' with ir if signals-interaction-influence-can occur
  mutually between e and ir" — mutual-influence simultaneity.
- Ellis 2006 §3.1 (Newtonian case): "The existential nature of the present is
  indeed unlike that of the past or future, for it is the set events that we
  can (according to Newtonian theory) actually influence at any instant in
  our history." An explicit influence-based existence criterion — but
  Newtonian, present-instant-sized, and **not carried over** into his SR/GR
  sections (§§3.2–3.3 shift to worldline-based growth). No minimal-realm or
  screening result anywhere.
- Ben-Yami 2019 (abstract): "What is simultaneous with an event is what can
  interact with it." Rovelli 2019 §IV.1 adopts the "diamond present" from
  Ben-Yami: "P ∈ D_E if and only if there are a P₋ ∈ E which is in the past
  of P and a P₊ ∈ E which is in the future of P", with the figure caption
  "Two simultaneous extended events: each can send and receive message from
  the other." Future cones enter, but for the simultaneity of **extended**
  events, with no fixed-point/b or screening claim.
- Savitt 2009 (via SEP, current entry): with Arthur 2006, "the present for a
  stretch of worldline or process of length T would be the region of spacetime
  comprised of the intersection of the future light cone of the point at the
  beginning of that process and the past light cone of the point at the end of
  it … often called a causal diamond." Arthur 2006 (abstract) states the same
  proposal: "that region of spacetime comprised between the forward lightcone
  of the beginning of a small interval of proper time t … and the backward
  lightcone of the end of that interval."
- Savitt 2020 (specious present): "The events that can influence events in π
  are just the events in the past light cones of events in π. The set
  containing all events that can act upon any event in π must be the past
  light cone of the latest event in π, I⁻(b)."
- Nobody read identifies J⁻(J⁺(b))\J⁺(b), proves minimality under screening
  on Cauchy slices, or concludes that bow-tie surplus events are causally
  idle. Rovelli's stance is opposite in spirit: "there are also facts that
  are real on distant galaxy at a time which is neither in our future, nor in
  our past, but nevertheless they are in the past of one another" (§V), i.e.
  elsewhere facts are real from other standpoints without needing a
  causal-role at b.

## X4 — realm containing the potential region fixes b's future; causal past does not

**NOT-FOUND** as a claim in the becoming literature. Two adjacent background
statements:

- **PARTIAL, Ellis 2006** (deterministic frame only). §1: for suitable
  matter, "initial data at an arbitrary time determines all physical
  evolution, including that of the spacetime structure, to the past and the
  future equally, because we can predict and retrodict from that data up to
  the Cauchy horizon" (citing Hawking–Ellis 1973: 226–255; Wald 1984:
  252–267). This is standard surface-based determinism (the frame in which
  premise (L) lives), with the Cauchy-horizon limitation named — but no
  realm-version, no J⁻(b)-does-not-fix contrast. §3.3 adds the quantum/
  complex-system caveat: "You cannot locally predict uniquely to either the
  future or the past from data on any 'time' surface (even though the past is
  already determined)."
- **PARTIAL, Ellis–Rothman 2010** (opposite premise). §3: "This ensures that
  there is no way the future spacetime can be predicted from the past: what
  will actually happen is not determined until it happens." They assert the
  past-does-not-fix-future half, but from irreducible quantum indeterminism,
  not from deterministic underdetermination by the causal past; the
  realm-containing half of X4 is absent.
- Stein 1991's probabilism debate and Dieks 1988's relativized probabilism
  concern whether SR constrains indeterminism, not which region fixes what:
  Dieks 1988 (abstract): "there is a straightforward relativistic
  generalization, and that therefore Maxwell's conclusion that the special
  theory of relativity should be amended is unwarranted … the special theory
  of relativity has no fundamental significance for this question."
- The genuine nearby prior art is in the **prediction** literature, already
  recorded by this project at full-text depth in
  `research/horizons/PRIOR_WORK_CHECK.md` (Geroch 1977 pp. 89–91 domain of
  prediction; Manchak 2008; Lesourd 2021) — not re-verified by this task. X4's
  "causal past does not fix the future" is Geroch's P(q)-smallness; "realm
  containing the potential region fixes J⁺(b)" was not found there either,
  per that check.

## Strongest contrary evidence / near misses

1. Influence-based criteria family (Stein 1991; Ellis 2006 §3.1; Ben-Yami
   2019; Rovelli 2019 diamond; Arthur 2006/Savitt 2009 diamonds; Savitt 2020).
   The *idea* "existence = causal role" is standard; every instance read is
   either past-directed or mutual-interaction for extended events. The X3
   construction differs by aiming existence-at-b at **b's future** and by
   claiming exactness/minimality.
2. Ellis's EBU/CBU growth is a rival ontology with a different boundary rule
   (proper time along Ricci eigenlines / worldline crystallization). Neither
   2006 nor 2010 nor 2014 discusses horizons restricting the block, so they do
   not preempt X1/X2, but a reviewer should check Ellis–Drossel 2020
   "Emergence of Time" and Riggs 2024 (critique of how the present/passage is
   defined) before claiming any gap.
3. Muller 1992 "Worldlines are Growing!" (preprint, cited and refuted by C&H
   1995) and Peacock 1992 propose worldline-dependent becomings that C&H
   eliminate in Minkowski spacetime — unread; potential prior art for
   growth/realm variants in SR.
4. Causal-set becoming (Rideout–Sorkin growth dynamics; Callender–Wüthrich
   2016 "What Becomes of a Causal Set?") treats covariant growth — unread
   here; flagged as the family most likely to contain growth-monotonicity
   discussions adjacent to X1.

## Limits

- Stein 1968, Savitt 2000, Savitt 2009, Arthur 2019, Clifton–Hogarth 1995 and
  Dieks 1988 were **not read at full-text depth** (paywalls and crawler
  failures; details in the coverage table). All verdicts for these rest on
  abstracts or on secondary statements, each labeled.
- Version caveats: Dieks 2006 read as the December 2005 PhilSci preprint;
  Ellis 2006 as arXiv v3 (v5 "Major revision" not compared); Ellis 2014 as
  arXiv:1407.7243 (NYAS published version not compared); Rovelli 2019 via
  ar5iv render of arXiv:1910.02474 (render stamp 2024-03-07); Stein 1991 from
  a JSTOR scan with OCR noise.
- The search was bounded (named sources + one focused ring of extras). No
  exhaustive search of growing-block critiques, causal-set growth dynamics,
  Muller/Peacock 1992, or Ellis–Drossel 2020 was performed.
- Quotes preserve the fetched text; line-break hyphenation from OCR scans was
  removed; "[sic]"-level quirks (e.g. "the set events" in Ellis 2006) are
  reproduced as extracted.

## Falsifiers for this audit

(i) Any becoming source stating a non-monotone becoming/existence domain in a
horizon spacetime, or a growth axiom refuted by horizons (defeats X1's
NOT-FOUND). (ii) Any historical/persistent enlargement of a becoming domain
with a distance threshold (defeats X2's NOT-FOUND). (iii) Any identification
of J⁻(J⁺(b))\J⁺(b), or of "can causally reach b's future" as an
existence/screening criterion (defeats X3's NOT-FOUND). (iv) Any statement
that a sub-Cauchy realm fixes J⁺(b) while J⁻(b) does not, in becoming or
prediction literature (defeats X4's NOT-FOUND).
