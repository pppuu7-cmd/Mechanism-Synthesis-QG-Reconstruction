#!/usr/bin/env python3
"""Iteration 028: linearized multi-wedge boundary-distribution intersection audit.

Purpose
-------
Appendix-D causal boundary primitives contain delta and delta-derivative terms
at the spectral boundary.  Before multiplying many such primitives on a cyclic
vertex graph, test the cheapest necessary geometric condition: are the
linearized edge constraints independent?

For K_k choose one vertex as gauge/root.  Each edge spectral boundary variable
is linearized as y_ab = x_a - x_b, with x_root=0.  The E=k(k-1)/2 edge forms
are rows of the reduced incidence matrix B, whose rank is k-1 and cycle nullity
is E-(k-1).  A product of Gaussian delta mollifiers

    I_eta = int exp(-|x|^2) prod_e delta_eta((B x)_e) dx

is evaluated exactly as a Gaussian integral.  If E>rank(B), the redundant
constraints generate a power divergence eta^{-(E-rank)}.  This is a necessary
warning for a naive pointwise product of the singular boundary pieces.

The script also verifies that the lowest delta coefficient in the Appendix-D
primitive is nonzero for the requested (rho,j), so the diagnostic term is
actually present before any sector/intertwiner cancellation.

Guardrail: this is a linearized common-spectral-coordinate / mollifier audit.
It is NOT a proof that the full group-valued Feynman-i-epsilon amplitude is
undefined.  Distributional extensions, correlated prescriptions, matrix
cancellations, or source-derived counterterms may still define the full object.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

ETAS=np.array([0.2,0.1,0.05,0.025,0.0125,0.00625],dtype=float)


def incidence(k:int)->np.ndarray:
    # root vertex k-1 is gauge fixed; columns are x_0...x_{k-2}
    rows=[]
    for a in range(k):
        for b in range(a+1,k):
            r=np.zeros(k-1,float)
            if a<k-1: r[a]+=1.0
            if b<k-1: r[b]-=1.0
            rows.append(r)
    return np.asarray(rows)


def poly_coeffs(rho:float,j2:int):
    # F=prod_m [1 + i y/(i rho+m)], ascending coefficients in y.
    c=np.array([1+0j],dtype=np.complex128)
    for m2 in range(-j2,j2+1,2):
        m=m2/2.0
        a=1j/(1j*rho+m)
        n=np.zeros(len(c)+1,dtype=np.complex128)
        n[:-1]+=c
        n[1:]+=c*a
        c=n
    return c


def exact_delta_product_integral(B:np.ndarray,eta:float)->float:
    # delta_eta(t)=exp(-(t/eta)^2)/(sqrt(pi)*eta)
    # exp(-x^T x) * prod exp(-(b_e.x)^2/eta^2)
    E=B.shape[0]
    A=np.eye(B.shape[1])+(B.T@B)/(eta*eta)
    sign,logdet=np.linalg.slogdet(A)
    if sign<=0: raise RuntimeError('nonpositive Gaussian matrix')
    # integral over R^d exp(-x^T A x)=pi^(d/2)/sqrt(det A)
    d=B.shape[1]
    logI=(d/2.0)*math.log(math.pi)-0.5*logdet-E*(0.5*math.log(math.pi)+math.log(eta))
    return math.exp(logI)


def fit_divergence(etas,vals):
    # I ~ eta^{-p}; fit last four points.
    x=np.log(etas[-4:]); y=np.log(vals[-4:])
    slope=np.polyfit(x,y,1)[0]
    return float(-slope)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--k',type=int,choices=[3,4,5],required=True)
    ap.add_argument('--rho',type=float,required=True)
    ap.add_argument('--j2',type=int,choices=[1,2,3],required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()

    B=incidence(a.k)
    E=B.shape[0]; rank=int(np.linalg.matrix_rank(B,tol=1e-12)); nullity=E-rank
    s=np.linalg.svd(B,compute_uv=False)
    coeff=poly_coeffs(a.rho,a.j2)
    # delta^(rho,j) coefficient multiplying delta(x): a1*(-i)
    delta0=coeff[1]*(-1j)
    vals=np.array([exact_delta_product_integral(B,e) for e in ETAS])
    pfit=fit_divergence(ETAS,vals)
    expected=float(nullity)
    exponent_error=abs(pfit-expected)

    out={
      'k':a.k,'rho':a.rho,'j':a.j2/2.0,
      'edges_E':E,'reduced_incidence_dimension':a.k-1,'incidence_rank':rank,
      'cycle_nullity_E_minus_rank':nullity,
      'singular_values':[float(x) for x in s],
      'appendix_D_delta0_coefficient':[float(delta0.real),float(delta0.imag)],
      'appendix_D_delta0_abs':float(abs(delta0)),
      'etas':ETAS.tolist(),'regularized_delta_product_integrals':vals.tolist(),
      'fitted_divergence_exponent':pfit,
      'expected_redundancy_exponent':expected,
      'exponent_error':exponent_error,
      'naive_pointwise_delta_product_locally_stable':bool(nullity==0),
      'verdict':('REDUNDANT_BOUNDARY_CONSTRAINT_POWER_DIVERGENCE'
                 if nullity>0 and abs(delta0)>1e-12 and exponent_error<0.08
                 else 'REVIEW_REQUIRED'),
      'guardrail':(
        'Linearized reduced-incidence Gaussian-mollifier audit of the lowest delta boundary term only. '
        'It excludes a regulator-independent naive pointwise product for this term when the predicted redundancy power is seen; '
        'it does not exclude a source-backed correlated i-epsilon/distributional extension or cancellations in the full amplitude.'
      )
    }
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if out['verdict']=='REVIEW_REQUIRED': raise SystemExit(7)

if __name__=='__main__': main()
