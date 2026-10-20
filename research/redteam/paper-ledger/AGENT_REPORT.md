# rt-paper-claim-ledger

Claude coordinator, 2026-10-20. `paper/` and `knowledge/` untouched; all changes
are proposals.

## Files

- `LEDGER.md`: 39 claims from `paper/main.tex` with line ranges, citation keys,
  knowledge records and depths, flags, and notes; bibliography orphans both ways.
- `FREEZE.md`: frozen passages with the gate that unfreezes each, passages safe
  as labelled working argument, passages safe as is, and two edits worth making now.

## Counts

| Flag | Claims |
|---|---|
| A traced to full-text record | 4 |
| B abstract or discovery support | 6 |
| C records conflict | 4 |
| D no knowledge record | 1 (BernalSanchez2005) |
| E own argument or elementary result | 27 |
| F wording stronger than support | 2 (rows 6, 13) |

Bibliography: 14 keys cited, 14 in `references.bib`, no orphans either way.
`paper/check_records.py`: 5/5 tests pass.

## Three highest-risk passages

1. **Putnam and Stein, lines 218–225.** Two readings of Putnam in the records.
   Stein's theorem is known only through OCR, and the paper ("too weak") and the
   theory map ("false", with two countermodels) word it differently. RC-2 rests
   on both, and Stein 1968 is still unread.
2. **Brading, lines 236–240.** One paper, three records, two depths. The fuller
   read came from an author-linked draft with no argument reconstruction. The
   paper's description matches that read, but the record set needs merging.
3. **Relational research task, lines 262–269 and 288–293.** The proposed
   "boundary of a published equivalence" may be occupied by the RC-1 neighbours
   `kb-clock-interactions` is reading now. Extending this passage before that
   read risks claiming an occupied region.

## Overall

The draft is hedged well. Most claims are its own elementary or philosophical
argument, stated as such, and the sourced claims mostly match their records. The
risk the red team named, thesis calcification, is real only if the frozen
passages are extended before their gates open.

## Not done

No edits to `paper/` or `knowledge/`. No independent re-read of any primary
source for this task. Depths are taken from the records, except where this
session re-read them for other tasks (Brading via the discriminators review).
