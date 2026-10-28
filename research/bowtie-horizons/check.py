"""Numerical checks for research/bowtie-horizons/RESULT.md. Standard library only.

1. Flat LambdaCDM (H0=67.4, Om=0.315, OL=1-Om; radiation neglected):
   remaining conformal time eta_rem(t) = int_t^inf c dt'/a(t') in comoving Gly.
2. de Sitter (P1R) failure example in flat-slicing conformal coordinates.
3. Thin-shell Vaidya: advanced time V_b at which the outgoing radial null ray
   from a centre point b (v_b < v1) reaches r=0, closed form vs. integration.
"""
import math

# ---------- 1. LambdaCDM ----------
H0 = 67.4                      # km/s/Mpc, Planck 2018 VI abstract (arXiv:1807.06209v4)
Om = 0.315
OL = 1.0 - Om
c = 299792.458                 # km/s
MPC_GLY = 3.26156e-3           # 1 Mpc in Gly
hubble_dist_gly = c / H0 * MPC_GLY          # c/H0 in Gly
hubble_time_gyr = 977.792 / H0              # 1/H0 in Gyr

def E(a):
    return math.sqrt(Om / a**3 + OL)

def simpson(f, lo, hi, n=20000):
    if n % 2: n += 1
    h = (hi - lo) / n
    s = f(lo) + f(hi)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(lo + i * h)
    return s * h / 3

def eta_rem(a):
    """comoving remaining conformal distance from scale factor a to a=inf, in Gly.
    int_a^inf da'/(a'^2 E(a')) ; substitute u = 1/a' -> int_0^{1/a} du / E(1/u)."""
    return hubble_dist_gly * simpson(lambda u: 1.0 / math.sqrt(Om * u**3 + OL), 0.0, 1.0 / a)

def eta_past(a):
    """comoving particle-horizon distance from a=0 to a (radiation neglected), Gly."""
    return hubble_dist_gly * simpson(lambda x: 1.0 / (x * x * E(x)) if x > 0 else 0.0, 1e-8, a)

def age(a):
    return hubble_time_gyr * simpson(lambda x: 1.0 / (x * E(x)) if x > 0 else 0.0, 1e-10, a)

def a_at_age(t):
    lo, hi = 1e-6, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if age(mid) < t: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

t0 = age(1.0)
er0 = eta_rem(1.0)
print("== LambdaCDM (flat, H0=%.1f, Om=%.3f, radiation neglected)" % (H0, Om))
print("age t0 = %.2f Gyr" % t0)
print("comoving event horizon eta_rem(t0) = %.2f Gly" % er0)
print("comoving particle horizon (no radiation) = %.2f Gly" % eta_past(1.0))
print("points on our t0 slice lack a common future with here-now iff d >= 2*eta_rem = %.2f Gly" % (2 * er0))
for tau in (0.1, 1.0, 5.0):
    a = a_at_age(t0 + tau)
    er = eta_rem(a)
    print("after tau=%.1f Gyr on our comoving worldline: eta_rem=%.2f Gly; "
          "t0-slice points with %.2f <= d < %.2f Gly drop out of D_pot" % (tau, er, er0 + er, 2 * er0))

# ---------- 2. de Sitter P1R failure ----------
# flat slicing, conformal time eta<0, comoving coords; causal relations = Minkowski on eta<0.
def J_rel(p, q):  # q in J^+(p)?
    return q[0] - p[0] >= abs(q[1] - p[1])
def elsewhere(p, q):
    return not J_rel(p, q) and not J_rel(q, p)
def common_future(p, q):
    d = abs(p[1] - q[1])
    return d < -(p[0] + q[0])   # apex of the two cones lies at eta<0
s, s2, x = (-2.0, 0.0), (-1.0, 0.0), (-1.0, 2.5)
print("\n== de Sitter (H=1, conformal coords)")
print("s prec s'? ", J_rel(s, s2) and s != s2)
print("x elsewhere of s:", elsewhere(s, x), " common future with s:", common_future(s, x))
print("x elsewhere of s':", elsewhere(s2, x), " common future with s':", common_future(s2, x))

# brute-force confirm common-future verdicts on a grid of candidate z (eta<0)
def brute(p, q, n=600):
    for i in range(1, n):
        eta = -3.0 * i / n * 0 + (-1e-9 - 3.0 * (1 - i / n))
        for j in range(-n, n + 1):
            z = (eta, 6.0 * j / n)
            if J_rel(p, z) and J_rel(q, z):
                return True
    return False
print("brute force: CF(s,x)=%s CF(s',x)=%s" % (brute(s, x), brute(s2, x)))

# ---------- 3. thin-shell Vaidya ----------
M, v1 = 1.0, 0.0
def V_closed(vb):
    r0 = (v1 - vb) / 2.0
    assert 0 < r0 < 2 * M
    return v1 - 2 * r0 + 4 * M * math.log(2 * M / (2 * M - r0))
def V_numeric(vb, h=1e-6):
    r, v = (v1 - vb) / 2.0, v1          # flat interior: r=(v-vb)/2 up to shell
    while r > 0:
        r += h * 0.5 * (1 - 2 * M / r)  # dr/dv=(1-2M/r)/2 in Schwarzschild region
        v += h
    return v
print("\n== Vaidya thin shell M=1 at v1=0")
for vb in (-3.9, -2.0, -0.5):
    print("v_b=%.2f  V_b closed=%.6f numeric=%.6f  (V_b - v1 = %.4f > 0)" %
          (vb, V_closed(vb), V_numeric(vb), V_closed(vb) - v1))
# P1R failure: s on axis at v_s=-2 (V_s>v1); s' on axis at v_s'=-0.01 with V_s' < v_x < V_s
vs, vs2 = -2.0, -0.01
Vs, Vs2 = V_closed(vs), V_closed(vs2)
vx = 0.5 * (Vs2 + Vs)
print("V_s=%.4f  V_s'=%.6f  choose v_x=%.4f in (V_s', V_s)" % (Vs, Vs2, vx))

# ---------- 4. historical closure H in a flat FLRW conformal slab ----------
# Conformal slab eta_bb < eta < eta_inf (1+1 suffices: the optimal r lies on
# the line through x and s). Claim: x in E(s) lies in H(s)=U_{r<=s} D(r) iff
# d < R_x + R_s + 2 P_s, with R = eta_inf - eta, P = eta - eta_bb.
import random
def in_H_brute(s, x, eb, ei, n=160):
    # search r in J^-(s) inside the slab with x not in J^+(r) and common future
    for i in range(1, n):
        er = eb + (s[0] - eb) * i / n
        lam = s[0] - er
        for j in range(-n, n + 1):
            xr = s[1] + lam * j / n
            r = (er, xr)
            if J_rel(r, x):
                continue
            if abs(x[1] - xr) < (ei - x[0]) + (ei - er):
                return True
    return False
def in_H_formula(s, x, eb, ei):
    d = abs(x[1] - s[1])
    return d < (ei - x[0]) + (ei - s[0]) + 2 * (s[0] - eb)
random.seed(1)
eb, ei = -3.0, 1.0
agree = tested = 0
for _ in range(400):
    s = (random.uniform(eb + 0.05, ei - 0.05), 0.0)
    x = (random.uniform(eb + 0.05, ei - 0.05), random.uniform(-14, 14))
    if not elsewhere(s, x):
        continue
    d = abs(x[1]); thr = (ei - x[0]) + (ei - s[0]) + 2 * (s[0] - eb)
    if abs(d - thr) < 0.15:          # skip grid-resolution boundary band
        continue
    tested += 1
    agree += in_H_brute(s, x, eb, ei) == in_H_formula(s, x, eb, ei)
print("\n== FLRW slab historical closure: formula vs brute force agree on %d/%d" % (agree, tested))
print("LambdaCDM same-slice H threshold 2(P0+R0) = %.1f Gly (radiation neglected: overestimate)"
      % (2 * (eta_past(1.0) + er0)))
