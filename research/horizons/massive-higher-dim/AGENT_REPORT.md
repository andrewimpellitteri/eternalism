# Agent report: novel-massive-higher-dim

11 November 2026. Native Claude research worker (Fable 5.2). Nothing committed. Nothing
outside this directory was edited. No packages installed, no agents launched.

## Verdict

Proved for every space dimension n ≥ 1: a tempered-distribution solution of the massive
Klein–Gordon equation on Minkowski spacetime that vanishes on the chronological past of
an event (or only on the tail of that cone) is zero. Finite-energy solutions are a
subclass. Tempered distributions give the same answer as finite energy. Smooth
solutions growing like e^{m|x|} are not fixed beyond the causal past, in every
dimension. For finite energy the needed exterior energy decay is a published statement
(Yang, arXiv:2309.15282v1), which I read with its proof.

## Files

| File | Contents |
|---|---|
| `RESULT.md` | Verdict, full proof, attacks, illustration, credits, limits |
| `sources.jsonl` | Eight records: two full-text, one abstract, five discovery |
| `cone_energy_2d.py` | Standard-library illustration in 2+1 dimensions |
| `AGENT_REPORT.md` | This report |

## Evidence

- A self-contained proof (RESULT.md): structure lemma for tempered solutions,
  non-stationary phase for test solutions with compact momentum support, and the
  conserved symplectic pairing, which tends to zero as t → −∞ and is constant.
- Yang's remark and appendix, read in the arXiv TeX source: energy in {|x| > |t|}
  tends to 0 for H¹ × L² data, any dimension, m = 1.
- Duell, Lemma 6 and Corollary 7, read: the pointwise estimate for n = 3, credited to
  Ruelle 1962 and Reed–Simon III.

## Checks

- `python3 cone_energy_2d.py` ran (about 4 seconds here). Fraction of energy in
  |x| ≥ |t| at t = −25, −50, −100: m = 0: 0.356, 0.355, 0.354; m = 0.5: 0.022, 0.007,
  0.000; m = 1: 0.000 throughout. Computed total energy over exact: within 3 × 10⁻⁴
  of 1 at every time. Built-in checks of the Bessel routine pass.
- `python3 scripts/check_sources.py`: 0 errors (4 warnings, all in other lanes).
- `python3 scripts/check_links.py`: 0 broken links.
- The proof was attacked at the points listed in RESULT.md: time slices of
  distributions, vanishing of ∂ₜu on the ball, failure at m = 0, uniformity in t,
  the cancellation in the pairing.

## Limitations

- One session wrote and checked the proof. No independent re-derivation.
- Yang's proof depends on two technical lemmas of that paper that I did not read. My
  own corollary proves the same decay without them.
- Strichartz 1981, Nelson 1971 (abstract only), Ruelle 1962, Reed–Simon III and
  Sadowski–Woronowicz 1971 were not read. Publisher pages were not tried; PDF tools
  are not installed here, so sources were read as TeX or through a text extraction.
- The published version of Yang's paper was seen only in a search extract; theorem
  numbers quoted for it (Theorem 1.9, Remark 1.10, Appendix D) come from that extract.
- The numerical script covers one rotationally symmetric datum in two dimensions.
- Novelty: none claimed. Two searches found no statement of the tempered-distribution
  theorem, which is weak evidence only.

## Unresolved questions

1. The growth threshold. Tempered solutions are fixed; solutions growing like
   e^{m|x|} are not. What about growth e^{ε|x|} with ε < m, or sub-exponential growth?
2. Does Sadowski–Woronowicz prove the quantum counterpart (past-cone algebra of a
   massive free field is everything), and in which dimension? The classical theorem
   here, for solutions in the one-particle norm, should be equivalent to it; I did
   not write that equivalence out.
3. What exactly does Nelson 1971 state, and is it the earliest source?
4. Is Yang's criticism of Strichartz's Corollary 2.2 correct? It does not affect this
   note.

## For the coordinator

The ledger line "Higher dimensions rest on an unchecked estimate" and the sentence in
the 1+1 note "which is standard and which I did not check at a source" can now be
replaced by a citation of Yang or of this note. The cone-algebras note's phrase "for a
massive field of finite energy it then vanishes everywhere" now holds in every
dimension and for tempered solutions. I edited neither file.
