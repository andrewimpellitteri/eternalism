#!/usr/bin/env python3
"""Cross-check: chain polynomials (in p) == labelled-enumeration polynomials,
for every stem of size <= 3 and every stage n <= N.  Also checks the closed
form a_n(2anti) = 1 - (q;q)_{n-1}."""
import json, sys
from ring import Poly
from chains import chain_sequences

N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
enum = json.load(open(f'out/enum_labelled_{N}.json'))
p = Poly([0, 1])
seq = chain_sequences(p, N, Poly)
ok = True
lines = []
for n in range(1, N + 1):
    st = enum['stages'][str(n)]['stem_polys']
    for s, poly in st.items():
        good = (Poly(poly) == seq[s][n - 1])
        ok &= good
    # closed form for the 2-antichain stem
    q = Poly([1, -1]); prod = Poly([1]); qj = Poly([1])
    for j in range(1, n):
        qj = qj * q
        prod = prod * (Poly([1]) - qj)
    good2 = (Poly(st['2anti']) == Poly([1]) - prod)
    ok &= good2
    lines.append(f'n={n}: all 8 stem polynomials chain==enumeration: '
                 f'{all(Poly(st[s]) == seq[s][n-1] for s in st)}; 2anti closed form: {good2}')
print('\n'.join(lines))
print('ALL OK' if ok else 'MISMATCH')
with open(f'out/crosscheck_{N}.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n' + ('ALL OK\n' if ok else 'MISMATCH\n'))
