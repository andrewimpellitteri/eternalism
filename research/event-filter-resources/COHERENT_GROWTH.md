# A finite coherent realization on the known norm-matching circle

Coordinator derivation, 21 October 2026. Application of the accepted circle
identity, not a new parameter classification. Independent review pending.

## Construction

Represent a naturally labelled n-causet C as an orthonormal register ket |C>.
For a down-set D of C, append a new maximal birth whose past is D, giving C_D.
Let m(D) count maximal elements of D. Use the prescribed amplitude

 t(C,D)=p^m(D) q^(n-|D|),      q=1-p.

Define V_n|C>=sum_D t(C,D)|C_D>. Distinct parents have disjoint sets of
labelled children: deleting the last birth uniquely recovers the parent.
Consequently V_n^dag V_n is diagonal, with entry sum_D |t(C,D)|^2.

**Proposition.** These maps are isometries for every stage iff
|p|^2+|1-p|^2=1.

Necessity follows already from the one-element parent, whose two transition
amplitudes are p and q. For sufficiency, put r=|p|^2 and s=|q|^2=1-r.
Then |t(C,D)|^2=r^m(D) s^(n-|D|), the ordinary real-percolation probability
of the new element having exactly past D. Its sum over down-sets is 1.
Combined with disjoint child supports, this proves the proposition.
This is the same norm-matching circle as the project's L² indicator measure;
the finite coherent register realization does not strengthen that classification.

Starting with the empty causet gives a normalized finite state
|psi_n>=sum_C A_p(C)|C>, retaining the labelled complex coefficients.
For any finite cylinder union E at this level, projecting onto
|chi_E>=sum_{C in E}|C>/sqrt(|E|) has probability

 P(success)=|sum_{C in E} A_p(C)|^2 / |E|.

Thus a finite quantum simulator can reproduce the scalar quantum measure by
event-dependent calibrated readout. The full-register probability for E prior
to erasure is instead sum_E |A_p(C)|^2. These are different measurements.

## Exact finite check

`check_causal_growth.py` independently builds all down-sets and labelled children
through n=6. Counts: 1,2,7,40,357,4824. At p=(1+i)/2 it verifies for every parent
that squared transition norms sum to one; distinct columns have disjoint
supports; full-level squared norm and summed scalar amplitude both equal one.
Every comparison uses rational real and imaginary parts.
The analytic proposition, rather than these finite checks, covers all n.

## What this does and does not solve

The simulator preserves finite complex coefficients coherently. It does not
supply an infinite scalar measure with prescribed completed-event values.
Orthogonal history storage has different decoherence data from the rank-one
scalar process; a later erasure filter reconstructs finite scalar event values
through a modified measurement. It is not an identification of those processes.

An isometry is abstractly implementable by a larger unitary; efficient circuit
synthesis, locality, covariance of accessible questions, and internal observers
are not supplied by this construction. The stage-labelled register and its
projectors are external simulator resources. Applying RECORD_LOSS.md to a
specified leakage channel gives a laboratory access restriction, not yet a
physical constraint on causal-set cosmology.

Outside the circle, preserving all these coefficients while keeping every
parent column normalized requires heralding or a changed encoding. Parent-wise
renormalization changes the amplitude rule. No statement excluding other
physical representations follows from the isometry calculation.
