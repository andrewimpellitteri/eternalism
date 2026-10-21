#!/usr/bin/env python3
"""Independent real-p control: Monte Carlo transitive percolation at p=1/2.

Each sample: n0=40 elements; for i<j the edge i->j is present with
probability p; the past of j is the transitive closure.  Stems of size <= 3
are found by brute force over down-sets of size <= 3 (no use of the chain
reduction).  Compares frequencies with the exact chain values at stage 40.
"""
import itertools, json, random, sys
from enumerate_labelled import canon, STEM_NAMES

def sample(n, p, rng):
    pasts = []
    for j in range(n):
        d = 0
        for i in range(j):
            if rng.random() < p:
                d |= pasts[i] | (1 << i)
        pasts.append(d)
    return pasts

def stems_present(pasts):
    small = [i for i, d in enumerate(pasts) if d.bit_count() <= 2]
    found = set()
    for k in (1, 2, 3):
        for sub in itertools.combinations(small, k):
            mask = 0
            for i in sub:
                mask |= 1 << i
            if all((pasts[i] & ~mask) == 0 for i in sub):
                idx = {e: a for a, e in enumerate(sub)}
                rel = {(idx[f], idx[e]) for e in sub for f in sub
                       if f != e and (pasts[e] >> f) & 1}
                found.add(STEM_NAMES[canon(rel, k)])
    return found

if __name__ == '__main__':
    p, n0, S = 0.5, 40, int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    rng = random.Random(20261021)
    counts = {}
    for _ in range(S):
        for s in stems_present(sample(n0, p, rng)):
            counts[s] = counts.get(s, 0) + 1
    exact = json.load(open('out/sequences.json'))['p=1/2 (control)']['float']
    lines = [f'Monte Carlo control: p=1/2, {S} samples of {n0}-element transitive percolation, seed 20261021']
    for s in ['1', '2chain', '2anti', '3chain', '3anti', 'V', 'Lambda', '2chain+1']:
        f = counts.get(s, 0) / S
        se = (f * (1 - f) / S) ** 0.5
        ex = exact[s][n0 - 1][0]
        z = (f - ex) / se if se > 0 else 0.0
        lines.append(f'  {s:9s} MC {f:.5f} +- {se:.5f}   exact a_40 {ex:.5f}   z = {z:+.2f}')
    print('\n'.join(lines))
    open('out/montecarlo_control.txt', 'w').write('\n'.join(lines) + '\n')
