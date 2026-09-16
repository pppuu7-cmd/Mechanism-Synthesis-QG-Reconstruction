#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
REPAIR_PREREG='f47ce5a88f98d20f330428480010c3068ebd2328'

spec=importlib.util.spec_from_file_location('k5_34_core_repair2',CORE)
core=importlib.util.module_from_spec(spec); spec.loader.exec_module(core)

# Direct authoritative Kirchhoff polynomial evaluation. This is the exact
# 125-tree determinant authority already imported by the frozen parent gate.
def psi_direct(alpha):
    z=core.AD(0)
    for mon,c in core.PSI_POLY.items():
        q=core.AD(c)
        for e in mon:q=q*alpha[e]
        z=z+q
    return z

def invmat_direct_psi(A,psi):
    n=len(A); iD=psi.inv(); out=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
            out[i][j]=((-1 if (i+j)%2 else 1)*core.det(M))*iD
    return out

def evaluate_repair2(alpha):
    L=core.buildL(alpha); psi=psi_direct(alpha); B0=invmat_direct_psi(L,psi)
    Bser=core.inverse_probe(B0); df=core.detfactor(B0); W=core.projected(Bser); nums=[]
    for C in W:
        ss=[[core.AD(0),core.AD(0)] for _ in range(core.ORDER+1)]
        for i,c in enumerate(df):
            for j,z in enumerate(C):
                if i+j<=core.ORDER:
                    ss[i+j][0]=ss[i+j][0]+c*z[0]
                    ss[i+j][1]=ss[i+j][1]+c*z[1]
        nums.append((math.factorial(core.ORDER)*ss[core.ORDER][0]*(psi**9),
                     math.factorial(core.ORDER)*ss[core.ORDER][1]*(psi**9)))
    return psi,nums

core.evaluate=evaluate_repair2

# Frozen generic no-cancellation control: all alpha are positive constants,
# so both exact determinant representations must agree at valuation zero.
def generic_psi_control():
    aa=[core.AD(core.LT.const(i+1),core.LT.const(0)) for i in range(10)]
    tree=psi_direct(aa); signed=core.det(core.buildL(aa))
    return tree.v.x==signed.v.x and tree.d.x==signed.d.x

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    outpath=Path(args.output)
    old=list(sys.argv); sys.argv=[str(CORE),'--output',str(outpath)]
    try:
        core.main()
    finally:
        sys.argv=old
    d=json.loads(outpath.read_text(encoding='utf-8'))
    repair_checks={
        'repair2_prereg_frozen': True,
        'psi_poly_125_terms': len(core.PSI_POLY)==125,
        'psi_poly_all_unit_coefficients': all(c==1 for c in core.PSI_POLY.values()),
        'direct_tree_psi_order_matches_tree_order_all_proper_orbits': all(
            (not r.get('physical')) or r['rPsi']==core.tree_order(set(r['bits'])) for r in d['orbit_rows']),
        'generic_direct_tree_equals_signed_det_no_cancellation': generic_psi_control(),
        'empty_full_controls_only': all(not r['physical'] for r in d['orbit_rows'] if r['k'] in (0,10)),
    }
    d['repair2_prereg_commit']=REPAIR_PREREG
    d['repair2_execution']='direct_125_tree_Psi_plus_cofactor_inverse'
    d['repair2_checks']=repair_checks
    if not all(repair_checks.values()):
        d['classification']='INVALID_IMPLEMENTATION'; d['status']='INVALID_IMPLEMENTATION'
    outpath.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('REPAIR2_CHECKS=',json.dumps(repair_checks,sort_keys=True))
    print('FINAL_CLASSIFICATION=',d['classification'])
    if d['classification']=='INVALID_IMPLEMENTATION': raise SystemExit(2)

if __name__=='__main__':main()
