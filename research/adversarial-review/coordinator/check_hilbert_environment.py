"""Finite exact moment checks, not an infinite extension proof."""
from fractions import Fraction as F
from itertools import combinations, product
from check_boundaries import closure, stats, principal, mul, power


def law(x, y):
    t = y * y / (x * (1-x))
    assert 0 <= t <= 1
    return [(x, 1-t), (F(1), t*x), (F(0), t*(1-x))]


def main():
    for x, y in ((F(1,2), F(0)), (F(1,2), F(1,4)), (F(1,2), F(1,2)),
                 (F(1,3), F(1,6))):
        atoms = law(x, y)
        aa, bb = x*x+y*y, (1-x)**2+y*y
        assert sum(w for _, w in atoms) == 1
        assert sum(w*g for g,w in atoms) == x
        assert sum(w*g*g for g,w in atoms) == aa
        assert sum(w*(1-g)**2 for g,w in atoms) == bb
        checked = 0
        for n in range(1,5):
            pairs = list(combinations(range(n),2))
            orders = {closure([e for j,e in enumerate(pairs) if mask>>j&1],n)
                      for mask in range(1<<len(pairs))}
            for C in orders:
                covers = [e for e in C if not any((e[0],k) in C and (k,e[1]) in C
                                                  for k in range(e[0]+1,e[1]))]
                incomparable = [e for e in pairs if e not in C]
                L, h = stats(C,n)
                assert (L,h) == (len(covers),len(incomparable))
                forced = ['present']*L+['absent']*h
                moment = F(0)
                for configuration in product(atoms, repeat=len(forced)):
                    prob = conditional = F(1)
                    for (g,w),kind in zip(configuration,forced):
                        prob *= w
                        conditional *= g if kind=='present' else 1-g
                    moment += prob*conditional*conditional
                assert moment == aa**L*bb**h
                checked += 1
        print(f'p={x}+i*{y}: environment moments and {checked} cylinder squared norms exact')
    # Independently verify the squared-level cap formula at an exterior point.
    A, B = F(13,16), F(13,16)  # p=1/2+3i/4, outside the disk
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        orders={closure([e for j,e in enumerate(pairs) if mask>>j&1],n)
                for mask in range(1<<len(pairs))}
        total=F(0)
        for C in orders:
            previous=frozenset((i,j) for i,j in C if j<n-1)
            if principal(C,n) and principal(previous,n-1):
                L,h=stats(C,n);total+=A**L*B**h
        k=n-2;pairs2=list(combinations(range(k),2))
        bases={closure([e for j,e in enumerate(pairs2) if mask>>j&1],k)
               for mask in range(1<<len(pairs2))}
        capped=F(0)
        for G in bases:
            L,h=stats(G,k)
            maxima=sum(not any((i,j) in G for j in range(i+1,k)) for i in range(k))
            capped+=A*A**(L+maxima)*B**h
        assert total==capped
    print('Squared DP level identity exact through n=5 at an exterior point')
    # Same cylinder diagonals do not preserve a finite union's quantum measure.
    atoms = law(F(1,2), F(1,4))
    new_union = F(0)
    for (g01,w01),(g02,w02),(g12,w12) in product(atoms,repeat=3):
        chain = g01*g12  # the 0->2 edge is redundant
        antichain = (1-g01)*(1-g02)*(1-g12)
        new_union += w01*w02*w12*(chain+antichain)**2
    p,q = (F(1,2),F(1,4)),(F(1,2),F(-1,4))
    Achain,Aanti = power(p,2),power(q,3)
    combined = tuple(a+b for a,b in zip(Achain,Aanti))
    old_union = sum(v*v for v in combined)
    assert old_union == F(221,4096)
    assert new_union == F(669,4096)
    assert new_union-old_union == F(7,64)
    print('Finite-union scope witness: original Q=221/4096, new Q=669/4096; diagonal norm matching changes interference')


if __name__=='__main__':
    main()
