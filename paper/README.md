# Article working draft

Main source: `main.tex`; bibliography: `references.bib`. The article advances a
provisional philosophical burden-of-proof argument, not a new physical result
or a completed novelty claim. It is separate from the final synthesis task.

Build from this directory with existing TeX tools:

On the current macOS host, the executables are under `/Library/TeX/texbin/`;
use that prefix if `pdflatex` or `bibtex` is not on the shell's search path.

```sh
mkdir -p ../tmp/pdfs/article ../output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=../tmp/pdfs/article main.tex
cd ../tmp/pdfs/article
BIBINPUTS=../../../paper: bibtex main
cd ../../../paper
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=../tmp/pdfs/article main.tex
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=../tmp/pdfs/article main.tex
cp ../tmp/pdfs/article/main.pdf ../output/pdf/temporal-ontology-working-draft.pdf
```

The first pass normally reports unresolved references until BibTeX and the
subsequent passes run. No dependencies are installed by these commands.
`SOURCE_AUDIT.md` is authoritative about read depth and manuscript claim scope.
`READINESS.md` lists the unmet source, argument and novelty gates.

Run the independent exact toy check with `python3 paper/check_records.py` from
the repository root. This validates the stated finite arithmetic only, not
the general proposition or any ontology.

The displayed author line is deliberately generic: human authorship, affiliation,
acknowledgments and any journal-specific AI-disclosure wording require a later
decision. The draft must not be submitted under invented author information.

The 21 October 2026 reframe replaces the earlier prospectus with a focused
paper on Brading's P1** and the coverage problem (8 pages). The
20 October revision and its reviews remain preserved under `reviews/`; the
external review and rebuild plan are under `reviews/external-2026-10-21/`.
`verification.json` records the build, citation counts and source/output
hashes. The submission gates in `READINESS.md` remain open pending independent
re-review.
