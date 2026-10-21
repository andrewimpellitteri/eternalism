#!/usr/bin/env python3
"""Covariant post events inside the stem algebra, and their variation.

Notation: for a causet C and k>=1, the k-skeleton K_k(C) = {x : |past(x)| <= k-1}.
Claims checked here (proofs in REPORT.md, Lemmas 2-3):
 (a) For a principal unlabelled H with |H| = n, the event
        D'_H = { K_n(C) is isomorphic to H }
     ('the n-th born element is a post with inclusive past H'),
     has stage-N amplitude  N(H) A_p(H) (q;q)_{N-n}   for every N >= n,
     as an exact polynomial identity in p.  Checked for n <= 5, N <= 8.
 (b) Stem characterization: for a finite causet C and a finite k-small
     poset P, K_k(C) ~= P  iff  P is a stem of C and no k-small poset of size
     |P|+1 is a stem of C.  Checked exhaustively for |C| <= 6, k <= 4.
 (c) Principal-shape variation P_n(p) = sum_{principal H, |H|=n} N(H)|A_p(H)|
     for n <= 9, so that the stem-limit set function has, at fixed rank n,
     disjoint events D'_H with sum |mu(D'_H)| = |(q;q)_inf| P_n(p).
"""
import itertools, json, sys
from collections import Counter, defaultdict
from enumerate_labelled import downsets, binom_poly, add_into, trim

def canon_sub(elems, pasts):
    """canonical code of the induced subposet on elems (refined brute force)."""
    elems = list(elems)
    k = len(elems)
    S = 0
    for e in elems:
        S |= 1 << e
    psz = {e: (pasts[e] & S).bit_count() for e in elems}
    fut = {e: sum(1 for f in elems if (pasts[f] >> e) & 1) for e in elems}
    key = lambda e: (psz[e], fut[e])
    groups = defaultdict(list)
    for e in elems:
        groups[key(e)].append(e)
    keys = sorted(groups)
    best = None
    for combo in itertools.product(*[itertools.permutations(groups[g]) for g in keys]):
        order = [e for part in combo for e in part]
        pos = {e: i for i, e in enumerate(order)}
        code = tuple(sorted((pos[f], pos[e]) for e in elems for f in elems
                            if f != e and (pasts[e] >> f) & 1))
        if best is None or code < best:
            best = code
    return (tuple(key(e) for e in sorted(elems, key=key)), best)

def skeleton(pasts, k):
    return [i for i, d in enumerate(pasts) if d.bit_count() <= k - 1]

def is_principal(elems, pasts):
    S = 0
    for e in elems:
        S |= 1 << e
    maxima = [e for e in elems if not any((pasts[f] >> e) & 1 for f in elems)]
    return len(maxima) == 1

def part_a(NMAX=8, ns=(1, 2, 3, 4, 5)):
    post = defaultdict(Counter)    # (N, n, canon) -> Counter[(L,H)]
    shape = defaultdict(Counter)   # (n, canon) -> Counter[(L,H)] for principal whole causets
    def visit(pasts, L, H):
        N = len(pasts)
        allel = list(range(N))
        if N in ns and is_principal(allel, pasts):
            shape[(N, canon_sub(allel, pasts))][(L, H)] += 1
        for n in ns:
            if n <= N:
                K = skeleton(pasts, n)
                if len(K) == n and is_principal(K, pasts):
                    post[(N, n, canon_sub(K, pasts))][(L, H)] += 1
        if N == NMAX:
            return
        for dm, u in downsets(pasts):
            visit(pasts + [dm], L + (dm & ~u).bit_count(), H + N - dm.bit_count())
    visit([0], 0, 0)
    def poly(cnt):
        acc = []
        for (L, H), c in cnt.items():
            add_into(acc, binom_poly(L, H), c)
        return trim(acc)
    def mul(a, b):
        r = [0] * (len(a) + len(b) - 1) if a and b else []
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                r[i + j] += x * y
        return trim(r)
    def qpoch(m):   # (q;q)_m with q = 1-p, as polynomial in p
        r = [1]; qj = [1]
        for j in range(1, m + 1):
            qj = mul(qj, [1, -1])
            r = mul(r, trim([1 - (qj[0] if qj else 0)] + [-c for c in qj[1:]]))
        return r
    checks = 0; bad = 0
    keys_shape = {k for k in shape}
    for (N, n, c), cnt in post.items():
        lhs = poly(cnt)
        rhs = mul(poly(shape[(n, c)]), qpoch(N - n))
        checks += 1
        if lhs != rhs:
            bad += 1
    # every principal shape at every N must appear (or have zero amplitude)
    missing = sum(1 for (n, c) in keys_shape for N in range(n, NMAX + 1) if (N, n, c) not in post)
    return checks, bad, missing, len(keys_shape)

def part_b(CMAX=6, kmax=4):
    checks = 0; bad = 0
    def all_causets(m):
        out = []
        def rec(pasts):
            if len(pasts) == m:
                out.append(pasts); return
            for dm, u in downsets(pasts):
                rec(pasts + [dm])
        rec([0])
        return out
    for m in range(1, CMAX + 1):
        for pasts in all_causets(m):
            ds = [dm for dm, u in downsets(pasts)]
            stems_by_size = defaultdict(set)
            for dm in ds:
                el = [i for i in range(m) if (dm >> i) & 1]
                if all(pasts[i].bit_count() <= kmax - 1 for i in el):
                    stems_by_size[len(el)].add((dm, canon_sub(el, pasts) if el else ()))
            for k in range(1, kmax + 1):
                K = skeleton(pasts, k)
                cK = canon_sub(K, pasts) if K else ()
                # k-small stems
                small = defaultdict(set)
                for dm in ds:
                    el = [i for i in range(m) if (dm >> i) & 1]
                    if all(pasts[i].bit_count() <= k - 1 for i in el):
                        small[len(el)].add(canon_sub(el, pasts) if el else ())
                rhs = {c for sz, cs in small.items() for c in cs if not small.get(sz + 1)}
                checks += 1
                if rhs != {cK}:
                    bad += 1
    return checks, bad

def part_c(NMAX=9, pvals=None):
    """P_n(p) = sum over naturally labelled G of size n-1 of |p|^{L+M} |q|^{h}."""
    res = {name: [0.0] * (NMAX + 1) for name in pvals}
    absw = {name: (abs(p), abs(1 - p)) for name, p in pvals.items()}
    agg = [Counter() for _ in range(NMAX)]
    def rec(pasts, L, H):
        m = len(pasts)
        allm = 0
        for d in pasts:
            allm |= d
        M = m - allm.bit_count()          # maximal elements = not in any past
        agg[m][(L + M, H)] += 1
        if m == NMAX - 1:
            return
        for dm, u in downsets(pasts):
            rec(pasts + [dm], L + (dm & ~u).bit_count(), H + m - dm.bit_count())
    agg[0][(0, 0)] += 1                   # empty G -> H is the 1-element poset
    rec([0], 0, 0)
    for name, (a, b) in absw.items():
        for m in range(NMAX):
            res[name][m + 1] = sum(c * a ** w * b ** h for (w, h), c in agg[m].items())
    return res

if __name__ == '__main__':
    lines = []
    ca, ba, miss, nsh = part_a()
    lines.append(f'(a) post-event identity amp_N(D\'_H) = N(H)A_p(H)(q;q)_(N-n): {ca} (N,n,H) cases, '
                 f'{ba} mismatches, {miss} missing; {nsh} principal shapes H with |H|<=5, N<=8')
    cb, bb = part_b()
    lines.append(f'(b) stem characterization of K_k(C): {cb} (C,k) cases (|C|<=6, k<=4), {bb} failures')
    pv = {'p=3/2': 1.5, 'p=(1+i)/2': 0.5 + 0.5j, 'p=1/2': 0.5}
    P = part_c(9, pv)
    for name, p in pv.items():
        q = 1 - p
        qq = 1.0
        for j in range(1, 400):
            qq *= (1 - q ** j)
        a, b = abs(p), abs(q); t = a + b; s = b / t
        cs = 1.0
        for j in range(1, 400):
            cs *= (1 - s ** j)
        lines.append(f'(c) {name}: |(q;q)_inf| = {abs(qq):.6f}; P_n = sum_principal N(H)|A_p(H)|, '
                     f'and |(q;q)_inf| P_n, n=1..9:')
        lines.append('    P_n:         ' + ' '.join(f'{x:.4g}' for x in P[name][1:]))
        lines.append('    |kappa| P_n: ' + ' '.join(f'{abs(qq) * x:.4g}' for x in P[name][1:]))
        lines.append('    RESULT.md lower bound for doubly-principal part, |p| t^(n-2) c_s, n=3..9: '
                     + ' '.join(f'{a * t ** (n - 2) * cs:.4g}' for n in range(3, 10)))
    print('\n'.join(lines))
    open('out/verify_posts.txt', 'w').write('\n'.join(lines) + '\n')
