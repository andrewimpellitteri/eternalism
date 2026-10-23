# Rank-one history Hilbert space and the event-intersection boundary

Bounded sidecar, 22 October 2026. This note derives the history-Hilbert
quotient for the scalar decoherence functional

    D(E,F) = conjugate(nu(E)) nu(F)

and tests whether event intersection induces an operator on that quotient.
It does not derive the coordinator's pre/postselection cost, specify a
physical causal-set observer, or claim that scalar D fixes every observable.

## Primary construction and our rank-one specialization

Dowker, Johnston and Sorkin, “Hilbert Spaces from Path Integrals,”
[arXiv:1002.0589v2, Sec. 2.3, Eqs. (2.1)–(2.4)](https://arxiv.org/html/1002.0589v2#S2.SS3),
give the general construction. They start with the free complex vector space
on the event algebra, put the decoherence-functional form on it, quotient its
null vectors, and complete. Their Eq. (2.1) uses strong positivity to ensure
nonnegative norm; Eqs. (2.2)–(2.4) display degeneracy, quotient/completion,
and the resulting inner product. I read the cited primary section in full
text; this is a targeted section-level check, not an independent audit of
the paper's later particle-mechanics examples or physical interpretations.

Now let `A` be an event algebra and let `nu` be a finitely additive complex
measure on it with `nu(X)=1`. Assume the rank-one functional above. It is
Hermitian and bi-additive, and for any finite events `E_i` and coefficients
`a_i`,

    sum_(i,j) conjugate(a_i) D(E_i,E_j) a_j
      = |sum_i a_i nu(E_i)|^2 >= 0.

Thus it is strongly positive. Let `H_free` be the free complex vector space
with basis symbols `delta_E` for `E in A`; its elements have finite support.
For `u=sum_E u(E) delta_E`, define

    Phi_nu(u) = sum_E u(E) nu(E).

The induced form (linear in its second argument) is

    <u,v> = sum_(E,F) conjugate(u(E)) D(E,F) v(F)
           = conjugate(Phi_nu(u)) Phi_nu(v).

Its null space is exactly

    N = {u : Phi_nu(u)=0}.

The map `u+N -> Phi_nu(u)` is an isometry from `H_free/N` onto `C`:
surjectivity follows from `Phi_nu(delta_X)=nu(X)=1`. Therefore the quotient
is already complete and the completed history Hilbert space is one
dimensional. In particular, event vectors map as

    [delta_E] -> nu(E),
    <[delta_E],[delta_F]> = D(E,F),
    [delta_X] -> 1.

This dimension-one result is a statement about the Hilbert space generated
by this rank-one `D`; it is not a claim that an underlying physical system,
observer, or instrument has one dimension. Dowker–Johnston–Sorkin's
construction is general in `D`; rank one, the representing measure `nu`,
and normalization are the present specialization.

## Exact criterion for event intersection to descend

Fix an event `A` and define on the free space the linear map

    S_A(delta_E) = delta_(E intersect A).

It induces a well-defined map on `H_free/N` exactly when it sends every null
vector to a null vector. Equivalently,

    Phi_nu(u)=0  implies  Phi_nu(S_A u)=0 for all u in H_free.

Because `Phi_nu` is onto `C`, this kernel inclusion is equivalent to a scalar
factorization `Phi_nu composed with S_A = lambda_A Phi_nu` for some complex
`lambda_A`. Evaluating on `delta_X` fixes `lambda_A=nu(A)`. Thus the exact
criterion is

    nu(E intersect A) = nu(A) nu(E)  for every E in A.       (1)

This is both necessary and sufficient. If (1) holds, the descended map acts
as multiplication by `nu(A)` on the one-dimensional quotient. Taking `E=A`
in (1) gives `nu(A)=nu(A)^2`, so this scalar is either zero or one and the
descended map is an orthogonal projection: only `0` or `I` is possible. The
event-value test `nu(A) in {0,1}` alone is not sufficient; (1) must hold for
every `E`.

If `nu` is a finite countably additive complex measure on the full sigma
algebra, with variation measure `lambda=|nu|`, (1) has the sharper equivalent
form

    lambda(A)=0  or  lambda(A^c)=0.                       (2)

Indeed, if (1) holds and `nu(A)=0`, it says `nu(E intersect A)=0` for every
measurable `E`, so the restriction of `nu` to `A` is the zero measure and
`lambda(A)=0`. If `nu(A)=1`, it says `nu(E intersect A^c)=0` for every `E`,
so `lambda(A^c)=0`. Conversely, either variation-null side makes (1) hold.
Thus any descended event-intersection projection is trivial modulo the
variation measure. This conclusion uses the full measurable event algebra
and finite countable additivity; the general algebraic criterion (1) is the
appropriate statement without those measure assumptions.

For the completed matched pair, this also rules out the intersection map for
the intrinsic event `E2={exactly two minimal elements}`. The completed-event
amplitudes differ from their depth-three values `1/2` and `1/2-i/5` by less
than `tau<10^-8` (see the matched-pair `RESULT.md`). Hence both `nu_j(E2)` and
`nu_j(E2^c)=1-nu_j(E2)` are nonzero for each model. Since
`|nu_j(B)|<=lambda_j(B)`, both `lambda_j(E2)` and `lambda_j(E2^c)` are
positive. Neither side is variation-null, so condition (2) fails and
`S_E2` does not descend on the completed cylinder sigma algebra. This uses
the completed finite-measure extension and its event-amplitude bound; the
depth-three cancellation witness above is a separate finite certificate.

The null-space criterion is the correct test; assigning an operator by
intuition from classical indicator functions is not enough.

## Exact cancellation witness from the depth-three seed

Use the seven depth-three labelled cylinders in the matched scalar seed. Write
`F_3={M_3=2}` for the four-cylinder event in the first-three-birth history
algebra. Let `C_0` and `C_1` be the cylinders whose predecessor-mask codes are
respectively `(0,0,0)` and `(0,0,1)`. The exact finite recursion in
`research/agentic-philosophy/creativity-loop/pilot/check_access.py` gives, in
both seed models,

    nu(C_0) = nu(C_1) = (3+4i)/40.

Consequently `u=delta_(C_0)-delta_(C_1)` is a nonzero free vector in the null
space: `Phi_nu(u)=0`. But `C_0 intersect F_3` is empty and
`C_1 intersect F_3=C_1`, so

    Phi_nu(S_(F_3)u) = 0 - (3+4i)/40 != 0.

Hence `S_(F_3)` does not descend to the rank-one history-Hilbert quotient.
This is an exact cancellation witness, not a numerical near-cancellation.
It also shows why the one-dimensional quotient alone does not furnish a
membership operator for the event algebra. The witness uses the finite
depth-three seed and does not require the completed-history extension.

For comparison, the same seed has

    nu_A(F_3)=1/2,  nu_B(F_3)=1/2-i/5,
    D_A(F_3,F_3)=1/4, D_B(F_3,F_3)=29/100.

So the two rank-one decoherence functionals are not equal under this common
event identification, despite each constructed history Hilbert space being
abstractly isomorphic to `C`. Dimension equality is not an equivalence
preserving the named event vectors, much less a physical indistinguishability
result.

## Scope and evidence limits

- **Primary source:** Dowker–Johnston–Sorkin, arXiv:1002.0589v2, Sec. 2.3,
  Eqs. (2.1)–(2.4); targeted full-text read of that section. The paper supplies
  the general free-space/null-quotient/completion construction. The rank-one
  specialization, intersection criterion (1), and depth-three witness above
  are independently derived here.
- **Project evidence:** read `research/observer-access-audit/RESULT.md` and
  `INDEPENDENT_REVIEW.md`, `research/covariant-observer-witness/RESULT.md`,
  `research/observer-growth-channel/RESULT.md`, and
  `research/agentic-philosophy/creativity-loop/pilot/STATE_READOUT.md` as
  project artifacts. These distinguish finite event-membership access,
  coherent filters, channels, and auxiliary `L2(P0)` readouts. They are not
  primary-source evidence and are not re-certified by this sidecar.
- The equality of two history-Hilbert dimensions does not imply equal `D`,
  equal event vectors, equal detector statistics, or ontological equivalence.
  Conversely, failure of this particular event-intersection map does not
  prove that no alternative operator, dilation, or instrument can represent
  a related question. Those require additional structure and are outside
  this note.
- The listed finite cancellation tests descent on the labelled depth-three
  event algebra only. It is not a classification of all events, all
  completions, all physically accessible observables, or the unlabelled
  quotient. It makes no empirical or temporal-ontology claim.
