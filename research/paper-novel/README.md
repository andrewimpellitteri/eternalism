# Doubly-principal complex-percolation note

`main.tex` is a standalone theorem-first working manuscript. It states the
accepted scalar classification and a separate conditional common-factor
covariant theorem. The existing philosophical article in `paper/` is unchanged.

Read the compiled manuscript at
`output/pdf/complex-percolation-note.pdf`. `CLAIM_LEDGER.md` gives claim status,
source locators, actual reading depth, falsifiers and excluded follow-ups.
`review/AGENT_REPORT.md` records the separate manuscript audit when completed;
`AGENT_REPORT.md` records coordinator disposition and build/verification results.

## Reproduce the exact checks

From the repository root, with Python 3 and its standard library:

```sh
python3 research/paper-novel/reproduce.py
```

The runner verifies the reviewed input hashes, checks manuscript references,
runs two existing exact finite scripts, and writes `verification.json` and
`reproduce_output.txt` here. It fails on changed inputs, a subprocess failure,
or a missing success marker. Those checks support the encoded finite cases;
the infinite classifications rely on the written proof.

## Build the standalone PDF

With an existing LaTeX installation, from this directory:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=complex-percolation-note main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=complex-percolation-note main.tex
```

The bibliography is embedded so there is no BibTeX/Biber dependency. Opening
`main.tex` in Codex also provides the source editor and PDF preview. No package
installation is part of this task.

The note is internally reviewed, not externally refereed or submitted. Priority
is bounded by the recorded search; no physical or temporal-ontology result is
claimed. The existing Lean certificate checks a finite kernel only.
