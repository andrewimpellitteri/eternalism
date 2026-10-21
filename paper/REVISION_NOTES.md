# Revision notes, 21 October 2026 (`article-revision-2`)

## Added

- Abstract: the two case findings and the causal-set analogue, with the existing hedges kept.
- Sec. 2: a worked admissibility case on Brading 2013/2015 against a composite block
  rival, following `research/article-admissibility/case/PROPOSED_PAPER_EDITS.md`
  items 1–6.
- Case I: the Clifton–Hogarth trichotomy as a precise exclusion of its premises'
  conjunction; the tested coupled preferred frame (Einstein-aether, LAGEOS α₁)
  against a stipulated hidden foliation; the Brading paragraph points to Sec. 2.
- Case II: the "research task" paragraph replaced by what is now known: the trinity
  results exclude interactions; normalization under interaction is model- and
  formulation-dependent (Cafasso; Smith–Ahmadi; Boette–Rossignoli; Ludescher;
  Hausmann); the project's three-state clock as an application.
- Records section: birth-order ancillarity in sequential growth (Rideout–Sorkin;
  Brightwell–Łuczak) and the growth/completion tension (Surya–Zalel; Sorkin;
  Arageorgis; Wüthrich–Callender; Dowker–Johnston–Surya), stated as one excluded
  conjunction per ontology.

## Deferred, with gates

| Material | Gate |
|---|---|
| The project's doubly-principal theorem for complex percolation and the conditional covariant extension | `adversarial-review` (claimed by codex-adversarial), then `paper-novel-result`, a separate paper |
| Long-shot results: no observable birth-order trace under norm-only covariance; stage-limit covtree walk without countable completion | Independent review of `research/longshots/`; priority checks; both are at most small remarks |
| Putnam/Stein paragraph | Printed Stein 1991 theorem; Putnam record reconciliation |
| Defender replies (Bourne, Correia–Rosenkranz, Cameron, Skow) | Full-text reads; still frozen per `research/redteam/paper-ledger/FREEZE.md` |

## Build

pdflatex + bibtex per `paper/README.md` (TeX Live under `/Library/TeX/texbin`),
12 pages, no undefined references or citations, no BibTeX warnings. Pages rendered
with `paper/render_pdf.swift` and pages 1, 3 and 9 inspected. Output:
`output/pdf/temporal-ontology-working-draft.pdf`. `python3 paper/check_records.py`
passes.
