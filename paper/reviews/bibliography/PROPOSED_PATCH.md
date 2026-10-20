# Proposed `paper/references.bib` patch

Review aid only; the shared bibliography was not edited.

1. In `Callender2011`, preserve the existing `editor = {Craig Callender}` and add `doi = {10.1093/oxfordhb/9780199298204.001.0001}`.
2. Add DOI fields:
   - `Bourne2006`: `10.1093/acprof:oso/9780199212804.001.0001`
   - `Cameron2015`: `10.1093/acprof:oso/9780198713296.001.0001`
   - `Skow2015`: `10.1093/acprof:oso/9780198713272.001.0001`
3. Replace `HoehnSmithLock2019` with a journal-form record, retaining its internal key if avoiding a `main.tex` edit:

```bibtex
@article{HoehnSmithLock2019,
  author = {Philipp A. H{"o}hn and Alexander R. H. Smith and Maximilian P. E. Lock},
  title = {Trinity of Relational Quantum Dynamics},
  journal = {Physical Review D}, year = {2021}, volume = {104}, pages = {066001},
  doi = {10.1103/PhysRevD.104.066001},
  url = {https://arxiv.org/abs/1912.00033v3},
  note = {arXiv:1912.00033v3; first submitted 2019-11-29, revised 2021-04-13}
}
```

This makes natbib render the 2021 journal-publication year while recording the exact arXiv text version inspected. It does not imply that the journal body was inspected or compared against v3. The arXiv v3 title is “The Trinity of Relational Quantum Dynamics”; the published journal title omits “The.”

4. In `BernalSanchez2005`, pin the existing arXiv URL to `https://arxiv.org/abs/gr-qc/0401112v3` and add a note such as `arXiv:gr-qc/0401112v3, revised 2005-02-15`; leave the 2005 journal year and DOI unchanged.
