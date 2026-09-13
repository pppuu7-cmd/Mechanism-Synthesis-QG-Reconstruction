#!/usr/bin/env python3
"""Aggregate frozen Iter076D A-D lane artifacts."""
from __future__ import annotations
import argparse, glob, json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-root',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows={}
    for fn in glob.glob(str(Path(a.input_root)/'**'/'*.json'),recursive=True):
        try:
            d=json.loads(Path(fn).read_text())
        except Exception:
            continue
        if d.get('iteration')=='Iter076D' and d.get('lane') in 'ABCD': rows[d['lane']]=d
    complete=set(rows)==set('ABCD')
    valid=complete and all(rows[k].get('valid') is True for k in 'ABCD')
    scope=rows.get('D',{}).get('scope')=='K4_PUSHFORWARD_NOT_ESTABLISHED'
    passed=bool(valid and scope)
    out={'iteration':'Iter076D','lanes_found':sorted(rows),'lane_valid':{k:rows[k].get('valid') for k in sorted(rows)},
         'scope_guard_ok':scope,'valid':passed,
         'classification':('ITER076D_SOURCE_DOMAIN_HAAR_AND_RELATIVE_GROUP_QUADRATIC_JETS_EXACT_SCOPED' if passed else 'ITER076D_SOURCE_DOMAIN_LOCAL_GEOMETRY_REVIEW'),
         'claim_lock':'No source-to-K4 pushforward; no epsilon^-1 coefficient; no physical vertex finiteness/divergence theorem; no G3/F9/G8/K5 promotion.'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(9)
if __name__=='__main__': main()
