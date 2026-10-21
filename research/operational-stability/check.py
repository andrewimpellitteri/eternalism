"""Exact witnesses for the operational-stability note. Standard library only."""
from fractions import Fraction as F
from math import comb

def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def power(z,n):
 out=(F(1),F(0))
 for _ in range(n):out=mul(out,z)
 return out

def binary_check(n):
 response=F(0); maxsquare=F(0); total=(F(0),F(0))
 for k in range(n+1):
  z=mul(power((F(1,2),F(1,2)),k),power((F(1,2),F(-1,2)),n-k))
  square=z[0]**2+z[1]**2
  response+=comb(n,k)*square; maxsquare=max(maxsquare,square)
  total=(total[0]+comb(n,k)*z[0],total[1]+comb(n,k)*z[1])
 assert total==(1,0) and response==1 and maxsquare==F(1,2**n)
 print(f'n={n}: total=1; response(conjugate weights)=1; sup_norm_squared={maxsquare}; variation_squared={2**n}')

def finite_dual_check():
 # A finite signed example tests the sharp approximation bound without normalization.
 a=[F(3),F(-2),F(4),F(-4)]; variation=sum(map(abs,a)); bound=F(2)
 b=[bound*x/variation for x in a]
 error=sum(abs(x-y) for x,y in zip(a,b))
 assert sum(map(abs,b))==bound and error==variation-bound
 # Every sign control (the real signed analogue of phase alignment).
 from itertools import product
 worst=max(abs(sum((x-y)*s for x,y,s in zip(a,b,signs))) for signs in product((-1,1),repeat=4))
 assert worst==error
 print(f'dual check: variation={variation}; budget={bound}; worst error={worst}=variation-budget')

def boolean_witness(n):
 assert n%2==0
 rays=[F(0)]*4
 for k in range(n+1):
  z=mul(power((F(1,2),F(1,2)),k),power((F(1,2),F(-1,2)),n-k))
  assert z[0]==0 or z[1]==0
  ray=0 if z[0]>0 else 2 if z[0]<0 else 1 if z[1]>0 else 3
  rays[ray]+=comb(n,k)*(abs(z[0])+abs(z[1]))
 best=F(0)
 for mask in range(16):
  re=(rays[0] if mask&1 else 0)-(rays[2] if mask&4 else 0)
  im=(rays[1] if mask&2 else 0)-(rays[3] if mask&8 else 0)
  best=max(best,re*re+im*im)
 # Cruder rational bound implied by choosing the heaviest one of four rays.
 assert 16*best>=sum(rays)**2
 print(f'Boolean witness n={n}: max event amplitude squared={best}; rays={rays}')

if __name__=='__main__':
 for n in (1,2,4,8,12,20):binary_check(n)
 finite_dual_check()
 for n in (2,4,8,12,20):boolean_witness(n)
 print('All exact checks passed.')
