#!/usr/bin/env python3
"""Iter044: source-faithful joint K3 spectral common-cycle audit.

This works before multiplying boundary-supported distributions. For the K3
boundary coordinates (u,v,-u-v), define Fourier combinations
  k1=s1*q1-s3*q3, k2=s2*q2-s3*q3,
and common cycle variable t=q3. The published j=1/2 finite-spectral-epsilon
integrand is then a rational function of t. Exact polynomial division isolates
whether the common spectral cycle direction carries a non-decaying polynomial
piece. This is an obstruction to the naive joint spectral integral only; it is
not a physical divergence theorem and does not define a finite part.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def parse_signs(txt: str):
    if len(txt) != 3 or any(c not in '+-' for c in txt):
        raise ValueError('signs must be like +++ or ++-')
    return tuple(1 if c == '+' else -1 for c in txt)


def cplx(z, n=18):
    z = sp.N(z, n)
    return [str(sp.re(z)), str(sp.im(z))]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gamma', required=True)
    ap.add_argument('--epsilon', required=True)
    ap.add_argument('--signs', required=True)
    ap.add_argument('--k1', default='0.37')
    ap.add_argument('--k2', default='-0.61')
    ap.add_argument('--output', required=True)
    a=ap.parse_args()

    gamma=sp.Rational(a.gamma); rho=gamma/2; eps=sp.Rational(a.epsilon)
    k1=sp.Rational(a.k1); k2=sp.Rational(a.k2)
    s1,s2,s3=parse_signs(a.signs)
    t=sp.symbols('t', real=True)
    I=sp.I

    den0=rho**2+sp.Rational(1,4)
    c1=2*rho/den0; c2=2/den0
    q1=s1*(k1+s3*t); q2=s2*(k2+s3*t); q3=t
    def F(q,s): return sp.expand(1+c1*s*q+(c2/2)*q*q)
    num=sp.expand(F(q1,s1)*F(q2,s2)*F(q3,s3))
    den=sp.expand((q1-I*eps)*(q2-I*eps)*(q3-I*eps))
    Q,R=sp.div(num,den,t,domain='QQ_I')
    Q=sp.expand(Q); R=sp.expand(R)

    qpoly=sp.Poly(Q,t)
    qdeg=(-1 if Q == 0 else int(qpoly.degree()))
    coeffs={str(p): cplx(qpoly.coeff_monomial(t**p)) for p in range(max(qdeg,0),-1,-1)} if Q != 0 else {}
    even_nonzero=[]
    if Q != 0:
        for p in range(qdeg,-1,-1):
            cc=sp.simplify(qpoly.coeff_monomial(t**p))
            if p % 2 == 0 and cc != 0: even_nonzero.append((p,cc))
    highest_even=(even_nonzero[0][0] if even_nonzero else None)

    # Exact reconstruction plus independent numerical probes.
    recon=sp.simplify(num/den-(Q+R/den))
    probes=[sp.Rational(-37,10),sp.Rational(-11,10),sp.Rational(2,5),sp.Rational(19,10),sp.Rational(43,10)]
    max_rel=0.0
    for tv in probes:
        z=complex(sp.N((num/den).subs(t,tv),30))
        zr=complex(sp.N((Q+R/den).subs(t,tv),30))
        max_rel=max(max_rel,abs(z-zr)/max(abs(z),1e-30))

    # EPRL/no-contact control F=1.
    ctrl_num=sp.Integer(1)
    ctrl_den=den
    CQ,CR=sp.div(ctrl_num,ctrl_den,t,domain='QQ_I')
    ctrl_q_zero=(sp.expand(CQ)==0)
    ctrl_asym_degree=sp.Poly(ctrl_num,t).degree()-sp.Poly(ctrl_den,t).degree()

    gates={
      'exact_division_identity': recon == 0,
      'numeric_reconstruction_relerr_lt_1e-11': max_rel < 1e-11,
      'source_polynomial_quotient_nonzero': Q != 0,
      'eprl_control_no_polynomial_quotient': ctrl_q_zero,
      'eprl_control_asymptotic_degree_minus3': int(ctrl_asym_degree) == -3,
    }
    obstruction=all(gates.values())
    out={
      'iteration':'Iter044','gamma':a.gamma,'rho':str(rho),'epsilon':a.epsilon,
      'signs':a.signs,'k1':a.k1,'k2':a.k2,'c1':str(c1),'c2':str(c2),
      'source_numerator_degree':int(sp.Poly(num,t).degree()),
      'source_denominator_degree':int(sp.Poly(den,t).degree()),
      'source_asymptotic_degree':int(sp.Poly(num,t).degree()-sp.Poly(den,t).degree()),
      'polynomial_quotient_degree':qdeg,
      'polynomial_quotient_coefficients':coeffs,
      'highest_nonzero_even_quotient_power':highest_even,
      'predicted_symmetric_cutoff_growth_power':(highest_even+1 if highest_even is not None else None),
      'max_numeric_reconstruction_relative_error':max_rel,
      'eprl_control_asymptotic_degree':int(ctrl_asym_degree),
      'gates':gates,
      'classification':('JOINT_K3_COMMON_CYCLE_SPECTRAL_OBSTRUCTION' if obstruction else 'JOINT_K3_SPECTRAL_AUDIT_REVIEW'),
      'claim_lock':('A nonzero common-cycle polynomial quotient obstructs the naive source-faithful joint K3 spectral integral along the redundant cycle direction. It does not prove physical causal-vertex divergence, does not choose a finite part or counterterm, and does not promote G3/F9/G8. A correlated Feynman/extension prescription remains the next object.'),
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if not all(gates.values()): raise SystemExit(9)

if __name__=='__main__': main()
