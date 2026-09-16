#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE_PATH=ROOT/'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
PREREG='3e5303665ecd423b84745e9b74c7a5682116685e'
CYCLE=(1,2,3,4,0)

spec=importlib.util.spec_from_file_location('compressed_s5_core',CORE_PATH)
core=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(core)

def invperm(p): return tuple(p.index(i) for i in range(len(p)))

def edge_sign(p,i):
    a,b=core.EDGES[i]
    return 1 if p[a] < p[b] else -1

def canon_matching(mt,p):
    out=[]
    for i,j in mt:
        a,b=core.ep(p,i),core.ep(p,j)
        out.append((min(a,b),max(a,b)))
    return tuple(sorted(out))

def mulc(s,z): return (Fraction(s)*z[0],Fraction(s)*z[1])

def transform_dict(d,p):
    global_sign=1
    for i in range(10): global_sign*=edge_sign(p,i)
    out={}
    collision=False
    for mt,chs in d.items():
        k=canon_matching(mt,p)
        val=tuple(mulc(global_sign,z) for z in chs)
        if k in out and out[k]!=val: collision=True
        out[k]=val
    return out,global_sign,collision

def enc(d):
    return {str(k):[[str(z[0]),str(z[1])] for z in v] for k,v in sorted(d.items(),key=lambda kv:str(kv[0]))}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    base=core.MATCH_COEFF
    fwd,sgn,col1=transform_dict(base,CYCLE)
    back,sgn2,col2=transform_dict(fwd,invperm(CYCLE))
    keys_exact=set(fwd)==set(base)
    coeff_exact=keys_exact and all(fwd[k]==base[k] for k in base)
    roundtrip=set(back)==set(base) and all(back[k]==base[k] for k in base)
    checks={
      'nonempty_match_coeff':bool(base),
      'ten_edges':len(core.EDGES)==10,
      'cycle_is_permutation':sorted(CYCLE)==list(range(5)),
      'forward_key_coverage_preserved':len(fwd)==len(base),
      'no_forward_key_collision':not col1,
      'no_inverse_key_collision':not col2,
      'inverse_roundtrip_exact':roundtrip,
    }
    valid=all(checks.values())
    if not valid: cls='INVALID_IMPLEMENTATION'
    elif coeff_exact: cls='COMPRESSED_SOURCE_S5_COVARIANCE_EXACT'
    else: cls='COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT'
    mism=[]
    if valid and not coeff_exact:
        for k in sorted(set(base)|set(fwd),key=str):
            if base.get(k)!=fwd.get(k):
                mism.append({'matching':str(k),'base':None if k not in base else [[str(x) for x in z] for z in base[k]],'transported':None if k not in fwd else [[str(x) for x in z] for z in fwd[k]]})
                if len(mism)>=12: break
    out={'gate':'K5_EXACT_CANCELLATION_COMPRESSED_SOURCE_S5_DIAGNOSTIC','prereg_commit':PREREG,'cycle':list(CYCLE),'inverse_cycle':list(invperm(CYCLE)),'matching_keys':len(base),'orientation_global_sign':sgn,'inverse_orientation_global_sign':sgn2,'checks':checks,'keys_exact':keys_exact,'coefficients_exact':coeff_exact,'mismatch_sample':mism,'classification':cls,'physical_corner_coefficients_used':False,'scientific_verdict':None}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True); Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 2 if cls=='INVALID_IMPLEMENTATION' else 0

if __name__=='__main__': raise SystemExit(main())