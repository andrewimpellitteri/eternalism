#!/usr/bin/env python3
"""Exact stage-n stem amplitudes a_n(S) at fixed numerical p (Gaussian
rationals), via the minimal-state chains of chains.py (checked against the
labelled enumeration as polynomials for n <= 8/9 by crosscheck.py).

Writes out/sequences.json (floats of every a_n, exact strings for n <= 12)
and out/sequences.txt (summary table)."""
import json, time
from fractions import Fraction as F
from ring import GQ
from chains import chain_sequences

PVALS = {
    'p=1/2 (control)':        (GQ(F(1, 2)), 80),
    'p=3/2':                  (GQ(F(3, 2)), 80),
    'p=(1+i)/2':              (GQ(F(1, 2), F(1, 2)), 80),
    'p=-1/2':                 (GQ(F(-1, 2)), 40),
    'p=(2-4i)/5 (|q|=1)':     (GQ(F(2, 5), F(-4, 5)), 60),
}

def fl(z):
    c = complex(z)
    return [c.real, c.imag]

if __name__ == '__main__':
    res = {}
    lines = []
    for name, (p, N) in PVALS.items():
        t0 = time.time()
        seq = chain_sequences(p, N, GQ)
        dt = time.time() - t0
        q = complex(1 - p)
        res[name] = {'p': fl(p), 'q': [q.real, q.imag], 'N': N, 'runtime_s': round(dt, 2),
                     'float': {s: [fl(x) for x in v] for s, v in seq.items()},
                     'exact_n_le_12': {s: [x.str() for x in v[:12]] for s, v in seq.items()},
                     'exact_last': {s: v[-1].str() for s, v in seq.items()},
                     # exact increments Delta_n = a_{n+1} - a_n, converted to float only at the end
                     'delta_float': {s: [fl(v[i + 1] - v[i]) for i in range(len(v) - 1)]
                                     for s, v in seq.items()}}
        lines.append(f'== {name}: |p|={abs(complex(p)):.4f} |q|={abs(q):.4f} '
                     f'|p|+|q|={abs(complex(p))+abs(q):.4f}  N={N}  ({dt:.1f}s)')
        for s, v in seq.items():
            pts = [n for n in (5, 10, 20, 40, 60, 80) if n <= N]
            vals = '  '.join(f'n={n}: {complex(v[n-1]):.6g}' for n in pts)
            lines.append(f'  {s:9s} {vals}')
    open('out/sequences.txt', 'w').write('\n'.join(lines) + '\n')
    json.dump(res, open('out/sequences.json', 'w'))
    print('\n'.join(lines))
