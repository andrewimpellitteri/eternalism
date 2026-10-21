#!/usr/bin/env python3
"""Grouping (label-dependence) diagnostics from the labelled enumeration.

E_m(S) = 'S is a stem at stage m but not at stage m-1'.  Its amplitude is
mu(E_m) = a_m - a_{m-1}.  E_m is a finite disjoint union of labelled stage-m
cylinders.  We compare
   |mu(E_m)|                    (the stage-grouped increment), with
   W_m(S) = sum_{cylinders C in E_m} |A_p(C)|   (ungrouped labelled pieces).
If sum_m W_m diverges, the series of labelled-cylinder amplitudes for the
stem event is not absolutely convergent, so its value depends on the order /
grouping (Riemann-Levy-Steinitz).  Also reports the total stage variation
U_m = sum_{all stage-m cylinders} |A_p(C)|.
Exact enumeration data, float evaluation.
"""
import json
from enumerate_labelled import STEMS, STEM_BIT

E = json.load(open('out/enum_labelled_9.json'))
P = {'p=1/2': 0.5, 'p=3/2': 1.5, 'p=(1+i)/2': 0.5 + 0.5j, 'p=-1/2': -0.5}
lines = ['Grouping diagnostics (labelled enumeration, stages m <= 9)']
out = {}
for name, p in P.items():
    q = 1 - p
    lines.append(f'== {name}')
    out[name] = {}
    U = []
    for m in range(1, 10):
        st = E['stages'][str(m)]
        U.append(sum(c * abs(p) ** L * abs(q) ** H for L, H, sb, c in st['LH_counts']))
    lines.append('  U_m (total variation of stage-m cylinders): ' + ' '.join(f'{u:.4g}' for u in U))
    out[name]['U'] = U
    for s in ['2chain', '2anti', '3chain', 'V', 'Lambda']:
        W, M = [], []
        for m in range(1, 10):
            st = E['stages'][str(m)]
            w = 0.0; mu = 0j
            for L, H, nb, c in st['first_LH_counts']:
                if nb & STEM_BIT[s]:
                    w += c * abs(p) ** L * abs(q) ** H
                    mu += c * p ** L * q ** H
            W.append(w); M.append(abs(mu))
        lines.append(f'  [{s}] m:        ' + ' '.join(f'{m:>9d}' for m in range(1, 10)))
        lines.append(f'  [{s}] |mu(E_m)|: ' + ' '.join(f'{x:9.3g}' for x in M))
        lines.append(f'  [{s}] W_m:       ' + ' '.join(f'{x:9.3g}' for x in W))
        out[name][s] = {'abs_mu_Em': M, 'W_m': W}
open('out/grouping.txt', 'w').write('\n'.join(lines) + '\n')
json.dump(out, open('out/grouping.json', 'w'), indent=1)
print('\n'.join(lines))
