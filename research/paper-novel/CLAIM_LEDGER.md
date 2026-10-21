# Manuscript claim ledger

Draft date: 2026-10-21. The manuscript is `main.tex`; the reviewed theorem
inputs are pinned in `input-manifest.json`. The scope authorization is the
accepted `research/adversarial-review/AGENT_REPORT.md`. A surviving internal
proof review is not an external referee report or a global priority certificate.

| Manuscript claim | Status and assumptions | Evidence / exact locator | Verification limit |
|---|---|---|---|
| Scalar matching measure on the labelled DP cylinder sigma-algebra exists iff p in [0,1] | Selected project theorem; finite complex-valued countable additivity and exact prescribed generator values | Theorem 1; `research/creative/RESULT.md`; native proof report; GLM scalar report and coordinator review | All-level proof is handwritten; checks are finite. Not arbitrary covariant events. |
| Every DP order is an arbitrary order with two caps | Elementary project derivation | Lemma 2, Eq. (4); two-cap bijection and cover count | Checked independently on small finite orders; proof supplies generality. |
| Endpoint probability is product (1-s^j) | Established classical identity, rederived | Lemma 3; Bombelli–Seggev–Watson 0809.2258v2, Sec. 2, Theorem 2.1, Eq. (2) | No probability theorem is claimed as new. |
| Explicit divergent DP variation bound | Proposed mathematical delta | Eq. (10) or its labelled `eq:divergence`; modulus normalization plus the two preceding lemmas | Individual level bound, not literal equality to the predecessor's cumulative term. Use labels if equation numbering changes. |
| Smaller labelled algebra differs from covariant posts algebra | Prior definition and scope distinction | Dowker–Zalel 2212.01149v2, Sec. V, Eqs. (29)–(31), Theorem 14 | The manuscript does not reprove their equality of algebras. |
| Prior authors recognized this calculation and suggested post techniques | Prior-work attribution | Dowker–Zalel v2 Sec. V, final paragraph after Eq. (31); Zalel 2021 thesis Ch. 6, §6.2.3, pp. 89–90 | A calculation in an already-suggested direction; no new problem statement or method. |
| Full-labelled extension obstruction and bounded-variation framework predate this note | Prior results | Dowker–Johnston–Surya 1007.2725v1 Sec. 4; Surya–Zalel 2003.11311v1 Theorem 2.1, App. B | Larger-domain nonextension alone does not prove the smaller-domain result. |
| Conditional covariant existence iff 0<p<=1 | Separate project theorem under all-principal common-factor (T), normalization on infinitely many posts, and finite complex CA | Theorem 5 in current numbering, label `thm:cov`; `research/creative/COVARIANT_RESULT.md` classification and its accepted audits | (T) is an added value rule, not implied by covariance. |
| Common factor cannot be zero under those assumptions | Elementary laminar-cover argument | Proof of `thm:cov`; fixed-rank disjointness and across-rank laminarity | Not the false assertion that arbitrary complex zero sets have zero-valued unions. |
| Classical measure supplies common factor c(1-p) and infinitely many posts | Established probability facts plus restriction | Bombelli–Seggev–Watson v2 Sec. 2, Theorem 2.1 and Eq. (2); its attribution of the infinite-post result to Alon et al. | The original Alon proof is not independently reproduced in this drafting task. |
| DP-only common-factor weakening fails | Project counterexample | Proposition `prop:dirac`, infinite blocks A2 followed by a post | Satisfies the weakened rule with zero factor; does not contradict the all-principal theorem. |
| Infinite-dimensional norm matching need not satisfy scalar obstruction | Standard indicator measure applied here | Scope section, L²(P_1/2) example; accepted vector counterexample and audits | Changes phase/off-diagonal data; no physical vector dynamics or new extension of fixed scalar data. |
| V2, V5, V6 exact values and finite multiplicity checks | Reproduced finite checks | Appendix; `reproduce.py`, `reproduce_output.txt`, `verification.json` | These numbers alone do not prove unbounded variation. |
| Lean scope | Finite certificate only | `formal/lean/Certificate.lean`; accepted implementation audit | Infinite theorem, sigma-algebras and countable additivity are not encoded. No new Lean work is claimed. |
| Physical / philosophical consequence | None established | Scope section | No empirical prediction, observer model or temporal-ontology conclusion. |

## Sources and reading depth

- **Dowker–Zalel, 2212.01149v2 (17 July 2023).** Coordinator targeted
  full-text reads of §§III.4 and V, Eqs. (29)–(31) and following paragraph,
  Theorem 14; earlier project source reviewers read the relevant sections.
  Publisher text was not compared. HTML rendering date is not version date.
- **Zalel, *Discrete random spacetimes: covariance and quantization in growth
  dynamics for causal sets* (Imperial, 2021).** Ch. 6 §6.2.3 pp. 89–90 was read
  in the prior native source/novelty lanes. This drafting task inherits their
  locator and could not obtain a fresh copy; it did not independently reopen
  the thesis PDF. The citation is prior-work attribution only. The priority
  delta is carried by the published Dowker–Zalel Sec. V statement, not by the
  thesis.
- **Bombelli–Seggev–Watson, 0809.2258v2 (25 September 2008).** Targeted full-text
  read of §2, Theorem 2.1, Eq. (2) and the following infinite-post attribution.
  Its probability identity is also rederived in the manuscript. No publisher
  comparison or independent rereading of the original Alon paper.
- **Dowker–Johnston–Surya, 1007.2725v1 (16 July 2010).** Targeted §4 review and
  prior project full-text audit. Cited for the established larger-algebra
  obstruction, not for the selected theorem.
- **Surya–Zalel, 2003.11311v1 (25 March 2020).** Targeted full-text read of
  §2.3, Theorem 2.1 and its bounded-variation context. Appendix B is cited as
  the proof location; its general extension machinery is not re-audited here.

## Corrections and excluded probes

The old ordinal-block certificate uses minimum-element seam counts; the
two-cap bound uses maxima. The accepted GLM suite distinguishes them. The
correct V2 is 1/sqrt(2). Natural-label multiplicity N(H) counts distinct
representatives, not all linear extensions without automorphism correction.

The historical local-renewal refinement has a rank-one qualification: it does
not force the unused kappa_1, and constancy starts at rank two. That refinement
is deliberately omitted; (T) in the paper explicitly assumes one common
factor. Shape-dependent division at p=0,1 is also omitted. The unaudited
rank-factor candidate and regularization follow-ups are not manuscript results.

## Falsifiers and priority limits

A defect in the two-cap correspondence, product identity, multiplicity,
laminarity or scalar finite-variation premise would defeat the affected proof.
A previous proof of the identical prescribed-value classification would
defeat the publication delta. Bounded searches in the accepted priority reports
do not exclude that possibility. No newness is claimed for generic measure
extension, the Euler product, the indicator construction, using agents or
using a proof assistant.
