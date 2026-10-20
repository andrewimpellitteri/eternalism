# Physics full-text spot-check

Task: `rt-fulltext-claim-spotcheck`
Coordinator claim: `codex-fulltext-spotcheck`
Date accessed: 2026-10-20
Sample: all eight frozen records in `sampling-frame.json` with `audit_lane="physics"`. The global frame is frozen at revision `82f1547` and contains 20 full-text records plus Stein and Malament as two required shallower-depth primaries; its eight seeded lane draws are unchanged. Two causal-set records were added as explicit RC-4 same-paper alias anchors. Findings are in `findings.jsonl`.

## Method and routes

I used web search to locate source versions, then opened the versioned arXiv HTML pages directly for the eight physics-lane records (the two causal-set alias anchors were added in this follow-up) and the fixed Fall 2021 SEP archive for the secondary record. For the SEP entry I also opened its author/citation metadata page to verify author and edition identity. I checked title, author and version at the source, then read the specific locator passages and compared stated assumptions and conclusions with the frozen register. Quotes are short decisive excerpts; each is fewer than 20 words per source. I did not use metadata alone to certify any full-text claim.

The arXiv routes were:

- `https://arxiv.org/html/2607.05840v1` — Madsen, abstract, Definition 2.6, Theorems 4.18/5.1, Corollary 5.6, and discussion.
- `https://arxiv.org/html/gr-qc/0401112v3` — Bernal and Sánchez, abstract and Theorems 1.1/1.2.
- `https://arxiv.org/html/1307.1714v2` — Dürr et al., abstract, Sections 2-4, 6 and 7.
- `https://arxiv.org/html/2502.12750v1` — Hersent, Sections 3-5, especially the kappa/rho examples and stated limitations.
- `https://arxiv.org/html/gr-qc/0403001v2` — Hartle, abstract, IGUS model, Sections III-IV and VI, and Appendix A.
- `https://arxiv.org/html/gr-qc/9904062v3` — Rideout and Sorkin, Sections 1.1, 3-5; cross-checked parameter formulas against the v3 LaTeX source.
- `https://arxiv.org/html/1502.00018v1` — Wüthrich and Callender, Sections 3-5, including their caveats on genericity and the interpretation of growth.

The SEP route was `https://plato.stanford.edu/archives/fall2021/entries/spacetime-bebecome/`, Sections 3.2 and the author's citation page. This is a **secondary** exposition of Stein, not a primary source. It supports the register's summary of the SEP account, but it does not verify the statement against Stein 1968. The version field's claimed October 2021 substantive-revision date is inaccurate: the page states a substantive revision in August 2017; SEP identifies the Fall 2021 archive as a minor correction.

## Results and limits

Five records are confirmed at the checked statement level: Madsen's approximate-isometry results; Bernal-Sánchez's smooth time-function/splitting theorems; the deliberately hedged Dürr et al. foliation claim; Hersent's model-specific modular flows; and Rideout-Sorkin's classical sequential-growth derivation and carefully separated interpretive language. The SEP record needs a version-date correction while remaining clearly marked as secondary. Hartle's entry is claim-overstated where it reports “passage is not fundamental” and calls the assumed framework a “four-dimensional block description”: the cited source models and describes subjective temporal organization in four-dimensional terms, while the stronger ontological reading needs a separate bridge premise. Wüthrich-Callender is also claim-overstated on population-level scarcity of large non-Hegelian subsets: the paper presents that genericity claim as a suspicion conditional on limited evidence, with an unpublished estimate, rather than an established result. Its finite counterexample to the CST analogue of Stein is directly checked and remains supported.

The arXiv papers were read at the locator/claim level; this was not a proof audit or independent reproduction. In particular, I did not verify Madsen's full proofs, rederive Bernal-Sánchez's construction, reproduce quantum-equilibrium results, or validate Hersent's C*-algebra completion. The source claims remain the authors' claims. The six original findings plus two required RC-4 alias anchors make eight audited physics records. The frozen frame identifies Madsen, Rideout-Sorkin, and Wüthrich-Callender as same-paper aliases of `frontier-causal-embedding-2026`, `frontier-causal-growth-1999`, and `frontier-causal-becoming-2015`, respectively. Madsen is irrelevant to RC-4's becoming claim; Rideout-Sorkin supports the stated growth model and author interpretation, not an ontology conclusion; Wüthrich-Callender supports its finite counterexample and compatibility argument, while the genericity/Lorentz inference must remain qualified. The SEP entry is background for RC-2 only and cannot replace its primary Stein/Malament evidence. Accepting Hartle's downgrade leaves no listed RC contract dependent on that sample record, but it prevents using it as direct evidence that physics establishes an ontology.

This run did not attempt the separately required primary Stein 1968 and Malament 1977 source routes; they are outside the assigned eight-record physics subset and require their own primary-text findings. This is a targeted statement-level check, not proof reproduction or a review of all 22 frame entries. Each source quote in `findings.jsonl` is fewer than 20 words; no additional verbatim source wording is used here.
