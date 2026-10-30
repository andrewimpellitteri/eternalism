"""Bounded sanity checks for the polar system; not a proof. Stdlib only, 15 s limit.

1. Momentum: evolve U_T = A_j d_j(c[U] U) radially, with f, c from the radial
   constraints alone, and test M = m_T - c f R^2 P Q -> 0 under refinement.
2. Formula: compare the Z ray integral with the ODE solution for f.
3. Falsification scan for estimate (B) on concentrated pulses and thin shells.
"""
import math
import signal

signal.alarm(15)


def cumtrapz(y, h):
    out, s = [0.0] * len(y), 0.0
    for i in range(1, len(y)):
        s += 0.5 * (y[i] + y[i - 1]) * h
        out[i] = s
    return out


def constraints(P, Q, R, h):
    """f, c, m from e by the integrating-factor formulas with regular center."""
    n = len(R)
    H = cumtrapz([R[i] * (P[i] * P[i] + Q[i] * Q[i]) for i in range(n)], h)
    Ei = cumtrapz([math.exp(x) for x in H], h)
    f = [1.0] * n
    for i in range(1, n):
        f[i] = math.exp(-H[i]) * Ei[i] / R[i]
    m = [0.5 * R[i] * (1.0 - f[i]) for i in range(n)]
    g = [0.0] * n
    for i in range(1, n):
        g[i] = (1.0 - f[i]) / (f[i] * R[i])
    logc = cumtrapz(g, h)
    return f, [math.exp(x) for x in logc], m


def faces(P, Q):
    """Face values: P lives at cell centers, Q at faces; P is even across R=0."""
    n = len(Q)
    Pf = [P[0]] + [0.5 * (P[i - 1] + P[i]) for i in range(1, n - 1)] + [P[-1]]
    Ef = [P[0] ** 2] + [0.5 * (P[i - 1] ** 2 + P[i] ** 2) for i in range(1, n - 1)] + [P[-1] ** 2]
    Eq = [math.sqrt(max(Ef[i], 0.0)) for i in range(n)]
    return Pf, Eq


def rhs(P, Q, R, h):
    """Conservative staggered form of P_T=div(cW), W_T=grad(cP).

    For frozen c=1 this is skew in the R^2-weighted inner product. The
    collocated R^-2 d_R(R^2 .) form was unstable at the center and is not used.
    """
    n = len(R)
    _, Eq = faces(P, Q)
    _, c, _ = constraints(Eq, Q, R, h)
    flux = [R[i] * R[i] * c[i] * Q[i] for i in range(n)]
    P_T = [3.0 * (flux[i + 1] - flux[i]) / (R[i + 1] ** 3 - R[i] ** 3) for i in range(n - 1)]
    cP = [0.5 * (c[i] + c[i + 1]) * P[i] for i in range(n - 1)]
    Q_T = [0.0] + [(cP[i] - cP[i - 1]) / h for i in range(1, n - 1)] + [0.0]
    return P_T, Q_T


def step(P, Q, R, h, dt):
    def add(a, b, s):
        return [x + s * y for x, y in zip(a, b)]
    k1 = rhs(P, Q, R, h)
    k2 = rhs(add(P, k1[0], .5 * dt), add(Q, k1[1], .5 * dt), R, h)
    k3 = rhs(add(P, k2[0], .5 * dt), add(Q, k2[1], .5 * dt), R, h)
    k4 = rhs(add(P, k3[0], dt), add(Q, k3[1], dt), R, h)
    w = lambda i: [(k1[i][j] + 2 * k2[i][j] + 2 * k3[i][j] + k4[i][j]) / 6.0
                   for j in range(len(k1[i]))]
    return add(P, w(0), dt), add(Q, w(1), dt)


def momentum(N, amp=0.35, T=1.0, Rmax=6.0):
    h = Rmax / N
    R = [h * i for i in range(N + 1)]
    Q = [-2 * amp * r * math.exp(-r * r) for r in R]
    Q[-1] = 0.0
    P = [0.8 * amp * math.exp(-((i + .5) * h) ** 2) for i in range(N)]
    dt = 0.25 * h
    for _ in range(int(round(T / dt)) - 1):
        P, Q = step(P, Q, R, h, dt)
    Pm, Qm = P, Q
    P0, Q0 = step(Pm, Qm, R, h, dt)
    Pp, Qp = step(P0, Q0, R, h, dt)
    mass = lambda p, q: constraints(faces(p, q)[1], q, R, h)
    mp, mm = mass(Pp, Qp)[2], mass(Pm, Qm)[2]
    f, c, _ = mass(P0, Q0)
    Pf, _ = faces(P0, Q0)
    res = sup = 0.0
    for i, r in enumerate(R):
        if r <= 4.0:
            m_T = (mp[i] - mm[i]) / (2 * dt)
            res = max(res, abs(m_T - c[i] * f[i] * r * r * Pf[i] * Q0[i]))
            sup = max(sup, abs(m_T))
    return res, sup, min(f), max(c), Q0[1] / h


print("1. momentum residual sup|m_T - c f R^2 P Q| on R<=4 (staggered scheme)")
prev = None
for N in (120, 240, 480, 960):
    r, mt, fmin, cmax, q0 = momentum(N)
    print(f"   N={N:4d} res={r:.3e} sup|m_T|={mt:.3e} "
          f"ratio={'-' if prev is None else format(prev / r, '.2f')} "
          f"fmin={fmin:.3f} cmax={cmax:.3f} Q(h)/h={q0:.4f}")
    prev = r

# 2. Ray formula at sample radii against the ODE solution.
N = 6000
h = 3.0 / N
R = [h * i for i in range(N + 1)]
e = [(0.9 + 0.5 * math.cos(3 * r)) * math.exp(-r * r / 2) for r in R]


def ei(x):
    i = min(int(x / h), N - 1)
    t = x / h - i
    return (1 - t) * e[i] + t * e[i + 1]


H = cumtrapz([R[i] * e[i] for i in range(N + 1)], h)
Ei = cumtrapz([math.exp(x) for x in H], h)
worst = 0.0
for X in (0.4, 1.1, 2.3):
    i = int(round(X / h))
    X = R[i]
    ns, nz = 400, 200
    Z = 0.0
    for a in range(ns):
        s = (a + .5) / ns
        J = sum((z := s + (1 - s) * (b + .5) / nz) * ei(z * X) for b in range(nz)) * (1 - s) / nz
        Z += s * s * ei(s * X) * math.exp(-X * X * J) / ns
    worst = max(worst, abs(1 - X * X * Z - math.exp(-H[i]) * Ei[i] / X))
print(f"2. max|1-R^2 Z - f_ODE| at sample radii = {worst:.2e}")

# 3. Estimate (B): L2(B_1, 3d measure) ratio with ||U||_inf <= 1.
N = 4000
h = 1.0 / N
R = [h * i for i in range(N + 1)]
zero = [0.0] * (N + 1)


def coeff(U):
    f, c, _ = constraints(U, zero, R, h)
    grad = [0.0] * (N + 1)
    for i in range(1, N + 1):
        Z = (1 - f[i]) / (R[i] * R[i])
        grad[i] = c[i] * R[i] * Z / f[i]
    return c, grad


def l2(y):
    return math.sqrt(sum(4 * math.pi * R[i] ** 2 * y[i] ** 2 for i in range(N + 1)) * h)


best = (0.0, None)
for eta in (0.01, 0.03, 0.1):
    for name, cen in (("center", 0.0), ("shell.1", 0.1), ("shell.9", 0.9)):
        bump = [math.exp(-((r - cen) / eta) ** 2) for r in R]
        for base in (0.0, 0.5, 1.0):
            V = [base] * (N + 1)
            U = [min(base + b, 1.0) if base < 1.0 else 1.0 - b for b in bump]
            cu, gu = coeff(U)
            cv, gv = coeff(V)
            D = [a - b for a, b in zip(U, V)]
            q = (l2([a - b for a, b in zip(cu, cv)])
                 + l2([a - b for a, b in zip(gu, gv)])) / l2(D)
            if q > best[0]:
                best = (q, (name, eta, base))
print(f"3. largest (B) ratio on B_1 over the scan = {best[0]:.3f} at {best[1]}")
