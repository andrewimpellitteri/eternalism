# Defeat search RC-3, and full-text reads for RC-2 / candidate C (Czerniawski; Clifton-Hogarth unread)

Status: 2026-10-19. Independent Claude-subagent passes. Quotes and equation locators are as
reported by the subagents from their own text extractions and were not re-read by the
coordinator. Not novelty claims.

## RC-3 sector-coherent conditioning: partly occupied

Read in full text (arXiv HTML, keyword-matched passages and Secs. III-VI): Hoehn, Smith, Lock
2007.00580. Reported: "such coherence is not physically accessible because it does not affect
the expectation value of any relational Dirac observable on account of the decomposition in
Eq. (33). In other words, superpositions and classical mixtures across the sigma-frequency
sectors are indistinguishable. Hence, superpositions of physical states across sigma-sectors
are mixed states and the pure physical states are those of either H+ or H-." Sector
normalization 1/2 appears in Eqs. 39, 47, 62. The paper also says a map conditioning only on
tau (not sigma) is not invertible, a consequence of the superselection rule, and that such
rules are often interpreted as lack of a reference frame and "can be lifted" with an
appropriate frame (sentence cut off in the extraction). Correction to the RC-3 text: Sec. VI
(relativistic localization, Kuchar) says only that conditioning on the non-covariant Minkowski
time projector gives a Klein-Gordon amplitude (Eq. 61) that does not separate frequencies,
so the denominator is not conserved if both appear; the superselection statement is near
Eq. (33) and footnote 13 (section number inferred from text offsets).

Closest follow-up: Hosseini and Lock, "The time of arrival problem in the Page-Wootters
formalism", arXiv 2604.00092 (v1, 31 Mar 2026): expectation values are "insensitive to
coherence between sigma = +/-"; the plain reduction map "coherently combines the different
superselection sectors"; the resulting clock state "cannot be normalised in a state-
independent manner"; fix by sector-wise partial-isometry reduction maps. Setting: free
particle, position conditioning, not the relativistic clock C_H = s p_t^2/2 + H_S.
Appendices not read closely.

Other reads (keyword level): 2101.11628 (positive-energy branch only), 2212.14081 (no sector
treatment), 2409.06479 (left/right-mover sectors only as a direct sum), 2509.22264 (remark
that mixing frequencies may conflict with charge superselection). The RC-3 contract's
"Delta" line ("no recorded source states ... the no-go") is wrong as written: the Dirac-
observable inaccessibility statement is already in 2007.00580 in prose, and falsifiers (ii)
and (iii) are partly met. Not found: an explicit normalized conditioning rule for a sector-
coherent clock preparation distinct from the sector-mixed rule, a derived cross-sector
interference term, or its measurability condition.

Narrowest unaddressed sub-case (not a novelty claim): conditioning instruments not twirled by
the constraint (effects on the kinematical space that are not block-diagonal in sigma), with
the external phase reference modelled explicitly (an auxiliary system carrying the sector
label): does a normalized conditional probability exist for (|+> + |->)/sqrt 2 that differs
from the sector-mixed rule, and what is the cross term and its measurability? Read 2604.00092
in full including Appendix A first. Search tool was US-only and snippet-based; absence of hits
is weak evidence. Bartlett-Rudolph-Spekkens (RMP 79, 555) not read.

## Czerniawski, full text (Clifton-Hogarth NOT read)

Paper: "Time and physical geometry. A formalization of Putnam's proof", Logic and Logical
Philosophy 29 (2020) 97-114, DOI 10.12775/LLP.2019.021, open access (apcz.umk.pl). The title
"A new formalization of the Putnam argument" given in the earlier defeat search is not this
paper's title; the Polish original is "Nowa formalizacja dowodu Putnama, ze czas nie plynie",
Filozofia Nauki 22(1) (2014) 45-57, not read. Math symbols were garbled in extraction; page
locators (pp. 97-114) are reliable, formulas are the subagent's reconstruction.

- Setting: events with worldlines of possible observers; monadic "real" predicate r; relation
  R, three-place in SR (R(y; x; Gamma): y simultaneous with x in the frame of worldline Gamma);
  reality read as a non-relational property, against Stein's two-place reading.
- Premises (as labelled): (1) presentism, all and only things existing now are real (p.98);
  I* something is real (p.99); II* another observer, possibly in relative motion, is real
  (p.99); III "no privileged observers", with R physical, coordinate-independent and
  tenselessly definable (p.100), strengthened to III* and later III''*, III'''* (p.108);
  (N) the implicit bridge from "now" to R (p.100); physical facts of SR/GR (F1)-(F3'*)
  (pp.103-109).
- Results: first proof (p.104) from I*, (1''*), III'*, (F1*) to a contradiction, against
  presentism; second proof (p.106, 109) from I*, (2''*), III''*, (F2*) to eternalism (E);
  variants via (F3*) and (L''*) (pp.108-109). Quote (p.107): "the transitivity of R is not
  necessary, since no assumption here requires this property."
- Necessity analysis is informal: no countermodels, no independence proofs, no subset
  analysis. Sec. 5 (pp.109-111) checks candidate relations R (spatial separation, Alexandrov
  present, lightlike, causal and chronological past, coincidence) one by one against (F3*)/
  (F3'*). Sec. 6 (pp.111-112) shows the proofs blocked if worldline variables are restricted
  to ether-rest observers; abstract and Sec. 7 identify the weak point as "an overly strong
  interpretation of the principle of relativity" (unrestricted quantification over observer
  worldlines).
- Bridge vs physical premises: partly separated in the text ((1),(2) ontic; (N) bridge;
  (F...) physical facts), but the move from (E) to "no flow of time" is asserted, not ablated
  (p.107 declares passage out of scope).

Verdict on the premise lattice: Czerniawski does not contain it. He gives a deductive
formalization and ad hoc blocking checks of two or three premises, and shows transitivity is
dispensable; the claim "transitivity is not needed" partly pre-empts one axis of any lattice.
Clifton and Hogarth (Synthese 103:355-387): paywalled; Springer redirect, OpenAlex and
Unpaywall closed; only search-engine paraphrase of the abstract (extends Stein's uniqueness to
worldline-dependent becoming unless sets of worldlines are privileged; "essentially only one
way"). It concerns which becoming relations are definable, not the Rietdijk-Putnam derivation,
so it looks like a classification result, but this is unconfirmed. A library or interlibrary
loan copy of Clifton-Hogarth is the one read that remains blocked.
