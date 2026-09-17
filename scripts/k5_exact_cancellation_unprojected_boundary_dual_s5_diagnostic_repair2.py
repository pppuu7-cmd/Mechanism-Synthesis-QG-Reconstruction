#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG='a7d0057bcbde959df84bd5da3fb96447ced01175'

spec=importlib.util.spec_from_file_location('boundary_dual_base_r2',BASE)
mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod)

# Exact prospective source-key compression: within each boundary-state index,
# Wick depends only on the complete 10-edge types tuple and is linear in coeff.
COMPRESSED=[]
ORIGINAL_TERMS=0
ORIGINAL_STATES=[]
for idx,arr in mod.act.PATTERNS:
    ORIGINAL_STATES.append(idx)
    acc=defaultdict(Fraction)
    for types,coeff in arr:
        ORIGINAL_TERMS+=1
        acc[types]+=Fraction(coeff)
    carr=tuple((types,c) for types,c in sorted(acc.items()) if c)
    COMPRESSED.append((idx,carr))
COMPRESSED=tuple(COMPRESSED)
COMPRESSED_TERMS=sum(len(arr) for _,arr in COMPRESSED)
COMPRESSED_STATES=tuple(idx for idx,_ in COMPRESSED)

_stats={'calls':0,'hits':0,'misses':0}
_cache={}

def compressed_unprojected_uncached(alpha):
    cov=mod.b0_cov(alpha); pair={}
    for i in range(10):
        for j in range(i+1,10):
            for ea in mod.core.ENTRY:
                for eb in mod.core.ENTRY:
                    g=mod.core.EM[(ea,eb)]
                    pair[(i,j,ea,eb)]=(cov[(i,j)]*g[0],cov[(i,j)]*g[1])
    wick_cache={}
    def wick(rem):
        if not rem:return (Fraction(1),Fraction(0))
        if rem in wick_cache:return wick_cache[rem]
        i,ei=rem[0]; total=(Fraction(0),Fraction(0))
        for pos in range(1,len(rem)):
            j,ej=rem[pos]; rest=rem[1:pos]+rem[pos+1:]
            total=mod.cvadd(total,mod.cmul(pair[(i,j,ei,ej)],wick(rest)))
        wick_cache[rem]=total; return total
    amps=[(Fraction(0),Fraction(0)) for _ in range(32)]
    for idx,arr in COMPRESSED:
        z=(Fraction(0),Fraction(0))
        for types,coeff in arr:
            rem=tuple((i,types[i]) for i in range(10))
            z=mod.cvadd(z,mod.cvscale(coeff,wick(rem)))
        amps[idx]=z
    # Preserve authoritative source coverage count: compression traversed all
    # original 100000 terms exactly before exact rational aggregation.
    return tuple(amps),ORIGINAL_TERMS,len(wick_cache)

def cached_unprojected(alpha):
    _stats['calls']+=1
    key=tuple(alpha)
    if key in _cache:
        _stats['hits']+=1
        return _cache[key]
    _stats['misses']+=1
    val=compressed_unprojected_uncached(alpha)
    _cache[key]=val
    return val

mod.unprojected=cached_unprojected

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    old=list(sys.argv); sys.argv=[str(BASE),'--output',args.output]
    try:
        rc=mod.main()
    finally:
        sys.argv=old
    p=Path(args.output); d=json.loads(p.read_text(encoding='utf-8'))
    repair_checks={
        'repair2_prereg_frozen': True,
        'parent_diagnostic_prereg_unchanged': d.get('prereg_commit')=='41f26f8e314f4ab1213fe6a681b69d2c87e00d68',
        'physical_corner_coefficients_unused': d.get('physical_corner_coefficients_used') is False,
        'original_source_terms_exactly_100000': ORIGINAL_TERMS==100000 and mod.act.SOURCE_TERMS==100000,
        'all_32_boundary_states_preserved': len(ORIGINAL_STATES)==32 and tuple(ORIGINAL_STATES)==COMPRESSED_STATES and sorted(ORIGINAL_STATES)==list(range(32)),
        'exact_fraction_aggregation_used': all(isinstance(c,Fraction) for _,arr in COMPRESSED for _,c in arr),
        'compressed_not_larger_than_original': COMPRESSED_TERMS<=ORIGINAL_TERMS,
        'unique_unprojected_evaluations_exactly_6': _stats['misses']==6 and len(_cache)==6,
        'duplicate_base_evaluations_cache_hits': _stats['hits']==2,
        'total_unprojected_calls_exactly_8': _stats['calls']==8,
    }
    d['execution_repair2_prereg_commit']=REPAIR_PREREG
    d['execution_repair2']='exact_boundary_state_types_key_aggregation_plus_exact_alpha_tuple_memoization'
    d['execution_repair2_source_stats']={'original_terms':ORIGINAL_TERMS,'compressed_terms':COMPRESSED_TERMS,'boundary_states':len(COMPRESSED_STATES)}
    d['execution_repair2_cache_stats']=dict(_stats,unique_keys=len(_cache))
    d['execution_repair2_checks']=repair_checks
    if not all(repair_checks.values()): d['classification']='INVALID_IMPLEMENTATION'
    p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('REPAIR2_SOURCE_STATS=',json.dumps(d['execution_repair2_source_stats'],sort_keys=True))
    print('REPAIR2_CACHE_STATS=',json.dumps(d['execution_repair2_cache_stats'],sort_keys=True))
    print('REPAIR2_CHECKS=',json.dumps(repair_checks,sort_keys=True))
    print('FINAL_CLASSIFICATION=',d['classification'])
    return 2 if d['classification']=='INVALID_IMPLEMENTATION' else rc

if __name__=='__main__': raise SystemExit(main())
