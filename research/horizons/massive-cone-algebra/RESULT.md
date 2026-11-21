# The past-cone algebra of a massive free field is everything

11 November 2026. Claude Code (Fable 5.2), research worker, task
`novel-massive-cone-algebra`. Checked only by the session that wrote it. Nothing here
is new mathematics. No temporal ontology is selected. Sources and read depth:
[sources.jsonl](sources.jsonl). Settles the open entry in the
[cone-algebra note](../cone-algebras/RESULT.md).

## Verdict

**Yes.** For a free scalar field of mass m > 0 in the vacuum representation on
Minkowski spacetime, the von Neumann algebra of the open forward light cone of any
point, and equally of the open backward cone, is all of B(H). The "larger set" in the
earlier note is the whole of Minkowski spacetime.

**Yes, a thin tube suffices.** The algebra of any open neighbourhood of a past (or
future) inertial half-worldline is already B(H).

**Status of the evidence.** The 1971 paper of Sadowski and Woronowicz was not read: it
is behind a publisher wall (HTTP 403) and no open copy was found. The verdict rests on
two later papers read in full text that state the result, credit it to that paper, and
in one case prove it by a different route, and on a short derivation written out
below. The proof route leans on a theorem of Borchers that was not read at its source.

## What is proved where

| Statement | Where | Read |
|---|---|---|
| For a net with a vacuum, the weak closure R(V) of a light-cone algebra is either B(H) or a type III₁ factor. It is B(H) if the energy-momentum spectrum has a mass gap, citing "[24, Thm 2]" = Sadowski–Woronowicz. It is type III₁ when the spectrum has weight on the boundary of the cone (massless particles), by Huygens' principle, citing Buchholz 1977 p. 161 and Longo 1979 | Buchholz and Roberts, arXiv:1304.2794v4, Sec. 1 and Sec. 3 (text after Prop. 3.2) | full-text (those sections) |
| If R(V) ≠ B(H), the spectrum of the translations is the whole closed forward cone. So a gap between the vacuum and the rest of the spectrum forces R(V) = B(H), and then "all lightcone algebras coincide". Case (a) again credits Sadowski–Woronowicz. Proof given, using Borchers' theorem on half-sided translations | Buchholz and Fredenhagen, arXiv:2305.11709v1, Lemma 3.1, cases (a)–(c), Prop. 3.2 | full-text |
| Free scalar field, any m ≥ 0, any continuous quasifree state: the algebra of an open set equals that of its envelope. Classical part: a distributional solution vanishing on an open set vanishes on its envelope | Strohmaier, arXiv:math-ph/0008043v2, Theorems 3.2 and 5.1, Cor. 5.3 | full-text |
| Timelike tube theorem for general (interacting) fields; history (Borchers 1961, Araki 1963); semi-infinite worldlines are allowed | Strohmaier and Witten, arXiv:2303.16380v1; Witten, arXiv:2303.02837v2, Sec. 3.1 | full-text (pages listed in sources) |
| "The open past light cone and the open isotropic tube are proved to be total sets", total meaning that the algebra equals that of all Minkowski space; Araki's and Borchers' conditions do not give this | Sadowski and Woronowicz 1971, abstract, seen only as a search-engine summary | discovery |

A warning about the last row: the abstract as summarised states no mass hypothesis. The
statement is false for massless fields in four dimensions (next section), so the
theorem must carry one. Buchholz and Roberts attach the mass gap to "Thm 2". I could
not check the exact hypotheses of the 1971 theorem, nor whether it is proved for the
free field only or for any theory with a gap.

## The argument, as read in Buchholz–Fredenhagen

Let M = R(V₊) and Ω the vacuum. Ω is cyclic for M (Reeh–Schlieder). Future timelike
translations U(τ) map M into itself and have positive energy.

1. Let Z be the largest projection in M that annihilates Ω. Then U(x) Z U(x)* = Z for
   all x (their Lemma 3.1).
2. On (1 − Z)H the vacuum is cyclic and separating for (1 − Z)M(1 − Z). Borchers'
   theorem then gives Δ^{iσ} U(x) Δ^{−iσ} = U(e^{−2πσ} x). So the spectrum of U on
   (1 − Z)H is invariant under scaling.
3. With a mass gap the only scale-invariant part of the spectrum is {0}. The vacuum is
   the only invariant vector, so (1 − Z)H = CΩ and the vacuum projection lies in M.
4. An algebra that contains the projection on a cyclic vector is B(H): any A′ in the
   commutant fixes the ray of Ω, so A′BΩ = BA′Ω = cBΩ for all B in M, and A′ = c.

The free field of mass m has spectrum {0} ∪ {p² = m²} ∪ {p² ≥ 4m²}, so the argument
applies, in any spacetime dimension ≥ 2. The backward cone follows by time reflection.
Step 4 and the application to the free field are mine; steps 1–3 are theirs.

## The thin tube

Let T be an open neighbourhood of the half-line {(t, 0) : t < 0}. For each s > 0 the
segment from (−s, 0) to (0, 0) lies in T, and its envelope is the open double cone D_s
between its endpoints (Strohmaier, Prop. 2.1). By his Theorem 5.1, R(T) ⊇ R(D_s). The
D_s increase to the open past cone V₋ of the origin, and every compactly supported
test function in V₋ lies in some D_s, so R(T) ⊇ R(V₋) = B(H).

So **the fields measurable near one inertial observer's past worldline generate every
observable of a massive free field**. The first step holds for interacting theories
(Strohmaier–Witten); the second for any theory with a mass gap, on the authors'
general assumptions. I did not find this two-step corollary stated in the sources
read. It is immediate and I claim no novelty for it. The statement that a tube around
a *whole* worldline is complete is Borchers 1961 (by its title and by Strohmaier's
and Witten's accounts; not read).

## Classical counterpart

For the free field the quantum statement is equivalent to a classical uniqueness
statement. Vectors h of the one-particle space correspond to real distributional
solutions ψ_h(f) = Im⟨h, Kf⟩ of the Klein–Gordon equation with finite one-particle
norm (data in H^{1/2} ⊕ H^{−1/2}). The Weyl operator W(h) commutes with R(O) exactly
when ψ_h vanishes on O. Hence:

- R(V₋) = B(H) implies that no non-zero solution of finite one-particle norm vanishes
  on V₋ (only the Weyl relations are used);
- conversely, if no such solution exists, the real subspace of V₋ is dense and
  R(V₋) = B(H) by the density lemma Strohmaier quotes as his Prop. 4.1.

For m > 0 every finite-energy solution has finite one-particle norm (norm² ≤
energy/m, since ω ≥ m). So the quantum theorem contains the finite-energy row of the
[massive-Minkowski note](../massive-minkowski/RESULT.md): **a finite-energy solution
with m > 0 that vanishes on the past cone of one event vanishes everywhere, in every
dimension**. That note proved it in one space dimension from Burnol's decay lemma and
left higher dimensions resting on an unchecked decay estimate. With Strohmaier's
Theorem 3.2 the same holds if the solution vanishes only near a past half-worldline.
This equivalence is this session's derivation from standard facts. It is not checked
by anyone else. The infinite-energy smooth solutions of that note, which vanish on a
past cone and not elsewhere, are outside the one-particle space, so there is no
conflict.

## Contrast with the massless case

Read in Buchholz–Roberts, Buchholz–Fredenhagen and Witten (Sec. 3.3); the primary
papers of Buchholz (1977, 1982), Longo (1979) and Hislop–Longo (1982) were blocked
and not read.

- Massless free field, even spacetime dimension: the commutator is supported on the
  light cone, so the algebras of the future and past cones of a point commute. R(V₊)
  is a proper subalgebra, a type III₁ factor.
- In general, with massless particles R(V₊) commutes with the outgoing massless fields
  created in the past cone (Buchholz–Fredenhagen eq. (4.6)). Information about them
  cannot be recovered in V₊. For asymptotically complete purely massless theories the
  vacuum is also separating for R(V₊) (their case (c), citing Buchholz 1982).
- With a mass gap none of this happens: R(V₊) = B(H), the translations are in it, and
  the extension of the dynamics to the past is unique.

So the dichotomy of the cone-algebra note stands and is now sharp on the massive
side: massless, four dimensions, the two cones are commuting systems; massive, each
cone alone is the whole system.

## Limits

- Sadowski–Woronowicz, Borchers (1961, and the half-sided translation theorem), Araki
  1963, Buchholz 1977 and 1982, Longo 1979 and Hislop–Longo 1982 were not read.
- Minkowski spacetime, vacuum representation. The proof uses translations that map
  the cone into itself and the spectrum condition. Nothing follows for spacetimes
  with a beginning or a cosmological horizon, where the classical notes find that
  massive matter stays outside past cones.
- Massless fields in odd spacetime dimensions have no gap and no Huygens principle.
  Which case holds there was not looked up.
- "Generates" means weak closure. Reaching a given observable needs measurements
  arbitrarily far back along the worldline, and of unbounded complexity. The classical
  note's figures (a quarter of the energy still outside the cone 200 time units back
  at m = 0.3) show how slow this is.
- Generating all observables is not determining the state from data, and it is no
  ontology. An algebra equal to B(H) says the cone is not a proper subsystem; it does
  not say the future is fixed or real.
