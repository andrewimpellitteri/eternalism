"""Exact recursion-versus-Mobius audit of the non-atomic-tail variant."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import comb

Z=(F(0),F(0));ONE=(F(1),F(0));D=F(1,10)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(r,a):return r*a[0],r*a[1]
def inv(a):
    v=a[0]**2+a[1]**2
    assert v
    return a[0]/v,-a[1]/v

def b(a):return abs(a[0])+abs(a[1])
def abs2(a):return a[0]**2+a[1]**2

def sumg(xs):
    s=Z
    for x in xs:s=add(s,x)
    return s

@lru_cache(None)
def ideals(C):return tuple(P for P in range(1<<len(C)) if all(not(P>>i&1) or C[i]&P==C[i] for i in range(len(C))))
@lru_cache(None)
def induce(C,P):
    old=[i for i in range(len(C)) if P>>i&1]
    return tuple(sum(1<<j for j,v in enumerate(old) if C[i]>>v&1) for i in old)

def maxima(C):
    below=0
    for row in C:below|=row
    return [i for i in range(len(C)) if not(below>>i&1)]

def q(C):
    n=len(C)
    if not n:return ONE
    if n==1:return F(1,2),F(0)
    if n==2:return (F(1,4),F(0)) if C[1] else (F(3,20),F(1,5))
    return D**n,F(0)

@lru_cache(None)
def recursive(C):
    return sub(inv(q(C)),sumg(recursive(induce(C,P)) for P in ideals(C) if P!=(1<<len(C))-1))

@lru_cache(None)
def mobius(C):
    ms=maxima(C);out=Z
    for bits in range(1<<len(ms)):
        keep=(1<<len(C))-1
        for j,v in enumerate(ms):
            if bits>>j&1:keep^=1<<v
        out=add(out,scale((-1)**bits.bit_count(),inv(q(induce(C,keep)))))
    return out

def w0(C):return D**(-len(C))*(1-D)**len(maxima(C))
def transition(C,P):return mul(q(C),recursive(induce(C,P)))
def t0(C,P):return (1-D)**len(maxima(induce(C,P)))*D**(len(C)-P.bit_count())

@lru_cache(None)
def canon(C):
    edges=[(j,i) for i,row in enumerate(C) for j in range(i) if row>>j&1]
    return min(tuple(sorted((p[j],p[i]) for j,i in edges)) for p in permutations(range(len(C))))

levels=[{():ONE}]
for n in range(5):
    nxt={}
    for C,a in levels[-1].items():
        for P in ideals(C):nxt[C+(P,)]=mul(a,transition(C,P))
    levels.append(nxt)
assert [len(x) for x in levels]==[1,1,2,7,40,357]
print('Labelled counts:',[len(x) for x in levels])
rows=0;bc=0
for n in range(6):
    for C in levels[n]:
        assert recursive(C)==mobius(C)!=Z
        perturb=b(sub(recursive(C),(w0(C),F(0))))
        bound=8*n+F(504,5)*comb(n,2)
        assert perturb<=bound
        if n>=3:assert w0(C)>=9**n>51*n*n>=perturb
    norms={}
    for C,a in levels[n].items():
        key=canon(C)
        if key in norms:assert norms[key]==abs2(a)
        else:norms[key]=abs2(a)
    print(f'n={n}: independent recursive/Mobius equality, perturbation bound, nonzero and norm-GC pass.')
    if n>4:continue
    rowmax=F(0)
    for C in levels[n]:
        ps=ideals(C)
        assert sumg(transition(C,P) for P in ps)==ONE
        assert sum(t0(C,P) for P in ps)==1
        assert all(transition(C,P)!=Z for P in ps)
        if n>=3:
            rowdist=sum(b(sub(transition(C,P),(t0(C,P),F(0)))) for P in ps)
            assert rowdist<=51*n*n/F(5**n)
            rowmax=max(rowmax,rowdist)
        for j,P in enumerate(ps):
            for Q in ps[j+1:]:
                B=induce(C,P|Q);old=[v for v in range(n) if (P|Q)>>v&1]
                Pb=sum(1<<k for k,v in enumerate(old) if P>>v&1)
                Qb=sum(1<<k for k,v in enumerate(old) if Q>>v&1)
                assert mul(transition(C,P),transition(B,Qb))==mul(transition(C,Q),transition(B,Pb))
                bc+=1
        rows+=1
    if n>=3:print(f'  exact maximum Gaussian row distance from reference={rowmax}; bound={51*n*n/F(5**n)}')

assert inv(q((0,)))==(F(2),F(0))
assert sub(inv(q((0,0))),(F(100),F(0)))==(F(-488,5),F(-16,5))
x=F(1,5)
zeta_sum=51*(x*(1+x)/(1-x)**3-x-4*x*x)
assert zeta_sum==F(4437,800)
print('Exact summable row-distance series:',zeta_sum)
key=canon((0,1,0));cp=[C for C in levels[3] if canon(C)==key]
ratios=[mul(levels[3][C],inv(levels[3][cp[0]])) for C in cp]
assert len(set(ratios))==2
for n in [4,5]:
    tops=[]
    for C in cp:
        while len(C)<n:C=C+((1<<len(C))-1,)
        tops.append(C)
    assert [mul(levels[n][C],inv(levels[n][tops[0]])) for C in tops]==ratios
print('Persistent cp phase:',ratios)
print('All',rows,'rows and',bc,'BC equations pass; 407 finite transitions nonzero.')
print('PASS: finite corroboration of the L1 construction; non-atomic completion is analytic, not simulated.')
