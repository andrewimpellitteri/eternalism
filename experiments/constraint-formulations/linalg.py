"""Small complex linear algebra on lists of lists. Standard library only.
Copied verbatim from experiments/clock-three-picture/linalg.py (same conventions;
Jacobi eigensolver on the real embedding; residuals asserted per call).

Hermitian eigendecomposition uses the cyclic Jacobi method on the real symmetric
embedding [[A, -B], [B, A]] of H = A + iB, then recovers complex eigenvectors and
orthonormalizes each eigenspace."""
import cmath
import math

TOL = 1e-10


def zeros(n, m=None):
    return [[0j] * (n if m is None else m) for _ in range(n)]


def eye(n):
    return [[1 + 0j if i == j else 0j for j in range(n)] for i in range(n)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def dag(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def add(*ms):
    return [[sum(m[i][j] for m in ms) for j in range(len(ms[0][0]))] for i in range(len(ms[0]))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def outer(u, v):
    return [[x * y.conjugate() for y in v] for x in u]


def inner(u, v):
    return sum(x.conjugate() * y for x, y in zip(u, v))


def norm(v):
    return math.sqrt(abs(inner(v, v)))


def maxabs(a):
    return max(abs(x) for row in a for x in row)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def _jacobi_symmetric(m, sweeps=100):
    n = len(m)
    a = [row[:] for row in m]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-28:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p], v[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    return [a[i][i] for i in range(n)], [[v[k][i] for k in range(n)] for i in range(n)]


def gram_schmidt(vectors, tol=1e-8):
    basis = []
    for v in vectors:
        w = v[:]
        for b in basis:
            c = inner(b, w)
            w = [x - c * y for x, y in zip(w, b)]
        nv = norm(w)
        if nv > tol:
            basis.append([x / nv for x in w])
    return basis


def eigh(h, cluster=1e-7):
    """Eigenvalues (sorted, with multiplicity) and orthonormal eigenspaces of Hermitian h.
    Returns a list of (eigenvalue, [basis vectors])."""
    n = len(h)
    assert maxabs(add(h, scale(-1, dag(h)))) < 1e-12, "not Hermitian"
    big = [[0.0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            a, b = h[i][j].real, h[i][j].imag
            big[i][j], big[i][j + n] = a, -b
            big[i + n][j], big[i + n][j + n] = b, a
    vals, vecs = _jacobi_symmetric(big)
    order = sorted(range(2 * n), key=lambda i: vals[i])
    groups, cur = [], [order[0]]
    for i in order[1:]:
        if abs(vals[i] - vals[cur[-1]]) < cluster:
            cur.append(i)
        else:
            groups.append(cur)
            cur = [i]
    groups.append(cur)
    out = []
    for g in groups:
        lam = sum(vals[i] for i in g) / len(g)
        cand = [[complex(vecs[i][k], vecs[i][k + n]) for k in range(n)] for i in g]
        basis = gram_schmidt(cand)
        for b in basis:  # residual check
            r = [x - lam * y for x, y in zip(matvec(h, b), b)]
            assert norm(r) < 1e-8, f"eigen residual {norm(r)}"
        out.append((lam, basis))
    assert sum(len(b) for _, b in out) == n, "eigenspace dimensions do not sum to n"
    return out


def expm_hermitian(h, t):
    """exp(-i t h) from the eigendecomposition."""
    n = len(h)
    u = zeros(n)
    for lam, basis in eigh(h):
        ph = cmath.exp(-1j * lam * t)
        for b in basis:
            for i in range(n):
                for j in range(n):
                    u[i][j] += ph * b[i] * b[j].conjugate()
    return u
