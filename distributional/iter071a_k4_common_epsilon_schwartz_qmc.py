#!/usr/bin/env python3
"""Iter071A: common-epsilon K4 Schwartz-action convergence pilot.

Frozen by status/ITERATION_071A_PREREG.md. This is a numerical pilot only.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.stats import qmc, norm
from distributional.k4_forest_order_finite_part import constrained_edge_flows, TREES

SIGMAS=['++++','+++-','++-+','++--','+-++','+-+-','+--+','+---']
EPS=np.array([0.20,0.10,0.05,0.025,0.0125],dtype=float)
SEEDS=[7101,7102,7103,7104]
M=16
GAMMA=1.2

def causal_signs(label):
    sg=[1 if c=='+' else -1 for c in label]
    return np.array([sg[a]*sg[b] for a,b in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]],dtype=float)

def linear_matrix(tree):
    y,x,_,_,det=constrained_edge_flows(tree,(sp.Integer(0),)*4)
    L=np.zeros((6,3),dtype=float)
    for e,xe in enumerate(x):
        for j,v in enumerate(y):
            L[e,j]=float(sp.diff(xe,v))
        if sp.simplify(xe-sum(sp.Rational(str(L[e,j]))*y[j] for j in range(3)))==0:
            pass
    return L,int(det)

def pair(z): return [float(np.real(z)),float(np.imag(z))]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--tree',required=True,choices=sorted(TREES)); ap.add_argument('--sigma',required=True,choices=SIGMAS); ap.add_argument('--output',required=True); a=ap.parse_args()
    L,tree_det=linear_matrix(a.tree)
    Q=L.T@L
    eig=np.linalg.eigvalsh(Q)
    p1=bool(np.all(eig>1e-12))
    C=np.linalg.cholesky(Q)
    jac=float(1.0/abs(np.linalg.det(C)))
    p1=bool(p1 and bool(np.isfinite(jac)) and jac>0)
    signs=causal_signs(a.sigma)
    rho=GAMMA/2.0; den0=rho*rho+0.25; c1=2*rho/den0; c2=2/den0
    all_est={}; finite=True; stable=True
    for eps in EPS:
        all_est[str(float(eps))]={}
        scramble_vals={0:[],1:[],2:[]}
        for seed in SEEDS:
            sampler=qmc.Sobol(d=3,scramble=True,seed=seed)
            u=sampler.random_base2(M)
            u=np.clip(u,1e-15,1-1e-15)
            z=norm.ppf(u)/math.sqrt(2.0)
            y=np.linalg.solve(C.T,z.T).T
            x=y@L.T
            numer=np.prod(1.0+c1*x+(c2/2.0)*x*x,axis=1)
            denom=np.prod(x-1j*float(eps)*signs[None,:],axis=1)
            ker=numer/denom
            polys=[np.ones(len(x)),1.0+x[:,0]-2.0*x[:,4]+x[:,5],1.0+x[:,0]*x[:,5]-x[:,1]*x[:,4]]
            pref=(math.pi**1.5)*jac
            for ti,poly in enumerate(polys):
                val=pref*np.mean(ker*poly)
                scramble_vals[ti].append(val)
        for ti in range(3):
            vals=np.asarray(scramble_vals[ti],dtype=np.complex128)
            mean=np.mean(vals)
            spread=float(np.max(np.abs(vals-mean))/max(1.0,abs(mean)))
            ok=bool(np.all(np.isfinite(vals.real)) and np.all(np.isfinite(vals.imag)))
            finite=bool(finite and ok)
            stable=bool(stable and spread<=0.05)
            all_est[str(float(eps))][f'G{ti}']={'scrambles':[pair(v) for v in vals],'mean':pair(mean),'normalized_scramble_spread':spread}
    cauchy=True; trend=True; convergence={}
    for ti in range(3):
        means=[]
        for eps in EPS:
            re,im=all_est[str(float(eps))][f'G{ti}']['mean']; means.append(complex(re,im))
        df=float(abs(means[-1]-means[-2])); dp=float(abs(means[-2]-means[-3]))
        relf=float(df/max(1.0,abs(means[-1])))
        ok4=bool(relf<=0.20); ok5=bool(df<=1.10*dp)
        cauchy=bool(cauchy and ok4); trend=bool(trend and ok5)
        convergence[f'G{ti}']={'final_difference':df,'previous_difference':dp,'final_normalized_difference':relf,'P4':ok4,'P5':ok5}
    valid=bool(p1 and finite)
    passed=bool(valid and stable and cauchy and trend)
    if not valid: cls='ITER071A_NUMERICAL_VALIDITY_FAIL'
    elif passed: cls='ITER071A_LANE_COMMON_EPSILON_SCHWARTZ_CONVERGENCE_SUPPORTED'
    else: cls='ITER071A_LANE_COMMON_EPSILON_SCHWARTZ_REVIEW'
    out={'iteration':'Iter071A','tree':a.tree,'sigma':a.sigma,'gamma':float(GAMMA),'epsilon_sequence':[float(v) for v in EPS],
         'sobol_seeds':list(SEEDS),'points_per_scramble':int(2**M),'Q':Q.tolist(),'Q_eigenvalues':[float(v) for v in eig],'whitening_jacobian':jac,'tree_incidence_det':int(tree_det),
         'estimates':all_est,'convergence':convergence,
         'predicates':{'P1_Q_POSITIVE_AND_JACOBIAN_VALID':bool(p1),'P2_ALL_ESTIMATES_FINITE':bool(finite),'P3_SCRAMBLE_STABILITY':bool(stable),'P4_FINAL_CAUCHY_BOUND':bool(cauchy),'P5_FINAL_STEP_NOT_WORSENING':bool(trend)},
         'valid':valid,'lane_pass':passed,'classification':cls,
         'claim_lock':'Reduced K4 common-epsilon Schwartz-action numerical pilot only; no S-prime theorem, arbitrary-path independence, K5 vertex theorem, or promotion.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('estimates','Q')},indent=2,sort_keys=True))
    if not valid: raise SystemExit(9)
if __name__=='__main__': main()
