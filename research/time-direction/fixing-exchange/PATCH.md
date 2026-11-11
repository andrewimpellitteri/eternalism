# PATCH.md — proposed repair to the direction-of-time section

10 November 2026. Coordinator session (Claude Code, Fable 5.2), at the user's request.
**Applied to `main.tex` on 10 November 2026 at the user's instruction.** The pinned hash
is the source before the edits. The note behind it,
[RESULT.md](RESULT.md), has a self-review only ([REDTEAM.md](REDTEAM.md)).

## Pinned source

- File: `research/what-the-past-can-fix/main.tex` (hand-written, not generated)
- SHA-256: `9d103bb5b71d6e573ec97a471fa7136849962705bf13aee912d2a172715804b9`
- Section: `\section{The direction of time}\label{sec:direction}` (line 526)

## Scope

The repair removes one false sentence, adds the statement that is true in its place,
and adds the closed dust corollary that shows why the sentence was false. It uses only
results already in the paper (Theorem `thm:massive`, Proposition `prop:mirror`) and
elementary linear algebra. It adds no citation, because the sources that should be
credited for the stationary-chance material (Markosian 1995; Crutchfield, Ellison and
Mahoney 2009) have not been read at the depth the paper requires. For that reason the
stationary result of RESULT.md §5 is **not** proposed for the paper here.

| Edit | Where (line) | Kind |
|---|---|---|
| D1 | Before the paragraph "So exact fixing has no arrow of its own." (540) | New proposition and corollary |
| D2 | First two sentences of that paragraph (540) | Replace |
| D3 | Open-question paragraph (548) | Replace one sentence |
| D4 | Abstract (50), optional | Replace one clause |

## D1. New proposition and corollary

Insert after the paragraph ending

```latex
Theorem~\ref{thm:main} carries its orientation in (CB); reverse it and the same proof gives the future lobe.
```

New text:

```latex
The mirror relates a past base at $b$ to a future base at $\theta(b)$. It does not compare the two bases at one standpoint. For that comparison the right objects are not the fixed events but the fixed quantities.

\begin{proposition}[Reciprocity and balance]\label{prop:balance}
Let $\mathcal L$ be a vector space $V$ of real fields on $M$, or a translate of one, and for $A\subseteq M$ let $K_A=\{\varphi\in V:\varphi|_A=0\}$. Let $A,C\subseteq M$.
\begin{enumerate}
\item A quantity that depends only on the field on $C$ is fixed by the field on $A$ if and only if it is a function on $V/(K_A+K_C)$. So what $A$ fixes about $C$ and what $C$ fixes about $A$ are the same quantities.
\item The freedom left on $C$ when the field on $A$ is given is $K_A/(K_A\cap K_C)$, and the freedom left on $A$ when the field on $C$ is given is $K_C/(K_A\cap K_C)$.
\item When these spaces are finite-dimensional, their dimensions differ by $\dim V|_C-\dim V|_A$.
\end{enumerate}
\end{proposition}

\begin{proof}
A function on $V$ depends only on the field on $A$ exactly when it is constant on cosets of $K_A$, and a function constant on cosets of $K_A$ and of $K_C$ is constant on cosets of $K_A+K_C$. The fields on $C$ compatible with a given field on $A$ form a coset of the image of $K_A$ under restriction to $C$, and the kernel of that restriction is $K_A\cap K_C$. The last claim follows from $\dim V|_A=\dim V-\dim K_A$.
\end{proof}

In particular no reading fixes another one way. If $y,z\notin F_{\mathcal L}(S)$ and $y\in F_{\mathcal L}(S\cup\{z\})$, then on $K_S$ the evaluation at $y$ is not zero and vanishes on the kernel of the evaluation at $z$, so it is a nonzero multiple of it, and $z\in F_{\mathcal L}(S\cup\{y\})$.

So two bases can differ in what each leaves open about the other, and only by the difference in what they carry. No symmetry of the law is used, and the statement holds for linear laws that are not reversal invariant. An event of $C$ lies in $F_{\mathcal L}(A)$ when its reading is one of the shared quantities; the sets $F_{\mathcal L}(A)\cap C$ and $F_{\mathcal L}(C)\cap A$ need not correspond, because a shared quantity can be a point reading on one side and not on the other.

\begin{corollary}[An arrow from epoch]\label{cor:epoch}
On the closed dust model let $m>0$ and $b=(\tau,Y)$. Then $F^+_m(b)=M$ for $0<\tau\le\pi$ and $F^+_m(b)=\Jp(b)$ for $\pi<\tau<2\pi$. Consequently, for $\tau<\pi$ the field on $\Isp(b)$ fixes the whole solution while the field on $\Is(b)$ does not; for $\tau>\pi$ the reverse holds; and for $\tau=\pi$ each fixes the whole solution.
\end{corollary}

\begin{proof}
The reflection $\eta\mapsto2\pi-\eta$ is an isometry reversing time orientation, and $\mathcal L_m$ is invariant under pullback by any isometry. Apply Proposition~\ref{prop:mirror} to Theorem~\ref{thm:massive}.
\end{proof}

In the terms of Proposition~\ref{prop:balance}, with $A=\Is(b)$ and $C=\Isp(b)$: before maximum expansion $K_C=0$ and $K_A\neq0$, so everything about the past of $b$ is fixed by its future and its future is open given its past. This is one law, one model and one standpoint, with the two bases on an equal footing. The law is reflection invariant and so is the geometry. The asymmetry at $b$ comes from where $b$ sits: the future of an early event contains a Cauchy surface and its past does not.
```

## D2. The false sentence

Old:

```latex
So exact fixing has no arrow of its own. Under equal bases each side is as fixed or unfixed from the other. ``The past is fixed and the future open'' cannot be read off the fixing relation, and the asymmetry needs another source.
```

New:

```latex
So the laws give exact fixing no arrow of their own. A model can still have one, as Corollary~\ref{cor:epoch} shows, and Proposition~\ref{prop:balance} says what it consists in: an imbalance in what the two bases carry. The arrow of Corollary~\ref{cor:epoch} points toward the larger side of the universe and reverses at maximum expansion, so it is not the asymmetry of ordinary thought. ``The past is fixed and the future open'' cannot be read off the laws, and where global geometry does not supply it the asymmetry needs another source.
```

## D3. The open question

Old:

```latex
We expect exact fixing to change little, since a macrocondition does not fix exact values, and the asymmetry to appear in conditional probabilities over completions.
```

New:

```latex
A selection of solutions can create one-way exact fixing only by making one reading a non-injective function of another, which the remark after Proposition~\ref{prop:balance} excludes for linear classes and a selection can restore. We expect a macrocondition to do this for few exact readings, since it does not fix exact values, and the asymmetry to appear in conditional probabilities over completions. There it has a definite size. For discrete readings $a$ of the past base and $c$ of the future base, under any probability measure on $\mathcal L$, $H(c\mid a)-H(a\mid c)=H(c)-H(a)$: the future is more open than the past, each given the other, by the amount by which its description carries more entropy.
```

The one-line argument that supports this clause is included in D1.

## D4. Abstract (optional)

Old:

```latex
Fixing also has no arrow of its own: for time-reversal invariant laws every such result has a mirror image, so the slogan that the past is fixed and the future open needs another source.
```

New:

```latex
The laws give fixing no arrow of their own: for time-reversal invariant laws every such result has a mirror image. A model can have one from its global geometry, as the closed dust universe does before and after maximum expansion, but that arrow reverses with epoch, so the slogan that the past is fixed and the future open needs another source.
```

If this exact sentence is not in the abstract as one string, apply by hand; the
anchor check below reports it.

## Not proposed

- The stationary-chance result and its bearing on Nomic Presentism (RESULT.md §5).
  It needs Markosian (1995) and the computational-mechanics papers read and cited
  first, and it belongs in the Markovian-presentism reply before the unified paper.
- Any change to `CLAIM_STATUS.md` or the synthesis.
- The introduction's "Fixing has no arrow of its own" phrase at line 111, which sits
  in a list of section pointers and stays acceptable once D2 is in.
