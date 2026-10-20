# Independent replication: edge-mask route to the two-cap result

Status: 2026-10-20. Probe `independent-replication`. This is a second
implementation of the finite combinatorics and the Dirac witness, deliberately
not using the baseline's poset enumeration as the derivation. It does **not**
re-prove the all-level analytic inequality; it checks the identities and values
at finite levels and records that boundary.

## Route

Baseline (`experiments/baseline/poscau.py`): enumerate relation masks on
`n` naturally labelled vertices, filter for transitivity, and sum amplitudes.

This replication: enumerate all **edge subsets** on `n` vertices, take the
transitive closure, deduplicate by the resulting **labelled** relation set, and
compute from the closures. The endpoint probability is computed directly from
edge subsets with exact rational weights `r^e s^{binom(n,2)-e}`. The two-cap
map and the Dirac history are re-implemented independently.

## Checks

1. **Endpoint identity.**
   `P_k = Σ_{edge subsets on k+1 vertices} [last vertex above all earlier] r^e s^{binom(k+1,2)-e}`
   equals `∏_{j=1}^k (1-s^j)` exactly, for `k=1..5` at
   `r=1/2, 2/5, 1/3` (exact `Fraction` arithmetic). This is the identity used in
   the two-cap bound, checked via the edge-subset route rather than the
   baseline's poset amplitudes.

2. **Two-cap decomposition.**
   For `k=1..4`, the set of labelled two-caps `G⊕{u}⊕{v}` of all labelled
   `k`-orders equals the set of labelled doubly-principal `(k+2)`-orders:
   counts `1, 2, 7, 40` — PASS.

3. **`V_5`, `V_6` at `p=(1+i)/2`.**
   Summing `|A_p(C)|` over labelled doubly-principal orders from closures:
   `V_5 = 1.015165042945`, `V_6 = 2.184089780164`, with `7` and `40` orders.
   Matches the exact `Q(√2)` values `3/4+3√2/16` and `31/32+55√2/64`.

4. **Dirac history.**
   Independent construction of `(A_2⊕{z_1})⊕(A_2⊕{z_2})⊕…` for `j=1..3`:
   each post past is principal but not doubly principal; the history has
   infinitely many posts. PASS.

## Discrepancy found and corrected

The first run canonicalized closures up to **unlabeled** isomorphism, which
conflated different natural labelings (e.g. the three two-element chains) and
gave `V_5=0.765165`, `5` doubly-principal orders instead of `7`. The paper's
`V_n` sums over **naturally labelled** causets, each once; the fix is to
deduplicate closures by the labelled relation set, not by isomorphism class.
After the fix all values match. This is recorded because it is a plausible
replication error, not a defect in the theorem.

## What this does and does not establish

- It independently reproduces the finite decomposition, the endpoint identity
  at `k≤5`, the `V_5/V_6` values, and the Dirac countermodel.
- It does **not** re-prove the all-level inequality
  `V_{k+2} ≥ |p|(|p|+|1-p|)^k c_s` for every `k`; the analytic two-cap proof
  and the infinite product remain the original argument, audited in
  `research/creative/proof-audit/AUDIT.md`. Finite checks are not a quantifier
  extension.
- No priority, physical or ontological claim is made.

## Known-result reduction

- At `p=1/2` the endpoint weights are real probabilities; the identity reduces
  to the classical post-probability product.
- At `p=(1+i)/2` the finite amplitudes reproduce the selected certificate.
- The scalar no-go's all-level step is still the analytic bound, not this
  script.

## Files

- `research/replication/replicate.py` — edge-mask enumeration, endpoint
  probability, two-cap set check, `V_n`, Dirac witness.
- `research/replication/AGENT_REPORT.md` — this report.

Standard library only; no installs; no board edits.

Run: `python3 replicate.py`.
