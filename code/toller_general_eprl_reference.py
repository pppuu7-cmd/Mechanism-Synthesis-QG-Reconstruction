#!/usr/bin/env python3
"""High-precision general Toller t^± oracle in EPRL booster kinematics.

Implements Eqs. (43), (44), and Ruhl-phase Wigner d Eq. (71) of
Bianchi, Chen & Gamonal, arXiv:2604.24945 / Phys. Rev. D 114, 046014.

The ordinary EPRL booster code calls d^(rho,k)_{j l m} with k=j_external,
j=j_external and auxiliary l>=j. Therefore diagonal Eq. (46) is insufficient
once Dl>0; this oracle tests exactly the needed j->l sector.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import mpmath as mp
mp.mp.dps=80

def _i(x):
    y=int(mp.nint(x))
    if abs(x-y)>mp.mpf('1e-30'): raise ValueError(f'expected integer, got {x}')
    return y

def fac(x):
    n=_i(x)
    if n<0:return mp.mpf('0')
    return mp.factorial(n)

def C(n,r):
    n=_i(n);r=_i(r)
    if r<0 or r>n:return mp.mpf('0')
    return mp.mpf(math.comb(n,r))

def sgnpow(x):return mp.mpf(-1 if _i(x)%2 else 1)

def h2f1_unitdisk(a,b,c,z,tol=None,maxterms=200000):
    """Direct Gauss series for real 0<=z<1; avoids mpmath branch-selector bugs.

    The Toller formulas use z=exp(-2 beta), so this series is the natural stable
    definition for the low-beta scan.  We stop relative to the accumulated sum.
    """
    if tol is None: tol=mp.mpf(10)**(-(mp.mp.dps-15))
    term=mp.mpc(1);total=mp.mpc(1)
    for n in range(1,maxterms+1):
        term*=((a+n-1)*(b+n-1)/((c+n-1)*n))*z
        total_new=total+term
        if abs(term)<tol*max(mp.mpf(1),abs(total_new)):
            return total_new
        total=total_new
    raise RuntimeError(f'2F1 series did not converge: z={z}, a={a}, b={b}, c={c}')

def pref(j,l,m,k):
    return mp.sqrt((1+2*j)*(1+2*l))*mp.sqrt(fac(j-k)*fac(j+k)*fac(l-k)*fac(l+k)/(fac(j-m)*fac(j+m)*fac(l-m)*fac(l+m)))

def tplus(j,l,m,k,rho,beta):
    z=mp.e**(-2*beta);s=mp.mpc(0);P=pref(j,l,m,k)
    a1=max(0,_i(m+k));b1=min(_i(j+m),_i(j+k));a2=max(0,_i(m+k));b2=min(_i(l+m),_i(l+k))
    for n1 in range(a1,b1+1):
      for n2 in range(a2,b2+1):
        q=mp.gamma(j+k+m-n1-n2+mp.j*rho)/mp.gamma(1+j+mp.j*rho)
        q*=fac(-k-m+n1+n2)*C(j-m,-k-m+n1)*C(l-m,-k-m+n2)*C(j+m,n1)*C(l+m,n2)
        q*=sgnpow(j-l+n1+n2)*mp.e**(beta*(-1+k+m-2*n2+mp.j*rho))
        q*=h2f1_unitdisk(1-k-m+n1+n2,1+l-mp.j*rho,1-j-k-m+n1+n2-mp.j*rho,z)
        s+=q
    return P*s

def tminus(j,l,m,k,rho,beta):
    z=mp.e**(-2*beta);s=mp.mpc(0);P=pref(j,l,m,k)
    a1=max(0,_i(m-k));b1=min(_i(l+m),_i(l-k));a2=max(0,_i(m-k));b2=min(_i(j+m),_i(j-k))
    for n1 in range(a1,b1+1):
      for n2 in range(a2,b2+1):
        q=mp.gamma(l-k+m-n1-n2-mp.j*rho)/mp.gamma(1+l-mp.j*rho)
        q*=fac(k-m+n1+n2)*C(l-m,k-m+n1)*C(j-m,k-m+n2)*C(l+m,n1)*C(j+m,n2)
        q*=sgnpow(n1+n2)*mp.e**(beta*(-1-k+m-2*n2-mp.j*rho))
        q*=h2f1_unitdisk(1+k-m+n1+n2,1+j+mp.j*rho,1-l+k-m+n1+n2+mp.j*rho,z)
        s+=q
    return P*s

def d_ruhl(j,l,m,k,rho,beta):
    z=1-mp.e**(-2*beta);s=mp.mpc(0);P=pref(j,l,m,k)/fac(1+j+l)
    a1=max(0,_i(m-k));b1=min(_i(j+m),_i(j-k));a2=max(0,_i(m-k));b2=min(_i(l+m),_i(l-k))
    for n1 in range(a1,b1+1):
      for n2 in range(a2,b2+1):
        q=sgnpow(n1+n2)*C(j-m,k-m+n1)*C(l-m,k-m+n2)*C(j+m,n1)*C(l+m,n2)
        q*=fac(j-k+l+m-n1-n2)*fac(k-m+n1+n2)
        q*=mp.e**(beta*(-1-k+m-2*n1-mp.j*rho))
        q*=mp.hyp2f1(1+k-m+n1+n2,1+j+mp.j*rho,2+j+l,z)
        s+=q
    return P*s

def c(z):return [float(mp.re(z)),float(mp.im(z))]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-dl',type=int,default=3);ap.add_argument('--output',default='results/toller_general_eprl_reference.json');args=ap.parse_args()
    cases=[];worst=mp.mpf('0');worst_offdiag=mp.mpf('0')
    for two_j in (1,2):
      j=mp.mpf(two_j)/2;k=j
      for dl in range(args.max_dl+1):
        l=j+dl
        for two_m in range(-two_j,two_j+1,2):
          m=mp.mpf(two_m)/2
          for gamma in (mp.mpf('0.4'),mp.mpf('1.2')):
            rho=gamma*j
            for beta in (mp.mpf('0.3'),mp.mpf('0.8'),mp.mpf('1.7')):
              tp=tplus(j,l,m,k,rho,beta);tm=tminus(j,l,m,k,rho,beta);d=d_ruhl(j,l,m,k,rho,beta)
              r=abs(tp+tm-d)/max(abs(d),mp.mpf('1e-60'));worst=max(worst,r)
              if dl>0:worst_offdiag=max(worst_offdiag,r)
              cond=(abs(tp)+abs(tm))/max(abs(d),mp.mpf('1e-60'))
              cases.append({'j':float(j),'l':float(l),'m':float(m),'gamma':float(gamma),'beta':float(beta),'d_ruhl':c(d),'t_plus':c(tp),'t_minus':c(tm),'relative_sum_residual':float(r),'cancellation_condition':float(cond)})
    passed=worst<mp.mpf('1e-35')
    out={'paper_equations':[43,44,71],'kinematics':'k=j_external, rho=gamma*j_external, auxiliary l=j..j+Dl as required by EPRL booster decomposition','max_Dl_tested':args.max_dl,'cases':len(cases),'worst_relative_sum_residual':float(worst),'worst_offdiagonal_l_gt_j_residual':float(worst_offdiag),'passed':passed,'verdict':'GENERAL_TOLLER_J_TO_L_SUM_RULE_VERIFIED' if passed else 'GENERAL_TOLLER_REFERENCE_FAILED','implication':'Dl>0 causal booster requires general t_{j l m}; diagonal Eq.46 alone is insufficient','scope':'high-precision analytic oracle only; phase conversion to sl2cfoam convention audited separately; no F9 credit'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
