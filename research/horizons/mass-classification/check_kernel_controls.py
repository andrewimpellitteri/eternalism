"""Bounded exact-series/smeared-spectral controls, not a classification proof."""
import json
import math
from pathlib import Path

PI=math.pi


def simpson(fn,lo,hi,n):
    assert n%2==0
    step=(hi-lo)/n
    return step/3*(fn(lo)+fn(hi)+sum((4 if j%2 else 2)*fn(lo+j*step)
                                  for j in range(1,n)))


def radial_riemann_derivative(duration,r,c):
    # Differentiate the convergent exact J0 power series, without a Bessel
    # library or a finite-difference derivative near the characteristic.
    u=duration*duration-r*r
    if u==0:
        return c*r/2
    coefficient=1.0
    total=0.0
    for n in range(1,100):
        coefficient*=(-c/4)/(n*n)
        term=-2*r*n*coefficient*u**(n-1)
        total+=term
        if n>20 and abs(term)<1e-18:
            break
    return total


def kernel(duration,r,c):
    assert 0<r<PI and 0<duration<2*PI
    derivative=0.0
    if r<duration:
        derivative+=radial_riemann_derivative(duration,r,c)/2
    if 2*PI-r<duration:
        derivative-=radial_riemann_derivative(duration,2*PI-r,c)/2
    return -derivative/(2*PI*math.sin(r))


def bump(r,lo,hi):
    z=2*(r-lo)/(hi-lo)-1
    return math.exp(-1/(1-z*z)) if abs(z)<1 else 0.0


def coefficients(lo,hi,modes,n):
    return [2/PI*simpson(lambda r,k=k:bump(r,lo,hi)*math.sin(k*r)*math.sin(r),
                         lo,hi,n) for k in range(1,modes+1)]


def spectral_pairing(coeff,duration,c):
    return math.fsum(k*a*math.sin(duration*math.sqrt(k*k+c))/math.sqrt(k*k+c)
                     for k,a in enumerate(coeff,1))


def run():
    results=[]
    # A direct cone before caustic, and both cells after it. The datum is
    # strictly away from wavefronts, so the smooth tail integral is sufficient.
    for duration,lo,hi in [(1.4,0.35,0.95),(4.0,0.5,1.2),(4.0,2.45,3.0)]:
        coarse=coefficients(lo,hi,512,4096)
        fine=coefficients(lo,hi,1024,8192)
        for c in (0.0,0.1,1.0,3.0):
            reference=simpson(lambda r:4*PI*math.sin(r)**2*kernel(duration,r,c)
                              *bump(r,lo,hi),lo,hi,4096)
            value=spectral_pairing(fine,duration,c)
            old=spectral_pairing(coarse,duration,c)
            assert abs(value-reference)<1e-8,(duration,c,value,reference)
            assert abs(value-old)<1e-7,(duration,c,value,old)
            if c==0:
                assert reference==0.0
            results.append({'duration':duration,'support':[lo,hi],
                            'constant_potential':c,'kernel_pairing':reference,
                            'spectral_pairing':value,'absolute_error':abs(value-reference),
                            'spectral_and_quadrature_refinement':abs(value-old)})
    corner=[]
    for c in (0.1,1.0,3.0):
        limit=(c/2+c*c*PI*PI/8)/(2*PI)
        errors=[]
        for alpha in (0.04,0.02,0.01,0.005):
            value=kernel(PI+alpha,PI-alpha/2,c)
            errors.append(abs(value-limit))
        assert all(b<a for a,b in zip(errors,errors[1:])),(c,errors)
        assert errors[-1]<0.01*max(1,limit)
        corner.append({'constant_potential':c,'predicted_corner':limit,
                       'errors_for_alpha_004_002_001_0005':errors})
    return {'status':'pass','normalization_and_image_controls':results,
            'constant_potential_corner_controls':corner,
            'scope':'Exact constant-potential series against smooth-data spectral pairings. No claim of full dust support or exact past vanishing follows from truncation; classification depends on the analytic proof.'}


if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
