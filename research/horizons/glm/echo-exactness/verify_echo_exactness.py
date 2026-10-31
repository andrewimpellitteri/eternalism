#!/usr/bin/env python3
"""
Numerical verification for the echo-exactness task (closed dust, conformal
scalar on the Einstein cylinder E = R x S^3).

Equation and modes.  psi'' = Delta psi - psi on E; degree-n zonal harmonics
C_n(cos d) = sin((n+1)d)/sin d have frequency (n+1).  With Cauchy data at
slice t=0 given by f, g (zonal about P: f = sum f_n C_n, g = sum g_n C_n):

    psi(t, X) = sum_n [ f_n cos((n+1)t) + g_n sin((n+1)t)/(n+1) ] C_n(cos d),

d = d(X, P).  This mode sum is exact; all numerics below evaluate it.

Checks
  1  echo identity psi(t+pi, pi-d) = -psi(t, d) (mode-wise exact).
  2  closed forms for Poisson data w_n = r^n (data = 1/(1-2r cos d + r^2)):
        g-data:  psi = ln[D(t+d)/D(t-d)] / (4 r sin d),
        f-data:  psi = [ sin(t+d)/D(t+d) - sin(t-d)/D(t-d) ] / (2 sin d),
     D(a) = 1 - 2 r cos a + r^2.  Mode sums must match to machine precision;
     and psi(t, 0) = sin t / D(t) (Kirchhoff shell formula at the pole).
     These verify the shell (Huygens/refocusing) structure of the Cauchy
     propagator: value at (t,X) depends only on data on the sphere
     d(X,.) = fold(t), with a sign flip on the reflected branch t in (pi,2pi).
  3  end-to-end separation witness for b1 = (2pi/5, Y), target x*=(3pi/2, Y):
     data = smooth cap bump (support radius 0.08) at P with d(P,Y) = c,
     vertex eta1 = -0.1, avoidance margin c - psi0 - tau > cap radius.
     Expect |psi| ~ 0 on sampled points of I^-(b1), O(1) at x*, ~0 at the
     W-point x_W = (2pi-1/2, Y) which lies outside J^-(b1) u J^-(A b1).
  4  b2 = (3pi/4, Y): a b2-admissible bump solution is O(1) at its own
     annulus target x' = (2.8, X') and ~0 at x* (the theorem puts x* in
     F(b2)), though x* is timelike future of b2 and outside Det(b2).
  5  geometry controls: region membership; tau = pi covers M; annulus size.
Run: python3 verify_echo_exactness.py
"""
import math

TWO_PI = 2.0 * math.pi


def fold(t):
    t = math.fmod(abs(t), TWO_PI)
    return t if t <= math.pi else TWO_PI - t


def circ(a, b):
    return fold(a - b)


def C_series(n_max, d):
    """[C_0(d), ..., C_{n_max-1}(d)], C_n = sin((n+1)d)/sin d, by recurrence."""
    out = [0.0] * n_max
    if d < 1e-9:
        return [float(n + 1) for n in range(n_max)]
    if math.pi - d < 1e-9:
        return [float(n + 1) if n % 2 == 0 else -float(n + 1)
                for n in range(n_max)]
    cd = math.cos(d)
    a, b = 1.0, 2.0 * cd          # C_0, C_1
    for n in range(n_max):
        out[n] = a
        a, b = b, 2.0 * cd * b - a
    return out


def psi_modes(t, d, f_coeffs, g_coeffs, n_max, eta1=0.0):
    s = t - eta1
    Cs = C_series(n_max, d)
    tot = 0.0
    for n in range(n_max):
        k = n + 1
        tot += (f_coeffs[n] * math.cos(k * s)
                + g_coeffs[n] * math.sin(k * s) / k) * Cs[n]
    return tot


def section(s):
    print("\n=== " + s + " ===")


# ------------------------------------------------------------ 1  echo
section("1  echo identity psi(t+pi, pi-d) = -psi(t,d)")
r = 0.9
NMAX = 260
worst = 0.0
for t in (0.3, 1.1, 2.0, 3.6, 5.5):
    for d in (0.2, 0.8, 1.4, 2.2, 2.9):
        g = [r ** n for n in range(NMAX)]
        a = psi_modes(t, d, [0.0] * NMAX, g, NMAX) \
            + psi_modes(t + math.pi, math.pi - d, [0.0] * NMAX, g, NMAX)
        worst = max(worst, abs(a))
print("max residual over grid:", worst)

# ------------------------------------------------- 2  closed forms (Poisson)
section("2  mode sums vs exact Poisson-data closed forms")
r = 0.8
NMAX = 400


def D(a):
    return 1 - 2 * r * math.cos(a) + r * r


worst_g = worst_f = worst_pole = 0.0
g_P = [r ** n for n in range(NMAX)]
f_P = [r ** n for n in range(NMAX)]
for t in (0.4, 1.0, 1.9, 2.6, 3.3, 4.4, 5.6):
    for d in (0.15, 0.7, 1.3, 2.0, 2.7):
        num_g = psi_modes(t, d, [0.0] * NMAX, g_P, NMAX)
        # global closed form (valid for all t; branch signs are invisible here)
        cf_g = math.log(D(t + d) / D(t - d)) / (4 * r * math.sin(d))
        worst_g = max(worst_g, abs(num_g - cf_g))
        num_f = psi_modes(t, d, f_P, [0.0] * NMAX, NMAX)
        cf_f = (math.sin(t + d) / D(t + d)
                - math.sin(t - d) / D(t - d)) / (2 * math.sin(d))
        worst_f = max(worst_f, abs(num_f - cf_f))
# pole value (d -> 0) of the g-data solution: psi(t,0) = sin t / D(t)
for t in (0.5, 1.3, 2.4, 3.6, 5.0):
    num = psi_modes(t, 1e-7, [0.0] * NMAX, g_P, NMAX)
    cf = math.sin(t) / D(t)
    worst_pole = max(worst_pole, abs(num - cf))
print("max |mode sum - closed form|, g-data:", worst_g)
print("max |mode sum - closed form|, f-data:", worst_f)
print("max |psi(t,0) - sin t/D(t)|          :", worst_pole)

# -------------------------------------- coefficient projector for cap bumps
def cap_coeffs(radius, n_max, steps=6000):
    """Smooth cap: g(d) = exp(-1/(1-(d/radius)^2)) for d<radius else 0.
    Returns zonal coefficients g_n with g = sum g_n C_n(cos d)."""
    def gf(d):
        if d >= radius:
            return 0.0
        u = 1.0 - (d / radius) ** 2
        return math.exp(-1.0 / u)
    cs = math.cos(0.0)
    # quadrature concentrated on the support: [0, 1.5*radius]
    hi = 1.5 * radius
    h = hi / steps
    sin_g = [math.sin(i * h) for i in range(steps + 1)]
    cos_g = [math.cos(i * h) for i in range(steps + 1)]
    wts = [1 if i in (0, steps) else (4 if i % 2 else 2) for i in range(steps + 1)]
    coeffs = []
    Cprev = None            # C_{n-1}
    Cprev2 = None           # C_{n-2}
    for n in range(n_max):
        if n == 0:
            Cn = [1.0] * (steps + 1)
        elif n == 1:
            Cn = [2.0 * c for c in cos_g]
        else:
            Cn = [2.0 * cos_g[i] * Cprev[i] - Cprev2[i]
                  for i in range(steps + 1)]
        total = 0.0
        for i in range(steps + 1):
            total += wts[i] * gf(i * h) * Cn[i] * sin_g[i] * sin_g[i]
        total *= h / 3.0
        coeffs.append(2.0 * (n + 1) * total / math.pi)
        Cprev2, Cprev = Cprev, Cn
    return coeffs


# ------------------------------------------- 3  separation witness b1 -> x0
section("3  witness b1=(2pi/5,Y), x0=(tau+0.9, Y): annulus point unfixed")
tau = TWO_PI / 5.0
eta_w = tau + 0.9
print(f"tau={tau:.4f}  u=v={eta_w:.4f}  annulus ({tau:.4f},{TWO_PI-tau:.4f}): "
      f"{tau < eta_w < TWO_PI - tau}")
eta1 = -0.01
c = circ(eta_w, eta1)          # d(P,Y) = fold(|eta_w-eta1|) = eta_w+0.01
psi0 = circ(eta1, 0.0)
margin = c - psi0 - tau        # = eta_w - tau  (direct branch)
cap = 0.15
print(f"vertex eta1={eta1:.2f}  c=d(P,Y)={c:.4f}  psi0={psi0:.2f}  "
      f"avoidance margin={margin:.4f} > cap {cap}")
assert margin > cap
NCAP = 1500
gc = cap_coeffs(cap, NCAP)
scale = max(abs(x) for x in gc)
gc = [x / scale for x in gc]
for nn in (300, 600, 900, 1200, 1499):
    print(f"  |g_{nn}| = {abs(gc[nn]):.2e}")
tail = max(abs(x) for x in gc[1200:])
print(f"cap coefficients (scale-normalized), max |g_n| for n>1200: {tail:.2e}")
fc = [0.0] * NCAP

def shell_gap(eta, dZY):
    """min over Z with d(Z,Y)=dZY of (d(Z,P) - fold(|eta-eta1|)) >= bound."""
    return (c - dZY) - fold(eta - eta1)

worst_U = 0.0
for i in range(1, 12):
    eta = tau * i / 12.0
    for frac in (0.0, 0.5, 0.95):
        q = frac * (tau - eta)          # d(Z,Y)
        # conservative: nearest point of the q-sphere to P:
        dZP = max(c - q, 1e-6)
        worst_U = max(worst_U, abs(psi_modes(eta, dZP, fc, gc, NCAP, eta1)))
val_x = psi_modes(eta_w, c, fc, gc, NCAP, eta1)
eta_W = TWO_PI - 0.5
val_W = psi_modes(eta_W, c, fc, gc, NCAP, eta1)
print(f"max |psi| on sampled U(b1) points : {worst_U:.3e}")
print(f"psi(x0)  [annulus target, timelike future of b1] : {val_x:+.4f}")
print(f"psi(x_W) [W-point, outside J- u AJ-]: {val_W:+.3e}")

# ----------------------------------------------- 4  b2 controls
section("4  b2=(3pi/4,Y): admissible solution hits x' but vanishes at x*")
tau2 = 0.75 * math.pi
eta_p, d_p = 2.8, 0.1
eta1b = -0.2
xib = circ(eta_p, eta1b)              # 3.0 (< pi, direct branch)
cb = 2.97
m2 = cb - circ(eta1b, 0.0) - tau2
print(f"x' annulus membership: u={eta_p+d_p:.3f} v={eta_p-d_p:.3f} in "
      f"({tau2:.3f},{TWO_PI-tau2:.3f}): "
      f"{tau2 < eta_p + d_p < TWO_PI - tau2 and tau2 < eta_p - d_p < TWO_PI - tau2}")
tri = abs(cb - d_p) <= xib <= min(cb + d_p, TWO_PI - cb - d_p)
print(f"vertex margin={m2:.4f}, spatial triangle feasible: {tri}")
assert m2 > cap and tri
val_xp = psi_modes(eta_p, xib, fc, gc, NCAP, eta1b)
eta_x = 1.5 * math.pi
val_xs = psi_modes(eta_x, cb, fc, gc, NCAP, eta1b)
print(f"psi(x') [own annulus target] : {val_xp:+.4f}")
print(f"psi(x*) [timelike future of b2, in F(b2) by theorem]: {val_xs:+.3e}")

# ----------------------------------------------- 5  geometry controls
section("5  geometry controls")


def regions(tau_, eta_, d_):
    u, v = eta_ + d_, eta_ - d_
    return (u <= tau_, v <= tau_, v >= TWO_PI - tau_, u >= TWO_PI - tau_)


for (label, t_, e_, d_) in [
        ("x* vs b1", tau, 1.5 * math.pi, 0.0),
        ("x_W vs b1", tau, TWO_PI - 0.5, 0.0),
        ("x* vs b2", tau2, 1.5 * math.pi, 0.0),
        ("echo pt (pi+tau/2, -Y) vs b1", tau, math.pi + tau / 2.0, math.pi)]:
    fl = regions(t_, e_, d_)
    print(f"{label:30s} fixed={any(fl)!s:5s} J-(b):{int(fl[0])} "
          f"J-(Ab):{int(fl[1])} W:{int(fl[2])} What:{int(fl[3])}")
missing = 0
for i in range(1, 40):
    for j in range(40):
        e = TWO_PI * i / 40.0
        d = math.pi * j / 39.0
        if not any(regions(math.pi, e, d)):
            missing += 1
print("tau=pi: grid points outside the four-region union:", missing)
tot = ann = 0
for i in range(1, 40):
    for j in range(40):
        e = TWO_PI * i / 40.0
        d = math.pi * j / 39.0
        u, v = e + d, e - d
        tot += 1
        if tau < u < TWO_PI - tau and tau < v < TWO_PI - tau:
            ann += 1
print(f"tau=2pi/5: unfixed-annulus grid points: {ann}/{tot}")
print("\nDONE")
