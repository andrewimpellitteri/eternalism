# Article working draft

> **This is not the project's main paper.** It is the earlier admissibility article. The main output
> is [What the Past Can Fix](../research/what-the-past-can-fix/). This folder stays here because
> records and issue text refer to its paths.

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

The 21 October 2026 redraft (second of the day) reframes the note around the
universe case as a problem of time: granting Brading's identification of what
exists with the genuine unities, the universe's present in special relativity
is the whole history, a global slice, a local region, outside the domain, or
absent; in canonical general relativity the global-slice option splits into
internal time (fails a regimented conservation test), an ideal clock (phantom
matter, FRW corrections per Thiemann), cosmic time (model-based, coordinative,
per Bamonti and Thébault) or no time (P1** restricted). The four-event coverage
model is retained. Supporting notes and source records are in
`research/brading-universe-frontier/`.

**Build status:** compiled locally on 21 October 2026 with pdfTeX (TeX Live
2026): 10 pages, all citations and references resolved on the final pass. The
one warning, an overfull box in the routes table, was fixed afterwards by
narrowing the table; rebuild to confirm. `verification.json` still describes
the previous version and should be regenerated from the next local build. The submission gates in `READINESS.md` remain open.

## Relation to the integrated research state, 28 October 2026

The [current project synthesis](../research/CURRENT_SYNTHESIS.md) and
[claim ledger](../research/CLAIM_STATUS.md) connect this article to the causal-set,
observer, Stein--GR, horizons and rival-grounding work. The article's constitutive
versus stage reading of dynamical sufficiency must keep determination separate
from existence: a region that fixes future values is not thereby shown to
constitute a unity or to make future events currently exist. The new screening
and common-extension results constrain that inference; they do not resolve
Brading's constitutive question or the article's submission gates. This article's
source and existing PDF have not been rewritten by that integration.
