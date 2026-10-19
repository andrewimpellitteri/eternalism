# Agent report: `kb-gr-qg-time`

## Files

- `knowledge/gr-qg/sources.jsonl`: retained the partial salvage’s stable lane IDs for core items, corrected its overstated read-depth labels to reflect the source pages actually inspected, added theorem/section/page locators where verified, and restored out-of-lane citations as explicitly discovery-only records. Reused the existing frontier ID `frontier-emergent-spin-glass-2025` for 2510.20902 rather than creating a duplicate record.
- `knowledge/gr-qg/comparison.md`: model/version comparison for global-hyperbolic spacetimes, regular cosmological time, Gödel’s solution, canonical GR/Dirac constraints, the Kuchař review lead, Anderson’s review, and 2510.20902. It records assumptions, global-time/foliation status, clock/observer limitations, empirical status, and what defeats stronger ontology claims.

## Primary reading completed

- Bernal–Sánchez, arXiv gr-qc/0401112v3: opened the primary HTML and read its abstract, Theorems 1.1–1.2 and proof construction (Secs. 2–3). Full-text label means the relevant short paper was read; no independent proof reproduction.
- Bernal–Sánchez, arXiv gr-qc/0306108v2: read the main theorem, relevant preliminary splitting remark, and proof locator in primary HTML. No reproduction.
- Andersson–Galloway–Howard, arXiv gr-qc/9709084v1: opened the primary PDF; checked the definition/regularity condition, Theorem 1.2, Minkowski example, and Corollary 2.6. Labeled `abstract` because the full proof was not read.
- Gödel, Rev. Mod. Phys. 21 (1949), DOI 10.1103/RevModPhys.21.447: read the four-page primary PDF; checked properties (4)–(6) and the metric argument for closed timelike lines. No independent derivation of the exact solution.
- Isham, arXiv gr-qc/9210011v1: inspected primary HTML sections on canonical setup, embedding foliations, internal time, and Dirac constraints. This is selective review reading, not a proof audit; label `abstract`.
- Anderson, arXiv 1009.2157v3: inspected primary HTML sections on frozen formalism, foliation/global-time issues, and York time. Selective review reading; label `abstract`.
- Saraidaris–Shaposhnik, arXiv 2510.20902v2: inspected primary HTML abstract, algebraic framework/theorems, model sections and discussion, including the stated low-energy detectability limitation. Partial read only; no proof, code, or numerical reproduction audit. The existing frontier discovery ID is the source-register record.

Other retained leads (Kuchař 2011, HKT, ADM, Thiemann, shape dynamics, Hawking, Butterfield–Isham) are `discovery` only. Their records avoid treating claims found in a summarizer’s salvage as source-verified. In particular Kuchař’s own article was not directly read, so the comparison attributes no detailed claim to him.

## Checks

- `python3 /Users/andrew/eternalism/scripts/check_sources.py /Users/andrew/eternalism/.worktrees/kb-gr-qg-time/knowledge/gr-qg`
- `python3 /Users/andrew/eternalism/scripts/check_sources.py --online /Users/andrew/eternalism/.worktrees/kb-gr-qg-time/knowledge/gr-qg`

Offline passed after the final edits: 13 records, 0 errors and 0 warnings. Online mode checked 9 arXiv IDs and 7 DOI lookups: 0 errors, with two `http unreachable` warnings for the DOI lookups attached to the Thiemann and shape-dynamics discovery leads. Their arXiv identifiers remain in those records. These warnings are endpoint reachability limits, not title mismatches.

## Limitations and unresolved questions

- The salvage file used summarizer-mediated reads and contained locators/depth labels that were not safe to inherit. The task register was rewritten from direct primary-source checks and the salvage-only ancillary leads were retained with lower depth. This lane did not reproduce any theorem or audit numerical code.
- No direct reading of Kuchař’s 2011 review, Hawking’s chronology-protection paper, ADM’s reprint, HKT, Thiemann, shape dynamics, or Butterfield–Isham was completed. These remain nearest-predecessor leads, not verified support.
- For cosmological time, only the definition, principal theorem, selected corollary and Minkowski example were verified. The regularity requirement is not a generic cosmological premise.
- The Gödel implication “CTCs prevent a time function and global hyperbolicity” is marked as a standard causal-theory inference, distinct from the claims Gödel states in his 1949 paper.
- 2510.20902 is a large-N algebraic/numerical diagnostic with time-independent boundary setup. Full theorem proofs, computational method/code, finite-N limits and any physical interpretation as spacetime were not audited.
- No conclusion about eternalism, presentism, passage, determinism, or the thermodynamic arrow follows from this survey.

## Coordinator review (2026-10-19)

Codex inspected all three deliverables and checked ownership and related source IDs.
Direct statement-level spot-checks: Bernal–Sánchez v3 Theorems 1.1–1.2 and version date;
Isham v1 Sec. 3.3.1 (compact Σ, assumed foliability, coordinate time versus clocks);
2510.20902v2 Sec. 5 Proposition 1 (restricted smearing class, not a universal
non-emergence theorem). These match the comparison's bounded wording. The coordinator
did not re-read Gödel's PDF or audit proofs. Re-running the online source checker
reproduced 0 errors and the same two endpoint-reachability warnings. Accepted for
integration as a bounded survey, with Kuchař and the other unread leads retained as gaps.
