# Verification audit — Czerniawski 2020 transitivity dispensability
Status: WORKING (split from lean-certificate; no encoding conflict with other agent).
Date: 2026-10-20. User authorized "build" after claim inventory.

## Target claim (recommended from claim inventory)
Source: Jan Czerniawski, "Time and Physical Geometry. A Formalization of Putnam's Proof",
Logic and Logical Philosophy 29(1), 2020, pp. 97-114. Open-access (CC BY-ND).
DOI: `10.12775/LLP.2019.021`. PDF verified locally (`sha256 8534b6ce...e838`).

Claim (Sec. 3, p. 107, verbatim from full-text PDF):
"It is worth noting that, for this [second proof variant], the transitivity of R is not
necessary, since no assumption here requires this property."

This is the dispensability claim for the transitivity premise in the RP argument.

## Why this is the best verification target
From claim inventory (`/tmp/claim_inventory.md`):
- Bounded scope (one premise dropped from one 16-step derivation).
- Explicit symbolic derivation (Sec. 2-3, pp. 98-109) with numbered premises.
- Full-text primary available (verified PDF hash, open access).
- Direct philosophical correspondence (shows RP's transitivity premise is not independently required).
- Does not depend on unread sources (Callender 2000, Bigaj 2008, CH full scan verification still pending).

## Proof-route audit (not encoding)

### Step 1: Identify the derivation
The second proof (Sec. 3, pp. 104-107) derives eternalism `(E)` from:
- `(2)`: presentism assumption (replaced first proof's `(1)`)
- `(2''*)`: strengthened version
- `III''*`: physical fact (no privileged observers / coordinate independence)
- `(L'*)`: lemma (derived from previous premises)
- `(F2*)`: physical fact of SR (simultaneity relation properties)
- `(F2'*)`: variant physical fact
- `(E)`: contradiction / eternalism conclusion

The derivation is a 16-step informal-symbolic sketch (pp. 108-109) with intermediate
steps marked "trivial" or omitted.

### Step 2: Check transitivity absence
Per source record (`knowledge/putnam-ablation/sources.jsonl`, `pa-czerniawski-2020`):
The claim that transitivity is dispensable applies specifically to this second proof
variant (Sec. 3), not the first proof (Sec. 2, p. 104) which may use transitivity implicitly.
The source explicitly notes this distinction.

Verification action needed: Confirm that no premise in `(2''*)`, `III''*`, `(F2*)`, `(F2'*)`,
or `(L'*)` references or requires the transitivity property of `R`.

### Step 3: Check independence claim strength
Czerniawski gives ONE dispensability claim (transitivity). It does NOT provide:
- Independence proof for definability (`III` / `III*` / `III''*`)
- Independence proof for the bridge premise `(N)` (presentism to reality relation)
- Countermodels for dropping other premises individually
- Systematic premise lattice (confirmed in claim inventory)

Therefore: this verification confirms ONE independence result only. It does not establish
a full lattice.

### Step 4: Correspondence to physical claim
The source separates premises into:
- Ontic: `(1)`, `(2)` (presentism / reality)
- Bridge: `(N)` (from "now" to relation `R`)
- Physical facts: `(F1)`, `(F2)`, `(F3)`, `(F1*)`, `(F2*)`, `(F3*)`, `(F1'*)`, `(F2'*)`
- Mathematical / logical: `(L*)`, `(L'*)`, `(L''*)`, `III`, `III*`, `III''*`, `III'''*`

The verification of the transitivity claim is a logical/mathematical verification: it shows
that the logical structure of one proof variant does not require a specific property of the
relation `R`. This is narrower than verifying a physical claim about spacetime.

### Step 5: Feasibility assessment
Lean feasibility for this claim: HIGH.
Requirements for formalization:
- Define reality predicate `r` as a monadic predicate.
- Define three-place relation `R(y; x; Gamma)` (simultaneity in frame of worldline Gamma).
- Encode premises `(2'')`, `III''*`, `(F2*)`, `(F2'*)`, `(L'*)` as logical statements.
- Prove the derivation of `(E)` without using a transitivity axiom for `R`.
- Show that adding a transitivity axiom does not change the derivation (optional, for independence proof).

No continuous measure theory, no complex analysis, no set theory beyond basic logic required.
Bounded scope (one derivation, ~16 steps, explicit premises).

## Toolchain note
No Lean installed (`.worktrees/lean-certificate/formal/INFEASIBILITY.md` confirmed absence of `lean`/`lake` and no `mathlib4`).
This audit does NOT claim any Lean build is possible here. It only confirms that IF the toolchain
were available, the Czerniawski claim is a well-bounded, explicit, and philosophically significant
target.

## Unverified elements
- The full primary `clifton-hogarth-1995.pdf` (user scan, 33 pp) requires manual verification to
  confirm the theorem statements quoted in secondary sources (Savitt 2011, Thyssen 2023, Saunders 2000).
- The `AGENT_REPORT.md` for `kb-csg-quantum-boundary` notes that Sec 3.A (infinite-limit non-uniqueness)
  is labeled `ours` and needs independent check.
- Callender 2000 (`pa-callender-2000`) and Bigaj 2008 (`pa-bigaj-2008`) remain at `discovery`
  depth; any full lattice requires these.

## Conclusion for split audit
This split delivers the claim audit, feasibility classification, and recommended target as
requested. No encoding performed. No collision with `.worktrees/lean-certificate/` agent.
Ready for coordinator/review before any Lean work proceeds.
