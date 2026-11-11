# PATCH.md — proposed manuscript edits from the local-clock note

10 November 2026. Coordinator session (Claude Code, Fable 5.2), at the user's request.
**Applied to `main.tex` on 10 November 2026 at the user's instruction**, with the
Ricci scalar written `\mathrm{Scal}`. The pinned hash below is the source before the edits. The note
behind these edits has had a self-review only ([REVIEW.md](REVIEW.md)); an independent
reader should check it before any edit is applied.

## Pinned source

- File: `research/stein-gr/main.tex` (1030 lines)
- SHA-256: `2ae387629fd8e2687ef3d87dedb3619975632fe4e13a0acf549650f6da28a492`
- Last commit touching it: `0587649`

## Scope

Only results that are fully proved on the manuscript's own category (connected
globally hyperbolic spacetimes) are proposed as numbered statements: Theorem 1,
Theorem 3 and Corollary A of [RESULT.md](RESULT.md), and Example 5 with the one-way
clock statement. The germ theorem and the exact criterion need disconnected objects,
so they appear only as a remark (E5), which the owner may drop.

None of the edits touches the three strings that `what-the-past-can-fix/assemble.py`
swaps in the energy section (`$M'$ above`, `$\Sigma$ as above`,
`near $w$, $v$ and the detour`). E3 adds statements to the Results section and E5 to
the Energy section, so both flow into the unified paper's `parts/` on the next
assemble. The unified paper's own prose needs the two follow-on changes in §9.

| Edit | Where (line in pinned source) | Kind |
|---|---|---|
| E1 | Introduction, "Locality is indispensable" bullet (114–117) | Replace sentence |
| E2 | Remark `rem:lc` (177–189) | Add sentence |
| E3 | After proof of Corollary `cor:nopresent` (288) | New proposition and two corollaries |
| E4 | Remark `rem:offshell` (198) | Replace sentence |
| E5 | End of Section `sec:energy` (806) | New proposition and remark |
| E6 | "A trilemma" paragraph (847) | Add sentences |
| E7 | "Locality does the work symmetry did" (857–859) | Replace clause |

## E1. Introduction bullet

Old:

```latex
\ref{prop:nonlocal}). Natural but non-local rules, such as ordering by a
canonical cosmological time, satisfy every other condition and make spacelike
events become.
```

New:

```latex
\ref{prop:nonlocal}). Natural but non-local rules, such as ordering by a
canonical cosmological time, satisfy every other condition and make spacelike
events become. Locality alone already forbids any relation that distinguishes
among spacelike-separated events of Minkowski spacetime
(Proposition~\ref{prop:noscale}).
\item \textbf{So is the range of spacetimes} (Proposition~\ref{prop:clock}).
On the class of spacetimes whose Ricci scalar does not increase to the future,
ordering by that scalar is local and transitive, contains the chronological
past, and has shared presents in dust cosmologies.
```

## E2. Remark `rem:lc`

Old:

```latex
a premise about becoming, not a consequence of relativity.
\end{remark}
```

New:

```latex
a premise about becoming, not a consequence of relativity. Reflection is
strong on its own. Before transitivity or (CB) is used, it excludes every
relation that depends on the separation of spacelike events
(Proposition~\ref{prop:noscale}). For example, the relation ``$x$ and $b$ lie
in a common diamond $\Ifut(z_1)\cap\Ichr(z_2)$ with $d(z_1,z_2)<\ell_0$'' is
defined from the metric in every spacetime and violates Reflection, since a
thin causally convex tube from $x$ to $b$ need not contain $z_1$ or $z_2$.
\end{remark}
```

Check before applying: `d` (Lorentzian distance) is not otherwise defined in the
manuscript. E3 defines it; if E3 is not taken, define it here.

## E3. New statements after Corollary `cor:nopresent`

Insert after the proof that ends

```latex
By Theorem~\ref{thm:main}(a), $x\le b$ and $b\le x$, and globally hyperbolic
spacetimes are causal, so $x=b$.
\end{proof}
```

New text:

```latex
The next three statements use (LC) alone. Call an assignment $M\mapsto R_M
\subseteq M\times M$ satisfying (LC) a \emph{local relation}; no transitivity
and no (CB) is assumed. Write $d_M(x,b)$ for the supremum of the lengths of
future causal curves from $x$ to $b$.

\begin{proposition}[No spacelike scale]\label{prop:noscale}
For every local relation $R$, $R_\Mink$ contains no pair of spacelike-separated
events or every such pair.
\end{proposition}

\begin{proof}
By (LC), $R_\Mink$ is invariant under the proper orthochronous Poincaré group,
which is transitive on ordered spacelike pairs of a given interval. So there is
$f:(0,\infty)\to\{0,1\}$ with $x\,R_\Mink\,b\iff f(s)=1$, $s$ the interval.

Let $C_\ell=\mathbb R_t\times\mathbb R^2\times S^1_\ell$ be the flat cylinder
with circle of length $\ell$; it lies in $\GH$, and $\{t=0\}$ is a Cauchy
hypersurface. Fix $0<a<\ell$ and $0<2\rho<\min\{a,\ell-a\}$. Let $x=(0,0,0)$,
$b=(0,0,a)$ in coordinates $(t,y,\theta)$, and
\[
S_1=\{t=0,\ |y|<\rho,\ \theta\in(-\rho,a+\rho)\},\qquad
S_2=\{t=0,\ |y|<\rho,\ \theta\in(a-\rho,\ell+\rho)\}.
\]
Each $S_i$ is acausal and contains $x$ and $b$. Put $N_i=\operatorname{int}
D(S_i)$. Let $\pi:\Mink\to C_\ell$ be the covering map and $\tilde S_i$ a lift
of $S_i$, a straight tube in $\{t=0\}$. We claim $\pi$ maps
$\operatorname{int}D_\Mink(\tilde S_i)$ isometrically onto $N_i$. Inextendible
causal curves lift, so $\pi(D_\Mink(\tilde S_i))\subseteq D(S_i)$. Conversely
let $p\in D^+(S_i)$ at height $\tau$ over $q\in S_i$, and let $\tilde q\in
\tilde S_i$ lift $q$. The straight past causal rays from $p$ meet $\{t=0\}$
once, in $\pi(\bar B(\tilde q,\tau))$, which therefore lies in $S_i$. The
preimage of $S_i$ is a disjoint union of translates of $\tilde S_i$, and the
ball is connected and contains $\tilde q$, so $\bar B(\tilde q,\tau)\subseteq
\tilde S_i$ and $(\tau,\tilde q)\in D^+_\Mink(\tilde S_i)$ projects to $p$.
The case of $D^-$ is the mirror image, and $\pi$ is injective over $\tilde S_i$.

$N_i$ is causally convex: if $p,q\in D(S_i)$, $p\le r\le q$ and $\lambda$ is an
inextendible causal curve through $r$, then the curve back from $q$ to $r$
followed by the past half of $\lambda$ meets $S_i$, and so does the curve from
$p$ to $r$ followed by the future half of $\lambda$; if neither meeting point
is on $\lambda$ there are $s_2\le r\le s_1$ in $S_i$, and acausality gives
$s_1=s_2=r$. Interiors follow by moving $p,q$ slightly. $N_i$ is connected,
and it is globally hyperbolic because it is isometric to
$\operatorname{int}D_\Mink(\tilde S_i)$, whose causal diamonds are compact
diamonds of $\Mink$. So $N_i\hookrightarrow C_\ell$ and
$N_i\cong\operatorname{int}D_\Mink(\tilde S_i)\hookrightarrow\Mink$ are
morphisms. In the first lift the endpoints are at interval $a$, in the second
at interval $\ell-a$. Applying (LC) four times,
\[
f(a)=[x\,R_{N_1}\,b]=[x\,R_{C_\ell}\,b]=[x\,R_{N_2}\,b]=f(\ell-a).
\]
Given $s,s'>0$ take $a=s$, $\ell=s+s'$. So $f$ is constant.
\end{proof}

The proof uses only flat spacetimes, so it holds on any full subcategory of
$\GH$ that contains $\Mink$ and the cylinders and is closed under restriction
to causally convex open subsets, including the vacuum and dominant-energy
subcategories.

\begin{corollary}[Local relations on Minkowski spacetime]\label{cor:localrel}
For a local relation $R$, $R_\Mink$ is a union of: the diagonal or nothing;
all future lightlike pairs or none; all past lightlike pairs or none; all
spacelike pairs or none; and the future (respectively past) timelike pairs
whose proper time lies in an arbitrary set $T_+$ (respectively $T_-$)
$\subseteq(0,\infty)$. Every such union is the restriction to $\Mink$ of a
local relation.
\end{corollary}

\begin{proof}
$R_\Mink$ is a union of orbits of the proper orthochronous Poincaré group, and
Proposition~\ref{prop:noscale} treats the spacelike orbits. Conversely,
equality, the horismos relations, the absence of any causal relation, and the
conditions $d_M(x,b)\in T_+$, $d_M(b,x)\in T_-$ are preserved and reflected by
morphisms, because causal curves between points of a causally convex set stay
in it.
\end{proof}

\begin{corollary}[Local presents]\label{cor:localpresent}
Let $R$ be a symmetric local relation that relates no two distinct causally
related events. Then for each $b\in\Mink$ the set of events $R$-related to $b$
is contained in $\{b\}$, or is the set of all events spacelike to $b$,
possibly together with $b$.
\end{corollary}

So a proper-time threshold survives locality and a spacelike one does not.
The causal hull of a timelike pair is the diamond between them, which every
causally convex region containing the pair contains and which fixes their
proper time. The causal hull of a spacelike pair is the two points.
```

## E4. Remark `rem:offshell`

Old:

```latex
Section~\ref{sec:energy} examines what happens without it.
```

New:

```latex
Section~\ref{sec:energy} examines what happens without it. On some natural
classes of spacetimes the conclusion then fails
(Proposition~\ref{prop:clock}).
```

## E5. End of Section `sec:energy`

Insert after the paragraph ending

```latex
literature (an abstract-level survey: Carlotto--Schoen, Corvino--Schoen,
Aretakis--Czimek--Rodnianski, Czimek--Rodnianski).
```

New text:

```latex
\paragraph{A class on which the theorem fails.} The off-shell premise cannot be
dropped in general. Let $\GH_{\mathrm{Scal}}$ be the full subcategory of spacetimes whose
Ricci scalar $\mathrm{Scal}$ is non-increasing along every future-directed causal curve.
It is closed under restriction to causally convex open subsets, and contains
$\Mink$, every vacuum spacetime, and the spatially flat expanding dust
Friedmann--Lemaître--Robertson--Walker models, where $\mathrm{Scal}$ is a positive
multiple of the density.

\begin{proposition}[A curvature clock]\label{prop:clock}
On $\GH_{\mathrm{Scal}}$ each of the following satisfies (LC), is transitive and contains
$\Ichr$:
\begin{enumerate}
\item[(i)] $\Jm_M\cup\{(x,b):\mathrm{Scal}(x)>\mathrm{Scal}(b)\}$;
\item[(ii)] $\Jm_M\cup\{(x,b):\mathrm{Scal}(x)\ge \mathrm{Scal}(b),\ \mathrm{Scal}(x)>0\}$;
\item[(iii)] $\{(x,b):\mathrm{Scal}(x)\ge \mathrm{Scal}(b)\}$.
\end{enumerate}
On $\Mink$, (i) and (ii) are $\Jm$ and (iii) is $\U$. On expanding dust models
(i) relates every event to every event of lower density, (ii) and (iii) are
the cosmic-time preorder, and the constant-density hypersurfaces are shared
presents for (ii). Hence Theorem~\ref{thm:main}(a) and (b) and
Corollary~\ref{cor:nopresent} all fail with $\GH_{\mathrm{Scal}}$ in place of $\GH$.
\end{proposition}

\begin{proof}
Morphisms preserve $\mathrm{Scal}$ and preserve and reflect $\Jm$, which gives (LC). In
$\GH_{\mathrm{Scal}}$, $x\le y$ implies $\mathrm{Scal}(x)\ge \mathrm{Scal}(y)$, which gives (CB) and the mixed cases
of transitivity. For (ii): if $x\le y$, $\mathrm{Scal}(y)\ge \mathrm{Scal}(b)$ and $\mathrm{Scal}(y)>0$, then
$\mathrm{Scal}(x)\ge \mathrm{Scal}(y)>0$ and $\mathrm{Scal}(x)\ge \mathrm{Scal}(b)$; if $\mathrm{Scal}(x)\ge \mathrm{Scal}(y)$, $\mathrm{Scal}(x)>0$ and $y\le b$,
then $\mathrm{Scal}(x)\ge \mathrm{Scal}(y)\ge \mathrm{Scal}(b)$. The remaining claims are read off.
\end{proof}

None of these is a becoming theory on $\GH$, where transitivity fails. The
third is the rule $\mathrm{Scal}(x)\ge \mathrm{Scal}(b)$ that locality alone does not exclude; what
excludes it on $\GH$ is that (T) and (CB) are demanded on every globally
hyperbolic geometry. The Milne wedge of Proposition~\ref{prop:nonlocal} is no
objection to it: the wedge is flat, and the rule returns $\Jm$ there and on
$\Mink$ alike. $\GH_{\mathrm{Scal}}$ is not a realistic class (a star has a spacelike
density gradient), and which class a becoming rule must cover is a premise we
do not argue.

\begin{remark}[Local clocks]\label{rem:clock}
More generally, let $\mathcal C\subseteq\GH$ be a full subcategory closed
under restriction and containing $\Mink$, and let $\kappa$ be a two-valued
isometry invariant of germs of the metric that is non-decreasing along
timelike curves in every member of $\mathcal C$ and non-constant on some
member $M$. Then $\Ichr\cup\{(x,b):\kappa(x)<\kappa(b)\}$ is a becoming theory
on $\mathcal C$ that equals $\Ichr$ on $\Mink$ and relates a spacelike pair of
$M$, by Lemma~\ref{lem:E}. So Theorem~\ref{thm:main}(a) can hold on
$\mathcal C$ only if $\mathcal C$ has no such local clock. If disconnected
spacetimes are admitted as objects, as in \citep[\S2.1]{FV2012}, the converse
holds too, and the theorem on $\mathcal C$ is equivalent to the statement that
every germ of $\mathcal C$ occurs chronologically after and before a flat
region, through finite chains of members of $\mathcal C$. That criterion is
weaker than the pocket problem: no slab is transported. We do not know whether
$\GH_{\mathrm{DEC}}$ satisfies it.
\end{remark}
```

Checks before applying:

- `lem:E` is stated for a single connected M; the use here is exactly that.
- The locator `\S2.1` for Fewster–Verch came from a tool extraction. Verify it.
- The converse sentence rests on RESULT.md Theorems 2 and 4, which have only a
  self-review. Drop the last four sentences of the remark if the owner wants only
  audited claims.
- The Ricci scalar is written `\mathrm{Scal}` so that it does not clash with the
  generic relation `R` of Proposition `prop:single` and of E3.

## E6. "A trilemma" paragraph

Old:

```latex
has become for another, are not addressed by the corollary. The corollary
says nothing about which horn to take.
```

New:

```latex
has become for another, are not addressed by the corollary. The corollary
says nothing about which horn to take. Rejecting transitivity buys a definite
thing in flat spacetime. By Corollary~\ref{cor:localpresent}, a local
symmetric relation among causally unrelated events of $\Mink$ is empty or is
spacelike separation itself, so the only local shared present there is the
whole elsewhere. Changing the category need not mean adding structure: a
restriction of the admissible spacetimes can suffice
(Proposition~\ref{prop:clock}).
```

## E7. "Locality does the work symmetry did"

Old:

```latex
(Proposition~\ref{prop:single}); natural global rules such as cosmological
time violate only locality (Proposition~\ref{prop:nonlocal}). So the
```

New:

```latex
(Proposition~\ref{prop:single}); cosmological time defined by proper time
from the past boundary violates only locality
(Proposition~\ref{prop:nonlocal}), while cosmic time read off a curvature
scalar is local and violates only the demand that the rule be a becoming
theory on every globally hyperbolic geometry
(Proposition~\ref{prop:clock}). So the
```

The sentence that follows ("rests on a locality principle of the kind…") should then
read "rests on that locality principle together with the off-shell premise of
Remark~\ref{rem:offshell}". Old:

```latex
curved-spacetime case for ``only the past has become'' rests on a locality
principle of the kind locally covariant field theory takes for granted and
```

New:

```latex
curved-spacetime case for ``only the past has become'' rests on the off-shell
premise of Remark~\ref{rem:offshell} together with a locality
principle of the kind locally covariant field theory takes for granted and
```

## 9. Follow-on changes in the unified paper

These are in `research/what-the-past-can-fix/main.tex`, which is hand-written, not
generated.

1. Introduction, "Becoming (Part I)" paragraph. After "Without transitivity they
   can: the bow tie of Section~\ref{sec:rigidity} has all three." add: "In flat
   spacetime it is the only local way: a local symmetric relation among causally
   unrelated events is empty or is spacelike separation
   (Corollary~\ref{cor:localpresent})."
2. Section `sec:realms`, after "Choosing between pointy and bow-tie needs further
   premises." add: "Under the locality premise of Part I no intermediate choice is
   available in flat spacetime (Corollary~\ref{cor:localpresent})." The sentence on
   Bigaj's "exhaustiveness stipulation" should stay as it is until his text is reread.

## Not proposed

- No change to the abstract. The abstract's Part I sentence stays true as written.
- No change to `CLAIM_STATUS.md`, `CURRENT_SYNTHESIS.md` or `REVIEW_QUEUE.md`. Those
  are the coordinator's ledgers, and the note has no independent review.
- No rebuild of either PDF.
