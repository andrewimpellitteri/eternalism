# Agent report: AQFT locality lane

## Files changed

- `knowledge/aqft-locality/sources.jsonl` — nine lane-prefixed source records, each with a read depth; full-text anchors carry versions, locators, assumptions, conclusions, proof status, and limitations.
- `knowledge/aqft-locality/theorem-assumption-map.md` — scoped theorem statements and assumption dependencies for Reeh–Schlieder, Tomita–Takesaki/Bisognano–Wichmann, Fewster–Verch natural-state no-go, and dynamical locality in a scalar example.
- `knowledge/aqft-locality/comparison-contract.md` — comparison contracts for a Minkowski vacuum net, the BW wedge-vacuum scalar-field case, and the locally covariant/dynamically local model family.

## Evidence and checks

- Read task brief, `AGENTS.md`, `README.md`, `knowledge/README.md`, and `knowledge/NOVELTY.md` before research.
- Searched `knowledge/frontier/`, `knowledge/foundations/`, and `knowledge/methods/` for AQFT/locality source overlap. No relevant AQFT records were found to reuse; those lanes' sources remain untouched.
- Inspected primary Haag–Kastler (1964) full scanned text; Bisognano–Wichmann (1975) full scanned text including its hypotheses/caveats and Tomita theorem statement; Fewster–Verch (2012) arXiv full text for Theorem 6.13 and Theorem 4.3; and Fewster–Rejzner (2020) arXiv full text for the Reeh–Schlieder statement and local preparation discussion.
- Parsed `sources.jsonl` as JSONL and checked unique IDs / record count; no repository test suite was run.

## Limitations and unresolved questions

- Reeh and Schlieder's 1961 original paper and Takesaki's 1970 monograph remain discovery-level; precise Reeh–Schlieder assumptions are sourced to the inspected Fewster–Rejzner theorem statement. The original Reeh–Schlieder record flags its DOI as unverified rather than presenting it as confirmed.
- The 1975 BW paper is read in full at the relevant sections, but the proof is not independently reconstructed; its wedge-algebra existence, domain, and density caveats are preserved. The 1976 companion record is discovery-level only.
- Fewster–Verch theorem statements and selected derivation passages were read, not independently proved. The report does not claim proof reproduction or universal applicability outside the stated models/categories.
- No inference is made from AQFT locality to eternalism, presentism, passage, determinism, global simultaneity, clock time, or thermodynamic arrow.

## Task status

Submitted for coordinator review; not accepted/integrated. No commits or board transitions performed.
