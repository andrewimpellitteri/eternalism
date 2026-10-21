# Refocus selection: rank result first, CPOBC as a bounded feasibility lane

Coordinator decision, 2026-10-21, task `refocus-selection-integration`. The
original coordinator (`codex-refocus-coordinator`) stopped mid-task; its
uncommitted edits were recovered in commit `b308ee3` and reviewed here before
the claim was taken over. This is a selection of where to spend effort, not a
novelty or priority finding.

## Inputs reviewed and rerun

| Lane | Deliverable | Rerun here | Status |
|---|---|---|---|
| `refocus-rank-audit` | `rank-audit/RESULT.md`, `check_bipartite_bound.py` | exact enumeration m=1..4; counterexample `W_3=200/169 < 230/169` reproduced | conditional pass after repair |
| `refocus-cpobc-reproduction` | `cpobc-reproduction/RESULT.md`, `check.py` | exact rational controls pass | restricted 2×2 self-adjoint nonsingular obstruction reproduced; propagation lemma imported |
| `refocus-cpobc-correspondence` | `cpobc-correspondence/RESULT.md`, `CORRECTIONS.md` | source records pass `check_sources.py --strict` | open boundary located; Xu chart normalization questioned |
| inherited rank proof | `rank-renewal-convergence/check_weighted.py` | all finite exact checks pass, including new `p=(50+120i)/169` regression | corrected Lemma 1(b), 2(ii), 2(iii) |

I re-derived the corrected bipartite row sum by hand: per lower vertex, the
empty row covers the cap directly (factor `a`), nonempty rows give
`(1+a)^m-1`; the upper-to-cap covers give `a^m`. At `m=1` this is `2a^2`,
matching the exhaustive `W_3`.

## Separated assessment

| Axis | Rank-only post theorem | CPOBC remaining 2×2 case |
|---|---|---|
| Correctness | proof repaired; structural steps audited; finite checks pass; one imported framework (Dowker–Zalel posts algebra) | only a restricted self-adjoint branch reproduced; non-self-adjoint, Jordan and chart-complement cases untouched |
| Priority | nearest predecessor (Dowker–Zalel 2212.01149v2 Sec. V) leaves the question inconclusive in the sections read; targeted search only | Xu §29.11 occupies most nearby branches; companion certificates not public; priority uncertain for any narrowed branch |
| Tractability | done modulo write-up and broader priority search | Xu reports a failed exact elimination; diagonal `R_3,R_4` normalization not justified by similarity alone; no CAS installed |
| Scope | measure-extension obstruction under a literal rank-only value rule; no ontology follows | mathematical physics of quantum growth; connection to temporal ontology indirect |

## Decision

1. **Main near-term target: the rank-only post theorem.** Exact claim
   contract: under the literal all-principal rank-only rule
   `ν(D_H)=κ_n N(H) A_p(H)`, a finite countably additive complex measure on
   the posts algebra with `ν(P_∞)=1` exists iff `0<p≤1`. Next gates: (i) a
   PhilPapers/full-text priority search including Dowker–Zalel citing works
   and Surya–Zalel follow-ups, (ii) an independent read of the imported posts
   algebra proof dependencies, (iii) a short write-up that states the value
   rule as an added premise.
2. **CPOBC: feasibility allocation only.** First gate: derive or refute the
   `R_3=diag(1,x), R_4=diag(1,y)` normalization from a symmetry of the
   equations. Second gate: regenerate the stage-three residual catalog from the
   transition rules. Promote to a main target only with a reproduced baseline
   and a concrete reason our method beats Xu's failed elimination.
   Dependency installs (a CAS) need a task that names them.
3. **Preserve:** the scalar BCPH note (now with errata) and the philosophy
   manuscript `paper/main.tex` are unchanged by this decision.

## Residual questions

- Is the rank-only value rule physically motivated, or only a mathematically
  natural restriction? The theorem's interest depends on the answer.
- Does Xu's chart follow from a scaling symmetry of MSR plus CPOBC that the
  source omits?
- The published Srivastava–Surya PRD full text was not read; only its abstract.
