"""Independent exact effect/channel and completed-labeling counterexamples.

Standard library; enumerate all transitive upper-triangular orders on three
points directly rather than importing either research lane's growth code.
"""
from fractions import Fraction as F
from itertools import product,permutations

ZERO=(F(0),F(0))
ONE=(F(1),F(0))

def gadd(x,y):return x[0]+y[0],x[1]+y[1]
def gmul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def conj(x):return x[0],-x[1]
def times(r,x):return r*x[0],r*x[1]
def power(x,n):
    out=ONE
    for _ in range(n):out=gmul(out,x)
    return out

def valid(C):
    return all(C[i]<(1<<i) and all(not(C[i]>>j&1) or C[j]&C[i]==C[j]
                                 for j in range(i)) for i in range(len(C)))

def canon(C):
    edges=[(j,i) for i,row in enumerate(C) for j in range(len(C)) if row>>j&1]
    return min(tuple(sorted((p[j],p[i]) for j,i in edges)) for p in permutations(range(len(C))))

def invariants(C):
    L=sum(1 for i,row in enumerate(C) for j in range(i) if row>>j&1 and
          not any((row>>k&1) and (C[k]>>j&1) for k in range(j+1,i)))
    h=len(C)*(len(C)-1)//2-sum(row.bit_count() for row in C)
    return L,h

def ray(C):
    L,h=invariants(C)
    return (L-h)%8 in {0,1}

causets=[C for C in product(range(1),range(2),range(4)) if valid(C)]
assert len(causets)==7
keys=[canon(C) for C in causets]
classes=list(dict.fromkeys(keys))
assert len(classes)==5
chosen=[i for i,C in enumerate(causets) if ray(C)]
assert {causets[i] for i in chosen}=={(0,0,3),(0,1,1)}
i,j=chosen
assert keys[i]!=keys[j] and keys.count(keys[i])==keys.count(keys[j])==1
n=len(causets);m=len(chosen)
D=[[F(a==b and a in chosen) for b in range(n)] for a in range(n)]
Q=[[F(1,m) if a in chosen and b in chosen else F(0) for b in range(n)] for a in range(n)]

def pinch(M):return [[x if keys[a]==keys[b] else ZERO for b,x in enumerate(row)] for a,row in enumerate(M)]
def class_record(M):return [sum((M[a][a][0] for a in range(n) if keys[a]==k),F(0)) for k in classes]
def expectation(B,M):
    out=ZERO
    for a in range(n):
        for b in range(n):out=gadd(out,times(B[a][b],M[b][a]))
    assert out[1]==0
    return out[0]
def make_pair(sign):
    M=[[ZERO for _ in range(n)] for _ in range(n)]
    M[i][i]=M[j][j]=(F(1,2),F(0))
    M[i][j]=M[j][i]=(F(sign,2),F(0))
    return M

plus,minus=make_pair(1),make_pair(-1)
assert pinch(plus)==pinch(minus)
assert class_record(plus)==class_record(minus)
assert [expectation(Q,s) for s in [plus,minus]]==[1,0]
assert [expectation(D,s) for s in [plus,minus]]==[1,1]
print('n=3: 7 labelled histories, 5 shape classes, event exactly V and Lambda (2 singleton classes).')
print('Identical pinched states and identical classical shape records; Q probabilities 1 and 0; membership probabilities both 1.')

# All within-class transpositions preserve both target effects and the witness
# input states. This establishes covariance for the stated finite register group.
for k in classes:
    members=[a for a in range(n) if keys[a]==k]
    for b in members[1:]:
        perm=list(range(n));a=members[0];perm[a],perm[b]=perm[b],perm[a]
        for B in [D,Q]:assert all(B[perm[a]][perm[b]]==B[a][b] for a in range(n) for b in range(n))
        for M in [plus,minus]:assert all(M[perm[a]][perm[b]]==M[a][b] for a in range(n) for b in range(n))
print('Finite within-class permutation invariance: D, Q, plus and minus all pass.')

# The reachable effect D/2 has norm error 1/2: (Q-D/2)^2=D/4.
B=[[Q[a][b]-D[a][b]/2 for b in range(n)] for a in range(n)]
B2=[[sum(B[a][k]*B[k][b] for k in range(n)) for b in range(n)] for a in range(n)]
assert B2==[[x/4 for x in row] for row in D]
print('Sharp all-input probability-error floor 1/2: attained by D/2; exact squared error operator equals D/4.')

p=(F(1,2),F(1,2));q=conj(p)
amplitudes=[]
for C in causets:
    L,h=invariants(C);amplitudes.append(gmul(power(p,L),power(q,h)))
rho=[[gmul(a,conj(b)) for b in amplitudes] for a in amplitudes]
assert sum(rho[a][a][0] for a in range(n))==1
assert all(amplitudes[a]==(F(1,4),F(1,4)) for a in chosen)
assert expectation(D,rho)==F(1,4)
assert expectation(Q,rho)==F(1,4)
assert expectation(Q,pinch(rho))==F(1,8)
print('Actual normalized percolation state: membership=1/4; coherent-filter probability=1/4 before and 1/8 after class pinching.')

# Class pinching fixes membership but removes cross-class coherent entries.
assert all((D[a][b] if keys[a]==keys[b] else 0)==D[a][b] for a in range(n) for b in range(n))
assert Q[i][j]==F(1,2) and keys[i]!=keys[j]

A=(0,0,3,0);Ap=(0,0,0,3)
assert valid(A) and valid(Ap) and canon(A)==canon(Ap)
assert ray(A[:3]) and not ray(Ap[:3])
print('Completed-covariance counterexample: isomorphic prefixes (0,0,3,0) and (0,0,0,3) give opposite n=3 event values.')
# Appending universal tops keeps them isomorphic and yields matching finite
# restrictions of the analytically specified infinite completion.
for _ in range(3):
    A=A+((1<<len(A))-1,);Ap=Ap+((1<<len(Ap))-1,)
    assert valid(A) and valid(Ap)
    # The same exchange 2 <-> 3 is still an isomorphism, independently checked.
    perm=list(range(len(A)));perm[2],perm[3]=perm[3],perm[2]
    assert all(bool(A[a]>>b&1)==bool(Ap[perm[a]]>>perm[b]&1)
               for a in range(len(A)) for b in range(len(A)))
print('Universal-top continuation: same exchange preserves every later relation; infinite conclusion uses the stated analytic construction.')
print('PASS: exact rational checks; no observer dynamics, general quantum measure, or novelty claim.')
