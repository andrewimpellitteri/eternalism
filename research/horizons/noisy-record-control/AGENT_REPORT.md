# Submission: noisy-record and cutoff controls

Task horizons-noisy-record-control; coordinator codex-noisy-record.
27 October 2026. Independent review required; no manuscript integration.

## Files and result

RESULT.md gives a self-contained sequence of smooth exact massless cylinder
solutions with unit conformal energy, vanishing aggregate field-record norm
and divergent point value at an exactly fixed dust target. It specifies the
physical-field conversion and distinguishes point values from fixed spatial
averages. A positive full-strip-record averaging bound is proved separately;
it is not promoted to a past-only observability bound.

The finite-band section proves that restricting the solution class to any
fixed finite set of spatial modes makes every event exactly fixed by any
nonempty open record region. This is a classical analyticity diagnostic,
not evidence that the physical theory has a frequency cutoff.

check_controls.py and verification.json record independent radial quadrature
checks of cross-mode cancellation, conserved energy, full-period record norm,
constant spatial averaging, and a small zonal-subspace observation Gram matrix.
sources.jsonl records the original teaching source read before derivation.

## Verification

The standard-library controls passed for bands K=4,8,16,32. Radial squared
field norms matched spectral expressions within 7e-18; energy and velocity
checks met 1e-11 tolerances. The six-dimensional zonal observation Gram matrix
had positive Cholesky pivots and a 512/1024-step refinement difference of
3.38e-12. This checks a small subspace, not the full harmonic matrix or a
uniform conditioning constant. The general assertions are analytical.

## Limitations and review questions

Review normalization of zonal harmonics, the phase-aligned target sequence,
the physical-volume weighting and real-analytic finite-band argument. The
chosen record norm sees field amplitudes, not derivatives or pointwise errors.
It does not describe an actual apparatus. The energy constraint is conformal,
not a claimed uniform bound on physical energy near the dust singularity.

The failure occurs even with all-strip records and therefore cannot be
attributed to causal horizons or refocusing. A fixed averaging profile kills
this particular sequence; stability for realistic past-only detector records
remains open here. Each sequence member has finite bandwidth but no common
cutoff contains the entire sequence. Finite-band uniqueness is a different
solution class from unrestricted smooth solutions.

The earlier bounded-ambiguity result keeps exact past agreement and changes
the equation. This result keeps the equation fixed and permits a specified
record error. Those quantifiers must remain separate. Neither result settles
a temporal ontology or claims original PDE theory or global priority.

Active worker outputs, manuscripts and unrelated changes were not edited.
