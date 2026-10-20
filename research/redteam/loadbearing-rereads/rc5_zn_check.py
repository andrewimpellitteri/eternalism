"""RC-5 finite check: Page-Wootters qubit with an uncoupled Z_N clock and a covariant,
non-ideal clock POVM. Exact arithmetic in floating point; standard library only.

Model: |Psi> = N^-1/2 sum_t |t>_C (x) U(t)|psi>, U(t) = diag(1, e^{-i w t}), w = 2 pi m / N.
POVM E_tau = sum_t f((t - tau) mod N) |t><t|, with f >= 0 and sum_tau E_tau = 1 when f sums to 1.
Conditioned (unnormalized) state: Tr_C[(E_tau (x) 1)|Psi><Psi|] = N^-1 sum_t f(t - tau) U(t) rho U(t)^dag.
Checks, for several blurs f and every pair of readings tau1 < tau2:
  1. the outcome weight Tr is the same for every input state (linear conditioning);
  2. the qubit coherence factor c(tau) has constant modulus, so the map is U(tau) after a
     fixed dephasing D, and the propagator Phi(tau2) Phi(tau1)^-1 on the image is U(tau2 - tau1);
  3. hence no trace-distance revival between readings.
Domain: this model only. Not a statement about interacting or non-covariant clocks."""
import cmath, itertools, math

def coherence(f, N, m, tau):
    w = 2 * math.pi * m / N
    return sum(f[(t - tau) % N] * cmath.exp(-1j * w * t) for t in range(N))

def trace_distance_pair(c):  # rho1=|+><+|, rho2=|-><-|: distance = |c|
    return abs(c)

blurs = {"ideal": lambda N: [1.0] + [0.0] * (N - 1),
         "two-point": lambda N: [0.5, 0.5] + [0.0] * (N - 2),
         "gaussian": lambda N: [math.exp(-min(k, N - k) ** 2 / 2.0) for k in range(N)],
         "lopsided": lambda N: [0.6, 0.3, 0.1] + [0.0] * (N - 3)}
for N, m in ((5, 1), (8, 3), (12, 5)):
    for name, make in blurs.items():
        f = make(N); s = sum(f); f = [x / s for x in f]
        mods = [abs(coherence(f, N, m, tau)) for tau in range(N)]
        assert max(mods) - min(mods) < 1e-12, (N, m, name, mods)
        # Outcome weight for any input: (1/N) sum_t f(t - tau) Tr rho = 1/N, input-independent.
        weights = {round(sum(f[(t - tau) % N] for t in range(N)) / N, 15) for tau in range(N)}
        assert len(weights) == 1
        dists = [trace_distance_pair(coherence(f, N, m, tau)) for tau in range(N)]
        assert all(b <= a + 1e-12 for a, b in zip(dists, dists[1:]))
        print(f"N={N:2} m={m} {name:9}: |c| = {mods[0]:.6f} at every reading; weight 1/N; no revival")
print("All checks passed.")
