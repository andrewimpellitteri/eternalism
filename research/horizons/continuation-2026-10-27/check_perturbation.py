"""Bounded spectral/quadrature controls, not a proof of exact past vanishing.

The analytic compact-support and all-smooth-solutions arguments are in RESULT.md.
No finite spectral truncation has exactly the compact support used in that proof.
"""
import json
import math
from pathlib import Path

PI = math.pi


def simpson(samples, width):
    n = len(samples) - 1
    assert n % 2 == 0
    return width / (3 * n) * (
        samples[0] + samples[-1]
        + 4 * sum(samples[1:-1:2]) + 2 * sum(samples[2:-1:2])
    )


def spectral_data(modes, quadrature):
    # Smooth nonnegative bump about -Y, supported at distance >=7*pi/8 from Y.
    eps = PI / 8
    rho = [eps * i / quadrature for i in range(quadrature + 1)]
    bump = [math.exp(-1 / (1 - (r / eps) ** 2)) if r < eps else 0.0 for r in rho]
    weights = [v * math.sin(r) for r, v in zip(rho, bump)]
    coeff = []
    # g(r)=sum c_k sin(kr)/sin(r); integrate in rho=pi-r to avoid endpoint loss.
    for k in range(1, modes + 1):
        parity = (-1) ** (k + 1)
        vals = [w * parity * math.sin(k * r) for r, w in zip(rho, weights)]
        coeff.append(2 / PI * simpson(vals, eps))
    positive_derivative = simpson([r * w for r, w in zip(rho, weights)], eps)
    return coeff, positive_derivative


def field(t, delta, coeff):
    return math.fsum(
        c * k * math.sin(t * math.sqrt(k * k + delta)) / math.sqrt(k * k + delta)
        for k, c in enumerate(coeff, 1)
    )


def derivative(t, coeff):
    return math.fsum(
        c * (t * math.cos(k * t) / (2 * k) - math.sin(k * t) / (2 * k * k))
        for k, c in enumerate(coeff, 1)
    )


def cos_integral(freq, t):
    return t if freq == 0 else math.sin(freq*t)/freq


def sin_integral(freq, t):
    return 0.0 if freq == 0 else (1-math.cos(freq*t))/freq


def dust_mode_derivative(k, t):
    # a_m=1, q(t)=(1-cos t)^2/4. Exact Duhamel integral, not RK time stepping.
    aa = (3/8, -1/2, 1/8)
    q0 = math.fsum(a*cos_integral(j, t) for j,a in enumerate(aa))
    qc = math.fsum(a/2*(cos_integral(2*k+j,t)+cos_integral(2*k-j,t)) for j,a in enumerate(aa))
    qs = math.fsum(a/2*(sin_integral(2*k+j,t)+sin_integral(2*k-j,t)) for j,a in enumerate(aa))
    return (math.cos(k*t)*(q0-qc)-math.sin(k*t)*qs)/(2*k*k)


def run():
    tau = PI / 4
    s = tau / 2
    target = 2 * PI - s
    c1, positive1 = spectral_data(256, 4096)
    c2, positive2 = spectral_data(512, 8192)
    assert tau < target < 2 * PI
    assert 7 * PI / 8 > tau
    assert positive2 > 0
    d_target = derivative(target, c2)
    d_period = derivative(2 * PI, c2)
    assert abs(d_target - positive2) < 1e-9
    assert abs(d_period - positive2) < 1e-9
    assert abs(d_target - derivative(target, c1)) < 1e-8
    assert abs(positive1 - positive2) < 1e-10
    unperturbed = field(target, 0, c2)
    # Finite truncation only approximates the analytically exact zero.
    assert abs(unperturbed) < 1e-9
    perturbed = []
    for delta in (-0.001, 0.001, 0.0001):
        value = field(target, delta, c2)
        assert value * delta > 0
        quotient = (value - unperturbed) / delta
        assert abs(quotient - positive2) / positive2 < 0.02
        perturbed.append({"delta": delta, "value": value, "difference_quotient": quotient})
    # Independent Green-kernel normalization: integrate G(r) over the sphere.
    # This must be 1 because (-Delta+1)^(-1) takes the constant 1 to itself.
    n = 4096
    rr = [PI * i / n for i in range(n + 1)]
    normalization = simpson([(PI-r)*math.sin(r)/PI for r in rr], PI)
    assert abs(normalization - 1) < 1e-10
    # Distinct physical-dust-mass model: verify mode integrals independently.
    dust_modes = []
    for k in (1, 2, 7):
        t = 2*PI
        expected = 5*PI/16 if k == 1 else 3*PI/(8*k*k)
        quad = simpson([((1-math.cos(u))**2/4)*math.sin(k*u)**2/(k*k) for u in [t*i/8192 for i in range(8193)]], t)
        direct = dust_mode_derivative(k,t)
        assert abs(quad-expected) < 1e-12
        assert abs(direct-expected) < 1e-12
        # Also check the sign and integral away from the period.
        t = target
        quad_target = simpson([-((1-math.cos(u))**2/4)*math.sin(k*(t-u))*math.sin(k*u)/(k*k) for u in [t*i/8192 for i in range(8193)]], t)
        assert abs(dust_mode_derivative(k,t)-quad_target) < 1e-11
        dust_modes.append({"k":k,"period_integral":quad,"expected":expected})
    dust_derivative = math.fsum(c*k*dust_mode_derivative(k,target) for k,c in enumerate(c2,1))
    dust_coarse = math.fsum(c*k*dust_mode_derivative(k,target) for k,c in enumerate(c1,1))
    dust_period = math.fsum(c*k*dust_mode_derivative(k,2*PI) for k,c in enumerate(c2,1))
    assert dust_derivative > 0 and dust_period > 0
    assert abs(dust_derivative-dust_coarse) < 1e-8
    return {
        "status": "pass",
        "tau_over_pi": 0.25,
        "target_over_pi": target / PI,
        "positive_resolvent_derivative": positive2,
        "spectral_derivative_at_target": d_target,
        "spectral_derivative_at_full_period": d_period,
        "unperturbed_truncation_residual": unperturbed,
        "perturbed_samples": perturbed,
        "green_kernel_integral": normalization,
        "ordinary_dust_mass": {"am":1,"derivative_at_target":dust_derivative,"derivative_at_period":dust_period,"independent_mode_integrals":dust_modes},
        "convergence": {"coarse_modes":256,"fine_modes":512,"coarse_quadrature":4096,"fine_quadrature":8192},
        "scope": "bounded quadrature/spectral controls; past agreement and nonzero interval proved analytically, not by finite truncation",
    }


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
    Path(__file__).with_name("verification.json").write_text(json.dumps(result, indent=2) + "\n")
