# Line-by-line red-team audit: the sixteen-case 1+1 census and its refinements

30 October 2026. Independent adversarial review (worker
`ontology-null-refinements-review`). Targets:
`research/ontology-reconstruction/coordinator/ONE_PLUS_ONE_CENSUS.md` (29/30
October corrected version, this worktree) and
`coordinator/check_1plus1_refinements.py`, with
`coordinator/PERSISTENCE_CONVENTIONS.md` read for the different n≥2 scope and
`coordinator/check_1plus1_census.py`, `check_1plus1_pc_census.py`,
`check_null_region_algebra.py` as supporting certificates. The salvaged
quota-interrupted worker checker
(`.agent-runtime/salvage/2026-10-30-quota/null_refinement_audit-6357469860a3.py`,
SHA256 `6357469…2de69`, hash re-verified this run) was audited by probe runs.

Verdict summary: **every mathematical claim of the corrected census verifies
under exactly its fixed premises; no counterexample was found; the coordinator's
three named defects of the salvaged checker and its 7-vs-8 count error are all
confirmed, and two further salvage defects not named by the coordinator were
found.** Two cosmetic census wordings are flagged (N1, N2). No novelty claim is
made or inherited; the mathematical and source novelty posture of the census is
left exactly as the coordinator stated it.

Route labels: **A** = analytic re-derivation by this lane (complete argument,
no grid); **E** = exact certificate re-implemented independently here
(`check_null_refinement_review.py`, exact sign-atom algebra, fresh code, no
coordinator imports); **W** = existing coordinator script executed under a
15 s hard timeout (all passed); **P** = probe run against the salvaged checker;
**S** = source/bibliographic check.

## 0. Premises fixed for every row below

S: b∈E_b; P_t: b≪c ⇒ E_b⊆E_c; F_t: E_b∩I⁺(b)=∅; covariance under
translations plus the boost subgroup, **no spatial reflection, no dilations,
no time reversal**; spacetime is flat 1+1 Minkowski. Reduction: translation
covariance gives E_b = b+P with P := E_0, so S ⇔ 0∈P, P_t ⇔ P+I⁻⊆P (past
set), F_t ⇔ P∩I⁺=∅. Null coordinates u_L = t−x, u_R = t+x; a boost rescales
(u_L,u_R) ↦ (u_L/h, h·u_R), h>0 (the census writes h = e^η with the opposite
η sign convention — same group, see N2). Refinement rows add one premise at a
time to this fixed base and are never mixed with premise changes.

## 1. Census reduction and structure (ONE_PLUS_ONE_CENSUS.md §1–§3)

| Obl | Claim | Verdict | Route |
|---|---|---|---|
| O1 | Translation reduction E_b = b+P; S/P_t/F_t ⇔ the three P-conditions, uniformly at every standpoint | **PASS** | A |
| O2 | Sign conventions: ≪ = strict componentwise increase of (u_L,u_R); ≤ = non-strict; region names N⁺R={u_L=0<u_R} (future, x>0), N⁺L={u_L>0,u_R=0}, N⁻R={u_L<0,u_R=0}, N⁻L={u_L=0,u_R<0}, RW={u_L<0<u_R}, LW={u_R<0<u_L} all match their (t,x) descriptions | **PASS** | A, E (PASS B block) |
| O3 | I⁻∪{0} ⊆ P mandatory; I⁺∩P = ∅ mandatory | **PASS** | A |
| O4 | Null branches are single boost orbits, so membership is all-or-nothing | **PASS** | A (branch = {(0,be^η)}) |
| O5 | Wedge all-or-nothing: with p=(−a,b), q=(−A,B)∈RW, h > max(a/A, B/b) puts q ≪ (−a/h, bh) = boost(p); boost invariance + past closure force q∈P | **PASS** | A (inequalities re-derived), E (exact rationals, PASS C) |
| O6 | Chains: N⁺R ⇒ RW ⇒ N⁻R and N⁺L ⇒ LW ⇒ N⁻L via exact timelike witnesses | **PASS** | A, E (exact region sums NpR+Im={Im,NmR,RW} etc.) |
| O7 | No cross-side implication and no self-return: past of an N⁺R point meets exactly I⁻∪RW∪N⁻R and cannot meet N⁺R itself (u_L would have to decrease while staying 0); past of an N⁻R point lies in I⁻; mirror identical | **PASS** | A, E (right-side pasts are disjoint from all left regions and from NpR) |
| O8 | Valid per-side triples are exactly n⁺≤w≤n⁻ (monotone), sides independent: **exactly 16** | **PASS** | A (set-wise past-closure sufficiency checked per region), E (64 unions → exactly 16 past sets = monotone) |
| O9 | Pairwise distinctness and identification: (000\|000)=I, (001\|001)=J⁻, (011\|011)=B, (111\|111)=C, (000\|011)=fifth family in E-space = {u_R<0}∪{0}, (011\|000)=mirror | **PASS** | A, E, W (census script item 4 and fifth-family cross-check agree pointwise) |

The strongest completeness attack — a single boost orbit (fixed product
−u_Lu_R) inside a wedge, which boost invariance alone would permit — fails
because O5's h-trick keeps the orbit (boosts preserve the product) while
making the target strictly timelike-future of the boosted member; past closure
then sweeps the whole wedge. This is the load-bearing step and it is correct.

## 2. Refinement rows (census §4, premises held fixed)

Notation: bits are (right|left) triples (n⁺, w, n⁻).

| Obl | Added premise | Claim | Verdict | Route |
|---|---|---|---|---|
| R1 | Reflection invariance P = σ(P) | exactly 4 rules: identical triples: I, J, B, C | **PASS** | A, E |
| R2 | (no extra premise) mirror identification of the 16 gives exactly **10** classes (4 fixed + 6 pairs), and this is *not* invariance | **PASS** | A, E |
| R3 | P_c (F_t retained) | exactly **9**; ⇔ both past-null bits 1; necessity via S+P_c ⇒ J⁻(0)⊆E₀ (the PERSISTENCE_CONVENTIONS §1 argument); sufficiency by exact case analysis on P+J⁻ | **PASS** | A, E |
| R4 | F_c (P_t retained) | exactly **9**; ⇔ both future-null bits 0 | **PASS** | A, E |
| R5 | P_c ∧ F_c | exactly **4**: J, J+RW, J+LW, B | **PASS** | A, E |
| R6 | Closedness (ordinary spacetime topology) | exactly **4**: J, C, {u_L≤0}, {u_R≤0}; necessity: cl(I⁻) forces both n⁻ bits, cl(RW)/cl(LW) force the n⁺ bit whenever w=1, leaving per-side 001 or 111; sufficiency: all four sets are closed | **PASS** | A, E |
| R7 | Closedness ∧ F_c | exactly **1**: J | **PASS** | A, E |
| R8 | Half-spaces: (111\|001) = {u_L≤0} =: P_L, (001\|111) = {u_R≤0} =: P_R; closed, boost-invariant, causally past-closed, self-inclusive, F_t, each contains one future-null branch hence fails F_c; **transitive** | **PASS** | A, E (closure/additivity exact; {u≤0}+{u≤0}={u≤0}) |
| R9 | E transitive ⇔ P+P⊆P under translation covariance | **PASS** | A (x−z = (x−y)+(y−z) with free increments; quantifiers checked both directions) |
| R10 | Transitivity | exactly **12**; failures are exactly the both-wedges rules (B, (011\|111), (111\|011), C) because RW+LW = ℝ² exactly (target construction with a>max(0,−u), b>max(0,v)), forcing I⁺⊆P against F_t | **PASS** | A, E |
| R11 | Transitivity sufficiency subfamily | no-wedge 4 rules: all members in {u_L≤0,u_R≤0}, sums land on an optional past-null ray only from that same ray or 0; one-wedge 8 rules: P = {u_L<0} ∪ ({0}×D), D ∈ {{0}, [0,∞), (−∞,0], ℝ}, all four D additive — the coordinator's additive-semigroup derivation is complete and correct | **PASS** | A, E (D-forms certified for all 8) |
| R12 | Transitivity ∧ closedness | **3**: J and the two half-spaces (C is both-wedges, hence not transitive) — the n≥2 row "transitivity+closedness ⇒ J" does **not** transfer | **PASS** | A, E |
| R13 | Transitivity ∧ P_c | **5**; ∧ F_c: **8**; ∧ P_c∧F_c: **3** (J, J+RW, J+LW) | **PASS** | A, E |
| R14 | Historical correction claims: "P_c+F_t gives nine whereas P_c+F_c gives four"; "the earlier script refutation changed F_t to F_c at the same time"; reflection **invariance** (4) versus mirror **quotient** (10); closed rules are J, C and the two null half-spaces (not just J and C) | all four **PASS** as stated; `check_1plus1_pc_census.py`'s docstring correction log confirms the premise-change history, and it checks the 4-case P_c+F_c statement only | A, E, W, P |

Every refinement-table converse was attacked and held: for R3 sufficiency the
critical case p∈N⁺R (needs w=1 already forced by the chain) and p∈LW∪N⁺L under
an N⁻R increment (result stays in one of LW/N⁺L/N⁻R/I⁻/N⁻L, all present);
for R6 the only potential extra closed pattern (011 per side with the n⁻ bits)
dies on cl(RW)∋N⁺R; for R10 the additivity of each of the twelve surviving
region unions is an exact set identity, not a sampling statement.

## 3. Checker and certificate audits

| Obl | Object | Verdict | Evidence |
|---|---|---|---|
| C1 | `check_1plus1_census.py` | **PASS** — witnesses sound; grid is declared witness-only; fifth-family cross-check agrees with this lane's independent derivation of E₀ = {u_R<0}∪{0} from the review's A′ = {a_R>0}∪{0} | W, A |
| C2 | `check_1plus1_refinements.py` (named audit target) | **PASS** — bit layout (n⁺, w, n⁻)×(R, L) consistent with census; F_c grid test covers exactly J⁺∖{0} in null coordinates; BOUNDARIES list contains exactly the six needed boundary incidences (cl(I⁻)→both N⁻; cl(RW)→N⁺R and N⁻R; cl(LW)→N⁺L and N⁻L); h_l/h_r coordinate identifications correct ((1,1,1)\|(0,0,1) ↔ u_L≤0); half-space additivity witnesses sound; scope sentence honest | W, A |
| C3 | `check_null_region_algebra.py` | **PASS** — exact atom algebra with correct NEG+POS = ℝ and open/closed propagation; 64-candidate reduction to 16 past sets; all counts asserted match §2 above; correctly described as a finite symbolic certificate for the *reduced* region algebra, with the continuous-domain reduction analytic | W, A |
| C4 | `check_1plus1_pc_census.py` | **PASS** — 4-case P_c+F_c statement only, with an honest correction log distinguishing F_t (9) from F_c (4) | W |
| P0 | Salvage run as-is | **REPAIR confirmed**: exits at line 231, `assert set(part) == {"Im","Ip","RW","LW"}` fails because the sign grid (±3, 0) contains the four null-branch points — exactly the coordinator's defect (i) and DIRECT_RECOVERY's "exits immediately at line 231" | P |
| P1 | + null regions in that assertion | **REPAIR confirmed**: `ValueError: (None, Fraction(0,1), True, True)` raised in `iv_superset_of_atom` (line 58) — the helper receives interval tuples while branching on the strings "NEG"/"ZERO"/"POS" — defect (ii) | P |
| P2 | + tuple→name decoding | **NEW finding, not coordinator-named**: `len(valid) == 0`; `Im+Im` is computed as {Im, Ip, LW, RW}. The helper's NEG/POS branches have inverted boundary disjuncts: `(lo == 0 and lo_o)` / `(hi == 0 and hi_o)` treat the *open* endpoint 0 as "contains the opposite ray", so the negative ray is declared to contain the positive ray. The ZERO branch is correct (`not lo_o`/`not hi_o`); the NEG/POS branches need the boundary case removed (`lo is None or lo < 0`; `hi is None or hi > 0`) | P |
| P3 | + corrected NEG/POS tests | O2, O2b, O3, O4, O5a–O5g, O6a all **PASS** — after the two helper fixes the salvage's algebra agrees with the census on the sixteen-case structure and every count through transitivity-12; then fails in O6b: the DESC expectation sets for (011\|000) and (000\|011) (`OPEN_L` and `frozenset({"Im","NmL","LW"})`) **omit "Zero"** although their own labels say "∪ {0}" — second NEW finding, not coordinator-named | P |
| P4 | + "Zero" restored in the two DESC sets | O6b–O6d **PASS**; crash at `assert len(ftc) == 7` — defect (iv): the correct transitivity∧F_c count is **8** (nine F_c rules minus the single both-wedges rule B), exactly as census §4 states | P |
| P5 | + count 8 | O6e and O7 **PASS** (the salvage's operational translation-form check is sound); crash in O8 at `assert (xn == rx) == want` — defect (iii) confirmed at original line 459: `rx, ry = region_of_point(x, y)` unpacks the returned region-name *string* into two variables; for a 2-character name such as "Ip" (the first drawn point with seed 7 is (1/2, 5/3) ∈ I⁺) it silently yields rx="I", ry="p" and the comparison assert fails; for 3-character names it would raise ValueError. Coordinator's description is exact | P |

Salvage audit bottom line: the coordinator named three code defects plus the
wrong count; all four are confirmed, the "seven" criticism is correct (8 is
right), and two further defects exist (P2 inverted boundary disjuncts, P3 two
omitted "Zero" atoms). No defect affects the *census mathematics*: the salvage's
corrected algebra (P3–P5) independently reproduces every count in §2 above.
Its O3b REPAIR note flags a census §3 sentence ("chronological past of N+R can
additionally meet N+R") that the coordinator had already corrected by 30
October — the salvage audited the pre-correction text, and its finding agrees
with the current wording.

## 4. Interpretation separations (task obligations)

* **Conditional set theory vs ontology.** Every result above is conditional
  mathematics: given the fixed premises (S, P_t, F_t, boost+translation
  covariance, flat 1+1), exactly these sixteen region unions — and their
  refinements — survive. No row selects an ontology: F_t is an ontological
  restriction (PERSISTENCE_CONVENTIONS §5's collar family shows what happens
  without it), closedness and transitivity are regularity preferences, and the
  census asserts no philosophical conclusion. The uniqueness of J under
  closedness+F_c is a corollary of chosen premises, not evidence that realms
  must be closed.
* **Topology vs physical regularity.** Three different axes are kept apart in
  the rows: causal/chronological structure (P_t, P_c, F_t, F_c — order-theoretic
  and physical), algebraic regularity of the existence relation (transitivity —
  equivalent to P+P⊆P, no topology and no physics), and topology (closedness —
  an ordinary-topology condition on E_b, carrying no causal content). The n≥2
  table's "closedness ⇒ {J, C}" and the 1+1 answer "closedness ⇒ 4" differ
  because of orbit structure, not because any physical premise changed.
* **Reflection covariance vs identification modulo symmetry.** Parity is not
  in the covariance group. Adding reflection as a premise (invariance) leaves
  4 rules; quotienting the 16 by the mirror (identification) yields 10 classes
  and leaves the asymmetric rules perfectly valid but paired. The census's
  distinction — which replaced an earlier conflation — is exactly right, and
  the 10 count is an orbit count (4 fixed + 6 pairs), not an invariance count.

## 5. Strongest attempted counterexamples (all failed)

1. **Partial-wedge membership.** P = I⁻∪{0} ∪ (one boost orbit of RW, i.e.
   fixed product −u_Lu_R). Kills itself: the h-trick of O5 maps the member
   above any same-wedge target while staying in P, so the whole wedge enters.
2. **Cross-side chains.** Sought a timelike pair coupling right-side regions to
   left-side regions (which would couple the triples and shrink 16). Exact
   pasts: right-side pasts stay in I⁻∪{right regions}; the only cross-side
   contact anywhere is *causal*, not chronological (J⁻ of an N⁺R point meets
   N⁻L), and that is precisely why P_c forces both n⁻ bits (R3) rather than
   shrinking the P_t census.
3. **Causal closure without the opposite past-null branch**, e.g. (011|000).
   Dies on the origin: 0∈P and w=(0,−1)∈J⁻(0) give 0+w = w = N⁻L ∉ P. The
   mandatory set for P_c is J⁻(0), not I⁻∪{0}; this is why R3's necessity is
   S+P_c, and the census's phrase "mandatory by S" should be read as "by S and
   the added P_c" (nit N1).
4. **A fifth closed rule**, per side (011) with both n⁻ bits. Dies on
   cl(RW) ∋ N⁺R: the sequence (−1/k, 1) lies in RW and converges to (0,1).
5. **Transitivity for B** via restricted sums. Dies exactly: RW+LW = ℝ², so
   P+P ⊇ I⁺, contradicting F_t. The four both-wedges failures are forced.
6. **Transferring n≥2 rows.** "Transitivity+closedness ⇒ J" and "closedness ⇒
   {J, C}" both fail in 1+1: the half-spaces P_L, P_R are closed, transitive
   (additive), causally persistent, F_t members of the sixteen. This refutes
   the *transfer*, not the census — it is the census's own claim and is the
   strongest confirmation target of the whole correction set.

## 6. Unproved extensions (labeled, per task)

* No Lean (or other proof-assistant) formalization exists for the census or the
  transitivity subfamily; the analytic proofs here and the exact symbolic
  certificate are the current verification status.
* The transitivity subfamily is derived for 1+1 flat Minkowski with the fixed
  group only. The n≥2 no-parity analogue, curved-spacetime analogues, and any
  version with translation covariance dropped (where the reduction to one set P
  fails and the family is no longer classified) are open and are not claimed.
* Prior art is discovery/abstract-level here (see `sources.jsonl`): the CH 1995
  Theorem 1 content is inherited from the project's full-text audit and was not
  re-read from the scan; Bigaj 2008 was checked at abstract level only. The
  dedicated census-depth prior-art audit the census proposes remains open. No
  novelty verdict is claimed or implied.

## 7. Repairs proposed (cosmetic; no count changes)

* **N1** (census §4): "For P_c, J⁻(0) is mandatory by S" — read "by S together
  with the added premise P_c" (the §1 argument needs both).
* **N2** (census §1): the boost formula (u_L,u_R) ↦ (e^{−η}u_L, e^{η}u_R)
  fixes a sign convention for η (boost toward −x); the group generated is the
  same, and nothing downstream depends on the label. Optional footnote.
* Salvage file: preserve as-is (done — original untouched; probes ran on copies
  under /private/tmp/opencode). Its corrected-algebra agreement (P3–P5) is
  worth one sentence in any final writeup about the interrupted run.

## 8. Verification commands and results

All runs: `python3 /private/tmp/opencode/t15.py python3 <script>` with a hard
15 s timeout; every run finished in ≤ 0.62 s; total recorded compute ≈ 2 s
(budget: 10 s per check, 30 s total).

| Command (cwd) | Exit | Elapsed |
|---|---|---|
| `check_null_refinement_review.py` (this lane) | 0 | 0.615 s |
| `coordinator/check_1plus1_census.py` | 0 | 0.160 s |
| `coordinator/check_1plus1_refinements.py` | 0 | 0.041 s |
| `coordinator/check_null_region_algebra.py` | 0 | 0.028 s |
| `coordinator/check_1plus1_pc_census.py` | 0 | 0.028 s |
| salvage probe0 (as-is) | 1 (line 231) | 0.054 s |
| probe1 (+null regions in assertion) | 1 (ValueError, helper) | 0.053 s |
| probe2 (+tuple decode) | 1 (`len(valid)==0`, inverted tests) | 0.069 s |
| probe3 (+fixed NEG/POS tests) | 1 (O6b DESC missing "Zero") | 0.159 s |
| probe4 (+Zero restored) | 1 (`len(ftc)==7`, actual 8) | 0.119 s |
| probe5 (+count 8) | 1 (O8 string unpack, line 459 orig.) | 0.598 s |

`shasum -a 256` on the salvage file re-verified
`6357469860a39c25deb0a550d276983726aa2b20e46ef2bf73ab8dcca8f2de69` before the
probes; probes ran on copies; the original is byte-identical afterwards.
