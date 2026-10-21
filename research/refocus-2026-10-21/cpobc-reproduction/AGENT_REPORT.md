# Agent report: CPOBC reproduction

## Files changed

- `RESULT.md` — complete restricted 2×2 self-adjoint nonsingular argument from Xu's necessary identities, exact controls, chart feasibility assessment, and limitations.
- `check.py` — independent exact-rational verification using Python standard library only.
- `check-output.txt` — output from the revised recorded run.
- `sources.jsonl` — versioned primary-source records and PDF hashes.
- `srivastava-surya-2603.25503v1.pdf` and `xu-2607.26672v1.pdf` — pinned source versions used.

## Evidence and checks

Reconstructed Xu arXiv:2607.26672v1 Sec. 29.11, Eqs. (252)-(260). For self-adjoint nonsingular Q1,Q2, [Q1(I-Q1),Q2]=0 restricts Q1's blocks to a complementary eigenvalue pair. The second identity [Q1 Q2^-1,Q1^-1 Q2]=0 becomes normality of C=Q1^-1 Q2. Its off-diagonal block is (q^-2-(1-q)^-2)DD*, forcing Q1,Q2 to commute. Then [R,Qn]=0 handles the distinct-R case directly; scalar R is handled by the two-precursor Hermiticity condition, whose exact polynomial coefficient is (2q-1)(1-r). This forces Q1 to commute with every antichain generator. Propagation to all transitions relies on the cited central-generator lemma, which is explicitly imported rather than claimed as reproduced.

The standard-library script checks the polynomial coefficient identity as exact coefficient maps, a mixed block with [F,B]=0 but nonzero normality commutator 27/4, the diagonal control, a distinct-R mixed candidate rejected by [R,Qn], and a noncomplementary-spectrum candidate rejected by [F,Qn]. It also retains the prior commuting, nonsingular noncommuting, and singular-r=1 controls with all displayed determinants. Command: `python3 research/refocus-2026-10-21/cpobc-reproduction/check.py` (PASS).

Strict source-contract check: `python3 scripts/check_sources.py --strict research/refocus-2026-10-21/cpobc-reproduction/sources.jsonl` — 1 file, 2 records, 0 errors, 0 warnings. Both primary records include `related_source_ids` and `open_questions`.

The chart audit now treats diagonal R3,R4 as a restricted ansatz rather than a proved gauge. It keeps x != 1, uses ad-q generally, and only uses q-a^2 on d=a. No chart elimination was run.

## Limitations and unresolved questions

This submission does not reproduce the central-generator propagation proof or the full theorem, and it says nothing about non-self-adjoint or singular branches. The source's larger first-simple-spectrum calculation has a supporting companion citation, but a public certificate/code artifact was not located. Full-chart feasibility is limited by the unproved generality of the diagonal R3,R4 ansatz and the missing residual catalog / determinant product. No algebra system was available and no packages were installed; the six-variable saturation was assessed but not executed. No existence or global nonexistence claim follows.
