"""Exact coherent labelled-growth diagnostic on the known norm-matching circle."""
from fractions import Fraction as F

def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def power(z,n):
 a=(F(1),F(0))
 for _ in range(n):a=mul(a,z)
 return a

def abs2(z):return z[0]*z[0]+z[1]*z[1]
def children(c,p,q):
 n=len(c)
 for d in range(1<<n):
  if any((d>>j)&1 and c[j]&~d for j in range(n)):continue
  mx=sum(1 for j in range(n) if (d>>j)&1 and not any((d>>k)&1 and ((c[k]>>j)&1) for k in range(n)))
  z=mul(power(p,mx),power(q,n-d.bit_count()))
  yield c+(d,),z

p=(F(1,2),F(1,2));q=(F(1,2),F(-1,2))
level={(): (F(1),F(0))}
for n in range(1,7):
 nxt={}
 for c,a in level.items():
  desc=list(children(c,p,q));assert sum(abs2(z) for _,z in desc)==1
  assert sum(z[0] for _,z in desc)==1 and sum(z[1] for _,z in desc)==0
  for child,z in desc:
   assert child not in nxt # different labelled parents have disjoint child sets
   nxt[child]=mul(a,z)
 level=nxt
 assert sum(abs2(z) for z in level.values())==1
 assert sum(z[0] for z in level.values())==1 and sum(z[1] for z in level.values())==0
 print(f'n={n}: labelled histories={len(level)}; sum amplitudes=1; squared norm=1; every parent column norm=1; disjoint column supports')
print('All coherent-growth exact checks passed.')
