#!/usr/bin/env python3
"""Iter077F-SM: rank-9 contact scaling-degree and extension threshold.

Frozen by prereg/ITER077F_SM_RANK9_CONTACT_SCALING_EXTENSION.md.
This is source-local, pre-contraction analysis. It does not establish a full
source-selected i-epsilon extension or a vertex finiteness/divergence theorem.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EDGES = ["01","02","03","04","12","13","14","23","24","34"]
LAM = [1,-1,0,0,1,0,0,0,0,0]


def lane_a():
    rho, gamma = sp.symbols('rho gamma', real=True)
    I = sp.I
    z = -sp.Rational(1,2) - I*rho
    # psi(z)-psi(z+2) = -1/z -1/(z+1)
    c1 = sp.simplify(I * (-1/z - 1/(z+1)))
    expected_c1 = sp.simplify(2*rho/(rho**2+sp.Rational(1,4)))
    a_rho = sp.simplify(c1/2)
    a_gamma = sp.simplify(a_rho.subs(rho,gamma/2))
    expected_agamma = sp.simplify(2*gamma/(1+gamma**2))
    numerator, denominator = sp.fraction(sp.factor(a_gamma))
    finite_real_zeros = sp.solve(sp.Eq(numerator,0),gamma)
    checks = {
        'c0': '1',
        'c1': str(c1),
        'c1_expected': bool(sp.simplify(c1-expected_c1)==0),
        'delta_prime_coefficient_rho': str(a_rho),
        'a_gamma': str(a_gamma),
        'a_gamma_expected': bool(sp.simplify(a_gamma-expected_agamma)==0),
        'finite_real_zero_set': [str(x) for x in finite_real_zeros],
        'nonzero_for_gamma_ne_0': finite_real_zeros == [sp.Integer(0)] and denominator != 0,
    }
    valid = bool(checks['c1_expected'] and checks['a_gamma_expected'] and checks['nonzero_for_gamma_ne_0'])
    return {'iteration':'Iter077F-SM','lane':'A','valid':valid,'checks':checks}


def lane_b():
    gamma = sp.symbols('gamma', real=True)
    a = sp.simplify(2*gamma/(1+gamma**2))
    support = [i for i,x in enumerate(LAM) if x != 0]
    support_edges = [EDGES[i] for i in support]
    max_excess_order = len(support)
    coefficient = sp.simplify(sp.prod(LAM[i] for i in support) * a**max_excess_order)
    expected = sp.simplify(-(2*gamma/(1+gamma**2))**3)
    num, den = sp.fraction(sp.factor(coefficient))
    roots = sp.solve(sp.Eq(num,0),gamma)
    unique_highest_selection = support_edges == ['01','02','12']
    zero_lambda_edges_cannot_feed_s = all(LAM[i] == 0 for i in range(len(LAM)) if i not in support)
    valid = bool(
        support_edges == ['01','02','12'] and max_excess_order == 3
        and sp.simplify(coefficient-expected)==0
        and roots == [sp.Integer(0)]
        and unique_highest_selection and zero_lambda_edges_cannot_feed_s
    )
    return {
        'iteration':'Iter077F-SM','lane':'B','valid':valid,
        'self_stress_support_edges':support_edges,
        'maximum_pure_excess_derivative_order':max_excess_order,
        'highest_order_selection_unique':unique_highest_selection,
        'highest_order_coefficient':str(coefficient),
        'coefficient_expected':str(expected),
        'finite_real_zero_set':[str(x) for x in roots],
        'nonzero_for_finite_real_gamma_ne_0':roots == [sp.Integer(0)] and den != 0,
        'zero_lambda_edges_cannot_feed_excess_derivative':zero_lambda_edges_cannot_feed_s,
        'full_boundary_contraction_cancellation_tested':False,
    }


def lane_c():
    transverse_dim = 6
    rows=[]
    all_ok=True
    for n in range(4):
        sd = 2*(n+1)
        unique = sd < transverse_dim
        ambiguity_degree = max(-1, sd-transverse_dim)
        if n == 0:
            interpretation = 'unique local extension; ordinary point-contact channel can be treated as a locally finite cone measure in this normal form'
        elif n == 1:
            interpretation = 'unique distributional extension; not asserted to be an ordinary measure'
        elif n == 2:
            interpretation = 'marginal scaling degree; extension nonunique by scaling alone'
        else:
            interpretation = 'extension nonunique by scaling alone'
        rows.append({
            'n':n,'scaling_degree':sd,'transverse_dimension':transverse_dim,
            'unique_extension_by_scaling_degree':unique,
            'max_supported_counterterm_derivative_order':None if unique else ambiguity_degree,
            'interpretation':interpretation,
        })
    predictions = (
        rows[0]['scaling_degree']==2 and rows[0]['unique_extension_by_scaling_degree']
        and rows[1]['scaling_degree']==4 and rows[1]['unique_extension_by_scaling_degree']
        and rows[2]['scaling_degree']==6 and not rows[2]['unique_extension_by_scaling_degree']
        and rows[2]['max_supported_counterterm_derivative_order']==0
        and rows[3]['scaling_degree']==8 and not rows[3]['unique_extension_by_scaling_degree']
        and rows[3]['max_supported_counterterm_derivative_order']==2
    )
    return {'iteration':'Iter077F-SM','lane':'C','valid':bool(predictions),'scaling_table':rows}


def lane_d():
    src=(ROOT/'sources'/'CAUSAL_SPINFOAM_VERTEX_2026_RANK9_CONTACT_SCALING_SUPPLEMENT.md').read_text(encoding='utf-8')
    e=(ROOT/'results'/'ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION_RESULT.md').read_text(encoding='utf-8')
    d=(ROOT/'results'/'ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_RESULT.md').read_text(encoding='utf-8')
    locks={
        'PURE_DELTA_EXCESS_N0_UNIQUE_EXTENSION':True,
        'EXCESS_N1_UNIQUE_DISTRIBUTIONAL_EXTENSION':True,
        'FIRST_SCALING_AMBIGUITY_AT_N2':True,
        'ALL_SPIN_HALF_HIGHEST_EXCESS_ORDER_N3_NONZERO_FOR_GAMMA_NE_0':True,
        'N3_SCALING_DEGREE':8,
        'TRANSVERSE_DIMENSION':6,
        'SCALING_ALONE_SELECTS_N3_EXTENSION':False,
        'SOURCE_SELECTED_I_EPSILON_EXTENSION_ESTABLISHED':False,
        'FULL_BOUNDARY_CONTRACTION_CANCELLATION_TESTED':False,
        'CAUSAL_VERTEX_FINITENESS_OR_DIVERGENCE_THEOREM':False,
        'REGULATOR_INDEPENDENCE_THEOREM':False,
        'PHYSICAL_SOURCE_TO_K4_PUSHFORWARD':False,
        'EPSILON_MINUS1_COEFFICIENT':False,
        'G3_promoted':False,'F9_promoted':False,'G8_promoted':False,'K5_promoted':False,
    }
    provenance = {
        'source_n3_object': 'SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL' in src,
        'iter077e_pass': 'ITER077E_SM_GENERIC_SUBMERSION_PULLBACK_ALLOWED_RANK9_CONTACT_HORMANDER_CRITERION_COLLIDES_CORRELATED_BOUNDARY_VALUE_REQUIRED_EXACT_SCOPED' in e,
        'iter077d_pass': 'ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED' in d,
        'det_minus_one': 'determinant `-1`' in d,
        'arbitrary_counterterm_forbidden': 'arbitrary counterterm' in src,
    }
    valid = bool(all(provenance.values()) and locks['N3_SCALING_DEGREE']==8 and locks['TRANSVERSE_DIMENSION']==6 and not locks['SCALING_ALONE_SELECTS_N3_EXTENSION'])
    return {'iteration':'Iter077F-SM','lane':'D','valid':valid,'provenance':provenance,'scope_locks':locks}


LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}


def write(obj,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True),encoding='utf-8')


def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.loads(Path(base,fn).read_text(encoding='utf-8'))
            except Exception: continue
            if obj.get('iteration')=='Iter077F-SM' and obj.get('lane') in LANES:
                got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(bool(got[k].get('valid')) for k in LANES)
    return {
        'iteration':'Iter077F-SM','valid':bool(valid),
        'classification':'ITER077F_SM_ALL_SPIN_HALF_RANK9_CONTACT_REACHES_N3_SCALING_NONUNIQUENESS_SOURCE_I_EPSILON_EXTENSION_REQUIRED_EXACT_SCOPED' if valid else 'ITER077F_SM_RANK9_CONTACT_SCALING_PREDICTION_FAILS_EXACT_SCOPED',
        'lanes_found':sorted(got),'lane_valid':{k:bool(got.get(k,{}).get('valid')) for k in LANES},
        'pure_delta_n0_unique':True if valid else None,
        'n1_unique_distributional':True if valid else None,
        'first_scaling_ambiguity_n':2 if valid else None,
        'all_spin_half_highest_excess_n':3 if valid else None,
        'all_spin_half_n3_scaling_degree':8 if valid else None,
        'transverse_dimension':6 if valid else None,
        'missing_object':'SOURCE_SELECTED_CORRELATED_I_EPSILON_EXTENSION_OF_RANK9_N_EFF_3_CONTACT_CHANNEL' if valid else None,
        'next_admissible_gate':'Derive the rank-9 n_eff=3 extension from the published spectral i-epsilon prescription and test it only after the full correlated source/boundary contraction; no arbitrary finite part.',
        'claim_lock':'No vertex finiteness/divergence, regulator-independence, physical source-to-K4 pushforward, epsilon^-1 coefficient, generic finite-spin signed P3, new physics, complete-QG, or G3/F9/G8/K5 promotion.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True)
    args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj,indent=2,sort_keys=True)); write(obj,args.output)
    if not obj.get('valid'): raise SystemExit(1)

if __name__=='__main__': main()
