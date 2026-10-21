"""Exact event-filter checks; no numerical eigensolver or external libraries."""
from fractions import Fraction as F
from math import comb
from itertools import product

def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,n):
 b=(F(1),F(0))
 for _ in range(n):b=mul(b,a)
 return b

def model(n):
 assert n%2==0
 count=[0]*4; sums=[(F(0),F(0)) for _ in range(4)]
 # a_w=p^k q^(n-k), phase exponent 2k-n modulo 8, divided by 2.
 for k in range(n+1):
  a=mul(power((F(1,2),F(1,2)),k),power((F(1,2),F(-1,2)),n-k))
  r=((2*k-n)//2)%4; number=comb(n,k)
  count[r]+=number
  sums[r]=(sums[r][0]+number*a[0],sums[r][1]+number*a[1])
 event_size=count[0]+count[1]
 z=(sums[0][0]+sums[1][0],sums[0][1]+sums[1][1])
 mu=z[0]**2+z[1]**2; detector=mu/event_size
 assert event_size==2**(n-1)+2**(n//2-1)
 assert mu==F((2**(n//2-1)+1)**2+2**(n-2),4)
 assert 0<=detector<=1
 # Projector Q=|chi_E><chi_E| has Q^2=Q and one eigenvalue 1.
 # Its entries on E are 1/m: entry of Q^2 is sum_m 1/m^2=1/m.
 assert event_size*F(1,event_size)**2==F(1,event_size)
 # Incoherent event membership alone produces a different probability.
 membership=F(event_size,2**n)
 print(f'n={n}: histories={2**n}; selected={event_size}; mu={mu}; detector={detector} ({float(detector):.8f}); membership={membership}')
 return count,sums

def independent_word_check(n):
 # A separate path: enumerate bit strings and a two-bit modular counter.
 counts=[0]*4; selected=(F(0),F(0)); number=0
 for word in product((0,1),repeat=n):
  a=(F(1),F(0)); counter=0
  for bit in word:
   counter=(counter+bit)%4
   a=mul(a,(F(1,2),F(1,2)) if bit else (F(1,2),F(-1,2)))
  counts[((2*counter-n)//2)%4]+=1
  phase=((2*counter-n)//2)%4
  if phase in (0,1):
   selected=(selected[0]+a[0],selected[1]+a[1]);number+=1
 c,s=model(n)
 assert c==counts and number==c[0]+c[1]
 assert selected==(s[0][0]+s[1][0],s[0][1]+s[1][1])
 print(f'  Independent word enumeration and modular recognizer agree at n={n}')

if __name__=='__main__':
 for n in (2,4,8):independent_word_check(n)
 for n in (12,20,40):model(n)
 print('All exact checks passed.')
