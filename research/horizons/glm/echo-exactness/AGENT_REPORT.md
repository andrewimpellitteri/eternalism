# AGENT_REPORT — horizons-echo-exactness

Date: 2026-10-25. Worker: OpenCode GLM (glm-5.3-flash), isolated worktree
`/Users/andrew/eternalism/.worktrees/horizons-echo-exactness`, branch
`agent/horizons-echo-exactness`. Status: **submission for review, not
accepted completion.**

## Done (files)

All outputs in `research/horizons/glm/echo-exactness/` plus this report:

* `RESULT.md` — main theorem, proofs, corollaries, verification notes,
  scope and open questions.
* `verify_echo_exactness.py` — self-contained verification (Python 3 stdlib
  only; no installs). Runs in ~2 s.
* `verify_output.txt` — captured run output (2026-10-25, this worktree).
* `sources.jsonl` — 8 records, contract-compliant (validated by script).

**Main result.** For the conformally coupled scalar on the closed dust model
$M=(0,2\pi)\times S^3$, $b=(\tau,Y)$, $0<\tau\le\pi$:

$$F_{\mathcal L}(b)=M\cap\big(\{u\le\tau\}\cup\{v\le\tau\}\cup\{v\ge2\pi-\tau\}\cup\{u\ge2\pi-\tau\}\big),\quad u=\eta+d,\ v=\eta-d.$$

Consequences: (1) the draft's conjectured fixed region
$J^-(b)\cup(A(J^-(b))\cap M)$ is **strictly smaller** — explicit counterexample
$x_W=(2\pi-\tau/2,Y)$, fixed but outside the draft's set, for every
$\tau<\pi$; (2) at the critical epoch $\tau=\pi$, $F_{\mathcal L}(b)=M$
while $\mathrm{Det}(b)=I^-_s(b)$: everything is fixed though nothing beyond
the strict past is guaranteed; (3) timelike-future events *are* fixed before
$\pi$ (e.g. $(\eta_x,Y)$, $\eta_x\in(2\pi-\tau,2\pi)$) — answering the
coordinator follow-up's question, so the draft's pre-threshold echo is not
spacelike-limited once exactness is known; (4) explicit epoch witness: the
same target $x^*=(3\pi/2,Y)$ is unfixed from $b_1=(2\pi/5,Y)$ (separating
pair constructed, realized numerically) and fixed from $b_2=(3\pi/4,Y)$,
with $\mathrm{Det}$ stationary at $I^-_s$ at both standpoints — the requested
explicit witness of epoch-dependent law-relative determination.

## Search capability check

* `web-search-prime` (MCP): **unavailable** — server responded 429
  "Weekly/Monthly Limit Exhausted … reset 2026-11-17". One query attempted,
  no retry loops.
* Fallback per brief: `websearch` tool **worked** (3 queries used) and
  `webfetch` **worked** (arxiv abstract page). Coverage is therefore narrower
  than a full lane audit: no quota-bound sweeps of recent literature.

## Source coverage (details in sources.jsonl)

* Full-text (local): frozen draft-3 main.tex (SHA per SOURCE.md),
  coordinator REVIEW.md, DRAFT3_FOLLOWUP.md.
* Abstract: Nolan arXiv:gr-qc/9703031v1 (CQG 14 (1997) 1295–1308) — Green
  function $\Sigma\delta(\Omega)+V\Theta(-\Omega)$ structure; minimal scalar
  tails in cosmology as the contrast case.
* Discovery: Carminati–McLenaghan/Wünsch Huygens-classification program
  (bibliographic only; no theorem relied on); Wald App. D and the draft's
  geometric sources (Geroch, HE, MS2008, Grøn–Johannesen, Bolotin–Tanatarov,
  Manchak) inherited with REVIEW's depths, not re-read.
* Code-audited: the in-task verification script and its captured output.

No external source's result is load-bearing for the theorem: the proof is
self-contained (mode sums, elementary spherical geometry, standard Cauchy
uniqueness on spacelike-disk developments). No `sorry`-style gaps are hidden
in code — the code is corroboration, not proof.

## Verification commands and results

```
python3 research/horizons/glm/echo-exactness/verify_echo_exactness.py
python3 - (JSONL contract validation of sources.jsonl)   -> OK, 8 records
```

Results: echo identity residual $2.7\times10^{-15}$; mode sums match exact
Poisson-data closed forms (g-part, f-part, pole value) to $\le1.1\times10^{-14}$
(this verifies the trace lemma's shell/refocusing/branch structure where a
closed form exists); end-to-end admissible bump: $|\psi|\le2.4\times10^{-3}$
on sampled constraint points vs $\psi(x_0)=+0.650$ at the annulus target and
$\psi(x_W)=4.3\times10^{-4}$ at the fixed W-point outside the draft's set;
$b_2$ control $\psi(x^*)=1.3\times10^{-3}$ vs $\psi(x')=+3.99$; region grids
as in RESULT.md §3.

## Strongest contrary evidence considered

1. **Huygens doubt (internal, resolved).** Initial numerics showed O(1)
   values where the shell missed the data support. Traced to two artifacts:
   Gaussian/Poisson mode windows are *not* spatially localized data (one-sided
   sine series carry long-range tails — the Poisson closed form then confirms
   the shell formula exactly, $12.74=5.23\times2.4$ cross-check), and narrow
   cap projections carry Gibbs lobes to ~2.5× the cap radius. With wider caps
   and margin discipline (cap radius < uniform shell clearance), contrasts
   of 50–3000× are obtained. The exact zero property for compactly supported
   data is a theorem (trace lemma), and the O(1e-3) numerics are truncation
   floor, not signal.
2. ** REVIEW's sufficient-vs-necessary objection** — honored: the new upper
   bound is proven by exhibiting separating solution pairs per annulus point,
   not by negating the geometric criterion. The draft's over-claim direction
   is avoided; indeed the true fixed set is *larger* than the draft's, so the
   draft's specific conjecture fails in the opposite direction from the
   review's countermodel pressure.
3. **Critical-epoch sanity** — at $\tau=\pi$ the four regions cover $M$ with
   two independent mechanisms (continuity onto $\overline U$; periodicity +
   disk development onto $\overline{J^+(A^{-2}b)}$-regions), so "everything
   fixed at $\pi$" does not rest on a single argument.

## Limitations

* Scope is the one law ($\mathcal L$ = smooth conformal-scalar solutions on
  this $M$), values-then-jets at $F$-points; not Belnap settledness, not
  epistemic prediction, not realistic cosmology, not other topologies.
* Numerics bounded to $n\le1500$ modes and rotation-reduced (zonal)
  configurations; "vanishing" numbers are $10^{-3}$–$10^{-4}$ floors. They
  corroborate, not prove.
* Search coverage reduced (primary MCP quota exhausted mid-task; fallback
  used). Novelty claim is correspondingly bounded: no systematic sweep for
  prior statements of the four-region formula was possible. The four-region
  result appears to be new, but that is a bounded audit statement, not a
  global priority claim.
* The proof of the upper bound (§2.4 of RESULT.md) is constructive-casework;
  a reviewer should re-derive the margin windows — they are the most
  error-prone element. The lower bound (§2.3) is short and I consider it
  robust.

## Proposed next tasks

1. Independent re-derivation/review of §2.4's margin windows and the
   reflected-branch case ($\eta_x>\pi$), ideally by a different model.
2. Extend the exact characterization to the closed radiation model
   (frequencies $\sqrt{n(n+2)}$, no periodization) — the machinery applies
   but the echo mechanism changes; this would test how much of the result is
   echo-specific.
3. Study $\bigcap_\mathcal L$ over a natural menu of local fields in the
   closed model against the now-known upper envelope.
4. Optional: Lean formalization of the trace lemma's kernel identity and the
   four-region union statement (pure geometry + Fourier on $S^3$); needs a
   task that names a build environment.
5. Manuscript integration: replace the open question after Prop echo with the
   four-region theorem; fix the abstract's "antipodal echo" wording per
   DRAFT3_FOLLOWUP; add the epoch witness as the explicit realization of
   conclusion 3 (epoch-dependent determination).

## Blockers

None outstanding. web-search-prime quota exhaustion (resets 2026-11-17) is
recorded above; it limited literature sweeps, not the mathematics.
