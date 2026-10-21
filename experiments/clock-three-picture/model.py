"""Z_3 clock + qubit with a clock-system interaction that does not commute with the
clock Hamiltonian. Standard library only. Run:

    python3 experiments/clock-three-picture/model.py

Conventions (all stated so the numbers can be reproduced by hand):
- Hilbert space C (x) S, clock first. omega = 1, clock energies {0, 1, 2}.
- Ideal clock readings |tau_k> = 3^{-1/2} sum_n exp(-i n t_k)|n>, t_k = 2 pi k / 3,
  orthonormal, with exp(-i H_C t_1)|tau_k> = |tau_{k+1}>.
- System H_S = (eps/2) sigma_z, eps = 1 (commensurate, so the g = 0 constraint
  surfaces are degenerate).
- H_int = g K (x) sigma_x with K a clock operator; default K = |tau_0><tau_0|, which
  does not commute with H_C.
- A constraint surface is an eigenspace V_lambda of H = H_C + H_S + H_int; physical
  states are vectors in one V_lambda (a pure state on a single surface).
- Non-ideal covariant POVM E_k = sum_j f((j - k) mod 3) |tau_j><tau_j|, f = (1-2d, d, d).
- Page-Wootters reduction R(k) = sqrt(3) (<tau_k| (x) 1); it is an isometry on V
  iff 3 B^dag (|tau_k><tau_k| (x) 1) B = 1 for an orthonormal basis B of V.
- Dirac observable for X: the time average G[X] = sum_lambda P_lambda X P_lambda over
  e^{-iHs}, valid when the spectrum is non-degenerate in Bohr frequencies.
"""
import cmath
import math

from linalg import (add, dag, eigh, eye, inner, kron, matmul, matvec, maxabs, norm,
                    outer, scale, zeros)

N = 3
T = [2 * math.pi * k / N for k in range(N)]
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
I2, I3 = eye(2), eye(N)


def tau(k):
    return [cmath.exp(-1j * n * T[k]) / math.sqrt(N) for n in range(N)]


def proj(v):
    return outer(v, v)


def hamiltonians(g, eps=1.0, K=None):
    HC = [[complex(n) if n == m else 0j for m in range(N)] for n in range(N)]
    HS = [[0.5 * eps + 0j, 0j], [0j, -0.5 * eps + 0j]]
    K = K if K is not None else proj(tau(0))
    H0 = add(kron(HC, I2), kron(I3, HS))
    return HC, HS, K, add(H0, scale(g, kron(K, SX)))


def povm(d):
    f = [1 - 2 * d, d, d]
    return [add(*[scale(f[(j - k) % N], proj(tau(j))) for j in range(N)]) for k in range(N)]


def reading_probs(psi, E):
    return [inner(psi, matvec(kron(Ek, I2), psi)).real for Ek in E]


def isometry_defect(basis, k):
    Pk = kron(proj(tau(k)), I2)
    gram = [[N * inner(a, matvec(Pk, b)) for b in basis] for a in basis]
    return maxabs(add(gram, scale(-1, eye(len(basis)))))


def conditional_state(psi, k):
    """Normalized system state at ideal reading k, and the reading probability."""
    t = tau(k)
    amp = [sum(t[n].conjugate() * psi[2 * n + s] for n in range(N)) for s in range(2)]
    p = norm(amp) ** 2
    return [a / math.sqrt(p) for a in amp] if p > 1e-14 else None, p


def section(title):
    print(f"\n=== {title}")


def main():
    section("1. Commutator and spectrum")
    HC, HS, K, _ = hamiltonians(0.0)
    comm = add(matmul(K, HC), scale(-1, matmul(HC, K)))
    print(f"||[K, H_C]|| = {maxabs(comm):.4f} (K = |tau_0><tau_0|)")
    for g in (0.0, 0.05, 0.2, 0.5, 1.0):
        spec = eigh(hamiltonians(g)[3])
        print(f"g = {g:<4}: surfaces (lambda: dim) = "
              + ", ".join(f"{lam:+.4f}:{len(b)}" for lam, b in spec))

    section("2. Known limit g -> 0: first-order splitting of the lambda = 0.5 surface")
    H0 = hamiltonians(0.0)[3]
    V = next(b for lam, b in eigh(H0) if abs(lam - 0.5) < 1e-6)
    Hint = kron(K, SX)
    block = [[inner(a, matvec(Hint, b)) for b in V] for a in V]
    first = sorted(lam for lam, bs in eigh(block) for _ in bs)
    g = 1e-3
    near = sorted(lam for lam, bs in eigh(hamiltonians(g)[3]) for _ in bs if abs(lam - 0.5) < 0.1)
    print(f"degenerate-perturbation prediction (lambda - 0.5)/g = {[round(x, 6) for x in first]}")
    print(f"numerical at g = 1e-3:              (lambda - 0.5)/g = {[round((x - 0.5) / g, 6) for x in near]}")

    section("3. g = 0 control: trinity conditions hold")
    for k in range(N):
        print(f"R({k}) isometry defect on V_0.5 = {isometry_defect(V, k):.2e}")
    U = [[cmath.exp(-1j * 0.5 * t) if 0 else 0j for _ in range(2)] for t in (0,)]  # placeholder
    psi = [(x + y) / math.sqrt(2) for x, y in zip(V[0], V[1])]
    s0, _ = conditional_state(psi, 0)
    worst = 0.0
    for k in range(N):
        sk, pk = conditional_state(psi, k)
        ev = [cmath.exp(-1j * 0.5 * T[k]) * s0[0], cmath.exp(1j * 0.5 * T[k]) * s0[1]]
        worst = max(worst, 1 - abs(inner(ev, sk)) ** 2)
        print(f"k = {k}: p(k) = {pk:.6f}")
    print(f"max infidelity between PW state and exp(-i H_S t_k) psi_S(0): {worst:.2e}")

    for g in (0.2, 0.5):
        section(f"4. Interacting case g = {g}: every surface, ideal and non-ideal readings")
        H = hamiltonians(g)[3]
        for lam, basis in eigh(H):
            psi = basis[0]
            pid = reading_probs(psi, povm(0.0))
            pni = reading_probs(psi, povm(0.1))
            iso = max(isometry_defect(basis, k) for k in range(N))
            print(f"lambda = {lam:+.4f} dim {len(basis)} | p_ideal = "
                  + " ".join(f"{p:.4f}" for p in pid) + " | p_nonideal(d=0.1) = "
                  + " ".join(f"{p:.4f}" for p in pni) + f" | max isometry defect = {iso:.3f}")

    section("5. Dirac vs PW: twirl identity on physical states (g = 0.5)")
    H = hamiltonians(0.5)[3]
    spec = eigh(H)
    P = [add(*[proj(b) for b in bs]) if len(bs) > 1 else proj(bs[0]) for _, bs in spec]
    E = povm(0.1)
    worst = 0.0
    for _, bs in spec:
        psi = bs[0]
        for k in range(N):
            X = kron(E[k], [[0.5 + 0j, 0.3 - 0.2j], [0.3 + 0.2j, -0.5 + 0j]])
            GX = add(*[matmul(matmul(p, X), p) for p in P])
            worst = max(worst, abs(inner(psi, matvec(GX, psi)) - inner(psi, matvec(X, psi))))
    print(f"max |<G[E_k (x) O]> - <E_k (x) O>| over surfaces and readings = {worst:.2e}")

    section("6. Is a two-dimensional surface ever kept at g != 0? (sweep)")
    Ks = {"|tau0><tau0|": proj(tau(0)),
          "|tau0><tau1| + h.c.": add(outer(tau(0), tau(1)), outer(tau(1), tau(0))),
          "|n=0><n=1| + h.c.": add(outer(*[[1 + 0j if i == a else 0j for i in range(N)] for a in (0, 1)]),
                                   outer(*[[1 + 0j if i == a else 0j for i in range(N)] for a in (1, 0)]))}
    for name, Kx in Ks.items():
        Kc = add(matmul(Kx, hamiltonians(0)[0]), scale(-1, matmul(hamiltonians(0)[0], Kx)))
        dims = []
        for g in (0.05, 0.2, 0.5, 1.0):
            dims.append(max(len(b) for _, b in eigh(hamiltonians(g, K=Kx)[3])))
        print(f"K = {name:22} ||[K,H_C]|| = {maxabs(Kc):.3f}; max surface dim at g = .05,.2,.5,1: {dims}")


if __name__ == "__main__":
    main()
