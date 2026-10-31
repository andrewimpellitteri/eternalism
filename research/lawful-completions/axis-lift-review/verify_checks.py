#!/usr/bin/env python3
"""Independent finite-difference checks for the AXIS_C11_RECONSTRUCTION review.

Pure standard library. Runtime ~1-2 s (budget: 10 s per check, 15 s hard cap,
30 s total). These checks support analytic statements proved by hand in
RESULT.md; they do not replace any analytic proof.
"""
import math, random, time

t0 = time.time()
random.seed(20261029)
PASS, FAIL = [], []

def check(name, ok, detail=""):
    (PASS if ok else FAIL).append((name, detail))

# ------------------------------------------------ model quotient data on (t,rho)
# r = rho*B(t,rho), B(t,0)=1 (a=1; C^2 with bounded 3rd weak derivatives);
# m = rho^3*c(t,rho) so m = O(r^3) with r ~ rho; lambda~1, nu~-1 stand-ins.
def B_(t, r): return 1.0 + 0.3*r + 0.2*r*r*math.sin(t) + 0.1*r*r*r*math.cos(t)
def R_(t, r): return r * B_(t, r)
def M_(t, r): return r**3 * (1.0 + 0.5*r*math.sin(t) + 0.25*r*r)
def MU(t, r): return 2.0*M_(t, r)/R_(t, r) if r > 1e-12 else 0.0

def d1t(f, t, r, h=1e-5): return (f(t+h, r) - f(t-h, r))/(2*h)
def d1r(f, t, r, h=1e-5): return (f(t, r+h) - f(t, r-h))/(2*h)
def d2tt(f, t, r, h=1e-4): return (f(t+h, r) - 2*f(t, r) + f(t-h, r))/(h*h)
def d2rr(f, t, r, h=1e-4): return (f(t, r+h) - 2*f(t, r) + f(t, r-h))/(h*h)
def d2rt(f, t, r, h=1e-4): return (d1r(f, t+h, r, h) - d1r(f, t-h, r, h))/(2*h)

def DV(f, t, r, which):  return d1t(f, t, r) if which == 't' else d1r(f, t, r)
def D2(f, t, r, a, b):
    if a == b == 't': return d2tt(f, t, r)
    if a == b == 'r': return d2rr(f, t, r)
    return d2rt(f, t, r)

# ---- Check A: parity algebra  X_rhorho = X_tt - 4 X_uv  on the model r ----
def Xuv(u, v): return R_((u+v)/2.0, (v-u)/2.0)
h = 1e-4
u0, v0 = 0.3, 0.9
Xuu = (Xuv(u0+h, v0) - 2*Xuv(u0, v0) + Xuv(u0-h, v0))/(h*h)
Xvv = (Xuv(u0, v0+h) - 2*Xuv(u0, v0) + Xuv(u0, v0-h))/(h*h)
Xuvd = (Xuv(u0+h, v0+h) - Xuv(u0+h, v0-h) - Xuv(u0-h, v0+h) + Xuv(u0-h, v0-h))/(4*h*h)
lhs = Xuu - 2*Xuvd + Xvv            # = X_rhorho
rhs = d2tt(R_, (u0+v0)/2.0, (v0-u0)/2.0, h) - 4*Xuvd
check("A. X_rhorho = X_tt - 4 X_uv", abs(lhs - rhs) < 5e-4,
      f"lhs={lhs:.6f} rhs={rhs:.6f}")

# ---- Check B: exact mu_ab quotient formula vs finite differences ----
# mu_ab = 2 m_ab/r - 2(m_a r_b + m_b r_a + m r_ab)/r^2 + 4 m r_a r_b/r^3
t1, r1 = 0.4, 0.6
def qform_mu(t, r, a, b):
    rr, mm = R_(t, r), M_(t, r)
    return (2*D2(M_, t, r, a, b)/rr
            - 2*(DV(M_, t, r, a)*DV(R_, t, r, b)
                 + DV(M_, t, r, b)*DV(R_, t, r, a)
                 + mm*D2(R_, t, r, a, b))/(rr*rr)
            + 4*mm*DV(R_, t, r, a)*DV(R_, t, r, b)/(rr**3))
for name, a, b, fd in (("mu_rr", 'r', 'r', d2rr(MU, t1, r1)),
                       ("mu_tr", 't', 'r', d2rt(MU, t1, r1)),
                       ("mu_tt", 't', 't', d2tt(MU, t1, r1))):
    qv = qform_mu(t1, r1, a, b)
    check(f"B. {name} quotient formula", abs(qv - fd) < 5e-3,
          f"formula={qv:.6f} finitediff={fd:.6f}")

# ---- Check C: term budget of  m_a = (1-mu) r^2 phi_a^2 / (2 field)  ----
# Stand-in RHS with phi_a = 1, field = 1: O(r^2) itself; differentiated once O(r).
def Mv_rhs(t, r): return (1.0 - MU(t, r)) * R_(t, r)**2 / 2.0
ratio = max(abs(Mv_rhs(t1, 10**(-k)))/(10**(-2*k)) for k in (1, 2, 3, 4))
check("C. m_a = O(r^2) at axis", ratio < 5.0, f"sup |RHS|/r^2 = {ratio:.3f}")
ratio_t = max(abs(d1t(Mv_rhs, t1, 10**(-k)))/(10**(-k)) for k in (2, 3, 4))
check("C. m_ab = O(r) at axis", ratio_t < 40.0, f"sup |d_t RHS|/r = {ratio_t:.3f}")

# ---- Check D: E = D n_x n_y lift with D = rho^2 sin(log rho) + regular part ----
# D satisfies every stated input bound (|D|<=Crho^2, |D_rho|<=Crho, |D_rhorho|<=C,
# D_rho(t,0)=0) yet D/rho^2 has no axis limit.
def Df(t, x, y):
    rho = math.hypot(x, y)
    if rho < 1e-12: return 0.0
    return rho*rho*math.sin(math.log(rho)) + 0.2*rho*rho*(1.0 + 0.5*math.cos(t))
def E11(t, x, y):
    rho = math.hypot(x, y); nx = x/rho
    return Df(t, x, y)*nx*nx
def dE(t, x, y, k, hh=1e-5):
    dx = hh if k == 0 else 0.0
    dy = hh if k == 1 else 0.0
    return (E11(t, x+dx, y+dy) - E11(t, x-dx, y-dy))/(2*hh)

x1, y1 = 0.9, 0.4
rho1 = math.hypot(x1, y1); nx, ny = x1/rho1, y1/rho1
eps = 1e-6
Dr = (Df(t1, x1+eps*nx, y1+eps*ny) - Df(t1, x1-eps*nx, y1-eps*ny))/(2*eps)
ok_formula = True
for k in (0, 1):
    nk = (nx, ny)[k]
    # component i=j=x:  d_k E_xx = Dr nk nx nx + (D/rho)(delta_kx nx + delta_kx nx - 2 nx^2 nk)
    form = Dr*nk*nx*nx + (Df(t1, x1, y1)/rho1)*(2.0*(1.0 if k == 0 else 0.0)*nx
                                                - 2*nx*nx*nk)
    if abs(form - dE(t1, x1, y1, k)) > 5e-4: ok_formula = False
check("D. d_k E_xx closed formula", ok_formula, f"rho={rho1:.2f}")

ratio_g = max(math.hypot(dE(t1, 10**(-k)*nx, 10**(-k)*ny, 0),
                         dE(t1, 10**(-k)*nx, 10**(-k)*ny, 1))/(10**(-k))
              for k in (2, 3, 4))
check("D. |grad E| = O(rho) at axis (C^1 lift with gradient value 0)",
      ratio_g < 25.0, f"sup |gradE|/rho = {ratio_g:.3f}")

def gradE(t, x, y, hh=1e-4):
    return (dE(t, x, y, 0, hh), dE(t, x, y, 1, hh))
def hessE(t, x, y, a, b, hh=1e-3):
    da = (hh, 0.0) if a == 0 else (0.0, hh)
    db = (hh, 0.0) if b == 0 else (0.0, hh)
    gpp = gradE(t, x+da[0]+db[0], y+da[1]+db[1])
    gpm = gradE(t, x+da[0]-db[0], y+da[1]-db[1])
    gmp = gradE(t, x-da[0]+db[0], y-da[1]+db[1])
    gmm = gradE(t, x-da[0]-db[0], y-da[1]-db[1])
    return tuple((p-q-r+s)/(4*hh*hh)
                 for p, q, r, s in zip(gpp, gpm, gmp, gmm))
Hmax = max(abs(hessE(t1, x1, y1, a, b)[0]) for a in (0, 1) for b in (0, 1))
check("D. |Hess E_xx| <= C off axis", Hmax < 30.0, f"max = {Hmax:.3f}")

worst = 0.0
for _ in range(60):
    ang = random.uniform(0, 2*math.pi); rad = random.uniform(0.003, 0.05)
    xA, yA = rad*math.cos(ang), rad*math.sin(ang)
    s = random.uniform(0.2, 1.8)
    xB, yB = -s*xA, -s*yA          # segment crosses the axis
    dist = math.hypot(xA-xB, yA-yB)
    ga, gb = gradE(t1, xA, yA), gradE(t1, xB, yB)
    dg = math.hypot(ga[0]-gb[0], ga[1]-gb[1])
    worst = max(worst, dg/dist)
check("D. gradient Lipschitz across axis (segment-crossing pairs)", worst < 40.0,
      f"sup ratio = {worst:.2f}")

vals = []
for k in (1, 2, 3, 4):
    rad = 10**(-k)
    # adaptive outer step so the stencil actually sits at radius ~rad
    hh = rad/10.0
    g1 = gradE(t1, rad*nx + hh*nx, rad*ny + hh*ny, hh/10)
    g0 = gradE(t1, rad*nx - hh*nx, rad*ny - hh*ny, hh/10)
    vals.append((g1[0] - g0[0])/(2*hh))
check("D. Hess E has no axis limit (sharpness: C^{1,1} need not be C^2)",
      abs(vals[0] - vals[-1]) > 0.2,
      f"Hess_xx at rho=1e-1..1e-4: {vals[0]:.3f} {vals[1]:.3f} {vals[2]:.3f} {vals[3]:.3f} (non-convergent, bounded)")

# ---- Check E: Hadamard bound |(Dn-D)/rho| <= sup_s |d_rho (D_n - D)(t,s)| ----
def Dn(t, x, y): return Df(t, x, y) + 0.01*x*y*y   # perturbed model, Dn(t,0)=0
ok_had = True
for _ in range(50):
    ang = random.uniform(0, 2*math.pi); rad = random.uniform(0.01, 0.5)
    cv, sv = math.cos(ang), math.sin(ang)
    sup = 0.0
    for j in range(21):
        s = rad*j/20
        dd = 1e-5
        # central difference of (Dn - D) along the ray at radius s
        dp = (Dn(t1, (s+dd)*cv, (s+dd)*sv) - Df(t1, (s+dd)*cv, (s+dd)*sv))
        dm = (Dn(t1, (s-dd)*cv, (s-dd)*sv) - Df(t1, (s-dd)*cv, (s-dd)*sv))
        sup = max(sup, abs((dp - dm)/(2*dd)))
    quot = abs(Dn(t1, rad*cv, rad*sv) - Df(t1, rad*cv, rad*sv))/rad
    if quot > sup + 1e-9: ok_had = False
check("E. |(Dn-D)/rho| <= sup|d_rho(Dn-D)| (C^1 convergence criterion)", ok_had, "")

# ---- Check F: p_uv = r_uv phi needs the wave equation (flat quotient model) ----
# p_uv - r_uv phi = lambda phi_u + nu phi_v + r phi_uv; lambda=1/2, nu=-1/2.
# phi = rho:  phi_u = -1/2, phi_v = +1/2, phi_uv = 0  ->  sum = -1/2 != 0
val_rho = 0.5*(-0.5) + (-0.5)*(0.5)
check("F. phi=rho violates p_uv=r_uv phi (lifts to |x|, not C^1)",
      abs(val_rho) > 1e-12, f"p_uv - r_uv phi = {val_rho}")
# phi = f(t) (axis-even): phi_u = phi_v = f'/2 -> sum = 0
val_ft = 0.5*(1.0) + (-0.5)*(1.0)
check("F. axis-even phi=f(t) satisfies p_uv = r_uv phi on flat model",
      abs(val_ft) < 1e-12, f"p_uv - r_uv phi = {val_ft}")

elapsed = time.time() - t0
print(f"elapsed {elapsed:.2f}s  PASS={len(PASS)} FAIL={len(FAIL)}")
for name, d in PASS: print(f"  [ok] {name} :: {d}")
for name, d in FAIL: print(f"  [XX] {name} :: {d}")
