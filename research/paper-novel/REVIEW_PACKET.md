# Review packet: theorem note

Prepared 2026-10-21 for external review. This file is a packaging checklist, not
part of the manuscript.

## Send these files

- `output/pdf/complex-percolation-note.pdf` — built manuscript (7 pages).
- `main.tex` — source; the bibliography is embedded.
- `CLAIM_LEDGER.md` — claim status, source locators and read-depth limits.
- `reproduce.py` — exact finite checks and manuscript cross-reference check.
- `reproduce_output.txt` — captured successful run.
- `verification.json` — pinned inputs, manuscript hash and check status.
- `review/AGENT_REPORT.md` — independent manuscript audit (proof and source
  correspondence, not a priority certificate).

Optional: the project’s `research/adversarial-review/AGENT_REPORT.md` for the
broader accepted scope. Do not send copyrighted primary scans.

## What the note claims

- A countably additive complex measure on the doubly-principal labelled
  cylinder sigma-algebra matching the prescribed complex-percolation amplitudes
  exists iff `p` is in `[0,1]`.
- The obstruction is the explicit divergent lower bound `V_n >=
  |p|(|p|+|1-p|)^{n-2} c_s`.
- A separate conditional covariant common-factor theorem holds iff `0<p<=1`
  under the all-principal rule `(T)` and normalization on infinitely many
  posts; a Dirac counterexample shows `(T)` cannot be weakened to
  doubly-principal pasts alone.
- The note does **not** claim a new general extension criterion, a physical
  dynamics, an empirical prediction or any temporal-ontology conclusion.

## Build and reproduce

```sh
# in research/paper-novel
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf \
  -jobname=complex-percolation-note main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf \
  -jobname=complex-percolation-note main.tex

# from the repository root
python3 research/paper-novel/reproduce.py
```

`reproduce.py` verifies six pinned source hashes, 22 manuscript labels, five
bibliography entries, 407 exact cylinder identities and the 26/26 bounded
scalar checks. It writes `verification.json` and `reproduce_output.txt`.

## Known limits to state in the cover letter

- Internal review, not external refereeing. The independent audit found no
  proof gap but did not perform a global priority search.
- The Zalel 2021 thesis is unavailable for independent reading here; it is
  cited as inherited prior-work attribution only. The priority delta rests on
  the published Dowker–Zalel Sec. V statement.
- The published Dowker–Zalel pagination was not collated; the arXiv v2 locators
  are what were checked.
- The finite checks corroborate bookkeeping; the infinite theorem rests on the
  written proof.
- The Lean certificate is a finite kernel only; it does not formalize the
  sigma-algebras or the infinite theorem.
- Author/affiliation/acknowledgments/AI-disclosure lines are deliberately
  generic and must be decided by the sender before submission.

## Suggested cover note

> The note classifies countably additive complex extensions of the
> doubly-principal complex-percolation amplitudes: existence holds exactly on
> `p in [0,1]`, via an explicit divergent level sum. It executes a calculation
> that Dowker–Zalel (CQG 40 (2023) 155015, Sec. V) explicitly leave
> inconclusive. A separate conditional covariant statement is included with its
> value rule and a Dirac counterexample to the weaker rule. The manuscript is
> internally reviewed and accompanied by a checked finite reproduction bundle;
> it is not a claim of global priority or of any ontological conclusion.
