"""Exact formal-radical and outward-interval checks of the diffuse pair.

Reuses the reviewed dyadic interval / poset utilities from the predecessor
at c6d31f5; no dependency installs and no writes to that lane. Formal linear
radical coefficients certify finite weight cancellation and independent
Mobius-vs-recursive inversion. Interval residuals are consistency checks;
RESULT.md supplies exact all-stage identities and measure extension.
"""
import hashlib
import importlib.util
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

sys.dont_write_bytecode = True
HELPER = Path(__file__).resolve().parent.parent / 'bc-matched-norms' / 'check.py'
spec = importlib.util.spec_from_file_location('bc_matched_checked_support', HELPER)
support = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = support
spec.loader.exec_module(support)
I, Z, ZERO, ONE, GRID = support.I, support.Z, support.ZERO, support.ONE, support.GRID
ideals, induce = support.ideals, support.induce
canonical, enumerate_posets = support.canonical, support.enumerate_posets
zsum, residual = support.zsum, support.residual
L = 1000


# Linear real radical forms: key None denotes 1; (n,c) denotes
# sqrt(25 L^(2n)-256 c^2). Imaginary parts remain exact rational numbers.
def form_add(a, b, sign=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + sign * value
        if not out[key]:
            del out[key]
    return out


def zform_add(a, b, sign=1):
    return form_add(a[0], b[0], sign), a[1] + sign * b[1]


@lru_cache(None)
def chain_count(c):
    actual = sum(p.bit_count() == 2 and induce(c, p) == (0, 1) for p in ideals(c))
    # Different combinatorial calculation: each upper vertex has one ancestor.
    assert actual == sum(row.bit_count() == 1 for row in c)
    assert actual <= len(c)
    return actual


@lru_cache(None)
def f_form(c, model):
    n = len(c)
    if n <= 2:
        q = support.early_q(c, model)
        d = support.gnorm2(q)
        return {None: q[0] / d}, -q[1] / d
    count = chain_count(c)
    h = F(-16 * count, 5)
    assert L**n >= 16 * n > abs(h)
    real = {(n, count): F(1, 5)} if count else {None: F(L**n)}
    return real, h if model == 'A' else -h


@lru_cache(None)
def w_recursive(c, model):
    result = f_form(c, model)
    for p in ideals(c)[:-1]:
        result = zform_add(result, w_recursive(induce(c, p), model), -1)
    return result


@lru_cache(None)
def w_mobius(c, model):
    below = 0
    for row in c:
        below |= row
    maxima = [j for j in range(len(c)) if not (below >> j & 1)]
    result = {}, F(0)
    full = (1 << len(c)) - 1
    for bits in range(1 << len(maxima)):
        keep = full
        for j, vertex in enumerate(maxima):
            if bits >> j & 1:
                keep ^= 1 << vertex
        result = zform_add(result, f_form(induce(c, keep), model), (-1)**bits.bit_count())
    return result


@lru_cache(None)
def radical(n, count):
    d = 25 * L**(2*n) - 256 * count**2
    assert d > 0
    return I.of(d).sqrt()


def evaluate(form):
    real = I.of(0)
    for key, value in form[0].items():
        real = real + (I.of(1) if key is None else radical(*key)) * value
    return Z(real, I.of(form[1]))


@lru_cache(None)
def w(c, model):
    return evaluate(w_recursive(c, model))


@lru_cache(None)
def q(c, model):
    f = evaluate(f_form(c, model))
    if len(c) <= 2:
        return Z.of(*support.early_q(c, model))
    r2 = F(L**(2*len(c)))
    f.norm2().tight(r2)
    # Exact reciprocal from the independently checked |f|^2 identity.
    return Z(f.re / r2, -f.im / r2)


def transition(c, p, model):
    return q(c, model) * w(induce(c, p), model)


@lru_cache(None)
def amplitude(c, model):
    return ONE if not c else amplitude(c[:-1], model) * transition(c[:-1], c[-1], model)


def maxima_count(c):
    below = 0
    for row in c:
        below |= row
    return len(c) - below.bit_count()


def w0(c):
    return F(L**len(c)) * F(L-1, L)**maxima_count(c)


def H(n):
    return L**2*n*n + 4*n*2**n


def zeta(n):
    return L**2*n*n*F(2, L)**n + 4*n*F(4, L)**n + 4*n*F(1, L)**n


def norm_signature(c):
    # Norm factors independent of the birth order. Later w factors are the
    # exact common formal-radical weights, represented by induced shape.
    rational, later = F(1), Counter()
    for j in range(len(c)):
        rational *= (support.gnorm2(support.early_q(c[:j], 'A'))
                     if j <= 2 else F(1, L**(2*j)))
        past = induce(c, c[j])
        if len(past) <= 2:
            wa = support.early_w(past, 'A')
            wb = support.early_w(past, 'B')
            assert support.gnorm2(wa) == support.gnorm2(wb)
            rational *= support.gnorm2(wa)
        else:
            later[(len(past), canonical(past))] += 1
    return rational, tuple(sorted(later.items()))


def decimal(i, digits=18):
    scale = 10**digits
    low = i.lo * scale // GRID
    high = support.ceildiv(i.hi * scale, GRID)
    def fmt(x):
        sign = '-' if x < 0 else ''
        a, b = divmod(abs(x), scale)
        return f'{sign}{a}.{b:0{digits}d}'
    return '[' + fmt(low) + ', ' + fmt(high) + ']'


def expanded(z, error):
    # The square containing an error disk is a conservative enclosure.
    bound = I.of(error).hi
    return Z(I(z.re.lo-bound, z.re.hi+bound), I(z.im.lo-bound, z.im.hi+bound))


def main():
    support.arithmetic_audit()
    print('Support SHA256:', hashlib.sha256(HELPER.read_bytes()).hexdigest())
    levels = [tuple(enumerate_posets(n)) for n in range(6)]
    assert [len(level) for level in levels] == [1, 1, 2, 7, 40, 357]
    print('Direct labelled counts:', [len(level) for level in levels])
    rows = transitions = pairs = 0
    for n, level in enumerate(levels):
        signatures, representatives = {}, {}
        for c in level:
            for model in 'AB':
                assert w_recursive(c, model) == w_mobius(c, model)
                assert w(c, model).norm2().lo > 0
                perturb = w(c, model) - Z.of(w0(c))
                upper = perturb.norm2().sqrt().hi
                assert F(upper, GRID) <= H(n) if n else perturb == ZERO
                if n >= 3:
                    assert H(n) < (L-1)**n <= w0(c)
                    assert w(c, model).norm2().hi < L**(2*n)*GRID
            if n >= 3:
                assert w_recursive(c, 'A') == w_recursive(c, 'B')
                # f_A-f_B is exactly the seed-chain ideal multiplicity.
                difference = zform_add(f_form(c, 'A'), f_form(c, 'B'), -1)
                assert difference == ({}, F(-32 * chain_count(c), 5))
            aa, ab = amplitude(c, 'A'), amplitude(c, 'B')
            residual(Z(aa.norm2()-ab.norm2(), I.of(0)))
            key, signature = canonical(c), norm_signature(c)
            if key in signatures:
                assert signatures[key] == signature
                for model in 'AB':
                    assert w_recursive(c, model) == w_recursive(representatives[key], model)
            signatures[key], representatives[key] = signature, c
        print(f'n={n}: exact recursive/Mobius weights, common later weights, '
              f'nonzero, norm match and {len(signatures)} shape classes pass.')
        if n > 4:
            continue
        for c in level:
            ps = ideals(c)
            reference = [w0(induce(c, p))/L**n for p in ps]
            assert sum(reference) == 1
            if n:
                assert max(reference) <= F(L-1, L)
            for model in 'AB':
                row = [transition(c, p, model) for p in ps]
                assert all(t.norm2().lo > 0 for t in row)
                residual(zsum(row)-ONE)
                if n >= 3:
                    distance = sum(F((t-Z.of(p0)).norm2().sqrt().hi, GRID)
                                   for t, p0 in zip(row, reference))
                    assert distance <= zeta(n)
                for j, p in enumerate(ps):
                    for other in ps[j+1:]:
                        both = p | other
                        b = induce(c, both)
                        vertices = [k for k in range(n) if both >> k & 1]
                        pb = sum(1 << k for k, v in enumerate(vertices) if p >> v & 1)
                        ob = sum(1 << k for k, v in enumerate(vertices) if other >> v & 1)
                        residual(transition(c, p, model)*transition(b, ob, model)
                                 - transition(c, other, model)*transition(b, pb, model))
            rows += 1
            transitions += len(ps)
            pairs += len(ps)*(len(ps)-1)//2
    print(f'Per model: {rows} MSR rows, {transitions} nonzero transitions, '
          f'{pairs} BC pair residual enclosures (parents through size 4).')
    S1 = lambda x: x/(1-x)**2-x-2*x*x
    S2 = lambda x: x*(1+x)/(1-x)**3-x-4*x*x
    total_zeta = L**2*S2(F(2,L))+4*S1(F(4,L))+4*S1(F(1,L))
    assert total_zeta < F(1, 8)
    print('Exact infinite row-distance sum:', total_zeta)
    print('Row-distance sum enclosure:', decimal(I.of(total_zeta)), '< 1/8.')
    assert zeta(4) < F(1, 2*L)
    print('For n>=4: each transition modulus < 1999/2000; fixed-path amplitudes decay.')
    assert H(3) < (L-1)**3 and H(4) < F(L**4,L)
    assert F(4,3)**2 < L-1 and F(4,3)*2 < L-1
    assert F(5,4)**2 < L and F(5,4)*2 < L
    tau = F(16, 7*L**2*(L-1))
    assert tau < F(1, 10**8)
    lower = F(1,25)-F(11,5)*tau-2*tau*tau
    assert lower > F(399999, 10000000)
    print('Global E2 amplitude tail <=', tau)
    print('Global completed E2 gap > 399999/10000000.')
    # Early sums, minimum-count increments and completed-value intervals.
    sums = {}
    for model in 'AB':
        gaussian = sum(sum(abs(x) for x in support.exact_early_amplitude(c, model))
                       for c in levels[3])
        assert gaussian == 2
        expected = Z.of(F(1,2), 0 if model == 'A' else F(-1,5))
        sums[model] = []
        for n in (3,4,5):
            val = zsum(amplitude(c, model) for c in levels[n] if c.count(0) == 2)
            sums[model].append(val)
            if n == 3:
                residual(val-expected)
            if n < 5:
                flow = zsum((amplitude(c, model)*q(c, model)).scale(
                    int(c.count(0)==1)-int(c.count(0)==2)) for c in levels[n])
                nxt = zsum(amplitude(c, model) for c in levels[n+1] if c.count(0)==2)
                residual(nxt-val-flow)
        error5 = F(16, 7*L**4*(L-1))
        completed = expanded(sums[model][-1], error5).norm2()
        sums[model].append(completed)
        print(f'Completed mu_{model}(E2) enclosure from depth 5:', decimal(completed))
    completed_gap = sums['B'][-1]-sums['A'][-1]
    assert F(completed_gap.lo, GRID) > F(399999,10000000)
    print('Completed gap enclosure:', decimal(completed_gap))
    # Naive real tail fails at the first parent containing both early shapes.
    # Its size-three cp weights differ in squared norm by (32/5)^2.
    naive_a = (F(L**3)-F(14,5), F(32,5))
    naive_b = (F(L**3)-F(14,5), F(0))
    assert support.gnorm2(naive_a)-support.gnorm2(naive_b) == F(1024,25)
    print('Naive shared-real tail killed: cp weight-square mismatch = 1024/25.')
    print('PASS. Atomlessness and all-stage claims use the analytic proof, not this cutoff.')


if __name__ == '__main__':
    main()
