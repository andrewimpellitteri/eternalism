"""Exact-rational check of the two-sided channel identity. Stdlib only; a check, not a proof.

Transport: q(t,x)=F(t-x/c) on [0,L], tau=L/c, inlet f(t)=F(t), outlet g(t)=F(t-tau).
Claim: y(t)=(1/L)*integral_0^L q(t,x) dx equals both
    (1/tau)*integral_0^tau f(t-s) ds   and   (1/tau)*integral_0^tau g(t+s) ds.
Each side is integrated separately, in its own variable, by an exact 9-point
Newton-Cotes rule, which is exact for the quartic F used here.
A wrong-side control, integral of f(t+s), must differ.
Also Q(t,x)=q(2b-t,L-x) is checked to equal q when F is palindromic about b-tau/2.
"""
from fractions import Fraction as Fr

NC = [Fr(989), Fr(5888), Fr(-928), Fr(10496), Fr(-4540), Fr(10496), Fr(-928), Fr(5888), Fr(989)]


def rule(h, a, b):
    """Integral of h over [a,b], exact for polynomials of degree at most 9."""
    d = (b - a) / 8
    return sum(w * h(a + d * i) for i, w in enumerate(NC)) * Fr(4, 14175) * d


def F(w):
    return Fr(3) - Fr(2, 7) * w + Fr(5, 3) * w ** 2 + Fr(1, 11) * w ** 3 - Fr(4, 5) * w ** 4


c, L = Fr(3, 2), Fr(9, 4)
tau = L / c
f = F
g = lambda t: F(t - tau)
for t in (Fr(0), Fr(5, 7), Fr(-13, 6), Fr(29, 3)):
    readout = rule(lambda x: F(t - x / c), Fr(0), L) / L
    past = rule(lambda s: f(t - s), Fr(0), tau) / tau
    future = rule(lambda s: g(t + s), Fr(0), tau) / tau
    wrong = rule(lambda s: f(t + s), Fr(0), tau) / tau
    assert readout == past == future
    assert wrong != past

b = Fr(2)
m = b - tau / 2
sym = lambda w: Fr(1) + (w - m) ** 2 - Fr(3, 5) * (w - m) ** 4
for t in (Fr(0), Fr(5, 7), Fr(11, 3)):
    for x in (Fr(0), Fr(1, 3), L):
        assert sym(t - x / c) == sym((2 * b - t) - (L - x) / c)
print("identities hold exactly at the sampled points; wrong-side control differs; tau =", tau)
