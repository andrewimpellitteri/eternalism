# Adversarial review of research/stein-gr/main.tex: everything except the proof of thm:main

Scope: items 1-9 of the brief. The proof of thm:main (Proofs, subsection 2) was not re-checked.
Read depth: main.tex full text. Quotations checked against the supplied text extracts (Clifton-Hogarth, Wuthrich-Callender, Viglione, Monton preprint, Choquet-Bruhat-Geroch, Minguzzi-Sanchez). Hawking-Ellis was NOT available, so the section number and exact hypotheses of its conservation theorem are unverified.

Verdict in one line: every result I checked is true or repairable. There is no fatal error. There are three substantive fixable problems (prop:nonlocal's (LC)-failure argument, thm:weyl's third claim, prop:dec's last sentence), one real overclaim (the causal-set "contrary to a published claim"), and a philosophical overreach ("unless they give up locality").

---

## 1. prop:single (one spacetime is not enough)

Checked: R = J^- U (J^-(x) x J^+(b)), i.e. (e,z) in P iff e <= x and b <= z.
- Reflexive: yes, from J^-. Contains I^-: yes. Relates x to b: yes.
- Transitive: the three mixed compositions land in J^- or P because <= is transitive. P o P needs z with b <= z <= x, so b <= x, which is impossible for spacelike x,b. Correct.
- Not I^-, J^-, U: (x,b) is in R but not in J^-. (b,x) is in neither J^- nor P, so R is not U. Correct.

Issues:
1. (presentational) "If M has no nontrivial isometries, R is invariant under all of them" is vacuous and conditional. The slogan "generic spacetimes have no symmetries" (abstract, intro) is used but not proved or cited. Cite a genericity result (e.g. Beig-Chrusciel type results for vacuum, or a standard statement for generic Lorentzian metrics) or say "there exist globally hyperbolic spacetimes with trivial isometry group, e.g. ...". Repair: one cited sentence.
2. (presentational) Line 195-197: "the dust-cosmology ordering by scalar curvature ... is a symmetric instance" is cryptic. An ordering by R is a local function of the point, so extended to all of GH it fails (CB) (in Minkowski R=0 is constant, so it gives U there). It is not an instance of Prop. single. Delete or explain.
3. (fixable, minor) The relation R is one spacetime, one pair, and depends on the choice of (x,b). That is fine for a counterexample, but the intro bullet "Stein-type uniqueness fails completely" should read "fails for spacetimes with trivial isometry group".

## 2. prop:nonlocal (cosmological time rule)

Well-defined on all of GH: yes. tau takes values in [0,infinity]. The dichotomy "tau finite everywhere or not" is a global but well-defined property. Reflexive and transitive in both branches: yes. (CB): yes. If x << b and tau(x) < infinity, concatenating a timelike curve of length d>0 from b to x with a past curve from x gives tau(b) >= tau(x)+d > tau(x). The orientation (x becomes for b iff tau(x) <= tau(b)) is right. Isometry invariance: yes. "Invariant under morphisms that are onto": true but it is only invariance under isomorphisms, i.e. under isometries, so the phrase is redundant. Say "isometries".

Main defect, (fixable, important): the proof of the (LC) violation is not self-contained.
- It goes through thm:main, so it inherits that theorem's off-shell premise and the other reviewer's findings. It is also circular as an illustration of why locality is needed.
- The "direct" argument offered ("tau depends on the entire causal past, so is not fixed by any causally convex neighbourhood") is a heuristic, not a proof. It does not exhibit a pair of spacetimes and a morphism.

Concrete repair, fully elementary: the Milne wedge I^+(0) is an open, causally convex subset of Minkowski and is globally hyperbolic (Cauchy surface a hyperboloid), so the inclusion is a morphism in GH. In Milne, tau(p) = sqrt(-p.p) is finite, so B_Milne is the tau-ordering and relates spacelike pairs (any spacelike pair with tau(x) < tau(b)). In Minkowski tau = infinity, so B_Mink = J^-. (LC) demands x B_Milne b iff x B_Mink b. This fails for a spacelike pair. This is a three-line counterexample independent of thm:main.

Smaller: "B relates spacelike pairs" holds in one direction per pair (tau(x) <= tau(b)), not both unless tau-values coincide. State it so.

## 3. thm:class (classification of the null-boundary freedom)

Forward direction: correct. B non-universal gives B_Mink != U, so thm:main(a) gives I^- <= B <= J^-, and B = I^- U (B n E^-). N inherits (LC) since J^- and I^- are preserved by causally convex isometric embeddings (a timelike curve in M' between image points lies in the image by convexity). (NC) is transitivity of B restricted to horismotic outputs. E^- = J^- \ I^- excludes the diagonal, which I^- (reflexive) contains, so there is no clash.

Converse: (NC) is sufficient for (T). I checked all cases.
- I^- o I^-: fine.
- I^- o N and N o I^-: by MS Prop 2.31(i) (p<<r<=q gives p<<q) the composite is chronological (or trivially diagonal).
- N o N: x<=y<=b gives x<=b. Either x<<b, so in I^-, or x in E^-(b), so by (NC) in N. x != b because x != y and causality of GH spacetimes. (LC) and (CB) are clear.
- Consistency with thm:flat: any LC N on Minkowski is Poincare-invariant, and the proper orthochronous Poincare group is transitive on null pairs, so N_Mink is empty or E^-. Consistent, so the converse does not contradict thm:flat.

Issues:
1. (presentational) The classification is a restatement ("any LC, (NC)-closed N works"), not an explicit parametrization. The abstract says "we classify it". That is fine as long as it is not read as a structure theorem. Add one sentence that (LC)+(NC) is the complete characterization and that thm:weyl is one instance.
2. (presentational) The MS 2.31(ii) quotation in the proof preamble ("q in E^+(p) or p<<q") is correct as given.

## 4. thm:weyl (Weyl-gated example)

Correct: N is contained in E^-. (NC) holds, because a concatenation of null segments between horismotic endpoints is an unbroken null pregeodesic (MS Thm 2.30(ii)), and it contains the Weyl point of the first segment. (LC) holds: a lightlike geodesic segment between points of a causally convex image is a causal curve with endpoints in the image, so it stays in the image, and isometries preserve the Weyl tensor. Minkowski gives N empty, hence B = I^-. Nowhere-vanishing Weyl gives B = J^-. The Schwarzschild exterior (Weyl = Riemann != 0 everywhere, Kretschmann 48M^2/r^6) is a valid example, and region I is globally hyperbolic (static with complete optical slice). Definitions with endpoints included are harmless.

Issues:
1. (fixable, real) Third claim, "strictly between I^- and J^- on spacetimes that are flat on a nonempty open set and curved elsewhere", is stated imprecisely and, as written, is not quite true.
   a. "Curved" must mean Weyl tensor nonzero. Conformally flat curved spacetimes (all FLRW) have N empty, so B = I^-. Require: Weyl vanishes on a nonempty open set V and is nonzero somewhere.
   b. The statement "horismotic pairs inside V are not in N" needs a causally convex V (the proof says "open causally convex V"; the theorem statement does not). Otherwise a pair x,b in V may be joined by a second, long null geodesic through the curved region (a cut-point/caustic configuration), and then (x,b) is in N because the definition says "some lightlike geodesic segment". Repair: "Weyl vanishes on a nonempty open causally convex set V and is nonzero somewhere" (small convex normal balls are causally convex, MS Remark 2.12 and section 2.3, so V exists whenever Weyl vanishes on any open set). Strictness: horismotic pairs in V exist, so B != J^-. Pairs on a short null segment through a point of nonzero Weyl inside a small causally convex normal ball exist, so B != I^-.
2. (fixable) The conformal-invariance citation, "(MS section 2.6)" for the Weyl tensor, is wrong in part. MS section 2.6 treats conformal invariance of lightlike (pre)geodesics only. A grep of MS finds no mention of the Weyl tensor. Conformal invariance of the (1,3) Weyl tensor is standard (e.g. Wald, Appendix D; Hawking-Ellis section 2.6). Fix the citation. In fact only vanishing of the Weyl tensor matters, and that is conformally invariant.
3. (fixable) Claim "determined by causal structure alone" (abstract and intro). What is proved is dependence only on the conformal class. To pass to "causal structure" one needs Malament / Hawking-King-McCarthy (causal automorphisms are conformal; for distinguishing spacetimes the causal relation determines the conformal class). Cite it, or write "conformal structure". Philosophically the relation is not definable from the abstract poset (M,<=) alone without reconstructing the manifold structure. Say so, since a causal-set reader will care.
4. (presentational) The gating by Weyl curvature is a "rule" nobody would propose as becoming. It is a possibility proof. A sentence saying so would stop an overreading. It also bears on Clifton-Hogarth's own pp.364-365 discussion: curvature-dependent coreality of null lines is a genuinely new option.

## 5. prop:reg (regularity)

Correct. B closed contains closure of I^-, which equals closure of J^- (MS Prop 2.17), hence J^- (J^- is contained in the closure of I^- in M x M: perturb q slightly to the future). With B <= J^- (non-universal), B = J^-. B\Delta open and inside J^\Delta gives B\Delta inside Int J^- = I^- (MS Prop 2.17, diagonal excluded). With (CB) and reflexivity, B = I^-. Presentational points:
- The reflexive-versus-strict convention for I^- (Framework: I^-, J^- reflexive; "We use I^+ open in MxM" uses strict) is inconsistent. State once that I^+ in the topological facts is the strict relation and that the diagonal is added back.
- "Topological regularity removes it" is OK, but philosophically closedness/openness is an additional premise on the becoming relation. It is not derived from anything. State as a premise (the abstract says "removes it", which is fine).
- The hypotheses are imposed for every M, but only Minkowski is needed to decide the endpoint choice via thm:main plus LC? No: to get B_M = J^-_M for all M one needs closedness in each M (or LC applied to a closed N type argument). The statement as given quantifies over all M, which is consistent.

## 6. prop:causets (causal sets)

Proof checked step by step and correct.
- {x,b} for incomparable x,b is convex: any chain u<=w<=v with u,v in {x,b} forces u=v, hence w=u. The antichain A is a locally finite poset, and both embeddings (a->x,a'->b) and the swap are morphisms. So the verdict is one symmetric bit beta. Yes.
- For x>b the interval [b,x] is finite and convex, so the verdict depends only on it. Yes.
- beta=1: in I u {z} (disjoint union, z incomparable to all of I) x B z and z B b by beta, so x B b by (T), and I embeds convexly, so x B b in I and hence everywhere. Valid, since all of I-disjoint-union-z is a locally finite poset. This gives universality.
- beta=0 and x B b for some x>b: adjoin e with e<y exactly for y>=x. M is convex in M' (nothing lies below e, so e cannot be an intermediate point of a chain with both ends in M). M' is locally finite ([e,y] = {e} u [x,y]). So x B b persists in M' (LC), e B x by (CB), and e B b by (T). But e and b are incomparable (b is not >= x and nothing is below e), contradicting beta=0. Valid. The one-element extension e<x is a legitimate causal set and [b,x] stays convex (indeed M does).
- If neither, B = the causal order by (CB). Correct.

Issues:
1. (fixable, real overclaim) Abstract: "contrary to a published claim that the analogue fails", and Section 6, "refutation". WC's claim (Wuthrich-Callender, section 3, "The analogue of this theorem, however, is straightforwardly false in CST") is about the analogue with automorphism invariance of a single causet, and that claim is TRUE on its own terms, as the paper's own Prop. single shows for the continuum. The paper proves a different, stronger-hypothesis statement (locality across all causal sets). It does not contradict WC. Verified details: the counterexample relation R in WC is exactly causal order plus {b,c},{c,b} on the diamond; R excludes <b,d>. WC's fn. 5 says "it could be a small proper part of a much larger causet" (verbatim correct). Also WC argue (pp. 8-9) the counterexample is non-generic (non-Hegelian subsets are rare in typical causets), a context the paper omits. Repair: replace "contrary to a published claim" with "the Wuthrich-Callender counterexample is not locally covariant"; say it shows exactly that automorphism-invariance within one causet is too weak, which WC also say.
2. (fixable) The claimed refutation sentence ("It is not the restriction of any becoming theory in the present sense: relating b to c fixes beta=1 ... relates b to d") is correct. Add the one-line reason {b,c} is convex in the diamond (so the verdict on it is the antichain's).
3. (presentational but significant) The category CS contains disconnected and wildly non-manifoldlike posets (antichains, I u {z}). The proof uses them essentially. This is the causal-set counterpart of the off-shell premise (rem:offshell) and should be flagged. If morphisms/objects are restricted to manifold-like causets (sprinklings of globally hyperbolic spacetimes), the proof is not available without checking that I u {z} and M u {e} remain manifold-like, and the sprinkling probability of such things is the physically relevant question. Say so in the Limits paragraph.
4. (presentational) "Discreteness removes the light-cone freedom" is fine but better: there is no lightlike/chronological distinction in a causal set.

## 7. prop:godel (totally vicious spacetimes) and Godel's modal step

Math: "every morphism into a totally vicious M is onto" is true; MS Remark 2.12 only says such spacetimes exist where the only nonempty open causally convex subset is M itself (it points to Sect 3.1), so the cited remark does not prove the statement. Give the three-line proof: take p in image U, closed timelike loop through p and any q (I^+(p) = I^-(p) = M by MS Def 3.2(ii)), choose a, b in U on the loop just after and just before p, and apply causal convexity of U to the causal sub-arc a->q->b. Then q in U. B_M = U_M follows from I^-(p) = M and (CB). Correct.

Issues:
1. (fixable) "Gödel-type universes are isolated" is only proved for morphisms INTO a totally vicious M. Morphisms OUT of a totally vicious M into a larger M' are not excluded by the proof. They are excluded for the Godel metric, because it is geodesically complete and hence inextendible (so an open isometric image in a connected M' is all of M'), but not for general totally vicious spacetimes: a non-complete totally vicious M may sit as an open, causally convex chronology-violating region of a bigger spacetime (Misner-like). In that case locality does transmit constraints. Repair: state the isolation claim for inextendible (or complete) totally vicious spacetimes, or prove no outgoing morphisms in general.
2. (fixable) Extended category: the proposition extends GH to all spacetimes, but thm:main and everything else are for GH. State explicitly that a theory on the extended category restricts to GH, and that the converse (extension of a GH theory by "U on totally vicious") needs checking of the outgoing morphisms in item 1.
3. (fixable, philosophical) "Gödel's modal step ... therefore needs a link between universes stronger than locality" conflates two things. Gödel's step (pp.561-562, checked in Monton's section 6) is about lawlike compossibility: if lapse exists in our world then whether it exists "depends on the particular way in which matter and its motion are arranged", which Gödel finds unsatisfactory. Monton's rejoinder is that the premise "the Gödel universe is physically possible" is doubtful. Locality in the (LC) sense is neither Gödel's premise nor the thing Monton denies. The paper's observation (LC transmits nothing from Godel to us) is correct and interesting, but it should be presented as "(LC) gives no way to run Godel's inference", not as a diagnosis of the modal step. Also "this is Gödel's first step, in Stein's terms" is an interpretive translation: Godel's first step is the absence of a global time function / foliation, and identifying that with "universal becoming" is a gloss.
4. (presentational) Prop nonlocal: "shows what such links look like" is unsupported; the cosmological-time rule is not a link between Godel and our universe (on Godel tau = infinity and B = J^- = U anyway).
5. (overclaim in abstract) "so that universal becoming there constrains nothing here" is true only in the formal sense above and only for the isolated case.

## 8. sec:energy

prop:dec. Structure: if M is DEC and flat on a nbhd of a Cauchy surface S, then M is flat.
- The hypothesis (DEC of the Einstein tensor G, which is divergence-free by Bianchi) is exactly what the Hawking-Ellis conservation theorem needs, with no field equation. G = 0 on S (indeed on a neighbourhood), so G = 0 on D(S) = M. Because the flat region is a NEIGHBOURHOOD, even the interior version of the theorem suffices. I could not check HE: section "4.3" and the closed-achronal hypothesis are plausible but unverified; the standard statement is Prop. 4.3.1. Verify and cite by proposition number.
- G = 0 only gives Ricci-flat, not flat. The paper then argues with CBG Theorem 3. Checked in the text: CBG Theorem 3 says there exists a development M of the initial data that is an extension of every other development, unique up to isometry. That gives embedding of M into the maximal development MD of its data. It does NOT by itself say MD is flat or Minkowski.
  - (fixable) Final sentence "which is Minkowski spacetime" is false in general: flat data on R x T^3 has a flat, non-Minkowski maximal development. It is true for M' of the paper (Cauchy slice R^3 with the Euclidean hyperplane data, K=0, whose maximal development is Minkowski, since Minkowski is geodesically complete hence inextendible, so it equals MD). So the "In particular" part about M' is fine, but the general statement M is flat is not established by CBG as cited.
  - Clean repair: "M is vacuum; the Riemann tensor satisfies the linear homogeneous tensor wave equation Box R = R*R (Bianchi plus Einstein = 0), vanishes with its derivative on a neighbourhood of S, so by uniqueness for linear hyperbolic equations (domain of dependence) it vanishes on D(S) = M". CBG is then unnecessary. Alternatively cite the geometric uniqueness theorem plus the fact that a flat development exists locally.
- "In particular M' is in GH_DEC only if g is flat on T_{2r}": follows once M' flat, since g' = Phi^*g on T_{2r}. Correct.

pocket discussion.
- (fixable) "so no pocket can be inserted" is a corollary of geometric uniqueness (a development is determined by data), not of the conservation theorem alone, and holds only when the whole causal past of the pocket on a Cauchy surface is vacuum and unmodified. State it as such.
- (overclaim) Abstract and intro: "the transfer reduces to an open gluing problem". The pocket problem is a SUFFICIENT condition for a verbatim proof, not equivalent to the transfer. Theorem could hold or fail in GH_DEC for other reasons. Rewrite: "sufficient condition". Also no claim that thm:main FAILS in GH_DEC is made or proved; say so explicitly.
- (overclaim, unverified) "existing gluing theorems do not provide" bounded flat regions adjacent to arbitrary curved vacuum regions. I could not audit the gluing literature (Corvino, Corvino-Schoen, Chrusciel-Delay, Chrusciel-Isenberg-Pollack, Carlotto-Schoen, Czimek-Rodnianski). Some of those do produce data that is exactly flat or Kerr on large regions. Reword to "we have not found" and add the caveat that this is a literature claim not audited at full-text depth, or cite the specific theorems and the exact reason they fall short (hypotheses on asymptotic ends, KID obstructions).
- Vaidya claim is plausible (ingoing Vaidya with m'>=0 satisfies DEC; flat before the shell). They are not globally hyperbolic complete models near the centre, so "explicit models exist" should be stated as models of the local configuration only.
- "closed under restriction to causally convex open subsets": true (and such subsets are globally hyperbolic since diamonds are compact).

## 9. Introduction, abstract and sec:phil

Quotations and locators (checked against ch1995.txt, wc.txt, v.txt, Monton):
- CH p.385 "each general relativistic spacetime ... much less to extend Theorem 2": verbatim and on p.385 (header "385" precedes it). OK.
- CH p.386 "more difficult, though more interesting": verbatim ("the more difficult, though more interesting, question"), on p.386. OK.
- CH p.360 reflexive convention, p.364 Lemma, p.365 Thm 1, pp.365-367 proof, pp.385-386 reflections, pp.364-365 causal-versus-chronological discussion: all verified.
- CH Theorem 1 as stated assumes definability from time-oriented metrical relations (includes reflections). The paper's note that the proof uses only rotations, boosts, translations is verified against the proof text (p.366). OK.
- WC section 3 quotation and fn.5 quotation: verbatim and located correctly. See item 6.1 for the misuse.
- Gödel pp.561-562 "as quoted in Monton section 6": Monton quotes the question at 561-2 and the modal step at 562. OK.
- MS locators: Prop 2.10, 2.16, 2.17, 2.31, Thm 2.30, Def 3.63, Thm 3.75 exist and say what is used. Remark 2.12 does not state the totally-vicious claim as a result (see 7). The Weyl citation to section 2.6 is wrong (see 4.2).
- CBG Theorem 3: exists and is as described, but see 8 on what it gives.

Overclaims and unfairness:
1. (fixable) Abstract/intro: "Stein proved ... must be the causal past, the chronological past, or the universal relation." The trichotomy is Clifton-Hogarth's. Stein's own theorem (as WC describe it) delivers the causal past. Intro paragraph attributes correctly; abstract should too.
2. (fixable) Intro: "(LC) is a precise version of the locality intuition that Viglione defends informally". Viglione's Causal Connection Condition says a temporal relation is absolute only if it obtains independently of the occurrence of any distinct causally disconnected event. That is a different, stronger principle: (LC) allows dependence on all events in a causally convex region, including events spacelike to both relata. Say "related to" and note the difference. Section 5 repeats "expresses".
3. (fixable, substantive philosophical) Section 5, "unless they give up locality" (and "Rejecting locality is a coherent option, but it is the option of global, cosmological becoming"): false dichotomy. A preferred foliation or cosmic time can be made local by enlarging the structure: take the category of globally hyperbolic spacetimes with a time function (or a foliation) as extra structure and morphisms preserving it. Then "tau(x) <= tau(b)" is locally covariant with respect to that category and satisfies (T), (CB). This is the standard route (Clifton-Hogarth note the preferred-frame option). The theorem shows that becoming cannot be defined from metric structure alone under (LC) and (CB),(T); it does not force locality to be abandoned. One may also drop (T) or (CB), or restrict the class of spacetimes. Rewrite as: becoming defined from the Lorentzian structure alone must be one of the three options unless extra structure is added.
4. (fixable) Section 5 "Limits": premises that carry the "robust part" and are listed incompletely. Missing: (CB), (T) themselves (CH concede transitivity "could be disputed"); the absolute, worldline-independent form; the off-shell universality (listed); the choice of a category (a fully naturality-based one). The statement "this holds in every globally hyperbolic spacetime, however asymmetric, and does not rely on any foliation" is correct as a corollary of thm:main only if thm:main is correct and only for becoming theories defined on all of GH.
5. (presentational) Intro bullet "Energy conditions ... the key construction is provably unavailable" is accurate for the specific M' only; rephrase "the construction used in the proof".
6. (presentational) Note-on-method claims "Quotations were checked against the primary texts". True for CH and WC (checked here), partial for Gödel (quoted via Monton), and not applicable to HE (unchecked here). Make the Gödel dependence explicit (already done).
7. (presentational) "Stein's theorem is the strongest positive result in the debate" is a value judgement; soften.

## Summary table

| Item | Result | Severity | Repair |
|---|---|---|---|
| prop:single | Correct | none | cite genericity; drop dust-cosmology remark |
| prop:nonlocal (CB, T, invariance) | Correct | none | |
| prop:nonlocal ((LC) failure argument) | Heuristic / circular | fixable | Milne inside Minkowski |
| thm:class both directions | Correct | none | (note it is a characterization) |
| thm:weyl claims 1,2 | Correct | none | |
| thm:weyl claim 3 and Weyl citation, "causal structure" | Imprecise | fixable | Weyl nonzero somewhere, V causally convex; fix MS citation; cite Malament/HKM |
| prop:reg | Correct | presentational | convention consistency |
| prop:causets | Correct | none | flag non-manifoldlike objects |
| WC "refutation" / "contrary to a published claim" | Overclaim | fixable | reword |
| prop:godel math | Correct for morphisms into M | fixable | prove convexity step; handle outgoing morphisms or restrict to inextendible |
| Godel modal step gloss | Mismatch with Gödel/Monton | fixable | reframe |
| prop:dec statement | Correct | none | |
| prop:dec proof ending ("Minkowski") | Wrong in general | fixable | use wave equation for Riemann |
| pocket/gluing claims | Unaudited literature claim; "reduces to" | fixable | "sufficient"; hedge |
| "unless they give up locality" | False dichotomy | fixable | extra-structure category |
| Viglione "precise version" | Overstated | fixable | "related to" |
| Abstract attribution of trichotomy to Stein | Misattribution | presentational | |
