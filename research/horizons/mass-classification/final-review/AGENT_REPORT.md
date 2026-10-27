# Agent report: fresh mass-classification audit

## Files changed

- `research/horizons/mass-classification/final-review/REVIEW.md` — independent adversarial reconstruction and verdict.
- `research/horizons/mass-classification/final-review/AGENT_REPORT.md` — this report.

No other files were changed. No board or task state was touched, and no commit, push, additional agent, install, or long numerical run was made.

## Evidence and verdict

**Verdict: survive**, within the candidate theorem's fixed-background smooth classical scope. The proof reviewed is pinned at SHA-256 `8142be49585e770d58f871a6c203a8ca7d6da78150dc62151199a35df6409273`. The current `RESULT.md` hash is `b89b8a0510fe58e9500485c1eba65cc749fb22fdec011e25e8cd2f48cdf337ed`. Subsequent bounded additions are the massless-versus-massive comparison, explicit restatement of the already-used one-image kernel factor in (6a), and a historical dependency paragraph pointing to completed reviews. No theorem or proof step changed.

I independently rebuilt the reduction from exact fixing to joint support of the velocity and displacement Cauchy kernels. I checked the normally convergent characteristic Volterra construction, the periodization/projection factors including the line zero-mode and (S^3) constant mode, the source-endpoint matrix identity and backward PDE, connectedness and analyticity of the open image cells, both nonzero-cell limits, and the cap/exterior test-data logic. The strongest attempted falsifier was a factor/sign or wrong-source-equation defect; I found none. The direct-cell value is (-V(t)/(8\pi)); the double-image corner value is (J/(2\pi)>0). These exclude an open joint-support hole in each connected cell, without asserting pointwise positivity elsewhere.

After forming the verdict, I consulted the separate front-jet derivation and the recorded bounded controls. They agree with the factor, sign, front jet, and corner value. The controls are limited to normalization/smeared pairings and a constant-potential corner check; they are not proof of the all-mass support theorem.

## Checks and limitations

This was an algebraic and proof-structure audit; no tests or numerical runs were performed. No external source-priority audit was performed. The review does not settle novelty, physical interpretation, quantum or finite-energy extensions, detector claims, or the independent manuscript massless result. No unresolved mathematical counterexample or required theorem correction was found. The review recommends making the one-image specialization (K=-R_r/(4\pi\sin r)) explicit near (5)–(6) to make the normalization transparent.

The comparison is stated explicitly in `RESULT.md`: before maximum expansion, massless fixing is the reported three-diamond set and positive-mass fixing is J⁻(b); at the threshold both are all of M by the dense-trace argument; after the threshold the cap is already the entire initial sphere. This comparison depends on the separate massless result, which this audit did not re-prove; it does not add a dependency to the positive-mass support proof.
