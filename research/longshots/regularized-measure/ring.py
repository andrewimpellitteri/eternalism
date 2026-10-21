"""Exact coefficient rings: Gaussian rationals and integer polynomials in p."""
from fractions import Fraction


class GQ:
    """Gaussian rational a + b i with Fraction parts."""
    __slots__ = ('re', 'im')

    def __init__(self, re, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)

    def _c(self, o):
        return o if isinstance(o, GQ) else GQ(o)

    def __add__(self, o):
        o = self._c(o); return GQ(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = self._c(o); return GQ(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return self._c(o) - self

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def __mul__(self, o):
        if isinstance(o, int):
            return GQ(self.re * o, self.im * o)
        o = self._c(o)
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def __eq__(self, o):
        o = self._c(o); return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __complex__(self):
        return complex(float(self.re), float(self.im))

    def __repr__(self):
        return f'GQ({self.re}, {self.im})'

    def str(self):
        return f'{self.re} + {self.im} i'

    @staticmethod
    def zero():
        return GQ(0)

    @staticmethod
    def one():
        return GQ(1)


class Poly:
    """Integer polynomial in p, coefficient list low->high."""
    __slots__ = ('c',)

    def __init__(self, c):
        c = list(c)
        while c and c[-1] == 0:
            c.pop()
        self.c = c

    def _c(self, o):
        return o if isinstance(o, Poly) else Poly([o])

    def __add__(self, o):
        o = self._c(o)
        n = max(len(self.c), len(o.c))
        a = self.c + [0] * (n - len(self.c))
        b = o.c + [0] * (n - len(o.c))
        return Poly([x + y for x, y in zip(a, b)])
    __radd__ = __add__

    def __neg__(self):
        return Poly([-x for x in self.c])

    def __sub__(self, o):
        return self + (-self._c(o))

    def __rsub__(self, o):
        return self._c(o) - self

    def __mul__(self, o):
        if isinstance(o, int):
            return Poly([x * o for x in self.c])
        o = self._c(o)
        if not self.c or not o.c:
            return Poly([])
        r = [0] * (len(self.c) + len(o.c) - 1)
        for i, x in enumerate(self.c):
            if x:
                for j, y in enumerate(o.c):
                    r[i + j] += x * y
        return Poly(r)
    __rmul__ = __mul__

    def __eq__(self, o):
        return self.c == self._c(o).c

    def iszero(self):
        return not self.c

    @staticmethod
    def zero():
        return Poly([])

    @staticmethod
    def one():
        return Poly([1])
