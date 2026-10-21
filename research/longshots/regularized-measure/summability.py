#!/usr/bin/env python3
"""Summability diagnostics for the stage sequences in out/sequences.json.

For each p and stem S (a_n = a_n(S), n = 1..N; Delta_n = a_{n+1} - a_n
computed exactly and converted to float):
  * convergence: |Delta_n| at the end, ratio |Delta_{n+1}/Delta_n|
  * growth: log|a_n| / n^2 and the slope of log|a_{n+1}/a_n| in n
  * Cesaro (C,1) and (C,2) means of a_n at N/2 and N
  * Abel: root-test radius of sum a_n x^n, R_A = 1/|a_N|^{1/N}
    (the Abel mean needs R_A >= 1)
  * Borel: root-test radius of sum a_n x^n / n!, R_B = 1/|a_N/N!|^{1/N}
    (Borel needs R_B > 0 and continuation along [0, inf))
  * Euler (E,1) means 2^{-M} sum_k C(M,k) a_k at M = N/2 and N
Floating point with logs (values up to 1e165 fit in doubles).
"""
import json, math, cmath

data = json.load(open('out/sequences.json'))
STEMS = ['2chain', '2anti', '3chain', '3anti', 'V', 'Lambda', '2chain+1']

def C(z): return complex(z[0], z[1])

def fmt(z):
    z = complex(z)
    if abs(z) > 1e6 or (abs(z) < 1e-4 and z != 0):
        return f'{abs(z):.3e}*e^({cmath.phase(z):+.2f}i)'
    return f'{z.real:+.6f}{z.imag:+.6f}i'

def cesaro(a, M, order):
    s = a[:M]
    for _ in range(order):
        acc = 0; out = []
        for k, x in enumerate(s):
            acc += x; out.append(acc / (k + 1))
        s = out
    return s[-1]

def euler(a, M):
    return sum(math.comb(M - 1, k) * a[k] for k in range(M)) / 2 ** (M - 1)

def logabs(z):
    return math.log(abs(z)) if z != 0 else float('-inf')

lines = []
summary = {}
for name, d in data.items():
    N = d['N']
    lines.append(f'=== {name}  (q = {complex(*d["q"]):.4f}, |q| = {abs(complex(*d["q"])):.4f}, N = {N})')
    summary[name] = {}
    for s in STEMS:
        a = [C(z) for z in d['float'][s]]
        D = [C(z) for z in d['delta_float'][s]]
        n = len(a)
        last = a[-1]
        dl = abs(D[-1]); ratio = abs(D[-1] / D[-2]) if D[-2] != 0 else float('nan')
        rootA = abs(last) ** (1 / n)
        lognf = math.lgamma(n + 1)
        rootB = math.exp((logabs(last) - lognf) / n) if last != 0 else 0
        g2 = logabs(last) / n ** 2
        # slope of log|a_{n+1}/a_n| over the last 10 stages (divergent case)
        sl = [logabs(a[i + 1]) - logabs(a[i]) for i in range(n - 11, n - 1)]
        slope = (sl[-1] - sl[0]) / (len(sl) - 1)
        c1h, c1 = cesaro(a, n // 2, 1), cesaro(a, n, 1)
        c2h, c2 = cesaro(a, n // 2, 2), cesaro(a, n, 2)
        eh, e = euler(a, n // 2), euler(a, n)
        lines.append(f'  [{s}] a_N = {fmt(last)}')
        lines.append(f'     |Delta_(N-1)| = {dl:.3e}, |Delta ratio| = {ratio:.4f}; log|a_N|/N^2 = {g2:.4f}; '
                     f'slope of log|a_(n+1)/a_n| = {slope:.4f}')
        lines.append(f'     Abel radius ~ {1/rootA:.3e}; Borel radius ~ {1/rootB:.3e}')
        lines.append(f'     (C,1): N/2 {fmt(c1h)}  N {fmt(c1)}')
        lines.append(f'     (C,2): N/2 {fmt(c2h)}  N {fmt(c2)}')
        lines.append(f'     (E,1): N/2 {fmt(eh)}  N {fmt(e)}')
        summary[name][s] = dict(a_N=[last.real, last.imag], abs_delta_last=dl, delta_ratio=ratio,
                                logabs_over_n2=g2, logratio_slope=slope,
                                abel_radius=1 / rootA, borel_radius=1 / rootB,
                                C1=[c1.real, c1.imag], C2=[c2.real, c2.imag], E1=[e.real, e.imag])
open('out/summability.txt', 'w').write('\n'.join(lines) + '\n')
json.dump(summary, open('out/summability.json', 'w'), indent=1)
print('\n'.join(lines))
