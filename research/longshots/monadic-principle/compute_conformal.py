"""Conformal-time budget for the monadic principle in closed FLRW (k=+1).

Monadic wrap condition (paper: prop:conformal, prop:dust, Cor. cor:cauchy):
the past cone of an event at conformal time eta_b covers the whole slice at
eta_c  iff  eta_b - eta_c > pi   (pi = diameter of the unit S^3), with eta
measured in units of the curvature radius. So the total conformal past since
the earliest slice must exceed pi.

eta0 = sqrt(|Ok|) * int_0^1 da / (a^2 E(a)),  E^2 = Or a^-4 + Om a^-3 + Ok a^-2 + OL,
closure: Or + Om + Ok + OL = 1.  Om=0.3153, Or=9.2e-5, h=0.6736 (Planck 2018).
Run: python3 compute_conformal.py
"""
import math

H0_INV_GPC = 4.45   # c/H0 in Gpc for h = 0.6736
AGE_GPC = 14.2      # conformal age today (particle-horizon radius), Gpc
OM, OR = 0.3153, 9.2e-5
PI = math.pi


def eta(a_lo, a_hi, Ok):
    OL = 1.0 - OM - Ok - OR

    def integrand(a):
        if a <= 0.0:                       # radiation-era limit: 1/(a^2 E) -> 1/sqrt(Or)
            return 1.0 / math.sqrt(OR)
        E2 = OR / a**4 + OM / a**3 + Ok / a**2 + OL
        return 1.0 / (a * a * math.sqrt(max(E2, 1e-300)))

    n, s = 400000, 0.0
    da = (a_hi - a_lo) / n
    for i in range(n):
        s += (integrand(a_lo + i * da) + integrand(a_lo + (i + 1) * da)) * da / 2
    return math.sqrt(abs(Ok)) * s


def future_eta(Ok):
    """Conformal time still available from a=1 until recollapse, or to a->inf."""
    OL = 1.0 - OM - Ok - OR

    def E2(a):
        return OR / a**4 + OM / a**3 + Ok / a**2 + OL

    amax = None
    prev = 1.0
    for i in range(1, 20001):
        x = 1.0 + 59.0 * i / 20000.0
        if E2(x) < 0:                      # recollapse found
            lo, hi = prev, x
            for _ in range(80):
                m = (lo + hi) / 2
                lo, hi = (m, hi) if E2(m) > 0 else (lo, m)
            amax = (lo + hi) / 2
            break
        prev = x
    top = amax * (1 - 1e-9) if amax else 100.0
    return eta(1.0, top, Ok)


def main():
    print(f"{'Ok':>8} {'eta0 rad':>9} {'+future':>8} {'total':>7} {'total/pi':>9}  deficit/pi")
    for Ok in (-0.001, -0.010, -0.044):
        e0, ef = eta(0.0, 1.0, Ok), future_eta(Ok)
        tot = e0 + ef
        print(f"{Ok:+8.3f} {e0:9.3f} {ef:8.3f} {tot:7.3f} {tot/PI:9.2f}  {(PI-tot)/PI:8.2f}")

    # Independent analytic cross-check: eta0[rad] = age_Gpc / curvature_radius,
    # R_c = (c/H0)/sqrt|Ok|.
    for Ok in (-0.001, -0.044):
        print(f"cross-check Ok={Ok:+.3f}: {AGE_GPC*math.sqrt(abs(Ok))/H0_INV_GPC:.3f} rad")

    # Wrap without any pre-history needs |Ok| ~ 0.97:
    need = (PI * H0_INV_GPC / AGE_GPC) ** 2
    print(f"|Ok| needed for eta0=pi with hot BB only: {need:.2f}")

    # Pre-history still needed, in rad and Gpc of conformal time:
    for Ok in (-0.001, -0.044):
        e0, ef, R_c = eta(0.0, 1.0, Ok), future_eta(Ok), H0_INV_GPC / math.sqrt(abs(Ok))
        d = PI - e0
        print(f"pre-history needed Ok={Ok:+.3f}: {d:.2f} rad = {d*R_c:.0f} Gpc = "
              f"{d/e0:.1f}x observed conformal age (even the whole future leaves {(PI-e0-ef)/ef:.1f}x)")


if __name__ == "__main__":
    main()
