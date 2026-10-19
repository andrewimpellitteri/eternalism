# Peer review: ordinal-module lower bound for reduced-poscau extension

**Review date:** 2026-10-19. **Scope:** independent mathematical audit of the
finite-gadget proposal against Dowker–Zalel, arXiv:2212.01149v2. Primary
source read: full text at the relevant sections (III.2–III.4 and V), with
equations and event-algebra definitions checked. This is a peer-review note,
not an integration or priority decision.

## Verdict

The ordinal-module argument is sound for a bounded complex measure on the
**labeled reduced-poscau sigma-algebra** if the finite family is counted as
naturally labeled gadgets and the reduced-tree cylinder amplitudes are those
fixed in the paper. A single finite family with total absolute module weight
`r>1` yields an exponentially growing family of pairwise disjoint cylinder
events along a subsequence of levels. The extension criterion then fails.
There is no need to prove the paper’s conjectured eventual formula for
`ζ_n^min` or its doubly-reduced analogue.

I found no fatal cancellation or multiplicity flaw. The material scope limit
is important: this proves non-extension on `\tilde{R}_b` or `\tilde{R}_p`,
depending on the gadgets, and does **not** by itself prove non-extension on
the covariant intersection `R_b` or `R_p`. The principal cylinder events are
label-sensitive. The post/doubly-principal construction therefore resolves a
specific case of the paper’s question for `\tilde{R}_p`, not automatically the
physical covariant algebra or a general decoherence-functional existence
question.

## Primary-paper details that matter

Dowker and Zalel define the labeled cylinders and their amplitudes in
arXiv:2212.01149v2, Eq. (26), as

`A(C_n) = p^{L(C_n)} q^{binom(n,2)-R(C_n)}`, `q=1-p`,

with `L` the number of links and `R` the number of strict relations. In
Sec. III.3 they state that principal causets are never merged in reduced
poscau: each is a node on its own and corresponds to its principal cylinder
(HTML §§III.3, paragraphs around Fig. 5; paper pp. 9–10). Non-principal nodes
are the coarse-grained remainder that completes the node-sets to a semiring.
For doubly-reduced poscau, Sec. V says to replace “principal” by “doubly
principal”; only these cylinder nodes remain singletons (HTML §V, theorem 14
and following paragraphs; pp. 15–16).

The extension test used in the paper is `sup_n S_n < ∞`, where
`S_n = Σ_{D_n at level n} |A(D_n)|` on the relevant tree. It is necessary for
finite complex-measure extension; their Sec. V applies the criterion to
`\tilde{R}_p` and reports inconclusive bounds because the all-node minimum
vanishes at valency-one nodes (Eq. (31) and discussion, HTML §V). The proposed
lower bound bypasses that obstacle by summing a selected set of singleton
nodes, all of which have valency irrelevant to their contribution to `S_n`.

## General lemma and proof audit

Let `F` be a finite family of size-`k` principal natural-label causets `G`.
Attach each `G` above a single root by ordinal sum, and define

`A(G) = p^{L(G)} q^{binom(k,2)-R(G)}`,
`B(G) = p^{min(G)} A(G)`,
`r(F) = Σ_{G∈F} |B(G)|`.

Here `min(G)` is the number of minimal elements. The root is below every
element of `G`; its only new links go to the minimal elements of `G`, so its
link count adds exactly `min(G)`. It adds `k` relations and `k` possible
pairs, hence it adds no `q` exponent. Thus `B(G)` is exactly the CT cylinder
amplitude of `root ⊕ G`.

If `G_1,…,G_m∈F`, form
`C(G_1,…,G_m)=root ⊕ G_1 ⊕ … ⊕ G_m`. Each checkpoint after a gadget is
principal: the last gadget has a unique maximum, and ordinal sum places every
earlier element below it. The map from tuples to naturally labeled
checkpoints is injective because the fixed label intervals recover each
induced block. The cross-block relations contribute no `q` factors; links
from the preceding unique maximum to the next gadget are exactly its minimal
elements, already counted in `B(G_i)`. Therefore

`A(C(G_1,…,G_m)) = ∏_i B(G_i)`.

At level `1+mk`, these distinct principal cylinder nodes are pairwise
disjoint and each is a singleton node in reduced poscau. Consequently

`S_{1+mk} ≥ Σ_{(G_1,…,G_m)∈F^m} |∏_i B(G_i)| = r(F)^m`.

If `r(F)>1`, the subsequence `S_{1+mk}` is unbounded, so no finite complex
measure can extend the prescribed cylinder premeasure to that reduced
sigma-algebra. Equivalently, under any purported finite complex measure the
variation of the disjoint family at each such level would be at least
`r(F)^m`, contradicting finite total variation on the whole space.

This also answers the finite-`k` question: a finite witness suffices because
the same gadget family can be repeated arbitrarily many times. No finite
truncation by itself would suffice; the repeatable ordinal-sum closure is the
step that turns it into an infinite-level obstruction.

### Post / doubly-principal version

Let `D=G ⊕ {top}` be obtained by adjoining a new universal maximum to a
principal `G` of size `k`. Then `D` is doubly principal: it has a unique
maximum, and deleting its last label leaves `G`, which is principal. The
amplitude for the root-attached block is

`B(D) = p^{min(D)} A(D) = p B(G)`,

because `min(D)=min(G)` and adding the top adds one link (from the former
unique maximum). More generally, for size `k`,
`R(D)=R(G)+k`, `L(D)=L(G)+1`, and `binom(k+1,2)-R(D)=binom(k,2)-R(G)`.

Repeating size-`k+1` doubly-principal blocks above one root gives checkpoints
at `n=1+(k+1)m`. Each endpoint is doubly principal: dropping its final
element leaves the preceding principal prefix ordinal-summed with the
principal `G` prefix of the last block. Distinct block tuples again give
distinct, disjoint doubly-principal cylinder nodes. The seam from the
preceding maximum to each `D_j` contributes exactly its minimal-element links,
so the full checkpoint amplitude is `A(C_m)=∏_{j=1}^m B(D_j)`. Thus the bound is
`S_{1+(k+1)m}^{(p)} ≥ (|p| r(F))^m`.

The same proof works for the proposed 40-block family. Its members are
`D=G⊕{top}` for each of the 40 naturally labeled principal causets `G` of
size 5. It establishes failure of extension to the labeled doubly-reduced
algebra `\tilde{R}_p` whenever `|p|r_5>1`.

## Exact finite calculation at `p=(1+i)/2`

For this parameter, `|p|=|q|=1/√2`. Enumerating all transitive relations on
labels `0,…,4` with every `i<4` related to `4` gives the 40 naturally labeled
principal size-5 gadgets. The exponent

`E(G)=L(G)+min(G)+10-R(G)`

has multiplicities `{5:1, 7:3, 8:6, 9:4, 10:11, 11:8, 12:6, 14:1}`. This is
a small exact enumeration: examine the `2^10=1024` upper-triangular relation
masks, reject non-transitive masks, require all four relations into the top,
then count covers, minima, and relations. The multiplicities sum to 40.

Therefore

`r_5 = Σ_G 2^{-E(G)/2} = 105/128 + 9/(8√2) ≈ 1.6158076288 > 1`.

This directly gives `S_{1+5m}^{(b)} ≥ r_5^m` and rules out extension to
`\tilde{R}_b` at this parameter. For posts, append a universal top to each
gadget. The size-6 doubly-principal block weight is

`r_6^{(p)} = |p| r_5 = 9/16 + 105/(128√2) ≈ 1.14255 > 71/64 > 1`,

where the strict bound follows from `√2 < 3/2`. Thus
`S_{1+6m}^{(p)} ≥ (r_6^{(p)})^m`, ruling out extension to the labeled
`\tilde{R}_p` for `p=(1+i)/2`. The exact check and finite enumeration were
reproduced independently with Python’s standard library; no external package
or large run was used.

## Smaller two-gadget check

There is also a hand-checkable size-4 doubly-principal family with only two
members:

- chain `D_1` on four labels: `B(D_1)=p^4`;
- two incomparable minima below a cap, with a new top above the cap,
  `D_2`: `B(D_2)=p^5q`.

Both are doubly principal. Repeating only these two types gives
`W_4=|p|^4+|p|^5|q|=a^4(1+ab)`, where `a=|p|`, `b=|q|`. For
`p=(1+i√3)/2`, `q=(1-i√3)/2`, both moduli are one, so `W_4=2` and the
variation grows at least as `2^m` on levels `1+4m`. This is a valid, simpler
non-extension region, but it is less discriminating: here the percolation
parameters themselves have unit modulus. At `p=(1+i)/2`, the same family has
`W_4=3/8<1` and says nothing; the 40-gadget size-6 family is the stronger
interior-modulus witness. The two-gadget result should therefore be presented
as an elementary check or corollary, while the 40-gadget result is the
substantive exact instance.

## Cancellation, multiplicity, and event-algebra audit

- **No coarse-graining cancellation in the bound.** Reduced poscau does merge
  non-principal causets into remainder nodes. But every principal causet stays
  in its own node, whose event is its labeled principal cylinder. The selected
  cylinders contribute their individual `|A(C)|` terms to `S_n`; amplitudes
  in a different merged node cannot cancel those absolute values.
- **Count label multiplicity.** The 40 gadgets are naturally labeled
  causets, not 40 unlabeled isomorphism classes. Distinct relation masks
  define distinct labeled cylinders even when two masks are isomorphic as
  abstract posets. The block interval labels make tuple-to-cylinder
  injectivity explicit.
- **No hidden interference among tuples.** At fixed `n`, distinct labeled
  prefixes define disjoint cylinder events. `S_n` sums their absolute
  amplitudes, not the modulus of their aggregate sum. This conclusion would
  not transfer unchanged to a quotient event formed by summing over
  relabelings.
- **Precise target.** The construction gives singleton nodes and disjoint
  events in `\tilde{R}_b` or `\tilde{R}_p`, which are generated by labeled
  principal/doubly-principal cylinders. A principal cylinder is generally
  label-sensitive and is not itself in covariant `R_b`/`R_p`. A finite complex
  measure on the smaller covariant intersection might still exist; the proof
  does not address it.
- **Interpretive limit.** Failure of this extension blocks the paper’s
  specified complex-measure construction on that labeled sigma-algebra. It
  does not show that no other quantum measure or decoherence-functional
  model exists, and it is not a claim about temporal ontology.

## Novelty and post-2023 search

The direct predecessor is Dowker & Zalel, “Observables for cyclic causal set
cosmologies,” arXiv:2212.01149v2 (17 July 2023), *Classical and Quantum
Gravity* 40 (2023) 155015. In Sec. III.4 they explicitly ask whether complex
transitive percolation extends to `\tilde{R}_b`; their reduced-tree numerical
work for levels 2–4 suggests an eventual lower bound on `ζ_n^min`, but is
presented as a suggestion, not a proof. In Sec. V they explicitly say their
application of the doubly-reduced criterion is inconclusive: the maximum
bound cannot prove extension, while the minimum criterion is null on
valency-one nodes; their Eq. (31) leaves the correction term to be controlled.
The ordinal-module proof is a different, explicit lower bound on `S_n` and
does not need those asymptotic conjectures. This appears to answer a precise
open question stated by the predecessor for one parameter value.

Targeted post-2023 searches for `reduced poscau`, complex transitive
percolation extension, doubly-reduced extension, and causal-set complex
measure found no direct published ordinal-module argument. A 2025 IISER Pune
master’s thesis by Ritesh Srivastava, *A study of quantum sequential growth
dynamics, observables in causal sets and renormalization*, has an abstract
covering quantum sequential growth, observables, measures, and repeated
collapse/refolding; only its repository abstract was checked, so its relevant
chapters remain a close unresolved lead. Ritesh Srivastava & Sumati Surya’s
2026 preprint *Implementing Bell causality in Quantum Sequential Growth*,
arXiv:2603.25503v1, is at abstract depth here and concerns noncommuting
transition operators and Bell-causality implementations, not the scalar
complex-percolation extension question in its abstract. Search absence is
not priority evidence; the thesis body, later versions/citing papers, and
authors’ follow-up work should be checked before any priority claim.

Primary locators:

- [Dowker & Zalel, arXiv:2212.01149v2](https://arxiv.org/html/2212.01149v2),
  §§III.2–III.4 and V; especially Eqs. (23)–(26), (29)–(31).
- [Surya & Zalel, arXiv:2003.11311v1](https://arxiv.org/abs/2003.11311v1),
  cited by Dowker–Zalel for the complex-measure extension criterion. Not
  independently re-audited in this subtask.
- [Srivastava, IISER Pune repository thesis record](https://dr.iiserpune.ac.in/items/2590b360-1407-43c1-8cec-6dfdc62ed936),
  abstract only here.
- [Srivastava & Surya, arXiv:2603.25503v1](https://arxiv.org/abs/2603.25503v1),
  abstract only here.

## Peer-review conclusion for the coordinator

I recommend the coordinator treat the 40-gadget argument as a valid exact
bounded-parameter theorem **conditional on the paper’s reduced-tree
amplitude assignment**, and present the 40 labels, exponent table, injection,
factorization, and target algebra explicitly. A short independent derivation
of the standard `sup S_n` extension criterion’s applicability to this tree
would make the proof self-contained, although Dowker–Zalel state it in Sec. V.
Do not claim the result settles extension on `R_p`, arbitrary complex `p`,
the general doubly-reduced family, or quantum dynamics outside this specific
complex-measure construction. The source itself identifies this narrow
extension problem as unresolved, but the targeted post-2023 prior search is
not exhaustive.
