"""Level-relativity on the Kac ring: a worked toy example for statement S7.

N balls on a ring, each white (+1) or black (-1). A fixed set of marked edges. Each
step every ball moves one place clockwise and flips colour if it crosses a marked
edge. The map on (colours, markers) is a bijection, so the microscopic class is
deterministic in both time directions, and the uniform measure is stationary.

Macrovariable: M_t = number of white balls.

Case A (stationary): uniform measure on all colours and markers.
Case B (conditioned): all balls white at t = 0, markers uniform. Times run both ways.

For each t we report H(M_t), the forward openness H(M_{t+1} | M_t) and the backward
openness H(M_t | M_{t+1}). Exact enumeration. A toy with its stated domain only.
"""
from itertools import product
from collections import Counter
from math import log2

def H(counter,total):
    return -sum(c/total*log2(c/total) for c in counter.values())

def step(col,mark,N):       # ball at site i moves to i+1, crossing edge i
    return tuple(col[(i-1)%N]*(-1 if mark[(i-1)%N] else 1) for i in range(N))
def back(col,mark,N):
    return tuple(col[(i+1)%N]*(-1 if mark[i] else 1) for i in range(N))

def trajectory(col,mark,N,tmin,tmax):
    out={0:col}; c=col
    for t in range(1,tmax+1): c=step(c,mark,N); out[t]=c
    c=col
    for t in range(-1,tmin-1,-1): c=back(c,mark,N); out[t]=c
    return out

def report(name,ensemble,N,tmin,tmax):
    total=len(ensemble); single={t:Counter() for t in range(tmin,tmax+1)}
    pair={t:Counter() for t in range(tmin,tmax)}
    for col,mark in ensemble:
        tr=trajectory(col,mark,N,tmin,tmax)
        m={t:sum(1 for v in tr[t] if v==1) for t in tr}
        for t in range(tmin,tmax+1): single[t][m[t]]+=1
        for t in range(tmin,tmax): pair[t][(m[t],m[t+1])]+=1
    print(name); print("   t   H(M_t)  open(next|now)  open(now|next)  difference")
    for t in range(tmin,tmax):
        h0,h1,hj=H(single[t],total),H(single[t+1],total),H(pair[t],total)
        print(f"  {t:3d}  {h0:6.3f}     {hj-h0:6.3f}          {hj-h1:6.3f}       {(hj-h0)-(hj-h1):+7.3f}")

if __name__=="__main__":
    N=6
    allcols=list(product((1,-1),repeat=N)); allmarks=list(product((0,1),repeat=N))
    report(f"Case A: stationary, N={N}, all {len(allcols)*len(allmarks)} microstates",
           [(c,m) for c in allcols for m in allmarks],N,-3,3)
    N=12
    marks=list(product((0,1),repeat=N))
    report(f"\nCase B: all white at t=0, N={N}, {len(marks)} marker sets",
           [((1,)*N,m) for m in marks],N,-8,26)

def case_c(N=16,mu=0.1,tmax=18):
    """All white at t = 0, markers independent with density mu (weighted, exact).
    Ball i is black at time t iff the markers on edges i..i+t-1 have odd sum."""
    from collections import defaultdict
    single=[defaultdict(float) for _ in range(tmax+1)]; pair=[defaultdict(float) for _ in range(tmax)]
    for bits in range(1<<N):
        k=bin(bits).count("1"); w=mu**k*(1-mu)**(N-k)
        mk=[(bits>>i)&1 for i in range(N)]
        par=[0]*N; ms=[N//2]
        for t in range(1,tmax+1):
            par=[par[i]^mk[(i+t-1)%N] for i in range(N)]
            ms.append((N-sum(par))//2)      # bins of two remove an exact parity oscillation
        for t in range(tmax+1): single[t][ms[t]]+=w
        for t in range(tmax): pair[t][(ms[t],ms[t+1])]+=w
    Hw=lambda d:-sum(p*log2(p) for p in d.values() if p>0)
    print(f"\nCase C: all white at t=0, N={N}, marker density {mu}, M binned in twos. Negative times mirror these.")
    print("   t   H(M_t)  open(next|now)  open(now|next)  difference")
    for t in range(tmax):
        h0,h1,hj=Hw(single[t]),Hw(single[t+1]),Hw(pair[t])
        print(f"  {t:3d}  {h0:6.3f}     {hj-h0:6.3f}          {hj-h1:6.3f}       {(hj-h0)-(hj-h1):+7.3f}")

if __name__=="__main__":
    case_c()
