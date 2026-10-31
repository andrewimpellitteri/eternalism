# Dense-stage countermodel review

**Verdict.** The construction in `tense-domain/DENSE_STAGE_CHECK.md` satisfies the displayed (D), (T1)–(T3), T(m) ⊆ D(m), and Loss's separate multiple-possible-futures assumption. Under Loss's displayed stage-relative tense and quantifier clauses, it falsifies (GB1). The branching-tree details check out, including ancestor closure of maximal histories and preservation of the eventually-zero condition. The result is conditional on those formal clauses; Loss's surrounding description and Figure 3 portray ordinary append-at-the-edge growth, which the construction does not model.

## Clause-by-clause check

Use nodes m=(t,p), t<0, where p:(−∞,t)→{0,1} is eventually zero toward −∞. Define mRn when m=(t,p), n=(u,q), t<u, and q restricted to (−∞,t) equals p. Let D(m)=T(m)=(−∞,t)∪{0}, with the usual order on times.

- **(D):** If mRn, then t<u, and (−∞,t)∪{0} is a proper subset of (−∞,u)∪{0}. Strictness is witnessed by t ∈ D(n)\D(m).
- **(T1), (T2), (T3):** Time domains persist by inclusion; the usual order on old times is unchanged; and 0 is the unique latest time at each node. Also T(m)=D(m), so the stated subset condition holds.
- **Multiple possible futures:** Fix any m=(t,p), choose u∈(t,0), and extend p to two distinct functions q₀,q₁ on (−∞,u) that differ somewhere in [t,u). Both extensions remain eventually zero toward −∞, and each gives an R-future of m. Indeed there are infinitely many such extensions. This also means the construction has no terminal stages, matching the source's footnote 17 convention of setting aside growth that stops.

The node relation has the required tree-like past. If (s,r)R(t,p), then necessarily s<t and r is p restricted to (−∞,s), so there is exactly one predecessor at each earlier index s; the predecessors are linearly ordered by s. More importantly for the tense clause, every maximal R-chain containing m=(t,p) contains every such ancestor. Each ancestor is comparable with every member of a chain containing m: earlier members must be restrictions of p, and later members extend p. If a maximal chain omitted that ancestor, it could be added while preserving linearity, contradicting maximality.

The eventually-zero restriction is stable in both directions needed by the construction. Restricting an eventually-zero function to an earlier domain remains eventually zero; extending it leaves its sufficiently early values unchanged, so the extension remains eventually zero. Any two nodes also have a common all-zero ancestor: choose an index earlier than both domains and earlier than both functions' zero cutoffs. Thus branch histories share a past, while incompatible extensions cannot later merge.

## Why (GB1) fails under the displayed semantics

Loss defines E x as ∃y(x=y), and his stage-relative existential quantifier ranges over D(m) (PMC HTML lines 174–177). Hence at a stage m, E x holds exactly when x∈D(m). The past operator quantifies over earlier stages on the same history (lines 171–173).

Fix any node m=(t,p) on any maximal history h. Every x∈D(m) already exists at some earlier ancestor on h: if x=0, choose any v<t, since 0∈D(v); if x<t, choose v with x<v<t, so x∈D(v). By the maximal-chain argument, (v, p restricted to (−∞,v))∈h. Therefore P E x holds for every currently quantified x∈D(m), making ∃x ¬P E x false at m,h. This holds at every node of every history, so its always-form A∃x ¬P E x is not valid (indeed false throughout this model). The structure thus falsifies the displayed GB1 while satisfying the stated structural clauses.

The mechanism is not failure of proper domain growth. At every t<u<0, the domain strictly increases. Rather, each x<0 first appears in the domain comparison after its cut t=x, but there is no earliest stage index after that cut in the dense order. The permanent element 0 has existed at every stage. Consequently there is no first-existence witness at any stage.

## Scope of the result

Loss calls (D) and (T1)–(T3) necessary/plausible constraints and explicitly leaves the general necessary-and-sufficient conditions on R open (lines 149–168). He then separately assumes every stage has multiple possible futures and invokes the proper-superset reading of (D) in the GB1–GB2 claim (lines 174–178). The countermodel meets those displayed assumptions. His prose also describes newer entities coming into existence (lines 114–119), and Figure 3 depicts a block whose latest time advances as more times are included (lines 157–160). The present construction instead inserts times below a fixed latest time. Thus it shows that the listed formal clauses alone do not encode append-at-the-edge growth; interpreting stages as only those append-at-the-edge possibilities would add a further semantic/modeling condition. This is a formal-scope observation, not an attribution of error to Loss and not a refutation of his intended account.

**Primary locator:** Roberto Loss, “Open future, supervaluationism and the growing-block theory: a stage-theoretical account,” *Synthese* 199 (2021), 14249–14266, corrected publication 2022, DOI 10.1007/s11229-021-03419-7, original PMC HTML §§2.3–2.4 as relevant: lines 149–182; especially tense and quantifier clauses and GB1–GB2 at lines 171–178. The displayed existential-clause footnotes 20–21 explain assignments and the union domain at lines 315–321; footnote 17 at lines 304–305 sets aside terminating growth. This is a clause-level audit, not a complete audit of the article's semantics or metaphysical interpretation.
