# Agent report: CPOBC correspondence

## Files changed

Created only within `research/refocus-2026-10-21/cpobc-correspondence/`:

- `RESULT.md` — source/claim ledger, normalization audit, qbc-holonomy read-only audit, scope verdict.
- `CORRECTIONS.md` — exact proposed replacement passages for the old lane.
- `SEARCH_LOG.md` — primary-source search, archive availability, coverage limits.
- `sources.jsonl` — stable source records with version, hash, read depth, locators, and limits.
- `source/` — downloaded arXiv e-print archives and extracted source trees used for this audit.

## Strongest findings

- The primary paper differentiates TOBC, NTOBC, and CPOBC correctly; CPOBC does not generally imply commutativity, and the paper's Pauli result is only a failed pure-Pauli ansatz, not a full two-dimensional no-go.
- `qbc-holonomy/check.py` reruns a scalar certificate and asserts output strings; it has no operator-equation test. The scalar certificate checks MSR, product-BC, and norm-GC. Its nontrivial path phase violates the primary's vector-GC requirement, so the result cannot be described as satisfying all assumptions of Srivastava–Surya.
- A commutative transition algebra need not decompose into scalar direct summands; nilpotent/Jordan extensions are the elementary obstruction to the inference in the old RESULT.
- Xu §29.11 is the nearest follow-on and makes priority uncertain for several narrowed branches. Its companion is listed as unpublished with no URL; the arXiv v1 archive has no executable certificates or row lists. The displayed `R3=diag(1,x), R4=diag(1,y)` form is not obtained by similarity alone from a general commuting diagonalizable pair; the eigenvalue normalization needs justification.

## Checks

- Read Srivastava–Surya arXiv v1 TeX §§3.1–3.5 and Appendix; recorded hashes in `sources.jsonl`.
- Read Xu arXiv v1 §29.11 and checked its bibliography and archive contents for the cited companion and code/certificate artifacts.
- Read `research/qbc-holonomy/RESULT.md` and `check.py` without changing them.
- Ran `python3 research/longshots/bc-nonzero/nonzero_continuation.py`; exact output reports 49 nonzero transitions, no MSR failures, 109 product-BC equations with zero failures, norm-GC success at stages 2–4, and the `(3/5−4/5i)` path holonomy.
- Confirmed APS DOI metadata and abstract; APS omits the arXiv v1 abstract’s inference that any nontrivial representation must be higher-dimensional. The final published full text was authorization-gated, so no equation-level comparison to arXiv v1 is claimed.
- Ran `python3 scripts/check_sources.py --strict research/refocus-2026-10-21/cpobc-correspondence`: 7 records, 0 errors, 0 warnings, 0 info.

## Limitations and unresolved questions

- The published APS body was not accessible; an accessible author manuscript or subscription copy is needed to verify final-version changes.
- Xu's cited unpublished companion/certificate archive was not located. Long symbolic rank and ideal claims remain unverified author reports here.
- The complete nonsingular irreducible 2×2 CPOBC classification remains open in inspected materials, especially delayed non-scalar onset after scalar `R2`, Jordan cases, and the complement of the displayed chart. The normalization itself may leave additional cases unexamined.
- This lane does not claim novelty or global priority. The reasonable disposition is conditional go for an explicitly bounded independently audited extension; no-go for a general `d=2` no-go or for the scalar phase seed as a full operator-QBC witness.
