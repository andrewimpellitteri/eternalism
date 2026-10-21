# Making the P1** note novel: the universe case meets the problem of time

Coordinator idea note, 2026-10-21. **Read depth: discovery only** (search
snippets and abstracts; no full text read). Nothing here is verified, and no
priority is claimed. Purpose: record candidate theses and the prior art they
must beat.

## Candidate thesis (headline)

Brading's local, law-constitutive presentism is the one presentism that does
not need a global foliation, so it escapes the Monton–Wüthrich debate about
presentism in quantum gravity. But it pays at the universe. Under her
conservation-under-isolation criterion, in general relativity the totality is
a genuine unity whose total energy is fixed by the Hamiltonian constraint and
which has no external evolution parameter. That is the "no present" case
(horn 4 in the four-option version of the trilemma). Then P1** is false or
undefined for the universe unless its quantifier is restricted to proper
subsystems. So GR physics, not textual gaps, forces the restriction, and the
restriction gives up her global claim.

Positive corollary: the restricted view (presents for subsystems relative to
internal clocks, none for the whole) has the same shape as relational quantum
dynamics (Page–Wootters and equivalent formalisms): a globally timeless state,
time relative to a clock subsystem. Brading's local presentism may be the
natural metaphysics of that physics, at the price of the global claim.

Which option holds depends on cosmology:

| Spacetime | Global conserved quantity for the totality | Horn |
|---|---|---|
| SR, compactly supported matter (Brading's stated setting) | total 4-momentum | universe is a unity; its present is W or a proper region (horns 1–2) |
| GR, asymptotically flat | ADM energy | as SR |
| GR, spatially closed | constrained to zero; whole is "frozen" | unity with no present (horn 4) |
| GR, open FLRW | no well-defined global quantity | criterion gives no verdict (horn 3a or 4) |

Each row is a claim to verify against GR sources before use.

## Update after full-text read of Wüthrich 2010

Kill test 1 passed (record: `sources.jsonl`, `wuthrich-2010-no-presentism-qg`).
Wüthrich predates Brading and defines presentism by an objective spatially
extended present (p. 261), which Brading rejects. He covers relativized
(Fine), point (Harrington) and past-light-cone (Stein) presents, not
dynamically individuated ones. The problem of time appears only in passing
(p. 260; p. 275 on loop quantum gravity). Nothing on the universe's own present
or on unity.

His p. 274 supplies a sharper argument. Reporting Isham (1991, p. 200), he
notes that the CMC reduction gives the universe a **time-dependent**
Hamiltonian, normally read as energy entering or leaving the system, "odd
indeed, as the system at stake is supposed to be the entire universe." That
yields a dilemma for the universe under Brading's own unity criterion
(conservation of total quantity of motion under isolation), for spatially
closed canonical GR:

- **Global time (CMC gauge):** the universe gets a global slice as its
  present (horn 2a), but its reduced Hamiltonian is time-dependent, so the
  conservation-under-isolation criterion fails for it. The present comes at
  the cost of the unity.
- **No gauge fixing (Hamiltonian constraint):** total energy is constrained
  to vanish and there is no evolution parameter. The universe can count as a
  conserved whole, but it has no present (horn 4).

Either the universe is a unity without a present, or it has a present but
fails the unity test. In both cases P1\*\* is not satisfied by a genuine
unity with a proper present. Status: conjecture. Scope: spatially closed,
CMC-sliceable spacetimes (Wüthrich notes the CMC approach is understood
mainly for the vacuum, spatially closed case, p. 271). To verify: read Isham
1991 itself; check whether every global-time gauge, not just CMC, gives a
time-dependent reduced Hamiltonian; and check whether Brading's criterion
needs the total quantity to be conserved or only defined.

## Update after full-text read of Monton (2005 preprint of 2006)

Also passed (record `monton-2006-presentism-qg`; preprint pagination). Monton
grants presentism is incompatible with SR and GR and rests it on fixed-foliation
quantum gravity: one hypersurface of a CMC (or Bohmian) foliation represents
the existing events (pp. 4-6). He calls relativized presentism "ad hoc and
unbelievable" (p. 6 n. 6), and allows emergent time (p. 20). No local presents,
no unity criterion, no universe-own-present case.

Use in the paper: Monton is exactly the horn-2a route (a global slice as the
universe's present). The new point is that this route, combined with Brading's
conservation-under-isolation criterion, costs the universe its unity
(Wüthrich p. 274, reporting Isham). So the dilemma joins two literatures that
have not met: the Monton-Wüthrich foliation debate and Brading's
law-constitutive local presentism. Brading's local view escapes Wüthrich's
Lorentz-symmetry objection to Monton, but meets the problem of time at the
universe.

## Update after reading Isham 1991 (printed pp. 192-202)

Record `isham-1991-conceptual-geometrical-qg`. Verified against page images.

1. **The quote is there, and broader than Wüthrich says.** p. 200, item 3a:
   a time-dependent Hamiltonian means energy can be fed into or taken out of
   the system; "a compact three-manifold Σ (the 'universe') has no external
   environment, and so the time-dependence is perhaps a little odd." It is
   stated for the general reduce-then-quantize approach (Sec. 5.2), shown in a
   closed FRW minisuperspace, not for CMC specifically. (The choice
   `t := π_a`, the momentum conjugate to the scale factor, is close to a
   mean-curvature time in FRW; that identification is ours, not Isham's.)
2. **Exception in his own example.** Eq. (5.2.8), matter time `t := φ`:
   `H_φ = ±(a²π_a²/12 + 12a⁴ − 2a⁶V(t))^{1/2}`. With `V = 0` (a free massless
   scalar clock) there is no explicit time dependence, so the reduced
   Hamiltonian is conserved. The universe then gets a global time **and** a
   conserved total quantity. The dilemma as stated earlier is false for
   deparametrizable models with an ideal clock field.
3. **Non-uniqueness.** Second item 3 (p. 200): there is no natural choice of
   time variable, and different choices need not give equivalent quantum
   theories. p. 196: for non-compact Σ the asymptotic structure might give an
   absolute time.

**Repaired dilemma (conjecture).** For a spatially closed universe in
canonical GR, a global present for the universe (horn 2a) either

- (i) uses a time whose reduced Hamiltonian is time-dependent, so Brading's
  conservation-under-isolation unity test fails for the universe; or
- (ii) uses an ideal clock (for example a free massless scalar), so the test
  can pass, but the present is fixed by the choice of a particular matter
  field. The dynamics does not select it uniquely (Isham p. 200), and
  different choices need not be equivalent.

Without gauge fixing, there is no evolution parameter (horn 4). Branch (ii)
is the defender's best route. It matters because Brading says the dynamics
fixes the present; here a choice of clock does. Whether a realistic universe
contains an ideal clock is a physics question we have not settled.

Next: check how the deparametrized models with a massless scalar or dust
clock (e.g. Brown–Kuchař dust; the massless scalar clock in loop quantum
cosmology) are treated in the literature, and whether "ideal clock" can be
made precise as "the time variable is cyclic in the reduced Hamiltonian".

## Prior art to beat (discovery level unless marked)

- **Monton 2006, "Presentism and quantum gravity"** (Dieks ed., *The Ontology
  of Spacetime*; PhilSci-Archive 2308). **Full text read (2005 preprint).**
  Presentism compatible with QG theories using a fixed (e.g. CMC) foliation.
  Global-present presentism; not Brading.
  https://philsci-archive.pitt.edu/2308/
- **Wüthrich 2010, "No presentism in quantum gravity"** (Petkov ed., *Space,
  Time, and Spacetime*). **Full text read.** Argues the CMC route fails. Same
  global target; see the update above.
  https://www.wuthrich.net/pub/WuthrichChristian2010PetkovColl_NoPresQG.pdf
- **Anderson, "A local resolution of the problem of time"** (arXiv:1809.01908
  and series). Abstract: "timelessness for the universe as a whole at the
  primary level with time being apparent ... in the parts", via Mach's Time
  Principle. Same whole/parts structure as the thesis, with no presentism.
  https://arxiv.org/abs/1809.01908
- **Höhn, Smith, Lock, "The trinity of relational quantum dynamics"**
  (arXiv:1912.00033). Equivalence of Dirac observables, Page–Wootters and
  deparametrization. Physics backbone of the positive corollary.
  https://arxiv.org/abs/1912.00033
- **Zero energy of closed universes**: arXiv gr-qc/9701028, 0803.0181,
  gr-qc/0511095 (pseudotensor and teleparallel frameworks; contested).
- **Quantum mereology** (second idea): Carroll–Singh arXiv:2005.12938;
  Loizeau et al. arXiv:2409.01391 (*Found. Phys.* 2024); PhilSci 29892
  (tensor-product mereology). None found citing Brading.
- Brading critique search 2024–2026: none found in this sweep (not exhaustive;
  PhilPapers full text not searched).

## Delta as currently understood

No source found links (i) Brading's law-constitutive unity criterion, (ii) its
application to the totality, and (iii) the Hamiltonian constraint. The
Monton–Wüthrich exchange concerns global-foliation presentism. Anderson states
the whole/parts timelessness structure without the existence question. The
candidate delta is the bridge, not any component.

## Kill tests before drafting

1. ~~Read Wüthrich 2010 in full.~~ Done: no Brading, no dynamical presents,
   no universe-own-present case. Passed.
2. Read Balaguer 2026 ch. 9 (the main unread scoop risk from the earlier audit).
3. Search Brading's own later work (2016 onward) for GR or the problem of time.
4. Check that her criterion is really conservation-based in a way that carries
   to GR (2013 p. 1105; 2015 p. 16); if she says it is SR or Newtonian only,
   the thesis becomes "the view does not extend to GR without loss".
5. Search the problem-of-time philosophy literature (Thébault, Gryb, Pooley,
   Huggett–Wüthrich) for "presentism" plus "relational time".

## Secondary ideas (kept)

- Quantum mereology makes Brading's "crucial question" precise: are there
  genuine subsystems picked out by the dynamics? (above sources)
- Strict isolation selects only the totality; approximate isolation suggests
  graded existence.
- Coverage and the universe case unify under "what exists are the genuine
  unities".
- Domain-of-dependence sizing gives a computable lower bound on a present.
