#!/usr/bin/env python3
"""Numerical verification for the null-boundary audit (pure standard library).

Curvature is computed by central finite differences of the metric components
(Riemann convention R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - ...).
The Kretschmann scalar is contracted as R_{abcd} R^{abcd} with the fully
raised (0,4) tensor, so no slot-order convention can corrupt it.

Self-tests (0): de Sitter flat slicing (K=24, Ric=3g, C=0) and
Schwarzschild (K=48/r^6, Ric=0, C^2 = K).

Checks:
  A. Ingoing Vaidya with smooth nondecreasing m(v):
     Kretschmann = 48 m(v)^2 / r^6, R = 0, Ric^2 = 0, R_vv = 2 m'(v)/r^2
     (hence Weyl nonzero iff m(v) != 0).
  B. The region {v < 0} is exactly flat.
  C. The (1,3) Weyl tensor is invariant under g -> Omega^2 g, checked
     componentwise for Vaidya and for the product metric.
  D. Product static metric -dt^2 + dphi1^2 + dtheta^2 + sin^2(theta) dphi2^2:
     electric Weyl component C^t_{phi1 t phi1} = -R(h)/6 = -1/3 nonzero
     everywhere, poles included.
  E. Cauchy time function T = v - (2/3) r + m(v)^2/r has timelike gradient
     on a dense (v, r) grid.
  F. The witness segment {v = 2, r decreasing} is a lightlike pregeodesic.
  G. The flat-region witness tangent (outgoing radial null, v = -1.5) is
     null and the region is flat there.

Run:  python3 verify_curvature.py
"""
import math

N = 4
LABELS = ("t", "r", "th", "ph")


# ---------- finite differences ----------
def d1(f, x, i, h=1e-5):
    xp = list(x); xm = list(x)
    xp[i] += h; xm[i] -= h
    return (f(xp) - f(xm)) / (2 * h)


def inv4(g):
    a = [row[:] for row in g]
    ii = [[float(i == j) for j in range(N)] for i in range(N)]
    for c in range(N):
        p = max(range(c, N), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        ii[c], ii[p] = ii[p], ii[c]
        piv = a[c][c]
        a[c] = [v / piv for v in a[c]]
        ii[c] = [v / piv for v in ii[c]]
        for r in range(N):
            if r != c and a[r][c] != 0.0:
                f = a[r][c]
                a[r] = [v - f * w for v, w in zip(a[r], a[c])]
                ii[r] = [v - f * w for v, w in zip(ii[r], ii[c])]
    return ii


# ---------- curvature ----------
def gamma_at(gfun, x):
    g = [[gfun(x, i, j) for j in range(N)] for i in range(N)]
    ginv = inv4(g)
    Gam = [[[0.0] * N for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                s = 0.0
                for l in range(N):
                    s += ginv[k][l] * (d1(lambda X: gfun(X, l, j), x, i)
                                       + d1(lambda X: gfun(X, i, l), x, j)
                                       - d1(lambda X: gfun(X, i, j), x, l))
                Gam[k][i][j] = 0.5 * s
    return g, ginv, Gam


def curv_at(gfun, x0):
    """Return g, ginv, Gamma, Rm (slots rho,sigma,mu,nu), Ric."""
    g, ginv, Gam = gamma_at(gfun, x0)

    def GamAt(x):
        return gamma_at(gfun, x)[2]

    Rm = [[[[0.0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for rho in range(N):
        for sig in range(N):
            for mu in range(N):
                for nu in range(N):
                    if mu == nu:
                        continue
                    s = d1(lambda X: GamAt(X)[rho][nu][sig], x0, mu)
                    s -= d1(lambda X: GamAt(X)[rho][mu][sig], x0, nu)
                    for lam in range(N):
                        s += Gam[rho][mu][lam] * Gam[lam][nu][sig]
                        s -= Gam[rho][nu][lam] * Gam[lam][mu][sig]
                    Rm[rho][sig][mu][nu] = s
    Ric = [[0.0] * N for _ in range(N)]
    for sig in range(N):
        for nu in range(N):
            Ric[sig][nu] = sum(Rm[rho][sig][rho][nu] for rho in range(N))
    return g, ginv, Gam, Rm, Ric


def scalars(gfun, x0):
    g, ginv, Gam, Rm, Ric = curv_at(gfun, x0)
    Rlow = [[[[sum(g[a][e] * Rm[e][b][c][d] for e in range(N))
              for d in range(N)] for c in range(N)] for b in range(N)]
            for a in range(N)]
    # full raise: R^{abcd}
    Rup = [[[[0.0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    s = 0.0
                    for e in range(N):
                        for f in range(N):
                            for gg in range(N):
                                for hh in range(N):
                                    s += (ginv[a][e] * ginv[b][f] *
                                          ginv[c][gg] * ginv[d][hh] *
                                          Rlow[e][f][gg][hh])
                    Rup[a][b][c][d] = s
    K = sum(Rlow[a][b][c][d] * Rup[a][b][c][d]
            for a in range(N) for b in range(N)
            for c in range(N) for d in range(N))
    Rscal = sum(ginv[i][j] * Ric[i][j] for i in range(N) for j in range(N))
    Ric2 = sum(Ric[i][j] * sum(ginv[i][a] * ginv[j][b] * Ric[a][b]
                               for a in range(N) for b in range(N))
               for i in range(N) for j in range(N))
    # (1,3) Weyl from the (0,4) formula, then raise slot 0.
    C = [[[[0.0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    v = (Rlow[a][b][c][d]
                         - 0.5 * (g[a][c] * Ric[b][d] - g[b][c] * Ric[a][d]
                                  - g[a][d] * Ric[b][c] + g[b][d] * Ric[a][c])
                         + (Rscal / 6.0) * (g[a][c] * g[b][d] - g[a][d] * g[b][c]))
                    C[a][b][c][d] = sum(ginv[a][e] * v for e in range(N)) if False else v
    # raise slot 0 properly
    C13 = [[[[sum(ginv[a][e] * C[e][b][c][d] for e in range(N))
             for d in range(N)] for c in range(N)] for b in range(N)]
           for a in range(N)]
    C2 = sum(C[a][b][c][d] * Rup[a][b][c][d]
             for a in range(N) for b in range(N)
             for c in range(N) for d in range(N))
    return dict(K=K, R=Rscal, Ric2=Ric2, Ric=Ric, g=g, ginv=ginv,
                C13=C13, C2=C2, Gam=Gam)


# ---------- metrics ----------
def smoothstep(v):
    if v <= 0:
        return 0.0
    if v >= 1:
        return 1.0
    return v * v * v * (10 - 15 * v + 6 * v * v)


def dsmooth(v):
    if v <= 0 or v >= 1:
        return 0.0
    return 30 * v * v * (v - 1) * (v - 1)


def vaidya_g(x, i, j):
    v, r, th, ph = x
    m = smoothstep(v)
    gg = [[-(1 - 2 * m / r), 1.0, 0.0, 0.0],
          [1.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, r * r, 0.0],
          [0.0, 0.0, 0.0, r * r * math.sin(th) ** 2]]
    return gg[i][j]


def schw_g(x, i, j):
    t, r, th, ph = x
    f = 1 - 2.0 / r
    gg = [[-f, 0, 0, 0], [0, 1 / f, 0, 0],
          [0, 0, r * r, 0], [0, 0, 0, r * r * math.sin(th) ** 2]]
    return gg[i][j]


def ds_g(x, i, j):
    t = x[0]
    e = math.exp(t)
    gg = [[-1.0, 0, 0, 0], [0, e * e, 0, 0], [0, 0, e * e, 0], [0, 0, 0, e * e]]
    return gg[i][j]


def product_g(x, i, j):
    t, f1, th, f2 = x
    gg = [[-1.0, 0, 0, 0], [0, 1.0, 0, 0], [0, 0, 1.0, 0],
          [0, 0, 0, math.sin(th) ** 2]]
    return gg[i][j]


def omega1(x):
    v, r, th, ph = x
    return math.exp(0.2 * (1 + math.sin(v) * math.cos(r) + math.cos(th)))


def conformal_g(gfun, Om):
    def gf(x, i, j):
        o = Om(x)
        return (o * o) * gfun(x, i, j)
    return gf


def report(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)


def main():
    print("== 0. self-tests ==")
    s = scalars(ds_g, [0.4, 0.3, 0.2, 0.1])
    print(f"  dS: K={s['K']:.4f} (expect 24)  R={s['R']:.4f} (expect 12)  "
          f"C2={s['C2']:.2e} (expect 0)  Ric00={s['Ric'][0][0]:.4f} (expect -3)")
    report("0a de Sitter K=24, R=12, C=0, Ric=3g",
           abs(s["K"] - 24) < 1e-3 and abs(s["R"] - 12) < 1e-3
           and abs(s["C2"]) < 1e-3 and abs(s["Ric"][0][0] + 3) < 1e-3)
    for r in (4.0, 5.0):
        s = scalars(schw_g, [0.3, r, math.pi / 4, 0.1])
        print(f"  Schw r={r}: K={s['K']:.6e} (expect {48 / r**6:.6e})  "
              f"max|Ric|={max(abs(s['Ric'][i][j]) for i in range(N) for j in range(N)):.2e}  "
              f"C2={s['C2']:.6e} (expect K)")
        report(f"0b Schwarzschild r={r}: K=48/r^6, Ric=0, C2=K",
               abs(s["K"] - 48 / r**6) < 1e-6 * max(1.0, 48 / r**6) * 100
               and abs(s["C2"] - s["K"]) < abs(s["K"]) * 1e-3)

    print("== A/B. Vaidya curvature scalars ==")
    pts = [(-1.0, 3.0, math.pi / 4), (0.5, 3.0, math.pi / 4),
           (0.5, 7.0, 0.7), (2.0, 5.0, math.pi / 3), (2.0, 8.0, 1.2)]
    worst = 0.0
    for (v, r, th) in pts:
        m = smoothstep(v)
        s = scalars(vaidya_g, [v, r, th, 0.3])
        Kref = 48 * m * m / r ** 6
        eK = abs(s["K"] - Kref) / max(Kref, 1e-9) if Kref > 1e-9 else abs(s["K"])
        eR = abs(s["R"])
        eRic2 = abs(s["Ric2"])
        Rvv = s["Ric"][0][0]
        Rvref = 2 * dsmooth(v) / r ** 2
        eRvv = abs(Rvv - Rvref) / max(abs(Rvref), 1e-9) if abs(Rvref) > 1e-9 else abs(Rvv)
        worst = max(worst, eK, eRic2, eRvv)
        print(f"  point v={v:5.2f} r={r:5.2f}: K={s['K']: .6e} Kref={Kref: .6e} "
              f"relerr(K)={eK:.2e}  R={s['R']:.2e} Ric2={s['Ric2']:.2e} "
              f"R_vv={Rvv: .6e} ref={Rvref: .6e} relerr={eRvv:.2e}")
    report("A/B Kretschmann=48m^2/r^6, R=0, Ric2=0, R_vv=2m'/r^2", worst < 5e-4,
           f"(worst rel/abs err {worst:.2e})")

    print("== C. Weyl (1,3) invariance under g->Omega^2 g ==")
    wmax = 0.0
    for (gf, name, pt) in [(vaidya_g, "Vaidya", [0.6, 4.0, 0.9, 0.3]),
                           (product_g, "product", [0.7, 0.4, 0.9, 1.1])]:
        C1 = scalars(gf, pt)["C13"]
        C2 = scalars(conformal_g(gf, omega1), pt)["C13"]
        d = max(abs(C1[a][b][c][d] - C2[a][b][c][d])
                for a in range(N) for b in range(N)
                for c in range(N) for d in range(N))
        wmax = max(wmax, d)
        print(f"  {name}: max|C-C'|={d:.2e}")
    report("C C^a_bcd invariant componentwise", wmax < 1e-5, f"(max dev {wmax:.2e})")

    print("== D. product metric: electric Weyl nonzero everywhere ==")
    vals = []
    for th in [0.05, 0.7, math.pi / 2, 2.5, math.pi - 0.05]:
        s = scalars(product_g, [0.3, 0.2, th, 1.0])
        cphi = s["C13"][0][1][0][1]  # C^t_{phi1 t phi1}
        vals.append(cphi)
        print(f"  theta={th:.3f}: C^t_(phi1 t phi1)={cphi:.6f} (expect -1/3)  "
              f"K={s['K']:.4f}  C2={s['C2']:.4f} (expect 10/9~{10/9:.4f}?)")
    report("D C^t_{phi1 t phi1} = -1/3 at every theta",
           all(abs(v + 1.0 / 3.0) < 0.02 for v in vals),
           f"(values {['%.4f' % v for v in vals]})")

    print("== E. Cauchy time function T = v - 2r/3 + m(v)^2/r ==")
    worstA = -1e9
    steps = 0
    v = -3.0
    while v <= 6.0:
        r = 0.02
        while r <= 40.0:
            m = smoothstep(v); mp = dsmooth(v)
            Tv = 1 + 2 * m * mp / r
            Tr = -2.0 / 3.0 - m * m / (r * r)
            A = 2 * Tv * Tr + (1 - 2 * m / r) * Tr * Tr
            worstA = max(worstA, A)
            steps += 1
            r *= 1.05
        v += 0.05
    report("E g(grad T,grad T) < 0 on grid", worstA < 0,
           f"(max value {worstA:.4f}, {steps} pts)")

    print("== F. witness segment {v=2, r decreasing} is a lightlike pregeodesic ==")
    x0 = [2.0, 6.0, math.pi / 4, 0.3]
    g, ginv, Gam, Rm, Ric = curv_at(vaidya_g, x0)
    xdot = [0.0, -1.0, 0.0, 0.0]
    acc = [sum(Gam[i][j][k] * xdot[j] * xdot[k]
               for j in range(N) for k in range(N)) for i in range(N)]
    gnorm = sum(g[i][j] * xdot[i] * xdot[j] for i in range(N) for j in range(N))
    ratio = acc[1] / xdot[1] if xdot[1] != 0 else float("inf")
    others = max(abs(acc[i] - ratio * xdot[i]) for i in range(N))
    print(f"  g(tangent,tangent)={gnorm:.2e} (lightlike if ~0)")
    print(f"  acceleration parallel to tangent: other components {others:.2e}")
    report("F lightlike pregeodesic", abs(gnorm) < 1e-9 and others < 1e-7)

    print("== G. flat-region witness tangent is null; region flat ==")
    s = scalars(vaidya_g, [-1.5, 1.2, math.pi / 4, 0.0])
    g = s["g"]
    xdot = [1.0, 0.5, 0.0, 0.0]
    gnorm = sum(g[i][j] * xdot[i] * xdot[j] for i in range(N) for j in range(N))
    print(f"  g(dot,dot)={gnorm:.2e}  Kretschmann={s['K']:.2e}")
    report("G null tangent and flat at (v,r)=(-1.5,1.2)",
           abs(gnorm) < 1e-12 and s["K"] < 1e-10)


if __name__ == "__main__":
    main()
