#!/usr/bin/env python3
"""q-Borel-Laplace regularization at p=-1/2 (q=3/2) for every stem of size
<= 3 and for the events {#minimal elements = j}, using exact q-Borel
coefficients and exact rational Pade continuation of the q-Borel transform.

Regularized value:  a_reg = a_1 + S_q^[lam](F)(1),  F(x) = sum_{n>=1} Delta_n x^n,
Delta_n = a_{n+1} - a_n, with the q-Laplace convention of qborel.py.
The pipeline is validated on the 2-antichain stem, whose regularized value is
known in closed form (qborel.py: exactly 1 for every direction lam).
Reliability is judged by agreement across Pade orders and directions lam.
"""
import cmath, math, json
from fractions import Fraction as F
from ring import GQ
from chains import chain_sequences
from qborel import qlaplace

q = F(3, 2)
N = 40
p = GQ(F(-1, 2))

def exact_real(seq):
    return [x.re for x in seq]

def minimal_count_sequences(N, jmax):
    """exact amplitude of {#min at stage n = j}, j=1..jmax, n=1..N (chain A)."""
    qq = 1 - F(-1, 2)
    A = {1: F(1)}
    out = {j: [] for j in range(1, jmax + 1)}
    def rec():
        for j in out:
            out[j].append(A.get(j, F(0)))
    rec()
    for m in range(1, N):
        qm = qq ** m
        nA = {}
        for M, w in A.items():
            nA[M + 1] = nA.get(M + 1, 0) + w * qm
            nA[M] = nA.get(M, 0) + w * (1 - qm)
        A = nA
        rec()
    return out

def pade(c, L, M):
    """Exact Pade [L/M] of sum c[k] x^k: returns (P, Q) coefficient lists."""
    # solve for Q (Q0 = 1): sum_{j=0}^M Q_j c_{k-j} = 0 for k = L+1..L+M
    A = [[(c[k - j] if 0 <= k - j < len(c) else F(0)) for j in range(1, M + 1)] for k in range(L + 1, L + M + 1)]
    b = [-(c[k] if k < len(c) else F(0)) for k in range(L + 1, L + M + 1)]
    n = M
    Mx = [row[:] + [bb] for row, bb in zip(A, b)]
    for col in range(n):
        piv = next((r for r in range(col, n) if Mx[r][col] != 0), None)
        if piv is None:
            raise ZeroDivisionError('singular Pade system')
        Mx[col], Mx[piv] = Mx[piv], Mx[col]
        for r in range(n):
            if r != col and Mx[r][col] != 0:
                f = Mx[r][col] / Mx[col][col]
                Mx[r] = [x - f * y for x, y in zip(Mx[r], Mx[col])]
    Qc = [F(1)] + [Mx[i][n] / Mx[i][i] for i in range(n)]
    Pc = [sum(Qc[j] * c[k - j] for j in range(0, min(k, M) + 1)) for k in range(L + 1)]
    return Pc, Qc

def poly_eval(cs, x):
    s = 0j
    for c in reversed(cs):
        s = s * x + float(c)
    return s

def regularize(a, orders, lams):
    D = [a[i + 1] - a[i] for i in range(len(a) - 1)]          # Delta_1..Delta_{N-1}
    b = [F(0)] + [D[n - 1] / q ** (n * (n - 1) // 2) for n in range(1, len(D) + 1)]
    root = max(abs(float(b[n])) ** (1 / n) for n in range(len(b) - 10, len(b)) if b[n] != 0) if any(b) else 0
    res = {}
    for (L, M) in orders:
        try:
            P, Qd = pade(b, L, M)
        except ZeroDivisionError:
            continue
        # scale for float evaluation
        Pf = [float(x) for x in P]; Qf = [float(x) for x in Qd]
        phi = lambda xi: poly_eval(P, xi) / poly_eval(Qd, xi)
        res[(L, M)] = [complex(float(a[0])) + qlaplace(phi, lam, K=30) for lam in lams]
    return root, res

if __name__ == '__main__':
    seqs = chain_sequences(p, N, GQ)
    targets = {s: exact_real(v) for s, v in seqs.items() if s != '1'}
    mins = minimal_count_sequences(N, 5)
    for j, v in mins.items():
        targets[f'#min={j}'] = v
    orders = [(19, 19), (18, 19), (17, 17), (15, 15), (12, 12)]
    lams = [1.0, 1.25, cmath.exp(0.7j), cmath.exp(2.0j)]
    lines = [f'q-Borel-Laplace + exact Pade continuation at p=-1/2 (q=3/2), stages n<={N}',
             'columns: Pade [L/M]; entries: regularized value for lam = ' + ', '.join(f'{l:.3f}' for l in lams)]
    out = {}
    for name, a in targets.items():
        root, res = regularize(a, orders, lams)
        lines.append(f'[{name}]  q-Borel coefficient root test |b_n|^(1/n) ~ {root:.3f} (radius ~ {1/root if root else float("inf"):.3f})')
        out[name] = {}
        for (L, M), vals in res.items():
            lines.append(f'   [{L}/{M}] ' + '  '.join(f'{v.real:+.8f}{v.imag:+.8f}i' for v in vals))
            out[name][f'{L}/{M}'] = [[v.real, v.imag] for v in vals]
    print('\n'.join(lines))
    open('out/qborel_pade.txt', 'w').write('\n'.join(lines) + '\n')
    json.dump(out, open('out/qborel_pade.json', 'w'), indent=1)
