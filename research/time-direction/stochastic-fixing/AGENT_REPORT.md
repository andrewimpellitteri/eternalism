# Agent report: novel-stochastic-fixing

11 November 2026. Native Claude research worker (Fable 5.2). The run was interrupted
three times by usage limits and resumed by the coordinator. A submission for review,
not an accepted result.

## Files written

All in `research/time-direction/stochastic-fixing/`. Nothing else was edited, and
nothing was committed.

- `RESULT.md`: verdict, definitions, four propositions with proofs, examples, answers
  to the three questions, credits, limits.
- `check_stochastic_fixing.py`: standard library only, exact rational probabilities.
- `sources.jsonl`: 11 records with read depth.
- `AGENT_REPORT.md`: this file.

## Verdict in brief

Exact fixing under a process law depends only on which histories are possible, and it
is reciprocal for every path measure. A stationary Markov chain read in full has
mirror-symmetric entropies on all sets of times whether or not it is reversible, so a
kernel arrow (non-reversibility, entropy production) is invisible to every amount of
fixing. It shows in labelled path statistics, in fixing at particular states, and in
which part of the present matters for each direction. A boundary arrow shows in the
balance and has no entropy production rate. The mirror proposition and the collapse
claim stand.

## Evidence

- Proofs of Propositions 1 to 4 in RESULT.md. All are short and elementary.
- `python3 check_stochastic_fixing.py` ends with "all checks passed". It took under
  ten seconds here. What it asserts:
  - E1 to E4: stationary laws solved exactly; detailed balance fails; entropy
    production values; the list of reversing relabellings found by exhaustive search
    over permutations; statewise and averaged openness; largest mirror gap in region
    entropies over all sets of times in 0..4 is below 1e-9; shared exact quantities of
    X_0 and X_k for k = 1..4.
  - E5: the path divergence from reversal matches the closed form of Proposition 4
    for n = 1..7 and the balance equals H(μ_n) − H(μ).
  - E6: {0,1} fix X_3 and {2,3} do not fix X_0; stationarity of windows checked.
  - E7: exact equality or inequality of record and reversed-record probabilities in
    five cases.
  - The arithmetic of the published random-insertion-process state laws in
    Crutchfield, Ellison and Mahoney.
- Sources read: Norris section 1.9 (all five pages, as page images); Crutchfield,
  Ellison and Mahoney (all four pages); Ellison et al. sections III.2, IV.2, V.4,
  VI.1; Bedingham and Maroney sections I, IV, V. The last two were read as text
  extracted from the ar5iv HTML rendering, kept in the session scratchpad and not in
  the repository.

## Checks not done

- No second reader. No Lean. No test added to `tests/`.
- `scripts/check_sources.py` and `scripts/check_links.py` were not run, since I was
  told to change nothing outside this directory and did not check whether they write.
- One extra check was run by hand and is not in the script: lumping two states of E2b
  into one gave a mirror gap of zero on 0..5 as well. I do not know whether that is
  general for two-valued readings and did not pursue it.

## Limitations

- Discrete time, finite state space, full-state readings for Proposition 2.
- The entropy-production literature is at abstract depth only, and the tool that
  fetched the two abstracts paraphrased them. Proposition 4 was derived here, not read.
- Kelly's book could not be read (image-only scan) and the Kolmogorov criterion is
  not sourced. The brief named both.
- Gács and Körner is cited from memory at discovery depth.
- arXiv version numbers for 1107.2168 and 1502.06830 were not confirmed, because the
  ar5iv rendering does not state them.
- Entropies are floating point. Equalities of entropies are checked to 1e-9 or 1e-12,
  not exactly.
- E7 is a classical analogue. The quantum proposition in the settling note was not
  rechecked and its script was not rerun.

## Strongest objection

The headline result is close to true by definition. Reciprocity of exact quantities
is immediate, and whether "fixing detects the arrow" depends on which of three
readings of fixing in distribution one adopts: with labelled conditional laws it
does, trivially, since K ≠ K*. The substantive content is only Proposition 2 and the
sorting of arrows by instrument, and Proposition 2 fails for coarse readings, which
are the physically relevant ones.

## Unresolved questions

1. Is Proposition 2 in print? Likely, given how short it is. I did not find it in the
   sections I read.
2. Is the minimum of entropy production over state relabellings a named quantity?
   Kelly's chapter is the place I would look first.
3. For coarse readings of a stationary chain, how large can the mirror asymmetry of
   region entropies be, and is it bounded by causal irreversibility or by entropy
   production? E6 gives one bit with a deterministic law.
4. Does a continuous-time or continuous-state version of Proposition 2 hold at finite
   resolution, as the fixing-exchange note's stationary result does?
5. Should the paper's direction section carry one sentence saying that a process law
   with no reversing symmetry has an arrow the fixing relation cannot express? That is
   the coordinator's call.
6. The Crutchfield, Ellison and Mahoney letter defines Ξ = C⁺ − C⁻ and reports
   Ξ ≈ 0.3245 for values that give −0.3245. I read it as a magnitude. The published
   version was not compared.
