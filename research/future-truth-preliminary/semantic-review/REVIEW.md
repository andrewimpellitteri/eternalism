# Semantic review: point freedom and future truth

## Scope and setup

Fix a spacetime $M$, a point $b$, and a linear scalar PDE on this fixed background. Assume its smooth global solution class $S$ is nonempty and affine (as for a fixed inhomogeneous linear equation); impose no norm, energy, positivity, or amplitude restriction. Let $U=I^-(b)$ and let the actual solution be $\phi\in S$. The histories compatible with the actual strict-past data are

\[
 E_\phi(b)=\{\psi\in S:\psi|_U=\phi|_U\}=\phi+V_b,
 \qquad V_b=\{h\in H:h|_U=0\},
\]

At a fixed event $x\in M$, the compatible value set is

\[
 R_x(\phi,b)=\{\psi(x):\psi\in E_\phi(b)\}
 =\phi(x)+\{h(x):h\in V_b\}.
\]

Here $H$ is the vector space of solutions of the associated homogeneous equation, so differences of elements of $S$ lie in $H$. The last set of differences is a linear subspace of $\mathbb R$. Since the only subspaces of $\mathbb R$ are $\{0\}$ and $\mathbb R$,

\[
R_x(\phi,b)=\{\phi(x)\}\quad\text{or}\quad R_x(\phi,b)=\mathbb R.
\]

In the second case, one nonzero $h\in V_b$ with $h(x)\ne0$ suffices: for every $r\in\mathbb R$, $\psi_r=\phi+[(r-\phi(x))/h(x)]h$ is a smooth global solution, agrees with $\phi$ on $U$, and has $\psi_r(x)=r$. This scaling step is essential; mere existence of one differing pair would not give all values without affine closure and unrestricted amplitudes.

## Which propositions become unsettled?

Represent a local proposition about the field value at $x$ by its truth set $A\subseteq\mathbb R$: it is true of a solution $\psi$ exactly when $\psi(x)\in A$. Relative to the actual past data, call it **settled true** if $R_x\subseteq A$, **settled false** if $R_x\cap A=\varnothing$, and **unsettled** if both $R_x\cap A$ and $R_x\setminus A$ are nonempty. Call the proposition **nontrivial on the full value domain** iff $\varnothing\ne A\ne\mathbb R$. Then, in the unrestricted affine setup:

- If $x$ is fixed from $b$, $R_x$ is a singleton, so every proposition has a settled truth value relative to these alternatives.
- If $x$ is not fixed from $b$, $R_x=\mathbb R$, so **every local proposition nontrivial on $\mathbb R$ is unsettled** relative to the actual strict-past equivalence class.
- Tautologies ($A=\mathbb R$) and contradictions ($A=\varnothing$) remain settled true and settled false, respectively, even when the value is free. For a threshold proposition such as $\phi(x)>c$, every finite real threshold $c$ gives a nontrivial truth set $(c,\infty)$, hence unsettledness follows when $R_x=\mathbb R$. The same is true for $\phi(x)\ge c$, equality to a specified value, and any other proper nonempty truth set.

Thus the conditional answer to the proposed positive-mass inference is **yes**, if its premise really is $F_L(b)=J^-(b)$ for this same unrestricted smooth solution class and fixed spacetime, and “unsettled” means variation among solutions agreeing with this actual $\phi$ on $I^-(b)$. Every $x\notin J^-(b)$ is then unfixed, so every nontrivial local threshold proposition at that $x$ is unsettled in the defined sense. This includes spacelike-incomparable points as well as points to the timelike future: “outside $J^-(b)$” is not synonymous with “future of $b$.” The conclusion is semantic/nomological variation across admissible solutions, not a conclusion about what exists or what an observer can predict.

## Quantifiers and class restrictions

The usual pairwise definition

\[
x\in F_L(b)\;\Longleftrightarrow\;\forall\psi,\chi\in S,
\ (\psi|_U=\chi|_U\Rightarrow\psi(x)=\chi(x))
\]

quantifies over every past-equivalence class. By itself, failure of this universal statement only supplies a pair, potentially in a class other than the one containing the actual solution. For an affine solution class, however, this mismatch disappears: if $\psi,\chi$ agree on $U$, then $h=\psi-\chi\in V_b$; translating and scaling $h$ around any chosen actual $\phi\in S$ creates compatible alternatives $\phi+th$. Hence in this precise affine setting global pairwise nonfixing is equivalent to non-singleton—and in fact full-real—value freedom in the actual class. Do not carry that equivalence over to a nonlinear or otherwise non-affine admissible class without proof.

The class of all smooth finite-energy solutions, with energy finite separately for each solution, is generally still closed under arbitrary real scaling for a linear equation; finiteness alone on compact Cauchy slices is not a shared upper bound. If a nonzero past-vanishing witness has finite energy, every real multiple remains finite-energy, so its evaluation image is still all of $\mathbb R$. Scaling is curtailed by a **common uniform bound** imposed on the entire comparison class, or another restriction not closed under scaling. Then the attainable value set may be proper, and a full-domain nontrivial threshold can remain settled if that set lies on one side. The criterion remains $R_x\cap A\ne\varnothing$ and $R_x\setminus A\ne\varnothing$. Specify whether “finite energy” means per-solution finiteness or a uniform cap.

## Multiple points and correlations

Pointwise freedom does not imply arbitrary joint freedom. At $(x_1,\ldots,x_n)$, the attainable vector set is

\[
 (\phi(x_1),\ldots,\phi(x_n))+
 \{(h(x_1),\ldots,h(x_n)):h\in V_b\},
\]

an affine subspace of \(\mathbb R^n\), possibly a proper subspace even when every coordinate projection is all of \(\mathbb R\). For example, if the only compatible perturbations at two points satisfy \(h(x_2)=h(x_1)\), each point can vary over all reals while the proposition \(\phi(x_1)<\phi(x_2)\) stays false whenever their actual values are equal; the diagonal joint range never crosses the inequality. Thus the one-point theorem does not settle propositions about relations between events, nor justify treating local alternatives as independently recombinable.

## Tiny branching example: truth on a history is not settled truth

Take a root $b$ with two complete branches, $H_T$ and $H_F$, and a future event label $x$ on each branch. Let $P$ say “the outcome at $x$ is 1.” On $H_T$, $P$ is true; on $H_F$, it is false. So $P$ has a determinate truth value **on each selected complete history**. At $b$, it is not settled if both branches remain admissible, since the two continuations disagree. A value's truth on the actual/selected history therefore does not by itself establish settled truth from the earlier history segment. This toy branching model illustrates a semantic distinction only; it is not a PDE counterexample or a physical model.

## Domain, reference, and interpretive limits

The argument holds $M$, $L$, $b$, the event $x$, the field interpretation, and the admissible solution class fixed across alternatives. A de re proposition about “the field value at $x$” presupposes that $x$ is a shared point of the fixed domain. If alternatives vary the spacetime or its domain, reference to $x$ needs a counterpart rule, and some alternatives may not contain $x$; the point-value argument does not supply either. Likewise, changing PDE, coefficients, boundary conditions, topology, or global solution class changes the comparison space rather than varying a solution under the same setup.

Finally, failure of the actual strict-past data to fix a proposition does not alone entail that its future referent is nonexistent, that there is objective passage, that the world is indeterministic in every sense, or that finite observers cannot know the answer. Nor does a fixed point value imply that the event is “settled” in a branching-time or metaphysical sense without a bridge premise connecting this solution-space semantics to that notion. The result concerns only truth variation across law-admissible solutions on one fixed spacetime with exactly matching strict-past field values.

## Final bounded audit of PRELIMINARY.md

**A/B/C obstruction: valid as a conditional incompatibility, not an independent no-go result.** Given two admitted models with the same stipulated complete grounds and laws, A and B yield the same truth value *from $b$* in both. C requires that value to track the designated model’s outcome, so if the two models give opposite outcomes for the same proposition, C yields different truth values. That is a direct contradiction. The argument requires the same proposition and reference across models and the asserted opposite outcomes; the physics and philosophy lie in defending the existence of such a pair and premises A–C. As the note says, B does not follow merely from “only the causal past exists,” and A is an added truth/ground supervenience principle. The derivation does not show that any premise is false.

**PDE transfer: correct under the stated affine-class conditions.** The $C_b(s^*)=s^*+V_b$ construction and scalar evaluation map establish that global pairwise nonfixing transfers to every actual-past class and yields the full real line at an unfixed point. Applying a positive-mass $F_L(b)=J^-(b)$ classification therefore gives the stated local predicate result, conditional on that classification holding for the exact same PDE, background, and solution class. This corollary says nothing by itself about grounds, truthmaking, passage, or event existence. The note correctly flags the multi-point and fixed-domain limits.

**Finite-energy correction:** read “finite norm bound destroys unrestricted scaling” as a common cap on the admissible comparison class. Requiring each smooth solution to have finite energy, including finite energy on compact Cauchy slices, is not itself such a cap: for a linear equation every finite scalar multiple still has finite energy. Thus finite-energy-per-solution alone generally preserves the scaling argument when the witness belongs to that class. A shared numerical bound, or another non-scaling-closed constraint, can restrict the evaluation image and must be analyzed separately.

## Limitation / next discriminating question

The positive-mass statement $F_L(b)=J^-(b)$ is treated here as a conditional premise from the project’s existing smooth-class note, not reproved. The next useful check is to state the exact PDE and global smooth solution class behind that identity, then test whether any intended common admissibility bound preserves full-real point-value freedom or merely nonuniqueness. That would discriminate unrestricted semantic unsettledness from bounded, finite-resource indeterminacy.
