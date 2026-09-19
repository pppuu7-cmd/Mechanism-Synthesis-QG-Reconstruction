#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'scripts/k5_34_orbit_exact_leading_coefficient_core_repair3_matching_key_frame.py'
PREREG_COMMIT='a42ae5afb4742211f96b7cca41efce274bb398e6'
CORE_COMMIT='ae1e2cf51d7da51ccbcbdbc289d0dc5326802a7c'

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    m=load(CORE,'r3_static_diag'); checks=m.static_checks(); false=[k for k,v in checks.items() if not bool(v)]
    out={'gate':'K5_34_ORBIT_MATCHING_KEY_FRAME_REPAIR3_STATIC_VALIDITY_DIAGNOSTIC','prereg_commit':PREREG_COMMIT,'core_commit':CORE_COMMIT,'checks':checks,'false_keys':false,'q18_values_used':False,'N_B_orders_or_coefficients_used':False,'heavy_resolver_launched':False,'scientific_verdict':None}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('FALSE_KEYS='+json.dumps(false));print('CHECKS='+json.dumps(checks,sort_keys=True));return 0
if __name__=='__main__': raise SystemExit(main())
