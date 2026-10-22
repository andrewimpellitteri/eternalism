"""Exact finite corroboration of the analytic all-stage construction.

No worker/seed imports. All down-set subsets and isomorphism permutations are
counted explicitly through five births. Mathematical infinity is proved in RESULT.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations

Z=(F(0),F(0));ONE=(F(1),F(0))

def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[0],a[1]-b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def inv(a):
    d=a[0]*a[0]+a[1]*a[1]
    assert d
    return a[0]/d,-a[1]/d

def norm2(a):return a[0]**2+a[1]**2
def ell1(a):return abs(a[0])+abs(a[1])
def gsum(xs):
    out=Z
    for x in xs:out=plus(out,x)
    return out

@lru_cache(None)
def downsets(C):
    return tuple(D for D in range(1<<len(C)) if all(not(D>>i&1) or C[i]&D==C[i] for i in range(len(C))))

@lru_cache(None)
def induced(C,D):
    old=[i for i in range(len(C)) if D>>i&1]
    return tuple(sum(1<<j for j,v in enumerate(old) if C[i]>>v&1) for i in old)

B={2:F(19,5)}
R={}
for n in range(3,9):
    R[n]=1+4**n*B[n-1]
    B[n]=1+(4**n+2**n)*B[n-1]

@lru_cache(None)
def q(C):
    n=len(C)
    if not n:return ONE
    if n==1:return F(1,2),F(0)
    if n==2:return (F(1,4),F(0)) if C[1] else (F(3,20),F(1,5))
    return 1/R[n],F(0)

@lru_cache(None)
def w(C):
    full=(1<<len(C))-1
    return minus(inv(q(C)),gsum(w(induced(C,D)) for D in downsets(C) if D!=full))

def t(C,D):return mul(q(C),w(induced(C,D)))

@lru_cache(None)
def canonical(C):
    edges=[(j,i) for i,row in enumerate(C) for j in range(i) if row>>j&1]
    return min(tuple(sorted((p[j],p[i]) for j,i in edges)) for p in permutations(range(len(C))))

lev=[{():ONE}]
for n in range(5):
    nxt={}
    for C,a in lev[n].items():
        for D in downsets(C):
            child=C+(D,)
            assert child not in nxt
            nxt[child]=mul(a,t(C,D))
    lev.append(nxt)
assert [len(x) for x in lev]==[1,1,2,7,40,357]
assert w(())==ONE and w((0,))==ONE
assert w((0,1))==(F(2),F(0)) and w((0,0))==(F(-3,5),F(-16,5))
assert sum(map(ell1,lev[3].values()))==F(8,5)
print('Labelled counts:',[len(x) for x in lev])
print('Exact seed Gaussian norm at level 3: 8/5')
checks=0;transitions=0
for n in range(5):
    max_proper=F(0)
    for C in lev[n]:
        ds=downsets(C);full=(1<<n)-1
        assert gsum(t(C,D) for D in ds)==ONE
        assert w(C)!=Z
        if n>=3:assert ell1(w(C))<=B[n]
        for D in ds:
            assert t(C,D)!=Z
            transitions+=1
        if n>=3:
            proper=sum((ell1(t(C,D)) for D in ds if D!=full),F(0))
            assert proper<F(1,2**n)
            assert ell1(minus(t(C,full),ONE))<=proper
            max_proper=max(max_proper,proper)
        for i,P in enumerate(ds):
            for Q in ds[i+1:]:
                union=P|Q
                parent=induced(C,union)
                old=[j for j in range(n) if union>>j&1]
                Pb=sum(1<<j for j,v in enumerate(old) if P>>v&1)
                Qb=sum(1<<j for j,v in enumerate(old) if Q>>v&1)
                assert mul(t(C,P),t(parent,Qb))==mul(t(C,Q),t(parent,Pb))
                checks+=1
    norms={};weights={}
    for C,a in lev[n+1].items():
        key=canonical(C)
        if key in norms:assert norms[key]==norm2(a)
        else:norms[key]=norm2(a)
        if key in weights:assert weights[key]==w(C)
        else:weights[key]=w(C)
        # Independent product over intrinsic element-pasts.
        past_prod=ONE;qprod=ONE
        for i in range(len(C)):
            past_prod=mul(past_prod,w(induced(C,C[i])))
            qprod=mul(qprod,q(C[:i]))
        assert a==mul(past_prod,qprod)
    print(f'Parent size {n}: MSR, nonzero, BC pass; next-level norm-GC and intrinsic product pass ({len(norms)} classes).')
    if n>=3:print(f'  q_{n}={q(next(iter(lev[n])))[0]}; max proper Gaussian sum={max_proper} < 2^-{n}')
print('Cumulative exact BC equations:',checks,'; nonzero transitions:',transitions)

# Exact two-successive-atomic-measure difference on a common finite refinement.
# At depth n+1, the old nu_n assigns A(C) to the timid child only. The padded
# infinite paths are distinct on this refinement, so no hidden support collision.
for n in [3,4]:
    delta={}
    for C,a in lev[n].items():
        for D in downsets(C):
            child=C+(D,)
            old=a if D==(1<<n)-1 else Z
            delta[child]=minus(lev[n+1][child],old)
    # Norm2 plus ell1 are exact; ell1 majorizes the TV norm, and the same
    # triangle estimate is checked per parent without taking irrational roots.
    local=F(0)
    for C,a in lev[n].items():
        proper=sum((ell1(t(C,D)) for D in downsets(C) if D!=(1<<n)-1),F(0))
        local+=ell1(a)*(ell1(minus(t(C,(1<<n)-1),ONE))+proper)
    assert sum(map(ell1,delta.values()))<=local
    assert local<=F(2,2**n)*sum(map(ell1,lev[n].values()))
print('Atomic-padding differences corroborate the exact local summable-tail estimate (Gaussian upper bounds).')

# A three-chain plus isolate has the same phase seed after successive tops.
cp_key=canonical((0,1,0))
cp=[C for C in lev[3] if canonical(C)==cp_key]
ratios=[]
for C in cp:
    ratios.append(mul(lev[3][C],inv(lev[3][cp[0]])))
assert {norm2(z) for z in ratios}=={F(1)} and len(set(ratios))==2
for n in [4,5]:
    topped=[]
    for C in cp:
        while len(C)<n:C=C+((1<<len(C))-1,)
        topped.append(C)
    assert [mul(lev[n][C],inv(lev[n][topped[0]])) for C in topped]==ratios
print('cp holonomy persists through stages 4 and 5:',ratios)
print('PASS: finite checks corroborate the all-stage proof; they do not prove infinity or full vector covariance.')
