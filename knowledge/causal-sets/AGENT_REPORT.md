# AGENT_REPORT: kb-causal-sets

Authorship: this is a Claude-subagent (Sonnet) completion of a lane whose OpenCode GLM
worker died when the Z.ai usage limit was hit. It is submitted for coordinator review, not
accepted completion.

Files written (only under knowledge/causal-sets/): sources.jsonl (8 records),
theorem-extraction.md, comparison-candidate-A.md, AGENT_REPORT.md.

## Taken from the dead worker's preserved files vs read afresh
- Taken: the extracted texts (csg.txt, becoming.txt, embed.txt), the abstract pages, and the
  LaTeX source of Rideout-Sorkin (e-print dated 2004-06-26, matching v3). I did not trust the
  worker's conclusions or any notes; its event log showed it never obtained the BLMS,
  Malament or HKM papers and never wrote deliverables.
- Read afresh by me: all of csg.txt, all of becoming.txt, embed.txt Secs. 1-3, Lemmas 4.1 and
  4.3, Prop. 4.16, Thm 4.18, Thm 5.1, Cor. 5.6, Secs. 6.1-6.2, and the reference list; plus the
  coordinator notes (fulltext-reads-causal-sets.md, csg_ancillarity_check.py header). I
  spot-checked formula (17), Eq. (12) pieces and P(C_n) in the LaTeX source.
- Re-fetched this session: arXiv abs page for 2003.11311 (title/version) and one web search.

## Search availability
WebSearch and WebFetch worked. The APS page for BLMS 1987 returned HTTP 403. A web search for
Malament 1977 JMP found no free full text; HKM 1976 was not located. These
three are unread; BLMS and Malament are recorded at discovery depth with DOIs taken from
Madsen's reference list; HKM has no record.

## Checks
`python3 scripts/check_sources.py --online knowledge/causal-sets`: 8 records, 6 arXiv IDs and
3 DOIs checked, 0 errors, 0 warnings. This verifies identifiers/titles only.

## Limitations
- Equation numbers are those of the ar5iv/arXiv-HTML renders; journal numbering unchecked.
- Madsen: proofs of Props 4.8-4.15, 5.3 and Appendices not audited; F2 formula layout
  originally flattened (square root resolved by coordinator below); preprint unrefereed.
- Brightwell et al. and Surya-Zalel records are discovery-depth and rest on the coordinator note.
- Existing seed/frontier records are abstract depth and were left untouched; the cs- records
  relate to them via related_source_ids rather than duplicating IDs.
- The candidate-A comparison contains our inference (flagged); nothing is a novelty claim.

## Unresolved
Obtain BLMS 1987, Malament 1977, HKM 1976 and Muller 2503.01719; read Brightwell et al. and
Surya-Zalel directly; check whether Madsen's F3 is implied by F2.

## Codex coordinator review and corrections (2026-10-19)

This section records a separate review of the Claude-subagent handback. The original
authorship and reading limits above remain in force.

- Opened [Rideout-Sorkin v3](https://arxiv.org/html/gr-qc/9904062v3), Secs. 1.1, 3, 5;
  spot-checked label/path independence and Eqs. (17)-(18), including the distinction between
  a labelled formation weight and the probability summed over inequivalent labellings.
- Opened [Wuthrich-Callender v1](https://arxiv.org/html/1502.00018v1), Secs. 3-4;
  checked the counterexample and their tenseless-history reading. Flagged their prose Stein
  reconstruction as unsuitable for direct formalization without a primary-source audit.
- Opened [Madsen v1](https://arxiv.org/html/2607.05840v1), Def. 2.6 and statements of
  Thm. 4.18 / Cor. 5.6. Resolved the missing square root in Eq. (4). No proof audit.
- Restricted observer-record equivalence to records explicitly defined as measurable
  functions of the shared covariant history. Corrected the labelling/foliation and
  stochastic-law/completed-history distinctions. Added separate six-item comparisons for
  the interpretive and embedding anchors.
- Re-ran `python3 scripts/check_sources.py --online
  .worktrees/kb-causal-sets/knowledge/causal-sets`: 8 records, 6 arXiv IDs, 3 DOI lookups,
  0 errors, 0 warnings. The lookups used the project cache; metadata checks do not verify claims.
- Re-ran `python3 -I knowledge/defeat-search/csg_ancillarity_check.py`: exact rational
  checks agree through n=5 for the tested parameters; no universal theorem inferred.
- Project test baseline: 7/8 tests pass; the existing live-board test expects 11 tasks
  while the board has 42. Already tracked as `rt-fix-live-contract-test`; unchanged here.

Review disposition: suitable for integration as a bounded survey and conditional comparison,
with the unread originals and proof limits retained. No new result or ontology conclusion.
