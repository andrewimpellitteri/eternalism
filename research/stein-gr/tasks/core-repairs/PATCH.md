# PATCH.md — chronology conventions and first-exit cases: verified, no replacement passages required

Task: `stein-core-repairs`. Date of check: 2026-10-25.

## Pinned source

- File: `research/stein-gr/main.tex` (900 lines)
- SHA-256: `7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886`
- Git: branch `agent/stein-core-repairs`, HEAD `0c6d2c5`; last change to `main.tex`
  in commit `f8caaa6` ("Apply second review's repairs: strict chronology in
  topological steps, complete Lemma D case split", 2026-10-25, diff
  `main.tex 49 lines changed, 31 insertions(+), 18 deletions(-)`; the companion
  `stein-gr.pdf` was rebuilt in the same commit).
- Re-hashed at end of run: unchanged (same SHA-256).

## Verdict

**Both findings of `SECOND_PASS_REVIEW.md` are already repaired in the pinned
source.** Per the brief ("if the author already fixed a finding, verify and
mark it resolved rather than proposing an obsolete patch"), this document
records the verification and does **not** propose replacements for repaired
passages. Three optional, non-blocking presentational refinements are offered
in §6 with exact TeX, for the author to take or leave.

| Finding (SECOND_PASS_REVIEW §) | Status in pinned source | Evidence |
|---|---|---|
| 1. Strict vs reflexive I conventions | **RESOLVED** | §2 below; checklist §4 |
| 2. Lemma D(ii) simultaneous t=0/shell crossing, both directions, p on initial slab | **RESOLVED** | §3 below; checklist §5 |

## 1. What commit `f8caaa6` changed

Verified by `git show f8caaa6 -- main.tex`. Exactly five hunks, all in
`research/stein-gr/main.tex`:

1. Framework paragraph (now ll. 137–145): defines strict sets `I^±_s`, states
   `I^± = I^±_s ∪ Δ`, the coincidence `x ∈ I^±_s(y) ⟺ x ≪ y` in causal
   spacetimes, and declares "MS's `I^±` are our strict sets".
2. Imported topological facts (now ll. 324–330): all stated with `I^±_s`.
3. Proof of Proposition `prop:reg` (now ll. 358–364): closure chain via
   `Ichr_s`; `Int Jm = Ichr_s`; diagonal added back; `(CB)` closes equality.
4. Proof of Lemma `lem:D`(ii) (now ll. 528–545): stopping times `τ_0`, `τ_exit`
   with `τ_0 ≤ τ_exit` **equality included**; pullback legitimacy near the
   closed tube; `p ∈ Σ` handled before the stopping times; reverse direction
   re-run with roles exchanged and no global coordinate `t` on `M`.
5. Proof of Lemma `lem:D`(iii) (now ll. 556–559): open diamond written with
   strict sets `Ifut_s(p^-) ∩ Ichr_s(q^+)`.

No definition, theorem, proposition, corollary or lemma *statement* was
modified (see §7).

## 2. Verification of Finding 1 (strict vs reflexive)

The defect class was: topological facts (openness of `I^±`, `Int J^± = I^±`,
closures) are true of the **strict** relation, while the manuscript's `I^±`
are reflexive; a reflexive chronological interval contains its vertex, so
`Int J^- = I^-` and "the diamond is open" are false under the reflexive
reading. Checked in the pinned source:

- **Framework (ll. 139–145).** `I^±, J^±` reflexive (CH 1995, p. 360);
  `x ≪ y` means `x ∈ I^±(y)`, `x ≠ y`; `I^±_s` defined by timelike curves;
  `I^± = I^±_s ∪ Δ`; `x ∈ I^±_s(y) ⟺ x ≪ y` *in causal spacetimes*. The
  identification is legitimate where used: every spacetime the topological
  facts are applied to (`M`, `N`, `M'`, `Mink`) is globally hyperbolic, hence
  causal, so reflexive-minus-diagonal equals strict. MS's own `I^±` are
  declared to be the strict sets. Consistent.
- **Imports (ll. 324–330).** Now: "`Ifut_s` is open in `M×M` (MS Prop. 2.16);
  `overline{Jp} = overline{Ifut_s}` and `Int Jp = Ifut_s` (MS Prop. 2.17), and
  likewise for the pasts"; push-up and horismos composition (MS Prop. 2.31);
  deformation (MS Thm. 2.30). All four verified verbatim against the primary
  source (below). No causality hypothesis is needed for Props. 2.16–2.17;
  they hold in every spacetime.
- **Regularity proof (ll. 358–364).** Closed case: `B ⊇ overline{I^-} =
  overline{I^-_s} = overline{J^-} ⊇ J^-` — the second equality is trivial
  (`Δ` closed and `Δ ⊆ overline{I^-_s}`), the third holds because `M` is
  globally hyperbolic (hence causally simple: MS states `overline{I^+} =
  overline{J^+} = J^+` at the causally simple level, §2.4 after Prop. 2.17;
  `J^±` closed by MS Prop. 3.68/3.71 as cited at l. 434). Open case:
  `B\Δ` open and `⊆ J^-` gives `B\Δ ⊆ Int J^- = I^-_s`, hence
  `B ⊆ I^-_s ∪ Δ = I^-`, and `(CB)` gives equality. Exactly the prescribed
  repair; the diagonal is added back explicitly.
- **Open diamond, Lemma D(iii) (ll. 556–559).** Now
  `J(p,q) ⊆ Ifut_s(p^-) ∩ Ichr_s(q^+) ⊆ D(Σ)`, "an open set (MS Props. 2.16,
  2.31)". Correct: `p^- ≪ p ≤ r ≤ q ≪ q^+` pushes up to `r ∈ I^+_s(p^-) ∩
  I^-_s(q^+)` by MS 2.31(i); the *strict* diamond is open (MS 2.16, sections
  of an open subset of `M×M`); containment in `D(Σ)` is causal convexity of
  `D(Σ)` with `p^-, q^+ ∈ int D`. Under the old reflexive reading the diamond
  would contain `p^-, q^+` as interior vertices and need not be open — the
  repair removes exactly that failure.
- **No residual occurrence of the defect.** Grep of every `Ichr/Ifut/≪/gg/E^-`
  occurrence (checklist §4): no site any longer concludes openness, interior,
  or a topological fact from the reflexive sets. Remaining reflexive uses are
  membership/(CB)/statement-level, where reflexivity is intended.

**Primary source verification** (my own, this run; read depth: full text of
the cited items, not a whole-paper audit):

Minguzzi, E. & Sánchez, M., *The causal hierarchy of spacetimes*,
arXiv:gr-qc/0609119 **v3** (24 Apr 2008), HTML rendition
https://arxiv.org/html/gr-qc/0609119v3 . The v3 comments field states it
"matches the one to be published at the proceedings", i.e. the ESI volume
cited in the manuscript as MS2008 (ESI Lect. Math. Phys., EMS, 2008,
pp. 299–358), so v3 numbering is the appropriate locator set for the book
citation. Checked, with exact wording:

- §2.3 (conventions): `p ≪ q` by future-directed **timelike** curve;
  `p ≤ q` by causal or constant curve (reflexive); `p → q` horismos;
  `E^± = J^± \ I^±`. Hence MS `J^±` = manuscript `J^±`, MS `I^±` =
  manuscript `I^±_s`, and MS `E^- = J^- \ I^-_s` = manuscript
  `J^- \ I^-` because `Δ ⊆ J^-`. The horismos definition at l. 292 is
  therefore convention-invariant.
- Prop. 2.16: "The set `I^+` is open in `M×M`." — matches l. 324.
- Prop. 2.17: "`J̄^+ = Ī^+`, `Int J^+ = I^+`, `J̇^+ = İ^+`." (any spacetime) —
  matches l. 325–326 ("and likewise for the pasts" covers the past variant;
  MS states the ± symmetry explicitly).
- Prop. 2.31 preamble and (i)–(ii): horismos ⟺ maximizing lightlike
  geodesic; `p ≪ r ≤ q ⟹ p ≪ q` (and mirrored); `r ∈ E^+(p), q ∈ E^+(r)
  ⟹ q ∈ E^+(p)` or `p ≪ q` — matches ll. 326–328 and the use at l. 407.
- Thm. 2.30(i)–(ii): causal curve not a maximizing lightlike curve ⟹ timelike
  deformation; maximizing lightlike ⟹ lightlike geodesic without conjugate
  points — matches l. 328–330 and the Theorem `thm:weyl` use.
- Bonus corroboration for the regularity closure chain: MS §2.4 (after Prop.
  2.17's discussion, K-relation remark) states that in causally simple
  spacetimes `Ī^+ = J̄^+ = J^+` — the exact level at which the proof uses it.

CH 1995 p. 360 (reflexive `I^-, J^-` convention) was **not** read directly by
me (paywalled); it is relied on as verified by `REVIEW_OTHER_RESULTS.md`
("CH p.360 reflexive convention … all verified"), and the bibliographic
identity of CH 1995 (Synthese 103, 355–387, doi:10.1007/BF01089733) was
confirmed via web search this run.

## 3. Verification of Finding 2 (Lemma D first-exit cases)

Checked by hand against the pinned source, ll. 505–569. The case analysis now
runs as follows and every first-event configuration is covered:

**Escape-path paragraph (ll. 506–517).** For `q ∈ ∂T_{2r}` with
`0 < t(q) ≤ 2r`: if `(s_q, y_q) ∉ B_0`, the vertical segment to `t=0` ends
outside `Σ'`; otherwise the point is on the lid `t=2r` (the other faces of
`∂T_{2r}` force `(s_q,y_q) ∉ B_0`), and the path with velocity
`(dt,dy) = (−1, (μ/2)ŷ)` for time `2r` ends at `|y| ∈ (r/2, 3r)` since
`μ > 1/2` and `μ < 5/2` … specifically `r/2 + μr < 3r`, so outside `Σ'` and
inside `T_{3r}`. Both paths have coordinate speed `< μ`, hence timelike for
`Φ^*g` and for `g'` (both within `ε` of `η_1` on `T_{3r}` since `6Kr ≤ ε`),
and end on `{t=0}\Σ' = S\Σ` (Φ injective). Time-reversed paths serve
`t(q) < 0`. Arithmetic re-checked: endpoints, containment, speeds — correct.

**(i) (ll. 518–526).** `p ∈ D^+_M(Σ)`, `p ∉ Φ(T_{2r})`; first `Σ`-meeting
`σ_1`; last boundary point `q` before it. `t(q) > 0` because `t` strictly
increases along future causal curves in the tube and `t(σ_1) = 0` (a `t(q)=0`
configuration is excluded automatically by the same monotonicity: a causal
segment of `S` would be constant). Segment `p→q` misses `Σ` (σ_1 is the
*first* meeting), escape path ends on `S\Σ`, and any past-inextendible
continuation meets the Cauchy surface `S` only at its start, hence misses
`Σ ⊆ S` — contradiction. Same argument in `M'`, where `{t=0}` is Cauchy.
No simultaneous case is *needed* here: the hypothesis "meets `Σ`" fixes the
terminal event inside the tube.

**(ii), forward `ψ(D^+_M(Σ)) ⊆ D^+_{M'}(Σ')` (ll. 528–541).**
- `p ∈ Σ` (i.e. `ψ(p) ∈ Σ'`): disposed of *before* the stopping times are
  defined — the reviewer's prescription, implemented verbatim.
- Otherwise `t(ψ(p)) ∈ (0, 2r)`: `< 2r` by (i) (`p ∈ Φ(T_{2r})`), `> 0`
  because a point of `D^+_M(Σ)\Σ` with `t < 0` would lie in `I^-(S)` by
  Lemma B, and acausality of `S` excludes `J^-(Σ)` meeting `I^-(S)` off `Σ`.
  (The manuscript leaves this one-liner implicit; see §6, refinement R1.)
- `τ_0` (first `t=0`) and `τ_exit` (first `∂T_{2r}`) both exist: `t` is
  strictly monotone along `g'`-causal curves and `t → −∞` along
  past-inextendible ones (established in the constants paragraph, ll. 485–488).
- Pullback legitimate "up to either time": interior points of the segment lie
  in `T_{2r}` where `g' = Φ^*g`; the endpoint lies on `overline{T_{2r}}` where
  `χ = 1` still gives the agreement, and `Φ` is a diffeomorphism on
  `T_{ρ0} ⊇ overline{T_{2r}}`.
- **`τ_0 ≤ τ_exit`, equality included:** the simultaneous t=0-on-the-shell
  crossing is handled by the `t=0` pullback branch (the chart agreement holds
  at the shared endpoint). Were `γ'(τ_0) ∉ Σ'`, the pulled-back segment ends
  on `S\Σ` and, continued past `S` (possible in `M`; meets `S` only there),
  is a past-inextendible `M`-curve from `p` missing `Σ` — contradiction. So
  `γ'(τ_0) ∈ Σ'`.
- **`τ_exit < τ_0`:** `t > 0` at the exit point, so the escape-path
  hypotheses hold; pulled-back segment + escape path + continuation again
  misses `Σ` — contradiction.
- This is exactly the missing case of the second review, now closed in both
  sub-branches.

**(ii), reverse `D^+_{M'}(Σ') ⊆ ψ(D^+_M(Σ))` (ll. 541–545).** Roles exchanged;
no global coordinate `t` on `M` asserted (the reviewer's second prescription,
implemented): every past-inextendible `M`-curve from a point of `Φ(T_{2r})`
meets the Cauchy surface `S`, and the dichotomy is
(a) reaches `S` before leaving the tube — the `S`-point lies in
`Φ(T_{2r}) ∩ S`; if it is in `Σ` we are done, otherwise transfer the segment
to `M'` and continue below `t=0`: past-inextendible `g'`-curve from `q`
missing `Σ'`, contradicting `q ∈ D^+_{M'}(Σ')`; a curve reaching `S` exactly
as it exits the tube falls in this case, so **simultaneity is covered here
too**;
(b) leaves `Φ(T_{2r})` first, at `q_1` with `t(q_1) ∈ (0, 2r]` (if it met
`S` earlier, case (a) applies; `t` strictly monotone inside the tube):
prefix (misses `Σ`), escape path (timelike for `Φ^*g` *and* for `g'`, so it
also reads as a `g'`-curve in `M'`), continuation below `t=0` in `M'` — a
past-inextendible `g'`-curve from `q` meeting `{t=0}` only at `S\Σ'` —
contradiction. I verified this assembly explicitly; the manuscript's "the
same two cases apply" compresses it but the mechanism is present and sound.
`D^−` time-reversed: tube, both metrics, and escape paths are symmetric
under `t ↦ −t`.

**(iii) (ll. 547–568).** Causal convexity of `D(Σ)` via
`J^-(q) ∩ J^+(Σ) ⊆ D^+(Σ)` with the acausality argument (re-checked:
`σ ≤ r ≤ z`, `σ, z ∈ Σ` ⟹ `σ = z = r`); openness of interior diamonds via
strict sets (Finding 1); `M'` connectedness via the cone inclusions
`D_{η_λ}(Σ') ⊆ D_{g'}(Σ') ⊆ D_{η_μ}(Σ')` — I re-derived both inclusions from
Lemma C (every `g'`-causal vector has `|u| < λ`, so `g'`-curves are
`η_λ`-curves, giving the first; `|u| ≤ μ ⟹ g'-timelike`, so `η_μ`-curves are
`g'`-curves, giving the second; narrower cones ⟹ larger domain of dependence,
as stated) — and the containment `I^-(q^+) ∩ I^+(z^-) ⊆ N'` at l. 567, which
holds because `z^-, q^+ ∈ relint Σ' ⊆ int D'` and `D'` is causally convex,
with interior points having strict-diamond neighborhoods (the same mechanism
as the openness step). Reflexive sets are harmless there: only membership is
asserted, no topology is drawn from them.

## 4. Occurrence-by-occurrence checklist — strict/reflexive conventions

Every occurrence of `Ichr/Ifut/≪/gg/E^-` in the pinned `main.tex` (grep
verified; line numbers of the pinned file). Status: **ok** under the repaired
convention.

| Lines | Site | Reading used | Assessment |
|---|---|---|---|
| 18–19 | macros `I^+, I^-` | — | neutral |
| 71, 105, 112 | intro prose | names only | neutral |
| 139–145 | framework: reflexive `I^±,J^±`; `≪` = minus diagonal; `I^±_s` strict; `I = I_s ∪ Δ`; MS `I^±` = strict | both, declared | **ok, repaired** |
| 163 | (CB) `I^-_M ⊆ B_M` | reflexive | ok (CH convention) |
| 191–192 | Prop. single statement | reflexive | ok |
| 196–201 | Prop. single proof | reflexive (e.g. `(x,b) ∈ J^-(x)×J^+(b)` needs `x ∈ J^-(x)`) | ok; reflexivity is used and available |
| 221–223 | Prop. nonlocal proof, `x ≪ b ⟹ τ(b) > τ(x)`; `x=b` trivial | strict for `≪`, reflexive for (CB) | ok |
| 224 | Milne wedge `I^+_Mink(0)` | set, either reading | neutral |
| 235 | Thm. flat trichotomy | reflexive `I^-` | ok, unchanged |
| 256–257 | Thm. main conclusion | reflexive | ok, unchanged |
| 275 | worldline becoming `I^-(b)∩λ ⊆ B` | reflexive (needs `b ∈ B`) | ok; used at l. 367 |
| 292 | `E^- = J^- \ I^-` | reflexive `I^-`; equals MS `E^-` since `Δ ⊆ J^-` | ok, convention-invariant |
| 295–301 | Thm. class statement | reflexive | ok, unchanged |
| 305–312 | Thm. weyl statement | reflexive | ok, unchanged |
| 317 | Prop. reg statement | reflexive + `Δ` | ok, unchanged |
| 324–330 | imported facts | **strict** throughout | **ok, repaired**; matches MS 2.16/2.17/2.31/2.30 verbatim |
| 333–339 | Thm. class proof | reflexive `B = I^- ∪ N`; MS 2.31 for compositions (diagonal trivial) | ok |
| 343–356 | Thm. weyl proof | `E^-`, MS Thm 2.30 | ok |
| 358–364 | Prop. reg proof | **strict** closures and interior; `Δ` added back | **ok, repaired** |
| 366–377 | Cor. worldline proof | `a ≪ b` strict; reflexive membership via (CB) | ok |
| 388 | Lemma R statement `e ≪ x` | strict (true in causal `M`; application needs only reflexive membership) | ok |
| 391–408 | Lemma R proof | `q_ε ≪ b_1` via `σ < 0` (genuinely strict); MS 2.31(i) | ok |
| 413–431 | Lemma E + example | closedness of `J^±` (causal simplicity) | ok, no chronology |
| 433–440 | Set-up | `J^+` closed | ok |
| 442–461 | Lemma B; `I^±(S)` at ll. 450–451 | membership at `t ≠ 0` | ok, convention-neutral |
| 463–491 | Lemma C, constants | metric cone control; MS Thm 3.75 | ok, no chronology symbols |
| 493–503 | Lemma D statement | domains of dependence only | ok |
| 505–517 | escape paths | coordinate speeds | ok |
| 518–526 | Lemma D(i) | causal curves, `t`-monotonicity | ok |
| 528–545 | Lemma D(ii) | stopping times; strict/first-event logic | **ok, repaired** (see §3) |
| 547–555 | Lemma D(iii) convexity | `≤` and acausality | ok |
| 556–559 | Lemma D(iii) openness | **strict** diamond `Ifut_s ∩ Ichr_s` | **ok, repaired** |
| 560–568 | `M'` connectedness; l. 567 `I^-(q^+) ∩ I^+(z^-) ⊆ N'` | membership only (reflexive harmless); topology from preceding strict argument | ok |
| 571–575 | transfer (eq:transfer) | (LC) only | ok |
| 577–603 | Lemma F + proof | `η`-causal curves, Cauchy hyperplane | ok, no chronology symbols |
| 605–623 | Thm. main proof; l. 612 `w ≪' ψ(x)` | strict `≪'` (prime = `g'`-chronology, understood); used via (CB) | ok; `≪'` undefined at first use (see §6 R3) |
| 625–646 | causet section | order `≤` (reflexive) | ok |
| 668–680 | Prop. godel; l. 670 `p ≪ p`; l. 675 `I^±(p) = M` | `≪` strict (correct for totally vicious); `I^±` reflexive (also true strictly) | ok, neutral |
| 700–753 | energy section; l. 739 `w ≪ x`, `v ≫ b` | strict, informal | ok |
| 754–801 | philosophy section; l. 777 | prose | neutral |

**Count:** 5 sites require the strict reading (324–330, 358–364, 556–559, plus
the genuinely-strict `≪` claims at 388/405/407 and 612) — all now carry `_s`
or are correct strict claims; every other site is reflexive-intended or
neutral. **No unresolved occurrence.**

## 5. Occurrence-by-occurrence checklist — first-event cases in Lemma D

| Configuration | Where covered | Status |
|---|---|---|
| (i) first exit `q` with `t(q) > 0`, any face of `∂T_{2r}` | ll. 518–526 + escape paths (vertical / lid) | ok |
| (i) hypothetical `t(q) = 0` exit | excluded by `t`-monotonicity + spacelike `S` (segment of `S` constant) | ok (automatic) |
| (ii) fwd `p ∈ Σ` (on the initial slab) | l. 529–530, disposed before stopping times | ok, repaired |
| (ii) fwd `τ_0 < τ_exit` (reaches `t=0` inside tube first) | ll. 535–538 | ok, repaired |
| (ii) fwd `τ_0 = τ_exit` (**simultaneous t=0 and shell crossing**) | l. 535 "equality included" — handled by the `t=0` pullback branch; pullback valid at the shared endpoint | ok, repaired |
| (ii) fwd `τ_exit < τ_0` (shell first, `t > 0` at exit) | ll. 538–540 + escape paths | ok, repaired |
| (ii) rev `q ∈ Σ'` | symmetric, immediate | ok |
| (ii) rev reaches `S` before exit (incl. reaching `S` exactly at exit) | ll. 541–545, dichotomy via Cauchy `S`; transfer + continue below `t=0` | ok, repaired |
| (ii) rev exits first (`t(q_1) > 0`) | ll. 541–545; prefix + escape path (timelike for both metrics) + `M'`-continuation | ok, repaired (assembly verified in §3) |
| (ii) pullback legitimacy up to stopping times | l. 532–534 (`g' = Φ^*g` near `overline{T_{2r}}` via `χ = 1`) | ok |
| `D^−` both directions | "time-reversed" (setup symmetric under `t ↦ −t`) | ok |
| Lemma F re-runs the mechanism in `(M', Mink)` | ll. 596–602, by reference to Lemma D | ok |

**Every strict/reflexive use and every simultaneous first-event case is
accounted for.**

## 6. Optional, non-blocking refinements (presentational only)

None of these is required for correctness; they close gaps of explicitness.
Exact replacement TeX against the pinned source:

**R1 (Lemma D(ii), justify `t(ψ(p)) > 0`.)** Replace, at ll. 529–530:

```latex
$\gamma'$ be a past-inextendible $g'$-causal curve from $\psi(p)$. If
$\psi(p)\in\Sigma'$ there is nothing to prove; otherwise $t(\psi(p))>0$. Along
```

with:

```latex
$\gamma'$ be a past-inextendible $g'$-causal curve from $\psi(p)$. If
$\psi(p)\in\Sigma'$ there is nothing to prove; otherwise $t(\psi(p))>0$,
since by Lemma~\ref{lem:B} a point with $t<0$ lies in $\Ichr(S)$, which
acausality of $S$ excludes for $D^+_M(\Sigma)\setminus\Sigma\subseteq
\Jm(\Sigma)$. Along
```

**R2 (Lemma D(iii), attach "open set" unambiguously.)** Replace, at
ll. 556–559:

```latex
$J(p,q)\subseteq\Ifut_{\mathrm s}(p^-)\cap\Ichr_{\mathrm s}(q^+)\subseteq
D(\Sigma)$, an open set (MS Props.~2.16, 2.31), so $N$ is causally convex, its causal diamonds are the
```

with:

```latex
$J(p,q)\subseteq\Ifut_{\mathrm s}(p^-)\cap\Ichr_{\mathrm s}(q^+)\subseteq
D(\Sigma)$, where the strict diamond is open (MS Props.~2.16, 2.31), so
every causal curve between $p$ and $q$ lies in $N$; $N$ is causally convex,
its causal diamonds are the
```

(This also removes the accidental overfull line introduced by the repair
commit's wrapping.)

**R3 (define `≪'` at first use).** At l. 612 the prime notation
(`w ≪' ψ(x)`) is used without definition. Either add to the framework
paragraph (l. 143, after "in causal spacetimes"): "for a metric `g'` we write
`≪'` for the corresponding strict relation", or replace the two occurrences
(ll. 612, 620) by prose ("are `g'`-chronologically related").

## 7. Why the theorem statements are unchanged

Commit `f8caaa6` modified only the framework paragraph, the imported-facts
paragraph, and three proofs (`prop:reg`, `lem:D`(ii), `lem:D`(iii)). The
statements of Theorems `thm:flat`, `thm:main`, `thm:class`, `thm:weyl`,
Propositions `prop:single`, `prop:nonlocal`, `prop:reg`, `prop:causets`,
`prop:godel`, `prop:dec`, Corollaries `cor:nopresent`, `cor:worldline`, and
Lemmas `lem:R`, `lem:E`, `lem:B`, `lem:C`, `lem:D`, `lem:F` are byte-identical
to the pre-repair source. The strict sets are *derived* notation
(`I^±_s = I^± \ Δ` in causal spacetimes, and every spacetime in scope is
causal): no statement quantifies over them, and the reflexive convention
together with (CB) — the CH-faithful reading — is preserved. Hence the
trichotomy, the sandwich `I^- ⊆ B ⊆ J^-`, the classification, non-uniqueness,
regularity dichotomy, and the corollaries are statement-identical before and
after the repair. **No genuine statement change exists or is needed.**

## 8. Source repairs vs. new mathematical assumptions

- The repairs are (a) a definitional clarification (strict sets as derived
  notation; declaration of MS's convention), (b) restatement of imported
  facts with the correct locators, and (c) completion of a geometric case
  split (simultaneous first event; reverse-inclusion dichotomy via the Cauchy
  surface).
- **No new mathematical assumption is introduced.** MS Props. 2.16–2.17 hold
  in every spacetime; the causally-simplicity-level closure identity is
  available in GH, which is where it is used; the simultaneous case is a
  possibility of the geometry that the old text failed to enumerate, not an
  added hypothesis; the reverse inclusion uses only that `S` is a Cauchy
  surface of `M`, already assumed.

## 9. Verification log (commands and results)

```text
shasum -a 256 main.tex
  -> 7ccc1d37b521e4a25af54c28ffc067066243bd190da79125d922037c90345886  (before and after run)
git show f8caaa6 -- main.tex
  -> 5 hunks, exactly the reviewed repairs; no statement hunks
grep -n 'Ichr\|Ifut\|\\ll\|\\gg\|horismos\|E\^-' main.tex
  -> 80 lines; classified in §4
webfetch https://arxiv.org/abs/gr-qc/0609119
  -> v3, 24 Apr 2008; comments: matches the ESI proceedings version (pp. 299–358)
webfetch https://arxiv.org/html/gr-qc/0609119v3
  -> §2.3 conventions, Prop. 2.16, Prop. 2.17, Thm. 2.30(i)–(ii),
     Prop. 2.31 preamble+(i)+(ii) all read and matched to the manuscript
pdflatex -interaction=nonstopmode -halt-on-error main.tex   (twice, on a copy
  in /private/tmp/opencode/stein-build; source untouched)
  -> exit 0 both passes; "Output written on main.pdf (13 pages)";
     undefined references: 0
```
