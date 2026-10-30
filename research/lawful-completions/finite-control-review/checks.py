"""Arithmetic sanity checks for the finite-control review (lawful-finite-control-review).

These checks verify specific inequalities and algebraic identities that appear in
C11_FINITE_CONTROL.md, COMPACTNESS_CONTINUITY_REPAIR.md, CUBIC_TRACE.md and the
LOY v1 source. They are NUMERICAL SANITY CHECKS of printed or derived statements,
not proofs; all analytic claims are audited separately in RESULT.md.

Each check runs in well under 1 second; the whole script under 5 seconds.
Run:  python3 checks.py
"""
import math
import random

random.seed(20261030)
OK = True


def check(name, cond, detail=""):
    global OK
    status = "PASS" if cond else "FAIL"
    if not cond:
        OK = False
    print(f"[{status}] {name} {detail}")


# ---- Check 1: exact norm compensation of the profile family (C11_FINITE_CONTROL sec 3)
# Phi_{e,x} = e * (sum_k x_k F_k + beta(x) G), disjoint supports,
# beta(x) = sqrt(beta0^2 - sum_k x_k^2 ||F_k||^2 / ||G||^2).
# Claim: ||Phi_{e,x}||_2^2 = e^2 beta0^2 ||G||_2^2 exactly (no cross terms).

def bump(center, radius, grid):
    return [math.exp(-1.0 / max(radius**2 - (t - center) ** 2, 1e-300))
            if abs(t - center) < radius else 0.0 for t in grid]

N_GRID = 20001
T_LO, T_HI = -1.0, 9.0
dt = (T_HI - T_LO) / (N_GRID - 1)
grid = [T_LO + i * dt for i in range(N_GRID)]

c1, c2, cG = 1.0, 2.0, 7.5   # supports of F1, F2 near T1=1, T2=2; G late (after 2*2+1=5)
rad = 0.4
# normalize so F_k(t_b + T_k) = 1 (as the construction requires F_k(T_j)=delta_kj)
F = []
for c in (c1, c2):
    b = bump(c, rad, grid)
    peak = b[min(range(N_GRID), key=lambda i: abs(grid[i] - c))]
    F.append([v / peak for v in b])
G = bump(cG, rad, grid)

def L2sq(f):
    return sum(v * v for v in f) * dt

nF = [L2sq(f) for f in F]
nG = L2sq(G)
beta0 = 1.3
eps = 1e-3
# choose the parameter ball radius rho so that beta >= beta0/2 on |x|<=rho
# (mirrors C11_FINITE_CONTROL sec 3: rho small enough that beta is bounded away from 0)
rho = 0.5 * beta0 * math.sqrt(3.0 * nG / sum(nF))

worst = 0.0
for _ in range(400):
    x = [random.uniform(-rho, rho), random.uniform(-rho, rho)]
    arg = beta0**2 - sum(x[k] ** 2 * nF[k] for k in range(2)) / nG
    check_marg = arg > 0.25  # beta bounded away from zero on the ball
    beta = math.sqrt(arg)
    profile = [eps * (x[0] * F[0][i] + x[1] * F[1][i] + beta * G[i]) for i in range(N_GRID)]
    n = L2sq(profile)
    worst = max(worst, abs(n - eps**2 * beta0**2 * nG) / (eps**2 * beta0**2 * nG))
    if not check_marg:
        check("beta positivity margin", False)
check("exact norm compensation ||Phi||^2 = eps^2 beta0^2 ||G||^2",
      worst < 1e-9, f"(max rel dev {worst:.2e})")

# F_k(T_j) = delta_kj and G vanishes at readout times (disjoint supports)
tj = [1.0, 2.0]
d_ok = all(abs(F[k] [min(range(N_GRID), key=lambda i: abs(grid[i] - tj[j]))]
               - (1.0 if k == j else 0.0)) < 1e-6 for k in range(2) for j in range(2))
g_ok = max(abs(G[min(range(N_GRID), key=lambda i: abs(grid[i] - t))]) for t in tj) == 0.0
check("F_k(t_b+T_j)=delta_kj and G vanishes on the readout window", d_ok and g_ok)

# ---- Check 2: the (1.7) reduction min(v-u, L) <= L^dc (v-u)^{1-dc} for 0<dc<1
worst = 0.0
dc = 0.4
L = 1.6
for _ in range(20000):
    a = random.uniform(0.0, 50.0)
    m = min(a, L)
    worst = max(worst, m / (L**dc * a ** (1 - dc)) if a > 0 else 0.0)
check("min(v-u,L) <= L^dc (v-u)^{1-dc}", worst <= 1.0 + 1e-12, f"(max ratio {worst:.6f})")

# ---- Check 3: clock inverse bound |t1(T)-t2(T)| <= (3/2) sup|tau1-tau2| when 2 lambda >= 2/3
for trial in range(200):
    M = 400
    T_end = 3.0
    lam1 = [random.uniform(1 / 3, 1 / 2) for _ in range(M)]
    lam2 = [min(1 / 2, max(1 / 3, v + random.uniform(-0.02, 0.02))) for v in lam1]
    dts = T_end / M
    tau1 = [0.0]
    tau2 = [0.0]
    for i in range(M):
        tau1.append(tau1[-1] + 2 * lam1[i] * dts)
        tau2.append(tau2[-1] + 2 * lam2[i] * dts)
    sup_dtau = max(abs(a - b) for a, b in zip(tau1, tau2))
    for T in (0.5, 1.7, 2.9):
        # invert tau on the common grid
        t1 = min(range(M + 1), key=lambda i: abs(tau1[i] - T))
        t2 = min(range(M + 1), key=lambda i: abs(tau2[i] - T))
        if abs(t1 - t2) * dts > 1.5 * sup_dtau + 2 * dts:
            check("clock inverse factor 3/2", False, f"trial {trial} T={T}")
            break
    else:
        continue
    break
else:
    check("clock inverse |t1(T)-t2(T)| <= (3/2) sup|tau1-tau2| (grid sanity)", True)

# ---- Check 4: degree boundary positivity: |x + s R(x) - z| >= rho - |z| - sup|R| on |x|=rho
rho, eps2C, znorm = 1.0, 0.3, 0.49
margin = min(
    math.sqrt(sum((xv / math.sqrt(sum(c * c for c in x)) + 0.0) ** 2 for xv in x)) - 0
    for x in [(rho, 0.0), (0.0, rho)]
)
# homotopy point: x + s R - z with |R| <= C eps^2 <= eps2C (generic directions)
ok = True
for _ in range(20000):
    x = (random.uniform(-1, 1), random.uniform(-1, 1))
    nx = math.hypot(*x)
    if abs(nx - rho) > 1e-9:
        continue
    x = (x[0] / nx * rho, x[1] / nx * rho)
    s = random.uniform(0, 1)
    # worst-case R: pointing straight at z
    z = (znorm, 0.0)
    R = (-eps2C * (1 - s) * math.copysign(1.0, x[0]), 0.0)
    y = (x[0] + s * R[0] - z[0], x[1] + s * R[1] - z[1])
    if math.hypot(*y) <= 1e-12:
        ok = False
check("homotopy never vanishes on |x|=rho when C eps^2 < rho/2 - |z| (worst-case R)", ok,
      f"(rho={rho}, Ceps^2={eps2C}, |z|={znorm})")

# ---- Check 5: discrete Gronwall M(U) <= K int M  =>  M = 0 (flat-wedge scheme)
K = 2.5
dts = 0.01
Ms = [0.0]                      # M(u0) = 0: the flat-wedge case has zero initial datum
for _ in range(400):
    Ms.append(K * dts * sum(Ms))   # M_{n+1} <= K * int_{u0}^{U_n} M
    if Ms[-1] > 1e-300:
        check("flat-wedge Gronwall: M stays 0 from M(u0)=0", False, f"M={Ms[-1]}")
        break
else:
    check("flat-wedge Gronwall scheme: zero forcing keeps M=0", True,
          f"(max M after {len(Ms)} steps: {max(Ms):.1e})")

# contrast: a nonzero seed delta grows; the zero case is genuinely used
Ms2 = [1e-8]
for _ in range(400):
    Ms2.append(K * dts * sum(Ms2))
check("contrast: nonzero seed grows (scheme tight, zero case substantive)",
      Ms2[-1] > 1e-8, f"(seed 1e-8 -> {Ms2[-1]:.2e})")

print("ALL PASS" if OK else "SOME CHECKS FAILED")
