# Independent audit: all parameters outside the classical segment

## Conclusion

The proposed lower bound is valid for the labeled doubly-reduced cylinder
algebra, subject to the paper's cylinder-amplitude and singleton-node
definitions. It yields a finite repeatable-block obstruction for every
`p ∈ C \ [0,1]`. Combined with the usual classical transitive-percolation
measure for real `p ∈ [0,1]`, this gives an extension classification for
that labeled algebra. It does not establish the analogous result for the
smaller covariant intersection algebra.

## Exact finite-block argument

Set `a=|p|`, `b=|1-p|`, `t=a+b`, `r=a/t`, and `s=b/t`. For `p` outside
`[0,1]`, the strict triangle inequality gives `t>1`; also `r,s∈(0,1)` and
`r+s=1`.

For a naturally labeled causet `G` on `k` labels, let `L(G)` be its number of
links and `R(G)` its number of strict relations. Write

`N_k=binom(k,2)`, `u(G)=L(G)+min(G)`, and `v(G)=N_k-R(G)`,

where `min(G)` is the number of minimal elements. If `G` is principal, then
`L(G)≥k-1`, `min(G)≥1`, and `v(G)≥0`, so `u(G)≥k` and `u(G)+v(G)≥k`.
The root-seamed cylinder weight is

`B_p(G)=p^{u(G)}(1-p)^{v(G)}`.

Taking absolute values and substituting `a=tr`, `b=ts` gives

`|B_p(G)|=t^{u(G)+v(G)}r^{u(G)}s^{v(G)}
          ≥t^k r^{u(G)}s^{v(G)}`.

Let `X_0,…,X_k` be the transitive closure of the random forward DAG on labels
`0<…<k`, with every possible edge independently present with probability
`r` and absent with probability `s`. For a fixed naturally labeled poset
closure `C`, the probability of obtaining `C` is

`r^{L(C)}s^{binom(k+1,2)-R(C)}`.

Indeed, every link must be an edge, every incomparable pair must be absent,
and all transitively redundant edges among comparable pairs may be either
present or absent; summing their independent probabilities contributes one
for each such pair. If `C` is obtained by putting a new root 0 below a
principal `G` on labels `1,…,k`, then its link count is `L(G)+min(G)` and
its incomparable-pair count is `v(G)`. Thus its probability is exactly
`r^{u(G)}s^{v(G)}`.

These root-seamed closures partition the event

`E_0 ∩ E_k`, where `E_0={0 reaches every other label}` and
`E_k={every label reaches k}`.

For the forward implication, the closure has a unique minimum 0, a unique
maximum k, and its induced causet on labels `1,…,k` is principal. Conversely,
every such root-seamed principal closure satisfies both reachability events.
Consequently

`Σ_{G principal on k labels} r^{u(G)}s^{v(G)} = P(E_0∩E_k)`.

The event `E_0` has probability
`F_k(s)=∏_{j=1}^k(1-s^j)`: expose labels in increasing order, and conditional
on all earlier labels being reachable from 0, label `j` is reachable exactly
when at least one of its `j` incoming edges from earlier labels is present.
Reversing the order gives `P(E_k)=F_k(s)` as well. Both reachability events
are increasing events in the independent edge indicators. Harris's inequality
(positive association for product Bernoulli measures) therefore gives

`P(E_0∩E_k) ≥ F_k(s)^2 ≥ F_∞(s)^2 > 0`,

where `F_∞(s)=∏_{j≥1}(1-s^j)` is positive for `0<s<1`, since
`Σ_j s^j<∞`.

Now append a new universal maximum to each principal `G`, forming
`D=G⊕{top}`. This is doubly principal. With seam weight
`B_p(D)=p^{min(D)}A_p(D)`, where
`A_p(D)=p^{L(D)}(1-p)^{binom(k+1,2)-R(D)}`, the appended top increases
`L` by one, increases `R` by `k`, and leaves `min` unchanged. Hence
`B_p(D)=p B_p(G)`. Summing over this finite family of all size-`k`
principal `G` gives

`W_{k+1}(p)=Σ_D |B_p(D)|
             =a Σ_{G principal}|B_p(G)|
             ≥a t^k F_∞(s)^2`.

For each fixed `p∉[0,1]`, `a>0`, `t>1`, and `F_∞(s)>0`; choose finite `k`
large enough that `W_{k+1}(p)>1`.

## Repetition and extension obstruction

Repeat blocks `D_1,…,D_m`, each selected from the finite size-`k+1`
doubly-principal family, above one initial root by ordinal sum. The endpoint
at level `1+(k+1)m` is doubly principal: deleting its final universal top
leaves the preceding principal prefix ordinal-summed with the principal
`G_m` prefix of the last block. Distinct block tuples give distinct labeled
cylinders because each block occupies a fixed label interval.

At each seam, the previous block's unique maximum is below all labels in the
next block. Its links go exactly to that block's minimal elements; all other
cross-block relations are present and contribute no absent-pair factor.
Thus the full endpoint amplitude factors as

`A_p(C_m)=∏_{j=1}^m B_p(D_j)`.

Every selected endpoint is a singleton node in the labeled doubly-reduced
tree. The disjoint family therefore contributes

`S_{1+(k+1)m}^{(p)} ≥ Σ_{(D_1,…,D_m)}|A_p(C_m)|=W_{k+1}(p)^m`.

Since `W_{k+1}(p)>1`, these level sums are unbounded. Any finite complex
measure extending the prescribed cylinder amplitudes would have finite total
variation on the whole sample space, bounding the sum of absolute values on
every disjoint finite family. This contradiction rules out such an extension
to the labeled doubly-reduced sigma-algebra for every `p∉[0,1]`.

For real `p∈[0,1]`, the independent-edge construction itself gives the
classical probability measure with the prescribed cylinder values, including
the degenerate endpoint measures. Thus the conclusion is an if-and-only-if
classification for extension of this prescribed complex-percolation
cylinder premeasure to the labeled doubly-reduced algebra.

## Proof-failure checks and limits

- No normalization factor is missing: `r^{u}s^v` is exactly the probability
  of the root-seamed closure. The exponent `u` includes the root's `min(G)`
  cover edges, while `v` counts exactly the incomparable pairs.
- The inequalities use `t^{u+v}≥t^k`; this follows from
  `u=L+min≥(k-1)+1=k` and `v≥0`. It does not require a sharper relation
  between links and incomparable pairs.
- The reachability events are both increasing in the same independent edge
  coordinates, so Harris applies in the stated direction. The endpoint
  product lower bound is uniform in `k` and strictly positive at each fixed
  `s∈(0,1)`.
- The selected family is finite for each chosen `k`, even though its size
  grows with `k`; once `W>1`, its repeated ordinal sums supply the unbounded
  sequence of disjoint finite families.
- The conclusion concerns the labeled doubly-reduced sigma-algebra generated
  by doubly-principal cylinders. It does not imply nonextension to the
  covariant intersection algebra, where these labeled cylinders need not be
  events individually. It also does not exclude other quantum measures or
  decoherence functionals.
- This is an independent proof audit, not a global priority claim. The direct
  predecessor and the scope caveat are documented in
  `causal-set-ordinal-module-review.md`.
