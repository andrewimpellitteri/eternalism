"""Independent 6x6 checks from closed-form clock-energy blocks; stdlib only."""
import cmath
import math
from fractions import Fraction as F

N=3
TAU=2*math.pi/3

def eye(n):
    return [[complex(i==j) for j in range(n)] for i in range(n)]

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def dag(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]

def err(a,b):
    return max(abs(x-y) for ra,rb in zip(a,b) for x,y in zip(ra,rb))

def sub(a,b):
    return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]

def evo(eps,g,origin,t):
    out=[[0j]*6 for _ in range(6)]
    for n in range(3):
        x=g if n==1 else 0
        z=eps/2
        r=math.hypot(x,z)
        c=math.cos(r*t)
        s=math.sin(r*t)/r if r else t
        phase=cmath.exp(-1j*(n-origin)*t)
        block=[[c-1j*s*z,-1j*s*x],[-1j*s*x,c+1j*s*z]]
        for i in range(2):
            for j in range(2):out[2*n+i][2*n+j]=phase*block[i][j]
    return out

def projector(k):
    return [[cmath.exp(-1j*(i//2-j//2)*k*TAU)/3 if i%2==j%2 else 0j
             for j in range(6)] for i in range(6)]

def cols(indices):
    return [[complex(i==j) for j in indices] for i in range(6)]

def scale(c,a):return [[c*x for x in row] for row in a]

def spectrum(eps,g):
    r=math.hypot(eps/2,g)
    return [-eps/2,eps/2,1-r,1+r,2-eps/2,2+eps/2]

def fixed_dim(energies,origin):
    return sum(abs((e-origin)/3-round((e-origin)/3))<1e-9 for e in energies)

def eig_dim(energies,origin):return sum(abs(e-origin)<1e-9 for e in energies)

I=eye(6)
for eps,g,origin,expected in [(1,0,0,False),(1,0,.5,True),(2,0,0,True),
                             (2,.5,1,False),(2,math.sqrt(3),1,True),
                             (2,math.sqrt(8),-2,True)]:
    u=evo(eps,g,origin,TAU)
    wrap=mul(mul(u,u),u)
    defect=err(wrap,I)
    assert (defect<1e-9)==expected
    assert err(wrap,evo(eps,g,origin,2*math.pi))<1e-12
    print(f'eps={eps} g={g:.9f} origin={origin}: max-entry wrap defect={defect:.9f}; valid={expected}')
assert err(evo(1,0,0,2*math.pi),scale(-1,I))<1e-12
print('Unshifted eps=1 free model: wrap equals -I; half-unit origin repairs it.')

for eps,g,origin,nd,nf in [(1,0,.5,2,2),(1,0,-.5,1,2),
                           (2,0,0,1,2),(2,0,1,2,2),
                           (2,math.sqrt(8),-2,1,4)]:
    es=spectrum(eps,g)
    assert eig_dim(es,origin)==nd and fixed_dim(es,origin)==nf
    print(f'Alias check eps={eps}, g={g:.9f}, origin={origin}: Dirac dim={nd}; fixed dim={nf}')

# Exact arithmetic certificate for integer-gap classification at chosen points.
# With eps=2, touched r^2=1+g^2. Unchanged energies are odd integers.
for g2,r in [(F(0),1),(F(3),2),(F(8),3),(F(15),4)]:
    assert 1+g2==r*r
assert F(1)+F(1,4)==F(5,4) # sqrt5/2 is irrational, so no scalar-origin repair.
print('Exact resonance certificates g^2 = 0,3,8,15; g=1/2 fails integer gaps analytically.')

J=cols([0,5]) # V_1 for eps=2 and both g=1/2, sqrt3.
seed=scale(math.sqrt(3),projector(0))
for g in [.5,math.sqrt(3)]:
    u=evo(2,g,1,TAU)
    seed_v=mul(seed,J)
    wrap_seed=err(mul(evo(2,g,1,2*math.pi),seed_v),seed_v)
    reading=err(mul(mul(u,projector(0)),J),mul(projector(1),J))
    assert reading>0.1
    if g==.5:assert wrap_seed>0.1
    else:assert wrap_seed<1e-12
    # Direct clock reductions computed independently of U's orbit.
    grams=[]
    for k in range(3):
        R=[[sum(cmath.exp(1j*n*k*TAU)*J[2*n+s][j] for n in range(3))
            for j in range(2)] for s in range(2)]
        grams.append(mul(dag(R),R))
    assert all(err(G,eye(2))<1e-12 for G in grams)
    print(f'g={g:.9f}: seed wrap defect={wrap_seed:.9f}, reading covariance defect={reading:.9f}; direct all-input reductions remain unitary.')

# Finite averaging of a nongroup unitary need not be an orthogonal projector.
u=evo(2,.5,1,TAU)
u2=mul(u,u)
A=[[sum(v)/3 for v in zip(*rows)] for rows in zip(I,u,u2)]
assert err(mul(A,A),A)>.01 and err(dag(A),A)>.01
print(f'Invalid finite twirl: idempotence defect={err(mul(A,A),A):.9f}; Hermiticity defect={err(dag(A),A):.9f}')
print('PASS: analytic classification corroborated; no eigensolver or worker code reused.')
