# Long shot: does birth order leave an interference trace under norm-only covariance?

Task `longshot-birth-order-interference`, Claude subagent, 2026-10-21. A
deliberately high-risk probe; no novelty claim. Exact Gaussian-rational
arithmetic (standard library). The subagent could not write this file; the
coordinator saved its report and re-ran the code (output byte-identical,
sha256 `a9903084…6171`).

Files: `birth_order_interference.py` (sha256 `8c4b62ca…9f1f9`), `out/results.txt`.
Reproduce: `python3 birth_order_interference.py out/results.txt`.

## Verdict: SCOPE CLARIFICATION; the "birth-order trace" reading is KILLED

1. **The invariance statement is correct in its scope.** Srivastava–Surya
   (arXiv:2603.25503v1 Sec. 3.1) say a phase "will leave the quantum measure
   invariant", where the measure is `⟨c_n|c_n⟩` of one labelled cylinder. That
   is exactly true. Path-dependent phases do change the decoherence functional
   between distinct labellings, and hence the measure of unions of labellings;
   in frozen models those unions are genuinely covariant events. Example (model
   PA, complex percolation at p = (1+i)/2 with a transition-covariant reflection
   twist): every labelled `|ψ|²` at stages 1–4 is unchanged, yet the covariant
   atom `cp⊕ω` has measure **37/40** instead of **9/8**. The mechanism
   (labelled amplitudes summed inside an unlabelled event) is already in Gudder
   2014 (arXiv:1403.7839v1, Sec. 5).
2. **What removes the phases.** Not the Markov sum rule, strong positivity,
   transition-level covariance or stage-3 Bell causality. They vanish only if:
   the phase must itself be relabelling-invariant (that is GC; tautological);
   transition moduli are stochastic at every node (Lemma S: `Σ|t_j| = 1` forces
   nonnegative reals); or GC is imposed on the decoherence functional, as
   Rideout states it (gr-qc/0212064v1 Sec. 4.2: "D(A,B) is invariant under
   relabeling of its arguments").
3. **No observable trace of birth order.** In every generic computed case
   (stages 3–4), an ordinary GC model with different amplitudes reproduces the
   phased model's covariant vector measure exactly (Lemma R). Covariant data
   then cannot reveal that the law weights birth orders with different phases.
   Two residues remain, neither a trace of birth order:
   - **R1 (Bell-causal frozen models).** Every frozen GC + Bell-causal model
     obeys `v(cp)² = 9 v(V) v(anti3)`; nonzero holonomy violates it. Classical
     Bell-causal non-DGC models are detected the same way, so this is model-class
     selection, not quantum birth-order interference.
   - **R2 (quantum-only boundary).** Destructive interference can force any GC
     reproduction to have a zero ancestor with nonzero descendants, which Markov
     growth forbids. Such targets are exact limits of GC-reproducible ones with
     amplitudes diverging like 1/ε; Rideout (thesis p. 112) anticipated this
     ("It is likely that this problem can be overcome using limits").
4. **Becoming.** Neither residue reaches objective becoming without bridge
   premises B1–B5 below.

## Definitions

- Growth adds one element per stage with past a down-set; all causets are
  naturally labelled. Stages 1–4: 1, 2, 7, 40 labelled causets; 1, 2, 5, 16
  classes.
- Vector measure: `ψ(c_n)` is the product of transition amplitudes; Markov sum
  rule (MSR) `Σ_children t = 1`.
- Decoherence functional in the paper's convention `D(α,β) = A*(α)A(β)`
  (conjugate-linear in the first slot); `μ(α) = D(α,α)`.
- GC: `ψ(c) = ψ(c′)` for isomorphic labelled causets. Norm-only GC:
  `|ψ(c)| = |ψ(c′)|`. Holonomy `w_j/w_1` = phase of `D(cyl c_1, cyl c_j)`.
- Events: stage-n class events and stage-n stem events are stage-dependent (not
  covariant; Surya–Zalel Sec. 2). **Frozen models**: from stage N every new
  element is born above everything; the infinite causet is `C_N⊕ω`, so
  `{C ≅ C_N⊕ω}` is a genuinely covariant event with vector measure `v(C) =
  Σ_j ψ(c_j^C)`.

## Models (MSR verified at every labelled node)

GC0 (complex percolation, p = (1+i)/2); PA (GC0 plus a transition-covariant
reflection twist at the 2-antichain node); PA4 (PA plus a stage-4 twist); PB (a
label-dependent twist, breaking transition covariance and BC); BCPH (Bell-causal
norm-only stage-3 model, x = 1/2, α₁ = 1/4, β₀ = α₁u, u = (3+4i)/5) and BCGC
(u = 1); OBS and OBSC (obstruction examples). For PA, PA4 and PB, `|ψ(c)|²`
equals GC0's for every labelled causet at stages 1–4.

## Key computations (exact)

| model | stage-3 class cp: labelled ψ | holonomies | v(cp) | μ(cp) |
|---|---|---|---|---|
| GC0 | (1−i)/4 ×3 | 1, 1, 1 | (3−3i)/4 | 9/8 |
| PA | (7+i)/20, (7+i)/20, (1−i)/4 | 1, 1, (3−4i)/5 | (19−3i)/20 | 37/40 |
| PB | −(1+i)/4, (1−i)/4, (1−i)/4 | 1, i, i | (1−3i)/4 | 5/8 |

PA frozen at 3: μ(cp ∪ V) = 29/20 (GC0: 5/4). Stage 4: C4.07 (W = 5) μ = 1/64
in PA vs 25/64 in GC0. Bell-causal family: `μ(cp) = x²|α₁|²(5 + 4cos θ)` vs the
GC value `9x²|α₁|²`, verified for seven unit phases.

**Lemma R reconstructions:** PA, PB, PA4 (16 atoms) each have an exact GC
reproduction. BCPH has a unique GC reproduction, which is not Bell-causal. OBS
and OBSC are obstructed (the chain2 ancestor is 0 with descendants −1/10, 1/5,
−1/10), but shifting by ε = 1/10, 1/100, 1/1000 gives reproducible targets with
chain2→cp amplitudes −1, −10, −100.

Additional lemma (e): total variation on the cylinder algebra is
`sup_n Σ|ψ(c_n)|`, which depends only on moduli, so phases can neither cause nor
cure non-extension.

## Srivastava–Surya, verbatim (arXiv:2603.25503v1)

- Sec. 3.1: "This implies that the inner product or quantum measure
  ⟨c_n|c_n⟩=⟨c_n′|c_n′⟩."
- Sec. 3.1 Note: "It is also possible to introduce a phase
  |c_n⟩=e^{iΦ(c_n,c_n′)}|c_n′⟩ since this will leave the quantum measure invariant.
  Because of the ensuing ambiguities, or generation of new parameters this will
  result in, we do not consider this option henceforth."
- Sec. 4: "one could stipulate that it isn’t the quantum vector measure that
  should be the same when implementing GC, but rather only its norm. Thus, one
  could introduce a path dependent phase into the definition. ... While we have
  explored these options, apart from trivial choices, the ensuing dynamics
  becomes rapidly more complex."

No contradiction: the Note concerns single cylinders; its "new parameters" turn
out to be physical at the level of D (37/40 vs 9/8).

## Bridge premises needed before any bearing on becoming

B1 labels/stages are a physical order of coming-into-being, not gauge; B2 the
amplitude assignment is ontic, not one of a class of covariantly equivalent laws;
B3 the model class (Bell causality, Markov growth with finite amplitudes) is a
law of nature; B4 interference between labellings is interference between real
alternative birth orders; B5 even granting B1–B4, a label-dependent measure on
completed causets is compatible with a block reading (Rideout treats the completed
causal set as the history).

## Nearest predecessors

Srivastava–Surya 2603.25503v1 (full-text, sections above); Gudder 1403.7839v1
Sec. 5 (full-text; same mechanism, unlabelled paths not covariant events);
Rideout gr-qc/0212064v1 Sec. 4.2 (full-text; GC as D-invariance; anticipates R2);
Surya–Zalel 2003.11311, Dowker–Johnston–Surya 1007.2725, covtree 1910.07292,
Brightwell–Luczak 0901.0240 (via `knowledge/csg-quantum/`, not re-read).

## Defeat search (bounded, 2026-10-21)

Web and INSPIRE (`refersto:recid:3136377` → one citer, Xu 2607.26672v1, not a
defeater; `refersto:recid:1287914` → none). No paper found computing norm-only-GC
phases on covariant events, stating Lemma R, or stating the stage-3 BC identity.
Google Scholar, Semantic Scholar and Henson's papers not checked.

## Limits and open questions

Scalar amplitudes only; stages ≤ 4; covariant events only in frozen models; BC at
stage 3 only; Lemma R only against frozen and eventually-percolation competitors.
Open: (1) does BC at stage ≥ 4 plus norm-only GC force zero holonomy (would kill
R1)? (2) do general infinite GC models reproduce R2 targets? (3) is there a
quantum covtree analogue of Lemma 4.9?
