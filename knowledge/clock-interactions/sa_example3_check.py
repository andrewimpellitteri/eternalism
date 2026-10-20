#!/usr/bin/env python3
"""Exact check of Smith-Ahmadi (arXiv:1712.00081v3) Sec. 4.3, Eqs. (24)-(26).

Standard library only. Ordering convention: kets |c s>, clock first (as in the
paper's |10>, |01>). Checks:
  1. [H_int, H_C (x) I] != 0 for the paper's interaction (so the example lies in
     the "[H_int, H_C] != 0" class as far as the commutator goes);
  2. H_int annihilates the paper's stated physical states |10>, |01>, i.e. the
     interaction acts trivially on the physical subspace;
  3. the null space of H = H_C + H_S + H_int is exactly span{|10>, |01>} for
     generic (Omega, a, b);
  4. the conditional state <t|Psi>> with |t> = exp(-i H_C t)|+> equals
     exp(-i H_S t) psi(0) (the paper prints exp(+i H_S t) in Eq. (26)).

This checks one worked example of one paper. It is not a general theorem.
"""
import cmath
import itertools

I2 = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Y = [[0, -1j], [1j, 0]]
Z = [[1, 0], [0, -1]]


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(2) for l in range(2)]
            for i in range(2) for k in range(2)]


def add(*ms, coeffs=None):
    coeffs = coeffs or [1] * len(ms)
    n = len(ms[0])
    return [[sum(c * m[i][j] for c, m in zip(coeffs, ms)) for j in range(n)] for i in range(n)]


def mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def norm(m):
    return max(abs(x) for row in m for x in row)


def apply(m, v):
    return [sum(m[i][j] * v[j] for j in range(len(v))) for i in range(len(m))]


Om, a, b = 0.7, 0.31, -0.45
HC = kron([[Om * z for z in r] for r in Z], I2)
HS = kron(I2, [[Om * z for z in r] for r in Z])
Hint = add(kron(X, X), kron(Y, Y), kron(Z, Z), kron(I2, I2), coeffs=[a, -a, b, b])
H = add(HC, HS, Hint)

comm = add(mul(Hint, HC), mul(HC, Hint), coeffs=[1, -1])
print("1. ||[H_int, H_C x I]|| =", round(norm(comm), 6), "(nonzero)" if norm(comm) > 1e-12 else "(zero)")

basis = {"00": 0, "01": 1, "10": 2, "11": 3}
for lab in ("10", "01"):
    e = [0] * 4
    e[basis[lab]] = 1
    print(f"2. ||H_int|{lab}>|| =", round(max(abs(x) for x in apply(Hint, e)), 12),
          f" ||H|{lab}>|| =", round(max(abs(x) for x in apply(H, e)), 12))

# 3. H is block diagonal on span{00,11} and span{01,10}; check determinant of the 00/11 block.
blk = [[H[0][0], H[0][3]], [H[3][0], H[3][3]]]
det = blk[0][0] * blk[1][1] - blk[0][1] * blk[1][0]
print("3. det of H on span{|00>,|11>} =", round(abs(det), 6), "(nonzero => null space is span{|01>,|10>})")
print("   H on span{|01>,|10>} max entry =", round(max(abs(H[i][j]) for i in (1, 2) for j in (1, 2)), 12))

# 4. conditional state
th, ph = 0.4, 1.1
Psi = [0] * 4
Psi[basis["10"]] = 2 ** 0.5 * cmath.cos(th)
Psi[basis["01"]] = 2 ** 0.5 * cmath.sin(th) * cmath.exp(1j * ph)
worst_minus, worst_plus = 0.0, 0.0
for t in [0.0, 0.3, 1.0, 2.2, 4.0]:
    clock_t = [cmath.exp(-1j * Om * t) / 2 ** 0.5, cmath.exp(1j * Om * t) / 2 ** 0.5]  # exp(-i Om Z t)|+>
    cond = [sum(clock_t[c].conjugate() * Psi[2 * c + s] for c in range(2)) for s in range(2)]
    psi0 = [cmath.cos(th), cmath.sin(th) * cmath.exp(1j * ph)]
    minus = [cmath.exp(-1j * Om * t) * psi0[0], cmath.exp(1j * Om * t) * psi0[1]]
    plus = [cmath.exp(1j * Om * t) * psi0[0], cmath.exp(-1j * Om * t) * psi0[1]]
    worst_minus = max(worst_minus, max(abs(x - y) for x, y in zip(cond, minus)))
    worst_plus = max(worst_plus, max(abs(x - y) for x, y in zip(cond, plus)))
print("4. max |<t|Psi>> - exp(-i H_S t)psi0| =", round(worst_minus, 12))
print("   max |<t|Psi>> - exp(+i H_S t)psi0| =", round(worst_plus, 6))
