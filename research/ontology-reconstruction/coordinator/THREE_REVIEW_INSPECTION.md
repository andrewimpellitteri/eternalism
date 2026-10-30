# Inspection of the three 29 October review submissions

Coordinator inspection record, 29 October 2026. The three adversarial
reviews dispatched in `BATCH2_RUN_PLAN.md` have submitted. This record
states what was inspected, what was reproduced, what was re-derived by the
coordinator, and what was integrated. It does not accept the tasks and does
not settle the proofs; the user asked to inspect findings before any proof
is treated as settled, so no board transitions were performed and
CLAIM_STATUS / CURRENT_SYNTHESIS are intentionally left unchanged this
round.

## Submissions inspected (read in full)

| Task | Worktree commit | Payload |
|---|---|---|
| `ontology-persistence-review` | `12b7a15` | O1–O24 verdicts, retractions R1–R3, fifth 1+1 assignment |
| `lawful-axis-source-review` | `a373453` | O1–O15 verdicts on LOY v1 source inputs, O7 lemma, typo audit |
| `lawful-axis-lift-review` | `0ca5ad1` | O1–O19 verdicts on the C¹,¹ lift, REPAIR-N1/N2/N3 |

## Checks reproduced by the coordinator

- `check_persistence_witnesses.py` (coordinator's own): PASS, all four
  lines.
- `persistence-review/check_independent.py`: PASS O1–O21, exact Fraction
  arithmetic.
- `persistence-review/check_1plus1_fifth.py`: PASS (5 lines), fifth
  assignment constructed and checked.
- `axis-lift-review/verify_checks.py`: PASS=14 FAIL=0, including the
  crossing-pair Lipschitz ratio 2.51 and the non-convergent-Hessian
  sharpness model.

## Coordinator second reads (new this session)

1. **O7 mixed-derivative estimate (the load-bearing |φ_uv|≤C lemma),
   verified analytically.** The identity ∂_u(φ+rψ)=−Krψ follows from
   (rφ)_uv=r_uvφ by expanding ∂_u(λφ+rφ_v) and cancelling λ_uφ against
   r_uvφ; ψ_u=−c/r with c:=φ_u+νψ+Krψ. The log-divergence contradiction in
   step 2 needs only continuity of c and the printed axis-inclusive (3.9).
   For step 3 I re-derived ∂_u(rc)=rB−cKr with B=φ_uu+ν_uψ+(Kr)_uψ and
   confirmed no term of B consumes φ_uv, so there is no circularity; the
   Gronwall bound |rc|≤Cr² uses r≍v−u from (3.2). The lemma also re-proves
   parity φ_ρ(t,0)=0 via c≡0 with ν=−λ on Γ. Both the source lane's and
   this re-derivation agree; the estimate now has two independent readings.
2. **REPAIR-N3 cross-axis Lipschitz proof, checked.** Case 1 (segment
   avoids the axis) is the standard C¹ bound; Case 2 (segment crosses at
   (z*,0)) uses |G|≤Cρ pointwise plus |x−z*|+|y−z*|≤|P−Q|. Only the two
   facts already proved are consumed. Inserted into
   `AXIS_C11_RECONSTRUCTION.md` §4.
3. **Fifth 1+1 assignment, verified analytically.** A'={0}∪{a∉I⁻(0):
   t_a+x_a>0} is boost-invariant because t+x scales by e^η>0; it is a
   future set because t+x strictly increases along timelike futures and
   I⁻(0) is a past set; S and F_t hold by construction; E_b={x:b−x∈A'} is
   Poincaré-covariant. Set-level distinctness from I, J, B, C at
   standpoint 0 confirmed (it contains the right wedge and the right
   future-null branch, misses the left wedge and all past nulls). The
   census's n≥2 hypothesis is therefore load-bearing and was honestly
   hedged; the hedge is upgraded in `PERSISTENCE_CONVENTIONS.md` §4.
   Defects found in the review script's *print labels only*: B's probe
   pattern is (T,F,T,T) and C's is (T,T,T,T), not the (F,F,T,T)/(T,F,T,T)
   printed; the script's assertions correctly test inequality against the
   fifth pattern, so all PASS/FAIL logic is unaffected. The script lives in
   the worker's worktree and was not edited; this record is the correction.

## Integrations applied (coordinator-owned files only)

`AXIS_C11_RECONSTRUCTION.md`: REPAIR-N2 (field equations r_uv=2mνλ/[(1−μ)r²]
and (rφ)_uv=r_uvφ added to §1 as explicit inputs, with the φ=ρ failure mode
stated); the §4 prose-sentence appeal for |φ_uv|≤C replaced by the O7
derivation with audit citation; confirmed-typo and Prop 3.18 u-side
sketch-fidelity caveats added; REPAIR-N1 (§2 term-by-term O(r) wording);
REPAIR-N3 (two-case proof inserted); §6 source-correspondence gate closed
with second-reader residuals listed.

`PERSISTENCE_CONVENTIONS.md` §4: the 1+1 caveat upgraded from "the orbit
argument changes" to "additional assignments exist", with the construction,
its verification status, and the open complete-1+1-census question.

## Still open (unchanged by this inspection)

- Smooth maximal/global-developability applicability: no smooth common
  development follows from the C¹,¹ argument; the Ringström-class route
  still needs either stronger regularity for these scattering solutions or
  a lower-regularity field-preserving development theorem with its full
  hypotheses. No smooth MGHD, C² metric, or pointwise axis Ricci claim.
- LOY v1 (2016 preprint) is the only recorded version; "printed" means
  v1-printed. The u-side halves of Prop 3.18 remain proof sketches; a
  defect there would weaken the pure-third-derivative inputs to v-side
  statements, not the lifting lemma or the O7 estimate.
- Retractions R1–R3 (persistence review §7) target other lanes'
  submissions (equivalence two-case census; causal-A3 row; any
  "covariance+persistence+closedness select J" suggestion). They are
  verified here as corrections of record but the affected worker files
  were not edited.
- Census prior-art audit remains unperformed; no novelty claim is made or
  implied for the census, the C¹,¹ reconstruction, or the O7 lemma.
- The 1+1 no-parity complete census is open (one fifth family + mirror
  known).

## Decision left to the user

Whether to accept the three review tasks, queue the proposed follow-ups
(second-reader pass on Prop 3.18 u-side sketches is done at O-lemma level;
a dedicated census prior-art audit and the 1+1 census are separate tasks),
and whether the repaired C¹,¹ note may be cited downstream. Nothing above
should be quoted as an accepted result until those decisions are recorded.

## Addendum (same day, later): complete 1+1 census

The review's flagged gap "complete 1+1 no-parity census not completed" is
now closed at coordinator level: exactly 16 covariant, self-inclusive,
chronologically persistent, F_t assignments exist in 1+1 without parity —
per side the monotone chain (future-null ⊆ wedge ⊆ past-null), sides
independent. I, J, B, C, the review's fifth family and its mirror are
among them; the mechanism explains why the n≥2 census holds (saturation
kills the chain freedom there). See
[ONE_PLUS_ONE_CENSUS.md](ONE_PLUS_ONE_CENSUS.md) and
`check_1plus1_census.py` (exact checks, 0.03 s; two checker defects of the
coordinator found and fixed during development are logged in the note).
The census is a coordinator deduction pending independent review; the
P_c variant (expected 9) is a labelled conjecture, not checked. The
discovery-level prior-art sweep in §7 of the note (Bigaj 2008 cumulativity
as nearest B-type relative; no census-form statement found) feeds, but does
not replace, the proposed dedicated audit.

## Continuation audit, 30 October: corrections to the inspection itself

The O7 argument is now replaced by its exact integrating-factor formula in
AXIS_C11_RECONSTRUCTION.md. Since w=rc vanishes at the axis merely from
bounded c, the logarithmic contradiction is unnecessary. K≤0 bounds the
integrating factor by one, giving |w|≤Cr² directly. The mixed-derivative
bound therefore does not assume scalar parity. The off-axis gradient is
locally Lipschitz, not necessarily C¹, and the corrected segment argument
uses |x|+|y|=|x−y| when a segment meets the axis. The earlier expression
subtracting a spacetime axis coordinate from spatial x,y is superseded.
HTML v1 mass equations are (2.10)–(2.11), distinct from the raw-TeX review's
numbering; the input list now records this explicitly.

The complete 1+1 census retains sixteen base cases, but its refinements had
errors. Reflection invariance leaves four rules; identifying mirrors gives
ten equivalence classes. Four rules are closed, including two asymmetric
null half-spaces; those also refute transferring the n≥2 transitivity row.
P_c with F_t retained gives nine cases, whereas P_c+F_c gives four. Thus
the later claim that a script refuted nine changed the exclusion premise.
ONE_PLUS_ONE_CENSUS.md and check_1plus1_refinements.py record the repairs.
The new full 1+1 classification and refinements remain coordinator
deductions awaiting a dedicated independent review; the earlier persistence
review audited the n≥2 four-case theorem, not these later extensions.
