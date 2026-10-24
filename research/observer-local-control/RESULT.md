# Causal-past access boundary for the heralded growth register

24 October 2026. Finite control result for a declared observer access model;
not a claim about physical causal-set locality, a universal observer no-go, or
temporal ontology.

## Model and criterion

At a fixed growth step, let a global parent history be `C`, its available
precursor labels be `P(C)`, and its scalar transition row be
`t_C(P)=q(C)w(P)`. A finite observer is assigned a carrier `O`, a record
`r(C)` consisting of the induced causal order on `O` plus a named finite memory
state, and an output register whose precursor labels are drawn from a common
finite alphabet. A spectator extension may change `C` and `P(C)` while leaving
`r(C)` fixed. The declared access rule permits a control to depend only on
`r(C)`; it cannot query the rest of `C`, the spectator, or the global list of
available precursors.

For the predecessor's heralded encoding, pad absent precursor labels with zero
and put `s_C=sum_P |t_C(P)|`. A successful parent-conditioned output is

`|v_C> = sum_P sqrt(|t_C(P)|/s_C) phase(t_C(P)) |P>`.

The success probability with the predecessor's common bound `B` is `s_C/B`.
Consequently:

* For a record-only controller to produce the same *conditional output state*
  on every global history with record `r`, the vectors `v_C` must agree up to
  an overall phase (for an isolated parent branch). If parent branches remain
  coherently controlled, those phases must also agree relative to the other
  branches, or be present in the allowed memory/control data.
* To reproduce the same heralded instrument, including its success/failure
  flag, `s_C` must also be a function of `r` (with the same `B`).

These are necessary conditions by equality of the output state and flag
probability. They are sufficient as finite abstract controls when the shared
conditional vector and success amplitude can be prepared from the accessible
record with the allowed ancillas. They say exactly what the matrix-level
construction requires from access; they do not say that those operations are
available as local matter dynamics.

## Abstract control and restricted realization

The checker gives two global parent contexts with the same observer record.
Both scalar rows sum to one and have total variation `s=1`, so herald flags
alone cannot distinguish them. In the first context both precursor labels
`p0,p1` are available, with `q=1/2` and `w(p0)=w(p1)=1`, giving row
`(1/2,1/2)`. In the second, a hidden spectator changes the globally available
set to `{p0}`; `q=1` and the restricted row is `(1)` (padded as `(1,0)` on the
common output alphabet). The conditioned square-root outputs have overlap
`1/sqrt(2)<1`. Thus one control selected only by the common local record cannot
implement both claimed conditional rows, even though both heralding rates are
identical. This is a finite abstract access counterexample in the `q(C)w(P)`
form. It is not asserted to be an actual pair of causets in the matched model.

A clean restricted case works: if all global histories sharing a record have
the same available precursor alphabet and same transition row, the controller
prepares that shared row state and (when required) its shared success
amplitude. More generally, multiplying a row by a common nonzero factor leaves its
conditioned state ray unchanged. Its modulus changes the
herald rate, and its phase is a parent-controlled phase: it is unobservable on
an isolated parent branch but can affect interference between coherent parent
branches. Therefore common spectator factors may be discarded for conditional
relative transition data, but not automatically for the full instrument or a
coherent multi-parent dilation. Nonunit scaling of a complete sum-one row
generally violates MSR; this algebraic observation applies to relative data
or restricted pieces, not automatically to another admissible full MSR row.

## Actual matched-model witness added during coordinator review

The original worker submission supplied only the abstract control above. The
coordinator checked its scope and added an actual same-size pair:

    C=(0,0,1),       D=(0,1,1),       observer o=2.

Both have the SAME closed observer past R={0,2}, with relation 0<2, and the
same assigned memory/global stage n=3. Vertex 1 is outside that past. In C
it is isolated; in D it lies above 0 and remains incomparable with observer 2.
The precursor P={1} (mask 2) is an ideal in C but not D: in D, selecting 1
without its predecessor 0 is invalid. The actual transition magnitude in C
is |q(C)w(single)|=L^-3=10^-9, while the corresponding padded coordinate in
D is zero. Thus the normalized global row states differ. Their relative
phase cannot remove this support mismatch. One controller given only the
identical local record cannot prepare both global precursor-register outputs.

This is a counterexample for the declared record-only controller and its
common output alphabet. It is not a universal locality obstruction: an
ambient system may carry global information and respond to it through its own
dynamics without the observer querying it. Those interactions are excluded
from this access contract, not disproved by the example.

There is a clean actual-model counterpart. Restrict output precursors to
ideals P contained in the closed past R. R is a down-set, so these are exactly
the ideals of its induced order. Define

    W_j(R)=sum_(P ideal R) |w_j(P)|.

On this subset the normalized row has coefficients

    sqrt(|w_j(P)|/W_j(R)) phase(w_j(P)) phase(q_j(C)).

The conditional state ray depends only on the induced R and fixed model
parameters. The global q factor drops out of relative row data. Its phase
remains relevant to a coherent superposition of different global parents.
Its modulus remains in the absolute success rate. The checker verifies both
the failed global row and the shared restricted row in models A and B.

## Exact past-size/branch-mass boundary

For n=|C|>=3 and any down-set R of size k, restricting the ORIGINAL global
success Kraus map to precursors P contained in R gives squared column norm

    p_local(C,R)=L^-n W_j(R)/B_n,        B_n=1+zeta_n.       (1)

This follows directly from t(C,P)=q(C)w(P) and |q(C)|=L^-n. It is the joint
probability of a successful growth flag and a retained precursor in R for
that basis parent; it is not a probability conditioned on that local event.

For k>=3 the same scalar row rule on the induced R implies

    W_j(R)=L^k s_j(R),       1<=s_j(R)<=B_k,
    p_local(C,R)=L^(k-n) s_j(R)/B_n
                 <=L^(k-n) B_k/B_n <(9/8)L^(k-n).          (2)

Here B_k<9/8 follows from zeta_k<=Z<1/8. For fixed k<3, W_j(R) is a finite
seed constant and (1) still gives exponential decay. Thus fixed-size past
access loses the full-register nonvanishing-success guarantee IN THIS
restricted-precursor implementation. More generally an unbounded deficit
n-k forces these retained-branch probabilities to zero. A uniform positive
retained-branch rate requires that deficit stay bounded (in this family).
For example, with k>=3 even one omitted vertex gives an upper bound below
0.001125; a retained-branch probability of at least 1% requires k=n.

The statement extends to arbitrary coherent inputs on parents with the same
past-size cap: child supports are disjoint, so the restricted K* K is diagonal
with the probabilities (1) on its diagonal. There is no interference that
can increase their maximum. It does not extend to arbitrary observer models
or alternative local instrument normalizations.

A concrete spectator family is C_n=(0,0,3,0,...,0), with observer 2 having
fixed three-element past R=(0,0,3). Extra births are isolated outside its
past. The checker evaluates (1) and (2) for n=3,4,5 in both models, using
content-pinned actual transitions. Renormalizing the restricted map can
produce a useful conditional local experiment, but changes the global
instrument and its calibration. Likewise an observer with a growing past,
a different coupling, or a different register may evade this named bound.
No matter dynamics, gauge action or physical impossibility theorem is supplied.

## Relation to the accepted construction and prior work

The accepted `observer-sequential-dilation/RESULT.md` proves the global finite
Kraus map and failure completion using `sqrt(|t|/B) phase(t)`, and explicitly
does not derive a physical local coupling. Its independent review checks the
finite protocol conditional on the transition recursion and row bounds. The
present result adds an access criterion: stage-by-stage parent control is
observer-local only if the relevant normalized row, norm and coherent relative
phase factor through the declared observer record. It does not repeat the
predecessor's deterministic parent-marginal obstruction or its diagonal-record
no-go.

Primary predecessors inspected in the accepted task record: Ozols, Roetteler
and Roland, arXiv:1103.2774v3, Sec. 4.1 Eqs. (11)–(15) (coherent acceptance
rotations) and Sec. 4.2 Eq. (16) (inverse preparation); Gudder,
arXiv:1204.5767v1, Sec. 5 Eq. (5.1), Theorem 5.1 and proof (amplitude
sequential growth). Their named passages are recorded at full-text depth in
`observer-sequential-dilation/sources.jsonl`; this worker relies on that
reviewed source record and does not claim a new theorem from either paper.
The use here is an elementary finite information-factorization criterion,
checked directly below, rather than a claimed result of those sources.

## Limits

The actual model witness and branch-mass identity concern a specified
finite history-register access contract. They do not show that the coherent
branch phases or global precursor output register are physically accessible.
A physical local realization still requires a
physical tensor-factor/algebra assignment, local couplings, memory update rule,
and symmetry-compatible controls. No empirical prediction, efficiency claim,
novelty claim, or temporal-ontology conclusion follows.
