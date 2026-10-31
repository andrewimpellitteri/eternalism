# Independent narrow review: horizon monotonicity lemma

**Verdict: sound under the stated hypotheses, with the dependencies below made explicit.** The proof is elementary and does not settle any broader ontology claim. This review audits only `research/lawful-completions/coordinator/HORIZON_REVIEW.md`'s candidate lemma and historical-potential closure.

## Definitions and exact claim

Take a connected, time-oriented, smooth Lorentzian manifold without boundary. Write \(a\le b\) for causal precedence, including equality and null-related pairs, and \(a\prec b\) for \(a\le b\) with \(a\ne b\). In a causal spacetime this is a partial order. Let

\[
D(s)=\{s\}\cup\{x:\neg(s\prec x)\ \text{and}\ \exists z\ (s\prec z\land x\prec z)\}.
\]

Call the spacetime future-directed in the review's stipulated sense if every pair \(s,x\) has a common **strict causal** future. Monotonicity means \(D(s)\subseteq D(p)\) whenever \(s\le p\) (the reverse implication proof below actually constructs \(s\ll p\)). Then, if the spacetime is causally simple,

\[
D\text{ is monotone}\quad\Longleftrightarrow\quad
\text{every pair has a common strict causal future}.
\]

The smooth, time-oriented, boundaryless assumptions supply nonempty local timelike futures and pasts. Causal simplicity supplies causality and closedness of every \(J^-(x)\); global hyperbolicity is a sufficient stronger assumption.

## Proof audit

**Forward direction.** A common strict causal successor for each \((s,x)\) makes the common-future clause automatic. Thus \(D(s)=\{x:\neg(s\prec x)\}\): the explicit \(\{s\}\) is already included because \(s\not\prec s\). This is the review's no-future domain \(D_{BT}(s)\). If \(s\le p\) and \(p\prec x\), transitivity gives \(s\le x\); the case \(s=x\) would give a causal loop and is impossible, so \(s\prec x\). Hence \(\neg(s\prec x)\) implies \(\neg(p\prec x)\). Therefore \(D(s)\subseteq D(p)\). No timelike assumption on the advance \(s\le p\) is used; null advances are included.

**Reverse direction.** If future-directedness fails, choose \(x,s_0\) with no common strict causal future. A common strict causal future is equivalent here to a common chronological future: from \(s\prec z\) and \(x\prec z\), choose a local point \(w\) with \(z\ll w\); push-up gives \(s\ll w\) and \(x\ll w\). The converse is immediate since \(\ll\) implies \(\prec\). Thus

\[
P_x:=I^-(I^+(x))
\]

is exactly the set of points sharing a common strict causal future with \(x\). It is open as a union of chronological pasts and is a past set (if \(q\in P_x\) and \(r\ll q\), then \(r\in P_x\)). It is nonempty: choose \(z\) with \(x\ll z\), so \(x\in I^-(z)\subseteq P_x\). It is proper because \(s_0\notin P_x\). Connectedness of \(M\) therefore implies \(\partial P_x\ne\varnothing\); choose \(p\in\partial P_x\). Since \(P_x\) is open, \(p\notin P_x\).

Every \(y\in J^-(x)\) belongs to \(P_x\): choose \(w\in I^+(x)\), and push-up from \(y\le x\ll w\) gives \(y\ll w\). Hence \(p\notin J^-(x)\). Causal simplicity makes \(J^-(x)\) closed, so some neighborhood \(U\) of \(p\) is disjoint from \(J^-(x)\). Smoothness, time orientation and absence of a manifold boundary permit a point \(r\in U\) with \(r\ll p\), chosen sufficiently close to \(p\). The open set \(I^+(r)\) contains \(p\); since \(p\in\partial P_x\), this open neighborhood meets \(P_x\). Pick \(q\in I^+(r)\cap P_x\). Then \(r\ll q\) and \(q\in P_x\); because \(P_x\) is a past set, \(r\in P_x\). Also \(r\notin J^-(x)\), so \(r\ne x\) and \(\neg(r\prec x)\). Membership \(r\in P_x\) supplies a common chronological, hence strict causal, future for \(r,x\), so \(x\in D(r)\). On the other hand, \(p\notin P_x\) means there is no common strict causal future for \(p,x\), and \(p\ne x\) because \(p\notin J^-(x)\). Thus \(x\notin D(p)\). Since \(r\ll p\), this contradicts monotonicity. The use of \(\prec\) including null pairs is consistent throughout: null common successors are upgraded to timelike ones by a later local successor, while the violating advance itself is timelike.

This proves the candidate. The topological step is valid: a nonempty proper open subset of a connected space has nonempty boundary. The openness step used at the end is also essential: boundary points of \(P_x\) are approached from within \(P_x\).

## Assumptions that cannot be silently dropped

- **Connectedness** links the nonempty proper set \(P_x\) to a boundary point in the same spacetime. On a disconnected union of future-directed components, pairs in different components have no common future, while the pointwise domains can remain monotone component by component; the stated equivalence can fail.
- **Causal simplicity** is used specifically to make \(J^-(x)\) closed and obtain a neighborhood disjoint from it. Without that, the selected boundary point may lie in \(\overline{J^-(x)}\), and the choice of \(r\notin J^-(x)\) near \(p\) is not justified. This proof gives no conclusion for causally pathological cases.
- **Smooth time orientation and no spacetime boundary** provide local timelike points just to the past and future of every event. If a boundary is allowed, such points need not exist at boundary events; restricting the claim to interior events or adding local-past/future hypotheses repairs this proof step.
- **Causal order properties** are needed where push-up, transitivity and causal-past closedness are invoked. Global hyperbolicity suffices, but is stronger than required; causal simplicity is the exact stated closure condition.
- **A nonempty future for each point** is used for \(x\in P_x\) and to push common causal futures to common chronological futures. It follows from the smooth time-oriented boundaryless spacetime assumptions; in an abstract causal frame it must be stipulated.

The converse quantifier is right: failure of the every-pair property gives one fixed \(x\) and one \(s_0\notin P_x\). The proof then constructs a different point \(r\) just before a boundary point \(p\) so that \(x\) is in \(D(r)\) but not \(D(p)\). It does not assert \(s_0\le p\), which is unnecessary.

## Historical-potential closure \(H\)

In a causal spacetime define \(H(s)=\bigcup_{r\le s}D(r)\). This is the least pointwise enlargement of \(D\) that is monotone under \(\le\): it contains \(D(s)\) by the index \(r=s\); nesting of index sets makes it monotone; and if \(K\) is any monotone assignment with \(D(r)\subseteq K(r)\) for every \(r\), then \(x\in D(r)\), \(r\le s\) implies \(x\in K(r)\subseteq K(s)\). The minimality claim is therefore exact once “enlargement” means pointwise inclusion of set-valued assignments on the same causal preorder.

Also \(H(s)\subseteq D_{BT}(s):=\{x:\neg(s\prec x)\}\). For if \(x\in D(r)\), \(r\le s\), and \(s\prec x\), then if \(x=r\) there is a causal loop through \(r\le s\prec r\), contrary to causality. Otherwise \(D(r)\)'s defining condition gives \(\neg(r\prec x)\), whereas transitivity of \(r\le s\prec x\) gives \(r\prec x\), again a contradiction. This exclusion proof needs a causal (loop-free) spacetime and transitive causal relation; it is not valid in an arbitrary frame with cycles. No topology such as causal simplicity is needed for the abstract minimality argument, but the no-future inclusion relies on these order properties. \(H\) need not equal \(D_{BT}\), and monotone historical closure alone says nothing about ontology or physical realization.

**Scope:** this review confirms the lemma and closure statement with the explicit assumptions above. It makes no novelty, physical, or temporal-ontology claim.
