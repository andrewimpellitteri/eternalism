#!/usr/bin/env python3
"""Order-reversal test for classical sequential growth (CSG) of causal sets.

Standard library only.  Exact rational arithmetic.

What it does, for n = 1..N (default N = 6):
  * enumerates every naturally labelled causal set on n elements by growing
    them one birth at a time (the new element's past is any down-set, "stem",
    of the parent), with the Rideout-Sorkin transition probability
        alpha = lambda(w, m) / lambda(n, 0),
        lambda(w, m) = sum_{k=m..w} C(w-m, k-m) t_k            (their eq. 12/17)
    where w = size of the new element's past, m = number of its maximal
    elements, n = size of the parent;
  * checks the counts against the known numbers of labelled and unlabelled
    posets, that probabilities sum to 1, and discrete general covariance
    (all natural labellings of one order have equal probability);
  * sums labelled probabilities to unlabelled orders (isomorphism classes);
  * compares each order with its dual (order reversed).

Usage:  python3 growth_reversal.py [N]      (N = 7 takes a few minutes)
"""
import sys
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial, log2

# ---------------------------------------------------------------- posets
# A naturally labelled poset on {0..n-1} is a tuple `past`, past[i] a bitmask
# of the elements below i (transitively closed, all bits < i).


def stems(past):
    """All down-sets of the poset, as bitmasks."""
    n = len(past)
    out = [0]
    for i in range(n):  # add element i to every down-set that contains past[i]
        out += [s | (1 << i) for s in out if s & past[i] == past[i]]
    return out


def n_maximal(past, s):
    """Number of maximal elements of the down-set s."""
    below = 0
    for i in range(len(past)):
        if s >> i & 1:
            below |= past[i]
    return bin(s & ~below).count("1")


def canon(n, rel):
    """Canonical form of the poset with strict relation rel (set of (a,b), a<b).
    Minimum over relabellings that respect an isomorphism-invariant colouring."""
    dn = [0] * n
    up = [0] * n
    for a, b in rel:
        dn[b] |= 1 << a
        up[a] |= 1 << b
    col = [(bin(dn[i]).count("1"), bin(up[i]).count("1")) for i in range(n)]
    col = [(col[i],
            tuple(sorted(col[j] for j in range(n) if dn[i] >> j & 1)),
            tuple(sorted(col[j] for j in range(n) if up[i] >> j & 1)))
           for i in range(n)]
    classes = {}
    for i in range(n):
        classes.setdefault(col[i], []).append(i)
    groups = [classes[k] for k in sorted(classes)]
    best = None
    for combo in product(*[permutations(g) for g in groups]):
        order = [x for g in combo for x in g]
        pos = [0] * n
        for p, x in enumerate(order):
            pos[x] = p
        key = tuple(sorted((pos[a], pos[b]) for a, b in rel))
        if best is None or key < best:
            best = key
    return (n, best)


def relation(past):
    return {(a, b) for b in range(len(past)) for a in range(b) if past[b] >> a & 1}


def dual_canon(n, rel):
    return canon(n, {(b, a) for a, b in rel})


# ---------------------------------------------------------------- dynamics

def lam(t, w, m):
    return sum(comb(w - m, k - m) * t(k) for k in range(m, w + 1))


def csg(t):
    """Generic Rideout-Sorkin dynamics with couplings t(k), t(0) = 1."""
    def alpha(past, s):
        n = len(past)
        w = bin(s).count("1")
        return F(lam(t, w, n_maximal(past, s)), lam(t, n, 0))
    return alpha


def originary_percolation(p):
    """Percolation in which every element after the first has an ancestor
    (Rideout-Sorkin sec. 4: extra factor 1/(1-q^n) at stage n)."""
    q = 1 - p
    def alpha(past, s):
        n = len(past)
        if n == 0:
            return F(1)
        if s == 0:
            return F(0)
        w = bin(s).count("1")
        return p ** n_maximal(past, s) * q ** (n - w) / (1 - q ** n)
    return alpha


def grow(alpha, N):
    """Yield, for n = 1..N, the dict {labelled poset: probability}."""
    level = {(): F(1)}
    for _ in range(N):
        nxt = {}
        for past, pr in level.items():
            for s in stems(past):
                a = alpha(past, s)
                if a:
                    nxt[past + (s,)] = pr * a  # each labelled poset arises once
        level = nxt
        yield level


LABELLED = [1, 1, 2, 7, 40, 357, 4824, 96428]   # OEIS A006455
UNLABELLED = [1, 1, 2, 5, 16, 63, 318, 2045]    # OEIS A000112

_cache = {}


def classify(past):
    if past not in _cache:
        n = len(past)
        rel = relation(past)
        _cache[past] = (canon(n, rel), dual_canon(n, rel))
    return _cache[past]


def report(name, alpha, N, generic=True, condition=None):
    print(f"\n== {name}")
    print("  n  orders  self-dual  max|mu(C)-mu(C*)|   total variation   KL(mu||mu*) bits")
    for n, level in enumerate(grow(alpha, N), start=1):
        assert sum(level.values()) == 1
        if generic and all(level.values()):
            assert len(level) == LABELLED[n]
        mu, per_label = {}, {}
        for past, pr in level.items():
            c, _ = classify(past)
            if condition and not condition(past):
                continue
            mu[c] = mu.get(c, 0) + pr
            # discrete general covariance: one value per order
            assert per_label.setdefault(c, pr) == pr
        if generic and all(level.values()) and not condition:
            assert len(mu) == UNLABELLED[n]
        tot = sum(mu.values())
        if tot == 0:
            continue
        dual = {}
        for past in level:
            c, d = classify(past)
            dual[c] = d
        mu = {c: v / tot for c, v in mu.items()}
        diffs = [abs(v - mu.get(dual[c], 0)) for c, v in mu.items()]
        # orders whose dual is outside the support
        missing = sum(v for c, v in mu.items() if mu.get(dual[c], 0) == 0)
        tv = sum(diffs) / 2
        if missing:
            kl = "infinite"
        else:
            kl = "%.6f" % sum(float(v) * log2(float(v) / float(mu[dual[c]]))
                              for c, v in mu.items() if v)
        selfdual = sum(1 for c in mu if dual[c] == c)
        print(f"  {n}  {len(mu):6d}  {selfdual:9d}  {str(max(diffs)):>18s}  "
              f"{float(tv):17.6f}   {kl}")


def antichain_test(t, N):
    """Proposition A: the order 'n-antichain under one top' has probability
    proportional to t_n, its dual 'one bottom under an n-antichain' to t_1^n."""
    for n in range(2, N):
        alpha = csg(t)
        top = tuple([0] * n + [(1 << n) - 1])
        bot = tuple([0] + [1] * n)
        level = None
        for level in grow(alpha, n + 1):
            pass
        ratio = level[top] / level[bot] if level[bot] else None
        expect = F(t(n), t(1) ** n) if t(1) else None
        assert ratio == expect
        print(f"   n={n}: mu(top over antichain)/mu(antichain over bottom) = {ratio}"
              f"  (= t_n / t_1^n)")


def has_bottom_and_top(past):
    n = len(past)
    full = (1 << (n - 1)) - 1
    if past[-1] != full:               # last-born is above everything
        return False
    return all(p & 1 for p in past[1:])  # element 0 is below everything


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    for p in (F(1, 2), F(1, 3), F(3, 4)):
        t = p / (1 - p)
        report(f"transitive percolation p = {p}", csg(lambda k, t=t: t ** k), N)
    report("t_n = 1/n!  (Rideout-Sorkin's 'more lifelike choice')",
           csg(lambda k: F(1, factorial(k))), N)
    report("forest: t_0 = t_1 = 1, others 0",
           csg(lambda k: F(1) if k < 2 else F(0)), N, generic=False)
    report("t_n = 1 for all n", csg(lambda k: F(1)), N)
    report("t = (1, 1, 2, 3, 5, 8, ...) arbitrary",
           csg(lambda k: F([1, 1, 2, 3, 5, 8, 13, 21][k])), N)
    report("originary percolation p = 1/2", originary_percolation(F(1, 2)), N,
           generic=False)
    report("originary percolation p = 1/2, conditioned on a top element too "
           "(the order between two posts, endpoints included)",
           originary_percolation(F(1, 2)), N, generic=False,
           condition=has_bottom_and_top)
    report("percolation p = 1/2 conditioned on bottom and top",
           csg(lambda k: F(1)), N, condition=has_bottom_and_top)
    report("t_n = 1/n! conditioned on bottom and top",
           csg(lambda k: F(1, factorial(k))), N, condition=has_bottom_and_top)
    print("\n== Proposition A check (exact)")
    for name, t in (("percolation p=1/3", lambda k: F(1, 2) ** k),
                    ("t_n = 1/n!", lambda k: F(1, factorial(k))),
                    ("t_n = 1", lambda k: F(1))):
        print("  ", name)
        antichain_test(t, min(N, 6))
    print("\nall assertions passed")


if __name__ == "__main__":
    main()
