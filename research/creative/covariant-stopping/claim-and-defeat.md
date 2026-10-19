# Covariant stopping, record quotients, and reduced-poscau extension

Status: research note, 2026-10-19. The stopping-time and hidden-record hypotheses below were defeated. A quantum-measure pivot yields an exact all-parameter obstruction: for every complex transitive-percolation parameter p outside [0,1], the cylinder premeasure does not extend to the labeled doubly-reduced poscau sigma-algebra, and hence does not extend to the larger labeled reduced-poscau sigma-algebra. The proof uses ordinal concatenation of doubly-principal blocks, with a finite 5-element gadget certificate as an exact check at one interior-disk parameter. Priority is unverified. No conclusion about temporal ontology follows.

## Two hypotheses considered

**H1 — “A covariant finite stopping rule can expose growth order missing from the unmarked completed causet.”** Interpret a rule as a finite stopping time on naturally labelled histories, with the local decision at stage n depending only on the isomorphism class of the n-element prefix. Candidate rule: stop when a 2-element antichain first occurs as a stem. The stop *event* is covariant: an unmarked completed causet has some such stem exactly when the rule eventually fires. But its stop index need not be a function of the completed unmarked causet; a three-element counterexample below falsifies that stronger conclusion. This is a real access distinction in the representation, but the conditional law of the index given the finite terminal order is fixed by order-invariance and hence is not a surviving new dynamics result.

**H2 — “A physically marked observer changes conditional ancillarity while its record still descends to the unmarked completed-history algebra.”** Rejected as internally inconsistent absent a special quotient. For a deterministic mark/record observable R on marked histories (M,μ), descent through the forgetful map π(M)=C requires R to be constant on every π-fiber (up to null sets). If two physically distinct marks over the same C produce different R, R is not an observable of the unmarked algebra. If the mark is instead a covariant instrument whose conditional kernel depends only on the unmarked causal order, adjoining that kernel to the CSG path law does not make birth order informative about coupling parameters after conditioning on C. A feedback instrument can change the growth law, but then it changes the model and leaves the CSG/DGC premise; it is not an observer-access counterexample within that premise.

## Exact finite witness: a local covariant hit does not give an invariant stop index

Let terminal C be the 3-element poset with exactly one relation, a < c, and isolated b. The three natural labellings are indexed by the position pair of the comparable elements: (0,1), (0,2), (1,2). Define τ to be the first n such that the n-element prefix contains a 2-element antichain as a stem. At prefix size 2:

| Comparable labels | First two births | τ |
|---|---|---:|
| (0,1) | chain | 3 |
| (0,2) | antichain | 2 |
| (1,2) | antichain | 2 |

For every covariant CSG law with positive weights on these paths, discrete general covariance gives equal path weight within this unlabelled terminal class. In standard CSG notation with t0=1, t1>0 and t2≥0, each has probability

    p(C-labelled) = t0 t1 / ((t0+t1)(t0+2t1+t2)).

For t=(1,1,1), this is 1/8 per path and total class weight 3/8. For t=(1,2,10), it is 2/45 per path and total class weight 2/15. In either case

    P(τ=2 | C) = 2/3,   P(τ=3 | C) = 1/3.

Thus τ is not a function of the unmarked terminal C, while the conditional distribution of τ given C is independent of the couplings. The distinction is between a history-level stopping time and a completed-order observable. A local “first hit” rule does not manufacture a covariant integer-valued stage observable.

**Proof for the general finite claim (not a novelty claim).** Fix n and an unlabelled finite poset C. Its naturally labelled realizations are its linear extensions with labels 0,…,n−1. Under discrete general covariance, each such path has the same probability p(C). Therefore, conditional on C (when p(C)>0), all its distinct natural labellings are uniform. Any finite stopping time τ adapted to the natural-label filtration is a function on these extensions, so for every k its conditional probability is

    P(τ=k | C) = #{natural labellings π of C with τ(π)=k} / #{natural labellings of C}.

The right side contains no CSG couplings. This applies to any finite prefix-adapted rule, including a rule with finite horizon N; it does not assert that τ itself descends to C. It also does not extend by itself to a measure on infinite completions, a quantum measure, or a growth law that violates DGC.

The smallest witness was checked by direct enumeration of the three natural extensions and exact fractions above. The conditional-law assertion is proved algebraically from equal path weights. It is not an optional-stopping theorem and requires no Markov claim beyond the CSG path law; no claim is made that a non-Markov process lacks a path-space measure.

## Six-part novelty contract

1. **Exact question / result.** Does a locally isomorphism-invariant finite stopping rule yield a stage observable on the completed unmarked causet? No in general. For any finite DGC growth law, its conditional distribution given the terminal unlabelled order is coupling-independent; its realized stage need not be determined by that order. Three-element witness above.
2. **Nearest primary predecessors and comparison.**
   - Rideout & Sorkin, *Classical sequential growth dynamics for causal sets*, arXiv:gr-qc/9904062v3 (full-text read in the integrated causal-set lane; §§3–5, esp. DGC/path independence and stage weights). Assumes internal temporality and DGC in a sequential law, plus Bell causality for the classified family. Establishes equal path probabilities for natural labellings of a finite causet and classifies CSG weights. Our conditional formula is a direct finite consequence, not a new premise or result.
   - Brightwell, Dowker, García, Henson & Sorkin, *“Observables” in causal set cosmology*, arXiv:gr-qc/0210061v2 (full text previously read in integrated lane; Theorem 1 / stem-set discussion). For CSG, characterizes the covariant observable algebra, generically up to null sets, through stem events. A “there exists a stem P” hit event is already a standard covariant observable. It does not assign a physical integer to the first stage at which P appeared.
   - Brightwell & Luczak, *Order-invariant measures on causal sets*, arXiv:0901.0240v3 (full-text read, §§1 and 3–4; published Ann. Appl. Probab. 21(4), 1493–1536 (2011), DOI 10.1214/10-AAP736). Explicitly states that if one stops after a fixed number of steps, then conditioned on the causal-set structure, each possible order of generation is equally likely; it identifies this order-invariance with Rideout–Sorkin general covariance. This occupies the central conditional-uniformity statement, including arbitrary growth processes in its framework. Our arbitrary adapted stopping-time expression is the finite counting corollary of the same conditional uniformity; H1 has no novelty claim left.
3. **What changes / why it matters.** The only precise extra observation is that the hitting time is not a quotient observable, even when the hit event is. The three-element example separates (i) the covariant proposition “a 2-antichain stem occurs” from (ii) the non-descending stage at which it first occurs. This is a useful counterexample to an overly strong access claim, but is elementary and substantially anticipated by the predecessors above. No physical observer instrument is specified by standard CSG.
4. **Smallest reproducible example / independent check.** Exactly three elements, with one comparable pair and one isolated element. Enumerate the three linear extensions. The counts yield 2/3 and 1/3. The displayed CSG path weights were independently checked by multiplying the t-family transition weights. Standard-library exact arithmetic; no dependencies or large runs.
5. **Falsifier / novelty defeater.** Strongest defeater already found: Brightwell–Luczak 0901.0240 says the conditional uniformity at fixed stopping size explicitly, and the proposed all-stopping-times law follows by summing/counting subsets of linear extensions. A prior paper explicitly proving the same statement for arbitrary adapted stopping times would further close even that small corollary. The “mark” route fails if the observable is required to descend to the unmarked quotient: fiber-constancy is necessary. A legitimate novelty path would need an explicit observer instrument with added physical state or backreaction and a result not reducible to changing the growth law; none is supplied here. Global priority is unverified.
6. **Novelty kinds and bridges.** Mathematical novelty: none claimed; the finite formula is a direct corollary of order-invariance. Formalization novelty: none. Physical novelty: none, since no instrument or dynamics beyond CSG is introduced. Philosophical consequence: none about passage, eternalism, presentism, or growing block. The result concerns conditional distributions over natural extensions and a failure of a stage index to descend to an unmarked quotient. Causal order, clock time, thermodynamic arrow, objective passage, and determinism remain distinct.

## Creative failed conjectures and limits

- Rejected conjecture: “covariance of the first-hit condition makes the first-hit stage covariant.” Counterexample: τ above.
- Rejected conjecture: “a physical mark can affect the order-conditioned law and remain invisible to the unmarked algebra.” If its observable genuinely changes within a forgetful-map fiber, it does not descend; if it factors through the unmarked order, it adds no mark-sensitive observable there.
- Defeated proposal: promote the finite conditional-uniformity identity into a new theorem for CSG. Brightwell–Luczak order-invariance already states its key premise and fixed-stage consequence. The stopped-time formula uses only elementary counting after that premise.
- No temporal ontology inference: non-descending stage data can be interpreted as extra physical structure, as gauge bookkeeping, or as a process description; the finite calculation selects none of these.

## Second route tested: physical record memory and forgetting a mark

The materially different idea was to model an observer with a finite internal bit S and an emitted binary record X along a distinguished observer chain, then erase S and ask whether the remaining record history is non-Markov while remaining independent of birth labels.

An exact minimal HMM witness exists. Let S1 be uniform on {0,1}; let S flip at each tick with probability 1/4; and conditionally emit X_i with

    P(X_i=1 | S_i=0)=1/4,     P(X_i=1 | S_i=1)=3/4.

Summing over the hidden state gives

    P(X3=1 | X1=0,X2=1)=15/28,
    P(X3=1 | X1=1,X2=1)=7/12,
    P(X3=1 | X2=1)=9/16.

So the emitted record is non-Markov after internal state is erased. If ticks lie on a physically distinguished chain, the record order is intrinsic and this construction does not use a natural-label choice. This is an exact finite recorder model, but it is an ordinary hidden Markov model placed on a chain. It is not a non-Markov CSG law: geometry is deterministic, the record bits are extra physical marks, and the Bell-causality test for competing geometric births is vacuous. The result therefore does not establish a new causal-set growth mechanism.

There is a sharp covariance check on any proposed richer version. Let a finite marked path law satisfy discrete general covariance on marked labeled histories, and let π erase the physical mark. For a fixed unmarked labeled causet c, define its marginal path weight

    P_π(c) = Σ_{m: π(m)=c} P(m).

If relabelings act equivariantly on marks and marked DGC gives P(m)=P(σm), then m↦σm is a bijection from the fiber over c to the fiber over σc. Hence P_π(c)=P_π(σc). The projected unmarked finite law still has path-independent weights. Under a state-based sequential transition law with the usual finite extension fibers, its unmarked quotient remains a Markov growth process. This is a direct fiber-sum proof, not a general claim about arbitrary hidden Markov observations or non-Markov measures.

Consequently, a covariant marked extension cannot generate label-order memory in the erased unmarked causet merely by hiding a color. It can create ordinary observer-record memory if the record remains a physical mark and a hidden internal state is erased; then the observer's state space has changed. Conversely, if an observer state s is a spectator outside the union B of two possible precursor sets, standard Bell causality forces the ratio p_s(C→C1)/p_s(C→C2) to equal the ratio of the reduced transitions on B. A dependence of that ratio on s is a Bell-causality violation. Dependence can remain when the observer record belongs to the relevant causal past/precursor union, but an explicit marked Bell-causal family and new observable consequence were not obtained.

**Prior-art defeat for this second route.** Rideout–Sorkin already discuss Ising spins on causal-set relations as additional matter degrees of freedom, and explicitly flag that physical reasonableness / a matter version of Bell causality would need examination. Dowker et al.'s covtree gives a manifestly label-independent event algebra and classical measures by random walks on covtree. Generic HMM filtering and lumpability already explain why hidden internal states produce non-Markov observations. The toy chain adds no causal-set theorem; the marked-fiber implication follows from DGC itself. The attempt is recorded as a failed conjecture, not as a novelty candidate.

### Second-route six-item contract (rejected)

1. **Question/result tested.** Can a physically marked observer create a non-Markov unmarked causal-set growth law while retaining label covariance? A marked DGC measure cannot create birth-label-dependent marginal path weights when the mark forgetful map is equivariant: fiber summation preserves DGC. The HMM record sequence can be non-Markov after hiding internal state, but it is a marked-record process on a fixed chain, not unmarked causal-set growth.
2. **Nearest primary predecessors.** Rideout–Sorkin, gr-qc/9904062v3, establishes CSG DGC and the t-family and discusses Ising-spin matter on relations (full-text integrated read). Dowker, Imambaccus, Owens, Sorkin & Zalel, arXiv:1910.07292v2, §2.3–2.4 and §§3–4, constructs covariant event algebra/stem observables and covtree random-walk measures (full-text read). Kemeny & Snell, *Finite Markov Chains* (1960), Theorem 6.3.2, gives the strong lumpability criterion: a quotient is Markov exactly when transitions into each quotient block agree across states in a block. The HMM observation non-Markov case is standard. None supplies a causal-set-specific new observer-memory effect.
3. **What changed / why it matters.** An observer's internal bit can encode physical memory not recoverable from the bare order, but encoding it as a mark changes the state space. Erasing an equivariantly marked DGC model preserves unmarked path covariance; a truly non-Markov output must either remain a marked observation, alter growth feedback, or leave the state-based CSG assumptions.
4. **Small example/check.** Two-state hidden bit plus binary output gives the exact conditional probabilities above. The finite fiber-sum no-go is proved as a bijection of mark fibers. The Bell spectator obstruction is the Bell ratio identity applied at fixed state s.
5. **Falsifier/novelty defeater.** A prior theorem on color-forgetting for covariant growth would make the fiber-sum statement fully occupied; in any case it is elementary from the definitions. A known marked/matter CSG satisfying local Bell causality would defeat a broader claim that recorder structure is absent; Rideout–Sorkin already has relation-spin matter. Ordinary lumpability/HMM theory defeats the generic non-Markov projection claim. A candidate would need a nontrivial covariant typed growth kernel, a non-vacuous Bell check, and a measurable output not reducible to generic hidden-state memory; none was found.
6. **Novelty kinds / bridge.** Mathematical: no new theorem beyond a fiber-sum corollary and standard HMM calculations. Formalization: none. Physical: the toy observer is an explicit added degree of freedom but no new causal-set interaction law is derived. Philosophical: no ontology or passage conclusion. Global priority remains unverified.

## Search and read-depth limits

Prior-work priority search was targeted, not systematic. Primary texts audited at full-text depth for Rideout–Sorkin, Brightwell et al., and Brightwell–Luczak 0901.0240; the latter's abstract and §§1, 3–4 were checked directly in version v3. Brightwell–Luczak's companion *Order-invariant measures on fixed causal sets*, arXiv:0901.0242v2, was checked at abstract depth as nearby pointed/natural-extension work. Broad search for “pointed/marked causal sets” did not establish absence of such work. No general statement beyond finite natural-extension classes is claimed. Infinite-stage conditional laws require separate measure-theoretic hypotheses; quantum sequential growth is outside scope.

## One exact reduced-algebra obstruction candidate

The stopping-time and physical-mark hypotheses above failed. A materially different route survives as an exact theorem about complex sequential growth, not as an observer theorem: for every p outside the classical interval, explicitly concatenated doubly-principal records force divergence of the variation norm on the doubly-reduced poscau tree. The same result holds on the larger reduced-poscau tree. It does **not** settle extension to the covariant intersection algebra alone.

### Finite gadget certificate

Use Dowker–Zalel's complex transitive-percolation amplitude on a naturally labelled finite order (C):

    A(C) = p^L q^(binom(n,2)-R),  q=1-p,

where (L) is its number of links and (R) its number of comparable pairs. Let (G) range over naturally labelled 5-element orders with a unique maximal element; let (m(G)) be its number of minimal elements. A direct exhaustive check of all (2^{10}=1024) forward-relation subsets, filtering for transitivity and a unique maximum, yields 40 principal orders. The exact bivariate histogram is

    (u,v) = (L(G)+m(G), 10-R(G)) : multiplicity
    (5,0):1, (6,1):3, (6,2):6, (6,3):4, (6,4):3,
    (7,3):7, (7,4):8, (7,5):6, (8,2):1, (8,6):1.

This verifies the one-variable histogram by (e=u+v): (5:1,7:3,8:6,9:4,10:11,11:8,12:6,14:1). It is independently checked by `reduced_poscau_obstruction.py`, using only the standard library. The integrated coordinator's existing `csg.grow` enumeration is an independent implementation check; this report does not import it.

When a principal block G is appended above a preceding principal order with a unique maximum, all cross-block pairs are comparable, so they add no q-exponent. The only new cross-block links run from the preceding unique maximum to the m(G) minimal elements of G. If A(G) denotes the intrinsic principal-cylinder amplitude, the seam-inclusive block factor is B(G)=p^m(G)A(G), namely

    B(G) = p^(L(G)+m(G)) q^(10-R(G)).

For any complex (p), write

    r_5(p) = sum_G |B(G)|
           = sum_(u,v) multiplicity(u,v) |p|^u |1-p|^v.

Append a new top to each G, obtaining a 6-element order H. It is doubly principal: H has a unique maximum and its restriction to the first five labels is the principal order G. The new top adds exactly one link and five relations, so L(H)=L(G)+1 and 15−R(H)=10−R(G). At a concatenation boundary, the cross-block factor is therefore B_double(H)=p B(G), and the total absolute block weight is

    r_6^double(p) = |p| r_5(p).

At (p=(1+i)/2), (q=(1-i)/2), the two moduli equal (1/\sqrt2). The exact sums are

    r_5 = 105/128 + 9/(8 sqrt(2)) = 1.6158076... > 1,
    r_6^double = 9/16 + 105/(128 sqrt(2)) = 1.14255... > 1.

Both inequalities are exact. For the latter, sqrt(2)<3/2 gives 105/(128 sqrt(2))>35/64, so r_6^double>36/64+35/64=71/64>1.

For a second, smaller subfamily, two doubly-principal 4-element blocks suffice at p=(1+i sqrt(3))/2, q=1-p: the chain of four has seam weight a^4, and the order with two incomparable minima below a cap below a final top has seam weight a^5 b, where a=|p| and b=|q|. Their sum W_4=a^4(1+ab)=2, so the same repetition argument works with only two gadget types and a 4-element base block at that parameter. This does not cover the interior-disk point p=(1+i)/2, where W_4=3/8<1.

At p=(1+i)/2, among uniform principal-block families of a fixed size, the five-element G family is the first one in this enumeration whose block sum exceeds one. The corresponding sums for k=1,2,3,4 are approximately 0.7071, 0.5000, 0.5303, and 0.8094; this minimality claim applies only within that construction.

### General all-parameter repetition proof

Let a=|p|, b=|1-p| and t=a+b. For p outside [0,1], strict triangle inequality gives t>1, and a,b>0. Put r=a/t and s=b/t; then r+s=1 with r,s in (0,1). For a k-element principal G, set u=L(G)+m(G) and v=binom(k,2)-R(G), so its seam-inclusive block weight is a^u b^v. Every nonminimal element has at least one incoming link, so L(G)≥k−m(G), hence u≥k; also v≥0. Therefore

    a^u b^v = t^(u+v) r^u s^v >= t^k r^u s^v.

Let r_k(r,s) be the sum of r^u s^v over all k-element principal G. This is exactly the probability in (k+1)-element real transitive percolation with relation probability r and nonrelation probability s of the event E∩F, where E says label 0 is an ancestor of every label and F says label k is a descendant of every label. Indeed, each causet in E∩F is uniquely 0⊕G with G principal, and its transitive-percolation probability is r^u s^v.

Sequential exposure gives P(E)=F_k(s):=product_{j=1}^k(1−s^j), since once label 0 is ancestor of the j existing labels, the next label joins its future iff at least one of its j independent birth choices is related. Reversing labels and the order shows P(F)=F_k(s) as well. Both E and F are increasing events in the independent primitive relation choices, so the product-measure correlation inequality gives P(E∩F)≥P(E)P(F)=F_k(s)^2. For completeness, the inequality follows by induction on the number of Bernoulli variables: conditional covariances are nonnegative by induction, while the covariance of the two conditional expectations as functions of the last Bernoulli variable is nonnegative because both functions are increasing. Since 0<s<1, F_infinity(s):=product_{j=1}^infinity(1−s^j)>0; this follows from convergence of sum_j s^j and the bound log(1−x)≥−2x for all sufficiently small x.

Combining these bounds gives

    r_k(a,b) := sum_G a^u b^v >= t^k r_k(r,s) >= t^k F_infinity(s)^2.

The right side grows without bound with k. Choose a finite k such that W:=a r_k(a,b)>1. For every principal G of size k, append a new top to obtain a doubly-principal H of size k+1. Its seam-inclusive weight is |p| times that of G, so the sum of absolute weights over these H is W.

Now ordinally concatenate any m-tuple of these H blocks above the singleton. Every resulting order is doubly principal, has size 1+m(k+1), and is a distinct node: the fixed (k+1)-label intervals recover the tuple. Their amplitudes factor over the blocks, giving

    S_(1+m(k+1)) >= W^m -> infinity.

For each m, the distinct resulting endpoints define pairwise-disjoint cylinder events at the fixed level 1+m(k+1), and their premeasure values are the corresponding block-amplitude products. Any finite complex measure extending the cylinder premeasure has finite total variation; on every finite disjoint family of measurable sets, the sum of absolute values is bounded by that total variation. Here that sum is at least W^m, which diverges. Therefore no finite complex-measure extension exists on the labeled doubly-reduced sigma-algebra for any p outside [0,1]. Since this sigma-algebra is contained in the larger labeled reduced-poscau sigma-algebra, extension to the latter is also impossible. This direct finite-variation contradiction does not depend on an extension-criterion theorem. For p in [0,1], real transitive percolation defines a probability measure on the full labeled-history sigma-algebra, whose restriction gives the extension. The finite 5-gadget calculation above supplies a sharper explicit k=5 certificate for p=(1+i)/2, where the general F_infinity bound need not give the smallest k.

### Six-part novelty contract for the all-parameter result

1. **Exact question/result.** Does the complex transitive-percolation premeasure extend to the labeled doubly-principal-cylinder sigma-algebra \(\widetilde{\mathcal R}_p\)? It does iff the transitive-percolation coupling p is real and in [0,1]. For p outside [0,1], the general real-order comparison and positive-association argument gives a finite block family of total seam weight W>1; repeated blocks force unbounded total variation. For p in [0,1], the ordinary path probability measure on the full labeled-history sigma-algebra restricts to the required measure. The subscript p names the posts algebra in Dowker–Zalel and does not denote dependence of the sigma-algebra on the numerical parameter. The result also excludes an extension on the larger labeled reduced-poscau sigma-algebra. It does not classify measures on the covariant intersection alone.
2. **Three nearest primary predecessors and comparison.** (i) Dowker & Zalel, *Observables for cyclic causal set cosmologies*, arXiv:2212.01149v2 (17 July 2023), §§III.2–III.4 and §V, especially Eqs. (23)–(26), (29)–(31): defines the reduced and doubly-reduced trees, gives the amplitude and the S_n criterion, and reports numerical evidence at levels 2–4. For the doubly-reduced tree it explicitly says the criterion is inconclusive: each level contains valency-one nodes with zero ζ. The repeated doubly-principal family gives a direct level-sum lower bound for every p outside [0,1]. This is very close prior art and defeats any broad claim about the problem itself. (ii) Dowker, Johnston & Surya, *On extending the Quantum Measure*, arXiv:1007.2725v1 (2010), §2 Claims 1–2 and §4: relates extension of the quantum measure/decoherence functional to a histories-Hilbert-space-valued measure and proves full labeled-history nonextension for nonreal complex-percolation p. Their result supplies the full-algebra obstruction, not the smaller cyclic-record tree bound. (iii) Surya & Zalel, *A Criterion for Covariance in Complex Sequential Growth Models*, arXiv:2003.11311v1 (2020), §§2–3, especially Theorem 2.1: gives bounded-variation criteria and full labeled-history extension results for complex percolation. It does not settle reduced or doubly-reduced poscau. Rideout–Sorkin gr-qc/9904062v3 is used as the background sequential-growth source by reference to the integrated record cs-rideout-sorkin-2000-v3. The source/version/locator records are in sources.jsonl.
3. **What changes / why it matters.** The proof resolves the extension question for the entire labeled doubly-reduced cylinder algebra, rather than only the authors' numerical points or a single parameter. Its mechanism is a finite principal-gadget block family whose total variation weight exceeds one after a sufficiently large finite cap; real transitive percolation and positive association supply a uniform lower bound for that weight. It also excludes extension on the larger labeled reduced-poscau algebra. It does not prove nonextension on the pure covariant intersection \(\tilde{\mathcal R}_p\cap\mathcal R\): a measure defined only on that intersection is a different extension problem. Nor does the scalar complex measure by itself define a full decoherence functional.
4. **Smallest reproducible witness/check.** The all-p proof is analytic, not an extrapolation from finite enumeration. For p=(1+i)/2, six-element doubly-principal blocks capped from the 40 principal 5-orders give the explicit weight \(W=9/16+105/(128\sqrt2)>71/64>1\); k≤4 uniform principal-block families have weight below one at this point. The script checks the 1024-mask enumeration and both histograms and writes the 40 retained relation sets with L, m, R, u, v data to `principal5_certificate.csv`. The additional two-type 4-element family gives W_4=2 at p=(1+i√3)/2. The general block repetition proof covers every p outside [0,1].
5. **Strongest novelty defeater / falsifier.** Dowker–Zalel explicitly pose this extension problem and conjecture broader failure from numerical work at levels 2–4. Their paper is the direct and strongest prior-art defeater; the present proof may be an elementary consequence of structures they introduced and could have appeared later. The derivation depends on: seam-inclusive amplitudes being p^m A(G), the endpoint-product identity \(Z_k(r,s)=\Pr(E_k\cap F_k)\), positive association for independent Bernoulli edge variables, and distinct doubly-principal cylinders at each repeated-block level. Each is stated and checked directly. Global priority remains unverified. A later proof of the same iff result on \(\widetilde{\mathcal R}_p\) would defeat novelty without invalidating this proof. Nothing here decides extension on \(\widetilde{\mathcal R}_p\cap\mathcal R\).
6. **Novelty type and bridge.** Mathematical: an all-parameter extension/nonextension theorem for the labeled doubly-principal cylinder sigma-algebra, conditional on Dowker–Zalel's definitions; global priority is unverified. Formalization: none. Physical: the theorem concerns a specified complex scalar-measure extension problem, not an observer instrument or completed decoherence functional. Philosophical: no conclusion about passage, eternalism, presentism, determinism, clock time, or thermodynamic arrow. The chosen event algebra and physical interpretation remain explicit premises.
