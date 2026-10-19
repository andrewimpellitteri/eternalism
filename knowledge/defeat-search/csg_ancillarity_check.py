"""Finite exact check of the RC-4 ancillarity argument (coordinator, 2026-10-19).

Claim tested (domain: causal sets with n <= N elements, exact rational arithmetic):
for classical sequential growth with Rideout-Sorkin transition probabilities
    tau(I) = lambda(w, m) / lambda(n, 0),   lambda(w, m) = sum_{k=m}^{w} C(w-m, k-m) t_k
(w = size of the new element's past I, m = number of maximal elements of I),
 (a) every naturally labelled causet in one isomorphism class has the same probability
     (path independence), so
 (b) given the final unlabelled causet C, the labelled outcome is uniform over the
     distinct natural labellings of C, and any label-dependent statistic has a
     conditional law that does not depend on the couplings t_k.
Contrast: a label-dependent growth law (weights depend on the birth index) breaks (a),
and the conditional law of the same statistic then depends on the parameter.

This is a finite-domain check, not a general theorem. Standard library only.
Run: python3 -I knowledge/defeat-search/csg_ancillarity_check.py
"""
from fractions import Fraction
from itertools import permutations
from math import comb
from collections import defaultdict

N = 5


def maximal(ideal, past):
    return [j for j in ideal if not any(j in past[k] for k in ideal if k != j)]


def ideals(past, n):
    """All down-closed subsets of the n existing elements."""
    out = []
    for mask in range(1 << n):
        s = frozenset(i for i in range(n) if mask >> i & 1)
        if all(past[j] <= s for j in s):
            out.append(s)
    return out


def lam(w, m, t):
    return sum(comb(w - m, k - m) * t[k] for k in range(m, w + 1))


def taus(past, n, t, bias=None):
    """Transition probabilities from an n-element causet to each possible new past."""
    ids = ideals(past, n)
    ws = []
    for I in ids:
        base = lam(len(I), len(maximal(I, past)), t)
        if bias is not None:
            base *= bias(n, I)
        ws.append(base)
    tot = sum(ws)
    return [(I, w / tot) for I, w in zip(ids, ws)]


def grow(t, nmax, bias=None):
    """Exact distribution over naturally labelled causets, stage by stage."""
    stages = [{(): Fraction(1)}]
    for n in range(nmax):
        nxt = defaultdict(Fraction)
        for pasts, pr in stages[-1].items():
            past = [frozenset(p) for p in pasts]
            for I, tau in taus(past, n, t, bias):
                nxt[pasts + (tuple(sorted(I)),)] += pr * tau
        stages.append(dict(nxt))
    return stages


def canon(pasts):
    n = len(pasts)
    rel = {(j, i) for i in range(n) for j in pasts[i]}
    best = None
    for perm in permutations(range(n)):
        r = tuple(sorted((perm[a], perm[b]) for a, b in rel))
        if best is None or r < best:
            best = r
    return (n, best)


def classes(dist):
    cl = defaultdict(list)
    for pasts, pr in dist.items():
        cl[canon(pasts)].append((pasts, pr))
    return cl


def above(pasts, i, j):
    """Statistic S: element i is above element j (j in past of i), labelled data."""
    return j in pasts[i]


def cond_law(cl, stat):
    """P(S | final unlabelled class) for each class."""
    out = {}
    for c, items in cl.items():
        tot = sum(p for _, p in items)
        out[c] = sum(p for x, p in items if stat(x)) / tot
    return out


def main():
    t1 = [Fraction(x) for x in (1, 1, 2, 3, 5, 8)]
    t2 = [Fraction(x) for x in (3, 1, 1, 4, 1, 5)]

    # sanity: transition probabilities are normalised by construction; check one stage
    for n in range(0, N):
        for pasts in grow(t1, n)[n]:
            past = [frozenset(p) for p in pasts]
            assert sum(p for _, p in taus(past, n, t1)) == 1

    ok_all = True
    for name, t in (("t1", t1), ("t2", t2)):
        dist = grow(t, N)[N]
        cl = classes(dist)
        const = all(len({p for _, p in items}) == 1 for items in cl.values())
        print(f"[{name}] n={N}: {len(dist)} labelled causets in {len(cl)} classes; "
              f"probability constant within every class: {const}")
        ok_all &= const

    d1, d2 = grow(t1, N)[N], grow(t2, N)[N]
    c1, c2 = classes(d1), classes(d2)
    stat = lambda x: above(x, 3, 1)
    l1, l2 = cond_law(c1, stat), cond_law(c2, stat)
    same = all(l1[c] == l2[c] for c in l1)
    marg1 = sum(p for x, p in d1.items() if stat(x))
    marg2 = sum(p for x, p in d2.items() if stat(x))
    print(f"statistic S = 'element 3 above element 1': P(S | class) equal for t1 and t2 "
          f"on every class: {same}; unconditional P(S) = {float(marg1):.4f} vs {float(marg2):.4f}")
    ok_all &= same and marg1 != marg2

    # prefix statistic: the labelled 3-element prefix, conditional on the final class
    def prefix(x):
        return x[:3]
    pre_same = True
    for c in c1:
        items1, items2 = c1[c], c2[c]
        tot1, tot2 = sum(p for _, p in items1), sum(p for _, p in items2)
        pf1, pf2 = defaultdict(Fraction), defaultdict(Fraction)
        for x, p in items1:
            pf1[prefix(x)] += p / tot1
        for x, p in items2:
            pf2[prefix(x)] += p / tot2
        pre_same &= dict(pf1) == dict(pf2)
    print(f"labelled 3-element prefix: conditional law given the final class identical for "
          f"t1 and t2: {pre_same}")
    ok_all &= pre_same

    # contrast: label-dependent growth (weights depend on the birth index)
    def bias_factory(a):
        return lambda n, I: (1 + a) if (n % 2 == 1 and len(I) > 0) else 1
    ba, bb = bias_factory(Fraction(0)), bias_factory(Fraction(3))
    e0, e1 = grow(t1, N, ba)[N], grow(t1, N, bb)[N]
    k0, k1 = classes(e0), classes(e1)
    nonconst = sum(1 for items in k1.values() if len({p for _, p in items}) > 1)
    m0, m1 = cond_law(k0, stat), cond_law(k1, stat)
    diff = sum(1 for c in m0 if m0[c] != m1[c])
    print(f"contrast (label-dependent law, bias a=3): classes with non-constant labelled "
          f"probability: {nonconst}/{len(k1)}; classes where P(S | class) depends on the "
          f"parameter: {diff}/{len(m0)}")
    ok_all &= nonconst > 0 and diff > 0

    print("RESULT:", "all checks consistent with the argument (domain n <= %d)" % N if ok_all
          else "SOME CHECK FAILED")


if __name__ == "__main__":
    main()
