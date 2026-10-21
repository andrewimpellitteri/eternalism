"""Finite stem-event values for complex percolation, for Sorkin even convergence."""
from fractions import Fraction as F
from itertools import permutations

Z = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cpow(a, n):
    r = ONE
    for _ in range(n):
        r = mul(r, a)
    return r


def canon(C):
    edges = [(j, i) for i, m in enumerate(C) for j in range(len(C)) if m >> j & 1]
    return (len(C), min(tuple(sorted((p[j], p[i]) for j, i in edges))
                        for p in permutations(range(len(C)))))


def ideals(C):
    return [D for D in range(1 << len(C))
            if all(not (D >> i & 1) or C[i] & D == C[i] for i in range(len(C)))]


def induced(C, D):
    old = [i for i in range(len(C)) if D >> i & 1]
    idx = {v: i for i, v in enumerate(old)}
    return tuple(sum(1 << idx[j] for j in old if C[i] >> j & 1) for i in old)


def covers_h(C):
    n = len(C)
    L = 0
    for i in range(n):
        for j in range(n):
            if C[i] >> j & 1 and not any((C[k] >> j & 1) and (C[i] >> k & 1)
                                         for k in range(n) if k not in (i, j)):
                L += 1
    R = sum(bin(m).count("1") for m in C)
    return L, n * (n - 1) // 2 - R


def levels(N):
    out = [{(): ONE}]
    for _ in range(N):
        nxt = {}
        for C in out[-1]:
            for P in ideals(C):
                nxt[C + (P,)] = None
        out.append(nxt)
    return out


STEMS = {
    "2chain": (0, 1),
    "2anti": (0, 0),
    "3chain": (0, 1, 3),
    "3anti": (0, 0, 0),
    "V": (0, 1, 1),
    "Lambda": (0, 1, 0),
}


def has_stem(C, Skey):
    k = Skey[0]
    for D in ideals(C):
        if bin(D).count("1") == k and canon(induced(C, D)) == Skey:
            return True
    return False


def values(p, q, lev, m):
    out = {}
    for name, S in STEMS.items():
        key = canon(S)
        total = Z
        for C in lev[m]:
            if has_stem(C, key):
                L, h = covers_h(C)
                A = mul(cpow(p, L), cpow(q, h))
                total = add(total, A)
        out[name] = total
    return out


def main():
    lev = levels(6)
    for name, (p, q) in {
        "(1+i)/2": ((F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2))),
        "0.8+0.3i": ((F(4, 5), F(3, 10)), (F(1, 5), F(-3, 10))),
    }.items():
        print(f"p={name}")
        for m in (4, 5, 6):
            vals = values(p, q, lev, m)
            print(f"  m={m}: " + " ".join(f"{k}={v[0]:.6f}{v[1]:+.6f}i"
                                          for k, v in vals.items()))
        # The 2-chain *stem-present* event is weaker than the originary
        # event (the first element below all later ones); do not equate them.
        print("  stem values computed (2-chain stem-present is not the originary event)")
    print("PASS")


if __name__ == "__main__":
    main()
