"""Reproduction check for the two-point decay claim in RESULT.md.

Free massive scalar, 4d Minkowski vacuum, proper spacelike separation s (units m^-1):
    W(s) = m K1(m s) / (4 pi^2 s),   K1(z) = int_0^inf exp(-z cosh t) dt.
Asymptotically W(s) ~ sqrt(pi m / 2)/(4 pi^2) * e^{-m s} * s^{-3/2}.
Standard library only. Run: python3 check_twopoint_decay.py
"""
import math

def K1(z: float) -> float:
    tmax = math.acosh(1 + 80.0 / z)
    n = 40000
    h = tmax / n
    s = 0.5 * (math.exp(-z) + math.exp(-z * math.cosh(tmax)))
    for i in range(1, n):
        s += math.exp(-z * math.cosh(i * h))
    return s * h

def W(s: float, m: float = 1.0) -> float:
    return m * K1(m * s) / (4 * math.pi ** 2 * s)

ASYMP = math.sqrt(math.pi / 2) / (4 * math.pi ** 2)  # limit of W(s)*e^s*s^{3/2}

def thickness(eps: float) -> float:
    ref = W(1.0)
    lo, hi = 1.0, 60.0
    while W(hi) > eps * ref:
        hi *= 2
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if W(mid) > eps * ref else (lo, mid)
    return 0.5 * (lo + hi)

if __name__ == "__main__":
    print(f"asymptotic constant sqrt(pi/2)/(4 pi^2) = {ASYMP:.6f}")
    for s in (3.0, 5.0, 8.0, 12.0):
        print(f"  s={s:5.1f}  W(s) e^s s^(3/2) = {W(s) * math.exp(s) * s ** 1.5:.6f}")
    for eps in (1e-2, 1e-3, 1e-6):
        print(f"  eps={eps:g}: W(s) < eps*W(1) at s = {thickness(eps):.2f} m^-1"
              f"   (log(1/eps) = {math.log(1 / eps):.2f})")
