"""Independent replication of experiments/clock-three-picture/SPEC.md.

Written from SPEC.md only (the original model.py / linalg.py / model_output.txt
were not consulted).  Standard library only.

Eigen-method (deliberately different from Jacobi rotations):
  1. Householder reduction of the complex Hermitian H to a real-diagonal
     Hermitian tridiagonal T (unitary similarity).
  2. Eigenvalues of T by bisection on Sturm-sequence negative counts.
  3. Eigenvalues within 1e-7 are grouped into one surface; the multiplicity is
     the Sturm count.
  4. Each eigenspace is the null space of (H - lambda I), found by Gaussian
     elimination with complete pivoting, then Gram-Schmidt orthonormalised.
  5. Every eigenpair is checked by its residual ||H b - lambda b||, and the
     nullity is checked against the Sturm multiplicity.
"""

import cmath
import math
import random

# ---------------------------------------------------------------- basic linalg
def zeros(r, c):
    return [[0j] * c for _ in range(r)]

def eye(n):
    m = zeros(n, n)
    for i in range(n):
        m[i][i] = 1 + 0j
    return m

def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = zeros(n, m)
    for i in range(n):
        ai = a[i]
        oi = out[i]
        for t in range(k):
            x = ai[t]
            if x != 0:
                bt = b[t]
                for j in range(m):
                    oi[j] += x * bt[j]
    return out

def dag(a):
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]

def add(a, b, s=1.0):
    return [[a[i][j] + s * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def scale(a, s):
    return [[s * x for x in row] for row in a]

def kron(a, b):
    ra, ca, rb, cb = len(a), len(a[0]), len(b), len(b[0])
    out = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k][j * cb + l] = a[i][j] * b[k][l]
    return out

def outer(u, v):
    return [[ui * vj.conjugate() for vj in v] for ui in u]

def matvec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]

def inner(u, v):  # <u|v>
    return sum(x.conjugate() * y for x, y in zip(u, v))

def vnorm(v):
    return math.sqrt(sum(abs(x) ** 2 for x in v))

def col(a, j):
    return [a[i][j] for i in range(len(a))]

def from_cols(cols):
    return [[c[i] for c in cols] for i in range(len(cols[0]))]

def maxabs(a):
    return max(abs(x) for row in a for x in row)

def inv2(a):
    (p, q), (r, s) = a
    det = p * s - q * r
    return [[s / det, -q / det], [-r / det, p / det]]

def herm_eig2(a):
    """Closed-form eigenvalues of a 2x2 Hermitian matrix (ascending)."""
    p, s = a[0][0].real, a[1][1].real
    q = a[0][1]
    m = (p + s) / 2
    r = math.sqrt(((p - s) / 2) ** 2 + abs(q) ** 2)
    return [m - r, m + r]

# --------------------------------------------------------- Hermitian eigensolver
def householder_tridiag(h):
    a = [row[:] for row in h]
    n = len(a)
    for k in range(n - 2):
        x = [a[i][k] for i in range(k + 1, n)]
        nx = vnorm(x)
        if nx < 1e-300:
            continue
        ph = x[0] / abs(x[0]) if abs(x[0]) > 0 else 1 + 0j
        alpha = -ph * nx
        v = x[:]
        v[0] -= alpha
        nv = vnorm(v)
        if nv < 1e-300:
            continue
        v = [vi / nv for vi in v]
        full = [0j] * (k + 1) + v
        p = add(eye(n), outer(full, full), -2.0)  # Hermitian unitary reflector
        a = matmul(matmul(p, a), p)
    d = [a[i][i].real for i in range(n)]
    e2 = [abs(a[i + 1][i]) ** 2 for i in range(n - 1)]
    return d, e2

def sturm_count(d, e2, x):
    """Number of eigenvalues of the tridiagonal strictly less than x."""
    cnt = 0
    q = d[0] - x
    if q == 0:
        q = -1e-300
    if q < 0:
        cnt += 1
    for i in range(1, len(d)):
        q = d[i] - x - e2[i - 1] / q
        if q == 0:
            q = -1e-300
        if q < 0:
            cnt += 1
    return cnt

def eigvals_bisect(h):
    n = len(h)
    d, e2 = householder_tridiag(h)
    lo = min(h[i][i].real - sum(abs(h[i][j]) for j in range(n) if j != i) for i in range(n)) - 1
    hi = max(h[i][i].real + sum(abs(h[i][j]) for j in range(n) if j != i) for i in range(n)) + 1
    vals = []
    for i in range(n):
        a, b = lo, hi  # count(a) <= i < count(b)
        for _ in range(300):
            mid = 0.5 * (a + b)
            if mid == a or mid == b:
                break
            if sturm_count(d, e2, mid) <= i:
                a = mid
            else:
                b = mid
        vals.append(0.5 * (a + b))
    return vals

def null_space(m, tol):
    """Null space by Gaussian elimination with complete pivoting."""
    a = [row[:] for row in m]
    nr, nc = len(a), len(a[0])
    perm = list(range(nc))
    r = 0
    for r in range(min(nr, nc)):
        best, bi, bj = -1.0, r, r
        for i in range(r, nr):
            for j in range(r, nc):
                if abs(a[i][j]) > best:
                    best, bi, bj = abs(a[i][j]), i, j
        if best < tol:
            break
        a[r], a[bi] = a[bi], a[r]
        for row in a:
            row[r], row[bj] = row[bj], row[r]
        perm[r], perm[bj] = perm[bj], perm[r]
        for i in range(r + 1, nr):
            f = a[i][r] / a[r][r]
            if f != 0:
                for j in range(r, nc):
                    a[i][j] -= f * a[r][j]
    else:
        r = min(nr, nc)
    rank = r
    basis = []
    for f in range(rank, nc):
        y = [0j] * nc
        y[f] = 1 + 0j
        for i in range(rank - 1, -1, -1):
            s = sum(a[i][j] * y[j] for j in range(i + 1, nc))
            y[i] = -s / a[i][i]
        x = [0j] * nc
        for pos, orig in enumerate(perm):
            x[orig] = y[pos]
        basis.append(x)
    return rank, basis

def gram_schmidt(vs):
    out = []
    for v in vs:
        w = v[:]
        for _ in range(2):
            for u in out:
                c = inner(u, w)
                w = [wi - c * ui for wi, ui in zip(w, u)]
        nw = vnorm(w)
        out.append([wi / nw for wi in w])
    return out

def surfaces(h, tol=1e-7, ns_tol=1e-8):
    """List of (lambda, B as list of column vectors, max residual)."""
    vals = eigvals_bisect(h)
    groups = []
    for v in vals:
        if groups and abs(v - groups[-1][-1]) <= tol:
            groups[-1].append(v)
        else:
            groups.append([v])
    n = len(h)
    out = []
    for g in groups:
        lam = sum(g) / len(g)
        m = [[h[i][j] - (lam if i == j else 0) for j in range(n)] for i in range(n)]
        rank, basis = null_space(m, ns_tol)
        assert len(basis) == len(g), ("nullity mismatch", lam, len(basis), len(g))
        basis = gram_schmidt(basis)
        res = 0.0
        for b in basis:
            hb = matvec(h, b)
            res = max(res, vnorm([x - lam * y for x, y in zip(hb, b)]))
        out.append((lam, basis, res))
    # orthonormality across all vectors
    allv = [b for _, bs, _ in out for b in bs]
    orth = max(abs(inner(u, v) - (1 if i == j else 0))
               for i, u in enumerate(allv) for j, v in enumerate(allv))
    return out, orth

# ------------------------------------------------------------------ model
W3 = cmath.exp(-2j * math.pi / 3)
TAU = [[cmath.exp(-1j * n * 2 * math.pi * k / 3) / math.sqrt(3) for n in range(3)] for k in range(3)]
T = [2 * math.pi * k / 3 for k in range(3)]
HC = [[0j, 0j, 0j], [0j, 1 + 0j, 0j], [0j, 0j, 2 + 0j]]
EPS = 1.0
HS = [[EPS / 2 + 0j, 0j], [0j, -EPS / 2 + 0j]]
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
I2, I3 = eye(2), eye(3)

def ket(n, dim):
    v = [0j] * dim
    v[n] = 1 + 0j
    return v

KS = {
    "tau0tau0": outer(TAU[0], TAU[0]),
    "tau0tau1+hc": add(outer(TAU[0], TAU[1]), outer(TAU[1], TAU[0])),
    "e0e1+hc": add(outer(ket(0, 3), ket(1, 3)), outer(ket(1, 3), ket(0, 3))),
    "e0e0": outer(ket(0, 3), ket(0, 3)),
}

def ham(g, K):
    h = add(kron(HC, I2), kron(I3, HS))
    return add(h, scale(kron(K, SX), g))

PI = [outer(TAU[k], TAU[k]) for k in range(3)]

def povm(d):
    f = [1 - 2 * d, d, d]
    return [sum_mats([scale(PI[j], f[(j - k) % 3]) for j in range(3)]) for k in range(3)]

def sum_mats(ms):
    out = ms[0]
    for m in ms[1:]:
        out = add(out, m)
    return out

def expval(op, psi):
    return inner(psi, matvec(op, psi))

def probs(psi, d):
    return [expval(kron(E, I2), psi).real for E in povm(d)]

def defect_entry_and_norm(basis):
    """max over k of: largest abs entry, and spectral norm, of 3 B^dag (Pi_k x 1) B - 1."""
    B = from_cols(basis)
    m_entry, m_norm = 0.0, 0.0
    for k in range(3):
        M = add(scale(matmul(matmul(dag(B), kron(PI[k], I2)), B), 3), eye(len(basis)), -1.0)
        m_entry = max(m_entry, maxabs(M))
        if len(basis) == 1:
            nrm = abs(M[0][0])
        else:
            ev = eigvals_bisect(M)
            nrm = max(abs(x) for x in ev)
        m_norm = max(m_norm, nrm)
    return m_entry, m_norm

def R(k):
    """R(k) = sqrt3 (<tau_k| x 1): 2x6."""
    bra = [[x.conjugate() for x in TAU[k]]]
    return scale(kron(bra, I2), math.sqrt(3))

def fmt(x, p=12):
    if isinstance(x, complex):
        if abs(x.imag) < 10 ** -(p + 2):
            return f"{x.real:+.{p}f}"
        return f"({x.real:+.{p}f}{x.imag:+.{p}f}j)"
    return f"{x:+.{p}f}"

def fmtm(m, p=10):
    return "[" + "; ".join("[" + ", ".join(fmt(x, p) for x in row) + "]" for row in m) + "]"

# ------------------------------------------------------------------ run
OUT = []
def say(s=""):
    OUT.append(s)
    print(s)

def main():
    say("Independent replication of clock-three-picture SPEC.md")
    say("Eigensolver: Householder tridiagonalisation + Sturm bisection; eigenspaces by")
    say("Gaussian elimination (complete pivoting) null space of H - lambda I; grouping tol 1e-7;")
    say("null-space pivot tolerance 1e-8. Residuals ||H b - lambda b|| reported.")
    say("Sanity: tau orthonormal: max |<tau_j|tau_k> - delta| = %.2e" %
        max(abs(inner(TAU[j], TAU[k]) - (1 if j == k else 0)) for j in range(3) for k in range(3)))
    U1 = [[cmath.exp(-1j * HC[n][n].real * T[1]) if n == m else 0j for m in range(3)] for n in range(3)]
    say("Sanity: max_k || e^{-i H_C t_1} tau_k - tau_{k+1} || = %.2e" %
        max(vnorm([a - b for a, b in zip(matvec(U1, TAU[k]), TAU[(k + 1) % 3])]) for k in range(3)))

    # ---- item 1
    say("\n== Item 1: largest |entry| of [K, H_C] ==")
    for name, K in KS.items():
        c = add(matmul(K, HC), matmul(HC, K), -1.0)
        say(f"  K={name:12s}  max|[K,H_C]| = {maxabs(c):.12f}")

    # ---- item 2 (+ item 5, item 4)
    gs = [0.0, 0.05, 0.2, 0.5, 1.0]
    K = KS["tau0tau0"]
    say("\n== Item 2: spectrum and surface dimensions, default K = |tau0><tau0| ==")
    say("  (also item 5 isometry defect per surface: 'entry' = largest abs entry as in SPEC,")
    say("   'norm' = spectral norm of the same matrix, which is basis-independent; equal for dim 1)")
    allsurf = {}
    for g in gs:
        s, orth = surfaces(ham(g, K))
        allsurf[g] = s
        say(f"  g={g}: {len(s)} surfaces, dims sum={sum(len(b) for _, b, _ in s)}, "
            f"global orthonormality err={orth:.1e}")
        for lam, b, res in s:
            de, dn = defect_entry_and_norm(b)
            say(f"    lambda={lam:+.12f}  dim={len(b)}  residual={res:.1e}  "
                f"defect(entry)={de:.12f}  defect(norm)={dn:.12f}")

    # ---- item 3
    say("\n== Item 3: first-order splitting of g=0 surface lambda=0.5 ==")
    s0 = [x for x in allsurf[0.0] if abs(x[0] - 0.5) < 1e-6][0]
    B = from_cols(s0[1])
    M = matmul(matmul(dag(B), kron(K, SX)), B)
    pert = herm_eig2(M)
    say(f"  dim V_0.5 at g=0: {len(s0[1])}")
    say(f"  eigenvalues of P (K x sx) P on V_0.5: {pert[0]:+.12f}, {pert[1]:+.12f}")
    gsmall = 1e-3
    ss, _ = surfaces(ham(gsmall, K))
    near = [lam for lam, b, _ in ss for _ in b if abs(lam - 0.5) < 0.05]
    say(f"  g=1e-3 eigenvalues near 0.5: {', '.join('%+.12f' % x for x in near)}")
    say(f"  (lambda(g)-0.5)/g: {', '.join('%+.9f' % ((x - 0.5) / gsmall) for x in near)}")
    say(f"  differences vs first order: "
        f"{', '.join('%.3e' % abs((x - 0.5) / gsmall - p) for x, p in zip(sorted(near), pert))}")

    # ---- item 4
    say("\n== Item 4: reading probabilities p(k) = <psi|E_k x 1|psi>, 1-dim surfaces, default K ==")
    for g in gs:
        for lam, b, _ in allsurf[g]:
            if len(b) != 1:
                continue
            p0 = probs(b[0], 0.0)
            p1 = probs(b[0], 0.1)
            say(f"  g={g:<4} lambda={lam:+.10f}  d=0: [{', '.join('%.12f' % x for x in p0)}]"
                f"  d=0.1: [{', '.join('%.12f' % x for x in p1)}]")
    say("  (multi-dim surfaces skipped here: p(k) is state dependent; see item 2 dims)")

    # ---- item 6
    say("\n== Item 6: twirl identity at g=0.5, default K, X = E_k(d=0.1) x O ==")
    O = [[0.5 + 0j, 0.3 - 0.2j], [0.3 + 0.2j, -0.5 + 0j]]
    s = allsurf[0.5]
    projs = [matmul(from_cols(b), dag(from_cols(b))) for _, b, _ in s]
    rng = random.Random(20261021)
    worst = 0.0
    for k, E in enumerate(povm(0.1)):
        X = kron(E, O)
        GX = sum_mats([matmul(matmul(P, X), P) for P in projs])
        for lam, b, _ in s:
            states = list(b)
            if len(b) > 1:
                c = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in b]
                nc = vnorm(c)
                states.append([sum(c[i] * b[i][r] for i in range(len(b))) / nc for r in range(6)])
            for psi in states:
                a1, a2 = expval(GX, psi), expval(X, psi)
                worst = max(worst, abs(a1 - a2))
                say(f"  k={k} lambda={lam:+.10f}  <G[X]>={fmt(a1, 12)}  <X>={fmt(a2, 12)}  |diff|={abs(a1 - a2):.1e}")
    say(f"  max |<G[X]> - <X>| over k, surfaces = {worst:.2e}")

    # ---- item 7
    say("\n== Item 7a: g=0 control on V_0.5 ==")
    b = s0[1]
    say("  Basis choice: B = Gram-Schmidt of elimination null-space vectors (stated quantities")
    say("  below are invariant under any unitary change of basis of V_0.5; see note).")
    for i, v in enumerate(b):
        say(f"    B_{i} = [{', '.join(fmt(x, 6) for x in v)}]")
    de, dn = defect_entry_and_norm(b)
    say(f"  isometry defect: entry={de:.3e}  norm={dn:.3e}")
    psi = [(x + y) / math.sqrt(2) for x, y in zip(b[0], b[1])]
    say(f"  p(k), psi=(B0+B1)/sqrt2, d=0:   [{', '.join('%.12f' % x for x in probs(psi, 0.0))}]")
    say(f"  p(k), psi=(B0+B1)/sqrt2, d=0.1: [{', '.join('%.12f' % x for x in probs(psi, 0.1))}]")
    cond = []
    for k in range(3):
        phi = matvec(R(k), psi)
        n = vnorm(phi)
        cond.append([x / n for x in phi])
    for k in range(3):
        Uk = [[cmath.exp(-1j * HS[0][0].real * T[k]), 0j], [0j, cmath.exp(-1j * HS[1][1].real * T[k])]]
        pred = matvec(Uk, cond[0])
        F = abs(inner(pred, cond[k])) ** 2
        say(f"  k={k}: fidelity(conditional state, e^(-i H_S t_k) cond_0) = {F:.12f}")
    # basis-independence check: random unitary rotation of basis
    rng2 = random.Random(7)
    th, a1, a2, a3 = (rng2.uniform(0, 6.3) for _ in range(4))
    u = [[cmath.exp(1j * a1) * math.cos(th), cmath.exp(1j * a2) * math.sin(th)],
         [-cmath.exp(-1j * a2) * math.sin(th) * cmath.exp(1j * a3), cmath.exp(-1j * a1) * math.cos(th) * cmath.exp(1j * a3)]]
    b2 = [[sum(b[i][r] * u[i][j] for i in range(2)) for r in range(6)] for j in range(2)]
    psi2 = [(x + y) / math.sqrt(2) for x, y in zip(b2[0], b2[1])]
    c2 = [matvec(R(k), psi2) for k in range(3)]
    c2 = [[x / vnorm(c) for x in c] for c in c2]
    F2 = [abs(inner(matvec([[cmath.exp(-1j * 0.5 * T[k]), 0j], [0j, cmath.exp(1j * 0.5 * T[k])]], c2[0]), c2[k])) ** 2 for k in range(3)]
    say(f"  check with randomly rotated basis: p(k) d=0 = [{', '.join('%.12f' % x for x in probs(psi2, 0.0))}], "
        f"fidelities = [{', '.join('%.12f' % x for x in F2)}], defect entry = {defect_entry_and_norm(b2)[0]:.2e}")

    say("\n== Item 7b: commuting control K = |0><0| ==")
    Kc = KS["e0e0"]
    for g in [0.2, 0.5, 1.0]:
        s, orth = surfaces(ham(g, Kc))
        say(f"  g={g}: dims = {[len(bb) for _, bb, _ in s]}  orth err={orth:.1e}")
        for lam, bb, res in s:
            de, dn = defect_entry_and_norm(bb)
            line = f"    lambda={lam:+.12f} dim={len(bb)} res={res:.1e} defect(entry)={de:.3e} defect(norm)={dn:.3e}"
            if len(bb) == 1:
                line += f"  p(k) d=0: [{', '.join('%.12f' % x for x in probs(bb[0], 0.0))}]"
                line += f" d=0.1: [{', '.join('%.12f' % x for x in probs(bb[0], 0.1))}]"
            else:
                # range of p(k) over the surface: eigenvalues of B^dag (E_k x 1) B
                Bm = from_cols(bb)
                rngs = []
                for E in povm(0.1):
                    ev = eigvals_bisect(matmul(matmul(dag(Bm), kron(E, I2)), Bm))
                    rngs.append(f"[{ev[0]:.12f},{ev[-1]:.12f}]")
                line += f"  p(k) range over surface (d=0.1): {' '.join(rngs)}"
            say(line)

    # ---- other K: spectra for completeness
    say("\n== Extra: spectra for the other K at g in {0.05,0.2,0.5,1.0} ==")
    for name in ["tau0tau1+hc", "e0e1+hc"]:
        for g in [0.05, 0.2, 0.5, 1.0]:
            s, orth = surfaces(ham(g, KS[name]))
            say(f"  K={name} g={g}: " + ", ".join(f"{lam:+.10f}(d{len(bb)})" for lam, bb, _ in s)
                + f"  maxres={max(r for _, _, r in s):.1e}")

    # ---- item 8
    say("\n== Item 8: accidental surface, K = |0><1| + h.c., g = 1 ==")
    s, orth = surfaces(ham(1.0, KS["e0e1+hc"]))
    for lam, bb, res in s:
        say(f"  lambda={lam:+.14f} dim={len(bb)} residual={res:.1e}")
    surf = [x for x in s if abs(x[0] - 1.5) < 1e-6][0]
    bb = surf[1]
    say(f"  surface at 1.5: dim={len(bb)}")
    lamvals = eigvals_bisect(ham(1.0, KS["e0e1+hc"]))
    near15 = [x for x in lamvals if abs(x - 1.5) < 1e-3]
    say(f"  raw bisection eigenvalues near 1.5: {', '.join('%.16f' % x for x in near15)}")
    Bm = from_cols(bb)
    M = [matmul(R(k), Bm) for k in range(3)]  # 2x2 maps (surface coords) -> system
    say(f"  det R(0)|_V = {fmt(M[0][0][0] * M[0][1][1] - M[0][0][1] * M[0][1][0], 12)}")
    M0i = inv2(M[0])
    A = [matmul(M[k], M0i) for k in range(3)]
    say("  NOTE: A_k = R(k)|_V (R(0)|_V)^{-1} maps system C^2 -> C^2 and is independent of the")
    say("  basis chosen for V (B -> BU cancels), so its entries are reported directly.")
    for k in range(3):
        say(f"  A_{k} = {fmtm(A[k])}")
        AA = matmul(dag(A[k]), A[k])
        ev = herm_eig2(AA)
        say(f"     A_{k}^dag A_{k} = {fmtm(AA)}  eigenvalues = {ev[0]:.12f}, {ev[1]:.12f}  "
            f"|det A_{k}| = {abs(A[k][0][0]*A[k][1][1]-A[k][0][1]*A[k][1][0]):.12f}")
    for k in range(3):
        P = matmul(A[(k + 1) % 3], inv2(A[k]))
        PP = matmul(dag(P), P)
        ev = herm_eig2(PP)
        say(f"  P_{k}->{(k+1)%3} = A_{(k+1)%3} A_{k}^-1 = {fmtm(P)}")
        say(f"     P^dag P = {fmtm(PP)}  eigenvalues = {ev[0]:.12f}, {ev[1]:.12f}  "
            f"max|P^dag P - 1| = {maxabs(add(PP, eye(2), -1.0)):.6f}")
    # trace distance experiment
    rng = random.Random(12345)
    def rand_unit():
        v = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2)]
        n = vnorm(v)
        return [x / n for x in v]
    def tdist(a, b):
        a = [x / vnorm(a) for x in a]
        b = [x / vnorm(b) for x in b]
        return math.sqrt(max(0.0, 1 - abs(inner(a, b)) ** 2))
    NP = 2000
    inc = 0
    maxinc = 0.0
    examples = []
    for t in range(NP):
        u, v = rand_unit(), rand_unit()
        ds = [tdist(matvec(A[k % 3], u), matvec(A[k % 3], v)) for k in range(4)]
        steps = [ds[k + 1] - ds[k] for k in range(3)]
        if max(steps) > 1e-12:
            inc += 1
        maxinc = max(maxinc, max(steps))
        if t < 3:
            examples.append(ds)
    say("  Trace distance D_k = T(A_k u/|A_k u|, A_k v/|A_k v|), k=0..3 (A_3 = A_0);")
    say(f"  random unit u,v: complex Gaussian, random.Random(12345), {NP} pairs")
    for i, ds in enumerate(examples):
        say(f"    pair {i}: D = [{', '.join('%.10f' % x for x in ds)}]")
    say(f"  fraction of pairs with D_(k+1) > D_k (+1e-12) at some step: {inc}/{NP} = {inc / NP:.4f}")
    say(f"  largest single-step increase observed: {maxinc:.6f}")

    with open(__file__.replace("replicate.py", "replicate_output.txt"), "w") as fh:
        fh.write("\n".join(OUT) + "\n")

if __name__ == "__main__":
    main()
