"""Energy outside the past light cone for the Klein-Gordon equation in 2+1 dimensions.

phi_tt - Laplacian(phi) + m^2 phi = 0 on R^{1+2}, rotationally symmetric, with data
phi(0) = exp(-r^2/w^2), phi_t(0) = 0. The solution is written exactly as a Hankel
integral,

    phi(t, r) = int_0^inf a(k) J0(k r) cos(omega t) k dk,   a(k) = (w^2/2) exp(-k^2 w^2/4),

with omega = sqrt(k^2 + m^2), and evaluated by Simpson quadrature in k. For each time t
the script reports

  * the fraction of the energy lying in {|x| >= |t|}, the complement of the past cone
    of the origin event, and
  * the computed total energy divided by its exact value pi/2 + m^2 pi w^2/4, as a check
    on the quadrature (it should be 1).

RESULT.md says the first number tends to 0 as t -> -infinity when m > 0. For m = 0 it
does not. This is a numerical illustration for one datum on a finite grid. It proves
nothing. Standard library only. Runtime about one to two minutes.
"""
import math

W = 2.0          # width of the Gaussian datum
KMAX = 6.0       # a(k) k is below 1e-15 beyond this
NK = 2000        # Simpson intervals in k (even)
DR = 0.1         # radial step
PAD = 15.0       # the datum is negligible beyond r = PAD, so the field is beyond |t| + PAD
DZ = 0.01        # Bessel table step


def _bessel(z):
    """J0(z), J1(z): power series below 10, Hankel asymptotic expansion above."""
    if z < 10.0:
        q = -0.25 * z * z
        term = 1.0; j0 = 1.0
        term1 = 0.5 * z; j1 = term1
        for n in range(1, 60):
            term *= q / (n * n); j0 += term
            term1 *= q / (n * (n + 1)); j1 += term1
        return j0, j1
    amp = math.sqrt(2.0 / (math.pi * z)); z2 = z * z
    p0 = 1 - 9 / (128 * z2) + 3675 / (32768 * z2 * z2)
    q0 = -1 / (8 * z) + 75 / (1024 * z * z2) - 59535 / (262144 * z * z2 * z2)
    p1 = 1 + 15 / (128 * z2) - 4725 / (32768 * z2 * z2)
    q1 = 3 / (8 * z) - 105 / (1024 * z * z2) + 72765 / (262144 * z * z2 * z2)
    c0 = z - 0.25 * math.pi; c1 = z - 0.75 * math.pi
    return (amp * (p0 * math.cos(c0) - q0 * math.sin(c0)),
            amp * (p1 * math.cos(c1) - q1 * math.sin(c1)))


def self_test():
    # first zero of J0, first zero of J1, and agreement of the two branches near z = 10
    assert abs(_bessel(2.404825557695773)[0]) < 1e-12
    assert abs(_bessel(3.831705970207512)[1]) < 1e-12
    amp = math.sqrt(2.0 / (math.pi * 10.0))
    lo = _bessel(10.0 - 1e-9); hi = _bessel(10.0)
    assert abs(lo[0] - hi[0]) < 1e-6 and abs(lo[1] - hi[1]) < 1e-6, (lo, hi)


def run(m, times=(0.0, -25.0, -50.0, -100.0)):
    zmax = KMAX * (max(abs(t) for t in times) + PAD) + 1.0
    nz = int(zmax / DZ) + 2
    J0 = [0.0] * nz; J1 = [0.0] * nz
    for i in range(nz):
        J0[i], J1[i] = _bessel(i * DZ)
    dk = KMAX / NK
    ks = [i * dk for i in range(NK + 1)]
    wts = [(1 if i in (0, NK) else (4 if i % 2 else 2)) * dk / 3.0 for i in range(NK + 1)]
    exact = 0.5 * math.pi + 0.25 * m * m * math.pi * W * W
    out = []
    for t in times:
        cp = []; ct = []; cr = []
        for k, wt in zip(ks, wts):
            om = math.sqrt(k * k + m * m)
            a = 0.5 * W * W * math.exp(-0.25 * k * k * W * W) * k * wt
            cp.append(a * math.cos(om * t))
            ct.append(-a * om * math.sin(om * t))
            cr.append(-a * k * math.cos(om * t))
        nr = int((abs(t) + PAD) / DR)
        e_tot = e_out = 0.0
        for j in range(nr):
            r = (j + 0.5) * DR
            p = pt = pr = 0.0
            s = r / DZ
            for i in range(NK + 1):
                z = ks[i] * s
                iz = int(z); f = z - iz
                j0 = J0[iz] + f * (J0[iz + 1] - J0[iz])
                j1 = J1[iz] + f * (J1[iz + 1] - J1[iz])
                p += cp[i] * j0; pt += ct[i] * j0; pr += cr[i] * j1
            e = 0.5 * (pt * pt + pr * pr + m * m * p * p) * 2.0 * math.pi * r * DR
            e_tot += e
            if r >= abs(t):
                e_out += e
        out.append((t, e_out / e_tot, e_tot / exact))
    return out


if __name__ == "__main__":
    self_test()
    print("2+1 dimensions, Gaussian datum of width 2. Columns: t, fraction of energy in |x| >= |t|, computed/exact total energy")
    for m in (0.0, 0.5, 1.0):
        for t, frac, ratio in run(m):
            print(f"m = {m:3.1f}  t = {t:7.1f}  outside = {frac:.4f}  total check = {ratio:.5f}")
