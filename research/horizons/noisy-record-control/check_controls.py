"""Independent radial quadrature controls; no numerical proof of uniqueness."""
import json
import math
from pathlib import Path

PI = math.pi
TARGET = 11 * PI / 6


def simpson(fn, lo, hi, steps):
    assert steps % 2 == 0
    h = (hi-lo)/steps
    return h/3 * (fn(lo)+fn(hi)+sum(
        (4 if i % 2 else 2)*fn(lo+i*h) for i in range(1,steps)))


def radial_norm(band, time, derivative=False, steps=1024):
    # The sin(r) in each zonal denominator cancels the radial volume factor.
    # This integrates the squared SUM, checking cross-mode cancellation.
    def integrand(r):
        total = 0.0
        for k in range(band,2*band):
            coefficient = (-math.sin(k*(time-TARGET)) if derivative else
                           math.cos(k*(time-TARGET))/k)/math.sqrt(band)
            total += coefficient*math.sin(k*r)
        return 2/PI*total*total
    return simpson(integrand,0,PI,steps)


def cap_overlap(k, ell, radius):
    if k == ell:
        return (radius-math.sin(2*k*radius)/(2*k))/PI
    return (math.sin((k-ell)*radius)/(k-ell)
            -math.sin((k+ell)*radius)/(k+ell))/PI


def restricted_gram(cutoff, steps):
    # Zonal subspace only: this bounded control is NOT the full harmonic Gram.
    labels = [(k,kind) for k in range(1,cutoff+1) for kind in (0,1)]
    tau = PI/3
    def phase(k,kind,t):
        return math.cos(k*t) if kind == 0 else math.sin(k*t)
    return [[simpson(lambda t: phase(k,a,t)*phase(ell,b,t)*
                     cap_overlap(k,ell,tau-t),0,tau,steps)
             for ell,b in labels] for k,a in labels]


def cholesky_pivots(matrix):
    n = len(matrix)
    lower = [[0.0]*n for _ in range(n)]
    pivots = []
    for i in range(n):
        for j in range(i+1):
            residual = matrix[i][j]-sum(lower[i][k]*lower[j][k] for k in range(j))
            if i == j:
                assert residual > 0, (i,residual)
                pivots.append(residual)
                lower[i][j] = math.sqrt(residual)
            else:
                lower[i][j] = residual/lower[j][j]
    return pivots


def run():
    controls = []
    for band in (4,8,16,32):
        max_error = 0.0
        for time in (0.23,1.17,TARGET):
            expected = sum(math.cos(k*(time-TARGET))**2/(band*k*k)
                           for k in range(band,2*band))
            actual = radial_norm(band,time)
            max_error = max(max_error,abs(actual-expected))
            expected_velocity = sum(math.sin(k*(time-TARGET))**2/band
                                    for k in range(band,2*band))
            assert abs(radial_norm(band,time,True)-expected_velocity) < 1e-11
            # Independently integrate the spatial gradient+position energy.
            weighted = simpson(lambda r: 2/PI*sum(
                math.cos(k*(time-TARGET))*math.sin(k*r)/math.sqrt(band)
                for k in range(band,2*band))**2,0,PI,1024)
            assert abs(weighted+radial_norm(band,time,True)-1) < 1e-11
        assert max_error < 1e-11
        full_record_sq = simpson(lambda t: sum(
            math.cos(k*(t-TARGET))**2/(band*k*k)
            for k in range(band,2*band)),0,2*PI,1024)
        exact_record_sq = PI/band*sum(1/(k*k) for k in range(band,2*band))
        assert abs(full_record_sq-exact_record_sq) < 1e-11
        target = sum(1/math.sqrt(2*PI*PI*band) for _ in range(band))
        assert abs(target-math.sqrt(band/(2*PI*PI))) < 1e-12
        # Constant averaging profile has zero overlap with all k>=2 bands.
        average = simpson(lambda r: 4*PI*sum(
            math.sin(k*r)*math.sin(r)/(k*math.sqrt(2*PI*PI*band))
            for k in range(band,2*band)),0,PI,1024)
        assert abs(average) < 1e-11
        controls.append({'band':band,'target_value':target,
                         'full_strip_record_norm':math.sqrt(full_record_sq),
                         'past_record_upper':math.sqrt(PI)/band,
                         'max_radial_norm_error':max_error})
    coarse = restricted_gram(3,512)
    fine = restricted_gram(3,1024)
    gram_error = max(abs(coarse[i][j]-fine[i][j]) for i in range(6) for j in range(6))
    assert gram_error < 1e-10
    pivots = cholesky_pivots(fine)
    return {'status':'pass','sequence_controls':controls,
            'zonal_cutoff':3,'zonal_gram_coarse_fine_max_error':gram_error,
            'zonal_gram_cholesky_pivots':pivots,
            'scope':'Radial quadrature and small zonal-subspace controls only; general statements are analytical. Cholesky is not an eigenvalue or cutoff-uniform conditioning bound.'}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('verification.json').write_text(json.dumps(result,indent=2)+'\n')
