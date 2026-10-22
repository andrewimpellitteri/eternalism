"""Small exact checks for the chosen readout model, not a detector experiment."""
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product

L = 1000
ZERO, ONE = (F(0), F(0)), (F(1), F(0))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def conj(a):
    return a[0], -a[1]


def norm2(a):
    return a[0]**2+a[1]**2


def summed(items):
    answer = ZERO
    for item in items:
        answer = add(answer, item)
    return answer


def ideals(c):
    return [p for p in range(1 << len(c))
            if all(not (p >> j & 1) or row & p == row for j, row in enumerate(c))]


def induce(c, p):
    old = [j for j in range(len(c)) if p >> j & 1]
    return tuple(sum(1 << k for k, v in enumerate(old) if c[j] >> v & 1) for j in old)


def q(c, model):
    if not c:
        return ONE
    if len(c) == 1:
        return F(1, 2), F(0)
    assert len(c) == 2
    return F(3, 20), F(-1 if c[1] and model == 'B' else 1, 5)


@lru_cache(None)
def w(c, model):
    value = q(c, model)
    d = norm2(value)
    f = value[0]/d, -value[1]/d
    proper = summed(w(induce(c, p), model) for p in ideals(c)[:-1])
    return f[0]-proper[0], f[1]-proper[1]


def amplitude(c, model):
    answer = ONE
    for n, p in enumerate(c):
        answer = mul(answer, mul(q(c[:n], model), w(induce(c[:n], p), model)))
    return answer


def maxima(c):
    below = 0
    for row in c:
        below |= row
    return len(c)-below.bit_count()


def reference(c):
    answer = F(1)
    for n, p in enumerate(c):
        past = induce(c[:n], p)
        answer *= F(L-1, L)**maxima(past) * F(1, L)**(n-len(past))
    return answer


def canonical(c):
    edges = [(a,b) for b,row in enumerate(c) for a in range(b) if row >> a & 1]
    return min(tuple(sorted((p[a],p[b]) for a,b in edges)) for p in permutations(range(len(c))))


def run():
    level = [c for c in product(range(1),range(2),range(4))
             if all(not (c[k] >> j & 1) or c[j] & c[k] == c[j]
                    for k in range(3) for j in range(k))]
    assert len(level) == 7
    ref = [reference(c) for c in level]
    assert all(p > 0 for p in ref) and sum(ref) == 1
    amps = {model:[amplitude(c,model) for c in level] for model in 'AB'}
    norms = {model:[norm2(a) for a in amps[model]] for model in 'AB'}
    assert norms['A'] == norms['B']
    assert summed(amps['A']) == summed(amps['B']) == ONE
    k3 = sum(v/p for v,p in zip(norms['A'],ref))
    assert k3 > 1
    pointer = {model:[v/(p*k3) for v,p in zip(norms[model],ref)] for model in 'AB'}
    assert pointer['A'] == pointer['B'] and sum(pointer['A']) == 1
    event = [i for i,c in enumerate(level) if c.count(0) == 2]
    assert len(event) == 4
    pe = sum(ref[i] for i in event)
    a = {model:summed(amps[model][i] for i in event) for model in 'AB'}
    assert a == {'A':(F(1,2),F(0)), 'B':(F(1,2),F(-1,5))}
    coherent, dephased = {}, {}
    for model in 'AB':
        direct = summed(mul(conj(amps[model][i]),amps[model][j])
                        for i in event for j in event)
        assert direct[1] == 0 and direct[0] == norm2(a[model])
        coherent[model] = direct[0]/(k3*pe)
        dephased[model] = sum(norms[model][i] for i in event)/(k3*pe)
        assert 0 <= coherent[model] <= 1 and 0 <= dephased[model] <= 1
    assert coherent['B']-coherent['A'] == F(1,25)/(k3*pe) > 0
    assert dephased['A'] == dephased['B']
    assert norm2(summed(conj(amps['A'][i]) for i in event)) == norm2(a['A'])
    # Extra L2 existence condition; these exact constants are used analytically.
    h3 = L**2*9+4*3*8
    assert F(h3,(L-1)**3) < F(1,100)
    s1 = lambda x:x/(1-x)**2-x-2*x*x
    s2 = lambda x:x*(1+x)/(1-x)**3-x-4*x*x
    z = L**2*s2(F(2,L))+4*s1(F(4,L))+4*s1(F(1,L))
    assert 3*z < F(3,8) < 1
    # NC1 exponent criterion is analytic, not a numerical integration test.
    alpha = F(3,4)
    assert 0 < alpha < 1 and 2*alpha > 1
    # NC3: normalized scalar amplitudes do not define additive probabilities.
    assert 2*F(1,2)**2 != 1
    # NC4: same completed finite order, different first-three minimum counts.
    c1,c2 = (0,0,1,0),(0,0,0,1)
    assert canonical(c1) == canonical(c2)
    assert c1[:3].count(0) == 2 and c2[:3].count(0) == 3
    assert c1.count(0) == c2.count(0) == 3
    # No prefix with two minima can exclude a later third minimum.
    prefix = (0,0,1)
    assert prefix.count(0) == 2
    assert (prefix+((1<<len(prefix))-1,)).count(0) == 2
    assert (prefix+(0,)).count(0) == 3
    return {
        'status':'PASS', 'domain':'finite depth-three chosen Hilbert readout',
        'cylinders':len(level), 'E2_prefix_cylinders':len(event),
        'K3':str(k3), 'P0_prefix_E2':str(pe),
        'pointer_probabilities_identical':True,
        'coherent_probabilities':{m:str(coherent[m]) for m in 'AB'},
        'coherent_gap':str(coherent['B']-coherent['A']),
        'coherent_gap_not_raw_quantum_measure_gap':coherent['B']-coherent['A'] != F(1,25),
        'dephasing_removes_distinction':True,
        'global_conjugation_control_preserves_coherent_probability':True,
        'L2_bound_constants_checked':True,
        'finite_prefix_decision_obstruction':True,
        'analytic_controls':'NC1 L1/L2 and NC2 quotient arguments remain analytic, not empirically scored',
        'limits':'No physical preparation, access, full covariance, novelty or ontology established.'
    }


if __name__ == '__main__':
    result = run()
    if '--json' in sys.argv:
        print(json.dumps(result,indent=2))
    else:
        for key,value in result.items():
            print(f'{key}: {value}')
