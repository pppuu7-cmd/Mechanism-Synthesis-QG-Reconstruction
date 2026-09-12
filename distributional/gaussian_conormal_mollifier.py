#!/usr/bin/env python3
"""Iteration 028B: Gaussian conormal/transversality test on collision graphs.

For a connected graph G, fix one vertex and let A=B_G\otimes I_3 map local
boost tangent coordinates x in R^{3(V-1)} to one R^3 difference per edge.
Regularize every delta constraint with a normalized Gaussian of width s_e*eta
and test the product against exp(-|x|^2/2).  The integral is analytic:

 I_eta = (2pi)^((n-m)/2) eta^{-m} prod_i s_i^{-1}
         / sqrt(det(I + A^T W A / eta^2)),

where each scalar row belonging to edge e has W=1/s_e^2.
If rank(A)=m (transverse forest), I_eta has a finite eta->0 limit independent
of relative regulator widths.  If m>rank(A), it diverges as
eta^{rank-m}; the scaled divergent coefficient generically depends on the
relative widths, exposing extension-scheme dependence.

This is an exact Gaussian test of the collision-delta surrogate, not a claim
that the Appendix-D Toller boundary distribution equals delta^3(g_a-g_b).
"""
from __future__ import annotations

import argparse, json, math
from pathlib import Path
import numpy as np

ETAS=np.array([0.5,0.25,0.125,0.0625,0.03125,0.015625],dtype=float)
CASES={
 'edge2':(2,[(0,1)]),
 'path3':(3,[(0,1),(1,2)]),
 'triangle3':(3,[(0,1),(1,2),(0,2)]),
 'cycle4':(4,[(0,1),(1,2),(2,3),(3,0)]),
 'K4':(4,[(a,b) for a in range(4) for b in range(a+1,4)]),
 'K5':(5,[(a,b) for a in range(5) for b in range(a+1,5)]),
}


def incidence_lift(V,edges):
    # Fix vertex 0. One scalar incidence row per edge, then kron with I3.
    B=np.zeros((len(edges),V-1),dtype=float)
    for i,(a,b) in enumerate(edges):
        if a!=0:B[i,a-1]+=1.0
        if b!=0:B[i,b-1]-=1.0
    return np.kron(B,np.eye(3))


def log_integral(A, edge_scales, eta):
    n=A.shape[1]; m=A.shape[0]
    # repeat each edge scale for its 3 Cartesian constraint rows
    s=np.repeat(np.asarray(edge_scales,dtype=float),3)
    Aw=A/s[:,None]
    M=np.eye(n)+(Aw.T@Aw)/(eta*eta)
    sign,ld=np.linalg.slogdet(M)
    if sign<=0: raise RuntimeError('nonpositive Gaussian determinant')
    return ((n-m)/2)*math.log(2*math.pi)-m*math.log(eta)-float(np.log(s).sum())-0.5*ld


def fit_slope(xs,logs):
    x=np.log(xs[-4:]); y=np.asarray(logs[-4:]);
    return float(np.polyfit(x,y,1)[0])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    rows=[]
    for name,(V,edges) in CASES.items():
        A=incidence_lift(V,edges); rank=int(np.linalg.matrix_rank(A,tol=1e-11)); m=A.shape[0]
        cycle=len(edges)-V+1; excess=m-rank
        schemes={
          'uniform':[1.0]*len(edges),
          'alternating':[1.0 if i%2==0 else 2.0 for i in range(len(edges))],
          'graded':[1.0+0.35*i for i in range(len(edges))],
        }
        scheme_rows={}
        for sn,scales in schemes.items():
            logs=[log_integral(A,scales,e) for e in ETAS]
            slope=fit_slope(ETAS,logs)
            # remove predicted divergence eta^{-excess}; finite forests use exponent zero
            scaled=[math.exp(L+excess*math.log(e)) for L,e in zip(logs,ETAS)]
            scheme_rows[sn]={
                'fitted_eta_power':slope,
                'predicted_eta_power':-excess,
                'last_scaled_coefficient':scaled[-1],
                'scaled_coefficient_tail_ratio':scaled[-1]/scaled[-2],
            }
        coeffs=[v['last_scaled_coefficient'] for v in scheme_rows.values()]
        spread=max(coeffs)/min(coeffs) if min(coeffs)>0 else float('inf')
        rows.append({
          'case':name,'V':V,'E':len(edges),'cycle_rank':cycle,'rank':rank,
          'constraint_rows':m,'normal_excess':excess,
          'classification':'TRANSVERSE_FOREST' if excess==0 else 'NONTRANSVERSE_CYCLE',
          'schemes':scheme_rows,'regulator_coefficient_spread':spread,
        })
    forests=[r for r in rows if r['normal_excess']==0]
    cycles=[r for r in rows if r['normal_excess']>0]
    out={
      'eta_values':ETAS.tolist(),'rows':rows,
      'forest_max_abs_power_error':max(abs(r['schemes']['uniform']['fitted_eta_power']) for r in forests),
      'cycle_max_abs_power_error':max(abs(r['schemes']['uniform']['fitted_eta_power']+r['normal_excess']) for r in cycles),
      'cycle_min_regulator_coefficient_spread':min(r['regulator_coefficient_spread'] for r in cycles),
      'verdict':'GAUSSIAN_CONORMAL_TRANSVERSALITY_AUDIT_COMPLETE',
      'guardrail':('Analytic Gaussian-mollifier result for the linear collision-delta surrogate. '
                   'Nontransversality here motivates, but does not by itself specify, the extension of the exact Toller Feynman distribution.'),
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
