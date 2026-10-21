# Independent manuscript audit

Date: 2026-10-21. Reviewed `research/paper-novel/main.tex` against the assigned
brief and the current `research/adversarial-review/AGENT_REPORT.md`. This is a
bounded proof and source-correspondence audit, not a global priority search or
acceptance decision.

## Verdict

**No material counterexample found to either stated theorem.** The labelled
doubly-principal classification is supported by the two-cap reduction and the
levelwise variation contradiction. The covariant classification is internally
consistent under its explicitly stronger hypotheses: a single finite factor
for every principal shape and normalization of both the whole space and
`P_infinity`. The manuscript keeps the two event algebras distinct and makes no
temporal-ontology inference. Keep the priority claim narrow: the paper solves
the specific unresolved estimate named by Dowker–Zalel; it does not provide a
new general extension criterion.

**Material submission gap:** the appendix says the repository contains
`reproduce.py`, `CLAIM_LEDGER.md`, and a `README.md` with review status
(main.tex:353–369, 384–387), but the assigned directory currently contains
only `main.tex`. Thus the claim ledger and advertised reproduction bundle are
not available to this review, and the paper does not yet meet the brief's
deliverable requirement for those artifacts. This is a packaging/reproducibility
defect, not a failure of the displayed proof.

## Proof audit

- **Two caps and counts (main.tex:53–103):** Every finite naturally labelled
  order with unique maximum has that maximum last and above every element.
  Applying this twice gives exactly `G ⊕ {u} ⊕ {v}` for the doubly-principal
  orders, including `G` empty at size two. The first cap contributes one cover
  from each maximal element of `G`; the second contributes one cover. No new
  incomparable pairs arise. The bound `L(G) ≥ k−M(G)` follows by assigning a
  cover with each nonmaximal vertex as lower endpoint; hence `w(G)≥k`.
  No counterexample or indexing defect found.
- **Endpoint product (main.tex:105–138):** The closure probability for a
  prescribed finite order is `r^L s^h`: covers are required, incomparable
  pairs' direct edges are forbidden, and each redundant comparable edge
  contributes a summed factor `r+s=1`. The event that the last vertex is
  above the previous ones is the sum over `G ⊕ {u}`. Reversing labels and
  arrows makes it the event that the first vertex reaches every later one;
  exposing successive vertices gives factors `1−s^j`, with no independence
  assumption between whole reachability events. Since `sum s^j` converges,
  the infinite product is positive. This agrees with the one-sided product
  locator in Bombelli–Seggev–Watson, Sec. 2, Eq. (2); the manuscript’s proof
  independently fixes its indexing.
- **Variation obstruction and converse (main.tex:140–189):** For
  `p∉[0,1]`, `a,b>0`, `t=a+b>1`, and `r,s∈(0,1)`. The cap identity gives
  `V_(k+2)=a Σ t^(w+h)r^w s^h`; using `w+h≥k` yields the valid lower bound
  `a t^k F_k(s) ≥ a t^k c_s`. No equality is asserted at the inequality
  step. Fixed-rank doubly-principal cylinders are pairwise disjoint, so their
  absolute values are bounded by the total variation of any matching finite
  complex measure. The unbounded sequence contradicts that bound. The
  probability construction for `0<p<1` and Dirac endpoints `p=0,1` match
  the generator values, with the stated zero-exponent convention. The
  restriction argument to larger sigma-algebras is used in the correct
  direction only.
- **Covariant events and laminar cover (main.tex:191–283):** The post event
  `D_H` is measurable: under natural labels a post with `n−1` ancestors must
  have label `n−1`; its finite past is a prefix condition and persistence is
  a countable intersection. Its intersection with `P_infinity` belongs to
  `R_p`. At equal ranks distinct shapes are disjoint. For unequal ranks, the
  later post's finite inclusive past determines whether an earlier post of
  the specified rank and shape exists; transitivity and persistence of the
  later post then make that earlier post persistent. Thus intersections are
  empty or the later-rank event. Every history in `P_infinity` has a least
  post label, so the countable `D_H` family covers it. This justifies the
  finite inclusion–exclusion plus continuity-from-below step when `κ=0`;
  the proof does not incorrectly treat arbitrary zero-valued sets as null.
- **Multiplicity and endpoint exclusions (main.tex:242–265):** Grouping
  labelled cylinders by unlabelled shape contributes exactly `N(H)` distinct
  natural-labelled representatives; no automorphism division is appropriate
  after this grouping. This makes the covariant rank-`n` variation exactly
  `|κ|V_n`. At `p=0`, shapes of size at least two have a cover and zero
  amplitude, and those ranks still cover `P_infinity`; the singleton does not
  need to be ruled out by division. For `0<p<1`, the common future survival
  factor is `c(1−p)` independent of the finite past shape; at `p=1` the chain
  gives factor one. No endpoint defect found.

## Algebra, prior work, and scope

The labelled algebra `D` (main.tex:53–63) is the sigma-algebra generated by
doubly-principal labelled cylinders. It is not the covariant posts algebra
`R_p` (main.tex:191–201), and the manuscript correctly says so. This matches
Dowker–Zalel, arXiv:2212.01149v2, Sec. V, Eq. (29) and the definition at
Eqs. (29)–(31), lines 980–1038 of the public full text: they define the same
doubly-principal cylinder subalgebra and report their complex-transitive-
percolation extension test there as inconclusive. In particular, their
valency-one obstruction explains why failure on the full cylinder algebra
does not settle the target smaller domain. Dowker–Zalel's closing discussion
at lines 1089–1107 explicitly suggests post-probability techniques to compute
the remaining sum. The manuscript fairly frames its delta as carrying out
that suggestion (main.tex:285–309), not as originating the general method.

Dowker–Johnston–Surya, arXiv:1007.2725v1, Sec. 4, Lemma 1 / Claims 4–5
(public full-text lines 857–953), proves the full-labelled complex-percolation
bounded-variation obstruction for non-real and outside-unit-modulus cases;
Surya–Zalel, arXiv:2003.11311v1, Theorem 2.1 (lines 680–709) gives the scalar
bounded-variation extension criterion on the finite-cylinder event algebra.
The manuscript does not overclaim these as proofs for the smaller prescribed-
value problem. Zalel's thesis Ch. 6, Sec. 6.2.3, printed pp. 89–90 is named,
but I did not independently retrieve or reread that thesis in this audit.

Bombelli–Seggev–Watson, arXiv:0809.2258v2, Sec. 2, Theorem 2.1 and Eq. (2),
does establish the one-sided product and states that infinitely many posts
occur almost surely, attributing the latter result to Alon et al. The
manuscript accurately presents this as a prior result and separately derives
the shape-independent future factor. This BSW source was read at full-text
depth. Its Theorem 2.1 gives the probability of a particular element being
a post on `N`, not by itself the almost-sure infinitely-many-post theorem;
the manuscript's wording correctly attributes that assertion to Alon et al
through BSW, though a direct citation to Alon et al. would strengthen the
source chain.

The covariant theorem is not an unconditional covariance result. The all-
principal, rank-independent `κ` rule and both normalizations are explicit in
the statement (main.tex:208–220); covariance alone is not claimed to imply
them. The weaker doubly-principal-only rule is separately refuted by the
Dirac example (main.tex:268–283). The manuscript does not import the local-
renewal refinement or the unresolved rank-only classification: its only
uniform factor rule is exactly the stronger all-principal assumption, and
main.tex:341–342 explicitly excludes rank-dependent factors as theorems.
The `κ_1` local-renewal correction in `coordinator/BOUNDARIES.md` is not
silently used. The rank-one counterassignment appears only as a finite-check
description (main.tex:366–367), not as a rank result.

Scope statements at main.tex:311–349 correctly distinguish the scalar complex
measure from `Q(E)=|μ(E)|²`, the Hilbert-valued norm-matching counterexample
from preservation of phases/off-diagonal data, and mathematical conclusions
from physical or philosophical bridge premises. The latter example is
presented as a counterexample to norm-only scope, not a new extension of the
fixed premeasure.

## Checks and limits

- Read the manuscript line-by-line and checked the key decompositions and
  endpoint cases directly.
- Ran the existing read-only exact-arithmetic fixture
  `python3 research/adversarial-review/coordinator/check_boundaries.py`:
  407 exact cylinder identities through rank five and the `κ_1` singleton
  counterassignment passed. This is finite corroboration only.
- Primary source read depths: full text for Dowker–Zalel 2212.01149v2,
  Dowker–Johnston–Surya 1007.2725v1, Surya–Zalel 2003.11311v1, and
  Bombelli–Seggev–Watson 0809.2258v2 at the listed locators. The thesis is
  discovery/locator level here, not full-text verified. No independent global
  priority search or Lean correspondence audit was performed.
- Could not rerun the manuscript-advertised `reproduce.py`; it is absent from
  `research/paper-novel/`. No changes were made outside this report.

Files changed: `research/paper-novel/review/AGENT_REPORT.md` only.
