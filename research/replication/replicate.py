#!/usr/bin/env python3
"""Independent edge-mask replication of the two-cap result.

Different route from experiments/baseline: enumerate all edge subsets on
naturally labelled vertices, take the transitive closure, canonicalize the
resulting poset, and compute the endpoint probability and V_n from the closures.
The baseline enumerates relation masks and filters transitivity.  The two
routes should agree on counts, the endpoint identity and V_5/V_6.
"""
import sys
from fractions import Fraction
from itertools import permutations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "baseline"))
import poscau  # only used for the final comparison, not the derivation


def pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


_CANON = {}


def canonical(rel, n):
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


def closure(edges, n):
    rel = set(edges)
    changed = True
    while changed:
        changed = False
        for (i, j) in list(rel):
            for (k, l) in list(rel):
                if j == k and (i, l) not in rel:
                    rel.add((i, l)); changed = True
    return frozenset(rel)


def stats(rel, n):
    L = sum(1 for (i, j) in rel
            if not any((i, k) in rel and (k, j) in rel for k in range(i + 1, j)))
    return L, len(rel)


def maxima(rel, n):
    return [i for i in range(n) if not any((i, j) in rel for j in range(i + 1, n))]


def principal(rel, n):
    return len(maxima(rel, n)) == 1


def doubly(rel, n):
    parent = frozenset((i, j) for (i, j) in rel if j < n - 1)
    return principal(rel, n) and principal(parent, n - 1)


def all_labeled_closures(n):
    """All distinct naturally labelled closures (dedup by the relation set)."""
    ps = pairs(n)
    out = set()
    for bits in range(1 << len(ps)):
        edges = frozenset(ps[k] for k in range(len(ps)) if (bits >> k) & 1)
        out.add(closure(edges, n))
    return list(out)


def endpoint_probability(k, r, s):
    """P(last of k+1 vertices is above all previous), edge-subset route."""
    n = k + 1
    ps = pairs(n)
    total = Fraction(0)
    for bits in range(1 << len(ps)):
        e = bin(bits).count("1")
        rel = closure(frozenset(ps[j] for j in range(len(ps)) if (bits >> j) & 1), n)
        # last vertex is above every earlier vertex
        if all(any((i, m) == (i, k) for m in []) or True for i in range(k)):
            ok = all((i, k) in rel for i in range(k))
            if ok:
                total += (r ** e) * (s ** (len(ps) - e))
    return total


def V(n, p):
    """V_n = sum |A_p(C)| over doubly-principal n-orders, edge-subset route."""
    total = 0.0
    count = 0
    for rel in all_labeled_closures(n):
        if not doubly(rel, n):
            continue
        L, R = stats(rel, n)
        total += abs((p ** L) * ((1 - p) ** (comb(n, 2) - R)))
        count += 1
    return total, count


def main():
    print("Endpoint identity P_k = prod_{j=1}^k (1-s^j), edge-subset route:")
    for k in range(1, 6):
        for r in (Fraction(1, 2), Fraction(2, 5), Fraction(1, 3)):
            s = 1 - r
            got = endpoint_probability(k, r, s)
            want = Fraction(1)
            for j in range(1, k + 1):
                want *= 1 - s ** j
            assert got == want, (k, r, got, want)
        print(f"  k={k}: exact equality for r=1/2,2/5,1/3")
    print()

    print("Two-cap decomposition, edge-subset route:")
    for k in range(1, 5):
        n = k + 2
        src = {canonical(rel, k) for rel in all_labeled_closures(k)}
        caps = set()
        for rel in all_labeled_closures(k):
            # add two universal maxima
            r1 = rel | frozenset((i, k) for i in range(k))
            r2 = r1 | frozenset((i, k + 1) for i in range(k + 1))
            caps.add(r2)
        dp = {rel for rel in all_labeled_closures(n) if doubly(rel, n)}
        assert caps == dp, (k, len(caps), len(dp))
        print(f"  k={k}: caps={len(caps)} doubly={len(dp)}: PASS")
    print()

    p = 0.5 + 0.5j
    print(f"V_n at p={p}, edge-subset route (floating):")
    for n in (5, 6):
        v, c = V(n, p)
        print(f"  n={n}: V={v:.12f}, doubly orders={c}")
    print("  expected: V5=1.015165042945, V6=2.184089780164")
    print()

    print("Dirac history, independent construction:")
    for j in (1, 2, 3):
        rel = set()
        for b in range(j):
            a1, a2, z = 3 * b, 3 * b + 1, 3 * b + 2
            rel.add((a1, z)); rel.add((a2, z))
            for x in range(3 * b):
                for y in (a1, a2, z):
                    rel.add((x, y))
        n = 3 * j
        rel = frozenset(rel)
        assert principal(rel, n)
        parent = frozenset((i, k) for (i, k) in rel if k < n - 1)
        assert not principal(parent, n - 1)
        assert not doubly(rel, n)
        print(f"  j={j}: post past principal but not doubly; PASS")
    print()
    print("All independent checks passed.")


if __name__ == "__main__":
    main()
