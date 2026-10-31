"""Test vertex uniformity of the difference estimate; not a proof. Stdlib, 15 s limit.

Predictions of CONTRACTION.md for compact data, as the cone vertex u0 recedes:
1. sup|d phi_c|/sup|d Phi| and sup|d log Lambda|/sup|d Phi| stay flat.
2. For one profile, trace(u0) - trace(2 u0) decays like 1/|u0|, so the whole
   sequence converges with no subsequence.
Grid spacing is fixed, so N grows with |u0|.
"""
import math

import volterra_check as vc

H = 1.0 / 40


def trace(Phi_of_v, u0):
    vc.U0 = u0
    N = int(round((vc.V_MAX - u0) / H))
    v0 = [u0 + H * j for j in range(N + 1)]
    v, phi, lam, h = vc.evolve([Phi_of_v(x) for x in v0], N)
    keep = [k for k in range(N + 1) if v[k] >= -1e-9]
    return [v[k] for k in keep], [phi[k] for k in keep], [lam[k] for k in keep]


base = lambda x: 0.3 * vc.bump(x, 1.0, 2.9) * math.cos(9.0 * (x - 2.0))
bumped = lambda x: base(x) + 0.03 * vc.bump(x, 1.1, 2.4) * math.sin(14.0 * x)
d0 = 0.03

print("1. Lipschitz ratios as u0 recedes")
keep = {}
for u0 in (-4.0, -8.0, -16.0):
    t, p1, l1 = trace(base, u0)
    _, p2, l2 = trace(bumped, u0)
    dPhi = max(abs(bumped(x) - base(x)) for x in t)
    dphi = max(abs(a - b) for a, b in zip(p1, p2))
    dlog = max(abs(math.log(a / b)) for a, b in zip(l1, l2))
    print(f"   u0={u0:6.1f} dphi/dPhi={dphi / dPhi:.5f} dlogLam/dPhi={dlog / dPhi:.5f}")
    keep[u0] = (p1, l1)
_, p3, l3 = trace(base, -32.0)
keep[-32.0] = (p3, l3)

print("2. distance between successive vertices, same profile")
prev = None
for a, b in ((-4.0, -8.0), (-8.0, -16.0), (-16.0, -32.0)):
    dp = max(abs(x - y) for x, y in zip(keep[a][0], keep[b][0]))
    dl = max(abs(x - y) for x, y in zip(keep[a][1], keep[b][1]))
    r = '-' if prev is None else format(prev / dp, '.2f')
    print(f"   u0={a:6.1f} vs {b:6.1f}: sup|d phi_c|={dp:.3e} sup|d lam|={dl:.3e} halving={r}")
    prev = dp
