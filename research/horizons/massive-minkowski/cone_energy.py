"""Energy outside the past light cone for the 1+1 Klein-Gordon equation.

phi_tt - phi_xx + m^2 phi = 0 on a periodic box, solved exactly mode by mode from
Gaussian data at t = 0. For each earlier time t we report the fraction of the conserved
energy lying in {|x| >= |t| - R}, the complement of a slightly shrunk past cone of the
origin event. The proposition in RESULT.md says this fraction tends to 0 as t -> -infinity
for m > 0. For m = 0 it stays at 1. A numerical illustration with its stated domain only.
"""
import cmath, math

def run(m, N=1024, L=1600.0, width=2.0, R=10.0, times=(0,-50,-100,-200,-400,-700)):
    dx=L/N; xs=[(j-N//2)*dx for j in range(N)]
    f=[math.exp(-(x/width)**2) for x in xs]
    ks=[2*math.pi*(n if n<N//2 else n-N)/L for n in range(N)]
    # forward DFT of the data (phi(0)=f, phi_t(0)=0)
    fh=[sum(f[j]*cmath.exp(-1j*ks[n]*xs[j]) for j in range(N))/N for n in range(N)]
    keep=[n for n in range(N) if abs(fh[n])>1e-14*max(abs(v) for v in fh)]
    out=[]
    for t in times:
        e_out=e_tot=0.0
        for j in range(0,N):
            x=xs[j]; p=pt=px=0j
            for n in keep:
                k=ks[n]; w=math.sqrt(k*k+m*m); ph=cmath.exp(1j*k*x)*fh[n]
                c=math.cos(w*t); s=math.sin(w*t)
                p+=ph*c; pt+=-ph*w*s; px+=1j*k*ph*c
            e=0.5*(pt.real**2+px.real**2+(m*p.real)**2)
            e_tot+=e
            if abs(x)>=abs(t)-R: e_out+=e
        out.append((t,e_out/e_tot))
    return out

if __name__=="__main__":
    for m in (0.0,0.3,1.0):
        res=run(m)
        print(f"m = {m}: "+"  ".join(f"t={t}: {fr:.4f}" for t,fr in res))
