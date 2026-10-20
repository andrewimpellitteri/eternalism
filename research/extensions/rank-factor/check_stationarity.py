#!/usr/bin/env python3
"""Check S(H,m) = N(H)A(H) R_{m-n} on finite data."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe
import kernel_sequence7 as ks

for p in (0.5, 0.5+0.5j):
    print('p=', p)
    data = probe.kernel(6, p)
    R = ks.R(7, p)
    worst = 0.0
    checks = 0
    for cH, d in data.items():
        n = d['n']; target = d['N'] * d['A']
        if abs(target) < 1e-12:
            continue
        for m, s in d['sums'].items():
            expected = R[m-n][0]
            err = abs(s/target - expected)
            worst = max(worst, err); checks += 1
            if err > 1e-9:
                print('  mismatch n=%d m=%d ratio=%s R=%s' % (n, m, s/target, expected))
    print('  checks=%d max error=%.3e' % (checks, worst))
