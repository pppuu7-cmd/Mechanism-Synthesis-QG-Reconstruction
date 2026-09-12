#!/usr/bin/env python3
"""Iter045: exact correlated K3 finite-part covariance audit.

Starting from the same source-faithful j=1/2 joint spectral density as Iter044,
subtract only the exact polynomial quotient in a chosen redundant cycle
coordinate and evaluate the symmetric Hadamard/PV remainder by residues.
The same physical rational density is parameterized independently by q1, q2,
or q3.  Equality of the resulting finite parts is a necessary coordinate-
covariance check for a candidate correlated extension.

This is a mathematical extension diagnostic.  It is not a causal-vertex
finiteness theorem and does not promote G3/F9/G8.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sympy as sp


def parse_signs(txt: str):
    if len(txt) != 3 or any(c not in '+-' for c in txt):
        raise ValueError('signs must be a three-character string such as ++-')
    return tuple(1 if c == '+' else -1 for c in txt)


def cpair(z, n=20):
    z = sp.N(z, n)
    return [str(sp.re(z)), str(sp.im(z))]


def build_kernel(gamma, epsilon, signs, k1, k2):
    t = sp.symbols('t', real=True)
    rho = gamma / 2
    s1, s2, s3 = signs
    den0 = rho**2 + sp.Rational(1, 4)
    c1 = 2*rho/den0
    c2 = 2/den0
    q1 = s1*(k1+s3*t)
    q2 = s2*(k2+s3*t)
    q3 = t

    def F(q, s):
        return sp.expand(1+c1*s*q+(c2/2)*q*q)

    num = sp.expand(F(q1,s1)*F(q2,s2)*F(q3,s3))
    den = sp.expand((q1-sp.I*epsilon)*(q2-sp.I*epsilon)*(q3-sp.I*epsilon))
    return t, (q1,q2,q3), sp.cancel(num/den), c1, c2


def finite_part_in_coordinate(t, qexpr, kernel):
    u = sp.symbols('u', real=True)
    slope = sp.simplify(sp.diff(qexpr,t))
    if slope == 0:
        raise ValueError('cycle coordinate has zero slope')
    # All K3 coordinates used here have |slope|=1.  Keep the real-line measure
    # explicitly to make the reparameterization convention visible.
    slope_int = int(slope)
    jac = sp.Rational(1, abs(slope_int))
    t_of_u = sp.solve(sp.Eq(u,qexpr),t)[0]
    Ku = sp.cancel(jac*kernel.subs(t,t_of_u))
    num, den = sp.fraction(Ku)
    Q, R = sp.div(num,den,u,domain='QQ_I')
    Q = sp.expand(Q)
    rem = sp.cancel(R/den)
    qdeg = -1 if Q == 0 else int(sp.Poly(Q,u).degree())
    a_minus1 = sp.simplify(sp.limit(u*rem,u,sp.oo))

    roots = list(sp.roots(den,u).keys())
    upper = []
    for r in roots:
        im = float(sp.N(sp.im(r),30))
        if im > 1e-14:
            upper.append(r)
        elif abs(im) <= 1e-14:
            raise ValueError(f'unexpected real-axis pole: {r}')

    residues = [sp.simplify(sp.limit((u-r)*rem,u,r)) for r in upper]
    fp = sp.simplify(2*sp.pi*sp.I*sum(residues)-sp.pi*sp.I*a_minus1)
    recon = sp.simplify(Ku-(Q+rem))
    return {
        'qdeg': qdeg,
        'Q': Q,
        'a_minus1': a_minus1,
        'roots': roots,
        'upper': upper,
        'fp': fp,
        'reconstruction_exact': recon == 0,
    }


def covariance_result(gamma_s, epsilon_s, signs_s, k1_s, k2_s):
    gamma = sp.Rational(gamma_s)
    eps = sp.Rational(epsilon_s)
    if eps <= 0:
        raise ValueError('epsilon must be positive')
    signs = parse_signs(signs_s)
    k1, k2 = sp.Rational(k1_s), sp.Rational(k2_s)
    t, qexprs, kernel, c1, c2 = build_kernel(gamma,eps,signs,k1,k2)
    rows = []
    fps = []
    for idx, qexpr in enumerate(qexprs, start=1):
        r = finite_part_in_coordinate(t,qexpr,kernel)
        fps.append(r['fp'])
        rows.append({
            'coordinate':f'q{idx}',
            'polynomial_quotient_degree':r['qdeg'],
            'a_minus1':cpair(r['a_minus1']),
            'finite_part':cpair(r['fp']),
            'upper_half_plane_pole_count':len(r['upper']),
            'reconstruction_exact':r['reconstruction_exact'],
        })

    diffs = [sp.simplify(fps[i]-fps[j]) for i in range(3) for j in range(i+1,3)]
    exact_equal = all(d == 0 for d in diffs)
    vals = [complex(sp.N(z,30)) for z in fps]
    scale = max(max(abs(z) for z in vals),1e-30)
    spread = max(abs(vals[i]-vals[j]) for i in range(3) for j in range(i+1,3))/scale
    qdeg3 = all(row['polynomial_quotient_degree'] == 3 for row in rows)
    recon = all(row['reconstruction_exact'] for row in rows)
    gates = {
        'exact_cycle_coordinate_finite_parts_equal': exact_equal,
        'numeric_relative_spread_lt_1e-11': spread < 1e-11,
        'exact_reconstruction_all_coordinates': recon,
        'pre_subtraction_polynomial_degree_three_all_coordinates': qdeg3,
    }
    return {
        'iteration':'Iter045A',
        'gamma':gamma_s,'epsilon':epsilon_s,'signs':signs_s,'k1':k1_s,'k2':k2_s,
        'rho':str(gamma/2),'c1':str(c1),'c2':str(c2),
        'finite_part_definition':'2*pi*i*sum_upper_residues - i*pi*a_minus1 after exact polynomial quotient subtraction',
        'rows':rows,
        'exact_pairwise_differences':[str(d) for d in diffs],
        'numeric_relative_spread':spread,
        'gates':gates,
        'classification':('K3_FINITE_PART_COORDINATE_COVARIANT' if all(gates.values()) else 'K3_FINITE_PART_COORDINATE_DEPENDENT'),
        'claim_lock':('Coordinate covariance is only a necessary structural property of this K3 finite-part candidate. '
                      'It does not prove the physical causal vertex, K4/K5 forest consistency, RG closure, G3, F9 or G8.'),
    }


def epsilon_scaling_result(gamma_s, signs_s, k1_s, k2_s, eps_list):
    rows=[]
    values=[]
    coord_ok=True
    for e in eps_list:
        r=covariance_result(gamma_s,e,signs_s,k1_s,k2_s)
        coord_ok = coord_ok and r['gates']['exact_cycle_coordinate_finite_parts_equal']
        z=complex(float(r['rows'][2]['finite_part'][0]),float(r['rows'][2]['finite_part'][1]))
        values.append(z)
        rows.append({'epsilon':e,'finite_part_q3':r['rows'][2]['finite_part'],
                     'coordinate_covariant_exactly':r['gates']['exact_cycle_coordinate_finite_parts_equal']})
    changes=[abs(values[i]-values[i-1]) for i in range(1,len(values))]
    ratios=[changes[i]/changes[i-1] if changes[i-1] else 0.0 for i in range(1,len(changes))]
    return {
        'iteration':'Iter045C','gamma':gamma_s,'signs':signs_s,'k1':k1_s,'k2':k2_s,
        'epsilon_sequence':eps_list,'rows':rows,'successive_absolute_changes':changes,
        'successive_change_ratios':ratios,
        'all_eps_coordinate_covariant_exactly':coord_ok,
        'last_step_absolute_change':changes[-1] if changes else None,
        'classification':'EPSILON_LIMIT_DIAGNOSTIC_RECORDED',
        'claim_lock':('Finite epsilon scaling is diagnostic only; a decreasing sequence is not by itself a theorem '
                      'of the distributional epsilon->0 limit or a physical vertex result.'),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['covariance','epsilon-scaling'],default='covariance')
    ap.add_argument('--gamma',required=True)
    ap.add_argument('--epsilon')
    ap.add_argument('--epsilon-list',default='0.2,0.05,0.01,0.002')
    ap.add_argument('--signs',required=True)
    ap.add_argument('--k1',required=True)
    ap.add_argument('--k2',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.mode == 'covariance':
        if not a.epsilon: raise SystemExit('--epsilon is required in covariance mode')
        out=covariance_result(a.gamma,a.epsilon,a.signs,a.k1,a.k2)
        ok=all(out['gates'].values())
    else:
        eps=[x.strip() for x in a.epsilon_list.split(',') if x.strip()]
        out=epsilon_scaling_result(a.gamma,a.signs,a.k1,a.k2,eps)
        ok=out['all_eps_coordinate_covariant_exactly']
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))
    if not ok: raise SystemExit(11)

if __name__=='__main__':
    main()
