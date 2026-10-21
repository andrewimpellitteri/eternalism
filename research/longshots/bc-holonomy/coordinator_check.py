"""Independent exact checker: bit-mask posets, permutations, no seed imports."""
from fractions import Fraction as F
from itertools import permutations

Z=(F(0),F(0));ONE=(F(1),F(0))

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def norm2(a):return a[0]**2+a[1]**2

def ideals(C):
    return [D for D in range(1<<len(C)) if all(not(D>>i&1) or C[i]&D==C[i] for i in range(len(C)))]

def amp(C,D):
    n=len(C)
    if n==0:return ONE
    if n==1:return F(1,2),F(0)
    if n>=3:return ONE if D==(1<<n)-1 else Z
    if C[1]:return (F(1,2) if D==3 else F(1,4)),F(0)
    return (F(11,20),F(-3,5)) if D==3 else (F(3,20),F(1,5))

def restrict(C,B,D):
    old=[i for i in range(len(C)) if B>>i&1]
    index={v:i for i,v in enumerate(old)}
    parent=tuple(sum(1<<index[j] for j in old if C[i]>>j&1) for i in old)
    event=sum(1<<index[j] for j in old if D>>j&1)
    return parent,event

def canon(C):
    # Canonical adjacency edge list under ALL bijections, not just natural labels.
    edges=[(j,i) for i,mask in enumerate(C) for j in range(len(C)) if mask>>j&1]
    return min(tuple(sorted((p[j],p[i]) for j,i in edges)) for p in permutations(range(len(C))))

levels=[{():ONE}]
for n in range(5):
    nxt={}
    for C,a in levels[-1].items():
        for D in ideals(C):
            child=C+(D,)
            assert child not in nxt
            nxt[child]=mul(a,amp(C,D))
    levels.append(nxt)
assert [len(x) for x in levels]==[1,1,2,7,40,357]
checks=0
for n in range(1,5):
    for C in levels[n]:
        ds=ideals(C)
        total=Z
        for D in ds:total=add(total,amp(C,D))
        assert total==ONE
        for i,P in enumerate(ds):
            for Q in ds[i+1:]:
                B,Pb=restrict(C,P|Q,P)
                B2,Qb=restrict(C,P|Q,Q)
                assert B==B2
                assert mul(amp(C,P),amp(B,Qb))==mul(amp(C,Q),amp(B,Pb))
                checks+=1
    classes={}
    for C,a in levels[n+1].items():
        key=canon(C)
        if key in classes:assert classes[key]==norm2(a)
        else:classes[key]=norm2(a)
    print(f'stage {n+1}: {len(levels[n+1])} labelled causets, {len(classes)} classes; exact MSR/BC/norm covariance pass; cumulative BC={checks}')
cp=(0,1,0)
key=canon(cp)
values=[a for C,a in levels[3].items() if canon(C)==key]
assert sorted(values)==sorted([(F(3,40),F(1,10))]*2+[(F(1,8),F(0))])
assert len({norm2(a) for a in values})==1 and len(set(values))==2
print('Independent Gaussian-rational holonomy witness verified with separate enumeration and canonicalization.')
print('PASS: finite zero-aware product-BC convention only; nonzero extension unresolved.')
