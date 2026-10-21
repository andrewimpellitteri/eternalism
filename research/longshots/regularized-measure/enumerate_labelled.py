#!/usr/bin/env python3
"""Labelled enumeration of complex transitive percolation (CTP) up to stage N.

Independent check path: every naturally labelled causet on n elements is
grown by adding a new maximal element whose past is a down-set D of the
current causet.  The transition amplitude is p^{|max D|} q^{m-|D|} with
q = 1-p and m the current size, so the cylinder amplitude is
p^{L(C)} q^{binom(n,2)-R(C)}.

For each stage n we aggregate labelled causets by (L, H, stem set), where
H = binom(n,2) - R and the stem set lists which unlabelled posets of size
<= 3 occur as down-sets (stems).  The stage-n stem amplitude is then the
exact integer polynomial a_n(S)(p) = sum count * p^L (1-p)^H.

Standard library only.  Usage: python3 enumerate_labelled.py N  (N<=9)
Writes out/enum_labelled_N.json.
"""
import itertools, json, sys, time
from collections import Counter

# ---- unlabelled posets of size <= 3 (stems) -------------------------------
def canon(rel, k):
    """rel: set of (i,j) with i<j in poset order, elements 0..k-1. Return
    canonical code = min over permutations of sorted relation tuple."""
    best = None
    for perm in itertools.permutations(range(k)):
        code = (k, tuple(sorted((perm[i], perm[j]) for (i, j) in rel)))
        if best is None or code < best:
            best = code
    return best

STEM_NAMES = {}
def _register():
    shapes = {
        '1':        (1, []),
        '2chain':   (2, [(0, 1)]),
        '2anti':    (2, []),
        '3chain':   (3, [(0, 1), (0, 2), (1, 2)]),
        '3anti':    (3, []),
        'V':        (3, [(0, 2), (1, 2)]),        # two minima below one top
        'Lambda':   (3, [(0, 1), (0, 2)]),        # one minimum below two
        '2chain+1': (3, [(0, 1)]),
    }
    for name, (k, rel) in shapes.items():
        STEM_NAMES[canon(set(rel), k)] = name
_register()
STEMS = ['1', '2chain', '2anti', '3chain', '3anti', 'V', 'Lambda', '2chain+1']
STEM_BIT = {s: 1 << i for i, s in enumerate(STEMS)}


def classify(elems, pasts):
    """elems: list of element indices forming a down-set; return stem bit."""
    k = len(elems)
    idx = {e: i for i, e in enumerate(elems)}
    rel = set()
    for e in elems:
        pe = pasts[e]
        for f in elems:
            if f != e and (pe >> f) & 1:
                rel.add((idx[f], idx[e]))
    return STEM_BIT[STEM_NAMES[canon(rel, k)]]


def new_stems(pasts, d, m):
    """New element z (index m) with past d. Return bits of stems of size<=3
    that contain z.  Such a stem is X u {z} with X a down-set, d subset X,
    |X| <= 2.  All such X are enumerated: X = d; X = d u {w}; and, when d is
    empty, X = {w, w2} with w minimal and past(w2) within {w}."""
    bits = 0
    dl = [i for i in range(m) if (d >> i) & 1]
    if len(dl) > 2:
        return 0
    full = pasts + [d]
    bits |= classify(dl + [m], full)
    if len(dl) <= 1:
        for w in range(m):
            if not (d >> w) & 1 and (pasts[w] & ~d) == 0:
                bits |= classify(dl + [w, m], full)
                if not dl:
                    # X = {w, w2}, a size-2 down-set containing w
                    for w2 in range(m):
                        if w2 != w and (pasts[w2] & ~(1 << w)) == 0:
                            bits |= classify([w, w2, m], full)
    return bits


def downsets(pasts):
    """All down-sets as (mask, union_of_pasts)."""
    ds = [(0, 0)]
    for i, pi in enumerate(pasts):
        bit = 1 << i
        ds += [(dm | bit, u | pi) for (dm, u) in ds if (pi & ~dm) == 0]
    return ds


def run(N):
    agg = [Counter() for _ in range(N + 1)]
    # first-appearance aggregation: (L, H, bits of stems that are new at this stage)
    first = [Counter() for _ in range(N + 1)]

    def dfs(pasts, L, H, stems):
        m = len(pasts)
        agg[m][(L, H, stems)] += 1
        if m == N:
            return
        for dm, u in downsets(pasts):
            size = dm.bit_count()
            nmax = (dm & ~u).bit_count()
            s2 = stems
            if size <= 2:
                s2 |= new_stems(pasts, dm, m)
            first[m + 1][(L + nmax, H + m - size, s2 & ~stems)] += 1
            if m + 1 == N:
                agg[N][(L + nmax, H + m - size, s2)] += 1
            else:
                dfs(pasts + [dm], L + nmax, H + m - size, s2)

    # stage 1: single element, stem '1'
    first[1][(0, 0, STEM_BIT['1'])] += 1
    dfs([0], 0, 0, STEM_BIT['1'])
    return agg, first

# ---- integer polynomials in p ---------------------------------------------
def binom_poly(L, H):
    """coefficients of p^L (1-p)^H as list."""
    from math import comb
    c = [0] * (L + H + 1)
    for j in range(H + 1):
        c[L + j] += comb(H, j) * (-1) ** j
    return c

def add_into(acc, c, w):
    if len(acc) < len(c):
        acc.extend([0] * (len(c) - len(acc)))
    for i, x in enumerate(c):
        acc[i] += w * x

def trim(c):
    while c and c[-1] == 0:
        c.pop()
    return c


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    t0 = time.time()
    agg, first = run(N)
    t1 = time.time()
    out = {'N': N, 'runtime_s': round(t1 - t0, 2), 'stages': {}}
    for n in range(1, N + 1):
        total = []
        stem_polys = {s: [] for s in STEMS}
        for (L, H, st), cnt in agg[n].items():
            c = binom_poly(L, H)
            add_into(total, c, cnt)
            for s in STEMS:
                if st & STEM_BIT[s]:
                    add_into(stem_polys[s], c, cnt)
        total = trim(total)
        ncausets = sum(agg[n].values())
        assert total == [1], (n, total)          # stage sum == 1 identically
        out['stages'][n] = {
            'labelled_causets': ncausets,
            'stage_sum_poly': total,
            'stem_polys': {s: trim(stem_polys[s]) for s in STEMS},
            # raw (L, H, count) data, enough to evaluate any |A_p| sum
            'LH_counts': [[L, H, st, c] for (L, H, st), c in agg[n].items()],
            'first_LH_counts': [[L, H, nb, c] for (L, H, nb), c in first[n].items()],
        }
        print(f'n={n}: {ncausets} naturally labelled causets, stage sum = 1 (polynomial identity) OK', flush=True)
    print(f'runtime {t1 - t0:.1f}s')
    with open(f'out/enum_labelled_{N}.json', 'w') as f:
        json.dump(out, f)
