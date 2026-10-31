"""Exact zonal solutions of psi_tt = Lap psi - psi on the unit S^3:
psi(t,r) = [G(t+r) - G(t-r)] / sin r, for any smooth 2pi-periodic G.
Checks the PDE residual, then separates the worker's and the paper's fixed sets."""
import math

PI = math.pi


def bump(x, c, w):
    y = ((x - c + PI) % (2 * PI) - PI) / w
    return math.exp(1 - 1 / (1 - y * y)) if abs(y) < 1 else 0.0


def make_G(tau):
    # 2pi-periodic, vanishes on [-tau, tau] + 2 pi Z, positive at pi.
    c, w = PI, PI - tau
    return lambda x: bump(x, c, w)


def psi(G, t, r):
    s = math.sin(r)
    if abs(s) < 1e-7:
        h = 1e-5
        return psi(G, t, r - h if r > 1 else r + h)
    return (G(t + r) - G(t - r)) / s


def residual(G, t, r, h=1e-3):
    p = psi(G, t, r)
    tt = (psi(G, t + h, r) - 2 * p + psi(G, t - h, r)) / h**2
    rr = (psi(G, t, r + h) - 2 * p + psi(G, t, r - h)) / h**2
    rad = rr + 2 * math.cos(r) / math.sin(r) * (psi(G, t, r + h) - psi(G, t, r - h)) / (2 * h)
    return tt - rad + p


def in_diamonds(t, d, tau):
    a = t + d <= tau
    b = (PI - d) + abs(t - PI) <= tau
    c = d + (2 * PI - t) <= tau
    return a or b or c


def worker_fixed(t, d, tau):
    u, v = t + d, t - d
    return u <= tau or v <= tau or v >= 2 * PI - tau or u >= 2 * PI - tau


tau = 1.0
G = make_G(tau)
worst = max(abs(residual(G, t / 7, r / 7)) for t in range(3, 40) for r in range(2, 20))
print("max PDE residual on grid", f"{worst:.2e}")
past = max(abs(psi(G, 0.01 + i * (tau - 0.02) / 50, 0.005 + j * (tau - (0.01 + i * (tau - 0.02) / 50) - 0.01) / 50))
           for i in range(51) for j in range(51))
print("max |psi| on the past cone of b", f"{past:.2e}")

n = disagree = worker_refuted = paper_refuted = 0
example = None
for i in range(1, 400):
    t = 2 * PI * i / 400
    for j in range(1, 200):
        d = PI * j / 200
        p, w = in_diamonds(t, d, tau), worker_fixed(t, d, tau)
        n += 1
        if p != w:
            disagree += 1
        value = abs(psi(G, t, d))
        if value > 1e-9:
            if w and not p:
                worker_refuted += 1
                if example is None or value > example[2]:
                    example = (t, d, value)
            if p:
                paper_refuted += 1
print("grid points", n, "sets disagree at", disagree)
print("points the worker calls fixed where a solution vanishing on the past is nonzero:", worker_refuted)
print("points inside the paper's diamonds where it is nonzero:", paper_refuted)
print("example (eta, d, |psi|)", example)
t, d = tau, PI - 1e-3
print("at (tau, antipode): worker fixed?", worker_fixed(t, d, tau), " in diamonds?", in_diamonds(t, d, tau), " |psi| =", f"{abs(psi(G, t, d)):.3f}")
