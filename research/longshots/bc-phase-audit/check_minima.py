"""Exact direct-poset enumeration versus a completed minimum-count law.

Stdlib only; enumerate all transitive predecessor-mask tuples through size 5,
rather than reusing the growth-tree checker. Infinite values use rational tail
bounds. No finite truncation is treated as proof of the infinite claim.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

Z=(F(0),F(0));ONE=(F(1),F(0));DELTA=F(1,10)
PHASES={'phase':(F(3,5),F(4,5)),'conjugate':(F(3,5),F(-4,5)),'real_control':ONE}

def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(a,x):return a*x[0],a*x[1]
def inv(x):
    d=x[0]**2+x[1]**2
    assert d
    return x[0]/d,-x[1]/d

def sumg(xs):
    s=Z
    for x in xs:s=add(s,x)
    return s

def valid(C):
    return all(all(not(C[i]>>j&1) or C[j]&C[i]==C[j] for j in range(i)) for i in range(len(C)))

@lru_cache(None)
def ideals(C):return tuple(P for P in range(1<<len(C)) if all(not(P>>i&1) or C[i]&P==C[i] for i in range(len(C))))
@lru_cache(None)
def induced(C,P):
    old=[i for i in range(len(C)) if P>>i&1]
    return tuple(sum(1<<j for j,v in enumerate(old) if C[i]>>v&1) for i in old)

def model(u):
    def q(C):
        n=len(C)
        if n==0:return ONE
        if n==1:return F(1,2),F(0)
        if n==2:return (F(1,4),F(0)) if C[1] else scale(F(1,4),u)
        return DELTA**n,F(0)
    @lru_cache(None)
    def w(C):return sub(inv(q(C)),sumg(w(induced(C,P)) for P in ideals(C) if P!=(1<<len(C))-1))
    def amplitude(C):
        a=ONE
        for j in range(len(C)):a=mul(a,mul(q(C[:j]),w(induced(C[:j],C[j]))))
        return a
    return amplitude

def count_polynomial(u,N):
    g=[Z,(F(3,8),F(0)),scale(F(1,8),sub((F(5),F(0)),u)),scale(F(1,8),u)]
    for n in range(3,N):
        q=DELTA**n;out=[Z]*(len(g)+1)
        for m,a in enumerate(g):
            out[m]=add(out[m],scale(1-q,a))
            out[m+1]=add(out[m+1],scale(q,a))
        g=out
    return g

saved_amplitudes={}
for name,u in PHASES.items():
    amplitude=model(u)
    saved_amplitudes[name]={}
    for N in range(3,6):
        causets=[C for C in product(*(range(1<<i) for i in range(N))) if valid(C)]
        assert len(causets)=={3:7,4:40,5:357}[N]
        coeff=[Z]*(N+1)
        for C in causets:
            m=C.count(0)
            a=amplitude(C)
            coeff[m]=add(coeff[m],a)
            saved_amplitudes[name][C]=a
        target=count_polynomial(u,N)
        assert coeff==target and sumg(coeff)==ONE
        print(f'{name}, N={N}: {len(causets)} posets; direct amplitude sums equal every coefficient of G_N exactly.')
        if N==3:print('  minimum-count amplitudes:',coeff[1:])

for C,a in saved_amplitudes['phase'].items():
    assert saved_amplitudes['conjugate'][C]==(a[0],-a[1])
V=(0,0,3)
def abs2(z):return z[0]**2+z[1]**2
c_phase=abs2(saved_amplitudes['phase'][V])
c_real=abs2(saved_amplitudes['real_control'][V])
assert c_phase==F(53,320) and c_real==F(1,64) and c_phase-c_real==F(3,20)
print('Fixed-data check: all conjugate amplitudes agree by conjugation through N=5; V cylinder gap versus real control is 3/20.')

L=12
b0_L=F(1);s_L=F(0)
for n in range(3,L+1):
    q=DELTA**n;b0_L*=1-q;s_L+=q/(1-q)
r=DELTA**(L+1)/(1-DELTA)
b_lo,b_hi=b0_L*(1-r),b0_L
s_lo,s_hi=s_L,s_L+r/(1-DELTA**(L+1))
assert F(899,900)<=b_lo<=b_hi<=1

def mu(b0,s,u):
    return b0*b0*((5+3*s-u[0])**2+u[1]**2)/64

def gap(b0,s):return b0*b0*(5+3*s)/80
lo_gap,hi_gap=gap(b_lo,s_lo),gap(b_hi,s_hi)
global_lo=F(899,900)**2/16
assert global_lo==F(808201,12960000) and 0<global_lo<=lo_gap<hi_gap
for b0,s in [(b_lo,s_lo),(b_hi,s_hi)]:
    assert mu(b0,s,PHASES['phase'])==mu(b0,s,PHASES['conjugate'])
    assert mu(b0,s,PHASES['phase'])-mu(b0,s,ONE)==gap(b0,s)
    A=b0*(5+3*s)/8;B=b0/8
    assert gap(b0,s)==F(16,3)*A*B*(c_phase-c_real)

# A separate finite tail polynomial recovers b0_L and b1_L=b0_L*s_L.
f=[F(1)]
for n in range(3,L+1):
    q=DELTA**n;out=[F(0)]*(len(f)+1)
    for m,c in enumerate(f):out[m]+=(1-q)*c;out[m+1]+=q*c
    f=out
assert f[0]==b0_L and f[1]==b0_L*s_L and sum(f)==1

def outward(v,places,upper=False):
    den=10**places
    scaled=(v.numerator*den+v.denominator-1)//v.denominator if upper else (v.numerator*den)//v.denominator
    return f'{scaled//den}.{scaled%den:0{places}d}'
print('Infinite tail enclosure: L=12, exact residual sum =',r)
for name,u in PHASES.items():
    lo,hi=mu(b_lo,s_lo,u),mu(b_hi,s_hi,u)
    assert 0<hi-lo<F(1,10**11)
    print(f'  mu_{name}(exactly 2 minima) in [{outward(lo,14)}, {outward(hi,14,True)}]')
print(f'  strict gap in [{outward(lo_gap,14)}, {outward(hi_gap,14,True)}]')
print('  global rational lower bound:',global_lo)
print('PASS: intrinsic event differs in the two specified dynamics. This is not a detector probability or a pure gauge comparison.')
