#!/usr/bin/env python3
import argparse,json,pathlib,sys
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()

def read(p):
    q=pathlib.Path(p)
    return q.read_text(encoding='utf-8') if q.exists() else ''

def has(p,*terms):
    t=read(p)
    return bool(t) and all(x in t for x in terms)

lane=a.lane
valid=False; source_incompatible=False; evidence=[]; missing=[]

if lane=='source_prescription':
    # Existing support-native construction explicitly disclaims equality to the physical source prescription;
    # K3 is source-faithful but K4 sequential extension is order dependent.
    p='regulated/correlated_cutspace_extension_audit.py'; t=read(p)
    evidence.append(p)
    if not t: missing.append(p)
    if 'does not establish that the physical causal EPRL/Toller spectral prescription equals' in t:
        missing.append('source-faithful correlated K5 finite-spectral-i-epsilon equality/derivation')
    if not has('status/ITERATION_044.md','JOINT_K3_COMMON_CYCLE_SPECTRAL_OBSTRUCTION'):
        missing.append('Iter044 source-faithful joint-spectral authority')
    if not has('status/ITERATION_046.md','K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT'):
        missing.append('Iter046 K4 multi-cycle authority')
    valid=not missing
elif lane=='extension_selection':
    evidence += ['status/ITERATION_039.md','status/ITERATION_040.md','status/ITERATION_042.md']
    known=(has('status/ITERATION_039.md','S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16 = FALSE') and
           has('status/ITERATION_040.md','QUADRATIC_ISOTROPIZATION_GENERATES_ALL_S5_INVARIANTS_THROUGH_16 = FALSE') and
           has('status/ITERATION_042.md','EDGE_LOCAL_APPENDIXD_SOURCE_UNIQUELY_SELECTS_EXTENSION = FALSE'))
    if not known: missing.append('terminal ambiguity-localization authorities')
    # No source-derived K5 selector has been promoted in the durable chain.
    if known: missing.append('source-derived selector/excluder for remaining K5 primitive extension directions')
    valid=False
elif lane=='order_regulator':
    evidence += ['status/ITERATION_045.md','status/ITERATION_046.md','status/ITERATION_063A_RESULT.md']
    if not has('status/ITERATION_045.md','K3_FINITE_PART_COORDINATE_COVARIANT'):
        missing.append('K3 correlated finite-part covariance')
    if has('status/ITERATION_046.md','K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT'):
        missing.append('K5 correlated prescription with regulator/order independence')
    else: missing.append('validated multi-cycle order/regulator authority')
    # Iter063A geometric tree/cycle prescription independence cannot replace distributional-extension order independence.
    valid=False
elif lane=='eprl_distributional_control':
    evidence += ['status/ITERATION_063C_RESULT.md','status/ITERATION_064A_RESULT.md','status/ITERATION_046.md']
    pointwise=(has('status/ITERATION_063C_RESULT.md','ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED') and
               has('status/ITERATION_064A_RESULT.md','ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS'))
    if not pointwise: missing.append('source/pointwise EPRL authority')
    # Explicitly require distributional, not pointwise/no-contact-only, control.
    missing.append('distributional K5 Eq.(5)/(6) independent-wedge EPRL control')
    valid=False
else:
    out={'lane':lane,'valid':False,'classification':'ITER065A_IMPLEMENTATION_INVALID','missing':['unknown lane']}
    pathlib.Path(a.output).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2)); sys.exit(4)

classification='ITER065A_LANE_QUALIFIED' if valid else ('ITER065A_K5_SCIENTIFIC_FAIL_SOURCE_INCOMPATIBLE_EXTENSION' if source_incompatible else 'ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING')
out={'lane':lane,'valid':bool(valid),'classification':classification,'evidence':evidence,'missing':missing,'prereg_commit':'987b0b27aaccc9e75ceed5fe209e9944a17f5e94','scope':'qualification only; blocked is not divergence/nonexistence'}
pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8'); print(json.dumps(out,indent=2,sort_keys=True))
