# Agent report: ontology-persistence-review

29 October 2026. Independent adversarial review of the coordinator's
persistence/census deduction. Submission for coordinator inspection — not
accepted completion. Branch `agent/ontology-persistence-review`, audited
content at commit `634988e`.

(Note: the root `AGENT_REPORT.md` previously on this branch belonged to the
`stein-gluing-audit` lane, commit `6a45026`; it remains in git history and on
that lane's branches. This file is the authorized report for the present
task only.)

## Verdict in brief

- **Collapse claim verified.** S + P_c ⇒ J⁻(b) ⊆ E_b is a correct one-line
  argument; with causal boundedness the earlier two-case census is one case
  (J). I⁻∪{b} fails P_c on the exact null step (0,0)→(1,1) while satisfying
  P_t. Retractions R1–R3 specified in RESULT.md §7.
- **Census audited, no material error found.** All 24 proof obligations of
  PERSISTENCE_CONVENTIONS.md verify analytically and by exact rational
  witnesses: covariance reduction, future-set lemma, saturation bridge
  (q_Z ≪ p_S ⇔ 2ZS > R²+S²), null-orbit arguments, exhaustive four-case
  partition (I, J, B, C), all converse clauses, all ten added-premise table
  rows, and the proper-time collar counterfamily.
- **New finding (candidate result, unreviewed):** in 1+1 Minkowski without
  parity, a fifth covariant, self-inclusive, chronologically persistent,
  F_t-respecting assignment exists
  (A′ = {0} ∪ {a ∉ I⁻(0) : t_a + x_a > 0}, E_b = b − A′; analytic case
  analysis + exact checks). The coordinator's n ≥ 2 hypothesis is therefore
  necessary for the census statement itself; his 1+1 caveat should be
  strengthened from "the orbit argument changes" to "additional assignments
  exist". This does not refute the census, which is asserted only for n ≥ 2.
- **Prior art and scope.** Clifton–Hogarth 1995 Theorem 1 ({I, J, U} under
  transitivity) interlocks with the census (adding transitivity gives {I, J};
  dropping F_t admits U); Thyssen's bowtie present is elsewhere-only and is
  neither B nor C; no prior statement of the census found at the searched
  depth; no novelty claim made or implied.

## Files

- `research/ontology-reconstruction/persistence-review/RESULT.md` —
  line-by-line proof-obligation verdicts (O1–O24), retractions, notes.
- `research/ontology-reconstruction/persistence-review/sources.jsonl` —
  source register per the knowledge-base schema, honest read depths.
- `research/ontology-reconstruction/persistence-review/AGENT_REPORT.md` —
  full report (search capability check, coverage, commands, limitations).
- `research/ontology-reconstruction/persistence-review/check_independent.py`
  and `check_1plus1_fifth.py` — exact witness checks (0.26 s, 0.48 s).

## Checks

`check_persistence_witnesses.py` (coordinator) reproduced: PASS, 0.08 s.
Independent scripts: all assertions PASS, ~0.8 s total compute, standard
library only, within the 10 s/15 s/30 s compute budget. Witness checks only;
the census exhaustiveness remains an analytic claim, independently
re-derived here.

## Limitations

No Lean formalization; CH primary not reread (inherited full-text audit
used); Thyssen 2019 partially read (abstract, §§1–2, bowtie excerpt);
prior-art search is a discovery-level negative result, not a novelty
verdict; the 1+1 fifth-assignment finding is my own and awaits review.
