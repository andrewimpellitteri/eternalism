"""Mode count for the past and future cones of a standpoint in a big-bang half-space.

Model. Spatially flat FLRW is conformal to the half-space eta > 0 of Minkowski
spacetime, and a conformally coupled massless field becomes the flat wave equation
there. We use the exact light-cone lattice in 1+1 dimensions,
    psi(eta+1, x) + psi(eta-1, x) = psi(eta, x+1) + psi(eta, x-1),
on rows eta = 0..T, with the big bang at row 0. Space is periodic with a period too
large for wrap-around to reach the cones. The lattice spacing is the cutoff.

info(R)      = rank of the restriction of the solution space to the region R
common       = info(A) + info(C) - info(A u C)
open(C | A)  = info(A u C) - info(A)
Exact integer arithmetic (fraction-free elimination mod a large prime would also do;
Fractions are fast enough here). A finite check with its stated domain only.
"""
from fractions import Fraction as Fr
import sys

def rank(rows):
    rows=[r[:] for r in rows]; rk=0
    ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        piv=next((i for i in range(rk,len(rows)) if rows[i][c]!=0),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        pr=rows[rk]; pv=pr[c]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]!=0:
                f=rows[i][c]/pv; ri=rows[i]
                rows[i]=[a-f*b if b else a for a,b in zip(ri,pr)]
        rk+=1
        if rk==len(rows): break
    return rk

def build(T,L):
    # column j of the solution matrix = evolution of the j-th unit datum on rows 0,1
    dim=2*L; table={}
    cur=[[Fr(int(j==x)) for j in range(dim)] for x in range(L)]            # row 0
    nxt=[[Fr(int(j==L+x)) for j in range(dim)] for x in range(L)]          # row 1
    table[0]=cur; table[1]=nxt
    for t in range(2,T+1):
        new=[[a+b-c for a,b,c in zip(nxt[(x+1)%L],nxt[(x-1)%L],cur[x])] for x in range(L)]
        cur,nxt=nxt,new; table[t]=new
    return table

def run(n,T,flip=False):
    L=2*T+6; tab=build(T,L)
    ev=lambda t,x: tab[t][x%L]
    past=[(t,x) for t in range(0,n) for x in range(-(n-t)+1,(n-t))]
    fut =[(t,x) for t in range(n+1,T+1) for x in range(-(t-n)+1,(t-n))]
    rA=rank([ev(*p) for p in past]) if past else 0
    rC=rank([ev(*p) for p in fut]) if fut else 0
    rAC=rank([ev(*p) for p in past+fut])
    return rA,rC,rAC

if __name__=="__main__":
    print("standpoint row n, last row T | info(past) info(future) common | open(fut|past) open(past|fut) | imbalance")
    for n,T in [(3,6),(3,9),(3,12),(3,16),(5,10),(5,16),(8,16),(4,8),(6,12),(8,12)]:
        rA,rC,rAC=run(n,T)
        print(f"  n={n:2d} T={T:2d} | {rA:3d} {rC:3d} {rA+rC-rAC:2d} | {rAC-rA:3d} {rAC-rC:3d} | {rC-rA:+d}")
