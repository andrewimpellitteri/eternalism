"""Bounded audit; analytic all-stage equalities are proved in RESULT.md.

No binary floats enter any decision. Circle coordinates generally contain
nested radicals: the later computation uses outward-rounded dyadic intervals,
not a claim of exact Gaussian-rational coordinates. Standard library only.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import isqrt

BITS = 256
GRID = 1 << BITS


def ceildiv(a, b):
    return -((-a) // b)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def of(x):
        if isinstance(x, I):
            return x
        x = F(x)
        return I(x.numerator * GRID // x.denominator,
                 ceildiv(x.numerator * GRID, x.denominator))

    def __add__(self, other):
        other = I.of(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I.of(other)

    def __mul__(self, other):
        other = I.of(other)
        ends = [a * b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return I(min(ends) // GRID, ceildiv(max(ends), GRID))

    __rmul__ = __mul__

    def inv(self):
        assert self.lo > 0 or self.hi < 0, "unresolved division by zero"
        return I(GRID * GRID // self.hi, ceildiv(GRID * GRID, self.lo))

    def __truediv__(self, other):
        return self * I.of(other).inv()

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(low // GRID, ceildiv(max(self.lo**2, self.hi**2), GRID))

    def sqrt(self):
        assert self.lo >= 0, "unresolved radicand sign"
        lower = isqrt(self.lo * GRID)
        upper = isqrt(self.hi * GRID)
        if upper * upper < self.hi * GRID:
            upper += 1
        return I(lower, upper)

    def contains(self, x):
        return F(self.lo, GRID) <= x <= F(self.hi, GRID)

    def tight(self, x):
        assert self.contains(x), (self, x)
        assert F(self.hi - self.lo, GRID) < max(abs(x), F(1, 10**60)) / 2**100


@dataclass(frozen=True)
class Z:
    re: I
    im: I

    @staticmethod
    def of(re=0, im=0):
        return Z(I.of(re), I.of(im))

    def __add__(self, other):
        return Z(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return Z(-self.re, -self.im)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Z(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def scale(self, r):
        return Z(self.re * r, self.im * r)

    def norm2(self):
        return self.re.square() + self.im.square()

    def inv(self):
        d = self.norm2()
        assert d.lo > 0
        return Z(self.re / d, -self.im / d)


ZERO, ONE = Z.of(), Z.of(1)


def zsum(xs):
    out = ZERO
    for x in xs:
        out = out + x
    return out


def residual(z):
    assert z.re.contains(0) and z.im.contains(0)
    assert max(z.re.hi - z.re.lo, z.im.hi - z.im.lo) < GRID // 2**100


@lru_cache(None)
def ideals(c):
    return tuple(p for p in range(1 << len(c))
                 if all(not (p >> j & 1) or row & p == row
                        for j, row in enumerate(c)))


@lru_cache(None)
def induce(c, subset):
    vertices = [j for j in range(len(c)) if subset >> j & 1]
    return tuple(sum(1 << k for k, v in enumerate(vertices) if c[j] >> v & 1)
                 for j in vertices)


def enumerate_posets(n):
    # Directly enumerate triangular relation masks; no growth-rule generator.
    for c in product(*(range(1 << j) for j in range(n))):
        if all(not (c[k] >> j & 1) or c[j] & c[k] == c[j]
               for k in range(n) for j in range(k)):
            yield c


@lru_cache(None)
def canonical(c):
    edges = [(a, b) for b, row in enumerate(c) for a in range(b) if row >> a & 1]
    return min(tuple(sorted((p[a], p[b]) for a, b in edges))
               for p in permutations(range(len(c))))


@lru_cache(None)
def radius(n):
    assert n >= 3
    bound = F(19, 5) if n == 3 else 2 * radius(n - 1)
    return 1 + 2**(2 * n + 10) * bound


def circle(s, r):
    if s == ZERO:
        return Z.of(r), Z.of(r)
    d = s.norm2()
    assert d.lo > 0, "S might contain zero: cannot choose a branch numerically"
    height2 = I.of(r * r) - d / 4
    assert height2.lo > 0
    rotated = Z(-s.im, s.re)
    f = s.scale(F(1, 2)) + rotated.scale(height2.sqrt() / d.sqrt())
    w = f - s
    f.norm2().tight(r * r)
    w.norm2().tight(r * r)
    return f, w


def early_q(c, model):
    if not c:
        return F(1), F(0)
    if len(c) == 1:
        return F(1, 2), F(0)
    assert len(c) == 2
    sign = -1 if c[1] and model == 'B' else 1
    return F(3, 20), F(sign, 5)


# Separate exact Gaussian-rational seed arithmetic.
def gadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def gmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gnorm2(a):
    return a[0]**2 + a[1]**2


@lru_cache(None)
def early_w(c, model):
    q = early_q(c, model)
    d = gnorm2(q)
    f = q[0] / d, -q[1] / d
    for p in ideals(c)[:-1]:
        wp = early_w(induce(c, p), model)
        f = f[0] - wp[0], f[1] - wp[1]
    return f


@lru_cache(None)
def rule(c, model):
    if len(c) <= 2:
        return Z.of(*early_q(c, model)), Z.of(*early_w(c, model))
    s = zsum(rule(induce(c, p), model)[1] for p in ideals(c)[:-1])
    f, w = circle(s, radius(len(c)))
    return f.inv(), w


def transition(c, p, model):
    return rule(c, model)[0] * rule(induce(c, p), model)[1]


@lru_cache(None)
def amplitude(c, model):
    return ONE if not c else amplitude(c[:-1], model) * transition(c[:-1], c[-1], model)


@lru_cache(None)
def exact_early_amplitude(c, model):
    if not c:
        return F(1), F(0)
    return gmul(exact_early_amplitude(c[:-1], model),
                gmul(early_q(c[:-1], model), early_w(induce(c[:-1], c[-1]), model)))


def predicted_norm2(c, model):
    # Independent intrinsic-past factorization, with exact rational norm factors.
    answer = F(1)
    for j in range(len(c)):
        parent = c[:j]
        past = induce(c, c[j])
        answer *= (gnorm2(early_q(parent, model)) if j <= 2 else 1 / radius(j)**2)
        answer *= (gnorm2(early_w(past, model)) if len(past) <= 2
                   else radius(len(past))**2)
    return answer


def arithmetic_audit():
    samples = [F(-17, 5), F(-1, 3), F(0), F(2, 7), F(11, 3), F(10**12, 3)]
    for x in samples:
        ix = I.of(x)
        assert ix.contains(x)
        ix.square().tight(x*x)
        if x:
            assert ix.inv().contains(1/x)
        for y in samples:
            assert (ix + I.of(y)).contains(x + y)
            assert (ix * I.of(y)).contains(x * y)
    for x in [F(0), F(2), F(1, 10**30), F(7, 3), F(10**24, 7)]:
        sx = I.of(x).sqrt()
        assert F(sx.lo, GRID)**2 <= x <= F(sx.hi, GRID)**2
    for s in [ZERO, Z.of(3, 4), Z.of(-3, 4), Z.of(0, -2)]:
        circle(s, F(10))
    print(f'Outward dyadic interval arithmetic: {BITS} bits; zero-S circle branch checked.')


def main():
    arithmetic_audit()
    levels = [tuple(enumerate_posets(n)) for n in range(6)]
    assert [len(x) for x in levels] == [1, 1, 2, 7, 40, 357]
    print('Direct triangular-mask labelled counts:', [len(x) for x in levels])
    rows, transitions, bell_pairs = 0, 0, 0
    for n, level in enumerate(levels):
        norms, shapes = {}, {}
        for c in level:
            a2 = predicted_norm2(c, 'A')
            assert a2 == predicted_norm2(c, 'B') > 0
            for model in 'AB':
                amplitude(c, model).norm2().tight(a2)
            key = canonical(c)
            if key in norms:
                assert norms[key] == a2
                if n <= 4:
                    for model in 'AB':
                        assert rule(c, model) == rule(shapes[key], model)
            norms[key], shapes[key] = a2, c
        print(f'n={n}: {len(level)} cylinder enclosures match exact squared-norm factors; '
              f'{len(norms)} isomorphism classes agree.')
        if n > 4:
            continue
        for c in level:
            ps = ideals(c)
            for model in 'AB':
                row = [transition(c, p, model) for p in ps]
                assert all(t.norm2().lo > 0 for t in row)
                residual(zsum(row) - ONE)
                if n >= 3:
                    e_upper = sum(F(t.norm2().sqrt().hi, GRID) for t in row[:-1])
                    assert e_upper < F(1, 2**(n + 10))
                    row[-1].norm2().tight(F(1))
                    # Critical padding estimate: timid phase stays close to 1.
                    assert F((row[-1] - ONE).norm2().sqrt().hi, GRID) < F(1, 2**(n + 10))
                for j, p in enumerate(ps):
                    for q in ps[j+1:]:
                        both = p | q
                        b = induce(c, both)
                        vertices = [v for v in range(n) if both >> v & 1]
                        pb = sum(1 << k for k, v in enumerate(vertices) if p >> v & 1)
                        qb = sum(1 << k for k, v in enumerate(vertices) if q >> v & 1)
                        residual(transition(c, p, model) * transition(b, qb, model)
                                 - transition(c, q, model) * transition(b, pb, model))
            rows += 1
            transitions += len(ps)
            bell_pairs += len(ps) * (len(ps) - 1) // 2
    print(f'Per model: {rows} MSR rows, {transitions} nonzero transitions, '
          f'{bell_pairs} scalar BC pair residuals enclosed (parents through size 4).')

    early = {}
    for model in 'AB':
        total, e2, gaussian = (F(0), F(0)), (F(0), F(0)), F(0)
        count_coefficients = {k: (F(0), F(0)) for k in (1, 2, 3)}
        for c in levels[3]:
            a = exact_early_amplitude(c, model)
            total = gadd(total, a)
            gaussian += abs(a[0]) + abs(a[1])
            k = c.count(0)
            count_coefficients[k] = gadd(count_coefficients[k], a)
            if c.count(0) == 2:
                e2 = gadd(e2, a)
        assert total == (1, 0) and gaussian == 2
        v = (F(3, 5), F(4 if model == 'A' else -4, 5))
        u = (F(3, 5), F(4, 5))
        assert count_coefficients == {
            1: ((4-v[0])/8, -v[1]/8),
            2: ((4+v[0]-u[0])/8, (v[1]-u[1])/8),
            3: (u[0]/8, u[1]/8),
        }
        early[model] = e2
    assert early == {'A': (F(1, 2), F(0)), 'B': (F(1, 2), F(-1, 5))}
    gap0 = gnorm2(early['B']) - gnorm2(early['A'])
    assert gap0 == F(1, 25)
    for model, expected in [('A', F(1, 16)), ('B', F(9, 400))]:
        union = gadd(exact_early_amplitude((0, 1, 0), model),
                     exact_early_amplitude((0, 0, 1), model))
        assert gnorm2(union) == expected
    print('Exact early E2 amplitudes:', early, '; squared-modulus gap B-A =', gap0)
    print('Full minimum-count polynomial checked: [(4-v)z+(4+v-u)z^2+uz^3]/8.')
    print('Two-cylinder union values A=1/16, B=9/400: stronger union data do NOT match.')

    sum_eps = F(1, 4096)
    variation_bound = F(2) / (1 - 2 * sum_eps)
    tau = 2 * variation_bound * sum_eps
    assert tau == F(2, 2047) < F(1, 1000)
    gap_lower = gap0 - F(11, 5) * tau - 2 * tau**2
    assert gap_lower > F(18899, 500000) > 0
    print('Global rational TV bound:', tau)
    print('Certified completed-event gap >=', gap_lower, '> 18899/500000 > 0.')
    for n in [4, 5]:
        vals = [zsum(amplitude(c, model) for c in levels[n] if c.count(0) == 2)
                for model in 'AB']
        # Finite-stage E2 event is used only as an approximant, not called covariant.
        gap = vals[1].norm2() - vals[0].norm2()
        assert gap.lo > 0
        print(f'n={n}: finite minimum-count gap is positive by rational enclosure.')
    print('PASS. Finite interval checks support, but do not replace, the analytic all-stage proof.')


if __name__ == '__main__':
    main()
