# Verification of draft 2 ("Unreal Is Not Open") against MATH_REVIEW.md and PHIL_REVIEW.md

Read depth: main.tex full-text, both reports full-text, mathematics re-derived by me. Citations checked
by arXiv abstract pages (abstract depth) and a web search (discovery depth). Section numbering note: the
logic section is Section 5 and the conclusion Section 6 in draft 2; "Section 6" in the request is read as the logic section.

## 1. Status of each referee item

Legend: FIXED / PARTLY / NOT / N/A (section or claim removed).

### MATH_REVIEW.md
- M1 Cauchy corollary: FIXED. Corollary (cauchy) now has the general-Cauchy-surface proof (lines 152-157), as recommended.
- M2 Prop (ds): N/A, removed with Section 5.
- M3 BGV remark: N/A, BGV no longer mentioned. No replacement conditional claim about inflation made.
- S1 ".2 on a sub-domain": FIXED. The text now says .2 fails on every generated subframe and only particular pair instances are repaired (lines 288-299). It does not define the "U is confluent in M" relativized condition, but nothing now needs it.
- S2 horizon problem = failure of .2: FIXED (lines 293-297: "is therefore not the failure of .2"). Abstract no longer says it.
- S3 inequality wording: PARTLY. Inequality is right (see 2). Wording is still "have no common past unless ...", about the extremal pair; "all such pairs have a common past iff eta_0 < 2 eta_ls" (eta_- = 0) would be cleaner. Optional inflation bound not added.
- S4 generalize to S^3/H^3 or say flat: FIXED by restriction: the common-past criterion is stated for R^3 only (line 288), and the abstract no longer claims .2 fails.
- S5 eta_+ = infinity: FIXED for the criterion (arbitrary eta_+). NEW problem: line 301-302 says "common futures, which these models have". Only true for eta_+ = infinity (or small separation). For finite eta_+ (LCDM, which the paper uses as motivation) far pairs have no common future. Qualify.
- S6 t onto: PARTLY. Definition of Cauchy time function (lines 85-88) gives t: M -> (alpha,beta) but never says t is onto, so S_c could be empty and the "if" direction would be vacuous for such c. Add "onto (alpha,beta)". Finite alpha is handled correctly (see 2). Independence of the choice of t is not stated, but not needed as the statement is for any t.
- S7 relation to Geroch P(b): FIXED (lines 113-120: "causal-curve analogue of the union of P(b) with events whose pasts lie in that of b; differ at most on null boundaries"). Acceptable; the "at most on null boundaries" is asserted, not proved.
- S8 known dust threshold / cite: FIXED (lines 215-226, Gron-Johannesen, Bolotin-Tanatarov, Geroch Fig. 5). Residual: the cited pages are at abstract depth only; the G-J abstract does not mention the max-expansion disappearance of the horizon, nor does the B-T one. The paper says "is known [..]"; this is plausible but unverified here.
- S9 "only there" conditional: N/A (Section 5 removed).
- S10 settled vs real with J^-: FIXED enough (lines 108-110, 238).
- S11 half of de Sitter: N/A.
- O1 parenthetical: FIXED/harmless. O2: fine. O3, O8, O10: N/A. O4: NOT (DoD-to-domain-of-dependence link not spelled out; optional). O5: FIXED (BdRV cited). O6: NOT (no MS2008 locators; optional). O7: PARTLY (Manchak claim worded "requires a compact Cauchy surface"; Hogarth 1993 not cited; sentence "only spatially closed models can cross the threshold" rests on Manchak and was not independently checked). O9: FIXED (H^3 included).

### PHIL_REVIEW.md
- 1.1 determinism vs settledness (MUST): FIXED. Renamed "determined from", "nomologically settled" only under DoD laws (Remark, lines 98-111).
- 1.1 collision with Belnap (MUST): FIXED, Belnap1992 cited and distinguished (line 103-107). Citation looks right (Synthese 92, 385-434).
- 1.1 informational openness (SHOULD): FIXED (lines 263-268).
- 1.2 oversell "closing of the future": FIXED (abstract and "Second" limit).
- 1.3 cite Rakic / weaken "new reading": FIXED (intro, Section 4). "Settled" conjunction with Earman/Hogarth: not cited, no novelty claim in abstract: acceptable.
- 1.3 I^- vs J^-: FIXED (lines 108-110).
- 1.3 Theorem for arbitrary Cauchy time function: FIXED (see 2), except the missing "onto".
- 2.1 atoms/object language/persistence (MUST): FIXED (lines 277-281, 299-303).
- 2.1 cite Fine, Lipman (MUST): FIXED.
- 2.1 "S4 exactly": FIXED (lines 305-307 leave it open).
- 2.1 Lewis/van der Schaaf authors: FIXED (arXiv confirms Marco Lewis, Nesta van der Schaaf). Bib key still vdSchaaf2026; EPTCS 447, 584-602 (AiML 2026) not added.
- 2.2 horizon relabelling: FIXED (demoted to remark; acknowledges both sides). Singularity-as-boundary caveat: NOT addressed (the criterion treats the big bang as no standpoint; unsaid). S^3 extension: not stated (optional).
- 2.3 "histories with no common origin": FIXED (deleted).
- Section 5 (3.1-3.5, all MUST items): N/A, removed as intended. Check that no residue remains: abstract, intro, conclusion contain no "shadow", "only there", "half", "grounding". Clean.
- Overclaim list (section 5 of the review): abstract qualifies closed dust, DoD, no "only there"/"half". Conclusion: "computable from conformal diagrams" (line 315) still unqualified for non-conformally-static models (the propositions cover only the product forms); PARTLY.

## 2. Mathematics re-check

- Theorem (char), alpha finite: CORRECT. (=>) negation gives K_c nonempty for all c in (alpha,t(x)); K_c compact (closed in compact J^-(x) cap S_c, since Is(b) open). P_n nonempty: choose y in K_{c_n}, causal curve x to y, t strictly monotone so it crosses each S_{c_i}, z_i not in Is(b) by push-up (y <= z_i << b would give y << b). Inverse limit of nonempty compact Hausdorff spaces nonempty. Each segment (and the initial segment from x to z_1) avoids Is(b) by push-up. The concatenation has t -> alpha, so a past endpoint p would need t(p) = alpha, impossible since t(p) in (alpha,beta). Nothing needs alpha = -infinity. Needs only that every S_c, c in (alpha,t(x)), is nonempty, i.e. t onto (flag above). Conformal time eta in (0,eta_+) is a valid Cauchy time function (complete Sigma).
- Corollary (cauchy) new proof: CORRECT. M = Is(S) cup S cup I+(S); first case by push-up (x = s gives s << b directly); second case: extension to an inextendible curve meets S; a meeting point to the future of x would give s' << x <= s, contradicting achronality; so the meeting point lies on the past-inextendible part and in Is(b). (Variable naming s, s' is slightly sloppy but fine.)
- Lemma (balls) with H^3: CORRECT. H^3 is complete with unique minimizing geodesics extendable indefinitely, so the extended geodesic endpoint lies at distance d + r_1 from Y and r_1 from X. S^3 cases (d + r_1 <= pi, > pi, X=Y, d = pi, r_1 >= pi) checked. r_2 <= 0 (empty ball) is consistent. Statement says r_2 <= pi only for S^3, which is what the text needs.
- Proposition (conformal) with H^3: CORRECT. x << b iff d < Delta eta holds in the static product with complete Sigma (and Delta eta < pi on S^3 since eta_+ - eta_- <= pi with open interval); J^-(x) cap S_c is the closed ball, Is(b) cap S_c the open ball; inclusion iff d + (eta_x - c) < eta_b - c. Open FLRW (a ~ sinh eta, cosh eta - 1) is conformal to (0,eta_+) x H^3. S^3 range <= pi covers closed radiation (0,pi) and global de Sitter (-pi/2,pi/2). The spatially flat claim includes finite eta_+ (LCDM): fine. Note: the abstract and prose text "spatially flat and open big-bang universes" is a corollary for any (eta_-,eta_+), including no big bang; fine.
- Proposition (dust): CORRECT, including threshold exactly eta_b = eta_- + pi giving Det = Is, Einstein static giving M. Closed dust threshold at eta = pi (a = (a_m/2)(1 - cos eta)). Caution: it applies to any closed model whose conformal range exceeds pi (e.g. closed with Lambda), not only dust; the text does not say otherwise.
- Common-past criterion: CORRECT for R^3: z <= x, y exists iff closed balls of radius eta_x - c and eta_y - c about X, Y meet for some c > eta_-, i.e. |X-Y| <= eta_x + eta_y - 2c, the sup over c not attained, hence strict inequality with eta_-. Directedness failure at every b when eta_- is finite follows (pairs at time eta_- + eps with separation 2(eta_b - eta_- - eps) exceed 2 eps). Holds trivially if eta_- = -infinity.
- Last-scattering inequality: CORRECT. Our past cone meets eta_ls in a closed ball of radius eta_0 - eta_ls, extreme separation 2(eta_0 - eta_ls); common past iff separation < 2(eta_ls - eta_-); hence eta_0 - eta_ls < eta_ls - eta_-. Fails without inflation (eta_-=0) with eta_0/eta_ls of order 50 (my recollection, not sourced). "unless ... holds with enough of it" is right if inflation lowers eta_-. Correct only for the flat conformal form (stated).
- Section 4 statement 2 (no event's past contains a Cauchy surface in flat/open/radiation/dS): follows from Proposition (conformal) and Corollary: if Is(b) contained a Cauchy surface then Det = M, but Det = Is != M.

## 3. New overclaims and citations

Overclaims / unsupported:
1. Line 301-302 "common futures, which these models have": false for finite eta_+ (see S5 above). Qualify to eta_+ = infinity.
2. Intro lines 63-64 "growing-block theorists who are determinists hold that the future is unreal yet fixed [Broad1923]": attributing determinism to Broad's Scientific Thought is not supported by anything in the paper, and I did not verify it in Broad. Reword ("a determinist growing-block position is available, cf. Broad") or drop the cite.
3. Intro line 64-66 Rakic's sea-fight characterization ("an event outside an observer's past that a decision inside it appears to settle"), and Section 4 "her sea-fight is, at most, settled from the observer, not real from her": I did not check the Rakic paper (BJPS 48 (1997) 257-280, locators fine); interpretive claim, flag as unverified.
4. Line 225-226 "only spatially closed models can cross the threshold": rests on Manchak; Prop (dust) shows only a sufficient closed-model mechanism. Safe wording: "consistent with Manchak".
5. Line 315 "computable from conformal diagrams" holds for the product-form models proved, not generally.
6. Lewis & van der Schaaf are described as studying "causal modal logics ... in the future direction" (line 303-304). The arXiv abstract speaks of chronological, causal and "after" relations; "future direction" is not in the abstract. Verify or soften.

Citations:
- Gron & Johannesen, EPJ Plus 126:30 (2011), arXiv:1103.4753: CORRECT (title "III: Universe models with positive spatial curvature" matches). Abstract does not mention the max-expansion horizon fact explicitly.
- Bolotin & Tanatarov arXiv:1310.6329: exists, "A Thousand Problems in Cosmology: Horizons". Correct as an arXiv preprint; no journal ref; the specific claim not verified.
- Lewis & van der Schaaf arXiv:2601.14029v2: authors, title and v2 correct. Missing Proc. AiML 2026, EPTCS 447, pp. 584-602.
- Lipman 2023 J. Phil. 120, 117-138: CORRECT (Martin A. Lipman, "Standpoints: A Study of a Metaphysical Picture", 120(3)). Add the first name to bib if desired.
- Broad 1923 Scientific Thought (Kegan Paul): bibliographically correct (Kegan Paul, Trench, Trubner, London); see overclaim 2.
- Belnap 1992 Synthese 92:385-434 and Goldblatt 1980 Studia Logica 39:219-236: match.

## Remaining must-fix
None blocking mathematically. Recommended before circulation: (a) add "onto" to the Cauchy-time-function definition; (b) qualify "common futures" for finite eta_+; (c) fix the Broad determinism attribution; (d) soften the Lewis-vdS "future direction" and the Rakic sea-fight sentence unless verified.
