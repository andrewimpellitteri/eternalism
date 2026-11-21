# Agent report: novel-massive-cone-algebra

11 November 2026. Claude Code (Fable 5.2), native research worker. Submission for
review, not accepted completion.

## Files written (all in research/horizons/massive-cone-algebra/)

- RESULT.md
- sources.jsonl (7 records, each parses as JSON)
- AGENT_REPORT.md

No other file was edited. Nothing was committed, installed or launched. No Python
check was written: the result is a literature finding plus a short operator-algebra
argument, and no numerical check would bear on it.

## Verdict

For a massive free scalar field in the Minkowski vacuum representation the algebra of
the open forward or backward light cone is B(H). A thin tube around a past inertial
half-worldline already generates B(H). Known result; no novelty claimed.

## Evidence

- Buchholz–Roberts, arXiv:1304.2794v4, p. 10: R(V) is B(H) or type III₁; B(H) with a
  mass gap, citing Sadowski–Woronowicz "Thm 2"; type III₁ with massless particles.
  Read.
- Buchholz–Fredenhagen, arXiv:2305.11709v1, Lemma 3.1 and Prop. 3.2: proof that
  R(V) ≠ B(H) forces spectrum on the whole cone. Read with proof.
- Strohmaier, arXiv:math-ph/0008043v2, Theorems 3.2 and 5.1: envelope theorem for the
  free field of any mass, classical and quantum. Read with proofs.
- Strohmaier–Witten and Witten 2023: general timelike tube theorem, semi-infinite
  curves, massless timelike commutativity in even dimensions. Read (pages listed).

## Checks

- sources.jsonl parsed line by line.
- Crossref confirms the 1971 paper's journal, volume, pages and DOI.
- The four-step argument in RESULT.md was re-derived by hand from the
  Buchholz–Fredenhagen text; step 4 and the free-field spectrum are added by me.
- The tube step was checked against Strohmaier's definitions: a segment's envelope is
  its double cone (Prop. 2.1), and the double cones exhaust the open past cone.

## Limitations

- Sadowski–Woronowicz 1971 not read (ScienceDirect 403; no open copy found). Its
  abstract was seen only as a search-engine paraphrase. Its exact hypotheses, and the
  theorem number "Thm 2", are taken from Buchholz–Roberts.
- Borchers' half-sided translation theorem, on which the read proof depends, was not
  read at a source. Borchers 1961 and Araki 1963 not read.
- Buchholz 1977, Longo 1979, Hislop–Longo 1982: Project Euclid blocked every request.
  Nothing is attributed to Hislop–Longo.
- The equivalence with a classical uniqueness statement in the one-particle norm
  class, and the consequence for finite-energy solutions in all dimensions, is this
  session's derivation and is unreviewed.
- Papers were read through a page-extraction tool; formula text was garbled in places
  and some pages were not returned (listed per source).

## Unresolved questions

- What exactly does Theorem 2 of Sadowski–Woronowicz assume, and what is their "open
  isotropic tube" (a neighbourhood of a lightlike line?) If that set is total, a
  massive field would be generated from a tube around a null line, which no envelope
  argument gives.
- Massless free fields in odd spacetime dimensions: B(H) or type III₁ for the cone?
- Is the thin-tube corollary for a half-worldline stated anywhere in print?
- The cone-algebra note and the massive-Minkowski note could now be updated by the
  coordinator: the massive entry is settled, and the higher-dimensional classical
  case follows from the quantum theorem. I did not edit them.
