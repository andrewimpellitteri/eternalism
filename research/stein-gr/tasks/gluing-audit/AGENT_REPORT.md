# Agent report: stein-gluing-audit

25 October 2026. Claimed by `claude-head` (head session, direct user request);
read-only adversarial proof lane.

## Task

Independently challenge domain transfer and the flat detour in
`research/stein-gr/main.tex` (audited at commit `498de2f3`): Lemmas B, C, D,
F, the constants paragraph, both transfer embeddings, and their assembly into
Theorem 7(a).

## Deliverable

`research/stein-gr/tasks/gluing-audit/PROOF_AUDIT.md` — dependency-by-
dependency verdict with a findings ledger, counterexample attempts, and
primary locators for imported causal facts.

## Evidence and checks

- Every embedding and transfer hypothesis traced: Lemma B (tubular coordinates,
  Lipschitz estimate), Lemma C (cone-control algebra re-derived, inequalities
  match the hypotheses exactly), constants paragraph (no circularity; 6Kr
  controls T_{3r}; 8λr < L is the tilt-slope constraint), Lemma D (escape
  paths re-derived with the inequalities checked: μ > 1/2, μ < 5/2, μr vs
  r/2; both D-inclusions; both stopping-event cases), Lemma F (boost/pullback
  argument reconstructed and validated), morphisms (x, b lie in rel-int Σ′ by
  the arc construction; N and ψ(N) are GH objects).
- SECOND_PASS_REVIEW repairs treated as proposals and verified in the audited
  source: strict-diamond openness in Lemma D(iii), and the τ₀ ≤ τ_exit
  equality case in Lemma D(ii). Both correctly applied.
- Counterexample attempts (brief requirement): boundary tie q = p; boosted
  end-cap escape; disconnected interior; r-chauvinism. All resolved; one
  produced a minor manuscript repair (F1).
- Both localization directions and detour acausality have complete quantified
  arguments; no failure exhibited.

## Findings

- No blocking findings.
- F1 (minor, fix at integration): Lemma F's "escape along the gradient of the
  distance to the arc" is spacelike at end caps; replace with uniform
  past-directed vertical descent and state C ≥ 2.
- Two cosmetic precision items (χ ≡ 1 on a neighborhood; η_c vestigial) and
  one imported citation to verify at integration (Bernal–Sánchez Thm 1.1/
  Rem 4.14 as stated for a compact acausal submanifold with boundary).

## Limitations

- Lemma-level audit of the geometry; not a re-derivation of the
  Minguzzi–Sánchez or Bernal–Sánchez source results (locators recorded;
  Bernal–Sánchez flagged for integration).
- Did not audit Theorems 8–9, Propositions 10/17/18 (other lanes), and did
  not draft any notation patch (core-repairs lane).

## Unresolved questions

- Whether the energy-rigidity lane's pocket problem admits a bounded ansatz
  (hand-off; out of scope here).
