#!/usr/bin/env python3
"""Iter077D-SM: exact mixed second jet of the true causal-vertex B-map.

Frozen by prereg/ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET.md.
No microlocal pullback, full-vertex finiteness, source-to-K4 pushforward, or
regulator-removal claim is made here.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EDGES = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
EX = sp.Matrix([1,0,0])
EY = sp.Matrix([0,1,0])
EZ = sp.Matrix([0,0,1])
NORMALS = [EX,EX,EX,EX,EX,EY,EY,EY,EZ,EZ]
LAM = sp.Matrix([1,-1,0,0,1,0,0,0,0,0])


def true_j() -> sp.Matrix:
    J = sp.zeros(10,12)
    for r, ((a,b), n) in enumerate(zip(EDGES, NORMALS)):
        for node in range(1,5):
            s = (1 if a == node else 0) - (1 if b == node else 0)
            for i in range(3):
                J[r,3*(node-1)+i] = s*n[i]
    return J


def kernel_basis() -> sp.Matrix:
    # Columns: common-y, z-at-node1, common-z-at-nodes2,3,4.
    R = sp.zeros(12,3)
    for node in range(1,5):
        R[3*(node-1)+1,0] = 1
    R[2,1] = 1
    for node in (2,3,4):
        R[3*(node-1)+2,2] = 1
    return R


def edge_difference_map(a: int, b: int) -> sp.Matrix:
    M = sp.zeros(3,12)
    if a != 0:
        for i in range(3): M[i,3*(a-1)+i] += 1
    if b != 0:
        for i in range(3): M[i,3*(b-1)+i] -= 1
    return M


def full_group_hessian() -> sp.Matrix:
    H = sp.zeros(12,12)
    I3 = sp.eye(3)
    for lam, (a,b), n in zip(LAM, EDGES, NORMALS):
        if lam == 0: continue
        M = edge_difference_map(a,b)
        P = I3 - n*n.T
        H += lam * M.T * P * M
    return sp.simplify(H)


def mixed_block(R: sp.Matrix) -> sp.Matrix:
    # Columns are eta_01^y, eta_01^z, eta_02^z.
    selected = [(0,EY),(0,EZ),(1,EZ)]
    L = sp.zeros(3,3)
    for q in range(3):
        x = R[:,q]
        for k,(edge_idx,tangent) in enumerate(selected):
            a,b = EDGES[edge_idx]
            d = edge_difference_map(a,b) * x
            L[q,k] = sp.simplify(LAM[edge_idx] * (tangent.T*d)[0])
    return L


def is_zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(v) == 0 for v in M)


def lane_a():
    src1 = (ROOT/'sources'/'CAUSAL_SPINFOAM_VERTEX_2026_TRUE_B_MAP_TRANSVERSALITY_SUPPLEMENT.md').read_text(encoding='utf-8')
    src2 = (ROOT/'sources'/'CAUSAL_SPINFOAM_VERTEX_2026_B_MAP_SECOND_JET_SUPPLEMENT.md').read_text(encoding='utf-8')
    ares = (ROOT/'results'/'ITER077A_TRUE_SOURCE_B_MAP_TRANSVERSALITY_RESULT.md').read_text(encoding='utf-8')
    cres = (ROOT/'results'/'ITER077C_SM_SOURCE_COLLISION_EXCEPTIONAL_STRATA_RESULT.md').read_text(encoding='utf-8')
    checks = {
        'first_jet_formula': 'dB_ab = n_ab . (dx_a-dx_b)' in src1,
        'second_jet_formula': 'B_ab = n_ab . d_ab + (1/2)(|d_ab|^2-(n_ab . d_ab)^2) + O(3)' in src2,
        'mixed_jet_formula': 'eta_ab . d_ab' in src2,
        'iter077a_pass': 'ITER077A_TRUE_SOURCE_B_MAP_HAS_GENERIC_FULL_RANK_COLLISION_WITNESS_SCALAR_K5_CYCLE_RELATIONS_DO_NOT_TRANSFER_EXACT_SCOPED' in ares,
        'iter077c_pass': 'ITER077C_SM_SOURCE_COLLISION_RANK9_EXCEPTIONAL_STRATUM_TRANSVERSE_CODIM3_EXACT_SCOPED' in cres,
        'frozen_witness': 'xxxxxyyyzz' in cres,
        'frozen_lambda': 'lambda=(1,-1,0,0,1,0,0,0,0,0)' in cres,
        'pullback_firewall': 'does **not** prove' in cres or 'does **not** by itself' in src2,
    }
    return {'iteration':'Iter077D-SM','lane':'A','valid':all(checks.values()),'checks':checks}


def lane_b():
    t = sp.symbols('t')
    ax,ay,az,cx,cy,cz = sp.symbols('ax ay az cx cy cz', real=True)
    I = sp.I
    sx = sp.Matrix([[0,1],[1,0]])
    sy = sp.Matrix([[0,-I],[I,0]])
    sz = sp.Matrix([[1,0],[0,-1]])
    I2 = sp.eye(2)
    avec = sp.Matrix([ax,ay,az]); cvec = sp.Matrix([cx,cy,cz]); d = avec-cvec
    A = (ax*sx+ay*sy+az*sz)/2
    C = (cx*sx+cy*sy+cz*sz)/2
    Lf = I2 - t*C + t**2*(C*C)/2
    Mid = I2 + 2*t*A + 2*t**2*(A*A)
    prod = Lf*Mid*Lf
    coeff1 = prod.applyfunc(lambda e: sp.expand(e).coeff(t,1))
    coeff2 = prod.applyfunc(lambda e: sp.expand(e).coeff(t,2))
    expect1 = d[0]*sx+d[1]*sy+d[2]*sz
    expect2 = sp.Rational(1,2)*(d.dot(d))*I2
    matrix_linear_ok = is_zero_matrix(sp.simplify(coeff1-expect1))
    matrix_quad_ok = is_zero_matrix(sp.simplify(coeff2-expect2))

    u,v = sp.symbols('u v', real=True)
    scalar = sp.series(sp.log(1+t*u+t**2*v),t,0,3).removeO().expand()
    log1 = sp.simplify(scalar.coeff(t,1)-u) == 0
    log2 = sp.simplify(scalar.coeff(t,2)-(v-u**2/2)) == 0
    # For v=|d|^2/2 this is exactly 1/2(|d|^2-(n.d)^2).
    eta_dot_d, eps = sp.symbols('eta_dot_d eps', real=True)
    mixed = sp.expand(t*(u+eps*eta_dot_d))
    mixed_ok = sp.simplify(mixed.coeff(t,1).coeff(eps,1)-eta_dot_d) == 0
    valid = bool(matrix_linear_ok and matrix_quad_ok and log1 and log2 and mixed_ok)
    return {
        'iteration':'Iter077D-SM','lane':'B','valid':valid,
        'pauli_linear_identity':bool(matrix_linear_ok),
        'pauli_quadratic_identity':bool(matrix_quad_ok),
        'log_linear_identity':bool(log1),'log_quadratic_identity':bool(log2),
        'normal_group_mixed_term':bool(mixed_ok),
    }


def lane_c():
    J = true_j(); R = kernel_basis()
    Hfull = full_group_hessian(); Hg = sp.simplify(R.T*Hfull*R)
    L = mixed_block(R)
    H6 = Hg.row_join(L).col_join(L.T.row_join(sp.zeros(3,3)))
    rankJ = J.rank(); left_nullity = 10-rankJ; right_nullity = 12-rankJ
    lambda_ok = (LAM.T*J == sp.zeros(1,12))
    kernel_ok = (J*R == sp.zeros(10,3)) and R.rank()==3
    expected_Hg = sp.Matrix([[0,0,0],[0,2,-1],[0,-1,0]])
    hg_ok = Hg == expected_Hg
    group_rank = Hg.rank()
    # The nonzero 2x2 block has determinant -1, proving opposite signs; the first basis vector is null.
    group_signature_ok = group_rank==2 and sp.det(Hg[1:3,1:3])==-1 and Hg[0,:]==sp.zeros(1,3) and Hg[:,0]==sp.zeros(3,1)
    l_rank = L.rank(); l_det = sp.det(L)
    h6_rank = H6.rank(); h6_det = sp.det(H6)
    Linv = L.inv()
    T = sp.eye(6)
    T[3:6,0:3] = -sp.Rational(1,2)*Linv*Hg
    target = sp.zeros(6,6)
    target[0:3,3:6] = L
    target[3:6,0:3] = L.T
    congruence_ok = sp.simplify(T.T*H6*T) == target
    # target is congruent via diag(I,L^-1) to [[0,I],[I,0]], which has inertia (3,3).
    S = sp.eye(6)
    S[3:6,3:6] = L.inv()
    canonical = sp.zeros(6,6)
    canonical[0:3,3:6] = sp.eye(3)
    canonical[3:6,0:3] = sp.eye(3)
    inertia_reduction_ok = sp.simplify(S.T*target*S) == canonical
    valid = bool(
        rankJ==9 and left_nullity==1 and right_nullity==3 and lambda_ok and kernel_ok
        and hg_ok and group_signature_ok and l_rank==3 and abs(int(l_det))==1
        and h6_rank==6 and h6_det==-1 and congruence_ok and inertia_reduction_ok
    )
    return {
        'iteration':'Iter077D-SM','lane':'C','valid':valid,
        'rank_J':rankJ,'left_nullity':left_nullity,'right_nullity':right_nullity,
        'lambda_left_null':bool(lambda_ok),'kernel_basis_exact':bool(kernel_ok),
        'H_group':[[str(x) for x in Hg.row(i)] for i in range(3)],
        'H_group_rank':group_rank,'H_group_signature':'(+,-,0)' if group_signature_ok else 'unverified',
        'L':[[str(x) for x in L.row(i)] for i in range(3)],
        'L_rank':l_rank,'L_det':str(l_det),
        'H6_rank':h6_rank,'H6_det':str(h6_det),
        'exact_congruence_to_offdiagonal':bool(congruence_ok),
        'exact_inertia_reduction_to_exchange_form':bool(inertia_reduction_ok),
        'H6_inertia':'(3+,3-)' if inertia_reduction_ok else 'unverified',
    }


def lane_d():
    J = true_j(); R = kernel_basis(); Hg = sp.simplify(R.T*full_group_hessian()*R); L = mixed_block(R)
    q = sp.Matrix(sp.symbols('q0:3', real=True)); eta = sp.Matrix(sp.symbols('e0:3', real=True)); t = sp.symbols('t', real=True)
    phi2 = sp.expand((sp.Rational(1,2)*(q.T*Hg*q)[0]) + (q.T*L*eta)[0])
    scaled = sp.expand((sp.Rational(1,2)*((t*q).T*Hg*(t*q))[0]) + ((t*q).T*L*(t*eta))[0])
    scaling_ok = sp.simplify(scaled-t**2*phi2)==0
    linear_zero = (LAM.T*J*R == sp.zeros(1,3))
    locks = {
        'HORMANDER_PULLBACK_AT_EXCEPTIONAL_STRATUM': False,
        'CORRELATED_TOLLER_GROUP_BOUNDARY_VALUE': False,
        'PHYSICAL_SOURCE_TO_K4_PUSHFORWARD': False,
        'PHYSICAL_REDUCED_K4_NUMERATOR_COEFFICIENT': False,
        'EPSILON_MINUS1_COEFFICIENT': False,
        'CAUSAL_VERTEX_FINITE_OR_DIVERGENT_THEOREM': False,
        'G3_promoted':False,'F9_promoted':False,'G8_promoted':False,'K5_promoted':False,
    }
    valid = bool(linear_zero and scaling_ok and L.rank()==3 and all(v is False for v in locks.values()))
    return {
        'iteration':'Iter077D-SM','lane':'D','valid':valid,
        'linear_term_zero_on_group_kernel':bool(linear_zero),
        'quadratic_homogeneous_scaling':bool(scaling_ok),
        'mixed_block_rank':L.rank(),
        'second_jet_expression':str(phi2),
        'scope_locks':locks,
    }


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
            if obj.get('iteration')=='Iter077D-SM' and obj.get('lane') in LANES:
                got[obj['lane']]=obj
    valid=set(got)==set(LANES) and all(bool(got[k].get('valid')) for k in LANES)
    return {
        'iteration':'Iter077D-SM','valid':bool(valid),
        'classification':'ITER077D_SM_RANK9_TRUE_B_MAP_MIXED_SECOND_JET_NONDEGENERATE_6D_EXACT_SCOPED' if valid else 'ITER077D_SM_RANK9_TRUE_B_MAP_SECOND_JET_DEGENERACY_PERSISTS_OR_SOURCE_PREDICTION_FAILS_EXACT_SCOPED',
        'lanes_found':sorted(got),'lane_valid':{k:bool(got.get(k,{}).get('valid')) for k in LANES},
        'next_admissible_gate':'Use the exact quadratic normal form with the source-selected 1D contact distribution to test local microlocal pullback/scaling at the rank-9 exceptional stratum.',
        'claim_lock':'No exceptional-stratum Hormander pullback theorem, correlated K5 boundary value, physical source-to-K4 pushforward, epsilon^-1 coefficient, vertex finiteness/divergence theorem, regulator-independence theorem, generic finite-spin signed P3, new physics, complete QG, or G3/F9/G8/K5 promotion.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=LANES); ap.add_argument('--aggregate-dir'); ap.add_argument('--output',required=True)
    args=ap.parse_args()
    if bool(args.lane)==bool(args.aggregate_dir): raise SystemExit('choose exactly one of --lane or --aggregate-dir')
    obj=LANES[args.lane]() if args.lane else aggregate(args.aggregate_dir)
    print(json.dumps(obj,indent=2,sort_keys=True)); write(obj,args.output)
    if not obj.get('valid'): raise SystemExit(1)


if __name__=='__main__': main()
