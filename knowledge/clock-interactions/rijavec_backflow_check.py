#!/usr/bin/env python3
"""Check of a consequence we draw (not the author's claim) from Rijavec,
arXiv:2204.11740v3, Sec. VI.4, Eqs. (89)-(91).

Rijavec's conditioned qubit map for an equal mixture of two eigensectors of the
universe Hamiltonian (eigenvalues 0 and E), with the commuting interaction
V = (1/Lambda) H (x) h, is, up to a common unitary U_0(t),
    Phi_t(rho) = 1/2 (rho + R(t) rho R(t)^dagger),  R(t) = exp(-i theta(t) sigma_x / 2),
    theta(t) = E_I * E * t / (Delta * Lambda)                       (from Eq. 90)
The paper states the state of |0><0| becomes maximally mixed at t = tau_D (Eq. 91).
Here we check that (i) theta(tau_D) = pi gives the maximally mixed state, and
(ii) the trace distance between the images of |0><0| and |1><1| is |cos(theta/2)|,
which is non-monotone in t (it returns to 1 at theta = 2 pi). Non-monotone trace
distance is information backflow, which excludes CP-divisibility of the family.

Domain: one model, two sectors, equal weights, the paper's commuting interaction,
ideal clock, mixed "stationary" universe state spanning two constraint values.
It is not a statement about a single constraint surface H = 0, where Rijavec's
evolution is unitary (Eq. 58). Standard library only.
"""
import cmath
import math


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def dag(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def R(theta):
    c, s = math.cos(theta / 2), math.sin(theta / 2)
    return [[c, -1j * s], [-1j * s, c]]


def phi(rho, theta):
    r = R(theta)
    rot = mat_mul(mat_mul(r, rho), dag(r))
    return [[0.5 * (rho[i][j] + rot[i][j]) for j in range(2)] for i in range(2)]


def trace_distance(a, b):
    d = [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]
    # 2x2 Hermitian traceless difference here: eigenvalues +-sqrt(-det)
    det = d[0][0] * d[1][1] - d[0][1] * d[1][0]
    tr = d[0][0] + d[1][1]
    disc = cmath.sqrt(tr * tr - 4 * det)
    return 0.5 * (abs((tr + disc) / 2) + abs((tr - disc) / 2))


zero = [[1, 0], [0, 0]]
one = [[0, 0], [0, 1]]
mm = phi(zero, math.pi)
print("(i) Phi_{theta=pi}(|0><0|) =", [[round(abs(x), 12) for x in row] for row in mm])
prev, rises = None, 0
for k in range(0, 41):
    th = 2 * math.pi * k / 40
    D = trace_distance(phi(zero, th), phi(one, th))
    if prev is not None and D > prev + 1e-12:
        rises += 1
    assert abs(D - abs(math.cos(th / 2))) < 1e-12
    prev = D
print("(ii) D(theta) == |cos(theta/2)| on 41 grid points; number of increases =", rises)
