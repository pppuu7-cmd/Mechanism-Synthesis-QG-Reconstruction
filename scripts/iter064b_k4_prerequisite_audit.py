#!/usr/bin/env python3
import argparse,json,pathlib,sys

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
ROOT=pathlib.Path('.')

def text(path):
    p=ROOT/path
    return p.read_text(encoding='utf-8') if p.exists() else ''

def req(path,terms):
    t=text(path)
    return {'path':str(path),'exists':bool(t),'missing':[x for x in terms if x not in t]}

checks=[]
if a.lane=='source_order':
    checks += [
      req(pathlib.Path('status/ITERATION_059_RESULT.md'),['K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED','34721276444','does **not** establish']),
      req(pathlib.Path('status/ITERATION_060_RESULT.md'),['K4_SOURCE_REVERSAL_ANALYTICITY_GEOMETRY_COVARIANT','34724006585']),
      req(pathlib.Path('status/ITERATION_062_RESULT.md'),['K4_ORDERED_ORIENTATION_BRIDGE_COVARIANT_CONVENTION_UNFIXED','34726816242'])]
elif a.lane=='basis_permutation':
    checks += [req(pathlib.Path('status/ITERATION_063A_RESULT.md'),['K4_ORDERED_BRIDGE_TREE_CYCLE_PRESCRIPTION_INDEPENDENT','34729151990','6144'])]
elif a.lane=='eprl_control':
    checks += [
      req(pathlib.Path('status/ITERATION_063C_RESULT.md'),['ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED','34732046499','unconstrained']),
      req(pathlib.Path('status/ITERATION_064A_RESULT.md'),['ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS','34732198011','2^10','not** equated'])]
elif a.lane=='scope_lock':
    files=['status/ITERATION_059_RESULT.md','status/ITERATION_060_RESULT.md','status/ITERATION_062_RESULT.md','status/ITERATION_063A_RESULT.md','status/ITERATION_063C_RESULT.md','status/ITERATION_064A_RESULT.md']
    checks += [req(pathlib.Path(f),[]) for f in files]
else:
    out={'lane':a.lane,'valid':False,'classification':'ITER064B_IMPLEMENTATION_INVALID','checks':[]}; pathlib.Path(a.output).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2)); sys.exit(4)

valid=all(c['exists'] and not c['missing'] for c in checks)
if a.lane=='scope_lock' and valid:
    combined='\n'.join(text(pathlib.Path(c['path'])) for c in checks)
    # Require explicit negative scope language rather than inferring absence from silence.
    guards=['not establish','does not establish','not a four-group Haar integration','does not promote']
    valid=all(g.lower() in combined.lower() for g in guards)
    if not valid: checks.append({'path':'combined-scope','exists':True,'missing':[g for g in guards if g.lower() not in combined.lower()]})
out={'lane':a.lane,'valid':bool(valid),'classification':'ITER064B_LANE_PASS' if valid else 'ITER064B_K5_REMAINS_BLOCKED_PREREQUISITE_GAP','checks':checks,'prereg_commit':'90e835e5c77290f768c6db2984441f8d30334882'}
pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(out,indent=2,sort_keys=True))
