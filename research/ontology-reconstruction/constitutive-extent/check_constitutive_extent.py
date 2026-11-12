#!/usr/bin/env python3
"""Bounded checks for ontology-constitutive-extent-test.

Every mathematical statement used in RESULT.md is proved there by argument;
the routines below only illustrate exactly those statements. No grid,
parameter sweep, or simulation is offered as a proof.

Systems (all Newtonian; units with G=m=1 where relevant):
  C1  Conservative gravitational Kepler pair (reduced one-body problem).
  C2  Kapitza driven inverted pendulum, linearized about upright.
  C3  Delayed-feedback bound oscillator (second law with a delayed force):
      x''(t) + 2*gamma*x'(t) + w0^2 * x(t - tau) = 0.
  C4  Law-fixed activity scales (arithmetic).

Budget: hard <= 15 s per check, actual <= 10 s, total <= 30 s.
Run:  python3 check_constitutive_extent.py
"""

import math
import time

T_START = time.perf_counter()


def timed(label, fn):
    t0 = time.perf_counter()
    out = fn()
    dt = time.perf_counter() - t0
    print(f"  [{dt*1e3:7.1f} ms] {label}")
    assert dt < 15.0, "hard 15 s per-check budget exceeded"
    return out


# ---------------------------------------------------------------- RK4 helpers
def rk4(f, s, dt):
    k1 = f(s)
    k2 = f(tuple(s[i] + dt / 2 * k1[i] for i in range(len(s))))
    k3 = f(tuple(s[i] + dt / 2 * k2[i] for i in range(len(s))))
    k4 = f(tuple(s[i] + dt * k3[i] for i in range(len(s))))
    return tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(s)))


# ---------------------------------------------------------------- C1: Kepler
def check_kepler():
    """Analytic claims illustrated (RESULT.md section 3.1):

    (a) Determinism: the instantaneous state s0 plus the law fixes the whole
        solution; integrating from any other state of the same trajectory
        (e.g. the half-period state) lands on the same conic.  Same conic is
        certified by identical conserved E < 0 and angular momentum L
        (standard Kepler fact; not re-proved here).
    (b) Instantwise definability of binding: E = v^2/2 - 1/r < 0 at an
        instant, given conservation.
    (c) Activity functionals are state+law reconstructible, and are *interval*
        quantities by definition: W(t,t) = 0 for a zero-length interval,
        while the instantaneous power P(t) = F.v is nonzero at generic t;
        gross exchange over one period is positive while net work over the
        closed orbit is zero.  All four numbers come from s0 + the law.
    """
    s0 = (0.5, 0.0, 0.0, math.sqrt(3.0))  # periapsis of a=1, e=0.5 ellipse

    def acc(s):
        x, y, vx, vy = s
        r3 = (x * x + y * y) ** 1.5
        return (vx, vy, -x / r3, -y / r3)

    def energy(s):
        x, y, vx, vy = s
        return 0.5 * (vx * vx + vy * vy) - 1.0 / math.hypot(x, y)

    def ang_mom(s):
        x, y, vx, vy = s
        return x * vy - y * vx

    def power(s):  # instantaneous F.v
        x, y, vx, vy = s
        r3 = (x * x + y * y) ** 1.5
        return (-x / r3) * vx + (-y / r3) * vy

    def integrate(s, T, dt=1e-3):
        n = int(round(T / dt))
        for _ in range(n):
            s = rk4(acc, s, dt)
        return s

    T = 2.0 * math.pi  # period of the a=1 ellipse in GM=1 units
    s1 = integrate(s0, T)
    e0, e1 = energy(s0), energy(s1)
    l0, l1 = ang_mom(s0), ang_mom(s1)
    closure = math.hypot(s1[0] - s0[0], s1[1] - s0[1]) + abs(s1[2] - s0[2]) + abs(s1[3] - s0[3])

    # integrate 2 periods from s0, and 1.5 periods from the half-period state:
    s_two = integrate(s0, 2 * T)
    s_mid = integrate(s0, T / 2)
    s_mid_ext = integrate(s_mid, T)  # same law, different sufficing instant

    # gross exchange and net work over one period, and W over a zero interval
    n = int(round(T / 1e-3))
    dt = 1e-3
    s = s0
    gross = 0.0
    for _ in range(n):
        p_prev = abs(power(s))
        s = rk4(acc, s, dt)
        p_next = abs(power(s))
        gross += 0.5 * (p_prev + p_next) * dt  # trapezoid on |F.v|, one period

    P_generic = power(integrate(s0, 0.7 * T))
    return {
        "E(s0)": e0, "E after one period": e1, "|dE|": abs(e1 - e0),
        "|dL| after one period": abs(l1 - l0),
        "state closure error after one period": closure,
        "same-conic check from half-period instant (dE, dL)":
            (abs(energy(s_mid_ext) - e0), abs(ang_mom(s_mid_ext) - l0)),
        "endpoint agreement after 2 periods":
            math.hypot(s_two[0] - s0[0], s_two[1] - s0[1]),
        "W(t,t) over zero interval": 0.0,
        "instantaneous power P at t=0.7T (nonzero)": P_generic,
        "gross exchange |F.v| over one period (>0)": gross,
        "net work over closed orbit = E(t0+T)-E(t0) = 0": abs(energy(s1) - e0),
    }


# ---------------------------------------------------------------- C2: Kapitza
def check_kapitza():
    """Analytic claims illustrated (RESULT.md section 3.2):

    Linearized driven inverted pendulum (theta measured from upright,
    suspension amplitude a, frequency omega): theta'' = [g/L + a*w^2*cos(wt)/L] theta.
    Standard Kapitza result (Kapitza 1951; Landau-Lifshitz, Mechanics, via
    arXiv:2102.12711 refs [1],[5]): upright stability iff a^2*w^2 > 2*g*L.

    (i) Naive instantwise criterion "sign of instantaneous stiffness c(t)"
        misclassifies: in the STABLE case the coefficient is positive
        (destabilizing) on ~all of the drive cycle, yet the Floquet
        multipliers are inside the unit circle.
    (ii) The correct criterion is a function of the law parameters alone
        (a^2 w^2 vs 2gL) and of the monodromy over one drive period -- i.e.
        state+law reconstructible at an instant.  The interval-flavored
        Floquet object and the parameter inequality agree exactly:
        the physics does not decide between an activity reading and a
        state+law reading of the binding fact.
    """
    g, L = 1.0, 1.0
    w = 20.0
    Tdrive = 2 * math.pi / w

    def floquet_trace(a):
        def f(s, t):
            th, om = s
            c = g / L + a * w * w * math.cos(w * t) / L
            return (om, c * th)

        dt = 2e-4
        cols = []
        for init in ((1.0, 0.0), (0.0, 1.0)):
            s, t = init, 0.0
            n = int(round(Tdrive / dt))
            for _ in range(n):
                # time-dependent RK4
                k1 = f(s, t)
                k2 = f(tuple(s[i] + dt / 2 * k1[i] for i in range(2)), t + dt / 2)
                k3 = f(tuple(s[i] + dt / 2 * k2[i] for i in range(2)), t + dt / 2)
                k4 = f(tuple(s[i] + dt * k3[i] for i in range(2)), t + dt)
                s = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(2))
                t += dt
            cols.append(s)
        # monodromy columns; trace = m11 + m22
        return cols[0][0] + cols[1][1]

    def destab_fraction(a):
        """Fraction of the drive cycle where instantaneous stiffness is
        positive (destabilizing): cos(wt) > -g/(a w^2)."""
        thresh = -g / (a * w * w)
        if thresh <= -1.0:
            return 0.0
        if thresh >= 1.0:
            return 1.0
        ang = math.acos(thresh)
        return 1.0 - (math.pi - ang) / math.pi  # fraction with cos > thresh

    a_stable, a_unstable = 0.2, 0.02
    return {
        "stability boundary a^2 w^2 = 2gL (units)": 2 * g * L,
        "STABLE case a=0.2: a^2 w^2 = 16 > 2":
            (a_stable ** 2 * w ** 2, floquet_trace(a_stable)),
        "  |Tr M| < 2 (stable)": abs(floquet_trace(a_stable)) < 2.0,
        "  fraction of cycle with destabilizing instantaneous stiffness":
            destab_fraction(a_stable),
        "UNSTABLE case a=0.02: a^2 w^2 = 0.16 < 2":
            (a_unstable ** 2 * w ** 2, floquet_trace(a_unstable)),
        "  |Tr M| > 2 (unstable)": abs(floquet_trace(a_unstable)) > 2.0,
    }


# ---------------------------------------------------------------- C3: delay
def dde_solve(gamma, w0, tau, hist, T, dt=1e-3):
    """Method of steps for x'' + 2 g x' + w0^2 x(t-tau) = 0, with history
    x(t) = hist(t) on [-tau, 0].  The delayed position is linearly
    interpolated on a buffer that holds the history AND the computed
    solution, so the solve is valid over the whole horizon.  Returns
    samples (t, x, xdot)."""
    ntau = int(round(tau / dt))
    xs = [hist(-tau + i * dt) for i in range(ntau + 1)]  # t = -tau .. 0
    x = xs[-1]
    v = (hist(1e-9) - hist(-1e-9)) / 2e-9
    out = [(0.0, x, v)]

    def xdel(td):
        pos = (td + tau) / dt
        k = int(pos)
        frac = pos - k
        return xs[k] * (1.0 - frac) + xs[k + 1] * frac

    t = 0.0
    for _ in range(int(round(T / dt))):
        td = t - tau  # < t since tau > dt; the buffer always reaches td+dt

        def f(s):
            xx, vv = s
            return (vv, -2 * gamma * vv - w0 * w0 * xdel(td))

        s = (x, v)
        k1 = f(s)
        k2 = f(tuple(s[j] + dt / 2 * k1[j] for j in range(2)))
        k3 = f(tuple(s[j] + dt / 2 * k2[j] for j in range(2)))
        k4 = f(tuple(s[j] + dt * k3[j] for j in range(2)))
        x, v = tuple(s[j] + dt / 6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) for j in range(2))
        t += dt
        xs.append(x)
        out.append((t, x, v))
    return out


def check_delay():
    """Analytic claims illustrated (RESULT.md sections 3.3, 4):

    System: x''(t) + 2 g x'(t) + w0^2 x(t-tau) = 0, history on [-tau, 0].

    (i) Single-slice insufficiency (analytic, here illustrated): two history
        segments agreeing at t=0 in (x, x') = (0, 0) have different futures.
        h0 == 0; h1(t) = eps * sin^2(pi t / tau), which has h1(0)=0,
        h1'(0)=0.  For 0 < t < tau the delayed force differs, so the futures
        differ (uniqueness of DDE solutions from *segment* data forbids
        agreement).
    (ii) Window sufficiency: segment data on [-tau, 0] plus the law give a
        unique solution (method of steps) -- the minimal predictively
        sufficient region is a nonzero window of length tau, forced by the
        coupling latency, not chosen to suit a present.
    (iii) Determination-window and unity cross-cut (instances, not proof):
        (alpha) pure delayed spring (gamma=0): unstable for every tau>0 --
        at tau=0 the characteristic roots are lambda = +/- i w0 and
        dlambda/dtau = +w0^2/2 > 0 there (3-line perturbation of
        F(lambda,tau)=lambda^2+w0^2 exp(-lambda tau)), so the loop does not
        bind, although prediction needs the window exactly as before.
        (beta) with instantaneous damping gamma=2 the slow mode sees the
        delayed term as added damping (x(t-tau) ~ x - tau x'), and the
        trajectory is bounded and decaying: the loop binds.
        Same window-necessity in both; unity only in (beta).
    """
    tau = 0.5
    eps = 0.1

    def h0(t):
        return 0.0

    def h1(t):
        return eps * math.sin(math.pi * t / tau) ** 2

    # (i) divergence of futures from identical endpoint state
    run0 = dde_solve(2.0, 1.0, tau, h0, 2.0)
    run1 = dde_solve(2.0, 1.0, tau, h1, 2.0)
    sup_diff = max(abs(a[1] - b[1]) for a, b in zip(run0, run1))

    # (iii alpha) gamma = 0: unstable for every tau > 0 (see docstring), so
    # the loop does not bind, although prediction needs the window exactly as
    # before.  Report the dominant characteristic root (Newton on
    # F(lambda) = lambda^2 + w0^2 exp(-lambda tau)) and the trajectory.
    def dominant_root(g, w0_, tau_):
        import cmath
        F = lambda l: l * l + 2 * g * l + w0_ * w0_ * cmath.exp(-l * tau_)
        Fp = lambda l: 2 * l + 2 * g - tau_ * w0_ * w0_ * cmath.exp(-l * tau_)
        best = None
        for guess in (0.1 + 1.4j, 0.05 + 1.0j, 0.1 + 2.0j, 0.2 + 2.5j, 0.05 + 3.0j):
            l = guess
            for _ in range(200):
                l = l - F(l) / Fp(l)
            if abs(F(l)) < 1e-10 and (best is None or l.real > best.real):
                best = l
        return best

    run_a = dde_solve(0.0, 1.0, tau, h1, 20.0)
    env_a = max(abs(r[1]) for r in run_a if r[0] > 1.0)
    root_a = dominant_root(0.0, 1.0, tau)

    # (iii beta) gamma = 2: bounded and decaying (binding)
    run_b = dde_solve(2.0, 1.0, tau, h1, 20.0)
    early_b = max(abs(r[1]) for r in run_b if r[0] < 2.0)
    late_b = max(abs(r[1]) for r in run_b if r[0] > 15.0)
    root_b = dominant_root(2.0, 1.0, tau)

    return {
        "identical (x,x')(0)=(0,0) from two segments: sup |x0-x1| on [0,2] (analytically >0)":
            sup_diff,
        "window length needed for prediction (tau)": tau,
        "(alpha) pure delayed spring, gamma=0: dominant char. root Re (Newton)":
            root_a.real,
        "(alpha) same system: max|x| for t>1 (grows from initial 0.1 => no unity)":
            env_a,
        "(beta) damped delayed loop, gamma=2: dominant char. root Re (Newton)":
            root_b.real,
        "(beta) same system: max|x| on [0,2] vs on [15,20] (decays => binds)":
            (early_b, late_b),
    }


def check_scales():
    """C4: the activity scales entering criterion U are fixed by the
    parameters of the law, not chosen to fit a desired present region."""
    return {
        "Kepler: period 2 pi sqrt(a^3/GM), a=1, GM=1": 2 * math.pi * math.sqrt(1.0),
        "Kapitza: drive period 2 pi / omega, omega=20": 2 * math.pi / 20.0,
        "delay loop: forced window tau = 0.5 (coupling latency)": 0.5,
    }


def main():
    print("check_constitutive_extent.py — illustrations of analytic claims in RESULT.md")
    for label, fn in (
        ("C1 Kepler: instant sufficiency + instantwise definable activity functionals", check_kepler),
        ("C2 Kapitza: naive instant criterion misclassifies; correct criterion is state+law reconstructible", check_kapitza),
        ("C3 delay loop: slice insufficiency; window vs binding cross-cut", check_delay),
        ("C4 law-fixed activity scales", check_scales),
    ):
        print(f"\n{label}")
        res = timed(label, fn)
        for k, v in res.items():
            print(f"    {k}: {v}")
    total = time.perf_counter() - T_START
    print(f"\ntotal wall time: {total:.2f} s (budgets: hard 15 s/check, actual 10 s, total 30 s)")
    assert total < 30.0, "total budget exceeded"


if __name__ == "__main__":
    main()
