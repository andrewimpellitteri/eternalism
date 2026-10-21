"""Exact checks for record-loss recovery bounds; fractions only."""
from fractions import Fraction as F

def optimum(m,g):
 c=(1-g)/m
 b=(m-2)*c/(1+(m-2)*c)
 error=(m-1)*c/(1+(m-2)*c)
 return b,error

def error_for(m,g,a,b):
 d=(a+(m-1)*b)/m
 parallel=g*a+(1-g)*d
 perpendicular=g*b+(1-g)*d
 return max(abs(1-parallel),abs(perpendicular))

for m in (2,3,4,8,32,128):
 for g in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
  b,err=optimum(m,g)
  assert 0<=b<=1 and error_for(m,g,F(1),b)==err
  # Separate coarse search over every permutation-symmetric effect on a grid.
  for ia in range(21):
   for ib in range(21):
    assert error_for(m,g,F(ia,20),F(ib,20))>=err
  if g==F(1,2):print(f'm={m}, gamma=1/2: optimal b={b}, uniform probability error={err}')

for g in (F(1,10),F(1,2),F(9,10)):
 # Required 2x2 preimage of target eta*J has negative determinant.
 eta=F(1,2)
 det=eta**2-(eta/g)**2
 assert det<0
 print(f'gamma={g}: exact preimage determinant={det}<0 (no positive effect)')

for n in (1,4,8,12,20):
 r=F(1,2)**n
 variance=1/(4*r*r)
 samples=variance/F(1,100)
 assert samples==25*4**n
 print(f'Independent leaked histories n={n}: visibility={r}; samples at x=0, RMSE 0.1: {samples}')
print('All exact record-loss checks passed.')
