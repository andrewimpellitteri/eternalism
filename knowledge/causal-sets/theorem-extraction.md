# Causal sets: theorem-level extraction

Status 2026-10-19. Claude-subagent completion of the lane; see AGENT_REPORT.md. Equation and
lemma numbers follow the arXiv renders named in sources.jsonl. Quotes are copied from the
extracted texts (ar5iv/arxiv HTML); sub/superscripts were flattened by extraction, so formulas
below are restated from the LaTeX source where noted. "Authors' claim" is not "established".
Not a novelty claim.

## 1. Rideout-Sorkin, gr-qc/9904062v3 (cs-rideout-sorkin-2000-v3), read depth full-text

Notation (Sec. 1.1): a causet is a locally finite poset, irreflexive order; a partial stem is a
finite subset containing its own past; a transition C->C' adds one maximal element whose past is
the "precursor set" (a partial stem of C); an n-element parent has "stage n".

Definitions (Sec. 3):
- Internal temporality: "each element is born either to the future of, or unrelated to, all
  existing elements; that is, no element can arise to the past of an existing element";
  equivalently the birth labelling is natural (x < y implies label(x) < label(y)).
- Label independence = discrete general covariance: "the net probability of forming any
  particular n-element causet C is independent of the order of birth we attribute to its
  elements. Thus, if gamma is any path through the poset P of finite causal sets that
  originates at the empty causet and terminates at C, then the product of the transition
  probabilities along the links of gamma must be the same as for any other path arriving at C."
  (Needs care: a link of P can represent several transitions; each representative must share
  the probability.) Only natural labellings are treated (footnote 3). Caveat stated by the
  authors: path independence "does not necessarily mean that [the arrival probability]
  carries an invariant meaning ... a statement like 'when the causet had 8 elements it was a
  chain' is itself meaningless before a certain birth order is chosen".
- Bell causality, Eq. (2): for children C1, C2 of C,
  prob(C->C1)/prob(C->C2) = prob(B->B1)/prob(B->B2),
  where B is the union of the two precursor sets, B_i = B plus an element added "in the same
  manner" as in C->C_i. Spectators (elements in neither precursor) may be deleted. Footnote 7:
  both numerators and denominators assumed nonzero.
- Markov sum rule: transition probabilities out of a parent sum to 1, counting children by
  distinct precursor sets (elements treated as distinguishable; multiplicities in the sum).

Results (Sec. 4; derived under the extra genericity assumption that no transition probability
vanishes):
- Lemma 1: at most one free parameter per family. Lemma 2: the gregarious-child probability
  depends only on |parent|; call it q_n, q_0 = 1.
- Lemma 3, Eq. (3): alpha_n = q_n * sum_{i=0}^n lambda_i / q_i with integer lambda_i.
- Eq. (7): alpha_n = sum_{k=0}^m (-1)^k C(m,k) q_n / q_{w-k}, w = |precursor|, m = number of its
  maximal elements. (Transitive percolation, Eq. (6): alpha_n = p^m (1-p)^(n-w), q_n = q^n.)
- Eq. (10)-(11): t_n = sum_k (-1)^(n-k) C(n,k)/q_k; Lemma 4: 1/q_n = sum_k C(n,k) t_k. All
  probabilities lie in [0,1] iff t_n >= 0 for all n (t_0 = 1).
- Eq. (12): alpha_n = [ sum_{l=m}^{w} C(w-m, w-l) t_l ] / [ sum_{j=0}^n C(n,j) t_j ].
- Eq. (17): lambda(w,m) := sum_{k=m}^{w} C(w-m, w-k) t_k, so q_i = 1/lambda(i,0) and
  alpha_i = lambda(w_i, m_i) / lambda(i, 0).
- Eq. (18): P(C) = prod_{x in C} lambda(w(x), m(x)) / prod_{j=0}^{|C|-1} lambda(j, 0), with
  w(x) = |past x|, m(x) = |maximal(past x)|. The labelled probability P(C~) equals P(C)
  (labelling independent) and the net probability of arriving at an unlabelled C is
  Prob_N(C) = W(C) P(C), W = number of inequivalent natural labellings (Sec. 5).
- Sec. 4.4: the family satisfies internal temporality, covariance (Eq. (18) is a product of
  poset invariants), Bell causality (ratios depend only on w, m), and the sum rule via the
  identity Eq. (15). The authors' footnote 5: the Markov assumption would have been forced by
  covariance anyway.
- Appendix Lemmas 5-6: Bell-causality equations are mutually consistent; remaining covariance
  equations reduce to identities. Examples: dust (t_0=1, others 0, antichain), forest
  (t_0=t_1=1), t_n = 1/n! offered as "candidate of the moment".

What the paper does NOT contain: any definition of "well-conditioned embedding", any notion of
observer, record or clock, any proof that labels are physically irrelevant (it is an
imposed condition), or a Bell-causality formulation free of a birth sequence (listed as open,
Sec. 7). Authors' interpretive statement, Sec. 1.1: "The phenomenological passage of time is
taken to be a manifestation of this continuing growth of the causet. Thus, we do not think of
the process as happening 'in time' but rather as 'constituting time'." This is a claim, not a
derived result.

## 2. Wuthrich-Callender, arXiv:1502.00018v1 (cs-wuthrich-callender-2015-v1), read depth full-text

Coordinator caution: the following is the secondary paper's prose reconstruction of Stein,
not a validated primary theorem. It omits a transitivity hypothesis and requires care about
reflexivity versus a strict past-pointing vector. The foundations lane already identified
problems with isolated Stein transcriptions. Do not reuse this as a formal statement.

Kinematics (Sec. 3). Stein's theorem as the authors state it: a binary relation R ("is definite
as of") on Minkowski space R^n, n >= 2, reflexive, non-trivial, non-universal, invariant under
time-orientation-preserving automorphisms and Lorentz covariant; if Rab holds for some pair
with ab past-pointing (timelike or null) then Rxy holds iff xy is past-pointing, i.e. R is
"is in the causal past of". The authors' claim: "The analogue of this theorem ... is
straightforwardly false in CST", shown by the four-element 'counterexample causet' (a minimal,
b and c incomparable middle, d maximal; R = reflexive pairs, past pairs, and the symmetric pair
<b,c>,<c,b>). R is automorphism invariant, neither trivial nor universal, yet includes a
spacelike pair. Mechanism: "non-Hegelian" events (identical relational profiles, pairwise
unrelated) can be swapped by automorphisms, whereas in Minkowski invariance plus transitivity
collapses R to the universal relation.
Their assessment: non-Hegelian subsets large enough to define a near-global present are, they
suspect, not generic (only an unpublished Meyer estimate for a 1+1 sprinkling is cited);
regular causets that have them would break Lorentz invariance; so "CST embraces [the dilemma]
and even makes it rigorous". Stein-style 'local' becoming (R = causal order) is available but
is observer-dependent and has Minkowski counterparts (Clifton-Hogarth).

Dynamics (Sec. 4).
- CSG read as a stochastic process is a sample space of labelled causets "run to infinity", a
  sigma-algebra and a measure: "the theory consists simply of a space of tenseless histories
  with a probability measure over them" (compatible with a block picture; Huggett's first option).
- Labels are pure gauge; with Alice's/Bob's birthday example, discrete general covariance makes
  "which came first" factless, so growth in label time is hard to read as a physical process.
  Earman's actualised-path proposal reintroduces becoming but conflicts with the pure-gauge
  reading (per Arageorgis).
- Their "novel and exotic" proposal: quotient by relabelling; the number of elements is gauge
  invariant, so there is gauge-invariant growth C1 -> C2 -> C3, but no fact which elements
  exist at stage 2 (a or b): "there is a determinate fact that it contains one of them".
  They say this is a model of ontological indeterminacy/vagueness, depends on event identity
  conditions, makes the past indeterminate too, and for percolation 'posts' (Fig. 3) elements
  become determinate at finite stages unless one insists the final causet is not fixed at any
  finite stage. They note the measure is defined only on Omega(infinity).
- Not claimed: that this becoming is the A-theorist's passage; they say it does "not answer
  to the typical A-theoretic demands".

## 3. Madsen, arXiv:2607.05840v1 (cs-madsen-2026-v1), read depth full-text for statements

Definition 2.6 (well-conditioned embedding). Let C be a finite causal set, (M,g) globally
hyperbolic, dimension d, curvature scale lambda := sup_T min(inj(M,h_T), |Rm[g]|^(-1/2)), where
h_T = g + 2 T_flat (x) T_flat (Eq. (1)). f: C -> M is (rho, c_*, K_d)-well-conditioned if:
- (F1) exact order preservation: f(x) in J^-(f(y)) iff x <= y.
- (F2) uniform density at scale: for every causal diamond D in [tau_min, c_* lambda] proper time
  and at h-distance >= c_* lambda from the boundary, | |f(C) cap D| - rho Vol(D) | <=
  delta_D rho Vol(D), delta_D = K_d sqrt(log(rho V_M) / (rho Vol_g(D))), with tau_min =
  c_*^(-1) rho^(-1/d) (log rho V_M)^(2/d) (Eqs. (2)-(4)). Coordinator checked the square
  root directly in the versioned arXiv HTML Eq. (4), 2026-10-19.
- (F3) distance preservation, Eq. (5): longest-chain length l_C(x,y) rescaled by (m_d rho)^(1/d)
  approximates proper time tau_g(f(x),f(y)) within C_d (tau^2/lambda^2 + log^(3/2)(rho V_M) /
  (rho V_M)^(1/(2d))) tau. Author footnote: whether F2 implies F3 is open.
Theorem 4.18 (as stated): two (rho, c_*, K_d)-well-conditioned embeddings of one finite C into
globally hyperbolic d-manifolds with curvature scale lambda and rho lambda^d >= c_*^(-2d)
(log rho V_max)^2 give a smooth diffeomorphism Phi: M1deg -> M2deg of the deep interiors with
Phi* g2 = g1 + E, ||E|| = O(rho^(-2/(5d)) lambda^(-2/5) log^(3/2)(rho V_max)) (Eq. (39)).
Proof strategy: Lorentzian trilateration with a d+1 anchor scaffold (Sec. 3, Lemma 4.1) and an
approximate Alexandrov-Zeeman/Procrustes step; moving Riemannian (Karcher) mean with
smoothing scale l* = rho^(-1/(5d)) lambda^(4/5); local diffeomorphism by cross-covariance
non-degeneracy (Lemma 4.10, Prop. 4.11); degree argument for global (Prop. 4.12); rigidity
Prop. 4.16.
Theorem 5.1: a Poisson sprinkling at density rho of such (M,g) is (rho,c_*,K_d)-well-conditioned
with probability >= 1 - (rho V_M)^(-K_d'). Corollary 5.6: a single C that is a Poisson
sprinkling of two such spacetimes forces them to agree up to epsilon(rho,lambda) =
O(rho^(-2/(5d)) lambda^(-2/5) log^(3/2)), with probability >= 1 - 2 (rho V_max)^(-K_d').
"Covariance" here is the covariance matrix Sigma(x) of embedded points (Lemma 4.3, Eq. (22)),
isotropic and non-degenerate under F2; it has nothing to do with discrete general covariance.
Sec. 6.2 (author's description of priors): Malament's theorem gives conformal structure from
causal order; Muller (arXiv:2503.01719) reportedly shows the finite order-only Hauptvermutung
is false and proves a countable dense-subset version. The paper concerns completed causets and
Poisson sprinklings, with no growth dynamics.
Unread/unchecked: proofs of Props 4.8-4.15 and 5.3, Appendices A-E, the Muller paper.

## 4. Original reconstruction results (not read)

Bombelli-Lee-Meyer-Sorkin 1987 (cs-bombelli-1987), Malament 1977 JMP (cs-malament-1977-jmp) and
Hawking-King-McCarthy 1976 were not obtained (paywalls; no free copies found by a standard web
search). No theorem statement from them is asserted here; only secondhand paraphrases in the
anchors exist. They remain to be read.
