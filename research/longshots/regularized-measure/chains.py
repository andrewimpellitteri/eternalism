#!/usr/bin/env python3
"""Exact minimal-state chains for stem events of size <= 3 in CTP.

Reduction (proved in REPORT.md, Lemma 1): whether an unlabelled poset S with
|S| = k is a stem of C_n depends only on the induced order on the k-skeleton
K_n = {x : |past(x)| <= k-1}, and the skeleton evolves as an exact
marginal chain: a new element with past D joins K iff |D| <= k-1, with
amplitude p^{|max D|} q^{m-|D|}; all other transitions together have
amplitude 1 - (sum of the small ones) and leave K unchanged (the full
transition amplitudes sum to 1 identically in p).

For stems of size <= 3 even less is needed.  Five chains:
  A  state M = #minimal elements                      -> '1','2anti','3anti'
  B  state (M, has a 'top')                            -> '2chain','2chain+1'
     (a top is an element whose past is a single minimal element)
  C  state (M, T = #tops, 3chain flag)                 -> '3chain'
  D  state (M, V flag)                                 -> 'V'
  E  state (n0, n1, Lambda flag); n0/n1 = #minimal with 0 / 1 top -> 'Lambda'
Transitions at stage m (m elements present):
  D = {}                 amp q^m
  D = {x}, x minimal     amp p q^{m-1}       (x becomes / stays a top base)
  D = {x<y}, y a top     amp p q^{m-2}
  D = {x,y} two minima   amp p^2 q^{m-2}
  other                  amp 1 - (sum of the above available moves)
The ring R is GQ (exact Gaussian rationals at a numerical p) or Poly
(integer polynomials in p, for exact cross-check with the enumeration).
"""
from collections import defaultdict


def _powers(q, N, R):
    out = [R.one()]
    for _ in range(N + 1):
        out.append(out[-1] * q)
    return out


def chain_sequences(p, N, R):
    """Return dict stem -> [a_1..a_N] (index n-1) in ring R."""
    one = R.one()
    q = one - p
    qp = _powers(q, N, R)
    p2 = p * p
    seq = {s: [] for s in ['1', '2anti', '3anti', '2chain', '2chain+1', '3chain', 'V', 'Lambda']}

    # stage 1: one minimal element
    A = {1: one}
    B = {(1, False): one}
    C = {(1, 0, False): one}
    D = {(1, False): one}
    E = {(1, 0, False): one}

    def record(n):
        z = R.zero()
        s1 = z; s2a = z; s3a = z
        for M, w in A.items():
            s1 = s1 + w
            if M >= 2: s2a = s2a + w
            if M >= 3: s3a = s3a + w
        s2c = z; s21 = z
        for (M, t), w in B.items():
            if t:
                s2c = s2c + w
                if M >= 2: s21 = s21 + w
        s3c = z
        for (M, T, f), w in C.items():
            if f: s3c = s3c + w
        sV = z
        for (M, f), w in D.items():
            if f: sV = sV + w
        sL = z
        for (n0, n1, f), w in E.items():
            if f: sL = sL + w
        for k, v in (('1', s1), ('2anti', s2a), ('3anti', s3a), ('2chain', s2c),
                     ('2chain+1', s21), ('3chain', s3c), ('V', sV), ('Lambda', sL)):
            seq[k].append(v)

    record(1)
    for m in range(1, N):            # m elements present -> m+1
        a_empty = qp[m]
        a_single = p * qp[m - 1]
        a_chain2 = p * qp[m - 2] if m >= 2 else R.zero()
        a_anti2 = p2 * qp[m - 2] if m >= 2 else R.zero()

        def add(dct, key, val):
            if key in dct:
                dct[key] = dct[key] + val
            else:
                dct[key] = val

        nA = {}
        for M, w in A.items():
            add(nA, M + 1, w * a_empty)
            add(nA, M, w * (one - a_empty))
        A = nA

        nB = {}
        for (M, t), w in B.items():
            add(nB, (M + 1, t), w * a_empty)
            add(nB, (M, True), w * (a_single * M))
            add(nB, (M, t), w * (one - a_empty - a_single * M))
        B = nB

        nC = {}
        for (M, T, f), w in C.items():
            add(nC, (M + 1, T, f), w * a_empty)
            add(nC, (M, T + 1, f), w * (a_single * M))
            if T:
                add(nC, (M, T, True), w * (a_chain2 * T))
            add(nC, (M, T, f), w * (one - a_empty - a_single * M - a_chain2 * T))
        C = nC

        nD = {}
        for (M, f), w in D.items():
            pairs = M * (M - 1) // 2
            add(nD, (M + 1, f), w * a_empty)
            if pairs:
                add(nD, (M, True), w * (a_anti2 * pairs))
            add(nD, (M, f), w * (one - a_empty - a_anti2 * pairs))
        D = nD

        nE = {}
        for (n0, n1, f), w in E.items():
            add(nE, (n0 + 1, n1, f), w * a_empty)
            if n0:
                add(nE, (n0 - 1, n1 + 1, f), w * (a_single * n0))
            if n1:
                add(nE, (n0, n1 - 1, True), w * (a_single * n1))
            # minimal elements already having >=2 tops: (M - n0 - n1) of them
            add(nE, (n0, n1, f), w * (one - a_empty - a_single * (n0 + n1)))
        # note: in E, single-element pasts on a minimal with >=2 tops are in
        # the 'stay' amplitude, consistent with the stay formula above.
        E = nE
        record(m + 1)
    return seq
