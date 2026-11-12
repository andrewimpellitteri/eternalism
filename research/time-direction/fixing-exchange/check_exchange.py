"""Finite sanity checks for the exchange note. Exact rational arithmetic. Not a proof."""
import random
from fractions import Fraction as Fr
from collections import Counter
from math import log2
random.seed(0)

def rank(rows):
    rows=[r[:] for r in rows]; rk=0; ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        piv=next((i for i in range(rk,len(rows)) if rows[i][c]!=0),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]!=0:
                f=rows[i][c]/rows[rk][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[rk])]
        rk+=1
    return rk
def closure(B,S):
    base=[B[s] for s in S]; r=rank(base) if base else 0
    return {p for p in range(len(B)) if rank(base+[B[p]])==r}

X,T=5,5
def roll(v,k): return v[-k:]+v[:-k]
def wave(d):
    rows=[d[:X],d[X:]]
    for t in range(2,T):
        a,b=roll(rows[-1],1),roll(rows[-1],-1)
        rows.append([a[i]+b[i]-rows[-2][i] for i in range(X)])
    return sum(rows,[])
def heat(d):
    rows=[d]
    for t in range(1,T):
        a,b=roll(rows[-1],1),roll(rows[-1],-1)
        rows.append([Fr(1,4)*a[i]+Fr(1,2)*rows[-1][i]+Fr(1,4)*b[i] for i in range(X)])
    return sum(rows,[])
def basis(f,dim):
    cols=[f([Fr(int(i==j)) for j in range(dim)]) for i in range(dim)]
    return [[cols[i][p] for i in range(dim)] for p in range(len(cols[0]))]
def test(B,name,trials=1500):
    n=len(B); hits=bad=0
    for _ in range(trials):
        S=set(random.sample(range(n),random.randint(0,len(B[0]))))
        c=closure(B,S); out=[p for p in range(n) if p not in c]
        if len(out)<2: continue
        y,z=random.sample(out,2)
        if y in closure(B,S|{z}):
            hits+=1; bad+= z not in closure(B,S|{y})
    print(f"{name}: marginal fixings {hits}, exchange violations {bad}")
test(basis(wave,2*X),"wave lattice"); test(basis(heat,X),"heat lattice (time-asymmetric, linear)")

n=12; o=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n): o[i][j]=random.random()<0.3
for k in range(n):
    for i in range(n):
        for j in range(n):
            if o[i][k] and o[k][j]: o[i][j]=True
down=lambda S:{i for i in range(n) for s in S if i==s or o[i][s]}
hits=bad=0
for _ in range(4000):
    S=set(random.sample(range(n),random.randint(0,4))); c=down(S)
    out=[p for p in range(n) if p not in c]
    if len(out)<2: continue
    y,z=random.sample(out,2)
    if y in down(S|{z}): hits+=1; bad+= z in down(S|{y})
print(f"poset down-closure: marginal cases {hits}, anti-exchange violations {bad}")

hist=[(s,s*s) for s in (-2,-1,0,1,2)]
inj=lambda k: len({h[k] for h in hist})==len(set(hist))
H=lambda v:-sum(c/len(v)*log2(c/len(v)) for c in Counter(v).values())
print("class {sF+s^2G}: z fixes y:",inj(0),"| y fixes z:",inj(1),"| H(z)=%.3f H(y)=%.3f"%(H([h[0] for h in hist]),H([h[1] for h in hist])))

# ---- Region-level checks (added in the second pass) ----
print("\nRegion-level balance on the wave lattice (rows are time steps, X=%d, T=%d)"%(X,T))
W=basis(wave,2*X)
rk=lambda P: rank([W[p] for p in P]) if P else 0
rows=lambda ts:[t*X+x for t in ts for x in range(X)]
def report(name,A,C):
    rA,rC,rAC=rk(A),rk(C),rk(A+C)
    openC,openA,common=rAC-rA,rAC-rC,rA+rC-rAC
    assert openC-openA==rC-rA
    print(f"  {name}: info(A)={rA} info(C)={rC} common={common} open(C|A)={openC} open(A|C)={openA}")
report("A = one early row, C = two later rows", rows([0]), rows([3,4]))
report("A = two early rows, C = one later row", rows([0,1]), rows([4]))
report("A = half of row 0 and 1, C = rows 3,4", [x for x in range(3)]+[X+x for x in range(3)], rows([3,4]))
bad=0
for _ in range(300):
    A=random.sample(range(len(W)),random.randint(1,8)); C=random.sample(range(len(W)),random.randint(1,8))
    bad+= (rk(A+C)-rk(A))-(rk(A+C)-rk(C)) != rk(C)-rk(A)
print("  random regions: balance violations",bad)

print("\nStochastic balance: H(next|now) - H(now|next) = H(next) - H(now)")
P=[[0.1,0.9,0.0],[0.0,0.2,0.8],[0.7,0.0,0.3]]          # irreversible 3-state chain (no detailed balance)
def step(p): return [sum(p[i]*P[i][j] for i in range(3)) for j in range(3)]
def Hd(p): return -sum(q*log2(q) for q in p if q>0)
def cond(p):                                           # returns H(next|now), H(now|next)
    q=step(p); joint=[[p[i]*P[i][j] for j in range(3)] for i in range(3)]
    Hj=-sum(v*log2(v) for r in joint for v in r if v>0)
    return Hj-Hd(p), Hj-Hd(q), Hd(p), Hd(q)
pi=[1/3]*3
for _ in range(5000): pi=step(pi)
f,b,h0,h1=cond(pi)
print("  stationary:      forward %.6f  backward %.6f  entropy change %.6f"%(f,b,h1-h0))
f,b,h0,h1=cond([0.98,0.01,0.01])
print("  low-entropy start: forward %.6f  backward %.6f  difference %.6f  entropy change %.6f"%(f,b,f-b,h1-h0))
f,b,h0,h1=cond([1/3,1/3,1/3]) if False else cond([0.05,0.05,0.90])
print("  another start:     forward %.6f  backward %.6f  difference %.6f  entropy change %.6f"%(f,b,f-b,h1-h0))
