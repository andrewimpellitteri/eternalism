# PATCH.md — proposed edits from the massive-Minkowski note

10 November 2026. Coordinator session (Claude Code, Fable 5.2), at the user's request.
**Applied 11 November 2026** under the user's instruction to improve the repository. The pinned hashes below are those of the draft date. The note behind it,
[RESULT.md](RESULT.md), has only its own self-attack as review.

## Pinned sources

- `research/horizons/main.tex`, SHA-256 `55e615411205be7d785bfb8fea7fa3c8fc92dc4461d78bee496244c6faf1b71d`
- `research/what-the-past-can-fix/main.tex`, SHA-256 `fd8b5fc234384b671ab48aa0471a3ee75310cc8483addb49b3d1e5b57943e6e1`
  (the working copy, which already carries today's uncommitted credit edits)

## Scope

The new proposition is stated at the strength actually established: part (a) in every
dimension, part (b) in one space dimension, where the decay lemma was read at its
source (Burnol, Theorem 1). The extension of (b) to higher dimensions is mentioned as
resting on an estimate that was not checked. For that reason **no row is added to
Theorem `thm:map`**, whose rows are asserted for the four-dimensional models. The
change to that theorem is to its reading paragraph only.

M1 goes into the horizons source and reaches the unified paper through
`assemble.py` (it lies inside the block copied to `parts/fixing_models.tex`, and it
does not touch the one string that script swaps there). U1–U4 go into the hand-written
unified `main.tex`.

| Edit | File | Where | Kind |
|---|---|---|---|
| M1 | horizons | After the proof of Proposition `prop:sharp` | New remark and proposition |
| M2 | horizons | Bibliography | Two entries |
| U1 | unified | Reading of Theorem `thm:map` | Replace one sentence |
| U2 | unified | Part III, after "prescribable with the same past." | Add two sentences |
| U3 | unified | Status appendix | New row |
| U4 | unified | Bibliography | Two entries |

## M1. Horizons source: remark and proposition

Insert after

```latex
agree on $\Is(b)$ but not at $x$.
\end{proof}
```

New text:

```latex
\begin{remark}[The class matters]\label{rem:class}
The witness in this proof is a plane wave, which has infinite energy. The verdict
$F_{\mathcal L}(b)=J^-(b)$ belongs to the class of all smooth solutions as well as
to the equation. The next proposition shows the verdict changing with the class
for one equation on one spacetime.
\end{remark}

\begin{proposition}[Massive fields on Minkowski spacetime]\label{prop:massmink}
On Minkowski spacetime $\mathbb R^{1+n}$ let $m>0$ and consider real solutions
of $\partial_t^2\phi-\Delta\phi+m^2\phi=0$.
\begin{enumerate}
\item[(a)] For the class of all smooth solutions, $F(b)=J^-(b)$ for every $b$.
\item[(b)] For $n=1$ and the class of finite-energy solutions (Cauchy data in
$H^1\times L^2$), $F(b)$ is the whole spacetime for every $b$, and the same holds
with the strict chronological future of $b$ as base.
\end{enumerate}
\end{proposition}

\begin{proof}
(a) $J^-(b)\subseteq F(b)$ by continuity. Let $x\notin J^-(b)$, with $b=(t_b,\vec Y)$.
As in the proof of Proposition~\ref{prop:sharp} choose a unit vector $\hat k$
such that $u=t-t_b-\hat k\cdot(\vec Z-\vec Y)$ is negative on $\Is(b)$ and positive
at $x$, and put $v=t-t_b+\hat k\cdot(\vec Z-\vec Y)$. For functions of $(u,v)$ the
equation reads $4\phi_{uv}+m^2\phi=0$. The function $j(z)=J_0(m\sqrt z)$ is entire
and satisfies $zj''+j'+\tfrac{m^2}{4}j=0$, so $R=j((u-s)(v-c))$ satisfies
$R_{uv}=-\tfrac{m^2}{4}R$ for all real $s,c$. Let $h\ge0$ be smooth with support in
$(0,\infty)$ and put
\[
\phi(u,v)=\int_0^u h(s)\,j\bigl((u-s)(v-c)\bigr)\,ds\quad(u>0),\qquad \phi=0\quad(u\le0).
\]
Since $R=1$ at $s=u$, $\phi_u=h(u)+\int_0^uhR_u\,ds$, and so
$\phi_{uv}=\int_0^uhR_{uv}\,ds=-\tfrac{m^2}{4}\phi$. Thus $\phi$ is a smooth solution
vanishing on $\Is(b)$. Taking $c$ close to $v(x)$ and $h$ a bump supported below
$u(x)$ gives $\phi(x)>0$.

(b) Take $b$ at the origin and let $\phi$ have finite energy and vanish on
$\Is(b)=\{t<-|x|\}$. At each $t<0$ the energy density vanishes on $|x|<|t|$, so all
of the conserved energy lies in $|x|\ge|t|$. For a finite-energy solution that
portion tends to zero as $t\to-\infty$ \citep[Theorem~1, with time
reversed]{Burnol2006}. Hence the energy is zero, and $\phi=0$ because $m>0$. The
future base is the time reverse.
\end{proof}

The solutions used in (a) grow like a modified Bessel function where
$(u-s)(v-c)<0$ and have infinite energy. The argument for (b) uses only the decay
of energy outside the light cone, which Burnol notes follows from H\"ormander's
estimates and fails at zero mass; for $n\ge2$ we have not checked a source for it.
A massive field carries nothing in from null infinity: its energy arrives from
past timelike infinity, which lies in the closure of every past light cone. So on
this background the past of an event fails to fix a finite-energy field only when
the field is massless. Weinstein argues that prediction from a past light cone in
electromagnetism needs the added assumption of no incoming radiation
\citep{Weinstein2011}; part (b) says that for a massive field of finite energy the
corresponding statement is a theorem, and a time-symmetric one. The fixing in (b)
uses the arbitrarily remote past, so it does not make such a field practically
predictable (compare Section~\ref{sec:mass}).
```

Checks before applying: `\Is` and `sec:mass` exist in the horizons source; `F(b)`
is the notation of that section. The theorem number cited is Burnol's own.

## M2. Horizons bibliography

Insert before

```latex
\end{thebibliography}
```

New text:

```latex
\bibitem[Burnol(2006)]{Burnol2006} J.-F. Burnol, Spacetime causality in the study of the Hankel transform, arXiv:math/0509619v4.
\bibitem[Weinstein(2011)]{Weinstein2011} S. Weinstein, Electromagnetism and time-asymmetry, arXiv:1004.1346v2.
```

These go at the end of the list, out of alphabetical order. Move them if the owner
prefers.

## U1. Unified paper: reading of Theorem `thm:map`

Old:

```latex
Determinism does not make the future fixed from a standpoint: in row one the law has unique
Cauchy evolution and nothing beyond the past is fixed.
```

New:

```latex
Determinism does not by itself make the future fixed from a standpoint: in row one the law has unique
Cauchy evolution and nothing beyond the past is fixed. That verdict belongs to the class as well as to the law. Row one is witnessed by solutions of infinite energy, and for a massive field on Minkowski spacetime the verdict changes with the class: all smooth solutions give $\Jm(b)$, while in one space dimension finite-energy solutions are fixed everywhere by the past of any event (Proposition~\ref{prop:massmink}). On an eternal flat background, the past of an event fails to fix the future only through what can arrive along null directions, or through solutions that a finiteness condition would exclude.
```

## U2. Unified paper: Part III

Old:

```latex
spacetime, $\phi(t,0)=\Phi(t)$ exactly, and every small central history is prescribable with the same
past.
```

New:

```latex
spacetime, $\phi(t,0)=\Phi(t)$ exactly, and every small central history is prescribable with the same
past. That freedom is carried by a massless field arriving from past null infinity. A massive linear field of finite energy has none of it on Minkowski spacetime (Proposition~\ref{prop:massmink}). Whether Theorem~\ref{thm:same-past} has an analogue for a massive scalar is open; the gravitational field itself remains massless.
```

## U3. Unified paper: status appendix

Insert after

```latex
The Fewster--Verch definitions were checked against arXiv v3 on 10 November\\
```

New text:

```latex
Proposition~\ref{prop:massmink}, Remark~\ref{rem:class} & Added 10 November; checked only by the session that drafted them. Part (b) is a corollary of Burnol's Theorem~1, read at its source, in one space dimension. The mathematics is not claimed as new\\
```

## U4. Unified paper: bibliography

Insert before

```latex
\bibitem[Carlotto and Schoen(2016)]{CarlottoSchoen2016}
```

New text:

```latex
\bibitem[Burnol(2006)]{Burnol2006} J.-F. Burnol, Spacetime causality in the study of the Hankel transform, arXiv:math/0509619v4.
```

and insert after

```latex
\bibitem[Wawer(2021)]{Wawer2021} J. Wawer, Tensed metaphysics and non-local grounding of truth, \emph{Disputatio} (2021). doi:10.2478/disp-2021-0023.
```

New text:

```latex
\bibitem[Weinstein(2011)]{Weinstein2011} S. Weinstein, Electromagnetism and time-asymmetry, arXiv:1004.1346v2.
```

## Not proposed

- No new row in Theorem `thm:map` and no change to its statement or proof.
- No change to the abstract or introduction. If the owner wants one, the natural place
  is the sentence in the "Determination on fixed backgrounds" paragraph that says the
  same metric gives different answers under different laws: add "and under different
  classes of solutions of one law".
- Nothing about a thin tube around a worldline, the tempered class, or the massless
  finite-energy case. None of those was verified.
