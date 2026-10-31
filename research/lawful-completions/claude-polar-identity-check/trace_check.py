"""Double-null test of the cubic central trace; not a proof. Stdlib only, 15 s limit.

March the SSESF first-order system of SMOOTHNESS_BOOTSTRAP.md s1 on the finite
cone from u0, with the axis at u=v, and report at central proper time T:
    e(eps) = |phi(t(T),t(T)) - Phi(T)|.
CUBIC_TRACE.md predicts e = O(eps^3), so e doubles by a factor near 8.
Two grids separate this scaling from the discretization error.
A second run adds a tail after readout. Its unchanged reading is forced by the
marching order, so that line illustrates decoupling and does not test it.
"""
import math
import signal

signal.alarm(15)

U0, V_MAX = -4.0, 3.0


def bump(v, a, b):
    if v <= a or v >= b:
        return 0.0
    s = 2.0 * (v - a) / (b - a) - 1.0
    return math.exp(1.0 - 1.0 / (1.0 - s * s))


def run(eps, N, T, tail=0.0):
    """Return the central reading at proper time T and the mass at (U0, V_MAX)."""
    h = (V_MAX - U0) / N
    v = [U0 + h * j for j in range(N + 1)]
    Phi = [eps * bump(x, 1.0, 3.0) + tail * bump(x, 2.6, 2.95) for x in v]
    lam = [0.5] * (N + 1)
    q = [0.5 * p for p in Phi]
    r = [0.5 * (x - U0) for x in v]
    p = [0.0] * (N + 1)
    for j in range(1, N + 1):
        p[j] = p[j - 1] + 0.5 * h * (q[j - 1] + q[j])
    m = [0.0] * (N + 1)

    def source(j, r, m, nu, lam, p):
        if r[j] <= 0.0:
            return 0.0, 0.0
        f = 1.0 - 2.0 * m[j] / r[j]
        Q = 2.0 * m[j] * nu[j] * lam[j] / (f * r[j] * r[j])
        return Q, Q * p[j] / r[j]

    def flux(j, q, lam, p, r, m):
        if r[j] <= 0.0:
            return 0.0
        f = 1.0 - 2.0 * m[j] / r[j]
        w = q[j] - lam[j] * p[j] / r[j]
        return f * w * w / (2.0 * lam[j])

    for j in range(1, N + 1):
        m[j] = m[j - 1] + 0.5 * h * (flux(j - 1, q, lam, p, r, m) + flux(j, q, lam, p, r, m))
    nu = [-0.5] * (N + 1)
    m_total = m[N]
    t_axis, phi_axis, lam_axis = [U0], [q[0] / lam[0]], [lam[0]]
    for i in range(N):
        Fl = [0.0] * (N + 1)
        Fq = [0.0] * (N + 1)
        for j in range(i + 1, N + 1):
            Fl[j], Fq[j] = source(j, r, m, nu, lam, p)
        l0, q0 = lam, q
        for it in range(2):
            ln, qn = l0[:], q0[:]
            if it == 0:
                for j in range(i + 1, N + 1):
                    ln[j] = l0[j] + h * Fl[j]
                    qn[j] = q0[j] + h * Fq[j]
            else:
                for j in range(i + 1, N + 1):
                    a, b = source(j, rn, mn, nun, lp, pn)
                    ln[j] = l0[j] + 0.5 * h * (Fl[j] + a)
                    qn[j] = q0[j] + 0.5 * h * (Fq[j] + b)
            rn, pn, mn, nun = [0.0] * (N + 1), [0.0] * (N + 1), [0.0] * (N + 1), [0.0] * (N + 1)
            nun[i + 1] = -ln[i + 1]
            for j in range(i + 1, N):
                rn[j + 1] = rn[j] + 0.5 * h * (ln[j] + ln[j + 1])
                pn[j + 1] = pn[j] + 0.5 * h * (qn[j] + qn[j + 1])
                g0 = flux(j, qn, ln, pn, rn, mn)
                mn[j + 1] = mn[j] + h * g0
                g1 = flux(j + 1, qn, ln, pn, rn, mn)
                mn[j + 1] = mn[j] + 0.5 * h * (g0 + g1)
                Q0, _ = source(j, rn, mn, nun, ln, pn)
                nun[j + 1] = nun[j] + h * Q0
                Q1, _ = source(j + 1, rn, mn, nun, ln, pn)
                nun[j + 1] = nun[j] + 0.5 * h * (Q0 + Q1)
            lp = ln
        lam, q, r, p, m, nu = ln, qn, rn, pn, mn, nun
        t_axis.append(U0 + h * (i + 1))
        phi_axis.append(q[i + 1] / lam[i + 1])
        lam_axis.append(lam[i + 1])
    tau = 0.0
    prev_t, prev_phi = 0.0, 0.0
    for k in range(1, len(t_axis)):
        if t_axis[k] <= 1e-9:  # the clock starts at t=0, which is a grid point
            continue
        step = 0.5 * (2 * lam_axis[k - 1] + 2 * lam_axis[k]) * h
        if tau + step >= T:
            w = (T - tau) / step
            return phi_axis[k - 1] + w * (phi_axis[k] - phi_axis[k - 1]), m_total
        tau += step
    raise RuntimeError("readout not reached")


T = 1.7
base = bump(T, 1.0, 3.0)
print(f"1. central reading at proper time T={T}: e=|phi - Phi(T)|")
prev = None
for eps in (0.2, 0.4, 0.8):
    a, _ = run(eps, 280, T)
    b, _ = run(eps, 560, T)
    best = b + (b - a) / 3.0
    e = abs(best - eps * base)
    print(f"   eps={eps:.1f} e={e:.4e} e/eps^3={e / eps ** 3:.4f} grid_change={abs(b - a):.2e} "
          f"factor={'-' if prev is None else format(e / prev, '.2f')}")
    prev = e

print("2. tail arriving after readout: same reading, more outgoing-cone mass")
for tail in (0.0, 0.6):
    phi, mass = run(0.4, 420, T, tail)
    print(f"   tail={tail:.1f} phi={phi:.10f} m(u0,Vmax)={mass:.6f}")
