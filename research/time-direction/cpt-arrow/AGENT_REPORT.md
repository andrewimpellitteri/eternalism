# Agent report: novel-cpt-arrow

11 November 2026. Native Claude worker (Fable 5.2). The run was interrupted once by a
usage limit before any file was written, and resumed in the same session. A worker
submission for review, not an accepted result.

## Files written

All in `research/time-direction/cpt-arrow/`. Nothing else was edited. Nothing was
committed.

- `RESULT.md`: verdict, corrected claim, reasons, credits, limits, requested change.
- `sources.jsonl`: 18 records, each with its read depth.
- `AGENT_REPORT.md`: this file.

No script. The task has no numerical content.

## Verdict in brief

The CPT step holds in a corrected form. Hollands and Wald's curved-spacetime PCT
theorem gives closure under a flip of the time orientation alone, which is the map
Proposition 2 uses. The flat theorem gives it only after composing with x ↦ −x. The
hypotheses are those of the theorems, not "locality and Lorentz invariance". For
general relativity and classical tensor fields no theorem is needed, and classically
the settling note's conclusion is false as stated. The quantum conclusion also needs a
bridge premise: that a world and its charge-conjugate with reversed time orientation
have the same orientation-free content.

## Evidence

| Claim in RESULT.md | Basis | Depth |
|---|---|---|
| Curved PCT theorem relates (M, g, e, T) and (M, g, e, −T) by an antilinear isomorphism, with a dual map on states | Hollands and Wald, Sec. 5, eq. (63), Theorem 3, diagrams (83)–(84) | Read |
| Flat theorem equals that map composed with the reflection isometry | Same, eqs. (87)–(89) | Read |
| The theorem relates an expanding universe to the contracting one, not processes within one | Same, text around eq. (90) | Read |
| Jost: weak local commutativity is equivalent to CPT in the Wightman framework | Greenberg; Dütsch and Gracia-Bondía; Chaichian et al. | Jost unread; three consistent secondary statements |
| Lorentz-invariant nonlocal CPT-violating models; Greenberg's argument disputed | Chaichian et al. Secs. 3–4; Dütsch and Gracia-Bondía Secs. 2, 5 | Read |
| Classical PT theorem for polynomial tensor theories; failure for spinors | Greaves and Thomas, Sec. 4.1, Theorem 1, Sec. 8 opening | Statements read; proofs unread |
| Time reversal as flip of temporal orientation; eq. (28) not invariant | Malament, Secs. 1 and 4 | Read |
| Roberts's position, his concession on the choice of orientation, Price's objection | Roberts, Secs. 7.1, 7.4.1–7.4.2, ch. 8 to end of 8.2 | Read |
| Proposition 2′ and the closure table rows marked elementary | My own argument | Self-checked only |
| Viscous-fluid example | My own calculation of parities under u ↦ −u | Self-checked only |

## Checks run

- `python3 scripts/check_sources.py`: 0 errors; no warning names a record of this lane.
- `python3 scripts/check_links.py`: 0 broken links.
- `sources.jsonl` parses as 18 JSON lines.
- Papers were read through a text-extraction tool. No files were downloaded into the
  repository and no packages were installed.

## Limitations

- Jost (1957) and Streater–Wightman were not read. The brief names them as primary
  statements. I could not reach them and used papers that state the theorem.
- Greaves (2010) could not be fetched (two refusals). Her diagnosis is reported
  second-hand from Roberts and a search summary. Earman (2002), Albert (2000), Price
  and Swanson are likewise at discovery depth.
- The Greenberg text extraction was degraded; formulas were partly illegible. The
  prose argument was readable.
- Hollands and Wald's axioms (their Secs. 2–4) were searched and not read through. I
  did not check the proof of their eq. (64), which carries the theorem.
- Proposition 2′ for quantum fields is a schema. The project has not defined a germ or
  a local clock for quantum states.
- The novelty search was thin. I did not look for a prior statement that combines a
  no-clock proposition with the Hollands–Wald form of the theorem.

## Unresolved questions

1. Is there a workable definition of a local clock on states of a locally covariant
   quantum field theory, for which Proposition 2′ is a theorem and not a schema?
2. Does any restricted, physically motivated class of states (Hadamard states on
   expanding cosmologies, say) carry a monotone local quantity, and is that class
   closed under the Hollands–Wald map? Their own example suggests not.
3. Roberts's Secs. 8.3–8.4 argue about whether matter–antimatter exchange can be a
   spacetime symmetry. They bear directly on the bridge premise and were not read.
4. Does the classical PT theorem extend to curved spacetime beyond the trivial
   observation that equations built from g, e and ∇ do not mention T? I found no
   source and did not look far.
5. The settling note's §1 says the mirror argument for collapse "goes through" with
   the combined reversal. That was outside this task and is unchecked.
6. Causal-set sequential growth and Tumulka's flash model are named in the settling
   note as candidate lawful directions. Neither falls under any row of the closure
   table, and neither was examined here.
