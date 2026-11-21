"""Spherically symmetric Klein-Gordon field in 3+1 dimensions, via p = r*phi.

p solves the 1+1 Klein-Gordon equation on the line with odd data, and its line energy
is the energy of phi. We take odd data p(0,r) = r*exp(-(r/w)^2), p_t(0,r) = 0, solve
exactly mode by mode on a periodic box, and report (i) the fraction of energy outside
the past cone of the central event (0,0), shrunk by R, and (ii) the central reading
phi(t,0) = p_r(t,0). For m > 0 the outside fraction tends to 0 (Proposition 1). For
m = 0 it stays near 1. A numerical illustration with its stated domain only.
"""
import cmath, math

def run(m,N=1024,L=1600.0,w=2.0,R=10.0,times=(-50,-100,-200,-400,-700)):
    dx=L/N; xs=[(j-N//2)*dx for j in range(N)]
    f=[x*math.exp(-(x/w)**2) for x in xs]
    ks=[2*math.pi*(n if n<N//2 else n-N)/L for n in range(N)]
    fh=[sum(f[j]*cmath.exp(-1j*ks[n]*xs[j]) for j in range(N))/N for n in range(N)]
    top=max(abs(v) for v in fh); keep=[n for n in range(N) if abs(fh[n])>1e-14*top]
    out=[]
    for t in times:
        e_out=e_tot=0.0
        for x in xs:
            p=pt=px=0j
            for n in keep:
                k=ks[n]; om=math.sqrt(k*k+m*m); ph=cmath.exp(1j*k*x)*fh[n]
                c=math.cos(om*t); s=math.sin(om*t)
                p+=ph*c; pt+=-ph*om*s; px+=1j*k*ph*c
            e=0.5*(pt.real**2+px.real**2+(m*p.real)**2); e_tot+=e
            if abs(x)>=abs(t)-R: e_out+=e
        centre=sum((1j*ks[n]*fh[n]*math.cos(math.sqrt(ks[n]**2+m*m)*t)).real for n in keep)
        out.append((t,e_out/e_tot,centre))
    return out

if __name__=="__main__":
    for m in (0.0,0.3,1.0):
        print(f"m = {m}")
        for t,fr,c in run(m): print(f"   t = {t:5d}   energy outside cone {fr:.4f}   phi(t,0) = {c:+.3e}")
