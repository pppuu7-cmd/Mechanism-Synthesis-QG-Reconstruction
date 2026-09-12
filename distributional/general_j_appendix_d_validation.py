#!/usr/bin/env python3
"""Iteration 027B: Appendix-D distributional identity beyond j=1/2.

For half-integer/integer j the product polynomial is built directly as
  F_j(rho+y,rho)=prod_{m=-j}^j (i(rho+y)+m)/(i rho+m).
Writing F=1+sum a_n y^n gives c_n/n! = a_n and therefore
  delta^(rho,j)=sum_{n=0}^{2j} a_{n+1}(-i)^(n+1) delta^(n).

We validate product-vs-expanded polynomial identities, exact complementary
Theta_+ + Theta_- cancellation on Schwartz tests, and mollifier convergence
for j=1 and 3/2.  This is a distributional primitive test only; it does not
define products of boundary distributions at multi-wedge intersections.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps=70
QTEST=[mp.mpf(x) for x in ('-2.7','-1.1','-0.25','0','0.41','1.3','2.4')]
TESTS=[('a',mp.mpf('0.8'),mp.mpf('0.35'),mp.mpf('-0.15')),('b',mp.mpf('1.7'),mp.mpf('-0.2'),mp.mpf('0.25'))]
ETAS=[mp.mpf(x) for x in ('0.25','0.125','0.0625','0.03125')]

def fmt(x,n=22): return mp.nstr(x,n)
def cfmt(z): return [fmt(mp.re(z)),fmt(mp.im(z))]

def mvals(j2): return [mp.mpf(k)/2 for k in range(-j2,j2+1,2)]

def poly_coeffs(rho,j2):
    # coefficients ascending in y for prod_m (1 + i y/(i rho+m))
    c=[mp.mpc(1)]
    for m in mvals(j2):
        a=1j/(1j*rho+m); n=[mp.mpc(0)]*(len(c)+1)
        for k,z in enumerate(c): n[k]+=z; n[k+1]+=z*a
        c=n
    return c

def F_product(y,rho,j2):
    z=mp.mpc(1)
    for m in mvals(j2): z*=(1j*(rho+y)+m)/(1j*rho+m)
    return z

def F_expanded(y,c): return sum(z*y**k for k,z in enumerate(c))

def phi(x,a,b,c): return mp.e**(-a*x*x)*(1+b*x+c*x*x)
def dphi0(n,a,b,c): return mp.diff(lambda x:phi(x,a,b,c),0,n)

def target_boundary(coeff,a,b,c):
    z=mp.mpc(0)
    for n in range(len(coeff)-1):
        A=coeff[n+1]*(-1j)**(n+1)
        z += A*((-1)**n)*dphi0(n,a,b,c)
    return z

def delta_eta_deriv(x,eta,n):
    # d^n/dx^n [exp(-(x/eta)^2)/(sqrt(pi) eta)] using physicists Hermite recursion.
    u=x/eta; H0=mp.mpf(1)
    if n==0: H=H0
    else:
        H1=2*u
        if n==1: H=H1
        else:
            hm2,hm1=H0,H1
            for k in range(1,n): hm2,hm1=hm1,2*u*hm1-2*k*hm2
            H=hm1
    return ((-1)**n)*H*mp.e**(-u*u)/(mp.sqrt(mp.pi)*eta**(n+1))

def H_eta(x,eta): return (1+mp.erf(x/eta))/2

def mollified(rho,j2,sigma,eta,a,b,c):
    coeff=poly_coeffs(rho,j2)
    def f(x):
        bd=mp.mpc(0)
        for n in range(len(coeff)-1): bd += coeff[n+1]*(-1j)**(n+1)*delta_eta_deriv(x,eta,n)
        return (H_eta(sigma*x,eta)+sigma*bd)*phi(x,a,b,c)
    L=9*eta
    return mp.quad(f,[-mp.inf,-L,0,L,mp.inf])

def target(rho,j2,sigma,a,b,c):
    bulk=mp.quad(lambda x:phi(x,a,b,c),[0,mp.inf]) if sigma>0 else mp.quad(lambda x:phi(x,a,b,c),[-mp.inf,0])
    return bulk+sigma*target_boundary(poly_coeffs(rho,j2),a,b,c)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rho',required=True); ap.add_argument('--j2',type=int,choices=[2,3],required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); rho=mp.mpf(a.rho); coeff=poly_coeffs(rho,a.j2)
    perr=max(abs(F_product(q,rho,a.j2)-F_expanded(q,coeff)) for q in QTEST)
    comp=[]; last=[]; rows=[]
    for name,A,B,C in TESTS:
        tp=target(rho,a.j2,1,A,B,C); tm=target(rho,a.j2,-1,A,B,C); total=mp.quad(lambda x:phi(x,A,B,C),[-mp.inf,0,mp.inf]); comp.append(abs(tp+tm-total))
        for s,t in ((1,tp),(-1,tm)):
            vals=[]
            for e in ETAS:
                z=mollified(rho,a.j2,s,e,A,B,C); vals.append({'eta':fmt(e),'error':fmt(abs(z-t))})
            last.append(mp.mpf(vals[-1]['error'])); rows.append({'test':name,'sigma':s,'target':cfmt(t),'mollifier':vals})
    # Higher derivative mollifiers converge more slowly; threshold is intentionally diagnostic.
    ok=perr<mp.mpf('1e-58') and max(comp)<mp.mpf('1e-58') and max(last)<mp.mpf('0.08')
    out={'rho':a.rho,'j':str(mp.mpf(a.j2)/2),'coefficients':[cfmt(z) for z in coeff],'max_polynomial_identity_error':fmt(perr),'max_exact_complement_action_error':fmt(max(comp)),'max_smallest_eta_mollifier_error':fmt(max(last)),'rows':rows,'verdict':'GENERAL_J_APPENDIX_D_PASS' if ok else 'GENERAL_J_APPENDIX_D_REVIEW','guardrail':'General-j distributional primitive validation; not a product-of-distributions definition and not a multi-collision finiteness result.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
    if not ok: raise SystemExit(7)
if __name__=='__main__': main()
