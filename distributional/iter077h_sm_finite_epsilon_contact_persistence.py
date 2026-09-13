#!/usr/bin/env python3
"""Iter077H-SM: finite spectral epsilon does not smooth the j=1/2 contact subterm."""
from __future__ import annotations

import argparse
import itertools
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
I = sp.I
LAM = [1, -1, 0, 0, 1, 0, 0, 0, 0, 0]


def lane_a():
    rho, eps, p = sp.symbols("rho eps p", real=True)
    sigma = sp.symbols("sigma", real=True, nonzero=True)
    D = rho**2 + sp.Rational(1,4)
    c1, c2 = 2*rho/D, 2/D
    a = I*sigma*eps
    F = 1 + c1*p + c2*p**2/2
    Q = c2*p/2 + c1 + a*c2/2
    R = 1 + a*c1 + a**2*c2/2
    division_ok = sp.expand(F - ((p-a)*Q + R)) == 0
    pole_prefactor = sp.simplify(R.subs(sigma**2,1))
    delta_coeff = sp.simplify(-I*(sigma*c1 + I*eps*c2/2))
    delta_prime_coeff = sp.simplify(-sigma*c2/2)
    exp_delta = sp.simplify((eps-2*I*sigma*rho)/D)
    exp_dp = sp.simplify(-sigma/D)
    expected_pole = sp.simplify(1 + (2*I*sigma*rho*eps-eps**2)/D)
    checks = {
        "division": bool(division_ok),
        "pole": sp.simplify(pole_prefactor-expected_pole)==0,
        "delta": sp.simplify(delta_coeff-exp_delta)==0,
        "delta_prime": sp.simplify(delta_prime_coeff-exp_dp)==0,
    }
    passed = all(checks.values())
    return {"iteration":"Iter077H-SM","lane":"A","valid":True,"scientific_outcome":"PASS" if passed else "FAIL","checks":checks,"pole_prefactor":str(pole_prefactor),"delta_coefficient":str(delta_coeff),"delta_prime_coefficient":str(delta_prime_coeff)}


def lane_b():
    rho, eps, gamma = sp.symbols("rho eps gamma", real=True)
    sigma = sp.symbols("sigma", real=True, nonzero=True)
    D = rho**2+sp.Rational(1,4)
    c1,c2=2*rho/D,2/D
    delta_eps=sp.simplify(eps*c2/2-I*sigma*c1)
    dp_eps=sp.simplify(-sigma*c2/2)
    dp_derivative=sp.diff(dp_eps,eps)
    A_gamma=sp.simplify(delta_eps.subs(rho,gamma/2))
    C_gamma=sp.simplify(dp_eps.subs(rho,gamma/2))
    limit_delta=sp.limit(delta_eps,eps,0,dir='+')
    expected_limit=-I*sigma*2*rho/D
    expected_dp=-sigma/D
    checks={
      "delta_prime_epsilon_independent":sp.simplify(dp_derivative)==0,
      "delta_prime_nonzero_symbolic":sp.factor(C_gamma)!=0,
      "A_gamma":sp.simplify(A_gamma-4*(eps-I*sigma*gamma)/(1+gamma**2))==0,
      "C_gamma":sp.simplify(C_gamma+4*sigma/(1+gamma**2))==0,
      "boundary_delta":sp.simplify(limit_delta-expected_limit)==0,
      "boundary_delta_prime":sp.simplify(dp_eps-expected_dp)==0,
    }
    passed=all(checks.values())
    return {"iteration":"Iter077H-SM","lane":"B","valid":True,"scientific_outcome":"PASS" if passed else "FAIL","checks":checks,"A_gamma":str(A_gamma),"C_gamma":str(C_gamma)}


def lane_c():
    gamma=sp.Rational(6,5); eps=sp.Rational(1,7); t=sp.symbols("t", real=True)
    failures=[]; leading_values=[]
    for signs in itertools.product((-1,1), repeat=10):
        poly=sp.Integer(1)
        for s,lam in zip(signs,LAM):
            A=sp.simplify(4*(eps-I*s*gamma)/(1+gamma**2))
            C=sp.simplify(-4*s/(1+gamma**2))
            poly*=A+I*C*t*lam
        poly=sp.expand(poly)
        degree=sp.Poly(poly,t).degree()
        lead=sp.simplify(sp.Poly(poly,t).LC())
        if degree!=3 or lead==0:
            failures.append("".join('+' if x==1 else '-' for x in signs))
        leading_values.append(lead)
    passed=len(failures)==0
    return {"iteration":"Iter077H-SM","lane":"C","valid":True,"scientific_outcome":"PASS" if passed else "FAIL","sign_assignments_checked":1024,"failures":failures,"all_degree_three_nonzero":passed,"distinct_leading_coefficients":len(set(map(str,leading_values))),"gamma":"6/5","epsilon":"1/7","symbolic_nonvanishing_condition":"finite real gamma; epsilon>0: every A_e=4(epsilon-i sigma_e gamma)/(1+gamma^2) and C_e=-4 sigma_e/(1+gamma^2) is nonzero"}


def lane_d():
    prereg=(ROOT/"prereg"/"ITER077H_SM_FINITE_EPSILON_CONTACT_PERSISTENCE.md").read_text(encoding="utf-8")
    source=(ROOT/"sources"/"ITER077H_SM_FINITE_EPSILON_JHALF_CONTACT_DERIVATION.md").read_text(encoding="utf-8")
    gres=(ROOT/"results"/"ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING_RESULT.md").read_text(encoding="utf-8")
    locks={
      "finite_eps_formula":"delta-prime coefficient is **independent of epsilon**" in source,
      "source_ordering_next":"ordering of source operations" in prereg,
      "no_nonexistence":"nonexistence of the full source-selected correlated boundary value" in prereg,
      "no_full_divergence":"full causal-vertex divergence" in prereg,
      "g_authority":"ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED" in gres,
    }
    passed=all(locks.values())
    return {"iteration":"Iter077H-SM","lane":"D","valid":True,"scientific_outcome":"PASS" if passed else "FAIL","classification_scope":"FINITE_SPECTRAL_EPSILON_DOES_NOT_TERMWISE_SMOOTH_THE_JHALF_CONTACT_SUBTERM","locks":locks}

LANES={"A":lane_a,"B":lane_b,"C":lane_c,"D":lane_d}

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: o=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if o.get('iteration')=='Iter077H-SM' and o.get('lane') in LANES: got[o['lane']]=o
    present=set(got)==set(LANES)
    if not present:
        return {"iteration":"Iter077H-SM","execution_valid":False,"verdict":"BLOCKED","classification":"ITER077H_SM_FINITE_EPSILON_CONTACT_BLOCKED_OBJECT_DEFINITION","lanes_found":sorted(got)}
    outcomes={k:got[k].get('scientific_outcome') for k in LANES}
    verdict='PASS' if all(v=='PASS' for v in outcomes.values()) else 'FAIL'
    cls='ITER077H_SM_FINITE_SPECTRAL_EPSILON_LEAVES_NONZERO_RANK9_N3_PURE_CONTACT_SUBTERM_CORRELATED_SOURCE_ORDERING_STILL_REQUIRED_EXACT_SCOPED' if verdict=='PASS' else 'ITER077H_SM_FINITE_EPSILON_CONTACT_PREDICTION_FAILS_EXACT_SCOPED'
    return {"iteration":"Iter077H-SM","execution_valid":True,"verdict":verdict,"classification":cls,"lane_scientific_outcomes":outcomes,"finite_epsilon_termwise_smoothing_resolves_rank9_contact":False if verdict=='PASS' else None,"next_admissible_gate":"Test an actual source ordering: integrate each CP1 wedge to a Toller function before K5 multiplication, or construct a jointly correlated spectral/group boundary value, then include smooth phase/measure/intertwiner factors."}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True); a=ap.parse_args()
    if bool(a.lane)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
    o=LANES[a.lane]() if a.lane else aggregate(a.aggregate_dir)
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(o,indent=2,sort_keys=True))
    if a.lane and not o.get('valid',False): raise SystemExit(1)
    if a.aggregate_dir and not o.get('execution_valid',False): raise SystemExit(1)
if __name__=='__main__': main()
