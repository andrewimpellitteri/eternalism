# Finite openness: the open future as a finite resource (claim contract — negative on physics, residual corollary only)

10 November 2026. GLM headless worker (longshot lane), per the brief. Checked only by
the session that wrote it. Prior work first: the primary sources below were fetched and
read at the stated depths. No temporal ontology is selected. Sources:
[sources.jsonl](sources.jsonl). Numbers: [check_horizons.py](check_horizons.py).
Inputs: `research/time-direction/fixing-exchange/RESULT.md` and
`research/time-direction/clock-content/CLAIM_CONTRACT.md` (read).

**Verdict up front.** The geometric core of the idea — an observer's past light cone
converges to a fixed comoving region of radius ≈ 63 Gly, of which ≈ 40 % is already
visible — is already in the literature, with the headline volume number published as
such (Gott et al. 2005: factor 2.36). Loeb (2002), Davis & Lineweaver (2004) and
Krauss & Scherrer (2007) state the convergence, the freezing of source images, and the
shrinking reachable set, with no ontological comment. The ontological consequence
(saturating standpoint-relative block, "openness as a finite budget") was not found
anywhere, but the strongest objection (§5) blocks it: comoving volume is not
information, signals from inside the reachable ball keep arriving forever, and the
finitude holds for one conventional measure only. Do not open a paper lane on this as
stated.

## 1. Exact question and proposed statement

Session claim (brief): with Ω_m = 0.315, h = 0.674, flat, the particle horizon is now
46.1 Gly, the ultimate particle horizon 62.8 Gly; ≈ 40 % of the ultimately visible
comoving volume is already in our past cone, and 4.7 % of the presently visible volume
lies inside our event horizon. Proposed idea: in ΛCDM the total that can ever enter one
observer's past is finite, so openness is a finite resource per standpoint.

**Verified (this run).** Standard integrals, flat ΛCDM, Simpson with singularity-free
substitutions (script output; two independent routes agree to 6.8×10⁻¹⁵ relative):

| Quantity | value (Ω_r = 9.2×10⁻⁵) | matter-only | session claim |
|---|---|---|---|
| particle horizon now χ_p(t₀) | 46.13 Gly | 47.01 Gly | 46.1 ✓ |
| event horizon now χ_eh(t₀) | 16.68 Gly | 16.68 Gly | — |
| ultimate particle horizon χ_∞ = χ_p + χ_eh | 62.81 Gly | 63.68 Gly | 62.8 ✓ |
| (χ_p/χ_∞)³ | 39.6 % | 40.2 % | ≈40 % ✓ |
| (χ_eh/χ_p)³ | 4.73 % | 4.47 % | 4.7 % ✓ |
| age t₀ (anchor) | 13.797 Gyr | — | ~13.8 ✓ |
| z_eh (light emitted now never arrives) | 1.87 | 1.87 | — (cf. §2) |

The session numbers reproduce exactly when radiation is included; the fractions are
robust at the claimed precision under both treatments. Convergence identity used: the
union of an observer's past cones is bounded in comoving coordinates because
∫₀^∞ dt/a(t) converges as Λ dominates; χ_∞ = χ_p(t₀) + χ_eh(t₀).

## 2. Three nearest predecessors (assumption / result level)

**P1 — Gott, Jurić et al. 2005, "A Map of the Universe"** (arXiv:astro-ph/0310571,
horizon sections + abstract read; exact quotes): "we will eventually ever be able to
see out to a co-moving distance of r_{t=∞} = 4.50 R_{H₀} = 19,000 Mpc … This is the
co-moving future visibility limit. No matter how long we wait, we will not be able to
see further than this." And: "The number of galaxies we will eventually ever be able to
see is only larger than number observable today by a factor of (r_{t=∞}/r_{t₀})³ =
2.36." Also the reachability limit 4,740 Mpc ↔ z = 1.69 ("Galaxies with redshifts
larger than 1.69 today are unreachable"). Assumptions: flat ΛCDM with w = −1 persisting
(they discuss vacuum decay and note late decay "will make a negligible correction").
Results: the same 62.9-Gly sphere at H₀ = 70, the same ≈ 42 % volume budget (1/2.36),
the same event-horizon redshift. No temporal ontology anywhere in the passages read.

**P2 — Davis & Lineweaver 2004, "Expanding Confusion"** (arXiv:astro-ph/0310808,
abstract, Secs. 1–3, Fig. 1 caption, App. B samples read): "The particle horizon is the
distance light can have travelled from t = 0 to a given time t (Eq. 27), whereas the
event horizon is the distance light can travel from a given time t to t = ∞ (Eq. 28)";
"Our past light cone approaches the cosmological event horizon as t₀ → ∞ (Eqs. 22 and
28)"; "galaxies with redshift z ∼ 1.8 are currently crossing our event horizon. These
are the most distant objects from which we will ever be able to receive information
about the present day"; Fig. 1 caption: "Our event horizon is our past light cone at
the end of time, t = ∞." This is precisely the convergence statement, as pedagogy.
Recomputing with their parameters (Ω_m = 0.3, Ω_Λ = 0.7, H₀ = 70) reproduces their
46-Glyr particle horizon anchor. No volume budget, no ontology.

**P3 — Ellis's evolving block universe line** (Ellis 2015 abstract; Deng 2017 abstract
+ excerpts; Earman 2008 as reported there): "spacetime should be regarded as an
evolving block universe, bounded to the future by the present time, which continually
extends to the future", with the future boundary defined by proper time along Ricci
eigenlines — a standpoint-relative becoming, but never tied to Λ, horizons, or any
saturation; Deng shows the view's growth claims need perspectival truth without
resolving it. No cosmological-constant consequence in anything read or found.

Supporting, not nearest: **Loeb 2002** (PRD 65, 047301; abstract, Sec. I, start of II
read): "an asymptotically de Sitter universe of this type possesses a moving light cone
out of which all distant sources will eventually exit"; "the event horizon asymptotes
to a fixed proper distance from us"; a source image "freezes on a particular time
frame" while luminosity distance and redshift "continue to increase exponentially". **
Krauss & Scherrer 2007** (arXiv:0704.0221, intro + CMB passages read): structures
outside the Local Group are "driven outside of the de Sitter event horizon in a
timescale on the order of 100 billion years"; "objects will not be observed to cross
the event horizon, light from them will be exponentially redshifted"; a far-future
observer "will see a single galaxy" — the "end of cosmology". Both draw epistemic and
observational consequences only.

## 3. What changes relative to these predecessors, and why it would matter

The proposed change was: draw the ontological consequence (standpoint-relative growing
block that saturates; openness as a finite budget). What the search showed: the
geometry is published including the volume budget (P1), and no ontology paper connects
Λ-driven horizon convergence to becoming. The change therefore reduces to one
philosophical posit — becoming indexed to causal access of a standpoint — plus the
published geometry. Searches that would have defeated the geometry-novelty claim were
run and did defeat it (§5). What remains is a corollary, not a theory.

## 4. Smallest reproducible example and independent check

`check_horizons.py` (stdlib only): Simpson on the substitutions a = x² and a = 1/x,
which remove the a^{−1/2} singularity; printed table above. Internal independent
routes: z-space integral vs a-space integral (agree to 6.8×10⁻¹⁵); resolution 2¹⁴ vs
2¹⁶ (5.9×10⁻¹⁵); anchors: age 13.797 Gyr, D&L's 46-Glyr particle horizon reproduced
under their parameters, z_eh = 1.87 against D&L's "z ∼ 1.8" and Gott's z = 1.69
(parameter differences, not discrepancies: χ_eh/cH₀ = 1.1497 here, 1.12 in Gott's
WMMAP-era parameters). Independent verification route for a reviewer: recompute the
same integrals in closed form (the flat ΛCDM horizon integrals reduce to hypergeometric
functions) or with astropy `FlatLambdaCDM` (not installed here; no installs allowed).

## 5. What would show the idea wrong, trivial, already known, or physically irrelevant

- **Already known (triggered).** The volume-budget statement is published: Gott et
  al.'s factor 2.36 *is* the session's "about 40 %". The convergence is D&L's one-line
  statement. The freezing images are Loeb's abstract. Arithmetic and geometric novelty:
  none.
- **Wrong.** Any measured w ≠ −1 or vacuum decay removes the saturation (Gott et al.
  state this caveat themselves); a universe without Λ has no such limit.
- **Trivial.** The convergence is textbook FLRW horizon kinematics (Rindler-lineage;
  D&L App. B collects sixty years of it). "A standpoint's causal past is bounded in de
  Sitter" needs no new machinery.
- **Physically irrelevant (strongest objection, confirmed).** (i) Comoving volume is
  not information: for any source strictly inside the event-horizon ball, emission and
  reception continue forever; images of sources near the horizon freeze and fade while
  "luminosity distance and redshift continue to increase exponentially" (Loeb), and
  "objects will not be observed to cross the event horizon" (Krauss & Scherrer). (ii)
  Horizon-scale quantum effects keep arriving: the de Sitter horizon carries
  thermodynamics and radiation, and semiclassical analyses must *choose* to neglect
  horizon-hidden information (Markkanen 2018, abstract); quantum gravity even proposes
  a finite entropy budget per observer (Huang 2026, abstract) — a different, already
  occupied sense of "finite budget". (iii) The measure is conventional: the comoving
  slice-volume is finite, but the proper volume of the ultimate ball, and the spacetime
  4-volume of the union of past cones (integrand ~ a³ ∝ e^{3Ht}), diverge. A "budget
  of openness" claim must name its measure; on the three natural measures (comoving
  volume, arriving signals, information) finiteness holds on exactly one.
- **Standpoint-relativity is empirically marginal (our note).** Two comoving observers
  at separation d have ultimate balls whose visible-volume difference is O((d/χ_∞)²) —
  ≈ 10⁻⁹ for a 1-Mpc separation — so the standpoint-relative saturation is true in
  principle and negligible for any real pair of observers.
- **Defeating searches run this run** (exa + OpenAlex via scholar_search): "growing
  block"/"event horizon"/"cosmological constant"; "evolving block universe"/"de
  Sitter"; presentism + event horizon; "becoming saturates in de Sitter". No paper
  found drawing the ontological consequence. Stoica's post-determined block universe
  (abstract checked) is quantum-theoretic and horizon-free.

## 6. Kinds of novelty kept apart

- **Mathematical:** none. Elementary integrals; closed forms exist.
- **Physical:** none. Every quantity is published; χ_eh/χ_p ≈ 4.5–4.7 % is an unstated
  elementary corollary of published quantities, not a new result.
- **Formalization:** none attempted.
- **Philosophical:** the only candidate residue: *if* becoming is indexed to causal
  access (a posit Ellis makes structurally), *then* in ΛCDM becoming saturates: the
  standpoint-relative block converges to a bounded comoving region while its proper
  content and signal flux diverge. Unclaimed in the literature found; unearned without
  the bridge premise; empirically marginal (§5). Relation to the project: the
  fixing-exchange lane measures openness by description-length imbalance
  (Prop. 3), the clock-content lane found the FLRW imbalance to be "cone geometry";
  this lane confirms that the geometric openness budget is (a) finite in ΛCDM, (b)
  already published, and (c) measure-dependent — supporting, not extending, those notes.

**Plain statement, as the brief requires:** the physical idea is already in the
literature (Gott et al. 2005 for the finite future visibility limit and the volume
factor; D&L 2004 for the convergence; Loeb 2002 and Krauss & Scherrer 2007 for the
consequences), and the ontological upgrade currently fails on the measure objection. A
clear negative is the deliverable.
