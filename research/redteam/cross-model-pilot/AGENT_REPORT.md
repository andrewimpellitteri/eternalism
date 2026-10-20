# rt-cross-model-pilot

Claude coordinator, 2026-10-20. The user authorized Stage 2 in chat on
2026-10-20 ("authorized"). Protocol, items, labels and the mechanical baseline
were committed in ed7dee3 **before** any auditor ran.

## Stage 1 (no model calls)

`PROTOCOL.md` checks the seven `REVIEW_NOTES.md` defects against the current
`knowledge/methods/pilot-design.md`, which was already revised once:

- Fixed there already: #1 (pass criteria now attainable), #3 (D3 retagged F1′),
  #4 (B2 predicted to catch D5), #6 (honest budget).
- Fixed here: #2 contamination (primary family is now record audits of real past
  failures and 2026 papers); #5 instance independence (instances drawn from
  different lanes and papers); #7 what a cross-model run adds (pre-registered
  same-family comparison).

## Stage 2 (run)

**Items.** 17 records shuffled with seed 20261020 (`build_stage2.py`): 8 real
past failures with documented ground truth and 9 records verified against
Crossref or arXiv. One defect (R14, Loriani et al.: 8 wrong given names) was new,
found while choosing clean controls; the knowledge record was corrected in 7e772af.

**Results** (`scores.txt`, scored by `score.py` under the pre-registered rules):

| Arm | Detected (of 8) | False flags (of 9) | Of the 3 the checker misses | Pre-registered verdict |
|---|---|---|---|---|
| `check_sources.py --online` (mechanical) | 5 | 0 | 0 | baseline |
| `author_sweep.py` (mechanical; **post hoc**, written after labels were known) | 7 | 0 | 2 (misses the venue error R02) | not pre-registered |
| Claude auditor (subagent, one session) | 8 | 0 | 3 | adds value; does not fail as a gate |
| GPT auditor (`codex exec`, one session) | 8 | 0 | 3 | adds value; does not fail as a gate |

Both auditors named the labelled field for every detection and marked nothing
unverifiable. **Same-family comparison:** GPT-family lanes produced R01, R02,
R06 and R14; the GPT auditor caught all four, so no same-family blind spot
appears, at n = 4.

**Interpretation.**
- The task had a ceiling. Every defect is a factual mismatch that one lookup
  exposes, so any auditor that actually looks catches it. That is evidence the
  original errors came from **writing metadata without a lookup**, not from a
  model's inability to see them.
- This pilot therefore cannot separate model families. Separating them needs
  defects that need judgment (overclaimed scope, a bridge premise typed as
  physics), which is the Family A/B design in `pilot-design.md`.
- The cheapest high-value control is mechanical: a Crossref/arXiv author
  comparison catches the hallucinated-name class the DOI checker cannot.

## Follow-on: knowledge-base author sweep

`author_sweep.py` over all 251 records with authors (202 checked against a
source) flagged 15. Of these, **5 had real author errors**, now corrected in
edfb803:
- `frontier-page-wootters-measurements-2023` credited Baumann and Lock instead of
  Hausmann, Schmidhuber and Castro-Ruiz (RC-5 cites this record).
- `frontier-emergence-time-qg-2012` added Rovelli to a single-author paper.
- Three `ico-qrf` records had invented given names: Alfred for Alexei Grinbaum,
  Christina for Carlo Cepollaro, James for Jeremy Butterfield, Costantino for Cyril
  Branciard.

The rest were false positives (transliteration, a name suffix, joined author
strings, a role note, Crossref formatting) or ambiguous ("Nicolas" vs. "Nick"
Ormrod, left unchanged). Adding the sweep, with these exclusions, to
`check_sources.py` would need the check owner's agreement.

## Cost and calls actually used

- Claude auditor: 1 subagent session, 31 web fetches, about 53k tokens, 107 s.
- GPT auditor: 1 `codex exec` session, 12 shell commands, about 1.43M input
  tokens (1.32M cached) and 9.7k output tokens.
- GLM: none. Its quota was exhausted at 08:25 UTC.
- Mechanical runs: 3 (checker, pilot author sweep, knowledge-base sweep).

## Limitations

- n = 17 and both auditors hit the ceiling. No rates are estimated.
- Each auditor saw all items in one session, not one per fresh context.
  Acceptable here because no paper appears twice, but it differs from the design.
- The Claude auditor could technically read the repository. It was told not to,
  and its report cites only web sources, but compliance was not enforced. The GPT
  auditor ran from an empty scratch directory, and its commands were inspected:
  all were network lookups.
- The author sweep was written after the labels were known and is reported as
  post hoc.
