#!/usr/bin/env python3
"""q-Borel-Laplace summation attempt for the 2-antichain stem at p=-1/2.

For |q|>1 the increments Delta_n = a_{n+1}-a_n = q^n (q;q)_{n-1} of the
2-antichain stem grow like |q|^{n^2/2}: every Gevrey (Borel / Mittag-Leffler
of finite order) method fails, and the natural candidate is q-Borel-Laplace
summation (Ramis; Zhang) in base q.  Convention used here (verified on
monomials below):
   B_q[sum a_n x^n](xi) = sum a_n q^{-n(n-1)/2} xi^n
   L_q^[lam][phi](x)    = sum_{k in Z} phi(lam q^k) / theta(lam q^k / x)
   theta(z)             = sum_{k in Z} q^{-k(k-1)/2} z^k
For F(x) = sum_{n>=1} Delta_n x^n, with t = 1/q:
   B(xi) = (q xi) g(-q xi),   g(y) = sum_{n>=0} (t;t)_n y^n,
and g satisfies g(y)(1-y) = 1 - t y g(t y), giving the meromorphic
continuation used below (poles at y = q^j, j>=0, i.e. xi = -q^{j-1}).
The sum at x=1 depends a priori on the direction lam in C*/q^Z.
Floating point (double); stated precision is the stability of the sums.
"""
import cmath, math, json

q = 1.5
t = 1 / q

def log_theta(z):
    """log theta(z) via log-sum-exp (theta overflows doubles for large |log z|)."""
    es = [-k * (k - 1) / 2 * math.log(q) + k * cmath.log(z) for k in range(-200, 201)]
    M = max(e.real for e in es)
    s = sum(cmath.exp(e - M) for e in es if e.real - M > -60)
    return M + cmath.log(s)

def qlaplace(phi, lam, x=1.0, K=40):
    s = 0j
    for k in range(-K, K + 1):
        xi = lam * q ** k
        lt = log_theta(xi / x)
        if lt.real > 700:
            continue                     # term below 1e-300
        s += phi(xi) * cmath.exp(-lt)
    return s

# ---- validation of the convention -------------------------------------
def validate():
    out = []
    for m in range(0, 5):
        for lam in (1.0, 1.23, 0.7 + 0.4j):
            for x in (1.0, 0.6):
                v = qlaplace(lambda xi, m=m: xi ** m * q ** (-m * (m - 1) / 2), lam, x)
                out.append(abs(v - x ** m))
    # convergent series sum (1/2)^n x^n at x=1 -> 2
    def phi(xi):
        tot = 0j
        for n in range(0, 200):
            e = n * math.log(0.5) - n * (n - 1) / 2 * math.log(q) + n * cmath.log(xi)
            if e.real < -700:
                if n > 5 and e.real < -700:
                    break
                continue
            tot += cmath.exp(e)
        return tot
    conv = [abs(qlaplace(phi, lam) - 2.0) for lam in (1.0, 1.3, 0.5 + 0.5j)]
    return max(out), max(conv)

# ---- B for the 2-antichain stem --------------------------------------
_tt = [1.0]
for n in range(1, 400):
    _tt.append(_tt[-1] * (1 - t ** n))

def g(y, depth=0):
    if abs(y) < 0.5:
        s = 0j; yn = 1 + 0j
        for n in range(400):
            s += _tt[n] * yn
            yn *= y
            if abs(yn) < 1e-30:
                break
        return s
    return (1 - t * y * g(t * y, depth + 1)) / (1 - y)

def B(xi):
    return (q * xi) * g(-q * xi)

def check_B_series():
    # compare the continuation B with the exact q-Borel power series
    # b_n = Delta_n q^{-n(n-1)/2}, Delta_n = q^n (q;q)_{n-1}, in exact rationals
    from fractions import Fraction as Fr
    Q = Fr(3, 2)
    bs = []
    qq = Fr(1)
    for n in range(1, 40):
        if n > 1:
            qq *= (1 - Q ** (n - 1))
        bs.append(float(Q ** n * qq / Q ** (n * (n - 1) // 2)))
    errs = []
    for xi in (0.1, -0.2 + 0.1j, 0.25j, 0.4):
        ser = sum(b * xi ** (n + 1) for n, b in enumerate(bs))
        errs.append(abs(ser - B(xi)))
    return max(errs)

if __name__ == '__main__':
    vm, vc = validate()
    eb = check_B_series()
    lines = ['q-Borel-Laplace check, 2-antichain stem, p=-1/2 (q=3/2)',
             f'convention check: max |L[B[x^m]](x) - x^m| over m<=4, 3 directions, 2 x-values = {vm:.2e}',
             f'convergent control sum (1/2)^n: max error vs 2 over 3 directions = {vc:.2e}',
             f'B continuation vs power series on |xi|<=0.25: max error = {eb:.2e}',
             '',
             'S(lam) = q-Borel-Laplace sum of sum Delta_n at x=1 (a_1 = 0, so S is the regularized a_inf):']
    res = {}
    lams = [1.0, 1.1, 1.2, 1.3, 1.4, 1.49, cmath.exp(0.5j), cmath.exp(1.5j), cmath.exp(2.5j), 1.2 * cmath.exp(-1.0j)]
    for lam in lams:
        v = qlaplace(B, lam)
        v2 = qlaplace(B, lam * q)     # q-periodicity check in lam
        res[str(lam)] = [v.real, v.imag]
        lines.append(f'  lam = {lam:.4f}:  S = {v.real:+.12f} {v.imag:+.12f}i   (|S(lam)-S(q lam)| = {abs(v - v2):.1e})')
    # zeta-regularized product candidate for 1-(q;q)_inf, for comparison only
    tinf = 1.0
    for n in range(1, 400):
        tinf *= (1 - t ** n)
    for branch, ph in (('+i', 1j), ('-i', -1j)):
        z = 1 - ph * q ** (-1 / 12) * tinf
        lines.append(f'  zeta-regularized 1-(q;q)_inf, (-1)^(-1/2) -> {branch}: {z.real:+.12f} {z.imag:+.12f}i')
    print('\n'.join(lines))
    open('out/qborel.txt', 'w').write('\n'.join(lines) + '\n')
    json.dump(res, open('out/qborel.json', 'w'))
