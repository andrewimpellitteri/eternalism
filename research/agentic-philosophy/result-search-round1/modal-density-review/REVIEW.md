# Independent review: dense-comb candidate

Date: 2026-10-31
Scope: Müller, “Defining a Relativity-Proof Notion of the Present via Spatio-temporal Indeterminism,” *Foundations of Physics* 50 (2020), 644–664, DOI [10.1007/s10701-019-00267-x](https://doi.org/10.1007/s10701-019-00267-x), specifically Definitions 6–12, Theorem 1, and footnotes 23–26. The journal PDF was read in full (full-text depth); no proof audit of BST beyond this paper is claimed.

## Verdict

The rational dense comb is a counterexample to Theorem 1 in the paper’s written Definition-6 hypothesis class. Its common trunk has identity co-presentness, despite the whole structure being non-featureless. The construction also satisfies the stated prior-choice condition for every pair of distinct histories and every eligible lower-bounded chain. I found no blocking defect in the candidate’s core order construction or in the trunk’s cause-like-locus calculation.

The cleanest surviving theorem-level statement is this: for the comb described below, `~` restricted to `h_T` is identity, while each branched history `h_q` has singleton classes on its trunk segment and one class consisting of its offshoot tail. Thus `~` restricted to `h_q` is neither identity nor universal. The universal relation on a *tail* must not be confused with the universal relation on the whole history.

This is a formal counterexample to the universal quantification over histories in Theorem 1, not a counterexample to a theorem about relativistic physical manifolds. No Minkowski embedding, spacelike-related events, or higher-dimensional BST result is established here.

## Construction and maximal histories

Let

\[
W=\mathbb R_T\;\cup\!\bigcup_{q\in\mathbb Q}(q,\infty)_q,
\]

with the usual order on the trunk and each offshoot, and `t_T < r_q` exactly when `t ≤ q < r`. There are no other cross-branch comparisons. Write

\[
h_T=\mathbb R_T,\qquad h_q=(-\infty,q]_T\cup(q,\infty)_q.
\]

These are exactly the maximal directed sets. A directed set containing an offshoot event can contain no point on another offshoot and no trunk point above its branch value; maximality then fills out `h_q`. A trunk-only directed set bounded above can be extended into an offshoot, while an unbounded trunk-only directed set extends to all of `h_T`.

The order on each listed history is order-isomorphic to \(\mathbb R\): on (h_q\), the trunk segment through (q_T) is followed densely by the (q)-offshoot. Consequently it has no endpoints, is dense, and every nonempty chain bounded below or above in that history has the corresponding real infimum or supremum there. Every chain in (W) lies in one listed history: a chain cannot mix incomparable branches or mix an offshoot with trunk points above its branch value. The required global infimum for a lower-bounded chain is therefore its infimum in that history, which is an event of (W). This includes chains whose offshoot part has infimum (q_T). The density condition also holds at the trunk/offshoot join because (q_T<r_q) has an intermediate (s_q) whenever (q<s<r).

For every (t\in\mathbb R),

\[
H(t_T)=\{h_T\}\cup\{h_q:q\ge t\},\qquad H(r_q)=\{h_q\}.
\]

If (t<t'), choose a rational (p\in[t,t')); then (h_p\in H(t_T)\setminus H(t'_T)). Hence distinct trunk events have distinct history sets.

## Prior choice, including the chain quantifier

For distinct histories, the shared trunk segment has a greatest point:

\[
h_T\cap h_q=(-\infty,q]_T,\qquad
h_p\cap h_q=(-\infty,\min(p,q)]_T.
\]

The maximal common event is the branch value (m=\min(p,q)), with (m=q) for the (h_T,h_q) pair. For p<q, the difference h_q\h_p contains both the trunk segment (p,q]_T and the q-offshoot tail; the reverse difference is the p-offshoot tail. In every history-pair case, all events in the relevant difference lie strictly above the maximal common trunk event m_T. Hence for every eligible nonempty chain (O\subseteq h_1\setminus h_2), m_T is strictly below every member of O and is maximal in (h_1\cap h_2). This verifies the paper’s literal lower-bounded-chain PCP condition, not only its singleton instances. If the eligible-chain phrase is read as requiring O itself to be lower bounded, the conclusion still holds; the construction supplies the same witness for every nonempty subset of the difference.

There are no other possible history-pair cases. In the paper’s split definition (p. 658), the choice points are exactly rational trunk events: each is maximal in the shared trunk of some pair of histories. Irrational trunk events are not maximal in any such shared trunk, and offshoot events occur in only one history. Each history contains non-choice events, so neither featureless clause applies: there is more than one history, and no history consists wholly of choice points. There are no incomparable-but-compatible pairs, so any no-funny-business condition whose antecedent requires such a pair is vacuous here; this observation is not needed for Definition 6 or the counterexample.

## Direct cause-like-locus and CC calculation

For a trunk event (t_T), a history outside (H(t_T)) has the form (h_p) with rational (p<t). It splits from every history in (H(t_T)) at (p_T), because its intersection with each such history has maximum (p_T). Conversely, if a trunk event (s_T<t_T) is not rational, choose a rational (p\) with (s<p<t); (h_p) and (h_T\in H(t_T)) are still undivided at (s_T), since their common trunk contains points above (s). Events not on the shared trunk cannot belong to the required intersections. Therefore

\[
\operatorname{cll}(t_T)=\mathbb Q\cap(-\infty,t).
\]

At each such (p_T), the partition of (H(p_T)) has the singleton cell \(\{h_p\}\) and the complementary cell \(\{h_T\}\cup\{h_r:r>p\}\). The histories containing (t_T) lie in the complementary cell. Thus the (t_T)-enabling outcome at (p_T) is exactly that complementary cell, and

\[
CC(t_T)=\{p_T\mathbin{\hookrightarrow}
  (\{h_T\}\cup\{h_r:r>p\}):p\in\mathbb Q,\ p<t\}.
\]

These sets differ for distinct trunk times: for (t<t'), an intervening rational index belongs only to (CC(t'_T)). Hence the trunk restriction is identity directly from Definitions 8–12.

For an offshoot event `r_q`, its only containing history is `h_q`, so Definition 8 asks for an outside history that splits from this singleton set. For each rational branch value `p<q`, the outside history `h_p` has intersection with `h_q` equal to the trunk through `p`, with maximum `p_T`; it therefore witnesses `p_T∈cll(r_q)`. The outside history `h_T` witnesses `q_T`, since `h_T∩h_q` has maximum `q_T`. Conversely, intersections of an outside history with `h_q` have maxima only at rational branch values below `q` or at `q` itself. Hence

\[
\operatorname{cll}(r_q)=\mathbb Q\cap(-\infty,q]
\]

In the rational comb under review, take `D=Q`. At any `p∈D` with `p<q`, the histories through `p` split at `p_T` into `{h_p}` and its complement `B_p={h_T}∪{h_d:d∈D,d>p}`. The history `h_q` is in `B_p`, so this is the enabling outcome for `r_q`. At `q_T`, `h_q` is the singleton split cell and is the enabling outcome. Thus

\[
CC(r_q)=\{p_T\mathbin{\hookrightarrow}B_p:p\in\mathbb Q,\ p<q\}
\cup\{q_T\mathbin{\hookrightarrow}\{h_q\}\}.
\]

All events on the `q`-offshoot tail have this same CC set. They are not co-present with trunk events, whose history sets are not singleton. The tail is one class *within* `h_q`, not a class equal to the whole history. Each `h_q` also contains trunk events with distinct CC sets, so its restricted relation is non-identity and non-universal. This corrects the earlier review’s offshoot calculation: I had incorrectly required a witness to split from every outside history, whereas Definition 8 requires an existential outside history that splits from the (here singleton) containing-history set.

The trunk and offshoot calculations agree with the paper’s Fact 4 characterization, `e₁ ~ e₂` iff `H(e₁)=H(e₂)`, but do not need that fact to establish either CC result. Theorem 1 fails already on `h_T`, where the relation is identity. The offshoot calculation confirms that this failure does not depend on a mistaken claim that a whole history has the universal relation.

## Bounded arbitrary-branch-set generalization

Replace `Q` throughout the comb construction by arbitrary `D⊆R`, with one offshoot `(d,∞)_d` for each `d∈D`. Use `h_T=R_T` and `h_d=(-∞,d]_T∪(d,∞)_d`. Every such `D` gives a Definition-6 structure when chains are nonempty: the maximal directed sets are exactly these histories; each is order-isomorphic to `R`; every chain lies in one history; and the real infimum/supremum supplies the required bound event. Density at a trunk/offshoot join uses the dense real order on the trunk when `t<d`, and the dense offshoot when `t=d`. For distinct histories the common trunk has maximum `m_T`, where `m` is the smaller branch value (or the sole branch value in a trunk/offshoot pair). Every event in either difference lies strictly above this maximum, including the trunk segment in `h_d\h_e` when `e<d`. Thus `m_T` witnesses PCP for every nonempty chain in the difference. The empty-chain convention is not needed; under the requested nonempty-chain convention the audit is direct.

For `d∈D`, let `B_d={h_T}∪{h_e:e∈D,e>d}`. The partition at `d_T` has cells `{h_d}` and `B_d`. Direct application of Definition 8 gives

\[
\operatorname{cll}(s_T)=D\cap(-\infty,s),\qquad
CC(s_T)=\{d_T\mathbin{\hookrightarrow}B_d:d\in D,\ d<s\}.
\]

Consequently, for `s<t`,

\[
CC(s_T)=CC(t_T)\quad\Longleftrightarrow\quad D\cap[s,t)=\varnothing.
\]

This remains true for isolated points, endpoints of gaps, dense sets, and sets with accumulation points: membership at `s` changes the CC set between `s` and any later `t`, while a branch point at `t` is not yet in `CC(t_T)`.

For an offshoot event `r_q` with `q∈D`, the corrected existential calculation gives

\[
\operatorname{cll}(r_q)=D\cap(-\infty,q],\qquad
CC(r_q)=\{d_T\mathbin{\hookrightarrow}B_d:d\in D,d<q\}
\cup\{q_T\mathbin{\hookrightarrow}\{h_q\}\}.
\]

Thus the offshoot transition includes every continued transition at an earlier branch point, as well as the departure transition at `q`. The last transition distinguishes every trunk event `s_T` with `s≤q` from the offshoot tail.

Choice points are exactly trunk events indexed by `D`. With no incomparable compatible events there are no modal correlations. The structure is non-featureless exactly when `D` is nonempty and `D≠R`: the first condition gives multiple histories, and the second ensures that `h_T` is not wholly made of choice points; no offshoot history is wholly choice points. If `D` is nonempty, `~` on `h_T` is never universal, since crossing any `d∈D` adds its CC transition. It is identity exactly when `D` is dense, by the displayed iff. Hence its restriction to `h_T` is nontrivial exactly when `D` is not dense. Every offshoot history `h_q` has a nontrivial relation for every `D`: its tail contains multiple mutually co-present events, and its prebranch trunk event `q_T` has a different CC set. Therefore, for nonempty proper `D`, every history has a nontrivial relation iff `D` is not dense.

Endpoint cases: `D=∅` gives a single history and universal co-presentness, so it is featureless by clause (i). `D=R` makes `h_T` wholly choice points and the structure has no modal correlations, so it is featureless by clause (ii); its trunk relation is identity. Dense proper `D` is non-featureless but fails the every-history conclusion because the trunk relation is identity. This is an exact classification only within this comb family; it proves neither a general BST repair nor a novelty claim.

## Corrections and limits in the candidate

- **Core result survives.** Definition 6 on pp. 657–658 states no stronger restriction excluding this order. Footnote 23 expressly omits Weiner’s postulate for simplicity; the comb also appears to satisfy it, since any two chains in a common trunk segment have the same real suprema in histories containing them. This additional observation does not enlarge the theorem’s physical scope.
- **Choice-point wording.** “Choice point” is pair-relative in the paper’s definition. The claim that rational trunk events are exactly the choice points should be read as “exactly the events that are choice points for at least one pair of distinct histories.” Non-rational trunk points are not choice points for any pair; offshoot points belong to no distinct shared-history pair.
- **Prior-choice supporting description.** The candidate understates the h_q\h_p difference when p<q: it includes trunk events in (p,q]_T as well as the q-offshoot tail. This does not break PCP; p_T remains strictly below the entire difference and maximal in the shared trunk.
- **Footnote 26.** The comb does establish that “every event is a choice point” is not necessary for identity on a history: the trunk has identity CC while containing irrational non-choice events. It does not show that the footnote’s stated condition is insufficient; that condition is presented as a sufficient identity case, not an iff characterization.
- **No proof of a minimal repair.** The proposed “sparseness” condition is a candidate restriction, not a proved repair or a demonstrated minimal one. “Between any two events there is a stretch containing no choice point” needs a precise quantifier and interval convention, and no argument establishes that it suffices in the paper’s full BST class, especially with non-past cause-like loci. No independently established physical premise is supplied by calling chancy events localized or generically sparse.
- **No metric for ‘arbitrarily small’ perturbations.** Moving from a dense rational branch set to the accumulation set \(\{1/n:n\ge1\}\) changes the order-distribution qualitatively, but the candidate gives no metric on branch-point sets or perturbation map that makes this change arbitrarily small. The point-like and unbounded classes can be calculated for the two examples; the continuity/instability claim under arbitrarily small redistribution is unsupported as stated.
- **Scope.** The source itself calls histories “space-times” in its BST framework (pp. 656, 661), but this abstract order is not thereby a relativistic spacetime in the geometric or empirical sense. It has no spacelike-separated event pairs and no Minkowski or physical-manifold representation established here. The proper conclusion is that the written abstract BST theorem is false without an additional hypothesis, not that relativity, presentism, or objective passage is refuted.
- **Priority.** This review did not independently conduct the candidate’s citation/erratum search. The absence of a known correction or predecessor remains unverified here; no priority claim follows from this audit.

The article gives Theorem 1 immediately after its statement on pp. 661–662 and no proof there. Its footnote 26 says identity would result if every event were a choice point with no modal correlations. The dense-comb calculation supplies a counterexample to the theorem’s conclusion without satisfying that sufficient scenario. The journal-level formal error is therefore bounded and checkable, while the candidate’s stronger physical motivation, minimal-repair, instability, and priority claims remain open or unsupported.

## Correction log

2026-10-31 follow-up: corrected the offshoot Definition-8 quantifier error in this review. The cause-like loci for `r_q` include every earlier branch point `p∈D, p<q` witnessed by `h_p`, as well as `q` witnessed by `h_T`; the CC set includes the corresponding continued transitions and the departure transition at `q`. Added and checked the arbitrary-`D` classification, including empty, full, dense-proper, and gap cases. The trunk counterexample and prior verdict are unchanged.
