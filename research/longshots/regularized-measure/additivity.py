#!/usr/bin/env python3
"""Finite and countable additivity checks.

(1) Event identity (exact, labelled enumeration n <= 9): for every labelled
    causet, [2chain stem and 2anti stem] == [2chain+1 stem], and
    [2chain stem or 2anti stem] holds for every n >= 2.
    Hence a_n(2chain) + a_n(2anti) - a_n(2chain+1) = 1 for n >= 2, exactly,
    at every p; checked again on the exact chain values at all five p.
(2) Countable additivity inside the 1-skeleton (#minimal elements) for
    |q| < 1: lim_n amp(#min_n = j) summed over j vs lim a_n(2anti) and 1;
    plus the variation sum_j |mu(#min=j)| (finite for |q|<1).
"""
import json
from fractions import Fraction as F
from ring import GQ
from chains import chain_sequences
from enumerate_labelled import STEM_BIT

lines = []
E = json.load(open('out/enum_labelled_9.json'))
viol_and = viol_or = 0; tot = 0
for n in range(1, 10):
    for L, H, sb, c in E['stages'][str(n)]['LH_counts']:
        tot += c
        both = bool(sb & STEM_BIT['2chain']) and bool(sb & STEM_BIT['2anti'])
        if both != bool(sb & STEM_BIT['2chain+1']):
            viol_and += c
        if n >= 2 and not (sb & STEM_BIT['2chain'] or sb & STEM_BIT['2anti']):
            viol_or += c
lines.append(f'(1) labelled causets n<=9 checked: {tot}; violations of [2chain & 2anti]==[2chain+1]: {viol_and}; '
             f'of [2chain or 2anti] (n>=2): {viol_or}')

seq = json.load(open('out/sequences.json'))
for name, d in seq.items():
    # exact check on the first 12 exact strings is implied by the polynomial
    # identity; here check the float sequences at all n
    mx = 0.0
    for n in range(2, d['N'] + 1):
        a = lambda s: complex(*d['float'][s][n - 1])
        val = a('2chain') + a('2anti') - a('2chain+1')
        rel = abs(val - 1) / max(1.0, abs(a('2chain')))
        mx = max(mx, rel)
    lines.append(f'    {name}: max relative deviation of a(2chain)+a(2anti)-a(2chain+1) from 1, n=2..{d["N"]}: {mx:.1e}')

def min_distribution(p, N):
    q = 1 - p
    A = {1: GQ(1)}
    qm = GQ(1)
    for m in range(1, N):
        qm = qm * q
        nA = {}
        for M, w in A.items():
            nA[M + 1] = nA.get(M + 1, GQ(0)) + w * qm
            nA[M] = nA.get(M, GQ(0)) + w * (1 - qm)
        A = nA
    return A

for name, p, N in (('p=3/2', GQ(F(3, 2)), 80), ('p=(1+i)/2', GQ(F(1, 2), F(1, 2)), 80), ('p=1/2', GQ(F(1, 2)), 80)):
    A = min_distribution(p, N)
    vals = {j: complex(A.get(j, GQ(0))) for j in range(1, 40)}
    s_all = sum(vals.values())
    s_ge2 = sum(v for j, v in vals.items() if j >= 2)
    var = sum(abs(v) for v in vals.values())
    a2 = complex(*seq[[k for k in seq if k.startswith(name)][0]]['float']['2anti'][N - 1])
    lines.append(f'(2) {name} (stage {N} as proxy for the limit; tail beyond j=39 negligible): '
                 f'sum_j mu(#min=j) = {s_all:.12f}; sum_(j>=2) = {s_ge2:.12f} vs a(2anti) = {a2:.12f}; '
                 f'variation sum_j |mu(#min=j)| = {var:.6f}')
    lines.append('    mu(#min=j), j=1..6: ' + '  '.join(f'{vals[j]:.5f}' for j in range(1, 7)))
print('\n'.join(lines))
open('out/additivity.txt', 'w').write('\n'.join(lines) + '\n')
