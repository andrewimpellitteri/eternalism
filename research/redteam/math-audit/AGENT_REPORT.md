# Agent report: mathematics red team (complex percolation theorem drafts)

24 October 2026. Adversarial audit of the selected target's mathematics:
`research/creative/RESULT.md`, `research/creative/COVARIANT_RESULT.md`,
`research/creative/proof-audit/` (AUDIT.md, verify_small.py),
`research/creative/covariant-stopping/reduced_poscau_obstruction.py`,
`formal/lean/Certificate.lean`, `formal/INFEASIBILITY.md`, and the
correspondence to Dowker–Zalel arXiv:2212.01149v2 (HTML, fetched and read
first-hand this session).

## Verdict

The two-cap proof of the labelled theorem and the conditional covariant
classification survive all attacks. The linchpin identity, the two-cap
algebra, the divergence, and the DZ correspondence all check out; two
documentation-level defects were found (one fixed, one reported for the
owner). Nothing found undermines a theorem statement.

## Findings

1. **Countermodel N(H) mismatch (fixed).**
   `experiments/extensions/countermodel.py` set N(H_j) = 2^j = |Aut(H_j)|,
   contradicting COVARIANT_RESULT.md's own definition (N(H) = n!/|Aut|).
   Correct values: N(H_1) = 3, N(H_2) = 180. The conclusion (no common kappa
   for the Dirac measure under rule (T)) is robust under either convention:
   kappa would be 8/3 vs 1024/180 under the documented definition, 4 vs 64
   under the old one. Fixed; all prints now follow the documented definition.

2. **RESULT.md's W certificate is misdescribed (reported, not fixed).**
   RESULT.md: "enumerating the 40 naturally labelled principal five-element
   blocks and capping them gives W = 9/16 + 105/(128√2) = 1.1425… > 71/64."
   Forensics with exact Q(√2) arithmetic: the script's quantity is
   r5 = Σ over principal 5-orders of 2^(−(L+min+C(5,2)−R)/2) = 105/128 +
   9/(8√2) ≈ 1.6158 (exponent uses MINIMA; verified reproducing the script's
   exact value), and W = r5/√2. The literal readings disagree: capping the 40
   principal 5-blocks once gives exactly V_6 = 2.1841 (the doubly-principal
   6-causets); capping twice gives 1.5444 (the principal-G part of V_7).
   Neither equals W. The value matches the script; the description does not
   match the quantity. RESULT.md already demotes W ("the general proof above
   does not extrapolate from that enumeration"), so no theorem is touched,
   but the sentence should be corrected by whoever reconstructs the
   superseded block argument's intent.

3. **Linchpin identity extended (new verification).** RESULT.md's crux,
   Σ_G r^(L+M) s^(C(k,2)−R) = ∏_{j≤k}(1−s^j) over all labelled k-orders, was
   verified EXACTLY (Fractions) at k = 5 and k = 6 for (r,s) = (2/5,3/5),
   (3/4,1/4), (9/10,1/10) — two levels beyond verify_small.py's k ≤ 4.

4. **Divergence pushed past the certificate (new verification).** At
   p = (1+i)/2, exact values: V_7 = 809/256 + (29/16)√2 ≈ 5.7234 (two-cap sum
   over all 357 five-element orders, agreeing with brute-force enumeration of
   doubly-principal 7-causets in method-shape), V_8 ≈ 17.6880 (float). The
   two-cap lower bound V_{k+2} ≥ |p|·t^k·c_s holds at every k ≤ 6 for six
   adversarial parameters: (1+i)/2, 1.05, −0.5, (1+3i)/4, 1.5i, 0.9+0.4i.

5. **DZ correspondence audited first-hand.** Fetched arXiv:2212.01149v2 HTML
   (not previously in the repo as text; the local PDFs are other papers).
   Verified: Eq. 26 amplitude, Eq. 24 zeta, Eq. 25 minima, Eq. 29 posts
   algebra, doubly-principal = "principal whose restriction to [0,n−2] is
   principal" (exactly delete-last-label under natural labelling), Eqs. 30–31
   criteria, and DZ's explicit statement that the R̃_p extension question is
   inconclusive/open — confirming the claimed delta of RESULT.md. Also
   verified DZ's "ζ = |p|+|1−p|−1 on every doubly principal causet"
   numerically on the doubly-reduced tree at two complex p (via the repo's
   poscau, cross-check only).

6. **Hand-audit of the proof steps.** Two-cap decomposition (uses natural
   labelling: the last label of a principal causet is its unique maximum —
   matches AUDIT.md's note), cover/relation bookkeeping under capping,
   w+h ≥ k with equality for the chain (verified numerically for k ≤ 5),
   finite total variation of complex measures, disjointness of same-size
   labelled cylinders, the covariant theorem's laminar-family argument,
   the p = 0 and p = 1 endpoints, and the finite-cutoff product
   N(H)A_p(H)·∏(1−q^j) (transitivity through the post's future is what makes
   the j-th step 1−q^j). No gaps found. The Lean kernel
   (`Certificate.lean`) builds under the local toolchain; `#print axioms`
   reports the four checked theorems axiom-free.

## Method note (recorded for honesty)

The first version of the independent enumerator used in this audit was
wrong: it rejected transitive relations containing redundant comparable
pairs, i.e. it enumerated Hasse diagrams, not causets. It produced
contradictions with the repo's cross-checked exact values (V_5, V_6) and 17
false "attacks." The disagreement with two independent implementations was
itself the diagnostic. The corrected enumerator (mask + transitive closure,
deduplicated) repels all attacks. This is a live demonstration of why the
project's independent-reproduction standard exists.

## Files changed

- `experiments/extensions/countermodel.py` (finding 1; import of `factorial`
  added, `n_representatives` per the documented definition).

## Checks

- All attacks re-run after the enumerator fix: all repelled.
- `check_certificate.sh` green end-to-end after the countermodel change.
- 104 tests green.

## Limitations and unresolved questions

- V_9 would need 2^21 relation masks (orders on 7 labels): not attempted;
  divergence is illustrated through V_8 only.
- Finding 2 (W description) awaits the owner's correction; the exact numbers
  above are everything needed to write it.
- RESULT.md's W block also warrants a pointer from the superseded-proof note
  to the obstruction script's actual quantity (r5, minima-based exponent).
