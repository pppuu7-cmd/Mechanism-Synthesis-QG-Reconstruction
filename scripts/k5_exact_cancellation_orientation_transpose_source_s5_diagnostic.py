#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CORE_PATH=ROOT/'scripts/k5_34_orbit_physical_numerator_action_flux_audit.py'
PREREG='3090c19b968edc7a34e6b6e08c65e8a00465971e'
CYCLE=(1,2,3,4,0)

spec=importlib.util.spec_from_file_location('orientation_transpose_core',CORE_PATH)
core=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(core)

def invperm(p): return tuple(p.index(i) for i in range(len(p)))

def edge_sign(p,i):
    a,b=core.EDGES[i]
    return 1 if p[a] < p[b] else -1

def transform_types(types,p):
    out=[None]*10
    for i,(r,c) in enumerate(types):
        j=core.ep(p,i)
        out[j]=(r,c) if edge_sign(p,i)==1 else (c,r)
    assert all(z is not None for z in out)
    return tuple(out)

def transform_tcw(d,p):
    out={}; collision=False
    for types,w in d.items():
        k=transform_types(types,p)
        if k in out and out[k]!=w: collision=True
        out[k]=w
    return out,collision

def recompress(tcw):
    mc=defaultdict(lambda:[[Fraction(0),Fraction(0)],[Fraction(0),Fraction(0)]])
    for types,w in tcw.items():
        for mt,z in core.compatible(types):
            for ch in (0,1):
                if w[ch]:
                    zz=core.cscale(w[ch],z)
                    mc[mt][ch][0]+=zz[0]; mc[mt][ch][1]+=zz[1]
    return {mt:((c[0][0],c[0][1]),(c[1][0],c[1][1])) for mt,c in mc.items() if any(c[ch] != [0,0] for ch in (0,1))}

def encw(w): return [str(w[0]),str(w[1])]
def encchs(v): return [[str(z[0]),str(z[1])] for z in v]

def sample_diff(a,b,kind,limit=12):
    out=[]
    for k in sorted(set(a)|set(b),key=str):
        if a.get(k)!=b.get(k):
            if kind=='tcw':
                av=None if k not in a else encw(a[k]); bv=None if k not in b else encw(b[k])
            else:
                av=None if k not in a else encchs(a[k]); bv=None if k not in b else encchs(b[k])
            out.append({'key':str(k),'base':av,'transported':bv})
            if len(out)>=limit: break
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    base=core.TCW
    fwd,col1=transform_tcw(base,CYCLE)
    back,col2=transform_tcw(fwd,invperm(CYCLE))
    fwd_keys=set(fwd)==set(base)
    tcw_exact=fwd_keys and all(fwd[k]==base[k] for k in base)
    roundtrip=set(back)==set(base) and all(back[k]==base[k] for k in base)
    recomp=recompress(fwd)
    match_keys=set(recomp)==set(core.MATCH_COEFF)
    match_exact=match_keys and all(recomp[k]==core.MATCH_COEFF[k] for k in core.MATCH_COEFF)
    base_recomp=recompress(base)
    base_compression_exact=(base_recomp==core.MATCH_COEFF)
    reversals=sum(edge_sign(CYCLE,i)==-1 for i in range(10))
    invreversals=sum(edge_sign(invperm(CYCLE),i)==-1 for i in range(10))
    checks={
      'ten_edges':len(core.EDGES)==10,
      'cycle_is_permutation':sorted(CYCLE)==list(range(5)),
      'inverse_is_permutation':sorted(invperm(CYCLE))==list(range(5)),
      'tcw_nonempty':bool(base),
      'tcw_forward_key_coverage':len(fwd)==len(base),
      'no_tcw_forward_collision':not col1,
      'no_tcw_inverse_collision':not col2,
      'tcw_inverse_roundtrip_exact':roundtrip,
      'base_recompression_equals_authoritative_match_coeff':base_compression_exact,
      'authoritative_match_count_945':len(core.MATCH_COEFF)==945,
    }
    valid=all(checks.values())
    if not valid: cls='INVALID_IMPLEMENTATION'
    elif not tcw_exact: cls='SOURCE_TYPE_S5_COVARIANCE_FAIL_EXACT'
    elif not match_exact: cls='ENTRY_COMPRESSION_S5_COVARIANCE_FAIL_EXACT'
    else: cls='ORIENTATION_TRANSPOSE_SOURCE_S5_EXACT'
    out={
      'gate':'K5_EXACT_CANCELLATION_ORIENTATION_TRANSPOSE_SOURCE_S5_DIAGNOSTIC',
      'prereg_commit':PREREG,
      'cycle':list(CYCLE),'inverse_cycle':list(invperm(CYCLE)),
      'orientation_reversals':reversals,'inverse_orientation_reversals':invreversals,
      'tcw_keys':len(base),'matching_keys':len(core.MATCH_COEFF),
      'checks':checks,'tcw_keys_exact':fwd_keys,'tcw_coefficients_exact':tcw_exact,
      'recompressed_matching_keys_exact':match_keys,'recompressed_matching_coefficients_exact':match_exact,
      'tcw_mismatch_sample':sample_diff(base,fwd,'tcw'),
      'matching_mismatch_sample':sample_diff(core.MATCH_COEFF,recomp,'match'),
      'classification':cls,'physical_corner_coefficients_used':False,'scientific_verdict':None,
    }
    p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 2 if cls=='INVALID_IMPLEMENTATION' else 0

if __name__=='__main__': raise SystemExit(main())
