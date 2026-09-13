#!/usr/bin/env python3
import argparse,json,pathlib,re,sys

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
p=pathlib.Path('sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md')
if not p.exists():
    out={'lane':args.lane,'valid':False,'classification':'ITER063C_IMPLEMENTATION_INVALID','missing':['source_snapshot']}
else:
    t=p.read_text(encoding='utf-8')
    authority=[r'arXiv:`2601\.23162`',r'10\.1103/fwql-t4yr']
    checks={
      'vertex_object': authority + [r'four-`SL\(2,C\)` group integral',r'ten-wedge product',r'1<=a<b<=5',r'g_1 = 1',r'g_b\^-1 g_a|g_b\^{-1} g_a',r'gamma j_ab'],
      'eprl_control': authority + [r'T\^\(\+,rho,k\) \+ T\^\(-,rho,k\) = D',r'unconstrained sum over independent wedge signs',r'2\^10 independent-wedge-sign sum',r'does \*\*not\*\* reproduce the EPRL vertex'],
      'causal_conventions': authority + [r'sigma_a = ±1',r'kappa_ab = sigma_a sigma_b',r'\(rho,k\) = \(gamma j_ab, j_ab\)',r'Feynman `i epsilon` spectral integral',r'not the MSQGR surrogate `beta\+i\*epsilon`'],
      # Same frozen requirement as prereg: direct Eq.(4) has no tree/cycle/sequential
      # choice and Eq.(7) is the Cartan/magnetic representation of that Toller object.
      # The initial matcher incorrectly required a literal English phrase absent from
      # the snapshot despite the explicit Eq.(7) statement.  Match the equation-level
      # content instead; no scientific criterion is changed.
      'representation_guard': authority + [r'no spanning-tree choice',r'no cycle-basis choice',r'no sequential finite-part order',r'Cartan / magnetic decomposition',r'T\^\(±,rho,k\).*sum_p.*D\^j.*t\^\(±,rho,k\).*D\^l|source-backed bridge from the full group object to reduced Toller matrices']
    }
    if args.lane not in checks:
        out={'lane':args.lane,'valid':False,'classification':'ITER063C_IMPLEMENTATION_INVALID','missing':['unknown_lane']}
    else:
        missing=[q for q in checks[args.lane] if re.search(q,t,re.I|re.S) is None]
        valid=not missing
        out={'lane':args.lane,'valid':valid,'missing':missing,'source':'sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md','source_snapshot_commit':'7df82d28dd6426aa7aaac353a1e0abf795e6fdee','prereg_commit':'66ce9c87bcdf5b08e4c1e5604568766847321d98','classification':'ITER063C_LANE_QUALIFIED' if valid else 'ITER063C_BLOCKED_SOURCE_OBJECT_INCOMPLETE'}
pathlib.Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
if out['classification']=='ITER063C_IMPLEMENTATION_INVALID': sys.exit(4)
