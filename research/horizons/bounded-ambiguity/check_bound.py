"""Bounded independent ODE controls for the analytical bound in RESULT.md."""
import json
import math
from pathlib import Path


def mode_difference(k, lam, t_end, steps, potential):
    # Integrate the difference equation directly, avoiding subtraction of two
    # rapidly oscillating approximate solutions and its phase-error artefact.
    dt = t_end / steps
    z = (0.0, 0.0, 0.0, 0.0)

    def rhs(t, state):
        dc, vc, ds, vs = state
        v = lam * potential(t)
        return (vc, -(k*k+v)*dc-v*math.cos(k*t),
                vs, -(k*k+v)*ds-v*math.sin(k*t)/k)

    def add(a, b, factor):
        return tuple(x+factor*y for x,y in zip(a,b))

    for i in range(steps):
        t = i*dt
        a = rhs(t,z)
        b = rhs(t+dt/2,add(z,a,dt/2))
        c = rhs(t+dt/2,add(z,b,dt/2))
        d = rhs(t+dt,add(z,c,dt))
        z = tuple(x+dt*(aa+2*bb+2*cc+dd)/6 for x,aa,bb,cc,dd in zip(z,a,b,c,d))
    return z[0],z[2]


def run():
    # Independent reference: constant-potential solutions are explicit.
    t = 1.3
    for k in (1,3,9):
        lam = 0.2
        dc,ds = mode_difference(k,lam,t,2048,lambda _:1.0)
        omega = math.sqrt(k*k+lam)
        assert abs(dc-(math.cos(omega*t)-math.cos(k*t))) < 1e-9
        assert abs(ds-(math.sin(omega*t)/omega-math.sin(k*t)/k)) < 1e-9
    assert mode_difference(2,0,1.0,32,lambda _:1.0)==(0.0,0.0)
    # S^3 dimension check, including the constant mode.
    for n in range(10):
        count=math.comb(n+3,3)-(math.comb(n+1,3) if n>=2 else 0)
        assert count==(n+1)**2

    t=15*math.pi/8
    q=lambda u:(1-math.cos(u))**2/4
    Q=(1.5*t-2*math.sin(t)+math.sin(2*t)/4)/4
    outcomes=[]
    for lam in (0.001,0.01,0.1):
        B=lam*Q*math.exp(lam*Q)
        squared_norm=0.0
        max_mode_ratio=0.0
        convergence=0.0
        for k in range(1,25):
            dc,ds=mode_difference(k,lam,t,4096,q)
            coarse=mode_difference(k,lam,t,2048,q)
            convergence=max(convergence,abs(dc-coarse[0]),abs(ds-coarse[1]))
            assert abs(dc)<=B/k+1e-9
            assert abs(ds)<=B/(k*k)+1e-9
            max_mode_ratio=max(max_mode_ratio,abs(dc)*k/B,abs(ds)*k*k/B)
            squared_norm+=k*k/(2*math.pi**2)*((dc/k)**2+ds**2)
        assert convergence<1e-7
        partial_norm=math.sqrt(squared_norm)
        all_mode_upper=B/math.sqrt(6)
        assert partial_norm<=all_mode_upper
        outcomes.append({'mass_squared':lam,'partial_point_functional_norm':partial_norm,
                         'analytical_all_mode_upper':all_mode_upper,
                         'largest_modal_bound_ratio':max_mode_ratio,
                         'max_coarse_fine_difference':convergence})
    return {'status':'pass','target_over_pi':t/math.pi,'Q':Q,
            'constant_potential_exact_controls':'passed; k=1,3,9',
            'zero_mass_control':'exact zero difference',
            'sphere_multiplicities':'checked n=0..9',
            'dust_checks':outcomes,'modes_checked':24,'fine_steps':4096,
            'scope':'bounded ODE and partial spectral controls; general upper bound and exact past agreement are analytical, not inferred from truncation'}


if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
