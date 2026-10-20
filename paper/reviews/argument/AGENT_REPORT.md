# Independent argument review

Review target: `paper/main.tex`, with `READINESS.md`, `SOURCE_AUDIT.md`, and `research/redteam/paper-ledger/FREEZE.md` as scope controls. This is a philosophical-argument review, not a source-by-source verification. I made no manuscript or bibliography edits and used no external sources.

## Assessment

The manuscript is usable as a clearly provisional working argument. Its central distinction among incompatibility, likelihood discrimination, and representation equivalence is coherent; it repeatedly names bridge premises and operational scope. I found no formal error in the displayed exclusion inference, the fixed-package likelihood claim, the measure/kernel proposition, the finite Markov example, or the observational/intervention counterexample.

This is not yet a new research contribution, and the manuscript does not claim that it is. The finite proposition is elementary and conditional on the exact measure and response-kernel preservation that it concludes will preserve probabilities. The finite-history example is explicitly an implementation comparison, not an ontology model. The intervention example correctly demonstrates that observationally matched structural causal models can differ under `do(X=0)`, but it does not assign either model to a temporal ontology.

## Blockers for a stronger philosophical article

1. **Admissibility remains the least defended premise.** The paragraph at lines 131–148 proposes consistency, empirical adequacy, constitutive fidelity, a specified interface, and independent motivation for auxiliaries. The reply at lines 367–373 says standards should be symmetric, but does not yet explain how constitutive commitments are identified independently of the desired verdict, or how “ad hoc,” “explanatory contribution,” and “cost” are assessed without covertly privileging a package. This is a risk of circularity because admissibility controls which realizations survive before the comparison is made. It is correctly listed as unmet in `READINESS.md`; it blocks treating the burden-of-proof framework as a defended method, though not using this as an exploratory draft.

   Suggested revision before a stronger article: require each view's constitutive commitments and auxiliary degrees of freedom to be stated before examining the discriminator; apply one public criterion to all candidate packages; report which conclusions change under reasonable alternative admissibility profiles. Do not claim the criterion is neutral merely because it is symmetric.

2. **The “strongest objections” are broad families, not yet reconstructed arguments.** The replies to parsimony, phenomenology, and inaccessible ontology are careful, but some objections are phrased at a level where the answer is the manuscript's own method (“state the bridge,” “articulate the comparison”) rather than engagement with a strongest defender's premise. That is suitable for this draft, whose status and source ledger say so, but cannot support a source-complete claim that the major alternatives have been answered.

3. **The positive explanatory route is announced more than argued.** The article allows physics to favor an ontology through explanatory understanding (lines 46–79, 225–258, 367–390), but supplies no worked case where explanatory virtues support one package under an independently defended standard. The text appropriately presents this as open; a research article would need either a concrete argument or a narrower thesis limited to the inferential bookkeeping.

## Precise optional improvements

- In the exclusion subsection, keep the quantifiers explicit: `P` excludes the conjunction only given the displayed entailments; `P` excludes `O` only if every admissible realization of `O` entails the disputed bridge/auxiliary conditions or otherwise conflicts with `P`. The current prose already says this, so no correction is required.
- In the proposition, consider renaming “Record-preserving translation” to “Probability preservation under matched kernels.” The present title may suggest the proposition constructs a substantive translation, whereas `F`, pushforward equality, and matching kernels are hypotheses. The proof itself is valid and accurately says preservation is assumed.
- In the intervention example, make the structural equations explicit in a parenthetical: `A: Z~Bern(1/2), X:=Z, Y:=X`; `B: Z~Bern(1/2), X:=Z, Y:=Z`. This makes the intervention semantics transparent and pre-empts the reading that setting `X` also changes the shared exogenous variable.
- The finite-history explanation is sound under its stated protocol restriction. Keep the sentence excluding interventions that modify future transitions adjacent to it; that condition carries the crucial difference between passive prefix release and an interactive sequential generator.

## Scope and dissent

I agree with the readiness/freeze distinction: most formal and illustrative passages are safe as explicitly labelled working argument, while the Putnam/Stein, Brading, relational-dynamics, record-to-becoming, and contribution passages remain gated. I did not audit citations, prove the proposition independently beyond checking its displayed argument, reconstruct defender/critic literature, or make any novelty judgment. My dissent is limited to the strength of the current admissibility defense: symmetric wording alone does not yet establish non-circularity, although the manuscript candidly flags that work as incomplete.

## Final integrated-manuscript check

I reviewed the integrated `paper/main.tex` diff. The attribution at the Callender/Maudlin passage now marks the methodological caution as the authors' inference. The clock-rate sentence correctly separates metric constraints from a passage bridge. The added admissibility paragraph directly acknowledges that symmetry alone does not ensure neutrality and says alternative profiles and verdict sensitivity must be stated; it does not claim to have solved the normative defense. The Stein wording now distinguishes the isolated OCR implication, surrounding contextual conditions, and the still-unverified printed theorem, without alleging an error in Stein's paper. Renaming the proposition and identifying `Z` as exogenous remove the two clarity risks I noted. “Smooth Cauchy slicings” is appropriately narrower.

I found no introduced logical or quantifier error. The intervention example still has the stated behavior under `do(X=0)` because only the structural assignment for X is replaced; B's Y remains a function of the unchanged exogenous Z. The probability proposition's pushforward/kernel hypotheses remain sufficient for its conclusion and are accurately signaled by the new title. The manuscript remains a provisional argument draft, not a new result or a completed defense of admissibility. PDF/build and exact-check claims are coordinator-reported; I did not independently rerun them in this review.
