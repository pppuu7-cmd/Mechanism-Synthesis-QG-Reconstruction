#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/k5_exact_cancellation_unprojected_boundary_dual_s5_diagnostic.py'
REPAIR_PREREG='fa0eb9027a7df8138a6cef734ef75fbf43200815'

spec=importlib.util.spec_from_file_location('boundary_dual_base',BASE)
mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod)

_orig_unprojected=mod.unprojected
_cache={}
_stats={'calls':0,'hits':0,'misses':0}

def cached_unprojected(alpha):
    _stats['calls']+=1
    key=tuple(alpha)
    if key in _cache:
        _stats['hits']+=1
        return _cache[key]
    _stats['misses']+=1
    val=_orig_unprojected(alpha)
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
    p=Path(args.output)
    d=json.loads(p.read_text(encoding='utf-8'))
    repair_checks={
        'repair1_prereg_frozen': True,
        'parent_diagnostic_prereg_unchanged': d.get('prereg_commit')=='41f26f8e314f4ab1213fe6a681b69d2c87e00d68',
        'physical_corner_coefficients_unused': d.get('physical_corner_coefficients_used') is False,
        'unique_unprojected_evaluations_exactly_6': _stats['misses']==6 and len(_cache)==6,
        'duplicate_base_evaluations_cache_hits': _stats['hits']==2,
        'total_unprojected_calls_exactly_8': _stats['calls']==8,
    }
    d['execution_repair1_prereg_commit']=REPAIR_PREREG
    d['execution_repair1']='exact_alpha_tuple_memoization_only'
    d['execution_repair1_cache_stats']=dict(_stats,unique_keys=len(_cache))
    d['execution_repair1_checks']=repair_checks
    if not all(repair_checks.values()):
        d['classification']='INVALID_IMPLEMENTATION'
    p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('REPAIR1_CACHE_STATS=',json.dumps(d['execution_repair1_cache_stats'],sort_keys=True))
    print('REPAIR1_CHECKS=',json.dumps(repair_checks,sort_keys=True))
    print('FINAL_CLASSIFICATION=',d['classification'])
    return 2 if d['classification']=='INVALID_IMPLEMENTATION' else rc

if __name__=='__main__': raise SystemExit(main())
