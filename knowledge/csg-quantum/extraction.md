# Quantum and non-covariant boundary of causal-set sequential growth (RC-4)

Status: 2026-10-20. Lane `kb-csg-quantum-boundary`. A Claude subagent completed this lane after
the GLM worker stopped on a provider quota. Every quote below was copied from the arXiv HTML
(LaTeXML) render of the version named in `sources.jsonl` and read in this run. Inline math is
transcribed from the LaTeXML alttext and simplified to plain text (for example `S_Z` for the
fraktur sigma-algebra). Locators give sections, equations, theorems and lemmas, never PDF pages.
"Authors' claim", "established (proved in the paper)" and "ours" are kept separate. This document
makes no novelty claim.

Web search worked: WebSearch, arXiv listing/API queries and Crossref lookups all returned
results. All primary texts came from `arxiv.org/html/<id>v<n>`. Nothing was paywalled at those
routes.

## 1. Verdict for the coordinator (RC-4)

1. **RC-4(a) is already published.** It is not just a corollary the project derived. Brightwell
   and Luczak (0901.0240v3, Sec. 1 and Sec. 4) define "order-invariance": conditional on the
   stage-k poset, every order of generation is equally likely. They present it as the content of
   Rideout-Sorkin general covariance. Their Theorem 4.2 extends it to the infinite outcome space,
   for each finite k, as a DLR-type identity. The coordinator's ancillarity derivation is
   therefore a restatement of a published characterization (`csgq-brightwell-luczak-2011-v3`).
2. **The completed infinite case is a real gap in the coordinator's note, and published
   mathematics already fills it.** On a fixed infinite causal set, order-invariant measures over
   birth orders need not be unique: for two disjoint infinite chains there is one for every
   q in [0,1] (0901.0240v3 Example 4 and Sec. 7; 0901.0242v2 Sec. 1). Section 3.A (ours) builds
   from this example a family of DGC walks on labelled poscau with identical covariant measures
   but different labelled measures, and a tail birth-order statistic that separates them. In the
   infinite limit, therefore, the covariant data is *not* a sufficient statistic, even inside the
   DGC class. The extra information lives only in non-covariant (label or stage) events. The CST
   papers read here declare those events unphysical (gr-qc/0210061v2 Sec. 2; 1910.07292v2
   Sec. 2.3).
3. **Non-path-independent (non-DGC) classical dynamics exist in print and do not reach covariant
   observables as such.** Every Alternating CSG model except Alternating Transitive Percolation
   violates DGC (2109.10749v1 Claim 3.5). Energetic causal sets declare a global birth order to
   be "the true causal order" (1902.05082v3). Covtree Lemma 4.9 and Sec. 5 (1910.07292v2) show
   that every walk on labelled poscau, "whether it satisfies Discrete General Covariance or not",
   induces a stem-algebra measure that some manifestly covariant covtree walk reproduces. Our
   reading is that DGC failure can never be witnessed by an event in R(S), only by non-covariant
   events.
4. **Quantum region.** Three features make the classical ancillarity argument fail or lose its
   meaning:
   (i) A quantum measure is non-additive, so there is no Kolmogorov conditional ("uniform over
   labellings") (1007.2725v1 Sec. 1, Eq. (1)).
   (ii) In complex sequential growth whose vector measure does not extend, only finite-stage
   labelled events carry a measure, and no nontrivial such event is covariant (2003.11311v1
   Sec. 2, Theorem 2.1, Corollary 3.6, Claim 3.8; 1007.2725v1 Lemma 1). The authors treat this
   as a failure of covariance, not as evidence that birth order is physical. Their proposed
   remedy, conditional convergence, would need "a preferred ordering of events" (1007.2725v1
   Sec. 5).
   (iii) The 2026 operator-valued work imposes GC as equality of labelled-path vectors. It
   explicitly sets aside a weaker norm-only covariance with path-dependent phases, under which
   labelling would enter interference (2603.25503v1 Sec. 3.1 Note; Sec. 4).
5. **Observer access.** No source read here contains a formal embedded-observer or record model
   for growth dynamics, classical or quantum. None answers "can observer records distinguish
   growth order in a non-covariant or quantum growth model?". The closest material is the
   following. An unanswered self-locating question appears in gr-qc/0202097v1 Sec. 7 ("this
   particular copy of S1 ... that 'we inhabit'"). Dowker's internal-view proposal is
   philosophical (2209.07653v2 Secs. 4.3-4.6). Sorkin contrasts a situated observer with a
   super-observer (gr-qc/0703098v1 Sec. 5). Zalel makes informal "local observer" remarks
   (2302.10582v1 Sec. 3.3 fn. 3; Sec. 7). In this literature "observable" means beable, not
   observer access (gr-qc/0210061v2 Sec. 1; 2109.10749v1 Sec. 1 footnote).

**What survives of the RC-4 sliver.** Read against these sources, the open region narrows to two
cases, and neither is a purely mathematical classical gap.

- **(α) Bridge-premise case.** Any record that distinguishes growth order must be a
  non-covariant event, either stage-indexed or a tail statistic of birth order. Whether an
  embedded record could correspond to such an event is a question about bridge premises
  (observer access versus the covariance postulate). The covariant mathematics settles nothing
  here.
- **(β) Quantum case.** Two quantum questions remain untreated:
  - in norm-only-covariant quantum sequential growth with path-dependent phases and an extending
    vector measure, do the phases change the quantum measure of covariant events?
  - in non-extending complex models, does the conditional-convergence ordering change covariant
    predictions?

Neither case was found treated anywhere. Section 8 lists the reads most likely to defeat this.

## 2. Per-source extraction (verbatim, with locators)

### 2.1 Brightwell and Luczak, Order-invariant measures on causal sets, 0901.0240v3 (full-text)

- Sec. 1: "The order in which the elements of the causal set are generated is not deemed to have
  any physical meaning, so it should not be possible to extract information about this order
  from the causal set at any stage. Rideout and Sorkin thus viewed growth processes as being
  Markov chains on the set of finite unlabeled causal sets, where each transition adds a new
  maximal element. They studied such processes with the property that, conditional on the causal
  set at some stage k being equal to some unlabeled k-element poset P, each linear extension of P
  is equally likely to have been the order in which the elements were generated. They called this
  property “general covariance.”"
- Sec. 1, Example 2 (random graph orders): "An interpretation is that, if we stop the process when
  there are k elements, and look at the structure of the poset, but not at the numbering of the
  elements, then, conditioned on this information, each linear extension of the poset is equally
  likely to have been the order in which the elements were generated."
- Sec. 1: "Our aim in this paper is, effectively, to study the class of growth processes
  satisfying general covariance: this class is vastly richer than the class of csg models."
- Sec. 4, definition (Eq. (4)): mu is order-invariant if, for Borel B_1..B_k, a suborder <^[k]
  and any linear extension lambda, mu(E(B_1...B_k, <^[k])) = mu(E(B_lambda(1)...B_lambda(k),
  lambda[<^[k]])). The paper then notes that "if a causet process is order-invariant, then it is
  order-Markov" and that "order-invariance is much stronger than the order-Markov condition".
- Theorem 4.2 (established): "Let mu be a causet measure. Then mu is order-invariant if and only
  if mu(E)=E_mu nu^k(E) for every E in F and every k in N." Gloss after the theorem: "we condition
  on all the information about omega except the order in which the first k elements are
  generated, and then realizing the conditional Gibbs measure, which in our setting is
  nu^k(.)(omega)."
- Sec. 5, Example 4 (two disjoint infinite chains B, C; choose the B-element with probability q):
  "It follows that mu_q is order-invariant for any q, since the expression for
  mu_q(E(a_1...a_k)) does not depend on the order of the a_i." Also: "If q in (0,1), then
  Xi=B∪C=Z a.s." Under the Pólya-urn variant, "the proportion of elements taken from B in the
  first n steps converges a.s. to some limit chi".
- Sec. 7: "It is not too hard to see that the order-invariant measures mu_q, for fixed q in [0,1],
  are extremal; moreover, these are the only order-invariant measures on P." Theorem 7.2:
  extremal iff trivial tails. Corollary 7.6: unique decomposition into extremal order-invariant
  measures.
- Not in the paper: any physical reading of tail statistics, observers or records.

Companion paper 0901.0242v2 (full-text, Sec. 1 only), Sec. 1: "As we shall see, depending on P,
there may be one, many, or no order-invariant probability measures on the set of linear
extensions of P".

### 2.2 Brightwell, Dowker, Garcia, Henson, Sorkin, gr-qc/0210061v2 (full-text)

- Sec. 1: "the word “observable” is inherited from an interpretation of quantum mechanics — the
  standard interpretation — in which the subject matter of the theory is not what is but what can
  be observed. However adequate this may be for laboratory science, it will not do for quantum
  gravity, and we should rather be seeking what Bell called the “be-ables”."
- Sec. 2: "The stochastic dynamics described above gives rise to a notion of probability that is
  too rich for our purposes, as it assigns a probability as an answer to the question “is element
  3 above element 1?”, which is not meaningful for us, as in any particular causet the answer
  depends on the labeling of the elements."
- Sec. 2: "In a causet, only the relations between elements have physical significance: the labels
  on causet elements are considered as physically meaningless."
- Sec. 3, Corollary 1 (established for generic CSG, real t_k >= 0 with some t_k > 0 for k >= 2):
  "For every set A in R, there is a set B in R(S) such that, in any CSG dynamics,
  mu(A sym-diff B)=0."
- Sec. 6: mu = mu~ restricted to R = mu~ composed with p^-1 (restriction and pushforward
  coincide).
- Sec. 7: "Might it be possible to consider dynamical models in more generality, constructing a
  measure on Omega and then imposing general covariance (and Bell causality for that matter)
  directly on the measure, in other words to find a dynamics that is fundamentally label free?
  Would that lead to a physical measure different to the one we have obtained here? We do not
  know." Also: "because there is nothing physical about a cylinder set itself, it might be
  objected that this is an attempt to impose a physical condition on an unphysical object."

### 2.3 Brightwell et al., General Covariance and the "Problem of Time", gr-qc/0202097v1 (full-text)

- Sec. 4, on the two roles of discrete general covariance: "On one hand it serves to limit the
  possible choices of the transition probabilities in such a way that the labels drop out of
  certain “net probabilities” ... On the other hand, general covariance limits the questions one
  can meaningfully ask about the causet".
- Sec. 5, on the distribution of the unlabelled poset formed by the first n births: "although such
  a distribution can be computed, it has no obvious meaning because a question like “Do the first
  three elements of C form a 3-chain [footnote] ?” has in general different answers depending on
  what order of birth you impute to the elements of C." Footnote: "The former corresponds to a
  question that the dynamics can’t answer, the latter to a question that is without any physical
  meaning at all."
- Sec. 7 (determinism): "In the case of (classical) general relativity, these difficulties are
  somewhat mitigated by the theory’s determinism, which means that predictions can effectively be
  made and verified locally. Such is not the case, however, in an indeterministic theory".
- Sec. 7 (quantum): "the theorems that above led us from the transition probabilities tau to the
  measure mu~ (and thence to mu) break down in the quantum case because the complex amplitudes that
  one is constructing are no longer necessarily bounded in absolute value, unlike probabilities
  which are confined to the compact space [0,1]".
- Sec. 7 (self-location; unanswered): "Consider instead something like this: “Given that S1 occurs
  as a stem in C what is the probability that a second stem S2 occurs containing this particular
  copy of S1 (the S1 that “we inhabit”)?”. When C contains more than one stem isomorphic to S1,
  this second type of question seems different from the first, and indeed not even clearly
  defined on the sole basis of the “absolute” measure mu. Does this mean we need a logically
  independent concept of conditional probability and an extended formalism to express it, which
  would re-open the “problem of time” in a new context? Or is it enough to remark that stems of
  sufficient complexity are unlikely to occur more than once, whence the problem is absent in
  practice?"

### 2.4 Surya and Zalel, 2003.11311v1 (full-text; Secs. 2.2-3 read in full)

- Abstract: "Because of the temporality of the growth process, in this approach, covariant
  observables (or beables) are measurable only if the quantum measure extends to the associated
  sigma algebra of events. This is not always guaranteed."
- Sec. 1: "for complex percolation (CP), where the dynamics is characterised by a single complex
  number q, the measure does not extend and hence cannot be defined for covariant events, unless
  q in [0,1], i.e., for “real” CP (RCP)."
- Sec. 2 (established): "Using the nesting property, we see that no event alpha in Z can be
  covariant unless alpha=Omega." Then: "This means that the event algebra Z does not suffice to
  be able to define covariant observables."
- Sec. 2.1, footnote 4: "It is important to note that if there are k order-isomorphic children in
  a given transition, then the measure not only counts each equally, but the multiplicity k
  appears in the Markovian sum. In this sense the measure does not treat order-isomorphism as
  “gauge”."
- Sec. 2.2, condition (a) in the quantum case: "Condition (a) is straightforward to implement since
  it requires that |c_n^i> = |c_n^j> whenever c_n^i ~ c_n^j, i.e., they are order-isomorphic."
  Eq. (16) sets the cylinder vector to the product of transition amplitudes along the unique
  labelled branch.
- Theorem 2.1 (established, App. B): "For a complex measure space (Omega,Z,mu_v), where Z is the
  event algebra generated from finite set operations on cylinder sets and mu_v:Z->C, mu_v has a
  unique extension to S_Z iff it is of bounded variation."
- Theorem 3.1: "mu_v is of bounded variation if sum_{n=1}^inf zeta_n^max converges. mu_v is not of
  bounded variation if sum_{n=1}^inf zeta_n^min diverges." Lemmas 3.4-3.5 identify zeta_n^max
  with the antichain node and zeta_n^min with the chain node; Eq. (45) gives both in terms of t_k;
  Corollary 3.6 restates the criterion.
- Claim 3.8 (finitely many couplings): bounded variation if all t_ki in R+, or m=1 and k_1>1, or
  1<m<inf and k_m-k_{m-1}>1. "It is not of bounded variation if t_1 not in R+ and m=1, k_1=1." The
  case k_m-k_{m-1}=1 is left open: "Unlike the m=1 case, however this is not sufficient to prove
  divergence." Claim 3.9 covers countable, asymptotically collinear couplings. Eqs. (60)-(62)
  re-prove that CP is not of bounded variation unless q in [0,1].
- Sec. 4: "Importantly, for the former class of dynamics, this implies that every covariant event
  in S_Z is measurable." On preclusion: "Using the principal of preclusion which states that
  (covariant) sets of quantum measure zero do not happen ... the originary event never happens"
  (for extending models with t_1=0, Eq. (67)).

### 2.5 Dowker, Johnston, Surya, On extending the Quantum Measure, 1007.2725v1 (full-text, Secs. 1, 4, 5)

- Sec. 1: "There is however no known analog of the Carathéodory-Kolmogorov extension theorem for
  quantum measures." Eq. (1) gives the quantum sum rule; the quantum measure "does not satisfy the
  Kolmogorov sum rule in the presence of quantum interference".
- Lemma 1 (established, Sec. 4): "The quantum vector measure of complex percolation is not of
  bounded variation when the parameter p is not real." Claim 5 covers |p|>1 or |q|>1. The product
  decoherence functional is D(alpha,beta)=A*(alpha)A(beta) (Eq. (43)).
- Sec. 5: "For causal sets on the other hand, one is interested in covariant or label invariant
  observables. Since the growth process generates only labelled causal sets, the events in A are
  not themselves observables."
- Sec. 5: "As we have seen, for complex percolation with p not real, mu_v does not extend to S_A,
  and hence the construction of covariant observables, if at all possible, requires a different
  approach."
- Sec. 5 (proposed remedy; authors' suggestion): "One option then is to require that the measure
  on S_A satisfy only a conditional convergence, with the conditionality determined by a preferred
  ordering of events in A. ... However, in order for this prescription to work in general, it is
  important to ensure that such an ordering procedure is unique." Also: "the failure of a quantum
  measure to have a “mathematical extension” does not mean that it cannot have a “physical
  extension”."

### 2.6 Srivastava and Surya, Implementing Bell causality in Quantum Sequential Growth, 2603.25503v1 (full-text, sections listed in record)

- Sec. 1: for C-valued models, "The computability of these models rests on the fact that these
  amplitudes form a commutative algebra."
- Sec. 2.2: "In [32] it is suggested that covariant and causal measures on A may be recovered
  without imposing these conditions at the sequential level, but we will not consider this
  approach here." ([32] is Brightwell and Luczak, Order-invariant measures on fixed causal sets.)
- Sec. 3.1, General Covariance: "The simplest implementation of GC on labelled poscau P, is to
  require that |c_n> = |c_n'> whenever c_n' ~ c_n and c_{n+1}' ~ c_{n+1}, or equivalently
  A_gamma(c_n)|Omega> = A_gamma(c_n')|Omega>. This implies that the inner product or quantum
  measure <c_n|c_n> = <c_n'|c_n'>. There is no operator ordering ambiguity, since A_gamma is
  strictly time ordered."
- Sec. 3.1, Note: "It is also possible to introduce a phase |c_n> = e^{i Phi(c_n,c_n')}|c_n'>
  since this will leave the quantum measure invariant. Because of the ensuing ambiguities, or
  generation of new parameters this will result in, we do not consider this option henceforth."
- Sec. 4: "one could stipulate that it isn’t the quantum vector measure that should be the same
  when implementing GC, but rather only its norm. Thus, one could introduce a path dependent phase
  into the definition. Such phases can similarly be introduced into the QBC relations. While we
  have explored these options, apart from trivial choices, the ensuing dynamics becomes rapidly
  more complex."
- Authors' main claims (abstract), taken from them and not checked: the two most natural QBC
  orderings force a commutative transition algebra; a d=2 Pauli representation is inconsistent.

### 2.7 Dowker and Surya, Extended percolation, gr-qc/0504069v1 (full-text)

- Sec. 1: EP "exhausts the class of Markovian dynamics compatible with general covariance and WBC"
  (attributed to Rideout-Varadarajan).
- Sec. 2, footnote 1: "Note that the couplings for the k+1th era are not only relative to a but
  also depend on a."
- Proposition 1 (established): "In an EP, the family of stem sets, S, generates the sigma algebra,
  R, of covariant measurable sets up to sets of measure zero."
- Sec. 4.1: "In CSG there is no fixed causal structure and the Bell causality condition is imposed
  on the dynamics at the level of the labelled (non-covariant) process." Also: "Whether, in
  particular, its implications for the covariant measure can be discovered/understood in covariant
  terms – in terms of stem predicates – is an interesting open question."
- Our note: the dependence of an era's couplings on the earlier causet is history dependence
  through the *unlabelled* stack, so EP stays inside DGC and the finite-stage ancillarity argument
  applies to it.

### 2.8 Covtree: Dowker, Imambaccus, Owens, Sorkin, Zalel 1910.07292v2 (full-text) and Zalel review 2302.10582v1 (full-text, Secs. 1, 2.3, 3.3, 7)

- 1910.07292v2 Sec. 1: "The sequence of the births is a total order on the spacetime atoms and
  contains unphysical, gauge information."
- Sec. 2.3: "the cylinder set cyl(C~_n) is the event “the causet at the end of stage n−1 of the
  process is C~_n” which refers to the unphysical, gauge information of the stage."
- Lemma 4.9 (established): "For every measure mu on R(S) there exists an extension mu~ to R~."
- Sec. 5: "lemma 4.9 means that although every covtree walk is apparently completely covariant in
  its setup, for every walk on labeled poscau – whether it satisfies Discrete General Covariance or
  not – there exists a covtree walk that produces the same measure on R(S). So, there is no easy
  relationship between the DGC condition on a labeled poscau walk and the manifest “covariance” of
  a covtree walk." Open question (i): a covtree condition matching walks that satisfy "DGC only,
  measures which Brightwell and Luczak call “order-invariant”".
- 2302.10582v1 Sec. 2.3: "one technical question which underpins this discussion is whether R is
  countably generated. As far as the author is aware, this is an open question."
- Sec. 3.3: "every measure on R(S) possesses some (not necessarily unique) extension to R~".
  Footnote 3, on rogues: "they can only be distinguished globally, not by any local observer living
  on them". Sec. 7: "(there is no God’s eye view, only the viewpoint of somewhat local
  observers)". These are informal remarks; no observer is modelled.

### 2.9 Bento, Dowker, Zalel, If time had no beginning, 2109.10749v1 (full-text, Secs. 1 fn., 3-3.2, 5)

- Sec. 1 footnote: "We use the term “observable” as a shorthand for “physical property” and not to
  imply that there need be any external observer."
- Claim 3.5 (established by explicit counterexample, Fig. 3): "An Alternating CSG model satisfies
  the discrete general covariance condition if and only if it is an Alternating Transitive
  Percolation model."
- Sec. 3.2: "Since the remaining Alternating CSG dynamics are not covariant, to ascertain whether
  they are causal either requires specifying a canonical method of relabeling ... which renders
  the Bell causality condition itself label-dependent and hence not covariant, or the condition (7)
  should be imposed for each consistent relabeling that exists."
- After Lemma 3.4: "Thus, at any finite stage of growth, Transitive Percolation (TP) and
  Alternating Transitive Percolation (ATP) cannot be distinguished. However the processes are
  different when run to infinity."
- Sec. 3 opening: "While the concept of Becoming could be regarded simply as a crutch in defining a
  model of random infinite causal sets and dispensed with once a measure has been defined on the
  full sigma algebra of events, Sorkin has proposed that growth is a physical process".

### 2.10 Philosophical sources on birth order and observers (full-text for the sections named)

- Sorkin gr-qc/0703098v1, Sec. 3: "a definite birth-order, or an “external time”, did figure in
  the description I gave, but it is to be regarded as an artifact of the description analogous to
  one’s choice of coordinates for writing down the Schwarzschild metric. Only insofar as it
  reflects the intrinsic causal order of the causal set is this auxiliary time objective. The
  residue is “pure gauge”."
- Sec. 5: "Super-observers do not exist however, and the attempt to put ourselves into their shoes
  brings the localized human experience of “the now” into conflict with the asynchronous
  multiplicity of “nows” of a CSG model".
- Sec. 6, footnote: "there seem to exist more general Markov processes that do produce, for
  example, the future of the origin in M4 [7]. These processes respect discrete general covariance
  in the sense of [1] but not Bell causality." ([7] is "Graham Brightwell, unpublished notes on
  general covariance". Unread.)
- Sec. 7: "This would be the analog of letting mu~ depend on the labeling but only computing
  probabilities with respect to mu." Also: "One might thus expect, in the causet case, that mu~
  should itself be relabeling invariant, for only in this way would the classical limit of the
  corresponding quantum theory have a chance to reproduce the Einstein equations." Footnote:
  "Notice that this condition of “discrete general covariance” is not itself formulated
  covariantly. Notice also that it says something less than the following formal statement: “the
  probability of a completed causet C (a causet of countably many elements) is independent of its
  labeling. This distinction was brought to light by Graham Brightwell, who also pointed out that
  this stronger statement does hold in the CSG models, even though it’s not implied by discrete
  general covariance alone."
- Dowker 1405.3492v1 (passage around Fig. 1): "However, there is no physical order of the births
  of the elements labelled 2 and 3 because they are not ordered in the causal set order. Sorkin
  calls this partially ordered growth asynchronous becoming." Also: "A Blockhead can always play
  the card of “running the process to infinity” ... My view on this manouevre is that it produces
  a different physical theory – some might want to call it a different interpretation of the
  theory – in which there is nothing to correlate with the occurrence of events." And: "We do not
  yet know if or how asynchronous becoming will be manifested in a quantum dynamics for causal set
  theory".
- Dowker 2209.07653v2, Sec. 4.4: "The label-induced picture of the process is partly subjective
  because the label-order exists in the minds of the scientists using the theory but the
  label-order of two atomic-events that have no precedence order is not physical. The picture is
  also partly objective because the label-order of two atomic-events that do have a precedence
  order is physical. A choice of natural labelling is a choice of gauge." Sec. 4.6: "An objective
  external view of the birth process does not exist. But, according to the Proposal, an objective
  view is possible if the view is internal." This is a proposal about experience. It contains no
  dynamics of records.

### 2.11 Contrast classes: physical birth order and labelling-free kinematics

- Cohen, Cortês, Elitzur, Smolin 1902.05082v3. Abstract: "(1) a birth order, which is the order in
  which events are generated; this is a total order which is the true causal order". Sec. 3.1:
  "This process is global, hence the birth order is a genuine causal order." Sec. 5: birth order
  "represents the full non-local causal dynamics" and is "never violated"; emergent Minkowski time
  can run against it. Birth order is a posit of the model, shown in simulation output. No internal
  record of it is analysed.
- Gudder 1405.0638v1 Sec. 2: "A causet is covariant if it has a unique labeling (up to ℓ-causet
  isomorphism). Covariance is a strong restriction which says that the elements of the causet have
  a unique “birth order” up to isomorphism." Theorem 2.1 characterises these c-causets as
  multipartite. Restricting to them removes the labelling question by construction.

## 3. Where the ancillarity argument fails (ours unless quoted)

**A. The completed infinite limit, inside DGC.** This is our construction from Brightwell-Luczak
Example 4. It needs an independent check.

- **Setup.** Take Example 4 and forget which chain is B. The stage-k labelled causet is then a
  word s in {A,O}^k with s_1 = A, where A is the chain containing element 0. Its probability is
  P_q(s) = q^a (1-q)^o + q^o (1-q)^a, with a = #A and o = #O.
- **DGC holds.** The isomorphism class of the stage-k causet is the unordered pair {a,o}, and P_q
  depends only on that pair. So the walk satisfies DGC (path independence) for every q. At finite
  stage, birth order is uniform given the stage-k poset, as RC-4(a) says.
- **The covariant measure is the same for every q.** For q in (0,1) both chains are a.s. infinite,
  so the completed unlabelled causet is a.s. "two disjoint infinite chains". The covariant measure
  is therefore the same point mass for all q in (0,1).
- **The labelled measures still differ.** They differ for q not in {q', 1-q'}. For example,
  P_q(AA) = q^2 + (1-q)^2.
- **A tail statistic separates them.** Let f = lim a_k / k. Then f equals q with probability q and
  1-q with probability 1-q. It is tail-measurable and non-covariant.
- **Consequence.** In the infinite limit, the covariant σ-algebra is not sufficient for the
  parameter q. Birth-order data is not ancillary. The finite-stage sufficient statistic, the
  stage-k unlabelled poset, is itself a stage-indexed event, which gr-qc/0202097v1 Sec. 5 calls
  meaningless.
- **Consistency with the literature.** This matches covtree Lemma 4.9 and the review's "not
  necessarily unique" extension.
- **Limits.**
  - The walk is not shown to be Bell-causal.
  - Sorkin's footnote reports Brightwell's unpublished point that, in CSG models proper, a
    stronger labelling-independence holds for completed causets. Bell-causal CSG may therefore
    exclude this phenomenon. Not checked.
  - Classical only.

**B. Non-DGC classical dynamics.** Here P(labelled node) depends on the labelling, so birth order
given the stage-k poset is not uniform. It carries information about the dynamics that the
stage-k unlabelled poset does not. Covtree Lemma 4.9 still applies: the covariant (R(S))
predictions equal those of some covariant walk. Hence the information is confined to
non-covariant events (Alternating CSG, Claim 3.5; ECS; general walks on labelled poscau).

**C. Complex sequential growth with GC imposed on amplitudes** (2003.11311v1 Sec. 2.2). All W(C)
labelled stage-n nodes of class C carry the same vector |c>. By additivity (Eq. (11)), the vector
for their union is W(C)|c>, so its quantum measure is W(C)^2 |A(C)|^2. The sum of the cylinder
measures is W(C)|A(C)|^2. Two consequences follow, by our arithmetic from Eqs. (11)-(12) and (16):

- interference across labellings is maximal and constructive;
- there is no Kolmogorov conditional "uniform over labellings", only amplitude-level equality.

The union is a stage-n event and is not covariant (2003.11311v1 Sec. 2).

**D. Norm-only covariance with path-dependent phases** (2603.25503v1 Sec. 3.1 Note; Sec. 4). If
|c_n^j> = e^{i Phi_j}|c>, the union of class C has quantum measure |sum_j e^{i Phi_j}|^2 |A|^2,
anywhere in [0, W^2 |A|^2]. Labelling phases then enter interference. Whether this survives into
covariant events requires an extending vector measure. **Conjecture-level; no source analyses
it.**

**E. Non-extending measures** (2003.11311v1 Theorem 2.1, Claim 3.8; 1007.2725v1 Lemma 1). Only
the finite-stage labelled algebra is measurable, and it contains no covariant event other than
Omega. The theory then has no covariant predictions, unless a conditional-convergence ordering is
adopted (1007.2725v1 Sec. 5). That ordering is the only place where a stage ordering is proposed
to enter covariant predictions. Uniqueness is flagged by the authors as required and not shown.

## 4. Observer access (answer to the coordinator's question)

No source among the 23 records answers whether observer records can distinguish growth order in
a non-covariant or quantum growth model. No formal embedded observer, record subsystem, or
observer-access hierarchy appears in any text read. The arXiv author listing for Wallden shows
histories, co-event and coarse-graining work, but nothing on records in causal-set growth.
Dowker's observer-related work is philosophical (1405.3492v1; 2209.07653v2).

Within the covariance postulate, our inference from covtree Lemma 4.9 is this: if records are
modelled as events in R(S), they cannot witness DGC failure or birth order as such. The question
therefore becomes whether some physically motivated record corresponds to a non-covariant event.
That is a bridge premise, not a theorem. gr-qc/0202097v1 Sec. 7 is the nearest primary
statement: an indexical "this particular stem" question that the authors say may need a
"logically independent concept of conditional probability".

## 5. Theory-comparison contract

Unit of comparison: model and version plus interpretation. The table maps each model to the
README contract's six questions.

| Model (source) | Ontology / passage claim | State space and dynamics | Covariance status | Where order or label information lives | Observer access | Empirical status |
|---|---|---|---|---|---|---|
| Generic CSG (Rideout-Sorkin; gr-qc/0210061v2) | Authors: growth is physical becoming (Sorkin, Dowker); the math is equally a measure on completed causets (2109.10749v1 Sec. 3) | Labelled poscau walk; real t_k; measure on R~ | DGC + BC | Finite stage: ancillary (order-invariance). Completed: Brightwell says labelling-independence holds (unpublished, via Sorkin fn.) | None; "observable" = beable | None; Brightwell-Luczak Sec. 1 say large-scale structure is a semiorder (citing [7] of their paper) |
| Extended percolation (gr-qc/0504069v1) | As CSG | Eras of GP; couplings depend on earlier unlabelled stack | DGC + WBC | As CSG | None | None |
| DGC-only (order-invariant) walks (0901.0240v3) | Not addressed (mathematics) | Measures on (label string, suborder) | DGC only | Finite stage: ancillary; infinite: non-unique, tail statistics (Sec. 3.A, ours) | None | None |
| Covtree walks (1910.07292v2) | Growth "vague" / asynchronous (2302.10582v1 Sec. 3.3) | Walk on sets of n-orders; measure on R(S) | Manifestly covariant | Absent by construction | None | None |
| Alternating CSG (2109.10749v1) | Authors doubt physical meaning of two-way growth | Alternating poscau | Only ATP satisfies DGC | Non-ATP: in labelled measure, not in convex-events | None | None |
| Complex SG (2003.11311v1; 1007.2725v1) | Quantum measure; preclusion | C-valued vector measure on Z | GC on amplitudes | Extending: only covariant events have measure; non-extending: only labelled events | None | None |
| Operator QSG (2603.25503v1) | Quantum measure | Transition operators, strict stage order | GC on vectors; phase option set aside | Open (phases) | None | None |
| c-causet QSG (1405.0638v1) | Not addressed | Unique-labelling causets, qubits | Trivial by restriction | None (unique labelling) | None | None |
| ECS (1902.05082v3) | Authors: birth order is "the true causal order"; becoming | Global optimising event generator | Non-covariant by design | Physical birth order (posited) | Not analysed | Numerical simulations only |

## 6. Keeping the categories apart

- **Temporal ontology and passage.** Growth-as-becoming is an authors' claim: Sorkin
  gr-qc/0703098v1; Dowker 1405.3492v1 and 2209.07653v2; ECS 1902.05082v3 Sec. 4.3. Bento et al.
  note that the same mathematics can be read as a measure on completed histories (Sec. 3). None of
  the mathematics in the stochastic or quantum papers decides between these readings.
- **Determinism.** CSG is indeterministic. gr-qc/0202097v1 Sec. 7 ties the difficulty of covariant
  prediction to indeterminism. Dust and forest are deterministic special cases (gr-qc/0210061v2
  Sec. 7).
- **Causal order versus birth order.**
  - The causal order is the poset.
  - Birth order is a natural labelling, called gauge in CST (gr-qc/0703098v1 Sec. 3;
    1910.07292v2 Sec. 1).
  - Birth order is physical only in ECS, where it can disagree with emergent Minkowski time (a
    clock-time notion, not the thermodynamic arrow).
- **Clock time.** No clock construction appears in any source except ECS's emergent Minkowski
  coordinate.
- **Thermodynamic arrow.** Not discussed by any source read here. ECS's "time asymmetric phase"
  concerns the dynamics generated by its event algorithm, not entropy.

## 7. Confirmation or correction of knowledge/defeat-search notes

- `fulltext-reads-causal-sets.md`, confirmed:
  - the quotes on "is element 3 above element 1?" (gr-qc/0210061v2 Sec. 2), the covariant
    sigma-algebra, Corollary 1, and the Sec. 7 open questions;
  - the restriction/pushforward identity (Sec. 6).
- **Correction to its locators.** Page numbers (p.4-5, p.16-17, App. A p.22) could not be checked
  against the HTML. Section locators are substituted here. Surya-Zalel App. A does define
  "covariant observable" as stated.
- **Correction to its claim "Observers and records: nothing in any of the three papers".** It holds
  for the three papers it read. However, gr-qc/0202097v1, which that note did not read, has the
  Sec. 7 "we inhabit" passage.
- **Correction to its RC-4(a) derivation.** The derivation is right at finite stage. It is
  published as Brightwell-Luczak order-invariance, with Rideout-Sorkin GC read that way. Its
  "completed infinite case is not argued" caveat matters: Sec. 3.A above shows non-sufficiency in
  the infinite limit for DGC-only walks.
- **Its claim that Surya-Zalel "show the measure may fail to extend" is confirmed, with precision.**
  They give a sufficient criterion for extension and a sufficient criterion for failure (Theorem
  3.1). Failure is proved for CP with q not in [0,1] and for single t_1 not in R+. One family is
  left undecided (k_m - k_{m-1} = 1).
- **`candidate-A.md`.**
  - The Dowker-Surya title is confirmed; it was listed as a snippet-only title.
  - The "Wallden ... records work ... not searched" gap is now searched, with no causal-set records
    paper found.
  - The "partly occupied" verdict is strengthened: both the finite-stage indistinguishability and
    the covariant/labelled translation are in print.

## 8. Narrowest unaddressed cases and likely defeaters (no novelty claim)

1. **Norm-only GC with path-dependent phases plus an extending vector measure.** Does
   Phi-dependence reach covariant events?
   - Most likely defeaters:
     - forward citations of 2603.25503 and 2003.11311;
     - Surya's and Zalel's later quantum growth papers;
     - Sorkin, "Toward a fundamental theorem of quantal measure theory" (MSCS 2012, cited by
       Surya-Zalel as [17]);
     - a quantum covtree walk (1910.07292v2 Sec. 5 (v)), if one has been published.
2. **Non-extending complex models with conditional convergence along a stage ordering.** Do
   different orderings give different covariant predictions?
   - Defeaters:
     - Sorkin-Surya "Constructing covariant observables in complex percolation" (cited as "in
       preparation"; not found);
     - Sorkin MSCS 2012.
3. **DGC-only infinite-limit non-sufficiency (Sec. 3.A).** Does any Bell-causal CSG model exhibit
   it?
   - Defeaters:
     - Brightwell's unpublished notes (cited by Sorkin gr-qc/0703098v1 [7]);
     - Brightwell-Luczak 0901.0242v2 body (uniqueness theorems; unread);
     - Brightwell-Georgiou on CSG large-scale structure (cited in 0901.0240v3 Sec. 1; not read).
4. **An embedded record model.** For example, a decorated causet whose sub-structure encodes
   records. Is any physically motivated record a non-covariant event?
   - Defeaters:
     - Dowker-Zalel 2212.01149 (cylinder-type algebra for cyclic dynamics; abstract only here);
     - Zalel's PhD thesis (2021; not located);
     - work on causal-set observers in the philosophy literature (Wüthrich-Callender already in
       KB; Arageorgis and Earman not read).

## 9. Unread or partly read, and why

- **Not available.**
  - Brightwell, unpublished notes on general covariance: not public.
  - Sorkin-Surya, "Constructing covariant observables in complex percolation": cited as in
    preparation, no arXiv entry found.
- **Not reached in this run.**
  - Sorkin, MSCS 22 (2012) 816-852: arXiv ID not identified.
  - Zalel PhD thesis: not located.
- **Abstract only.** gr-qc/0504066, gr-qc/9401003, 1106.6269, 2212.01149, 2008.02607, 0901.3675,
  1307.6167. The reason is time priority; none was named as decisive in the brief except
  gr-qc/0504066, which is covered through Dowker-Surya.
- **Partly read** (see each record's limits).
  - 1007.2725v1 Sec. 3.
  - 2603.25503v1 Secs. 3.3-3.5 and Appendix.
  - 0901.0240v3 Sec. 8 proofs.
  - 0901.0242v2 beyond Sec. 1.
  - 2109.10749v1 Sec. 4.
  - 2302.10582v1 Secs. 4-6.
  - 1902.05082v3 Secs. 2 and 3.2-3.3.
  - 1405.0638v1 Secs. 3 and later.
- **Publisher versions not compared.** None of the publisher versions behind the recorded DOIs
  was compared with the arXiv versions read.
