#!/usr/bin/env python3
"""q-Borel-Laplace in a LARGER base Q = q^s (s > 1) at p=-1/2, q=3/2.

In base q the q-Borel transform of the non-antichain stems has radius 0
(qborel_pade.py root test).  In base Q = q^s with s > 1 the transform
B_Q(xi) = sum_n Delta_n Q^{-n(n-1)/2} xi^n is entire, and we evaluate it
directly from exact coefficients (n <= NMAX) in log space -- no Pade.
Truncation control: we report the largest |term| omitted proxy (the last
few terms' size at the largest |xi| used).  The q-Laplace sum in base Q is
   S^[lam] = sum_k B_Q(lam Q^k) / theta_Q(lam Q^k).
Question: are the values finite, independent of lam and of s?

Result recorded in REPORT.md: no.  Even for the 2-antichain stem (exact
base-q value 1, qborel.py) every s > 1 gives huge, lam-dependent numbers.
Reason: Delta_n ~ q^{n^2/2}, so b_n ~ q^{-(s-1) n^2/2} and
|B_Q(xi)| ~ exp((log|xi|)^2 / (2 (s-1) log q)), while
|theta_Q(xi)| ~ exp((log|xi|)^2 / (2 s log q)); since 1/(s-1) > 1/s for
every s > 1 the base-Q Laplace series diverges along the spiral, and the
finite numbers printed are artefacts of the truncation |k| <= 14.
s = 1 with the raw truncated series is evaluated beyond the radius of
convergence (2anti/3anti: radius 1/q; other stems: radius 0 -> 'nan');
the exact continuation for 2anti is in qborel.py.
"""
import cmath, math, json
from fractions import Fraction as F
from ring import GQ
from chains import chain_sequences

NMAX = 90
q = F(3, 2)

def log_theta(z, Q):
    lQ = math.log(Q)
    es = [-k * (k - 1) / 2 * lQ + k * cmath.log(z) for k in range(-300, 301)]
    M = max(e.real for e in es)
    return M + cmath.log(sum(cmath.exp(e - M) for e in es if e.real - M > -60))

def make_terms(D, s):
    """log-coefficients of B_Q: list of (n, log|b_n|, sign)."""
    lQ = s * math.log(1.5)
    out = []
    for n, d in enumerate(D, start=1):
        if d == 0:
            continue
        l = math.log(abs(d.numerator)) - math.log(d.denominator) - n * (n - 1) / 2 * lQ
        out.append((n, l, 1 if d > 0 else -1))
    return out

def laplace(terms, lam, s, K=14):
    """sum_k B_Q(lam Q^k)/theta_Q(lam Q^k), all products formed in log space.
    Returns (value, tail proxy, max log-size of any single product).  A max
    log-size above ~600 means the truncated Borel series is not controlling
    the sum (method inapplicable at this truncation)."""
    Q = 1.5 ** s
    tot = 0j; worst_tail = 0.0; maxlog = -1e9
    for k in range(-K, K + 1):
        xi = lam * Q ** k
        lt = log_theta(xi, Q)
        lx = cmath.log(xi)
        exps = [(l + n * lx - lt, sg) for (n, l, sg) in terms]
        mx = max(e.real for e, _ in exps)
        maxlog = max(maxlog, mx)
        if mx > 600:
            return complex('nan'), float('inf'), maxlog
        tot += sum(sg * cmath.exp(e) for e, sg in exps if e.real > -700)
        worst_tail = max(worst_tail, max(math.exp(e.real) for e, _ in exps[-5:]))
    return tot, worst_tail, maxlog

if __name__ == '__main__':
    seqs = chain_sequences(GQ(F(-1, 2)), NMAX, GQ)
    lines = [f'q-Borel-Laplace in base Q = q^s, p=-1/2, exact coefficients n <= {NMAX}',
             'entry: regularized a_inf = a_1 + S^[lam]  (tail = largest truncation-term proxy)']
    out = {}
    lams = [1.0, 1.3, cmath.exp(0.7j), cmath.exp(2.0j)]
    for name in ['2anti', '3anti', '2chain', '2chain+1', '3chain', 'V', 'Lambda']:
        a = [x.re for x in seqs[name]]
        D = [a[i + 1] - a[i] for i in range(len(a) - 1)]
        lines.append(f'[{name}]')
        out[name] = {}
        for s in (1.0, 1.25, 1.5, 2.0):
            terms = make_terms(D, s)
            vals = []
            for lam in lams:
                v, tail, mx = laplace(terms, lam, s)
                vals.append((float(a[0]) + v, tail))
            lines.append(f'   s={s:4.2f}: ' + '  '.join(f'{v.real:+.4e}{v.imag:+.4e}i (tail {t:.0e})' for v, t in vals))
            out[name][str(s)] = [[v.real, v.imag, t] for v, t in vals]
    print('\n'.join(lines))
    open('out/qborel_base.txt', 'w').write('\n'.join(lines) + '\n')
    json.dump(out, open('out/qborel_base.json', 'w'), indent=1)
