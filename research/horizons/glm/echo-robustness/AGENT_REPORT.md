# Agent report: horizons-echo-robustness

25 October 2026. Worker submission for independent review. Branch
`agent/horizons-echo-robustness`, worktree
`/Users/andrew/eternalism/.worktrees/horizons-echo-robustness`. Frozen input
used: `research/horizons/coordinator-review/dispatch-2026-10-25/main.tex`
(SHA-256 verified against SOURCE.md's `bbd59269…c84bbe`); REVIEW.md and
DRAFT3_FOLLOWUP.md used as leads only.

## Done / files

Question: for the rescaled equation $\psi_{tt}=\Delta\psi-(1+\delta)\psi$ on
the unit Einstein cylinder, for which constant $\delta$ does the antipodal
echo identity $\psi(t+\pi,-X)=-\psi(t,X)$ hold for **every** smooth solution
with arbitrary Cauchy data?

Answer derived: **iff $\delta=0$** (sharp). Exact per-degree condition:
$\omega_n^2=(n+1)^2+\delta>0$ and $\omega_n=(n+1)+2k$, equivalently the
integer lattice $\delta=4k(n+1+k)$ with $(n+1)+2k>0$ (Theorem 1). Every
$\delta\neq0$ leaves infinitely many violating degrees, with explicit
single-mode failure witnesses for named perturbations (δ=1, δ=8, δ=−8).

- `research/horizons/glm/echo-robustness/RESULT.md` — full results with
  proofs: sector condition, sharp classification, witnesses; the
  geometry-vs-field distinction (cone/singularity refocusing is
  δ-independent; the value echo is not); ESU determination
  $F(b)=M$ for every δ via slice-swallowing (echo not needed there); the
  δ-free integral (degree-0) determination that survives on the dust strip;
  the ordinary-mass-on-dust model kept separate via a lemma (solution space
  invariant under the echo map iff the potential is π-periodic;
  $1+m^2a^2$ is not); framing answer: the echo is a special conformal/spectral
  recurrence (isolated Huygens point), not a stable causal-geometric
  consequence.
- `research/horizons/glm/echo-robustness/sources.jsonl` — 16 source records,
  depths labeled honestly, validated JSONL.
- `research/horizons/glm/echo-robustness/check_modes.py` — bounded stdlib
  verification.
- `AGENT_REPORT.md` — this file (root, replacing the previous lane's
  committed report in this worktree).

## Search capability check

Task-assigned Z.ai tool `web-search-prime` returned `MCP error -429`,
code 1310 "Weekly/Monthly Limit Exhausted … reset 2026-11-17" on the first
relevant query. Unavailable for the whole task; no retry loops. Fallback:
OpenCode `websearch` plus direct fetches of public primary pages
(doi.org, EMS Press excerpt, arXiv abs/ar5iv pages) — this worked
throughout. Coverage is correspondingly narrower than a systematic search.

## Source coverage

Frozen dispatch and both reviews read full-text. External anchors:
Belger–Schimming–Wünsch 1997 survey (selected sections via publisher
excerpt — the constant-curvature Huygens-only-at-one-potential result used
to frame the echo as an isolated tail-free point); Günther 1988
(discovery only); Berest–Veselov (abstract); Yagdjian's de Sitter Huygens
paper (abstract; theorems read via his survey 1305.4404 §3, recorded as a
secondary); 2026 conformal-boundary-rigidity preprint §1 (the
"spacetime antipode" refocusing statement); Sanders 2021 (KG-on-ESU and
harmonics spectrum locators, selected sections); tails context (EPJC 2017,
abstract). Geroch 1977, Grøn–Johannesen 2011, Manchak 2008, Wald App. D:
**not read this task**; recorded at discovery depth with the dependency on
REVIEW.md's audit stated. One correction made during verification: the de
Sitter Huygens paper's author is Karen Yagdjian (J. Math. Phys. 54, 091503,
2013) — an initial misattribution was caught by fetching the arXiv page.

## Verification commands and results

- `python3 research/horizons/glm/echo-robustness/check_modes.py` —
  (i) exact integer-arithmetic scan of the sector condition over
  δ ∈ [−40, 40], n ≤ 24: only δ=0 has all sectors echoing; δ=8 → {0},
  δ=12 → {1}, δ=20 → {3}, δ=−8 → {2}, δ=−12 → {3}, δ=−4 → ∅ (zero-frequency
  exclusion), matching the lattice formula by hand; (ii) RK4 integration of
  witness modes: echo residuals ~1e-14/1e-15 where Theorem 1 predicts echo
  (δ=0 n=0,3; δ=8 n=0; δ=−8 n=2), order-1 where it predicts failure
  (δ=1 n=0: 1.4; δ=8 n=1: −0.75; δ=−8 n=0 exponential: −0.68).
- `python3 -c` JSONL validation — 16 records, all required contract fields,
  depths within the allowed enum. Passed.
- All proofs in RESULT.md are by hand (mode algebra + ODE phase-plane
  arguments + one computation lemma); the script is corroboration, not the
  proof.

## Strongest contrary evidence / what could make this wrong

- The Huygens literature (BSW survey) already isolates the conformal
  potential on constant curvature in a stronger operator form, so the δ=0
  sharpness should be viewed as a known-in-spirit phenomenon re-derived in
  mode form for this problem — not as a new mathematical discovery. No
  novelty is claimed.
- The dispatch's proposition is an inclusion $A(J^-(b))\subseteq F(b)$, not
  the identity itself. I show the identity powering its proof holds only at
  δ=0; I did **not** prove that the inclusion fails at δ≠0 for a fixed b
  (the witnesses violate the identity, not directly the inclusion). This
  gap is stated in RESULT.md §4.3 and §8.
- The BSW constant-curvature statement was read from an imperfect OCR
  excerpt; the garbled formula was reconstructed as $c=((n-1)/2)^2K$ from
  context and cross-checked against the de Sitter literature, but the
  primary (Günther's monograph) was not consulted. Flagged as an open
  verification item.

## Limitations

- Fallback search only (quota-exhausted assigned tool); no citation
  chasing forward from the anchors; no systematic novelty audit — per the
  brief, none is claimed.
- The pointwise-determination question on the dust strip at δ≠0 (does
  $F(b)=J^-(b)$ exactly?) remains open, as does the dispatch's own
  exactness question at δ=0; a localization reduction exists (support
  avoidance is compatible with every $x\notin J^-(b)$) but the final
  nonvanishing step was not proven.
- The Floquet genericity remark for the dust-mass $2\pi$ recurrence is
  explicitly labeled an unverified expectation.
- No installs, no large runs, no extra agents, no board/runner/shared-file
  edits, no push/merge.

## Proposed next tasks

1. Prove or disprove $F_{\mathcal L}(b)=J^-(b)$ on the pre-threshold dust
   strip for a named δ≠0 (e.g. δ=1), using the support-localization
   reduction plus the tail term of the retarded kernel (first-order Duhamel
   in δ looks tractable).
2. Verify the BSW constant-curvature Huygens classification against
   Günther's monograph and pin page-level locators (closes the OCR gap).
3. Dust-mass model: decide Floquet genericity of the $2\pi$-recurrence
   failure for $v(\eta)=1+m^2a(\eta)^2$, and whether any all-solutions
   affine echo exists for $m\neq0$ (task separation already documented in
   RESULT.md §6).
4. If the manuscript adopts the echo proposition, add a robustness remark:
   the mechanism is isolated at the conformal coupling (mode lattice
   condition), with the Huygens-literature citation.

## Unresolved questions

- Whether sector echoes at special δ (e.g. δ=8, degree 0) can combine with
  anything to restore any pointwise inclusion on the strip (my reading: no,
  since event values mix degrees — stated as a conjecture, not proved).
- Independent confirmation of the OCR-reconstructed BSW formula.
