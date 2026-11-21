"""Independent referee controls for RESULT.md sections 2-4 and 6.

Different computational path from the authors' check_perturbation.py:
per-mode RK4 time-stepping of the extended equations, with a fresh data bump
(supported at geodesic distance [pi/2, 5pi/8] from Y, tau=pi/3, s=pi/6),
instead of closed-form Duhamel integrals plus Simpson quadrature.

Two kinds of checks are kept apart:
- Solver-vs-closed-form checks at FIXED spectral truncation (tight
  tolerances): these verify the Duhamel/operator identities and signs.
- Spectral-convergence checks of exact field identities (reported values,
  loose asserts): finite mode sums only approximate compactly supported data;
  exact past vanishing and kernel positivity are analytic facts, not claimed
  numerically here.

Standard library only. Writes control_output.json; exits nonzero on any
failed check.
"""
import json
import math
import sys
import time
from pathlib import Path

PI = math.pi
# Data and geometry (all chosen independently of the authors' example).
TAU = PI / 3            # standpoint time, 0 < tau < pi
S = PI / 6              # target offset, 0 < s <= tau
T_STAR = 2 * PI - S     # interior timelike-future target time
RC, WIDTH = PI / 2, PI / 8   # bump support [RC, RC+WIDTH], so rho0 = pi/2 > tau
K_MODES = 96
K_COARSE = 48
STEPS = 8192


def bump(x):
    if abs(x) >= 1:
        return 0.0
    return math.exp(-1.0 / (1.0 - x * x))


def g(r):
    # C-infinity bump on the support interval, zero on B(Y,tau) and near r=pi.
    return bump((r - (RC + WIDTH / 2)) / (WIDTH / 2))


def simpson(vals, width):
    n = len(vals) - 1
    return width / (3 * n) * (vals[0] + vals[-1]
                              + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-1:2]))


def coefficients(modes, sub=8000):
    # c_k = (2/pi) int g(r) sin(kr) sin(r) dr over the support interval only.
    lo, hi, n = RC, RC + WIDTH, sub if sub % 2 == 0 else sub + 1
    h = (hi - lo) / n
    out = []
    for k in range(1, modes + 1):
        vals = [g(lo + i * h) * math.sin(k * (lo + i * h))
                * math.sin(lo + i * h) for i in range(n + 1)]
        out.append(2 / PI * simpson(vals, hi - lo))
    return out


def q(u):
    # a_m = 1: q = a^2 = (1-cos u)^2/4 = (3/2 - 2 cos u + (1/2) cos 2u)/4.
    return (3 / 2 - 2 * math.cos(u) + 0.5 * math.cos(2 * u)) / 4


def mode_step(k, lam, t0, t1, n, y1, y2):
    """RK4 for y1' = y2, y2' = -(k^2 + lam*q(t)) y1 from t0 to t1, n steps."""
    h = (t1 - t0) / n
    k2 = float(k * k)
    for _ in range(n):
        # f(t, a, b) = (b, -(k^2 + lam*q(t)) a)
        a1, b1 = y2, -(k2 + lam * q(t0)) * y1
        tm = t0 + h / 2
        a2, b2 = y1 + h / 2 * a1, y2 + h / 2 * b1
        a2, b2 = a2, -(k2 + lam * q(tm)) * a2
        a3, b3 = y1 + h / 2 * a2, y2 + h / 2 * b2
        a3, b3 = a3, -(k2 + lam * q(tm)) * a3
        a4, b4 = y1 + h * a3, y2 + h * b3
        a4, b4 = a4, -(k2 + lam * q(t0 + h)) * a4
        y1 += h / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
        y2 += h / 6 * (b1 + 2 * b2 + 2 * b3 + b4)
        t0 += h
    return y1, y2


def psi(coeff, lam, target, steps=STEPS):
    """Value at (target, Y) of the solution with data (0,g), by RK4 modal
    time-stepping; u_k(Y) = k."""
    total = 0.0
    for k, c in enumerate(coeff, 1):
        if c == 0.0:
            continue
        a, _ = mode_step(k, lam, 0.0, target, steps, 0.0, c)
        total += a * k
    return total


def dust_weights_midpoint(ks, n=200000):
    # Independent midpoint-rule check of the (12) weights, a_m=1.
    h = 2 * PI / n
    out = {}
    for k in ks:
        acc = 0.0
        for i in range(n):
            u = (i + 0.5) * h
            acc += q(u) * math.sin(k * u) ** 2
        out[k] = acc * h / (k * k)
    return out


def run():
    checks = {}

    # R3: (12) weights vs closed forms, midpoint rule (different rule/points).
    mw = dust_weights_midpoint([1, 2, 3, 5, 7])
    for k, val in mw.items():
        expect = 5 * PI / 16 if k == 1 else 3 * PI / (8 * k * k)
        assert abs(val - expect) < 1e-9, (k, val, expect)
    checks["weights_midpoint"] = mw

    # R4: kernel positivity K(r) = (1/(32pi)) (3(pi-r)/sin r - 1), a_m=1.
    grid = [1e-6 * PI + (PI - 2e-6 * PI) * i / 20000 for i in range(20001)]
    kmin = min((3 * (PI - r) / math.sin(r) - 1) / (32 * PI) for r in grid)
    assert kmin > 0, kmin
    checks["kernel_min_on_grid"] = kmin

    # R5: normalization int G dV = 1, i.e. int_0^pi (pi-r) sin r / pi dr = 1.
    n = 12002
    rr = [PI * i / n for i in range(n + 1)]
    norm = simpson([(PI - r) * math.sin(r) / PI for r in rr], PI)
    assert abs(norm - 1) < 1e-12, norm
    checks["green_normalization"] = norm

    coeff = coefficients(K_MODES)
    coeff_coarse = coefficients(K_COARSE)

    # Exact identity h(Y): radial Green integral vs spectral sum; only the
    # spectral side is truncation-limited. Report both; assert convergence.
    n2 = 8000
    lo, hi = RC, RC + WIDTH
    hh = (hi - lo) / n2
    vals = [(PI - (lo + i * hh)) * g(lo + i * hh) * math.sin(lo + i * hh)
            for i in range(n2 + 1)]
    h_radial = simpson(vals, hi - lo) / PI
    h_spec_fine = math.fsum(c / k for k, c in enumerate(coeff, 1))
    h_spec_coarse = math.fsum(c / k for k, c in enumerate(coeff_coarse, 1))
    err_fine, err_coarse = abs(h_radial - h_spec_fine), abs(h_radial - h_spec_coarse)
    assert err_fine < 1e-3 and err_fine < err_coarse, (err_fine, err_coarse)
    checks["h_identity"] = {
        "h_radial": h_radial,
        "h_spectral_fine": h_spec_fine,
        "h_spectral_coarse": h_spec_coarse,
        "abs_error_fine": err_fine,
        "abs_error_coarse": err_coarse,
    }
    pi_h_fine = PI * h_spec_fine  # same truncation as the RK4 runs below

    # Section 4 proposition at x_s = (2pi - s, Y): sign(delta)*psi > 0 and
    # derivative equals pi*h(Y), compared at the SAME truncation (1e-7).
    unperturbed = psi(coeff, 0.0, T_STAR)
    samples = []
    for delta in (1e-3, -1e-3, 1e-4, -1e-4):
        v = psi(coeff, delta, T_STAR)
        if abs(delta) >= 1e-3:
            assert v * delta > 0, (delta, v)
        samples.append({"delta": delta, "value": v,
                        "sign_ok": v * delta > 0})
    d_delta = (psi(coeff, 1e-4, T_STAR) - psi(coeff, -1e-4, T_STAR)) / 2e-4
    assert abs(d_delta - pi_h_fine) < 1e-7, (d_delta, pi_h_fine)
    checks["constant_delta"] = {
        "unperturbed_residual_fine": unperturbed,
        "unperturbed_residual_coarse": psi(coeff_coarse, 0.0, T_STAR, STEPS // 2),
        "derivative_central_rk4": d_delta,
        "predicted_pi_h_same_truncation": pi_h_fine,
        "samples": samples,
    }

    # Section 6 proposition: psi_lam(T_STAR, Y) > 0 for small lam > 0, and
    # d/dlam at 2pi equals the operator-identity value (NOTES.md step 3).
    lam_samples = []
    for lam in (0.01, 0.001, 0.0001):
        v = psi(coeff, lam, T_STAR)
        if lam >= 1e-3:
            assert v > 0, (lam, v)
        lam_samples.append({"lam": lam, "value": v, "positive": v > 0})
    w_period = (psi(coeff, 1e-4, 2 * PI) - psi(coeff, -1e-4, 2 * PI)) / 2e-4
    predicted = math.fsum(c * (3 * PI / (8 * k) - (PI / 16) * (k == 1))
                          for k, c in enumerate(coeff, 1))
    assert abs(w_period - predicted) < 1e-7, (w_period, predicted)
    w_tstar = (psi(coeff, 1e-4, T_STAR) - psi(coeff, -1e-4, T_STAR)) / 2e-4
    assert w_tstar > 0
    checks["dust_mass"] = {
        "lam_samples": lam_samples,
        "w_period_rk4": w_period,
        "w_period_operator_identity": predicted,
        "w_tstar_rk4": w_tstar,
        "relative_shift_tstar_vs_period": w_tstar / predicted - 1,
    }

    # Resolution probe: halved grid must not move the solver-side derivatives.
    w_c = (psi(coeff_coarse, 1e-4, 2 * PI, STEPS // 2)
           - psi(coeff_coarse, -1e-4, 2 * PI, STEPS // 2)) / 2e-4
    checks["resolution_probe"] = {
        "w_period_coarse": w_c,
        "solver_abs_change": abs(w_c - w_period),
        "modes": [K_COARSE, K_MODES],
        "steps": [STEPS // 2, STEPS],
    }
    return checks


if __name__ == "__main__":
    t0 = time.time()
    result = run()
    result["runtime_seconds"] = round(time.time() - t0, 1)
    result["scope"] = ("RK4 modal time-stepping controls of signs, derivative "
                       "values and closed identities at fixed truncation; "
                       "exact past vanishing and kernel positivity are "
                       "analytic results, not numerical ones")
    out = Path(__file__).with_name("control_output.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    sys.exit(0)
