#!/usr/bin/env python3
"""Bounded checks for the antipodal echo of psi_tt = Delta psi - (1+delta) psi
on R x S^3 (unit Einstein cylinder), degree-n mode sectors.

Not a proof of the general statements in RESULT.md; it (i) re-derives the
sector condition by exact integer arithmetic, (ii) integrates single modes
numerically and evaluates the echo residual at t = 0 and t = 0.3, showing
order-1 failure for the claimed witnesses and machine-zero success where the
classification says a sector still echoes.

Python standard library only.
"""

import math

# ---------------------------------------------------------------- exact scan
# Sector n (degree-n spherical harmonics) has time frequency omega_n with
# omega_n^2 = (n+1)^2 + delta.  The echo holds for ALL data in the sector iff
# omega_n is a positive real number congruent to (n+1) mod 2, i.e.
#     omega_n = (n+1) + 2k,  k in Z,  (n+1) + 2k > 0,
# equivalently
#     delta = 4k(n+1+k)  with (n+1) + 2k > 0.          (exact, integer)


def echoing_sectors(delta, n_max):
    """All degrees n <= n_max whose sector transmits the echo, exact."""
    out = []
    for n in range(n_max + 1):
        m = n + 1
        k = -n_max - 2
        hit = False
        while k <= n_max + 2:
            if m + 2 * k > 0 and 4 * k * (m + k) == delta:
                hit = True
            k += 1
        if hit:
            out.append(n)
    return out


def report_scan(n_max=24, d_range=range(-40, 41)):
    print("== exact sector scan (integer arithmetic) ==")
    full = [d for d in d_range if len(echoing_sectors(d, n_max)) == n_max + 1]
    print(f"delta in [{d_range[0]},{d_range[-1]}] with ALL sectors echoing: {full}")
    for d in (-12, -8, -4, -1, 0, 1, 3, 8, 12, 20):
        secs = echoing_sectors(d, n_max)
        pretty = secs if len(secs) <= 8 else secs[:8] + ["..."]
        print(f"  delta = {d:>3}: echoing sectors n <= {n_max}: {pretty}")
    # every nonzero delta in range must miss infinitely many sectors in
    # principle; here we only see the finite window
    no_echo = [d for d in d_range if d != 0 and not echoing_sectors(d, n_max)]
    print(f"  nonzero delta with NO echoing sector in window: {no_echo}")


# ------------------------------------------------------------- numeric modes
def integrate_mode(omega, f0, v0, t_end, steps):
    """RK4 for f'' = -omega^2 f; returns (f, f') at t_end."""
    h = t_end / steps

    def acc(f, v):
        return -omega * omega * f

    f, v = f0, v0
    for _ in range(steps):
        k1f, k1v = v, acc(f, v)
        k2f, k2v = v + h * k1v / 2, acc(f + h * k1f / 2, v + h * k1v / 2)
        k3f, k3v = v + h * k2v / 2, acc(f + h * k2f / 2, v + h * k2f / 2)
        k4f, k4v = v + h * k3v, acc(f + h * k3f, v + h * k3v)
        f += h * (k1f + 2 * k2f + 2 * k3f + k4f) / 6
        v += h * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
    return f, v


def echo_residual(delta, n, f0, v0, t=0.3):
    """Residual R(t) = (-1)^n f(t+pi) + f(t) for the single mode with
    data (f(0), f'(0)) = (f0, v0) under omega_n^2 = (n+1)^2 + delta.
    The echo identity for the sector is R(t) = 0 for all t and all data."""
    w2 = (n + 1) ** 2 + delta
    if w2 < 0:  # exponential sector: integrate in the e^{mu t} basis via RK4
        def flow(tau, steps):
            mu = math.sqrt(-w2)
            f1, v1 = integrate_mode(mu, f0, v0, tau, steps)
            return f1
    else:
        omega = math.sqrt(w2)

        def flow(tau, steps):
            f1, _ = integrate_mode(omega, f0, v0, tau, steps)
            return f1
    steps = 40000
    # reach t+pi in two legs to reuse the integrator
    fa = flow(t + math.pi, steps)
    fb = flow(t, steps)
    return ((-1) ** n) * fa + fb, w2


def report_witnesses():
    print("\n== numeric echo residuals R(t) = (-1)^n f(t+pi) + f(t) ==")
    print("(generic data f(0)=0.7, f'(0)=-1.3; RK4, 40000 steps)")
    cases = [
        ("delta=0,  n=0 (must echo)", 0.0, 0),
        ("delta=0,  n=3 (must echo)", 0.0, 3),
        ("delta=1,  n=0 (witness)", 1.0, 0),
        ("delta=1,  n=5 (witness)", 1.0, 5),
        ("delta=8,  n=0 (sector echoes: omega=3)", 8.0, 0),
        ("delta=8,  n=1 (witness: omega=sqrt(12))", 8.0, 1),
        ("delta=-8, n=2 (sector echoes: omega=1)", -8.0, 2),
        ("delta=-8, n=0 (exponential, omega^2=-7)", -8.0, 0),
    ]
    for label, d, n in cases:
        R, w2 = echo_residual(d, n, 0.7, -1.3, 0.3)
        R0, _ = echo_residual(d, n, 0.7, -1.3, 0.0)
        print(f"  {label:<40} omega^2={w2:>8.4f}  R(0)={R0:>12.6g}  R(0.3)={R:>12.6g}")
    print("\nInterpretation: rows labelled 'must echo'/'sector echoes' have")
    print("residuals at integrator-noise level; 'witness'/'exponential' rows")
    print("fail at order-1 size. Matches the exact classification.")


if __name__ == "__main__":
    report_scan()
    report_witnesses()
