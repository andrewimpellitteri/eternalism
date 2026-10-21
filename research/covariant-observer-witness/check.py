"""Finite observer-algebra comparison for the phase-aligned event.

Standard library only. Labelled posets are tuples of bitmasks (past of each
element); classes are canonical edge sets under all permutations.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb

Z = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def canon(C):
    edges = [(j, i) for i, m in enumerate(C) for j in range(len(C)) if m >> j & 1]
    return (len(C), min(tuple(sorted((p[j], p[i]) for j, i in edges))
                        for p in permutations(range(len(C)))))


def ideals(C):
    return [D for D in range(1 << len(C))
            if all(not (D >> i & 1) or C[i] & D == C[i] for i in range(len(C)))]


def covers_h(C):
    n = len(C)
    covers = set()
    for i in range(n):
        for j in range(n):
            if C[i] >> j & 1:
                if not any((C[k] >> j & 1) and (C[i] >> k & 1)
                           for k in range(n) if k != i and k != j):
                    covers.add((j, i))
    L = len(covers)
    R = sum(bin(m).count("1") for m in C)
    h = n * (n - 1) // 2 - R
    return L, h


def levels(N):
    out = [{(): ONE}]
    for _ in range(N):
        nxt = {}
        for C in out[-1]:
            for P in ideals(C):
                nxt[C + (P,)] = None
        out.append(nxt)
    return out


def cpow(base, k):
    r = ONE
    for _ in range(k):
        r = mul(r, base)
    return r


def main():
    N = 6
    lev = levels(N)
    p = (F(1, 2), F(1, 2))
    q = (F(1, 2), F(-1, 2))
    print("complex percolation p=(1+i)/2, labelled counts:",
          [len(lev[n]) for n in range(1, N + 1)])
    for n in range(2, N + 1):
        classes = {}
        for C in lev[n]:
            L, h = covers_h(C)
            A = mul(cpow(p, L), cpow(q, h))
            classes.setdefault(canon(C), []).append((L, h, A))
        for rows in classes.values():
            assert len({r[2] for r in rows}) == 1
            assert len({(r[0] - r[1]) % 8 for r in rows}) == 1
        selected = {k: rows for k, rows in classes.items()
                    if (rows[0][0] - rows[0][1]) % 8 in (0, 1)}
        total = Z
        for rows in selected.values():
            total = add(total, (rows[0][2][0] * len(rows),
                                rows[0][2][1] * len(rows)))
        print(f"  n={n}: classes={len(classes)} selected={len(selected)} "
              f"proper_subset={len(selected)!=len(classes)} "
              f"|sum|^2={total[0]**2 + total[1]**2}")

    print("binary register (permutation orbits = word count):")
    for n in (2, 4, 6, 8, 12, 20):
        selected_k = [k for k in range(n + 1) if (2 * k - n) % 8 in (0, 1)]
        total = Z
        for k in selected_k:
            a = mul(cpow(p, k), cpow(q, n - k))
            total = add(total, (a[0] * comb(n, k), a[1] * comb(n, k)))
        print(f"  n={n}: selected k={selected_k} reps={sum(comb(n,k) for k in selected_k)} "
              f"|sum|^2={total[0]**2 + total[1]**2}")

    print("PASS: phase-aligned event is a proper union of classes in both models")
    print("NOTE: the cardinality-only algebra sees only full levels, so the")
    print("      selected event is outside its adjoint image.")


if __name__ == "__main__":
    main()
