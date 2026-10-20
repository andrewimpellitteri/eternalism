#!/usr/bin/env python3
"""Finite next-post kernel for rank-only post factors.

For a post with inclusive past H, the next post's inclusive past J must have H
as its previous post past.  Any countably additive measure on the covariant
post algebra satisfies the laminar conservation identity

    nu(D_H) = sum_{J next from H} nu(D_J).

Under the rank-only rule nu(D_H)=kappa_n N(H)A_p(H), this becomes a linear
system for kappa_n.  This script computes the finite kernel

    S(H, J) = A_p(J)

over next-post pasts J up to size M, grouped by the unlabeled shape of H, and
compares the partial sums to N(H)A_p(H).  It is a finite diagnostic, not the
infinite identity.
"""
import sys
from itertools import permutations
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "experiments" / "baseline"))
import poscau  # noqa: E402

_CANON = {}
_NCOUNT = {}


def posts(rel, n):
    out = []
    for i in range(n):
        below = all((j, i) in rel for j in range(i))
        above = all((i, j) in rel for j in range(i + 1, n))
        if below and above:
            out.append(i)
    return out


def canon(rel, n):
    key = (rel, n)
    if key in _CANON:
        return _CANON[key]
    best = None
    for perm in permutations(range(n)):
        t = tuple(sorted((perm[i], perm[j]) for (i, j) in rel))
        if best is None or t < best:
            best = t
    _CANON[key] = best
    return best


def n_labelings(canon_form, n):
    key = (canon_form, n)
    if key in _NCOUNT:
        return _NCOUNT[key]
    count = 0
    for rel in poscau.causets(n):
        if canon(rel, n) == canon_form:
            count += 1
    _NCOUNT[key] = count
    return count


def representative(canon_form, n):
    for rel in poscau.causets(n):
        if canon(rel, n) == canon_form:
            return rel
    raise KeyError(canon_form)


def kernel(M, p):
    """Return {canon(H): (n, N(H), A(H), {m: sum A(J)})} for H up to M-1."""
    out = {}
    for m in range(2, M + 1):
        for J in poscau.causets(m):
            if not poscau.is_principal(J, m):
                continue
            ps = posts(J, m)
            if len(ps) < 2:
                continue
            pidx = ps[-2]                 # previous post (max is last)
            n = pidx + 1
            H = frozenset((i, j) for (i, j) in J if j <= pidx)
            cH = canon(H, n)
            if cH not in out:
                rep = representative(cH, n)
                out[cH] = {
                    "n": n,
                    "N": n_labelings(cH, n),
                    "A": poscau.amplitude(rep, n, p),
                    "sums": {},
                }
            out[cH]["sums"][m] = out[cH]["sums"].get(m, 0) + poscau.amplitude(J, m, p)
    return out


def report(M, p):
    print(f"p={p}; M={M}")
    data = kernel(M, p)
    for cH, d in sorted(data.items(), key=lambda kv: (kv[1]["n"], str(kv[0]))):
        target = d["N"] * d["A"]
        print(f"  H size {d['n']}: N={d['N']} A={d['A']:.6g} target N*A={target:.6g}")
        for m in sorted(d["sums"]):
            s = d["sums"][m]
            print(f"    J size {m}: sum A(J)={s:.6g}  ratio/target={s/target:.6g}" if abs(target) > 1e-12 else f"    J size {m}: sum A(J)={s:.6g} (target 0)")
    print()


if __name__ == "__main__":
    for p in (0.5, 0.5 + 0.5j, 0.2 + 0.7j):
        report(6, p)
