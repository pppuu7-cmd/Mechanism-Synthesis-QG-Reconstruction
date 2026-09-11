#!/usr/bin/env python3
"""Demonstrate the hierarchy between causal-sector preservation and single-pole closure.

A coarse/refinement map can preserve the +/- Toller sector while mapping one basis mode to a
superposition of several same-sector pole modes. Such a map passes CCI but not the much stronger
'single label maps to single label' property. This prevents MSQGR from incorrectly equating CCI
with closure of one gamma-simple pole label.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def norm2(v): return math.sqrt(sum(abs(x)**2 for x in v))
def project(v,signs,target): return [x if s==target else 0j for x,s in zip(v,signs)]
def leakage(v,signs,target): return norm2(project(v,signs,-target))/(norm2(v)+1e-30)
def support(v,tol=1e-12): return sum(abs(x)>tol for x in v)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='results/toller_embedding_taxonomy.json');args=ap.parse_args()
    signs=[+1,+1,+1,-1,-1,-1]
    maps={
      'single_same_sector':[1+0j,0j,0j,0j,0j,0j],
      'superposition_same_sector':[0.7+0j,0.5j,0.3+0j,0j,0j,0j],
      'small_cross_sector':[0.7+0j,0.5j,0j,1e-3+0j,0j,0j],
      'balanced_cross_sector':[0.7+0j,0.2+0j,0j,0.7j,0j,0j]
    }
    rows=[]
    for name,v in maps.items():
        leak=leakage(v,signs,+1);supp=support(v)
        rows.append({'map':name,'support_size':supp,'cci_pass':leak<1e-12,'single_label_closure':supp==1,'relative_cross_sector_leakage':leak})
    out={'rows':rows,'verdict':'CCI_STRICTLY_WEAKER_THAN_SINGLE_LABEL_CLOSURE','interpretation':'Same-sector superpositions can satisfy causal cylindrical intertwining even when no single gamma-simple pole label closes. Therefore the exact half-integer obstruction for naive mode multiplication does not by itself violate CCI; it only rules out an over-simple coarse-graining ansatz.','scope':'finite basis taxonomy; physical coefficients/embeddings must be computed from dynamics'}
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
    good={r['map']:r for r in rows}
    if not good['superposition_same_sector']['cci_pass'] or good['superposition_same_sector']['single_label_closure'] or good['small_cross_sector']['cci_pass']: raise SystemExit(1)
if __name__=='__main__':main()
