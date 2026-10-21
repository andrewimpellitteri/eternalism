# Coordinator review: event-filter-resource-boundary

Reviewer: coordinator, 2026-10-21. Submission by `codex-event-filter`, with
later coordinator additions (`RECORD_LOSS.md`, `COHERENT_GROWTH.md`) and an
independent review of the record-loss claims.

## Verdict

**Accept as a scoped finite instrument/calibration result.** The published
event-filter construction is reconstructed at named locators, a finite
coherent-register instrument is exhibited, and the resource statement is
separated from any physical or ontological claim.

## Independent checks performed

- Reran `check.py`: exact binomial and separate word-enumeration paths agree.
  For n=20, event size 524800, endpoint-summed measure 525313/4, detector
  probability 525313/2099200 ~ 0.25024, membership probability 1025/2048.
  The detector probability tends to 1/4 while the measure diverges.
- Reran `check_record_loss.py`: the claimed visibility/leakage and sample
  counts reproduce exactly.
- Reran `check_causal_growth.py`: labelled complex-percolation columns through
  n=6 have unit norm and disjoint child supports; the simulator is an
  isometry on the stated finite domain.
- Checked the `eta <= 1/m` argument: equality on all normalized inputs forces
  the effect `Q = eta |u_E><u_E|`, whose nonzero eigenvalue is `eta m`; hence
  `eta <= 1/m`, attained by the equal-superposition projector. The subspace
  version `eta <= 1/||Pi u_E||^2` follows the same way. This is elementary and
  is not claimed as new.

## Priority and scope

- The generic filter factor is attributed to Frauca-Sorkin 1610.02087v1
  Sections 5.2 and 6.2.1; the 1/2-versus-1/3 photonic comparison to
  Chakraborti-Sorkin-Sinha 2407.15702v3. No exhaustive priority search was
  performed because no novelty claim is made.
- `RECORD_LOSS.md` has an independent mathematical review and no refutation
  was found; its scope is the stated Schur channel, all-input effect, and
  locally unbiased commuting family.
- `COHERENT_GROWTH.md` is a finite isometric simulator, not a causal-set
  observer or an infinite extension; it was written after the independent
  review and is accepted only at that scope.

## Limits

The instrument is an abstract coherent register, not complex causal-set
growth. Recognition is separated from coherent erasure. The calibration
bound is event-specific unless a common efficiency is demanded; no universal
exponential shot cost, hardware lower bound, or temporal-ontology conclusion
follows. The full-depth primary reconstruction outside the cited sections was
not completed.
