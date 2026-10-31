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
| Putnam/Stein paragraph | Closed 21 Oct: printed Stein p. 149 theorem inspected; Putnam record reconciled. The article uses the contextual condition (iv). |
| Defender replies (Bourne, Correia–Rosenkranz, Cameron, Skow) | Full-text reads; still frozen per `research/redteam/paper-ledger/FREEZE.md` |

## Build

pdflatex + bibtex per `paper/README.md` (TeX Live under `/Library/TeX/texbin`),
12 pages, no undefined references or citations, no BibTeX warnings. Pages rendered
with `paper/render_pdf.swift` and pages 1, 3 and 9 inspected. Output:
`output/pdf/temporal-ontology-working-draft.pdf`. `python3 paper/check_records.py`
passes.


## Independent review corrections, 21 October 2026

Applied revision-2 review R1–R7 (BL1, MA1–MA8, MI1–MI4). The completion
obstruction now concerns extension of the prescribed scalar amplitude rule to
the full cylinder-generated sigma-algebra; it no longer rules out arbitrary
measures on covariant events. Finite-cylinder decidability is distinguished
from finite positive witnesses, and the differing readings of Sorkin, Arageorgis
and Wüthrich–Callender are preserved. The Clifton–Hogarth implication and
reflexive conventions are explicit. Clock pinching preserves conditional ratios;
normalization of individual trajectories does not establish an all-state
isometry. Structured step constraints require their own dynamics and spectra.
Preferred-frame bounds and Brading's unresolved existence bridge are qualified.
The review's source-access limitations remain in
`paper/reviews/revision-2/REVIEW.md`; corrections do not upgrade source read depths.

## Rewrite, 24 October 2026: "Does the Universe Have a Present?"

Unreviewed rewrite (Claude session; not yet independently reviewed). Previous
version is commit c505534.

- Thesis reframed. Savitt's objection is the *location* problem (which sustaining
  region is present). The new argument is a *shape* problem specific to the
  universe: its stages must be bounded by global surfaces, fixed in SR by total
  energy-momentum, and in a closed GR universe only by a time "unique and proper"
  to the system, Brading's own notion of true time (2017). The problem-of-time
  routes are now classified in her terms (apparent / true-of-an-enlarged-system /
  mathematical / none) instead of via the regimented conservation test, which is
  demoted to a subsidiary bridge (footnoted momentum caveat).
- Concessions added: the SR universe case is manageable (global slab for the
  whole alone is allowed by "at least in the first instance local"); presents are
  regions, not slices; "every slab is a present" answered (no sequence of stages).
- Gödel 1949 (via Monton's quotation) distinguished: contingency is not the
  objection. Belot-Earman via Monton. Earman 2002 / Maudlin 2002 pointer only.
- Exits rewritten: whole-history present, restriction to subsystems (the
  anti-solipsism passage, 2013 p. 1110, now used), and "find the true time"
  (Brown's dynamical approach as Brading's suggested route, flagged as open).
- Dropped as main content: the four-point coverage proposition (now a footnote).
- Corrected: 2013 n. 3 was misdescribed (the footnote uses "principle of unity"
  neutrally; the omitted next sentence, "it applies to all three", is now quoted).

Sources read at full text this session: Brading 2013, 2015 and 2017 (author-site
PDFs, kbrading.org); Savitt 2021 SEP sec. 3.3 (live); Monton 2005 preprint sec. 6.
All Brading, Savitt, Gödel/Monton quotations string-checked against those texts;
Isham, Thiemann, Bamonti-Thebault and Wuthrich quotations string-checked against
the PDFs in the repository root (differences only hyphenation/capitalization).
GHTW quotations are inherited from the earlier audited draft, not rechecked.
Build: pdflatex+bibtex, clean (no errors, no undefined references), 12 pages.
