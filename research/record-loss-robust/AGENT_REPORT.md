# Agent report: record-loss-robust-boundary

Sole-worker result, 2026-10-21. Files: `RESULT.md`, `check.py`, this report.

## Result

For the stated block-correlated Gram-record model with `m` blocks of `B`
perfectly correlated positions:

- targeted access at fraction `f` leaves `max(0, m - f m B)` hidden blocks, so
  the visibility is `gamma^{max(0,m-fmB)}` and the threshold is `f_c=1/B`;
- random access has `E[V]=[1-(1-f)^B(1-gamma)]^m`, so for fixed `B` and `f<1`
  it decays exponentially in `m`, with no interior threshold;
- independent per-bit leakage has exponent `mB(1-f)`, which is much larger
  than the correlated exponent when `f` is near one.

The qualitative point is that a resource claim stated only as an accessed
fraction is incomplete: the access model and correlation structure set the
boundary. Targeted block access is exponentially cheaper than random access.

## Checks

`python3 research/record-loss-robust/check.py`:
- exhaustive targeted minima for `m<=5`, `B<=3`, every `k`;
- exact rational random-access expectations at four `(m,B,f,gamma)` points,
  matching the closed form;
- the exponent comparison at `m=100`, `B=4`, `f=9/10`.

All pass. The checks are finite; the formulas are elementary exact
combinatorics.

## Scope and limits

- The model is a finite record register with binary block records, known block
  partition, and a two-history visibility target. It is not a causal-set growth
  model and not a physical observer.
- Collective measurements, signed estimators, entangled inputs,
  environment-assisted correction and biased estimation are outside the model.
- No new full-text primary reads were added; the prior-work comparison is
  inherited from `RECORD_LOSS.md` (Buscemi–Chiribella–D'Ariano,
  Buscemi, Frauca–Sorkin), with the read-depth limits recorded there.
- No novelty claim. The coverage argument is elementary; the value is the
  explicit access-model dependence, not a new erasure theorem.
