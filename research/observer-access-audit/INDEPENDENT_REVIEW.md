# Independent review: finite observer channels and completed-history covariance

This review independently checks the finite operator claim and the specified
four-element relabeling example. It is a bounded mathematical correspondence
audit. It does not derive a physical observer, establish novelty, or supply a
quantum measure on completed causal sets.

## Findings

Let the finite history Hilbert space have orthonormal basis `|C>` and let
`E` be a nonempty union of finite isomorphism classes. Write

\[
D_E=\sum_{C\in E}|C\rangle\langle C|,\qquad
|u_E\rangle=\sum_{C\in E}|C\rangle,\qquad
Q_E=|u_E\rangle\langle u_E|/m,\quad m=|E|.
\]

`D_E` is the diagonal membership effect. `Q_E` is the normalized rank-one
coherent effect. They encode different questions: for a pure state with
coordinates `a_C`, their probabilities are respectively
`sum_{C in E}|a_C|^2` and `|sum_{C in E}a_C|^2/m`.

Let `Pi_b` project onto the span of histories in isomorphism class `b`. For
the channels in the task, direct trace-duality gives

\[
\Delta^*(X)=\sum_b\Pi_bX\Pi_b,\qquad
\mathrm{im}(\Delta^*)=\bigoplus_b\mathcal B(\Pi_b\mathcal H),
\]

and, for the classical class register,

\[
\Gamma^*(Y)=\sum_b\langle b|Y|b\rangle\Pi_b,\qquad
\mathrm{im}(\Gamma^*)=\mathrm{span}\{\Pi_b\}.
\]

The first image consists of all block-diagonal operators and preserves
coherence inside a class while deleting coherence between classes. The second
image consists only of operators constant on each class block; `Gamma` also
discards all within-class coherence. Since `E` is a union of classes,
`D_E=sum_{b subset E} Pi_b` belongs to both images. When `E` meets two or
more classes, `Q_E` has nonzero off-block matrix entries, so it is not in
either image. Thus recognizing the finite shape event does not preserve its
coherent filter under either channel.

This is an exact all-input statement: an output effect implements an input
effect `T` for every state exactly when its adjoint image is `T`, by
`Tr(F C(rho))=Tr(C^*(F)rho)` and separation of Hermitian operators by density
matrices.

## Exact three-element check

I independently enumerated the seven naturally labeled three-element posets
using past masks, requiring each birth precursor to be a down-set. With `L`
the number of covers and `h` the number of incomparable unordered pairs, the
two event members for `(L-h) mod 8 in {0,1}` are

| Past masks | Shape | `L` | `h` | Residue | `p^L q^h` |
|---|---|---:|---:|---:|---|
| `(0,0,3)` | two minima below a common maximum | 2 | 1 | 1 | `(1+i)/4` |
| `(0,1,1)` | one minimum below two maxima | 2 | 1 | 1 | `(1+i)/4` |

Here `p=(1+i)/2` and `q=(1-i)/2`. The selected shapes are distinct
isomorphism classes and each has exactly one naturally labeled representative
at this level. Hence `m=2`, the coherent amplitude sum is `(1+i)/2`, and its
squared modulus is `1/2`. The event membership effect and coherent effect are
therefore

\[
D_E=|V\rangle\langle V|+|\Lambda\rangle\langle\Lambda|,
\quad
Q_E=\tfrac12(|V\rangle+|\Lambda\rangle)(\langle V|+\langle\Lambda|).
\]

For an exact identical-output witness, put
`|psi_±>=(|V> ± |Lambda>)/sqrt(2)` and `rho_±=|psi_±><psi_±|`. Each
occupied class is a singleton, so these vectors are invariant under
permutations within their respective finite isomorphism classes. Both
channels give the same output on the two states: `Delta(rho_±)` is the
diagonal mixture with weights `1/2,1/2`, and `Gamma(rho_±)` assigns class
probability `1/2` to each of `V` and `Lambda`. Yet

\[
\mathrm{Tr}(Q_E\rho_+)=1,\qquad
\mathrm{Tr}(Q_E\rho_-)=0.
\]

For comparison, `Tr(D_E rho_+)=Tr(D_E rho_-)=1`. This pair proves that no
measurement on either channel output can reproduce `Q_E` on all inputs. It
also keeps the distinction between the membership effect and the coherent
filter visible without relying on a large-level computation.

As an additional check on the phase-aligned preparation, the seven-history
state with amplitudes `p^L q^h` is normalized: the squared norms by shape are
`1/8` for the antichain, `1/8` for each of the three one-link labeled
histories, `1/8` for each of `V, Lambda`, and `1/4` for the chain. For this
preparation, `Tr(D_E rho)=1/4` and `Tr(Q_E rho)=1/4`; after class pinching,
`Tr(Q_E Delta(rho))=1/8`. The equality of the first two values before
pinching is specific to these equal aligned amplitudes and does not make the
effects equal.

## Completed-history relabeling check

Interpret each tuple as the predecessor bit masks of a naturally labeled
causet. The tuple `(0,0,3,0)` has relations `0<2, 1<2`, with element 3
isolated. The tuple `(0,0,0,3)` has relations `0<3, 1<3`, with element 2
isolated. Exchanging labels 2 and 3 is an order isomorphism. Appending to
each the same chain of universal tops gives two natural labelings of one
countable, past-finite completed causet; extend the isomorphism by fixing each
new top.

The first three births in the first enumeration form the two-minima/common-top
shape, with `(L,h)=(2,1)` and residue 1, so the event holds. The first three
births in the second form an antichain, with `(L,h)=(0,3)` and residue 5, so
the event fails. Therefore this finite-prefix event is not invariant under
relabeling of the completed causet. The finite-level phase event remains
isomorphism-invariant at a fixed level; that fact does not make its
enumeration-selected cylinder event covariant on completed histories.

## Source boundary and limitations

I checked the primary source definitions directly. Brightwell, Dowker, García,
Henson, and Sorkin, *“Observables” in causal set cosmology*,
[arXiv:gr-qc/0210061v2](https://arxiv.org/html/gr-qc/0210061v2), full-text
read for this definition: Section 2 defines a covariant question by
relabeling-invariance of a set of completed labeled causets (see also the
formal criterion in Section 2); Section 3 defines a stem event existentially
over natural labelings. The tested event instead fixes the first three birth
labels, so it is not that stem event.

Mozota Frauca and Sorkin, *How to Measure the Quantum Measure*,
[arXiv:1610.02087v1](https://arxiv.org/html/1610.02087v1), Section 5.2,
Eqs. (42)–(46), full text checked for this construction: their event filter
uses the equal-weight ancilla superposition, and Eq. (43) retains a
final-system endpoint Kronecker delta. The `Q_E` used here is the simpler
rank-one finite-register target explicitly specified in this audit; it is not
a derivation of their more general instrument or its endpoint-sensitive
measure.

The algebra and finite enumeration were checked independently with a short,
standard-library-only calculation using exact rational complex pairs and
permutation-based isomorphism canonicalization. No packages were installed,
no large computation was run, and no shared checker or source was edited.
There is no claim here about an infinite-level limit, a physical observer's
available instrument, or a quantum measure on the completed causal set.
