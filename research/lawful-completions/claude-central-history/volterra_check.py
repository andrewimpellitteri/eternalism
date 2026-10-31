"""Try to falsify causal inversion of the central trace; not a proof. Stdlib, 15 s limit.

Exact axis identity on a finite cone with L=Phi on the cone and log 2lam = int K:
    2 lam(t,t) phi_c(t) = Phi(t) + I[Phi](t),   I = int 2 lam K phi (s,t) ds.
Prescribing phi_c(t) = y(tau(t)) gives the causal fixed point
    Phi(t) = 2 lam(t,t) y(tau(t)) - I[Phi](t) = Phi(t) + 2 lam (y o tau - phi_c).
Raising omega at fixed amplitude raises the scale-invariant size eps*omega and can
collapse (eps=0.6, omega=6pi blows up), so derivative loss is tested at fixed eps*omega.
These ratios cover one domain. Grids cannot prove the claim.
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


def evolve(Phi, N):
    """March the first-order SSESF system; return axis arrays t, phi_c, lam."""
    h = (V_MAX - U0) / N
    v = [U0 + h * j for j in range(N + 1)]
    lam = [0.5] * (N + 1)
    q = [0.5 * x for x in Phi]
    r = [0.5 * (x - U0) for x in v]
    p = [0.0] * (N + 1)
    for j in range(1, N + 1):
        p[j] = p[j - 1] + 0.5 * h * (q[j - 1] + q[j])
    m = [0.0] * (N + 1)
    nu = [-0.5] * (N + 1)

    def source(j, r, m, nu, lam, p):
        if r[j] <= 0.0:
            return 0.0, 0.0
        Q = 2.0 * m[j] * nu[j] * lam[j] / ((1.0 - 2.0 * m[j] / r[j]) * r[j] * r[j])
        return Q, Q * p[j] / r[j]

    def flux(j, q, lam, p, r, m):
        if r[j] <= 0.0:
            return 0.0
        w = q[j] - lam[j] * p[j] / r[j]
        return (1.0 - 2.0 * m[j] / r[j]) * w * w / (2.0 * lam[j])

    for j in range(1, N + 1):
        m[j] = m[j - 1] + 0.5 * h * (flux(j - 1, q, lam, p, r, m) + flux(j, q, lam, p, r, m))
    phi_c = [q[0] / lam[0]]
    lam_c = [lam[0]]
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
        phi_c.append(q[i + 1] / lam[i + 1])
        lam_c.append(lam[i + 1])
    return v, phi_c, lam_c, h


def invert(eps, omega, N, iters):
    target = lambda T: eps * bump(T, 1.0, 2.9) * math.cos(omega * (T - 2.0))
    v0 = [U0 + (V_MAX - U0) / N * j for j in range(N + 1)]
    Phi = [target(x) if x > 0.0 else 0.0 for x in v0]
    out = []
    for _ in range(iters):
        v, phi, lam, h = evolve(Phi, N)
        tau = [0.0] * (N + 1)
        for k in range(1, N + 1):
            if v[k] > 1e-9:
                tau[k] = tau[k - 1] + h * (lam[k - 1] + lam[k])
        res = [target(tau[k]) - phi[k] if v[k] > 1e-9 else 0.0 for k in range(N + 1)]
        c0 = max(abs(x) for x in res)
        c1 = max(abs(res[k + 1] - res[k]) / h for k in range(N))
        out.append((c0, c1))
        Phi = [Phi[k] + 2.0 * lam[k] * res[k] for k in range(N + 1)]
    return out


def show(eps, omega, N, iters):
    o = invert(eps, omega, N, iters)
    r0 = [o[k + 1][0] / o[k][0] for k in range(iters - 1) if o[k][0] > 1e-13]
    r1 = [o[k + 1][1] / o[k][1] for k in range(iters - 1) if o[k][1] > 1e-12]
    print(f"   eps={eps:.2f} omega={omega:5.1f} C0={' '.join(format(a, '.1e') for a, _ in o)}")
    print(f"      C1={' '.join(format(b, '.1e') for _, b in o)}  "
          f"C0 ratio {r0[-1]:.3f}  C1 ratio {r1[-1]:.3f}")


if __name__ == "__main__":
    print("Residual of phi_c - y o tau per iteration, with the last contraction ratio")
    print("1. fixed |y'|: eps*omega held at 1.88, the fair derivative-loss test")
    for w in (2, 6, 12, 18):
        show(0.3 * 2 / w, w * math.pi, 560, 4)
    print("2. amplitude sweep at fixed omega: a Lipschitz constant O(eps^2) quarters")
    for e in (0.3, 0.15, 0.075):
        show(e, 6 * math.pi, 420, 4)
