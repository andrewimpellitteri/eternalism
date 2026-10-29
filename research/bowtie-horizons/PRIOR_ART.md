# Prior-art synthesis for the screening claims X1–X4

28 October 2026, native Claude, integrating three GLM audits
(`research/bowtie-horizons-prior-art/{prediction,bst,becoming}/`, submitted
for review). Quotes marked *verified* were re-checked by me against the
primary text; all others are as reported by the GLM audits.

## Closest neighbours

| Source | What it has | Overlap |
|---|---|---|
| Belnap 1992, *Synthese* 92, p.395 (reported from OCR scan; **not verified**) | "If there are 'event horizons' … there can be compatible point events without a common causal future"; tabled | Same structural threat behind X1, in BST, for a common-future criterion of compatibility. Not about existence domains or growth. |
| Belnap–Müller–Placek 2022, *Branching Space-Times* (OUP, open access) Fact 9.14, p.316 (*verified*) | GR spacetimes where every pair has a common causal future induce one-history BST structures | Uses the same directedness condition as RESULT.md Prop. 1/7, for a different purpose |
| BMP 2022 §10.5, p.362 (*verified*) | Parts of the elsewhere are "neither dynamically past, nor present, nor future"; "the reach of causation … does not extend far enough across space" | Closest statement to "bow-tie surplus events are causally idle" (X3). No screening or minimality theorem, no Cauchy slices, no existence domain. |
| Friedman–Kaiser–Gallicchio 2013, *PRD* 88, 044038 (GLM partial read) | Explicit "no shared causal future" thresholds in FLRW with Λ, for cosmic Bell tests | Threshold arithmetic behind X1/X2 is prior art. No growth axiom, no historical domain, no two-sided R_x + R_s + 2P_s bound. |
| van der Schaaf 2026, arXiv:2601.14029v2 (project-recorded and GLM) | Failure of future confluence in globally hyperbolic spacetimes; S4.2 vs S4 | Premise of X1 on the modal-logic side |
| Jaeger 2025, NYU dissertation (GLM partial read) | Markov-style screening of regions by boundaries, static backgrounds | Conceptual neighbour of X3; probabilistic, not domain-of-dependence screening |
| Geroch 1977; Manchak 2008; Lesourd 2021; Smeenk–Wüthrich 2021 | Prediction domains P(q); genuine prediction; determination by closed-universe light cones; CBG determinism | Ingredients of X4. No realm-wise or minimal-screening formulation. |
| Stein, Clifton–Hogarth, Dieks, Arthur, Savitt, Ellis, Rovelli | Relativistic becoming | Nothing on horizons or influence-based existence. Ellis 2006 and Ellis–Rothman 2010 PARTIAL on determinism framing only. |

## Revised status of each claim

- **X1** (instantaneous causal potential violates (P1R) without pairwise
  common futures). The premise, that horizons break common-future criteria,
  is anticipated: Belnap 1992 (if verified), BMP 2022, FKG 2013, van der
  Schaaf 2026. The claim itself, applied to C&R's existence rationale and
  their growth axiom with the exact characterization (Prop. 7, coordinator
  lemma), was not found.
- **X2** (historical repair misses D_BT \ H in dust + Λ). Not found.
  Threshold-style horizon arithmetic in exact FLRW is prior art (FKG 2013).
- **X3** (the causal-potential realm is the minimal screening realm). Not
  found as stated. BMP §10.5 is the closest neighbour (causal reach fails
  to classify part of the elsewhere); Jaeger 2025 is a probabilistic
  analogue.
- **X4** (realm rigidity). Components standard (CBG; prediction
  literature). The realm-wise formulation was not found; it is still
  conditional on premise L′ (PREMISE_L.md).

## Effect on the novelty estimate

Unchanged in kind, sharper in content. The mathematics is not new. The
application to Correia–Rosenkranz still looks new on everything read, but
it must cite the BST anticipations. In particular, Belnap already flagged
horizons as a problem for common-future criteria in 1992 and set it aside.
That makes X1 the least novel of the four. X3 (with the bow-tie-surplus
reading) and X2 carry most of whatever novelty there is.

These audits cover named sources with mixed read depths; several are
abstract-only (Clifton–Hogarth, Savitt, Arthur 2019, Dieks 1988). Absence of
hits is not novelty.

## Open source gates

- Verify Belnap 1992 p.395 against a clean copy (the open mirror failed
  certificate checks; JSTOR is gated).
- C&R *Nothing to Come* Appendix 3.
- Full reads of Clifton–Hogarth 1995 and Savitt 2000/2009, currently
  abstract-level.
