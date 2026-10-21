"""Three constraint formulations for the same Z_3 clock + qubit + interaction.

Standard library only. Run:

    python3 experiments/constraint-formulations/formulations.py

Conventions: see SPEC.md in this directory (fixed before the code). Sections:
  1  formulation A: eigenvalue constraint (surfaces of H)
  2  formulation B: step-invariance / history states (Boette-Rossignoli Eqs. 2-5;
     HSC Sec. 5 Eqs. 24-27), variants B1 (uniform), B2 (closure), B3 (no closure)
  3  formulation C0: verbatim replica of Ludescher et al. Example 32 (validation)
  4  C1 wrap/origin and matched-lambda diagnostics
  5  known-limit check at g = 0 against the closed forms of SPEC.md
  6  side-by-side conditional predictions at interacting comparison points
  7  cross-check against ../clock-three-picture/model_output.txt
"""
import cmath
import math
import os
import random
import re

from linalg import (add, dag, eigh, expm_hermitian, eye, inner, kron, matmul,
                    matvec, maxabs, norm, outer, scale, zeros)

N = 3
T = [2 * math.pi * k / N for k in range(N)]  # t_k = 2 pi k / 3
T1 = T[1]
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
I2, I3 = eye(2), eye(N)
TAU = [[cmath.exp(-1j * n * T[k]) / math.sqrt(N) for n in range(N)] for k in range(N)]

K_RD = [[TAU[0][i] * TAU[0][j].conjugate() for j in range(3)] for i in range(3)]  # |tau_0><tau_0|
K_EN = [[0 + 0j, 0j, 0j], [0j, 1 + 0j, 0j], [0j, 0j, 0j]]                     # |n=1><n=1|


def vscale(c, v):
    return [c * x for x in v]


def proj3_at(g):
    """Reading projector |tau_g><tau_g| (position basis of the clock)."""
    return [[TAU[g][i] * TAU[g][j].conjugate() for j in range(3)] for i in range(3)]


def tau(k):
    return TAU[k]


def hamiltonian(g, eps, K):
    HC = [[complex(n) if n == m else 0j for m in range(N)] for n in range(N)]
    HS = [[0.5 * eps + 0j, 0j], [0j, -0.5 * eps + 0j]]
    H0 = add(kron(HC, I2), kron(I3, HS))
    return add(H0, scale(g, kron(K, SX)))


def hs_sys(eps):
    return [[0.5 * eps + 0j, 0j], [0j, -0.5 * eps + 0j]]


def sys_step(eps, k):
    """e^{-i H_S t_k}, closed form (H_S diagonal)."""
    return [[cmath.exp(-1j * 0.5 * eps * T[k]), 0j], [0j, cmath.exp(1j * 0.5 * eps * T[k])]]


def slices(psi):
    """|S(k)> = sqrt(3) (<tau_k| x 1)|psi> as three 2-vectors."""
    return [[sum(cmath.exp(1j * n * T[k]) * psi[2 * n + s] for n in range(N))
             for s in range(2)] for k in range(N)]


def p_read(psi):
    return [norm(s) ** 2 / 3 for s in slices(psi)]


def p_dev(psi):
    return max(abs(x - 1 / 3) for x in p_read(psi))


def seed_M0():
    """sqrt(3) |tau_0><tau_0| (x) 1 (Ludescher M_0^{(1)})."""
    return scale(math.sqrt(3), kron(proj3_at(0), I2))


def null_space(a, tol=1e-7):
    """Orthonormal basis of ker(a) for square a, via eigh of a^dag a (PSD)."""
    h = matmul(dag(a), a)
    top = max(abs(h[i][i].real) for i in range(len(h))) + 1.0
    basis = []
    for lam, bs in eigh(h, cluster=1e-9):
        if lam < tol * top:
            basis.extend(bs)
    for b in basis:
        r = norm(matvec(a, b))
        assert r < 1e-6, f"null-space residual {r}"
    return basis


def commutator_maxabs(a, b):
    return maxabs(add(matmul(a, b), scale(-1, matmul(b, a))))


def phase_infid(u, w):
    """1 - |<w,u>|^2 / (||u|| ||w||)^2; invariant under phases of either side."""
    du, dw = norm(u), norm(w)
    if du < 1e-14 or dw < 1e-14:
        return float("nan")
    return 1.0 - abs(inner(w, u)) ** 2 / (du * dw) ** 2


def inv_n(m):
    n = len(m)
    if n == 1:
        return [[1 / m[0][0]]]
    if n == 2:
        a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
        det = a * d - b * c
        return [[d / det, -b / det], [-c / det, a / det]]
    aug = [row[:] + [1 + 0j if i == j else 0j for j in range(n)]
           for i, row in enumerate(m)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and abs(aug[r][col]) > 1e-300:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def sec(title):
    print(f"\n=== {title}")


# ---------------------------------------------------------------- formulation A
def lane_A(eps, g, K, label):
    spec = eigh(hamiltonian(g, eps, K))
    rows = []
    for lam, basis in spec:
        p = p_read(basis[0])
        cn = [math.sqrt(3 * x) for x in p]
        print(f"   A ({label}, eps={eps}, g={g}): lam = {lam:+.4f} dim {len(basis)} | p = "
              + " ".join(f"{x:.4f}" for x in p)
              + f" | max|p-1/3| = {p_dev(basis[0]):.1e} | cond norms = "
              + " ".join(f"{x:.3f}" for x in cn))
        rows.append((lam, len(basis)))
    return rows


def lane_A_surface_maps(eps, g, K, lam_target):
    """On the 2-dim surface nearest lam_target: reduction R(k), maps A_k = R(k) R(0)^-1."""
    lam, V = min(eigh(hamiltonian(g, eps, K)),
                 key=lambda lb: abs(lb[0] - lam_target) if len(lb[1]) == 2 else 1e9)
    assert len(V) == 2, "no 2-dim surface near target"
    R = []
    for k in range(N):
        cols = [slices(b)[k] for b in V]
        R.append([[cols[j][i] for j in range(2)] for i in range(2)])
    A = [matmul(R[k], inv_n(R[0])) for k in range(N)]
    return lam, V, A


# ---------------------------------------------------------------- formulation B
def step_ops_B(variant, g, eps):
    """steps[t] = U_{t,(t-1) mod 3}, 2x2 unitaries. Kick convention:
    V = e^{-i H_S t_1} e^{-i g t_1 sigma_x} (sigma_x kick applied first)."""
    free = sys_step(eps, 1)
    a = g * T1
    kmat = [[math.cos(a) + 0j, -1j * math.sin(a)], [-1j * math.sin(a), math.cos(a) + 0j]]
    kick = matmul(free, kmat)  # e^{-i H_S t_1} e^{-i g t_1 sigma_x}
    if variant == "B1":     # interaction on at every step; closure only if V^3 = 1
        return [kick, kick, kick]
    if variant == "B2":     # kick on leaving tau_0; last step = (U_21 U_10)^-1
        return [inv_n(matmul(free, kick)), kick, free]
    if variant == "B3":     # kick on leaving tau_0; last step free (no closure)
        return [free, kick, free]
    raise ValueError(variant)


def U_big(steps):
    """U = sum_t |tau_t><tau_{t-1}| (x) U_{t,t-1}, clock first."""
    u = zeros(6)
    for t in range(N):
        u = add(u, kron(outer(tau(t), tau((t - 1) % N)), steps[t]))
    return u


def lane_B(variant, eps, g, detail=False):
    steps = step_ops_B(variant, g, eps)
    U = U_big(steps)
    mon = matmul(matmul(steps[0], steps[2]), steps[1])  # U_02 U_21 U_10
    out = dict(variant=variant, eps=eps, g=g,
               closure=maxabs(add(mon, scale(-1, eye(2)))),
               unitarity=maxabs(add(matmul(dag(U), U), scale(-1, eye(6)))),
               dim=len(null_space(add(U, scale(-1, eye(6))))),
               steps=steps)
    if out["closure"] < 1e-9:
        u3 = matmul(matmul(U, U), U)
        out["U3"] = maxabs(add(u3, scale(-1, eye(6))))
        w = cmath.exp(-2j * math.pi / N)
        out["degen"] = [out["dim"]] + [len(null_space(add(U, scale(-w ** k, eye(6)))))
                                       for k in (1, 2)]
    if detail and out["dim"] > 0:
        A = [eye(2)]
        for s in (steps[1], steps[2], steps[0]):
            A.append(matmul(s, A[-1]))
        chain, pd = 0.0, 0.0
        for psi in null_space(add(U, scale(-1, eye(6)))):
            S = slices(psi)
            pd = max(pd, p_dev(psi))
            for t in range(N):
                diff = [a - b for a, b in zip(S[t], matvec(steps[t], S[(t - 1) % N]))]
                chain = max(chain, norm(diff))
        out.update(A=A, chain=chain, pdev=pd,
                   unit_maps=max(maxabs(add(matmul(dag(a), a), scale(-1, eye(2)))) for a in A))
    return out


# ---------------------------------------------------------------- formulation C0
def ex32_U(g, K):
    """Ludescher Eq. (58): U_g |x1,x2> = e^{-i(2 pi g/3) K (x1-x2)^2} |x1+g, x2+g>."""
    u = zeros(9)
    for x1 in range(N):
        for x2 in range(N):
            d = (x1 - x2) % N
            u[3 * ((x1 + g) % N) + ((x2 + g) % N)][3 * x1 + x2] = \
                cmath.exp(-2j * math.pi * g * K * d * d / N)
    return u


def ex32_dP(d, P):
    """|d;P> = 3^{-1/2} sum_g conj(chi_P(g)) |g, g+d> (Eq. 59)."""
    v = [0j] * 9
    for g in range(N):
        v[3 * g + (g + d) % N] = cmath.exp(-2j * math.pi * P * g / N) / math.sqrt(N)
    return v


def ex32_seed_op(g):
    """sqrt(3) |g><g|_1 (x) 1_2 on the 9-dim space."""
    op = zeros(9)
    for x2 in range(N):
        op[3 * g + x2][3 * g + x2] = math.sqrt(3)
    return op


def ex32_cm_op():
    """sqrt(3) sum_x |-floor(x/2), x-floor(x/2)><...| on the 9-dim space."""
    op = zeros(9)
    for x in range(N):
        op[3 * (-(x // 2) % N) + (x - (x // 2)) % N][3 * (-(x // 2) % N) + (x - (x // 2)) % N] = \
            math.sqrt(3)
    return op


def ex32_replica(K=1):
    sec(f"3. C0: verbatim replica of Ludescher et al. Example 32 (Z_3, K = {K})")
    U = [ex32_U(g, K) for g in range(N)]
    checks = []
    checks.append(("U_1^3 = 1", maxabs(add(matmul(matmul(U[1], U[1]), U[1]), scale(-1, eye(9))))))
    checks.append(("U_2 = U_1^2", maxabs(add(U[2], scale(-1, matmul(U[1], U[1]))))))
    locked = [ex32_dP(d, (K * d * d) % N) for d in range(N)]
    Fix = null_space(add(U[1], scale(-1, eye(9))))
    ov = [[inner(a, b) for b in locked] for a in Fix]
    ovd = maxabs(add(matmul(dag(ov), ov), scale(-1, eye(3)))) if len(Fix) == 3 else float("nan")
    checks.append((f"Fix(U_1) (dim {len(Fix)}) = span|d;Kd^2>", ovd))
    m0 = [matvec(ex32_seed_op(0), b) for b in locked]
    frame = 0.0
    for g in range(N):
        opg = ex32_seed_op(g)
        tgt = [matvec(opg, b) for b in locked]
        imgs = [matvec(U[g], c) for c in m0]
        frame = max(frame, maxabs([[imgs[i][j] - tgt[i][j] for j in range(9)] for i in range(3)]))
    checks.append(("M_g = U_g M_0 = sqrt(3)|g><g|_1 (x)1 on H_phys", frame))
    comp = zeros(3)
    for g in range(N):
        imgs = [matvec(U[g], c) for c in m0]
        imgm = [[imgs[c][r] for c in range(3)] for r in range(9)]  # columns = imgs
        comp = add(comp, matmul(dag(imgm), imgm))
    comp = scale(1 / N, comp)
    checks.append(("(1/n) sum_g M_g^dag M_g = 1_phys", maxabs(add(comp, scale(-1, eye(3))))))

    def local_persp(coefs, g):
        vin = [sum(c * col[j] for c, col in zip(coefs, m0)) for j in range(9)]
        v = vin
        for _ in range(g % N):
            v = matvec(U[1], v)
        return v

    rng = random.Random(3)
    c = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]
    c = [x / norm(c) for x in c]
    fac = 0.0
    for g in range(N):
        v = local_persp(c, g)
        pg = zeros(9)
        for b in range(N):
            pg[3 * g + b][3 * g + b] = 1 + 0j
        diff = [a - b for a, b in zip(v, matvec(pg, v))]
        fac = max(fac, norm(diff))
    checks.append(("local seed: |psi(g)> = |g>_1 (x) |psi_S(g)>_2", fac))
    maps = []
    for g in range(2):
        X, Y = [], []
        for d in range(N):
            e = [1 + 0j if i == d else 0j for i in range(3)]
            v0, v1 = local_persp(e, g), local_persp(e, g + 1)
            X.append(v0[3 * (g % N):3 * (g % N) + 3])
            Y.append(v1[3 * ((g + 1) % N):3 * ((g + 1) % N) + 3])
        Xm = [[X[j][i] for j in range(3)] for i in range(3)]
        Ym = [[Y[j][i] for j in range(3)] for i in range(3)]
        maps.append(matmul(Ym, inv_n(Xm)))
    gdep = maxabs(add(maps[0], scale(-1, maps[1])))
    # center-of-mass seed: Eq. (60) step map, checked on each locked basis state
    cmop = ex32_cm_op()
    phop = zeros(9)
    for x1 in range(N):
        for x2 in range(N):
            d = (x1 - x2) % N
            phop[3 * x1 + x2][3 * x1 + x2] = cmath.exp(-2j * math.pi * K * d * d / N)
    ok60 = 0.0
    for d in range(N):
        v0 = matvec(cmop, locked[d])
        v1 = matvec(U[1], v0)
        rel0 = [v0[3 * ((-(dd // 2)) % N) + (dd - (dd // 2)) % N] for dd in range(N)]
        rel1 = [v1[3 * ((1 - (dd // 2)) % N) + (1 + dd - (dd // 2)) % N] for dd in range(N)]
        pred = [sum(phop[dd2][dd] * rel0[dd] for dd in range(N)) for dd2 in range(N)]
        ok60 = max(ok60, max(abs(a - b) for a, b in zip(rel1, pred)))
    checks.append(("cm seed: Eq. (60) step map = e^{-i(2pi/3)K(X1-X2)^2}", ok60))
    for name, val in checks:
        print(f"   {name}: {val:.2e}")
    print("   local-seed step maps on the Z_3 system:")
    for name, m in (("U_eff(0->1)", maps[0]), ("U_eff(1->2)", maps[1])):
        print(f"     {name} = " + " / ".join(" ".join(f"{x:.4f}" for x in row) for row in m))
    print(f"   ||U_eff(0->1) - U_eff(1->2)||_max = {gdep:.4f}  (paper: g-dependent)")
    return all(v < 1e-6 for _, v in checks)


# ---------------------------------------------------------------- formulation C1
def unitary_C(eps, g, K, origin):
    """Cyclic candidate U_lambda; it is a Z_N action only if U_lambda**N=I."""
    H_shifted = add(hamiltonian(g, eps, K), scale(-origin, eye(6)))
    U = expm_hermitian(H_shifted, 2 * math.pi / N)
    wrap = matmul(matmul(U, U), U)
    energies = [lam for lam, _ in eigh(hamiltonian(g, eps, K))]
    gap_defect = max((abs((a - b) - round(a - b))
                      for i, a in enumerate(energies) for b in energies[:i]), default=0.0)
    return U, maxabs(add(wrap, scale(-1, eye(6)))), gap_defect


def eigenspace_dim(eps, g, K, target, tol=1e-7):
    return sum(len(basis) for lam, basis in eigh(hamiltonian(g, eps, K))
               if abs(lam - target) < tol)


def lane_C(eps, g, K, label, origin=0.0):
    U, wrap_defect, gap_defect = unitary_C(eps, g, K, origin)
    B = null_space(add(U, scale(-1, eye(6))))
    dim = len(B)
    res = dict(dim=dim, eps=eps, g=g, K=label, origin=origin,
               wrap=wrap_defect, gap_defect=gap_defect,
               is_action=wrap_defect < 1e-8)
    action_label = "Z3 action" if res["is_action"] else "unitary diagnostic only; not a Z3 action"
    if dim == 0:
        print(f"-- C1 ({label}, eps={eps}, g={g}, lambda={origin:+.6f}): "
              f"Fix dim=0; wrap defect={wrap_defect:.2e}; integer-gap defect={gap_defect:.2e}; {action_label}")
        return res
    M0 = seed_M0()
    frame, comp, fac = 0.0, zeros(dim), 0.0
    for gk in range(N):
        cols = [matvec(M0, b) for b in B]
        for _ in range(gk):
            cols = [matvec(U, c) for c in cols]
        tgt = [matvec(scale(math.sqrt(3), kron(proj3_at(gk), I2)), b) for b in B]
        frame = max(frame, maxabs([[cols[i][j] - tgt[i][j] for j in range(6)]
                                   for i in range(dim)]))
        img = [[cols[c][r] for c in range(dim)] for r in range(6)]  # columns = cols
        comp = add(comp, matmul(dag(img), img))
    comp = scale(1 / N, comp)
    comp_def = maxabs(add(comp, scale(-1, eye(dim))))
    for b in B:
        v = matvec(M0, b)
        for gk in range(N):
            if gk:
                v = matvec(U, v)
            pg = kron(proj3_at(gk), I2)  # reading-position slice, not an energy block
            fac = max(fac, norm([x - y for x, y in zip(v, matvec(pg, v))]))
    rng_c = random.Random(11)
    cb = [complex(rng_c.gauss(0, 1), rng_c.gauss(0, 1)) for _ in range(dim)]
    cb = [x / norm(cb) for x in cb]
    psi_mix = [sum(c * bb[i] for c, bb in zip(cb, B)) for i in range(6)]
    pd = max(max(p_dev(b) for b in B), p_dev(psi_mix))
    print(f"-- C1 ({label}, eps={eps}, g={g}, lambda={origin:+.6f}): "
          f"Fix dim={dim} | wrap defect={wrap_defect:.2e} | integer-gap defect={gap_defect:.2e}"
          f" | {action_label} | max|p-1/3| = {pd:.1e}"
          f" | local seed/readout covariance defect = {frame:.2e} | completeness defect = {comp_def:.2e}"
          f" | factorization defect = {fac:.2e}")
    res.update(pdev=pd, frame=frame, comp=comp_def, fac=fac)
    return res


def lane_C_dynamics(eps, g, K, origin=0.0):
    """One-step maps of perspectival system states in Fix(U_lambda), if dim=2."""
    U, _, _ = unitary_C(eps, g, K, origin)
    B = null_space(add(U, scale(-1, eye(6))))
    if len(B) != 2:
        return None
    M0 = seed_M0()

    def persp(b, k):
        v = matvec(M0, b)
        for _ in range(k):
            v = matvec(U, v)
        return [v[2 * k], v[2 * k + 1]]

    X = [persp(b, 0) for b in B]
    Xm = [[X[j][i] for j in range(2)] for i in range(2)]
    A = []
    for k in (1, 2):
        Y = [persp(b, k) for b in B]
        Ym = [[Y[j][i] for j in range(2)] for i in range(2)]
        A.append(matmul(Ym, inv_n(Xm)))
    return A


# ---------------------------------------------------------------- sections
def dyn_infid(A, eps, rng):
    worst = 0.0
    for _ in range(50):
        v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2)]
        u = [x / norm(v) for x in v]
        for k in range(N):
            worst = max(worst, phase_infid(matvec(A[k % N], u),
                                           matvec(sys_step(eps, k), u)))
    return worst


def known_limit():
    sec("5. Known-limit check at g = 0 (closed forms from SPEC.md)")
    rng = random.Random(7)
    for eps in (1, 2):
        print(f"-- eps = {eps}")
        spec = eigh(hamiltonian(0.0, eps, K_RD))
        dims = [(lam, len(b)) for lam, b in spec if len(b) == 2]
        closed = "{0.5, 1.5}" if eps == 1 else "{1}"
        print(f"   A : closed 2-dim surfaces at lam in {closed} | computed: {dims}")
        for lam, _ in dims:
            _, V, A = lane_A_surface_maps(eps, 0.0, K_RD, lam)
            print(f"      lam = {lam:+.2f}: p dev {p_dev(V[0]):.1e}"
                  f" | infid(A_k, e^-iH_S t_k) = {dyn_infid(A, eps, rng):.1e}")
        for v in ("B1", "B3"):
            closed_dim = 0 if eps == 1 else 2
            r = lane_B(v, eps, 0.0, detail=(closed_dim == 2))
            extra = ""
            if closed_dim == 2 and r["dim"] == 2:
                extra = (f" | p dev {r['pdev']:.1e}"
                         f" | infid = {dyn_infid(r['A'], eps, rng):.1e}")
            print(f"   {v}: closed dim {closed_dim} | computed dim = {r['dim']}{extra}")
        r = lane_B("B2", eps, 0.0, detail=True)
        print(f"   B2: closed dim 2, p = 1/3, A_k = e^-iH_S t_k | computed dim = {r['dim']}"
              f" | p dev {r['pdev']:.1e} | chain resid {r['chain']:.1e}"
              f" | infid = {dyn_infid(r['A'], eps, rng):.1e}")
        matched_lambda = 0.5 if eps == 1 else 1.0
        c1 = lane_C(eps, 0.0, K_RD, "K_rd", matched_lambda)
        if c1["dim"] == 2:
            A = lane_C_dynamics(eps, 0.0, K_RD, matched_lambda)
            print(f"      C1 infid(cumulative maps, e^-iH_S t_k) = "
                  f"{dyn_infid([eye(2)] + A, eps, rng):.1e}")
    print("-- interacting dimensions (g = 0.5)")
    for K, lab in ((K_RD, "K_rd"), (K_EN, "K_en")):
        for eps in (1, 2):
            lane_C(eps, 0.5, K, lab, 0.0)


def origin_alias_checks():
    sec("4. Wrap closure, scalar-origin repair, and matched-lambda alias checks")
    cases = [
        ("K_rd", K_RD, 1, 0.0, 0.5, True, 2, 2),
        ("K_rd", K_RD, 1, 0.0, -0.5, True, 1, 2),
        ("K_en", K_EN, 2, 0.0, 1.0, True, 2, 2),
        ("K_en", K_EN, 2, 0.0, 0.0, True, 1, 2),
        ("K_en", K_EN, 2, 0.5, 1.0, False, 2, 2),
        ("K_en", K_EN, 2, math.sqrt(3), 1.0, True, 2, 2),
        ("K_en", K_EN, 2, math.sqrt(3), 0.0, True, 0, 2),
        ("K_rd", K_RD, 1, 0.5, -0.5527, False, 1, 0),
    ]
    for label, K, eps, g, origin, repair_expected, dirac_expected, fix_expected in cases:
        U, wrap, gap_defect = unitary_C(eps, g, K, origin)
        fix_dim = len(null_space(add(U, scale(-1, eye(6)))))
        dirac_dim = eigenspace_dim(eps, g, K, origin)
        alias_dim = fix_dim - dirac_dim
        status = "valid Z3 action" if wrap < 1e-8 else "NONCLOSING unitary diagnostic"
        repair = gap_defect < 1e-8
        assert repair == repair_expected
        assert dirac_dim == dirac_expected and fix_dim == fix_expected
        print(f"   {label}, eps={eps}, g={g:.9g}, lambda={origin:+.6g}: "
              f"wrap ||U^3-I||_max={wrap:.3e}; integer-gap residual={gap_defect:.3e}; "
              f"some scalar-origin repair={'yes' if repair else 'no'}; "
              f"dim V_lambda={dirac_dim}; dim Fix(U_lambda)={fix_dim}; "
              f"extra phase-alias dim={alias_dim}; {status}")


def comparisons():
    sec("6. Side-by-side conditional predictions at interacting points")
    print("\n## point 1: K_rd, eps=1, g=0.5 (reading-projector interaction)")
    lane_A(1, 0.5, K_RD, "K_rd")
    for v in ("B1", "B2", "B3"):
        r = lane_B(v, 1, 0.5)
        extra = f", |U^3-1| = {r['U3']:.1e}, degeneracies {r['degen']}" if "U3" in r else ""
        status = "closed Z3 action" if r["closure"] < 1e-8 else "nonclosing unitary diagnostic only"
        print(f"   {v}: dim E_1(U) diagnostic = {r['dim']} | wrap |M-1| = "
              f"{r['closure']:.1e} | {status}{extra}")
    lane_C(1, 0.5, K_RD, "K_rd", 0.0)

    print("\n## point 2: K_en, eps=2, g=0.5 (energy-projector interaction)")
    lane_A(2, 0.5, K_EN, "K_en")
    b2 = lane_B("B2", 2, 0.5, detail=True)
    print(f"   B2 (closure-imposed step convention): dim = {b2['dim']}; cumulative maps:")
    for k in (1, 2, 3):
        print(f"      A_{k} = " + " / ".join(" ".join(f"{x:.4f}" for x in row)
                                             for row in b2["A"][k]))
    lane_C(2, 0.5, K_EN, "K_en", 1.0)

    print("\n## point 3: fine-tuned K_en, eps=2, g* = sqrt(3) "
          "(n=1 block eigenvalue 1 + sqrt(1+g^2) = 3)")
    gstar = math.sqrt(3)
    print(f"   g* = {gstar:.12f}")
    lane_A(2, gstar, K_EN, "K_en")
    lam, V, A = lane_A_surface_maps(2, gstar, K_EN, 3.0)
    iso = [maxabs(add(matmul(dag(a), a), scale(-1, eye(2)))) for a in A]
    print(f"   A  on the dim-2 surface lam = {lam:+.6f}: isometry defects |A_k^dag A_k - 1|"
          f" = [{iso[1]:.4f}, {iso[2]:.4f}, {iso[0]:.4f}] (k = 1, 2, 3)")
    b2 = lane_B("B2", 2, gstar)
    print(f"   B2: dim = {b2['dim']}")
    c_res = lane_C(2, gstar, K_EN, "K_en", 1.0)
    assert c_res["is_action"] and c_res["frame"] > 1e-4
    hc = [[complex(n) if n == m else 0j for m in range(3)] for n in range(3)]
    assert commutator_maxabs(kron(K_EN, SX), kron(hc, I2)) < 1e-12
    A = lane_C_dynamics(2, gstar, K_EN, 1.0)
    if A:
        for k, m in enumerate(A, start=1):
            print(f"   C1 one-step map g={k - 1} -> {k}: "
                  + " / ".join(" ".join(f"{x:.4f}" for x in row) for row in m))
        gen = expm_hermitian(add(hs_sys(2), scale(gstar, SX)), T1)
    print("   comparison only: e^{-i(H_S + g* sigma_x)t_1} for a uniform-kick convention = "
              + " / ".join(" ".join(f"{x:.4f}" for x in row) for row in gen))
    print("   No equivalence to this uniform-kick model is claimed without an intertwiner preserving the seed and readings.")
    print("-- Same valid action at lambda=0 has aliasing: compare V_0 with Fix(U_0).")
    lane_C(2, gstar, K_EN, "K_en", 0.0)


def crosscheck():
    sec("7. Cross-check vs ../clock-three-picture/model_output.txt (eps=1, K_rd)")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "clock-three-picture", "model_output.txt")
    try:
        with open(path) as f:
            txt = f.read()
    except OSError as e:
        print(f"   prior output not readable ({e}); skipped")
        return
    mine0 = [(round(lam, 4), d) for lam, d in lane_A(1, 0.0, K_RD, "K_rd")]
    ref0 = next((ln.strip() for ln in txt.splitlines() if ln.strip().startswith("g = 0")),
                None)
    print(f"   prior : {ref0}")
    print(f"   mine  : g = 0    : surfaces (lambda: dim) = "
          + ", ".join(f"{lam:+.4f}:{d}" for lam, d in mine0))
    block, grab = [], False
    for ln in txt.splitlines():
        s = ln.strip()
        if s.startswith("=== "):
            grab = "g = 0.5" in s
            continue
        if grab and s.startswith("lambda = "):
            m = re.match(r"lambda = ([+-]\d+\.\d+) dim (\d+)", s)
            if m:
                block.append((round(float(m.group(1)), 4), int(m.group(2))))
    mine5 = [(round(lam, 4), d) for lam, d in lane_A(1, 0.5, K_RD, "K_rd")]
    print(f"   prior g=0.5 (lambda, dim) = {sorted(block)}")
    print(f"   mine  g=0.5 (lambda, dim) = {sorted(mine5)}")
    ok = len(block) == len(mine5) and all(
        abs(a[0] - b[0]) < 1e-3 and a[1] == b[1]
        for a, b in zip(sorted(block), sorted(mine5)))
    print(f"   agree: {ok}")


def main():
    sec("1. Formulation A: eigenvalue constraint, surface tables at g = 0.5")
    for K, lab in ((K_RD, "K_rd"), (K_EN, "K_en")):
        for eps in (1, 2):
            lane_A(eps, 0.5, K, lab)

    sec("2. Formulation B: step-invariance")
    r = lane_B("B2", 1, 0.5, detail=True)
    print("-- structural checks, B2 (eps=1, g=0.5): closure-imposed finite history")
    print(f"   |U^dag U - 1| = {r['unitarity']:.1e}"
          f" | closure |U_02 U_21 U_10 - 1| = {r['closure']:.1e}"
          f" | |U^3 - 1| = {r['U3']:.1e} | degeneracies (1, w, w^2) = {r['degen']}"
          f" | history chain resid = {r['chain']:.1e} | p dev = {r['pdev']:.1e}"
          f" | max |A_k^dag A_k - 1| = {r['unit_maps']:.1e}")
    print("-- dimensions over the grid (eps, g)")
    for v in ("B1", "B2", "B3"):
        row = []
        for eps in (1, 2):
            for g in (0.0, 0.5):
                r = lane_B(v, eps, g)
                label = "closed Z3" if r["closure"] < 1e-8 else "nonclosing diagnostic"
                row.append(f"eps={eps},g={g}: dim E1(U)={r['dim']}, "
                           f"wrap={r['closure']:.2e} ({label})")
        print(f"   {v}: " + " | ".join(row))

    ex32_replica(1)
    known_limit()
    origin_alias_checks()
    comparisons()
    crosscheck()


if __name__ == "__main__":
    main()
