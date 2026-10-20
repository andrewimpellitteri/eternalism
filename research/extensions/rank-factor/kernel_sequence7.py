#!/usr/bin/env python3
"""R_k via post-free T: S=T + {max}, k>=2."""
import sys
from pathlib import Path
import cmath, math
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "experiments" / "baseline"))
import poscau

def posts(rel,n):
    return [i for i in range(n) if all((j,i) in rel for j in range(i)) and all((i,j) in rel for j in range(i+1,n))]
def minima(rel,n):
    return [i for i in range(n) if not any((j,i) in rel for j in range(i))]
def maxima(rel,n):
    return [i for i in range(n) if not any((i,j) in rel for j in range(i+1,n))]

def R(max_k,p):
    out={1:(p,1)}
    for k in range(2,max_k+1):
        total=0; count=0
        for T in poscau.causets(k-1):
            if posts(T,k-1): continue
            m=len(maxima(T,k-1)); mn=len(minima(T,k-1))
            total += poscau.amplitude(T,k-1,p) * (p**m) * (p**mn)
            count+=1
        out[k]=(total,count)
    return out

def roots(coeffs,it=300):
    n=len(coeffs)-1; c=[complex(x) for x in coeffs]; lead=c[-1]; c=[x/lead for x in c]
    rs=[cmath.exp(2j*math.pi*k/n)*0.8 for k in range(n)]
    for _ in range(it):
        new=[]
        for i,z in enumerate(rs):
            num=sum(c[j]*z**j for j in range(n+1)); den=1
            for j,w in enumerate(rs):
                if i!=j: den*=z-w
            new.append(z-num/den if den else z)
        rs=new
    return rs

for p in (0.5,0.5+0.5j,0.2+0.7j):
    print('p=',p)
    r=R(7,p)
    for k in range(1,8):
        print(' R%d = %r (terms %d)'%(k,r[k][0],r[k][1]))
    coeff=[1]+[-r[k][0] for k in range(1,8)]
    rs=sorted(roots(coeff),key=abs)
    for z in rs: print('   root %s |z=%.6g'%(z,abs(z)))
    print()
