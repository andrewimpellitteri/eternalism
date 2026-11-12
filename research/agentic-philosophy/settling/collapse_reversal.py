"""Is the outcome record of a collapse dynamics time-symmetric?

Toy collapse model on a d-level system. Between collapses the state evolves by a fixed
unitary U = exp(-iH) with H real symmetric (a time-reversal invariant Hamiltonian; time
reversal is complex conjugation). At each step a collapse occurs with Kraus operators
K_o, real symmetric and positive, with sum_o K_o^2 = 1 (the analogue of the self-adjoint
Gaussian localisations of GRW). The record is the sequence of outcomes o_1 ... o_n.

    P(o_1 ... o_n) = Tr( A rho_0 A^dagger ),   A = K_{o_n} U ... U K_{o_1}.

We compare the probability of every record with that of its reversal, for
(a) the maximally mixed initial state, (b) a pure initial state.
Exact up to floating point. A finite check with its stated domain only.
"""
import cmath, math, itertools, random
random.seed(1)

def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def dag(A): return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def eye(d): return [[1.0+0j if i==j else 0j for j in range(d)] for i in range(d)]

def expm_minus_i(H,terms=60):
    d=len(H); out=eye(d); term=eye(d)
    for n in range(1,terms):
        term=[[sum(term[i][k]*(-1j*H[k][j]) for k in range(d))/n for j in range(d)] for i in range(d)]
        out=[[out[i][j]+term[i][j] for j in range(d)] for i in range(d)]
    return out

def model(d=3,n_out=2):
    H=[[0.0]*d for _ in range(d)]
    for i in range(d):
        for j in range(i,d): H[i][j]=H[j][i]=random.uniform(-1,1)
    U=expm_minus_i(H)
    # collapse operators diagonal in a fixed real basis: K_o = diag(sqrt(p_o(i)))
    P=[[random.random() for _ in range(d)] for _ in range(n_out)]
    for i in range(d):
        s=sum(P[o][i] for o in range(n_out))
        for o in range(n_out): P[o][i]/=s
    K=[[[complex(math.sqrt(P[o][i])) if i==j else 0j for j in range(d)] for i in range(d)] for o in range(n_out)]
    return U,K

def prob(seq,U,K,rho):
    A=K[seq[0]]
    for o in seq[1:]: A=mm(K[o],mm(U,A))
    return tr(mm(A,mm(rho,dag(A)))).real

def asymmetry(U,K,rho,n):
    worst=0.0; total=0.0; kl=0.0
    for seq in itertools.product(range(len(K)),repeat=n):
        p=prob(seq,U,K,rho); q=prob(seq[::-1],U,K,rho)
        worst=max(worst,abs(p-q)); total+=p
        if p>0 and q>0: kl+=p*math.log2(p/q)
    return worst,total,kl

if __name__=="__main__":
    d=3; U,K=model(d)
    mixed=[[ (1/d if i==j else 0)+0j for j in range(d)] for i in range(d)]
    pure=[[0j]*d for _ in range(d)]; pure[0][0]=1+0j
    for name,rho in (("maximally mixed",mixed),("pure",pure)):
        for n in (3,5,7):
            w,t,kl=asymmetry(U,K,rho,n)
            print(f"{name:16s} n={n}: total prob {t:.6f}  max |P(record)-P(reversed)| = {w:.2e}  KL(forward||reversed) = {kl:.4f} bits")
    # entropy of the state grows from the pure start and is constant from the mixed one
    def vn_proxy(rho): return 1-tr(mm(rho,rho)).real          # linear entropy
    def step(rho):
        rho=mm(U,mm(rho,dag(U)))
        out=[[0j]*d for _ in range(d)]
        for Ko in K:
            t_=mm(Ko,mm(rho,dag(Ko)))
            out=[[out[i][j]+t_[i][j] for j in range(d)] for i in range(d)]
        return out
    for name,rho in (("maximally mixed",mixed),("pure",pure)):
        vals=[]
        for _ in range(6): vals.append(vn_proxy(rho)); rho=step(rho)
        print(f"{name:16s} linear entropy of the averaged state by step: "+" ".join(f"{v:.3f}" for v in vals))
