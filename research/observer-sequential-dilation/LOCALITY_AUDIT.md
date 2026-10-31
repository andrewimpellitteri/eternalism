# Locality and parent-marginal audit of sequential observer dilation

Bounded sidecar, 24 October 2026. This reads the predecessor `RESULT.md` and
`CIRCUIT.md`, `event-filter-resources/COHERENT_GROWTH.md`, and
`longshots/bc-matched-diffuse/RESULT.md`. It does not redo the growth bounds,
audit a broader literature, or make a novelty or ontology claim. Source-read
depth here is project-artifact audit; no external paper was newly checked.

## What the proposed stage operation establishes

For a finite parent set and its distinct labelled children, consider the
success Kraus operator

    K_n |C> = sum_P sqrt(|t(C,P)|/B_n) phase(t(C,P)) |CP>,
    B_n = 1 + zeta_n.

Unique deletion of the last birth gives disjoint child supports for different
parents. Therefore

    K_n^dag K_n |C> = r_C |C>,
    r_C = sum_P |t(C,P)|/B_n <= 1.

The leftover effect `I-K_n^dag K_n` is a failure outcome, so this is a valid
heralded finite-register operation when the displayed amplitudes can be
implemented. On input `sum_C alpha_C |C>`, its success probability is
`sum_C |alpha_C|^2 r_C`; conditioned on success, the output is `K_n alpha`
divided by the square root of that probability. The bound `r_C <= 1` is a
uniform upper bound on the row sum, not a uniform lower bound on success.
Across stages the all-success probability is the product of the conditional
stage success probabilities along the actually updated state. It cannot be
replaced by a product of worst-case lower bounds unless such lower bounds are
separately proved.

This operation is not the coherent growth isometry in
`COHERENT_GROWTH.md`: its coefficient modulus is `sqrt(|t|/B_n)`, not `|t|`.
It realizes a square-root reweighting of the transition row. In particular,
the named formula alone does not prepare the prescribed path amplitudes
`A(CP)=A(C)t(C,P)`. That distinction should remain visible in any claimed
observer-preparation result.

## Deterministic prefix preservation in the total-variation encoding

The target encoding in `RESULT.md` is
`psi_n(C)=sqrt(|A(C)|/V_n) phase(A(C))`, so its parent probability is
`|A(C)|/V_n`. Do not compute this marginal by summing `|A(CP)|^2` once per
precursor: that is a different, raw-amplitude encoding. For the target used
here, the child-sector probability is

    sum_P |A(CP)| / V_(n+1)
      = |A(C)| s(C) / V_(n+1),
    s(C)=sum_P |t(C,P)|.

A deterministic prefix-preserving isometry preserves each parent-sector
probability. It can therefore produce the target only if every occupied
parent has `s(C)=V_(n+1)/V_n`. Nonconstant row variation obstructs this
restricted deterministic preparation. It does not obstruct parent mixing,
heralding, or a changed encoding.

Exact MSR toy control: take parent amplitudes `a_A=a_B=1/2` and transition
rows `(1,0)` and `(2,-1)`. Their row variations are 1 and 3, and child
amplitudes are the parent amplitude times the listed transition. The child
total variation is `1/2+3/2=2`. Thus the existing parent probabilities are
`1/2,1/2`, while the target child total-variation parent marginals are
`(1/2)/2=1/4` and `(3/2)/2=3/4`. A deterministic prefix-preserving isometry
cannot change those sector probabilities, so it cannot prepare this target.
The zero transition is allowed only for this exact algebraic control; it is
not asserted to occur in the actual matched pair.

For the same toy, set `B_3=3`. The controlled success Kraus map has row
successes `1/3` and `1`, hence forward success `(1/2)(1/3)+(1/2)(1)=2/3`.
Conditioning on that flag gives parent marginals `1/4,3/4` as required.
The common reverse-readout success contributes another factor `2/3`; because
`V_4=2`, the full baseline success is `(2/3)^2/V_4^2=1/9`. Counting forward
success but treating readout as a free ideal projector would incorrectly give
`(2/3)/V_4^2=1/6`.

The exact control illustrates the obstruction and flag accounting only. The
current checker separately reports a nonconstant row-variation witness among
actual size-four parents of the matched pair, so the restricted
obstruction applies there as well. No full-growth recalculation is made here.

**Encoding warning.** If instead one uses raw amplitude coefficients
proportional to `|A(C)|`, the Born parent probabilities are proportional to
`|A(C)|^2`; the parent-marginal test must then be derived for that different
encoding. The preceding total-variation obstruction does not silently carry
over to it.

## Assumptions still needed for a physical observer

The word “sequential” here means a sequence of parent-controlled operations
on finite history registers. It supplies no spacetime locality. A physical
interpretation still needs at least:

- A physical carrier and tensor-factor or algebra assignment for parent,
  child, memory, and herald registers; a rule for which controls can couple;
  and a resource bound (range, depth, energy, or communication) as histories
  grow. A finite matrix acting on a global history label is not a local
  interaction merely because it is applied one stage at a time.
- An implementable source of the complex transition phases and the required
  square-root magnitudes, plus coherent storage and control accuracy. The
  predecessor circuit already notes that arbitrary finite unitaries and a
  model-dependent phase gate are mathematical resources, not derived
  cosmological dynamics.
- A symmetry action on the physical registers and admissible controls. The
  finite representative-permutation covariance in `CIRCUIT.md` does not show
  each gate is allowed by that symmetry. Full completed-history relabeling
  invariance requires a specified action preserving the relevant measure,
  event, and instrument. Input-state invariance or a permitted preparation
  rule is a further issue; apparatus covariance alone does not provide it.
- A reason heralding and its recorded failures are physically available, and
  a specification of what happens to discarded environments. The success
  flag is part of the instrument and its statistics, not a removable
  normalization convention.

These are physical premises, distinct from the matrix definitions. Even if
all are supplied, an observer interpretation needs an explicit account of
what the memory records and which events it can recognize. Nothing here
selects a temporal ontology, objective passage, determinism, or a
thermodynamic arrow.

## Two inference controls

1. **False inference:** “The depth-n maps are sequential finite-register
   operations, therefore they are spacetime-local dynamics (or an internal
   observer).” **Control/counterpart:** sequentiality only orders abstract
   parent-controlled gates. A counterpart claim would specify physical
   carriers, allowed local couplings, resource scaling, and an observer's
   memory/readout map. `CIRCUIT.md` explicitly leaves those implementation
   facts open.

2. **False inference:** “Because a common positive-growth dilation has a
   reverse circuit, the universe or cosmological growth physically evolves
   backward, or a completed-event detector is automatically available.”
   **Control/counterpart:** retaining the full unitary dilation, including
   environments and flags, makes its inverse available on the encoded image
   when that circuit is controllable. In `RESULT.md`, reverse positive-growth
   readout contributes its own success factor `r_N`; together with forward
   preparation the baseline rate is `r_N^2/V_N^2`, not the rate obtained by
   treating the final projector as free. The toy above gives `1/9` versus the
   incorrect `1/6`. For an isometry, the adjoint reverses states in its image;
   it does not define inverse dynamics on arbitrary states. Reversing only a
   heralded successful branch is not a deterministic inverse: failure
   branches and their flags remain part of the full dilation. Reverse circuit
   access therefore adds an operational capability under a controllability
   assumption, not cosmological reverse evolution, a finite detector for a
   completed infinite-history event, or a universal no-go when that access is
   absent.

The matched-diffuse result's intrinsic completed event is defined by a limit
of finite-prefix predicates; its finite approximants do not themselves
constitute a completed-event detector. Reverse access can help evaluate a
specified finite predicate coherently when its circuit is available. It does
not collapse the limit or supply uniform physical resources for the completed
predicate.
